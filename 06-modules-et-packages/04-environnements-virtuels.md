🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.4 : Environnements virtuels

## Introduction

Un **environnement virtuel** est un espace isolé pour votre projet Python qui possède ses propres packages et versions. C'est l'une des bonnes pratiques les plus importantes en développement Python.

### Analogie simple
Imaginez vos projets Python comme des **appartements** :
- **Sans environnement virtuel** = tous vos projets partagent le même appartement (conflits possibles)
- **Avec environnement virtuel** = chaque projet a son propre appartement avec ses propres affaires

## Pourquoi utiliser des environnements virtuels ?

### Problème sans environnements virtuels

Imaginez cette situation :
- **Projet A** nécessite `Django 3.2`
- **Projet B** nécessite `Django 4.1`
- Vous ne pouvez installer qu'une seule version globalement !

```bash
# Sans environnement virtuel - PROBLÈME !
pip install django==3.2  # Pour le projet A
pip install django==4.1  # Écrase la version 3.2 !
# Le projet A ne fonctionne plus...
```

### Solution avec environnements virtuels

```bash
# Avec environnements virtuels - SOLUTION !
# Projet A
python -m venv projet_a_env
source projet_a_env/bin/activate
pip install django==3.2

# Projet B (dans un autre terminal)
python -m venv projet_b_env
source projet_b_env/bin/activate
pip install django==4.1

# Les deux projets coexistent sans problème !
```

## Création d'environnements virtuels

### Méthode 1 : venv (recommandée)

`venv` est inclus dans Python 3.3+ et est la méthode standard.

```bash
# Créer un environnement virtuel
python -m venv mon_env

# Sur certains systèmes Linux/Mac
python3 -m venv mon_env

# Créer avec un nom descriptif
python -m venv projet_ecommerce_env
```

### Structure créée

```
mon_env/
├── bin/           # Scripts d'activation (Linux/Mac)
│   ├── activate
│   ├── pip
│   └── python
├── Scripts/       # Scripts d'activation (Windows)
│   ├── activate.bat
│   ├── pip.exe
│   └── python.exe
├── lib/           # Packages installés
│   └── python3.x/
│       └── site-packages/
└── pyvenv.cfg     # Configuration
```

### Méthode 2 : virtualenv (alternative)

```bash
# Installer virtualenv si nécessaire
pip install virtualenv

# Créer un environnement
virtualenv mon_env

# Spécifier une version de Python
virtualenv -p python3.9 mon_env
```

## Activation et désactivation

### Sur Linux/Mac

```bash
# Activer l'environnement
source mon_env/bin/activate

# Votre prompt change pour indiquer l'environnement actif
(mon_env) user@computer:~/projet$

# Désactiver l'environnement
deactivate
```

### Sur Windows

```bash
# Activer l'environnement
mon_env\Scripts\activate

# Ou avec PowerShell
mon_env\Scripts\Activate.ps1

# Prompt modifié
(mon_env) C:\Users\User\projet>

# Désactiver
deactivate
```

### Vérifier l'activation

```bash
# Vérifier quel Python est utilisé
which python        # Linux/Mac
where python        # Windows

# Vérifier les packages installés
pip list

# Vérifier le chemin des packages
python -c "import sys; print(sys.path)"
```

## Workflow complet avec un projet

### Étape 1 : Créer le projet

```bash
# Créer le dossier du projet
mkdir mon_projet_web
cd mon_projet_web

# Créer l'environnement virtuel
python -m venv venv

# Structure initiale
mon_projet_web/
├── venv/          # Environnement virtuel
└── src/           # Code source (à créer)
```

### Étape 2 : Activer et installer les dépendances

```bash
# Activer l'environnement
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Mettre à jour pip
pip install --upgrade pip

# Installer les packages nécessaires
pip install flask requests beautifulsoup4

# Créer requirements.txt
pip freeze > requirements.txt
```

### Étape 3 : Développer le projet

```python
# src/app.py
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Analyseur de site web</h1>
    <form method="POST" action="/analyze">
        <input type="url" name="url" placeholder="URL du site" required>
        <button type="submit">Analyser</button>
    </form>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form['url']

    try:
        # Récupérer la page
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parser le HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraire des informations
        title = soup.find('title')
        title_text = title.text if title else "Titre non trouvé"

        links = soup.find_all('a', href=True)
        images = soup.find_all('img', src=True)

        # Statistiques
        stats = {
            'titre': title_text,
            'nb_liens': len(links),
            'nb_images': len(images),
            'taille_html': len(response.content),
            'status_code': response.status_code
        }

        return f'''
        <h2>Analyse de {url}</h2>
        <p><strong>Titre:</strong> {stats['titre']}</p>
        <p><strong>Nombre de liens:</strong> {stats['nb_liens']}</p>
        <p><strong>Nombre d'images:</strong> {stats['nb_images']}</p>
        <p><strong>Taille HTML:</strong> {stats['taille_html']} octets</p>
        <p><strong>Code de statut:</strong> {stats['status_code']}</p>
        <a href="/">Analyser un autre site</a>
        '''

    except Exception as e:
        return f'<h2>Erreur:</h2><p>{str(e)}</p><a href="/">Retour</a>'

if __name__ == '__main__':
    app.run(debug=True)
```

### Étape 4 : Tester le projet

```bash
# Toujours dans l'environnement activé
python src/app.py

# Ouvrir http://localhost:5000 dans le navigateur
```

### Étape 5 : Partager le projet

```bash
# Créer le fichier requirements.txt
pip freeze > requirements.txt

# Contenu généré
cat requirements.txt
```

**Résultat :**
```
beautifulsoup4==4.12.2
blinker==1.6.2
certifi==2023.7.22
charset-normalizer==3.2.0
click==8.1.7
Flask==2.3.3
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
requests==2.31.0
soupsieve==2.4.1
urllib3==2.0.4
Werkzeug==2.3.7
```

## Reproduction de l'environnement

### Sur une autre machine

```bash
# Cloner ou télécharger le projet
git clone https://github.com/user/mon_projet_web.git
cd mon_projet_web

# Créer un nouvel environnement virtuel
python -m venv venv

# Activer l'environnement
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer exactement les mêmes dépendances
pip install -r requirements.txt

# Lancer l'application
python src/app.py
```

## Bonnes pratiques

### 1. Nommage des environnements

```bash
# ✅ Bon : noms descriptifs
python -m venv blog_env
python -m venv ecommerce_env
python -m venv data_analysis_env

# ✅ Encore mieux : dans le dossier du projet
cd mon_projet
python -m venv venv  # Standard largement adopté
```

### 2. Fichier .gitignore

Toujours exclure l'environnement virtuel du contrôle de version :

```gitignore
# .gitignore
venv/
env/
.env
*.pyc
__pycache__/
.DS_Store
```

### 3. Script d'activation automatique

Créer un script pour simplifier l'activation :

```bash
# activate_project.sh (Linux/Mac)
#!/bin/bash
cd /chemin/vers/mon_projet
source venv/bin/activate
echo "Environnement activé pour mon_projet"
```

```batch
:: activate_project.bat (Windows)
@echo off
cd C:\chemin\vers\mon_projet
call venv\Scripts\activate.bat
echo Environnement active pour mon_projet
```

### 4. Vérification de l'environnement

```python
# check_env.py
import sys
import os

def check_virtual_env():
    """Vérifie si on est dans un environnement virtuel."""
    if hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    ):
        print("✅ Environnement virtuel activé")
        print(f"Python: {sys.executable}")
        print(f"Préfixe: {sys.prefix}")
    else:
        print("❌ Pas d'environnement virtuel")
        print("Activez votre environnement avec: source venv/bin/activate")

if __name__ == "__main__":
    check_virtual_env()
```

## Gestion de plusieurs projets

### Structure recommandée

```
~/Projets/
├── projet_blog/
│   ├── venv/
│   ├── src/
│   ├── requirements.txt
│   └── README.md
├── projet_api/
│   ├── venv/
│   ├── app/
│   ├── requirements.txt
│   └── README.md
└── projet_data/
    ├── venv/
    ├── notebooks/
    ├── requirements.txt
    └── README.md
```

### Script de gestion de projets

```python
# project_manager.py
import os
import subprocess
import sys

class ProjectManager:
    """Gestionnaire de projets Python avec environnements virtuels."""

    def __init__(self, projects_dir="~/Projets"):
        self.projects_dir = os.path.expanduser(projects_dir)
        os.makedirs(self.projects_dir, exist_ok=True)

    def create_project(self, project_name):
        """Crée un nouveau projet avec environnement virtuel."""
        project_path = os.path.join(self.projects_dir, project_name)

        if os.path.exists(project_path):
            print(f"Le projet {project_name} existe déjà")
            return False

        try:
            # Créer le dossier du projet
            os.makedirs(project_path)

            # Créer l'environnement virtuel
            venv_path = os.path.join(project_path, "venv")
            subprocess.run([sys.executable, "-m", "venv", venv_path],
                         check=True)

            # Créer les dossiers standards
            os.makedirs(os.path.join(project_path, "src"))
            os.makedirs(os.path.join(project_path, "tests"))

            # Créer les fichiers de base
            with open(os.path.join(project_path, "requirements.txt"), "w") as f:
                f.write("# Dépendances du projet\n")

            with open(os.path.join(project_path, "README.md"), "w") as f:
                f.write(f"# {project_name}\n\nDescription du projet\n")

            with open(os.path.join(project_path, ".gitignore"), "w") as f:
                f.write("venv/\n*.pyc\n__pycache__/\n.env\n")

            print(f"✅ Projet {project_name} créé avec succès")
            print(f"📁 Dossier: {project_path}")
            print(f"🐍 Pour activer: cd {project_path} && source venv/bin/activate")

            return True

        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de la création: {e}")
            return False

    def list_projects(self):
        """Liste tous les projets."""
        if not os.path.exists(self.projects_dir):
            print("Aucun projet trouvé")
            return

        projects = [d for d in os.listdir(self.projects_dir)
                   if os.path.isdir(os.path.join(self.projects_dir, d))]

        if not projects:
            print("Aucun projet trouvé")
            return

        print("📋 Projets disponibles:")
        for project in sorted(projects):
            project_path = os.path.join(self.projects_dir, project)
            venv_exists = os.path.exists(os.path.join(project_path, "venv"))
            status = "✅" if venv_exists else "❌"
            print(f"  {status} {project}")

    def activate_project(self, project_name):
        """Génère la commande d'activation pour un projet."""
        project_path = os.path.join(self.projects_dir, project_name)

        if not os.path.exists(project_path):
            print(f"Projet {project_name} non trouvé")
            return

        venv_path = os.path.join(project_path, "venv")
        if not os.path.exists(venv_path):
            print(f"Environnement virtuel non trouvé pour {project_name}")
            return

        # Commandes d'activation selon l'OS
        if os.name == 'nt':  # Windows
            activate_cmd = f"cd {project_path} && venv\\Scripts\\activate"
        else:  # Linux/Mac
            activate_cmd = f"cd {project_path} && source venv/bin/activate"

        print(f"Pour activer le projet {project_name}:")
        print(f"  {activate_cmd}")

def main():
    """Interface en ligne de commande."""
    pm = ProjectManager()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python project_manager.py create <nom_projet>")
        print("  python project_manager.py list")
        print("  python project_manager.py activate <nom_projet>")
        return

    command = sys.argv[1]

    if command == "create" and len(sys.argv) == 3:
        pm.create_project(sys.argv[2])
    elif command == "list":
        pm.list_projects()
    elif command == "activate" and len(sys.argv) == 3:
        pm.activate_project(sys.argv[2])
    else:
        print("Commande inconnue ou arguments manquants")

if __name__ == "__main__":
    main()
```

### Utilisation du gestionnaire

```bash
# Créer un nouveau projet
python project_manager.py create mon_nouveau_projet

# Lister les projets
python project_manager.py list

# Obtenir la commande d'activation
python project_manager.py activate mon_nouveau_projet
```

## Environnements virtuels avec requirements.txt

### Workflow de développement

```bash
# 1. Créer le projet
mkdir projet_analyse_data
cd projet_analyse_data
python -m venv venv
source venv/bin/activate

# 2. Installer les packages de base
pip install pandas matplotlib jupyter

# 3. Sauvegarder les dépendances
pip freeze > requirements.txt

# 4. Ajouter de nouveaux packages
pip install seaborn scikit-learn

# 5. Mettre à jour requirements.txt
pip freeze > requirements.txt
```

### Requirements.txt avec commentaires

```txt
# requirements.txt

# Analyse de données
pandas>=1.3.0
numpy>=1.21.0

# Visualisation
matplotlib>=3.3.0
seaborn>=0.11.0

# Machine Learning
scikit-learn>=1.0.0

# Jupyter
jupyter>=1.0.0
ipykernel>=6.0.0

# Utilitaires
requests>=2.25.0
python-dotenv>=0.19.0

# Développement (optionnel)
# pytest>=6.0.0
# black>=21.0.0
```

## Outils avancés

### pipenv (alternative moderne)

```bash
# Installer pipenv
pip install pipenv

# Créer un projet avec pipenv
mkdir mon_projet
cd mon_projet
pipenv install requests flask

# Activer l'environnement
pipenv shell

# Installer les dépendances de développement
pipenv install pytest --dev

# Installer depuis Pipfile
pipenv install
```

### conda (pour la data science)

```bash
# Créer un environnement conda
conda create --name mon_env python=3.9

# Activer
conda activate mon_env

# Installer des packages
conda install pandas numpy matplotlib

# Exporter l'environnement
conda env export > environment.yml

# Recréer l'environnement
conda env create -f environment.yml
```

## Dépannage courant

### Problème : Python pas trouvé après activation

```bash
# Vérifier le chemin Python
which python
echo $PATH

# Recréer l'environnement si nécessaire
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
```

### Problème : Packages non trouvés

```bash
# Vérifier que l'environnement est activé
pip list

# Vérifier le chemin d'installation
python -c "import sys; print(sys.path)"

# Réinstaller si nécessaire
pip install -r requirements.txt
```

### Problème : Conflits de versions

```bash
# Voir l'arbre des dépendances
pip install pipdeptree
pipdeptree

# Nettoyer et réinstaller
pip freeze > packages.txt
pip uninstall -r packages.txt -y
pip install -r requirements.txt
```

## Exercices pratiques

### Exercice 1 : Projet blog simple

Créez un projet de blog avec Flask :
1. Créez l'environnement virtuel
2. Installez Flask, SQLAlchemy, et Flask-Login
3. Créez une application basique
4. Générez requirements.txt

### Exercice 2 : Analyse de données météo

Créez un projet d'analyse météo :
1. Environnement avec pandas, requests, matplotlib
2. Script pour récupérer des données météo
3. Analyse et graphiques
4. Documentation du setup

### Exercice 3 : Gestionnaire de projets

Améliorez le gestionnaire de projets :
1. Ajoutez la suppression de projets
2. Ajoutez la sauvegarde/restauration d'environnements
3. Intégrez Git automatiquement
4. Créez une interface graphique simple

## Solutions des exercices

### Solution Exercice 1 : Blog simple

```bash
# Création du projet
mkdir blog_simple
cd blog_simple
python -m venv venv
source venv/bin/activate

# Installation des dépendances
pip install flask flask-sqlalchemy flask-login
pip freeze > requirements.txt
```

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre-clé-secrète'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle de données
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Créer les tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if title and content:
            post = Post(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            flash('Article créé avec succès!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Veuillez remplir tous les champs', 'error')

    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/layout.html -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Blog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .post { border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 5px; }
        .btn { background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
        .form-group { margin: 15px 0; }
        input, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        textarea { height: 200px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Mon Blog</h1>
        <nav>
            <a href="{{ url_for('home') }}" class="btn">Accueil</a>
            <a href="{{ url_for('new_post') }}" class="btn">Nouvel Article</a>
        </nav>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/home.html -->
{% extends "layout.html" %}
{% block content %}
    <h2>Articles récents</h2>

    {% if posts %}
        {% for post in posts %}
            <div class="post">
                <h3>{{ post.title }}</h3>
                <p><small>Publié le {{ post.date_posted.strftime('%d/%m/%Y à %H:%M') }}</small></p>
                <p>{{ post.content }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p>Aucun article pour le moment. <a href="{{ url_for('new_post') }}">Créez le premier !</a></p>
    {% endif %}
{% endblock %}
```

```html
<!-- templates/new_post.html -->
{% extends "layout.html" %}
{% block content %}
    <h2>Nouvel Article</h2>

    <form method="POST">
        <div class="form-group">
            <label for="title">Titre:</label>
            <input type="text" id="title" name="title" required>
        </div>

        <div class="form-group">
            <label for="content">Contenu:</label>
            <textarea id="content" name="content" required></textarea>
        </div>

        <button type="submit" class="btn">Publier</button>
    </form>
{% endblock %}
```

```txt
# requirements.txt final
blinker==1.6.2
click==8.1.7
Flask==2.3.3
Flask-Login==0.6.2
Flask-SQLAlchemy==3.0.5
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
SQLAlchemy==2.0.20
Werkzeug==2.3.7
```

## Résumé

Les environnements virtuels sont essentiels pour :

1. **Isoler les dépendances** de chaque projet
2. **Éviter les conflits** de versions
3. **Faciliter la collaboration** et le déploiement
4. **Maintenir la propreté** du système Python global
5. **Reproduire** exactement l'environnement de développement

### Commandes essentielles à retenir

```bash
# Créer un environnement
python -m venv venv

# Activer
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Désactiver
deactivate

# Sauvegarder les dépendances
pip freeze > requirements.txt

# Restaurer les dépendances
pip install -r requirements.txt
```

Dans la prochaine section, nous verrons comment créer des packages distribuables et les publier sur PyPI.

⏭️
