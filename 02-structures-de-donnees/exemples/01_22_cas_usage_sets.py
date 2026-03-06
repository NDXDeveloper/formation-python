# ============================================================================
#   Section 2.1 : Les Sets - Cas d'usage pratiques et frozenset
#   Description : Éliminer doublons, éléments uniques, vérifier unicité,
#                 mots uniques, frozenset immuable
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# 1. Éliminer les doublons d'une liste
liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
liste_sans_doublons = list(set(liste))
print(f"Sans doublons : {sorted(liste_sans_doublons)}")  # [1, 2, 3, 4]

# Pour éliminer les doublons en préservant l'ordre :
liste_ordonnee = list(dict.fromkeys(liste))
print(f"Ordre préservé : {liste_ordonnee}")  # [1, 2, 3, 4]

# 2. Trouver les éléments uniques entre deux listes
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
uniques = sorted(set(liste1) ^ set(liste2))
print(f"Éléments uniques : {uniques}")  # [1, 2, 3, 6, 7, 8]

# 3. Vérifier si tous les éléments d'une liste sont uniques
def tous_uniques(liste):
    return len(liste) == len(set(liste))

print(f"[1,2,3,4] uniques : {tous_uniques([1, 2, 3, 4])}")  # True
print(f"[1,2,2,3] uniques : {tous_uniques([1, 2, 2, 3])}")  # False

# 4. Trouver les mots uniques dans un texte
texte = "le chat et le chien jouent avec le chat"
mots = texte.split()
mots_uniques = set(mots)
print(f"Mots uniques : {sorted(mots_uniques)}")
print(f"Nombre de mots uniques : {len(mots_uniques)}")  # 6

# --- Frozenset (set immuable) ---
print("\n--- Frozenset ---")
nombres_immutables = frozenset([1, 2, 3, 4, 5])

# On peut lire mais pas modifier
print(f"3 in frozenset : {3 in nombres_immutables}")  # True

try:
    nombres_immutables.add(6)
except AttributeError as e:
    print(f"AttributeError : {e}")

# Utile comme clé de dictionnaire
dict_avec_frozenset = {
    frozenset([1, 2]): "ensemble A",
    frozenset([3, 4]): "ensemble B"
}
print(f"frozenset([1,2]) -> {dict_avec_frozenset[frozenset([1, 2])]}")

# Set de sets
set_de_sets = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6])
}
print(f"Set de frozensets : {set_de_sets}")
