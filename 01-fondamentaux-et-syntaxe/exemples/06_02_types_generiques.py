# ============================================================================
#   Section 6.3 : Types génériques (Collections)
#   Description : Annotations pour list, dict, tuple, set avec types d'éléments
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

# --- list ---
nombres: list[int] = [1, 2, 3, 4, 5]
noms: list[str] = ["Alice", "Bob", "Charlie"]
prix: list[float] = [19.99, 29.99, 9.99]

def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes."""
    return sum(notes) / len(notes)

print(f"Moyenne : {calculer_moyenne([12.0, 15.0, 18.0])}")  # 15.0

# --- dict ---
ages: dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

prix_fruits: dict[str, float] = {
    "pomme": 2.50,
    "banane": 1.80,
    "orange": 3.20
}

def compter_occurrences(texte: str) -> dict[str, int]:
    """Compte les occurrences de chaque mot."""
    mots = texte.split()
    compteur: dict[str, int] = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

print(compter_occurrences("le chat le chien le chat"))

# --- tuple ---
personne: tuple[str, int] = ("Alice", 25)
coordonnees: tuple[float, float, float] = (10.5, 20.3, 5.8)

def obtenir_info() -> tuple[str, int, str]:
    """Retourne (nom, age, ville)."""
    return "Alice", 25, "Paris"

print(obtenir_info())  # ('Alice', 25, 'Paris')

# Tuple de longueur variable
nombres_var: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"Tuple variable : {nombres_var}")

# --- set ---
nombres_uniques: set[int] = {1, 2, 3, 4, 5}
tags: set[str] = {"python", "programming", "tutorial"}

def obtenir_lettres_uniques(texte: str) -> set[str]:
    """Retourne l'ensemble des lettres uniques dans un texte."""
    return set(texte.lower())

print(f"Lettres uniques dans 'Bonjour' : {sorted(obtenir_lettres_uniques('Bonjour'))}")
