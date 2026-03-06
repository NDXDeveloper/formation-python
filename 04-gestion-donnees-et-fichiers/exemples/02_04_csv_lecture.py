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
        print(f"  Age: {ligne['age']} ans")
        print(f"  Salaire: {ligne['salaire']} EUR")
        print(f"  Service: {ligne['service']}")
        print()

# Nettoyage
os.remove('employes.csv')
