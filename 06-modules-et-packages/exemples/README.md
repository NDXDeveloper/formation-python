# Chapitre 06 - Modules et packages : Exemples testables

Ce dossier contient **13 fichiers** Python exécutables extraits des cours du chapitre 06.

## Fichiers

### Section 6.1 : Importation et création de modules

| Fichier | Description | Source |
|---------|-------------|--------|
| `01_01_importation_modules.py` | Syntaxes d'import (import, alias, from, import *), modules standard (math, datetime, os, re) | 01-importation-et-creation-modules.md |
| `01_02_creation_modules.py` | Créer ses propres modules (operations.py, geometrie.py), importer et utiliser | 01-importation-et-creation-modules.md |
| `01_03_name_et_organisation.py` | `__name__ == "__main__"`, exécution directe vs import, sys.path, organisation | 01-importation-et-creation-modules.md |

### Section 6.2 : Structure des packages

| Fichier | Description | Source |
|---------|-------------|--------|
| `02_01_package_simple.py` | Créer un package (mathematiques) avec `__init__.py`, 3 méthodes d'import | 02-structure-des-packages.md |
| `02_02_init_avance.py` | `__init__.py` avancé : imports simplifiés, `__version__`, `__all__` | 02-structure-des-packages.md |
| `02_03_sous_packages.py` | Sous-packages (utilitaires/texte/), imports relatifs, formatage et validation | 02-structure-des-packages.md |
| `02_04_main_et_all.py` | `__main__.py` (python -m package), `__all__` pour contrôler les exports | 02-structure-des-packages.md |
| `02_05_exemple_complet_bibliotheque.py` | Package complet : bibliotheque avec models/livre.py, services/gestion_livres.py | 02-structure-des-packages.md |

### Section 6.3 : Gestion des dépendances avec pip

| Fichier | Description | Source |
|---------|-------------|--------|
| `03_01_pip_et_requirements.py` | pip --version, pip list, pip show, pip freeze, créer un requirements.txt | 03-gestion-dependances-pip.md |

### Section 6.4 : Environnements virtuels (venv)

| Fichier | Description | Source |
|---------|-------------|--------|
| `04_01_creer_et_inspecter_venv.py` | Créer un venv, inspecter sa structure, lire pyvenv.cfg, vérifier l'isolation | 04-environnements-virtuels.md |
| `04_02_gitignore_et_structure.py` | .gitignore Python, structure de projet recommandée, bonnes pratiques | 04-environnements-virtuels.md |

### Section 6.5 : Outils modernes (Poetry, Pipenv)

| Fichier | Description | Source |
|---------|-------------|--------|
| `05_01_pyproject_toml.py` | Créer et parser un pyproject.toml (Poetry), groupes de dépendances, notations de versions | 05-outils-modernes-poetry-pipenv.md |
| `05_02_pipfile_demo.py` | Créer et parser un Pipfile (Pipenv), comparaison pip/Pipenv/Poetry, workflows | 05-outils-modernes-poetry-pipenv.md |

## Sorties attendues

### 01_01_importation_modules.py
```
=== import math ===
pi = 3.141592653589793
sqrt(16) = 4.0
cos(0) = 1.0

=== import avec alias ===
Aujourd'hui : (date du jour)
Dans 30 jours : (date + 30 jours)

=== from ... import ===
Dossier courant : (chemin courant)
Fichiers Python : (liste des .py)

=== Modules standard utiles ===
random.randint(1, 100) = (valeur aléatoire)
re.findall('[0-9]+', 'Il a 25 ans et 3 enfants') = ['25', '3']
```

### 01_02_creation_modules.py
```
=== Module operations ===
addition(10, 5) = 15
soustraction(10, 5) = 5
multiplication(6, 7) = 42

=== Module geometrie ===
aire_cercle(5) = 78.53975
aire_rectangle(4, 6) = 24
perimetre_rectangle(4, 6) = 20
```

### 01_03_name_et_organisation.py
```
=== Exécution directe (python calculs.py) ===
[module calculs] __name__ = __main__
Exécution directe : tests...
addition(3, 5) = 8
multiplication(4, 7) = 28

=== Import du module ===
[module calculs] __name__ = calculs
Résultat : 15

=== Module utilitaires ===
Version : 1.0.0
Documentation : Module utilitaires - fonctions d'aide.
Nom du module : utilitaires

=== sys.path (3 premiers) ===
  (chemins du sys.path)
```

### 02_01_package_simple.py
```
=== Méthode 1 : import complet ===
5 + 3 = 8
5 - 3 = 2

=== Méthode 2 : import avec alias ===
Aire du cercle (r=5) : 78.53975

=== Méthode 3 : from ... import ===
6 x 7 = 42
10 / 3 = 3.33
```

### 02_02_init_avance.py
```
=== Imports simplifiés ===
10 + 5 = 15
6 x 7 = 42

=== Version du package ===
Version : 1.0.0

=== __all__ ===
Exports : ['addition', 'soustraction', 'multiplication', 'division', 'aire_cercle', 'aire_rectangle', 'perimetre_rectangle']
```

### 02_03_sous_packages.py
```
=== Import complet ===
BONJOUR LE MONDE

=== Import avec alias ===
Bonjour Le Monde

=== Import direct ===
PYTHON
True
False

=== Import sous-package ===
trop d'espaces
True
False
True
False
```

### 02_04_main_et_all.py
```
=== __main__.py ===
Exécution avec python -m calculatrice :
=== Calculatrice ===
15 + 7 = 22
15 - 7 = 8

=== __all__ ===
fonction_publique() : publique
CONSTANTE : 42
_fonction_privee() : privee
__all__ : ['fonction_publique', 'CONSTANTE']
```

### 02_05_exemple_complet_bibliotheque.py
```
=== Package bibliothèque ===
Recherche 'Python' : Python pour débutants par John Doe (disponible)

Catalogue :
  - Python pour débutants par John Doe (disponible)
  - JavaScript avancé par Jane Smith (disponible)
  - Data Science avec Python par Alice Martin (disponible)

Version : 1.0.0
```

### 03_01_pip_et_requirements.py
```
=== Version de pip ===
pip (version) from (chemin)

=== Packages installés (5 premiers) ===
Package          Version
---------------- --------
(5 premiers packages)
...

=== pip show pip ===
Name: pip
Version: (version)
(autres infos)

=== pip freeze (5 premiers) ===
(5 premiers packages==version)
... (N packages au total)

=== Création d'un requirements.txt ===
Contenu du fichier :
# Requêtes HTTP
requests==2.31.0
...
```

### 04_01_creer_et_inspecter_venv.py
```
=== Création d'un environnement virtuel ===
Environnement créé dans : (chemin)

=== Structure du venv ===
bin/
  activate
  python
  python3
  ...
include/
lib/
  pythonX.Y/
    site-packages/
pyvenv.cfg

=== Contenu de pyvenv.cfg ===
  home = /usr/bin
  include-system-site-packages = false
  version = X.Y.Z
  ...

=== Exécutables disponibles ===
  activate, python, python3, ...

=== Python du venv vs Python système ===
Python venv   : (chemin venv)
Python système : (chemin système)

=== Répertoire site-packages ===
Emplacement : lib/pythonX.Y/site-packages
Nombre d'éléments : 0

=== Pourquoi utiliser des venv ? ===
  1. Isolation des dépendances par projet
  ...
```

### 04_02_gitignore_et_structure.py
```
=== Contenu recommandé pour .gitignore ===
(contenu .gitignore)

=== Structure de projet recommandée ===
(arbre du projet)

=== Fichiers a committer vs ignorer ===
A COMMITTER :
  [OK] Code source (.py)
  ...
A NE PAS COMMITTER :
  [X]  venv/ ou env/
  ...

=== Bonnes pratiques ===
  1. Un environnement virtuel par projet
  ...
```

### 05_01_pyproject_toml.py
```
=== Exemple de pyproject.toml (Poetry) ===
(contenu pyproject.toml)

=== Lecture du pyproject.toml ===
Nom du projet : mon-api
Version : 0.1.0
Dependances principales (5) :
  python = ^3.11
  fastapi = ^0.104.0
  ...
Dependances de dev (4) :
  pytest = ^7.4.0
  ...
Scripts (entry points) :
  mon-api -> mon_api.main:start
Build system :
  requires : ['poetry-core']
  backend  : poetry.core.masonry.api

=== Notation des versions (Poetry) ===
  ^2.31.0  -> >=2.31.0, <3.0.0 (Compatible version majeure)
  ...
```

### 05_02_pipfile_demo.py
```
=== Exemple de Pipfile (Pipenv) ===
(contenu Pipfile)

=== Lecture du Pipfile ===
Source : pypi -> https://pypi.org/simple
Packages principaux (5) :
  requests = *
  ...
Packages de dev (3) :
  pytest = *
  ...

=== Comparaison des formats ===
  (tableau comparatif pip/Pipenv/Poetry)

=== Quand utiliser quel outil ? ===
  pip + venv : ...
  Pipenv : ...
  Poetry : ...

=== Workflow typique Poetry ===
  1. poetry new mon_projet
  ...

=== Workflow typique Pipenv ===
  1. mkdir mon_projet && cd mon_projet
  ...
```

## Exécution

```bash
# Exécuter un fichier spécifique
python3 01_01_importation_modules.py

# Exécuter tous les fichiers
for f in *.py; do echo "=== $f ==="; python3 "$f"; echo; done
```

## Notes

- Tous les exemples de packages/modules créent des répertoires temporaires (`_temp_*`) et les suppriment après exécution.
- Les fichiers 03, 04 et 05 concernent principalement des commandes shell (pip, venv, poetry, pipenv). Les fichiers Python démontrent les concepts programmatiquement.
- Le fichier `05_01_pyproject_toml.py` utilise `tomllib` (Python 3.11+). Pour les versions antérieures, installer `tomli`.
