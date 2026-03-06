# ============================================================================
#   Section 11.5 : Creation et consommation d'APIs REST
#   Description : API REST complete pour un blog - CRUD utilisateurs,
#                 articles, commentaires, pagination, filtrage, CORS,
#                 erreurs personnalisees, client API
#   Fichier source : 05-creation-consommation-apis-rest.md
# ============================================================================

"""API REST complete pour un blog avec client de consommation."""

from fastapi import FastAPI, HTTPException, Query, Path, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from fastapi.testclient import TestClient
from datetime import datetime


# === Modeles Pydantic ===

class UtilisateurCreate(BaseModel):
    nom: str = Field(..., min_length=2, max_length=100)
    email: str
    bio: str | None = None
    mot_de_passe: str = Field(..., min_length=8)


class Utilisateur(BaseModel):
    id: int
    nom: str
    email: str
    bio: str | None = None
    date_inscription: datetime


class ArticleCreate(BaseModel):
    titre: str = Field(..., min_length=5, max_length=200)
    contenu: str = Field(..., min_length=10)
    categorie: str
    tags: list[str] = []

    @field_validator('titre')
    @classmethod
    def titre_pas_vide(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Le titre ne peut pas etre vide")
        return v


class Article(BaseModel):
    id: int
    titre: str
    contenu: str
    categorie: str
    tags: list[str]
    auteur_id: int
    date_publication: datetime
    nombre_vues: int = 0


class CommentaireCreate(BaseModel):
    contenu: str = Field(..., min_length=1, max_length=500)


class Commentaire(BaseModel):
    id: int
    contenu: str
    article_id: int
    auteur_id: int
    date_creation: datetime


# === Application FastAPI ===

app = FastAPI(
    title="Blog API",
    description="Une API REST complete pour gerer un blog",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de donnees en memoire
users_db: dict[int, dict] = {}
articles_db: dict[int, dict] = {}
comments_db: dict[int, dict] = {}
next_user_id = 1
next_article_id = 1
next_comment_id = 1


# === Erreurs personnalisees ===

class ResourceNotFound(HTTPException):
    def __init__(self, resource: str, id: int):
        super().__init__(
            status_code=404,
            detail=f"{resource} avec l'ID {id} n'a pas ete trouve"
        )


# === Routes Utilisateurs ===

@app.post("/api/utilisateurs", response_model=Utilisateur,
          status_code=status.HTTP_201_CREATED, tags=["Utilisateurs"])
def creer_utilisateur(utilisateur: UtilisateurCreate):
    global next_user_id
    # Verifier email unique
    for u in users_db.values():
        if u["email"] == utilisateur.email:
            raise HTTPException(status_code=409, detail="Email deja utilise")
    user = {
        "id": next_user_id,
        "nom": utilisateur.nom,
        "email": utilisateur.email,
        "bio": utilisateur.bio,
        "date_inscription": datetime.now()
    }
    users_db[next_user_id] = user
    next_user_id += 1
    return user


@app.get("/api/utilisateurs", response_model=list[Utilisateur],
         tags=["Utilisateurs"])
def lire_utilisateurs(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    users = list(users_db.values())
    return users[skip:skip + limit]


@app.get("/api/utilisateurs/{user_id}", response_model=Utilisateur,
         tags=["Utilisateurs"])
def lire_utilisateur(user_id: int):
    if user_id not in users_db:
        raise ResourceNotFound("Utilisateur", user_id)
    return users_db[user_id]


@app.delete("/api/utilisateurs/{user_id}",
            status_code=status.HTTP_204_NO_CONTENT, tags=["Utilisateurs"])
def supprimer_utilisateur(user_id: int):
    if user_id not in users_db:
        raise ResourceNotFound("Utilisateur", user_id)
    del users_db[user_id]
    return None


# === Routes Articles ===

@app.post("/api/articles", response_model=Article,
          status_code=status.HTTP_201_CREATED, tags=["Articles"])
def creer_article(article: ArticleCreate, auteur_id: int = Query(...)):
    global next_article_id
    if auteur_id not in users_db:
        raise ResourceNotFound("Auteur", auteur_id)
    art = {
        "id": next_article_id,
        "titre": article.titre,
        "contenu": article.contenu,
        "categorie": article.categorie,
        "tags": article.tags,
        "auteur_id": auteur_id,
        "date_publication": datetime.now(),
        "nombre_vues": 0
    }
    articles_db[next_article_id] = art
    next_article_id += 1
    return art


@app.get("/api/articles", response_model=list[Article], tags=["Articles"])
def lire_articles(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    categorie: str | None = None,
    auteur_id: int | None = None
):
    articles = list(articles_db.values())
    if categorie:
        articles = [a for a in articles if a["categorie"] == categorie]
    if auteur_id:
        articles = [a for a in articles if a["auteur_id"] == auteur_id]
    return articles[skip:skip + limit]


@app.get("/api/articles/{article_id}", response_model=Article,
         tags=["Articles"])
def lire_article(article_id: int):
    if article_id not in articles_db:
        raise ResourceNotFound("Article", article_id)
    articles_db[article_id]["nombre_vues"] += 1
    return articles_db[article_id]


@app.delete("/api/articles/{article_id}",
            status_code=status.HTTP_204_NO_CONTENT, tags=["Articles"])
def supprimer_article(article_id: int):
    if article_id not in articles_db:
        raise ResourceNotFound("Article", article_id)
    del articles_db[article_id]
    return None


# === Routes Commentaires ===

@app.post("/api/articles/{article_id}/commentaires",
          response_model=Commentaire,
          status_code=status.HTTP_201_CREATED, tags=["Commentaires"])
def creer_commentaire(
    article_id: int,
    commentaire: CommentaireCreate,
    auteur_id: int = Query(...)
):
    global next_comment_id
    if article_id not in articles_db:
        raise ResourceNotFound("Article", article_id)
    comment = {
        "id": next_comment_id,
        "contenu": commentaire.contenu,
        "article_id": article_id,
        "auteur_id": auteur_id,
        "date_creation": datetime.now()
    }
    comments_db[next_comment_id] = comment
    next_comment_id += 1
    return comment


@app.get("/api/articles/{article_id}/commentaires",
         response_model=list[Commentaire], tags=["Commentaires"])
def lire_commentaires(article_id: int):
    if article_id not in articles_db:
        raise ResourceNotFound("Article", article_id)
    return [c for c in comments_db.values() if c["article_id"] == article_id]


# === Statistiques ===

@app.get("/api/stats", tags=["Statistiques"])
def obtenir_statistiques():
    return {
        "nombre_utilisateurs": len(users_db),
        "nombre_articles": len(articles_db),
        "nombre_commentaires": len(comments_db)
    }


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Bienvenue sur l'API Blog",
        "version": "1.0.0",
        "documentation": "/docs"
    }


# === Client API ===

class BlogAPIClient:
    """Client pour consommer l'API Blog."""

    def __init__(self, client):
        self.client = client

    def creer_utilisateur(self, nom, email, mot_de_passe, bio=None):
        r = self.client.post("/api/utilisateurs", json={
            "nom": nom, "email": email,
            "mot_de_passe": mot_de_passe, "bio": bio
        })
        r.raise_for_status()
        return r.json()

    def obtenir_utilisateurs(self, skip=0, limit=10):
        r = self.client.get("/api/utilisateurs", params={"skip": skip, "limit": limit})
        r.raise_for_status()
        return r.json()

    def creer_article(self, titre, contenu, categorie, auteur_id, tags=None):
        r = self.client.post("/api/articles", json={
            "titre": titre, "contenu": contenu,
            "categorie": categorie, "tags": tags or []
        }, params={"auteur_id": auteur_id})
        r.raise_for_status()
        return r.json()

    def obtenir_articles(self, **kwargs):
        r = self.client.get("/api/articles", params=kwargs)
        r.raise_for_status()
        return r.json()

    def creer_commentaire(self, article_id, contenu, auteur_id):
        r = self.client.post(
            f"/api/articles/{article_id}/commentaires",
            json={"contenu": contenu},
            params={"auteur_id": auteur_id}
        )
        r.raise_for_status()
        return r.json()

    def obtenir_stats(self):
        r = self.client.get("/api/stats")
        r.raise_for_status()
        return r.json()


# === Tests ===
if __name__ == "__main__":
    test_client = TestClient(app)
    api = BlogAPIClient(test_client)

    print("=== Endpoint racine ===")
    r = test_client.get("/")
    print(f"  {r.json()}")

    print("\n=== Creer des utilisateurs ===")
    u1 = api.creer_utilisateur("Alice Dupont", "alice@example.com", "motdepasse1", "Dev Python")
    print(f"  Cree: {u1['nom']} (id={u1['id']})")
    u2 = api.creer_utilisateur("Bob Martin", "bob@example.com", "motdepasse2")
    print(f"  Cree: {u2['nom']} (id={u2['id']})")

    print("\n=== Email en double (409 Conflict) ===")
    r = test_client.post("/api/utilisateurs", json={
        "nom": "Alice Clone", "email": "alice@example.com", "mot_de_passe": "12345678"
    })
    print(f"  {r.status_code}: {r.json()['detail']}")

    print("\n=== Lister les utilisateurs ===")
    users = api.obtenir_utilisateurs()
    for u in users:
        print(f"  id={u['id']}, nom={u['nom']}, bio={u['bio']}")

    print("\n=== Creer des articles ===")
    a1 = api.creer_article(
        "Introduction a REST",
        "REST est un style d'architecture pour les APIs web...",
        "Tech", u1["id"], ["REST", "API", "Python"]
    )
    print(f"  Cree: '{a1['titre']}' par auteur {a1['auteur_id']}")

    a2 = api.creer_article(
        "Guide Python avance",
        "Les decorateurs et metaclasses en Python...",
        "Tech", u1["id"], ["Python", "avance"]
    )
    print(f"  Cree: '{a2['titre']}' par auteur {a2['auteur_id']}")

    a3 = api.creer_article(
        "Decouverte de la science",
        "Les dernieres avancees scientifiques nous montrent...",
        "Science", u2["id"], ["Science"]
    )
    print(f"  Cree: '{a3['titre']}' par auteur {a3['auteur_id']}")

    print("\n=== Lire un article (incremente les vues) ===")
    r = test_client.get(f"/api/articles/{a1['id']}")
    art = r.json()
    print(f"  '{art['titre']}' - vues={art['nombre_vues']}")
    r = test_client.get(f"/api/articles/{a1['id']}")
    art = r.json()
    print(f"  2eme lecture - vues={art['nombre_vues']}")

    print("\n=== Filtrer par categorie ===")
    articles_tech = api.obtenir_articles(categorie="Tech")
    print(f"  Tech: {len(articles_tech)} articles")
    articles_science = api.obtenir_articles(categorie="Science")
    print(f"  Science: {len(articles_science)} articles")

    print("\n=== Filtrer par auteur ===")
    articles_alice = api.obtenir_articles(auteur_id=u1["id"])
    print(f"  Articles d'Alice: {len(articles_alice)}")

    print("\n=== Pagination ===")
    page1 = api.obtenir_articles(skip=0, limit=2)
    print(f"  Page 1 (limit=2): {len(page1)} articles")
    page2 = api.obtenir_articles(skip=2, limit=2)
    print(f"  Page 2 (skip=2, limit=2): {len(page2)} articles")

    print("\n=== Commentaires ===")
    c1 = api.creer_commentaire(a1["id"], "Excellent article sur REST !", u2["id"])
    print(f"  Commentaire cree: '{c1['contenu']}'")
    c2 = api.creer_commentaire(a1["id"], "Merci pour le partage", u1["id"])
    print(f"  Commentaire cree: '{c2['contenu']}'")

    r = test_client.get(f"/api/articles/{a1['id']}/commentaires")
    comments = r.json()
    print(f"  Commentaires de l'article {a1['id']}: {len(comments)}")

    print("\n=== Article inexistant (404) ===")
    r = test_client.get("/api/articles/999")
    print(f"  {r.status_code}: {r.json()['detail']}")

    print("\n=== Validation : titre trop court (422) ===")
    r = test_client.post("/api/articles", json={
        "titre": "ABC", "contenu": "Contenu valide suffisamment long",
        "categorie": "Tech"
    }, params={"auteur_id": 1})
    print(f"  {r.status_code}: validation erreur (titre trop court)")

    print("\n=== Statistiques ===")
    stats = api.obtenir_stats()
    print(f"  Utilisateurs: {stats['nombre_utilisateurs']}")
    print(f"  Articles: {stats['nombre_articles']}")
    print(f"  Commentaires: {stats['nombre_commentaires']}")

    print("\n=== Supprimer un article ===")
    r = test_client.delete(f"/api/articles/{a3['id']}")
    print(f"  DELETE /api/articles/{a3['id']}: {r.status_code}")
    stats = api.obtenir_stats()
    print(f"  Articles restants: {stats['nombre_articles']}")

    print("\n=== Supprimer un utilisateur ===")
    r = test_client.delete(f"/api/utilisateurs/{u2['id']}")
    print(f"  DELETE /api/utilisateurs/{u2['id']}: {r.status_code}")
    stats = api.obtenir_stats()
    print(f"  Utilisateurs restants: {stats['nombre_utilisateurs']}")
