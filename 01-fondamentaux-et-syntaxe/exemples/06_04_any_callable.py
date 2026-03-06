# ============================================================================
#   Section 6.5-6.6 : Any, object et Callable
#   Description : Type Any pour valeurs quelconques, Callable pour fonctions
#                 en paramètre, transformer_liste avec map/filter
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import Any, Callable
from collections.abc import Callable as CallableABC

# --- Any ---
def traiter_donnee(donnee: Any) -> Any:
    """Accepte n'importe quel type et retourne n'importe quel type."""
    return donnee

valeur: Any = 42
print(f"Any (int) : {valeur}")
valeur = "texte"
print(f"Any (str) : {valeur}")
valeur = [1, 2, 3]
print(f"Any (list) : {valeur}")

# --- object ---
def afficher(valeur: object) -> None:
    """Accepte n'importe quel objet."""
    print(f"object : {valeur}")

afficher(42)
afficher("texte")

# --- Callable ---
def appliquer_operation(
    valeur: int,
    operation: Callable[[int], int]
) -> int:
    """Applique une opération à une valeur."""
    return operation(valeur)

def doubler(x: int) -> int:
    return x * 2

def tripler(x: int) -> int:
    return x * 3

resultat1 = appliquer_operation(5, doubler)
resultat2 = appliquer_operation(5, tripler)
print(f"doubler(5) = {resultat1}")   # 10
print(f"tripler(5) = {resultat2}")   # 15

# --- Callable avec transformer_liste ---
def transformer_liste(
    liste: list[int],
    fonction: CallableABC[[int], int]
) -> list[int]:
    """Transforme chaque élément d'une liste."""
    return [fonction(x) for x in liste]

def carre(x: int) -> int:
    return x ** 2

nombres = [1, 2, 3, 4, 5]
carres = transformer_liste(nombres, carre)
print(f"carrés de {nombres} = {carres}")  # [1, 4, 9, 16, 25]
