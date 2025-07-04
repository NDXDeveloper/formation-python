🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.2 : Formats de données (JSON, CSV, XML)

## Introduction

Dans le monde réel, les données sont rarement stockées sous forme de texte brut. Elles sont organisées selon des formats standardisés qui permettent de structurer l'information de manière logique et portable. Cette section vous apprendra à manipuler les trois formats de données les plus courants : JSON, CSV et XML.

## Pourquoi utiliser des formats structurés ?

### Avantages des formats structurés
- **Lisibilité** : Structure claire et organisée
- **Interopérabilité** : Échange entre différents systèmes
- **Validation** : Possibilité de vérifier la structure
- **Portabilité** : Indépendant du langage de programmation

### Cas d'usage typiques
- **APIs** : Échange de données entre applications
- **Configuration** : Paramètres d'applications
- **Export/Import** : Données depuis/vers Excel, bases de données
- **Logs structurés** : Faciliter l'analyse automatique

## Format JSON (JavaScript Object Notation)

### Qu'est-ce que JSON ?

JSON est un format léger et lisible pour l'échange de données. Malgré son nom, il n'est pas limité à JavaScript et est devenu le standard pour les APIs web.

### Structure de base JSON

```json
{
  "nom": "Alice",
  "age": 30,
  "ville": "Paris",
  "mariee": false,
  "enfants": ["Tom", "Emma"],
  "adresse": {
    "rue": "123 rue de la Paix",
    "code_postal": "75001"
  }
}
```

### Types de données JSON
- **Chaînes** : `"texte"`
- **Nombres** : `42`, `3.14`
- **Booléens** : `true`, `false`
- **null** : `null`
- **Tableaux** : `[1, 2, 3]`
- **Objets** : `{"clé": "valeur"}`

### Lecture de JSON avec Python

```python
import json

# Lecture depuis un fichier
with open('donnees.json', 'r', encoding='utf-8') as f:
    donnees = json.load(f)
    print(donnees)

# Lecture depuis une chaîne
json_string = '{"nom": "Bob", "age": 25}'
donnees = json.loads(json_string)
print(f"Nom: {donnees['nom']}, Age: {donnees['age']}")
```

**Exemple pratique :**

```python
# Création d'un fichier JSON d'exemple
donnees_exemple = {
    "utilisateurs": [
        {"nom": "Alice", "email": "alice@email.com", "actif": True},
        {"nom": "Bob", "email": "bob@email.com", "actif": False},
        {"nom": "Charlie", "email": "charlie@email.com", "actif": True}
    ],
    "version": "1.0",
    "derniere_mise_a_jour": "2024-01-15"
}

# Sauvegarde
with open('utilisateurs.json', 'w', encoding='utf-8') as f:
    json.dump(donnees_exemple, f, indent=2, ensure_ascii=False)

# Lecture et affichage
with open('utilisateurs.json', 'r', encoding='utf-8') as f:
    donnees = json.load(f)
    print("Utilisateurs actifs :")
    for utilisateur in donnees['utilisateurs']:
        if utilisateur['actif']:
            print(f"- {utilisateur['nom']} ({utilisateur['email']})")
```

### Écriture de JSON avec Python

```python
import json

# Dictionnaire Python à convertir
donnees = {
    "produits": [
        {"nom": "Laptop", "prix": 999.99, "stock": 5},
        {"nom": "Souris", "prix": 29.99, "stock": 50}
    ],
    "magasin": "TechStore"
}

# Écriture dans un fichier
with open('inventaire.json', 'w', encoding='utf-8') as f:
    json.dump(donnees, f, indent=2, ensure_ascii=False)

# Conversion en chaîne
json_string = json.dumps(donnees, indent=2, ensure_ascii=False)
print(json_string)
```

### Options importantes pour JSON

```python
import json
from datetime import datetime

donnees = {
    "nom": "François",
    "date": datetime.now(),
    "prix": 29.99
}

# Gestion des types non-JSON
def serializer_date(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f"Type {type(obj)} non sérialisable")

# Écriture avec options
with open('donnees.json', 'w', encoding='utf-8') as f:
    json.dump(donnees, f,
              indent=2,                    # Indentation pour lisibilité
              ensure_ascii=False,          # Permet les caractères non-ASCII
              default=serializer_date,     # Gestion des types personnalisés
              sort_keys=True)              # Trie les clés
```

## Format CSV (Comma-Separated Values)

### Qu'est-ce que CSV ?

CSV est un format simple pour représenter des données tabulaires. Chaque ligne représente un enregistrement et les colonnes sont séparées par des virgules (ou autres délimiteurs).

### Structure de base CSV

```csv
nom,age,ville,salaire
Alice,30,Paris,45000
Bob,25,Lyon,38000
Charlie,35,Marseille,52000
```

### Lecture de CSV avec Python

```python
import csv

# Lecture basique
with open('employes.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)  # Chaque ligne est une liste
```

### Lecture avec DictReader (recommandé)

```python
import csv

# Lecture avec en-têtes comme clés
with open('employes.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"Nom: {ligne['nom']}, Salaire: {ligne['salaire']}€")
```

**Exemple pratique complet :**

```python
import csv

# Création d'un fichier CSV d'exemple
donnees_employes = [
    ['nom', 'age', 'ville', 'salaire'],
    ['Alice', '30', 'Paris', '45000'],
    ['Bob', '25', 'Lyon', '38000'],
    ['Charlie', '35', 'Marseille', '52000'],
    ['Diana', '28', 'Nice', '41000']
]

# Écriture du fichier
with open('employes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(donnees_employes)

# Lecture et analyse
def analyser_employes(fichier_csv):
    employes = []
    with open(fichier_csv, 'r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            employes.append({
                'nom': ligne['nom'],
                'age': int(ligne['age']),
                'ville': ligne['ville'],
                'salaire': int(ligne['salaire'])
            })

    # Calculs
    salaire_moyen = sum(emp['salaire'] for emp in employes) / len(employes)
    age_moyen = sum(emp['age'] for emp in employes) / len(employes)

    print(f"Nombre d'employés: {len(employes)}")
    print(f"Salaire moyen: {salaire_moyen:.2f}€")
    print(f"Âge moyen: {age_moyen:.1f} ans")

    return employes

# Utilisation
employes = analyser_employes('employes.csv')
```

### Écriture de CSV avec Python

```python
import csv

# Données à écrire
produits = [
    {'nom': 'Laptop', 'prix': 999.99, 'categorie': 'Informatique'},
    {'nom': 'Livre', 'prix': 15.50, 'categorie': 'Culture'},
    {'nom': 'Casque', 'prix': 89.99, 'categorie': 'Audio'}
]

# Écriture avec DictWriter
with open('produits.csv', 'w', newline='', encoding='utf-8') as f:
    colonnes = ['nom', 'prix', 'categorie']
    writer = csv.DictWriter(f, fieldnames=colonnes)

    writer.writeheader()  # Écrit les en-têtes
    writer.writerows(produits)  # Écrit toutes les lignes

print("Fichier produits.csv créé avec succès!")
```

### Gestion des délimiteurs spéciaux

```python
import csv

# CSV avec point-virgule (format français)
with open('donnees_fr.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['nom', 'prix'])
    writer.writerow(['Produit A', '19,99'])  # Virgule décimale française

# Lecture avec point-virgule
with open('donnees_fr.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.reader(f, delimiter=';')
    for ligne in lecteur:
        print(ligne)
```

## Format XML (eXtensible Markup Language)

### Qu'est-ce que XML ?

XML est un format de balisage extensible qui permet de créer des documents structurés hiérarchiquement. Il est très utilisé dans les systèmes d'entreprise et les échanges de données.

### Structure de base XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bibliotheque>
    <livre id="1">
        <titre>Le Petit Prince</titre>
        <auteur>Antoine de Saint-Exupéry</auteur>
        <annee>1943</annee>
        <genre>Fiction</genre>
    </livre>
    <livre id="2">
        <titre>1984</titre>
        <auteur>George Orwell</auteur>
        <annee>1949</annee>
        <genre>Dystopie</genre>
    </livre>
</bibliotheque>
```

### Lecture de XML avec Python

```python
import xml.etree.ElementTree as ET

# Lecture depuis un fichier
tree = ET.parse('bibliotheque.xml')
root = tree.getroot()

print(f"Élément racine: {root.tag}")

# Parcours des livres
for livre in root.findall('livre'):
    livre_id = livre.get('id')
    titre = livre.find('titre').text
    auteur = livre.find('auteur').text
    annee = livre.find('annee').text

    print(f"Livre {livre_id}: {titre} par {auteur} ({annee})")
```

**Exemple pratique complet :**

```python
import xml.etree.ElementTree as ET

# Création d'un fichier XML d'exemple
def creer_xml_exemple():
    # Création de la structure XML
    root = ET.Element("catalogue")

    # Ajout de produits
    produits = [
        {"id": "1", "nom": "Smartphone", "prix": "599", "stock": "25"},
        {"id": "2", "nom": "Tablette", "prix": "399", "stock": "15"},
        {"id": "3", "nom": "Laptop", "prix": "899", "stock": "8"}
    ]

    for produit_data in produits:
        produit = ET.SubElement(root, "produit", id=produit_data["id"])

        nom = ET.SubElement(produit, "nom")
        nom.text = produit_data["nom"]

        prix = ET.SubElement(produit, "prix")
        prix.text = produit_data["prix"]

        stock = ET.SubElement(produit, "stock")
        stock.text = produit_data["stock"]

    # Sauvegarde
    tree = ET.ElementTree(root)
    tree.write('catalogue.xml', encoding='utf-8', xml_declaration=True)
    print("Fichier catalogue.xml créé!")

# Lecture et analyse du XML
def analyser_catalogue(fichier_xml):
    try:
        tree = ET.parse(fichier_xml)
        root = tree.getroot()

        print(f"Analyse du catalogue ({root.tag}):")
        print("-" * 40)

        total_stock = 0
        for produit in root.findall('produit'):
            produit_id = produit.get('id')
            nom = produit.find('nom').text
            prix = float(produit.find('prix').text)
            stock = int(produit.find('stock').text)
            total_stock += stock

            print(f"ID: {produit_id} | {nom} | {prix}€ | Stock: {stock}")

        print(f"\nStock total: {total_stock} articles")

    except ET.ParseError as e:
        print(f"Erreur de parsing XML: {e}")
    except FileNotFoundError:
        print(f"Fichier {fichier_xml} non trouvé")

# Utilisation
creer_xml_exemple()
analyser_catalogue('catalogue.xml')
```

### Écriture de XML avec Python

```python
import xml.etree.ElementTree as ET

def creer_xml_configuration():
    # Création de la configuration
    config = ET.Element("configuration")

    # Section base de données
    db = ET.SubElement(config, "base_de_donnees")

    host = ET.SubElement(db, "host")
    host.text = "localhost"

    port = ET.SubElement(db, "port")
    port.text = "5432"

    nom_db = ET.SubElement(db, "nom")
    nom_db.text = "mon_app"

    # Section logging
    logging = ET.SubElement(config, "logging")
    logging.set("niveau", "INFO")

    fichier_log = ET.SubElement(logging, "fichier")
    fichier_log.text = "app.log"

    # Sauvegarde formatée
    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for child in elem:
                indent(child, level+1)
            if not child.tail or not child.tail.strip():
                child.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    indent(config)
    tree = ET.ElementTree(config)
    tree.write('config.xml', encoding='utf-8', xml_declaration=True)
    print("Configuration XML créée!")

# Utilisation
creer_xml_configuration()
```

## Comparaison des formats

### Tableau comparatif

| Critère | JSON | CSV | XML |
|---------|------|-----|-----|
| **Lisibilité** | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| **Simplicité** | ★★★★☆ | ★★★★★ | ★★☆☆☆ |
| **Flexibilité** | ★★★★☆ | ★★☆☆☆ | ★★★★★ |
| **Taille** | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| **Support types** | ★★★☆☆ | ★☆☆☆☆ | ★★★★☆ |
| **Performance** | ★★★★☆ | ★★★★★ | ★★★☆☆ |

### Quand utiliser chaque format ?

**JSON** - Idéal pour :
- APIs REST
- Configuration d'applications
- Échange de données web
- Données semi-structurées

**CSV** - Idéal pour :
- Données tabulaires
- Export/import Excel
- Données statistiques
- Logs simples

**XML** - Idéal pour :
- Documents structurés complexes
- Échange B2B
- Configuration avec validation
- Données hiérarchiques

## Exemples pratiques complets

### Exemple 1 : Convertisseur de formats

```python
import json
import csv
import xml.etree.ElementTree as ET

def csv_vers_json(fichier_csv, fichier_json):
    """Convertit un fichier CSV en JSON"""
    donnees = []

    with open(fichier_csv, 'r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            donnees.append(ligne)

    with open(fichier_json, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=2, ensure_ascii=False)

    print(f"Conversion terminée: {fichier_csv} → {fichier_json}")

def json_vers_csv(fichier_json, fichier_csv):
    """Convertit un fichier JSON en CSV"""
    with open(fichier_json, 'r', encoding='utf-8') as f:
        donnees = json.load(f)

    if not donnees:
        print("Aucune donnée à convertir")
        return

    # Obtenir les colonnes depuis le premier enregistrement
    colonnes = list(donnees[0].keys())

    with open(fichier_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(donnees)

    print(f"Conversion terminée: {fichier_json} → {fichier_csv}")

# Test des conversions
# csv_vers_json('employes.csv', 'employes.json')
# json_vers_csv('employes.json', 'employes_copie.csv')
```

### Exemple 2 : Gestionnaire de configuration multi-format

```python
import json
import xml.etree.ElementTree as ET
import os

class GestionnaireConfig:
    def __init__(self):
        self.config = {}

    def charger_json(self, fichier):
        """Charge une configuration JSON"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"Configuration JSON chargée depuis {fichier}")
        except FileNotFoundError:
            print(f"Fichier {fichier} non trouvé")

    def sauvegarder_json(self, fichier):
        """Sauvegarde la configuration en JSON"""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        print(f"Configuration sauvegardée en JSON dans {fichier}")

    def charger_xml(self, fichier):
        """Charge une configuration XML simple"""
        try:
            tree = ET.parse(fichier)
            root = tree.getroot()
            self.config = {}

            for element in root:
                if len(element) == 0:  # Élément simple
                    self.config[element.tag] = element.text
                else:  # Élément avec sous-éléments
                    self.config[element.tag] = {}
                    for sous_element in element:
                        self.config[element.tag][sous_element.tag] = sous_element.text

            print(f"Configuration XML chargée depuis {fichier}")
        except FileNotFoundError:
            print(f"Fichier {fichier} non trouvé")

    def afficher_config(self):
        """Affiche la configuration actuelle"""
        print("Configuration actuelle:")
        print(json.dumps(self.config, indent=2, ensure_ascii=False))

    def modifier_valeur(self, cle, valeur):
        """Modifie une valeur de configuration"""
        self.config[cle] = valeur
        print(f"Valeur modifiée: {cle} = {valeur}")

# Utilisation
gestionnaire = GestionnaireConfig()

# Configuration par défaut
gestionnaire.config = {
    "nom_app": "MonApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

# Sauvegarde et chargement
gestionnaire.sauvegarder_json('app_config.json')
gestionnaire.afficher_config()
```

## Gestion des erreurs communes

### Erreurs JSON

```python
import json

def lire_json_securise(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Fichier {fichier} non trouvé")
        return None
    except json.JSONDecodeError as e:
        print(f"Erreur de format JSON: {e}")
        return None
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return None

# Test avec un JSON invalide
donnees = lire_json_securise('fichier_invalide.json')
if donnees:
    print("Données chargées avec succès")
```

### Erreurs CSV

```python
import csv

def lire_csv_securise(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            # Détecter le délimiteur automatiquement
            echantillon = f.read(1024)
            f.seek(0)

            dialecte = csv.Sniffer().sniff(echantillon)
            lecteur = csv.DictReader(f, dialect=dialecte)

            return list(lecteur)
    except FileNotFoundError:
        print(f"Fichier {fichier} non trouvé")
        return []
    except csv.Error as e:
        print(f"Erreur CSV: {e}")
        return []
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return []

# Test
donnees = lire_csv_securise('donnees.csv')
print(f"Nombre de lignes lues: {len(donnees)}")
```

## Exercices pratiques

### Exercice 1 : Carnet d'adresses JSON

Créez un programme qui gère un carnet d'adresses au format JSON.

```python
import json
import os

class CarnetAdresses:
    def __init__(self, fichier='carnet.json'):
        self.fichier = fichier
        self.contacts = self.charger_contacts()

    def charger_contacts(self):
        """Charge les contacts depuis le fichier JSON"""
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Erreur de format JSON, création d'un nouveau carnet")
                return []
        return []

    def sauvegarder_contacts(self):
        """Sauvegarde les contacts dans le fichier JSON"""
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump(self.contacts, f, indent=2, ensure_ascii=False)
        print("Contacts sauvegardés!")

    def ajouter_contact(self, nom, email, telephone):
        """Ajoute un nouveau contact"""
        contact = {
            "nom": nom,
            "email": email,
            "telephone": telephone
        }
        self.contacts.append(contact)
        print(f"Contact {nom} ajouté!")

    def afficher_contacts(self):
        """Affiche tous les contacts"""
        if not self.contacts:
            print("Aucun contact trouvé")
            return

        print("\n=== CARNET D'ADRESSES ===")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['nom']}")
            print(f"   Email: {contact['email']}")
            print(f"   Téléphone: {contact['telephone']}")
            print()

    def rechercher_contact(self, nom):
        """Recherche un contact par nom"""
        for contact in self.contacts:
            if nom.lower() in contact['nom'].lower():
                return contact
        return None

# Utilisation
carnet = CarnetAdresses()
carnet.ajouter_contact("Alice Dupont", "alice@email.com", "01.23.45.67.89")
carnet.ajouter_contact("Bob Martin", "bob@email.com", "06.12.34.56.78")
carnet.afficher_contacts()
carnet.sauvegarder_contacts()
```

### Exercice 2 : Analyseur de ventes CSV

Créez un programme qui analyse des données de ventes depuis un fichier CSV.

```python
import csv
from datetime import datetime
from collections import defaultdict

def analyser_ventes(fichier_csv):
    """Analyse les données de ventes depuis un fichier CSV"""

    # Lecture des données
    ventes = []
    try:
        with open(fichier_csv, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            for ligne in lecteur:
                ventes.append({
                    'date': ligne['date'],
                    'produit': ligne['produit'],
                    'quantite': int(ligne['quantite']),
                    'prix_unitaire': float(ligne['prix_unitaire']),
                    'vendeur': ligne['vendeur']
                })
    except FileNotFoundError:
        print(f"Fichier {fichier_csv} non trouvé")
        return

    # Analyses
    total_ventes = sum(v['quantite'] * v['prix_unitaire'] for v in ventes)
    total_quantite = sum(v['quantite'] for v in ventes)

    # Ventes par produit
    ventes_par_produit = defaultdict(lambda: {'quantite': 0, 'chiffre': 0})
    for vente in ventes:
        produit = vente['produit']
        chiffre = vente['quantite'] * vente['prix_unitaire']
        ventes_par_produit[produit]['quantite'] += vente['quantite']
        ventes_par_produit[produit]['chiffre'] += chiffre

    # Ventes par vendeur
    ventes_par_vendeur = defaultdict(lambda: {'quantite': 0, 'chiffre': 0})
    for vente in ventes:
        vendeur = vente['vendeur']
        chiffre = vente['quantite'] * vente['prix_unitaire']
        ventes_par_vendeur[vendeur]['quantite'] += vente['quantite']
        ventes_par_vendeur[vendeur]['chiffre'] += chiffre

    # Affichage des résultats
    print("=== ANALYSE DES VENTES ===")
    print(f"Chiffre d'affaires total: {total_ventes:.2f}€")
    print(f"Quantité totale vendue: {total_quantite}")
    print(f"Nombre de transactions: {len(ventes)}")

    print("\n=== TOP PRODUITS ===")
    produits_tries = sorted(ventes_par_produit.items(),
                           key=lambda x: x[1]['chiffre'], reverse=True)
    for produit, stats in produits_tries[:5]:
        print(f"{produit}: {stats['quantite']} unités, {stats['chiffre']:.2f}€")

    print("\n=== PERFORMANCE VENDEURS ===")
    vendeurs_tries = sorted(ventes_par_vendeur.items(),
                           key=lambda x: x[1]['chiffre'], reverse=True)
    for vendeur, stats in vendeurs_tries:
        print(f"{vendeur}: {stats['quantite']} unités, {stats['chiffre']:.2f}€")

# Création d'un fichier de test
def creer_fichier_test():
    ventes_test = [
        ['date', 'produit', 'quantite', 'prix_unitaire', 'vendeur'],
        ['2024-01-15', 'Laptop', '2', '999.99', 'Alice'],
        ['2024-01-15', 'Souris', '5', '29.99', 'Bob'],
        ['2024-01-16', 'Clavier', '3', '79.99', 'Alice'],
        ['2024-01-16', 'Laptop', '1', '999.99', 'Charlie'],
        ['2024-01-17', 'Souris', '8', '29.99', 'Bob'],
        ['2024-01-17', 'Écran', '2', '299.99', 'Charlie'],
    ]

    with open('ventes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(ventes_test)

    print("Fichier de test créé!")

# Test
creer_fichier_test()
analyser_ventes('ventes.csv')
```

## Bonnes pratiques

### 1. Validation des données

```python
import json

def valider_donnees_json(donnees, schema):
    """Valide les données selon un schéma simple"""
    for cle, type_attendu in schema.items():
        if cle not in donnees:
            return False, f"Clé manquante: {cle}"
        if not isinstance(donnees[cle], type_attendu):
            return False, f"Type incorrect pour {cle}: attendu {type_attendu.__name__}"
    return True, "Validation réussie"

# Exemple d'utilisation
schema_utilisateur = {
    "nom": str,
    "age": int,
    "email": str,
    "actif": bool
}

# Test avec des données valides
utilisateur_valide = {
    "nom": "Alice",
    "age": 30,
    "email": "alice@email.com",
    "actif": True
}

valide, message = valider_donnees_json(utilisateur_valide, schema_utilisateur)
print(f"Validation: {message}")

# Test avec des données invalides
utilisateur_invalide = {
    "nom": "Bob",
    "age": "trente",  # Erreur: devrait être un int
    "email": "bob@email.com"
    # Erreur: clé "actif" manquante
}

valide, message = valider_donnees_json(utilisateur_invalide, schema_utilisateur)
print(f"Validation: {message}")
```

### 2. Gestion robuste des erreurs

```python
import json
import csv
import xml.etree.ElementTree as ET
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def lire_fichier_robuste(fichier, format_fichier):
    """Lecture robuste avec gestion d'erreurs complète"""
    try:
        if format_fichier.lower() == 'json':
            with open(fichier, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
                logging.info(f"Fichier JSON {fichier} lu avec succès")
                return donnees

        elif format_fichier.lower() == 'csv':
            donnees = []
            with open(fichier, 'r', encoding='utf-8') as f:
                lecteur = csv.DictReader(f)
                for ligne in lecteur:
                    donnees.append(ligne)
                logging.info(f"Fichier CSV {fichier} lu avec succès ({len(donnees)} lignes)")
                return donnees

        elif format_fichier.lower() == 'xml':
            tree = ET.parse(fichier)
            root = tree.getroot()
            logging.info(f"Fichier XML {fichier} lu avec succès")
            return root

        else:
            raise ValueError(f"Format {format_fichier} non supporté")

    except FileNotFoundError:
        logging.error(f"Fichier {fichier} non trouvé")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Erreur JSON dans {fichier}: {e}")
        return None
    except csv.Error as e:
        logging.error(f"Erreur CSV dans {fichier}: {e}")
        return None
    except ET.ParseError as e:
        logging.error(f"Erreur XML dans {fichier}: {e}")
        return None
    except UnicodeDecodeError as e:
        logging.error(f"Erreur d'encodage dans {fichier}: {e}")
        return None
    except Exception as e:
        logging.error(f"Erreur inattendue avec {fichier}: {e}")
        return None

# Utilisation
donnees_json = lire_fichier_robuste('config.json', 'json')
donnees_csv = lire_fichier_robuste('ventes.csv', 'csv')
donnees_xml = lire_fichier_robuste('catalogue.xml', 'xml')
```

### 3. Optimisation des performances

```python
import json
import csv
from typing import Generator, Dict, Any

def lire_gros_json_par_chunks(fichier: str, taille_chunk: int = 1000) -> Generator[Dict[str, Any], None, None]:
    """Lecture d'un gros fichier JSON ligne par ligne (JSON Lines format)"""
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            chunk = []
            for ligne in f:
                try:
                    objet = json.loads(ligne.strip())
                    chunk.append(objet)

                    if len(chunk) >= taille_chunk:
                        yield chunk
                        chunk = []
                except json.JSONDecodeError:
                    continue  # Ignore les lignes malformées

            # Yield du dernier chunk s'il n'est pas vide
            if chunk:
                yield chunk

    except FileNotFoundError:
        print(f"Fichier {fichier} non trouvé")

def traiter_gros_csv(fichier: str, fonction_traitement) -> None:
    """Traite un gros fichier CSV ligne par ligne pour économiser la mémoire"""
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)

            for numero_ligne, ligne in enumerate(lecteur, 1):
                try:
                    fonction_traitement(ligne, numero_ligne)
                except Exception as e:
                    print(f"Erreur ligne {numero_ligne}: {e}")
                    continue

                # Affichage du progrès
                if numero_ligne % 10000 == 0:
                    print(f"Traité {numero_ligne} lignes...")

    except FileNotFoundError:
        print(f"Fichier {fichier} non trouvé")

# Exemple d'utilisation pour gros fichiers
def analyser_ligne_vente(ligne, numero):
    """Fonction de traitement pour chaque ligne de vente"""
    try:
        montant = float(ligne['montant'])
        if montant > 1000:
            print(f"Ligne {numero}: Grosse vente de {montant}€")
    except ValueError:
        print(f"Ligne {numero}: Montant invalide")

# Utilisation
# traiter_gros_csv('gros_fichier_ventes.csv', analyser_ligne_vente)
```

### 4. Sécurité et validation avancée

```python
import json
import re
from datetime import datetime
from typing import Any, Dict, List, Union

class ValidateurDonnees:
    """Classe pour valider des données selon des règles personnalisées"""

    @staticmethod
    def valider_email(email: str) -> bool:
        """Valide un format d'email basique"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def valider_telephone(telephone: str) -> bool:
        """Valide un numéro de téléphone français"""
        # Enlève tous les espaces, points, tirets
        tel_nettoye = re.sub(r'[\s\.\-]', '', telephone)
        # Vérifie le format français
        pattern = r'^(?:\+33|0)[1-9](?:[0-9]{8})$'
        return bool(re.match(pattern, tel_nettoye))

    @staticmethod
    def valider_date(date_str: str, format_date: str = '%Y-%m-%d') -> bool:
        """Valide une date selon un format donné"""
        try:
            datetime.strptime(date_str, format_date)
            return True
        except ValueError:
            return False

    @staticmethod
    def valider_range_numerique(valeur: Union[int, float], min_val: float = None, max_val: float = None) -> bool:
        """Valide qu'une valeur numérique est dans une plage"""
        if min_val is not None and valeur < min_val:
            return False
        if max_val is not None and valeur > max_val:
            return False
        return True

def valider_donnees_avancees(donnees: Dict[str, Any], regles: Dict[str, Dict]) -> tuple[bool, List[str]]:
    """
    Valide des données selon des règles avancées

    regles = {
        'nom_champ': {
            'type': type_attendu,
            'obligatoire': bool,
            'validateur': fonction_validation,
            'min': valeur_min,
            'max': valeur_max
        }
    }
    """
    erreurs = []

    for champ, regles_champ in regles.items():
        valeur = donnees.get(champ)

        # Vérification obligatoire
        if regles_champ.get('obligatoire', False) and valeur is None:
            erreurs.append(f"Champ obligatoire manquant: {champ}")
            continue

        # Si le champ n'est pas obligatoire et est None, on passe
        if valeur is None:
            continue

        # Vérification du type
        type_attendu = regles_champ.get('type')
        if type_attendu and not isinstance(valeur, type_attendu):
            erreurs.append(f"Type incorrect pour {champ}: attendu {type_attendu.__name__}, reçu {type(valeur).__name__}")
            continue

        # Validation personnalisée
        validateur = regles_champ.get('validateur')
        if validateur and not validateur(valeur):
            erreurs.append(f"Validation échouée pour {champ}: {valeur}")

        # Validation de plage pour les nombres
        if isinstance(valeur, (int, float)):
            min_val = regles_champ.get('min')
            max_val = regles_champ.get('max')
            if not ValidateurDonnees.valider_range_numerique(valeur, min_val, max_val):
                erreurs.append(f"Valeur hors plage pour {champ}: {valeur} (min: {min_val}, max: {max_val})")

        # Validation de longueur pour les chaînes
        if isinstance(valeur, str):
            min_len = regles_champ.get('min_length')
            max_len = regles_champ.get('max_length')
            if min_len and len(valeur) < min_len:
                erreurs.append(f"Longueur insuffisante pour {champ}: {len(valeur)} < {min_len}")
            if max_len and len(valeur) > max_len:
                erreurs.append(f"Longueur excessive pour {champ}: {len(valeur)} > {max_len}")

    return len(erreurs) == 0, erreurs

# Exemple d'utilisation avancée
regles_utilisateur = {
    'nom': {
        'type': str,
        'obligatoire': True,
        'min_length': 2,
        'max_length': 50
    },
    'email': {
        'type': str,
        'obligatoire': True,
        'validateur': ValidateurDonnees.valider_email
    },
    'age': {
        'type': int,
        'obligatoire': True,
        'min': 0,
        'max': 120
    },
    'telephone': {
        'type': str,
        'obligatoire': False,
        'validateur': ValidateurDonnees.valider_telephone
    },
    'date_inscription': {
        'type': str,
        'obligatoire': True,
        'validateur': lambda x: ValidateurDonnees.valider_date(x, '%Y-%m-%d')
    }
}

# Test avec des données
utilisateur_test = {
    'nom': 'Alice Dupont',
    'email': 'alice@email.com',
    'age': 30,
    'telephone': '01.23.45.67.89',
    'date_inscription': '2024-01-15'
}

valide, erreurs = valider_donnees_avancees(utilisateur_test, regles_utilisateur)
if valide:
    print("✅ Données valides!")
else:
    print("❌ Erreurs de validation:")
    for erreur in erreurs:
        print(f"  - {erreur}")
```

### 5. Nettoyage et normalisation des données

```python
import csv
import json
import re
from typing import Dict, Any, List

class NettoyeurDonnees:
    """Classe utilitaire pour nettoyer et normaliser les données"""

    @staticmethod
    def nettoyer_chaine(texte: str) -> str:
        """Nettoie une chaîne de caractères"""
        if not isinstance(texte, str):
            return str(texte)

        # Supprime les espaces en début/fin
        texte = texte.strip()

        # Supprime les espaces multiples
        texte = re.sub(r'\s+', ' ', texte)

        # Supprime les caractères de contrôle
        texte = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', texte)

        return texte

    @staticmethod
    def normaliser_telephone(telephone: str) -> str:
        """Normalise un numéro de téléphone au format français"""
        if not telephone:
            return ""

        # Supprime tout sauf les chiffres et le +
        telephone = re.sub(r'[^\d+]', '', telephone)

        # Convertit +33 en 0
        if telephone.startswith('+33'):
            telephone = '0' + telephone[3:]

        # Formate en 01.23.45.67.89
        if len(telephone) == 10 and telephone.startswith('0'):
            return '.'.join([telephone[i:i+2] for i in range(0, 10, 2)])

        return telephone  # Retourne tel quel si pas au bon format

    @staticmethod
    def normaliser_email(email: str) -> str:
        """Normalise une adresse email"""
        if not email:
            return ""

        email = email.strip().lower()

        # Validation basique
        if '@' not in email:
            return email

        return email

    @staticmethod
    def convertir_type_securise(valeur: str, type_cible: type):
        """Convertit une valeur vers un type avec gestion d'erreurs"""
        if not valeur or valeur.strip() == "":
            return None

        try:
            if type_cible == int:
                # Gère les nombres avec des espaces ou des virgules
                valeur_nettoyee = re.sub(r'[^\d-]', '', valeur)
                return int(valeur_nettoyee) if valeur_nettoyee else None

            elif type_cible == float:
                # Gère les nombres avec virgule décimale française
                valeur_nettoyee = valeur.replace(',', '.').replace(' ', '')
                valeur_nettoyee = re.sub(r'[^\d.-]', '', valeur_nettoyee)
                return float(valeur_nettoyee) if valeur_nettoyee else None

            elif type_cible == bool:
                valeur_lower = valeur.lower().strip()
                if valeur_lower in ['true', 'vrai', 'oui', '1', 'yes']:
                    return True
                elif valeur_lower in ['false', 'faux', 'non', '0', 'no']:
                    return False
                return None

            else:
                return type_cible(valeur)

        except (ValueError, TypeError):
            return None

def nettoyer_donnees_csv(fichier_entree: str, fichier_sortie: str, regles_nettoyage: Dict[str, Dict]) -> None:
    """
    Nettoie un fichier CSV selon des règles données

    regles_nettoyage = {
        'nom_colonne': {
            'type': type_cible,
            'nettoyeur': fonction_nettoyage,
            'obligatoire': bool
        }
    }
    """
    donnees_nettoyees = []
    erreurs = []

    try:
        with open(fichier_entree, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)

            for numero_ligne, ligne in enumerate(lecteur, 1):
                ligne_nettoyee = {}
                ligne_valide = True

                for colonne, valeur in ligne.items():
                    if colonne in regles_nettoyage:
                        regles = regles_nettoyage[colonne]

                        # Application du nettoyeur personnalisé
                        nettoyeur = regles.get('nettoyeur')
                        if nettoyeur:
                            valeur = nettoyeur(valeur)

                        # Conversion de type
                        type_cible = regles.get('type', str)
                        if type_cible != str:
                            valeur = NettoyeurDonnees.convertir_type_securise(valeur, type_cible)
                        else:
                            valeur = NettoyeurDonnees.nettoyer_chaine(valeur)

                        # Vérification obligatoire
                        if regles.get('obligatoire', False) and valeur is None:
                            erreurs.append(f"Ligne {numero_ligne}: Valeur obligatoire manquante pour {colonne}")
                            ligne_valide = False
                            continue

                        ligne_nettoyee[colonne] = valeur
                    else:
                        # Nettoyage basique pour les colonnes sans règles
                        ligne_nettoyee[colonne] = NettoyeurDonnees.nettoyer_chaine(valeur)

                if ligne_valide:
                    donnees_nettoyees.append(ligne_nettoyee)

    except FileNotFoundError:
        print(f"Fichier {fichier_entree} non trouvé")
        return

    # Sauvegarde des données nettoyées
    if donnees_nettoyees:
        with open(fichier_sortie, 'w', newline='', encoding='utf-8') as f:
            colonnes = donnees_nettoyees[0].keys()
            writer = csv.DictWriter(f, fieldnames=colonnes)
            writer.writeheader()
            writer.writerows(donnees_nettoyees)

        print(f"✅ Nettoyage terminé: {len(donnees_nettoyees)} lignes sauvegardées dans {fichier_sortie}")

    # Affichage des erreurs
    if erreurs:
        print(f"❌ {len(erreurs)} erreurs détectées:")
        for erreur in erreurs[:10]:  # Affiche seulement les 10 premières
            print(f"  - {erreur}")

# Exemple d'utilisation
regles_employes = {
    'nom': {
        'type': str,
        'nettoyeur': NettoyeurDonnees.nettoyer_chaine,
        'obligatoire': True
    },
    'email': {
        'type': str,
        'nettoyeur': NettoyeurDonnees.normaliser_email,
        'obligatoire': True
    },
    'telephone': {
        'type': str,
        'nettoyeur': NettoyeurDonnees.normaliser_telephone,
        'obligatoire': False
    },
    'salaire': {
        'type': float,
        'obligatoire': True
    },
    'age': {
        'type': int,
        'obligatoire': True
    }
}

# Utilisation
# nettoyer_donnees_csv('employes_bruts.csv', 'employes_nettoyes.csv', regles_employes)
```

### 6. Sauvegarde et versioning des données

```python
import json
import csv
import shutil
from datetime import datetime
import os
from pathlib import Path

class GestionnaireSauvegarde:
    """Gestionnaire pour sauvegardes automatiques avec versioning"""

    def __init__(self, dossier_sauvegarde: str = "sauvegardes"):
        self.dossier_sauvegarde = Path(dossier_sauvegarde)
        self.dossier_sauvegarde.mkdir(exist_ok=True)

    def creer_nom_fichier_version(self, nom_base: str) -> str:
        """Crée un nom de fichier avec timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom, extension = os.path.splitext(nom_base)
        return f"{nom}_{timestamp}{extension}"

    def sauvegarder_json(self, donnees: dict, nom_fichier: str, garder_versions: int = 5) -> str:
        """Sauvegarde des données JSON avec versioning"""
        # Nom du fichier avec version
        nom_version = self.creer_nom_fichier_version(nom_fichier)
        chemin_sauvegarde = self.dossier_sauvegarde / nom_version

        try:
            with open(chemin_sauvegarde, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)

            print(f"✅ Sauvegarde JSON: {chemin_sauvegarde}")

            # Nettoyage des anciennes versions
            self.nettoyer_anciennes_versions(nom_fichier, garder_versions)

            return str(chemin_sauvegarde)

        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return None

    def sauvegarder_csv(self, donnees: list, nom_fichier: str, garder_versions: int = 5) -> str:
        """Sauvegarde des données CSV avec versioning"""
        if not donnees:
            print("Aucune donnée à sauvegarder")
            return None

        nom_version = self.creer_nom_fichier_version(nom_fichier)
        chemin_sauvegarde = self.dossier_sauvegarde / nom_version

        try:
            with open(chemin_sauvegarde, 'w', newline='', encoding='utf-8') as f:
                if isinstance(donnees[0], dict):
                    # Données sous forme de dictionnaires
                    colonnes = donnees[0].keys()
                    writer = csv.DictWriter(f, fieldnames=colonnes)
                    writer.writeheader()
                    writer.writerows(donnees)
                else:
                    # Données sous forme de listes
                    writer = csv.writer(f)
                    writer.writerows(donnees)

            print(f"✅ Sauvegarde CSV: {chemin_sauvegarde}")

            # Nettoyage des anciennes versions
            self.nettoyer_anciennes_versions(nom_fichier, garder_versions)

            return str(chemin_sauvegarde)

        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return None

    def nettoyer_anciennes_versions(self, nom_base: str, garder: int) -> None:
        """Supprime les anciennes versions en gardant seulement les N plus récentes"""
        nom, extension = os.path.splitext(nom_base)
        pattern = f"{nom}_*{extension}"

        # Trouve tous les fichiers correspondant au pattern
        fichiers_versions = list(self.dossier_sauvegarde.glob(pattern))

        if len(fichiers_versions) > garder:
            # Trie par date de modification (plus récent en premier)
            fichiers_versions.sort(key=lambda x: x.stat().st_mtime, reverse=True)

            # Supprime les anciens fichiers
            for fichier_ancien in fichiers_versions[garder:]:
                try:
                    fichier_ancien.unlink()
                    print(f"🗑️ Ancienne version supprimée: {fichier_ancien.name}")
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression de {fichier_ancien}: {e}")

    def lister_versions(self, nom_base: str) -> list:
        """Liste toutes les versions d'un fichier"""
        nom, extension = os.path.splitext(nom_base)
        pattern = f"{nom}_*{extension}"

        fichiers_versions = list(self.dossier_sauvegarde.glob(pattern))
        fichiers_versions.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        versions = []
        for fichier in fichiers_versions:
            stat = fichier.stat()
            versions.append({
                'nom': fichier.name,
                'chemin': str(fichier),
                'taille': stat.st_size,
                'date_modification': datetime.fromtimestamp(stat.st_mtime)
            })

        return versions

    def restaurer_version(self, nom_version: str, nom_destination: str) -> bool:
        """Restaure une version spécifique"""
        chemin_source = self.dossier_sauvegarde / nom_version

        if not chemin_source.exists():
            print(f"❌ Version {nom_version} non trouvée")
            return False

        try:
            shutil.copy2(chemin_source, nom_destination)
            print(f"✅ Version restaurée: {nom_version} → {nom_destination}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la restauration: {e}")
            return False

# Exemple d'utilisation
def exemple_gestionnaire_sauvegarde():
    # Initialisation
    gestionnaire = GestionnaireSauvegarde("mes_sauvegardes")

    # Données d'exemple
    config = {
        "version": "2.1",
        "database": {
            "host": "localhost",
            "port": 5432
        },
        "features": ["auth", "logging", "cache"]
    }

    employes = [
        {"nom": "Alice", "poste": "Dev", "salaire": 45000},
        {"nom": "Bob", "poste": "Designer", "salaire": 38000},
        {"nom": "Charlie", "poste": "Manager", "salaire": 55000}
    ]

    # Sauvegardes
    gestionnaire.sauvegarder_json(config, "config.json", garder_versions=3)
    gestionnaire.sauvegarder_csv(employes, "employes.csv", garder_versions=3)

    # Liste des versions
    print("\n=== Versions de config.json ===")
    versions_config = gestionnaire.lister_versions("config.json")
    for version in versions_config:
        print(f"- {version['nom']} ({version['date_modification']}) - {version['taille']} bytes")

    # Exemple de restauration
    if versions_config:
        premiere_version = versions_config[0]['nom']
        gestionnaire.restaurer_version(premiere_version, "config_restaure.json")

# Utilisation
# exemple_gestionnaire_sauvegarde()
```

## Résumé des bonnes pratiques

### ✅ À faire

1. **Toujours valider les données** avant traitement
2. **Gérer les erreurs** de façon robuste
3. **Spécifier l'encodage** (UTF-8 recommandé)
4. **Nettoyer les données** lors de l'import
5. **Sauvegarder avec versioning** pour éviter les pertes
6. **Utiliser des schémas** pour valider la structure
7. **Logger les opérations** importantes
8. **Traiter les gros fichiers** par chunks

### ❌ À éviter

1. **Ne pas valider** les données d'entrée
2. **Ignorer les erreurs** d'encodage
3. **Charger de gros fichiers** entièrement en mémoire
4. **Oublier de fermer** les fichiers (utiliser `with`)
5. **Ne pas gérer** les cas d'erreur
6. **Mélanger les formats** sans conversion appropriée
7. **Stocker des mots de passe** en clair dans les JSON
8. **Ne pas documenter** la structure des données

Cette section vous a montré comment implémenter des pratiques robustes pour la manipulation des formats de données. La prochaine section abordera la sérialisation avec pickle pour sauvegarder des objets Python complexes.

⏭️
