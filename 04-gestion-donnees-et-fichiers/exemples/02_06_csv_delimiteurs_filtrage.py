# ============================================================================
#   Section 4.2 : CSV - Délimiteurs et filtrage
#   Description : Utiliser le point-virgule comme délimiteur,
#                 filtrer et exporter des données CSV
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import csv
import os

# --- Gérer différents délimiteurs ---
print("=== Délimiteur point-virgule ===")

# Créer un fichier avec point-virgule
with open('donnees_fr.csv', 'w', encoding='utf-8', newline='') as f:
    ecrivain = csv.writer(f, delimiter=';')
    ecrivain.writerow(['Nom', 'Ville', 'Population'])
    ecrivain.writerow(['Paris', 'France', '2200000'])
    ecrivain.writerow(['Lyon', 'France', '515000'])

# Lire avec point-virgule
with open('donnees_fr.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier, delimiter=';')
    for ligne in lecteur:
        print(ligne)

# --- Filtrer et exporter ---
print("\n=== Filtrer et exporter ===")

# Créer un fichier CSV source
with open('employes.csv', 'w', encoding='utf-8', newline='') as f:
    f.write("nom,prenom,age,salaire,service\n")
    f.write("Dupont,Marie,28,35000,Informatique\n")
    f.write("Martin,Pierre,35,42000,Marketing\n")
    f.write("Bernard,Sophie,32,38000,Informatique\n")

# Lire les données
employes = []
with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        employes.append(ligne)

# Filtrer : seulement le service Informatique
informaticiens = [e for e in employes if e['service'] == 'Informatique']

# Exporter les résultats
with open('informaticiens.csv', 'w', encoding='utf-8', newline='') as fichier:
    colonnes = ['nom', 'prenom', 'age', 'salaire']
    ecrivain = csv.DictWriter(fichier, fieldnames=colonnes, extrasaction='ignore')
    ecrivain.writeheader()
    ecrivain.writerows(informaticiens)

print(f"{len(informaticiens)} informaticiens exportés")

# Vérification
with open('informaticiens.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
os.remove('donnees_fr.csv')
os.remove('employes.csv')
os.remove('informaticiens.csv')
