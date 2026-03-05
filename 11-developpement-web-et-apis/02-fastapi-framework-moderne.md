🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.2 FastAPI - Framework moderne et asynchrone

## Introduction

**FastAPI** est un framework web Python moderne, rapide et élégant, spécialement conçu pour créer des APIs. Lancé en 2018 par Sebastián Ramírez, FastAPI est rapidement devenu l'un des frameworks Python les plus populaires et les plus appréciés de la communauté.

Le nom "FastAPI" n'est pas un hasard : ce framework est réellement rapide, tant en termes de performances d'exécution que de vitesse de développement. C'est l'outil idéal pour créer des APIs REST modernes et performantes.

## Qu'est-ce qui rend FastAPI spécial ?

FastAPI se distingue des autres frameworks Python par plusieurs caractéristiques uniques qui en font un choix excellent pour le développement d'APIs modernes.

### 1. Performances exceptionnelles

FastAPI est l'un des frameworks Python les plus rapides disponibles. Ses performances sont comparables à celles de Node.js et de Go, deux langages réputés pour leur vitesse. Cette rapidité est rendue possible grâce à :

- L'utilisation de **Starlette** pour les fonctionnalités web
- Le support natif de la **programmation asynchrone** (async/await)
- L'architecture optimisée pour les opérations I/O

### 2. Validation automatique des données

Grâce à **Pydantic**, FastAPI valide automatiquement toutes les données entrantes et sortantes. Plus besoin d'écrire du code de validation manuellement ! Si un client envoie des données incorrectes, FastAPI rejette automatiquement la requête avec un message d'erreur clair.

**Exemple :**
```python
class Utilisateur(BaseModel):
    nom: str
    age: int
    email: str

@app.post("/utilisateurs")
def creer_utilisateur(utilisateur: Utilisateur):
    return utilisateur
```

Si quelqu'un envoie un âge sous forme de texte au lieu d'un nombre, FastAPI le détecte et renvoie une erreur automatiquement !

### 3. Documentation interactive automatique

C'est l'une des fonctionnalités les plus impressionnantes de FastAPI : la documentation de votre API est générée **automatiquement** ! Dès que vous créez une route, elle apparaît dans une interface interactive où vous pouvez tester vos endpoints directement depuis votre navigateur.

FastAPI génère deux interfaces de documentation :
- **Swagger UI** (accessible via `/docs`) - Interface moderne et interactive
- **ReDoc** (accessible via `/redoc`) - Documentation alternative plus épurée

### 4. Type hints Python natifs

FastAPI exploite pleinement les **annotations de type** Python (type hints) introduites dans Python 3.6+. Cela signifie que vous utilisez la syntaxe Python standard, et FastAPI fait le reste :

```python
@app.get("/items/{item_id}")
def lire_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

Ces annotations servent à :
- Valider automatiquement les données
- Générer la documentation
- Améliorer l'auto-complétion dans votre IDE
- Détecter les erreurs avant l'exécution

### 5. Programmation asynchrone native

FastAPI est conçu dès le départ pour supporter la **programmation asynchrone**. Vous pouvez écrire du code asynchrone avec `async` et `await` de manière naturelle :

```python
@app.get("/data")
async def obtenir_data():
    data = await recuperer_depuis_base_de_donnees()
    return data
```

Cela permet de gérer des milliers de connexions simultanées avec une excellente performance.

### 6. Basé sur des standards

FastAPI respecte et implémente des standards ouverts :
- **OpenAPI** (anciennement Swagger) pour la spécification des APIs
- **JSON Schema** pour la validation des données
- **OAuth2** pour l'authentification
- **JWT** (JSON Web Tokens) pour les tokens d'accès

Cela garantit la compatibilité avec de nombreux outils et services existants.

## Pourquoi choisir FastAPI ?

### Pour les débutants

Si vous débutez en développement web, FastAPI est un excellent choix car :

- ✅ **Syntaxe intuitive** : Très facile à apprendre et à comprendre
- ✅ **Documentation excellente** : Tutoriels clairs et exemples nombreux
- ✅ **Erreurs explicites** : Messages d'erreur clairs qui vous aident à comprendre vos erreurs
- ✅ **Auto-complétion** : Votre éditeur vous guide grâce aux type hints
- ✅ **Moins de code** : Accomplissez plus avec moins de lignes

### Pour les développeurs expérimentés

Si vous avez déjà de l'expérience, FastAPI offre :

- ⚡ **Performances de production** : Prêt pour des applications à haute charge
- 🔧 **Flexibilité** : Architecture modulaire et extensible
- 🛡️ **Sécurité** : Mécanismes de sécurité intégrés
- 📊 **Type safety** : Détection des erreurs à la compilation
- 🔄 **Async/await** : Support complet de la programmation asynchrone

### Pour les projets professionnels

FastAPI est adapté aux environnements professionnels car :

- 📈 **Scalabilité** : Gère facilement la montée en charge
- 🏢 **Adopté par de grandes entreprises** : Microsoft, Uber, Netflix utilisent FastAPI
- 🧪 **Testabilité** : Facile à tester avec pytest
- 📖 **Documentation auto-générée** : Réduit le travail de documentation
- 🔒 **Maintenance** : Code propre et facile à maintenir

## Comparaison avec d'autres frameworks

Voyons comment FastAPI se positionne par rapport à Django et Flask, les deux autres frameworks Python populaires.

### FastAPI vs Django

**Django** est un framework **full-stack** très complet.

| Aspect | Django | FastAPI |
|--------|--------|---------|
| **Type** | Full-stack (tout inclus) | Spécialisé APIs |
| **Taille** | Lourd, beaucoup de fonctionnalités | Léger et focalisé |
| **Courbe d'apprentissage** | Plus longue | Plus courte |
| **Performance** | Bonne | Excellente |
| **Async natif** | Partiellement | Complètement |
| **Documentation auto** | Non | Oui |
| **Cas d'usage** | Sites web complets | APIs modernes |

**Quand choisir Django :** Pour créer un site web complet avec interface d'administration, authentification complète, et nombreuses fonctionnalités intégrées.

**Quand choisir FastAPI :** Pour créer des APIs REST performantes, des microservices, ou des backends pour applications mobiles/SPA.

### FastAPI vs Flask

**Flask** est un micro-framework minimaliste et flexible.

| Aspect | Flask | FastAPI |
|--------|-------|---------|
| **Type** | Micro-framework | Framework API |
| **Age** | Plus ancien (2010) | Plus récent (2018) |
| **Validation** | Manuelle | Automatique |
| **Documentation** | Manuelle | Automatique |
| **Type hints** | Optionnel | Central |
| **Async** | Via extensions | Natif |
| **Performance** | Bonne | Meilleure |

**Quand choisir Flask :** Pour des projets simples, quand vous voulez un contrôle total sur l'architecture, ou pour des applications web traditionnelles.

**Quand choisir FastAPI :** Pour des APIs modernes nécessitant validation automatique, documentation interactive, et hautes performances.

### Tableau récapitulatif

```
┌──────────────────────────────────────────────────────┐
│                Choix du framework                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Site web complet avec admin → Django                │
│  API REST moderne → FastAPI                          │
│  Application web simple → Flask                      │
│  Microservices haute performance → FastAPI           │
│  Prototype rapide flexible → Flask                   │
│  API asynchrone → FastAPI                            │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## Les bases techniques de FastAPI

FastAPI repose sur plusieurs bibliothèques et technologies clés.

### Starlette

**Starlette** est un framework ASGI léger qui fournit les fonctionnalités web de base. FastAPI est construit par-dessus Starlette et ajoute :
- La validation de données avec Pydantic
- La génération automatique de documentation
- La gestion de la sérialisation
- Des raccourcis et fonctionnalités supplémentaires

### Pydantic

**Pydantic** est une bibliothèque de validation de données utilisant les type hints Python. Elle permet de :
- Valider automatiquement les données
- Convertir les types
- Générer des schémas JSON
- Créer des modèles de données robustes

### ASGI

**ASGI** (Asynchronous Server Gateway Interface) est le successeur moderne de WSGI. C'est une spécification qui définit comment les serveurs web et les applications Python communiquent.

ASGI supporte :
- Les connexions HTTP/2
- Les WebSockets
- La programmation asynchrone
- Les connexions longues

**Note :** Flask utilise WSGI (synchrone), tandis que FastAPI utilise ASGI (asynchrone). Django supporte les deux (WSGI et ASGI).

### Uvicorn

**Uvicorn** est un serveur ASGI ultra-rapide qui fait tourner votre application FastAPI. C'est l'équivalent asynchrone de Gunicorn (pour Flask/Django).

## Architecture d'une application FastAPI

Une application FastAPI typique suit cette structure :

```
mon_projet/
│
├── main.py              # Point d'entrée de l'application
├── models.py            # Modèles Pydantic
├── routers/             # Routes organisées par domaine
│   ├── users.py
│   ├── items.py
│   └── auth.py
├── database.py          # Configuration base de données
├── dependencies.py      # Dépendances réutilisables
├── config.py           # Configuration de l'app
└── requirements.txt    # Dépendances Python
```

### Flux d'une requête

Voici ce qui se passe quand un client envoie une requête à votre API FastAPI :

```
1. Client envoie une requête HTTP
   ↓
2. Uvicorn (serveur ASGI) reçoit la requête
   ↓
3. FastAPI identifie la route correspondante
   ↓
4. FastAPI valide les paramètres avec Pydantic
   ↓
5. FastAPI exécute les dépendances (auth, DB, etc.)
   ↓
6. La fonction de vue est appelée
   ↓
7. FastAPI valide la réponse avec Pydantic
   ↓
8. FastAPI sérialise la réponse en JSON
   ↓
9. Uvicorn renvoie la réponse au client
```

Tout cela se fait automatiquement ! Vous n'avez qu'à écrire votre logique métier.

## Cas d'usage de FastAPI

FastAPI est particulièrement adapté pour :

### 1. APIs REST

C'est le cas d'usage principal de FastAPI. Parfait pour créer des APIs RESTful propres et performantes.

**Exemples :**
- API pour une application mobile
- Backend pour une application React/Vue/Angular
- API publique pour des développeurs tiers

### 2. Microservices

FastAPI est excellent pour créer des architectures microservices grâce à :
- Sa légèreté
- Ses performances
- Sa facilité de déploiement
- Son support de la documentation

### 3. Machine Learning et Data Science

FastAPI est très populaire dans le monde du ML/DS pour :
- Déployer des modèles en production
- Créer des APIs de prédiction
- Exposer des pipelines de traitement de données

**Exemples :**
- API de reconnaissance d'images
- Service de recommandation
- API d'analyse de sentiment

### 4. Applications temps réel

Grâce au support des WebSockets et de l'asynchrone :
- Chats en temps réel
- Notifications push
- Tableaux de bord en direct
- Applications collaboratives

### 5. Backends pour applications mobiles

FastAPI est idéal comme backend pour applications iOS/Android :
- API JSON simple et claire
- Authentification JWT intégrée
- Gestion des fichiers (uploads d'images)
- Push notifications

## Écosystème et communauté

### Popularité croissante

FastAPI a connu une croissance explosive depuis sa sortie :
- ⭐ Plus de 70 000 étoiles sur GitHub
- 📈 Adoption rapide par les entreprises
- 📚 Documentation traduite en plusieurs langues
- 🎓 Nombreux tutoriels et cours

### Extensions et intégrations

FastAPI s'intègre facilement avec de nombreux outils :

**Bases de données :**
- SQLAlchemy (SQL)
- Tortoise ORM (async ORM)
- Motor (MongoDB async)
- Redis (cache)

**Authentification :**
- OAuth2
- JWT
- Auth0
- Keycloak

**Déploiement :**
- Docker
- Kubernetes
- AWS Lambda
- Heroku
- Google Cloud Run

**Monitoring :**
- Prometheus
- Grafana
- Sentry
- New Relic

**Testing :**
- pytest
- TestClient (intégré à FastAPI)
- Locust (tests de charge)

## Les concepts clés à maîtriser

Pour devenir efficace avec FastAPI, vous devrez comprendre :

### 1. Type hints Python

```python
def calculer(a: int, b: int) -> int:
    return a + b
```

Les annotations de type sont au cœur de FastAPI.

### 2. Programmation asynchrone

```python
async def fonction_async():
    resultat = await operation_longue()
    return resultat
```

Comprendre `async` et `await` est essentiel pour les performances.

### 3. Modèles Pydantic

```python
class Utilisateur(BaseModel):
    nom: str
    age: int
```

Les modèles définissent la structure de vos données.

### 4. Décorateurs Python

```python
@app.get("/")
def route():
    return {"message": "Hello"}
```

Les décorateurs sont utilisés pour définir les routes.

### 5. Dépendances

```python
def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()
```

Le système de dépendances permet d'injecter des ressources.

## Philosophie de FastAPI

FastAPI suit plusieurs principes de conception :

### 1. Developer Experience (DX)

FastAPI est conçu pour rendre les développeurs heureux et productifs :
- Auto-complétion dans l'IDE
- Messages d'erreur clairs
- Documentation interactive
- Moins de code répétitif

### 2. Standards ouverts

Utilisation de standards reconnus (OpenAPI, JSON Schema) plutôt que de créer de nouveaux formats propriétaires.

### 3. Performance sans compromis

Obtenir d'excellentes performances sans sacrifier la facilité d'utilisation.

### 4. Type safety

Utiliser le système de types Python pour détecter les erreurs tôt et avoir une meilleure auto-complétion.

### 5. Prêt pour la production

Code de production robuste dès le premier jour, pas seulement pour les prototypes.

## Ce que vous allez apprendre

Dans les sections suivantes de ce chapitre sur FastAPI, vous découvrirez :

### 11.2.1 Installation et premier projet FastAPI
- Comment installer FastAPI et ses dépendances
- Créer votre première application
- Lancer un serveur de développement
- Tester vos premiers endpoints

### 11.2.2 Routes et validation avec Pydantic
- Créer des modèles de données avec Pydantic
- Valider automatiquement les données
- Gérer différents types de paramètres
- Créer des modèles complexes et imbriqués

### 11.2.3 Endpoints asynchrones et performances
- Comprendre la programmation asynchrone
- Utiliser `async` et `await`
- Optimiser les performances de votre API
- Gérer la concurrence

## Prérequis recommandés

Pour tirer le meilleur parti de ce chapitre, il est recommandé d'avoir :

**Connaissances essentielles :**
- ✅ Bases solides de Python (variables, fonctions, classes)
- ✅ Compréhension des décorateurs Python
- ✅ Notions de programmation orientée objet

**Connaissances utiles (mais pas obligatoires) :**
- 📚 Bases de HTTP et des APIs REST
- 📚 Utilisation d'un terminal/ligne de commande
- 📚 Concepts de JSON
- 📚 Notions de bases de données (SQL)

**Pas nécessaire :**
- ❌ Expérience préalable avec des frameworks web
- ❌ Connaissance approfondie de la programmation asynchrone
- ❌ Maîtrise de JavaScript ou du front-end

Tout ce dont vous avez besoin sera expliqué au fur et à mesure !

## Ressources officielles

Pour aller plus loin, voici les ressources officielles de FastAPI :

- **Documentation officielle :** https://fastapi.tiangolo.com/
- **Code source (GitHub) :** https://github.com/tiangolo/fastapi
- **Tutoriel officiel :** https://fastapi.tiangolo.com/tutorial/
- **Guide utilisateur :** https://fastapi.tiangolo.com/tutorial/
- **Référence API :** https://fastapi.tiangolo.com/reference/

## Conclusion de l'introduction

FastAPI représente une nouvelle génération de frameworks web Python. Il combine la simplicité de Flask, la puissance des standards modernes, et des performances exceptionnelles. Que vous créiez une petite API pour un projet personnel ou un backend robuste pour une application en production, FastAPI a tout ce qu'il vous faut.

Dans la prochaine section, nous allons mettre les mains dans le code et créer votre première application FastAPI. Vous verrez à quel point il est simple de démarrer !

**Prêt à coder ? Allons-y ! 🚀**

---

⏭️ [Installation et premier projet FastAPI](/11-developpement-web-et-apis/02.1-installation-premier-projet-fastapi.md)
