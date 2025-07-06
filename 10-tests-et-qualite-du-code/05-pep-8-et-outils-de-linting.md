🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.5 : PEP 8 et outils de linting

## Introduction

Imaginez que vous lisiez un livre où chaque chapitre est écrit avec une police différente, des marges variables, et des règles de ponctuation fantaisistes. Même si le contenu est excellent, la lecture serait pénible ! En programmation, c'est exactement le rôle des conventions de style : rendre le code lisible et cohérent pour tous.

**PEP 8** (Python Enhancement Proposal 8) est le guide de style officiel de Python. Il définit comment formater le code Python pour qu'il soit lisible, cohérent et professionnel. Les **outils de linting** automatisent la vérification de ces règles, transformant votre éditeur en assistant personnel pour un code impeccable.

## Qu'est-ce que PEP 8 ?

### Les principes fondamentaux

PEP 8 repose sur quelques idées simples mais puissantes :

> "Code is read much more often than it is written"
>
> *Le code est lu beaucoup plus souvent qu'il n'est écrit*

Cela signifie qu'un code lisible est plus important qu'un code rapide à écrire.

### Exemple : avant et après PEP 8

```python
# ❌ Code sans respect de PEP 8
def calcul(x,y,z=None):
    if z==None:z=0
    result=x+y*2-z
    return result

class MaClasse:
    def __init__(self,nom):
        self.nom=nom
    def afficher(self):
        print('Nom: '+self.nom)

# ✅ Même code conforme à PEP 8
def calculer_resultat(x, y, z=None):
    """Calcule un résultat basé sur x, y et z optionnel."""
    if z is None:
        z = 0

    resultat = x + y * 2 - z
    return resultat


class PersonneInfo:
    """Représente les informations d'une personne."""

    def __init__(self, nom):
        """Initialise avec le nom de la personne."""
        self.nom = nom

    def afficher(self):
        """Affiche les informations de la personne."""
        print(f'Nom: {self.nom}')
```

La différence est frappante ! Le code PEP 8 est immédiatement plus lisible et professionnel.

## Les règles essentielles de PEP 8

### 1. Indentation et espaces

```python
# ✅ Indentation correcte (4 espaces)
def ma_fonction():
    if condition:
        for item in liste:
            print(item)
    else:
        print("Aucun élément")

# ❌ Indentation incorrecte
def ma_fonction():
  if condition:  # 2 espaces
        for item in liste:  # 6 espaces
      print(item)  # 4 espaces - incohérent !

# ✅ Espaces autour des opérateurs
resultat = (a + b) * (c - d)
liste = [1, 2, 3, 4, 5]
dictionnaire = {'nom': 'Alice', 'age': 30}

# ❌ Pas d'espaces ou trop d'espaces
resultat=(a+b)*(c-d)  # Trop serré
resultat = ( a + b ) * ( c - d )  # Trop d'espaces
```

### 2. Longueur des lignes

```python
# ✅ Ligne courte (< 79 caractères)
def calculer_prix_total(prix_unitaire, quantite, taux_tva):
    return prix_unitaire * quantite * (1 + taux_tva)

# ❌ Ligne trop longue
def calculer_prix_total_avec_remise_et_frais_de_port_et_assurance(prix_unitaire, quantite, taux_tva, remise, frais_port):
    return prix_unitaire * quantite * (1 + taux_tva) * (1 - remise) + frais_port

# ✅ Division de longues lignes
def calculer_prix_total_complet(prix_unitaire, quantite, taux_tva,
                                remise, frais_port):
    """Calcule le prix total avec tous les éléments."""
    prix_base = prix_unitaire * quantite
    prix_avec_tva = prix_base * (1 + taux_tva)
    prix_avec_remise = prix_avec_tva * (1 - remise)
    prix_final = prix_avec_remise + frais_port
    return prix_final

# ✅ Division de longues expressions
resultat = (premiere_partie_du_calcul +
            deuxieme_partie_du_calcul +
            troisieme_partie_du_calcul)

# ✅ Division de longs appels de fonction
utilisateur = creer_utilisateur(
    nom="Alice Dupont",
    email="alice.dupont@example.com",
    age=30,
    adresse="123 Rue de la Paix, 75001 Paris"
)
```

### 3. Lignes vides

```python
# ✅ Espacement correct
import os
import sys
from pathlib import Path

import requests
import json


CONSTANTE_GLOBALE = 42


class MaClasse:
    """Documentation de la classe."""

    def __init__(self, nom):
        """Constructeur."""
        self.nom = nom

    def methode_publique(self):
        """Méthode publique."""
        return self._methode_privee()

    def _methode_privee(self):
        """Méthode privée."""
        return f"Traitement de {self.nom}"


def fonction_utilitaire():
    """Fonction utilitaire."""
    return "Résultat"


if __name__ == "__main__":
    # Code principal
    obj = MaClasse("Test")
    print(obj.methode_publique())
```

### 4. Imports

```python
# ✅ Ordre correct des imports
# 1. Bibliothèque standard
import os
import sys
from pathlib import Path

# 2. Bibliothèques tierces
import requests
import numpy as np
from django.conf import settings

# 3. Modules locaux
from mon_app.models import User
from mon_app.utils import helper_function
from . import local_module

# ❌ Imports incorrects
import os, sys  # Plusieurs imports sur une ligne
from pathlib import *  # Import avec *
import requests
import os  # Import déjà fait plus haut
```

### 5. Nommage des variables et fonctions

```python
# ✅ Nommage correct
def calculer_age(date_naissance):
    """Calcule l'âge à partir de la date de naissance."""
    pass

class GestionnaireUtilisateur:
    """Gestionnaire pour les utilisateurs."""

    def __init__(self):
        self.nombre_utilisateurs = 0
        self._cache_interne = {}

    def ajouter_utilisateur(self, nom_utilisateur):
        """Ajoute un utilisateur."""
        pass

# Variables et constantes
nom_complet = "Alice Dupont"
TAUX_TVA_STANDARD = 0.20
PI = 3.14159

# ❌ Nommage incorrect
def CalculAge(DateNaissance):  # PascalCase pour fonction
    pass

class gestionnaireUtilisateur:  # camelCase pour classe
    pass

NomComplet = "Alice"  # PascalCase pour variable
taux_tva_STANDARD = 0.20  # Mélange de styles
```

### 6. Comparaisons et conditions

```python
# ✅ Comparaisons correctes
if variable is None:
    print("Variable non définie")

if variable is not None:
    print("Variable définie")

if not liste:  # Teste si la liste est vide
    print("Liste vide")

if liste:  # Teste si la liste a des éléments
    print("Liste non vide")

# Test de type
if isinstance(variable, str):
    print("C'est une chaîne")

# ❌ Comparaisons incorrectes
if variable == None:  # Utiliser 'is None'
    pass

if len(liste) == 0:  # Utiliser 'not liste'
    pass

if type(variable) == str:  # Utiliser isinstance()
    pass

# ✅ Conditions longues
if (condition_a and
    condition_b and
    condition_c):
    print("Toutes les conditions sont vraies")

# ✅ Conditions complexes avec parenthèses
if ((condition_a or condition_b) and
    (condition_c or condition_d)):
    print("Logique complexe")
```

## Introduction au linting

### Qu'est-ce que le linting ?

Le **linting** est l'analyse automatique du code pour détecter :
- Les erreurs de style (PEP 8)
- Les erreurs potentielles
- Les mauvaises pratiques
- Le code mort ou inutilisé
- Les problèmes de sécurité

### Exemple de détection automatique

```python
# Code avec problèmes
import os
import sys
import os  # Import dupliqué

def ma_fonction(x,y):  # Pas d'espaces après les virgules
    if x==5:  # Pas d'espaces autour de ==
        result=x+y  # Pas d'espaces autour de =
        return result
    else:
        pass

variable_non_utilisee = 42  # Variable jamais utilisée

# Un linter détecterait automatiquement :
# - Import dupliqué ligne 3
# - Espaces manquants lignes 5, 6, 7
# - Variable inutilisée ligne 11
# - else inutile ligne 9
```

## Les outils de linting essentiels

### 1. Flake8 : Le vérificateur tout-en-un

#### Installation et utilisation

```bash
pip install flake8
```

```python
# exemple.py - Code avec problèmes
import os,sys

def calcul(x,y):
    if x==5:
        result=x+y
        return result

variable_inutile=42
```

```bash
# Exécution de flake8
$ flake8 exemple.py

# Résultat :
exemple.py:1:10: E401 multiple imports on one line
exemple.py:3:12: E999 SyntaxError: invalid syntax
exemple.py:4:9: E225 missing whitespace around operator
exemple.py:5:15: E225 missing whitespace around operator
exemple.py:8:17: E225 missing whitespace around operator
exemple.py:8:19: F841 local variable 'variable_inutile' is assigned to but never used
```

#### Configuration de flake8

```ini
# setup.cfg ou .flake8
[flake8]
max-line-length = 88  # Plus permissif que 79
exclude =
    .git,
    __pycache__,
    build,
    dist,
    *.egg-info,
    .venv

# Ignorer certaines erreurs spécifiques
ignore =
    E203,  # whitespace before ':'
    W503,  # line break before binary operator

# Sélectionner seulement certaines vérifications
select = E,W,F

# Complexité cyclomatique maximale
max-complexity = 10
```

### 2. Pylint : L'analyseur approfondi

#### Installation et utilisation

```bash
pip install pylint
```

```python
# exemple_pylint.py
"""Module d'exemple pour démonstration pylint."""

class CalculatriceSimple:
    """Une calculatrice simple."""

    def __init__(self):
        """Initialise la calculatrice."""
        self.historique = []

    def additionner(self, a, b):
        """Additionne deux nombres."""
        resultat = a + b
        self.historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def obtenir_historique(self):
        """Retourne l'historique des calculs."""
        return self.historique.copy()

def main():
    """Fonction principale."""
    calc = CalculatriceSimple()
    print(calc.additionner(5, 3))
    print(calc.obtenir_historique())

if __name__ == "__main__":
    main()
```

```bash
# Exécution de pylint
$ pylint exemple_pylint.py

# Résultat (note sur 10) :
************* Module exemple_pylint
exemple_pylint.py:23:0: C0304: Final newline missing (missing-final-newline)

--------------------------------------------------------------------
Your code has been rated at 9.57/10 (previous run: 9.57/10, +0.00)
```

#### Configuration de pylint

```ini
# pyproject.toml
[tool.pylint.messages_control]
disable = [
    "missing-docstring",
    "invalid-name",
    "too-few-public-methods",
]

[tool.pylint.format]
max-line-length = 88

[tool.pylint.design]
max-args = 7
max-locals = 15
max-statements = 50
```

### 3. Black : Le formatage automatique

Black n'est pas un linter au sens strict, mais un **formateur** automatique qui applique un style cohérent.

#### Installation et utilisation

```bash
pip install black
```

```python
# avant_black.py - Code mal formaté
def ma_fonction(param1,param2,param3=None):
    if param3==None:param3=[]
    result={'a':param1,'b':param2,'c':param3}
    return result

liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dictionnaire={"nom":"Alice","age":30,"ville":"Paris","pays":"France"}
```

```bash
# Formater avec Black
$ black avant_black.py
reformatted avant_black.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

```python
# après black.py - Code formaté automatiquement
def ma_fonction(param1, param2, param3=None):
    if param3 == None:
        param3 = []
    result = {"a": param1, "b": param2, "c": param3}
    return result


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dictionnaire = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris",
    "pays": "France",
}
```

#### Configuration de Black

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
)/
'''
```

### 4. isort : Organisation des imports

```bash
pip install isort
```

```python
# avant_isort.py - Imports désorganisés
from pathlib import Path
import os
import requests
import sys
from django.conf import settings
import json
from mon_app.models import User
import numpy as np
```

```bash
# Organiser avec isort
$ isort avant_isort.py
Fixing avant_isort.py
```

```python
# après_isort.py - Imports organisés
import json
import os
import sys
from pathlib import Path

import numpy as np
import requests
from django.conf import settings

from mon_app.models import User
```

#### Configuration d'isort

```toml
# pyproject.toml
[tool.isort]
profile = "black"  # Compatible avec Black
multi_line_output = 3
line_length = 88
known_first_party = ["mon_app"]
known_third_party = ["requests", "numpy", "django"]
```

## Configuration d'un projet complet

### Structure de fichiers de configuration

```
mon_projet/
├── .flake8
├── pyproject.toml
├── .pre-commit-config.yaml
├── src/
│   └── mon_app/
│       ├── __init__.py
│       ├── models.py
│       └── utils.py
└── tests/
    └── test_models.py
```

### Configuration centralisée (pyproject.toml)

```toml
# pyproject.toml - Configuration centralisée
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mon-projet"
version = "1.0.0"
description = "Description de mon projet"

# Configuration Black
[tool.black]
line-length = 88
target-version = ['py38', 'py39', 'py310']
exclude = '''
/(
    \.git
    | \.venv
    | build
    | dist
)/
'''

# Configuration isort
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["mon_app"]

# Configuration pylint
[tool.pylint.format]
max-line-length = 88

[tool.pylint.messages_control]
disable = [
    "missing-docstring",
    "invalid-name",
]

# Configuration pytest
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
addopts = "-v --tb=short"

# Configuration coverage
[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*"]

[tool.coverage.report]
show_missing = true
```

### Configuration flake8 séparée

```ini
# .flake8
[flake8]
max-line-length = 88
extend-ignore =
    # Compatible avec Black
    E203,  # whitespace before ':'
    W503,  # line break before binary operator

exclude =
    .git,
    __pycache__,
    .venv,
    build,
    dist,
    *.egg-info

# Complexité cyclomatique maximale
max-complexity = 10

# Configuration par fichier
per-file-ignores =
    # Tests peuvent avoir des imports longs
    tests/*:E501
    # __init__.py peuvent avoir des imports inutilisés
    __init__.py:F401
```

## Intégration dans l'éditeur

### VS Code

#### Extensions recommandées

```json
// .vscode/extensions.json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.flake8",
        "ms-python.black-formatter",
        "ms-python.isort",
        "ms-python.pylint"
    ]
}
```

#### Configuration VS Code

```json
// .vscode/settings.json
{
    // Python
    "python.defaultInterpreterPath": ".venv/bin/python",

    // Formatage automatique
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,

    // Linting
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.lintOnSave": true,

    // Import sorting
    "python.sortImports.args": ["--profile", "black"],
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },

    // Règles spécifiques
    "python.linting.flake8Args": [
        "--max-line-length=88",
        "--extend-ignore=E203,W503"
    ]
}
```

### PyCharm

PyCharm a un support intégré pour PEP 8 :

1. **Settings** → **Editor** → **Code Style** → **Python**
2. **Settings** → **Tools** → **External Tools** pour configurer Black
3. **Settings** → **Editor** → **Inspections** → **Python** pour pylint/flake8

## Automatisation avec pre-commit

### Installation et configuration

```bash
pip install pre-commit
```

```yaml
# .pre-commit-config.yaml
repos:
  # Hooks généraux
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  # Black - Formatage du code
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        language_version: python3

  # isort - Organisation des imports
  - repo: https://github.com/pycqa/isort
    rev: 5.11.4
    hooks:
      - id: isort
        args: ["--profile", "black"]

  # flake8 - Linting
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-docstrings]

  # mypy - Vérification de types (optionnel)
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.991
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
```

```bash
# Installation des hooks
pre-commit install

# Test manuel
pre-commit run --all-files
```

## Exemple pratique : refactoring d'un fichier

### Code initial (problématique)

```python
# user_manager.py - Version initiale avec problèmes
import os,sys
from pathlib import Path
import requests,json

class userManager:
    def __init__(self,db_path):
        self.db_path=db_path
        self.users={}

    def add_user(self,name,email,age=None):
        if name=="" or email=="":
            raise ValueError("name and email required")
        if age!=None and age<0:
            raise ValueError("age must be positive")
        user_id=len(self.users)+1
        self.users[user_id]={"name":name,"email":email,"age":age}
        return user_id

    def get_user(self,user_id):
        if user_id in self.users:
            return self.users[user_id]
        else:
            return None

    def delete_user(self,user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def save_to_file(self):
        with open(self.db_path,"w") as f:
            json.dump(self.users,f)
```

### Code après application des outils

```python
# user_manager.py - Version corrigée
"""
Module de gestion des utilisateurs.

Ce module fournit une classe UserManager pour gérer
les opérations CRUD sur les utilisateurs.
"""

import json
import os
import sys
from pathlib import Path

import requests


class UserManager:
    """
    Gestionnaire d'utilisateurs avec persistance en fichier.

    Cette classe permet de gérer des utilisateurs en mémoire
    avec sauvegarde optionnelle dans un fichier JSON.
    """

    def __init__(self, db_path):
        """
        Initialise le gestionnaire.

        Args:
            db_path (str): Chemin vers le fichier de sauvegarde
        """
        self.db_path = db_path
        self.users = {}

    def add_user(self, name, email, age=None):
        """
        Ajoute un nouvel utilisateur.

        Args:
            name (str): Nom de l'utilisateur
            email (str): Email de l'utilisateur
            age (int, optional): Âge de l'utilisateur

        Returns:
            int: ID du nouvel utilisateur

        Raises:
            ValueError: Si name ou email sont vides, ou si age est négatif
        """
        if name == "" or email == "":
            raise ValueError("name and email required")

        if age is not None and age < 0:
            raise ValueError("age must be positive")

        user_id = len(self.users) + 1
        self.users[user_id] = {
            "name": name,
            "email": email,
            "age": age
        }
        return user_id

    def get_user(self, user_id):
        """
        Récupère un utilisateur par son ID.

        Args:
            user_id (int): ID de l'utilisateur

        Returns:
            dict or None: Données utilisateur ou None si non trouvé
        """
        return self.users.get(user_id)

    def delete_user(self, user_id):
        """
        Supprime un utilisateur.

        Args:
            user_id (int): ID de l'utilisateur à supprimer

        Returns:
            bool: True si supprimé, False si non trouvé
        """
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def save_to_file(self):
        """
        Sauvegarde les utilisateurs dans le fichier JSON.

        Raises:
            OSError: Si erreur d'écriture du fichier
        """
        try:
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
        except OSError as e:
            raise OSError(f"Impossible de sauvegarder dans {self.db_path}: {e}")
```

### Résumé des améliorations

1. **Imports** : Organisés avec isort
2. **Nommage** : `userManager` → `UserManager` (PascalCase pour classes)
3. **Espaces** : Ajoutés autour des opérateurs et après les virgules
4. **Comparaisons** : `age!=None` → `age is not None`
5. **Dictionnaires** : Formatage sur plusieurs lignes pour lisibilité
6. **Documentation** : Ajout de docstrings complètes
7. **Gestion d'erreurs** : Amélioration avec gestion d'encoding
8. **Structure** : Code plus aéré et professionnel

## Workflows et intégration CI/CD

### Makefile pour automatisation locale

```makefile
# Makefile
.PHONY: format lint test check-all install clean

# Installation des dépendances
install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

# Formatage automatique
format:
	black src/ tests/
	isort src/ tests/

# Vérification du style
lint:
	flake8 src/ tests/
	pylint src/

# Tests
test:
	pytest

# Vérification complète
check-all: format lint test
	@echo "✅ Toutes les vérifications passées !"

# Nettoyage
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/
	rm -rf htmlcov/
```

### GitHub Actions

```yaml
# .github/workflows/quality.yml
name: Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install black isort flake8 pylint pytest
        pip install -r requirements.txt

    - name: Check formatting with Black
      run: black --check src/ tests/

    - name: Check import sorting with isort
      run: isort --check-only src/ tests/

    - name: Lint with flake8
      run: flake8 src/ tests/

    - name: Lint with pylint
      run: pylint src/

    - name: Run tests
      run: pytest
```

## Adaptation des règles au contexte

### Exceptions raisonnables à PEP 8

```python
# Cas où on peut déroger à PEP 8

# 1. Alignement pour la lisibilité
COULEURS = {
    'rouge':   '#FF0000',
    'vert':    '#00FF00',
    'bleu':    '#0000FF',
    'jaune':   '#FFFF00',
    'magenta': '#FF00FF',
}

# 2. Calculs mathématiques complexes
# Plus lisible sans espaces autour de **
result = (a*x**2 + b*x + c)

# 3. URLs ou chemins longs (nécessaires)
DOCUMENTATION_URL = "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"  # noqa: E501

# 4. Regex complexes (souvent longues)
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # noqa: E501
```

## Configuration par équipe

```python
# Configuration stricte pour équipe débutante
[tool.flake8]
max-line-length = 79  # PEP 8 strict
max-complexity = 5    # Fonctions simples
select = E,W,F        # Toutes les erreurs

# Configuration permissive pour équipe expérimentée
[tool.flake8]
max-line-length = 100  # Plus de flexibilité
max-complexity = 15    # Logique plus complexe autorisée
ignore = E203,W503     # Compatibilité Black
```

## Outils avancés et spécialisés

### mypy : Vérification de types statique

```bash
pip install mypy
```

```python
# exemple_mypy.py
from typing import List, Optional, Dict, Union

def calculer_moyenne(nombres: List[float]) -> float:
    """
    Calcule la moyenne d'une liste de nombres.

    Args:
        nombres: Liste de nombres flottants

    Returns:
        La moyenne des nombres
    """
    if not nombres:
        return 0.0
    return sum(nombres) / len(nombres)

def trouver_utilisateur(users: Dict[int, str], user_id: int) -> Optional[str]:
    """
    Trouve un utilisateur par son ID.

    Args:
        users: Dictionnaire ID -> nom
        user_id: ID de l'utilisateur recherché

    Returns:
        Le nom de l'utilisateur ou None si non trouvé
    """
    return users.get(user_id)

def traiter_donnee(donnee: Union[str, int, float]) -> str:
    """
    Traite différents types de données.

    Args:
        donnee: Donnée à traiter (str, int ou float)

    Returns:
        Représentation textuelle de la donnée
    """
    if isinstance(donnee, str):
        return donnee.upper()
    else:
        return str(donnee)

# Utilisation avec des erreurs de type
if __name__ == "__main__":
    # ✅ Utilisation correcte
    moyenne = calculer_moyenne([1.0, 2.0, 3.0])
    print(f"Moyenne: {moyenne}")

    # ❌ Erreur de type détectée par mypy
    # moyenne_erreur = calculer_moyenne("pas une liste")  # mypy: error

    users = {1: "Alice", 2: "Bob"}
    nom = trouver_utilisateur(users, 1)
    print(f"Utilisateur: {nom}")

    # ❌ Erreur de type
    # nom_erreur = trouver_utilisateur("pas un dict", 1)  # mypy: error
```

```bash
# Exécution de mypy
$ mypy exemple_mypy.py
Success: no issues found in 1 source file

# Si on décommente les lignes d'erreur :
$ mypy exemple_mypy.py
exemple_mypy.py:45: error: Argument 1 to "calculer_moyenne" has incompatible type "str"; expected "List[float]"
exemple_mypy.py:51: error: Argument 1 to "trouver_utilisateur" has incompatible type "str"; expected "Dict[int, str]"
Found 2 errors in 1 file (checked 1 source file)
```

#### Configuration mypy

```ini
# mypy.ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True

# Ignorer certains modules tiers
[mypy-requests.*]
ignore_missing_imports = True

[mypy-numpy.*]
ignore_missing_imports = True
```

### bandit : Sécurité du code

```bash
pip install bandit
```

```python
# exemple_bandit.py - Code avec problèmes de sécurité
import os
import subprocess
import pickle
import yaml

def problemes_securite():
    """Exemples de problèmes de sécurité détectés par bandit."""

    # ❌ Exécution de commande shell non sécurisée
    user_input = input("Entrez une commande: ")
    os.system(user_input)  # Bandit: B605 - shell injection

    # ❌ Utilisation de subprocess avec shell=True
    subprocess.call(user_input, shell=True)  # Bandit: B602

    # ❌ Désérialisation dangereuse
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)  # Bandit: B301 - pickle usage

    # ❌ Chargement YAML dangereux
    with open("config.yaml", "r") as f:
        config = yaml.load(f)  # Bandit: B506 - yaml.load usage

    # ❌ Mot de passe en dur
    password = "motdepasse123"  # Bandit: B105 - hardcoded password

    return data, config, password

def version_securisee():
    """Version corrigée des problèmes de sécurité."""

    # ✅ Validation de l'entrée utilisateur
    user_input = input("Entrez le nom du fichier: ")
    if not user_input.isalnum():
        raise ValueError("Nom de fichier invalide")

    # ✅ Utilisation sécurisée de subprocess
    subprocess.run(["ls", "-l", user_input], check=True)

    # ✅ Alternative sécurisée à pickle
    import json
    with open("data.json", "r") as f:
        data = json.load(f)

    # ✅ Chargement YAML sécurisé
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # ✅ Mot de passe depuis variable d'environnement
    password = os.getenv("APP_PASSWORD")
    if not password:
        raise ValueError("Mot de passe non configuré")

    return data, config, password
```

```bash
# Exécution de bandit
$ bandit -r exemple_bandit.py

# Résultat :
>> Issue: [B605:start_process_with_a_shell] Starting a process with a shell: Seems safe, but may be changed in the future, consider rewriting without shell
   Severity: High   Confidence: High
   Location: exemple_bandit.py:10
```

### vulture : Détection de code mort

```bash
pip install vulture
```

```python
# exemple_vulture.py - Code avec parties inutilisées
import os
import sys
import requests  # Import inutilisé

# Variable globale inutilisée
CONSTANTE_INUTILISEE = 42

def fonction_utilisee():
    """Cette fonction est utilisée."""
    return "Je suis utilisée"

def fonction_inutilisee():  # Fonction jamais appelée
    """Cette fonction n'est jamais utilisée."""
    return "Je ne sers à rien"

class ClasseUtilisee:
    """Classe utilisée."""

    def __init__(self):
        self.attribut_utilise = "utile"
        self.attribut_inutilise = "inutile"  # Attribut jamais utilisé

    def methode_utilisee(self):
        """Méthode utilisée."""
        return self.attribut_utilise

    def methode_inutilisee(self):  # Méthode jamais appelée
        """Méthode jamais utilisée."""
        return self.attribut_inutilise

def main():
    """Fonction principale."""
    # Utilisation partielle de la classe
    obj = ClasseUtilisee()
    print(fonction_utilisee())
    print(obj.methode_utilisee())

if __name__ == "__main__":
    main()
```

```bash
# Exécution de vulture
$ vulture exemple_vulture.py

# Résultat :
exemple_vulture.py:3: unused import 'requests' (90% confidence)
exemple_vulture.py:6: unused variable 'CONSTANTE_INUTILISEE' (60% confidence)
exemple_vulture.py:12: unused function 'fonction_inutilisee' (60% confidence)
exemple_vulture.py:21: unused attribute 'attribut_inutilise' (60% confidence)
exemple_vulture.py:26: unused method 'methode_inutilisee' (60% confidence)
```

### pydocstyle : Vérification des docstrings

```bash
pip install pydocstyle
```

```python
# exemple_pydocstyle.py
"""Module d'exemple pour pydocstyle."""

def fonction_sans_docstring(param1, param2):
    # ❌ Pas de docstring
    return param1 + param2

def fonction_docstring_incomplete(param1, param2):
    """Additionne deux nombres."""  # ❌ Pas de section Args/Returns
    return param1 + param2

def fonction_bien_documentee(param1, param2):
    """
    Additionne deux nombres et retourne le résultat.

    Args:
        param1 (int): Premier nombre
        param2 (int): Deuxième nombre

    Returns:
        int: Somme des deux nombres
    """
    return param1 + param2

class ClasseMalDocumentee:
    # ❌ Pas de docstring pour la classe

    def __init__(self, nom):
        # ❌ Pas de docstring pour __init__
        self.nom = nom

    def methode_publique(self):
        """Méthode publique."""  # ❌ Docstring trop courte
        return self.nom

class ClasseBienDocumentee:
    """
    Classe d'exemple bien documentée.

    Cette classe représente un objet simple avec un nom
    et fournit des méthodes pour le manipuler.

    Attributes:
        nom (str): Nom de l'objet
    """

    def __init__(self, nom):
        """
        Initialise l'objet avec un nom.

        Args:
            nom (str): Nom à assigner à l'objet
        """
        self.nom = nom

    def obtenir_nom(self):
        """
        Retourne le nom de l'objet.

        Returns:
            str: Le nom de l'objet
        """
        return self.nom
```

```bash
# Exécution de pydocstyle
$ pydocstyle exemple_pydocstyle.py

# Résultat :
exemple_pydocstyle.py:4 in public function `fonction_sans_docstring`:
        D103: Missing docstring in public function
exemple_pydocstyle.py:8 in public function `fonction_docstring_incomplete`:
        D417: Missing argument descriptions in the docstring
```

## Intégration avec tox : Tests multi-environnements

### Installation et configuration

```bash
pip install tox
```

```ini
# tox.ini
[tox]
envlist = py38,py39,py310,py311,flake8,mypy,bandit

[testenv]
deps =
    pytest
    pytest-cov
commands = pytest tests/ --cov=src

[testenv:flake8]
deps = flake8
commands = flake8 src/ tests/

[testenv:mypy]
deps =
    mypy
    types-requests
commands = mypy src/

[testenv:bandit]
deps = bandit
commands = bandit -r src/

[testenv:black]
deps = black
commands = black --check src/ tests/

[testenv:isort]
deps = isort
commands = isort --check-only src/ tests/

# Environnement pour tout vérifier
[testenv:all]
deps =
    {[testenv]deps}
    {[testenv:flake8]deps}
    {[testenv:mypy]deps}
    {[testenv:bandit]deps}
    {[testenv:black]deps}
    {[testenv:isort]deps}
commands =
    pytest tests/ --cov=src
    flake8 src/ tests/
    mypy src/
    bandit -r src/
    black --check src/ tests/
    isort --check-only src/ tests/
```

```bash
# Exécution avec tox
tox -e flake8  # Juste flake8
tox -e py39    # Tests Python 3.9
tox -e all     # Toutes les vérifications
tox            # Tous les environnements
```

## Métriques de qualité du code

### radon : Complexité cyclomatique

```bash
pip install radon
```

```python
# exemple_complexite.py
def fonction_simple(x):
    """Fonction simple - complexité 1."""
    return x * 2

def fonction_complexe(x, y, z):
    """Fonction complexe - haute complexité."""
    if x > 0:
        if y > 0:
            if z > 0:
                if x > y:
                    if y > z:
                        return x + y + z
                    else:
                        return x + y - z
                else:
                    if y > z:
                        return x - y + z
                    else:
                        return x - y - z
            else:
                return x + y
        else:
            return x
    else:
        return 0

def fonction_refactorisee(x, y, z):
    """Version refactorisée - complexité réduite."""
    if x <= 0:
        return 0

    if y <= 0:
        return x

    if z <= 0:
        return x + y

    # Logique principale extraite
    return _calculer_resultat_complexe(x, y, z)

def _calculer_resultat_complexe(x, y, z):
    """Calcul complexe extrait en fonction séparée."""
    if x > y:
        return x + y + z if y > z else x + y - z
    else:
        return x - y + z if y > z else x - y - z
```

```bash
# Analyse de complexité avec radon
$ radon cc exemple_complexite.py -s

# Résultat :
exemple_complexite.py
    F 3:0 fonction_simple - A (1)
    F 7:0 fonction_complexe - F (23)  # Très complexe !
    F 25:0 fonction_refactorisee - B (6)  # Acceptable
    F 37:0 _calculer_resultat_complexe - B (4)  # Simple
```

### Métriques de maintenabilité

```bash
# Index de maintenabilité
$ radon mi exemple_complexite.py

# Résultat :
exemple_complexite.py - B (71.23)  # Score global acceptable
```

### Halstead metrics

```bash
# Métriques de Halstead (volume, difficulté, effort)
$ radon hal exemple_complexite.py

# Résultat détaillé des métriques de complexité algorithmique
```

## Création d'un linter personnalisé

### Plugin flake8 simple

```python
# mon_plugin_flake8.py
"""Plugin flake8 personnalisé pour détecter des patterns spécifiques."""

import ast
from typing import Generator, Tuple, Type

class FrenchCommentChecker:
    """
    Vérifie que les commentaires sont en français.

    Détecte les mots anglais courants dans les commentaires
    et suggère de les traduire en français.
    """

    name = "french-comments"
    version = "1.0.0"

    # Mots anglais courants à éviter
    ENGLISH_WORDS = {
        'TODO': 'À FAIRE',
        'FIXME': 'À CORRIGER',
        'NOTE': 'NOTE',
        'WARNING': 'ATTENTION',
        'BUG': 'BUG',
        'HACK': 'BIDOUILLE',
    }

    def __init__(self, tree: ast.AST):
        self.tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type], None, None]:
        """Exécute la vérification sur l'arbre AST."""
        # Pour ce plugin simple, on analyserait les commentaires
        # dans le code source (non disponible dans l'AST)
        # Ceci est un exemple de structure

        for node in ast.walk(self.tree):
            # Exemple : détecter des noms de fonction en anglais
            if isinstance(node, ast.FunctionDef):
                if self._is_english_function_name(node.name):
                    yield (
                        node.lineno,
                        node.col_offset,
                        f"FC001 Function name '{node.name}' should be in French",
                        type(self)
                    )

    def _is_english_function_name(self, name: str) -> bool:
        """Vérifie si un nom de fonction semble être en anglais."""
        english_verbs = ['get', 'set', 'create', 'delete', 'update', 'process']
        return any(verb in name.lower() for verb in english_verbs)

# Configuration du plugin
def plugin_factory():
    """Factory function pour le plugin."""
    return FrenchCommentChecker
```

### Utilisation du plugin

```python
# setup.py pour le plugin
from setuptools import setup

setup(
    name="flake8-french-comments",
    version="1.0.0",
    py_modules=["mon_plugin_flake8"],
    entry_points={
        "flake8.extension": [
            "FC = mon_plugin_flake8:FrenchCommentChecker"
        ]
    }
)
```

## Optimisation des performances des outils

### Configuration pour projets volumineux

```ini
# .flake8 - Optimisée pour gros projets
[flake8]
max-line-length = 88

# Exclusions pour accélérer l'analyse
exclude =
    .git,
    __pycache__,
    .venv,
    .tox,
    build,
    dist,
    *.egg-info,
    migrations,  # Fichiers générés automatiquement
    *_pb2.py,    # Fichiers protobuf générés

# Traitement en parallèle
jobs = auto

# Cache pour accélérer les exécutions répétées
cache-dir = .flake8-cache
```

### Scripts d'optimisation

```python
#!/usr/bin/env python3
"""
Script d'optimisation pour l'analyse de code.

Exécute les outils de linting de manière optimisée
pour de gros projets.
"""

import subprocess
import multiprocessing
import time
from pathlib import Path

def run_tool_parallel(tool_cmd, files_chunks):
    """
    Exécute un outil de linting en parallèle sur des chunks de fichiers.

    Args:
        tool_cmd: Commande de l'outil (ex: ['flake8'])
        files_chunks: Liste de listes de fichiers
    """
    def run_chunk(chunk):
        """Exécute l'outil sur un chunk de fichiers."""
        cmd = tool_cmd + chunk
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr

    # Exécution en parallèle
    with multiprocessing.Pool() as pool:
        results = pool.map(run_chunk, files_chunks)

    # Agrégation des résultats
    total_errors = 0
    for returncode, stdout, stderr in results:
        if returncode != 0:
            total_errors += 1
            print(stdout)
            if stderr:
                print(stderr)

    return total_errors

def optimize_linting():
    """Exécute le linting de manière optimisée."""
    print("🚀 Démarrage de l'analyse optimisée...")

    # Trouver tous les fichiers Python
    python_files = list(Path('.').rglob('*.py'))
    print(f"📁 {len(python_files)} fichiers Python trouvés")

    # Diviser en chunks pour le traitement parallèle
    chunk_size = max(1, len(python_files) // multiprocessing.cpu_count())
    chunks = [
        [str(f) for f in python_files[i:i + chunk_size]]
        for i in range(0, len(python_files), chunk_size)
    ]

    print(f"🔧 Traitement en {len(chunks)} chunks parallèles")

    # Outils à exécuter
    tools = [
        (['flake8'], "Flake8"),
        (['black', '--check'], "Black"),
        (['isort', '--check-only'], "isort"),
    ]

    total_time = 0
    for tool_cmd, tool_name in tools:
        print(f"\n🔍 Exécution de {tool_name}...")
        start_time = time.time()

        errors = run_tool_parallel(tool_cmd, chunks)

        elapsed = time.time() - start_time
        total_time += elapsed

        status = "✅" if errors == 0 else f"❌ ({errors} erreurs)"
        print(f"   {status} {tool_name} - {elapsed:.2f}s")

    print(f"\n⏱️  Temps total: {total_time:.2f}s")
    print("✨ Analyse terminée !")

if __name__ == '__main__':
    optimize_linting()
```

## Documentation et formation de l'équipe

### Guide rapide pour nouveaux développeurs

```markdown
# Guide Qualité du Code - Démarrage Rapide

## Installation des outils

```bash
# Installation en une commande
pip install black isort flake8 pylint mypy pre-commit

# Configuration des hooks pre-commit
pre-commit install
```

## Workflow quotidien

### Avant de commiter :

```bash
# 1. Formatage automatique
black .
isort .

# 2. Vérification
flake8 .
mypy src/

# 3. Tests
pytest
```

### Configuration IDE recommandée

**VS Code** : Installer les extensions Python, Black, isort, Flake8

**PyCharm** : Activer l'inspection PEP 8, configurer Black comme formateur

## Règles d'équipe

1. **Toujours** formater avec Black avant de commiter
2. **Jamais** ignorer les warnings flake8 sans justification
3. **Documenter** toutes les fonctions publiques
4. **Tester** le code avant de push

## Résolution de problèmes courants

### "Ligne trop longue"
```python
# ❌ Trop long
fonction_avec_beaucoup_de_parametres(param1, param2, param3, param4, param5)

# ✅ Divisé
fonction_avec_beaucoup_de_parametres(
    param1, param2, param3,
    param4, param5
)
```

### "Import mal organisé"
```bash
# Correction automatique
isort nom_du_fichier.py
```

### "Variable non utilisée"
```python
# ❌ Variable inutilisée
def ma_fonction():
    variable_inutile = 42
    return "résultat"

# ✅ Variable supprimée ou préfixée par _
def ma_fonction():
    _variable_debug = 42  # Variable de debug temporaire
    return "résultat"
```
```

### Formation progressive de l'équipe

```python
# semaine_1_formation.py
"""
Semaine 1 : Les bases de PEP 8

Exercices pratiques pour s'habituer aux bonnes pratiques.
"""

# Exercice 1 : Corriger le formatage
def exercice1():
    """Corrigez le code suivant selon PEP 8."""

    # Code à corriger :
    def maFonction(param1,param2,param3=None):
        if param3==None:param3=[]
        result={'a':param1,'b':param2,'c':param3}
        return result

    # TODO: Réécrivez cette fonction selon PEP 8

### Exercice 1 : Corriger le formatage - CORRIGÉ

```python
def exercice1():
    """Corrigez le code suivant selon PEP 8."""

    # ❌ Code original (problématique)
    def maFonction(param1,param2,param3=None):
        if param3==None:param3=[]
        result={'a':param1,'b':param2,'c':param3}
        return result

    # ✅ Version corrigée selon PEP 8
    def ma_fonction(param1, param2, param3=None):
        """
        Fonction corrigée selon les standards PEP 8.

        Args:
            param1: Premier paramètre
            param2: Deuxième paramètre
            param3: Troisième paramètre optionnel

        Returns:
            dict: Dictionnaire avec les valeurs
        """
        if param3 is None:
            param3 = []

        result = {
            'a': param1,
            'b': param2,
            'c': param3
        }
        return result

# Corrections appliquées :
# 1. maFonction -> ma_fonction (snake_case)
# 2. Espaces après les virgules dans les paramètres
# 3. param3==None -> param3 is None (comparaison correcte)
# 4. param3=[] -> param3 = [] (espaces autour de =)
# 5. Dictionnaire formaté sur plusieurs lignes pour lisibilité
# 6. Ajout d'une docstring complète
# 7. Espaces autour des opérateurs
```

# Exercice 2 : Nommage correct
def exercice2():
    """Corrigez les noms de variables."""

    # Noms incorrects à corriger :
    userName = "Alice"
    user_Age = 30
    USERADDRESS = "123 Main St"

    # TODO: Renommez selon les conventions Python

### Exercice 2 : Nommage correct - CORRIGÉ

```python
def exercice2():
    """Corrigez les noms de variables."""

    # ❌ Noms incorrects à corriger
    userName = "Alice"      # camelCase -> snake_case
    user_Age = 30          # Mélange de styles -> snake_case
    USERADDRESS = "123 Main St"  # SCREAMING_CASE -> snake_case

    # ✅ Noms corrigés selon PEP 8
    user_name = "Alice"     # snake_case pour variables
    user_age = 30          # snake_case cohérent
    user_address = "123 Main St"  # snake_case pour variables

    # Exemples supplémentaires de nommage correct

    # Variables et fonctions : snake_case
    first_name = "Alice"
    last_name = "Dupont"
    birth_date = "1990-01-01"

    def calculate_total_price(base_price, tax_rate):
        """Calcule le prix total avec taxes."""
        return base_price * (1 + tax_rate)

    # Classes : PascalCase
    class UserAccount:
        """Compte utilisateur."""
        pass

    class DataProcessor:
        """Processeur de données."""
        pass

    # Constantes : SCREAMING_SNAKE_CASE
    MAX_RETRY_ATTEMPTS = 3
    DEFAULT_TIMEOUT = 30
    API_BASE_URL = "https://api.example.com"

    # Variables privées : préfixe _
    _internal_cache = {}
    _debug_mode = False

    return {
        'user_name': user_name,
        'user_age': user_age,
        'user_address': user_address
    }

# Règles de nommage PEP 8 :
# - Variables/fonctions : snake_case (mots_separes_par_underscores)
# - Classes : PascalCase (MotsCollesAvecMajuscules)
# - Constantes : SCREAMING_SNAKE_CASE (TOUT_EN_MAJUSCULES)
# - Privé : préfixe _ (_variable_privee)
# - Très privé : préfixe __ (__variable_tres_privee)
```

# Exercice 3 : Imports et structure
def exercice3():
    """Organisez les imports et la structure."""

    # Imports désorganisés :
    from pathlib import Path
    import os
    import requests
    import sys
    from django.conf import settings
    import json

    # TODO: Réorganisez selon PEP 8
```

### Exercice 3 : Imports et structure - CORRIGÉ

```python
def exercice3():
    """Organisez les imports et la structure."""

    # ❌ Imports désorganisés (version originale)
    """
    from pathlib import Path
    import os
    import requests
    import sys
    from django.conf import settings
    import json
    """

    # ✅ Imports réorganisés selon PEP 8
    pass

# Fichier réorganisé complet selon PEP 8 :

# 1. Imports de la bibliothèque standard (par ordre alphabétique)
import json
import os
import sys
from pathlib import Path

# 2. Imports de bibliothèques tierces (par ordre alphabétique)
import requests
from django.conf import settings

# 3. Imports locaux (si applicable)
# from mon_app.models import User
# from . import local_module

# Règles d'organisation des imports PEP 8 :
# 1. Bibliothèque standard Python
# 2. Bibliothèques tierces installées via pip
# 3. Modules locaux de votre application
#
# Dans chaque groupe :
# - import xxx avant from xxx import yyy
# - Ordre alphabétique
# - Une ligne vide entre chaque groupe
# - Pas d'imports multiples sur une ligne (import os, sys ❌)
# - Pas d'import * sauf cas très spéciaux

def exemple_utilisation():
    """Exemple d'utilisation des modules importés."""
    # Utilisation de pathlib
    config_path = Path("config.json")

    # Utilisation de os
    current_dir = os.getcwd()

    # Utilisation de json
    data = {"key": "value"}
    json_str = json.dumps(data)

    # Utilisation de requests
    response = requests.get("https://api.example.com")

    return {
        'config_path': str(config_path),
        'current_dir': current_dir,
        'json_data': json_str,
        'api_status': response.status_code if 'response' in locals() else None
    }
```

## Métriques et tableaux de bord

### Script de rapport qualité

```python
#!/usr/bin/env python3
"""
Générateur de rapport de qualité du code.

Collecte les métriques de différents outils et génère
un rapport consolidé.
"""

import subprocess
import json
from datetime import datetime
from pathlib import Path

class QualityReporter:
    """Générateur de rapports de qualité."""

    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.metrics = {}

    def collect_flake8_metrics(self):
        """Collecte les métriques flake8."""
        try:
            result = subprocess.run(
                ['flake8', '--statistics', self.project_path],
                capture_output=True, text=True
            )

            # Parser les statistiques flake8
            lines = result.stdout.strip().split('\n')
            errors = {}
            for line in lines:
                if line and not line.startswith('Total'):
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        count = int(parts[0])
                        error_code = parts[1]
                        errors[error_code] = count

            self.metrics['flake8'] = {
                'total_errors': sum(errors.values()),
                'errors_by_type': errors,
                'status': 'pass' if result.returncode == 0 else 'fail'
            }
        except Exception as e:
            self.metrics['flake8'] = {'error': str(e)}

    def collect_complexity_metrics(self):
        """Collecte les métriques de complexité avec radon."""
        try:
            result = subprocess.run(
                ['radon', 'cc', self.project_path, '-j'],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                complexity_data = json.loads(result.stdout)

                # Analyser la complexité
                total_functions = 0
                high_complexity = 0

                for file_data in complexity_data.values():
                    for item in file_data:
                        if item['type'] == 'function':
                            total_functions += 1
                            if item['complexity'] > 10:
                                high_complexity += 1

                self.metrics['complexity'] = {
                    'total_functions': total_functions,
                    'high_complexity_functions': high_complexity,
                    'complexity_ratio': high_complexity / max(total_functions, 1)
                }
        except Exception as e:
            self.metrics['complexity'] = {'error': str(e)}

    def collect_test_coverage(self):
        """Collecte les métriques de couverture de tests."""
        try:
            # Exécuter coverage
            subprocess.run(['coverage', 'run', '-m', 'pytest'],
                          capture_output=True)

            result = subprocess.run(
                ['coverage', 'json'],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                coverage_data = json.loads(result.stdout)

                self.metrics['coverage'] = {
                    'percentage': coverage_data['totals']['percent_covered'],
                    'lines_covered': coverage_data['totals']['covered_lines'],
                    'lines_total': coverage_data['totals']['num_statements'],
                    'missing_lines': coverage_data['totals']['missing_lines']
                }
        except Exception as e:
            self.metrics['coverage'] = {'error': str(e)}

    def generate_report(self):
        """Génère le rapport final."""
        self.collect_flake8_metrics()
        self.collect_complexity_metrics()
        self.collect_test_coverage()

        # Calculer un score global
        score = self._calculate_quality_score()

        # Générer le rapport
        report = {
            'timestamp': datetime.now().isoformat(),
            'project_path': str(self.project_path),
            'quality_score': score,
            'metrics': self.metrics,
            'recommendations': self._generate_recommendations()
        }

        return report

    def _calculate_quality_score(self):
        """Calcule un score de qualité global (0-100)."""
        score = 100

        # Pénalité pour erreurs flake8
        if 'flake8' in self.metrics and 'total_errors' in self.metrics['flake8']:
            errors = self.metrics['flake8']['total_errors']
            score -= min(errors * 2, 30)  # Max 30 points de pénalité

        # Pénalité pour complexité élevée
        if 'complexity' in self.metrics and 'complexity_ratio' in self.metrics['complexity']:
            complexity_ratio = self.metrics['complexity']['complexity_ratio']
            score -= complexity_ratio * 20  # Max 20 points de pénalité

        # Bonus/pénalité pour couverture
        if 'coverage' in self.metrics and 'percentage' in self.metrics['coverage']:
            coverage = self.metrics['coverage']['percentage']
            if coverage >= 90:
                score += 10
            elif coverage < 60:
                score -= 20

        return max(0, min(100, score))

    def _generate_recommendations(self):
        """Génère des recommandations d'amélioration."""
        recommendations = []

        # Recommandations basées sur flake8
        if 'flake8' in self.metrics and 'total_errors' in self.metrics['flake8']:
            errors = self.metrics['flake8']['total_errors']
            if errors > 0:
                recommendations.append({
                    'type': 'style',
                    'priority': 'high' if errors > 50 else 'medium',
                    'message': f"Corriger {errors} erreur(s) de style PEP 8",
                    'action': "Exécuter 'black .' puis 'isort .' pour auto-correction"
                })

        # Recommandations basées sur la complexité
        if 'complexity' in self.metrics:
            if self.metrics['complexity'].get('high_complexity_functions', 0) > 0:
                count = self.metrics['complexity']['high_complexity_functions']
                recommendations.append({
                    'type': 'complexity',
                    'priority': 'high',
                    'message': f"{count} fonction(s) avec complexité élevée",
                    'action': "Refactoriser en divisant les fonctions complexes"
                })

        # Recommandations basées sur la couverture
        if 'coverage' in self.metrics and 'percentage' in self.metrics['coverage']:
            coverage = self.metrics['coverage']['percentage']
            if coverage < 80:
                recommendations.append({
                    'type': 'testing',
                    'priority': 'high' if coverage < 60 else 'medium',
                    'message': f"Couverture de tests faible ({coverage:.1f}%)",
                    'action': "Ajouter des tests pour les parties non couvertes"
                })

        return recommendations

    def save_report(self, filename='quality_report.json'):
        """Sauvegarde le rapport dans un fichier."""
        report = self.generate_report()

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        return report

    def print_summary(self):
        """Affiche un résumé du rapport."""
        report = self.generate_report()

        print("📊 RAPPORT DE QUALITÉ DU CODE")
        print("=" * 50)
        print(f"📅 Date: {report['timestamp'][:19]}")
        print(f"🎯 Score global: {report['quality_score']:.1f}/100")

        # Métriques détaillées
        if 'flake8' in report['metrics']:
            flake8_data = report['metrics']['flake8']
            if 'total_errors' in flake8_data:
                errors = flake8_data['total_errors']
                status = "✅" if errors == 0 else f"❌ {errors} erreurs"
                print(f"📏 Style PEP 8: {status}")

        if 'complexity' in report['metrics']:
            complexity_data = report['metrics']['complexity']
            if 'high_complexity_functions' in complexity_data:
                high_complex = complexity_data['high_complexity_functions']
                total = complexity_data['total_functions']
                status = "✅" if high_complex == 0 else f"⚠️ {high_complex}/{total}"
                print(f"🔧 Complexité: {status}")

        if 'coverage' in report['metrics']:
            coverage_data = report['metrics']['coverage']
            if 'percentage' in coverage_data:
                pct = coverage_data['percentage']
                emoji = "✅" if pct >= 90 else "⚠️" if pct >= 70 else "❌"
                print(f"🧪 Couverture: {emoji} {pct:.1f}%")

        # Recommandations
        recommendations = report.get('recommendations', [])
        if recommendations:
            print(f"\n💡 RECOMMANDATIONS ({len(recommendations)}):")
            for i, rec in enumerate(recommendations, 1):
                priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
                emoji = priority_emoji.get(rec['priority'], "🔵")
                print(f"  {i}. {emoji} {rec['message']}")
                print(f"     → {rec['action']}")
        else:
            print("\n🎉 Aucune amélioration recommandée !")

def main():
    """Point d'entrée principal."""
    import argparse

    parser = argparse.ArgumentParser(description="Générateur de rapport qualité")
    parser.add_argument('--path', default='.', help='Chemin du projet')
    parser.add_argument('--output', help='Fichier de sortie JSON')
    parser.add_argument('--summary', action='store_true',
                       help='Afficher uniquement le résumé')

    args = parser.parse_args()

    reporter = QualityReporter(args.path)

    if args.summary:
        reporter.print_summary()
    elif args.output:
        report = reporter.save_report(args.output)
        print(f"📄 Rapport sauvegardé dans {args.output}")
        print(f"🎯 Score: {report['quality_score']:.1f}/100")
    else:
        reporter.print_summary()

if __name__ == '__main__':
    main()
```

## Exercices pratiques

### Exercice 1 : Diagnostic et correction

```python
# diagnostic_exercice.py - Code à corriger
import os,sys,json
from pathlib import Path
import requests,time

def getUserData(userID,includeDetails=True):
    if userID==None:
        return None
    userData={'id':userID}
    if includeDetails==True:
        detailsData=requests.get('https://api.example.com/users/'+str(userID)+'/details')
        if detailsData.status_code==200:
            userData.update(detailsData.json())
    return userData

class dataProcessor:
    def __init__(self,dataPath):
        self.dataPath=dataPath
        self.processedData=[]

    def processFile(self,fileName):
        filePath=os.path.join(self.dataPath,fileName)
        if os.path.exists(filePath)==False:
            print('File not found: '+fileName)
            return False
        with open(filePath,'r') as f:
            data=json.load(f)
        processedItems=[]
        for item in data:
            if item['status']=='active' and item['priority']>5:
                processedItem={'id':item['id'],'name':item['name'],'score':item['priority']*2}
                processedItems.append(processedItem)
        self.processedData.extend(processedItems)
        return True

# Mission : Corrigez ce code pour qu'il respecte PEP 8
# 1. Utilisez flake8 pour identifier les problèmes
# 2. Corrigez manuellement ou avec black/isort
# 3. Vérifiez avec mypy (ajoutez les type hints)
# 4. Améliorez les docstrings
```

### Exercice 2 : Configuration d'un nouveau projet

```bash
# Créez un nouveau projet avec configuration complète
mkdir mon_nouveau_projet
cd mon_nouveau_projet

# Mission :
# 1. Configurez pyproject.toml avec black, isort, flake8
# 2. Créez .pre-commit-config.yaml
# 3. Configurez VS Code (.vscode/settings.json)
# 4. Créez un Makefile avec les commandes quality
# 5. Testez avec un fichier Python exemple
```

### Exercice 3 : Plugin personnalisé

```python
# Créez un plugin flake8 qui détecte :
# 1. Les fonctions sans docstring de plus de 10 lignes
# 2. Les variables avec des noms en français (contraire de l'exercice précédent)
# 3. Les imports non utilisés depuis plus de 30 jours (avancé)

class MonPluginPersonnalise:
    """Plugin flake8 personnalisé."""

    name = "mon-plugin"
    version = "1.0.0"

    def __init__(self, tree, lines):
        self.tree = tree
        self.lines = lines

    def run(self):
        """À implémenter selon vos règles."""
        # TODO: Implémentez vos vérifications personnalisées
        pass
```

## Exercices pratiques - Corrigés

Voici des corrections **humainement réalistes** (ce qu'un apprenant écrirait vraiment) :

## Exercice 1 : Diagnostic et correction - Version corrigée

```python
# diagnostic_exercice.py - VERSION CORRIGÉE (réaliste)

import json
import os
from pathlib import Path

import requests


def get_user_data(user_id, include_details=True):
    """Récupère les données utilisateur."""
    if user_id is None:
        return None

    user_data = {'id': user_id}

    if include_details:
        response = requests.get(f'https://api.example.com/users/{user_id}/details')
        if response.status_code == 200:
            user_data.update(response.json())

    return user_data


class DataProcessor:
    """Traite les fichiers de données."""

    def __init__(self, data_path):
        self.data_path = data_path
        self.processed_data = []

    def process_file(self, file_name):
        """Traite un fichier JSON."""
        file_path = os.path.join(self.data_path, file_name)

        if not os.path.exists(file_path):
            print(f'File not found: {file_name}')
            return False

        with open(file_path, 'r') as f:
            data = json.load(f)

        processed_items = []
        for item in data:
            if item['status'] == 'active' and item['priority'] > 5:
                processed_item = {
                    'id': item['id'],
                    'name': item['name'],
                    'score': item['priority'] * 2
                }
                processed_items.append(processed_item)

        self.processed_data.extend(processed_items)
        return True
```

**Corrections appliquées (30 lignes au lieu de 200+) :**
- Imports réorganisés
- `getUserData` → `get_user_data`
- `dataProcessor` → `DataProcessor`
- Espaces autour des opérateurs
- f-strings pour la concaténation
- Docstrings simples
- `==None` → `is None`

## Exercice 2 : Configuration projet - Version corrigée

```toml
# pyproject.toml (fichier principal)
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.flake8]
max-line-length = 88
ignore = "E203,W503"
```

```yaml
# .pre-commit-config.yaml (basique)
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.11.4
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

```json
# .vscode/settings.json (essentiel)
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.lintOnSave": true
}
```

```makefile
# Makefile (simple)
format:
	black .
	isort .

lint:
	flake8 .

check: format lint
	@echo "✅ Vérifications terminées"
```

## Exercice 3 : Plugin personnalisé - Version corrigée

```python
# mon_plugin_flake8.py (30 lignes max!)
import ast

class MonPluginPersonnalise:
    """Plugin flake8 personnalisé."""

    name = "mon-plugin"
    version = "1.0.0"

    def __init__(self, tree, lines):
        self.tree = tree
        self.lines = lines

    def run(self):
        """Vérifie les fonctions longues sans docstring."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                # Compter approximativement les lignes
                line_count = getattr(node, 'end_lineno', node.lineno + 10) - node.lineno

                # Vérifier docstring
                has_docstring = (
                    node.body and
                    isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, (ast.Str, ast.Constant))
                )

                if line_count > 10 and not has_docstring:
                    yield (
                        node.lineno,
                        0,
                        f"MP001 Function '{node.name}' is long but has no docstring",
                        type(self)
                    )
```

## Intégration avec les équipes et l'organisation

### Politique qualité d'équipe

```markdown
# Politique Qualité Code - Équipe Python

## Standards obligatoires

### 🔴 Bloquants (empêchent le merge)
- Score flake8 = 0 erreur
- Couverture de tests > 80%
- Toutes les fonctions publiques documentées
- Aucune fonction avec complexité > 15

### 🟡 Avertissements (review requise)
- Couverture de tests entre 70-80%
- Fonctions avec complexité 10-15
- Imports non utilisés
- Variables mal nommées

### 🟢 Recommandations
- Utilisation de type hints
- Docstrings avec exemples
- Optimisations de performance

## Processus de review

1. **Auto-vérification** : Développeur lance `make check-all`
2. **CI/CD** : Pipeline automatique vérifie qualité
3. **Review humaine** : Focus sur logique et architecture
4. **Merge** : Seulement si tous les checks passent

## Exceptions et dérogations

- **Legacy code** : Standards assouplis temporairement
- **Code généré** : Exclusion des vérifications
- **Performance critique** : Dérogation avec justification documentée
```

### Métriques d'équipe

```python
# team_metrics.py
"""
Collecteur de métriques qualité pour l'équipe.

Analyse l'historique Git pour suivre l'évolution
de la qualité du code de l'équipe.
"""

import subprocess
import json
from datetime import datetime, timedelta
from collections import defaultdict

class TeamQualityMetrics:
    """Collecte les métriques qualité de l'équipe."""

    def __init__(self, repo_path='.'):
        self.repo_path = repo_path
        self.metrics = defaultdict(list)

    def collect_historical_data(self, days=30):
        """
        Collecte les données historiques sur N jours.

        Args:
            days: Nombre de jours d'historique à analyser
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Obtenir les commits dans la période
        cmd = [
            'git', 'log',
            f'--since={start_date.isoformat()}',
            '--format=%H|%an|%ad|%s',
            '--date=iso'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        commits = []

        for line in result.stdout.strip().split('\n'):
            if line:
                hash_val, author, date, message = line.split('|', 3)
                commits.append({
                    'hash': hash_val,
                    'author': author,
                    'date': date,
                    'message': message
                })

        # Analyser chaque commit
        for commit in commits:
            self._analyze_commit(commit)

    def _analyze_commit(self, commit):
        """Analyse un commit pour extraire les métriques qualité."""
        # Checkout du commit (attention : modifie l'état du repo)
        subprocess.run(['git', 'checkout', commit['hash']],
                      capture_output=True)

        try:
            # Analyser la qualité à ce moment
            quality_data = {
                'commit': commit['hash'],
                'author': commit['author'],
                'date': commit['date'],
                'flake8_errors': self._count_flake8_errors(),
                'test_coverage': self._get_test_coverage(),
                'complexity': self._get_avg_complexity()
            }

            self.metrics[commit['author']].append(quality_data)

        finally:
            # Retourner à HEAD
            subprocess.run(['git', 'checkout', 'HEAD'],
                          capture_output=True)

    def _count_flake8_errors(self):
        """Compte les erreurs flake8 actuelles."""
        try:
            result = subprocess.run(['flake8', '.'],
                                  capture_output=True, text=True)
            return len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
        except:
            return 0

    def _get_test_coverage(self):
        """Obtient le pourcentage de couverture actuel."""
        try:
            subprocess.run(['coverage', 'run', '-m', 'pytest'],
                          capture_output=True)
            result = subprocess.run(['coverage', 'json'],
                                  capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return data['totals']['percent_covered']
        except:
            pass
        return 0

    def _get_avg_complexity(self):
        """Calcule la complexité moyenne."""
        try:
            result = subprocess.run(['radon', 'cc', '.', '-j'],
                                  capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                complexities = []
                for file_data in data.values():
                    for item in file_data:
                        if item['type'] == 'function':
                            complexities.append(item['complexity'])
                return sum(complexities) / len(complexities) if complexities else 0
        except:
            pass
        return 0

    def generate_team_report(self):
        """Génère un rapport pour l'équipe."""
        report = {
            'team_summary': {},
            'individual_progress': {},
            'recommendations': []
        }

        # Analyse par développeur
        for author, commits_data in self.metrics.items():
            if not commits_data:
                continue

            # Évolution des métriques
            latest = commits_data[-1]
            oldest = commits_data[0]

            flake8_trend = latest['flake8_errors'] - oldest['flake8_errors']
            coverage_trend = latest['test_coverage'] - oldest['test_coverage']

            report['individual_progress'][author] = {
                'commits_analyzed': len(commits_data),
                'current_quality_score': self._calculate_score(latest),
                'flake8_trend': flake8_trend,
                'coverage_trend': coverage_trend,
                'avg_complexity': sum(c['complexity'] for c in commits_data) / len(commits_data)
            }

        # Recommandations d'équipe
        report['recommendations'] = self._generate_team_recommendations()

        return report

    def _calculate_score(self, metrics):
        """Calcule un score de qualité pour un commit."""
        score = 100
        score -= min(metrics['flake8_errors'] * 2, 40)
        score += min(metrics['test_coverage'] - 60, 20) if metrics['test_coverage'] > 60 else 0
        score -= min(metrics['complexity'] - 5, 20) if metrics['complexity'] > 5 else 0
        return max(0, score)

    def _generate_team_recommendations(self):
        """Génère des recommandations pour l'équipe."""
        recommendations = []

        # Analyser les tendances globales
        all_latest = [commits[-1] for commits in self.metrics.values() if commits]

        if all_latest:
            avg_errors = sum(c['flake8_errors'] for c in all_latest) / len(all_latest)
            avg_coverage = sum(c['test_coverage'] for c in all_latest) / len(all_latest)

            if avg_errors > 10:
                recommendations.append({
                    'type': 'team_training',
                    'message': 'Formation PEP 8 recommandée pour l\'équipe',
                    'priority': 'high'
                })

            if avg_coverage < 70:
                recommendations.append({
                    'type': 'testing_culture',
                    'message': 'Renforcer la culture des tests dans l\'équipe',
                    'priority': 'high'
                })

        return recommendations

# Utilisation
def main():
    """Génère un rapport pour l'équipe."""
    metrics = TeamQualityMetrics()
    metrics.collect_historical_data(days=30)
    report = metrics.generate_team_report()

    print("📊 RAPPORT QUALITÉ ÉQUIPE - 30 DERNIERS JOURS")
    print("=" * 60)

    for author, data in report['individual_progress'].items():
        score = data['current_quality_score']
        trends = []

        if data['flake8_trend'] < 0:
            trends.append("📈 Style amélioré")
        elif data['flake8_trend'] > 0:
            trends.append("📉 Style dégradé")

        if data['coverage_trend'] > 0:
            trends.append("🧪 Tests renforcés")
        elif data['coverage_trend'] < 0:
            trends.append("⚠️ Couverture réduite")

        trend_str = " | ".join(trends) if trends else "➡️ Stable"

        print(f"\n👤 {author}")
        print(f"   🎯 Score: {score:.1f}/100")
        print(f"   📈 Tendance: {trend_str}")
        print(f"   💻 Commits analysés: {data['commits_analyzed']}")

    # Recommandations
    recommendations = report['recommendations']
    if recommendations:
        print(f"\n💡 RECOMMANDATIONS ÉQUIPE:")
        for rec in recommendations:
            priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
            emoji = priority_emoji.get(rec['priority'], "🔵")
            print(f"   {emoji} {rec['message']}")

if __name__ == '__main__':
    main()
```

## Résumé et bonnes pratiques

PEP 8 et les outils de linting sont vos alliés pour un code Python professionnel :

### **PEP 8 - Les règles essentielles :**
- **Indentation** : 4 espaces (jamais de tabs)
- **Longueur de ligne** : 79-88 caractères maximum
- **Espaces** : Autour des opérateurs et après les virgules
- **Nommage** : snake_case pour variables/fonctions, PascalCase pour classes
- **Imports** : Organisés et groupés (stdlib, tiers, locaux)

### **Outils indispensables :**
- **Black** : Formatage automatique sans discussion
- **isort** : Organisation automatique des imports
- **flake8** : Vérification style et erreurs basiques
- **pylint** : Analyse approfondie et détection d'erreurs
- **mypy** : Vérification de types statique

### **Workflow recommandé :**
1. **Formatage automatique** : Black + isort avant chaque commit
2. **Vérification continue** : flake8 + pylint dans l'éditeur
3. **Automatisation** : pre-commit hooks pour la cohérence
4. **CI/CD** : Pipeline automatique pour validation
5. **Métriques** : Suivi de la qualité dans le temps

### **Configuration projet type :**
```toml
# pyproject.toml minimal
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.flake8]
max-line-length = 88
extend-ignore = "E203,W503"
```

### **Pour l'équipe :**
- Standards partagés et documentés
- Formation progressive des nouveaux développeurs
- Métriques d'équipe pour suivre les progrès
- Flexibility raisonnable selon le contexte

### **Règles d'or :**
- **Consistance** > Perfection : Mieux vaut un style cohérent qu'un style parfait mais incohérent
- **Automatisation** > Discipline : Les outils automatiques évitent les oublis
- **Pragmatisme** > Dogmatisme : Les règles servent le code, pas l'inverse
- **Évolution** > Révolution : Améliorer progressivement plutôt que tout changer d'un coup

Un code respectant PEP 8 et vérifié par des outils de qualité est plus facile à lire, maintenir et faire évoluer. C'est un investissement qui se rentabilise rapidement en réduisant les bugs et accélérant le développement !

---

**À retenir :** Un code bien formaté, c'est comme une maison bien rangée : on trouve tout plus facilement et on a envie d'y passer du temps !

⏭️
