# ============================================================================
#   Section 2.1 : Les Sets - Créer un set et caractéristiques
#   Description : Set vide, à partir de liste, doublons éliminés, pas d'ordre
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Set vide (attention : {} crée un dictionnaire vide, pas un set)
mon_set = set()

# Set avec des éléments
nombres = {1, 2, 3, 4, 5}
fruits = {"pomme", "banane", "orange"}

# Créer un set à partir d'une liste (élimine les doublons)
liste_avec_doublons = [1, 2, 2, 3, 3, 3, 4]
nombres_uniques = set(liste_avec_doublons)
print(nombres_uniques)  # {1, 2, 3, 4}

# Créer un set à partir d'une chaîne
lettres = set("hello")
print(sorted(lettres))  # ['e', 'h', 'l', 'o']

# --- Caractéristiques ---
# Les doublons sont automatiquement éliminés
nombres = {1, 2, 2, 3, 3, 3}
print(nombres)  # {1, 2, 3}

# Les éléments doivent être immuables (hashables) : nombres (int, float), booléens, chaînes, tuples
valide = {1, "texte", (1, 2), 3.14, True}
print(f"Set valide : {sorted(str(e) for e in valide)}")
# Note : True et 1 partagent la même valeur et le même hachage → ils comptent comme UN
# seul élément (l'ensemble ci-dessus contient donc 4 éléments distincts, pas 5)

# Les listes ne peuvent pas être dans un set
try:
    invalide = {[1, 2, 3]}
except TypeError as e:
    print(f"TypeError : {e}")
