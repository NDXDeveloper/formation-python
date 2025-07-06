🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 11 : Développement web et APIs

## Introduction

Le développement web et la création d'APIs constituent aujourd'hui l'un des domaines d'application les plus importants de Python. Ce module vous permettra de comprendre les concepts fondamentaux du web, d'apprendre à créer des applications web simples et de maîtriser la communication entre applications via des APIs.

## Objectifs du module

À la fin de ce module, vous serez capable de :

- Comprendre les protocoles HTTP/HTTPS et leur fonctionnement
- Créer des applications web simples avec des frameworks Python
- Développer et consommer des APIs REST
- Gérer les données avec des bases de données relationnelles
- Implémenter l'authentification et la sécurité de base
- Déployer des applications web en production

## Prérequis

Avant de commencer ce module, vous devez maîtriser :

- Les concepts de programmation orientée objet (Module 3)
- La gestion des fichiers et formats de données (Module 4)
- Les modules et packages Python (Module 6)
- Les bibliothèques standard essentielles (Module 7)
- La gestion des erreurs et exceptions (Module 9)

## Vue d'ensemble du développement web avec Python

### Qu'est-ce que le développement web ?

Le développement web consiste à créer des applications accessibles via un navigateur web ou des clients HTTP. Ces applications peuvent être :

- **Sites web statiques** : pages HTML/CSS/JavaScript servies directement
- **Applications web dynamiques** : génération de contenu en temps réel
- **APIs (Application Programming Interfaces)** : services permettant la communication entre applications
- **Applications web complètes** : combinaison d'interface utilisateur et d'API

### Architecture client-serveur

Le web fonctionne selon un modèle client-serveur :

```
Client (Navigateur/App) <---> Serveur Web <---> Base de données
```

**Client** : envoie des requêtes HTTP
**Serveur** : traite les requêtes et renvoie des réponses
**Base de données** : stocke et récupère les données

### Protocole HTTP

HTTP (HyperText Transfer Protocol) est le protocole de communication du web :

**Méthodes HTTP principales :**
- `GET` : récupérer des données
- `POST` : créer de nouvelles ressources
- `PUT` : mettre à jour des ressources existantes
- `DELETE` : supprimer des ressources
- `PATCH` : mise à jour partielle

**Codes de statut courants :**
- `200 OK` : requête réussie
- `201 Created` : ressource créée avec succès
- `400 Bad Request` : requête malformée
- `401 Unauthorized` : authentification requise
- `404 Not Found` : ressource introuvable
- `500 Internal Server Error` : erreur serveur

### Formats de données web

**JSON (JavaScript Object Notation)** : format standard pour les APIs modernes
```json
{
  "id": 1,
  "nom": "Martin",
  "email": "martin@example.com",
  "actif": true
}
```

**HTML (HyperText Markup Language)** : langage de balisage pour les pages web
```html
<!DOCTYPE html>
<html>
<head>
    <title>Ma page</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <p>Contenu de la page</p>
</body>
</html>
```

## Écosystème Python pour le web

### Frameworks web populaires

**Micro-frameworks :**
- **Flask** : léger, flexible, idéal pour débuter
- **FastAPI** : moderne, avec support intégré d'OpenAPI
- **Bottle** : minimaliste, une seule dépendance

**Frameworks complets :**
- **Django** : batteries incluses, admin interface
- **Pyramid** : modulaire, adaptable
- **Tornado** : asynchrone, haute performance

### Bibliothèques essentielles

**Requêtes HTTP :**
- `requests` : client HTTP simple et élégant
- `httpx` : client HTTP moderne avec support async
- `urllib` : bibliothèque standard Python

**Bases de données :**
- `sqlite3` : base de données légère (standard)
- `SQLAlchemy` : ORM (Object-Relational Mapping)
- `psycopg2` : connecteur PostgreSQL
- `pymongo` : connecteur MongoDB

**Sérialisation et validation :**
- `json` : manipulation JSON (standard)
- `pydantic` : validation de données
- `marshmallow` : sérialisation/désérialisation

## Concepts fondamentaux

### Serveur WSGI

WSGI (Web Server Gateway Interface) est la spécification standard pour les applications web Python :

```python
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello World']
```

### Routage

Le routage associe des URLs à des fonctions Python :

```python
# Exemple conceptuel
routes = {
    '/': home_page,
    '/users': list_users,
    '/users/<id>': get_user,
}
```

### Templates

Les templates permettent de générer du HTML dynamiquement :

```html
<!-- Template exemple -->
<h1>Bonjour {{ nom }}</h1>
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### Middleware

Les middlewares traitent les requêtes avant qu'elles atteignent l'application :

```python
# Exemple de middleware pour logging
def logging_middleware(app):
    def wrapper(environ, start_response):
        print(f"Requête: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return app(environ, start_response)
    return wrapper
```

## APIs REST

### Principes REST

REST (Representational State Transfer) est un style architectural pour les APIs :

1. **Stateless** : chaque requête est indépendante
2. **Cacheable** : les réponses peuvent être mises en cache
3. **Uniform Interface** : interface cohérente
4. **Layered System** : architecture en couches

### Conception d'API REST

**Ressources et URLs :**
```
GET    /api/users          # Liste tous les utilisateurs
POST   /api/users          # Crée un nouvel utilisateur
GET    /api/users/123      # Récupère l'utilisateur 123
PUT    /api/users/123      # Met à jour l'utilisateur 123
DELETE /api/users/123      # Supprime l'utilisateur 123
```

**Réponses structurées :**
```json
{
  "status": "success",
  "data": {
    "id": 123,
    "nom": "Martin",
    "email": "martin@example.com"
  },
  "message": "Utilisateur récupéré avec succès"
}
```

## Sécurité web

### Authentification et autorisation

**Authentification** : vérifier l'identité
- Sessions et cookies
- Tokens JWT (JSON Web Tokens)
- OAuth 2.0

**Autorisation** : contrôler l'accès aux ressources
- Rôles et permissions
- Middleware d'autorisation

### Vulnérabilités communes

**Injection SQL** : utiliser des requêtes paramétrées
```python
# Vulnérable
query = f"SELECT * FROM users WHERE id = {user_id}"

# Sécurisé
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

**XSS (Cross-Site Scripting)** : échapper les données utilisateur
**CSRF (Cross-Site Request Forgery)** : utiliser des tokens CSRF
**HTTPS** : chiffrer les communications

## Outils de développement

### Serveur de développement

```bash
# Flask
python -m flask run

# Django
python manage.py runserver

# Serveur Python simple
python -m http.server 8000
```

### Débogage

```python
# Mode debug Flask
app.debug = True

# Logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Tests

```python
# Test d'API avec requests
import requests

def test_api():
    response = requests.get('http://localhost:5000/api/users')
    assert response.status_code == 200
    assert 'users' in response.json()
```

## Bonnes pratiques

### Structure de projet

```
mon_projet/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── templates/
├── tests/
├── requirements.txt
├── config.py
└── run.py
```

### Configuration

```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
```

### Gestion des erreurs

```python
from flask import jsonify

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

## Prochaines étapes

Ce module vous guidera à travers quatre sections principales :

1. **Frameworks web** : créer des applications avec Flask ou Django
2. **Client HTTP** : faire des requêtes avec la bibliothèque requests
3. **APIs REST** : développer et consommer des services web
4. **Bases de données** : intégrer SQLite pour la persistance

Chaque section combinera théorie et pratique avec des exemples concrets et des exercices progressifs.

---

*Prêt à plonger dans le monde du développement web avec Python ? Commençons par explorer les frameworks web !*

⏭️
