# ============================================================================
#   Section 2.2 : Tester une collection avec any() et all()
#   Description : any (au moins un vrai), all (tous vrais), souvent avec une
#                 expression génératrice ; cas particulier de la collection vide
#   Fichier source : 02-comprehensions.md
# ============================================================================

nombres = [2, 4, 6, 8]

print(all(n % 2 == 0 for n in nombres))   # True  (tous pairs ?)
print(any(n > 5 for n in nombres))         # True  (au moins un > 5 ?)
print(any(n < 0 for n in nombres))         # False (au moins un négatif ?)

# Valider toute une collection
notes = [12, 15, 8, 18]
print(all(0 <= note <= 20 for note in notes))  # True (toutes valides)
print(any(note < 10 for note in notes))        # True (au moins un échec)

# Collection vide : all([]) -> True, any([]) -> False
print(all([]))  # True
print(any([]))  # False
