# ============================================================================
#   Section 6.1-6.2 : Introduction et type hints de base
#   Description : Typage dynamique, annotations de variables et fonctions,
#                 types int, str, float, bool, None
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

# --- Typage dynamique de Python ---
age = 25        # int
nom = "Alice"   # str
prix = 19.99    # float

print(type(age), type(nom), type(prix))

# --- Sans vs avec type hints ---
# Sans type hints
def calculer_prix_sans(prix, quantite, remise):
    return prix * quantite * (1 - remise)

# Avec type hints (plus clair !)
def calculer_prix(prix: float, quantite: int, remise: float) -> float:
    return prix * quantite * (1 - remise)

print(calculer_prix(100.0, 5, 0.1))  # 450.0

# --- Annotations de variables ---
age: int = 25
nom: str = "Alice"
prix: float = 19.99
est_actif: bool = True

print(f"{nom}, {age} ans, prix: {prix}, actif: {est_actif}")

# --- Fonctions avec type hints ---
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres entiers."""
    return a + b

def saluer(nom: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {nom} !"

def afficher_message(texte: str) -> None:
    """Affiche un message (ne retourne rien)."""
    print(texte)

print(additionner(5, 3))   # 8
print(saluer("Alice"))     # Bonjour Alice !
afficher_message("Type hints de base fonctionnent !")
