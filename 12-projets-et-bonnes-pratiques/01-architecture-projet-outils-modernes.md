🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.1 Architecture de projet et outils modernes

## Introduction

Lorsque vous débutez en Python, vous écrivez probablement vos programmes dans un seul fichier. C'est parfait pour apprendre ! Mais au fur et à mesure que vos projets grandissent, il devient essentiel d'organiser votre code de manière structurée et professionnelle.

Dans ce chapitre, nous allons découvrir comment structurer un projet Python moderne, quels outils utiliser pour faciliter le développement, et comment adopter les bonnes pratiques dès le début.

---

## Pourquoi l'architecture est-elle importante ?

Une bonne architecture de projet vous permet de :

- **Retrouver facilement votre code** : vous savez exactement où chercher
- **Collaborer efficacement** : d'autres développeurs comprennent votre organisation
- **Maintenir et faire évoluer** : ajouter des fonctionnalités devient plus simple
- **Réutiliser votre code** : vous pouvez facilement importer vos modules dans d'autres projets
- **Tester votre code** : une structure claire facilite l'écriture de tests

---

## Structure de base d'un projet Python

Voici une structure de projet recommandée pour débuter :

```
mon_projet/
│
├── src/
│   └── mon_projet/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── docs/
│   └── README.md
│
├── .gitignore
├── pyproject.toml
└── README.md
```

### Explications détaillées

#### Le dossier `src/`

Le dossier `src/` (source) contient tout votre code source. C'est là que vit votre application.

**Pourquoi `src/mon_projet/` et pas juste `mon_projet/` ?**
Cette structure en deux niveaux est une bonne pratique moderne car elle évite certains problèmes d'importation et force l'installation du package avant de l'utiliser.

#### Le fichier `__init__.py`

Ce fichier (qui peut être vide) transforme un simple dossier en un **package Python**. Il permet d'importer votre code comme ceci :

```python
from mon_projet import main  
from mon_projet.utils import ma_fonction  
```

#### Le dossier `tests/`

Tous vos tests unitaires vont ici. Séparer les tests du code source garde votre projet organisé et facilite l'exécution des tests.

Convention de nommage : chaque fichier de test commence par `test_` pour être automatiquement détecté par les outils de test comme `pytest`.

#### Le dossier `docs/`

La documentation de votre projet. Au minimum, vous devriez avoir un fichier `README.md` qui explique :
- Ce que fait votre projet
- Comment l'installer
- Comment l'utiliser
- Des exemples

#### Le fichier `.gitignore`

Ce fichier indique à Git quels fichiers **ne pas** suivre dans le contrôle de version. Exemple de contenu :

```
# Fichiers Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Environnements virtuels
venv/  
env/  
ENV/  

# IDEs
.vscode/
.idea/
*.swp

# Distribution
dist/  
build/  
*.egg-info/

# Tests
.pytest_cache/
.coverage
htmlcov/

# Fichiers de configuration locaux
.env
config.local.py
```

#### Le fichier `requirements.txt`

Liste toutes les dépendances (bibliothèques externes) de votre projet avec leurs versions :

```
requests==2.31.0  
pandas>=2.0.0  
numpy==1.24.3  
```

Installation des dépendances :
```bash
pip install -r requirements.txt
```

Génération automatique depuis votre environnement :
```bash
pip freeze > requirements.txt
```

---

## Structure pour différents types de projets

### Projet simple (script ou petit outil)

```
mon_script/
├── mon_script.py
├── requirements.txt
└── README.md
```

Pour un petit projet personnel ou un script, pas besoin de compliquer les choses !

### Application web (Flask/FastAPI)

```
mon_app_web/
│
├── src/
│   └── mon_app/
│       ├── __init__.py
│       ├── main.py
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── users.py
│       │   └── products.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── user.py
│       │   └── product.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── database.py
│       └── static/
│           ├── css/
│           └── js/
│
├── tests/
├── requirements.txt
└── README.md
```

Cette structure sépare les responsabilités :
- **routes/** : gère les endpoints de l'API
- **models/** : définit les structures de données
- **services/** : contient la logique métier
- **static/** : fichiers CSS, JavaScript, images

### Projet Data Science

```
projet_data/
│
├── data/
│   ├── raw/          # Données brutes (ne jamais modifier)
│   ├── processed/    # Données nettoyées
│   └── results/      # Résultats d'analyse
│
├── notebooks/        # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   └── 02_modeling.ipynb
│
├── src/
│   └── projet_data/
│       ├── __init__.py
│       ├── preprocessing.py
│       ├── features.py
│       └── visualization.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

## Outils modernes pour la gestion de projet

### 1. Poetry - Gestionnaire de dépendances moderne

**Poetry** est un outil qui remplace `pip` et `virtualenv` en offrant une meilleure gestion des dépendances.

#### Installation de Poetry

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

#### Créer un nouveau projet avec Poetry

```bash
poetry new mon_projet
```

Cela crée automatiquement la structure suivante :

```
mon_projet/
├── mon_projet/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

#### Le fichier `pyproject.toml`

C'est le cœur de votre projet avec Poetry. Il remplace `setup.py` et `requirements.txt` :

```toml
[tool.poetry]
name = "mon_projet"  
version = "0.1.0"  
description = "Description de mon projet"  
authors = ["Votre Nom <email@example.com>"]  

[tool.poetry.dependencies]
python = "^3.10"  
requests = "^2.31.0"  
pandas = "^2.0.0"  

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"  
black = "^23.0.0"  

[build-system]
requires = ["poetry-core"]  
build-backend = "poetry.core.masonry.api"  
```

#### Commandes Poetry essentielles

```bash
# Ajouter une dépendance
poetry add requests

# Ajouter une dépendance de développement (tests, etc.)
poetry add --group dev pytest

# Installer toutes les dépendances
poetry install

# Exécuter un script dans l'environnement Poetry
poetry run python mon_script.py

# Activer l'environnement virtuel
poetry shell

# Mettre à jour les dépendances
poetry update

# Générer requirements.txt (pour compatibilité)
poetry export -f requirements.txt --output requirements.txt
```

### 2. Black - Formateur de code automatique

**Black** formate automatiquement votre code selon les standards Python (PEP 8). Plus besoin de débats sur le style de code !

#### Installation

```bash
pip install black
# ou avec Poetry
poetry add --group dev black
```

#### Utilisation

```bash
# Formater un fichier
black mon_fichier.py

# Formater tout un dossier
black src/

# Vérifier sans modifier (mode dry-run)
black --check src/

# Voir les différences sans modifier
black --diff src/
```

#### Configuration dans `pyproject.toml`

```toml
[tool.black]
line-length = 88  
target-version = ['py310']  
include = '\.pyi?$'  
extend-exclude = '''  
/(
  # Dossiers à exclure
  \.eggs
  | \.git
  | \.venv
  | build
  | dist
)/
'''
```

**Exemple avant/après Black :**

Avant :
```python
def ma_fonction(x,y,z):
    resultat=x+y+z
    return resultat
```

Après :
```python
def ma_fonction(x, y, z):
    resultat = x + y + z
    return resultat
```

### 3. Ruff - Linter ultra-rapide

**Ruff** est un linter Python moderne, écrit en Rust, qui remplace plusieurs outils (Flake8, isort, etc.) et est 10-100 fois plus rapide !

#### Installation

```bash
pip install ruff
# ou avec Poetry
poetry add --group dev ruff
```

#### Utilisation

```bash
# Analyser votre code
ruff check .

# Corriger automatiquement les erreurs possibles
ruff check --fix .

# Formater les imports
ruff check --select I --fix .
```

#### Configuration dans `pyproject.toml`

```toml
[tool.ruff]
line-length = 88  
target-version = "py310"  

# Fichiers à exclure
exclude = [
    ".git",
    "__pycache__",
    ".venv",
    "venv",
]

[tool.ruff.lint]
# Règles à activer
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]

# Règles à ignorer
ignore = [
    "E501",  # line too long (géré par Black)
]
```

### 4. mypy - Vérificateur de types

**mypy** vérifie les annotations de types dans votre code Python pour détecter les erreurs avant l'exécution.

#### Installation

```bash
pip install mypy
# ou avec Poetry
poetry add --group dev mypy
```

#### Utilisation

```bash
# Vérifier un fichier
mypy mon_fichier.py

# Vérifier un dossier
mypy src/
```

#### Exemple de code avec types

```python
def additionner(a: int, b: int) -> int:
    return a + b

# mypy détectera l'erreur ici
resultat: str = additionner(5, 10)  # Erreur : int assigné à str
```

#### Configuration dans `pyproject.toml`

```toml
[tool.mypy]
python_version = "3.10"  
warn_return_any = true  
warn_unused_configs = true  
disallow_untyped_defs = true  
```

### 5. pre-commit - Hooks Git automatiques

**pre-commit** exécute automatiquement des vérifications avant chaque commit Git.

#### Installation

```bash
pip install pre-commit
# ou avec Poetry
poetry add --group dev pre-commit
```

#### Configuration `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace  # Supprime espaces en fin de ligne
      - id: end-of-file-fixer    # Ajoute ligne vide en fin de fichier
      - id: check-yaml           # Vérifie syntaxe YAML
      - id: check-added-large-files  # Empêche gros fichiers

  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
```

#### Installation des hooks

```bash
pre-commit install
```

Maintenant, à chaque `git commit`, les outils s'exécutent automatiquement !

### 6. pytest - Framework de tests moderne

**pytest** est l'outil de référence pour écrire et exécuter des tests en Python.

#### Installation

```bash
pip install pytest
# ou avec Poetry
poetry add --group dev pytest
```

#### Structure des tests

```
tests/
├── __init__.py
├── conftest.py          # Configuration partagée
├── test_utils.py
└── test_main.py
```

#### Configuration dans `pyproject.toml`

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]  
python_files = "test_*.py"  
python_functions = "test_*"  
addopts = "-v --tb=short"  
```

#### Exécution des tests

```bash
# Tous les tests
pytest

# Tests avec couverture de code
pytest --cov=src/mon_projet

# Tests d'un fichier spécifique
pytest tests/test_utils.py

# Tests en mode verbose
pytest -v
```

---

## Configuration complète d'un projet moderne

Voici un exemple de `pyproject.toml` complet pour un projet bien configuré :

```toml
[tool.poetry]
name = "mon-projet-moderne"  
version = "0.1.0"  
description = "Un projet Python bien structuré"  
authors = ["Votre Nom <email@example.com>"]  
readme = "README.md"  
packages = [{include = "mon_projet", from = "src"}]  

[tool.poetry.dependencies]
python = "^3.10"  
requests = "^2.31.0"  
pydantic = "^2.5.0"  

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"  
pytest-cov = "^4.1.0"  
black = "^23.11.0"  
ruff = "^0.1.6"  
mypy = "^1.7.0"  
pre-commit = "^3.5.0"  

[build-system]
requires = ["poetry-core"]  
build-backend = "poetry.core.masonry.api"  

[tool.black]
line-length = 88  
target-version = ['py310']  

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I", "B", "C4", "UP"]  
ignore = ["E501"]  

[tool.mypy]
python_version = "3.10"  
warn_return_any = true  
warn_unused_configs = true  

[tool.pytest.ini_options]
testpaths = ["tests"]  
addopts = "-v --cov=src/mon_projet --cov-report=html"  
```

---

## Fichier README.md complet

Voici un template de README professionnel :

```markdown
# Mon Projet Moderne

Description courte et claire de votre projet.

## 🚀 Installation

### Prérequis

- Python 3.10 ou supérieur
- Poetry (recommandé) ou pip

### Avec Poetry (recommandé)

```bash
# Cloner le repository
git clone https://github.com/votre-nom/mon-projet.git  
cd mon-projet  

# Installer les dépendances
poetry install

# Activer l'environnement
poetry shell
```

### Avec pip

```bash
# Cloner le repository
git clone https://github.com/votre-nom/mon-projet.git  
cd mon-projet  

# Créer un environnement virtuel
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation

```python
from mon_projet import MaClasse

# Exemple d'utilisation
instance = MaClasse()  
resultat = instance.faire_quelque_chose()  
print(resultat)  
```

## 🧪 Tests

```bash
# Exécuter tous les tests
pytest

# Avec rapport de couverture
pytest --cov=src/mon_projet --cov-report=html
```

## 🛠️ Développement

### Installation de l'environnement de développement

```bash
poetry install --with dev  
pre-commit install  
```

### Outils de qualité du code

```bash
# Formater le code
black src/

# Vérifier avec le linter
ruff check src/

# Vérifier les types
mypy src/
```

## 📝 Structure du projet

```
mon-projet/
├── src/  
│   └── mon_projet/      # Code source  
├── tests/               # Tests unitaires  
├── docs/                # Documentation  
└── pyproject.toml       # Configuration du projet
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

## 📄 License

Ce projet est sous licence MIT - voir [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**Votre Nom**
- GitHub: [@votre-nom](https://github.com/votre-nom)
- Email: email@example.com
```

---

## Workflow de développement recommandé

Voici un workflow type pour travailler sur votre projet :

### 1. Initialisation du projet

```bash
# Créer le projet avec Poetry
poetry new mon_projet  
cd mon_projet  

# Initialiser Git
git init

# Créer le .gitignore
touch .gitignore  # Puis copier le contenu recommandé

# Installer pre-commit
poetry add --group dev pre-commit black ruff mypy pytest  
poetry install  
pre-commit install  
```

### 2. Développement quotidien

```bash
# 1. Créer une branche pour votre fonctionnalité
git checkout -b feature/ma-nouvelle-fonctionnalite

# 2. Écrire votre code dans src/mon_projet/

# 3. Écrire les tests dans tests/

# 4. Exécuter les tests
poetry run pytest

# 5. Formater et vérifier le code
poetry run black src/ tests/  
poetry run ruff check src/ tests/ --fix  
poetry run mypy src/  

# 6. Commiter (pre-commit s'exécute automatiquement)
git add .  
git commit -m "feat: ajout de ma nouvelle fonctionnalité"  

# 7. Pousser vers le repository
git push origin feature/ma-nouvelle-fonctionnalite
```

### 3. Avant de partager votre code

```bash
# Vérifier que tout fonctionne
poetry run pytest --cov

# Mettre à jour la documentation
# Modifier README.md si nécessaire

# Vérifier la qualité globale
poetry run black --check src/  
poetry run ruff check src/  
poetry run mypy src/  

# Créer une Pull Request sur GitHub/GitLab
```

---

## Comparaison des outils traditionnels vs modernes

| Tâche | Outil traditionnel | Outil moderne | Avantage |
|-------|-------------------|---------------|----------|
| Gestion des dépendances | pip + requirements.txt | Poetry | Résolution de dépendances, fichier lock |
| Formatage du code | Manual (PEP 8) | Black | Automatique, pas de débat |
| Linting | Flake8, Pylint | Ruff | 10-100x plus rapide |
| Vérification de types | Annotations manuelles | mypy | Détection d'erreurs automatique |
| Tests | unittest | pytest | Syntaxe plus simple, plus de fonctionnalités |
| Environnement virtuel | venv + pip | Poetry | Géré automatiquement |

---

## Conseils pour débuter

### Commencez simple

Ne vous sentez pas obligé d'utiliser tous ces outils dès le début ! Voici une progression naturelle :

**Niveau 1 - Débutant :**
- Structure de dossiers basique (src/, tests/, README.md)
- requirements.txt
- .gitignore

**Niveau 2 - Intermédiaire :**
- Poetry pour la gestion des dépendances
- Black pour le formatage
- pytest pour les tests

**Niveau 3 - Avancé :**
- Ruff pour le linting
- mypy pour les types
- pre-commit pour les hooks
- Configuration complète dans pyproject.toml

### Adoptez progressivement les bonnes pratiques

1. **Commencez par la structure** : organisez votre code en modules dès le départ
2. **Ajoutez des tests** : même simples, ils apportent beaucoup de valeur
3. **Documentez** : un bon README fait toute la différence
4. **Automatisez** : les outils modernes vous font gagner du temps

### Ressources pour aller plus loin

- **Documentation officielle Poetry** : https://python-poetry.org/docs/
- **Guide Black** : https://black.readthedocs.io/
- **Documentation Ruff** : https://docs.astral.sh/ruff/
- **pytest documentation** : https://docs.pytest.org/
- **Python Packaging Guide** : https://packaging.python.org/

---

## Résumé

Une bonne architecture de projet Python moderne comprend :

✅ **Structure claire** : séparation du code source, des tests et de la documentation

✅ **Gestion des dépendances** : Poetry ou requirements.txt

✅ **Qualité du code** : Black (formatage), Ruff (linting), mypy (types)

✅ **Tests automatisés** : pytest avec couverture de code

✅ **Contrôle de version** : Git avec .gitignore approprié

✅ **Documentation** : README.md complet et à jour

✅ **Automatisation** : pre-commit hooks pour maintenir la qualité

L'objectif n'est pas d'utiliser tous ces outils immédiatement, mais de comprendre leur utilité et de les adopter progressivement au fur et à mesure que vos projets grandissent en complexité.

Un projet bien structuré est un projet qui vous fera gagner du temps à long terme, facilitera la collaboration et rendra votre code plus professionnel ! 🚀

⏭️ [Gestion de version avec Git](/12-projets-et-bonnes-pratiques/02-gestion-version-git.md)
