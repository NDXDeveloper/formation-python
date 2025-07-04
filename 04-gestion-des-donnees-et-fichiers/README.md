🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 4 : Gestion des données et fichiers

## Introduction

La gestion des données et des fichiers est un aspect fondamental de la programmation Python. Dans le monde réel, les applications doivent constamment interagir avec des sources de données externes : fichiers texte, bases de données, APIs, formats structurés comme JSON ou CSV. Ce module vous donnera les compétences nécessaires pour manipuler efficacement ces différents types de données.

## Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

- Lire et écrire des fichiers dans différents formats (texte, binaire)
- Manipuler des données structurées (JSON, CSV, XML)
- Utiliser la sérialisation pour sauvegarder et restaurer des objets Python
- Gérer les chemins de fichiers de manière portable avec `pathlib`
- Comprendre les bonnes pratiques de gestion des ressources fichiers
- Gérer les erreurs liées aux opérations sur fichiers

## Pourquoi ce module est-il important ?

### Dans le développement quotidien

La manipulation de fichiers est omniprésente dans le développement :
- **Configuration** : Lecture de fichiers de configuration (JSON, YAML, INI)
- **Logging** : Écriture de logs dans des fichiers
- **Import/Export** : Traitement de données CSV, Excel pour des analyses
- **Sauvegarde** : Sérialisation d'objets complexes
- **Intégration** : Échange de données avec d'autres systèmes

### Exemples concrets d'utilisation

```python
# Lecture d'un fichier de configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Traitement d'un fichier CSV
import csv
with open('ventes.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Produit: {row['produit']}, Ventes: {row['montant']}")

# Sauvegarde d'un objet complexe
import pickle
data = {'utilisateurs': users, 'parametres': settings}
with open('backup.pkl', 'wb') as f:
    pickle.dump(data, f)
```

## Types de données que nous couvrirons

### 1. Fichiers texte et binaires
- Encodage des caractères (UTF-8, ASCII, etc.)
- Modes d'ouverture des fichiers
- Lecture ligne par ligne vs lecture complète
- Gestion des gros fichiers

### 2. Formats de données structurées

**JSON (JavaScript Object Notation)**
- Format léger et lisible
- Parfait pour les APIs et la configuration
- Support natif en Python

**CSV (Comma-Separated Values)**
- Format universel pour les données tabulaires
- Facilement exportable vers Excel
- Traitement ligne par ligne possible

**XML (eXtensible Markup Language)**
- Format hiérarchique et extensible
- Utilisé dans de nombreux systèmes legacy
- Validation possible avec des schémas

### 3. Sérialisation Python
- **Pickle** : Format binaire Python natif
- Sauvegarde d'objets complexes
- Restauration exacte des types Python

### 4. Gestion moderne des chemins
- **pathlib** : Approche orientée objet
- Compatibilité multi-plateforme
- Opérations avancées sur les chemins

## Concepts clés à retenir

### Gestion des ressources avec `with`
```python
# Bonne pratique - fermeture automatique
with open('fichier.txt', 'r') as f:
    contenu = f.read()
# Le fichier est automatiquement fermé
```

### Gestion des erreurs
```python
try:
    with open('fichier.txt', 'r') as f:
        contenu = f.read()
except FileNotFoundError:
    print("Le fichier n'existe pas")
except PermissionError:
    print("Permissions insuffisantes")
```

### Encodage des caractères
```python
# Spécifier l'encodage pour éviter les erreurs
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()
```

## Bonnes pratiques que nous aborderons

1. **Toujours utiliser des gestionnaires de contexte** (`with` statement)
2. **Spécifier l'encodage** pour les fichiers texte
3. **Gérer les erreurs** appropriées (FileNotFoundError, PermissionError)
4. **Valider les données** lors de la lecture
5. **Optimiser les performances** pour les gros fichiers
6. **Utiliser pathlib** pour la manipulation des chemins
7. **Choisir le bon format** selon le contexte

## Structure du module

Ce module est organisé en 4 sections principales :

1. **4.1 - Lecture/écriture de fichiers** : Fondamentaux des opérations fichiers
2. **4.2 - Formats de données** : JSON, CSV, XML
3. **4.3 - Sérialisation** : Pickle et techniques avancées
4. **4.4 - Gestion des chemins** : pathlib et bonnes pratiques

## Prérequis

Avant de commencer ce module, assurez-vous de maîtriser :
- Les structures de données Python (listes, dictionnaires)
- La gestion des erreurs avec try/except
- Les concepts de base de la programmation orientée objet
- L'utilisation des gestionnaires de contexte (`with`)

## Environnement de travail

Pour ce module, vous aurez besoin de :
- Python 3.6+ installé
- Un éditeur de texte ou IDE
- Accès en lecture/écriture au système de fichiers
- Les modules standards : `json`, `csv`, `xml`, `pickle`, `pathlib`

## Cas d'usage pratiques

Tout au long de ce module, nous travaillerons sur des exemples concrets :
- Création d'un système de configuration modulaire
- Analyse de données de ventes à partir de fichiers CSV
- Sauvegarde et restauration d'état d'application
- Traitement de flux de données XML
- Gestion de logs structurés

---

**Prêt à commencer ?** La section suivante vous apprendra les fondamentaux de la lecture et écriture de fichiers en Python.

⏭️
