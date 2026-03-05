🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.5 Déploiement et distribution

## Introduction

Vous avez créé une application Python qui fonctionne parfaitement sur votre ordinateur. Maintenant, vous voulez la partager avec le monde ! C'est là qu'intervient le **déploiement** et la **distribution**.

### Qu'est-ce que le déploiement ?

Le **déploiement** consiste à rendre votre application accessible aux utilisateurs finaux. Cela peut signifier :
- Publier une bibliothèque Python sur PyPI
- Mettre en ligne une application web
- Distribuer un script ou un outil en ligne de commande
- Créer un exécutable pour Windows/Mac/Linux

### Qu'est-ce que la distribution ?

La **distribution** est le processus de **packager** votre code pour qu'il soit facilement installable et utilisable par d'autres.

### Les différents types de déploiement

📦 **Package Python** : bibliothèque installable avec `pip`

🌐 **Application web** : site web accessible via un navigateur

🖥️ **Application desktop** : programme avec interface graphique

⚙️ **Script/CLI** : outil en ligne de commande

🐳 **Conteneur Docker** : application dans un environnement isolé

---

## Préparation du code pour le déploiement

Avant de déployer, assurez-vous que votre code est prêt.

### 1. Structure du projet claire

```
mon_projet/
├── src/
│   └── mon_projet/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_main.py
├── docs/
│   └── README.md
├── .gitignore
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

### 2. Fichier requirements.txt à jour

Listez toutes les dépendances nécessaires :

```bash
# Générer requirements.txt
pip freeze > requirements.txt
```

Ou créez-le manuellement avec les versions :

```txt
# requirements.txt
requests>=2.28.0  
fastapi>=0.100.0  
pydantic>=2.0.0  
uvicorn[standard]>=0.23.0  
```

**Bonnes pratiques** :
- Utilisez `>=` pour les versions minimales
- Utilisez `==` seulement si une version spécifique est requise
- Commentez les dépendances non évidentes

### 3. Variables d'environnement

Ne commitez **JAMAIS** de secrets (mots de passe, clés API) dans votre code !

**Mauvais** ❌ :
```python
# config.py
DATABASE_URL = "postgresql://user:password@localhost/db"  
API_KEY = "sk_live_123456789"  
```

**Bon** ✅ :
```python
# config.py
import os

DATABASE_URL = os.getenv("DATABASE_URL")  
API_KEY = os.getenv("API_KEY")  

if not API_KEY:
    raise ValueError("API_KEY n'est pas définie")
```

Créez un fichier `.env` (et ajoutez-le au `.gitignore`) :

```bash
# .env (ne pas commiter !)
DATABASE_URL=postgresql://user:password@localhost/db  
API_KEY=sk_live_123456789  
DEBUG=True  
```

Utilisez `python-dotenv` pour charger les variables :

```bash
pip install python-dotenv
```

```python
# config.py
from dotenv import load_dotenv  
import os  

# Charger les variables d'environnement
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  
API_KEY = os.getenv("API_KEY")  
DEBUG = os.getenv("DEBUG", "False") == "True"  
```

### 4. Fichier de configuration

Créez un fichier de configuration centralisé :

```python
# config.py
import os  
from pathlib import Path  

class Config:
    """Configuration de base"""
    # Chemins
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"

    # Base de données
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

    # API
    API_KEY = os.getenv("API_KEY")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

    # Debug
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

class ProductionConfig(Config):
    """Configuration pour la production"""
    DEBUG = False

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"

# Sélectionner la configuration
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

env = os.getenv("ENVIRONMENT", "development")  
config = config_map[env]()  
```

### 5. Logging approprié

Configurez le logging pour la production :

```python
# logger.py
import logging  
import sys  

def setup_logger(name: str, level: str = "INFO"):
    """Configure le logger"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # Handler pour la console
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # Format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Utilisation
logger = setup_logger(__name__)  
logger.info("Application démarrée")  
logger.error("Une erreur s'est produite")  
```

---

## Créer un package Python

Si vous voulez que d'autres puissent installer votre code avec `pip install mon_package`, vous devez créer un package.

### Structure d'un package

```
mon_package/
├── src/
│   └── mon_package/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   └── test_module1.py
├── README.md
├── LICENSE
├── setup.py
├── setup.cfg
└── pyproject.toml
```

### Le fichier `setup.py`

```python
# setup.py
from setuptools import setup, find_packages

# Lire le README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lire les requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mon_package",
    version="0.1.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Une courte description de votre package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-nom/mon_package",
    project_urls={
        "Bug Tracker": "https://github.com/votre-nom/mon_package/issues",
        "Documentation": "https://mon-package.readthedocs.io/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mon_package=mon_package.main:main",
        ],
    },
)
```

### Le fichier `pyproject.toml` (moderne)

Le format moderne et recommandé est `pyproject.toml` (PEP 621) :

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=45", "wheel"]  
build-backend = "setuptools.build_meta"  

[project]
name = "mon_package"  
version = "0.1.0"  
description = "Une courte description de votre package"  
readme = "README.md"  
authors = [  
    {name = "Votre Nom", email = "votre.email@example.com"}
]
license = {text = "MIT"}  
classifiers = [  
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
keywords = ["exemple", "tutorial", "python"]  
requires-python = ">=3.10"  
dependencies = [  
    "requests>=2.28.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "mypy>=1.0",
]

[project.urls]
Homepage = "https://github.com/votre-nom/mon_package"  
Documentation = "https://mon-package.readthedocs.io/"  
Repository = "https://github.com/votre-nom/mon_package.git"  
"Bug Tracker" = "https://github.com/votre-nom/mon_package/issues"

[project.scripts]
mon_package = "mon_package.main:main"

[tool.setuptools.packages.find]
where = ["src"]
```

### Le fichier `__init__.py`

```python
# src/mon_package/__init__.py
"""
Mon Package
~~~~~~~~~~~

Description de votre package.

Exemple d'utilisation :
    >>> from mon_package import ma_fonction
    >>> ma_fonction()
"""

__version__ = "0.1.0"
__author__ = "Votre Nom"
__email__ = "votre.email@example.com"

# Importer les fonctions principales pour faciliter l'usage
from .module1 import fonction_importante  
from .module2 import AutreClasse  

__all__ = [
    "fonction_importante",
    "AutreClasse",
]
```

### Construire le package

```bash
# Installer les outils nécessaires
pip install build twine

# Construire le package
python -m build

# Cela crée :
# - dist/mon_package-0.1.0.tar.gz (source distribution)
# - dist/mon_package-0.1.0-py3-none-any.whl (wheel)
```

### Tester localement

```bash
# Installer votre package en mode éditable (développement)
pip install -e .

# Ou installer le package construit
pip install dist/mon_package-0.1.0-py3-none-any.whl
```

---

## Publier sur PyPI

PyPI (Python Package Index) est le dépôt officiel des packages Python.

### Créer un compte

1. Allez sur [pypi.org](https://pypi.org/)
2. Créez un compte
3. Vérifiez votre email
4. Activez l'authentification à deux facteurs (recommandé)
5. Créez un token API dans les paramètres de votre compte

### Publier sur TestPyPI (recommandé pour débuter)

TestPyPI est une version de test de PyPI :

```bash
# Installer twine si ce n'est pas déjà fait
pip install twine

# Publier sur TestPyPI
python -m twine upload --repository testpypi dist/*

# Vous serez invité à entrer :
# Username: __token__
# Password: votre-token-api
```

### Tester l'installation depuis TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ mon_package
```

### Publier sur PyPI (production)

Une fois que tout fonctionne sur TestPyPI :

```bash
# Publier sur PyPI
python -m twine upload dist/*

# Maintenant tout le monde peut installer votre package !
pip install mon_package
```

### Automatiser avec `.pypirc`

Créez un fichier `~/.pypirc` pour éviter de retaper vos identifiants :

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__  
password = votre-token-pypi  

[testpypi]
repository = https://test.pypi.org/legacy/  
username = __token__  
password = votre-token-testpypi  
```

**Important** : Ne commitez jamais ce fichier ! Ajoutez-le au `.gitignore`.

---

## Versionnage sémantique

Utilisez le **versionnage sémantique** (SemVer) : `MAJOR.MINOR.PATCH`

### Format : `X.Y.Z`

- **X (MAJOR)** : changements incompatibles avec les versions précédentes
- **Y (MINOR)** : nouvelles fonctionnalités compatibles
- **Z (PATCH)** : corrections de bugs compatibles

### Exemples

```
1.0.0   → Première version stable
1.0.1   → Correction d'un bug
1.1.0   → Ajout d'une nouvelle fonctionnalité
2.0.0   → Changement cassant l'API
```

### Phases de développement

```
0.1.0   → Développement initial
0.2.0   → Nouvelles fonctionnalités (alpha)
0.9.0   → Version beta
1.0.0   → Première version stable
1.0.1   → Correction de bug
2.0.0   → Nouvelle version majeure
```

### Gestion des versions dans le code

```python
# src/mon_package/__version__.py
__version__ = "0.1.0"

# src/mon_package/__init__.py
from .__version__ import __version__

# setup.py ou pyproject.toml
# Lire la version depuis __version__.py
import re  
from pathlib import Path  

version_file = Path("src/mon_package/__version__.py")  
version_match = re.search(r'^__version__ = ["\']([^"\']*)["\']', version_file.read_text(encoding='utf-8'), re.M)  
version = version_match.group(1) if version_match else "0.0.0"  
```

---

## Déploiement d'applications web

### Option 1 : Heroku (Simple, payant)

**Heroku** est une plateforme cloud qui simplifie le déploiement (plans à partir de ~5$/mois).

#### Prérequis

```bash
# Installer Heroku CLI
# Windows : télécharger depuis heroku.com
# Mac : brew install heroku/brew/heroku
# Linux : curl https://cli-assets.heroku.com/install.sh | sh
```

#### Préparation de l'application

Créez un fichier `Procfile` à la racine :

```
# Procfile (pour application web)
web: uvicorn main:app --host 0.0.0.0 --port $PORT

# Ou pour Flask
web: gunicorn main:app --bind 0.0.0.0:$PORT

# Ou pour Django
web: gunicorn myproject.wsgi --log-file -
```

Créez un fichier `runtime.txt` :

```txt
# runtime.txt
python-3.11.0
```

#### Déploiement

```bash
# Se connecter à Heroku
heroku login

# Créer une application
heroku create mon-app-python

# Ajouter les variables d'environnement
heroku config:set API_KEY=votre_cle_api  
heroku config:set DATABASE_URL=votre_url_database  

# Déployer avec Git
git add .  
git commit -m "Prêt pour le déploiement"  
git push heroku main  

# Ouvrir l'application
heroku open

# Voir les logs
heroku logs --tail
```

### Option 2 : Render (Gratuit et moderne)

**Render** est une alternative moderne à Heroku.

#### Déploiement sur Render

1. Créez un compte sur [render.com](https://render.com)
2. Créez un nouveau "Web Service"
3. Connectez votre repository GitHub
4. Configurez :
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Ajoutez les variables d'environnement
6. Déployez !

### Option 3 : DigitalOcean App Platform

1. Créez un compte sur [digitalocean.com](https://www.digitalocean.com/)
2. Créez une nouvelle App
3. Connectez votre repository
4. L'application se déploie automatiquement

### Option 4 : Railway

**Railway** offre un déploiement ultra-simple :

```bash
# Installer Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialiser
railway init

# Déployer
railway up
```

### Option 5 : Vercel (pour FastAPI/Flask)

```bash
# Installer Vercel CLI
npm install -g vercel

# Créer vercel.json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}

# Déployer
vercel
```

---

## Docker : Conteneurisation

**Docker** permet d'empaqueter votre application avec toutes ses dépendances.

### Pourquoi Docker ?

✅ **Reproductibilité** : fonctionne partout de la même façon

✅ **Isolation** : chaque application dans son propre environnement

✅ **Déploiement simplifié** : une seule commande pour déployer

✅ **Scalabilité** : facile de multiplier les instances

### Installation de Docker

- **Windows/Mac** : Docker Desktop ([docker.com](https://www.docker.com/))
- **Linux** : `sudo apt install docker.io` (Ubuntu)

### Créer un Dockerfile

```dockerfile
# Dockerfile
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile optimisé (avec cache)

```dockerfile
# Dockerfile
FROM python:3.11-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Créer un utilisateur non-root
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Installer les dépendances (layer en cache)
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copier le code
COPY --chown=appuser:appuser . .

# Changer d'utilisateur
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Fichier `.dockerignore`

Créez un `.dockerignore` pour exclure les fichiers inutiles :

```
# .dockerignore
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/  
env/  
.git/
.gitignore
.vscode/
.idea/
*.md
tests/
.pytest_cache/
.coverage
htmlcov/  
dist/  
build/  
*.egg-info/
```

### Construire et exécuter

```bash
# Construire l'image
docker build -t mon-app:latest .

# Exécuter le conteneur
docker run -p 8000:8000 mon-app:latest

# Exécuter en arrière-plan
docker run -d -p 8000:8000 --name mon-app-container mon-app:latest

# Voir les logs
docker logs mon-app-container

# Arrêter le conteneur
docker stop mon-app-container

# Supprimer le conteneur
docker rm mon-app-container
```

### Docker Compose (plusieurs services)

Créez un `docker-compose.yml` pour gérer plusieurs services :

```yaml
# docker-compose.yml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - API_KEY=${API_KEY}
    depends_on:
      - db
    volumes:
      - .:/app
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Utilisation :

```bash
# Démarrer tous les services
docker-compose up

# Démarrer en arrière-plan
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter tous les services
docker-compose down

# Reconstruire et démarrer
docker-compose up --build
```

### Publier sur Docker Hub

```bash
# Se connecter
docker login

# Taguer l'image
docker tag mon-app:latest votre-nom/mon-app:latest

# Pousser sur Docker Hub
docker push votre-nom/mon-app:latest

# Maintenant n'importe qui peut l'utiliser :
docker pull votre-nom/mon-app:latest  
docker run -p 8000:8000 votre-nom/mon-app:latest  
```

---

## Déploiement sur le cloud

### AWS (Amazon Web Services)

#### Option 1 : AWS Elastic Beanstalk (Simple)

```bash
# Installer EB CLI
pip install awsebcli

# Initialiser
eb init -p python-3.11 mon-app

# Créer un environnement et déployer
eb create mon-app-env

# Déployer les mises à jour
eb deploy

# Ouvrir l'application
eb open

# Voir les logs
eb logs
```

#### Option 2 : AWS Lambda (Serverless)

Pour des fonctions simples sans serveur :

```python
# lambda_function.py
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
```

Packager :
```bash
# Créer un package avec dépendances
pip install -r requirements.txt -t .  
zip -r function.zip .  

# Uploader sur AWS Lambda via la console
```

#### Option 3 : AWS ECS (Docker)

Déployer vos conteneurs Docker sur AWS ECS (Elastic Container Service).

### Google Cloud Platform (GCP)

#### Google Cloud Run (Docker serverless)

```bash
# Installer gcloud CLI
# Suivre les instructions sur cloud.google.com

# Se connecter
gcloud auth login

# Créer un projet
gcloud projects create mon-projet

# Définir le projet
gcloud config set project mon-projet

# Construire l'image
gcloud builds submit --tag gcr.io/mon-projet/mon-app

# Déployer sur Cloud Run
gcloud run deploy mon-app \
  --image gcr.io/mon-projet/mon-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

#### Google App Engine (PaaS)

```yaml
# app.yaml
runtime: python311

entrypoint: gunicorn -b :$PORT main:app

env_variables:
  API_KEY: "votre-cle"
```

```bash
# Déployer
gcloud app deploy
```

### Microsoft Azure

#### Azure App Service

```bash
# Installer Azure CLI
# Suivre les instructions sur azure.microsoft.com

# Se connecter
az login

# Créer un groupe de ressources
az group create --name mon-groupe --location westeurope

# Créer un plan App Service
az appservice plan create --name mon-plan --resource-group mon-groupe --sku B1 --is-linux

# Créer l'application web
az webapp create --resource-group mon-groupe --plan mon-plan --name mon-app --runtime "PYTHON|3.11"

# Configurer pour déploiement Git
az webapp deployment source config-local-git --name mon-app --resource-group mon-groupe

# Pousser votre code
git remote add azure <url-git-fournie>  
git push azure main  
```

---

## CI/CD : Intégration et déploiement continus

L'**intégration continue** (CI) teste automatiquement votre code à chaque commit. Le **déploiement continu** (CD) déploie automatiquement les versions validées.

### GitHub Actions

Créez `.github/workflows/ci-cd.yml` :

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: Run tests
      run: |
        pytest --cov=src tests/

    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 src/ --max-line-length=88

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v4

    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "mon-app"
        heroku_email: "votre.email@example.com"
```

### GitLab CI/CD

Créez `.gitlab-ci.yml` :

```yaml
# .gitlab-ci.yml
stages:
  - test
  - deploy

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - venv/

test:
  stage: test
  image: python:3.11
  script:
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
    - pytest --cov=src tests/
  only:
    - main
    - merge_requests

deploy:
  stage: deploy
  image: python:3.11
  script:
    - pip install build twine
    - python -m build
    - twine upload dist/*
  only:
    - tags
  when: manual
```

---

## Monitoring et maintenance

Une fois déployée, votre application a besoin de **surveillance**.

### Logging en production

```python
# logger.py
import logging  
import sys  
from logging.handlers import RotatingFileHandler  

def setup_production_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # File handler (rotation)
    file_handler = RotatingFileHandler(
        'app.log',
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(logging.WARNING)

    # Format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
```

### Services de monitoring

**Sentry** (erreurs et exceptions) :

```bash
pip install sentry-sdk
```

```python
import sentry_sdk

sentry_sdk.init(
    dsn="votre-dsn-sentry",
    traces_sample_rate=1.0,
)

# Les erreurs seront automatiquement envoyées à Sentry
```

**New Relic** (performance) :

```bash
pip install newrelic
```

```python
import newrelic.agent  
newrelic.agent.initialize('newrelic.ini')  
```

### Health checks

Ajoutez un endpoint de santé :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/ready")
async def readiness_check():
    # Vérifier base de données, etc.
    return {"status": "ready"}
```

---

## Documentation et README

Un bon README est **essentiel** pour que les autres utilisent votre projet.

### Template de README complet

```markdown
# Mon Projet Python

![CI/CD](https://github.com/votre-nom/mon-projet/workflows/CI/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Description courte et accrocheuse de votre projet.

## 🚀 Fonctionnalités

- ✨ Fonctionnalité 1
- 🔥 Fonctionnalité 2
- 💪 Fonctionnalité 3

## 📋 Prérequis

- Python 3.10 ou supérieur
- pip
- (Autres prérequis)

## 🔧 Installation

### Installation via pip

```bash
pip install mon-projet
```

### Installation depuis les sources

```bash
git clone https://github.com/votre-nom/mon-projet.git  
cd mon-projet  
pip install -r requirements.txt  
```

## 💻 Utilisation

### Exemple basique

```python
from mon_projet import ma_fonction

resultat = ma_fonction("exemple")  
print(resultat)  
```

### Exemple avancé

```python
from mon_projet import MaClasse

instance = MaClasse(param1="valeur1")  
instance.faire_quelque_chose()  
```

## 🐳 Docker

```bash
docker build -t mon-projet .  
docker run -p 8000:8000 mon-projet  
```

## 🧪 Tests

```bash
pytest
```

## 📚 Documentation

Documentation complète disponible sur [docs.mon-projet.com](https://docs.mon-projet.com)

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md).

1. Fork le projet
2. Créez une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commitez (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. Push (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 📝 Changelog

Voir [CHANGELOG.md](CHANGELOG.md) pour l'historique des versions.

## 📄 Licence

Ce projet est sous licence MIT - voir [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Votre Nom** - [GitHub](https://github.com/votre-nom)

## 🙏 Remerciements

- Merci à [contributeur] pour [contribution]
- Inspiré par [projet]

## 📧 Contact

Pour toute question : votre.email@example.com

## 🔗 Liens utiles

- [Documentation](https://docs.mon-projet.com)
- [Issues](https://github.com/votre-nom/mon-projet/issues)
- [Discussions](https://github.com/votre-nom/mon-projet/discussions)
```

---

## Checklist de déploiement

Avant de déployer en production, vérifiez :

### ✅ Code

- [ ] Tous les tests passent
- [ ] Code formaté (Black, Ruff)
- [ ] Pas de warnings
- [ ] Type hints vérifiés (mypy)
- [ ] Documentation à jour

### ✅ Configuration

- [ ] Variables d'environnement configurées
- [ ] Aucun secret dans le code
- [ ] Fichier .env.example fourni
- [ ] Configuration production vs développement

### ✅ Dépendances

- [ ] requirements.txt à jour
- [ ] Versions spécifiées
- [ ] Pas de dépendances inutiles

### ✅ Sécurité

- [ ] Secrets dans variables d'environnement
- [ ] HTTPS activé
- [ ] CORS configuré correctement
- [ ] Rate limiting activé
- [ ] Validation des inputs

### ✅ Performance

- [ ] Caching configuré
- [ ] Base de données indexée
- [ ] Connexions poolées
- [ ] Logs optimisés

### ✅ Monitoring

- [ ] Logging configuré
- [ ] Health checks en place
- [ ] Alertes configurées
- [ ] Backup automatique

### ✅ Documentation

- [ ] README complet
- [ ] CHANGELOG à jour
- [ ] LICENSE présent
- [ ] Documentation API

### ✅ Infrastructure

- [ ] Dockerfile testé
- [ ] docker-compose.yml valide
- [ ] CI/CD configuré
- [ ] Rollback possible

---

## Bonnes pratiques de déploiement

### 1. Déploiement progressif

Ne déployez pas tout d'un coup en production :

```
Développement → Staging → Production
```

### 2. Blue-Green Deployment

Maintenez deux environnements identiques :
- **Blue** : version actuelle en production
- **Green** : nouvelle version

Basculez de Blue à Green une fois que tout est validé.

### 3. Canary Deployment

Déployez progressivement :
- 5% du trafic sur la nouvelle version
- Si OK, 25% du trafic
- Si OK, 50% du trafic
- Si OK, 100% du trafic

### 4. Rollback rapide

Toujours avoir un plan B :

```bash
# Git tags pour version
git tag v1.2.3  
git push --tags  

# En cas de problème
git checkout v1.2.2
# Redéployer
```

### 5. Database migrations

Utilisez des outils de migration :

```bash
# Avec Alembic (SQLAlchemy)
alembic init alembic  
alembic revision --autogenerate -m "Initial migration"  
alembic upgrade head  

# Rollback si nécessaire
alembic downgrade -1
```

### 6. Zero-downtime deployment

- Utilisez un load balancer
- Déployez sur une instance à la fois
- Health checks avant de router le trafic

---

## Sécurité en production

### 1. Ne jamais exposer de secrets

```python
# ❌ Mauvais
DATABASE_URL = "postgresql://user:password@localhost/db"

# ✅ Bon
DATABASE_URL = os.getenv("DATABASE_URL")
```

### 2. Utiliser HTTPS

```python
# Avec FastAPI
from fastapi import FastAPI  
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware  

app = FastAPI()  
app.add_middleware(HTTPSRedirectMiddleware)  
```

### 3. Rate limiting

```python
from slowapi import Limiter  
from slowapi.util import get_remote_address  

limiter = Limiter(key_func=get_remote_address)

@app.get("/api/data")
@limiter.limit("5/minute")
async def get_data():
    return {"data": "..."}
```

### 4. Validation des inputs

```python
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    email: EmailStr
    age: int

    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('Age invalide')
        return v
```

### 5. Mise à jour régulière des dépendances

```bash
# Vérifier les vulnérabilités
pip install safety  
safety check  

# Mettre à jour les dépendances
pip install --upgrade -r requirements.txt
```

---

## Résumé

Le déploiement d'une application Python implique plusieurs étapes :

### 📦 Préparation

✅ Structure de projet claire

✅ Variables d'environnement pour les secrets

✅ Configuration séparée (dev/prod)

✅ Tests qui passent

### 🚀 Distribution

✅ Package Python avec `setup.py` ou `pyproject.toml`

✅ Publication sur PyPI

✅ Versionnage sémantique

### 🌐 Déploiement web

✅ Plateformes simples : Heroku, Render, Railway

✅ Cloud providers : AWS, GCP, Azure

✅ Conteneurisation avec Docker

### 🔄 CI/CD

✅ GitHub Actions / GitLab CI

✅ Tests automatiques

✅ Déploiement automatique

### 📊 Monitoring

✅ Logging approprié

✅ Health checks

✅ Alertes (Sentry, etc.)

### 🔒 Sécurité

✅ Pas de secrets dans le code

✅ HTTPS activé

✅ Rate limiting

✅ Validation des inputs

### Pour débuter

1. **Commencez simple** : Heroku ou Render pour vos premières apps
2. **Automatisez** : CI/CD dès le début
3. **Documentez** : un bon README est crucial
4. **Surveillez** : logs et monitoring dès le départ
5. **Itérez** : déployez souvent, apprenez des erreurs

Le déploiement peut sembler complexe au début, mais avec la pratique, il devient une seconde nature. Chaque déploiement est une opportunité d'apprendre et d'améliorer votre processus ! 🚀

⏭️ [Introduction à la Data Science](/13-introduction-data-science/README.md)
