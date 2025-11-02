🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.1 Introduction aux frameworks web

## Qu'est-ce qu'un framework web ?

Un **framework web** est un ensemble d'outils et de bibliothèques qui facilite la création d'applications web. Plutôt que de tout coder à partir de zéro, un framework vous fournit une structure et des fonctionnalités prêtes à l'emploi pour gérer les aspects courants du développement web.

Imaginez que vous voulez construire une maison : vous pourriez fabriquer chaque brique et chaque outil vous-même, ou bien utiliser des matériaux et des outils déjà prêts. Le framework web, c'est comme avoir une boîte à outils complète avec des fondations solides pour construire votre application.

## Comprendre le fonctionnement du web

Avant de plonger dans les frameworks, il est important de comprendre quelques concepts de base :

### Le modèle Client-Serveur

Le web fonctionne selon un modèle **client-serveur** :

- **Le client** : C'est votre navigateur web (Chrome, Firefox, Safari, etc.). Il envoie des **requêtes** pour demander des pages ou des données.
- **Le serveur** : C'est un ordinateur qui héberge votre application web. Il reçoit les requêtes et renvoie des **réponses** (pages HTML, données JSON, etc.).

```
┌─────────────┐                    ┌─────────────┐
│   Client    │   ──── Requête ──→ │   Serveur   │
│ (Navigateur)│                    │   (Python)  │
│             │   ←── Réponse ──── │             │
└─────────────┘                    └─────────────┘
```

### Le protocole HTTP

Les communications entre le client et le serveur utilisent le protocole **HTTP** (HyperText Transfer Protocol). Ce protocole définit différents types de requêtes :

- **GET** : Récupérer des données (afficher une page)
- **POST** : Envoyer des données (soumettre un formulaire)
- **PUT** : Mettre à jour des données
- **DELETE** : Supprimer des données

### Les URLs et les routes

Une **URL** (Uniform Resource Locator) est l'adresse d'une ressource sur le web :

```
https://monsite.com/articles/123
│      │          │        │
│      │          │        └─ Paramètre (ID de l'article)
│      │          └────────── Route/Chemin
│      └───────────────────── Nom de domaine
└──────────────────────────── Protocole
```

Les frameworks web utilisent un système de **routes** pour associer des URLs à des fonctions Python spécifiques.

## Pourquoi utiliser un framework web ?

Les frameworks web Python vous évitent de réinventer la roue en fournissant :

### 1. Gestion des routes et des requêtes HTTP

Au lieu d'écrire du code complexe pour analyser les requêtes HTTP, le framework le fait pour vous :

```python
# Sans framework : code complexe et fastidieux
# Avec framework : simple et lisible
@app.route('/hello')
def hello():
    return "Bonjour le monde !"
```

### 2. Gestion des templates HTML

Les frameworks permettent de créer des pages HTML dynamiques en mélangeant du HTML avec des variables Python.

### 3. Sécurité intégrée

Protection contre les attaques courantes (injection SQL, XSS, CSRF, etc.) sans avoir à tout implémenter manuellement.

### 4. Gestion de session et authentification

Systèmes prêts à l'emploi pour gérer les connexions utilisateurs, les cookies, les sessions, etc.

### 5. Interaction avec les bases de données

Outils pour se connecter facilement à des bases de données et manipuler les données.

### 6. Validation des données

Vérification automatique que les données envoyées par l'utilisateur sont valides et sécurisées.

## Les principaux frameworks web Python

Python dispose de plusieurs frameworks web excellents, chacun avec ses propres caractéristiques :

### Django - Le framework "batteries incluses"

**Django** est le framework web Python le plus populaire et le plus complet.

**Caractéristiques :**
- Framework **full-stack** : tout est inclus (ORM, admin, authentification, etc.)
- Idéal pour les **projets complexes** et de grande envergure
- Architecture **MTV** (Model-Template-View), similaire au pattern MVC
- Panel d'administration automatique
- ORM puissant pour gérer les bases de données
- Grande communauté et documentation exhaustive

**Quand l'utiliser :**
- Applications web complètes (sites e-commerce, réseaux sociaux, etc.)
- Projets nécessitant une base solide et évolutive
- Équipes cherchant des conventions établies

**Exemple simple :**
```python
# views.py
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Bienvenue sur mon site Django !")
```

### Flask - Le micro-framework flexible

**Flask** est un framework minimaliste et flexible.

**Caractéristiques :**
- Framework **minimaliste** : fournit l'essentiel, vous ajoutez ce dont vous avez besoin
- Très **flexible** et modulaire
- Courbe d'apprentissage douce
- Idéal pour les petits projets et les APIs
- Grande liberté dans l'organisation du code

**Quand l'utiliser :**
- Petites applications web
- APIs REST
- Prototypes rapides
- Projets nécessitant une grande flexibilité

**Exemple simple :**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Bienvenue sur mon site Flask !"

if __name__ == '__main__':
    app.run()
```

### FastAPI - Le framework moderne et rapide

**FastAPI** est un framework moderne et performant, spécialisé dans la création d'APIs.

**Caractéristiques :**
- Framework **moderne** utilisant les dernières fonctionnalités Python (async/await, type hints)
- Extrêmement **rapide** (performances comparables à Node.js)
- Validation automatique des données avec **Pydantic**
- Documentation API automatique (Swagger/OpenAPI)
- Conçu pour la programmation **asynchrone**
- Excellent pour les **APIs REST** et les microservices

**Quand l'utiliser :**
- APIs REST modernes
- Applications nécessitant de hautes performances
- Projets utilisant la programmation asynchrone
- Microservices

**Exemple simple :**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def accueil():
    return {"message": "Bienvenue sur mon API FastAPI !"}
```

### Comparaison rapide

| Critère | Django | Flask | FastAPI |
|---------|--------|-------|---------|
| **Type** | Full-stack | Micro-framework | Framework API |
| **Courbe d'apprentissage** | Moyenne | Facile | Moyenne |
| **Flexibilité** | Moyenne | Très élevée | Élevée |
| **Performance** | Bonne | Bonne | Excellente |
| **Async natif** | Partiellement | Non | Oui |
| **Cas d'usage typique** | Sites web complets | Petites apps, APIs | APIs modernes, microservices |
| **Batteries incluses** | ✅ Oui | ❌ Non | ⚠️ Pour les APIs |

## Concepts communs aux frameworks web

Quel que soit le framework choisi, vous retrouverez certains concepts fondamentaux :

### 1. Les routes (Routing)

Une route associe une URL à une fonction Python qui génère la réponse :

```python
@app.route('/articles')  # Route
def liste_articles():    # Fonction associée
    return "Liste des articles"
```

### 2. Les vues (Views)

Les **vues** sont les fonctions qui traitent les requêtes et retournent des réponses. Elles contiennent la logique métier de votre application.

### 3. Les templates

Les **templates** sont des fichiers HTML avec des parties dynamiques qui seront remplacées par des données Python :

```html
<h1>Bonjour {{ nom_utilisateur }} !</h1>
<p>Vous avez {{ nombre_messages }} nouveaux messages.</p>
```

### 4. Les modèles (Models)

Les **modèles** représentent la structure de vos données et facilitent l'interaction avec la base de données :

```python
class Article:
    titre: str
    contenu: str
    date_publication: datetime
```

### 5. Les middlewares

Les **middlewares** sont des fonctions qui s'exécutent avant ou après le traitement d'une requête (pour la journalisation, l'authentification, etc.).

## Anatomie d'une requête web

Comprendre le cycle de vie d'une requête aide à mieux appréhender les frameworks :

```
1. L'utilisateur entre une URL dans son navigateur
   ↓
2. Le navigateur envoie une requête HTTP au serveur
   ↓
3. Le framework reçoit la requête
   ↓
4. Le framework identifie la route correspondante
   ↓
5. La fonction de vue associée est exécutée
   ↓
6. La vue peut accéder à la base de données
   ↓
7. La vue génère une réponse (HTML, JSON, etc.)
   ↓
8. Le framework envoie la réponse au navigateur
   ↓
9. Le navigateur affiche le résultat à l'utilisateur
```

## Qu'allez-vous apprendre dans ce chapitre ?

Dans les sections suivantes, vous découvrirez :

- **FastAPI** : Comment créer des APIs modernes et performantes
- **Flask** : Comment construire des applications web légères
- **Requêtes HTTP** : Comment communiquer avec d'autres services
- **APIs REST** : Comment créer et consommer des interfaces de programmation
- **Bases de données** : Comment stocker et récupérer des données avec SQLAlchemy

## Prérequis pour ce chapitre

Avant de commencer le développement web avec Python, assurez-vous de bien maîtriser :

- ✅ Les bases de Python (variables, fonctions, classes)
- ✅ La programmation orientée objet
- ✅ La gestion des erreurs
- ✅ Les décorateurs (concept utilisé pour définir les routes)
- ✅ Les notions de base de HTML (utile mais pas indispensable)

## Choisir son premier framework

Pour débuter, nous vous recommandons de commencer par **FastAPI** si vous voulez créer des APIs, ou **Flask** si vous préférez créer des sites web complets avec des pages HTML.

**FastAPI** est le choix idéal si :
- Vous voulez apprendre les pratiques modernes
- Vous êtes intéressé par la création d'APIs
- Vous aimez la validation automatique et la documentation

**Flask** est le choix idéal si :
- Vous débutez complètement en développement web
- Vous voulez comprendre les fondamentaux sans complexité
- Vous préférez une approche progressive et simple

**Django** peut venir plus tard, une fois que vous aurez compris les concepts de base avec un framework plus simple.

## Conclusion

Les frameworks web Python sont des outils puissants qui simplifient grandement le développement d'applications web. Ils gèrent les aspects techniques complexes pour que vous puissiez vous concentrer sur la logique métier de votre application.

Dans les prochaines sections, vous apprendrez à créer vos premières applications web avec FastAPI et Flask, en commençant par des exemples simples puis en progressant vers des concepts plus avancés.

Le développement web peut sembler intimidant au début, mais avec de la pratique et un bon framework, vous serez rapidement capable de créer des applications impressionnantes !

---

⏭️ [FastAPI - Framework moderne et asynchrone](/11-developpement-web-et-apis/02-fastapi-framework-moderne.md)
