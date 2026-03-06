# ============================================================================
#   Section 6.13-6.14 : Valeurs par défaut et annotations *args/**kwargs
#   Description : Combiner type hints et valeurs par défaut,
#                 annoter *args et **kwargs
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import Any

# --- Valeurs par défaut avec type hints ---
def creer_liste(
    elements: list[int] | None = None,
    taille: int = 10
) -> list[int]:
    """Crée une liste avec des éléments ou une liste vide."""
    if elements is None:
        return [0] * taille
    return elements

print(f"Liste par défaut : {creer_liste()}")           # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(f"Liste donnée : {creer_liste([1, 2, 3])}")      # [1, 2, 3]
print(f"Liste taille 3 : {creer_liste(taille=3)}")     # [0, 0, 0]

def saluer(
    nom: str = "Anonyme",
    titre: str = "M."
) -> str:
    return f"Bonjour {titre} {nom}"

print(saluer())                    # Bonjour M. Anonyme
print(saluer("Alice", "Mme"))     # Bonjour Mme Alice

# --- Annotations *args et **kwargs ---
def somme(*nombres: int) -> int:
    """Somme un nombre variable d'entiers."""
    return sum(nombres)

print(f"somme(1, 2, 3, 4, 5) = {somme(1, 2, 3, 4, 5)}")  # 15

def afficher_infos(**infos: str) -> None:
    """Affiche des informations (clés et valeurs str)."""
    for cle, valeur in infos.items():
        print(f"  {cle}: {valeur}")

print("Infos :")
afficher_infos(nom="Alice", ville="Paris", metier="Dev")

# Avec Any pour accepter n'importe quel type
def fonction_flexible(*args: Any, **kwargs: Any) -> None:
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")

print("Flexible :")
fonction_flexible(1, "deux", 3.0, nom="Alice", age=25)
