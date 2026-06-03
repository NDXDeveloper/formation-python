# ============================================================================
#   Section 4.2 : CSV - Lecture de fichiers CSV
#   Description : csv.reader() et csv.DictReader() pour lire des données
#                 tabulaires
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import csv
import os

# Créer un fichier CSV de test
with open('employes.csv', 'w', encoding='utf-8', newline='') as f:
    f.write("nom,prenom,age,salaire,service\n")
    f.write("Dupont,Marie,28,35000,Informatique\n")
    f.write("Martin,Pierre,35,42000,Marketing\n")
    f.write("Bernard,Sophie,32,38000,Informatique\n")

# --- Méthode 1 : csv.reader() ---
print("=== csv.reader() ===")

with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier)

    entetes = next(lecteur)
    print("Colonnes :", entetes)

    for ligne in lecteur:
        nom = ligne[0]
        prenom = ligne[1]
        age = ligne[2]
        print(f"{prenom} {nom} - {age} ans")

# --- Méthode 2 : csv.DictReader() (recommandé) ---
print("\n=== csv.DictReader() ===")

with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.DictReader(fichier)

    for ligne in lecteur:
        print(f"{ligne['prenom']} {ligne['nom']}")
        print(f"  Âge: {ligne['age']} ans")
        print(f"  Salaire: {ligne['salaire']} EUR")
        print(f"  Service: {ligne['service']}")
        print()

# --- Pourquoi le module csv (et pas split(',')) ? ---
# Sur un champ contenant une virgule (entre guillemets), split(',') se trompe :
print("=== csv.reader vs split(',') ===")
with open('villes.csv', 'w', encoding='utf-8', newline='') as f:
    f.write('ville,population\n')
    f.write('"Lyon, France",515000\n')   # virgule DANS le champ ville

with open('villes.csv', 'r', encoding='utf-8') as f:
    next(f)  # ignorer l'en-tête
    ligne = next(f)
    print("split(',') :", ligne.strip().split(','))   # 3 morceaux -> FAUX

with open('villes.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.reader(f)
    next(lecteur)
    print("csv.reader :", next(lecteur))               # 2 champs -> correct

# Nettoyage
os.remove('employes.csv')
os.remove('villes.csv')
