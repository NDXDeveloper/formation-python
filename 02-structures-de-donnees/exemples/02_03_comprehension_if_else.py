# ============================================================================
#   Section 2.2 : Compréhensions de listes - Avec if-else
#   Description : Transformation conditionnelle, classification, notes
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Remplacer les nombres négatifs par 0
nombres = [-2, -1, 0, 1, 2, 3]
positifs_ou_zero = [x if x >= 0 else 0 for x in nombres]
print(positifs_ou_zero)  # [0, 0, 0, 1, 2, 3]

# Classifier les nombres en "pair" ou "impair"
nombres = [1, 2, 3, 4, 5]
classification = ["pair" if x % 2 == 0 else "impair" for x in nombres]
print(classification)  # ['impair', 'pair', 'impair', 'pair', 'impair']

# Appliquer une réduction aux produits chers
prix = [100, 200, 150, 300]
prix_soldes = [p * 0.8 if p > 150 else p for p in prix]
print(prix_soldes)  # [100, 160.0, 150, 240.0]

# Convertir des notes en appréciation
notes = [18, 12, 8, 15]
appreciations = ["Excellent" if n >= 16 else "Bien" if n >= 12 else "Passable" for n in notes]
print(appreciations)  # ['Excellent', 'Bien', 'Passable', 'Bien']
