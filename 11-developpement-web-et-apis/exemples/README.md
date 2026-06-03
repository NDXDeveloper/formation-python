# Chapitre 11 - Développement web et APIs : Exemples

Ce dossier contient les exemples exécutables du chapitre 11, un fichier `.py` par thème, numérotés selon la section du cours (`01_*` → 11.1, `02_*` → 11.2, … `06_*` → 11.6).

**Chaque fichier est autonome.** Les applications FastAPI et Flask se démontrent elles-mêmes via `TestClient` / `test_client` (aucun serveur à lancer manuellement) ; `04_01` démarre un petit serveur FastAPI local dans un thread pour illustrer `requests` sans dépendre d'Internet ; les exemples SQLAlchemy utilisent une base SQLite en mémoire ou temporaire. Sorties vérifiées avec FastAPI, Pydantic v2, SQLAlchemy 2.0, Flask et requests sur Python 3.12.

## Fichiers d'exemples

### 01_01_concepts_web.py
- **Section** : 11.1 - Introduction aux frameworks web
- **Fichier source** : `01-introduction-frameworks-web.md`
- **Description** : Concepts fondamentaux du web - méthodes HTTP, parsing d'URLs avec urllib.parse, simulation de routeur avec décorateurs, cycle requête/réponse, comparaison des frameworks Python
- **Sortie attendue** :
  - Méthodes HTTP : GET, POST, PUT, DELETE avec descriptions
  - Décomposition d'URL (scheme, netloc, path, query params)
  - Routeur simulant l'association chemin/méthode -> fonction
  - Cycle requête/réponse avec dictionnaires
  - Tableau comparatif Flask vs Django vs FastAPI

### 02_01_fastapi_concepts.py
- **Section** : 11.2 - FastAPI framework moderne
- **Fichier source** : `02-fastapi-framework-moderne.md`
- **Description** : Concepts Pydantic - BaseModel, validation (valide, conversion auto, erreurs), modèles imbriqués (Adresse dans UtilisateurComplet), sérialisation (model_dump, model_dump_json)
- **Sortie attendue** :
  - Validation d'un utilisateur valide
  - Conversion automatique de types (str "28" -> int 28)
  - Erreur de validation sur email invalide
  - Modèle imbriqué avec Adresse
  - Sérialisation dict et JSON

### 02_02_premier_projet_fastapi.py
- **Section** : 11.2.1 - Installation et premier projet FastAPI
- **Fichier source** : `02.1-installation-premier-projet-fastapi.md`
- **Description** : Application FastAPI avec TestClient - routes GET (/, /bonjour, /info, /utilisateur/{nom}, /age/{age}, /articles), POST/PUT/DELETE avec modèle Article, erreur de validation (422 sur /age/abc)
- **Sortie attendue** :
  - GET / : message de bienvenue
  - GET /bonjour : salutation simple
  - GET /info : nom et version de l'API
  - GET /utilisateur/Alice : salutation personnalisée
  - GET /age/25 : âge valide accepté
  - POST /articles : création d'article (201)
  - PUT /articles/1 : modification d'article
  - DELETE /articles/1 : suppression (204)
  - GET /age/abc : erreur validation 422

### 02_03_routes_validation_pydantic.py
- **Section** : 11.2.2 - Routes et validation Pydantic
- **Fichier source** : `02.2-routes-et-validation-pydantic.md`
- **Description** : Blog API avec validation avancée - Field (min_length, max_length), ArticleCreation avec Auteur imbriqué, Query params avec contraintes, path params, field_validator personnalisé (nom avec espace, force du mot de passe), endpoint de recherche, ModificationUtilisateur
- **Sortie attendue** :
  - Création d'article valide (201)
  - Erreur validation titre trop court (422)
  - Article par ID, liste avec pagination
  - Recherche par mot-clé et catégorie
  - Création utilisateur avec validation mot de passe fort
  - Modification d'utilisateur (chemin + corps + query)

### 02_04_endpoints_asynchrones.py
- **Section** : 11.2.3 - Endpoints asynchrones
- **Fichier source** : `02.3-endpoints-asynchrones.md`
- **Description** : Endpoints async FastAPI - middleware de timing (X-Process-Time), asyncio.gather pour fetch parallèle, calcul Fibonacci synchrone, asyncio.wait_for timeout, Semaphore limiteur de concurrence, BackgroundTasks pour email, cache simple avec /meteo/{ville}
- **Sortie attendue** :
  - Header X-Process-Time présent dans les réponses
  - Récupération parallèle de 3 sources
  - Calcul Fibonacci synchrone (résultat correct)
  - Timeout sur opération longue
  - Semaphore limitant la concurrence
  - BackgroundTask programmée pour envoi email
  - Cache météo : miss puis hit

### 03_01_flask_bases.py
- **Section** : 11.3 - Flask micro-framework
- **Fichier source** : `03-flask-micro-framework.md`
- **Description** : Flask bases - routes (/, /about, /contact), routes paramétrées (/user/<username>, /post/<int:post_id>), url_for, sessions (login/dashboard/logout), inspection de l'objet request, gestionnaires d'erreurs (404 HTML et JSON)
- **Sortie attendue** :
  - Pages d'accueil, about, contact (200)
  - Route paramétrée avec username et post_id
  - url_for générant les bons chemins
  - Session : login -> dashboard avec nom -> logout -> redirect
  - Objet request : méthode, path, headers
  - Erreur 404 HTML et JSON

### 03_02_flask_api_rest.py
- **Section** : 11.3 - Flask micro-framework
- **Fichier source** : `03-flask-micro-framework.md`
- **Description** : API REST complète avec Flask - CRUD tâches (GET all, GET by id, POST create, PUT update, DELETE), jsonify, request.get_json, codes HTTP
- **Sortie attendue** :
  - GET /api/tasks : 2 tâches initiales
  - GET /api/tasks/1 : tâche spécifique
  - GET /api/tasks/999 : 404
  - POST : création d'une 3e tâche (201)
  - PUT /api/tasks/1 : marquer done=True
  - DELETE /api/tasks/2 : suppression
  - État final : 2 tâches restantes

### 04_01_requetes_http_requests.py
- **Section** : 11.4 - Requêtes HTTP avec requests
- **Fichier source** : `04-requetes-http-requests.md`
- **Description** : Bibliothèque requests - serveur FastAPI local (port 9999) avec uvicorn en thread, GET avec params, POST json, PUT, DELETE, headers personnalisés, Session requests, timeout (ReadTimeout sur /slow), gestion complète des erreurs (Timeout, ConnectionError, HTTPError), propriétés de Response
- **Sortie attendue** :
  - GET /users : liste JSON, status 200, Content-Type, temps de réponse
  - GET avec params : URL construite avec query string
  - GET /users/1 : utilisateur spécifique
  - GET /users/999 : 404 avec détail
  - response.ok et raise_for_status
  - POST /users : création (201)
  - PUT /users/1 : mise à jour
  - DELETE /users/2 : suppression
  - Headers personnalisés envoyés
  - Session partageant les headers
  - Timeout après 1s sur /slow
  - Gestion erreurs : HTTPError 404, ConnectionError

### 05_01_api_rest_complete.py
- **Section** : 11.5 - Création et consommation d'APIs REST
- **Fichier source** : `05-creation-consommation-apis-rest.md`
- **Description** : API REST complète de blog **en mémoire** (modèles Pydantic + dictionnaires, sans base de données) - CRUD utilisateurs/articles/commentaires, ResourceNotFound, CORS, pagination (skip/limit), filtrage (catégorie, auteur_id), compteur de vues, BlogAPIClient, field_validator. *Note : version **en mémoire** (modèles Pydantic + dictionnaires, aucune base à configurer). Voir `05_02_api_rest_sqlalchemy.py` pour la **même API avec persistance SQLAlchemy**, fidèle au `.md`.*
- **Sortie attendue** :
  - Endpoint racine avec message de bienvenue
  - Création 2 utilisateurs (201)
  - Email en double : 409 Conflict
  - Création 3 articles avec tags et catégories
  - Lecture incrémentant les vues
  - Filtrage par catégorie (Tech: 2, Science: 1)
  - Filtrage par auteur
  - Pagination (skip/limit)
  - Commentaires sur article
  - 404 article inexistant
  - 422 validation titre trop court
  - Statistiques (users, articles, commentaires)
  - Suppression article et utilisateur

### 05_02_api_rest_sqlalchemy.py
- **Section** : 11.5 - Création et consommation d'APIs REST
- **Fichier source** : `05-creation-consommation-apis-rest.md`
- **Description** : La **même** API REST de blog, mais avec **persistance SQLAlchemy** (modèles ORM `UserTable`/`ArticleTable`/`CommentaireTable` + schémas Pydantic), fidèle au `.md`. Le cours répartit ce code en `models.py`/`database.py`/`main.py` ; ici tout est réuni dans un fichier unique. CRUD complet, filtrage + tri (`sort`/`order`), PATCH partiel, relation `article.auteur` (modèle `ArticleAvecAuteur`), statistiques (article le plus vu). Base SQLite **en mémoire** (`StaticPool`) : auto-suffisant, testable via `TestClient`, sans fichier laissé sur le disque. *Pendant persistant de `05_01` (version en mémoire).*
- **Sortie attendue** :
  - Endpoint racine avec message de bienvenue
  - Création 2 utilisateurs (201), email en double : 409 Conflict
  - Création 3 articles (tags stockés en JSON, catégories)
  - Lecture avec auteur (`auteur.nom`) incrémentant les vues (1 -> 2)
  - Filtrage par catégorie (Tech: 2), tri par vues (plus vu en premier)
  - Modification partielle PATCH (200, nouveau titre)
  - 2 commentaires sur l'article
  - 404 article inexistant, 422 titre trop court
  - Statistiques (2 users, 3 articles, 2 commentaires, article le plus vu)
  - Suppressions (204) : 2 articles et 1 utilisateur restants

### 06_01_intro_bdd_orm.py
- **Section** : 11.6 - Bases de données et ORM
- **Fichier source** : `06-bases-de-donnees-orm-sqlalchemy.md`
- **Description** : Comparaison SQL brut (sqlite3) vs ORM (SQLAlchemy) - CREATE TABLE, INSERT, SELECT avec filtre, UPDATE, DELETE. Tableau comparatif final
- **Sortie attendue** :
  - SQL brut : 3 utilisateurs, filtre age>30 (2), mise à jour Alice (29 ans), suppression (2 restants)
  - ORM : mêmes opérations avec objets Python
  - Tableau comparatif : 6 opérations comparées

### 06_02_sqlalchemy_crud.py
- **Section** : 11.6.1 - Introduction à SQLAlchemy
- **Fichier source** : `06.1-introduction-sqlalchemy.md`
- **Description** : CRUD complet SQLAlchemy - declarative_base, modèles User et Produit (Integer, String, Float, Boolean, Text), context manager get_session() avec commit/rollback, CREATE (add, add_all, flush), READ (all, get, filter, count), UPDATE, DELETE, transaction rollback sur IntegrityError
- **Sortie attendue** :
  - CREATE : 4 utilisateurs, 3 produits
  - READ : tous les users, par ID, filtre age>30 (2), par email, count, produits en stock (2)
  - UPDATE : Alice age 28->29, email modifié
  - DELETE : Bob supprimé, 3 restants
  - TRANSACTION : rollback sur email dupliqué, User 'Test' n'existe pas
  - Types de colonnes : String, Text, Float, Boolean, Integer
  - État final : 3 utilisateurs, 3 produits

### 06_03_sqlalchemy_relations.py
- **Section** : 11.6.2 - Modèles et relations
- **Fichier source** : `06.2-modeles-et-relations.md`
- **Description** : Relations SQLAlchemy - One-to-Many (Auteur/Livre), Many-to-One (Article/Commentaire), Many-to-Many (Etudiant/Cours avec table d'association), One-to-One (Utilisateur/Profil avec uselist=False), cascade delete-orphan, auto-référentiel (Employe/Manager), Association Object (Inscription avec notes), exemple complet Bibliothèque, eager loading (joinedload/selectinload)
- **Sortie attendue** :
  - One-to-Many : Hugo 3 livres, Molière 2 livres
  - Many-to-One : article avec 3 commentaires
  - Many-to-Many : 3 étudiants, 3 cours, inscriptions croisées, ajout/retrait dynamique
  - One-to-One : utilisateur avec profil (type Profil, pas liste)
  - Cascade : orphelin supprimé, cascade sur delete auteur (0 livres)
  - Auto-référentiel : hiérarchie CEO -> Managers -> Employés
  - Association Object : inscription avec note 15/20, date, statut
  - Bibliothèque : 3 livres, emprunt de 2 livres par un membre
  - Eager loading : joinedload et selectinload (4 auteurs chargés)

### 06_04_sqlalchemy_requetes.py
- **Section** : 11.6.3 - Requêtes et migrations
- **Fichier source** : `06.3-requetes-et-migrations.md`
- **Description** : Requêtes avancées SQLAlchemy - filtres multiples (chaînage, multi-conditions), opérateurs logiques (and_, or_, not_, combinaison complexe), comparaisons (LIKE, IN, BETWEEN, IS NULL), tri (ORDER BY asc/desc, multi-colonnes), pagination (LIMIT/OFFSET, first, one_or_none), sélection de colonnes (labels), jointures (JOIN, OUTERJOIN), agrégations (COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING), sous-requêtes (scalar_subquery, corrélée), SQL brut (text), eager loading, fonction de recherche avancée avec pagination
- **Sortie attendue** :
  - Filtres multiples : 5 livres (année>1840 ET prix<15)
  - or_ : 5 livres (avant 1840 OU après 2000)
  - Combinaison complexe : 5 livres
  - LIKE 'Le%' : 4 livres, '%python%' insensible : 2
  - IN : 3 livres, BETWEEN 1840-1860 : 4, IS NULL : 1
  - Tri par titre, prix desc, nationalité+nom
  - Pagination : page 2 avec 3 par page
  - JOIN : 9 livres, Français : 5, OUTERJOIN : 10 (avec anonyme)
  - COUNT:10, SUM:153.30, AVG:17.03, MIN:8.50, MAX:42.00
  - GROUP BY : 4 auteurs, HAVING >2 : Victor Hugo (3)
  - Sous-requêtes : 2 livres chers, 1 auteur moderne
  - SQL brut : 2 livres > 20 EUR
  - Recherche avancée : français (5), Python (2), pagination prix<=12

## Dépendances

```bash
pip install fastapi uvicorn httpx pydantic flask requests sqlalchemy email-validator
```

> `email-validator` n'est requis que par `05_02_api_rest_sqlalchemy.py` (champ `EmailStr`, comme dans le `.md`). Les autres exemples emploient `email: str` et n'en ont pas besoin.

## Exécution

Chaque fichier est autonome et peut être exécuté indépendamment :

```bash
python3 01_01_concepts_web.py
python3 02_01_fastapi_concepts.py
# ...
python3 06_04_sqlalchemy_requetes.py
```

Les fichiers de base de données temporaires sont automatiquement créés dans `/tmp/` et nettoyés après exécution.
