# ============================================================================
#   Section 2.3 : defaultdict - Dictionnaires avec valeurs par défaut
#   Description : Problème KeyError, solution defaultdict, types de factory
#                 (int, list, set, dict, custom)
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import defaultdict

# --- Problème avec dict classique ---
compteur = {}
texte = "hello"
for lettre in texte:
    if lettre in compteur:
        compteur[lettre] += 1
    else:
        compteur[lettre] = 1
print(f"Dict classique : {compteur}")

# --- Solution : defaultdict ---
compteur = defaultdict(int)  # int() retourne 0
texte = "hello"
for lettre in texte:
    compteur[lettre] += 1  # Pas besoin de vérifier !
print(f"defaultdict : {dict(compteur)}")

# --- Différents types de factory ---
# int() retourne 0
dd_int = defaultdict(int)
print(f"int : {dd_int['cle_inexistante']}")  # 0

# list() retourne []
dd_list = defaultdict(list)
print(f"list : {dd_list['cle_inexistante']}")  # []

# set() retourne set()
dd_set = defaultdict(set)
print(f"set : {dd_set['cle_inexistante']}")  # set()

# str() retourne ''
dd_str = defaultdict(str)
print(f"str : '{dd_str['cle_inexistante']}'")  # ''

# Fonction personnalisée
def valeur_par_defaut():
    return "N/A"

dd_custom = defaultdict(valeur_par_defaut)
print(f"custom : {dd_custom['cle_inexistante']}")  # 'N/A'
