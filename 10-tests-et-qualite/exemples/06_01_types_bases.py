# ============================================================================
#   Section 10.6 : Validation de types avec mypy
#   Description : Types de base - typage dynamique, type hints sur
#                 variables et fonctions, annotations int/str/float/bool
#   Fichier source : 06-validation-types-mypy.md
# ============================================================================

# --- Python est dynamiquement type ---
print("=== Typage dynamique ===")

x = 5
y = "hello"
z = [1, 2, 3]
print(f"x = {x} (type: {type(x).__name__})")
print(f"y = {y} (type: {type(y).__name__})")
print(f"z = {z} (type: {type(z).__name__})")


def additionner_dynamique(a, b):
    return a + b


print(f"\nadditionner(5, 3) = {additionner_dynamique(5, 3)}")
print(f"additionner('Hello', ' World') = {additionner_dynamique('Hello', ' World')}")

try:
    additionner_dynamique(5, "3")
except TypeError as e:
    print(f"additionner(5, '3') -> TypeError: {e}")


# --- Type hints sur les fonctions ---
print("\n=== Fonctions avec type hints ===")


def additionner(a: int, b: int) -> int:
    """Additionne deux entiers."""
    return a + b


def diviser(a: float, b: float) -> float:
    """Divise deux nombres."""
    return a / b


def afficher_message(message: str) -> None:
    """Affiche un message (ne retourne rien)."""
    print(f"  Message : {message}")


print(f"additionner(5, 3) = {additionner(5, 3)}")
print(f"diviser(10.0, 3.0) = {diviser(10.0, 3.0):.2f}")
afficher_message("Bonjour le monde !")


# --- Variables avec annotations ---
print("\n=== Variables annotees ===")

age: int = 25
prix: float = 19.99
nom: str = "Alice"
est_actif: bool = True
resultat: None = None

print(f"age: int = {age}")
print(f"prix: float = {prix}")
print(f"nom: str = {nom}")
print(f"est_actif: bool = {est_actif}")
print(f"resultat: None = {resultat}")


# --- Classe avec annotations ---
print("\n=== Classe avec annotations ===")


class Personne:
    nom: str
    age: int

    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age


p = Personne("Bob", 30)
print(f"Personne : {p.nom}, {p.age} ans")
