# ============================================================================
#   Section 6.4 : Types optionnels et Union
#   Description : Type | None pour valeurs optionnelles, unions de types
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

# --- Type | None (valeur optionnelle) ---
def chercher_utilisateur(id: int) -> str | None:
    """
    Cherche un utilisateur par ID.
    Retourne le nom ou None si non trouvé.
    """
    utilisateurs = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return utilisateurs.get(id)

print(chercher_utilisateur(1))   # Alice
print(chercher_utilisateur(99))  # None

# Variables optionnelles
nom: str | None = None
nom = "Alice"
print(f"nom = {nom}")

age: int | None = None
age = 25
print(f"age = {age}")

# --- Union de types (Type1 | Type2) ---
nombre: int | float = 42
print(f"nombre (int) = {nombre}")
nombre = 3.14
print(f"nombre (float) = {nombre}")

def diviser(a: int | float, b: int | float) -> float:
    """Divise deux nombres (entiers ou décimaux)."""
    return a / b

print(f"diviser(10, 3) = {diviser(10, 3):.4f}")

def obtenir_valeur(cle: str) -> str | int:
    valeurs = {"nom": "Alice", "age": 25}
    return valeurs.get(cle, "inconnu")

print(f"obtenir_valeur('nom') = {obtenir_valeur('nom')}")
print(f"obtenir_valeur('age') = {obtenir_valeur('age')}")
print(f"obtenir_valeur('xyz') = {obtenir_valeur('xyz')}")
