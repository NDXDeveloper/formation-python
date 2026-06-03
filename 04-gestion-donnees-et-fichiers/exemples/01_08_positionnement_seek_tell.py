# ============================================================================
#   Section 4.1 : Positionnement dans un fichier (seek et tell)
#   Description : tell() pour connaître la position, seek() pour la déplacer,
#                 mode 'r+' pour lire ET écrire
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# Créer un fichier de test
with open('donnees.txt', 'w', encoding='utf-8') as f:
    f.write("ABCDEFGHIJ")

# --- tell() et seek() ---
print("=== tell() et seek() ===")
with open('donnees.txt', 'r', encoding='utf-8') as f:
    print(f"Position initiale : {f.tell()}")   # 0
    print(f"read(3) : {f.read(3)}")             # ABC
    print(f"Position : {f.tell()}")             # 3

    f.seek(0)                                   # revenir au début
    print(f"Après seek(0), read(2) : {f.read(2)}")  # AB

    f.seek(5)                                   # sauter à la position 5
    print(f"Après seek(5), read() : {f.read()}")    # FGHIJ

# --- Le mode 'r+' : lire ET écrire sans effacer ---
print("\n=== Mode 'r+' ===")
with open('donnees.txt', 'r+', encoding='utf-8') as f:
    f.seek(0)
    f.write("12345")        # remplace les 5 premiers caractères

with open('donnees.txt', 'r', encoding='utf-8') as f:
    print(f"Après r+/write au début : {f.read()}")  # 12345FGHIJ

# Nettoyage
os.remove('donnees.txt')
