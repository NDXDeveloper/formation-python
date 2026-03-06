# ============================================================================
#   Section 7.1 : Les modules os, sys et subprocess
#   Description : Module os.path - manipulation de chemins, vérifications,
#                 splitext, split, getsize, rename, stat
#   Fichier source : 01-os-sys-subprocess.md
# ============================================================================

import os
import shutil

# --- Manipulation des chemins avec os.path ---
print("=== os.path : manipulation de chemins ===")

# Joindre des parties de chemin
chemin = os.path.join("dossier", "sous_dossier", "fichier.txt")
print(f"Chemin joint : {chemin}")

# Vérifier si un chemin existe
print(f"\n'mon_fichier.txt' existe ? {os.path.exists('mon_fichier.txt')}")

# Créer un fichier temporaire pour les tests
with open("_test_fichier.txt", "w") as f:
    f.write("Contenu du fichier de test\nDeuxième ligne\n")

print(f"'_test_fichier.txt' existe ? {os.path.exists('_test_fichier.txt')}")
print(f"  Est un fichier ? {os.path.isfile('_test_fichier.txt')}")
print(f"  Est un répertoire ? {os.path.isdir('_test_fichier.txt')}")

# Chemin absolu
chemin_absolu = os.path.abspath("_test_fichier.txt")
print(f"\nChemin absolu : {chemin_absolu}")

# --- Séparer nom et extension ---
print("\n=== splitext et split ===")

nom_complet = "document.pdf"
nom, extension = os.path.splitext(nom_complet)
print(f"Nom : {nom}, Extension : {extension}")

nom_complet2 = "archive.tar.gz"
nom2, extension2 = os.path.splitext(nom_complet2)
print(f"Nom : {nom2}, Extension : {extension2}")

# Séparer répertoire et nom de fichier
chemin = "/home/utilisateur/documents/rapport.txt"
repertoire, fichier = os.path.split(chemin)
print(f"\nRépertoire : {repertoire}")
print(f"Fichier : {fichier}")

# --- Taille et statistiques de fichier ---
print("\n=== Taille et statistiques ===")

taille = os.path.getsize("_test_fichier.txt")
print(f"Taille du fichier : {taille} octets")

stats = os.stat("_test_fichier.txt")
print(f"Taille (stat) : {stats.st_size} octets")
print(f"Dernière modification : {stats.st_mtime:.0f} (timestamp)")

# --- Renommer un fichier ---
print("\n=== Renommer un fichier ===")

os.rename("_test_fichier.txt", "_test_renomme.txt")
print(f"Fichier renommé : '_test_fichier.txt' -> '_test_renomme.txt'")
print(f"'_test_renomme.txt' existe ? {os.path.exists('_test_renomme.txt')}")
print(f"'_test_fichier.txt' existe ? {os.path.exists('_test_fichier.txt')}")

# --- Variables d'environnement ---
print("\n=== Variables d'environnement ===")

home = os.environ.get("HOME")
print(f"Répertoire home : {home}")

api_key = os.environ.get("API_KEY", "cle_par_defaut")
print(f"API_KEY : {api_key}")

# Définir une variable temporaire
os.environ["MA_VARIABLE"] = "ma_valeur"
print(f"MA_VARIABLE : {os.environ.get('MA_VARIABLE')}")

# --- Parcourir une arborescence ---
print("\n=== Parcourir une arborescence (os.walk) ===")

# Créer une structure pour la démo
os.makedirs("_temp_arbre/src", exist_ok=True)
os.makedirs("_temp_arbre/docs", exist_ok=True)
with open("_temp_arbre/src/main.py", "w") as f:
    f.write("print('hello')\n")
with open("_temp_arbre/src/utils.py", "w") as f:
    f.write("def helper(): pass\n")
with open("_temp_arbre/docs/readme.txt", "w") as f:
    f.write("Documentation\n")

for racine, dossiers, fichiers in os.walk("_temp_arbre"):
    print(f"\nDossier : {racine}")
    for fichier in sorted(fichiers):
        chemin_complet = os.path.join(racine, fichier)
        taille = os.path.getsize(chemin_complet)
        print(f"  {fichier} ({taille} octets)")

# Nettoyage
os.remove("_test_renomme.txt")
shutil.rmtree("_temp_arbre")
del os.environ["MA_VARIABLE"]
print("\nNettoyage effectué")
