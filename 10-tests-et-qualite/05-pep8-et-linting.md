🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.5 PEP 8 et outils de linting

## Introduction au style de code

### Pourquoi un style de code cohérent ?

Imaginez que vous lisiez un livre où chaque chapitre est écrit dans un style différent : différentes polices, espacements, façons de ponctuer... Ce serait difficile à lire ! C'est la même chose pour le code.

**Un code bien stylé est** :
- Plus facile à lire
- Plus facile à maintenir
- Plus professionnel
- Plus facile à partager

**Analogie** : Le style de code, c'est comme la grammaire et l'orthographe pour l'écriture. Un texte peut être compréhensible avec des fautes, mais il est beaucoup plus agréable à lire quand il est bien écrit.

### Le code se lit plus qu'il ne s'écrit

Un programme est lu beaucoup plus souvent qu'il n'est écrit. Un style cohérent rend cette lecture plus fluide et permet de se concentrer sur la logique plutôt que sur la forme.

```python
# ❌ Code difficile à lire
def calcul(x,y,z):a=x+y;b=a*z;return b

# ✅ Code facile à lire
def calculer_total(prix, quantite, taux_taxe):
    sous_total = prix + quantite
    total = sous_total * taux_taxe
    return total
```

---

## Qu'est-ce que PEP 8 ?

### Définition

**PEP 8** (Python Enhancement Proposal 8) est le guide de style officiel pour le code Python. C'est un document qui décrit les conventions de codage recommandées par la communauté Python.

**Créé en 2001** par Guido van Rossum (le créateur de Python), Barry Warsaw et Nick Coghlan, PEP 8 est devenu la référence pour écrire du code Python lisible et cohérent.

### PEP 8 n'est pas obligatoire

PEP 8 contient des **recommandations**, pas des règles strictes. Votre code fonctionnera même si vous ne suivez pas PEP 8. Cependant :

- La plupart des projets Python professionnels suivent PEP 8
- C'est une convention largement acceptée
- Cela facilite la collaboration
- Les outils automatiques l'utilisent comme référence

### La règle d'or de PEP 8

> "La cohérence est importante. La cohérence au sein d'un projet est plus importante. La cohérence au sein d'un module ou d'une fonction est la plus importante."

Si votre projet utilise déjà un style différent, restez cohérent avec ce style plutôt que de suivre PEP 8 aveuglément.

---

## Les règles principales de PEP 8

### 1. Indentation

**Règle** : Utilisez **4 espaces** par niveau d'indentation (jamais de tabulations).

```python
# ✅ Bon - 4 espaces
def ma_fonction():
    if condition:
        faire_quelque_chose()
        faire_autre_chose()

# ❌ Mauvais - 2 espaces ou tabulation
def ma_fonction():
  if condition:
    faire_quelque_chose()
```

**Configuration de l'éditeur** : Configurez votre éditeur pour insérer 4 espaces quand vous appuyez sur Tab.

### 2. Longueur des lignes

**Règle** : Maximum **79 caractères** par ligne (88 avec Black).

```python
# ✅ Bon
resultat = calculer_moyenne(
    donnees_utilisateur,
    filtre_actif=True,
    inclure_valeurs_nulles=False
)

# ❌ Mauvais - ligne trop longue
resultat = calculer_moyenne(donnees_utilisateur, filtre_actif=True, inclure_valeurs_nulles=False, mode="complet")
```

**Pourquoi 79 caractères ?**
- Permet d'avoir deux fichiers côte à côte sur un écran standard
- Facilite la lecture (les yeux se fatiguent avec de longues lignes)
- Compatible avec tous les terminaux

### 3. Lignes vides

**Règle** : Utilisez des lignes vides pour organiser le code.

```python
# ✅ Bon
import os
import sys

CONSTANTE = 42


class MaClasse:
    """Documentation de la classe."""

    def __init__(self):
        self.attribut = None

    def methode1(self):
        pass

    def methode2(self):
        pass


def fonction_globale():
    pass


# ❌ Mauvais - manque de séparation
import os
import sys
CONSTANTE = 42
class MaClasse:
    def __init__(self):
        self.attribut = None
    def methode1(self):
        pass
def fonction_globale():
    pass
```

**Convention** :
- 2 lignes vides avant les classes et fonctions de niveau module
- 1 ligne vide entre les méthodes d'une classe
- 1 ligne vide pour séparer des groupes logiques dans une fonction

### 4. Importations

**Règle** : Organisez les imports de manière structurée.

```python
# ✅ Bon - imports organisés
# 1. Bibliothèque standard
import os
import sys
from datetime import datetime

# 2. Bibliothèques tierces
import numpy as np
import pandas as pd
import requests

# 3. Imports locaux
from mon_package import ma_fonction
from mon_package.module import MaClasse

# ❌ Mauvais - imports désorganisés
from mon_package import ma_fonction
import sys
import requests, pandas
from datetime import *
import os
```

**Règles pour les imports** :
- Un import par ligne (sauf pour `from X import A, B`)
- Grouper en 3 catégories : standard, tierce, local
- Séparer chaque groupe par une ligne vide
- Ordre alphabétique dans chaque groupe
- Éviter `from module import *`

### 5. Espaces autour des opérateurs

**Règle** : Un espace autour des opérateurs, pas d'espace avant les parenthèses.

```python
# ✅ Bon
x = 5
y = x + 10
resultat = fonction(a, b, c)
liste = [1, 2, 3, 4]
dico = {'cle': 'valeur'}

# ❌ Mauvais
x=5
y = x+10
resultat = fonction (a,b,c)
liste = [1,2,3,4]
dico = {'cle':'valeur'}
```

**Détails** :
- Espace autour de `=`, `+`, `-`, `*`, `/`, `==`, etc.
- Pas d'espace avant `:` dans les dictionnaires et slices
- Pas d'espace avant `(` dans les appels de fonction
- Pas d'espace à l'intérieur des parenthèses/crochets

### 6. Nommage des variables

**Règle** : Suivez les conventions de nommage Python.

```python
# ✅ Bon
# Variables et fonctions : snake_case
ma_variable = 42
nombre_total = 100
def calculer_moyenne():
    pass

# Classes : PascalCase
class CompteBancaire:
    pass

class GestionnaireUtilisateurs:
    pass

# Constantes : UPPER_CASE
PI = 3.14159
MAX_CONNEXIONS = 100
CHEMIN_CONFIG = "/etc/config"

# Variables "privées" : _prefixe
class MaClasse:
    def __init__(self):
        self._attribut_prive = None

    def _methode_privee(self):
        pass

# ❌ Mauvais
MaVariable = 42  # Variable en PascalCase
def CalculerMoyenne():  # Fonction en PascalCase
    pass
class compte_bancaire:  # Classe en snake_case
    pass
pi = 3.14159  # Constante en minuscules
```

**Convention de nommage complète** :

| Type | Convention | Exemple |
|------|------------|---------|
| Variable | snake_case | `ma_variable` |
| Fonction | snake_case | `calculer_total()` |
| Classe | PascalCase | `CompteBancaire` |
| Constante | UPPER_CASE | `MAX_SIZE` |
| Module | snake_case | `mon_module.py` |
| Privé | _prefixe | `_variable_interne` |

### 7. Noms de variables significatifs

**Règle** : Utilisez des noms descriptifs et évitez les abréviations obscures.

```python
# ✅ Bon - noms explicites
nombre_utilisateurs = 42
prix_total = calculer_prix(quantite, prix_unitaire)
date_inscription = datetime.now()

def calculer_moyenne_etudiants(notes):
    return sum(notes) / len(notes)

# ❌ Mauvais - noms cryptiques
n = 42
pt = calc(q, pu)
di = datetime.now()

def calc_moy(n):
    return sum(n) / len(n)
```

**Exceptions acceptables** :
- `i`, `j`, `k` pour les compteurs de boucles simples
- `x`, `y`, `z` pour les coordonnées
- `f` pour les fichiers dans un contexte très court
- Variables mathématiques standard (comme dans `a*x**2 + b*x + c`)

### 8. Comparaisons

**Règle** : Utilisez les comparaisons appropriées.

```python
# ✅ Bon
if variable is None:
    pass

if variable is not None:
    pass

if ma_liste:  # Vrai si la liste n'est pas vide
    pass

if not ma_liste:  # Vrai si la liste est vide
    pass

# ❌ Mauvais
if variable == None:
    pass

if len(ma_liste) > 0:
    pass

if len(ma_liste) == 0:
    pass
```

**Règles** :
- Utilisez `is` / `is not` pour comparer avec `None`, `True`, `False`
- Utilisez `==` / `!=` pour comparer des valeurs
- Testez directement les collections vides/non vides

### 9. Commentaires

**Règle** : Écrivez des commentaires clairs qui expliquent le "pourquoi", pas le "quoi".

```python
# ✅ Bon - explique le pourquoi
# On divise par 1000 car les prix sont stockés en centimes
prix_euros = prix_centimes / 100

# On utilise un cache pour éviter de recalculer
# (cette opération est coûteuse : ~2 secondes)
if cle not in cache:
    cache[cle] = calculer_valeur_complexe()

# ❌ Mauvais - répète le code
# Incrémente i
i += 1

# Boucle sur les éléments
for element in liste:
    print(element)
```

**Bonnes pratiques** :
- Expliquez les décisions non évidentes
- Documentez les hacks et solutions de contournement
- Mettez à jour les commentaires quand vous changez le code
- Évitez les commentaires évidents qui dupliquent le code

### 10. Docstrings

**Règle** : Documentez les modules, classes et fonctions avec des docstrings.

```python
# ✅ Bon
def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres.

    Args:
        nombres (list): Liste de nombres.

    Returns:
        float: La moyenne des nombres.

    Raises:
        ValueError: Si la liste est vide.
    """
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
    return sum(nombres) / len(nombres)

# ❌ Mauvais - pas de docstring
def calculer_moyenne(nombres):
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
    return sum(nombres) / len(nombres)
```

---

## Exemples de code PEP 8 complet

### Avant et après

**Avant** (ne suit pas PEP 8) :

```python
import sys,os
from datetime import datetime
def calcul(x,y):a=x+y;return a
class compte:
  def __init__(self,solde):self.solde=solde
  def depot(self,montant):
   self.solde+=montant
   return self.solde
```

**Après** (suit PEP 8) :

```python
"""Module de gestion de comptes bancaires."""

import os
import sys
from datetime import datetime


TAUX_INTERET = 0.03


class CompteBancaire:
    """Représente un compte bancaire simple.

    Attributes:
        solde (float): Le solde actuel du compte.
    """

    def __init__(self, solde_initial=0):
        """Initialise un nouveau compte.

        Args:
            solde_initial (float): Le solde de départ.
                Par défaut 0.
        """
        self.solde = solde_initial

    def deposer(self, montant):
        """Dépose de l'argent sur le compte.

        Args:
            montant (float): Le montant à déposer.

        Returns:
            float: Le nouveau solde.

        Raises:
            ValueError: Si le montant est négatif.
        """
        if montant < 0:
            raise ValueError("Le montant doit être positif")

        self.solde += montant
        return self.solde


def calculer_total(prix, quantite):
    """Calcule le prix total.

    Args:
        prix (float): Prix unitaire.
        quantite (int): Quantité.

    Returns:
        float: Prix total.
    """
    total = prix * quantite
    return total
```

---

## Outils de linting

### Qu'est-ce que le linting ?

Le **linting** est le processus d'analyse automatique de code pour détecter :
- Les erreurs de style (violations de PEP 8)
- Les bugs potentiels
- Les mauvaises pratiques
- Le code mort ou inutilisé
- Les problèmes de sécurité

**Analogie** : Un linter, c'est comme un correcteur orthographique pour le code. Il souligne les problèmes et suggère des améliorations.

### Pourquoi utiliser un linter ?

1. **Gain de temps** : Détection automatique des problèmes
2. **Cohérence** : Style uniforme dans tout le projet
3. **Apprentissage** : Apprendre les bonnes pratiques
4. **Qualité** : Moins de bugs et code plus maintenable
5. **Revue de code** : Moins de commentaires sur le style

---

## Les principaux outils de linting

### 1. flake8 : Le linter standard

**flake8** combine plusieurs outils pour vérifier PEP 8, détecter les erreurs et la complexité.

#### Installation

```bash
pip install flake8
```

#### Utilisation

```bash
# Vérifier un fichier
flake8 mon_fichier.py

# Vérifier un dossier
flake8 mon_package/

# Avec statistiques
flake8 --statistics mon_package/

# Afficher seulement certains types d'erreurs
flake8 --select=E501 mon_package/
```

#### Exemple de sortie

```bash
$ flake8 exemple.py
exemple.py:1:1: E302 expected 2 blank lines, found 1
exemple.py:5:80: E501 line too long (85 > 79 characters)
exemple.py:10:1: W293 blank line contains whitespace
exemple.py:15:1: F401 'os' imported but unused
```

**Codes d'erreur** :
- **E** : Erreurs de style PEP 8
- **W** : Avertissements de style PEP 8
- **F** : Erreurs détectées par PyFlakes (bugs potentiels)
- **C** : Complexité (cyclomatic complexity)
- **N** : Erreurs de nommage

#### Configuration

Créez un fichier `.flake8` ou `setup.cfg` :

```ini
# fichier: .flake8
[flake8]
max-line-length = 88
exclude =
    .git,
    __pycache__,
    venv,
    .venv,
    tests/fixtures/*
ignore =
    E203,  # Espace avant ':'
    W503,  # Saut de ligne avant opérateur binaire
```

### 2. pylint : Le linter complet

**pylint** est plus strict et détaillé que flake8. Il vérifie plus de choses mais peut être plus verbeux.

#### Installation

```bash
pip install pylint
```

#### Utilisation

```bash
# Analyser un fichier
pylint mon_fichier.py

# Analyser un package
pylint mon_package/

# Format JSON pour traitement automatique
pylint --output-format=json mon_fichier.py

# Voir les statistiques
pylint --reports=y mon_fichier.py
```

#### Exemple de sortie

```bash
$ pylint exemple.py
************* Module exemple
exemple.py:1:0: C0114: Missing module docstring (missing-module-docstring)
exemple.py:5:0: C0103: Variable name "X" doesn't conform to snake_case naming style (invalid-name)
exemple.py:10:0: W0612: Unused variable 'resultat' (unused-variable)

-----------------------------------
Your code has been rated at 7.50/10
```

**Pylint donne une note sur 10** à votre code.

#### Configuration

Créez un fichier `.pylintrc` :

```bash
# Générer un fichier de config par défaut
pylint --generate-rcfile > .pylintrc
```

Exemple de configuration :

```ini
# fichier: .pylintrc
[MASTER]
ignore=tests,docs

[MESSAGES CONTROL]
disable=
    missing-docstring,
    too-few-public-methods,
    too-many-arguments

[FORMAT]
max-line-length=88
indent-string='    '

[BASIC]
good-names=i,j,k,x,y,z,df,ax
```

### 3. Black : Le formateur automatique

**Black** est différent : il ne vérifie pas, il **reformate** automatiquement votre code selon un style cohérent.

> "Black is the uncompromising code formatter."

#### Installation

```bash
pip install black
```

#### Utilisation

```bash
# Formater un fichier
black mon_fichier.py

# Formater un dossier
black mon_package/

# Voir ce qui serait changé sans modifier
black --check mon_fichier.py

# Voir les différences
black --diff mon_fichier.py
```

#### Avant et après Black

**Avant** :

```python
def fonction_complexe(parametre1,parametre2,parametre3):
    resultat=parametre1+parametre2
    if resultat>100:return resultat*parametre3
    else:
     return resultat
```

**Après** :

```python
def fonction_complexe(parametre1, parametre2, parametre3):
    resultat = parametre1 + parametre2
    if resultat > 100:
        return resultat * parametre3
    else:
        return resultat
```

#### Configuration

Black a très peu d'options (c'est volontaire !). Fichier `pyproject.toml` :

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''
```

**Note** : Black utilise 88 caractères par ligne au lieu de 79 (c'est un choix débattu).

### 4. isort : Tri automatique des imports

**isort** organise automatiquement vos imports selon PEP 8.

#### Installation

```bash
pip install isort
```

#### Utilisation

```bash
# Trier les imports d'un fichier
isort mon_fichier.py

# Trier tout le projet
isort .

# Voir ce qui serait changé
isort --check-only mon_fichier.py

# Voir les différences
isort --diff mon_fichier.py
```

#### Avant et après isort

**Avant** :

```python
from mon_package import fonction
import sys
import requests
from datetime import datetime
import os
```

**Après** :

```python
import os
import sys
from datetime import datetime

import requests

from mon_package import fonction
```

#### Configuration

Compatible avec Black dans `pyproject.toml` :

```toml
[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
```

### 5. mypy : Vérification de types

**mypy** vérifie les annotations de types (type hints).

#### Installation

```bash
pip install mypy
```

#### Utilisation

```bash
# Vérifier un fichier
mypy mon_fichier.py

# Vérifier un package
mypy mon_package/

# Avec plus de détails
mypy --strict mon_fichier.py
```

#### Exemple

```python
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres."""
    return a + b

# ✅ OK
resultat = additionner(5, 3)

# ❌ Erreur détectée par mypy
resultat = additionner("5", "3")  # error: Argument 1 has incompatible type "str"; expected "int"
```

### 6. bandit : Sécurité

**bandit** analyse le code pour détecter les problèmes de sécurité courants.

#### Installation

```bash
pip install bandit
```

#### Utilisation

```bash
# Analyser un fichier
bandit mon_fichier.py

# Analyser un dossier
bandit -r mon_package/

# Niveau de sévérité
bandit -ll mon_fichier.py  # Low level
```

#### Exemple

```python
# ❌ Bandit détectera ce problème
import pickle

def charger_donnees(fichier):
    with open(fichier, 'rb') as f:
        return pickle.load(f)  # Risque de sécurité !
```

---

## Configuration d'un projet complet

### Structure recommandée

```
mon_projet/
├── src/
│   └── mon_package/
│       ├── __init__.py
│       └── module.py
├── tests/
│   └── test_module.py
├── .flake8
├── .pylintrc
├── pyproject.toml
├── setup.py
└── README.md
```

### pyproject.toml (configuration centralisée)

```toml
# fichier: pyproject.toml

[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
show_missing = true
```

### .flake8 (configuration flake8)

```ini
# fichier: .flake8
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude =
    .git,
    __pycache__,
    .venv,
    venv,
    build,
    dist,
    *.egg-info
per-file-ignores =
    __init__.py:F401
    tests/*:F401,F811
```

---

## Intégration dans l'éditeur

### Visual Studio Code

Extensions recommandées :
- **Python** (Microsoft) : Support Python complet
- **Pylance** : IntelliSense avancé
- **Black Formatter** : Formatage automatique
- **Flake8** : Linting en temps réel

Configuration `settings.json` :

```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "[python]": {
        "editor.rulers": [88],
        "editor.tabSize": 4
    }
}
```

### PyCharm

PyCharm inclut déjà un vérificateur PEP 8.

Configuration :
1. **Settings** → **Editor** → **Code Style** → **Python**
2. Cocher "Use PEP 8 coding style guide"
3. **Settings** → **Tools** → **External Tools** pour ajouter Black

### Autres éditeurs

La plupart des éditeurs ont des plugins pour :
- Sublime Text : SublimeLinter-flake8
- Vim/Neovim : ALE, vim-flake8
- Emacs : flycheck

---

## Automatisation avec pre-commit

### Qu'est-ce que pre-commit ?

**pre-commit** est un outil qui exécute automatiquement des vérifications avant chaque commit git.

#### Installation

```bash
pip install pre-commit
```

#### Configuration

Créez un fichier `.pre-commit-config.yaml` :

```yaml
# fichier: .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.10

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=88', '--extend-ignore=E203,W503']

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  - repo: https://github.com/pycqa/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ['-ll']
```

#### Activation

```bash
# Installer les hooks
pre-commit install

# Exécuter manuellement sur tous les fichiers
pre-commit run --all-files

# Test sur un fichier
pre-commit run --files mon_fichier.py
```

Maintenant, avant chaque commit, tous les outils s'exécutent automatiquement !

---

## Intégration dans CI/CD

### GitHub Actions

Créez `.github/workflows/lint.yml` :

```yaml
name: Linting

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install flake8 black isort mypy
        pip install -r requirements.txt

    - name: Run Black
      run: black --check .

    - name: Run isort
      run: isort --check-only .

    - name: Run flake8
      run: flake8 .

    - name: Run mypy
      run: mypy src/
```

### GitLab CI

Créez `.gitlab-ci.yml` :

```yaml
lint:
  stage: test
  image: python:3.10
  script:
    - pip install flake8 black isort
    - black --check .
    - isort --check-only .
    - flake8 .
  only:
    - merge_requests
    - main
```

---

## Workflow recommandé

### 1. Configuration initiale du projet

```bash
# Installer les outils
pip install black isort flake8 mypy pre-commit

# Créer les fichiers de configuration
touch .flake8 pyproject.toml .pre-commit-config.yaml

# Installer pre-commit
pre-commit install
```

### 2. Pendant le développement

```bash
# Formater automatiquement
black .
isort .

# Vérifier le code
flake8 .
mypy src/
```

### 3. Avant de commiter

```bash
# Pre-commit s'exécute automatiquement
git add .
git commit -m "Mon message"

# Ou manuellement
pre-commit run --all-files
```

### 4. Dans la CI/CD

Les mêmes vérifications s'exécutent automatiquement sur chaque push/PR.

---

## Gérer les violations PEP 8

### Ignorer une ligne spécifique

```python
# Ignorer une erreur flake8 sur une ligne
mon_dictionnaire = {"cle_tres_tres_longue": "valeur"}  # noqa: E501

# Ignorer une erreur pylint
variable = fonction()  # pylint: disable=invalid-name
```

**Note** : À utiliser avec parcimonie ! Expliquez pourquoi dans un commentaire.

### Ignorer un fichier entier

```python
# En haut du fichier
# flake8: noqa

# Ou pour pylint
# pylint: skip-file
```

### Désactiver temporairement une règle

```python
# pylint: disable=too-many-arguments
def fonction_avec_beaucoup_arguments(a, b, c, d, e, f):
    pass
# pylint: enable=too-many-arguments
```

---

## Cas pratique : Refactorisation d'un fichier

### Fichier initial (nombreuses violations)

```python
import sys,os
from datetime import *
def calc(x,y,z):
 result=x+y
 if result>z:return result
 else:return 0
class user:
 def __init__(self,n,a):self.name=n;self.age=a
 def isAdult(self):
  if self.age>=18:return True
  else:return False
```

### Étape 1 : Exécuter flake8

```bash
$ flake8 exemple.py
exemple.py:1:10: E401 multiple imports on one line
exemple.py:2:1: F403 'from datetime import *' used; unable to detect undefined names
exemple.py:3:1: E302 expected 2 blank lines, found 0
exemple.py:3:15: E231 missing whitespace after ','
exemple.py:4:1: E111 indentation is not a multiple of 4
exemple.py:5:2: E225 missing whitespace around operator
exemple.py:5:11: E701 multiple statements on one line (colon)
exemple.py:6:2: E701 multiple statements on one line (colon)
exemple.py:7:1: E302 expected 2 blank lines, found 0
exemple.py:7:7: E999 SyntaxError: invalid syntax
exemple.py:8:1: E111 indentation is not a multiple of 4
exemple.py:8:25: E702 multiple statements on one line (semicolon)
exemple.py:9:1: E111 indentation is not a multiple of 4
exemple.py:9:6: N802 function name should be lowercase
exemple.py:10:2: E111 indentation is not a multiple of 4
exemple.py:10:18: E701 multiple statements on one line (colon)
exemple.py:11:2: E701 multiple statements on one line (colon)
```

**25 erreurs détectées !**

### Étape 2 : Appliquer Black

```bash
$ black exemple.py
```

Le fichier est automatiquement reformaté.

### Étape 3 : Appliquer isort

```bash
$ isort exemple.py
```

Les imports sont organisés.

### Étape 4 : Corrections manuelles

```python
"""Module de gestion d'utilisateurs."""

import os
import sys
from datetime import datetime


def calculer_resultat(valeur_x, valeur_y, seuil):
    """Calcule un résultat basé sur un seuil.

    Args:
        valeur_x (int): Première valeur.
        valeur_y (int): Deuxième valeur.
        seuil (int): Valeur seuil.

    Returns:
        int: Le résultat du calcul.
    """
    resultat = valeur_x + valeur_y

    if resultat > seuil:
        return resultat
    else:
        return 0


class Utilisateur:
    """Représente un utilisateur.

    Attributes:
        nom (str): Le nom de l'utilisateur.
        age (int): L'âge de l'utilisateur.
    """

    def __init__(self, nom, age):
        """Initialise un utilisateur.

        Args:
            nom (str): Le nom.
            age (int): L'âge.
        """
        self.nom = nom
        self.age = age

    def est_majeur(self):
        """Vérifie si l'utilisateur est majeur.

        Returns:
            bool: True si majeur, False sinon.
        """
        return self.age >= 18
```

### Étape 5 : Vérification finale

```bash
$ flake8 exemple.py
# Aucune erreur !

$ pylint exemple.py
# Note: 10.00/10
```

---

## Bonnes pratiques

### 1. Commencez tôt

Configurez le linting dès le début du projet. Plus vous attendez, plus il y aura de travail de correction.

### 2. Automatisez

Utilisez :
- Formatage automatique au moment de sauvegarder (Black)
- Pre-commit hooks
- CI/CD pour vérifier chaque commit

### 3. Soyez pragmatique

PEP 8 donne des guidelines, pas des lois. Si une règle ne fait pas sens pour votre projet, ajustez-la.

```python
# Parfois, c'est OK de dépasser 79 caractères pour la lisibilité
URLS = {
    'production': 'https://api.monsite.com/v1/endpoint/tres/long/chemin',
    'staging': 'https://staging-api.monsite.com/v1/endpoint/tres/long/chemin',
}
```

### 4. Équipe avant tout

L'important est que toute l'équipe suive les mêmes règles. Discutez et convenez d'un style ensemble.

### 5. Formation continue

Utilisez les messages d'erreur des linters comme opportunités d'apprentissage.

### 6. Refactorisez progressivement

Ne tentez pas de tout corriger d'un coup sur un vieux projet. Procédez progressivement :
1. Nouveaux fichiers : respect strict
2. Fichiers modifiés : correction au passage
3. Anciens fichiers : refactorisation planifiée

---

## Outils complémentaires

### 1. autopep8 : Correction automatique

Corrige automatiquement les violations PEP 8 :

```bash
pip install autopep8

# Corriger un fichier
autopep8 --in-place --aggressive mon_fichier.py
```

### 2. yapf : Formateur de Google

Alternative à Black, développé par Google :

```bash
pip install yapf

# Formater
yapf --in-place mon_fichier.py
```

### 3. vulture : Détection de code mort

Trouve le code non utilisé :

```bash
pip install vulture

# Analyser
vulture mon_package/
```

### 4. radon : Mesure de complexité

Mesure la complexité cyclomatique :

```bash
pip install radon

# Complexité cyclomatique
radon cc mon_package/ -a

# Maintenabilité
radon mi mon_package/
```

---

## Résumé

### Points clés à retenir

1. **PEP 8** est le guide de style officiel de Python
2. **Suivre PEP 8** améliore la lisibilité et la maintenabilité
3. **Indentation** : 4 espaces
4. **Longueur de ligne** : 79-88 caractères
5. **Nommage** : snake_case pour fonctions/variables, PascalCase pour classes
6. **Imports** : Organisés en 3 groupes (standard, tierce, local)
7. **Utilisez des linters** pour automatiser les vérifications
8. **Black** reformate automatiquement le code
9. **Pre-commit** vérifie le code avant chaque commit
10. **La cohérence** est plus importante que la perfection

### Outils essentiels

| Outil | Usage | Commande |
|-------|-------|----------|
| **flake8** | Vérification PEP 8 | `flake8 .` |
| **black** | Formatage automatique | `black .` |
| **isort** | Organisation imports | `isort .` |
| **mypy** | Vérification types | `mypy src/` |
| **pylint** | Analyse approfondie | `pylint mon_package/` |
| **pre-commit** | Hooks git | `pre-commit run --all-files` |

### Configuration minimale

```bash
# Installation
pip install black isort flake8 pre-commit

# Créer .flake8
cat > .flake8 << EOF
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,.venv
EOF

# Créer pyproject.toml
cat > pyproject.toml << EOF
[tool.black]
line-length = 88

[tool.isort]
profile = "black"
EOF

# Installer pre-commit
pre-commit install
```

### Commandes quotidiennes

```bash
# Formater le code
black .
isort .

# Vérifier le code
flake8 .

# Avant commit
pre-commit run --all-files

# Dans l'éditeur : activer "Format on Save"
```

### Checklist qualité du code

- [ ] Le code suit PEP 8
- [ ] Indentation cohérente (4 espaces)
- [ ] Lignes < 88 caractères
- [ ] Imports organisés
- [ ] Nommage cohérent (snake_case, PascalCase)
- [ ] Docstrings sur fonctions/classes publiques
- [ ] Pas de code mort
- [ ] Pas d'imports inutilisés
- [ ] Complexité raisonnable
- [ ] Tests passent
- [ ] Linters ne rapportent pas d'erreur

---

## Ressources complémentaires

- **PEP 8 officiel** : https://peps.python.org/pep-0008/
- **Guide de style Google** : https://google.github.io/styleguide/pyguide.html
- **Real Python - PEP 8** : https://realpython.com/python-pep8/
- **Black documentation** : https://black.readthedocs.io/
- **flake8 documentation** : https://flake8.pycqa.org/
- **pylint documentation** : https://pylint.pycqa.org/
- **Pre-commit** : https://pre-commit.com/

**Un code propre est un code qui respire ! Prenez le temps de bien le formater.** ✨

⏭️ [Validation de types avec mypy](/10-tests-et-qualite/06-validation-types-mypy.md)
