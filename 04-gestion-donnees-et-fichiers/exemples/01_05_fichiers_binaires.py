# ============================================================================
#   Section 4.1 : Fichiers binaires
#   Description : Écriture, lecture, copie et lecture par morceaux de fichiers
#                 binaires
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# --- Écriture d'un fichier binaire ---
donnees = bytes([0, 1, 2, 3, 4, 5])

with open('donnees.bin', 'wb') as fichier:
    fichier.write(donnees)

print("Fichier binaire créé")

# --- Lecture d'un fichier binaire ---
with open('donnees.bin', 'rb') as fichier:
    contenu_binaire = fichier.read()
    print(f"Taille du fichier : {len(contenu_binaire)} octets")
    print(f"Contenu : {list(contenu_binaire)}")

# --- Copier un fichier binaire ---
with open('donnees.bin', 'rb') as source:
    contenu = source.read()

with open('copie.bin', 'wb') as destination:
    destination.write(contenu)

print("Fichier copié avec succès")

# --- Lire un fichier binaire par morceaux ---
# Créer un fichier un peu plus gros pour la démo
with open('gros_fichier.bin', 'wb') as f:
    f.write(bytes(range(256)) * 10)  # 2560 octets

taille_morceau = 1024  # 1 Ko à la fois

print(f"\nLecture par morceaux de {taille_morceau} octets :")
with open('gros_fichier.bin', 'rb') as fichier:
    while True:
        morceau = fichier.read(taille_morceau)
        if not morceau:
            break
        print(f"Lu {len(morceau)} octets")

# Nettoyage
os.remove('donnees.bin')
os.remove('copie.bin')
os.remove('gros_fichier.bin')
