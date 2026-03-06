# ============================================================================
#   Section 2.2 : Compréhensions de listes - Cas d'usage pratiques
#   Description : Extraire données, nettoyer lignes, filtrer voyelles, aplatir
#   Fichier source : 02-comprehensions.md
# ============================================================================

# 1. Extraire des données structurées
etudiants = [
    {"nom": "Alice", "age": 20, "note": 18},
    {"nom": "Bob", "age": 22, "note": 14},
    {"nom": "Charlie", "age": 21, "note": 16}
]

# Extraire seulement les noms
noms = [etudiant["nom"] for etudiant in etudiants]
print(noms)  # ['Alice', 'Bob', 'Charlie']

# Extraire les noms des étudiants ayant plus de 15
bons_etudiants = [e["nom"] for e in etudiants if e["note"] >= 15]
print(bons_etudiants)  # ['Alice', 'Charlie']

# 2. Traiter des fichiers (simulé)
lignes = ["  ligne 1  ", "  ligne 2\n", "ligne 3  "]
lignes_nettoyees = [ligne.strip() for ligne in lignes]
print(lignes_nettoyees)  # ['ligne 1', 'ligne 2', 'ligne 3']

# 3. Filtrer et transformer en une étape
texte = "Python Est Un Langage Génial"
voyelles = [c.lower() for c in texte if c.lower() in 'aeiouy']
print(voyelles)  # ['y', 'o', 'e', 'u', 'a', 'a', 'e', 'i', 'a']

# 4. Aplatir une structure imbriquée
listes_imbriquees = [[1, 2], [3, 4], [5, 6]]
liste_plate = [element for sous_liste in listes_imbriquees for element in sous_liste]
print(liste_plate)  # [1, 2, 3, 4, 5, 6]
