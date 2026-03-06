# ============================================================================
#   Section 2.2 : Compréhensions imbriquées avancées
#   Description : Matrice identité, filtrer listes imbriquées,
#                 dictionnaires imbriqués
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- Matrice identité 4x4 ---
taille = 4
identite = [[1 if i == j else 0 for j in range(taille)] for i in range(taille)]

print("Matrice identité :")
for ligne in identite:
    print(ligne)

# --- Filtrer des listes imbriquées ---
print()
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Extraire seulement les nombres pairs
pairs = [x for ligne in matrice for x in ligne if x % 2 == 0]
print(f"Pairs : {pairs}")  # [2, 4, 6, 8]

# Garder seulement les lignes qui contiennent au moins un nombre > 5
lignes_filtrees = [ligne for ligne in matrice if any(x > 5 for x in ligne)]
print(f"Lignes avec x > 5 : {lignes_filtrees}")  # [[4, 5, 6], [7, 8, 9]]

# --- Dictionnaires imbriqués ---
print()
categories = ["fruits", "legumes"]
items = {"fruits": ["pomme", "banane"], "legumes": ["carotte", "tomate"]}

longueurs = {
    categorie: {item: len(item) for item in items[categorie]}
    for categorie in categories
}
print(longueurs)
# {'fruits': {'pomme': 5, 'banane': 6}, 'legumes': {'carotte': 7, 'tomate': 6}}
