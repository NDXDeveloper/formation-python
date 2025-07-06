🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 11.1 : Frameworks web (Flask basics)

## Introduction

Un framework web est une boîte à outils qui simplifie le développement d'applications web. Au lieu de tout coder depuis zéro, vous utilisez des composants prêts à l'emploi pour gérer les requêtes HTTP, le routage, les templates, etc.

Flask est un micro-framework Python idéal pour débuter : il est simple, flexible et permet de comprendre les concepts fondamentaux du web.

## Pourquoi Flask ?

**Avantages de Flask :**
- Simplicité d'apprentissage
- Flexibilité : vous ajoutez seulement ce dont vous avez besoin
- Documentation excellente
- Grande communauté
- Parfait pour les petites et moyennes applications

**Comparaison rapide :**
- **Flask** : minimaliste, vous construisez votre application étape par étape
- **Django** : "batteries incluses", beaucoup de fonctionnalités intégrées

## Installation et première application

### Installation

```bash
# Créer un environnement virtuel
python -m venv flask_env
source flask_env/bin/activate  # Sur Windows: flask_env\Scripts\activate

# Installer Flask
pip install flask
```

### Votre première application Flask

Créez un fichier `app.py` :

```python
from flask import Flask

# Créer une instance Flask
app = Flask(__name__)

# Définir une route
@app.route('/')
def accueil():
    return '<h1>Bienvenue dans mon application Flask !</h1>'

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)
```

**Exécution :**
```bash
python app.py
```

Ouvrez votre navigateur sur `http://127.0.0.1:5000`

**Explication du code :**
- `Flask(__name__)` : crée l'application Flask
- `@app.route('/')` : décorateur qui associe l'URL "/" à la fonction
- `app.run(debug=True)` : lance le serveur en mode débogage

## Routage et URLs

### Routes simples

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return '<h1>Page d\'accueil</h1>'

@app.route('/apropos')
def a_propos():
    return '<h1>À propos de nous</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contactez-nous</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

### Routes avec paramètres

```python
@app.route('/utilisateur/<nom>')
def profil_utilisateur(nom):
    return f'<h1>Profil de {nom}</h1>'

@app.route('/article/<int:id>')
def afficher_article(id):
    return f'<h1>Article numéro {id}</h1>'

@app.route('/produit/<float:prix>')
def prix_produit(prix):
    return f'<h1>Produit à {prix:.2f}€</h1>'
```

**Types de paramètres :**
- `<nom>` : chaîne de caractères (par défaut)
- `<int:id>` : nombre entier
- `<float:prix>` : nombre décimal
- `<path:chemin>` : chaîne avec des slashes

### Méthodes HTTP

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        nom = request.form['nom']
        return f'<h1>Bonjour {nom} !</h1>'
    else:
        return '''
        <form method="POST">
            <input type="text" name="nom" placeholder="Votre nom">
            <button type="submit">Envoyer</button>
        </form>
        '''
```

## Templates avec Jinja2

Les templates séparent la logique Python de la présentation HTML.

### Structure des dossiers

```
mon_app/
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    └── utilisateur.html
```

### Template de base

Créez `templates/base.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mon Application{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        nav { background: #333; padding: 10px; }
        nav a { color: white; text-decoration: none; margin-right: 10px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/apropos">À propos</a>
        <a href="/contact">Contact</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

### Template d'accueil

Créez `templates/index.html` :

```html
{% extends "base.html" %}

{% block title %}Accueil - Mon Application{% endblock %}

{% block content %}
<h1>Bienvenue sur mon site !</h1>
<p>Ceci est la page d'accueil.</p>

{% if utilisateur %}
    <p>Bonjour {{ utilisateur }} !</p>
{% else %}
    <p>Vous n'êtes pas connecté.</p>
{% endif %}

<h2>Nos services :</h2>
<ul>
{% for service in services %}
    <li>{{ service }}</li>
{% endfor %}
</ul>
{% endblock %}
```

### Utilisation des templates

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    services = ['Développement web', 'Conseil', 'Formation']
    return render_template('index.html',
                         utilisateur='Marie',
                         services=services)

@app.route('/utilisateur/<nom>')
def profil_utilisateur(nom):
    return render_template('utilisateur.html', nom=nom)
```

## Gestion des formulaires

### Formulaire simple

Créez `templates/formulaire.html` :

```html
{% extends "base.html" %}

{% block title %}Formulaire de contact{% endblock %}

{% block content %}
<h1>Contactez-nous</h1>

{% if message %}
    <div style="color: green; padding: 10px; border: 1px solid green;">
        {{ message }}
    </div>
{% endif %}

<form method="POST">
    <p>
        <label>Nom :</label><br>
        <input type="text" name="nom" required>
    </p>
    <p>
        <label>Email :</label><br>
        <input type="email" name="email" required>
    </p>
    <p>
        <label>Message :</label><br>
        <textarea name="message" rows="4" cols="50" required></textarea>
    </p>
    <p>
        <button type="submit">Envoyer</button>
    </p>
</form>
{% endblock %}
```

### Traitement du formulaire

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']

        # Ici, vous pourriez sauvegarder en base de données
        # ou envoyer un email

        return render_template('formulaire.html',
                             message=f'Merci {nom}, votre message a été envoyé !')

    return render_template('formulaire.html')
```

## Gestion des erreurs

### Pages d'erreur personnalisées

```python
@app.errorhandler(404)
def page_non_trouvee(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erreur_serveur(error):
    return render_template('500.html'), 500
```

Créez `templates/404.html` :

```html
{% extends "base.html" %}

{% block title %}Page non trouvée{% endblock %}

{% block content %}
<h1>Erreur 404</h1>
<p>La page que vous cherchez n'existe pas.</p>
<p><a href="/">Retour à l'accueil</a></p>
{% endblock %}
```

## Sessions et cookies

### Configuration des sessions

```python
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'votre-clé-secrète-très-sécurisée'

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        nom_utilisateur = request.form['nom_utilisateur']
        mot_de_passe = request.form['mot_de_passe']

        # Vérification simple (à améliorer en production)
        if nom_utilisateur == 'admin' and mot_de_passe == 'secret':
            session['utilisateur'] = nom_utilisateur
            return redirect(url_for('tableau_de_bord'))
        else:
            return render_template('connexion.html',
                                 erreur='Identifiants incorrects')

    return render_template('connexion.html')

@app.route('/tableau-de-bord')
def tableau_de_bord():
    if 'utilisateur' not in session:
        return redirect(url_for('connexion'))

    return f'<h1>Bienvenue {session["utilisateur"]} !</h1>'

@app.route('/deconnexion')
def deconnexion():
    session.pop('utilisateur', None)
    return redirect(url_for('accueil'))
```

## Fichiers statiques

### Organisation des fichiers

```
mon_app/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
└── templates/
    └── base.html
```

### Utilisation dans les templates

```html
<!-- Dans base.html -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

## Exemple complet : Application de blog simple

```python
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Données simulées (en production, utilisez une base de données)
articles = [
    {
        'id': 1,
        'titre': 'Premier article',
        'contenu': 'Ceci est le contenu du premier article.',
        'date': datetime(2024, 1, 15)
    },
    {
        'id': 2,
        'titre': 'Deuxième article',
        'contenu': 'Contenu du deuxième article.',
        'date': datetime(2024, 1, 20)
    }
]

@app.route('/')
def accueil():
    return render_template('blog/index.html', articles=articles)

@app.route('/article/<int:id>')
def afficher_article(id):
    article = next((a for a in articles if a['id'] == id), None)
    if article:
        return render_template('blog/article.html', article=article)
    else:
        return render_template('404.html'), 404

@app.route('/nouvel-article', methods=['GET', 'POST'])
def nouvel_article():
    if request.method == 'POST':
        nouveau_article = {
            'id': len(articles) + 1,
            'titre': request.form['titre'],
            'contenu': request.form['contenu'],
            'date': datetime.now()
        }
        articles.append(nouveau_article)
        return redirect(url_for('accueil'))

    return render_template('blog/nouveau.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercices pratiques

### Exercice 1 : Application de calcul

Créez une application Flask qui :
1. Affiche un formulaire avec deux champs numériques
2. Propose quatre opérations (+, -, *, /)
3. Affiche le résultat sur la même page

**Template `calculatrice.html` :**
```html
{% extends "base.html" %}

{% block content %}
<h1>Calculatrice</h1>

<form method="POST">
    <p>
        <input type="number" name="nombre1" placeholder="Premier nombre" required>
    </p>
    <p>
        <select name="operation" required>
            <option value="">Choisir une opération</option>
            <option value="+">Addition (+)</option>
            <option value="-">Soustraction (-)</option>
            <option value="*">Multiplication (*)</option>
            <option value="/">Division (/)</option>
        </select>
    </p>
    <p>
        <input type="number" name="nombre2" placeholder="Deuxième nombre" required>
    </p>
    <p>
        <button type="submit">Calculer</button>
    </p>
</form>

{% if resultat is defined %}
    <h2>Résultat : {{ resultat }}</h2>
{% endif %}
{% endblock %}
```

### Exercice 2 : Liste de tâches

Créez une application de gestion de tâches qui permet de :
1. Ajouter une nouvelle tâche
2. Afficher la liste des tâches
3. Marquer une tâche comme terminée

**Structure suggérée :**
```python
taches = [
    {'id': 1, 'texte': 'Faire les courses', 'termine': False},
    {'id': 2, 'texte': 'Apprendre Flask', 'termine': True}
]
```

### Exercice 3 : Générateur de mots de passe

Créez une application qui génère des mots de passe avec :
1. Un formulaire pour choisir la longueur
2. Des options (majuscules, minuscules, chiffres, symboles)
3. Affichage du mot de passe généré

## Solutions des exercices

### Solution Exercice 1 : Calculatrice

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    if request.method == 'POST':
        try:
            nombre1 = float(request.form['nombre1'])
            nombre2 = float(request.form['nombre2'])
            operation = request.form['operation']

            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
                if nombre2 != 0:
                    resultat = nombre1 / nombre2
                else:
                    resultat = "Erreur : Division par zéro"

            return render_template('calculatrice.html', resultat=resultat)

        except ValueError:
            return render_template('calculatrice.html',
                                 resultat="Erreur : Nombres invalides")

    return render_template('calculatrice.html')
```

### Solution Exercice 2 : Liste de tâches

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

taches = [
    {'id': 1, 'texte': 'Faire les courses', 'termine': False},
    {'id': 2, 'texte': 'Apprendre Flask', 'termine': True}
]

@app.route('/')
def liste_taches():
    return render_template('taches.html', taches=taches)

@app.route('/ajouter', methods=['POST'])
def ajouter_tache():
    nouvelle_tache = {
        'id': max([t['id'] for t in taches]) + 1 if taches else 1,
        'texte': request.form['texte'],
        'termine': False
    }
    taches.append(nouvelle_tache)
    return redirect(url_for('liste_taches'))

@app.route('/terminer/<int:id>')
def terminer_tache(id):
    tache = next((t for t in taches if t['id'] == id), None)
    if tache:
        tache['termine'] = True
    return redirect(url_for('liste_taches'))
```

### Solution Exercice 3 : Générateur de mots de passe

```python
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/generateur', methods=['GET', 'POST'])
def generateur_mot_de_passe():
    if request.method == 'POST':
        longueur = int(request.form.get('longueur', 8))

        caracteres = ''
        if request.form.get('minuscules'):
            caracteres += string.ascii_lowercase
        if request.form.get('majuscules'):
            caracteres += string.ascii_uppercase
        if request.form.get('chiffres'):
            caracteres += string.digits
        if request.form.get('symboles'):
            caracteres += '!@#$%^&*'

        if caracteres:
            mot_de_passe = ''.join(random.choice(caracteres)
                                  for _ in range(longueur))
            return render_template('generateur.html',
                                 mot_de_passe=mot_de_passe)
        else:
            return render_template('generateur.html',
                                 erreur="Choisissez au moins un type de caractère")

    return render_template('generateur.html')
```

## Bonnes pratiques

### Organisation du code

```python
# config.py
class Config:
    SECRET_KEY = 'votre-clé-secrète'
    DEBUG = True

# app.py
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enregistrer les routes
    from routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

### Sécurité de base

```python
# Éviter les injections XSS
from flask import escape

@app.route('/utilisateur/<nom>')
def profil(nom):
    return f'<h1>Profil de {escape(nom)}</h1>'

# Valider les données d'entrée
@app.route('/age/<int:age>')
def verifier_age(age):
    if age < 0 or age > 150:
        return "Âge invalide", 400
    return f'Votre âge : {age} ans'
```

## Résumé

Flask est un excellent framework pour débuter le développement web avec Python. Les concepts clés à retenir :

- **Routes** : associer des URLs à des fonctions Python
- **Templates** : séparer la logique de la présentation
- **Formulaires** : gérer les données envoyées par l'utilisateur
- **Sessions** : maintenir l'état entre les requêtes
- **Gestion d'erreurs** : créer des pages d'erreur personnalisées

Dans la prochaine section, nous verrons comment utiliser la bibliothèque `requests` pour faire des requêtes HTTP vers d'autres services web.

---

*Pratiquez ces concepts avec les exercices proposés avant de passer à la suite !*

⏭️
