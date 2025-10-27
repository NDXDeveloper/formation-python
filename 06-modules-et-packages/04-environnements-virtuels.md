🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.4 Environnements virtuels (venv)

## Introduction

Un **environnement virtuel** (virtual environment) est un espace isolé qui contient sa propre installation de Python et ses propres packages. C'est comme avoir plusieurs installations de Python indépendantes sur votre ordinateur, chacune avec ses propres bibliothèques.

**Pourquoi est-ce important ?** Imaginez que vous travaillez sur deux projets Python :
- Projet A nécessite Django version 3.2
- Projet B nécessite Django version 4.2

Sans environnements virtuels, vous ne pourriez avoir qu'une seule version de Django installée, ce qui causerait des conflits. Les environnements virtuels résolvent ce problème en isolant les dépendances de chaque projet.

---

## Pourquoi utiliser des environnements virtuels ?

### Problèmes sans environnements virtuels

**Scénario problématique :**
```
Installation système (globale)
├── Python 3.11
├── Django 3.2
├── requests 2.28.0
└── pandas 1.5.0

Projet A → nécessite Django 3.2 ✅
Projet B → nécessite Django 4.2 ❌ Conflit !
```

Si vous mettez à jour Django pour le Projet B, vous cassez le Projet A.

### Solution avec environnements virtuels

```
Environnement virtuel Projet A
├── Python 3.11
├── Django 3.2
└── requests 2.28.0

Environnement virtuel Projet B
├── Python 3.11
├── Django 4.2
└── pandas 2.0.0

Les deux projets fonctionnent sans conflit ! ✅
```

### Avantages des environnements virtuels

1. **Isolation des dépendances** : Chaque projet a ses propres packages
2. **Reproductibilité** : Facile de recréer l'environnement exact d'un projet
3. **Propreté** : Le système Python reste propre
4. **Sécurité** : Pas besoin de droits administrateur pour installer des packages
5. **Expérimentation** : Tester des packages sans affecter d'autres projets
6. **Versions multiples** : Utiliser différentes versions d'un même package

---

## Module venv

Python inclut depuis la version 3.3 le module `venv` qui permet de créer des environnements virtuels facilement, sans installation supplémentaire.

**Alternatives :**
- `virtualenv` : Version plus ancienne et plus flexible
- `conda` : Utilisé principalement en data science
- `pipenv` et `poetry` : Outils modernes combinant venv et gestion de dépendances

Dans ce tutoriel, nous utiliserons `venv` car c'est l'outil standard intégré à Python.

---

## Créer un environnement virtuel

### Syntaxe de base

```bash
python -m venv nom_environnement
```

Ou selon votre système :
```bash
python3 -m venv nom_environnement
```

### Création étape par étape

**Étape 1 : Créer un dossier pour votre projet**
```bash
mkdir mon_projet
cd mon_projet
```

**Étape 2 : Créer l'environnement virtuel**
```bash
python -m venv venv
```

Cette commande crée un dossier `venv` contenant :
```
mon_projet/
    venv/
        bin/          (ou Scripts/ sous Windows)
            python
            pip
            activate
        lib/
            python3.11/
                site-packages/
        include/
        pyvenv.cfg
```

**Note sur le nom :** Par convention, on nomme souvent l'environnement `venv`, `.venv`, ou `env`. Vous pouvez utiliser n'importe quel nom.

### Que contient l'environnement virtuel ?

- **bin/** (ou **Scripts/** sous Windows) : Exécutables Python et pip
- **lib/** : Packages Python installés
- **include/** : Fichiers d'en-tête C
- **pyvenv.cfg** : Configuration de l'environnement

---

## Activer l'environnement virtuel

Après création, vous devez **activer** l'environnement pour l'utiliser.

### Sur Linux et macOS

```bash
source venv/bin/activate
```

### Sur Windows

**PowerShell :**
```powershell
venv\Scripts\Activate.ps1
```

**Command Prompt :**
```cmd
venv\Scripts\activate.bat
```

### Git Bash sur Windows

```bash
source venv/Scripts/activate
```

### Vérification de l'activation

Quand l'environnement est activé, vous verrez son nom entre parenthèses dans votre terminal :

```bash
(venv) user@computer:~/mon_projet$
```

Pour vérifier quel Python est utilisé :
```bash
which python    # Linux/macOS
where python    # Windows
```

Résultat attendu :
```
/home/user/mon_projet/venv/bin/python
```

---

## Utiliser l'environnement virtuel

### Installer des packages

Une fois l'environnement activé, utilisez pip normalement :

```bash
(venv) $ pip install requests
(venv) $ pip install pandas numpy matplotlib
```

Les packages sont installés **uniquement** dans cet environnement virtuel.

### Vérifier les packages installés

```bash
(venv) $ pip list
```

Résultat (environnement nouvellement créé) :
```
Package    Version
---------- -------
pip        23.2.1
setuptools 68.0.0
```

Après installation de packages :
```
Package    Version
---------- -------
certifi    2023.7.22
charset-normalizer  3.2.0
idna       3.4
pip        23.2.1
requests   2.31.0
setuptools 68.0.0
urllib3    2.0.4
```

### Créer requirements.txt

```bash
(venv) $ pip freeze > requirements.txt
```

Contenu de `requirements.txt` :
```
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
requests==2.31.0
urllib3==2.0.4
```

### Exécuter des scripts Python

Avec l'environnement activé, Python utilisera automatiquement les packages de cet environnement :

```bash
(venv) $ python mon_script.py
```

---

## Désactiver l'environnement virtuel

Pour sortir de l'environnement virtuel et revenir au Python système :

```bash
(venv) $ deactivate
```

Le préfixe `(venv)` disparaît :
```bash
user@computer:~/mon_projet$
```

**Important :** La désactivation ne supprime pas l'environnement, elle arrête simplement de l'utiliser.

---

## Supprimer un environnement virtuel

Pour supprimer complètement un environnement virtuel :

### Sur Linux et macOS

```bash
rm -rf venv
```

### Sur Windows

```cmd
rmdir /s venv
```

Ou simplement supprimer le dossier manuellement dans l'explorateur de fichiers.

**Note :** Il est sans danger de supprimer un environnement virtuel. Vous pouvez toujours en recréer un nouveau avec `python -m venv venv` et réinstaller les packages depuis `requirements.txt`.

---

## Workflow typique avec venv

### Démarrer un nouveau projet

```bash
# 1. Créer le dossier du projet
mkdir mon_nouveau_projet
cd mon_nouveau_projet

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# 4. Installer les packages nécessaires
pip install flask requests pandas

# 5. Créer requirements.txt
pip freeze > requirements.txt

# 6. Créer votre code
touch app.py

# 7. Travailler sur le projet...
```

### Reprendre un projet existant

```bash
# 1. Cloner ou ouvrir le projet
cd mon_projet_existant

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement
source venv/bin/activate  # Linux/macOS

# 4. Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

# 5. Travailler sur le projet...
python app.py
```

### Fin de session de travail

```bash
# 1. Sauvegarder votre travail
git add .
git commit -m "Ajout de nouvelles fonctionnalités"

# 2. Désactiver l'environnement
deactivate
```

---

## Environnements virtuels et Git

### Fichier .gitignore

**Important :** Ne commitez JAMAIS votre environnement virtuel dans Git. Les environnements virtuels sont spécifiques à chaque machine.

**Fichier : `.gitignore`**
```
# Environnements virtuels
venv/
env/
.venv/
ENV/
env.bak/
venv.bak/

# Fichiers Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Environnement
.env
.env.local
```

### Ce qu'il faut committer

```
✅ À committer :
    - Code source (.py)
    - requirements.txt
    - README.md
    - .gitignore
    - Fichiers de configuration
    - Documentation

❌ À ne PAS committer :
    - venv/ ou env/
    - __pycache__/
    - *.pyc
    - .env (variables d'environnement sensibles)
```

### Structure de projet recommandée

```
mon_projet/
    venv/                  # Ignoré par Git
    src/
        __init__.py
        main.py
        utils.py
    tests/
        test_main.py
    requirements.txt       # Committé
    .gitignore            # Committé
    README.md             # Committé
    .env.example          # Committé
    .env                  # Ignoré par Git
```

---

## Bonnes pratiques

### 1. Un environnement virtuel par projet

```
✅ BON :
projets/
    projet_a/
        venv/
        app.py
        requirements.txt
    projet_b/
        venv/
        main.py
        requirements.txt

❌ MAUVAIS :
projets/
    venv/  ← Partagé entre plusieurs projets
    projet_a/
        app.py
    projet_b/
        main.py
```

### 2. Activer l'environnement avant de travailler

**Toujours activer avant d'installer des packages ou d'exécuter du code :**

```bash
# ✅ BON
cd mon_projet
source venv/bin/activate
pip install requests
python app.py

# ❌ MAUVAIS
cd mon_projet
pip install requests  # S'installe dans le système !
python app.py
```

### 3. Nommer l'environnement de manière standard

Noms recommandés :
- `venv` (le plus courant)
- `.venv` (caché sur Linux/macOS)
- `env`
- `virtualenv`

**Évitez** des noms comme `mon_env`, `python_env`, etc.

### 4. Mettre à jour pip après création

```bash
(venv) $ pip install --upgrade pip
```

### 5. Maintenir requirements.txt à jour

Après chaque installation de package :
```bash
(venv) $ pip freeze > requirements.txt
```

Ou créer manuellement pour ne lister que les dépendances directes :
```
# requirements.txt
flask==2.3.0
requests==2.31.0
pandas==2.0.0
```

### 6. Documenter les prérequis

Dans votre README.md :

```markdown
## Installation

### Prérequis
- Python 3.8 ou supérieur

### Setup
1. Cloner le repository
```bash
git clone https://github.com/username/projet.git
cd projet
```

2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Lancer l'application
```bash
python app.py
```
```

### 7. Utiliser .env pour les variables d'environnement

Ne stockez jamais de secrets dans le code. Utilisez python-dotenv :

```bash
(venv) $ pip install python-dotenv
```

**Fichier : `.env`** (ignoré par Git)
```
DATABASE_URL=postgresql://localhost/mabase
SECRET_KEY=super_secret_key_123
API_KEY=abc123xyz789
```

**Fichier : `.env.example`** (committé dans Git)
```
DATABASE_URL=postgresql://localhost/mabase
SECRET_KEY=your_secret_key_here
API_KEY=your_api_key_here
```

**Utilisation dans le code :**
```python
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
```

---

## Environnements virtuels dans les IDEs

### Visual Studio Code

VS Code détecte automatiquement les environnements virtuels.

**Sélectionner l'interpréteur :**
1. Ouvrir la palette de commandes : `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur Mac)
2. Taper : "Python: Select Interpreter"
3. Choisir l'interpréteur dans `venv/bin/python`

**Configuration automatique :**
VS Code active automatiquement l'environnement dans le terminal intégré.

**Fichier : `.vscode/settings.json`**
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.terminal.activateEnvironment": true
}
```

### PyCharm

PyCharm gère excellemment les environnements virtuels.

**Créer un environnement :**
1. File → Settings → Project → Python Interpreter
2. Cliquer sur l'icône d'engrenage → Add
3. Choisir "Virtualenv Environment"
4. Choisir "New environment" et sélectionner l'emplacement

PyCharm active automatiquement l'environnement.

### Jupyter Notebook

Pour utiliser votre environnement dans Jupyter :

```bash
(venv) $ pip install ipykernel
(venv) $ python -m ipykernel install --user --name=venv --display-name="Python (venv)"
```

Ensuite, dans Jupyter, sélectionnez le kernel "Python (venv)".

---

## Environnements virtuels avec différentes versions de Python

### Créer un environnement avec une version spécifique

Si vous avez plusieurs versions de Python installées :

```bash
# Utiliser Python 3.9
python3.9 -m venv venv39

# Utiliser Python 3.11
python3.11 -m venv venv311
```

### Vérifier la version de Python

```bash
source venv/bin/activate
python --version
```

### Cas d'usage

Certains projets nécessitent des versions spécifiques de Python :

```
projet_ancien/
    venv38/          # Python 3.8 pour compatibilité

projet_nouveau/
    venv311/         # Python 3.11 pour nouvelles fonctionnalités
```

---

## Problèmes courants et solutions

### Problème 1 : Commande venv introuvable

**Erreur :**
```
No module named venv
```

**Solution (Ubuntu/Debian) :**
```bash
sudo apt-get install python3-venv
```

**Solution (autres systèmes) :**
Installer virtualenv :
```bash
pip install virtualenv
virtualenv venv
```

### Problème 2 : Permission refusée sur Windows (PowerShell)

**Erreur :**
```
... cannot be loaded because running scripts is disabled on this system
```

**Solution :**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Ou utilisez Command Prompt au lieu de PowerShell.

### Problème 3 : L'environnement n'est pas activé

**Symptôme :** Vous installez des packages mais ils ne sont pas trouvés.

**Vérification :**
```bash
which python  # Linux/macOS
where python  # Windows
```

Si le résultat ne pointe pas vers `venv/bin/python`, réactivez :
```bash
source venv/bin/activate
```

### Problème 4 : Packages installés avant de créer venv

**Symptôme :** Packages manquants dans l'environnement virtuel.

**Solution :**
1. Créer requirements.txt du système :
```bash
pip freeze > requirements_system.txt
```

2. Créer et activer venv :
```bash
python -m venv venv
source venv/bin/activate
```

3. Installer les packages nécessaires :
```bash
pip install -r requirements_system.txt
```

### Problème 5 : Environnement corrompu

**Symptôme :** Erreurs bizarres, packages manquants.

**Solution :** Recréer l'environnement :
```bash
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Problème 6 : Espace disque insuffisant

**Symptôme :** Chaque projet a son environnement = beaucoup d'espace.

**Solutions :**
- Supprimer les environnements inutilisés
- Utiliser `virtualenvwrapper` pour centraliser les environnements
- Utiliser `conda` qui partage les packages entre environnements

### Problème 7 : Prompt ne montre pas (venv)

**Solution :**
```bash
export VIRTUAL_ENV_DISABLE_PROMPT=0
source venv/bin/activate
```

Ou vérifier manuellement :
```bash
echo $VIRTUAL_ENV
```

---

## Alternatives à venv

### virtualenv

Plus flexible que venv, avec plus d'options :

```bash
pip install virtualenv
virtualenv venv
virtualenv -p python3.9 venv39
```

### virtualenvwrapper

Facilite la gestion de plusieurs environnements :

```bash
pip install virtualenvwrapper

# Créer un environnement
mkvirtualenv mon_projet

# Lister les environnements
lsvirtualenv

# Activer un environnement
workon mon_projet

# Désactiver
deactivate

# Supprimer
rmvirtualenv mon_projet
```

### conda

Populaire en data science :

```bash
conda create -n mon_env python=3.11
conda activate mon_env
conda install pandas numpy matplotlib
conda deactivate
```

**Avantages de conda :**
- Gère Python ET autres packages (R, C++, etc.)
- Packages pré-compilés (plus rapides)
- Meilleure résolution de dépendances

**Inconvénients :**
- Plus lourd
- Plus lent
- Moins de packages disponibles que PyPI

### pipenv et poetry

Outils modernes qui combinent venv et pip (voir section 6.5).

---

## Comparaison des outils

| Outil | Avantages | Inconvénients | Cas d'usage |
|-------|-----------|---------------|-------------|
| **venv** | Intégré à Python, simple, léger | Fonctionnalités limitées | Projets Python standards |
| **virtualenv** | Plus flexible, compatible anciennes versions | Installation nécessaire | Projets nécessitant flexibilité |
| **conda** | Gère non-Python, packages pré-compilés | Lourd, plus lent | Data science, calcul scientifique |
| **pipenv** | Gestion moderne, Pipfile | Parfois lent | Projets modernes |
| **poetry** | Gestion complète du projet | Courbe d'apprentissage | Projets à publier |

---

## Automatisation avec des scripts

### Script d'initialisation (Linux/macOS)

**Fichier : `setup.sh`**
```bash
#!/bin/bash

echo "🚀 Configuration de l'environnement..."

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
    echo "✅ Dépendances installées"
else
    echo "⚠️  requirements.txt introuvable"
fi

echo "✅ Environnement prêt !"
echo "Pour activer : source venv/bin/activate"
```

Utilisation :
```bash
chmod +x setup.sh
./setup.sh
```

### Script d'initialisation (Windows)

**Fichier : `setup.bat`**
```batch
@echo off
echo Configuration de l'environnement...

REM Créer l'environnement virtuel
python -m venv venv

REM Activer l'environnement
call venv\Scripts\activate.bat

REM Mettre à jour pip
pip install --upgrade pip

REM Installer les dépendances
if exist requirements.txt (
    pip install -r requirements.txt
    echo Dependances installees
) else (
    echo requirements.txt introuvable
)

echo Environnement pret !
echo Pour activer : venv\Scripts\activate
```

### Makefile pour automatiser

**Fichier : `Makefile`**
```makefile
.PHONY: install clean run test

install:
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

run:
	. venv/bin/activate && python app.py

test:
	. venv/bin/activate && pytest

dev:
	. venv/bin/activate && pip install -r requirements-dev.txt
```

Utilisation :
```bash
make install  # Créer l'environnement et installer
make run      # Lancer l'application
make test     # Lancer les tests
make clean    # Nettoyer
```

---

## Exemple complet : Projet Flask

### Structure du projet

```
mon_app_flask/
    venv/
    app/
        __init__.py
        routes.py
        models.py
    tests/
        test_routes.py
    app.py
    requirements.txt
    .env
    .env.example
    .gitignore
    README.md
```

### Configuration étape par étape

```bash
# 1. Créer le projet
mkdir mon_app_flask
cd mon_app_flask

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement
source venv/bin/activate  # Linux/macOS

# 4. Installer Flask
pip install flask python-dotenv

# 5. Créer requirements.txt
pip freeze > requirements.txt
```

### Fichier principal

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
    return "Hello from virtual environment!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Exécution

```bash
(venv) $ python app.py
```

### Partage du projet

**requirements.txt :**
```
blinker==1.6.2
click==8.1.7
Flask==2.3.3
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
python-dotenv==1.0.0
Werkzeug==2.3.7
```

Un autre développeur peut recréer l'environnement avec :
```bash
git clone https://github.com/username/mon_app_flask.git
cd mon_app_flask
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## Résumé

Dans cette section, vous avez appris :

- Ce que sont les environnements virtuels et pourquoi ils sont indispensables
- Comment créer, activer et désactiver un environnement virtuel avec venv
- Le workflow typique pour démarrer et reprendre un projet
- Comment gérer les environnements virtuels avec Git
- Les bonnes pratiques pour organiser vos projets
- Comment résoudre les problèmes courants
- Les alternatives à venv (virtualenv, conda, etc.)
- Comment automatiser la création d'environnements

**Points clés à retenir :**

1. **Toujours utiliser un environnement virtuel** pour chaque projet Python
2. **Ne jamais committer venv/** dans Git
3. **Maintenir requirements.txt à jour** pour documenter les dépendances
4. **Activer l'environnement avant de travailler** sur le projet
5. **Un environnement par projet** pour éviter les conflits

Les environnements virtuels sont une pratique fondamentale en Python professionnel. Ils vous permettent de travailler proprement sur plusieurs projets sans créer de conflits entre dépendances. Combinés avec pip et requirements.txt, ils rendent vos projets reproductibles et faciles à partager.

Dans la prochaine section, nous découvrirons des outils modernes comme Poetry et Pipenv qui améliorent encore la gestion des environnements et des dépendances.

⏭️ [Outils modernes (Poetry, Pipenv)](/06-modules-et-packages/05-outils-modernes-poetry-pipenv.md)
