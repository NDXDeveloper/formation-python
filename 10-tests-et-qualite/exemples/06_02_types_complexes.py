# ============================================================================
#   Section 10.6 : Validation de types avec mypy
#   Description : Types complexes - list, dict, set, tuple, Optional,
#                 Union, Any, Callable, Iterable, Sequence, Mapping
#   Fichier source : 06-validation-types-mypy.md
# ============================================================================

from typing import Callable, Iterable, Sequence, Mapping

# --- Collections typees (syntaxe Python 3.9+) ---
print("=== Collections typees ===")

nombres: list[int] = [1, 2, 3, 4, 5]
prenoms: list[str] = ["Alice", "Bob", "Charlie"]
ages: dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}
uniques: set[int] = {1, 2, 3, 4, 5}
personne: tuple[str, int, bool] = ("Alice", 25, True)
coordonnees: tuple[int, ...] = (10, 20, 30, 40)

print(f"nombres: list[int] = {nombres}")
print(f"prenoms: list[str] = {prenoms}")
print(f"ages: dict[str, int] = {ages}")
print(f"uniques: set[int] = {uniques}")
print(f"personne: tuple[str, int, bool] = {personne}")
print(f"coordonnees: tuple[int, ...] = {coordonnees}")


# --- Optional (valeur ou None) ---
print("\n=== Optional (str | None) ===")


def trouver_utilisateur(user_id: int) -> str | None:
    """Trouve un utilisateur par son ID."""
    utilisateurs = {1: "Alice", 2: "Bob"}
    return utilisateurs.get(user_id)


nom = trouver_utilisateur(1)
if nom is not None:
    print(f"Trouve : {nom}")

nom2 = trouver_utilisateur(999)
print(f"trouver_utilisateur(999) = {nom2}")


# --- Union (plusieurs types) ---
print("\n=== Union (int | float | str) ===")


def formater_valeur(valeur: int | float | str) -> str:
    """Formate une valeur en chaine."""
    return f"Valeur : {valeur}"


print(formater_valeur(42))
print(formater_valeur(3.14))
print(formater_valeur("texte"))


# --- Callable (fonctions comme parametres) ---
print("\n=== Callable ===")


def executer_operation(
    x: int,
    y: int,
    operation: Callable[[int, int], int]
) -> int:
    """Execute une operation sur deux nombres."""
    return operation(x, y)


def additionner(a: int, b: int) -> int:
    return a + b


def multiplier(a: int, b: int) -> int:
    return a * b


resultat1 = executer_operation(5, 3, additionner)
resultat2 = executer_operation(5, 3, multiplier)
print(f"executer_operation(5, 3, additionner) = {resultat1}")
print(f"executer_operation(5, 3, multiplier) = {resultat2}")


# --- Iterable, Sequence, Mapping ---
print("\n=== Iterable, Sequence, Mapping ===")


def somme(nombres: Iterable[int]) -> int:
    """Calcule la somme de nombres iterables."""
    return sum(nombres)


print(f"somme([1, 2, 3]) = {somme([1, 2, 3])}")
print(f"somme((1, 2, 3)) = {somme((1, 2, 3))}")
print(f"somme({{1, 2, 3}}) = {somme({1, 2, 3})}")
print(f"somme(range(1, 4)) = {somme(range(1, 4))}")


def premier_element(sequence: Sequence[str]) -> str:
    """Retourne le premier element d'une sequence."""
    return sequence[0]


print(f"premier_element(['a', 'b', 'c']) = {premier_element(['a', 'b', 'c'])}")
print(f"premier_element('abc') = {premier_element('abc')}")


def compter_occurrences(texte: str) -> Mapping[str, int]:
    """Compte les occurrences de chaque caractere."""
    compteur: dict[str, int] = {}
    for char in texte:
        compteur[char] = compteur.get(char, 0) + 1
    return compteur


print(f"compter_occurrences('hello') = {compter_occurrences('hello')}")
