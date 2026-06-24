# ============================================================================
#   Section 6.17 : Type hints et documentation (docstring + doctest)
#   Description : combiner type hints + docstring détaillée + exemples doctest
#                 exécutables (python -m doctest 06_17_documentation_type_hints.py)
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================


def rechercher_utilisateur(
    nom: str,
    age_min: int | None = None,
    age_max: int | None = None,
) -> list[dict[str, str | int]]:
    """
    Recherche des utilisateurs selon des critères.

    Les type hints indiquent les types, la docstring explique la logique
    et les cas particuliers.

    Args:
        nom: Nom à rechercher (insensible à la casse).
        age_min: Âge minimum inclus. Si None, pas de limite inférieure.
        age_max: Âge maximum inclus. Si None, pas de limite supérieure.

    Returns:
        Liste de dictionnaires {'nom': str, 'age': int} correspondants.

    Examples:
        >>> rechercher_utilisateur("Alice")
        [{'nom': 'Alice', 'age': 25}]
        >>> rechercher_utilisateur("Bob", age_min=20, age_max=30)
        [{'nom': 'Bob', 'age': 28}]
    """
    # Données d'exemple (en pratique : une base de données)
    base = [{"nom": "Alice", "age": 25}, {"nom": "Bob", "age": 28}]
    resultats = [u for u in base if u["nom"].lower() == nom.lower()]
    if age_min is not None:
        resultats = [u for u in resultats if u["age"] >= age_min]
    if age_max is not None:
        resultats = [u for u in resultats if u["age"] <= age_max]
    return resultats


print(rechercher_utilisateur("Alice"))                        # [{'nom': 'Alice', 'age': 25}]
print(rechercher_utilisateur("Bob", age_min=20, age_max=30))  # [{'nom': 'Bob', 'age': 28}]
print(rechercher_utilisateur("Inconnu"))                      # []
