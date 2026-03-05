🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.3 Flask - Micro-framework léger

## Introduction à Flask

**Flask** est un micro-framework web Python créé par Armin Ronacher en 2010. Le terme "micro" ne signifie pas que Flask est limité, mais plutôt qu'il fournit les outils essentiels pour créer une application web sans imposer de structure rigide. C'est un framework minimaliste qui vous laisse une grande liberté dans vos choix d'architecture.

Flask est souvent décrit comme le couteau suisse du développement web Python : simple, flexible, et parfait pour une grande variété de projets.

## Pourquoi choisir Flask ?

### Philosophie "micro"

Flask suit une philosophie minimaliste : il ne fournit que l'essentiel (routage, templates, sessions) et vous laisse ajouter ce dont vous avez besoin via des extensions. C'est comme acheter une voiture de base et choisir vous-même les options que vous voulez.

### Avantages de Flask

**1. Simplicité et facilité d'apprentissage**
Flask a une API simple et intuitive. Vous pouvez créer une application fonctionnelle en quelques lignes de code.

**2. Flexibilité maximale**
Contrairement à Django qui impose une structure, Flask vous laisse organiser votre code comme vous le souhaitez.

**3. Légèreté**
Flask ne charge que ce dont vous avez besoin. Votre application reste rapide et légère.

**4. Excellent pour apprendre**
Flask vous force à comprendre comment les choses fonctionnent, ce qui en fait un excellent outil pédagogique.

**5. Extensibilité**
Des centaines d'extensions Flask sont disponibles pour ajouter des fonctionnalités (bases de données, authentification, etc.).

**6. Documentation de qualité**
Flask dispose d'une documentation claire et complète, idéale pour les débutants.

### Quand utiliser Flask ?

Flask est idéal pour :

- ✅ Petites et moyennes applications web
- ✅ Prototypes rapides et MVPs
- ✅ APIs REST simples
- ✅ Applications nécessitant une architecture personnalisée
- ✅ Projets d'apprentissage
- ✅ Microservices légers
- ✅ Applications avec des besoins spécifiques

Flask est moins adapté pour :

- ❌ Applications très complexes nécessitant beaucoup de fonctionnalités intégrées (considérez Django)
- ❌ APIs nécessitant une validation de données très stricte et automatique (considérez FastAPI)
- ❌ Projets où vous voulez une structure imposée dès le départ

## Installation de Flask

### Créer l'environnement virtuel

Comme toujours, commencez par créer un environnement virtuel :

```bash
# Créer un dossier pour votre projet
mkdir mon_projet_flask  
cd mon_projet_flask  

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate
```

### Installer Flask

```bash
pip install Flask
```

C'est tout ! Flask est installé et prêt à l'emploi. Le package est léger et s'installe rapidement.

### Vérifier l'installation

```bash
python -c "import flask; print(flask.__version__)"
```

Vous devriez voir la version de Flask s'afficher (par exemple, 3.0.0).

## Votre première application Flask

Créons la plus simple application Flask possible.

### Le code minimal

Créez un fichier `app.py` :

```python
from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route
@app.route('/')
def hello():
    return "Bonjour, bienvenue sur Flask !"

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)
```

### Explication ligne par ligne

```python
from flask import Flask
```
Importe la classe `Flask` qui est le cœur de votre application.

```python
app = Flask(__name__)
```
Crée une instance de Flask. Le paramètre `__name__` aide Flask à localiser les ressources (templates, fichiers statiques).

```python
@app.route('/')
```
Décorateur qui associe une fonction à une URL. Ici, `/` représente la racine du site.

```python
def hello():
    return "Bonjour, bienvenue sur Flask !"
```
La fonction qui sera exécutée quand quelqu'un visite cette URL. Elle retourne le contenu à afficher.

```python
if __name__ == '__main__':
    app.run(debug=True)
```
Lance le serveur de développement si le fichier est exécuté directement. `debug=True` active le mode debug avec rechargement automatique.

### Lancer l'application

```bash
python app.py
```

Vous devriez voir :
```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
```

Ouvrez votre navigateur et allez à `http://127.0.0.1:5000/`. Vous verrez votre message !

**Note :** Flask utilise par défaut le port 5000, tandis que FastAPI utilise 8000.

## Les routes dans Flask

Les routes définissent comment votre application répond aux différentes URLs.

### Routes simples

```python
@app.route('/')
def home():
    return "Page d'accueil"

@app.route('/about')
def about():
    return "À propos de nous"

@app.route('/contact')
def contact():
    return "Contactez-nous"
```

### Routes avec paramètres

Vous pouvez capturer des parties de l'URL comme paramètres :

```python
@app.route('/user/<username>')
def show_user(username):
    return f"Profil de l'utilisateur : {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Vous lisez l'article numéro {post_id}"
```

**Types de convertisseurs disponibles :**
- `<string:name>` : Chaîne de caractères (par défaut)
- `<int:id>` : Nombre entier
- `<float:price>` : Nombre décimal
- `<path:subpath>` : Chaîne acceptant les slashes
- `<uuid:identifier>` : UUID

### Routes avec plusieurs paramètres

```python
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f"Article {post_id} de {username}"
```

### Méthodes HTTP

Par défaut, les routes acceptent uniquement GET. Pour accepter d'autres méthodes :

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Traiter la connexion
        return "Connexion en cours..."
    else:
        # Afficher le formulaire
        return "Formulaire de connexion"
```

### URLs dynamiques avec url_for()

Flask fournit `url_for()` pour générer des URLs de manière dynamique :

```python
from flask import url_for

@app.route('/')
def index():
    # Génère l'URL de la fonction 'show_user'
    profile_url = url_for('show_user', username='alice')
    return f"URL du profil : {profile_url}"
```

**Avantage :** Si vous changez l'URL de votre route, tous les liens seront automatiquement mis à jour.

## Templates avec Jinja2

Les templates permettent de générer du HTML dynamique. Flask utilise **Jinja2**, un moteur de templates puissant.

### Structure des dossiers

Flask s'attend à trouver les templates dans un dossier `templates` :

```
mon_projet_flask/
│
├── app.py
└── templates/
    ├── index.html
    ├── about.html
    └── base.html
```

### Votre premier template

**templates/index.html :**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Ma première page Flask</title>
</head>
<body>
    <h1>Bonjour {{ nom }} !</h1>
    <p>Vous avez {{ age }} ans.</p>
</body>
</html>
```

**app.py :**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nom='Alice', age=25)
```

La fonction `render_template()` :
1. Charge le fichier HTML
2. Remplace les variables `{{ nom }}` et `{{ age }}`
3. Retourne le HTML final

### Variables dans les templates

Jinja2 utilise `{{ }}` pour afficher des variables :

```html
<h1>{{ titre }}</h1>
<p>{{ description }}</p>
<p>Prix : {{ prix }} €</p>
```

### Structures de contrôle

**Conditions :**
```html
{% if utilisateur_connecte %}
    <p>Bienvenue {{ nom_utilisateur }} !</p>
{% else %}
    <p>Veuillez vous connecter</p>
{% endif %}
```

**Boucles :**
```html
<ul>
{% for produit in produits %}
    <li>{{ produit.nom }} - {{ produit.prix }} €</li>
{% endfor %}
</ul>
```

### Template de base et héritage

Créez un template de base pour éviter la répétition :

**templates/base.html :**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mon Site{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Accueil</a>
        <a href="{{ url_for('about') }}">À propos</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 Mon Site</p>
    </footer>
</body>
</html>
```

**templates/index.html :**
```html
{% extends "base.html" %}

{% block title %}Accueil - Mon Site{% endblock %}

{% block content %}
    <h1>Bienvenue sur la page d'accueil</h1>
    <p>Ceci est le contenu de la page d'accueil.</p>
{% endblock %}
```

Le template `index.html` **hérite** de `base.html` et remplit les blocs définis.

### Filtres Jinja2

Les filtres modifient les variables :

```html
<!-- Mettre en majuscules -->
<h1>{{ titre|upper }}</h1>

<!-- Mettre en minuscules -->
<p>{{ description|lower }}</p>

<!-- Capitaliser -->
<p>{{ nom|capitalize }}</p>

<!-- Longueur -->
<p>{{ liste|length }} éléments</p>

<!-- Valeur par défaut -->
<p>{{ variable|default('Valeur par défaut') }}</p>

<!-- Arrondir -->
<p>{{ prix|round(2) }} €</p>

<!-- Formater une date (méthode de l'objet datetime) -->
<p>{{ date.strftime('%d/%m/%Y') }}</p>
```

## Gestion des données statiques

Les fichiers CSS, JavaScript, images sont appelés "fichiers statiques".

### Structure des dossiers

```
mon_projet_flask/
│
├── app.py
├── templates/
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

### Utiliser les fichiers statiques

Dans vos templates, utilisez `url_for('static', filename='...')` :

```html
<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- JavaScript -->
<script src="{{ url_for('static', filename='js/script.js') }}"></script>

<!-- Image -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

## Gestion des formulaires

Flask facilite le traitement des formulaires HTML.

### Formulaire simple

**templates/contact.html :**
```html
{% extends "base.html" %}

{% block content %}
<h1>Contactez-nous</h1>

<form method="POST" action="{{ url_for('contact') }}">
    <label for="nom">Nom :</label>
    <input type="text" id="nom" name="nom" required>

    <label for="email">Email :</label>
    <input type="email" id="email" name="email" required>

    <label for="message">Message :</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Envoyer</button>
</form>
{% endblock %}
```

**app.py :**
```python
from flask import Flask, render_template, request, redirect, url_for

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']

        # Traiter les données (sauvegarder en base, envoyer un email, etc.)
        print(f"Message de {nom} ({email}): {message}")

        # Rediriger vers une page de confirmation
        return redirect(url_for('merci'))

    # GET : afficher le formulaire
    return render_template('contact.html')

@app.route('/merci')
def merci():
    return "Merci pour votre message !"
```

### Objet request

L'objet `request` contient toutes les informations sur la requête :

```python
from flask import request

@app.route('/test')
def test():
    # Données du formulaire (POST)
    nom = request.form.get('nom')

    # Paramètres URL (GET: ?search=python)
    search = request.args.get('search')

    # Méthode HTTP
    method = request.method

    # Headers
    user_agent = request.headers.get('User-Agent')

    # IP du client
    ip = request.remote_addr

    # Cookies
    session_id = request.cookies.get('session_id')

    return "OK"
```

### Extension Flask-WTF pour les formulaires

Pour des formulaires plus complexes, utilisez l'extension Flask-WTF :

```bash
pip install Flask-WTF
```

**forms.py :**
```python
from flask_wtf import FlaskForm  
from wtforms import StringField, EmailField, TextAreaField, SubmitField  
from wtforms.validators import DataRequired, Email  

class ContactForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Envoyer')
```

**app.py :**
```python
from forms import ContactForm

app.config['SECRET_KEY'] = 'votre-clé-secrète-ici'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Formulaire valide
        nom = form.nom.data
        email = form.email.data
        message = form.message.data
        # Traiter les données...
        return redirect(url_for('merci'))

    return render_template('contact.html', form=form)
```

**templates/contact.html :**
```html
<form method="POST">
    {{ form.hidden_tag() }}

    {{ form.nom.label }}
    {{ form.nom() }}
    {% if form.nom.errors %}
        <ul>{% for error in form.nom.errors %}<li>{{ error }}</li>{% endfor %}</ul>
    {% endif %}

    {{ form.email.label }}
    {{ form.email() }}

    {{ form.message.label }}
    {{ form.message() }}

    {{ form.submit() }}
</form>
```

Flask-WTF gère automatiquement la validation et la protection CSRF !

## Sessions et Cookies

Les sessions permettent de stocker des données spécifiques à un utilisateur entre les requêtes.

### Utiliser les sessions

```python
from flask import Flask, session, redirect, url_for

app = Flask(__name__)  
app.secret_key = 'votre-clé-secrète-super-sécurisée'  

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    # Vérifier les identifiants...

    # Stocker dans la session
    session['username'] = username
    session['logged_in'] = True

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        username = session['username']
        return f"Tableau de bord de {username}"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Supprimer la session
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))
```

Les données de session sont stockées côté client dans un cookie sécurisé et signé.

## Messages flash

Les messages flash permettent d'afficher des messages ponctuels (confirmations, erreurs, etc.).

```python
from flask import flash, get_flashed_messages

@app.route('/action')
def action():
    # Différentes catégories de messages
    flash('Opération réussie !', 'success')
    flash('Attention : vérifiez vos données', 'warning')
    flash('Erreur lors du traitement', 'error')

    return redirect(url_for('index'))
```

**Dans votre template :**
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

## Blueprints : organiser votre code

Pour les applications plus grandes, les **blueprints** permettent d'organiser le code en modules.

### Structure avec blueprints

```
mon_projet_flask/
│
├── app.py
├── blueprints/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── login.html
│   └── blog/
│       ├── __init__.py
│       ├── routes.py
│       └── templates/
│           └── posts.html
└── templates/
    └── base.html
```

### Créer un blueprint

**blueprints/blog/routes.py :**
```python
from flask import Blueprint, render_template

# Créer le blueprint
blog_bp = Blueprint('blog', __name__,
                    template_folder='templates',
                    url_prefix='/blog')

@blog_bp.route('/')
def index():
    return render_template('posts.html')

@blog_bp.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Article {post_id}"
```

**blueprints/blog/__init__.py :**
```python
from .routes import blog_bp
```

### Enregistrer le blueprint

**app.py :**
```python
from flask import Flask  
from blueprints.blog import blog_bp  
from blueprints.auth import auth_bp  

app = Flask(__name__)

# Enregistrer les blueprints
app.register_blueprint(blog_bp)  
app.register_blueprint(auth_bp)  

@app.route('/')
def index():
    return "Page d'accueil principale"

if __name__ == '__main__':
    app.run(debug=True)
```

Les routes du blueprint `blog` seront accessibles via `/blog/`, `/blog/post/1`, etc.

## Bases de données avec Flask-SQLAlchemy

Flask-SQLAlchemy est l'extension la plus populaire pour gérer les bases de données.

### Installation

```bash
pip install Flask-SQLAlchemy
```

### Configuration

```python
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Créer l'instance SQLAlchemy
db = SQLAlchemy(app)
```

### Définir un modèle

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relation
    author = db.relationship('User', backref=db.backref('posts', lazy=True))
```

### Créer la base de données

```python
# Dans un shell Python ou dans votre app
with app.app_context():
    db.create_all()
```

### Opérations CRUD

**Create (Créer) :**
```python
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return "Utilisateur créé !"
```

**Read (Lire) :**
```python
@app.route('/users')
def users():
    # Tous les utilisateurs
    all_users = User.query.all()

    # Un utilisateur spécifique
    user = User.query.filter_by(username='alice').first()

    # Avec condition
    users = User.query.filter(User.id > 5).all()

    return render_template('users.html', users=all_users)
```

**Update (Mettre à jour) :**
```python
@app.route('/update-user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.email = request.form['new_email']
    db.session.commit()

    return "Utilisateur mis à jour !"
```

**Delete (Supprimer) :**
```python
@app.route('/delete-user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return "Utilisateur supprimé !"
```

### Relations entre modèles

```python
# Un utilisateur peut avoir plusieurs articles
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Utilisation
user = User.query.first()  
user_posts = user.posts  # Tous les articles de cet utilisateur  

post = Post.query.first()  
author_name = post.author.username  # Nom de l'auteur  
```

## Flask en mode API

Flask peut aussi servir d'API REST, comme FastAPI.

### API REST simple

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Données simulées
tasks = [
    {"id": 1, "title": "Apprendre Flask", "done": False},
    {"id": 2, "title": "Créer une API", "done": False}
]

# GET : Lire toutes les tâches
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# GET : Lire une tâche spécifique
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Tâche non trouvée"}), 404

# POST : Créer une tâche
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT : Mettre à jour une tâche
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Tâche non trouvée"}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task)

# DELETE : Supprimer une tâche
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Tâche supprimée"}), 200
```

### Extension Flask-RESTX

Pour des APIs plus complexes avec documentation automatique :

```bash
pip install flask-restx
```

```python
from flask import Flask  
from flask_restx import Api, Resource, fields  

app = Flask(__name__)  
api = Api(app, version='1.0', title='Mon API',  
          description='Une API créée avec Flask-RESTX')

# Namespace
ns = api.namespace('tasks', description='Opérations sur les tâches')

# Modèle de données
task_model = api.model('Task', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='Titre de la tâche'),
    'done': fields.Boolean(description='Tâche terminée ?')
})

tasks = []

@ns.route('/')
class TaskList(Resource):
    @ns.doc('list_tasks')
    @ns.marshal_list_with(task_model)
    def get(self):
        """Liste toutes les tâches"""
        return tasks

    @ns.doc('create_task')
    @ns.expect(task_model)
    @ns.marshal_with(task_model, code=201)
    def post(self):
        """Créer une nouvelle tâche"""
        return api.payload, 201

@ns.route('/<int:id>')
class Task(Resource):
    @ns.doc('get_task')
    @ns.marshal_with(task_model)
    def get(self, id):
        """Récupérer une tâche par son ID"""
        task = next((t for t in tasks if t['id'] == id), None)
        if task:
            return task
        api.abort(404, "Tâche non trouvée")
```

Flask-RESTX génère automatiquement une documentation Swagger, similaire à FastAPI !

## Gestion des erreurs

### Erreurs personnalisées

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Pour les APIs
@app.errorhandler(404)
def api_not_found(e):
    if request.path.startswith('/api/'):
        return jsonify({"error": "Ressource non trouvée"}), 404
    return render_template('404.html'), 404
```

### Exceptions personnalisées

```python
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response

# Utilisation
@app.route('/endpoint')
def endpoint():
    if condition_invalide:
        raise InvalidUsage("Données invalides", status_code=400)
```

## Configuration de Flask

### Différentes configurations

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clé-par-défaut'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# Utilisation
app.config.from_object(DevelopmentConfig)
```

### Variables d'environnement

```python
import os

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')  
```

## Comparaison Flask vs FastAPI

Maintenant que vous connaissez les deux, voici une comparaison :

| Aspect | Flask | FastAPI |
|--------|-------|---------|
| **Objectif principal** | Applications web & APIs | APIs modernes |
| **Facilité d'apprentissage** | Très facile | Facile |
| **Validation de données** | Manuelle (ou WTF-Forms) | Automatique (Pydantic) |
| **Documentation auto** | Non (sauf extensions) | Oui (Swagger/ReDoc) |
| **Performance** | Bonne | Excellente |
| **Async natif** | Non (extensions) | Oui |
| **Templates** | Oui (Jinja2) | Non (focalisé API) |
| **Type hints** | Optionnel | Essentiel |
| **Flexibilité** | Très élevée | Élevée |
| **Maturité** | Très mature (2010) | Récent (2018) |
| **Cas d'usage** | Sites web complets | APIs REST/GraphQL |

**Choisissez Flask si :**
- ✅ Vous voulez créer un site web avec templates HTML
- ✅ Vous préférez une approche simple et traditionnelle
- ✅ Vous voulez un contrôle total sur l'architecture
- ✅ Vous créez une application avec beaucoup de pages HTML

**Choisissez FastAPI si :**
- ✅ Vous créez principalement des APIs
- ✅ Vous voulez une validation automatique stricte
- ✅ Vous avez besoin de hautes performances
- ✅ Vous aimez la programmation asynchrone

## Extensions Flask populaires

Flask dispose d'un écosystème riche d'extensions :

### Pour les bases de données
- **Flask-SQLAlchemy** : ORM SQLAlchemy intégré
- **Flask-Migrate** : Migrations de base de données
- **Flask-MongoEngine** : MongoDB

### Pour l'authentification
- **Flask-Login** : Gestion des sessions utilisateur
- **Flask-JWT-Extended** : JSON Web Tokens
- **Flask-Security** : Sécurité complète

### Pour les APIs
- **Flask-RESTX** : APIs REST avec documentation
- **Flask-RESTful** : Extension REST simple
- **Flask-CORS** : Gestion CORS

### Pour les formulaires
- **Flask-WTF** : Intégration WTForms
- **Flask-Uploads** : Upload de fichiers

### Utilitaires
- **Flask-Mail** : Envoi d'emails
- **Flask-Caching** : Mise en cache
- **Flask-SocketIO** : WebSockets en temps réel
- **Flask-Admin** : Interface d'administration

## Bonnes pratiques Flask

### 1. Structure de projet

Pour un projet moyen/grand :
```
mon_projet/
│
├── app/
│   ├── __init__.py          # Créer l'app
│   ├── models.py            # Modèles de données
│   ├── routes.py            # Routes principales
│   ├── forms.py             # Formulaires
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       └── ...
├── migrations/              # Migrations de DB
├── tests/                   # Tests
├── config.py               # Configuration
├── requirements.txt        # Dépendances
└── run.py                  # Point d'entrée
```

### 2. Factory Pattern

Utilisez le pattern Application Factory pour plus de flexibilité :

```python
# app/__init__.py
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app

# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
```

### 3. Sécurité

```python
# Ne jamais hardcoder les secrets
app.secret_key = os.environ.get('SECRET_KEY')

# Utiliser HTTPS en production
if not app.debug:
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True

# Protection CSRF avec Flask-WTF
from flask_wtf.csrf import CSRFProtect  
csrf = CSRFProtect(app)  

# Headers de sécurité
from flask_talisman import Talisman  
Talisman(app)  
```

### 4. Logging

```python
import logging  
from logging.handlers import RotatingFileHandler  

if not app.debug:
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Application startup')
```

### 5. Tests

```python
import unittest  
from app import create_app, db  

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```

## Déploiement Flask

### Serveur de production

En production, n'utilisez pas `app.run()`. Utilisez un serveur WSGI comme Gunicorn :

```bash
pip install gunicorn
```

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

- `-w 4` : 4 workers (processus)
- `-b 0.0.0.0:8000` : Écoute sur tous les interfaces, port 8000
- `app:app` : Module et variable de l'application

### Avec Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .  
RUN pip install -r requirements.txt  

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

### Variables d'environnement

Créez un fichier `.env` :
```
SECRET_KEY=votre-clé-secrète  
DATABASE_URL=postgresql://user:pass@localhost/db  
FLASK_ENV=production  
```

Chargez-le avec `python-dotenv` :
```python
from dotenv import load_dotenv  
load_dotenv()  
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ Ce qu'est Flask et pourquoi il est populaire  
✅ Comment installer et créer votre première application  
✅ Le système de routing et les URLs dynamiques  
✅ Les templates Jinja2 et l'héritage de templates  
✅ La gestion des fichiers statiques (CSS, JS, images)  
✅ Le traitement des formulaires avec et sans extensions  
✅ Les sessions et cookies  
✅ L'organisation du code avec les blueprints  
✅ L'intégration de bases de données avec SQLAlchemy  
✅ La création d'APIs REST avec Flask  
✅ La gestion des erreurs  
✅ Les bonnes pratiques et le déploiement

Flask est un excellent framework pour apprendre les concepts du développement web grâce à sa simplicité et sa flexibilité. Une fois que vous maîtrisez Flask, vous avez une base solide pour explorer d'autres frameworks ou créer vos propres applications web !

---


⏭️ [Requêtes HTTP avec requests](/11-developpement-web-et-apis/04-requetes-http-requests.md)
