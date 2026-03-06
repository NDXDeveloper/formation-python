# ============================================================================
#   Section 2.1 : Les Tuples - Créer un tuple
#   Description : Tuple vide, avec éléments, un seul élément, packing
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Tuple vide
mon_tuple = ()
autre_tuple = tuple()

# Tuple avec des éléments
coordonnees = (10, 20)
informations = ("Alice", 25, "Paris")

# Tuple avec un seul élément (attention à la virgule !)
un_element = (5,)  # Correct
pas_un_tuple = (5)  # Ceci est juste un entier entre parenthèses

print(f"un_element = {un_element}, type = {type(un_element)}")
print(f"pas_un_tuple = {pas_un_tuple}, type = {type(pas_un_tuple)}")

# Création sans parenthèses (packing)
point = 3, 4
print(point)        # (3, 4)
print(type(point))  # <class 'tuple'>
