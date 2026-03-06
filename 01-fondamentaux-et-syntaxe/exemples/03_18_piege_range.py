# ============================================================================
#   Section 3.18 : Piège de range()
#   Description : range(5) s'arrête avant 5, range(1, 6) pour avoir 1 à 5
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# range(5) génère : 0, 1, 2, 3, 4 (pas 5 !)
print("range(5) :")
for i in range(5):
    print(i)  # Affiche 0 à 4

# Pour avoir 1 à 5 :
print("\nrange(1, 6) :")
for i in range(1, 6):
    print(i)  # Affiche 1 à 5
