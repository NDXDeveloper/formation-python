# ============================================================================
#   Section 11.2.1 : Installation et premier projet FastAPI
#   Description : Premiere application FastAPI - routes GET/POST/PUT/DELETE,
#                 parametres de chemin, validation de type, configuration
#   Fichier source : 02.1-installation-premier-projet-fastapi.md
# ============================================================================

"""Premier projet FastAPI avec routes et parametres."""

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

# Creer l'application avec des metadonnees
app = FastAPI(
    title="Mon API FastAPI",
    description="Une API de demonstration",
    version="1.0.0"
)


# --- Modele Pydantic ---
class Article(BaseModel):
    titre: str
    contenu: str


# --- Routes GET ---

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API FastAPI !"}


@app.get("/bonjour")
def dire_bonjour():
    return {"message": "Bonjour ! Comment allez-vous ?"}


@app.get("/info")
def obtenir_info():
    return {
        "nom_application": "Mon API",
        "version": "1.0.0",
        "framework": "FastAPI"
    }


@app.get("/utilisateur/{nom}")
def lire_utilisateur(nom: str):
    return {"message": f"Bonjour {nom} !"}


@app.get("/age/{age}")
def verifier_age(age: int):
    if age >= 18:
        return {"message": f"Vous avez {age} ans, vous etes majeur."}
    else:
        return {"message": f"Vous avez {age} ans, vous etes mineur."}


@app.get("/articles")
def lire_articles():
    return {"articles": ["Article 1", "Article 2"]}


# --- Routes POST/PUT/DELETE ---

@app.post("/articles")
def creer_article(article: Article):
    return {"message": "Article cree", "article": article.model_dump()}


@app.put("/articles/{id}")
def modifier_article(id: int, article: Article):
    return {"message": f"Article {id} modifie"}


@app.delete("/articles/{id}")
def supprimer_article(id: int):
    return {"message": f"Article {id} supprime"}


# --- Tests avec TestClient ---
if __name__ == "__main__":
    client = TestClient(app)

    print("=== GET / ===")
    response = client.get("/")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /bonjour ===")
    response = client.get("/bonjour")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /info ===")
    response = client.get("/info")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /utilisateur/Alice ===")
    response = client.get("/utilisateur/Alice")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /age/25 (majeur) ===")
    response = client.get("/age/25")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /age/15 (mineur) ===")
    response = client.get("/age/15")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== GET /age/abc (validation erreur) ===")
    response = client.get("/age/abc")
    print(f"  Status: {response.status_code}")
    print(f"  Erreur validation: type={response.json()['detail'][0]['type']}")

    print("\n=== GET /articles ===")
    response = client.get("/articles")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== POST /articles ===")
    response = client.post("/articles", json={"titre": "Mon article", "contenu": "Contenu"})
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== PUT /articles/1 ===")
    response = client.put("/articles/1", json={"titre": "Modifie", "contenu": "Nouveau"})
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== DELETE /articles/1 ===")
    response = client.delete("/articles/1")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")

    print("\n=== Configuration de l'app ===")
    print(f"  Titre: {app.title}")
    print(f"  Description: {app.description}")
    print(f"  Version: {app.version}")
