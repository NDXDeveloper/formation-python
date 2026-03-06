# ============================================================================
#   Section 10.6 : Validation de types avec mypy
#   Description : Classes typees - annotations de classe, TypeAlias,
#                 Generic[T], classe comme type de parametre
#   Fichier source : 06-validation-types-mypy.md
# ============================================================================

from typing import TypeAlias, TypeVar, Generic

# --- Classe avec annotations ---
print("=== Classe annotee ===")


class Utilisateur:
    """Represente un utilisateur."""
    nom: str
    email: str
    age: int
    actif: bool

    def __init__(self, nom: str, email: str, age: int) -> None:
        self.nom = nom
        self.email = email
        self.age = age
        self.actif = True

    def desactiver(self) -> None:
        """Desactive l'utilisateur."""
        self.actif = False

    def est_majeur(self) -> bool:
        """Verifie si l'utilisateur est majeur."""
        return self.age >= 18

    def obtenir_info(self) -> str:
        """Retourne une chaine d'information."""
        statut = "actif" if self.actif else "inactif"
        return f"{self.nom} ({self.email}) - {statut}"


# Utiliser une classe comme type
def envoyer_email(utilisateur: Utilisateur, sujet: str, message: str) -> bool:
    """Envoie un email a un utilisateur."""
    if not utilisateur.actif:
        print(f"  {utilisateur.nom} est inactif, email non envoye")
        return False
    print(f"  Email envoye a {utilisateur.email} : {sujet}")
    return True


user = Utilisateur("Alice", "alice@example.com", 25)
print(user.obtenir_info())
print(f"Est majeur : {user.est_majeur()}")
envoyer_email(user, "Bienvenue", "Merci de votre inscription")

user.desactiver()
envoyer_email(user, "Rappel", "N'oubliez pas...")


# --- TypeAlias ---
print("\n=== TypeAlias ===")

UserId: TypeAlias = int
Email: TypeAlias = str
Utilisateurs: TypeAlias = dict[UserId, Utilisateur]


def obtenir_utilisateur(
    utilisateurs: Utilisateurs,
    user_id: UserId
) -> Utilisateur | None:
    """Obtient un utilisateur par son ID."""
    return utilisateurs.get(user_id)


db: Utilisateurs = {
    1: Utilisateur("Alice", "alice@test.com", 25),
    2: Utilisateur("Bob", "bob@test.com", 30),
}

u = obtenir_utilisateur(db, 1)
if u is not None:
    print(f"Trouve : {u.obtenir_info()}")
print(f"obtenir_utilisateur(db, 999) = {obtenir_utilisateur(db, 999)}")


# --- Generic ---
print("\n=== Generic[T] ===")

T = TypeVar('T')


class Boite(Generic[T]):
    """Une boite generique pouvant contenir n'importe quel type."""

    def __init__(self, contenu: T) -> None:
        self.contenu = contenu

    def obtenir(self) -> T:
        """Retourne le contenu."""
        return self.contenu

    def remplacer(self, nouveau: T) -> None:
        """Remplace le contenu."""
        self.contenu = nouveau


boite_int: Boite[int] = Boite(42)
print(f"boite_int.obtenir() = {boite_int.obtenir()}")
boite_int.remplacer(100)
print(f"Apres remplacer(100) : {boite_int.obtenir()}")

boite_str: Boite[str] = Boite("Hello")
print(f"boite_str.obtenir() = {boite_str.obtenir()}")

boite_liste: Boite[list[int]] = Boite([1, 2, 3])
print(f"boite_liste.obtenir() = {boite_liste.obtenir()}")
