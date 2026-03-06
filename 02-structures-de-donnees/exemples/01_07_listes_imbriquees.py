# ============================================================================
#   Section 2.1 : Les Listes - Listes imbriquées
#   Description : Matrice 2D, accès aux éléments imbriqués, parcours
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Matrice (tableau 2D)
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[0])      # [1, 2, 3]
print(matrice[1][2])   # 6

# Liste de listes avec des données variées
etudiants = [
    ["Alice", 20, "Informatique"],
    ["Bob", 22, "Mathématiques"],
    ["Charlie", 21, "Physique"]
]

for etudiant in etudiants:
    nom, age, specialite = etudiant
    print(f"{nom} a {age} ans et étudie {specialite}")
