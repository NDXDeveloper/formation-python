# ============================================================================
#   Section 4.2 : CSV - Écriture de fichiers CSV
#   Description : csv.writer() avec writerows(), csv.DictWriter() avec
#                 writeheader() et writerows()
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import csv
import os

# --- Méthode 1 : csv.writer() ---
print("=== csv.writer() ===")

donnees = [
    ['nom', 'prenom', 'age'],
    ['Dubois', 'Jean', '40'],
    ['Petit', 'Claire', '29'],
    ['Roux', 'Thomas', '33']
]

with open('nouveau_fichier.csv', 'w', encoding='utf-8', newline='') as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(donnees)

print("Fichier CSV créé !")

# Vérification
with open('nouveau_fichier.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# --- Méthode 2 : csv.DictWriter() (recommandé) ---
print("=== csv.DictWriter() ===")

employes = [
    {'nom': 'Durand', 'prenom': 'Alice', 'age': 30, 'service': 'RH'},
    {'nom': 'Moreau', 'prenom': 'Bob', 'age': 27, 'service': 'Finance'},
    {'nom': 'Simon', 'prenom': 'Clara', 'age': 31, 'service': 'IT'}
]

with open('employes_nouveaux.csv', 'w', encoding='utf-8', newline='') as fichier:
    colonnes = ['nom', 'prenom', 'age', 'service']
    ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)
    ecrivain.writeheader()
    ecrivain.writerows(employes)

print("Fichier CSV avec dictionnaires créé !")

# Vérification
with open('employes_nouveaux.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
os.remove('nouveau_fichier.csv')
os.remove('employes_nouveaux.csv')
