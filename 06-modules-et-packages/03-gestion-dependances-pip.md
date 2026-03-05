🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.3 Gestion des dépendances avec pip

## Introduction

**pip** (Pip Installs Packages) est le gestionnaire de packages officiel de Python. Il permet d'installer, de mettre à jour et de gérer facilement des bibliothèques (packages) tierces depuis le Python Package Index (PyPI).

Plutôt que de réinventer la roue, pip vous permet d'utiliser des milliers de packages créés par la communauté Python pour ajouter des fonctionnalités à vos projets : manipulation de données, création d'interfaces web, traitement d'images, intelligence artificielle, et bien plus encore.

---

## Qu'est-ce qu'une dépendance ?

Une **dépendance** est un package externe dont votre projet a besoin pour fonctionner. Par exemple :

- Vous développez une application web → vous avez besoin de Flask ou Django
- Vous analysez des données → vous avez besoin de pandas et numpy
- Vous manipulez des images → vous avez besoin de Pillow

Au lieu d'écrire tout ce code vous-même, vous installez ces packages avec pip et les utilisez dans votre projet.

---

## Vérifier l'installation de pip

pip est généralement installé automatiquement avec Python. Pour vérifier :

```bash
# Vérifier la version de pip
pip --version

# Ou avec python -m pip
python -m pip --version
```

Résultat attendu :
```
pip 24.0 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

Si pip n'est pas installé, vous pouvez l'installer avec :
```bash
python -m ensurepip --upgrade
```

---

## Installer un package

### Installation simple

Pour installer un package, utilisez la commande `pip install` :

```bash
pip install requests
```

Cette commande :
1. Cherche le package "requests" sur PyPI
2. Télécharge la dernière version
3. Installe le package et ses dépendances

### Installation de plusieurs packages

Vous pouvez installer plusieurs packages en une seule commande :

```bash
pip install requests pandas matplotlib
```

### Installer une version spécifique

Pour installer une version précise d'un package :

```bash
# Version exacte
pip install requests==2.28.0

# Version minimale
pip install requests>=2.25.0

# Version dans une plage
pip install requests>=2.25.0,<3.0.0
```

Opérateurs de version disponibles :
- `==` : Version exacte (par exemple : `==2.28.0`)
- `>=` : Version minimale (par exemple : `>=2.25.0`)
- `<=` : Version maximale (par exemple : `<=2.30.0`)
- `>` : Strictement supérieur
- `<` : Strictement inférieur
- `!=` : Exclure une version

### Utilisation après installation

Une fois installé, vous pouvez importer le package dans votre code Python :

```python
# Après avoir fait : pip install requests
import requests

response = requests.get('https://api.github.com')  
print(response.status_code)  
```

---

## Lister les packages installés

### Afficher tous les packages

Pour voir tous les packages installés :

```bash
pip list
```

Résultat :
```
Package         Version
--------------- -------
certifi         2023.7.22  
charset-normalizer  3.2.0  
idna            3.4  
requests        2.31.0  
urllib3         2.0.4  
```

### Afficher les détails d'un package

Pour obtenir des informations détaillées sur un package :

```bash
pip show requests
```

Résultat :
```
Name: requests  
Version: 2.31.0  
Summary: Python HTTP for Humans.  
Home-page: https://requests.readthedocs.io  
Author: Kenneth Reitz  
Author-email: me@kennethreitz.org  
License: Apache 2.0  
Location: /usr/lib/python3.11/site-packages  
Requires: certifi, charset-normalizer, idna, urllib3  
Required-by:  
```

### Afficher les packages obsolètes

Pour voir quels packages peuvent être mis à jour :

```bash
pip list --outdated
```

Résultat :
```
Package    Version  Latest   Type
---------- -------- -------- -----
requests   2.28.0   2.31.0   wheel  
numpy      1.24.0   1.25.2   wheel  
```

---

## Mettre à jour un package

### Mettre à jour un package spécifique

```bash
pip install --upgrade requests

# Ou version courte
pip install -U requests
```

### Mettre à jour pip lui-même

Il est recommandé de maintenir pip à jour :

```bash
pip install --upgrade pip

# Ou avec python -m pip
python -m pip install --upgrade pip
```

---

## Désinstaller un package

Pour supprimer un package :

```bash
pip uninstall requests
```

pip vous demandera confirmation :
```
Proceed (Y/n)? Y
```

Pour désinstaller sans confirmation :
```bash
pip uninstall -y requests
```

Désinstaller plusieurs packages :
```bash
pip uninstall requests pandas numpy
```

---

## Le fichier requirements.txt

### Qu'est-ce que requirements.txt ?

Le fichier `requirements.txt` est un fichier texte qui liste toutes les dépendances de votre projet. C'est une pratique standard en Python qui permet de :

- Documenter les packages nécessaires
- Faciliter l'installation sur d'autres machines
- Assurer la reproductibilité de l'environnement

### Créer un fichier requirements.txt

**Méthode 1 : Générer automatiquement**

Générer la liste de tous les packages installés :

```bash
pip freeze > requirements.txt
```

Cela crée un fichier `requirements.txt` contenant :
```
certifi==2023.7.22  
charset-normalizer==3.2.0  
idna==3.4  
requests==2.31.0  
urllib3==2.0.4  
```

**Méthode 2 : Créer manuellement**

Vous pouvez créer le fichier manuellement en listant uniquement vos dépendances directes :

```
# requirements.txt
requests==2.31.0  
pandas>=1.5.0  
matplotlib==3.7.2  
numpy>=1.24.0,<2.0.0  
```

**Bonnes pratiques :**
- Listez uniquement les packages que vous utilisez directement
- Spécifiez les versions pour assurer la reproductibilité
- Ajoutez des commentaires pour expliquer l'usage si nécessaire

```
# requirements.txt

# Requêtes HTTP
requests==2.31.0

# Analyse de données
pandas>=1.5.0  
numpy>=1.24.0  

# Visualisation
matplotlib==3.7.2  
seaborn>=0.12.0  
```

### Installer depuis requirements.txt

Pour installer tous les packages listés dans `requirements.txt` :

```bash
pip install -r requirements.txt
```

Cette commande est très utile pour :
- Configurer un nouvel environnement de développement
- Déployer votre application sur un serveur
- Permettre à d'autres développeurs de reproduire votre environnement

### Différents fichiers requirements

Pour des projets plus complexes, vous pouvez avoir plusieurs fichiers :

```
requirements/
    base.txt          # Dépendances communes
    dev.txt           # Dépendances de développement
    prod.txt          # Dépendances de production
    test.txt          # Dépendances pour les tests
```

**Fichier : `requirements/base.txt`**
```
# Dépendances nécessaires partout
requests==2.31.0  
python-dotenv==1.0.0  
```

**Fichier : `requirements/dev.txt`**
```
# Inclure les dépendances de base
-r base.txt

# Outils de développement
pytest==7.4.0  
black==23.7.0  
flake8==6.0.0  
ipython==8.14.0  
```

**Fichier : `requirements/prod.txt`**
```
# Inclure les dépendances de base
-r base.txt

# Dépendances spécifiques à la production
gunicorn==21.2.0
```

Installation :
```bash
# Développement
pip install -r requirements/dev.txt

# Production
pip install -r requirements/prod.txt
```

---

## Rechercher des packages

### Rechercher sur PyPI

Pour trouver des packages disponibles, visitez [PyPI.org](https://pypi.org/) ou utilisez votre moteur de recherche.

**Exemple de recherche :** "python package for json"

### Packages populaires par domaine

**Développement Web :**
- `flask` : Micro-framework web
- `django` : Framework web complet
- `fastapi` : Framework moderne et rapide

**Analyse de données :**
- `pandas` : Manipulation de données
- `numpy` : Calcul numérique
- `matplotlib` : Visualisation
- `seaborn` : Visualisation statistique

**Machine Learning :**
- `scikit-learn` : Algorithmes ML
- `tensorflow` : Deep learning
- `pytorch` : Deep learning

**Utilitaires :**
- `requests` : Requêtes HTTP
- `pillow` : Traitement d'images
- `python-dotenv` : Gestion des variables d'environnement
- `click` : Interface en ligne de commande

**Automatisation et scraping :**
- `selenium` : Automatisation de navigateur
- `beautifulsoup4` : Parsing HTML/XML
- `scrapy` : Framework de web scraping

---

## PyPI - Python Package Index

### Qu'est-ce que PyPI ?

**PyPI** (Python Package Index) est le dépôt officiel de packages Python. C'est comme une "bibliothèque" géante où :

- Les développeurs publient leurs packages
- pip télécharge les packages lors de l'installation
- Plus de 500 000 packages sont disponibles

Site web : https://pypi.org/

### Structure d'une page PyPI

Chaque package sur PyPI a une page contenant :

- **Description** : Qu'est-ce que fait le package
- **Installation** : Comment l'installer
- **Documentation** : Lien vers la doc complète
- **Versions** : Historique des versions
- **Statistiques** : Téléchargements, popularité
- **Licence** : Type de licence du package
- **Dépendances** : Autres packages nécessaires

### Exemple : Page du package requests

URL : https://pypi.org/project/requests/

Informations visibles :
- Version actuelle : 2.31.0
- Description : "Python HTTP for Humans"
- Installation : `pip install requests`
- Licence : Apache 2.0
- Documentation : https://requests.readthedocs.io

---

## Installer des packages depuis GitHub

Vous pouvez installer des packages directement depuis un dépôt Git :

```bash
# Depuis une URL GitHub
pip install git+https://github.com/username/repository.git

# Depuis une branche spécifique
pip install git+https://github.com/username/repository.git@branch-name

# Depuis un tag ou commit
pip install git+https://github.com/username/repository.git@v1.0.0
```

Exemple pratique :
```bash
pip install git+https://github.com/psf/requests.git
```

---

## Installation en mode éditable (développement)

Lorsque vous développez votre propre package, vous pouvez l'installer en mode éditable :

```bash
pip install -e /chemin/vers/votre/package
```

Avantages :
- Les modifications du code source sont immédiatement visibles
- Pas besoin de réinstaller après chaque changement
- Utile pour le développement et les tests

Exemple :
```bash
# Structure du projet
mon_package/
    setup.py
    mon_package/
        __init__.py
        module.py

# Installation en mode éditable
cd mon_package  
pip install -e .  
```

---

## Fichier setup.py (création de package)

> 💡 **Note :** `setup.py` est l'approche historique pour configurer un package Python. L'approche moderne utilise `pyproject.toml` (voir section 6.5 sur Poetry). Pour de nouveaux projets, préférez `pyproject.toml`.

Pour distribuer votre propre package, vous pouvez créer un fichier `setup.py` :

```python
from setuptools import setup, find_packages

setup(
    name="mon_package",
    version="1.0.0",
    description="Description de mon package",
    author="Votre Nom",
    author_email="email@example.com",
    url="https://github.com/username/mon_package",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pandas>=1.3.0",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
```

Installation de votre package :
```bash
# Installation normale
pip install .

# Installation en mode éditable
pip install -e .
```

---

## Commandes pip utiles

### Résumé des commandes principales

```bash
# Installation
pip install package_name  
pip install package_name==1.0.0  
pip install -r requirements.txt  

# Mise à jour
pip install --upgrade package_name  
pip install --upgrade pip  

# Désinstallation
pip uninstall package_name  
pip uninstall -y package_name  

# Information
pip list  
pip list --outdated  
pip show package_name  
pip freeze  
pip freeze > requirements.txt  

# Recherche (deprecated, utiliser PyPI.org)
# pip search était disponible mais est désormais désactivé

# Cache
pip cache list  
pip cache purge  

# Aide
pip help  
pip help install  
```

### Options utiles

```bash
# Installation silencieuse (sans affichage)
pip install -q requests

# Installation avec affichage détaillé
pip install -v requests

# Ne pas installer les dépendances
pip install --no-deps package_name

# Spécifier un index alternatif
pip install --index-url https://pypi.org/simple/ package_name

# Télécharger sans installer
pip download package_name
```

---

## Bonnes pratiques

### 1. Utiliser des environnements virtuels

**⚠️ Important :** N'installez JAMAIS de packages avec pip globalement (dans le système). Utilisez toujours un environnement virtuel.

Pourquoi ?
- Éviter les conflits entre projets
- Isoler les dépendances
- Faciliter la reproduction de l'environnement

Nous verrons les environnements virtuels en détail dans la section suivante (6.4).

### 2. Fixer les versions dans requirements.txt

```bash
# ✅ BON : Versions fixées
requests==2.31.0  
pandas==1.5.3  

# ⚠️ Risqué : Sans version
requests  
pandas  

# 🔄 Compromis : Version minimale
requests>=2.31.0  
pandas>=1.5.0,<2.0.0  
```

### 3. Séparer les dépendances de développement

Créez des fichiers requirements séparés :
- `requirements.txt` : Dépendances de production
- `requirements-dev.txt` : Outils de développement

```bash
# requirements.txt
requests==2.31.0  
flask==2.3.0  

# requirements-dev.txt
pytest==7.4.0  
black==23.7.0  
flake8==6.0.0  
```

### 4. Documenter les versions de Python supportées

Dans votre README ou documentation, spécifiez :

````markdown
## Prérequis

- Python 3.10 ou supérieur
- pip 21.0 ou supérieur

## Installation

```bash
pip install -r requirements.txt
```
````

### 5. Mettre à jour régulièrement

Vérifiez régulièrement les mises à jour :

```bash
# Vérifier les packages obsolètes
pip list --outdated

# Mettre à jour prudemment
# Lire les changelogs avant de mettre à jour
pip install --upgrade package_name
```

### 6. Utiliser pip-tools pour gérer les dépendances

`pip-tools` est un ensemble d'outils pour gérer les dépendances :

```bash
pip install pip-tools
```

Créer un fichier `requirements.in` avec vos dépendances directes :
```
# requirements.in
flask  
requests  
```

Compiler pour générer `requirements.txt` avec toutes les dépendances :
```bash
pip-compile requirements.in
```

### 7. Vérifier la sécurité des dépendances

Utilisez des outils comme `safety` pour détecter les vulnérabilités :

```bash
pip install safety  
safety check  
```

---

## Problèmes courants et solutions

### Problème 1 : Permission denied

**Erreur :**
```
ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied
```

**Solution :**
N'utilisez JAMAIS `sudo pip install`. Utilisez un environnement virtuel à la place.

> 📝 **PEP 668 :** Sur les distributions Linux récentes (Ubuntu 23.04+, Fedora 38+, etc.), `pip install` en dehors d'un environnement virtuel est **bloqué** par défaut avec l'erreur `externally-managed-environment`. C'est un comportement voulu pour protéger les packages système. La solution est toujours d'utiliser un environnement virtuel (voir section 6.4).

Si vous devez absolument installer globalement :
```bash
pip install --user package_name
```

### Problème 2 : Package introuvable

**Erreur :**
```
ERROR: Could not find a version that satisfies the requirement package_name
```

**Solutions :**
- Vérifier l'orthographe du package sur PyPI.org
- Vérifier la compatibilité avec votre version de Python
- Mettre à jour pip : `pip install --upgrade pip`

### Problème 3 : Conflit de versions

**Erreur :**
```
ERROR: Cannot install package-a and package-b because these package versions have conflicting dependencies.
```

**Solutions :**
- Utiliser un environnement virtuel séparé
- Ajuster les versions des packages
- Consulter la documentation pour connaître les versions compatibles

### Problème 4 : Problème de certificat SSL

**Erreur :**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solution temporaire :**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package_name
```

**Solution permanente :**
Mettre à jour les certificats de votre système.

### Problème 5 : Cache corrompu

**Solution :**
```bash
pip cache purge  
pip install --no-cache-dir package_name  
```

### Problème 6 : Installation lente

**Solutions :**
- Utiliser un miroir PyPI plus proche
- Utiliser le cache pip
- Installer les packages compilés (wheels) plutôt que depuis les sources

```bash
pip install --only-binary :all: package_name
```

---

## Comparaison : pip vs autres gestionnaires

### pip vs conda

**pip :**
- ✅ Standard pour Python
- ✅ Accès à tout PyPI (500k+ packages)
- ✅ Léger et rapide
- ❌ Gère uniquement Python

**conda :**
- ✅ Gère Python ET d'autres langages
- ✅ Résolution de dépendances plus robuste
- ✅ Packages binaires pré-compilés
- ❌ Plus lent
- ❌ Moins de packages disponibles

**Quand utiliser quoi ?**
- Projets Python purs → pip
- Data science / calcul scientifique → conda
- Projets complexes avec dépendances non-Python → conda

### pip vs Poetry vs Pipenv

Nous verrons ces outils modernes dans la section 6.5 (Outils modernes).

---

## Commandes avancées

### Créer un wheel

Un wheel est un format de distribution pré-compilé pour Python :

```bash
pip wheel package_name
```

### Installer depuis un fichier local

```bash
# Installer un fichier .whl
pip install package-1.0.0-py3-none-any.whl

# Installer depuis un fichier .tar.gz
pip install package-1.0.0.tar.gz
```

### Installer avec contraintes

Utiliser un fichier de contraintes pour limiter les versions :

```bash
# constraints.txt
numpy<2.0.0  
pandas>=1.0.0,<2.0.0  

# Installation avec contraintes
pip install -c constraints.txt requests
```

### Vérifier les dépendances

```bash
# Afficher l'arbre des dépendances
pip install pipdeptree  
pipdeptree  
```

Résultat :
```
requests==2.31.0
├── certifi [required: >=2017.4.17]
├── charset-normalizer [required: >=2,<4]
├── idna [required: >=2.5,<4]
└── urllib3 [required: >=1.21.1,<3]
```

---

## Exemple complet : Créer et gérer un projet

### Étape 1 : Créer la structure du projet

```bash
mkdir mon_projet  
cd mon_projet  
```

### Étape 2 : Créer un environnement virtuel (section 6.4)

```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
# ou
venv\Scripts\activate  # Windows
```

### Étape 3 : Installer les dépendances

```bash
pip install requests pandas flask
```

### Étape 4 : Créer requirements.txt

```bash
pip freeze > requirements.txt
```

### Étape 5 : Développer votre application

```python
# app.py
import requests  
import pandas as pd  
from flask import Flask  

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Étape 6 : Partager votre projet

Votre projet contient maintenant :
```
mon_projet/
    venv/              (à ne pas partager)
    app.py
    requirements.txt   (à partager)
    README.md
    .gitignore
```

**Fichier : `.gitignore`**
```
venv/
__pycache__/
*.pyc
.env
```

Les autres développeurs pourront recréer l'environnement avec :
```bash
pip install -r requirements.txt
```

---

## Résumé

Dans cette section, vous avez appris :

- Ce qu'est pip et comment l'utiliser pour gérer les packages Python
- Comment installer, mettre à jour et désinstaller des packages
- L'importance du fichier `requirements.txt` pour documenter les dépendances
- Comment rechercher et explorer les packages sur PyPI
- Les bonnes pratiques pour gérer les dépendances
- Comment résoudre les problèmes courants
- Les commandes pip avancées pour des cas d'usage spécifiques

pip est un outil essentiel dans l'écosystème Python qui vous permet d'accéder à une immense bibliothèque de packages créés par la communauté. Combiné avec les environnements virtuels (section suivante), pip devient un outil puissant pour gérer efficacement vos projets Python.

Dans la prochaine section, nous verrons comment créer des environnements virtuels isolés pour chaque projet, une pratique indispensable pour tout développeur Python professionnel.

⏭️ [Environnements virtuels (venv)](/06-modules-et-packages/04-environnements-virtuels.md)
