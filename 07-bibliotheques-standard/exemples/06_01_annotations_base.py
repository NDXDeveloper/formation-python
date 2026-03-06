# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Annotations de type basiques - variables, fonctions,
#                 types de collections (list, dict, tuple, set)
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

# ==========================================
# 1. Variables simples
# ==========================================
print("=== Variables avec annotations ===")

nom: str = "Alice"
age: int = 25
prix: float = 19.99
actif: bool = True

print(f"nom: {nom} (type: {type(nom).__name__})")
print(f"age: {age} (type: {type(age).__name__})")
print(f"prix: {prix} (type: {type(prix).__name__})")
print(f"actif: {actif} (type: {type(actif).__name__})")

# Python n'applique PAS ces types à l'exécution
age_test: int = 25
age_test = "vingt-cinq"  # Pas d'erreur à l'exécution !
print(f"\nage_test: {age_test} (type: {type(age_test).__name__}) - Python n'empêche pas ça")

# ==========================================
# 2. Fonctions annotées
# ==========================================
print("\n=== Fonctions annotées ===")

def saluer(nom: str) -> str:
    """Retourne un message de salutation"""
    return f"Bonjour {nom}!"

def additionner(a: int, b: int) -> int:
    """Additionne deux nombres"""
    return a + b

def afficher_info(nom: str, age: int) -> None:
    """Affiche des informations (ne retourne rien)"""
    print(f"  {nom} a {age} ans")

resultat: str = saluer("Alice")
print(f"saluer('Alice') = {resultat}")

somme: int = additionner(5, 3)
print(f"additionner(5, 3) = {somme}")

afficher_info("Bob", 30)

# ==========================================
# 3. Listes typées
# ==========================================
print("\n=== list[type] ===")

nombres: list[int] = [1, 2, 3, 4, 5]
prenoms: list[str] = ["Alice", "Bob", "Charlie"]
matrice: list[list[int]] = [[1, 2], [3, 4], [5, 6]]

print(f"nombres: {nombres}")
print(f"prenoms: {prenoms}")
print(f"matrice: {matrice}")

def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes"""
    return sum(notes) / len(notes)

notes = [15.0, 12.5, 18.0, 14.0]
print(f"Moyenne de {notes} = {calculer_moyenne(notes)}")

# ==========================================
# 4. Dictionnaires typés
# ==========================================
print("\n=== dict[key_type, value_type] ===")

ages: dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

codes: dict[int, str] = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
}

utilisateurs: dict[str, dict[str, str]] = {
    "alice": {"email": "alice@example.com", "ville": "Paris"},
    "bob": {"email": "bob@example.com", "ville": "Lyon"}
}

print(f"ages: {ages}")
print(f"codes: {codes}")
print(f"utilisateurs: {utilisateurs}")

def compter_occurrences(mots: list[str]) -> dict[str, int]:
    """Compte les occurrences de chaque mot"""
    compteur: dict[str, int] = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

mots = ["python", "est", "python", "cool", "est"]
print(f"Occurrences de {mots}: {compter_occurrences(mots)}")

# ==========================================
# 5. Tuples typés
# ==========================================
print("\n=== tuple[types...] ===")

coordonnees: tuple[float, float] = (48.8566, 2.3522)
personne: tuple[str, int, bool] = ("Alice", 25, True)
nombres_var: tuple[int, ...] = (1, 2, 3, 4, 5)

print(f"coordonnees: {coordonnees}")
print(f"personne: {personne}")
print(f"nombres (variable): {nombres_var}")

def diviser(a: int, b: int) -> tuple[int, int]:
    """Retourne le quotient et le reste"""
    return a // b, a % b

quotient, reste = diviser(10, 3)
print(f"diviser(10, 3) = quotient={quotient}, reste={reste}")

# ==========================================
# 6. Ensembles typés
# ==========================================
print("\n=== set[type] ===")

nombres_uniques: set[int] = {1, 2, 3, 4, 5}
tags: set[str] = {"python", "programmation", "tutorial"}

print(f"nombres_uniques: {nombres_uniques}")
print(f"tags: {tags}")

def obtenir_elements_uniques(items: list[str]) -> set[str]:
    """Retourne les éléments uniques d'une liste"""
    return set(items)

fruits = ["pomme", "banane", "pomme", "orange", "banane"]
print(f"Elements uniques de {fruits}: {obtenir_elements_uniques(fruits)}")
