# ============================================================================
#   Section 4.2 : XML - Créer et écrire un fichier XML
#   Description : Construire un arbre XML avec Element, SubElement,
#                 indentation et sauvegarde
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import xml.etree.ElementTree as ET
import os

# Créer l'élément racine
bibliotheque = ET.Element('bibliotheque')

# Créer le premier livre
livre1 = ET.SubElement(bibliotheque, 'livre')
livre1.set('id', '1')

titre1 = ET.SubElement(livre1, 'titre')
titre1.text = 'Introduction à Python'

auteur1 = ET.SubElement(livre1, 'auteur')
auteur1.text = 'Alice Dupont'

annee1 = ET.SubElement(livre1, 'annee')
annee1.text = '2024'

# Créer le deuxième livre
livre2 = ET.SubElement(bibliotheque, 'livre')
livre2.set('id', '2')

titre2 = ET.SubElement(livre2, 'titre')
titre2.text = 'Data Science en Python'

auteur2 = ET.SubElement(livre2, 'auteur')
auteur2.text = 'Bob Martin'

annee2 = ET.SubElement(livre2, 'annee')
annee2.text = '2024'

# Créer l'arbre et sauvegarder
arbre = ET.ElementTree(bibliotheque)
ET.indent(arbre, space='    ')  # Python 3.9+
arbre.write('nouvelle_bibliotheque.xml', encoding='utf-8', xml_declaration=True)

print("Fichier XML créé !")

# Vérification
with open('nouvelle_bibliotheque.xml', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
os.remove('nouvelle_bibliotheque.xml')
