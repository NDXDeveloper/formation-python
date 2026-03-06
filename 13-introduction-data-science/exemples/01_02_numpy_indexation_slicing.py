# ============================================================================
#   Section 13.1.2 : Indexation et slicing avances
#   Description : Indexation 1D/2D, slicing, indexation par liste, indexation
#                 booleenne, modification avec indexation, indexation fancy,
#                 where/argmax/argmin/nonzero, vues vs copies, exemples pratiques
#   Fichier source : 01.2-indexation-slicing-avances.md
# ============================================================================

"""Indexation et slicing avances avec NumPy."""

import numpy as np


# ============================================================
# INDEXATION DE BASE
# ============================================================
print("=" * 50)
print("INDEXATION DE BASE")
print("=" * 50)

# --- Arrays 1D ---
arr = np.array([10, 20, 30, 40, 50])

print(f"\n  Premier element: {arr[0]}")
print(f"  Troisieme element: {arr[2]}")
print(f"  Dernier element: {arr[-1]}")
print(f"  Avant-dernier: {arr[-2]}")

# --- Modification ---
arr = np.array([10, 20, 30, 40, 50])
arr[0] = 100
print(f"\n  Array modifie: {arr}")

arr[1] = 200
arr[3] = 400
print(f"  Array modifie: {arr}")


# ============================================================
# INDEXATION MULTIDIMENSIONNELLE
# ============================================================
print(f"\n{'=' * 50}")
print("INDEXATION MULTIDIMENSIONNELLE")
print("=" * 50)

matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12]])

print(f"\n  Matrice:\n{matrice}")

print(f"\n  Element ligne 0, colonne 2: {matrice[0, 2]}")
print(f"  Element ligne 1, colonne 1: {matrice[1, 1]}")
print(f"  Element ligne 2, colonne 3: {matrice[2, 3]}")

print(f"  Derniere ligne, derniere colonne: {matrice[-1, -1]}")
print(f"  Premiere ligne, derniere colonne: {matrice[0, -1]}")

# --- Lignes et colonnes entieres ---
matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12]])

print(f"\n  Ligne 0: {matrice[0]}")
print(f"  Ligne 1: {matrice[1]}")
print(f"  Derniere ligne: {matrice[-1]}")

print(f"  Colonne 0: {matrice[:, 0]}")
print(f"  Colonne 2: {matrice[:, 2]}")
print(f"  Derniere colonne: {matrice[:, -1]}")


# ============================================================
# SLICING 1D
# ============================================================
print(f"\n{'=' * 50}")
print("SLICING 1D")
print("=" * 50)

arr = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

print(f"\n  Indices 2 a 5: {arr[2:5]}")
print(f"  Indices 0 a 3: {arr[0:3]}")
print(f"  Du debut a 4: {arr[:4]}")
print(f"  De 6 a la fin: {arr[6:]}")
print(f"  Tous les 2 elements: {arr[::2]}")
print(f"  Indices 1 a 8, par pas de 2: {arr[1:8:2]}")
print(f"  Array inverse: {arr[::-1]}")


# ============================================================
# SLICING 2D
# ============================================================
print(f"\n{'=' * 50}")
print("SLICING 2D")
print("=" * 50)

matrice = np.array([[1,  2,  3,  4,  5],
                    [6,  7,  8,  9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20]])

print(f"\n  Matrice complete:\n{matrice}")

print(f"\n  Deux premieres lignes:\n{matrice[:2]}")
print(f"\n  Trois premieres colonnes:\n{matrice[:, :3]}")
print(f"\n  Sous-matrice [1:3, 2:5]:\n{matrice[1:3, 2:5]}")
print(f"\n  Lignes 0 et 2:\n{matrice[::2]}")
print(f"\n  Colonnes paires:\n{matrice[:, ::2]}")


# ============================================================
# INDEXATION PAR LISTE D'INDICES
# ============================================================
print(f"\n{'=' * 50}")
print("INDEXATION PAR LISTE D'INDICES")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

indices = [1, 3, 5]
print(f"\n  Elements aux indices 1, 3, 5: {arr[indices]}")
print(f"  Elements [0, 2, 4, 8]: {arr[[0, 2, 4, 8]]}")
print(f"  Avec repetitions [1, 1, 3, 3]: {arr[[1, 1, 3, 3]]}")

# --- Indexation avancee 2D ---
matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12]])

lignes = [0, 2]
print(f"\n  Lignes 0 et 2:\n{matrice[lignes]}")

lignes = [0, 1, 2]
colonnes = [1, 2, 3]
print(f"  Elements diagonaux: {matrice[lignes, colonnes]}")

lignes = [0, 0, 2, 2]
colonnes = [0, 3, 0, 3]
print(f"  Les 4 coins: {matrice[lignes, colonnes]}")


# ============================================================
# INDEXATION BOOLEENNE
# ============================================================
print(f"\n{'=' * 50}")
print("INDEXATION BOOLEENNE")
print("=" * 50)

arr = np.array([10, 25, 30, 15, 40, 5, 35])

masque = arr > 20
print(f"\n  Masque (> 20): {masque}")
print(f"  Valeurs > 20: {arr[masque]}")
print(f"  Valeurs > 20 (direct): {arr[arr > 20]}")

# --- Conditions multiples ---
arr = np.array([10, 25, 30, 15, 40, 5, 35, 20])

print(f"\n  Valeurs entre 15 et 35: {arr[(arr >= 15) & (arr <= 35)]}")
print(f"  Valeurs < 15 ou > 35: {arr[(arr < 15) | (arr > 35)]}")
print(f"  Valeurs PAS egales a 25: {arr[arr != 25]}")
print(f"  Valeurs PAS > 30: {arr[~(arr > 30)]}")

# --- Indexation booleenne 2D ---
matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12]])

print(f"\n  Valeurs > 6: {matrice[matrice > 6]}")

masque = matrice % 2 == 0
print(f"  Valeurs paires: {matrice[masque]}")

masque_lignes = matrice[:, 0] > 5
print(f"  Lignes ou premiere colonne > 5:\n{matrice[masque_lignes]}")


# ============================================================
# MODIFICATION AVEC INDEXATION
# ============================================================
print(f"\n{'=' * 50}")
print("MODIFICATION AVEC INDEXATION")
print("=" * 50)

# --- Par slicing ---
arr = np.array([0, 10, 20, 30, 40, 50])
arr[1:4] = 99
print(f"\n  Apres modification (slice=99): {arr}")

arr[1:4] = [11, 22, 33]
print(f"  Apres modification (sequence): {arr}")

# --- Par indexation booleenne ---
arr = np.array([10, 25, 30, 15, 40, 5, 35])
arr[arr > 30] = 30
print(f"\n  Valeurs plafonnees a 30: {arr}")

arr = np.array([5, -2, 8, -7, 3, -1])
arr[arr < 0] = 0
print(f"  Negatifs remplaces par 0: {arr}")

arr = np.array([10, 20, 30, 40, 50])
arr[arr < 35] += 5
print(f"  Valeurs < 35 incrementees: {arr}")

# --- Modification 2D ---
matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrice[1] = [40, 50, 60]
print(f"\n  Ligne modifiee:\n{matrice}")

matrice[:, 2] = [300, 600, 900]
print(f"  Colonne modifiee:\n{matrice}")

matrice[0:2, 0:2] = [[11, 22], [44, 55]]
print(f"  Sous-matrice modifiee:\n{matrice}")


# ============================================================
# INDEXATION FANCY
# ============================================================
print(f"\n{'=' * 50}")
print("INDEXATION FANCY")
print("=" * 50)

matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

lignes = [0, 2, 3]
colonnes = [1, 3]

resultat = matrice[np.ix_(lignes, colonnes)]
print(f"\n  Sous-matrice avec np.ix_:\n{resultat}")

resultat2 = matrice[lignes][:, colonnes]
print(f"  Meme resultat:\n{resultat2}")

# --- Diagonale ---
matrice = np.array([[1,  2,  3,  4],
                    [5,  6,  7,  8],
                    [9, 10, 11, 12]])

indices = np.arange(3)
diagonale = matrice[indices, indices]
print(f"\n  Diagonale: {diagonale}")

anti_diag = matrice[indices, [2, 1, 0]]
print(f"  Anti-diagonale: {anti_diag}")


# ============================================================
# FONCTIONS UTILES
# ============================================================
print(f"\n{'=' * 50}")
print("FONCTIONS UTILES")
print("=" * 50)

# --- where ---
arr = np.array([10, 25, 30, 15, 40, 5, 35])
indices_w = np.where(arr > 20)
print(f"\n  Indices des valeurs > 20: {indices_w}")
print(f"  Valeurs correspondantes: {arr[indices_w]}")

matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

lignes, colonnes = np.where(matrice > 5)
print(f"\n  Positions ou valeur > 5:")
print(f"  Lignes: {lignes}")
print(f"  Colonnes: {colonnes}")
print(f"  Valeurs: {matrice[lignes, colonnes]}")

# --- argmax / argmin ---
arr = np.array([30, 10, 50, 20, 40])
idx_max = np.argmax(arr)
print(f"\n  Index du max: {idx_max}")
print(f"  Valeur max: {arr[idx_max]}")

idx_min = np.argmin(arr)
print(f"  Index du min: {idx_min}")
print(f"  Valeur min: {arr[idx_min]}")

matrice = np.array([[1, 5, 3],
                    [9, 2, 7]])
print(f"\n  Index du max (aplati): {np.argmax(matrice)}")
print(f"  Index max par ligne: {np.argmax(matrice, axis=1)}")
print(f"  Index max par colonne: {np.argmax(matrice, axis=0)}")

# --- nonzero ---
arr = np.array([0, 5, 0, 8, 0, 3, 0])
indices_non_nuls = np.nonzero(arr)
print(f"\n  Indices non nuls: {indices_non_nuls}")
print(f"  Valeurs non nulles: {arr[indices_non_nuls]}")

matrice = np.array([[0, 1, 0],
                    [2, 0, 3],
                    [0, 0, 4]])
lignes, colonnes = np.nonzero(matrice)
print(f"  Lignes des non-nuls: {lignes}")
print(f"  Colonnes des non-nuls: {colonnes}")


# ============================================================
# VUES VS COPIES
# ============================================================
print(f"\n{'=' * 50}")
print("VUES VS COPIES")
print("=" * 50)

# --- Slice = vue ---
arr = np.array([0, 10, 20, 30, 40])
vue = arr[1:4]
print(f"\n  Vue: {vue}")

vue[0] = 999
print(f"  Vue apres modification: {vue}")
print(f"  Array original: {arr}")

# --- Copie explicite ---
arr = np.array([0, 10, 20, 30, 40])
copie = arr[1:4].copy()
print(f"\n  Copie: {copie}")

copie[0] = 999
print(f"  Copie apres modification: {copie}")
print(f"  Array original: {arr}")

# --- Indexation fancy = copie ---
arr = np.array([0, 10, 20, 30, 40])
indices = [1, 3]
copie = arr[indices]
copie[0] = 999
print(f"\n  Array original (fancy): {arr}")

arr = np.array([10, 20, 30, 40, 50])
copie = arr[arr > 25]
copie[0] = 999
print(f"  Array original (bool): {arr}")

# --- Verifier vue/copie ---
arr = np.array([0, 10, 20, 30, 40])
vue = arr[1:4]
print(f"\n  Vue partage la base: {vue.base is arr}")

copie = arr[1:4].copy()
print(f"  Copie partage la base: {copie.base is arr}")

print(f"  Original a une base: {arr.base is None}")


# ============================================================
# EXEMPLES PRATIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLES PRATIQUES")
print("=" * 50)

# --- Normalisation min-max ---
print(f"\n  --- Normalisation min-max ---")
donnees = np.array([10, 25, 15, 30, 20, 35])
min_val = np.min(donnees)
max_val = np.max(donnees)
donnees_normalisees = (donnees - min_val) / (max_val - min_val)
print(f"  Donnees normalisees: {donnees_normalisees}")

# --- Remplacement conditionnel ---
print(f"\n  --- Remplacement conditionnel ---")
donnees = np.array([15, 18, 200, 19, -50, 17, 20, 16], dtype=float)
seuil_bas = 10
seuil_haut = 100
donnees_clean = donnees.copy()
mediane = np.median(donnees[(donnees >= seuil_bas) & (donnees <= seuil_haut)])
donnees_clean[(donnees_clean < seuil_bas) | (donnees_clean > seuil_haut)] = mediane
print(f"  Donnees originales: {donnees}")
print(f"  Donnees nettoyees: {donnees_clean}")

# --- Extraction de sous-matrices ---
print(f"\n  --- Scores etudiants ---")
scores = np.array([[85, 90, 78, 92],
                   [88, 75, 95, 87],
                   [70, 85, 80, 88],
                   [92, 88, 85, 90],
                   [78, 82, 88, 84]])

math_chimie = scores[:, [0, 2]]
print(f"  Scores Math et Chimie:\n{math_chimie}")

bons_en_math = scores[scores[:, 0] > 85]
print(f"\n  Etudiants avec > 85 en Math:\n{bons_en_math}")

moyennes = np.mean(scores, axis=1)
print(f"\n  Moyennes des etudiants: {moyennes}")

elite = scores[moyennes > 85]
print(f"\n  Etudiants d'elite (moyenne > 85):\n{elite}")

# --- Grille de donnees ---
print(f"\n  --- Grille de donnees ---")
x = np.arange(0, 5)
y = np.arange(0, 3)
X, Y = np.meshgrid(x, y)
print(f"  Grille X:\n{X}")
print(f"  Grille Y:\n{Y}")

distances = np.sqrt(X**2 + Y**2)
print(f"  Distances:\n{np.round(distances, 2)}")

masque = distances < 2.5
print(f"\n  Points proches (distance < 2.5):")
print(f"  X: {X[masque]}")
print(f"  Y: {Y[masque]}")
