# ============================================================================
#   Section 2.1 : Exemple pratique - Gestion d'étudiants
#   Description : Liste de tuples, set de matières, dictionnaire matière->étudiants
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Liste de tuples pour les étudiants
etudiants = [
    ("Alice", 18, ["Math", "Physique", "Informatique"]),
    ("Bob", 19, ["Math", "Chimie"]),
    ("Charlie", 18, ["Physique", "Informatique", "Chimie"])
]

# Extraire toutes les matières uniques avec un set
toutes_matieres = set()
for nom, age, matieres in etudiants:
    toutes_matieres.update(matieres)

print("Matières enseignées :", sorted(toutes_matieres))

# Créer un dictionnaire : matière -> liste d'étudiants
matieres_etudiants = {matiere: [] for matiere in toutes_matieres}

for nom, age, matieres in etudiants:
    for matiere in matieres:
        matieres_etudiants[matiere].append(nom)

print("\nÉtudiants par matière :")
for matiere, noms in sorted(matieres_etudiants.items()):
    print(f"  {matiere}: {', '.join(noms)}")
