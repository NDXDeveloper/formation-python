# ============================================================================
#   Section 11.5 : Creation et consommation d'APIs REST (version SQLAlchemy)
#   Description : API REST complete pour un blog, adossee a une base de
#                 donnees via SQLAlchemy ORM (utilisateurs, articles,
#                 commentaires) : CRUD, pagination, filtrage, tri, CORS,
#                 erreurs 404/409/422, client de consommation.
#   Fichier source : 05-creation-consommation-apis-rest.md
# ============================================================================

"""API REST complete pour un blog, adossee a SQLAlchemy (version persistante).

Cet exemple reproduit en UN SEUL fichier l'API SQLAlchemy decrite dans le
chapitre. Le cours repartit ce code en plusieurs modules :

    models.py    -> les modeles Pydantic (validation / serialisation)
    database.py  -> le moteur, la session et les modeles SQLAlchemy (tables)
    main.py      -> l'application FastAPI et les routes

et utilise une base fichier "sqlite:///./blog.db". Ici, on emploie une base
SQLite EN MEMOIRE avec StaticPool : l'unique connexion est partagee entre les
threads de TestClient, l'exemple reste auto-suffisant, testable, et ne laisse
aucun fichier sur le disque.

A comparer avec 05_01_api_rest_complete.py, qui implemente la MEME API mais
EN MEMOIRE (dictionnaires Python, sans base de donnees ni ORM).

Note : les modeles SQLAlchemy (tables) sont ici suffixes "Table"
(UserTable, ArticleTable, CommentaireTable) pour eviter toute collision de
noms avec les modeles Pydantic (Utilisateur, Article, Commentaire) dans ce
fichier unique. Dans le cours, ils vivent dans deux modules separes.
"""

from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import (
    JSON, Column, DateTime, ForeignKey, Integer, String, Text, create_engine
)
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker
from sqlalchemy.pool import StaticPool


# ============================================================================
#   Modeles Pydantic  (models.py dans le cours)
#   Role : valider les requetes et serialiser les reponses.
# ============================================================================

class UtilisateurBase(BaseModel):
    nom: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    bio: str | None = None


class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str = Field(..., min_length=8)


class Utilisateur(UtilisateurBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_inscription: datetime


class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=5, max_length=200)
    contenu: str = Field(..., min_length=10)
    categorie: str
    tags: list[str] = []


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    auteur_id: int
    date_publication: datetime
    nombre_vues: int = 0


class ArticleAvecAuteur(Article):
    auteur: Utilisateur


class CommentaireBase(BaseModel):
    contenu: str = Field(..., min_length=1, max_length=500)


class CommentaireCreate(CommentaireBase):
    pass


class Commentaire(CommentaireBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    article_id: int
    auteur_id: int
    date_creation: datetime


# ============================================================================
#   Base de donnees SQLAlchemy  (database.py dans le cours)
#   Role : le moteur, la session, et les modeles = les TABLES.
# ============================================================================

# Le cours utilise une base fichier : "sqlite:///./blog.db".
# Ici : base en memoire + StaticPool pour partager l'unique connexion entre
# les threads de TestClient et ne rien ecrire sur le disque.
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserTable(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    bio = Column(Text, nullable=True)
    mot_de_passe = Column(String(255), nullable=False)
    date_inscription = Column(DateTime, nullable=False)


class ArticleTable(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    titre = Column(String(200), nullable=False)
    contenu = Column(Text, nullable=False)
    categorie = Column(String(100), nullable=False)
    tags = Column(JSON, default=list)  # liste de chaines stockee en JSON
    auteur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    date_publication = Column(DateTime, nullable=False)
    nombre_vues = Column(Integer, default=0)

    auteur = relationship("UserTable")


class CommentaireTable(Base):
    __tablename__ = "commentaires"
    id = Column(Integer, primary_key=True)
    contenu = Column(String(500), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    auteur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    date_creation = Column(DateTime, nullable=False)


def get_db():
    """Dependance FastAPI : fournit une session, fermee en fin de requete."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================================
#   Application FastAPI  (main.py dans le cours)
# ============================================================================

app = FastAPI(
    title="Blog API",
    description="Une API REST complete pour gerer un blog (SQLAlchemy)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creer les tables
Base.metadata.create_all(bind=engine)


# ==================== UTILISATEURS ====================

@app.post("/api/utilisateurs", response_model=Utilisateur,
          status_code=status.HTTP_201_CREATED, tags=["Utilisateurs"])
def creer_utilisateur(utilisateur: UtilisateurCreate,
                      db: Session = Depends(get_db)):
    """Creer un nouvel utilisateur (email unique)."""
    db_user = db.query(UserTable).filter(
        UserTable.email == utilisateur.email
    ).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cet email est deja utilise"
        )

    db_utilisateur = UserTable(
        nom=utilisateur.nom,
        email=utilisateur.email,
        bio=utilisateur.bio,
        mot_de_passe=utilisateur.mot_de_passe,  # A hasher en production !
        date_inscription=datetime.now(),
    )
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


@app.get("/api/utilisateurs", response_model=list[Utilisateur],
         tags=["Utilisateurs"])
def lire_utilisateurs(skip: int = Query(0, ge=0),
                      limit: int = Query(10, ge=1, le=100),
                      db: Session = Depends(get_db)):
    """Lister les utilisateurs avec pagination."""
    return db.query(UserTable).offset(skip).limit(limit).all()


@app.get("/api/utilisateurs/{utilisateur_id}", response_model=Utilisateur,
         tags=["Utilisateurs"])
def lire_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    """Recuperer un utilisateur par son ID."""
    utilisateur = db.query(UserTable).filter(
        UserTable.id == utilisateur_id
    ).first()
    if not utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouve"
        )
    return utilisateur


@app.put("/api/utilisateurs/{utilisateur_id}", response_model=Utilisateur,
         tags=["Utilisateurs"])
def modifier_utilisateur(utilisateur_id: int, utilisateur: UtilisateurCreate,
                         db: Session = Depends(get_db)):
    """Mettre a jour un utilisateur."""
    db_utilisateur = db.query(UserTable).filter(
        UserTable.id == utilisateur_id
    ).first()
    if not db_utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouve"
        )
    db_utilisateur.nom = utilisateur.nom
    db_utilisateur.email = utilisateur.email
    db_utilisateur.bio = utilisateur.bio
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


@app.delete("/api/utilisateurs/{utilisateur_id}",
            status_code=status.HTTP_204_NO_CONTENT, tags=["Utilisateurs"])
def supprimer_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    """Supprimer un utilisateur."""
    db_utilisateur = db.query(UserTable).filter(
        UserTable.id == utilisateur_id
    ).first()
    if not db_utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouve"
        )
    db.delete(db_utilisateur)
    db.commit()
    return None


# ==================== ARTICLES ====================

@app.post("/api/articles", response_model=Article,
          status_code=status.HTTP_201_CREATED, tags=["Articles"])
def creer_article(article: ArticleCreate, auteur_id: int,
                  db: Session = Depends(get_db)):
    """Creer un article (l'auteur doit exister)."""
    auteur = db.query(UserTable).filter(UserTable.id == auteur_id).first()
    if not auteur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Auteur non trouve"
        )
    db_article = ArticleTable(
        titre=article.titre,
        contenu=article.contenu,
        categorie=article.categorie,
        tags=article.tags,
        auteur_id=auteur_id,
        date_publication=datetime.now(),
        nombre_vues=0,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


@app.get("/api/articles", response_model=list[Article], tags=["Articles"])
def lire_articles(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    categorie: str | None = None,
    auteur_id: int | None = None,
    sort: str = Query("date_publication",
                      pattern="^(date_publication|nombre_vues|titre)$"),
    order: str = Query("desc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db),
):
    """Lister les articles avec filtrage, tri et pagination."""
    query = db.query(ArticleTable)

    if categorie:
        query = query.filter(ArticleTable.categorie == categorie)
    if auteur_id:
        query = query.filter(ArticleTable.auteur_id == auteur_id)

    if order == "desc":
        query = query.order_by(getattr(ArticleTable, sort).desc())
    else:
        query = query.order_by(getattr(ArticleTable, sort).asc())

    return query.offset(skip).limit(limit).all()


@app.get("/api/articles/{article_id}", response_model=ArticleAvecAuteur,
         tags=["Articles"])
def lire_article(article_id: int, db: Session = Depends(get_db)):
    """Recuperer un article avec son auteur (incremente les vues)."""
    article = db.query(ArticleTable).filter(
        ArticleTable.id == article_id
    ).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouve"
        )
    article.nombre_vues += 1
    db.commit()
    return article


@app.patch("/api/articles/{article_id}", response_model=Article,
           tags=["Articles"])
def modifier_article_partiel(article_id: int,
                             titre: str | None = None,
                             contenu: str | None = None,
                             categorie: str | None = None,
                             db: Session = Depends(get_db)):
    """Modifier partiellement un article (seuls les champs fournis)."""
    db_article = db.query(ArticleTable).filter(
        ArticleTable.id == article_id
    ).first()
    if not db_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouve"
        )
    if titre is not None:
        db_article.titre = titre
    if contenu is not None:
        db_article.contenu = contenu
    if categorie is not None:
        db_article.categorie = categorie
    db.commit()
    db.refresh(db_article)
    return db_article


@app.delete("/api/articles/{article_id}",
            status_code=status.HTTP_204_NO_CONTENT, tags=["Articles"])
def supprimer_article(article_id: int, db: Session = Depends(get_db)):
    """Supprimer un article."""
    db_article = db.query(ArticleTable).filter(
        ArticleTable.id == article_id
    ).first()
    if not db_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouve"
        )
    db.delete(db_article)
    db.commit()
    return None


# ==================== COMMENTAIRES ====================

@app.post("/api/articles/{article_id}/commentaires",
          response_model=Commentaire,
          status_code=status.HTTP_201_CREATED, tags=["Commentaires"])
def creer_commentaire(article_id: int, commentaire: CommentaireCreate,
                      auteur_id: int, db: Session = Depends(get_db)):
    """Ajouter un commentaire a un article."""
    article = db.query(ArticleTable).filter(
        ArticleTable.id == article_id
    ).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouve"
        )
    db_commentaire = CommentaireTable(
        contenu=commentaire.contenu,
        article_id=article_id,
        auteur_id=auteur_id,
        date_creation=datetime.now(),
    )
    db.add(db_commentaire)
    db.commit()
    db.refresh(db_commentaire)
    return db_commentaire


@app.get("/api/articles/{article_id}/commentaires",
         response_model=list[Commentaire], tags=["Commentaires"])
def lire_commentaires_article(article_id: int, db: Session = Depends(get_db)):
    """Recuperer tous les commentaires d'un article."""
    article = db.query(ArticleTable).filter(
        ArticleTable.id == article_id
    ).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouve"
        )
    return db.query(CommentaireTable).filter(
        CommentaireTable.article_id == article_id
    ).all()


@app.delete("/api/commentaires/{commentaire_id}",
            status_code=status.HTTP_204_NO_CONTENT, tags=["Commentaires"])
def supprimer_commentaire(commentaire_id: int, db: Session = Depends(get_db)):
    """Supprimer un commentaire."""
    db_commentaire = db.query(CommentaireTable).filter(
        CommentaireTable.id == commentaire_id
    ).first()
    if not db_commentaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Commentaire non trouve"
        )
    db.delete(db_commentaire)
    db.commit()
    return None


# ==================== STATISTIQUES / RACINE ====================

@app.get("/api/stats", tags=["Statistiques"])
def obtenir_statistiques(db: Session = Depends(get_db)):
    """Statistiques globales du blog."""
    return {
        "nombre_utilisateurs": db.query(UserTable).count(),
        "nombre_articles": db.query(ArticleTable).count(),
        "nombre_commentaires": db.query(CommentaireTable).count(),
        "article_plus_vu": db.query(ArticleTable).order_by(
            ArticleTable.nombre_vues.desc()
        ).first(),
    }


@app.get("/", tags=["Root"])
def root():
    """Endpoint racine de l'API."""
    return {
        "message": "Bienvenue sur l'API Blog",
        "version": "1.0.0",
        "documentation": "/docs",
    }


# ============================================================================
#   Client de consommation  (BlogAPIClient dans le cours)
#   Le cours s'appuie sur `requests` contre un serveur en cours d'execution ;
#   ici on enveloppe un TestClient pour rester auto-suffisant et testable.
# ============================================================================

class BlogAPIClient:
    """Petit client pour consommer l'API Blog."""

    def __init__(self, client):
        self.client = client

    def creer_utilisateur(self, nom, email, mot_de_passe, bio=None):
        r = self.client.post("/api/utilisateurs", json={
            "nom": nom, "email": email,
            "mot_de_passe": mot_de_passe, "bio": bio,
        })
        r.raise_for_status()
        return r.json()

    def creer_article(self, titre, contenu, categorie, auteur_id, tags=None):
        r = self.client.post("/api/articles", params={"auteur_id": auteur_id},
                             json={"titre": titre, "contenu": contenu,
                                   "categorie": categorie, "tags": tags or []})
        r.raise_for_status()
        return r.json()

    def obtenir_article(self, article_id):
        r = self.client.get(f"/api/articles/{article_id}")
        r.raise_for_status()
        return r.json()

    def obtenir_articles(self, **params):
        r = self.client.get("/api/articles", params=params)
        r.raise_for_status()
        return r.json()

    def creer_commentaire(self, article_id, contenu, auteur_id):
        r = self.client.post(f"/api/articles/{article_id}/commentaires",
                             params={"auteur_id": auteur_id},
                             json={"contenu": contenu})
        r.raise_for_status()
        return r.json()

    def obtenir_statistiques(self):
        r = self.client.get("/api/stats")
        r.raise_for_status()
        return r.json()


# ============================================================================
#   Demonstration via TestClient (aucun serveur a lancer)
# ============================================================================

if __name__ == "__main__":
    test_client = TestClient(app)
    api = BlogAPIClient(test_client)

    print("=== Endpoint racine ===")
    print(f"  {test_client.get('/').json()}")

    print("\n=== Creer des utilisateurs ===")
    u1 = api.creer_utilisateur("Alice Dupont", "alice@example.com",
                               "motdepasse1", "Developpeuse Python")
    print(f"  Cree: {u1['nom']} (id={u1['id']})")
    u2 = api.creer_utilisateur("Bob Martin", "bob@example.com", "motdepasse2")
    print(f"  Cree: {u2['nom']} (id={u2['id']})")

    print("\n=== Email en double (409 Conflict) ===")
    r = test_client.post("/api/utilisateurs", json={
        "nom": "Alice Clone", "email": "alice@example.com",
        "mot_de_passe": "12345678",
    })
    print(f"  {r.status_code}: {r.json()['detail']}")

    print("\n=== Creer des articles ===")
    a1 = api.creer_article("Introduction a REST",
                           "REST est un style d'architecture pour les APIs web...",
                           "Tech", u1["id"], ["REST", "API", "Python"])
    print(f"  Cree: '{a1['titre']}' (auteur {a1['auteur_id']})")
    a2 = api.creer_article("Guide Python avance",
                           "Les decorateurs et metaclasses en Python...",
                           "Tech", u1["id"], ["Python", "avance"])
    print(f"  Cree: '{a2['titre']}' (auteur {a2['auteur_id']})")
    a3 = api.creer_article("Decouverte de la science",
                           "Les dernieres avancees scientifiques nous montrent...",
                           "Science", u2["id"], ["Science"])
    print(f"  Cree: '{a3['titre']}' (auteur {a3['auteur_id']})")

    print("\n=== Lire un article avec auteur (incremente les vues) ===")
    art = api.obtenir_article(a1["id"])
    print(f"  '{art['titre']}' par {art['auteur']['nom']} - vues={art['nombre_vues']}")
    art = api.obtenir_article(a1["id"])
    print(f"  2eme lecture - vues={art['nombre_vues']}")

    print("\n=== Filtrer par categorie / trier par vues ===")
    tech = api.obtenir_articles(categorie="Tech")
    print(f"  Tech: {len(tech)} articles")
    par_vues = api.obtenir_articles(sort="nombre_vues", order="desc")
    print(f"  Plus vu en premier: '{par_vues[0]['titre']}' ({par_vues[0]['nombre_vues']} vues)")

    print("\n=== Modification partielle (PATCH) ===")
    r = test_client.patch(f"/api/articles/{a2['id']}",
                          params={"titre": "Guide Python (mis a jour)"})
    print(f"  {r.status_code}: nouveau titre = '{r.json()['titre']}'")

    print("\n=== Commentaires ===")
    api.creer_commentaire(a1["id"], "Excellent article sur REST !", u2["id"])
    api.creer_commentaire(a1["id"], "Merci pour le partage", u1["id"])
    coms = test_client.get(f"/api/articles/{a1['id']}/commentaires").json()
    print(f"  Commentaires de l'article {a1['id']}: {len(coms)}")

    print("\n=== Article inexistant (404) ===")
    r = test_client.get("/api/articles/999")
    print(f"  {r.status_code}: {r.json()['detail']}")

    print("\n=== Validation : titre trop court (422) ===")
    r = test_client.post("/api/articles", params={"auteur_id": u1["id"]}, json={
        "titre": "ABC", "contenu": "Contenu valide suffisamment long",
        "categorie": "Tech",
    })
    print(f"  {r.status_code}: validation erreur (titre trop court)")

    print("\n=== Statistiques ===")
    stats = api.obtenir_statistiques()
    print(f"  Utilisateurs: {stats['nombre_utilisateurs']}")
    print(f"  Articles: {stats['nombre_articles']}")
    print(f"  Commentaires: {stats['nombre_commentaires']}")
    plus_vu = stats["article_plus_vu"]
    print(f"  Article le plus vu: '{plus_vu['titre']}' ({plus_vu['nombre_vues']} vues)")

    print("\n=== Suppressions ===")
    r = test_client.delete(f"/api/articles/{a3['id']}")
    print(f"  DELETE article {a3['id']}: {r.status_code}")
    r = test_client.delete(f"/api/utilisateurs/{u2['id']}")
    print(f"  DELETE utilisateur {u2['id']}: {r.status_code}")
    stats = api.obtenir_statistiques()
    print(f"  Articles restants: {stats['nombre_articles']}, "
          f"utilisateurs restants: {stats['nombre_utilisateurs']}")
