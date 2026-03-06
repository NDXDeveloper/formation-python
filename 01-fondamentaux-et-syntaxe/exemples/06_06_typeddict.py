# ============================================================================
#   Section 6.8 : TypedDict (Dictionnaires typés)
#   Description : Définir des dictionnaires avec structure fixe et typée,
#                 champs optionnels avec total=False
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import TypedDict

# Définir la structure d'un dictionnaire
class Personne(TypedDict):
    nom: str
    age: int
    ville: str

def creer_personne(nom: str, age: int, ville: str) -> Personne:
    return {"nom": nom, "age": age, "ville": ville}

def afficher_personne(personne: Personne) -> None:
    print(f"{personne['nom']}, {personne['age']} ans, {personne['ville']}")

alice: Personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

afficher_personne(alice)
afficher_personne(creer_personne("Bob", 30, "Lyon"))

# --- TypedDict avec champs optionnels ---
class Utilisateur(TypedDict, total=False):
    nom: str
    age: int
    email: str | None
    telephone: str | None

user: Utilisateur = {"nom": "Charlie", "age": 28}
print(f"Utilisateur : {user}")
