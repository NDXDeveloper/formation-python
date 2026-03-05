🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.5 Outils modernes (Poetry, Pipenv)

## Introduction

Dans les sections précédentes, nous avons vu comment gérer les dépendances avec **pip** et les environnements virtuels avec **venv**. Ces outils fonctionnent bien, mais nécessitent de jongler entre plusieurs commandes et fichiers (`requirements.txt`, activation manuelle de venv, etc.).

Les outils modernes comme **Poetry** et **Pipenv** ont été créés pour simplifier et améliorer ce workflow en offrant :
- Gestion automatique des environnements virtuels
- Résolution intelligente des dépendances
- Séparation des dépendances de développement et de production
- Verrouillage des versions pour une reproductibilité parfaite
- Gestion simplifiée du cycle de vie des projets

**Analogie :** Si pip + venv sont comme utiliser des outils séparés (tournevis, marteau, clés), Poetry et Pipenv sont comme des couteaux suisses qui intègrent tout en un seul outil.

---

## Pourquoi des outils modernes ?

### Limites de pip + requirements.txt

**Problème 1 : Résolution de dépendances**
```
# requirements.txt
django==3.2.0  
requests==2.28.0  

# Mais si Django nécessite requests>=2.25.0,<2.29.0 ?
# pip n'avertit pas des conflits potentiels
```

**Problème 2 : Dépendances transitives**
```
# Vous installez : flask
# Flask installe automatiquement : werkzeug, jinja2, click, etc.
# pip freeze capture tout, même les dépendances indirectes
```

**Problème 3 : Gestion manuelle de venv**
```bash
# Workflow traditionnel (plusieurs étapes)
python -m venv venv  
source venv/bin/activate  
pip install flask  
pip freeze > requirements.txt  
deactivate  
```

### Ce que les outils modernes apportent

**Pipenv et Poetry offrent :**

1. **Fichiers de dépendances intelligents**
   - Distinction entre dépendances directes et transitives
   - Séparation développement / production
   - Verrouillage des versions exactes

2. **Gestion automatique des environnements**
   - Création automatique de venv
   - Activation implicite
   - Détection de l'environnement

3. **Résolution de dépendances**
   - Détection et résolution des conflits
   - Graphe de dépendances complet

4. **Workflow simplifié**
   - Une commande pour tout faire
   - Moins d'étapes manuelles

---

## Pipenv

### Qu'est-ce que Pipenv ?

**Pipenv** est un outil qui combine pip et virtualenv en une seule interface cohérente. Il a été créé par Kenneth Reitz (créateur de requests) et est recommandé officiellement par Python.org.

**Philosophie :** "Pipenv vise à apporter le meilleur de tous les mondes de packaging à Python."

### Installation de Pipenv

```bash
# Installation globale
pip install --user pipenv

# Ou avec pip système
pip install pipenv

# Vérification
pipenv --version
```

Résultat attendu :
```
pipenv, version 2023.10.20
```

### Les fichiers de Pipenv

Pipenv utilise deux fichiers principaux :

**1. Pipfile** : Fichier de configuration (équivalent amélioré de requirements.txt)  
**2. Pipfile.lock** : Fichier de verrouillage (versions exactes de toutes les dépendances)  

---

## Commencer avec Pipenv

### Créer un nouveau projet

```bash
# Créer le dossier du projet
mkdir mon_projet  
cd mon_projet  

# Initialiser Pipenv
pipenv install
```

Cette commande :
1. Crée un environnement virtuel automatiquement
2. Crée un fichier `Pipfile`
3. Crée un fichier `Pipfile.lock`

**Fichier généré : `Pipfile`**
```toml
[[source]]
url = "https://pypi.org/simple"  
verify_ssl = true  
name = "pypi"  

[packages]

[dev-packages]

[requires]
python_version = "3.11"
```

### Installer des packages

```bash
# Installer un package
pipenv install requests

# Installer plusieurs packages
pipenv install flask pandas numpy

# Installer une version spécifique
pipenv install django==4.2.0
```

Après installation, le `Pipfile` est mis à jour :
```toml
[[source]]
url = "https://pypi.org/simple"  
verify_ssl = true  
name = "pypi"  

[packages]
requests = "*"  
flask = "*"  
pandas = "*"  
numpy = "*"  
django = "==4.2.0"  

[dev-packages]

[requires]
python_version = "3.11"
```

### Installer des dépendances de développement

Pour les outils utilisés uniquement en développement (tests, linting, etc.) :

```bash
# Installer en tant que dépendance de développement
pipenv install --dev pytest black flake8

# Ou version courte
pipenv install -d pytest
```

Le `Pipfile` devient :
```toml
[packages]
requests = "*"  
flask = "*"  

[dev-packages]
pytest = "*"  
black = "*"  
flake8 = "*"  
```

### Activer l'environnement virtuel

**Méthode 1 : Shell interactif**
```bash
pipenv shell
```

Vous entrez dans un sous-shell avec l'environnement activé :
```bash
(mon_projet) user@computer:~/mon_projet$
```

Pour sortir :
```bash
exit
```

**Méthode 2 : Exécution directe**
```bash
# Exécuter une commande dans l'environnement
pipenv run python app.py

# Exécuter un script
pipenv run python mon_script.py

# Lancer pytest
pipenv run pytest
```

### Afficher les dépendances

```bash
# Lister les packages installés
pipenv graph
```

Résultat :
```
requests==2.31.0
├── certifi [required: >=2017.4.17, installed: 2023.7.22]
├── charset-normalizer [required: >=2,<4, installed: 3.2.0]
├── idna [required: >=2.5,<4, installed: 3.4]
└── urllib3 [required: >=1.21.1,<3, installed: 2.0.4]

flask==2.3.3
├── blinker [required: >=1.6.2, installed: 1.6.2]
├── click [required: >=8.1.3, installed: 8.1.7]
├── itsdangerous [required: >=2.1.2, installed: 2.1.2]
├── jinja2 [required: >=3.1.2, installed: 3.1.2]
│   └── markupsafe [required: >=2.0, installed: 2.1.3]
└── werkzeug [required: >=2.3.7, installed: 2.3.7]
```

### Désinstaller des packages

```bash
# Désinstaller un package
pipenv uninstall requests

# Désinstaller un package de développement
pipenv uninstall --dev pytest
```

### Mettre à jour les packages

```bash
# Mettre à jour tous les packages
pipenv update

# Mettre à jour un package spécifique
pipenv update flask

# Voir les packages obsolètes
pipenv update --outdated
```

---

## Le fichier Pipfile.lock

### Qu'est-ce que Pipfile.lock ?

Le fichier `Pipfile.lock` contient les **versions exactes** de tous les packages (incluant les dépendances transitives) et leurs hash de sécurité.

**But :** Garantir que tout le monde installe exactement les mêmes versions.

**Exemple de contenu (extrait) :**
```json
{
    "_meta": {
        "hash": {
            "sha256": "7e7ef69da7248742e869378f8421880cf8f0017f96d94d086813baa518a65489"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.11"
        }
    },
    "default": {
        "requests": {
            "hashes": [
                "sha256:58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f",
                "sha256:942c5a758f98d7479f8f71c55c1cb7cb5dca7f3f5c3a3d1c6f8c2a2a4e9f8c1a"
            ],
            "index": "pypi",
            "version": "==2.31.0"
        }
    },
    "develop": {}
}
```

### Utilisation de Pipfile.lock

```bash
# Installer depuis Pipfile.lock (reproductibilité exacte)
pipenv install --ignore-pipfile

# Ou simplement
pipenv sync

# Régénérer le lock file
pipenv lock
```

**Workflow recommandé :**
1. Développement : Modifier `Pipfile` et faire `pipenv install`
2. Production : Utiliser `pipenv sync` pour installer depuis `Pipfile.lock`

---

## Migrer depuis requirements.txt

### Importer requirements.txt

Si vous avez un projet existant avec requirements.txt :

```bash
# Pipenv détecte automatiquement requirements.txt
pipenv install

# Ou spécifier explicitement
pipenv install -r requirements.txt
```

Pipenv convertira automatiquement en `Pipfile` et `Pipfile.lock`.

### Générer requirements.txt depuis Pipfile

Si vous avez besoin d'un requirements.txt pour la compatibilité :

```bash
# Générer requirements.txt
pipenv requirements > requirements.txt

# Générer avec les dépendances de dev
pipenv requirements --dev > requirements-dev.txt
```

---

## Poetry

### Qu'est-ce que Poetry ?

**Poetry** est un outil moderne de gestion de dépendances et de packaging Python. Il va plus loin que Pipenv en offrant également des fonctionnalités pour créer et publier des packages.

**Philosophie :** Fournir un outil unique pour toutes les étapes du cycle de vie d'un projet Python.

### Installation de Poetry

**Méthode recommandée (Linux/macOS) :**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Méthode recommandée (Windows PowerShell) :**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

**Vérification :**
```bash
poetry --version
```

Résultat :
```
Poetry (version 1.7.0)
```

**Configuration PATH :**
Ajoutez Poetry à votre PATH si nécessaire :
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Les fichiers de Poetry

Poetry utilise principalement :

**1. pyproject.toml** : Fichier de configuration du projet (standard PEP 518)  
**2. poetry.lock** : Fichier de verrouillage des dépendances  

---

## Commencer avec Poetry

### Créer un nouveau projet

```bash
# Créer un nouveau projet complet
poetry new mon_projet
```

Structure créée automatiquement :
```
mon_projet/
    mon_projet/
        __init__.py
    tests/
        __init__.py
    pyproject.toml
    README.md
```

**Ou initialiser dans un dossier existant :**
```bash
mkdir mon_projet  
cd mon_projet  
poetry init  
```

Poetry pose des questions interactives :
```
Package name [mon_projet]:  
Version [0.1.0]:  
Description []:  
Author [Nom <email@example.com>, n to skip]:  
License []:  
Compatible Python versions [^3.11]:  

Would you like to define your main dependencies interactively? (yes/no) [yes]  
Would you like to define your development dependencies interactively? (yes/no) [yes]  
```

### Le fichier pyproject.toml

**Fichier généré : `pyproject.toml`**
```toml
[tool.poetry]
name = "mon-projet"  
version = "0.1.0"  
description = ""  
authors = ["Votre Nom <email@example.com>"]  
readme = "README.md"  

[tool.poetry.dependencies]
python = "^3.11"

[tool.poetry.group.dev.dependencies]

[build-system]
requires = ["poetry-core"]  
build-backend = "poetry.core.masonry.api"  
```

### Installer des dépendances

```bash
# Installer un package
poetry add requests

# Installer plusieurs packages
poetry add flask pandas numpy

# Installer une version spécifique
poetry add django@4.2.0

# Installer avec contrainte de version
poetry add "requests>=2.28.0,<3.0.0"
```

Le `pyproject.toml` est mis à jour :
```toml
[tool.poetry.dependencies]
python = "^3.11"  
requests = "^2.31.0"  
flask = "^2.3.3"  
pandas = "^2.0.3"  
numpy = "^1.25.2"  
django = "4.2.0"  
```

**Note sur les versions :** `^2.31.0` signifie `>=2.31.0,<3.0.0` (compatible avec la version majeure)

### Installer des dépendances de développement

```bash
# Installer en tant que dépendance de développement
poetry add --group dev pytest black flake8

# Ou ancienne syntaxe
poetry add -D pytest
```

Le `pyproject.toml` devient :
```toml
[tool.poetry.dependencies]
python = "^3.11"  
requests = "^2.31.0"  

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"  
black = "^23.7.0"  
flake8 = "^6.0.0"  
```

### Installer toutes les dépendances

```bash
# Installer depuis pyproject.toml
poetry install

# Installer sans les dépendances de dev (production)
poetry install --without dev

# Installer uniquement les dépendances de dev
poetry install --only dev
```

### Exécuter des commandes

```bash
# Exécuter dans l'environnement Poetry
poetry run python app.py

# Exécuter pytest
poetry run pytest

# Exécuter un script
poetry run python mon_script.py
```

### Activer l'environnement virtuel

```bash
# Ouvrir un shell dans l'environnement
poetry shell
```

Vous entrez dans l'environnement :
```bash
(mon-projet-py3.11) user@computer:~/mon_projet$
```

Pour sortir :
```bash
exit
```

### Afficher les dépendances

```bash
# Lister les packages
poetry show

# Afficher l'arbre des dépendances
poetry show --tree

# Voir les détails d'un package
poetry show requests
```

Résultat de `poetry show --tree` :
```
requests 2.31.0 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<3

flask 2.3.3 A simple framework for building complex web applications.
├── blinker >=1.6.2
├── click >=8.1.3
├── itsdangerous >=2.1.2
├── jinja2 >=3.1.2
└── werkzeug >=2.3.7
```

### Mettre à jour les dépendances

```bash
# Mettre à jour tous les packages
poetry update

# Mettre à jour un package spécifique
poetry update requests

# Voir les packages obsolètes
poetry show --outdated
```

### Supprimer des dépendances

```bash
# Supprimer un package
poetry remove requests

# Supprimer un package de dev
poetry remove --group dev pytest
```

---

## Le fichier poetry.lock

Le fichier `poetry.lock` fonctionne comme `Pipfile.lock` :
- Contient les versions exactes de toutes les dépendances
- Garantit la reproductibilité
- Doit être versionné dans Git

**Workflow :**
```bash
# Développement : ajouter des packages
poetry add requests

# Production : installer depuis le lock file
poetry install --no-root
```

---

## Migrer depuis requirements.txt vers Poetry

### Import automatique

```bash
# Poetry peut importer requirements.txt
poetry add $(cat requirements.txt)
```

### Import manuel

Si vous avez un `requirements.txt` :
```
flask==2.3.3  
requests==2.31.0  
pandas==2.0.3  
```

Créez un projet Poetry et ajoutez les dépendances :
```bash
poetry init  
poetry add flask@2.3.3 requests@2.31.0 pandas@2.0.3  
```

### Exporter vers requirements.txt

```bash
# Exporter vers requirements.txt
poetry export -f requirements.txt --output requirements.txt

# Sans hash (plus lisible)
poetry export -f requirements.txt --output requirements.txt --without-hashes

# Avec les dépendances de dev
poetry export -f requirements.txt --output requirements.txt --with dev
```

---

## Fonctionnalités avancées de Poetry

### Scripts personnalisés (entry points)

Vous pouvez définir des points d'entrée console dans `pyproject.toml`. Le format est `nom = "module:fonction"` :

```toml
[tool.poetry.scripts]
start = "mon_projet.main:run"
```

Exécution :
```bash
poetry run start
```

> ⚠️ **Attention :** `[tool.poetry.scripts]` crée des **points d'entrée console** (comme `setuptools` `console_scripts`). Ce ne sont pas des alias pour des commandes shell. Le format doit être `module:fonction`. Pour exécuter des outils comme pytest ou ruff, utilisez directement `poetry run pytest` ou un `Makefile`.

### Groupes de dépendances

Organisez vos dépendances par groupe :

```toml
[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
sphinx = "^5.0.0"  
sphinx-rtd-theme = "^1.0.0"  

[tool.poetry.group.lint]
optional = true

[tool.poetry.group.lint.dependencies]
pylint = "^2.17.0"  
mypy = "^1.4.0"  
```

Installation par groupe :
```bash
poetry install --with docs  
poetry install --with lint,docs  
poetry install --without dev  
```

### Créer un package distribuable

Poetry facilite la création de packages :

```bash
# Construire le package
poetry build
```

Cela crée :
```
dist/
    mon_projet-0.1.0-py3-none-any.whl
    mon_projet-0.1.0.tar.gz
```

### Publier sur PyPI

```bash
# Configurer les credentials PyPI
poetry config pypi-token.pypi your-token-here

# Publier
poetry publish
```

---

## Comparaison : pip/venv vs Pipenv vs Poetry

| Fonctionnalité | pip + venv | Pipenv | Poetry |
|----------------|-----------|--------|--------|
| **Installation** | Intégré à Python | `pip install pipenv` | Installation séparée |
| **Fichier de config** | requirements.txt | Pipfile | pyproject.toml |
| **Lock file** | ❌ Non | ✅ Pipfile.lock | ✅ poetry.lock |
| **Gestion venv** | Manuelle | ✅ Automatique | ✅ Automatique |
| **Résolution dépendances** | ⚠️ Basique | ✅ Avancée | ✅ Très avancée |
| **Dev vs Prod** | Fichiers séparés | ✅ Section [dev-packages] | ✅ Groupes |
| **Graphe dépendances** | ❌ Non (pipdeptree) | ✅ `pipenv graph` | ✅ `poetry show --tree` |
| **Build packages** | setuptools | ⚠️ Limité | ✅ Intégré |
| **Publication PyPI** | twine | ⚠️ Non | ✅ `poetry publish` |
| **Performance** | ✅ Rapide | ⚠️ Peut être lent | ✅ Rapide |
| **Courbe apprentissage** | ⚠️ Plusieurs outils | ⚠️ Moyenne | ⚠️ Moyenne |
| **Standard** | ✅ Officiel | ⚠️ Recommandé | ⚠️ Populaire |

---

## Quand utiliser quel outil ?

### Utilisez pip + venv si :
- ✅ Vous débutez avec Python
- ✅ Projet simple avec peu de dépendances
- ✅ Vous voulez utiliser les outils standards
- ✅ Script rapide ou prototype
- ✅ Environnement avec contraintes (pas d'installation autorisée)

### Utilisez Pipenv si :
- ✅ Vous voulez un outil simple et intégré
- ✅ Projet de taille moyenne
- ✅ Vous voulez une meilleure gestion des dépendances que pip
- ✅ Migration facile depuis requirements.txt
- ✅ Recommandation officielle de Python.org

### Utilisez Poetry si :
- ✅ Nouveau projet professionnel
- ✅ Vous allez créer un package à publier
- ✅ Projet avec nombreuses dépendances
- ✅ Vous voulez les meilleures performances
- ✅ Workflow moderne et complet
- ✅ Gestion avancée de versions

---

## Configuration de Poetry

### Voir la configuration

```bash
poetry config --list
```

### Paramètres utiles

```bash
# Créer les venv dans le dossier du projet
poetry config virtualenvs.in-project true

# Emplacement des venv
poetry config virtualenvs.path

# Ne pas créer de venv (utiliser l'environnement actuel)
poetry config virtualenvs.create false
```

### Fichier de configuration

Poetry stocke sa configuration dans :
- Linux/macOS : `~/.config/pypoetry/config.toml`
- Windows : `%APPDATA%\pypoetry\config.toml`

**Exemple de configuration :**
```toml
[virtualenvs]
create = true  
in-project = true  
path = "{cache-dir}/virtualenvs"  

[repositories.testpypi]
url = "https://test.pypi.org/legacy/"
```

---

## Configuration de Pipenv

### Variables d'environnement

```bash
# Créer le venv dans le projet
export PIPENV_VENV_IN_PROJECT=1

# Ignorer Pipfile.lock
export PIPENV_SKIP_LOCK=1

# Timeout pour les opérations
export PIPENV_TIMEOUT=300
```

### Fichier .env

Pipenv charge automatiquement les variables depuis `.env` :

**Fichier : `.env`**
```
DEBUG=True  
DATABASE_URL=postgresql://localhost/mabase  
SECRET_KEY=super_secret  
```

```python
import os

# Pipenv charge automatiquement .env
debug = os.getenv('DEBUG')  
database_url = os.getenv('DATABASE_URL')  
```

---

## Exemple complet : Projet avec Poetry

### Initialisation

```bash
# Créer le projet
poetry new mon_api

cd mon_api
```

Structure créée :
```
mon_api/
    mon_api/
        __init__.py
    tests/
        __init__.py
    pyproject.toml
    README.md
```

### Installation des dépendances

```bash
# Dépendances principales
poetry add fastapi uvicorn sqlalchemy pydantic-settings

# Dépendances de développement
poetry add --group dev pytest ruff mypy httpx

# Dépendances de documentation
poetry add --group docs sphinx
```

### Configuration pyproject.toml

```toml
[tool.poetry]
name = "mon-api"  
version = "0.1.0"  
description = "Une API RESTful avec FastAPI"  
authors = ["Votre Nom <email@example.com>"]  
readme = "README.md"  

[tool.poetry.dependencies]
python = "^3.11"  
fastapi = "^0.104.0"  
uvicorn = {extras = ["standard"], version = "^0.24.0"}  
sqlalchemy = "^2.0.0"  
pydantic-settings = "^2.0.0"  

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"  
ruff = "^0.1.0"  
mypy = "^1.5.0"  
httpx = "^0.25.0"  

[tool.poetry.group.docs.dependencies]
sphinx = "^7.0.0"

[tool.poetry.scripts]
mon-api = "mon_api.main:start"

[tool.ruff]
line-length = 88  
target-version = "py311"  

[tool.mypy]
python_version = "3.11"  
warn_return_any = true  
warn_unused_configs = true  

[build-system]
requires = ["poetry-core"]  
build-backend = "poetry.core.masonry.api"  
```

### Code de l'API

**Fichier : `mon_api/main.py`**
```python
from fastapi import FastAPI

app = FastAPI(title="Mon API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

### Utilisation

```bash
# Installer les dépendances
poetry install

# Lancer le serveur de développement
poetry run uvicorn mon_api.main:app --reload

# Exécuter les tests
poetry run pytest

# Linter et formateur (ruff remplace black + flake8)
poetry run ruff check mon_api/  
poetry run ruff format mon_api/  

# Vérifier les types
poetry run mypy mon_api/
```

### Déploiement

```bash
# Construire le package
poetry build

# Installer en production (sans dev dependencies)
poetry install --without dev
```

---

## Exemple complet : Projet avec Pipenv

### Initialisation

```bash
mkdir mon_app  
cd mon_app  
pipenv install  
```

### Installation des dépendances

```bash
# Dépendances principales
pipenv install flask flask-sqlalchemy python-dotenv

# Dépendances de développement
pipenv install --dev pytest black flake8
```

### Fichier Pipfile résultant

```toml
[[source]]
url = "https://pypi.org/simple"  
verify_ssl = true  
name = "pypi"  

[packages]
flask = "*"  
flask-sqlalchemy = "*"  
python-dotenv = "*"  

[dev-packages]
pytest = "*"  
black = "*"  
flake8 = "*"  

[requires]
python_version = "3.11"
```

### Code de l'application

**Fichier : `app.py`**
```python
from flask import Flask  
from dotenv import load_dotenv  
import os  

load_dotenv()

app = Flask(__name__)  
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')  

@app.route('/')
def home():
    return {"message": "Hello from Pipenv!"}

if __name__ == '__main__':
    app.run(debug=True)
```

**Fichier : `.env`**
```
SECRET_KEY=super_secret_key_123  
DEBUG=True  
```

### Utilisation

```bash
# Activer l'environnement
pipenv shell

# Lancer l'application
python app.py

# Ou sans activer
pipenv run python app.py

# Exécuter les tests
pipenv run pytest

# Formater le code
pipenv run black .
```

---

## Migration entre outils

### De pip/venv vers Pipenv

```bash
# Importer requirements.txt
pipenv install -r requirements.txt

# Pipenv crée Pipfile et Pipfile.lock
# Vous pouvez supprimer requirements.txt si désiré
```

### De pip/venv vers Poetry

```bash
# Initialiser Poetry
poetry init

# Ajouter les dépendances du requirements.txt
poetry add $(cat requirements.txt | grep -v "#" | xargs)
```

### De Pipenv vers Poetry

```bash
# Générer requirements.txt depuis Pipenv
pipenv requirements > requirements.txt

# Initialiser Poetry
poetry init

# Importer les dépendances
poetry add $(cat requirements.txt | xargs)
```

### De Poetry vers Pipenv

```bash
# Exporter depuis Poetry
poetry export -f requirements.txt -o requirements.txt

# Importer dans Pipenv
pipenv install -r requirements.txt
```

---

## Bonnes pratiques

### 1. Choisir un outil et s'y tenir

**Ne mélangez pas les outils dans un même projet :**

```
❌ MAUVAIS :
mon_projet/
    requirements.txt
    Pipfile
    pyproject.toml   # Trop d'outils !

✅ BON :
mon_projet/
    pyproject.toml   # Un seul outil
```

### 2. Toujours versionner les lock files

```bash
# .gitignore
venv/
__pycache__/
.env

# MAIS commitez :
# Pipfile.lock
# poetry.lock
```

### 3. Documenter l'outil utilisé

Dans votre README.md :

````markdown
## Installation

Ce projet utilise Poetry pour la gestion des dépendances.

### Prérequis
- Python 3.11+
- Poetry 1.7+

### Setup
```bash
# Installer Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Installer les dépendances
poetry install

# Lancer l'application
poetry run python app.py
```
````

### 4. Séparer dev et production

```bash
# Développement : installer tout
poetry install

# Production : sans dev dependencies
poetry install --without dev
```

### 5. Mettre à jour régulièrement

```bash
# Pipenv
pipenv update

# Poetry
poetry update

# Vérifier les packages obsolètes
poetry show --outdated
```

### 6. Utiliser les scripts

Définissez des scripts pour les tâches courantes :

**Poetry :** utilisez directement `poetry run` avec les outils installés :

```bash
poetry run uvicorn app.main:app --reload  
poetry run pytest tests/  
poetry run ruff check .  
```

Ou combinez avec un `Makefile` pour des raccourcis :
```makefile
dev:
	poetry run uvicorn app.main:app --reload
test:
	poetry run pytest tests/
lint:
	poetry run ruff check .
```

---

## Problèmes courants et solutions

### Problème 1 : Poetry/Pipenv lent

**Solution :**
```bash
# Poetry : désactiver keyring
poetry config keyring.enabled false

# Utiliser un cache local
poetry config cache-dir /tmp/poetry-cache

# Pipenv : augmenter le timeout
export PIPENV_TIMEOUT=600
```

### Problème 2 : Conflit de dépendances

**Pipenv :**
```bash
# Forcer la résolution
pipenv install --skip-lock

# Nettoyer et réinstaller
pipenv --rm  
pipenv install  
```

**Poetry :**
```bash
# Mode verbeux pour voir le problème
poetry add package_name -vvv

# Forcer une version spécifique
poetry add "package_name==1.0.0"
```

### Problème 3 : Environnement virtuel corrompu

**Pipenv :**
```bash
# Supprimer l'environnement
pipenv --rm

# Recréer
pipenv install
```

**Poetry :**
```bash
# Trouver l'emplacement du venv
poetry env info --path

# Supprimer
poetry env remove python

# Recréer
poetry install
```

### Problème 4 : Poetry ne trouve pas Python

**Solution :**
```bash
# Spécifier la version de Python
poetry env use python3.11

# Ou chemin complet
poetry env use /usr/bin/python3.11
```

### Problème 5 : Pipenv SSL certificate error

**Solution :**
```bash
# Désactiver SSL (temporaire, dev seulement)
pipenv install --pypi-mirror https://pypi.org/simple
```

---

## Résumé

Dans cette section, vous avez appris :

- **Les limites de pip/venv** et pourquoi des outils modernes ont été créés
- **Pipenv** : outil simple qui combine pip et virtualenv
  - Utilisation de Pipfile et Pipfile.lock
  - Commandes principales : install, shell, run, graph
  - Migration depuis/vers requirements.txt
- **Poetry** : outil complet pour le cycle de vie des projets
  - Utilisation de pyproject.toml (standard PEP 518)
  - Gestion avancée des dépendances avec groupes
  - Création et publication de packages
- **Comparaison des outils** et quand utiliser chacun
- **Exemples pratiques** avec FastAPI et Flask
- **Migration** entre différents outils
- **Bonnes pratiques** pour une gestion efficace

**Points clés à retenir :**

1. **pip + venv** : Standard, simple, mais manuel
2. **Pipenv** : Bon compromis entre simplicité et fonctionnalités
3. **Poetry** : Outil le plus complet pour projets professionnels
4. Choisissez un outil adapté à vos besoins et votre niveau
5. Les lock files sont essentiels pour la reproductibilité

Les outils modernes simplifient considérablement la gestion des dépendances Python. Bien qu'ils ajoutent une couche d'abstraction, ils résolvent de nombreux problèmes et rendent le développement plus efficace et moins sujet aux erreurs.

Pour les débutants, commencez avec pip + venv pour bien comprendre les concepts de base, puis explorez Pipenv ou Poetry quand vous serez plus à l'aise.

⏭️ [Bibliothèques standard essentielles](/07-bibliotheques-standard/README.md)
