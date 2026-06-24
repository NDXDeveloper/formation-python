# ============================================================================
#   Section 2.23 : Comparaisons enchaînées
#   Description : enchaîner des comparaisons (18 <= age < 65), équivalence avec and
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

age = 25

# « age est-il entre 18 (inclus) et 65 (exclu) ? »
print(18 <= age < 65)           # True

# Équivaut à (mais plus court et plus lisible) :
print(18 <= age and age < 65)   # True

note = 14
if 10 <= note < 16:
    print("Mention assez bien ou bien")

# L'enchaînement marche avec tous les opérateurs de comparaison
print(1 < 2 < 3 < 4)            # True
print(0 <= age <= 17)           # False
