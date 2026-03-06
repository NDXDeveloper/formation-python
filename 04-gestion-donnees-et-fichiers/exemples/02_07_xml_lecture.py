# ============================================================================
#   Section 4.2 : XML - Lecture de fichiers XML
#   Description : Parser un fichier XML avec ElementTree, accéder aux
#                 éléments, attributs et texte
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import xml.etree.ElementTree as ET
import os

# Créer un fichier XML de test
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

# --- Lire un fichier XML ---
arbre = ET.parse('bibliotheque.xml')
racine = arbre.getroot()

print(f"Élément racine : {racine.tag}")

# Parcourir tous les livres
for livre in racine.findall('livre'):
    livre_id = livre.get('id')  # Récupérer l'attribut
    titre = livre.find('titre').text
    auteur = livre.find('auteur').text
    annee = livre.find('annee').text
    prix = livre.find('prix').text

    print(f"\nLivre ID: {livre_id}")
    print(f"  Titre: {titre}")
    print(f"  Auteur: {auteur}")
    print(f"  Année: {annee}")
    print(f"  Prix: {prix} EUR")

# Nettoyage
os.remove('bibliotheque.xml')
