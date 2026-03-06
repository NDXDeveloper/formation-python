# ============================================================================
#   Section 6.16 : Type hints dans les compréhensions
#   Description : Annoter les variables résultantes des compréhensions,
#                 fonctions retournant des compréhensions
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

# Compréhension de liste
carres: list[int] = [x**2 for x in range(10)]
print(f"Carrés : {carres}")

# Compréhension de dictionnaire
ages: dict[str, int] = {nom: age for nom, age in [("Alice", 25), ("Bob", 30)]}
print(f"Ages : {ages}")

# Annoter dans une fonction
def generer_carres(n: int) -> list[int]:
    return [x**2 for x in range(n)]

print(f"Carrés de 0 à 4 : {generer_carres(5)}")  # [0, 1, 4, 9, 16]
