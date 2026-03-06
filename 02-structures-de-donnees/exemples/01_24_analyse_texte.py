# ============================================================================
#   Section 2.1 : Exemple pratique - Analyse de texte
#   Description : Compteur de mots avec dictionnaire, mots uniques avec set
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

texte = "Python est un langage de programmation. Python est facile à apprendre."

# Convertir en minuscules et séparer en mots
mots = texte.lower().replace(".", "").split()

# Compter les occurrences avec un dictionnaire
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

print("Fréquence des mots :")
for mot, count in compteur.items():
    print(f"  {mot}: {count}")

# Mots uniques avec un set
mots_uniques = set(mots)
print(f"\nNombre de mots uniques : {len(mots_uniques)}")
