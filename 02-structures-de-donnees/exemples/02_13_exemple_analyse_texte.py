# ============================================================================
#   Section 2.2 : Exemple pratique - Analyse de texte avec compréhensions
#   Description : Fréquence des mots, mots fréquents avec compréhensions
#   Fichier source : 02-comprehensions.md
# ============================================================================

texte = "Python est un langage de programmation. Python est facile à apprendre."

# Nettoyer et séparer les mots
mots = texte.lower().replace(".", "").split()

# Compter la fréquence des mots avec une compréhension de dictionnaire
frequence = {mot: mots.count(mot) for mot in set(mots)}
print("Fréquence :", dict(sorted(frequence.items())))

# Garder seulement les mots qui apparaissent plus d'une fois
mots_frequents = {mot: freq for mot, freq in frequence.items() if freq > 1}
print(f"Mots fréquents : {mots_frequents}")  # {'python': 2, 'est': 2}
