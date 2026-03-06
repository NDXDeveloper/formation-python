# ============================================================================
#   Section 4.1 : Lecture de fichiers texte
#   Description : Quatre méthodes de lecture : read(), itération ligne par
#                 ligne, readlines(), readline()
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# Créer un fichier de test
with open('mon_document.txt', 'w', encoding='utf-8') as f:
    f.write("Bonjour le monde\n")
    f.write("Python est génial\n")
    f.write("Troisième ligne\n")

# --- Méthode 1 : Lire tout le contenu d'un coup ---
print("=== read() ===")
fichier = open('mon_document.txt', 'r', encoding='utf-8')
contenu = fichier.read()
print(contenu)
fichier.close()

# --- Méthode 2 : Lire ligne par ligne ---
print("=== Itération ligne par ligne ===")
fichier = open('mon_document.txt', 'r', encoding='utf-8')
for ligne in fichier:
    print(ligne.strip())
fichier.close()

# --- Méthode 3 : Lire toutes les lignes dans une liste ---
print("\n=== readlines() ===")
fichier = open('mon_document.txt', 'r', encoding='utf-8')
lignes = fichier.readlines()
fichier.close()

print(f"Le fichier contient {len(lignes)} lignes")
for i, ligne in enumerate(lignes, 1):
    print(f"Ligne {i}: {ligne.strip()}")

# --- Méthode 4 : Lire une seule ligne ---
print("\n=== readline() ===")
fichier = open('mon_document.txt', 'r', encoding='utf-8')
premiere_ligne = fichier.readline()
deuxieme_ligne = fichier.readline()
print("Première ligne:", premiere_ligne.strip())
print("Deuxième ligne:", deuxieme_ligne.strip())
fichier.close()

# Nettoyage
os.remove('mon_document.txt')
