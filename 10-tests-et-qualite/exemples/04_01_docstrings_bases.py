# ============================================================================
#   Section 10.4 : Documentation avec docstrings
#   Description : Bases des docstrings - acces via __doc__, help(),
#                 inspect.signature, PEP 257
#   Fichier source : 04-documentation-docstrings.md
# ============================================================================

import inspect


def saluer(nom):
    """Salue une personne par son nom."""
    return f"Bonjour {nom} !"


def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.

    Cette fonction prend une liste de nombres et retourne
    leur moyenne arithmetique. La liste ne doit pas etre vide.
    """
    return sum(nombres) / len(nombres)


# --- Acces a la docstring ---
print("=== Acces aux docstrings ===")
print(f"saluer.__doc__ : {saluer.__doc__}")
print(f"calculer_moyenne.__doc__ : {calculer_moyenne.__doc__}")

# --- Signature ---
print("\n=== Signatures ===")
print(f"signature saluer : {inspect.signature(saluer)}")
print(f"signature calculer_moyenne : {inspect.signature(calculer_moyenne)}")

# --- Utilisation ---
print("\n=== Utilisation ===")
print(saluer("Alice"))
print(f"Moyenne de [1, 2, 3, 4, 5] : {calculer_moyenne([1, 2, 3, 4, 5])}")

# --- help() ---
print("\n=== help(saluer) ===")
help(saluer)
