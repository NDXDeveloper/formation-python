🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11. Développement web et APIs

## Bienvenue dans le monde du développement web

Félicitations d'être arrivé jusqu'ici ! Vous avez acquis les fondamentaux de Python, maîtrisé la programmation orientée objet, appris à gérer les données et les fichiers, et découvert de nombreux concepts avancés. Maintenant, il est temps de faire quelque chose d'excitant : **créer des applications web** !

Ce chapitre marque un tournant dans votre apprentissage. Vous allez transformer vos compétences Python en applications accessibles depuis un navigateur web ou utilisables par d'autres programmes. C'est ici que Python rencontre Internet !

## Qu'est-ce que le développement web ?

Le **développement web** est l'art de créer des applications qui fonctionnent sur Internet ou sur des réseaux privés. Ces applications peuvent être :

### Sites web classiques
Des pages web que les utilisateurs visitent avec leur navigateur :
- Sites vitrines (présentation d'une entreprise)
- Blogs et sites de contenu
- E-commerce (boutiques en ligne)
- Réseaux sociaux
- Applications web interactives

### Applications web modernes (SPA)
Des applications qui fonctionnent dans le navigateur mais se comportent comme des applications natives :
- Gmail, Google Docs
- Twitter, Facebook
- Netflix, Spotify
- Slack, Discord

### APIs (Interfaces de programmation)
Des services web que d'autres programmes utilisent pour échanger des données :
- APIs de paiement (Stripe, PayPal)
- APIs de cartes (Google Maps)
- APIs de réseaux sociaux (Twitter, Facebook)
- APIs de données (météo, actualités)

## Pourquoi Python pour le web ?

Python est devenu l'un des langages les plus populaires pour le développement web, et pour de bonnes raisons :

### 1. Simplicité et productivité

Python permet de créer des applications web rapidement, avec moins de code que de nombreux autres langages. Ce qui prendrait des centaines de lignes en Java ou C# peut souvent se faire en quelques dizaines de lignes en Python.

### 2. Frameworks puissants

Python dispose d'excellents frameworks web qui facilitent énormément le travail :
- **Django** : Framework complet pour les sites web complexes
- **Flask** : Micro-framework flexible et léger
- **FastAPI** : Framework moderne pour créer des APIs ultra-rapides

### 3. Écosystème riche

Des milliers de bibliothèques Python sont disponibles pour :
- Se connecter à n'importe quelle base de données
- Gérer l'authentification et la sécurité
- Traiter des images et des fichiers
- Intégrer des services externes
- Déployer facilement en production

### 4. Polyvalence

Python peut gérer aussi bien :
- Le **backend** (côté serveur) : logique métier, bases de données
- Le **traitement de données** : analyses, rapports
- Les **APIs** : communication entre applications
- Le **machine learning** : intégration de modèles d'IA

### 5. Adoption massive

De nombreuses entreprises utilisent Python pour leur web :
- **Instagram** : Utilisé par des millions de personnes (Django)
- **Spotify** : Recommandations musicales (Flask)
- **Netflix** : Analyses de données et APIs
- **Uber** : Services backend (FastAPI)
- **Dropbox** : Infrastructure serveur

## Le modèle client-serveur : comprendre les bases

Avant de plonger dans le code, il est essentiel de comprendre comment fonctionne le web.

### Schéma simple

```
┌─────────────────┐                  ┌─────────────────┐
│                 │                  │                 │
│     CLIENT      │  ───Requête────→ │     SERVEUR     │
│   (Navigateur)  │                  │     (Python)    │
│                 │  ←──Réponse───── │                 │
│                 │                  │                 │
└─────────────────┘                  └─────────────────┘
```

### Le client

Le **client** est généralement un navigateur web (Chrome, Firefox, Safari) ou une application mobile. C'est ce que l'utilisateur voit et avec quoi il interagit.

**Rôle du client :**
- Afficher l'interface utilisateur
- Envoyer des requêtes au serveur
- Recevoir et afficher les réponses
- Gérer les interactions utilisateur

### Le serveur

Le **serveur** est un ordinateur qui héberge votre application Python. Il attend les requêtes des clients et leur répond.

**Rôle du serveur :**
- Recevoir et traiter les requêtes
- Exécuter la logique métier (calculs, validations)
- Accéder aux bases de données
- Générer et envoyer des réponses

### Une conversation simple

Voici un exemple de dialogue client-serveur :

```
Client : "Bonjour serveur, donne-moi la liste des produits"  
Serveur : "Voici les produits : [Produit1, Produit2, Produit3]"  

Client : "Je veux acheter le Produit2"  
Serveur : "D'accord, Produit2 ajouté à votre panier"  

Client : "Montre-moi mon panier"  
Serveur : "Votre panier contient : [Produit2], Total: 29,99€"  
```

Votre code Python gère toute la logique du serveur !

## Qu'est-ce qu'une API ?

Le terme **API** (Application Programming Interface) revient constamment dans le développement web moderne. Comprendre ce concept est essentiel.

### Définition simple

Une **API** est comme un serveur dans un restaurant :

- Vous (le client) ne pouvez pas aller directement en cuisine
- Le serveur (l'API) prend votre commande
- Il transmet la commande à la cuisine (le système backend)
- Il vous apporte votre plat (les données)

Une API est donc une **interface** qui permet à des programmes de communiquer entre eux.

### API Web (ou API REST)

Une **API Web** utilise le protocole HTTP (le même que les sites web) pour échanger des données. Au lieu de renvoyer des pages HTML, elle renvoie généralement des données au format JSON.

**Exemple de requête à une API :**
```
GET https://api.meteo.com/ville/paris
```

**Réponse de l'API (JSON) :**
```json
{
  "ville": "Paris",
  "temperature": 18,
  "conditions": "Nuageux",
  "humidite": 65
}
```

### Pourquoi créer des APIs ?

Les APIs sont partout dans le développement moderne :

**1. Applications mobiles**
Les apps iOS/Android communiquent avec un serveur via une API :
```
App mobile → API Python → Base de données
```

**2. Applications web modernes (SPA)**
Les applications React/Vue/Angular utilisent des APIs :
```
Frontend JavaScript → API Python → Base de données
```

**3. Intégration entre systèmes**
Différents services communiquent via des APIs :
```
Votre app → API de paiement Stripe → Transaction  
Votre app → API Google Maps → Affichage carte  
```

**4. Microservices**
Une application complexe divisée en petits services :
```
Service Utilisateurs (API) ←→ Service Commandes (API) ←→ Service Paiements (API)
```

**5. Partage de données**
Permettre à d'autres développeurs d'utiliser vos données/services :
```
API Météo publique ← Développeurs externes  
API Twitter ← Applications tierces  
```

## Les deux approches du développement web avec Python

Il existe deux grandes approches pour développer des applications web avec Python :

### Approche 1 : Applications web traditionnelles (Full-Stack)

Le serveur Python génère les pages HTML complètes et les envoie au navigateur.

```
Navigateur → Serveur Python → Génère HTML → Envoie au navigateur
```

**Frameworks typiques :** Django, Flask (avec templates)

**Avantages :**
- ✅ Architecture simple et directe
- ✅ Tout géré par Python (HTML, CSS, logique)
- ✅ Bon pour le SEO (référencement)
- ✅ Moins de complexité frontend

**Cas d'usage :**
- Sites vitrines
- Blogs
- Tableaux de bord d'administration
- Applications internes d'entreprise

### Approche 2 : API Backend + Frontend séparé (Architecture moderne)

Le serveur Python ne fait qu'une API qui envoie des données JSON. Le frontend (React, Vue, Angular) gère l'affichage.

```
Frontend JavaScript → API Python (JSON) → Base de données
```

**Frameworks typiques :** FastAPI, Flask (API mode), Django REST Framework

**Avantages :**
- ✅ Séparation claire frontend/backend
- ✅ Réutilisabilité (une API pour web + mobile)
- ✅ Équipes spécialisées possibles
- ✅ Applications plus interactives
- ✅ Meilleures performances

**Cas d'usage :**
- Applications web modernes (SPA)
- Applications mobiles
- Microservices
- APIs publiques

### Quelle approche choisir ?

```
┌─────────────────────────────────────────────────────┐
│          Choisir son architecture web               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Site vitrine simple → Approche traditionnelle      │
│  Blog, portfolio → Approche traditionnelle          │
│  Application interactive → API + Frontend           │
│  App mobile + web → API + Frontend                  │
│  Microservices → API                                │
│  Projet avec équipes séparées → API + Frontend      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Les protocoles et standards du web

Pour développer des applications web, vous devez comprendre quelques protocoles de base.

### HTTP : Le protocole du web

**HTTP** (HyperText Transfer Protocol) est le protocole qui permet la communication sur le web.

**Méthodes HTTP principales :**

| Méthode | Usage | Exemple |
|---------|-------|---------|
| **GET** | Récupérer des données | Afficher une page, lire des articles |
| **POST** | Créer des données | Soumettre un formulaire, créer un compte |
| **PUT** | Modifier complètement | Mettre à jour un profil utilisateur |
| **PATCH** | Modifier partiellement | Changer juste le nom d'utilisateur |
| **DELETE** | Supprimer des données | Supprimer un article, fermer un compte |

**Codes de statut HTTP :**

| Code | Signification | Exemple |
|------|---------------|---------|
| **200** | OK | Requête réussie |
| **201** | Created | Ressource créée avec succès |
| **400** | Bad Request | Données invalides |
| **401** | Unauthorized | Authentification requise |
| **403** | Forbidden | Accès refusé |
| **404** | Not Found | Ressource introuvable |
| **500** | Server Error | Erreur côté serveur |

### JSON : Le format d'échange de données

**JSON** (JavaScript Object Notation) est le format standard pour échanger des données entre applications web.

**Exemple de JSON :**
```json
{
  "utilisateur": {
    "id": 123,
    "nom": "Alice Dupont",
    "email": "alice@example.com",
    "age": 28,
    "actif": true,
    "roles": ["utilisateur", "editeur"],
    "adresse": {
      "rue": "123 rue de la Paix",
      "ville": "Paris",
      "code_postal": "75001"
    }
  }
}
```

JSON ressemble beaucoup aux dictionnaires Python ! Python peut facilement convertir entre les deux :

```python
import json

# Python dict → JSON
data = {"nom": "Alice", "age": 28}  
json_string = json.dumps(data)  

# JSON → Python dict
data = json.loads(json_string)
```

### REST : Une architecture pour les APIs

**REST** (Representational State Transfer) est un style d'architecture pour concevoir des APIs.

**Principes REST :**

1. **Ressources identifiées par URLs**
   - `/utilisateurs` - Liste des utilisateurs
   - `/utilisateurs/123` - Utilisateur avec l'ID 123
   - `/articles/456/commentaires` - Commentaires de l'article 456

2. **Utilisation des méthodes HTTP**
   - `GET /utilisateurs` - Lire tous les utilisateurs
   - `POST /utilisateurs` - Créer un utilisateur
   - `PUT /utilisateurs/123` - Modifier l'utilisateur 123
   - `DELETE /utilisateurs/123` - Supprimer l'utilisateur 123

3. **Format de données standardisé (JSON)**

4. **Sans état (Stateless)**
   - Chaque requête est indépendante
   - Le serveur ne garde pas de session

**Exemple d'API REST complète :**

```
GET    /api/articles          → Lire tous les articles  
GET    /api/articles/5        → Lire l'article 5  
POST   /api/articles          → Créer un article  
PUT    /api/articles/5        → Modifier l'article 5  
DELETE /api/articles/5        → Supprimer l'article 5  
GET    /api/articles/5/auteur → Lire l'auteur de l'article 5  
```

## Les bases de données dans le développement web

Presque toutes les applications web utilisent une base de données pour stocker les informations.

### Pourquoi une base de données ?

- 💾 **Persistance** : Les données survivent aux redémarrages
- 🔍 **Recherche** : Trouver rapidement des informations
- 🔒 **Intégrité** : Garantir la cohérence des données
- 👥 **Multi-utilisateurs** : Plusieurs utilisateurs simultanés
- 📊 **Relations** : Lier différents types de données

### Types de bases de données

**Bases de données SQL (relationnelles) :**
- **PostgreSQL** - Très populaire, robuste, open source
- **MySQL** - Largement utilisé, simple
- **SQLite** - Léger, parfait pour débuter
- **SQL Server** - Microsoft

**Bases de données NoSQL :**
- **MongoDB** - Documents JSON
- **Redis** - Clé-valeur, cache rapide
- **Cassandra** - Big data, très scalable

### Python et les bases de données

Python peut se connecter à n'importe quelle base de données :

```python
# Avec SQLite (inclus dans Python)
import sqlite3

# Avec PostgreSQL
import psycopg2

# Avec MongoDB
from pymongo import MongoClient
```

Mais nous utiliserons généralement un **ORM** (Object-Relational Mapping) qui simplifie le travail :

```python
# Avec SQLAlchemy (ORM populaire)
class Utilisateur(Base):
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)

# Créer un utilisateur
utilisateur = Utilisateur(nom="Alice", email="alice@example.com")  
session.add(utilisateur)  
```

## Sécurité dans le développement web

La sécurité est **critique** dans le développement web. Voici les menaces principales à connaître :

### Menaces courantes

**1. Injection SQL**
Un attaquant insère du code SQL malveillant dans vos requêtes.
- ✅ **Protection** : Utiliser des requêtes paramétrées, ORM

**2. XSS (Cross-Site Scripting)**
Injection de JavaScript malveillant dans vos pages.
- ✅ **Protection** : Échapper le HTML, valider les entrées

**3. CSRF (Cross-Site Request Forgery)**
Forcer un utilisateur authentifié à faire des actions non désirées.
- ✅ **Protection** : Tokens CSRF, SameSite cookies

**4. Authentification faible**
Mots de passe faibles, sessions non sécurisées.
- ✅ **Protection** : Hash des mots de passe, JWT, OAuth2

**5. Exposition de données sensibles**
Fuites d'informations confidentielles.
- ✅ **Protection** : Chiffrement, HTTPS, variables d'environnement

### Bonnes pratiques de sécurité

```
✅ Toujours utiliser HTTPS en production
✅ Ne jamais stocker de mots de passe en clair
✅ Valider toutes les entrées utilisateur
✅ Utiliser des frameworks qui protègent par défaut
✅ Garder les dépendances à jour
✅ Ne jamais exposer les clés secrètes dans le code
✅ Implémenter des limites de taux (rate limiting)
```

Les frameworks Python comme Django et FastAPI incluent de nombreuses protections par défaut !

## Déploiement : du développement à la production

Créer votre application en local n'est que la première étape. Il faut ensuite la **déployer** pour la rendre accessible sur Internet.

### Environnements

**Développement (local) :**
- Sur votre ordinateur
- Pour coder et tester
- Erreurs visibles et détaillées

**Staging (pré-production) :**
- Environnement de test identique à la production
- Pour tester avant mise en ligne

**Production :**
- Serveur accessible publiquement
- Configuration optimisée pour performances et sécurité

### Options de déploiement

**Solutions cloud simples :**
- **Heroku** - Très simple, payant (plans à partir de 5$/mois)
- **PythonAnywhere** - Spécialisé Python
- **Railway** - Moderne et facile
- **Render** - Alternative à Heroku

**Cloud providers majeurs :**
- **AWS** (Amazon) - Le plus complet
- **Google Cloud** - Puissant et performant
- **Azure** (Microsoft) - Intégration Microsoft

**Containerisation :**
- **Docker** - Empaqueter votre application
- **Kubernetes** - Orchestration de containers

**Serverless :**
- **AWS Lambda** - Fonctions sans serveur
- **Google Cloud Functions**
- **Azure Functions**

## Ce que vous allez apprendre dans ce chapitre

Ce chapitre est divisé en plusieurs sections progressives qui vous emmèneront du débutant au développeur web capable de créer des APIs professionnelles.

### 11.1 Introduction aux frameworks web
Vous découvrirez les principaux frameworks Python (Django, Flask, FastAPI) et comprendrez comment choisir le bon outil pour votre projet.

### 11.2 FastAPI - Framework moderne et asynchrone
Vous apprendrez à créer des APIs ultra-rapides avec FastAPI :
- Installation et premier projet
- Validation automatique avec Pydantic
- Programmation asynchrone pour les performances

### 11.3 Flask - Micro-framework léger
Vous découvrirez Flask, un framework minimaliste et flexible parfait pour débuter ou créer des applications simples.

### 11.4 Requêtes HTTP avec requests
Vous apprendrez à communiquer avec d'autres APIs et services web, à envoyer et recevoir des données.

### 11.5 Création et consommation d'APIs REST
Vous maîtriserez les concepts REST et créerez des APIs complètes avec tous les endpoints nécessaires.

### 11.6 Bases de données et ORM (SQLite + SQLAlchemy)
Vous apprendrez à :
- Connecter votre application à une base de données
- Utiliser SQLAlchemy pour manipuler les données
- Créer des modèles et des relations
- Effectuer des requêtes complexes

## Compétences que vous développerez

À la fin de ce chapitre, vous serez capable de :

**Compétences techniques :**
- ✅ Créer des APIs REST complètes et fonctionnelles
- ✅ Gérer l'authentification et l'autorisation
- ✅ Se connecter et manipuler des bases de données
- ✅ Valider automatiquement les données
- ✅ Documenter automatiquement vos APIs
- ✅ Gérer les erreurs de manière professionnelle
- ✅ Optimiser les performances avec l'asynchrone
- ✅ Tester vos applications web
- ✅ Déployer en production

**Compétences conceptuelles :**
- ✅ Comprendre l'architecture client-serveur
- ✅ Maîtriser les principes REST
- ✅ Concevoir des APIs cohérentes et maintenables
- ✅ Implémenter des bonnes pratiques de sécurité
- ✅ Gérer les bases de données relationnelles

## Projets que vous pourrez créer

Avec les compétences de ce chapitre, vous pourrez développer :

**APIs et backends :**
- 📱 Backend pour application mobile
- 💬 API de chat en temps réel
- 🛒 API e-commerce
- 📝 API de gestion de tâches
- 🔐 Service d'authentification

**Applications web :**
- 📰 Blog ou site de contenu
- 📊 Tableau de bord analytique
- 🗂️ Gestionnaire de projets
- 💼 Application métier interne
- 🎓 Plateforme d'apprentissage

**Intégrations et microservices :**
- 🔗 Intégration de services tiers
- ⚙️ Webhooks et automatisations
- 🎯 Microservices spécialisés
- 🤖 Bot avec APIs

## Prérequis pour ce chapitre

Pour tirer le meilleur parti de ce chapitre, assurez-vous de maîtriser :

**Indispensable :**
- ✅ Bases de Python (variables, fonctions, boucles, conditions)
- ✅ Programmation orientée objet (classes, objets, héritage)
- ✅ Gestion des erreurs (try/except)
- ✅ Manipulation de dictionnaires et de listes
- ✅ Compréhension des décorateurs

**Utile mais pas obligatoire :**
- 📚 Notions de JSON
- 📚 Bases de SQL
- 📚 Utilisation du terminal
- 📚 Concepts HTTP de base

**Pas nécessaire :**
- ❌ Connaissance de JavaScript ou HTML/CSS
- ❌ Expérience en développement web
- ❌ Maîtrise des bases de données

Tout sera expliqué progressivement !

## Conseils pour réussir ce chapitre

### 1. Pratiquez, pratiquez, pratiquez

Le développement web s'apprend en faisant. N'hésitez pas à :
- Taper le code vous-même (pas de copier-coller)
- Expérimenter et modifier les exemples
- Créer vos propres petits projets parallèles

### 2. Utilisez les outils de développement

Familiarisez-vous avec :
- Les DevTools de votre navigateur (F12)
- Postman ou Insomnia pour tester les APIs
- La documentation interactive de FastAPI

### 3. Lisez les erreurs attentivement

Les messages d'erreur sont vos amis ! Ils vous indiquent précisément ce qui ne va pas.

### 4. Construisez progressivement

Commencez simple et ajoutez des fonctionnalités petit à petit. Ne cherchez pas à tout faire en même temps.

### 5. Consultez la documentation

La documentation officielle des frameworks est excellente. N'hésitez pas à la consulter régulièrement.

### 6. Testez constamment

Testez chaque fonctionnalité au fur et à mesure. Ne codez pas pendant des heures avant de tester.

## L'état d'esprit du développeur web

Le développement web peut être challengeant, mais aussi extrêmement gratifiant. Voici quelques principes à garder en tête :

**🎯 Pensez utilisateur**
Votre API ou application doit être intuitive et facile à utiliser.

**🔒 La sécurité d'abord**
Ne négligez jamais la sécurité, même pour un projet de test.

**📖 Documentez votre code**
Une bonne documentation facilite la maintenance et la collaboration.

**🧪 Testez tout**
Les tests vous font gagner du temps et évitent les bugs en production.

**🔄 Itérez**
Commencez simple, puis améliorez progressivement.

**🤝 Partagez et apprenez**
La communauté Python est formidable. N'hésitez pas à poser des questions !

## Ressources complémentaires

Pour aller plus loin, voici quelques ressources utiles :

**Documentation officielle :**
- FastAPI : https://fastapi.tiangolo.com/
- Flask : https://flask.palletsprojects.com/
- Django : https://www.djangoproject.com/
- SQLAlchemy : https://www.sqlalchemy.org/

**Apprendre les APIs REST :**
- REST API Tutorial : https://restfulapi.net/
- HTTP Status Codes : https://httpstatuses.com/

**Tester les APIs :**
- Postman : https://www.postman.com/
- Insomnia : https://insomnia.rest/

**Déploiement :**
- Heroku : https://www.heroku.com/
- Railway : https://railway.app/
- Render : https://render.com/

## Conclusion de l'introduction

Le développement web avec Python est un domaine passionnant et en pleine expansion. Que vous souhaitiez créer votre propre startup, travailler comme développeur backend, ou simplement donner vie à vos idées, les compétences que vous allez acquérir dans ce chapitre sont précieuses et très demandées sur le marché.

Python excelle dans le développement web grâce à sa simplicité, ses frameworks puissants, et son écosystème riche. Vous allez découvrir qu'avec quelques lignes de code Python, vous pouvez créer des applications impressionnantes.

Le voyage commence maintenant ! Dans la prochaine section, nous allons explorer les différents frameworks web Python et comprendre lequel choisir selon vos besoins.

**Prêt à construire le web avec Python ? C'est parti ! 🚀**

---


⏭️ [Introduction aux frameworks web](/11-developpement-web-et-apis/01-introduction-frameworks-web.md)
