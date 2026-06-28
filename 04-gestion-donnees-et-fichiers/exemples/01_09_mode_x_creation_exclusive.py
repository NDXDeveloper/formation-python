# ============================================================================
#   Section 4.1 : Mode 'x' - Création exclusive
#   Description : Créer un fichier seulement s'il n'existe pas ; FileExistsError
#                 si le fichier existe déjà (contrairement à 'w' qui écrase)
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# Au cas où un ancien fichier traînerait
if os.path.exists('rapport.txt'):
    os.remove('rapport.txt')

# --- Première création avec 'x' : réussit (le fichier n'existe pas) ---
try:
    with open('rapport.txt', 'x', encoding='utf-8') as fichier:
        fichier.write("Premier rapport\n")
    print("Fichier créé")
except FileExistsError:
    print("Le fichier existe déjà : aucune donnée écrasée")

# --- Deuxième tentative avec 'x' : échoue (le fichier existe maintenant) ---
try:
    with open('rapport.txt', 'x', encoding='utf-8') as fichier:
        fichier.write("Tentative d'écrasement")
    print("Fichier créé")
except FileExistsError:
    print("Le fichier existe déjà : aucune donnée écrasée")

# Le contenu d'origine est intact : le mode 'x' n'a rien écrasé
with open('rapport.txt', 'r', encoding='utf-8') as f:
    print("Contenu conservé :", f.read().strip())

# Nettoyage
os.remove('rapport.txt')
