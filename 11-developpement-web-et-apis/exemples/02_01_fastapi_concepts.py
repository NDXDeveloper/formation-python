# ============================================================================
#   Section 11.2 : FastAPI - Framework moderne et asynchrone
#   Description : Concepts cles de FastAPI - Pydantic, type hints,
#                 validation automatique, serialisation JSON
#   Fichier source : 02-fastapi-framework-moderne.md
# ============================================================================

"""Demonstration des concepts cles de FastAPI sans demarrer de serveur."""

from pydantic import BaseModel, ValidationError

# --- Modeles Pydantic (validation automatique) ---
print("=== Modeles Pydantic ===")


class Utilisateur(BaseModel):
    nom: str
    age: int
    email: str


# Creation valide
user = Utilisateur(nom="Alice", age=25, email="alice@example.com")
print(f"  Utilisateur valide : {user}")
print(f"  JSON : {user.model_dump_json()}")

# Validation automatique : conversion de type
user2 = Utilisateur(nom="Bob", age="30", email="bob@test.com")
print(f"  Conversion auto (age='30' -> int) : age={user2.age}, type={type(user2.age).__name__}")

# Validation automatique : erreur
print("\n  Validation avec donnees invalides :")
try:
    Utilisateur(nom="Charlie", age="pas_un_nombre", email="charlie@test.com")
except ValidationError as e:
    print(f"  ValidationError : {e.error_count()} erreur(s)")
    for err in e.errors():
        print(f"    - {err['loc']}: {err['msg']}")


# --- Type hints et parametres ---
print("\n=== Type hints pour parametres ===")


def lire_item(item_id: int, q: str | None = None) -> dict:
    """Simule un endpoint FastAPI avec parametres types."""
    resultat: dict = {"item_id": item_id}
    if q is not None:
        resultat["q"] = q
    return resultat


print(f"  lire_item(42) = {lire_item(42)}")
print(f"  lire_item(42, q='test') = {lire_item(42, q='test')}")


# --- Modeles imbriques ---
print("\n=== Modeles imbriques ===")


class Adresse(BaseModel):
    rue: str
    ville: str
    code_postal: str


class UtilisateurComplet(BaseModel):
    nom: str
    age: int
    email: str
    adresse: Adresse


user3 = UtilisateurComplet(
    nom="Alice",
    age=25,
    email="alice@example.com",
    adresse=Adresse(rue="123 rue Python", ville="Paris", code_postal="75001")
)
print(f"  {user3.nom} habite a {user3.adresse.ville}")
print(f"  Schema JSON : {list(UtilisateurComplet.model_json_schema()['properties'].keys())}")


# --- Serialisation ---
print("\n=== Serialisation ===")

# Vers dictionnaire
user_dict = user.model_dump()
print(f"  model_dump() : {user_dict}")

# Vers JSON
user_json = user.model_dump_json()
print(f"  model_dump_json() : {user_json}")

# Depuis dictionnaire
data = {"nom": "David", "age": 28, "email": "david@test.com"}
user4 = Utilisateur(**data)
print(f"  Depuis dict : {user4}")
