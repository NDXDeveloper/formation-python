# ============================================================================
#   Section 4.2 : XML - Modification et recherche XPath
#   Description : Modifier un élément XML existant, rechercher avec XPath
#                 (find, findall), parser un flux RSS
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

# --- Modifier un fichier XML ---
print("=== Modification XML ===")

arbre = ET.parse('bibliotheque.xml')
racine = arbre.getroot()

for livre in racine.findall('livre'):
    titre = livre.find('titre').text
    if 'Python' in titre:
        prix = livre.find('prix')
        ancien_prix = prix.text
        prix.text = '24.99'
        print(f"Prix modifié : {ancien_prix} -> {prix.text}")

arbre.write('bibliotheque_modifiee.xml', encoding='utf-8', xml_declaration=True)

# --- Rechercher avec XPath ---
print("\n=== Recherche XPath ===")

arbre = ET.parse('bibliotheque.xml')
racine = arbre.getroot()

# Trouver tous les titres
titres = racine.findall('.//titre')
for titre in titres:
    print(titre.text)

# Trouver les livres de 2024
livres_2024 = racine.findall(".//livre[annee='2024']")
print(f"\n{len(livres_2024)} livres de 2024")

# --- Parser un flux RSS (XML) ---
print("\n=== Parser un flux RSS ===")

rss_content = """
<rss version="2.0">
    <channel>
        <title>Mon Blog Tech</title>
        <item>
            <title>Nouveau tutoriel Python</title>
            <link>https://blog.com/python-tuto</link>
            <description>Apprenez Python facilement</description>
        </item>
        <item>
            <title>Les bases du Machine Learning</title>
            <link>https://blog.com/ml-basics</link>
            <description>Introduction au ML</description>
        </item>
    </channel>
</rss>
"""

racine = ET.fromstring(rss_content)

for item in racine.findall('.//item'):
    titre = item.find('title').text
    lien = item.find('link').text
    description = item.find('description').text

    print(f">> {titre}")
    print(f"   {lien}")
    print(f"   {description}")
    print()

# Nettoyage
os.remove('bibliotheque.xml')
os.remove('bibliotheque_modifiee.xml')
