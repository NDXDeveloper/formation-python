🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.5 : Déploiement et distribution

## Introduction

Imaginez que vous avez créé une magnifique application Python sur votre ordinateur. Elle fonctionne parfaitement, mais maintenant vous voulez que d'autres personnes puissent l'utiliser. Comment faire ? C'est là qu'interviennent le déploiement et la distribution !

Le **déploiement** consiste à mettre votre application en production (sur un serveur accessible au public), tandis que la **distribution** consiste à empaqueter votre code pour que d'autres développeurs puissent l'installer facilement.

Pensez-y comme la différence entre :
- 🏠 **Distribution** : Donner la recette d'un gâteau (package Python)
- 🍰 **Déploiement** : Ouvrir une pâtisserie qui vend le gâteau (application web)

## Pourquoi c'est important ?

### Les défis du passage en production

Votre code qui fonctionne sur votre machine peut rencontrer des problèmes ailleurs :

```python
# Sur votre machine : ✅ Ça marche
import mon_module_local

# Sur le serveur : ❌ Module introuvable !
# ModuleNotFoundError: No module named 'mon_module_local'
```

### Les différences d'environnement

| Votre machine | Serveur de production |
|---------------|----------------------|
| Python 3.11   | Python 3.9          |
| 16 GB RAM     | 2 GB RAM            |
| SSD rapide    | Disque lent         |
| Développement | Performance critique |

## Types de déploiement

### 1. Application web (serveur)

Votre application tourne sur un serveur et les utilisateurs y accèdent via un navigateur.

```
Utilisateur → Navigateur → Internet → Serveur → Votre App Python
```

### 2. Package Python (distribution)

Votre code devient une bibliothèque que d'autres développeurs peuvent installer.

```bash
pip install votre-package
```

### 3. Application desktop

Votre application devient un exécutable que les utilisateurs installent sur leur ordinateur.

```
votre-app.exe  # Windows
votre-app.dmg  # macOS
votre-app.deb  # Linux
```

## Préparation au déploiement

### Structurer votre projet

Une structure propre facilite grandement le déploiement :

```
mon-projet/
├── README.md
├── requirements.txt          # Dépendances
├── setup.py                 # Configuration du package
├── .env.example             # Variables d'environnement
├── .gitignore               # Fichiers à ignorer
├── Dockerfile               # Pour Docker
├── src/
│   └── mon_projet/
│       ├── __init__.py
│       ├── main.py
│       ├── config/
│       └── utils/
├── tests/
│   └── test_main.py
├── docs/
│   └── installation.md
└── scripts/
    ├── start.sh             # Script de démarrage
    └── deploy.sh            # Script de déploiement
```

### Gérer les dépendances

#### Fichier requirements.txt

```txt
# requirements.txt
# Dépendances principales
flask==2.3.3
requests==2.31.0
pandas==2.0.3

# Dépendances de développement (optionnel)
pytest==7.4.0
black==23.7.0
flake8==6.0.0
```

#### Générer requirements.txt

```bash
# Installer vos packages
pip install flask requests pandas

# Générer le fichier
pip freeze > requirements.txt

# Ou plus proprement (sans les sous-dépendances)
pip list --format=freeze --not-required > requirements.txt
```

#### Installer les dépendances

```bash
# Sur le serveur de production
pip install -r requirements.txt
```

### Variables d'environnement

Les informations sensibles (mots de passe, clés API) ne doivent jamais être dans le code !

#### Fichier .env.example

```env
# .env.example - Template pour les variables d'environnement
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key-here
DEBUG=False
PORT=5000
```

#### Utilisation dans le code

```python
# config.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class Config:
    """Configuration de l'application."""

    # Variables d'environnement avec valeurs par défaut
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))

    # Validation
    if not SECRET_KEY or SECRET_KEY == 'dev-secret-key':
        if not DEBUG:
            raise ValueError("SECRET_KEY doit être définie en production!")

# main.py
from config import Config

def create_app():
    """Crée l'application avec la configuration."""
    config = Config()

    print(f"🚀 Démarrage en mode {'DEBUG' if config.DEBUG else 'PRODUCTION'}")
    print(f"🔗 Base de données: {config.DATABASE_URL}")

    return config

if __name__ == "__main__":
    config = create_app()
```

### Scripts de déploiement

#### Script de démarrage (start.sh)

```bash
#!/bin/bash
# start.sh - Script pour démarrer l'application

echo "🚀 Démarrage de l'application..."

# Vérifier que Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 non trouvé!"
    exit 1
fi

# Créer l'environnement virtuel s'il n'existe pas
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
echo "📚 Installation des dépendances..."
pip install -r requirements.txt

# Vérifier que le fichier .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Fichier .env manquant!"
    echo "📋 Copiez .env.example vers .env et configurez vos variables"
    cp .env.example .env
    echo "✏️  Éditez le fichier .env avant de redémarrer"
    exit 1
fi

# Démarrer l'application
echo "✅ Démarrage de l'application..."
python src/mon_projet/main.py
```

#### Script de déploiement (deploy.sh)

```bash
#!/bin/bash
# deploy.sh - Script de déploiement automatisé

set -e  # Arrêter en cas d'erreur

echo "🚀 Déploiement automatisé"

# Étape 1: Tests
echo "🧪 Exécution des tests..."
python -m pytest tests/ -v
if [ $? -ne 0 ]; then
    echo "❌ Tests échoués! Déploiement annulé."
    exit 1
fi

# Étape 2: Build
echo "🏗️  Construction du package..."
python setup.py sdist bdist_wheel

# Étape 3: Sauvegarde
echo "💾 Sauvegarde de la version actuelle..."
if [ -d "backup" ]; then
    rm -rf backup
fi
mkdir backup
cp -r src backup/

# Étape 4: Déploiement
echo "📦 Déploiement des nouveaux fichiers..."
# Ici vous copieriez vers votre serveur
# rsync -av src/ user@server:/path/to/app/

# Étape 5: Redémarrage des services
echo "🔄 Redémarrage des services..."
# sudo systemctl restart mon-app
# ou
# supervisorctl restart mon-app

echo "✅ Déploiement terminé avec succès!"
```

## Création d'un package Python

### Fichier setup.py

Le fichier `setup.py` définit comment votre projet peut être installé :

```python
# setup.py
from setuptools import setup, find_packages

# Lire le README pour la description longue
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lire les requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    # Informations de base
    name="mon-super-projet",
    version="1.0.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Un package Python fantastique",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votreusername/mon-super-projet",

    # Configuration du package
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    # Métadonnées
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],

    # Dépendances
    python_requires=">=3.8",
    install_requires=requirements,

    # Dépendances optionnelles
    extras_require={
        "dev": ["pytest>=7.0", "black>=23.0", "flake8>=6.0"],
        "docs": ["sphinx>=5.0", "sphinx-rtd-theme>=1.0"],
    },

    # Scripts en ligne de commande
    entry_points={
        "console_scripts": [
            "mon-cli=mon_projet.cli:main",
        ],
    },

    # Fichiers de données à inclure
    include_package_data=True,
    package_data={
        "mon_projet": ["data/*.json", "templates/*.html"],
    },
)
```

### Construction du package

```bash
# Installer les outils de build
pip install build twine

# Construire le package
python -m build

# Cela créé :
# dist/
# ├── mon-super-projet-1.0.0.tar.gz        # Source distribution
# └── mon_super_projet-1.0.0-py3-none-any.whl  # Wheel distribution
```

### Publication sur PyPI

```bash
# 1. Créer un compte sur https://pypi.org/

# 2. Installer twine
pip install twine

# 3. Vérifier le package
twine check dist/*

# 4. Tester sur TestPyPI d'abord (recommandé)
twine upload --repository testpypi dist/*

# 5. Publier sur PyPI
twine upload dist/*

# 6. Installer votre package
pip install mon-super-projet
```

### Exemple complet : Package de calculatrice

Créons un package complet pour une calculatrice :

#### Structure du projet

```
calculatrice-package/
├── README.md
├── setup.py
├── requirements.txt
├── src/
│   └── calculatrice/
│       ├── __init__.py
│       ├── core.py
│       ├── cli.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_cli.py
└── examples/
    └── example_usage.py
```

#### Code source

**src/calculatrice/__init__.py**
```python
"""
Calculatrice - Un package Python pour les calculs simples.

Usage:
    from calculatrice import Calculator

    calc = Calculator()
    result = calc.add(2, 3)
    print(result)  # 5
"""

from .core import Calculator
from .utils import validate_number

__version__ = "1.0.0"
__author__ = "Votre Nom"
__all__ = ["Calculator", "validate_number"]
```

**src/calculatrice/core.py**
```python
"""Module principal de la calculatrice."""

from .utils import validate_number

class Calculator:
    """Calculatrice simple avec historique."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Additionne deux nombres."""
        validate_number(a)
        validate_number(b)

        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Soustrait deux nombres."""
        validate_number(a)
        validate_number(b)

        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiplie deux nombres."""
        validate_number(a)
        validate_number(b)

        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divise deux nombres."""
        validate_number(a)
        validate_number(b)

        if b == 0:
            raise ValueError("Division par zéro impossible")

        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """Retourne l'historique des calculs."""
        return self.history.copy()

    def clear_history(self):
        """Efface l'historique."""
        self.history.clear()
```

**src/calculatrice/utils.py**
```python
"""Fonctions utilitaires."""

def validate_number(value):
    """Valide qu'une valeur est un nombre."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Attendu un nombre, reçu {type(value).__name__}")

    if isinstance(value, float) and value != value:  # NaN check
        raise ValueError("NaN n'est pas autorisé")
```

**src/calculatrice/cli.py**
```python
"""Interface en ligne de commande."""

import sys
from .core import Calculator

def main():
    """Point d'entrée de l'interface CLI."""
    print("🧮 Calculatrice CLI")
    print("Commandes: add, sub, mul, div, history, quit")

    calc = Calculator()

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command == "quit" or command == "q":
                break
            elif command == "history":
                history = calc.get_history()
                if history:
                    print("Historique:")
                    for operation in history:
                        print(f"  {operation}")
                else:
                    print("Aucun historique")
            elif command in ["add", "sub", "mul", "div"]:
                try:
                    a = float(input("Premier nombre: "))
                    b = float(input("Deuxième nombre: "))

                    if command == "add":
                        result = calc.add(a, b)
                    elif command == "sub":
                        result = calc.subtract(a, b)
                    elif command == "mul":
                        result = calc.multiply(a, b)
                    elif command == "div":
                        result = calc.divide(a, b)

                    print(f"Résultat: {result}")

                except ValueError as e:
                    print(f"Erreur: {e}")
            else:
                print("Commande inconnue")

        except KeyboardInterrupt:
            break
        except EOFError:
            break

    print("\nAu revoir!")

if __name__ == "__main__":
    main()
```

#### Tests

**tests/test_core.py**
```python
"""Tests pour le module core."""

import pytest
from calculatrice import Calculator

def test_calculator_creation():
    """Test la création d'une calculatrice."""
    calc = Calculator()
    assert calc.get_history() == []

def test_addition():
    """Test l'addition."""
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5
    assert "2 + 3 = 5" in calc.get_history()

def test_division_par_zero():
    """Test la division par zéro."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Division par zéro"):
        calc.divide(1, 0)

def test_validation_types():
    """Test la validation des types."""
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("not a number", 5)
```

#### README.md

```markdown
# Calculatrice Python

Une calculatrice simple avec historique des opérations.

## Installation

```bash
pip install calculatrice
```

## Usage

### En tant que bibliothèque

```python
from calculatrice import Calculator

calc = Calculator()

# Opérations de base
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(3, 7)   # 21
result = calc.divide(15, 3)    # 5.0

# Historique
print(calc.get_history())
```

### En ligne de commande

```bash
calculatrice-cli
```

## Développement

```bash
# Cloner le projet
git clone https://github.com/username/calculatrice
cd calculatrice

# Installer en mode développement
pip install -e .[dev]

# Lancer les tests
pytest

# Formater le code
black src/
```

## Licence

MIT License
```

## Déploiement web avec Flask

### Application Flask simple

```python
# app.py
from flask import Flask, render_template, request, jsonify
from calculatrice import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def index():
    """Page d'accueil."""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API pour les calculs."""
    try:
        data = request.get_json()
        operation = data['operation']
        a = float(data['a'])
        b = float(data['b'])

        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        else:
            return jsonify({'error': 'Opération inconnue'}), 400

        return jsonify({
            'result': result,
            'history': calc.get_history()[-10:]  # Dernières 10 opérations
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/history')
def history():
    """API pour l'historique."""
    return jsonify({'history': calc.get_history()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Configuration pour production

**config.py**
```python
import os

class Config:
    """Configuration de base."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

class DevelopmentConfig(Config):
    """Configuration de développement."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration de production."""
    DEBUG = False

    # Sécurité renforcée en production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY must be set in production")

class TestingConfig(Config):
    """Configuration de test."""
    TESTING = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
```

**app.py modifié**
```python
from flask import Flask
from config import config
import os

def create_app(config_name=None):
    """Factory pour créer l'application."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Enregistrer les routes
    from routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

## Containerisation avec Docker

### Dockerfile

```dockerfile
# Dockerfile
# Utiliser une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY src/ ./src/
COPY app.py .
COPY config.py .

# Créer un utilisateur non-root pour la sécurité
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Exposer le port
EXPOSE 5000

# Variables d'environnement
ENV FLASK_ENV=production
ENV PYTHONPATH=/app/src

# Commande par défaut
CMD ["python", "app.py"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-secret-key-here
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web
    restart: unless-stopped

volumes:
  logs:
```

### Configuration Nginx

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream app {
        server web:5000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

### Commandes Docker

```bash
# Construire et lancer
docker-compose up --build

# Lancer en arrière-plan
docker-compose up -d

# Voir les logs
docker-compose logs -f web

# Arrêter
docker-compose down

# Construire seulement
docker build -t mon-app .

# Lancer un container
docker run -p 5000:5000 -e SECRET_KEY=mysecret mon-app
```

## Déploiement sur différentes plateformes

### Heroku

#### Fichiers nécessaires

**Procfile**
```
web: python app.py
```

**runtime.txt**
```
python-3.11.0
```

#### Commandes de déploiement

```bash
# 1. Installer Heroku CLI
# 2. Connecter à Heroku
heroku login

# 3. Créer l'application
heroku create mon-app-calculatrice

# 4. Configurer les variables d'environnement
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production

# 5. Déployer
git push heroku main

# 6. Ouvrir l'application
heroku open
```

### DigitalOcean App Platform

**app.yaml**
```yaml
name: calculatrice-app
services:
- name: web
  source_dir: /
  github:
    repo: username/calculatrice-app
    branch: main
  run_command: python app.py
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  env:
  - key: SECRET_KEY
    value: your-secret-key
    type: SECRET
  - key: FLASK_ENV
    value: production
  http_port: 5000
```

### VPS traditionnel

#### Script de déploiement

```bash
#!/bin/bash
# deploy-vps.sh

# Configuration
SERVER_USER="ubuntu"
SERVER_HOST="your-server.com"
APP_DIR="/var/www/calculatrice"

echo "🚀 Déploiement sur VPS..."

# 1. Transférer les fichiers
echo "📦 Transfert des fichiers..."
rsync -avz --exclude='.git' --exclude='__pycache__' \
    ./ $SERVER_USER@$SERVER_HOST:$APP_DIR/

# 2. Installer les dépendances sur le serveur
echo "📚 Installation des dépendances..."
ssh $SERVER_USER@$SERVER_HOST << EOF
    cd $APP_DIR
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
EOF

# 3. Redémarrer le service
echo "🔄 Redémarrage du service..."
ssh $SERVER_USER@$SERVER_HOST "sudo systemctl restart calculatrice"

echo "✅ Déploiement terminé!"
```

#### Service systemd

```ini
# /etc/systemd/system/calculatrice.service
[Unit]
Description=Calculatrice Flask App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/var/www/calculatrice
Environment=PATH=/var/www/calculatrice/venv/bin
Environment=FLASK_ENV=production
Environment=SECRET_KEY=your-secret-key
ExecStart=/var/www/calculatrice/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Activer et démarrer le service
sudo systemctl enable calculatrice
sudo systemctl start calculatrice
sudo systemctl status calculatrice
```

## Monitoring et maintenance

### Logging en production

```python
# logging_config.py
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    """Configure le logging pour la production."""

    if not app.debug:
        # Créer le dossier logs s'il n'existe pas
        if not os.path.exists('logs'):
            os.mkdir('logs')

        # Handler pour fichier avec rotation
        file_handler = RotatingFileHandler(
            'logs/calculatrice.log',
            maxBytes=10240000,  # 10MB
            backupCount=10
        )

        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Calculatrice startup')

# Dans app.py
from logging_config import setup_logging

app = create_app()
setup_logging(app)
```

### Health check

```python
# Dans app.py
@app.route('/health')
def health_check():
    """Endpoint de vérification de santé."""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': time.time()
    })

@app.route('/metrics')
def metrics():
    """Métriques basiques."""
    import psutil

    return jsonify({
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'calculations_count': len(calc.get_history())
    })
```

### Script de monitoring

```bash
#!/bin/bash
# monitor.sh - Script de monitoring simple

URL="http://localhost:5000/health"
EMAIL="admin@example.com"

# Vérifier que l'application répond
if ! curl -f -s $URL > /dev/null; then
    echo "❌ Application down!" | mail -s "App Down Alert" $EMAIL

    # Essayer de redémarrer
    sudo systemctl restart calculatrice

    # Vérifier à nouveau
    sleep 10
    if curl -f -s $URL > /dev/null; then
        echo "✅ Application restarted successfully" | mail -s "App Restored" $EMAIL
    fi
fi
```

## Sauvegarde et récupération

### Script de sauvegarde

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/var/backups/calculatrice"
DATE=$(date +%Y%m%d_%H%M%S)
APP_DIR="/var/www/calculatrice"

# Créer le dossier de sauvegarde
mkdir -p $BACKUP_DIR

# Sauvegarder le code
tar -czf $BACKUP_DIR/app_$DATE.tar.gz -C $APP_DIR .

# Sauvegarder les logs
cp -r $APP_DIR/logs $BACKUP_DIR/logs_$DATE

# Nettoyer les anciennes sauvegardes (garder 7 jours)
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
find $BACKUP_DIR -name "logs_*" -mtime +7 -exec rm -rf {} \;

echo "✅ Sauvegarde terminée: $BACKUP_DIR/app_$DATE.tar.gz"

# Optionnel: Envoyer vers le cloud
# aws s3 cp $BACKUP_DIR/app_$DATE.tar.gz s3://mon-bucket/backups/
```

### Script de récupération

```bash
#!/bin/bash
# restore.sh

BACKUP_DIR="/var/backups/calculatrice"
APP_DIR="/var/www/calculatrice"

# Lister les sauvegardes disponibles
echo "📋 Sauvegardes disponibles:"
ls -lt $BACKUP_DIR/*.tar.gz | head -10

# Demander quelle sauvegarde restaurer
read -p "Nom du fichier de sauvegarde (sans .tar.gz): " BACKUP_NAME

BACKUP_FILE="$BACKUP_DIR/$BACKUP_NAME.tar.gz"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Fichier de sauvegarde introuvable: $BACKUP_FILE"
    exit 1
fi

# Arrêter l'application
echo "🛑 Arrêt de l'application..."
sudo systemctl stop calculatrice

# Sauvegarder la version actuelle avant restauration
echo "💾 Sauvegarde de sécurité de la version actuelle..."
tar -czf $BACKUP_DIR/before_restore_$(date +%Y%m%d_%H%M%S).tar.gz -C $APP_DIR .

# Restaurer la sauvegarde
echo "🔄 Restauration en cours..."
cd $APP_DIR
tar -xzf $BACKUP_FILE

# Redémarrer l'application
echo "🚀 Redémarrage de l'application..."
sudo systemctl start calculatrice

# Vérifier que tout fonctionne
sleep 5
if curl -f -s http://localhost:5000/health > /dev/null; then
    echo "✅ Restauration réussie!"
else
    echo "❌ Problème détecté après restauration"
    echo "🔧 Vérifiez les logs: sudo systemctl status calculatrice"
fi
```

### Automatisation avec cron

```bash
# Éditer la crontab
crontab -e

# Ajouter une sauvegarde quotidienne à 2h du matin
0 2 * * * /var/www/calculatrice/scripts/backup.sh >> /var/log/backup.log 2>&1

# Sauvegarde hebdomadaire complète le dimanche à 1h
0 1 * * 0 /var/www/calculatrice/scripts/full_backup.sh >> /var/log/backup.log 2>&1
```

## Sécurité en production

### Configuration sécurisée

```python
# security_config.py
import os
from werkzeug.middleware.proxy_fix import ProxyFix

def configure_security(app):
    """Configure la sécurité de l'application."""

    # Headers de sécurité
    @app.after_request
    def security_headers(response):
        # Empêcher l'intégration dans des iframes
        response.headers['X-Frame-Options'] = 'DENY'

        # Empêcher la détection du type MIME
        response.headers['X-Content-Type-Options'] = 'nosniff'

        # Protection XSS
        response.headers['X-XSS-Protection'] = '1; mode=block'

        # HTTPS uniquement (si en production)
        if not app.debug:
            response.headers['Strict-Transport-Security'] = 'max-age=31536000'

        return response

    # Configuration pour les proxies (nginx, etc.)
    if not app.debug:
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    # Limitation du taux de requêtes
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["1000 per hour", "100 per minute"]
    )

    # Limitation spécifique pour l'API
    @app.route('/api/calculate', methods=['POST'])
    @limiter.limit("10 per minute")
    def calculate_limited():
        return calculate()

# Dans app.py
from security_config import configure_security

app = create_app()
configure_security(app)
```

### Variables d'environnement sécurisées

```bash
# /etc/environment (sur le serveur)
SECRET_KEY="votre-clé-très-secrète-et-longue"
DATABASE_URL="postgresql://user:password@localhost/calculatrice"
REDIS_URL="redis://localhost:6379/0"
```

```python
# secure_config.py
import os
import secrets

class SecureConfig:
    """Configuration sécurisée pour la production."""

    def __init__(self):
        # Générer une clé secrète si elle n'existe pas
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            if os.environ.get('FLASK_ENV') == 'production':
                raise ValueError("SECRET_KEY doit être définie en production!")
            else:
                self.SECRET_KEY = secrets.token_hex(32)
                print("⚠️  Clé secrète générée automatiquement (dev seulement)")

    @property
    def database_url(self):
        """URL de base de données avec validation."""
        url = os.environ.get('DATABASE_URL')
        if not url:
            return 'sqlite:///app.db'  # Valeur par défaut

        # Valider l'URL
        if url.startswith('postgres://'):
            # Heroku utilise postgres:// mais SQLAlchemy veut postgresql://
            url = url.replace('postgres://', 'postgresql://', 1)

        return url
```

### Firewall et accès

```bash
# Configuration UFW (Ubuntu)
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Autoriser SSH (adaptez le port si nécessaire)
sudo ufw allow 22/tcp

# Autoriser HTTP et HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Activer le firewall
sudo ufw enable

# Vérifier le statut
sudo ufw status verbose
```

## Tests en production

### Tests de fumée (smoke tests)

```python
# smoke_tests.py
import requests
import sys
import time

def test_application_health(base_url):
    """Tests basiques pour vérifier que l'app fonctionne."""

    tests_passed = 0
    tests_total = 0

    def run_test(name, test_func):
        nonlocal tests_passed, tests_total
        tests_total += 1

        try:
            test_func()
            print(f"✅ {name}")
            tests_passed += 1
        except Exception as e:
            print(f"❌ {name}: {e}")

    # Test 1: Health check
    def test_health():
        response = requests.get(f"{base_url}/health", timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'healthy'

    run_test("Health check", test_health)

    # Test 2: Page d'accueil
    def test_homepage():
        response = requests.get(base_url, timeout=10)
        assert response.status_code == 200

    run_test("Page d'accueil", test_homepage)

    # Test 3: API de calcul
    def test_calculation_api():
        response = requests.post(
            f"{base_url}/api/calculate",
            json={'operation': 'add', 'a': 2, 'b': 3},
            timeout=10
        )
        assert response.status_code == 200
        data = response.json()
        assert data['result'] == 5

    run_test("API de calcul", test_calculation_api)

    # Test 4: Gestion d'erreur
    def test_error_handling():
        response = requests.post(
            f"{base_url}/api/calculate",
            json={'operation': 'divide', 'a': 1, 'b': 0},
            timeout=10
        )
        assert response.status_code == 400
        data = response.json()
        assert 'error' in data

    run_test("Gestion d'erreur", test_error_handling)

    # Résultats
    print(f"\n📊 Résultats: {tests_passed}/{tests_total} tests réussis")

    if tests_passed == tests_total:
        print("🎉 Tous les tests sont passés!")
        return True
    else:
        print("😞 Certains tests ont échoué")
        return False

if __name__ == "__main__":
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5000"

    print(f"🧪 Tests de fumée sur {base_url}")
    success = test_application_health(base_url)

    sys.exit(0 if success else 1)
```

### Intégration dans le déploiement

```bash
#!/bin/bash
# deploy_with_tests.sh

set -e  # Arrêter en cas d'erreur

APP_URL="https://mon-app.com"

echo "🚀 Déploiement avec tests automatisés"

# Étape 1: Déploiement
echo "📦 Déploiement de l'application..."
./deploy.sh

# Étape 2: Attendre que l'app soit prête
echo "⏳ Attente du démarrage de l'application..."
sleep 30

# Étape 3: Tests de fumée
echo "🧪 Exécution des tests de fumée..."
python smoke_tests.py $APP_URL

if [ $? -eq 0 ]; then
    echo "✅ Déploiement réussi!"
else
    echo "❌ Tests échoués, rollback nécessaire"
    ./rollback.sh
    exit 1
fi
```

## Performance et optimisation en production

### Cache avec Redis

```python
# cache_config.py
import redis
import json
import os
from functools import wraps

# Configuration Redis
redis_client = redis.from_url(
    os.environ.get('REDIS_URL', 'redis://localhost:6379/0'),
    decode_responses=True
)

def cache_result(expiration=300):  # 5 minutes par défaut
    """Décorateur pour mettre en cache les résultats."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Créer une clé de cache unique
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"

            # Essayer de récupérer depuis le cache
            try:
                cached_result = redis_client.get(cache_key)
                if cached_result:
                    return json.loads(cached_result)
            except:
                pass  # En cas d'erreur Redis, continuer sans cache

            # Calculer le résultat
            result = func(*args, **kwargs)

            # Mettre en cache
            try:
                redis_client.setex(
                    cache_key,
                    expiration,
                    json.dumps(result)
                )
            except:
                pass  # En cas d'erreur Redis, continuer sans cache

            return result

        return wrapper
    return decorator

# Utilisation dans l'application
@app.route('/api/complex-calculation', methods=['POST'])
@cache_result(expiration=600)  # Cache 10 minutes
def complex_calculation():
    """Calcul complexe avec cache."""
    data = request.get_json()

    # Simulation d'un calcul coûteux
    import time
    time.sleep(2)

    result = sum(range(data.get('n', 1000)))
    return jsonify({'result': result})
```

### Monitoring des performances

```python
# performance_monitor.py
import time
import psutil
from flask import g, request
from functools import wraps

class PerformanceMonitor:
    """Moniteur de performance pour Flask."""

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Initialise le monitoring sur l'application."""
        app.before_request(self.before_request)
        app.after_request(self.after_request)

    def before_request(self):
        """Enregistre le début de la requête."""
        g.start_time = time.time()
        g.start_cpu = psutil.cpu_percent()
        g.start_memory = psutil.virtual_memory().percent

    def after_request(self, response):
        """Enregistre la fin de la requête et les métriques."""
        if hasattr(g, 'start_time'):
            duration = time.time() - g.start_time
            cpu_usage = psutil.cpu_percent() - g.start_cpu
            memory_usage = psutil.virtual_memory().percent - g.start_memory

            # Log des requêtes lentes
            if duration > 1.0:  # Plus d'1 seconde
                self.app.logger.warning(
                    f"Requête lente: {request.method} {request.path} "
                    f"({duration:.2f}s, CPU: {cpu_usage:.1f}%, "
                    f"Mémoire: {memory_usage:.1f}%)"
                )

            # Ajouter les métriques aux headers (dev seulement)
            if self.app.debug:
                response.headers['X-Response-Time'] = f"{duration:.3f}s"
                response.headers['X-CPU-Usage'] = f"{cpu_usage:.1f}%"

        return response

# Dans app.py
monitor = PerformanceMonitor(app)
```

### Load balancing avec nginx

```nginx
# /etc/nginx/sites-available/calculatrice
upstream app_servers {
    server 127.0.0.1:5000 weight=1 max_fails=3 fail_timeout=30s;
    server 127.0.0.1:5001 weight=1 max_fails=3 fail_timeout=30s;
    server 127.0.0.1:5002 weight=1 max_fails=3 fail_timeout=30s;
}

server {
    listen 80;
    server_name calculatrice.example.com;

    # Redirection HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name calculatrice.example.com;

    # Configuration SSL
    ssl_certificate /etc/letsencrypt/live/calculatrice.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/calculatrice.example.com/privkey.pem;

    # Sécurité SSL
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;

    # Headers de sécurité
    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    # Gestion des fichiers statiques
    location /static {
        alias /var/www/calculatrice/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Proxy vers l'application
    location / {
        proxy_pass http://app_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Timeouts
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;

        # Health check
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    }

    # Health check endpoint
    location /health {
        access_log off;
        proxy_pass http://app_servers;
    }
}
```

## Monitoring et alertes avancés

### Intégration avec des services de monitoring

```python
# monitoring_integrations.py
import os
import requests
import logging

class SlackNotifier:
    """Notificateur Slack pour les alertes."""

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_alert(self, message, level="warning"):
        """Envoie une alerte sur Slack."""

        colors = {
            "info": "#36a64f",      # Vert
            "warning": "#ff9900",   # Orange
            "error": "#ff0000"      # Rouge
        }

        payload = {
            "attachments": [{
                "color": colors.get(level, "#ff9900"),
                "title": f"🚨 Alerte Calculatrice ({level.upper()})",
                "text": message,
                "footer": "Système de monitoring",
                "ts": int(time.time())
            }]
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            response.raise_for_status()
        except Exception as e:
            logging.error(f"Erreur envoi Slack: {e}")

class HealthChecker:
    """Vérificateur de santé de l'application."""

    def __init__(self, app_url, slack_notifier=None):
        self.app_url = app_url
        self.slack_notifier = slack_notifier
        self.last_status = None

    def check_health(self):
        """Vérifie la santé de l'application."""

        try:
            response = requests.get(
                f"{self.app_url}/health",
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()

                # Vérifier les métriques
                metrics = requests.get(f"{self.app_url}/metrics", timeout=10).json()

                alerts = []

                # CPU élevé
                if metrics.get('cpu_percent', 0) > 80:
                    alerts.append(f"CPU élevé: {metrics['cpu_percent']:.1f}%")

                # Mémoire élevée
                if metrics.get('memory_percent', 0) > 85:
                    alerts.append(f"Mémoire élevée: {metrics['memory_percent']:.1f}%")

                # Disque plein
                if metrics.get('disk_percent', 0) > 90:
                    alerts.append(f"Disque plein: {metrics['disk_percent']:.1f}%")

                if alerts and self.slack_notifier:
                    message = "Problèmes détectés:\n" + "\n".join(f"• {alert}" for alert in alerts)
                    self.slack_notifier.send_alert(message, "warning")

                # Application en vie
                if self.last_status != "healthy":
                    if self.slack_notifier and self.last_status is not None:
                        self.slack_notifier.send_alert("✅ Application rétablie", "info")

                self.last_status = "healthy"
                return True

            else:
                raise Exception(f"Status code: {response.status_code}")

        except Exception as e:
            if self.last_status != "unhealthy":
                if self.slack_notifier:
                    self.slack_notifier.send_alert(f"❌ Application inaccessible: {e}", "error")

            self.last_status = "unhealthy"
            return False

# Script de monitoring
def main():
    """Script principal de monitoring."""

    app_url = os.environ.get('APP_URL', 'http://localhost:5000')
    slack_webhook = os.environ.get('SLACK_WEBHOOK_URL')

    slack_notifier = SlackNotifier(slack_webhook) if slack_webhook else None
    health_checker = HealthChecker(app_url, slack_notifier)

    print(f"🔍 Monitoring de {app_url}")

    while True:
        is_healthy = health_checker.check_health()
        status = "✅ Healthy" if is_healthy else "❌ Unhealthy"
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {status}")

        time.sleep(60)  # Vérifier chaque minute

if __name__ == "__main__":
    main()
```

## Documentation pour les utilisateurs

### README.md complet

```markdown
# Calculatrice API

Une API REST simple pour effectuer des calculs mathématiques avec historique.

## 🚀 Démarrage rapide

### Installation locale

```bash
# Cloner le projet
git clone https://github.com/username/calculatrice-api.git
cd calculatrice-api

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditez .env avec vos valeurs

# Démarrer l'application
python app.py
```

L'application sera disponible sur http://localhost:5000

### Avec Docker

```bash
# Construction et lancement
docker-compose up --build

# Ou avec Docker seulement
docker build -t calculatrice .
docker run -p 5000:5000 -e SECRET_KEY=mysecret calculatrice
```

## 📡 API Reference

### Endpoints

#### GET /health
Vérification de santé de l'application.

**Réponse:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": 1234567890
}
```

#### POST /api/calculate
Effectue un calcul mathématique.

**Corps de la requête:**
```json
{
  "operation": "add|subtract|multiply|divide",
  "a": 5,
  "b": 3
}
```

**Réponse:**
```json
{
  "result": 8,
  "history": ["5 + 3 = 8"]
}
```

**Codes d'erreur:**
- `400` - Paramètres invalides
- `500` - Erreur serveur

#### GET /api/history
Récupère l'historique des calculs.

**Réponse:**
```json
{
  "history": [
    "5 + 3 = 8",
    "10 - 4 = 6",
    "7 * 2 = 14"
  ]
}
```

### Exemples d'utilisation

#### curl
```bash
# Addition
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 5, "b": 3}'

# Historique
curl http://localhost:5000/api/history
```

#### Python
```python
import requests

# Calcul
response = requests.post('http://localhost:5000/api/calculate', json={
    'operation': 'multiply',
    'a': 7,
    'b': 6
})
print(response.json())  # {'result': 42, 'history': [...]}

# Historique
response = requests.get('http://localhost:5000/api/history')
print(response.json())
```

#### JavaScript
```javascript
// Calcul
fetch('/api/calculate', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    operation: 'divide',
    a: 15,
    b: 3
  })
})
.then(response => response.json())
.then(data => console.log(data.result)); // 5
```

## 🔧 Configuration

### Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|---------|
| `SECRET_KEY` | Clé secrète pour Flask | `dev-secret-key` |
| `FLASK_ENV` | Environnement (`development`/`production`) | `development` |
| `PORT` | Port d'écoute | `5000` |
| `REDIS_URL` | URL Redis pour le cache | `redis://localhost:6379/0` |

### Configuration de production

Pour déployer en production:

1. Définissez `FLASK_ENV=production`
2. Utilisez une `SECRET_KEY` forte et unique
3. Configurez un serveur web (nginx) en proxy
4. Utilisez un gestionnaire de processus (systemd, supervisord)
5. Configurez le monitoring et les sauvegardes

## 🔒 Sécurité

- Limitation du taux de requêtes (10/minute par IP)
- Headers de sécurité HTTPS
- Validation des entrées utilisateur
- Pas de données sensibles dans les logs

## 📊 Monitoring

### Métriques disponibles

GET `/metrics` retourne:
```json
{
  "cpu_percent": 25.5,
  "memory_percent": 45.2,
  "disk_percent": 60.1,
  "calculations_count": 1520
}
```

### Logs

Les logs sont stockés dans `logs/calculatrice.log` avec rotation automatique.

Niveaux:
- `INFO`: Démarrage, arrêt normal
- `WARNING`: Requêtes lentes, ressources élevées
- `ERROR`: Erreurs d'application

## 🚀 Déploiement

### Heroku

1. Créer l'application: `heroku create mon-app`
2. Configurer les variables: `heroku config:set SECRET_KEY=...`
3. Déployer: `git push heroku main`

### VPS

Voir le fichier `docs/deployment.md` pour les instructions détaillées.

## 🧪 Tests

```bash
# Tests unitaires
pytest

# Tests d'intégration
pytest tests/integration/

# Coverage
pytest --cov=src/

# Tests de fumée en production
python smoke_tests.py https://mon-app.herokuapp.com
```

## 🤝 Contributing

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit les changements (`git commit -am 'Ajout nouvelle fonctionnalite'`)
4. Push la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

## 📝 Licence

MIT License - voir le fichier `LICENSE` pour les détails.

## 📞 Support

- 🐛 Issues: https://github.com/username/calculatrice-api/issues
- 📧 Email: support@example.com
- 💬 Slack: #calculatrice-support
```

## Checklist de déploiement

### Avant le déploiement

```markdown
## 📋 Checklist de déploiement

### ✅ Code et tests
- [ ] Tous les tests passent
- [ ] Code review terminée
- [ ] Documentation à jour
- [ ] Variables d'environnement configurées
- [ ] Secrets et clés API sécurisés

### ✅ Infrastructure
- [ ] Serveur configuré et accessible
- [ ] Base de données configurée
- [ ] Redis/Cache configuré (si applicable)
- [ ] SSL/TLS configuré
- [ ] Firewall configuré

### ✅ Monitoring
- [ ] Logs configurés
- [ ] Health checks en place
- [ ] Alertes configurées
- [ ] Métriques disponibles
- [ ] Monitoring external en place

### ✅ Sauvegarde
- [ ] Stratégie de sauvegarde définie
- [ ] Script de restauration testé
- [ ] Sauvegarde des données existantes
- [ ] Plan de rollback prêt

### ✅ Sécurité
- [ ] Headers de sécurité configurés
- [ ] Rate limiting en place
- [ ] Validation des entrées
- [ ] Accès restreints configurés
- [ ] Scan de sécurité effectué

### ✅ Performance
- [ ] Tests de charge effectués
- [ ] Cache configuré
- [ ] CDN configuré (si applicable)
- [ ] Compression activée
- [ ] Base de données optimisée

### ✅ Post-déploiement
- [ ] Tests de fumée réussis
- [ ] Monitoring fonctionnel
- [ ] Performance acceptable
- [ ] Équipe informée
- [ ] Documentation utilisateur mise à jour
```

# 12.5 : Déploiement et distribution

## Conclusion

Le déploiement et la distribution d'applications Python nécessitent de maîtriser plusieurs aspects :

### 🎯 Points clés à retenir

1. **Préparation** : Structure propre, dépendances gérées, configuration externalisée
2. **Sécurité** : Variables d'environnement, HTTPS, validation des entrées
3. **Monitoring** : Logs, métriques, alertes, health checks
4. **Sauvegarde** : Stratégie claire, tests de restauration, rollback possible
5. **Performance** : Cache, load balancing, optimisation des ressources
6. **Documentation** : Instructions claires pour l'installation et l'utilisation

### 🛣️ Étapes recommandées pour débuter

1. **Commencez simple** : Déployez d'abord sur une plateforme comme Heroku
2. **Automatisez progressivement** : Scripts de déploiement, tests automatiques
3. **Ajoutez le monitoring** : Logs, métriques, alertes essentielles
4. **Renforcez la sécurité** : HTTPS, variables d'environnement, rate limiting
5. **Optimisez selon les besoins** : Cache, load balancing, CDN

### 🚨 Erreurs courantes à éviter

❌ **Ne jamais faire :**
- Déployer sans tests
- Mettre des secrets dans le code
- Ignorer les logs d'erreur
- Négliger les sauvegardes
- Déployer directement en production

✅ **Toujours faire :**
- Tester sur un environnement similaire à la production
- Utiliser des variables d'environnement pour la configuration
- Monitorer les performances et erreurs
- Avoir un plan de rollback
- Documenter le processus de déploiement

### 🎓 Pour aller plus loin

Une fois que vous maîtrisez les bases, vous pouvez explorer :

- **Orchestration** : Kubernetes, Docker Swarm
- **CI/CD avancée** : GitHub Actions, GitLab CI, Jenkins
- **Infrastructure as Code** : Terraform, Ansible
- **Monitoring avancé** : Prometheus, Grafana, ELK Stack
- **Sécurité renforcée** : Vault, audit de sécurité automatisé

### 🏆 Objectif final

L'objectif n'est pas d'avoir le déploiement le plus complexe, mais le plus **fiable** et **adapté à vos besoins**. Une application simple qui fonctionne parfaitement vaut mieux qu'une architecture complexe qui tombe en panne.

Commencez petit, apprenez de vos erreurs, et évoluez progressivement vers plus de sophistication selon vos besoins réels.

## Exercices pratiques

### Exercice 1 : Première application en production
1. Créez une API Flask simple (calculatrice ou to-do list)
2. Déployez-la sur Heroku
3. Configurez le monitoring de base
4. Testez le processus de rollback

### Exercice 2 : Package Python
1. Créez un package Python utilitaire
2. Configurez setup.py correctement
3. Publiez sur TestPyPI
4. Installez et testez votre package

### Exercice 3 : Déploiement avec Docker
1. Containerisez votre application
2. Utilisez docker-compose pour l'orchestration
3. Configurez un reverse proxy nginx
4. Ajoutez SSL avec Let's Encrypt

### Exercice 4 : Monitoring complet
1. Intégrez des métriques custom
2. Configurez des alertes Slack
3. Créez un dashboard de monitoring
4. Testez la détection d'incidents

## Ressources complémentaires

### 📚 Documentation officielle
- [Flask Deployment Options](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Docker Best Practices](https://docs.docker.com/develop/best-practices/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)

### 🛠️ Outils recommandés

#### Déploiement
- **Heroku** : Déploiement simple pour débuter
- **DigitalOcean App Platform** : Alternative moderne à Heroku
- **AWS Elastic Beanstalk** : AWS géré facilement
- **Google Cloud Run** : Serverless containers

#### Monitoring
- **Sentry** : Tracking d'erreurs
- **New Relic** : Monitoring d'application
- **DataDog** : Monitoring complet
- **Uptime Robot** : Monitoring de disponibilité

#### CI/CD
- **GitHub Actions** : Intégré à GitHub
- **GitLab CI** : Intégré à GitLab
- **Travis CI** : Service cloud simple
- **CircleCI** : Puissant et flexible

### 📖 Lectures recommandées

```python
# Livres essentiels pour le déploiement Python
livres_recommandes = [
    {
        "titre": "Flask Web Development",
        "auteur": "Miguel Grinberg",
        "focus": "Développement et déploiement Flask"
    },
    {
        "titre": "Python Tricks",
        "auteur": "Dan Bader",
        "focus": "Bonnes pratiques Python"
    },
    {
        "titre": "Effective Python",
        "auteur": "Brett Slatkin",
        "focus": "Code Python professionnel"
    },
    {
        "titre": "Docker Deep Dive",
        "auteur": "Nigel Poulton",
        "focus": "Containerisation avancée"
    }
]

for livre in livres_recommandes:
    print(f"📖 {livre['titre']} - {livre['auteur']}")
    print(f"   Focus: {livre['focus']}")
```

## Templates et starters

### Starter Flask API

```python
# Structure recommandée pour une API Flask
"""
flask-api-starter/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── tests/
├── migrations/
├── scripts/
│   ├── deploy.sh
│   └── backup.sh
├── requirements.txt
├── config.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
"""

# Template de configuration
class Config:
    """Configuration de base."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Rate limiting
    RATELIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or 'memory://'

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

class ProductionConfig(Config):
    """Configuration production."""

    def __init__(self):
        super().__init__()

        # Validation des variables critiques
        required_vars = ['SECRET_KEY', 'DATABASE_URL']
        missing_vars = [var for var in required_vars if not os.environ.get(var)]

        if missing_vars:
            raise ValueError(f"Variables manquantes: {missing_vars}")

# Factory pattern pour l'application
def create_app(config_name='default'):
    """Crée l'application Flask."""
    app = Flask(__name__)

    # Configuration
    config_mapping = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
        'default': DevelopmentConfig
    }

    app.config.from_object(config_mapping[config_name])

    # Extensions
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    limiter = Limiter(app, key_func=get_remote_address)

    # Blueprints
    from app.routes.api import api_bp
    from app.routes.health import health_bp

    app.register_blueprint(api_bp, url_prefix='/api/v1')
    app.register_blueprint(health_bp)

    return app
```

### Template Dockerfile production-ready

```dockerfile
# Dockerfile multi-stage pour optimiser la taille
FROM python:3.11-slim as builder

# Variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Installer les dépendances système pour la compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Créer l'environnement virtuel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage final - image de production
FROM python:3.11-slim

# Copier l'environnement virtuel du stage builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Installer seulement les dépendances runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Créer un utilisateur non-root
RUN useradd --create-home --shell /bin/bash --uid 1000 appuser

# Créer les dossiers nécessaires
WORKDIR /app
RUN mkdir -p /app/logs && chown -R appuser:appuser /app

# Copier le code
COPY --chown=appuser:appuser . .

# Changer vers l'utilisateur non-root
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Exposer le port
EXPOSE 5000

# Point d'entrée avec script de démarrage
COPY --chown=appuser:appuser scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
```

### Script d'entrypoint production

```bash
#!/bin/bash
# entrypoint.sh

set -e

echo "🚀 Démarrage de l'application..."

# Attendre que la base de données soit prête
if [ "$DATABASE_URL" ]; then
    echo "⏳ Attente de la base de données..."

    # Extraire l'host et le port de l'URL
    DB_HOST=$(echo $DATABASE_URL | sed -E 's/.*@([^:]+).*/\1/')
    DB_PORT=$(echo $DATABASE_URL | sed -E 's/.*:([0-9]+)\/.*/\1/')

    # Attendre que la DB soit accessible
    timeout 30 bash -c "until nc -z $DB_HOST $DB_PORT; do sleep 1; done"
    echo "✅ Base de données accessible"
fi

# Migrations de base de données
if [ "$FLASK_ENV" = "production" ] && [ "$RUN_MIGRATIONS" = "true" ]; then
    echo "🔄 Exécution des migrations..."
    flask db upgrade
fi

# Vérification de santé de l'application
echo "🏥 Vérification de la configuration..."
python -c "
from app import create_app
app = create_app()
with app.app_context():
    print('✅ Configuration validée')
"

echo "✅ Démarrage terminé"

# Exécuter la commande passée en argument
exec "$@"
```

### CI/CD avec GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: '3.11'
  NODE_VERSION: '18'

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
          POSTGRES_USER: test
          POSTGRES_DB: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
        cache: 'pip'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Lint with flake8
      run: |
        flake8 app/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 app/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

    - name: Type checking with mypy
      run: mypy app/

    - name: Security check with bandit
      run: bandit -r app/

    - name: Test with pytest
      env:
        DATABASE_URL: postgresql://test:test@localhost:5432/test
        SECRET_KEY: test-secret-key
      run: |
        pytest tests/ -v --cov=app --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Login to DockerHub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: |
          myapp/calculatrice:latest
          myapp/calculatrice:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: [test, build]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
    - uses: actions/checkout@v4

    - name: Deploy to production
      run: |
        echo "🚀 Déploiement en production..."
        # Ici vous déployeriez réellement
        # Par exemple avec SSH, kubectl, etc.

    - name: Run smoke tests
      run: |
        python scripts/smoke_tests.py https://mon-app.com

    - name: Notify team
      if: always()
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#deployments'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## Métriques et KPIs de déploiement

### Dashboard de métriques

```python
# metrics_dashboard.py
from flask import Blueprint, render_template, jsonify
import psutil
import time
from datetime import datetime, timedelta

metrics_bp = Blueprint('metrics', __name__)

class MetricsCollector:
    """Collecteur de métriques pour le dashboard."""

    def __init__(self):
        self.start_time = time.time()
        self.request_count = 0
        self.error_count = 0
        self.response_times = []

    def record_request(self, response_time, is_error=False):
        """Enregistre une requête."""
        self.request_count += 1
        if is_error:
            self.error_count += 1
        self.response_times.append(response_time)

        # Garder seulement les 1000 dernières mesures
        if len(self.response_times) > 1000:
            self.response_times = self.response_times[-1000:]

    def get_metrics(self):
        """Retourne les métriques actuelles."""
        uptime = time.time() - self.start_time
        avg_response_time = (
            sum(self.response_times) / len(self.response_times)
            if self.response_times else 0
        )

        return {
            'uptime_seconds': uptime,
            'uptime_human': str(timedelta(seconds=int(uptime))),
            'total_requests': self.request_count,
            'error_count': self.error_count,
            'error_rate': (self.error_count / self.request_count * 100) if self.request_count > 0 else 0,
            'avg_response_time': avg_response_time,
            'system': {
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_percent': psutil.disk_usage('/').percent,
                'load_average': psutil.getloadavg()[0] if hasattr(psutil, 'getloadavg') else 0
            }
        }

# Instance globale du collecteur
metrics_collector = MetricsCollector()

@metrics_bp.route('/dashboard')
def dashboard():
    """Dashboard de métriques."""
    return render_template('metrics_dashboard.html')

@metrics_bp.route('/api/metrics')
def api_metrics():
    """API des métriques."""
    return jsonify(metrics_collector.get_metrics())

# Middleware pour enregistrer les métriques
def setup_metrics_middleware(app):
    """Configure le middleware de métriques."""

    @app.before_request
    def before_request():
        from flask import g
        g.start_time = time.time()

    @app.after_request
    def after_request(response):
        if hasattr(g, 'start_time'):
            response_time = time.time() - g.start_time
            is_error = response.status_code >= 400
            metrics_collector.record_request(response_time, is_error)

        return response
```

### Template de dashboard

```html
<!-- templates/metrics_dashboard.html -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Calculatrice API</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-value {
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }
        .metric-label {
            color: #666;
            margin-top: 5px;
        }
        .status-healthy { color: #28a745; }
        .status-warning { color: #ffc107; }
        .status-danger { color: #dc3545; }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard Calculatrice API</h1>
            <p>Monitoring en temps réel • Dernière mise à jour: <span id="last-update"></span></p>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value" id="uptime">-</div>
                <div class="metric-label">Uptime</div>
            </div>

            <div class="metric-card">
                <div class="metric-value" id="total-requests">-</div>
                <div class="metric-label">Total Requêtes</div>
            </div>

            <div class="metric-card">
                <div class="metric-value" id="error-rate">-</div>
                <div class="metric-label">Taux d'Erreur</div>
            </div>

            <div class="metric-card">
                <div class="metric-value" id="avg-response-time">-</div>
                <div class="metric-label">Temps de Réponse Moyen</div>
            </div>

            <div class="metric-card">
                <div class="metric-value" id="cpu-usage">-</div>
                <div class="metric-label">CPU</div>
            </div>

            <div class="metric-card">
                <div class="metric-value" id="memory-usage">-</div>
                <div class="metric-label">Mémoire</div>
            </div>
        </div>

        <div class="chart-container">
            <h3>Utilisation des Ressources</h3>
            <canvas id="resourceChart" width="400" height="200"></canvas>
        </div>
    </div>

    <script>
        // Configuration du graphique
        const ctx = document.getElementById('resourceChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'CPU %',
                    data: [],
                    borderColor: 'rgb(255, 99, 132)',
                    tension: 0.1
                }, {
                    label: 'Mémoire %',
                    data: [],
                    borderColor: 'rgb(54, 162, 235)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });

        // Fonction pour mettre à jour les métriques
        function updateMetrics() {
            fetch('/api/metrics')
                .then(response => response.json())
                .then(data => {
                    // Métriques générales
                    document.getElementById('uptime').textContent = data.uptime_human;
                    document.getElementById('total-requests').textContent = data.total_requests.toLocaleString();

                    // Taux d'erreur avec couleur
                    const errorRate = data.error_rate.toFixed(1) + '%';
                    const errorElement = document.getElementById('error-rate');
                    errorElement.textContent = errorRate;
                    errorElement.className = 'metric-value ' +
                        (data.error_rate > 5 ? 'status-danger' :
                         data.error_rate > 1 ? 'status-warning' : 'status-healthy');

                    // Temps de réponse
                    document.getElementById('avg-response-time').textContent =
                        (data.avg_response_time * 1000).toFixed(0) + 'ms';

                    // Ressources système
                    const cpuElement = document.getElementById('cpu-usage');
                    cpuElement.textContent = data.system.cpu_percent.toFixed(1) + '%';
                    cpuElement.className = 'metric-value ' +
                        (data.system.cpu_percent > 80 ? 'status-danger' :
                         data.system.cpu_percent > 60 ? 'status-warning' : 'status-healthy');

                    const memoryElement = document.getElementById('memory-usage');
                    memoryElement.textContent = data.system.memory_percent.toFixed(1) + '%';
                    memoryElement.className = 'metric-value ' +
                        (data.system.memory_percent > 85 ? 'status-danger' :
                         data.system.memory_percent > 70 ? 'status-warning' : 'status-healthy');

                    // Mettre à jour le graphique
                    const now = new Date().toLocaleTimeString();
                    chart.data.labels.push(now);
                    chart.data.datasets[0].data.push(data.system.cpu_percent);
                    chart.data.datasets[1].data.push(data.system.memory_percent);

                    // Garder seulement les 20 derniers points
                    if (chart.data.labels.length > 20) {
                        chart.data.labels.shift();
                        chart.data.datasets[0].data.shift();
                        chart.data.datasets[1].data.shift();
                    }

                    chart.update('none');

                    // Dernière mise à jour
                    document.getElementById('last-update').textContent =
                        new Date().toLocaleTimeString();
                })
                .catch(error => {
                    console.error('Erreur lors de la récupération des métriques:', error);
                });
        }

        // Mise à jour initiale et périodique
        updateMetrics();
        setInterval(updateMetrics, 5000); // Toutes les 5 secondes
    </script>
</body>
</html>
```

## Résumé final

Le déploiement et la distribution d'applications Python est un processus complexe mais gratifiant. En suivant les bonnes pratiques et en utilisant les outils appropriés, vous pouvez créer des applications robustes et fiables.

### 🎯 Votre parcours d'apprentissage

1. **Maîtrisez les bases** : Structure de projet, gestion des dépendances
2. **Apprenez Docker** : Containerisation et orchestration
3. **Automatisez** : CI/CD, tests automatiques, déploiements
4. **Monitorez** : Logs, métriques, alertes
5. **Sécurisez** : HTTPS, variables d'environnement, validation
6. **Optimisez** : Performance, scalabilité, coûts

### 🚀 Prochaines étapes

Maintenant que vous avez terminé ce module, vous êtes prêt à :
- Déployer vos premières applications en production
- Créer et distribuer vos propres packages Python
- Mettre en place des pipelines de déploiement automatisés
- Monitorer et maintenir vos applications

Le déploiement est un domaine en constante évolution. Continuez à apprendre, expérimenter et partager vos expériences avec la communauté !

**Félicitations** 🎉 pour avoir terminé ce module complet sur les bonnes pratiques et le déploiement Python. Vous avez maintenant toutes les clés pour devenir un développeur Python professionnel !

⏭️
