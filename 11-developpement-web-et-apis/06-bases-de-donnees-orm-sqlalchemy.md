🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.6 Bases de données et ORM (SQLite + SQLAlchemy)

## Introduction

Bienvenue dans ce chapitre consacré aux bases de données et à l'ORM avec Python ! Si vous développez des applications, vous aurez très souvent besoin de stocker et de manipuler des données de manière persistante. C'est exactement ce que nous allons apprendre dans ce chapitre.

## Qu'est-ce qu'une base de données ?

Une **base de données** est un système organisé pour stocker, gérer et récupérer des informations de manière structurée et efficace. Imaginez-la comme un classeur numérique sophistiqué où vos données sont organisées de façon logique et accessible.

### Pourquoi avez-vous besoin d'une base de données ?

Sans base de données, vous pourriez être tenté de stocker vos données dans des fichiers texte ou des variables Python. Mais cela pose plusieurs problèmes :

**Problèmes sans base de données :**
```python
# Données en mémoire - perdues à l'arrêt du programme
utilisateurs = [
    {"nom": "Alice", "email": "alice@example.com"},
    {"nom": "Bob", "email": "bob@example.com"}
]

# Fichier texte - difficile à gérer et risqué
with open("users.txt", "w") as f:
    f.write("Alice,alice@example.com\n")
    f.write("Bob,bob@example.com\n")
```

**Limites de ces approches :**
- Les données en mémoire disparaissent quand le programme s'arrête
- Les fichiers texte sont difficiles à interroger efficacement
- Pas de gestion des accès simultanés (plusieurs utilisateurs en même temps)
- Risque de corruption des données
- Pas de validation automatique
- Difficile de maintenir l'intégrité des données
- Performances médiocres avec de grandes quantités de données

**Avantages d'une base de données :**
- **Persistance** : Les données restent sauvegardées même après l'arrêt du programme
- **Organisation** : Structure claire avec des tables, colonnes et relations
- **Recherche rapide** : Retrouver des informations en quelques millisecondes
- **Intégrité** : Garantit la cohérence des données avec des contraintes
- **Concurrence** : Plusieurs utilisateurs peuvent accéder aux données simultanément
- **Sécurité** : Contrôle d'accès et droits utilisateurs
- **Scalabilité** : Gère facilement des millions d'enregistrements

## Types de bases de données

Il existe deux grandes familles de bases de données :

### Bases de données relationnelles (SQL)

Ce sont les plus courantes. Elles organisent les données en **tables** (comme des feuilles Excel) avec des lignes et des colonnes.

**Exemples :**
- SQLite (ce que nous utiliserons)
- PostgreSQL
- MySQL
- Oracle
- SQL Server

**Structure typique :**

Table `utilisateurs` :
```
+----+----------+----------------------+-----+
| id | nom      | email                | age |
+----+----------+----------------------+-----+
| 1  | Alice    | alice@example.com    | 28  |
| 2  | Bob      | bob@example.com      | 35  |
| 3  | Claire   | claire@example.com   | 42  |
+----+----------+----------------------+-----+
```

Table `commandes` :
```
+----+-----------------+------------+----------------+
| id | utilisateur_id  | produit    | montant        |
+----+-----------------+------------+----------------+
| 1  | 1               | Laptop     | 899.99         |
| 2  | 1               | Souris     | 29.99          |
| 3  | 2               | Clavier    | 79.99          |
+----+-----------------+------------+----------------+
```

**Caractéristiques :**
- Structure rigide avec schéma défini
- Données reliées entre elles (relations)
- Langage de requête standardisé : SQL (Structured Query Language)
- Excellente pour des données structurées

### Bases de données NoSQL

Bases de données "non relationnelles" pour des données moins structurées ou très volumineuses.

**Exemples :**
- MongoDB (documents)
- Redis (clé-valeur)
- Cassandra (colonnes)
- Neo4j (graphes)

**Quand les utiliser ?**
- Données très variables en structure
- Besoin de scalabilité horizontale extrême
- Données sous forme de documents JSON
- Graphes de relations complexes

Dans ce cours, nous nous concentrons sur les **bases de données relationnelles** avec SQLite, car elles sont :
- Plus courantes dans la majorité des applications
- Plus faciles à apprendre pour débuter
- Parfaitement adaptées à la plupart des projets

## Qu'est-ce que SQLite ?

**SQLite** est un système de gestion de base de données relationnelle (SGBDR) léger et autonome. C'est le choix parfait pour apprendre et pour de nombreuses applications réelles.

### Caractéristiques de SQLite

**Points forts :**
- **Sans serveur** : Pas besoin d'installer un serveur de base de données séparé
- **Fichier unique** : Toute la base de données tient dans un seul fichier `.db`
- **Zéro configuration** : Fonctionne immédiatement sans configuration
- **Intégré à Python** : Le module `sqlite3` est inclus dans Python
- **Léger** : Très peu de ressources système nécessaires
- **Fiable** : Utilisé par des millions d'applications (navigateurs, smartphones, etc.)
- **Portable** : Un fichier de base de données fonctionne sur tous les systèmes

**Cas d'usage idéaux :**
- Applications de bureau
- Applications mobiles (iOS, Android)
- Prototypes et développement
- Sites web avec trafic faible à moyen
- Applications embarquées
- Stockage local de données
- Tests et apprentissage

**Limites à connaître :**
- Pas adapté aux très gros volumes d'écritures simultanées
- Pas de gestion d'utilisateurs sophistiquée
- Moins performant que PostgreSQL/MySQL pour des applications massives

### SQLite vs autres bases de données

| Critère              | SQLite                | PostgreSQL/MySQL       |
|----------------------|-----------------------|------------------------|
| Installation         | Aucune (inclus)       | Serveur à installer    |
| Configuration        | Aucune                | Configuration requise  |
| Fichier              | Un seul fichier       | Plusieurs fichiers     |
| Utilisateurs         | Application locale    | Multi-utilisateurs     |
| Taille               | Très léger (< 1 MB)   | Plus lourd (> 50 MB)   |
| Performance          | Excellente (lecture)  | Excellente (tout)      |
| Complexité           | Simple                | Plus complexe          |
| Idéal pour           | Apps simples/moyennes | Apps complexes/grandes |

**En résumé :** SQLite est parfait pour apprendre et pour une grande partie des applications que vous créerez. Une fois que vous maîtriserez SQLite, passer à PostgreSQL ou MySQL sera très facile.

## Qu'est-ce que SQL ?

**SQL** (Structured Query Language) est le langage standardisé pour communiquer avec les bases de données relationnelles.

### Exemples de commandes SQL

```sql
-- Créer une table
CREATE TABLE utilisateurs (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
);

-- Insérer des données
INSERT INTO utilisateurs (nom, email, age)
VALUES ('Alice', 'alice@example.com', 28);

-- Lire des données
SELECT * FROM utilisateurs WHERE age > 25;

-- Mettre à jour
UPDATE utilisateurs SET age = 29 WHERE nom = 'Alice';

-- Supprimer
DELETE FROM utilisateurs WHERE id = 3;
```

**Le problème avec SQL brut :**
Bien que puissant, écrire du SQL directement dans votre code Python a des inconvénients :
- Syntaxe différente de Python (mélange de langages)
- Risque d'erreurs de syntaxe
- Vulnérabilité aux injections SQL si mal utilisé
- Code difficile à maintenir
- Changement de base de données = réécriture du code

**C'est là qu'intervient l'ORM !**

## Qu'est-ce qu'un ORM ?

**ORM** signifie **Object-Relational Mapping** (Mappage Objet-Relationnel). C'est une technique de programmation qui permet de manipuler des données de base de données comme des objets Python.

### Concept de l'ORM

Un ORM fait le pont entre deux mondes :
- Le monde **orienté objet** de Python (classes, objets)
- Le monde **relationnel** des bases de données (tables, lignes)

**Analogie :**
Imaginez un traducteur simultané qui traduit automatiquement vos phrases Python en SQL, et les réponses SQL en objets Python. C'est exactement ce que fait un ORM !

### Sans ORM vs Avec ORM

**Sans ORM (SQL brut avec sqlite3) :**
```python
import sqlite3

# Connexion
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# Créer une table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        email TEXT
    )
''')

# Insérer des données
cursor.execute(
    "INSERT INTO users (nom, email) VALUES (?, ?)",
    ("Alice", "alice@example.com")
)
conn.commit()

# Récupérer des données
cursor.execute("SELECT * FROM users WHERE nom = ?", ("Alice",))
row = cursor.fetchone()
print(f"ID: {row[0]}, Nom: {row[1]}, Email: {row[2]}")

# Fermeture
conn.close()
```

**Avec ORM (SQLAlchemy) :**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuration
Base = declarative_base()
engine = create_engine('sqlite:///ma_base.db')
Session = sessionmaker(bind=engine)
session = Session()

# Définir le modèle (la structure)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)

# Créer la table
Base.metadata.create_all(engine)

# Insérer des données (comme un objet Python !)
alice = User(nom="Alice", email="alice@example.com")
session.add(alice)
session.commit()

# Récupérer des données (comme des objets Python !)
user = session.query(User).filter(User.nom == "Alice").first()
print(f"ID: {user.id}, Nom: {user.nom}, Email: {user.email}")
```

**Différences notables :**
- Avec l'ORM, vous manipulez des **objets Python** naturellement
- Plus besoin d'écrire des requêtes SQL manuellement
- Le code est plus lisible et maintenable
- Protection automatique contre les injections SQL
- Facilité de changement de base de données

## Pourquoi utiliser SQLAlchemy ?

**SQLAlchemy** est l'ORM le plus populaire et le plus puissant pour Python. Il est utilisé par des milliers d'entreprises et de projets open source.

### Avantages de SQLAlchemy

**1. Productivité accrue**
```python
# Créer 3 utilisateurs en quelques lignes
users = [
    User(nom="Alice", email="alice@example.com"),
    User(nom="Bob", email="bob@example.com"),
    User(nom="Claire", email="claire@example.com")
]
session.add_all(users)
session.commit()

# Rechercher facilement
users_seniors = session.query(User).filter(User.age > 50).all()
```

**2. Code Python idiomatique**
Vous écrivez du Python pur, pas du SQL déguisé en strings.

**3. Sécurité**
Protection automatique contre les injections SQL (une vulnérabilité majeure).

**4. Portabilité**
Changez de SQLite vers PostgreSQL en modifiant une seule ligne de configuration.

**5. Relations simplifiées**
Gérez facilement les liens entre tables (un auteur a plusieurs livres, etc.).

**6. Migrations de schéma**
Évoluez votre base de données de manière contrôlée avec Alembic.

**7. Performances optimisées**
SQLAlchemy génère du SQL optimisé et offre des outils de mise en cache.

**8. Écosystème riche**
Compatible avec Flask, FastAPI, Django (via des extensions), et bien d'autres.

### SQLAlchemy dans l'écosystème Python

SQLAlchemy s'intègre parfaitement avec les frameworks web modernes :

```python
# Avec FastAPI
from fastapi import FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

# Avec Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return User.query.get(user_id)
```

## Concepts clés à retenir

Avant de plonger dans les détails techniques, voici les concepts fondamentaux :

### 1. Modèle (Model)
Une **classe Python** qui représente une **table** en base de données.

```python
class User(Base):
    __tablename__ = 'users'
    # ... définition des colonnes
```

### 2. Session
Un espace de travail temporaire pour manipuler des données. C'est votre interface avec la base de données.

```python
session = Session()
session.add(user)      # Préparer
session.commit()       # Sauvegarder
```

### 3. Requête (Query)
Une demande d'informations à la base de données, écrite en Python.

```python
users = session.query(User).filter(User.age > 18).all()
```

### 4. Relations
Les liens entre différentes tables (un utilisateur a plusieurs commandes, etc.).

```python
class User(Base):
    commandes = relationship("Commande")

class Commande(Base):
    user_id = Column(Integer, ForeignKey('users.id'))
```

### 5. Migration
Un fichier qui décrit une modification du schéma de la base de données.

```python
# Migration : ajouter une colonne 'age' à la table users
def upgrade():
    op.add_column('users', sa.Column('age', sa.Integer()))
```

## Architecture d'une application avec SQLAlchemy

Voici comment s'organise typiquement une application Python utilisant SQLAlchemy :

```
mon_application/
│
├── models.py          # Définition des modèles (tables)
├── database.py        # Configuration de la connexion
├── main.py            # Logique principale de l'application
│
├── alembic/           # Migrations (évolution du schéma)
│   └── versions/
│
└── ma_base.db         # Fichier SQLite (créé automatiquement)
```

**Exemple de structure :**

```python
# database.py - Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///ma_base.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# models.py - Modèles
from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    email = Column(String(100))

# main.py - Utilisation
from database import Session, engine, Base
from models import User

# Créer les tables
Base.metadata.create_all(engine)

# Utiliser
session = Session()
user = User(nom="Alice", email="alice@example.com")
session.add(user)
session.commit()
```

## Ce que vous allez apprendre

Ce chapitre est divisé en trois parties complémentaires :

### 11.6.1 Introduction à SQLAlchemy
Vous apprendrez les fondamentaux :
- Installation et configuration
- Création de votre premier modèle
- Opérations CRUD (Create, Read, Update, Delete)
- Gestion des sessions et transactions
- Bonnes pratiques de base

### 11.6.2 Modèles et relations
Vous approfondirez la modélisation :
- Relations One-to-Many (un à plusieurs)
- Relations Many-to-Many (plusieurs à plusieurs)
- Relations One-to-One (un à un)
- Clés étrangères et contraintes
- Chargement optimisé des relations

### 11.6.3 Requêtes et migrations
Vous maîtriserez les techniques avancées :
- Requêtes complexes avec filtres multiples
- Jointures et agrégations
- Sous-requêtes et optimisations
- Migrations avec Alembic
- Évolution du schéma de base de données

## Prérequis

Pour suivre ce chapitre, vous devez être à l'aise avec :
- Les bases de Python (variables, fonctions, classes)
- La programmation orientée objet (héritage, attributs)
- Les concepts de base (fichiers, imports)

**Pas besoin de connaître SQL !** Nous allons tout vous enseigner progressivement.

## Installation

Avant de commencer, assurez-vous d'avoir installé SQLAlchemy :

```bash
# Installation de base
pip install sqlalchemy

# Pour les migrations (nous le verrons plus tard)
pip install alembic
```

**SQLite est déjà inclus** dans Python, aucune installation supplémentaire n'est nécessaire !

## Pourquoi ce choix pédagogique ?

Nous avons choisi SQLite + SQLAlchemy pour ce cours car :

**SQLite** parce que :
- Pas de configuration complexe
- Fonctionne immédiatement
- Parfait pour apprendre
- Utilisable en production pour de nombreux cas

**SQLAlchemy** parce que :
- C'est l'ORM de référence en Python
- Très bien documenté
- Large communauté
- Compétence valorisée professionnellement
- Facilement transférable à d'autres frameworks

## Conseil pour l'apprentissage

**Prenez votre temps !** Les bases de données et les ORM peuvent sembler complexes au début, mais :
1. Commencez par les exemples simples
2. Expérimentez avec le code
3. Ne cherchez pas à tout comprendre d'un coup
4. Pratiquez régulièrement
5. Consultez la documentation officielle en complément

**Astuce :** Créez un petit projet personnel (gestion de bibliothèque, carnet d'adresses, etc.) pendant que vous apprenez. Cela rendra les concepts plus concrets et mémorables.

## Ressources complémentaires

Pour aller plus loin après ce cours :

**Documentation officielle :**
- SQLAlchemy : https://docs.sqlalchemy.org/
- SQLite : https://www.sqlite.org/docs.html
- Alembic : https://alembic.sqlalchemy.org/

**Tutoriels et guides :**
- SQLAlchemy Tutorial (officiel)
- Real Python - SQLAlchemy guides
- Full Stack Python - SQLAlchemy section

**Communauté :**
- Stack Overflow (tag: sqlalchemy)
- Reddit: r/learnpython
- Discord Python Communities

## Prêt à commencer ?

Maintenant que vous comprenez **pourquoi** et **comment** nous allons utiliser les bases de données avec SQLAlchemy, il est temps de passer à la pratique !

Dans la prochaine section (11.6.1), nous allons :
- Créer notre première base de données
- Définir notre premier modèle
- Effectuer nos premières opérations CRUD
- Manipuler des données comme des objets Python

**Rappel important :** L'apprentissage des bases de données est un investissement. Une fois maîtrisé, ce sera l'un des outils les plus utiles de votre boîte à outils de développeur Python. Pratiquement toutes les applications web et de nombreuses applications de bureau utilisent des bases de données.

Alors, êtes-vous prêt à donner vie à vos données ? C'est parti ! 🚀

⏭️ [Introduction à SQLAlchemy](/11-developpement-web-et-apis/06.1-introduction-sqlalchemy.md)
