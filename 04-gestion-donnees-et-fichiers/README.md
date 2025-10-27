🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4. Gestion des Données et Fichiers

## Introduction au Chapitre

Bienvenue dans le chapitre 4 ! Jusqu'à présent, vous avez appris les fondamentaux de Python : variables, structures de contrôle, fonctions, et programmation orientée objet. Maintenant, il est temps de découvrir comment **sauvegarder**, **organiser** et **manipuler** des données de manière persistante.

Dans le monde réel, un programme ne travaille pas uniquement avec des données en mémoire qui disparaissent dès que le programme se termine. Les applications ont besoin de :

- 📂 **Sauvegarder** des informations pour les réutiliser plus tard
- 📥 **Lire** des données depuis des fichiers ou des sources externes
- 📤 **Exporter** des résultats vers différents formats
- 🔄 **Échanger** des données avec d'autres programmes ou systèmes
- 🗂️ **Organiser** les fichiers et dossiers de manière structurée

Ce chapitre vous apprendra à maîtriser tous ces aspects essentiels de la programmation.

---

## Pourquoi la Gestion des Données est Importante ?

### Exemples Concrets

Imaginez quelques situations courantes :

**Situation 1 : Application de gestion de tâches**
- Vous créez une to-do list
- L'utilisateur ajoute des tâches
- Le programme se ferme
- ❌ **Sans sauvegarde** : toutes les tâches sont perdues !
- ✅ **Avec sauvegarde** : les tâches sont récupérées au prochain démarrage

**Situation 2 : Analyse de données**
- Vous recevez un fichier CSV avec 10 000 lignes de ventes
- Vous devez calculer des statistiques
- ❌ **Sans gestion de fichiers** : impossible de traiter ces données
- ✅ **Avec gestion de fichiers** : vous pouvez lire, analyser et exporter les résultats

**Situation 3 : Configuration d'application**
- Votre application a des préférences utilisateur (langue, thème, etc.)
- L'utilisateur personnalise l'application
- ❌ **Sans persistance** : il doit tout reconfigurer à chaque lancement
- ✅ **Avec fichier de configuration** : les préférences sont conservées

**Situation 4 : Partage de données**
- Vous développez une API web
- D'autres programmes doivent communiquer avec le vôtre
- ❌ **Sans format standard** : impossible d'échanger des données
- ✅ **Avec JSON/XML** : les systèmes peuvent communiquer facilement

---

## Vue d'Ensemble du Chapitre

Ce chapitre est structuré en quatre grandes parties, chacune couvrant un aspect essentiel de la gestion des données :

### 4.1 Lecture et Écriture de Fichiers Texte et Binaires

**Ce que vous apprendrez :**
- Ouvrir et fermer des fichiers de manière sécurisée
- Lire le contenu de fichiers texte (plusieurs méthodes)
- Écrire et modifier des fichiers
- Travailler avec des fichiers binaires (images, etc.)
- Utiliser le gestionnaire de contexte `with`
- Gérer les erreurs courantes

**Cas d'usage :**
- Logs d'application
- Lecture de documents
- Traitement de fichiers texte
- Manipulation d'images ou fichiers binaires

**Exemple concret :**
```python
# Lire un fichier
with open('notes.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()
    print(contenu)

# Écrire dans un fichier
with open('rapport.txt', 'w', encoding='utf-8') as fichier:
    fichier.write("Mon rapport\n")
    fichier.write("Données importantes...")
```

---

### 4.2 Formats de Données (JSON, CSV, XML)

**Ce que vous apprendrez :**
- **JSON** : format moderne pour APIs et configurations
- **CSV** : format tabulaire pour tableurs et données
- **XML** : format structuré pour documents complexes
- Convertir entre différents formats
- Choisir le bon format selon vos besoins

**Cas d'usage :**
- Configuration d'applications (JSON)
- Export/import de données Excel (CSV)
- Flux RSS et documents structurés (XML)
- Communication avec des APIs web (JSON)

**Exemple concret :**
```python
import json

# Sauvegarder des données en JSON
utilisateur = {
    "nom": "Dupont",
    "age": 30,
    "competences": ["Python", "SQL"]
}

with open('utilisateur.json', 'w', encoding='utf-8') as f:
    json.dump(utilisateur, f, indent=4)

# Relire les données
with open('utilisateur.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data['nom'])
```

---

### 4.3 Sérialisation avec Pickle

**Ce que vous apprendrez :**
- Concept de sérialisation (mise en conserve d'objets)
- Sauvegarder n'importe quel objet Python
- Charger des objets sauvegardés
- Cas d'usage et précautions de sécurité

**Cas d'usage :**
- Sauvegardes de jeux vidéo
- Cache de résultats de calculs
- Sauvegarde d'objets complexes
- Sessions utilisateur

**Exemple concret :**
```python
import pickle

class Joueur:
    def __init__(self, nom, niveau, points):
        self.nom = nom
        self.niveau = niveau
        self.points = points

joueur = Joueur("Alice", 10, 5000)

# Sauvegarder
with open('sauvegarde.pkl', 'wb') as f:
    pickle.dump(joueur, f)

# Recharger plus tard
with open('sauvegarde.pkl', 'rb') as f:
    joueur_charge = pickle.load(f)
    print(f"{joueur_charge.nom} - Niveau {joueur_charge.niveau}")
```

---

### 4.4 Gestion des Chemins avec Pathlib

**Ce que vous apprendrez :**
- Manipuler des chemins de fichiers de manière moderne
- Vérifier l'existence de fichiers et dossiers
- Créer, déplacer, renommer des fichiers
- Lister et rechercher des fichiers
- Écrire du code compatible Windows/Linux/macOS

**Cas d'usage :**
- Organisation automatique de fichiers
- Systèmes de backup
- Recherche de fichiers
- Scripts de maintenance

**Exemple concret :**
```python
from pathlib import Path

# Construction de chemins
projet = Path('projets') / 'python' / 'mon_app'

# Créer des dossiers
projet.mkdir(parents=True, exist_ok=True)

# Rechercher tous les fichiers .py
for fichier in Path('.').rglob('*.py'):
    print(fichier.name)

# Informations sur un fichier
fichier = Path('script.py')
if fichier.exists():
    print(f"Taille : {fichier.stat().st_size} octets")
```

---

## Les Concepts Clés à Maîtriser

À la fin de ce chapitre, vous saurez :

### 1. Persistance des Données
**Concept :** Les données survivent après l'arrêt du programme

```python
# Sans persistance
notes = ["Faire les courses", "Appeler Marie"]
# Programme terminé → données perdues

# Avec persistance
import json
with open('notes.json', 'w') as f:
    json.dump(notes, f)
# Programme terminé → données sauvegardées ✅
```

### 2. Formats de Données
**Concept :** Structurer les données de manière standardisée

| Format | Usage Principal |
|--------|----------------|
| Texte brut | Logs, notes simples |
| JSON | APIs, configuration |
| CSV | Données tabulaires |
| XML | Documents structurés |
| Pickle | Objets Python complexes |

### 3. Gestion des Ressources
**Concept :** Ouvrir et fermer proprement les fichiers

```python
# ❌ Mauvaise pratique
f = open('fichier.txt', 'r')
contenu = f.read()
f.close()  # On peut oublier !

# ✅ Bonne pratique
with open('fichier.txt', 'r') as f:
    contenu = f.read()
# Fermeture automatique
```

### 4. Encodage
**Concept :** Gérer correctement les caractères spéciaux

```python
# ✅ Spécifier l'encodage pour les accents
with open('texte.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()
```

### 5. Chemins Portables
**Concept :** Écrire du code qui fonctionne sur tous les systèmes

```python
from pathlib import Path

# ✅ Portable (fonctionne partout)
chemin = Path('dossier') / 'sous_dossier' / 'fichier.txt'

# ❌ Pas portable (seulement Windows)
chemin = 'dossier\\sous_dossier\\fichier.txt'

# ❌ Pas portable (seulement Unix)
chemin = 'dossier/sous_dossier/fichier.txt'
```

---

## Flux de Travail Typique

Voici un exemple complet montrant comment ces compétences s'articulent :

```python
from pathlib import Path
import json
import csv

# 1. Organisation des fichiers (pathlib)
projet = Path('mon_projet')
dossier_data = projet / 'data'
dossier_data.mkdir(parents=True, exist_ok=True)

# 2. Collecter des données
utilisateurs = [
    {"nom": "Alice", "age": 30, "ville": "Paris"},
    {"nom": "Bob", "age": 25, "ville": "Lyon"},
    {"nom": "Charlie", "age": 35, "ville": "Marseille"}
]

# 3. Sauvegarder en JSON (configuration, API)
fichier_json = dossier_data / 'utilisateurs.json'
with open(fichier_json, 'w', encoding='utf-8') as f:
    json.dump(utilisateurs, f, indent=4, ensure_ascii=False)

# 4. Exporter en CSV (pour Excel)
fichier_csv = dossier_data / 'utilisateurs.csv'
with open(fichier_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nom', 'age', 'ville'])
    writer.writeheader()
    writer.writerows(utilisateurs)

# 5. Créer un rapport texte
rapport = dossier_data / 'rapport.txt'
with open(rapport, 'w', encoding='utf-8') as f:
    f.write("=== RAPPORT D'ANALYSE ===\n\n")
    f.write(f"Nombre d'utilisateurs : {len(utilisateurs)}\n")
    age_moyen = sum(u['age'] for u in utilisateurs) / len(utilisateurs)
    f.write(f"Âge moyen : {age_moyen:.1f} ans\n")

print("✅ Traitement terminé !")
print(f"📁 Fichiers créés dans : {dossier_data}")
```

**Ce code illustre :**
- Création d'une structure de dossiers
- Manipulation de différents formats de données
- Écriture de fichiers texte et structurés
- Organisation cohérente du projet

---

## Pièges Courants à Éviter

### 1. Oublier de fermer les fichiers

```python
# ❌ Dangereux
f = open('fichier.txt', 'r')
contenu = f.read()
# Oubli de f.close() → fuite de ressources

# ✅ Sûr avec 'with'
with open('fichier.txt', 'r') as f:
    contenu = f.read()
```

### 2. Ignorer l'encodage

```python
# ❌ Peut causer des erreurs avec les accents
with open('texte.txt', 'r') as f:  # Encodage par défaut variable
    contenu = f.read()

# ✅ Explicite et portable
with open('texte.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()
```

### 3. Chemins codés en dur

```python
# ❌ Ne fonctionne que sur Linux
chemin = '/home/alice/documents/fichier.txt'

# ❌ Ne fonctionne que sur Windows
chemin = 'C:\\Users\\Alice\\Documents\\fichier.txt'

# ✅ Portable
from pathlib import Path
chemin = Path.home() / 'documents' / 'fichier.txt'
```

### 4. Ne pas gérer les erreurs

```python
# ❌ Peut crasher le programme
with open('fichier.txt', 'r') as f:
    contenu = f.read()

# ✅ Gestion robuste
try:
    with open('fichier.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier introuvable")
except PermissionError:
    print("Pas les permissions nécessaires")
```

### 5. Confondre les modes d'ouverture

```python
# ⚠️ Mode 'w' écrase le fichier existant !
with open('important.txt', 'w') as f:
    f.write("Nouvelle donnée")  # L'ancien contenu est perdu

# ✅ Mode 'a' pour ajouter à la fin
with open('important.txt', 'a') as f:
    f.write("Nouvelle donnée")  # L'ancien contenu est conservé
```

---

## Prérequis pour ce Chapitre

Avant de commencer, assurez-vous de maîtriser :

✅ **Variables et types de données** : chaînes, listes, dictionnaires
✅ **Structures de contrôle** : if/else, boucles for/while
✅ **Fonctions** : définition et appel de fonctions
✅ **Gestion des exceptions** : try/except (sera approfondi)
✅ **Compréhension de base** : ce qu'est un fichier, un dossier, un chemin

Si vous n'êtes pas à l'aise avec ces concepts, nous vous recommandons de réviser les chapitres précédents.

---

## Ce que Vous Allez Construire

Au fil de ce chapitre, vous allez créer plusieurs petits projets pratiques :

### Projet 1 : Gestionnaire de Notes
- Sauvegarder des notes dans des fichiers texte
- Lire et afficher les notes existantes
- Organiser les notes par catégorie

### Projet 2 : Analyseur de Données CSV
- Lire un fichier CSV de ventes
- Calculer des statistiques (total, moyenne)
- Exporter un rapport en JSON

### Projet 3 : Système de Configuration
- Créer un fichier de configuration JSON
- Lire et modifier la configuration
- Valider les paramètres

### Projet 4 : Organisateur de Fichiers
- Scanner un dossier
- Organiser les fichiers par extension
- Créer des backups automatiques

---

## Ressources et Outils

### Modules Python à Connaître

| Module | Usage | Section |
|--------|-------|---------|
| `open()` | Fichiers texte/binaires | 4.1 |
| `json` | Format JSON | 4.2 |
| `csv` | Format CSV | 4.2 |
| `xml.etree.ElementTree` | Format XML | 4.2 |
| `pickle` | Sérialisation | 4.3 |
| `pathlib` | Gestion de chemins | 4.4 |

### Éditeurs de Texte Utiles

Pour visualiser et éditer vos fichiers de données :
- **VS Code** : excellent support de JSON, CSV, XML
- **Notepad++** (Windows) : léger et rapide
- **Sublime Text** : rapide et élégant
- **Tableurs** : Excel, LibreOffice Calc pour CSV

---

## Conseils pour Réussir ce Chapitre

### 1. Pratiquez avec de Vrais Fichiers
Ne vous contentez pas de lire les exemples. Créez vos propres fichiers, testez le code, expérimentez !

### 2. Commencez Petit
Avant de créer des projets complexes, assurez-vous de maîtriser les opérations de base.

### 3. Gérez Toujours les Erreurs
Dans le monde réel, les fichiers peuvent ne pas exister, être corrompus, ou inaccessibles. Anticipez ces situations.

### 4. Utilisez `with` Systématiquement
C'est la meilleure pratique pour gérer les fichiers. Cela évite les fuites de ressources.

### 5. Documentez vos Formats
Si vous créez des fichiers de données, documentez leur structure pour vous et les autres développeurs.

### 6. Testez sur Différents Systèmes
Si possible, testez votre code sur Windows ET Linux/macOS pour vous assurer qu'il est portable.

---

## Structure Recommandée pour vos Projets

Voici une organisation de dossiers typique :

```
mon_projet/
├── src/                    # Code source
│   ├── main.py
│   └── utils.py
├── data/                   # Fichiers de données
│   ├── input/             # Données d'entrée
│   ├── output/            # Résultats générés
│   └── config/            # Fichiers de configuration
├── tests/                 # Tests (chapitre 10)
├── docs/                  # Documentation
└── README.md             # Description du projet
```

**Avantages de cette structure :**
- Séparation claire code/données
- Facile à naviguer
- Prêt pour la collaboration
- Évite les conflits de chemins

---

## Prêt à Commencer ?

Vous avez maintenant une vue d'ensemble complète de ce chapitre. Vous comprenez :

✅ Pourquoi la gestion des fichiers est essentielle
✅ Les différents formats de données disponibles
✅ Comment organiser votre code et vos fichiers
✅ Les pièges à éviter
✅ Ce que vous allez apprendre dans chaque section

**Dans la prochaine section (4.1)**, nous allons entrer dans le vif du sujet avec la lecture et l'écriture de fichiers texte et binaires. C'est la base de tout le reste !

---

## Aide-Mémoire Rapide

### Syntaxe Essentielle à Retenir

```python
# Lire un fichier texte
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

# Écrire dans un fichier
with open('fichier.txt', 'w', encoding='utf-8') as f:
    f.write("Mon contenu")

# JSON
import json
with open('data.json', 'w') as f:
    json.dump(donnees, f, indent=4)

# CSV
import csv
with open('data.csv', 'r') as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne)

# Pathlib
from pathlib import Path
chemin = Path('dossier') / 'fichier.txt'
if chemin.exists():
    print(chemin.read_text())
```

---

Maintenant, passons aux choses sérieuses avec la section 4.1 ! 🚀

⏭️ [Lecture/écriture de fichiers texte et binaires](/04-gestion-donnees-et-fichiers/01-lecture-ecriture-fichiers.md)
