# ============================================================================
#   Section 4.1 : Le gestionnaire de contexte with
#   Description : Utiliser with pour ouvrir/fermer automatiquement,
#                 exemple lecture-transformation-écriture
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# Créer un fichier source de test
with open('source.txt', 'w', encoding='utf-8') as f:
    f.write("bonjour le monde\n")
    f.write("python est génial\n")
    f.write("troisième ligne\n")

# --- Syntaxe avec with ---
print("=== Lecture avec with ===")
with open('source.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()
    print(contenu)
# Ici, le fichier est déjà fermé (pas besoin de close())

# --- Exemple complet : lecture + transformation + écriture ---
print("=== Transformation en majuscules ===")

# Lire un fichier
with open('source.txt', 'r', encoding='utf-8') as fichier_source:
    lignes = fichier_source.readlines()

# Transformer les données
lignes_majuscules = [ligne.upper() for ligne in lignes]

# Écrire dans un nouveau fichier
with open('destination.txt', 'w', encoding='utf-8') as fichier_dest:
    fichier_dest.writelines(lignes_majuscules)

print("Traitement terminé !")

# Vérification
with open('destination.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
os.remove('source.txt')
os.remove('destination.txt')
