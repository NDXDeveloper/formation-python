# ============================================================================
#   Section 11.2.2 : Routes et validation avec Pydantic
#   Description : Modeles Pydantic, validation automatique, parametres de
#                 chemin/requete/corps, Field, validators, modeles imbriques
#   Fichier source : 02.2-routes-et-validation-pydantic.md
# ============================================================================

"""Routes et validation avec Pydantic - API de gestion d'articles."""

from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field, field_validator
from fastapi.testclient import TestClient
from datetime import datetime


app = FastAPI(
    title="API de Blog",
    description="Une API pour gerer un blog",
    version="1.0.0"
)


# --- Modeles Pydantic ---

class Auteur(BaseModel):
    nom: str = Field(..., min_length=2, max_length=100)
    email: str


class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=5, max_length=200)
    contenu: str = Field(..., min_length=10)
    tags: list[str] = []
    publie: bool = False


class ArticleCreation(ArticleBase):
    auteur: Auteur


class Article(ArticleBase):
    id: int
    auteur: Auteur
    date_creation: datetime
    vues: int = 0


class ModificationUtilisateur(BaseModel):
    nom: str | None = None
    age: int | None = None


# Modele avec validation personnalisee
class Inscription(BaseModel):
    nom: str
    age: int
    mot_de_passe: str

    @field_validator('nom')
    @classmethod
    def nom_doit_contenir_espace(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('Le nom doit contenir un espace (prenom et nom)')
        return v

    @field_validator('mot_de_passe')
    @classmethod
    def mot_de_passe_fort(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Le mot de passe doit contenir au moins 8 caracteres')
        if not any(char.isdigit() for char in v):
            raise ValueError('Le mot de passe doit contenir au moins un chiffre')
        return v


# --- Base de donnees simulee ---
articles_db: list[dict] = []
prochain_id = 1


# --- Routes ---

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur l'API de Blog"}


@app.post("/articles", response_model=Article, status_code=201)
def creer_article(article: ArticleCreation):
    global prochain_id
    nouvel_article = {
        "id": prochain_id,
        "titre": article.titre,
        "contenu": article.contenu,
        "tags": article.tags,
        "publie": article.publie,
        "auteur": article.auteur.model_dump(),
        "date_creation": datetime.now(),
        "vues": 0
    }
    articles_db.append(nouvel_article)
    prochain_id += 1
    return nouvel_article


@app.get("/articles", response_model=list[Article])
def lire_articles(
    publies_seulement: bool = Query(False),
    limite: int = Query(10, ge=1, le=100),
    tag: str | None = Query(None)
):
    resultats = articles_db.copy()
    if publies_seulement:
        resultats = [a for a in resultats if a["publie"]]
    if tag:
        resultats = [a for a in resultats if tag in a["tags"]]
    return resultats[:limite]


@app.get("/articles/{article_id}", response_model=Article)
def lire_article(
    article_id: int = Path(..., ge=1)
):
    for article in articles_db:
        if article["id"] == article_id:
            article["vues"] += 1
            return article
    raise HTTPException(status_code=404, detail="Article non trouve")


@app.delete("/articles/{article_id}")
def supprimer_article(article_id: int):
    for index, article in enumerate(articles_db):
        if article["id"] == article_id:
            articles_db.pop(index)
            return {"message": f"Article {article_id} supprime avec succes"}
    raise HTTPException(status_code=404, detail="Article non trouve")


@app.get("/recherche")
def rechercher(
    q: str = Query(..., min_length=3, max_length=50),
    limite: int = Query(10, ge=1, le=100),
    page: int = Query(1, ge=1)
):
    return {"requete": q, "limite": limite, "page": page}


@app.put("/utilisateurs/{utilisateur_id}")
def modifier_utilisateur(
    utilisateur_id: int,
    notifier: bool = False,
    utilisateur: ModificationUtilisateur = None
):
    return {
        "utilisateur_id": utilisateur_id,
        "modifications": utilisateur.model_dump() if utilisateur else {},
        "notification_envoyee": notifier
    }


# --- Tests ---
if __name__ == "__main__":
    client = TestClient(app)

    # --- Test routes de base ---
    print("=== GET / ===")
    r = client.get("/")
    print(f"  {r.status_code}: {r.json()}")

    # --- Creer des articles ---
    print("\n=== POST /articles (article valide) ===")
    article_data = {
        "titre": "Introduction a FastAPI",
        "contenu": "FastAPI est un framework moderne pour creer des APIs",
        "tags": ["python", "fastapi", "api"],
        "publie": True,
        "auteur": {"nom": "Alice Dupont", "email": "alice@example.com"}
    }
    r = client.post("/articles", json=article_data)
    print(f"  {r.status_code}: id={r.json()['id']}, titre='{r.json()['titre']}'")

    print("\n=== POST /articles (2eme article, non publie) ===")
    article2 = {
        "titre": "Guide Pydantic complet",
        "contenu": "Pydantic permet de valider les donnees automatiquement",
        "tags": ["python", "pydantic"],
        "publie": False,
        "auteur": {"nom": "Bob Martin", "email": "bob@example.com"}
    }
    r = client.post("/articles", json=article2)
    print(f"  {r.status_code}: id={r.json()['id']}, titre='{r.json()['titre']}'")

    # --- Validation : titre trop court ---
    print("\n=== POST /articles (titre trop court -> erreur 422) ===")
    r = client.post("/articles", json={
        "titre": "ABC",
        "contenu": "Contenu suffisamment long pour la validation",
        "auteur": {"nom": "Test User", "email": "test@test.com"}
    })
    print(f"  {r.status_code}: {r.json()['detail'][0]['type']}")

    # --- Lire les articles ---
    print("\n=== GET /articles ===")
    r = client.get("/articles")
    print(f"  {r.status_code}: {len(r.json())} articles")

    print("\n=== GET /articles?publies_seulement=true ===")
    r = client.get("/articles?publies_seulement=true")
    print(f"  {r.status_code}: {len(r.json())} articles publies")

    print("\n=== GET /articles?tag=pydantic ===")
    r = client.get("/articles?tag=pydantic")
    print(f"  {r.status_code}: {len(r.json())} articles avec tag 'pydantic'")

    # --- Lire un article specifique ---
    print("\n=== GET /articles/1 ===")
    r = client.get("/articles/1")
    print(f"  {r.status_code}: titre='{r.json()['titre']}', vues={r.json()['vues']}")

    # --- Article inexistant ---
    print("\n=== GET /articles/999 (404) ===")
    r = client.get("/articles/999")
    print(f"  {r.status_code}: {r.json()['detail']}")

    # --- Recherche avec Query params ---
    print("\n=== GET /recherche?q=python&limite=5&page=2 ===")
    r = client.get("/recherche?q=python&limite=5&page=2")
    print(f"  {r.status_code}: {r.json()}")

    # --- Recherche : q trop court ---
    print("\n=== GET /recherche?q=ab (trop court -> 422) ===")
    r = client.get("/recherche?q=ab")
    print(f"  {r.status_code}: validation erreur")

    # --- Combinaison path + query + body ---
    print("\n=== PUT /utilisateurs/42?notifier=true ===")
    r = client.put("/utilisateurs/42?notifier=true",
                   json={"nom": "Alice Dupont", "age": 26})
    print(f"  {r.status_code}: {r.json()}")

    # --- Supprimer ---
    print("\n=== DELETE /articles/2 ===")
    r = client.delete("/articles/2")
    print(f"  {r.status_code}: {r.json()}")

    # --- Validation personnalisee (Pydantic) ---
    print("\n=== Validation personnalisee (field_validator) ===")
    try:
        Inscription(nom="Alice", age=25, mot_de_passe="abc")
    except Exception as e:
        errors = e.errors()
        for err in errors:
            print(f"  Erreur: {err['loc']} - {err['msg']}")

    try:
        Inscription(nom="Alice Dupont", age=25, mot_de_passe="motdepasse1")
        print("  Inscription valide : Alice Dupont")
    except Exception as e:
        print(f"  Erreur: {e}")

    # --- Modeles imbriques ---
    print("\n=== Modeles imbriques ===")
    auteur = Auteur(nom="Charlie Brown", email="charlie@test.com")
    print(f"  Auteur: {auteur.model_dump()}")
