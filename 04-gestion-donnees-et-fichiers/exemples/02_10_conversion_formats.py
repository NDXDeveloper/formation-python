# ============================================================================
#   Section 4.2 : Conversion entre formats
#   Description : Convertir CSV vers JSON, JSON vers CSV, XML vers JSON
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import csv
import json
import xml.etree.ElementTree as ET
import os

# --- Préparer les fichiers sources ---

# CSV source
with open('employes.csv', 'w', encoding='utf-8', newline='') as f:
    f.write("nom,prenom,age,salaire,service\n")
    f.write("Dupont,Marie,28,35000,Informatique\n")
    f.write("Martin,Pierre,35,42000,Marketing\n")
    f.write("Bernard,Sophie,32,38000,Informatique\n")

# XML source
xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<bibliotheque>
    <livre id="1">
        <titre>Python pour débutants</titre>
        <auteur>Jean Dupont</auteur>
        <annee>2023</annee>
        <prix>29.99</prix>
    </livre>
    <livre id="2">
        <titre>Programmation avancée</titre>
        <auteur>Marie Martin</auteur>
        <annee>2024</annee>
        <prix>39.99</prix>
    </livre>
</bibliotheque>"""

with open('bibliotheque.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

# --- CSV -> JSON ---
print("=== CSV -> JSON ===")

employes = []
with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        employes.append(ligne)

with open('employes.json', 'w', encoding='utf-8') as fichier:
    json.dump(employes, fichier, indent=4, ensure_ascii=False)

print("Conversion CSV -> JSON terminée")

# --- JSON -> CSV ---
print("\n=== JSON -> CSV ===")

with open('employes.json', 'r', encoding='utf-8') as fichier:
    employes = json.load(fichier)

with open('employes_export.csv', 'w', encoding='utf-8', newline='') as fichier:
    if employes:
        colonnes = employes[0].keys()
        ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)
        ecrivain.writeheader()
        ecrivain.writerows(employes)

print("Conversion JSON -> CSV terminée")

# Vérification
with open('employes_export.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# --- XML -> JSON ---
print("=== XML -> JSON ===")

arbre = ET.parse('bibliotheque.xml')
racine = arbre.getroot()

livres = []
for livre in racine.findall('livre'):
    livre_dict = {
        'id': livre.get('id'),
        'titre': livre.find('titre').text,
        'auteur': livre.find('auteur').text,
        'annee': livre.find('annee').text,
        'prix': livre.find('prix').text
    }
    livres.append(livre_dict)

with open('bibliotheque.json', 'w', encoding='utf-8') as fichier:
    json.dump({'livres': livres}, fichier, indent=4, ensure_ascii=False)

print("Conversion XML -> JSON terminée")

# Vérification
with open('bibliotheque.json', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
for f in ['employes.csv', 'employes.json', 'employes_export.csv',
          'bibliotheque.xml', 'bibliotheque.json']:
    os.remove(f)
