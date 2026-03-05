🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.2 Formats de Données (JSON, CSV, XML)

## Introduction

Les données que nous manipulons en programmation doivent souvent être **sauvegardées**, **échangées** ou **partagées** entre différents programmes ou systèmes. Pour cela, on utilise des **formats de données standardisés** qui permettent de structurer l'information de manière claire et universelle.

Dans ce chapitre, nous allons découvrir les trois formats les plus courants :

- **JSON** (JavaScript Object Notation) : format léger et moderne, très utilisé dans les API web
- **CSV** (Comma-Separated Values) : format tabulaire simple, idéal pour les tableurs
- **XML** (eXtensible Markup Language) : format structuré et verbeux, encore utilisé dans certains systèmes

---

## JSON (JavaScript Object Notation)

### Qu'est-ce que le JSON ?

JSON est un format de données **léger** et **facile à lire** pour les humains comme pour les machines. Il est devenu le standard pour l'échange de données sur le web.

### Structure d'un fichier JSON

Voici à quoi ressemble un fichier JSON :

```json
{
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 28,
    "ville": "Paris",
    "competences": ["Python", "JavaScript", "SQL"],
    "actif": true,
    "adresse": {
        "rue": "12 rue de la Paix",
        "code_postal": "75002"
    }
}
```

**Types de données supportés :**
- Chaînes de caractères (entre guillemets)
- Nombres (entiers ou décimaux)
- Booléens (`true` ou `false`)
- Listes (entre crochets `[]`)
- Objets/dictionnaires (entre accolades `{}`)
- `null` (valeur nulle)

### Le Module `json` en Python

Python dispose d'un module intégré pour travailler avec JSON :

```python
import json
```

### Lire un fichier JSON

```python
import json

# Ouvrir et lire un fichier JSON
with open('personne.json', 'r', encoding='utf-8') as fichier:
    donnees = json.load(fichier)

# Accéder aux données
print(donnees['nom'])           # Dupont  
print(donnees['age'])            # 28  
print(donnees['competences'])    # ['Python', 'JavaScript', 'SQL']  
print(donnees['adresse']['rue'])     # 12 rue de la Paix  
```

**Note :** `json.load()` lit directement depuis un fichier et retourne un dictionnaire Python.

### Écrire dans un fichier JSON

```python
import json

# Données Python (dictionnaire)
personne = {
    "nom": "Martin",
    "prenom": "Lucas",
    "age": 35,
    "ville": "Lyon",
    "competences": ["Python", "Django", "PostgreSQL"],
    "actif": True
}

# Sauvegarder dans un fichier JSON
with open('nouvelle_personne.json', 'w', encoding='utf-8') as fichier:
    json.dump(personne, fichier, indent=4, ensure_ascii=False)

print("Fichier JSON créé avec succès !")
```

**Paramètres importants de `json.dump()` :**
- `indent=4` : rend le JSON lisible avec une indentation de 4 espaces
- `ensure_ascii=False` : permet de garder les accents et caractères spéciaux

### Convertir entre Python et JSON (sans fichier)

#### Python → JSON (chaîne de caractères)

```python
import json

data = {"nom": "Alice", "age": 30}

# Convertir en chaîne JSON
json_string = json.dumps(data, indent=2)  
print(json_string)  
print(type(json_string))  # <class 'str'>  
```

#### JSON → Python

```python
import json

json_string = '{"nom": "Bob", "age": 25}'

# Convertir en dictionnaire Python
data = json.loads(json_string)  
print(data)  
print(type(data))  # <class 'dict'>  
```

**Résumé des fonctions :**
- `json.load()` : lit depuis un **fichier**
- `json.loads()` : lit depuis une **chaîne de caractères** (s = string)
- `json.dump()` : écrit dans un **fichier**
- `json.dumps()` : écrit dans une **chaîne de caractères**

### Exemple : Liste de personnes

```python
import json

# Liste de dictionnaires
personnes = [
    {"nom": "Dupont", "age": 30, "ville": "Paris"},
    {"nom": "Martin", "age": 25, "ville": "Lyon"},
    {"nom": "Bernard", "age": 35, "ville": "Marseille"}
]

# Sauvegarder
with open('personnes.json', 'w', encoding='utf-8') as f:
    json.dump(personnes, f, indent=4, ensure_ascii=False)

# Relire
with open('personnes.json', 'r', encoding='utf-8') as f:
    personnes_lues = json.load(f)

# Parcourir les données
for personne in personnes_lues:
    print(f"{personne['nom']} a {personne['age']} ans")
```

### Gestion des erreurs JSON

```python
import json

try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Le fichier n'existe pas")
except json.JSONDecodeError as e:
    print(f"Erreur de format JSON : {e}")
```

---

## CSV (Comma-Separated Values)

### Qu'est-ce que le CSV ?

CSV est un format de fichier **tabulaire** (comme un tableau) où les valeurs sont séparées par des virgules (ou parfois des points-virgules). C'est le format favori des tableurs comme Excel ou Google Sheets.

### Structure d'un fichier CSV

Exemple de fichier `employes.csv` :

```csv
nom,prenom,age,salaire,service  
Dupont,Marie,28,35000,Informatique  
Martin,Pierre,35,42000,Marketing  
Bernard,Sophie,32,38000,Informatique  
```

**Caractéristiques :**
- La première ligne contient souvent les **en-têtes** (noms des colonnes)
- Chaque ligne suivante représente une **entrée**
- Les valeurs sont séparées par des virgules (ou `;` en France)

### Le Module `csv` en Python

```python
import csv
```

### Lire un fichier CSV

#### Méthode 1 : Avec `csv.reader()`

```python
import csv

with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier)

    # Lire l'en-tête
    entetes = next(lecteur)
    print("Colonnes :", entetes)

    # Lire les données
    for ligne in lecteur:
        nom = ligne[0]
        prenom = ligne[1]
        age = ligne[2]
        print(f"{prenom} {nom} - {age} ans")
```

#### Méthode 2 : Avec `csv.DictReader()` (recommandé)

Cette méthode est plus pratique car elle retourne des dictionnaires :

```python
import csv

with open('employes.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.DictReader(fichier)

    for ligne in lecteur:
        # On accède par nom de colonne
        print(f"{ligne['prenom']} {ligne['nom']}")
        print(f"  Âge: {ligne['age']} ans")
        print(f"  Salaire: {ligne['salaire']} €")
        print(f"  Service: {ligne['service']}")
        print()
```

### Écrire dans un fichier CSV

#### Méthode 1 : Avec `csv.writer()`

```python
import csv

donnees = [
    ['nom', 'prenom', 'age'],
    ['Dubois', 'Jean', '40'],
    ['Petit', 'Claire', '29'],
    ['Roux', 'Thomas', '33']
]

with open('nouveau_fichier.csv', 'w', encoding='utf-8', newline='') as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(donnees)  # Écrire toutes les lignes

print("Fichier CSV créé !")
```

**Note :** Le paramètre `newline=''` évite des lignes vides sur Windows.

#### Méthode 2 : Avec `csv.DictWriter()` (recommandé)

```python
import csv

employes = [
    {'nom': 'Durand', 'prenom': 'Alice', 'age': 30, 'service': 'RH'},
    {'nom': 'Moreau', 'prenom': 'Bob', 'age': 27, 'service': 'Finance'},
    {'nom': 'Simon', 'prenom': 'Clara', 'age': 31, 'service': 'IT'}
]

with open('employes_nouveaux.csv', 'w', encoding='utf-8', newline='') as fichier:
    colonnes = ['nom', 'prenom', 'age', 'service']
    ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)

    # Écrire l'en-tête
    ecrivain.writeheader()

    # Écrire les données
    ecrivain.writerows(employes)

print("Fichier CSV avec dictionnaires créé !")
```

### Gérer différents délimiteurs

En France, on utilise souvent le point-virgule `;` comme délimiteur :

```python
import csv

# Lire avec point-virgule
with open('donnees_fr.csv', 'r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier, delimiter=';')
    for ligne in lecteur:
        print(ligne)

# Écrire avec point-virgule
with open('export_fr.csv', 'w', encoding='utf-8', newline='') as fichier:
    ecrivain = csv.writer(fichier, delimiter=';')
    ecrivain.writerow(['Nom', 'Ville', 'Population'])
    ecrivain.writerow(['Paris', 'France', '2200000'])
```

### Exemple complet : Filtrer et exporter

```python
import csv

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
```

---

## XML (eXtensible Markup Language)

### Qu'est-ce que le XML ?

XML est un format de données **structuré** qui utilise des **balises** (comme HTML). Il est plus verbeux que JSON mais offre plus de flexibilité pour représenter des données complexes.

### Structure d'un fichier XML

Exemple de fichier `bibliotheque.xml` :

```xml
<?xml version="1.0" encoding="UTF-8"?>
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
</bibliotheque>
```

**Caractéristiques :**
- Balises ouvrantes et fermantes : `<titre>...</titre>`
- Attributs : `id="1"`
- Structure hiérarchique (arborescente)

### Le Module `xml.etree.ElementTree`

Python dispose d'un module intégré pour manipuler XML :

```python
import xml.etree.ElementTree as ET
```

### Lire un fichier XML

```python
import xml.etree.ElementTree as ET

# Charger le fichier XML
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
    print(f"  Prix: {prix} €")
```

### Créer et écrire un fichier XML

```python
import xml.etree.ElementTree as ET

# Créer l'élément racine
bibliotheque = ET.Element('bibliotheque')

# Créer le premier livre
livre1 = ET.SubElement(bibliotheque, 'livre')  
livre1.set('id', '1')  # Ajouter un attribut  

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
ET.indent(arbre, space='    ')  # Python 3.9+, pour l'indentation  
arbre.write('nouvelle_bibliotheque.xml', encoding='utf-8', xml_declaration=True)  

print("Fichier XML créé !")
```

### Modifier un fichier XML existant

```python
import xml.etree.ElementTree as ET

# Charger le fichier
arbre = ET.parse('bibliotheque.xml')  
racine = arbre.getroot()  

# Trouver un livre spécifique et modifier son prix
for livre in racine.findall('livre'):
    titre = livre.find('titre').text
    if 'Python' in titre:
        prix = livre.find('prix')
        ancien_prix = prix.text
        prix.text = '24.99'
        print(f"Prix modifié : {ancien_prix} → {prix.text}")

# Sauvegarder les modifications
arbre.write('bibliotheque_modifiee.xml', encoding='utf-8', xml_declaration=True)
```

### Rechercher des éléments avec XPath

```python
import xml.etree.ElementTree as ET

arbre = ET.parse('bibliotheque.xml')  
racine = arbre.getroot()  

# Trouver tous les titres
titres = racine.findall('.//titre')  
for titre in titres:  
    print(titre.text)

# Trouver les livres de 2024
livres_2024 = racine.findall(".//livre[annee='2024']")  
print(f"\n{len(livres_2024)} livres de 2024")  
```

### Exemple : Parser un flux RSS (XML)

```python
import xml.etree.ElementTree as ET

# Exemple de flux RSS simplifié
xml_content = """
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

# Parser le XML
racine = ET.fromstring(xml_content)

# Extraire les articles
for item in racine.findall('.//item'):
    titre = item.find('title').text
    lien = item.find('link').text
    description = item.find('description').text

    print(f"📰 {titre}")
    print(f"   {lien}")
    print(f"   {description}\n")
```

---

## Comparaison des Formats

### Tableau comparatif

| Critère | JSON | CSV | XML |
|---------|------|-----|-----|
| **Lisibilité** | ⭐⭐⭐⭐ Excellente | ⭐⭐⭐⭐⭐ Très simple | ⭐⭐ Verbeux |
| **Taille fichier** | ⭐⭐⭐⭐ Compact | ⭐⭐⭐⭐⭐ Très compact | ⭐⭐ Volumineux |
| **Structure** | Hiérarchique | Tabulaire | Hiérarchique |
| **Types de données** | Oui | Non (tout en texte) | Non (tout en texte) |
| **Usage web** | ⭐⭐⭐⭐⭐ Standard | ⭐⭐ Rare | ⭐⭐⭐ Courant |
| **Tableurs** | ⭐⭐ Possible | ⭐⭐⭐⭐⭐ Natif | ⭐ Difficile |

### Quand utiliser chaque format ?

#### JSON
**À utiliser pour :**
- APIs web et services REST
- Configuration d'applications
- Données structurées avec hiérarchie
- Échange de données entre systèmes modernes

**Exemple d'usage :** Configuration d'une application, données d'une API météo

#### CSV
**À utiliser pour :**
- Données tabulaires simples
- Export/import vers des tableurs (Excel, Google Sheets)
- Gros volumes de données simples
- Logs et données de capteurs

**Exemple d'usage :** Liste de clients, données de ventes, résultats de mesures

#### XML
**À utiliser pour :**
- Documents structurés complexes
- Systèmes legacy (anciens)
- Flux RSS/Atom
- Configurations complexes

**Exemple d'usage :** Flux RSS, documents techniques, échange B2B

---

## Exemple Pratique : Conversion entre Formats

### CSV → JSON

```python
import csv  
import json  

# Lire le CSV
employes = []  
with open('employes.csv', 'r', encoding='utf-8') as fichier:  
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        employes.append(ligne)

# Écrire en JSON
with open('employes.json', 'w', encoding='utf-8') as fichier:
    json.dump(employes, fichier, indent=4, ensure_ascii=False)

print("Conversion CSV → JSON terminée")
```

### JSON → CSV

```python
import json  
import csv  

# Lire le JSON
with open('employes.json', 'r', encoding='utf-8') as fichier:
    employes = json.load(fichier)

# Écrire en CSV
with open('employes_export.csv', 'w', encoding='utf-8', newline='') as fichier:
    if employes:
        colonnes = employes[0].keys()
        ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)
        ecrivain.writeheader()
        ecrivain.writerows(employes)

print("Conversion JSON → CSV terminée")
```

### XML → JSON

```python
import xml.etree.ElementTree as ET  
import json  

# Lire le XML
arbre = ET.parse('bibliotheque.xml')  
racine = arbre.getroot()  

# Convertir en dictionnaires
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

# Sauvegarder en JSON
with open('bibliotheque.json', 'w', encoding='utf-8') as fichier:
    json.dump({'livres': livres}, fichier, indent=4, ensure_ascii=False)

print("Conversion XML → JSON terminée")
```

---

## Bonnes Pratiques

### 1. Toujours spécifier l'encodage

```python
# ✅ Bon
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ❌ À éviter
with open('data.json', 'r') as f:
    data = json.load(f)
```

### 2. Gérer les erreurs

```python
import json

try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Fichier non trouvé")
    config = {}  # Configuration par défaut
except json.JSONDecodeError:
    print("Format JSON invalide")
    config = {}
```

### 3. Valider les données

```python
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Vérifier que les clés attendues existent
if 'database' in config and 'port' in config:
    print("Configuration valide")
else:
    print("Configuration incomplète")
```

### 4. CSV : Utiliser DictReader/DictWriter

```python
# ✅ Bon - Plus lisible
with open('data.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['nom'])

# ❌ Moins bon - Indices numériques
with open('data.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row[0])  # Quelle colonne ?
```

### 5. Indenter le JSON pour la lisibilité

```python
# ✅ Bon - Lisible
json.dump(data, f, indent=4, ensure_ascii=False)

# ❌ Fonctionnel mais illisible
json.dump(data, f)
```

---

## Résumé

### Fonctions principales

#### JSON
```python
import json

# Fichiers
json.load(fichier)      # Lire depuis un fichier  
json.dump(data, fichier) # Écrire dans un fichier  

# Chaînes
json.loads(string)      # Parser une chaîne JSON  
json.dumps(data)        # Convertir en chaîne JSON  
```

#### CSV
```python
import csv

# Lecture
csv.reader(fichier)           # Liste de listes  
csv.DictReader(fichier)       # Liste de dictionnaires  

# Écriture
csv.writer(fichier)           # Écrire des listes  
csv.DictWriter(fichier, ...)  # Écrire des dictionnaires  
```

#### XML
```python
import xml.etree.ElementTree as ET

# Lecture
ET.parse('fichier.xml')       # Parser un fichier  
ET.fromstring(string)         # Parser une chaîne  

# Recherche
racine.find('balise')         # Trouver un élément  
racine.findall('balise')      # Trouver tous les éléments  

# Écriture
arbre.write('fichier.xml')    # Sauvegarder
```

### Points clés

✅ **JSON** est le format moderne pour les APIs et configurations  
✅ **CSV** est idéal pour les données tabulaires et les tableurs  
✅ **XML** reste utilisé pour les systèmes legacy et documents structurés  
✅ Python offre des outils natifs excellents pour ces trois formats  
✅ Toujours gérer les erreurs et spécifier l'encodage UTF-8

---

Vous maîtrisez maintenant les trois principaux formats de données ! Ces compétences sont essentielles pour échanger des données avec d'autres programmes et services.

⏭️ [Sérialisation avec pickle](/04-gestion-donnees-et-fichiers/03-serialisation-pickle.md)
