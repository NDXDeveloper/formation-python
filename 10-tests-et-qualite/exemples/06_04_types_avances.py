# ============================================================================
#   Section 10.6 : Validation de types avec mypy
#   Description : Types avances - Literal, TypedDict, Final, Protocol
#   Fichier source : 06-validation-types-mypy.md
# ============================================================================

from typing import Literal, TypedDict, Final, Protocol

# --- Literal : valeurs specifiques ---
print("=== Literal ===")


def changer_couleur(couleur: Literal["rouge", "vert", "bleu"]) -> None:
    """Change la couleur."""
    print(f"  Couleur changee en {couleur}")


changer_couleur("rouge")
changer_couleur("vert")
changer_couleur("bleu")


# --- TypedDict : dictionnaires avec structure ---
print("\n=== TypedDict ===")


class PersonneDict(TypedDict):
    """Structure d'un dictionnaire personne."""
    nom: str
    age: int
    email: str
    actif: bool


def creer_personne(nom: str, age: int, email: str) -> PersonneDict:
    """Cree un dictionnaire personne."""
    return {
        "nom": nom,
        "age": age,
        "email": email,
        "actif": True
    }


def afficher_personne(personne: PersonneDict) -> None:
    """Affiche les informations d'une personne."""
    statut = "actif" if personne["actif"] else "inactif"
    print(f"  {personne['nom']}, {personne['age']} ans ({personne['email']}) - {statut}")


personne = creer_personne("Alice", 25, "alice@example.com")
afficher_personne(personne)

bob = creer_personne("Bob", 30, "bob@example.com")
afficher_personne(bob)


# --- Final : valeurs constantes ---
print("\n=== Final ===")

PI: Final = 3.14159
MAX_CONNEXIONS: Final[int] = 100


class Configuration:
    """Configuration de l'application."""
    VERSION: Final[str] = "1.0.0"
    DEBUG: Final[bool] = False

    def __init__(self) -> None:
        self.app_name: Final = "MonApp"


config = Configuration()
print(f"PI = {PI}")
print(f"MAX_CONNEXIONS = {MAX_CONNEXIONS}")
print(f"Configuration.VERSION = {Configuration.VERSION}")
print(f"Configuration.DEBUG = {Configuration.DEBUG}")
print(f"config.app_name = {config.app_name}")


# --- Protocol : duck typing avec types ---
print("\n=== Protocol ===")


class Affichable(Protocol):
    """Protocole pour les objets affichables."""
    def afficher(self) -> str: ...


class Utilisateur:
    """Utilisateur - implemente le protocole implicitement."""
    def __init__(self, nom: str) -> None:
        self.nom = nom

    def afficher(self) -> str:
        return f"Utilisateur: {self.nom}"


class Produit:
    """Produit - implemente aussi le protocole."""
    def __init__(self, nom: str, prix: float) -> None:
        self.nom = nom
        self.prix = prix

    def afficher(self) -> str:
        return f"Produit: {self.nom} - {self.prix} EUR"


def afficher_objet(obj: Affichable) -> None:
    """Affiche n'importe quel objet affichable."""
    print(f"  {obj.afficher()}")


user = Utilisateur("Alice")
produit = Produit("Livre", 15.99)

afficher_objet(user)
afficher_objet(produit)
