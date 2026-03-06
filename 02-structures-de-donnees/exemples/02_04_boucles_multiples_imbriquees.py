# ============================================================================
#   Section 2.2 : Compréhensions - Boucles multiples et imbriquées
#   Description : Plusieurs for, combinaisons, aplatir matrice,
#                 compréhensions imbriquées, table de multiplication, transposer
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- Plusieurs boucles for ---
# Créer toutes les paires possibles
couleurs = ["rouge", "vert", "bleu"]
tailles = ["S", "M", "L"]

combinaisons = [(couleur, taille) for couleur in couleurs for taille in tailles]
print(combinaisons)

# Aplatir une matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elements = [element for ligne in matrice for element in ligne]
print(elements)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Créer des paires de coordonnées
coordonnees = [(x, y) for x in range(3) for y in range(3)]
print(coordonnees)

# --- Compréhensions imbriquées ---
# Matrice 3x3 de zéros
matrice = [[0 for _ in range(3)] for _ in range(3)]
print(matrice)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Table de multiplication
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for ligne in table:
    print(ligne)

# Transposer une matrice
print()
matrice = [[1, 2, 3], [4, 5, 6]]
transposee = [[ligne[i] for ligne in matrice] for i in range(len(matrice[0]))]
print(f"Originale : {matrice}")
print(f"Transposée : {transposee}")  # [[1, 4], [2, 5], [3, 6]]
