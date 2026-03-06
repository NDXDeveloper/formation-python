# ============================================================================
#   Section 4.1 : Exemples pratiques
#   Description : Compter les mots, fichier de log, lire un CSV simple,
#                 sauvegarder/relire une liste
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os
from datetime import datetime

# --- Exemple 1 : Compter les mots dans un fichier ---
print("=== Compter les mots ===")

with open('texte.txt', 'w', encoding='utf-8') as f:
    f.write("Python est un langage de programmation\n")
    f.write("Il est simple et puissant\n")

with open('texte.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()
    mots = contenu.split()
    print(f"Nombre de mots : {len(mots)}")

# --- Exemple 2 : Créer un fichier de log ---
print("\n=== Fichier de log ===")

def ajouter_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('application.log', 'a', encoding='utf-8') as log:
        log.write(f"[{timestamp}] {message}\n")

ajouter_log("Application démarrée")
ajouter_log("Traitement des données...")
ajouter_log("Application terminée")

with open('application.log', 'r', encoding='utf-8') as f:
    print(f.read())

# --- Exemple 3 : Lire un fichier CSV simple ---
print("=== Lire un CSV simple ===")

with open('donnees.csv', 'w', encoding='utf-8') as f:
    f.write("nom,age,ville\n")
    f.write("Alice,30,Paris\n")
    f.write("Bob,25,Lyon\n")
    f.write("Charlie,35,Marseille\n")

with open('donnees.csv', 'r', encoding='utf-8') as fichier:
    next(fichier)  # Ignorer les en-têtes
    for ligne in fichier:
        valeurs = ligne.strip().split(',')
        print(valeurs)

# --- Exemple 4 : Sauvegarder une liste en fichier ---
print("\n=== Sauvegarder/relire une liste ===")

noms = ["Alice", "Bob", "Charlie", "Diana"]

# Sauvegarder
with open('noms.txt', 'w', encoding='utf-8') as fichier:
    for nom in noms:
        fichier.write(nom + '\n')

# Relire
with open('noms.txt', 'r', encoding='utf-8') as fichier:
    noms_lus = [ligne.strip() for ligne in fichier]
    print(noms_lus)

# Nettoyage
for f in ['texte.txt', 'application.log', 'donnees.csv', 'noms.txt']:
    os.remove(f)
