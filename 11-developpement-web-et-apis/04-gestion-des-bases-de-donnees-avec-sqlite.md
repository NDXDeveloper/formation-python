🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 11.4 : Gestion des bases de données avec SQLite

## Introduction

Une base de données est comme un classeur géant et intelligent qui stocke et organise vos données de manière structurée. SQLite est parfait pour débuter : c'est une base de données légère, sans serveur, qui stocke tout dans un simple fichier.

Dans cette section, nous allons apprendre à intégrer SQLite dans nos applications web Flask pour remplacer nos listes Python temporaires par un stockage permanent et fiable.

## Qu'est-ce que SQLite ?

### Avantages de SQLite

- **Simple** : Pas de serveur à configurer, tout dans un fichier
- **Léger** : Parfait pour le développement et les petites applications
- **Fiable** : Transactions ACID, gestion des erreurs
- **Standard** : Utilise le langage SQL standard
- **Intégré** : Inclus dans Python par défaut

### Concepts de base

**Table** : Comme une feuille Excel avec des colonnes et des lignes
```
Table "utilisateurs"
┌────┬─────────┬──────────┬─────────────────────┐
│ id │ nom     │ prenom   │ email               │
├────┼─────────┼──────────┼─────────────────────┤
│ 1  │ Dupont  │ Jean     │ jean@email.com      │
│ 2  │ Martin  │ Marie    │ marie@email.com     │
└────┴─────────┴──────────┴─────────────────────┘
```

**SQL** : Langage pour communiquer avec la base de données
- `SELECT` : lire des données
- `INSERT` : ajouter des données
- `UPDATE` : modifier des données
- `DELETE` : supprimer des données

## Premiers pas avec SQLite en Python

### Import et connexion

```python
import sqlite3
from datetime import datetime

# Se connecter à la base de données (crée le fichier s'il n'existe pas)
conn = sqlite3.connect('ma_base.db')

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Toujours fermer la connexion à la fin
conn.close()
```

### Création d'une table

```python
import sqlite3

def creer_base_donnees():
    """Crée la base de données et les tables"""

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    # Créer la table utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Créer la table articles
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            contenu TEXT NOT NULL,
            auteur_id INTEGER NOT NULL,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            publie BOOLEAN DEFAULT 1,
            FOREIGN KEY (auteur_id) REFERENCES utilisateurs (id)
        )
    ''')

    # Sauvegarder les changements
    conn.commit()
    conn.close()

    print("✅ Base de données créée avec succès")

# Créer la base
creer_base_donnees()
```

### Insertion de données

```python
import sqlite3

def ajouter_utilisateur(nom, prenom, email, age=None):
    """Ajoute un nouvel utilisateur"""

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO utilisateurs (nom, prenom, email, age)
            VALUES (?, ?, ?, ?)
        ''', (nom, prenom, email, age))

        # Récupérer l'ID du nouvel utilisateur
        user_id = cursor.lastrowid

        conn.commit()
        print(f"✅ Utilisateur ajouté avec l'ID {user_id}")
        return user_id

    except sqlite3.IntegrityError as e:
        print(f"❌ Erreur : {e}")
        return None
    finally:
        conn.close()

# Exemples d'utilisation
ajouter_utilisateur("Dupont", "Jean", "jean.dupont@email.com", 25)
ajouter_utilisateur("Martin", "Marie", "marie.martin@email.com", 30)
ajouter_utilisateur("Durand", "Pierre", "pierre.durand@email.com")
```

### Lecture de données

```python
import sqlite3

def obtenir_tous_utilisateurs():
    """Récupère tous les utilisateurs"""

    conn = sqlite3.connect('blog.db')
    # Configurer pour avoir des dictionnaires au lieu de tuples
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM utilisateurs ORDER BY date_creation DESC')
    utilisateurs = cursor.fetchall()

    conn.close()

    # Convertir en liste de dictionnaires
    return [dict(user) for user in utilisateurs]

def obtenir_utilisateur_par_id(user_id):
    """Récupère un utilisateur par son ID"""

    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM utilisateurs WHERE id = ?', (user_id,))
    utilisateur = cursor.fetchone()

    conn.close()

    return dict(utilisateur) if utilisateur else None

def rechercher_utilisateurs(terme):
    """Recherche des utilisateurs par nom, prénom ou email"""

    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Utiliser LIKE pour une recherche partielle
    cursor.execute('''
        SELECT * FROM utilisateurs
        WHERE nom LIKE ? OR prenom LIKE ? OR email LIKE ?
        ORDER BY nom, prenom
    ''', (f'%{terme}%', f'%{terme}%', f'%{terme}%'))

    utilisateurs = cursor.fetchall()
    conn.close()

    return [dict(user) for user in utilisateurs]

# Tests
print("📋 Tous les utilisateurs :")
for user in obtenir_tous_utilisateurs():
    print(f"   {user['prenom']} {user['nom']} - {user['email']}")

print("\n🔍 Recherche 'Martin' :")
for user in rechercher_utilisateurs('Martin'):
    print(f"   {user['prenom']} {user['nom']}")
```

### Modification et suppression

```python
import sqlite3

def modifier_utilisateur(user_id, **modifications):
    """Modifie un utilisateur"""

    if not modifications:
        print("❌ Aucune modification spécifiée")
        return False

    # Construire la requête dynamiquement
    champs = []
    valeurs = []

    for champ, valeur in modifications.items():
        if champ in ['nom', 'prenom', 'email', 'age']:
            champs.append(f'{champ} = ?')
            valeurs.append(valeur)

    if not champs:
        print("❌ Aucun champ valide à modifier")
        return False

    valeurs.append(user_id)  # Pour la clause WHERE

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    try:
        requete = f"UPDATE utilisateurs SET {', '.join(champs)} WHERE id = ?"
        cursor.execute(requete, valeurs)

        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Utilisateur {user_id} modifié")
            return True
        else:
            print(f"❌ Utilisateur {user_id} non trouvé")
            return False

    except sqlite3.IntegrityError as e:
        print(f"❌ Erreur : {e}")
        return False
    finally:
        conn.close()

def supprimer_utilisateur(user_id):
    """Supprime un utilisateur"""

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    # Vérifier d'abord si l'utilisateur existe
    cursor.execute('SELECT nom, prenom FROM utilisateurs WHERE id = ?', (user_id,))
    utilisateur = cursor.fetchone()

    if not utilisateur:
        print(f"❌ Utilisateur {user_id} non trouvé")
        conn.close()
        return False

    try:
        cursor.execute('DELETE FROM utilisateurs WHERE id = ?', (user_id,))
        conn.commit()
        print(f"✅ Utilisateur {utilisateur[1]} {utilisateur[0]} supprimé")
        return True

    except sqlite3.Error as e:
        print(f"❌ Erreur lors de la suppression : {e}")
        return False
    finally:
        conn.close()

# Tests
modifier_utilisateur(1, age=26, email="jean.nouveau@email.com")
# supprimer_utilisateur(3)
```

## Intégration avec Flask

### Gestionnaire de base de données

```python
import sqlite3
from flask import g, Flask
import os

app = Flask(__name__)

# Configuration
DATABASE = 'app.db'

def get_db():
    """Obtient une connexion à la base de données"""
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Pour avoir des dictionnaires
    return g.db

def close_db(error=None):
    """Ferme la connexion à la base de données"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.teardown_appcontext
def close_db(error):
    """Ferme automatiquement la DB à la fin de chaque requête"""
    close_db()

def init_db():
    """Initialise la base de données"""
    db = get_db()

    # Créer les tables
    db.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    db.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            contenu TEXT NOT NULL,
            auteur_id INTEGER NOT NULL,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            publie BOOLEAN DEFAULT 1,
            FOREIGN KEY (auteur_id) REFERENCES utilisateurs (id)
        )
    ''')

    db.commit()

# Initialiser la DB au démarrage
with app.app_context():
    init_db()
```

### Modèles de données (classes)

```python
from flask import g
import sqlite3

class Utilisateur:
    """Modèle pour gérer les utilisateurs"""

    def __init__(self, id=None, nom=None, prenom=None, email=None, age=None, date_creation=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.age = age
        self.date_creation = date_creation

    @classmethod
    def creer(cls, nom, prenom, email, age=None):
        """Crée un nouvel utilisateur"""
        db = get_db()

        try:
            cursor = db.execute('''
                INSERT INTO utilisateurs (nom, prenom, email, age)
                VALUES (?, ?, ?, ?)
            ''', (nom, prenom, email, age))

            db.commit()

            # Récupérer l'utilisateur créé
            return cls.obtenir_par_id(cursor.lastrowid)

        except sqlite3.IntegrityError:
            return None

    @classmethod
    def obtenir_par_id(cls, user_id):
        """Récupère un utilisateur par ID"""
        db = get_db()

        row = db.execute(
            'SELECT * FROM utilisateurs WHERE id = ?', (user_id,)
        ).fetchone()

        if row:
            return cls(
                id=row['id'],
                nom=row['nom'],
                prenom=row['prenom'],
                email=row['email'],
                age=row['age'],
                date_creation=row['date_creation']
            )
        return None

    @classmethod
    def obtenir_tous(cls):
        """Récupère tous les utilisateurs"""
        db = get_db()

        rows = db.execute(
            'SELECT * FROM utilisateurs ORDER BY date_creation DESC'
        ).fetchall()

        return [cls(
            id=row['id'],
            nom=row['nom'],
            prenom=row['prenom'],
            email=row['email'],
            age=row['age'],
            date_creation=row['date_creation']
        ) for row in rows]

    def sauvegarder(self):
        """Sauvegarde les modifications"""
        db = get_db()

        if self.id:
            # Mise à jour
            db.execute('''
                UPDATE utilisateurs
                SET nom = ?, prenom = ?, email = ?, age = ?
                WHERE id = ?
            ''', (self.nom, self.prenom, self.email, self.age, self.id))
        else:
            # Création
            cursor = db.execute('''
                INSERT INTO utilisateurs (nom, prenom, email, age)
                VALUES (?, ?, ?, ?)
            ''', (self.nom, self.prenom, self.email, self.age))
            self.id = cursor.lastrowid

        db.commit()
        return True

    def supprimer(self):
        """Supprime l'utilisateur"""
        if not self.id:
            return False

        db = get_db()
        db.execute('DELETE FROM utilisateurs WHERE id = ?', (self.id,))
        db.commit()
        return True

    def to_dict(self):
        """Convertit en dictionnaire"""
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'age': self.age,
            'date_creation': self.date_creation
        }

    def __repr__(self):
        return f"<Utilisateur {self.prenom} {self.nom}>"

class Article:
    """Modèle pour gérer les articles"""

    def __init__(self, id=None, titre=None, contenu=None, auteur_id=None,
                 date_creation=None, publie=True):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.auteur_id = auteur_id
        self.date_creation = date_creation
        self.publie = publie

    @classmethod
    def creer(cls, titre, contenu, auteur_id):
        """Crée un nouvel article"""
        db = get_db()

        cursor = db.execute('''
            INSERT INTO articles (titre, contenu, auteur_id)
            VALUES (?, ?, ?)
        ''', (titre, contenu, auteur_id))

        db.commit()
        return cls.obtenir_par_id(cursor.lastrowid)

    @classmethod
    def obtenir_par_id(cls, article_id):
        """Récupère un article par ID"""
        db = get_db()

        row = db.execute(
            'SELECT * FROM articles WHERE id = ?', (article_id,)
        ).fetchone()

        if row:
            return cls(
                id=row['id'],
                titre=row['titre'],
                contenu=row['contenu'],
                auteur_id=row['auteur_id'],
                date_creation=row['date_creation'],
                publie=row['publie']
            )
        return None

    @classmethod
    def obtenir_tous(cls, publies_seulement=True):
        """Récupère tous les articles"""
        db = get_db()

        if publies_seulement:
            requete = '''
                SELECT a.*, u.nom, u.prenom
                FROM articles a
                JOIN utilisateurs u ON a.auteur_id = u.id
                WHERE a.publie = 1
                ORDER BY a.date_creation DESC
            '''
        else:
            requete = '''
                SELECT a.*, u.nom, u.prenom
                FROM articles a
                JOIN utilisateurs u ON a.auteur_id = u.id
                ORDER BY a.date_creation DESC
            '''

        rows = db.execute(requete).fetchall()

        articles = []
        for row in rows:
            article = cls(
                id=row['id'],
                titre=row['titre'],
                contenu=row['contenu'],
                auteur_id=row['auteur_id'],
                date_creation=row['date_creation'],
                publie=row['publie']
            )
            # Ajouter les informations de l'auteur
            article.auteur_nom = row['nom']
            article.auteur_prenom = row['prenom']
            articles.append(article)

        return articles

    def obtenir_auteur(self):
        """Récupère l'auteur de l'article"""
        return Utilisateur.obtenir_par_id(self.auteur_id)

    def to_dict(self):
        """Convertit en dictionnaire"""
        data = {
            'id': self.id,
            'titre': self.titre,
            'contenu': self.contenu,
            'auteur_id': self.auteur_id,
            'date_creation': self.date_creation,
            'publie': self.publie
        }

        # Ajouter les infos auteur si disponibles
        if hasattr(self, 'auteur_nom'):
            data['auteur'] = f"{self.auteur_prenom} {self.auteur_nom}"

        return data
```

### API Flask avec SQLite

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# ... (code de connexion DB et modèles ci-dessus) ...

@app.route('/api/utilisateurs', methods=['GET'])
def obtenir_utilisateurs():
    """Liste tous les utilisateurs"""

    # Paramètres de pagination
    page = request.args.get('page', 1, type=int)
    limite = request.args.get('limit', 10, type=int)
    recherche = request.args.get('search', '', type=str)

    utilisateurs = Utilisateur.obtenir_tous()

    # Filtrer par recherche si spécifiée
    if recherche:
        utilisateurs = [
            u for u in utilisateurs
            if recherche.lower() in u.nom.lower()
            or recherche.lower() in u.prenom.lower()
            or recherche.lower() in u.email.lower()
        ]

    # Pagination simple
    debut = (page - 1) * limite
    fin = debut + limite
    utilisateurs_page = utilisateurs[debut:fin]

    return jsonify({
        'success': True,
        'data': [u.to_dict() for u in utilisateurs_page],
        'pagination': {
            'page': page,
            'limit': limite,
            'total': len(utilisateurs),
            'pages': (len(utilisateurs) + limite - 1) // limite
        }
    })

@app.route('/api/utilisateurs/<int:user_id>', methods=['GET'])
def obtenir_utilisateur(user_id):
    """Récupère un utilisateur spécifique"""

    utilisateur = Utilisateur.obtenir_par_id(user_id)

    if not utilisateur:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

    return jsonify({
        'success': True,
        'data': utilisateur.to_dict()
    })

@app.route('/api/utilisateurs', methods=['POST'])
def creer_utilisateur():
    """Crée un nouvel utilisateur"""

    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Données manquantes'
        }), 400

    # Validation
    champs_requis = ['nom', 'prenom', 'email']
    for champ in champs_requis:
        if champ not in donnees or not donnees[champ]:
            return jsonify({
                'success': False,
                'error': f'{champ} requis'
            }), 400

    # Créer l'utilisateur
    utilisateur = Utilisateur.creer(
        nom=donnees['nom'],
        prenom=donnees['prenom'],
        email=donnees['email'],
        age=donnees.get('age')
    )

    if not utilisateur:
        return jsonify({
            'success': False,
            'error': 'Email déjà utilisé'
        }), 400

    return jsonify({
        'success': True,
        'data': utilisateur.to_dict(),
        'message': 'Utilisateur créé avec succès'
    }), 201

@app.route('/api/utilisateurs/<int:user_id>', methods=['PUT'])
def modifier_utilisateur(user_id):
    """Modifie un utilisateur"""

    utilisateur = Utilisateur.obtenir_par_id(user_id)

    if not utilisateur:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Données manquantes'
        }), 400

    # Mettre à jour les champs fournis
    if 'nom' in donnees:
        utilisateur.nom = donnees['nom']
    if 'prenom' in donnees:
        utilisateur.prenom = donnees['prenom']
    if 'email' in donnees:
        utilisateur.email = donnees['email']
    if 'age' in donnees:
        utilisateur.age = donnees['age']

    try:
        utilisateur.sauvegarder()
        return jsonify({
            'success': True,
            'data': utilisateur.to_dict(),
            'message': 'Utilisateur modifié avec succès'
        })
    except sqlite3.IntegrityError:
        return jsonify({
            'success': False,
            'error': 'Email déjà utilisé'
        }), 400

@app.route('/api/utilisateurs/<int:user_id>', methods=['DELETE'])
def supprimer_utilisateur(user_id):
    """Supprime un utilisateur"""

    utilisateur = Utilisateur.obtenir_par_id(user_id)

    if not utilisateur:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

    nom_complet = f"{utilisateur.prenom} {utilisateur.nom}"

    if utilisateur.supprimer():
        return jsonify({
            'success': True,
            'message': f'Utilisateur {nom_complet} supprimé avec succès'
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Erreur lors de la suppression'
        }), 500

@app.route('/api/articles', methods=['GET'])
def obtenir_articles():
    """Liste tous les articles"""

    articles = Article.obtenir_tous()

    return jsonify({
        'success': True,
        'data': [a.to_dict() for a in articles],
        'count': len(articles)
    })

@app.route('/api/articles', methods=['POST'])
def creer_article():
    """Crée un nouvel article"""

    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Données manquantes'
        }), 400

    # Validation
    champs_requis = ['titre', 'contenu', 'auteur_id']
    for champ in champs_requis:
        if champ not in donnees:
            return jsonify({
                'success': False,
                'error': f'{champ} requis'
            }), 400

    # Vérifier que l'auteur existe
    auteur = Utilisateur.obtenir_par_id(donnees['auteur_id'])
    if not auteur:
        return jsonify({
            'success': False,
            'error': 'Auteur non trouvé'
        }), 400

    # Créer l'article
    article = Article.creer(
        titre=donnees['titre'],
        contenu=donnees['contenu'],
        auteur_id=donnees['auteur_id']
    )

    return jsonify({
        'success': True,
        'data': article.to_dict(),
        'message': 'Article créé avec succès'
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
```

## Requêtes SQL avancées

### Jointures

```python
def obtenir_articles_avec_auteurs():
    """Récupère les articles avec les informations des auteurs"""

    db = get_db()

    cursor = db.execute('''
        SELECT
            a.id,
            a.titre,
            a.contenu,
            a.date_creation,
            u.nom as auteur_nom,
            u.prenom as auteur_prenom,
            u.email as auteur_email
        FROM articles a
        INNER JOIN utilisateurs u ON a.auteur_id = u.id
        WHERE a.publie = 1
        ORDER BY a.date_creation DESC
    ''')

    articles = []
    for row in cursor.fetchall():
        articles.append({
            'id': row['id'],
            'titre': row['titre'],
            'contenu': row['contenu'][:200] + '...',  # Aperçu
            'date_creation': row['date_creation'],
            'auteur': {
                'nom': row['auteur_nom'],
                'prenom': row['auteur_prenom'],
                'email': row['auteur_email']
            }
        })

    return articles
```

### Agrégations et statistiques

```python
def obtenir_statistiques():
    """Calcule diverses statistiques"""

    db = get_db()

    # Nombre d'articles par auteur
    cursor = db.execute('''
        SELECT
            u.nom,
            u.prenom,
            COUNT(a.id) as nb_articles
        FROM utilisateurs u
        LEFT JOIN articles a ON u.id = a.auteur_id
        GROUP BY u.id, u.nom, u.prenom
        ORDER BY nb_articles DESC
    ''')

    stats_auteurs = [
        {
            'auteur': f"{row['prenom']} {row['nom']}",
            'nb_articles': row['nb_articles']
        }
        for row in cursor.fetchall()
    ]

    # Articles par mois
    cursor = db.execute('''
        SELECT
            strftime('%Y-%m', date_creation) as mois,
            COUNT(*) as nb_articles
        FROM articles
        WHERE publie = 1
        GROUP BY strftime('%Y-%m', date_creation)
        ORDER BY mois DESC
        LIMIT 12
    ''')

    articles_par_mois = [
        {
            'mois': row['mois'],
            'nb_articles': row['nb_articles']
        }
        for row in cursor.fetchall()
    ]

    # Totaux généraux
    cursor = db.execute('''
        SELECT
            (SELECT COUNT(*) FROM utilisateurs) as total_utilisateurs,
            (SELECT COUNT(*) FROM articles WHERE publie = 1) as total_articles_publies,
            (SELECT COUNT(*) FROM articles WHERE publie = 0) as total_brouillons
    ''')

    totaux = dict(cursor.fetchone())

    return {
        'totaux': totaux,
        'articles_par_auteur': stats_auteurs,
        'articles_par_mois': articles_par_mois
    }
```

### Recherche textuelle

```python
def rechercher_contenu(terme):
    """Recherche dans les titres et contenus d'articles"""

    db = get_db()

    cursor = db.execute('''
        SELECT
            a.id,
            a.titre,
            a.contenu,
            u.nom as auteur_nom,
            u.prenom as auteur_prenom,
            -- Calculer la pertinence (simple)
            CASE
                WHEN a.titre LIKE ? THEN 3
                WHEN a.contenu LIKE ? THEN 1
                ELSE 0
            END as pertinence
        FROM articles a
        INNER JOIN utilisateurs u ON a.auteur_id = u.id
        WHERE a.publie = 1
        AND (a.titre LIKE ? OR a.contenu LIKE ?)
        ORDER BY pertinence DESC, a.date_creation DESC
    ''', (f'%{terme}%', f'%{terme}%', f'%{terme}%', f'%{terme}%'))

    resultats = []
    for row in cursor.fetchall():
        # Extraire un aperçu avec le terme mis en évidence
        contenu = row['contenu']
        index = contenu.lower().find(terme.lower())

        if index != -1:
            debut = max(0, index - 50)
            fin = min(len(contenu), index + 100)
            apercu = contenu[debut:fin]
            if debut > 0:
                apercu = "..." + apercu
            if fin < len(contenu):
                apercu = apercu + "..."
        else:
            apercu = contenu[:150] + "..."

        resultats.append({
            'id': row['id'],
            'titre': row['titre'],
            'apercu': apercu,
            'auteur': f"{row['auteur_prenom']} {row['auteur_nom']}",
            'pertinence': row['pertinence']
        })

    return resultats

# Test de la recherche
resultats = rechercher_contenu("Python")
for resultat in resultats:
    print(f"📄 {resultat['titre']} - {resultat['auteur']}")
    print(f"   {resultat['apercu']}")
    print(f"   Pertinence: {resultat['pertinence']}")
```

## Transactions et gestion d'erreurs

### Transactions simples

```python
import sqlite3

def transferer_articles(ancien_auteur_id, nouveau_auteur_id):
    """Transfère tous les articles d'un auteur à un autre"""

    conn = sqlite3.connect('blog.db')

    try:
        # Démarrer une transaction
        conn.execute('BEGIN TRANSACTION')

        # Vérifier que les deux auteurs existent
        cursor = conn.execute('SELECT COUNT(*) FROM utilisateurs WHERE id IN (?, ?)',
                             (ancien_auteur_id, nouveau_auteur_id))
        if cursor.fetchone()[0] != 2:
            raise ValueError("Un des auteurs n'existe pas")

        # Compter les articles à transférer
        cursor = conn.execute('SELECT COUNT(*) FROM articles WHERE auteur_id = ?',
                             (ancien_auteur_id,))
        nb_articles = cursor.fetchone()[0]

        if nb_articles == 0:
            print("Aucun article à transférer")
            conn.rollback()
            return False

        # Effectuer le transfert
        conn.execute('UPDATE articles SET auteur_id = ? WHERE auteur_id = ?',
                    (nouveau_auteur_id, ancien_auteur_id))

        # Valider la transaction
        conn.commit()
        print(f"✅ {nb_articles} article(s) transféré(s) avec succès")
        return True

    except Exception as e:
        # Annuler en cas d'erreur
        conn.rollback()
        print(f"❌ Erreur lors du transfert : {e}")
        return False
    finally:
        conn.close()

# Test
# transferer_articles(1, 2)
```

### Gestion avancée des erreurs

```python
import sqlite3
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Gestionnaire de base de données avec gestion d'erreurs avancée"""

    def __init__(self, db_path='app.db'):
        self.db_path = db_path

    def executer_avec_retry(self, operation, *args, max_tentatives=3):
        """Exécute une opération avec retry automatique"""

        for tentative in range(max_tentatives):
            try:
                conn = sqlite3.connect(self.db_path)
                conn.row_factory = sqlite3.Row

                try:
                    resultat = operation(conn, *args)
                    conn.commit()
                    return resultat
                except Exception as e:
                    conn.rollback()
                    raise e
                finally:
                    conn.close()

            except sqlite3.OperationalError as e:
                if "database is locked" in str(e) and tentative < max_tentatives - 1:
                    logger.warning(f"Base verrouillée, tentative {tentative + 1}/{max_tentatives}")
                    time.sleep(0.1 * (2 ** tentative))  # Backoff exponentiel
                    continue
                else:
                    logger.error(f"Erreur opérationnelle : {e}")
                    raise
            except sqlite3.IntegrityError as e:
                logger.error(f"Erreur d'intégrité : {e}")
                raise
            except Exception as e:
                logger.error(f"Erreur inattendue : {e}")
                raise

        raise sqlite3.OperationalError("Nombre maximum de tentatives atteint")

    def creer_utilisateur_securise(self, nom, prenom, email, age=None):
        """Crée un utilisateur avec gestion d'erreurs complète"""

        def operation(conn, nom, prenom, email, age):
            # Validation des données
            if not nom or len(nom.strip()) < 2:
                raise ValueError("Le nom doit contenir au moins 2 caractères")

            if not prenom or len(prenom.strip()) < 2:
                raise ValueError("Le prénom doit contenir au moins 2 caractères")

            if not email or '@' not in email:
                raise ValueError("Email invalide")

            if age is not None and (age < 0 or age > 120):
                raise ValueError("Âge invalide")

            # Vérifier l'unicité de l'email
            cursor = conn.execute('SELECT id FROM utilisateurs WHERE email = ?', (email,))
            if cursor.fetchone():
                raise ValueError("Cet email est déjà utilisé")

            # Créer l'utilisateur
            cursor = conn.execute('''
                INSERT INTO utilisateurs (nom, prenom, email, age)
                VALUES (?, ?, ?, ?)
            ''', (nom.strip(), prenom.strip(), email.strip().lower(), age))

            # Récupérer l'utilisateur créé
            cursor = conn.execute('SELECT * FROM utilisateurs WHERE id = ?', (cursor.lastrowid,))
            return dict(cursor.fetchone())

        try:
            return self.executer_avec_retry(operation, nom, prenom, email, age)
        except ValueError as e:
            logger.warning(f"Données invalides : {e}")
            return {'error': str(e)}
        except Exception as e:
            logger.error(f"Erreur lors de la création : {e}")
            return {'error': 'Erreur interne'}

# Utilisation
db_manager = DatabaseManager()
resultat = db_manager.creer_utilisateur_securise("Doe", "John", "john.doe@email.com", 30)

if 'error' in resultat:
    print(f"❌ {resultat['error']}")
else:
    print(f"✅ Utilisateur créé : {resultat['prenom']} {resultat['nom']}")
```

## Migration et évolution de schéma

### Système de migrations

```python
import sqlite3
import os
from datetime import datetime

class MigrationManager:
    """Gestionnaire de migrations de base de données"""

    def __init__(self, db_path='app.db'):
        self.db_path = db_path
        self.migrations_dir = 'migrations'
        self._ensure_migrations_table()

    def _ensure_migrations_table(self):
        """Crée la table des migrations si elle n'existe pas"""
        conn = sqlite3.connect(self.db_path)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT UNIQUE NOT NULL,
                description TEXT,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def get_current_version(self):
        """Récupère la version actuelle de la base"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            'SELECT version FROM migrations ORDER BY executed_at DESC LIMIT 1'
        )
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def execute_migration(self, version, description, sql_commands):
        """Exécute une migration"""
        conn = sqlite3.connect(self.db_path)

        try:
            conn.execute('BEGIN TRANSACTION')

            # Vérifier que cette migration n'a pas déjà été exécutée
            cursor = conn.execute('SELECT 1 FROM migrations WHERE version = ?', (version,))
            if cursor.fetchone():
                print(f"⚠️ Migration {version} déjà exécutée")
                conn.rollback()
                return False

            # Exécuter les commandes SQL
            for sql in sql_commands:
                conn.execute(sql)

            # Enregistrer la migration
            conn.execute('''
                INSERT INTO migrations (version, description)
                VALUES (?, ?)
            ''', (version, description))

            conn.commit()
            print(f"✅ Migration {version} exécutée : {description}")
            return True

        except Exception as e:
            conn.rollback()
            print(f"❌ Erreur lors de la migration {version} : {e}")
            return False
        finally:
            conn.close()

# Exemple de migrations
def run_migrations():
    """Exécute toutes les migrations nécessaires"""

    manager = MigrationManager()
    current_version = manager.get_current_version()

    print(f"Version actuelle : {current_version or 'Aucune'}")

    # Migration 1: Création des tables de base
    if not current_version:
        manager.execute_migration(
            version='001_initial',
            description='Création des tables utilisateurs et articles',
            sql_commands=[
                '''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''',
                '''CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titre TEXT NOT NULL,
                    contenu TEXT NOT NULL,
                    auteur_id INTEGER NOT NULL,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (auteur_id) REFERENCES utilisateurs (id)
                )'''
            ]
        )

    # Migration 2: Ajout de la colonne âge
    if current_version in [None, '001_initial']:
        manager.execute_migration(
            version='002_add_age',
            description='Ajout de la colonne âge aux utilisateurs',
            sql_commands=[
                'ALTER TABLE utilisateurs ADD COLUMN age INTEGER'
            ]
        )

    # Migration 3: Ajout de la colonne publié
    if current_version in [None, '001_initial', '002_add_age']:
        manager.execute_migration(
            version='003_add_published',
            description='Ajout de la colonne publie aux articles',
            sql_commands=[
                'ALTER TABLE articles ADD COLUMN publie BOOLEAN DEFAULT 1'
            ]
        )

    # Migration 4: Ajout d'une table de commentaires
    if current_version in [None, '001_initial', '002_add_age', '003_add_published']:
        manager.execute_migration(
            version='004_add_comments',
            description='Création de la table commentaires',
            sql_commands=[
                '''CREATE TABLE IF NOT EXISTS commentaires (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    article_id INTEGER NOT NULL,
                    auteur_nom TEXT NOT NULL,
                    contenu TEXT NOT NULL,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (article_id) REFERENCES articles (id) ON DELETE CASCADE
                )''',
                'CREATE INDEX idx_commentaires_article ON commentaires(article_id)'
            ]
        )

# Exécuter les migrations
run_migrations()
```

## Optimisation et performance

### Index pour améliorer les performances

```python
def creer_index_optimisation():
    """Crée des index pour optimiser les requêtes courantes"""

    conn = sqlite3.connect('blog.db')

    try:
        # Index sur l'email des utilisateurs (recherche fréquente)
        conn.execute('CREATE INDEX IF NOT EXISTS idx_utilisateurs_email ON utilisateurs(email)')

        # Index sur l'auteur des articles
        conn.execute('CREATE INDEX IF NOT EXISTS idx_articles_auteur ON articles(auteur_id)')

        # Index composé pour les articles publiés, triés par date
        conn.execute('CREATE INDEX IF NOT EXISTS idx_articles_publie_date ON articles(publie, date_creation DESC)')

        # Index pour la recherche textuelle
        conn.execute('CREATE INDEX IF NOT EXISTS idx_articles_titre ON articles(titre)')

        # Index pour les commentaires par article
        conn.execute('CREATE INDEX IF NOT EXISTS idx_commentaires_article ON commentaires(article_id)')

        conn.commit()
        print("✅ Index créés pour optimiser les performances")

    except Exception as e:
        print(f"❌ Erreur lors de la création des index : {e}")
    finally:
        conn.close()

creer_index_optimisation()
```

### Analyse des performances

```python
def analyser_performances_requete(requete, params=None):
    """Analyse les performances d'une requête SQL"""

    conn = sqlite3.connect('blog.db')

    try:
        # Activer l'analyse des requêtes
        conn.execute('PRAGMA query_log = ON')

        # Analyser le plan d'exécution
        if params:
            plan = conn.execute(f'EXPLAIN QUERY PLAN {requete}', params).fetchall()
        else:
            plan = conn.execute(f'EXPLAIN QUERY PLAN {requete}').fetchall()

        print("📊 Plan d'exécution :")
        for row in plan:
            print(f"   {row}")

        # Mesurer le temps d'exécution
        import time

        debut = time.time()
        if params:
            resultats = conn.execute(requete, params).fetchall()
        else:
            resultats = conn.execute(requete).fetchall()
        fin = time.time()

        print(f"\n⏱️ Temps d'exécution : {(fin - debut) * 1000:.2f}ms")
        print(f"📄 Résultats : {len(resultats)} ligne(s)")

        return resultats

    finally:
        conn.close()

# Test d'analyse
print("Analyse de la requête des articles avec auteurs :")
analyser_performances_requete('''
    SELECT a.titre, u.nom, u.prenom
    FROM articles a
    INNER JOIN utilisateurs u ON a.auteur_id = u.id
    WHERE a.publie = 1
    ORDER BY a.date_creation DESC
''')
```

## Sauvegarde et restauration

### Sauvegarde automatique

```python
import sqlite3
import shutil
import os
from datetime import datetime

def sauvegarder_base_donnees(db_path='blog.db', backup_dir='backups'):
    """Crée une sauvegarde de la base de données"""

    if not os.path.exists(db_path):
        print(f"❌ Base de données {db_path} non trouvée")
        return False

    # Créer le dossier de sauvegarde
    os.makedirs(backup_dir, exist_ok=True)

    # Nom de fichier avec timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}.db')

    try:
        # Méthode 1: Copie simple du fichier
        shutil.copy2(db_path, backup_path)

        # Vérifier l'intégrité de la sauvegarde
        conn = sqlite3.connect(backup_path)
        conn.execute('PRAGMA integrity_check').fetchone()
        conn.close()

        print(f"✅ Sauvegarde créée : {backup_path}")
        return backup_path

    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        if os.path.exists(backup_path):
            os.remove(backup_path)
        return False

def sauvegarder_avec_sql_dump(db_path='blog.db', backup_dir='backups'):
    """Crée une sauvegarde SQL (format texte)"""

    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    sql_path = os.path.join(backup_dir, f'dump_{timestamp}.sql')

    try:
        conn = sqlite3.connect(db_path)

        with open(sql_path, 'w', encoding='utf-8') as f:
            # Écrire les commandes SQL pour recréer la base
            for ligne in conn.iterdump():
                f.write(f'{ligne}\n')

        conn.close()

        print(f"✅ Dump SQL créé : {sql_path}")
        return sql_path

    except Exception as e:
        print(f"❌ Erreur lors du dump SQL : {e}")
        return False

def nettoyer_anciennes_sauvegardes(backup_dir='backups', garder_jours=7):
    """Supprime les sauvegardes anciennes"""

    if not os.path.exists(backup_dir):
        return

    import time

    maintenant = time.time()
    limite = garder_jours * 24 * 60 * 60  # Convertir en secondes

    for fichier in os.listdir(backup_dir):
        chemin_fichier = os.path.join(backup_dir, fichier)

        if os.path.isfile(chemin_fichier):
            age = maintenant - os.path.getctime(chemin_fichier)

            if age > limite:
                try:
                    os.remove(chemin_fichier)
                    print(f"🗑️ Ancienne sauvegarde supprimée : {fichier}")
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression de {fichier} : {e}")

# Système de sauvegarde automatique
def sauvegarde_complete():
    """Effectue une sauvegarde complète"""
    print("🔄 Début de la sauvegarde...")

    # Sauvegarde binaire
    backup_path = sauvegarder_base_donnees()

    # Sauvegarde SQL
    sql_path = sauvegarder_avec_sql_dump()

    # Nettoyage
    nettoyer_anciennes_sauvegardes(garder_jours=7)

    print("✅ Sauvegarde terminée")

    return backup_path and sql_path

# Exécuter la sauvegarde
sauvegarde_complete()
```

## Exercices pratiques

### Exercice 1 : Système de tags

Créez un système de tags pour les articles avec :
- Table `tags` (id, nom, couleur)
- Table `article_tags` (article_id, tag_id) pour la relation many-to-many
- Fonctions pour ajouter/supprimer des tags aux articles
- Recherche d'articles par tags

### Exercice 2 : Système de commentaires

Étendez la base de données avec :
- Table `commentaires` liée aux articles
- Possibilité de répondre aux commentaires (commentaires imbriqués)
- Modération des commentaires (approuvé/en attente)
- Statistiques sur les commentaires

### Exercice 3 : Historique des modifications

Implémentez un système d'audit avec :
- Table `audit_log` pour tracer toutes les modifications
- Déclencheurs (triggers) pour enregistrer automatiquement les changements
- Fonction pour récupérer l'historique d'un enregistrement

## Solutions des exercices

### Solution Exercice 1 : Système de tags

```python
import sqlite3
from datetime import datetime

def creer_tables_tags():
    """Crée les tables pour le système de tags"""

    conn = sqlite3.connect('blog.db')

    try:
        # Table des tags
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT UNIQUE NOT NULL,
                couleur TEXT DEFAULT '#3498db',
                description TEXT,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Table de liaison article-tags (many-to-many)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS article_tags (
                article_id INTEGER NOT NULL,
                tag_id INTEGER NOT NULL,
                date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (article_id, tag_id),
                FOREIGN KEY (article_id) REFERENCES articles (id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
        print("✅ Tables des tags créées")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        conn.close()

class TagManager:
    """Gestionnaire des tags"""

    @staticmethod
    def creer_tag(nom, couleur='#3498db', description=''):
        """Crée un nouveau tag"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        try:
            cursor = conn.execute('''
                INSERT INTO tags (nom, couleur, description)
                VALUES (?, ?, ?)
            ''', (nom.strip().lower(), couleur, description))

            conn.commit()

            # Récupérer le tag créé
            tag = conn.execute('SELECT * FROM tags WHERE id = ?', (cursor.lastrowid,)).fetchone()
            return dict(tag)

        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def obtenir_tous_tags():
        """Récupère tous les tags avec leurs statistiques"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        cursor = conn.execute('''
            SELECT
                t.*,
                COUNT(at.article_id) as nb_articles
            FROM tags t
            LEFT JOIN article_tags at ON t.id = at.tag_id
            GROUP BY t.id
            ORDER BY nb_articles DESC, t.nom
        ''')

        tags = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tags

    @staticmethod
    def ajouter_tag_article(article_id, tag_id):
        """Ajoute un tag à un article"""
        conn = sqlite3.connect('blog.db')

        try:
            conn.execute('''
                INSERT OR IGNORE INTO article_tags (article_id, tag_id)
                VALUES (?, ?)
            ''', (article_id, tag_id))

            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def supprimer_tag_article(article_id, tag_id):
        """Supprime un tag d'un article"""
        conn = sqlite3.connect('blog.db')

        try:
            conn.execute('''
                DELETE FROM article_tags
                WHERE article_id = ? AND tag_id = ?
            ''', (article_id, tag_id))

            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def obtenir_tags_article(article_id):
        """Récupère tous les tags d'un article"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        cursor = conn.execute('''
            SELECT t.*
            FROM tags t
            INNER JOIN article_tags at ON t.id = at.tag_id
            WHERE at.article_id = ?
            ORDER BY t.nom
        ''', (article_id,))

        tags = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tags

    @staticmethod
    def rechercher_articles_par_tags(tag_names):
        """Recherche des articles par noms de tags"""
        if not tag_names:
            return []

        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        # Construire la requête dynamiquement
        placeholders = ','.join(['?' for _ in tag_names])

        cursor = conn.execute(f'''
            SELECT DISTINCT
                a.id,
                a.titre,
                a.date_creation,
                u.nom as auteur_nom,
                u.prenom as auteur_prenom,
                COUNT(DISTINCT at.tag_id) as tags_matches
            FROM articles a
            INNER JOIN utilisateurs u ON a.auteur_id = u.id
            INNER JOIN article_tags at ON a.id = at.article_id
            INNER JOIN tags t ON at.tag_id = t.id
            WHERE t.nom IN ({placeholders}) AND a.publie = 1
            GROUP BY a.id
            ORDER BY tags_matches DESC, a.date_creation DESC
        ''', tag_names)

        articles = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return articles

# Tests du système de tags
def tester_systeme_tags():
    """Teste le système de tags"""

    print("🏷️ Test du système de tags")

    # Créer les tables
    creer_tables_tags()

    # Créer quelques tags
    tags_test = [
        ('python', '#3776ab', 'Langage de programmation'),
        ('web', '#e44d26', 'Développement web'),
        ('database', '#336791', 'Bases de données'),
        ('tutorial', '#28a745', 'Tutoriels et guides')
    ]

    tag_ids = {}
    for nom, couleur, desc in tags_test:
        tag = TagManager.creer_tag(nom, couleur, desc)
        if tag:
            tag_ids[nom] = tag['id']
            print(f"✅ Tag créé : {nom}")

    # Afficher tous les tags
    print("\n📋 Tous les tags :")
    tags = TagManager.obtenir_tous_tags()
    for tag in tags:
        print(f"   🏷️ {tag['nom']} ({tag['nb_articles']} articles)")

    # Ajouter des tags aux articles (supposons que les articles 1 et 2 existent)
    if tag_ids:
        TagManager.ajouter_tag_article(1, tag_ids.get('python'))
        TagManager.ajouter_tag_article(1, tag_ids.get('tutorial'))
        TagManager.ajouter_tag_article(2, tag_ids.get('web'))
        TagManager.ajouter_tag_article(2, tag_ids.get('python'))
        print("✅ Tags ajoutés aux articles")

    # Rechercher des articles par tags
    print("\n🔍 Articles avec le tag 'python' :")
    articles = TagManager.rechercher_articles_par_tags(['python'])
    for article in articles:
        print(f"   📄 {article['titre']} - {article['auteur_prenom']} {article['auteur_nom']}")

# Exécuter le test
tester_systeme_tags()
```

### Solution Exercice 2 : Système de commentaires

```python
def creer_table_commentaires():
    """Crée la table des commentaires avec support des réponses"""

    conn = sqlite3.connect('blog.db')

    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS commentaires (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                article_id INTEGER NOT NULL,
                parent_id INTEGER NULL,
                auteur_nom TEXT NOT NULL,
                auteur_email TEXT NOT NULL,
                contenu TEXT NOT NULL,
                statut TEXT DEFAULT 'en_attente' CHECK (statut IN ('en_attente', 'approuve', 'rejete')),
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                date_moderation TIMESTAMP NULL,
                moderateur_id INTEGER NULL,
                FOREIGN KEY (article_id) REFERENCES articles (id) ON DELETE CASCADE,
                FOREIGN KEY (parent_id) REFERENCES commentaires (id) ON DELETE CASCADE,
                FOREIGN KEY (moderateur_id) REFERENCES utilisateurs (id)
            )
        ''')

        # Index pour améliorer les performances
        conn.execute('CREATE INDEX IF NOT EXISTS idx_commentaires_article ON commentaires(article_id)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_commentaires_parent ON commentaires(parent_id)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_commentaires_statut ON commentaires(statut)')

        conn.commit()
        print("✅ Table commentaires créée")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        conn.close()

class CommentaireManager:
    """Gestionnaire des commentaires"""

    @staticmethod
    def ajouter_commentaire(article_id, auteur_nom, auteur_email, contenu, parent_id=None):
        """Ajoute un nouveau commentaire"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        try:
            cursor = conn.execute('''
                INSERT INTO commentaires (article_id, parent_id, auteur_nom, auteur_email, contenu)
                VALUES (?, ?, ?, ?, ?)
            ''', (article_id, parent_id, auteur_nom, auteur_email, contenu))

            conn.commit()

            # Récupérer le commentaire créé
            commentaire = conn.execute('SELECT * FROM commentaires WHERE id = ?', (cursor.lastrowid,)).fetchone()
            return dict(commentaire)

        except Exception as e:
            print(f"❌ Erreur lors de l'ajout du commentaire : {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def obtenir_commentaires_article(article_id, inclure_en_attente=False):
        """Récupère tous les commentaires d'un article avec structure hiérarchique"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        # Construire la condition de statut
        condition_statut = "c.statut = 'approuve'" if not inclure_en_attente else "c.statut IN ('approuve', 'en_attente')"

        cursor = conn.execute(f'''
            SELECT * FROM commentaires c
            WHERE c.article_id = ? AND {condition_statut}
            ORDER BY c.parent_id NULLS FIRST, c.date_creation ASC
        ''', (article_id,))

        commentaires_raw = [dict(row) for row in cursor.fetchall()]
        conn.close()

        # Organiser en structure hiérarchique
        commentaires_dict = {c['id']: c for c in commentaires_raw}
        commentaires_organises = []

        for commentaire in commentaires_raw:
            commentaire['reponses'] = []

            if commentaire['parent_id'] is None:
                # Commentaire principal
                commentaires_organises.append(commentaire)
            else:
                # Réponse à un commentaire
                parent = commentaires_dict.get(commentaire['parent_id'])
                if parent:
                    parent['reponses'].append(commentaire)

        return commentaires_organises

    @staticmethod
    def moderer_commentaire(commentaire_id, nouveau_statut, moderateur_id=None):
        """Modère un commentaire (approuve/rejette)"""
        if nouveau_statut not in ['approuve', 'rejete']:
            return False

        conn = sqlite3.connect('blog.db')

        try:
            cursor = conn.execute('''
                UPDATE commentaires
                SET statut = ?, date_moderation = CURRENT_TIMESTAMP, moderateur_id = ?
                WHERE id = ?
            ''', (nouveau_statut, moderateur_id, commentaire_id))

            conn.commit()
            return cursor.rowcount > 0

        except Exception as e:
            print(f"❌ Erreur lors de la modération : {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtenir_commentaires_en_attente():
        """Récupère tous les commentaires en attente de modération"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        cursor = conn.execute('''
            SELECT
                c.*,
                a.titre as article_titre
            FROM commentaires c
            INNER JOIN articles a ON c.article_id = a.id
            WHERE c.statut = 'en_attente'
            ORDER BY c.date_creation ASC
        ''')

        commentaires = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return commentaires

    @staticmethod
    def obtenir_statistiques_commentaires():
        """Calcule les statistiques des commentaires"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        # Statistiques générales
        cursor = conn.execute('''
            SELECT
                COUNT(*) as total,
                COUNT(CASE WHEN statut = 'approuve' THEN 1 END) as approuves,
                COUNT(CASE WHEN statut = 'en_attente' THEN 1 END) as en_attente,
                COUNT(CASE WHEN statut = 'rejete' THEN 1 END) as rejetes,
                COUNT(CASE WHEN parent_id IS NOT NULL THEN 1 END) as reponses
            FROM commentaires
        ''')

        stats_generales = dict(cursor.fetchone())

        # Top commentateurs
        cursor = conn.execute('''
            SELECT
                auteur_nom,
                auteur_email,
                COUNT(*) as nb_commentaires
            FROM commentaires
            WHERE statut = 'approuve'
            GROUP BY auteur_nom, auteur_email
            ORDER BY nb_commentaires DESC
            LIMIT 10
        ''')

        top_commentateurs = [dict(row) for row in cursor.fetchall()]

        # Articles les plus commentés
        cursor = conn.execute('''
            SELECT
                a.id,
                a.titre,
                COUNT(c.id) as nb_commentaires
            FROM articles a
            LEFT JOIN commentaires c ON a.id = c.article_id AND c.statut = 'approuve'
            GROUP BY a.id, a.titre
            ORDER BY nb_commentaires DESC
            LIMIT 10
        ''')

        articles_populaires = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return {
            'generales': stats_generales,
            'top_commentateurs': top_commentateurs,
            'articles_populaires': articles_populaires
        }

# Tests du système de commentaires
def tester_systeme_commentaires():
    """Teste le système de commentaires"""

    print("💬 Test du système de commentaires")

    # Créer la table
    creer_table_commentaires()

    # Ajouter des commentaires de test (supposons que l'article 1 existe)
    commentaire1 = CommentaireManager.ajouter_commentaire(
        article_id=1,
        auteur_nom="Alice Lectrice",
        auteur_email="alice@email.com",
        contenu="Excellent article ! Très informatif."
    )

    if commentaire1:
        print(f"✅ Commentaire principal ajouté (ID: {commentaire1['id']})")

        # Ajouter une réponse
        reponse = CommentaireManager.ajouter_commentaire(
            article_id=1,
            auteur_nom="Bob Développeur",
            auteur_email="bob@email.com",
            contenu="Je suis d'accord avec Alice, merci pour le partage !",
            parent_id=commentaire1['id']
        )

        if reponse:
            print(f"✅ Réponse ajoutée (ID: {reponse['id']})")

    # Ajouter un autre commentaire
    CommentaireManager.ajouter_commentaire(
        article_id=1,
        auteur_nom="Charlie Curieux",
        auteur_email="charlie@email.com",
        contenu="Pourriez-vous détailler la partie sur les migrations ?"
    )

    # Afficher les commentaires en attente
    print("\n⏳ Commentaires en attente de modération :")
    en_attente = CommentaireManager.obtenir_commentaires_en_attente()
    for comm in en_attente:
        print(f"   💬 {comm['auteur_nom']}: {comm['contenu'][:50]}...")

    # Approuver quelques commentaires
    if en_attente:
        for comm in en_attente[:2]:  # Approuver les 2 premiers
            CommentaireManager.moderer_commentaire(comm['id'], 'approuve', moderateur_id=1)
            print(f"✅ Commentaire {comm['id']} approuvé")

    # Afficher la structure hiérarchique
    print("\n🌳 Structure des commentaires de l'article 1 :")
    commentaires = CommentaireManager.obtenir_commentaires_article(1)

    def afficher_commentaire(comm, niveau=0):
        indent = "  " * niveau
        print(f"{indent}💬 {comm['auteur_nom']}: {comm['contenu'][:50]}...")
        for reponse in comm['reponses']:
            afficher_commentaire(reponse, niveau + 1)

    for commentaire in commentaires:
        afficher_commentaire(commentaire)

    # Afficher les statistiques
    print("\n📊 Statistiques des commentaires :")
    stats = CommentaireManager.obtenir_statistiques_commentaires()

    gen = stats['generales']
    print(f"   Total: {gen['total']}")
    print(f"   Approuvés: {gen['approuves']}")
    print(f"   En attente: {gen['en_attente']}")
    print(f"   Réponses: {gen['reponses']}")

# Exécuter le test
tester_systeme_commentaires()
```

## Solution Exercice 3 : Historique des modifications

```python
def creer_table_audit():
    """Crée la table d'audit pour tracer les modifications"""

    conn = sqlite3.connect('blog.db')

    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                table_name TEXT NOT NULL,
                record_id INTEGER NOT NULL,
                operation TEXT NOT NULL CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE')),
                old_values TEXT,
                new_values TEXT,
                user_id INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT,
                user_agent TEXT
            )
        ''')

        # Index pour améliorer les performances des requêtes d'audit
        conn.execute('CREATE INDEX IF NOT EXISTS idx_audit_table_record ON audit_log(table_name, record_id)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_log(timestamp)')

        conn.commit()
        print("✅ Table d'audit créée")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        conn.close()

def creer_triggers_audit():
    """Crée les déclencheurs pour l'audit automatique"""

    conn = sqlite3.connect('blog.db')

    try:
        # Trigger pour INSERT sur utilisateurs
        conn.execute('''
            CREATE TRIGGER IF NOT EXISTS audit_utilisateurs_insert
            AFTER INSERT ON utilisateurs
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (table_name, record_id, operation, new_values)
                VALUES (
                    'utilisateurs',
                    NEW.id,
                    'INSERT',
                    json_object(
                        'nom', NEW.nom,
                        'prenom', NEW.prenom,
                        'email', NEW.email,
                        'age', NEW.age
                    )
                );
            END
        ''')

        # Trigger pour UPDATE sur utilisateurs
        conn.execute('''
            CREATE TRIGGER IF NOT EXISTS audit_utilisateurs_update
            AFTER UPDATE ON utilisateurs
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (table_name, record_id, operation, old_values, new_values)
                VALUES (
                    'utilisateurs',
                    NEW.id,
                    'UPDATE',
                    json_object(
                        'nom', OLD.nom,
                        'prenom', OLD.prenom,
                        'email', OLD.email,
                        'age', OLD.age
                    ),
                    json_object(
                        'nom', NEW.nom,
                        'prenom', NEW.prenom,
                        'email', NEW.email,
                        'age', NEW.age
                    )
                );
            END
        ''')

        # Trigger pour DELETE sur utilisateurs
        conn.execute('''
            CREATE TRIGGER IF NOT EXISTS audit_utilisateurs_delete
            AFTER DELETE ON utilisateurs
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (table_name, record_id, operation, old_values)
                VALUES (
                    'utilisateurs',
                    OLD.id,
                    'DELETE',
                    json_object(
                        'nom', OLD.nom,
                        'prenom', OLD.prenom,
                        'email', OLD.email,
                        'age', OLD.age
                    )
                );
            END
        ''')

        conn.commit()
        print("✅ Déclencheurs d'audit créés")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        conn.close()

class AuditManager:
    """Gestionnaire de l'audit et de l'historique"""

    @staticmethod
    def obtenir_historique_enregistrement(table_name, record_id):
        """Récupère l'historique complet d'un enregistrement"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        cursor = conn.execute('''
            SELECT * FROM audit_log
            WHERE table_name = ? AND record_id = ?
            ORDER BY timestamp ASC
        ''', (table_name, record_id))

        historique = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return historique

    @staticmethod
    def obtenir_modifications_recentes(limite=50):
        """Récupère les modifications récentes dans toutes les tables"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        cursor = conn.execute('''
            SELECT * FROM audit_log
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limite,))

        modifications = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return modifications

    @staticmethod
    def analyser_changements(old_values_json, new_values_json):
        """Analyse les changements entre deux versions"""
        import json

        try:
            old_values = json.loads(old_values_json) if old_values_json else {}
            new_values = json.loads(new_values_json) if new_values_json else {}
        except:
            return []

        changements = []

        # Champs modifiés
        for champ in set(old_values.keys()) | set(new_values.keys()):
            old_val = old_values.get(champ)
            new_val = new_values.get(champ)

            if old_val != new_val:
                changements.append({
                    'champ': champ,
                    'ancienne_valeur': old_val,
                    'nouvelle_valeur': new_val
                })

        return changements

    @staticmethod
    def generer_rapport_audit(table_name=None, date_debut=None, date_fin=None):
        """Génère un rapport d'audit détaillé"""
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        # Construire la requête avec filtres
        conditions = []
        params = []

        if table_name:
            conditions.append('table_name = ?')
            params.append(table_name)

        if date_debut:
            conditions.append('timestamp >= ?')
            params.append(date_debut)

        if date_fin:
            conditions.append('timestamp <= ?')
            params.append(date_fin)

        where_clause = 'WHERE ' + ' AND '.join(conditions) if conditions else ''

        # Statistiques générales
        cursor = conn.execute(f'''
            SELECT
                operation,
                table_name,
                COUNT(*) as count
            FROM audit_log
            {where_clause}
            GROUP BY operation, table_name
            ORDER BY table_name, operation
        ''', params)

        stats_operations = [dict(row) for row in cursor.fetchall()]

        # Activité par jour
        cursor = conn.execute(f'''
            SELECT
                DATE(timestamp) as date,
                COUNT(*) as nb_operations
            FROM audit_log
            {where_clause}
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
            LIMIT 30
        ''', params)

        activite_quotidienne = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return {
            'stats_operations': stats_operations,
            'activite_quotidienne': activite_quotidienne,
            'periode': {
                'debut': date_debut,
                'fin': date_fin
            }
        }

    @staticmethod
    def restaurer_version(table_name, record_id, timestamp):
        """Restaure un enregistrement à une version antérieure"""
        # Cette fonction nécessiterait une implémentation spécifique
        # selon la structure de chaque table
        # Ici, on montre le principe pour la table utilisateurs

        if table_name != 'utilisateurs':
            return False, "Restauration non supportée pour cette table"

        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row

        try:
            # Trouver la version à cette date
            cursor = conn.execute('''
                SELECT old_values, new_values, operation FROM audit_log
                WHERE table_name = ? AND record_id = ? AND timestamp <= ?
                ORDER BY timestamp DESC
                LIMIT 1
            ''', (table_name, record_id, timestamp))

            version = cursor.fetchone()

            if not version:
                return False, "Aucune version trouvée à cette date"

            # Récupérer les valeurs à restaurer
            if version['operation'] == 'DELETE':
                values_json = version['old_values']
            else:
                values_json = version['new_values'] or version['old_values']

            if not values_json:
                return False, "Données de version introuvables"

            import json
            values = json.loads(values_json)

            # Restaurer les données
            conn.execute('''
                UPDATE utilisateurs
                SET nom = ?, prenom = ?, email = ?, age = ?
                WHERE id = ?
            ''', (values['nom'], values['prenom'], values['email'],
                  values['age'], record_id))

            conn.commit()
            return True, "Version restaurée avec succès"

        except Exception as e:
            conn.rollback()
            return False, f"Erreur lors de la restauration : {e}"
        finally:
            conn.close()

# Tests du système d'audit
def tester_systeme_audit():
    """Teste le système d'audit"""

    print("📋 Test du système d'audit")

    # Créer les tables et triggers
    creer_table_audit()
    creer_triggers_audit()

    # Effectuer quelques modifications pour générer de l'audit
    print("\n🔄 Simulation de modifications...")

    # Ces opérations déclencheront automatiquement l'audit
    conn = sqlite3.connect('blog.db')

    # Insérer un utilisateur de test
    cursor = conn.execute('''
        INSERT INTO utilisateurs (nom, prenom, email, age)
        VALUES (?, ?, ?, ?)
    ''', ('Test', 'Audit', 'audit@test.com', 25))

    user_id = cursor.lastrowid

    # Modifier l'utilisateur
    conn.execute('''
        UPDATE utilisateurs SET age = ?, email = ?
        WHERE id = ?
    ''', (26, 'audit.nouveau@test.com', user_id))

    conn.commit()
    conn.close()

    print(f"✅ Utilisateur de test créé et modifié (ID: {user_id})")

    # Consulter l'historique
    print(f"\n📊 Historique de l'utilisateur {user_id} :")
    historique = AuditManager.obtenir_historique_enregistrement('utilisateurs', user_id)

    for entry in historique:
        print(f"   {entry['timestamp']}: {entry['operation']}")

        if entry['operation'] == 'UPDATE':
            changements = AuditManager.analyser_changements(
                entry['old_values'], entry['new_values']
            )
            for change in changements:
                print(f"      📝 {change['champ']}: {change['ancienne_valeur']} → {change['nouvelle_valeur']}")

    # Afficher les modifications récentes
    print("\n🕐 Modifications récentes :")
    recentes = AuditManager.obtenir_modifications_recentes(10)

    for modif in recentes:
        print(f"   {modif['timestamp']}: {modif['operation']} sur {modif['table_name']} (ID: {modif['record_id']})")

    # Générer un rapport
    print("\n📈 Rapport d'audit :")
    rapport = AuditManager.generer_rapport_audit()

    print("   Opérations par table :")
    for stat in rapport['stats_operations']:
        print(f"      {stat['table_name']}.{stat['operation']}: {stat['count']}")

# Exécuter le test
tester_systeme_audit()
```

## Bonnes pratiques et conseils finaux

### Sécurité de la base de données

```python
import sqlite3
import hashlib
import secrets

def securiser_base_donnees():
    """Applique les mesures de sécurité de base"""

    conn = sqlite3.connect('blog.db')

    try:
        # Activer les clés étrangères (important pour l'intégrité)
        conn.execute('PRAGMA foreign_keys = ON')

        # Configurer le mode WAL pour de meilleures performances concurrentes
        conn.execute('PRAGMA journal_mode = WAL')

        # Optimiser la taille des pages
        conn.execute('PRAGMA page_size = 4096')

        # Configurer le cache
        conn.execute('PRAGMA cache_size = 10000')

        conn.commit()
        print("✅ Configuration de sécurité appliquée")

    except Exception as e:
        print(f"❌ Erreur de configuration : {e}")
    finally:
        conn.close()

def hacher_mot_de_passe(mot_de_passe):
    """Hache un mot de passe de manière sécurisée"""
    # Générer un salt aléatoire
    salt = secrets.token_hex(32)

    # Hacher avec le salt
    hash_obj = hashlib.pbkdf2_hmac('sha256',
                                   mot_de_passe.encode('utf-8'),
                                   salt.encode('utf-8'),
                                   100000)  # 100k iterations

    return f"{salt}:{hash_obj.hex()}"

def verifier_mot_de_passe(mot_de_passe, hash_stocke):
    """Vérifie un mot de passe contre son hash"""
    try:
        salt, hash_password = hash_stocke.split(':')

        hash_obj = hashlib.pbkdf2_hmac('sha256',
                                       mot_de_passe.encode('utf-8'),
                                       salt.encode('utf-8'),
                                       100000)

        return hash_obj.hex() == hash_password
    except:
        return False

# Appliquer la sécurisation
securiser_base_donnees()
```

### Surveillance et maintenance

```python
def verifier_integrite_base():
    """Vérifie l'intégrité de la base de données"""
    conn = sqlite3.connect('blog.db')

    try:
        # Vérification d'intégrité
        cursor = conn.execute('PRAGMA integrity_check')
        resultat = cursor.fetchone()[0]

        if resultat == 'ok':
            print("✅ Intégrité de la base de données: OK")
        else:
            print(f"⚠️ Problème d'intégrité détecté: {resultat}")

        # Statistiques de la base
        cursor = conn.execute('PRAGMA database_list')
        print("\n📊 Informations de la base:")
        for row in cursor.fetchall():
            print(f"   Base: {row[1]}, Fichier: {row[2]}")

        # Taille des tables
        cursor = conn.execute('''
            SELECT name,
                   (SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=m.name) as table_count
            FROM sqlite_master m WHERE type='table'
        ''')

        print("\n📋 Tables dans la base:")
        for row in cursor.fetchall():
            table_name = row[0]
            cursor2 = conn.execute(f'SELECT COUNT(*) FROM {table_name}')
            count = cursor2.fetchone()[0]
            print(f"   {table_name}: {count} enregistrement(s)")

    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
    finally:
        conn.close()

def optimiser_base_donnees():
    """Optimise les performances de la base"""
    conn = sqlite3.connect('blog.db')

    try:
        print("🔧 Optimisation de la base de données...")

        # Analyser les statistiques des tables
        conn.execute('ANALYZE')

        # Défragmenter la base
        conn.execute('VACUUM')

        print("✅ Optimisation terminée")

    except Exception as e:
        print(f"❌ Erreur d'optimisation: {e}")
    finally:
        conn.close()

# Maintenance périodique
def maintenance_complete():
    """Effectue une maintenance complète"""
    print("🛠️ Début de la maintenance...")

    verifier_integrite_base()
    optimiser_base_donnees()
    sauvegarde_complete()  # Fonction définie précédemment

    print("✅ Maintenance terminée")

# Exécuter la maintenance
maintenance_complete()
```

## Résumé des concepts clés

### Points essentiels à retenir

1. **SQLite est parfait pour débuter** : Simple, sans serveur, fiable
2. **Toujours utiliser des paramètres liés** : Protection contre l'injection SQL
3. **Gérer les connexions proprement** : Toujours fermer les connexions
4. **Structurer avec des classes** : Modèles pour organiser le code
5. **Prévoir la migration** : Les bases de données évoluent
6. **Surveiller les performances** : Index et optimisation

### Checklist pour une application avec base de données

```python
# ✅ Connexion sécurisée
def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

# ✅ Requêtes paramétrées
cursor.execute('SELECT * FROM users WHERE email = ?', (email,))

# ✅ Gestion d'erreurs
try:
    # Opération base de données
    conn.commit()
except sqlite3.IntegrityError:
    # Gérer l'erreur spécifique
    conn.rollback()
finally:
    conn.close()

# ✅ Transactions pour opérations multiples
try:
    conn.execute('BEGIN TRANSACTION')
    # Plusieurs opérations
    conn.commit()
except:
    conn.rollback()

# ✅ Index pour les performances
CREATE INDEX idx_users_email ON users(email);

# ✅ Sauvegardes régulières
# Script de sauvegarde automatique
```

### Évolutions possibles

Avec SQLite maîtrisé, vous pouvez explorer :

- **Bases plus complexes** : PostgreSQL, MySQL
- **ORM avancés** : SQLAlchemy, Django ORM
- **NoSQL** : MongoDB, Redis
- **Réplication** : Clusters de bases de données
- **Analyse** : Data warehousing, business intelligence

SQLite vous a donné les fondations solides pour comprendre les bases de données relationnelles. Ces concepts s'appliquent à tous les systèmes de base de données !

---

*Pratiquez en créant vos propres applications avec persistance de données pour maîtriser ces concepts essentiels.*

⏭️
