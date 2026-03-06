# Chapitre 11 - Developpement web et APIs : Exemples

## Fichiers d'exemples

### 01_01_concepts_web.py
- **Section** : 11.1 - Introduction aux frameworks web
- **Fichier source** : `01-introduction-frameworks-web.md`
- **Description** : Concepts fondamentaux du web - methodes HTTP, parsing d'URLs avec urllib.parse, simulation de routeur avec decorateurs, cycle requete/reponse, comparaison des frameworks Python
- **Sortie attendue** :
  - Methodes HTTP : GET, POST, PUT, DELETE avec descriptions
  - Decomposition d'URL (scheme, netloc, path, query params)
  - Routeur simulant l'association chemin/methode -> fonction
  - Cycle requete/reponse avec dictionnaires
  - Tableau comparatif Flask vs Django vs FastAPI

### 02_01_fastapi_concepts.py
- **Section** : 11.2 - FastAPI framework moderne
- **Fichier source** : `02-fastapi-framework-moderne.md`
- **Description** : Concepts Pydantic - BaseModel, validation (valide, conversion auto, erreurs), modeles imbriques (Adresse dans UtilisateurComplet), serialisation (model_dump, model_dump_json)
- **Sortie attendue** :
  - Validation d'un utilisateur valide
  - Conversion automatique de types (str "28" -> int 28)
  - Erreur de validation sur email invalide
  - Modele imbrique avec Adresse
  - Serialisation dict et JSON

### 02_02_premier_projet_fastapi.py
- **Section** : 11.2.1 - Installation et premier projet FastAPI
- **Fichier source** : `02.1-installation-premier-projet-fastapi.md`
- **Description** : Application FastAPI avec TestClient - routes GET (/, /bonjour, /info, /utilisateur/{nom}, /age/{age}, /articles), POST/PUT/DELETE avec modele Article, erreur de validation (422 sur /age/abc)
- **Sortie attendue** :
  - GET / : message de bienvenue
  - GET /bonjour : salutation simple
  - GET /info : nom et version de l'API
  - GET /utilisateur/Alice : salutation personnalisee
  - GET /age/25 : age valide accepte
  - POST /articles : creation d'article (201)
  - PUT /articles/1 : modification d'article
  - DELETE /articles/1 : suppression (204)
  - GET /age/abc : erreur validation 422

### 02_03_routes_validation_pydantic.py
- **Section** : 11.2.2 - Routes et validation Pydantic
- **Fichier source** : `02.2-routes-et-validation-pydantic.md`
- **Description** : Blog API avec validation avancee - Field (min_length, max_length), ArticleCreation avec Auteur imbrique, Query params avec contraintes, path params, field_validator personnalise (nom avec espace, force du mot de passe), endpoint de recherche, ModificationUtilisateur
- **Sortie attendue** :
  - Creation d'article valide (201)
  - Erreur validation titre trop court (422)
  - Article par ID, liste avec pagination
  - Recherche par mot-cle et categorie
  - Creation utilisateur avec validation mot de passe fort
  - Modification partielle utilisateur (PATCH)

### 02_04_endpoints_asynchrones.py
- **Section** : 11.2.3 - Endpoints asynchrones
- **Fichier source** : `02.3-endpoints-asynchrones.md`
- **Description** : Endpoints async FastAPI - middleware de timing (X-Process-Time), asyncio.gather pour fetch parallele, calcul Fibonacci synchrone, asyncio.wait_for timeout, Semaphore limiteur de concurrence, BackgroundTasks pour email, cache simple avec /meteo/{ville}
- **Sortie attendue** :
  - Header X-Process-Time present dans les reponses
  - Recuperation parallele de 3 sources
  - Calcul Fibonacci synchrone (resultat correct)
  - Timeout sur operation longue
  - Semaphore limitant la concurrence
  - BackgroundTask programmee pour envoi email
  - Cache meteo : miss puis hit

### 03_01_flask_bases.py
- **Section** : 11.3 - Flask micro-framework
- **Fichier source** : `03-flask-micro-framework.md`
- **Description** : Flask bases - routes (/, /about, /contact), routes parametrees (/user/<username>, /post/<int:post_id>), url_for, sessions (login/dashboard/logout), inspection de l'objet request, gestionnaires d'erreurs (404 HTML et JSON)
- **Sortie attendue** :
  - Pages d'accueil, about, contact (200)
  - Route parametree avec username et post_id
  - url_for generant les bons chemins
  - Session : login -> dashboard avec nom -> logout -> redirect
  - Objet request : methode, path, headers
  - Erreur 404 HTML et JSON

### 03_02_flask_api_rest.py
- **Section** : 11.3 - Flask micro-framework
- **Fichier source** : `03-flask-micro-framework.md`
- **Description** : API REST complete avec Flask - CRUD taches (GET all, GET by id, POST create, PUT update, DELETE), jsonify, request.get_json, codes HTTP
- **Sortie attendue** :
  - GET /api/tasks : 2 taches initiales
  - GET /api/tasks/1 : tache specifique
  - GET /api/tasks/999 : 404
  - POST : creation d'une 3eme tache (201)
  - PUT /api/tasks/1 : marquer done=True
  - DELETE /api/tasks/2 : suppression
  - Etat final : 2 taches restantes

### 04_01_requetes_http_requests.py
- **Section** : 11.4 - Requetes HTTP avec requests
- **Fichier source** : `04-requetes-http-requests.md`
- **Description** : Bibliotheque requests - serveur FastAPI local (port 9999) avec uvicorn en thread, GET avec params, POST json, PUT, DELETE, headers personnalises, Session requests, timeout (ReadTimeout sur /slow), gestion complete des erreurs (Timeout, ConnectionError, HTTPError), proprietes de Response
- **Sortie attendue** :
  - GET /users : liste JSON, status 200, Content-Type, temps de reponse
  - GET avec params : URL construite avec query string
  - GET /users/1 : utilisateur specifique
  - GET /users/999 : 404 avec detail
  - response.ok et raise_for_status
  - POST /users : creation (201)
  - PUT /users/1 : mise a jour
  - DELETE /users/2 : suppression
  - Headers personnalises envoyes
  - Session partageant headers
  - Timeout apres 1s sur /slow
  - Gestion erreurs : HTTPError 404, ConnectionError

### 05_01_api_rest_complete.py
- **Section** : 11.5 - Creation et consommation d'APIs REST
- **Fichier source** : `05-creation-consommation-apis-rest.md`
- **Description** : API REST complete blog - modeles Pydantic (UtilisateurCreate, Article, Commentaire), CRUD utilisateurs/articles/commentaires, ResourceNotFound, CORS, pagination (skip/limit), filtrage (categorie, auteur_id), compteur de vues, BlogAPIClient, field_validator
- **Sortie attendue** :
  - Endpoint racine avec message bienvenue
  - Creation 2 utilisateurs (201)
  - Email en double : 409 Conflict
  - Creation 3 articles avec tags et categories
  - Lecture incrementant les vues
  - Filtrage par categorie (Tech: 2, Science: 1)
  - Filtrage par auteur
  - Pagination (skip/limit)
  - Commentaires sur article
  - 404 article inexistant
  - 422 validation titre trop court
  - Statistiques (users, articles, commentaires)
  - Suppression article et utilisateur

### 06_01_intro_bdd_orm.py
- **Section** : 11.6 - Bases de donnees et ORM
- **Fichier source** : `06-bases-de-donnees-orm-sqlalchemy.md`
- **Description** : Comparaison SQL brut (sqlite3) vs ORM (SQLAlchemy) - CREATE TABLE, INSERT, SELECT avec filtre, UPDATE, DELETE. Tableau comparatif final
- **Sortie attendue** :
  - SQL brut : 3 utilisateurs, filtre age>30 (2), mise a jour Alice (29 ans), suppression (2 restants)
  - ORM : memes operations avec objets Python
  - Tableau comparatif : 6 operations comparees

### 06_02_sqlalchemy_crud.py
- **Section** : 11.6.1 - Introduction a SQLAlchemy
- **Fichier source** : `06.1-introduction-sqlalchemy.md`
- **Description** : CRUD complet SQLAlchemy - declarative_base, modeles User et Produit (Integer, String, Float, Boolean, Text), context manager get_session() avec commit/rollback, CREATE (add, add_all, flush), READ (all, get, filter, count), UPDATE, DELETE, transaction rollback sur IntegrityError
- **Sortie attendue** :
  - CREATE : 4 utilisateurs, 3 produits
  - READ : tous les users, par ID, filtre age>30 (2), par email, count, produits en stock (2)
  - UPDATE : Alice age 28->29, email modifie
  - DELETE : Bob supprime, 3 restants
  - TRANSACTION : rollback sur email duplique, User 'Test' n'existe pas
  - Types de colonnes : String, Text, Float, Boolean, Integer
  - Etat final : 3 utilisateurs, 3 produits

### 06_03_sqlalchemy_relations.py
- **Section** : 11.6.2 - Modeles et relations
- **Fichier source** : `06.2-modeles-et-relations.md`
- **Description** : Relations SQLAlchemy - One-to-Many (Auteur/Livre), Many-to-One (Article/Commentaire), Many-to-Many (Etudiant/Cours avec table d'association), One-to-One (Utilisateur/Profil avec uselist=False), cascade delete-orphan, auto-referentiel (Employe/Manager), Association Object (Inscription avec notes), exemple complet Bibliotheque, eager loading (joinedload/selectinload)
- **Sortie attendue** :
  - One-to-Many : Hugo 3 livres, Moliere 2 livres
  - Many-to-One : article avec 3 commentaires
  - Many-to-Many : 3 etudiants, 3 cours, inscriptions croisees, ajout/retrait dynamique
  - One-to-One : utilisateur avec profil (type Profil, pas liste)
  - Cascade : orphelin supprime, cascade sur delete auteur (0 livres)
  - Auto-referentiel : hierarchie CEO -> Managers -> Employes
  - Association Object : inscription avec note 15/20, date, statut
  - Bibliotheque : 3 livres, emprunt de 2 livres par un membre
  - Eager loading : joinedload et selectinload (4 auteurs charges)

### 06_04_sqlalchemy_requetes.py
- **Section** : 11.6.3 - Requetes et migrations
- **Fichier source** : `06.3-requetes-et-migrations.md`
- **Description** : Requetes avancees SQLAlchemy - filtres multiples (chainage, multi-conditions), operateurs logiques (and_, or_, not_, combinaison complexe), comparaisons (LIKE, IN, BETWEEN, IS NULL), tri (ORDER BY asc/desc, multi-colonnes), pagination (LIMIT/OFFSET, first, one_or_none), selection de colonnes (labels), jointures (JOIN, OUTERJOIN), agregations (COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING), sous-requetes (scalar_subquery, correlee), SQL brut (text), eager loading, fonction de recherche avancee avec pagination
- **Sortie attendue** :
  - Filtres multiples : 5 livres (annee>1840 ET prix<15)
  - or_ : 5 livres (avant 1840 OU apres 2000)
  - Combinaison complexe : 5 livres
  - LIKE 'Le%' : 4 livres, '%python%' insensible : 2
  - IN : 3 livres, BETWEEN 1840-1860 : 4, IS NULL : 1
  - Tri par titre, prix desc, nationalite+nom
  - Pagination : page 2 avec 3 par page
  - JOIN : 9 livres, Francais : 5, OUTERJOIN : 10 (avec anonyme)
  - COUNT:10, SUM:153.30, AVG:17.03, MIN:8.50, MAX:42.00
  - GROUP BY : 4 auteurs, HAVING >2 : Victor Hugo (3)
  - Sous-requetes : 2 livres chers, 1 auteur moderne
  - SQL brut : 2 livres > 20 EUR
  - Recherche avancee : francais (5), Python (2), pagination prix<=12

## Dependances

```bash
pip install fastapi uvicorn httpx pydantic flask requests sqlalchemy
```

## Execution

Chaque fichier est autonome et peut etre execute independamment :

```bash
python3 01_01_concepts_web.py
python3 02_01_fastapi_concepts.py
# ...
python3 06_04_sqlalchemy_requetes.py
```

Les fichiers de base de donnees temporaires sont automatiquement crees dans `/tmp/` et nettoyes apres execution.
