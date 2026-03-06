# ============================================================================
#   Section 2.4 : Regex - re.sub() et re.split()
#   Description : Remplacer avec regex, fonction de remplacement, diviser
#                 avec regex
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# --- re.sub() - Remplacer ---
texte = "Il y a 123 pommes et 456 oranges"

# Remplacer tous les nombres par 'X'
nouveau = re.sub(r'\d+', 'X', texte)
print(nouveau)  # Il y a X pommes et X oranges

# Avec une fonction de remplacement
def doubler(match):
    nombre = int(match.group())
    return str(nombre * 2)

nouveau = re.sub(r'\d+', doubler, texte)
print(nouveau)  # Il y a 246 pommes et 912 oranges

# --- re.split() - Diviser ---
print()

# Split sur les espaces (multiple)
texte = "un    deux  trois     quatre"
mots = re.split(r'\s+', texte)
print(mots)  # ['un', 'deux', 'trois', 'quatre']

# Split sur plusieurs séparateurs
texte2 = "un,deux;trois:quatre"
parties = re.split(r'[,;:]', texte2)
print(parties)  # ['un', 'deux', 'trois', 'quatre']

# Split avec limite
texte3 = "a-b-c-d-e"
parties = re.split(r'-', texte3, maxsplit=2)
print(parties)  # ['a', 'b', 'c-d-e']
