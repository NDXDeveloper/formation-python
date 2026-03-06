# ============================================================================
#   Section 2.2 : Exemple pratique - Opérations matricielles
#   Description : Addition de matrices et transposition avec compréhensions
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Addition de matrices
matrice_a = [[1, 2, 3], [4, 5, 6]]
matrice_b = [[7, 8, 9], [10, 11, 12]]

# Additionner élément par élément
somme = [
    [matrice_a[i][j] + matrice_b[i][j] for j in range(len(matrice_a[0]))]
    for i in range(len(matrice_a))
]
print(f"A + B = {somme}")  # [[8, 10, 12], [14, 16, 18]]

# Transposition
matrice = [[1, 2, 3], [4, 5, 6]]
transposee = [[ligne[i] for ligne in matrice] for i in range(len(matrice[0]))]
print(f"Transposée = {transposee}")  # [[1, 4], [2, 5], [3, 6]]
