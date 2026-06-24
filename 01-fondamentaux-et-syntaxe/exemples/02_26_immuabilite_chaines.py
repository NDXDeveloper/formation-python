# ============================================================================
#   Section 2.26 : Immuabilité des chaînes
#   Description : les str sont immuables ; les méthodes renvoient une nouvelle
#                 chaîne ; mot[0] = ... lève une TypeError
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Les méthodes renvoient une NOUVELLE chaîne (l'originale est inchangée) ---
texte = "bonjour"
texte.upper()          # renvoie "BONJOUR"... mais ne modifie PAS texte
print(texte)           # bonjour (inchangé !)

texte = texte.upper()  # pour « changer » la chaîne, il faut la réaffecter
print(texte)           # BONJOUR

# --- Lecture par index : OK ; modification en place : interdite ---
mot = "Python"
print(mot[0])          # P (lecture)

try:
    mot[0] = "J"       # une chaîne est immuable
except TypeError as e:
    print(f"TypeError : {e}")  # 'str' object does not support item assignment
