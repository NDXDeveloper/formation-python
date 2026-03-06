# ============================================================================
#   Section 2.1 : Les Tuples - Opérations et cas d'usage
#   Description : Concaténation, répétition, count, index, cas d'usage
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Opérations sur les tuples ---
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concaténation
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Répétition
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Longueur
print(len(tuple1))  # 3

# Vérifier la présence d'un élément
print(2 in tuple1)  # True

# Compter les occurrences
nombres = (1, 2, 3, 2, 4, 2)
print(nombres.count(2))  # 3

# Trouver l'index
print(nombres.index(3))  # 2

# --- Quand utiliser les tuples ? ---
# 1. Données qui ne doivent pas changer
DATE_NAISSANCE = (15, 8, 1990)
print(f"Date : {DATE_NAISSANCE}")

# 2. Comme clés de dictionnaire
positions = {
    (0, 0): "origine",
    (1, 0): "droite",
    (0, 1): "haut"
}
print(f"Position (0,0) : {positions[(0, 0)]}")

# 3. Retourner plusieurs valeurs d'une fonction
def obtenir_coordonnees():
    return 10, 20

x, y = obtenir_coordonnees()
print(f"x={x}, y={y}")

# 4. Garantir l'intégrité des données
JOURS_SEMAINE = ("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")
print(f"Jours : {JOURS_SEMAINE}")
