# Exemples - Chapitre 07 : Bibliothèques standard

Ce dossier contient **35 fichiers** d'exemples exécutables couvrant les 6 sections du chapitre 7.

## Section 7.1 : os, sys et subprocess

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `01_01_os_systeme_et_repertoires.py` | Module os : informations système, création/suppression de répertoires (mkdir, makedirs, rmdir), listdir, chdir | `01-os-sys-subprocess.md` |
| `01_02_os_path_et_fichiers.py` | os.path (join, exists, isfile, abspath, splitext, split), getsize, stat, rename, variables d'environnement, os.walk | `01-os-sys-subprocess.md` |
| `01_03_sys_interpreteur.py` | sys.version, platform, executable, sys.path, stdout/stderr, getsizeof, sys.argv via subprocess | `01-os-sys-subprocess.md` |
| `01_04_subprocess_commandes.py` | subprocess.run, capture_output, gestion d'erreurs (FileNotFoundError, CalledProcessError), stdin, shell, pathlib | `01-os-sys-subprocess.md` |
| `01_05_exemple_complet_analyseur.py` | Exemple complet : analyseur de projet combinant os, sys et subprocess sur un mini-projet temporaire | `01-os-sys-subprocess.md` |

## Section 7.2 : datetime et time

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `02_01_datetime_base.py` | datetime.now, timezone, création, composants, strftime, strptime, calcul d'âge, parsing sécurisé | `02-datetime-et-time.md` |
| `02_02_date_time_timedelta.py` | date.today, classe time, timedelta (création, arithmétique), différences de dates, comparaisons, min/max | `02-datetime-et-time.md` |
| `02_03_module_time.py` | timestamp, localtime, conversion datetime/timestamp, sleep, perf_counter, classe Chronometre (context manager) | `02-datetime-et-time.md` |
| `02_04_fuseaux_horaires.py` | ZoneInfo (Paris, Tokyo, New York), conversions de fuseaux, UTC, bonnes pratiques | `02-datetime-et-time.md` |
| `02_05_exemples_pratiques.py` | Système de rappels, journal avec fichier temporaire, CalculateurTravail (8h=120 EUR), échéances (10000 EUR/12 mois) | `02-datetime-et-time.md` |

## Section 7.3 : math, random et statistics

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `03_01_math_base.py` | Constantes (pi, e, tau, inf, nan), calculs cercle, fabs/copysign, ceil/floor/trunc/round, facture avec TVA | `03-math-random-statistics.md` |
| `03_02_math_avance.py` | sqrt/pow/cbrt/exp, intérêts composés, logarithmes, trigonométrie, distance euclidienne, gcd/lcm/factorial/comb/perm, probabilités loto | `03-math-random-statistics.md` |
| `03_03_random.py` | random/uniform/randint, choice/choices/sample, shuffle, PaquetDeCartes, distributions (seed=42) | `03-math-random-statistics.md` |
| `03_04_statistics.py` | mean/geometric_mean/harmonic_mean, median, mode/multimode, analyse salaires, variance/stdev, quantiles, correlation | `03-math-random-statistics.md` |
| `03_05_casino_monte_carlo.py` | Simulation casino (roulette+blackjack), estimation de Pi par Monte Carlo, simulation de notes (seed=42) | `03-math-random-statistics.md` |

## Section 7.4 : itertools et functools

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `04_01_itertools_infinis.py` | count, cycle, repeat, GestionnaireID | `04-itertools-et-functools.md` |
| `04_02_itertools_filtrage.py` | chain, compress, dropwhile/takewhile, filterfalse, islice, groupby, analyse de logs | `04-itertools-et-functools.md` |
| `04_03_itertools_combinatoires.py` | product, permutations, combinations, combinations_with_replacement, grilles loto, accumulate, tee, zip_longest | `04-itertools-et-functools.md` |
| `04_04_functools_reduce_partial.py` | reduce (somme, produit, max), fusion de dictionnaires, partial (puissance, multiplier, print, conversion d'unités) | `04-itertools-et-functools.md` |
| `04_05_functools_cache_et_classes.py` | lru_cache (fibonacci), triangle de Pascal, wraps (décorateur chronomètre), total_ordering, singledispatch | `04-itertools-et-functools.md` |
| `04_06_exemple_complet_transactions.py` | AnalyseurTransactions (groupby catégorie, top clients, CA cumulé) + pipeline de traitement de texte avec Counter | `04-itertools-et-functools.md` |

## Section 7.5 : logging et configuration

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `05_01_logging_base.py` | Logging vs print, niveaux de log (DEBUG..CRITICAL), basicConfig, format personnalisé, format détaillé | `05-logging-et-configuration.md` |
| `05_02_logging_fichiers_handlers.py` | FileHandler, console+fichier, RotatingFileHandler avec rotation par taille, types de handlers | `05-logging-et-configuration.md` |
| `05_03_loggers_nommes_hierarchie.py` | Loggers nommés (auth, database, api), hiérarchie (app.module.fonction), filtres personnalisés | `05-logging-et-configuration.md` |
| `05_04_dictconfig.py` | Configuration par dictionnaire (dictConfig), configuration depuis fichier INI (fileConfig) | `05-logging-et-configuration.md` |
| `05_05_application_utilisateurs.py` | GestionnaireUtilisateurs avec logging (ajout, suppression, doublons, email invalide) | `05-logging-et-configuration.md` |
| `05_06_logging_exceptions.py` | Stack traces avec exc_info, logging.exception(), bonnes pratiques (niveaux, lazy formatting, infos sensibles) | `05-logging-et-configuration.md` |
| `05_07_exemple_complet_ecommerce.py` | Application e-commerce (Produit, Panier, GestionnaireCommandes) avec dictConfig et RotatingFileHandler | `05-logging-et-configuration.md` |
| `05_08_exemple_webapp.py` | Simulation webapp (login, accès pages, traitement données) avec logs access/erreurs séparés | `05-logging-et-configuration.md` |

## Section 7.6 : typing - Annotations avancées

| Fichier | Description | Fichier source |
|---------|-------------|----------------|
| `06_01_annotations_base.py` | Annotations de variables et fonctions, types de collections (list, dict, tuple, set) | `06-typing-annotations-avancees.md` |
| `06_02_union_optional_any.py` | Union (|), X \| None, Any, TypeAlias | `06-typing-annotations-avancees.md` |
| `06_03_callable_typevar.py` | Callable (types de fonctions), TypeVar (génériques, contraintes, bornes) | `06-typing-annotations-avancees.md` |
| `06_04_generic_classes.py` | Classes génériques avec Generic (Pile[T], Cache[K, V] avec expiration) | `06-typing-annotations-avancees.md` |
| `06_05_literal_final_protocol.py` | Literal, Final, Protocol (duck typing structurel), NewType, @overload | `06-typing-annotations-avancees.md` |
| `06_06_exemple_complet_taches.py` | Système de gestion de tâches (dataclass, Literal, Protocol, TypeAlias, notifications) | `06-typing-annotations-avancees.md` |

## Sorties attendues

### 01_01 - os système et répertoires
```
=== Informations système ===
Système d'exploitation : posix
Plateforme détaillée : linux
...
=== Création et suppression de répertoires ===
...
=== Lister le contenu d'un répertoire ===
...
```

### 01_02 - os.path et fichiers
```
=== os.path - Manipulation de chemins ===
...
=== Informations sur les fichiers ===
...
=== Variables d'environnement ===
...
=== os.walk - Parcours récursif ===
...
```

### 01_03 - sys interpréteur
```
=== Informations sur l'interpréteur ===
Python version : 3.x.x ...
...
=== Taille des objets en mémoire ===
...
=== sys.argv ===
...
```

### 01_04 - subprocess commandes
```
=== subprocess.run() ===
...
=== Gestion des erreurs ===
...
```

### 01_05 - Analyseur de projet
```
=== Analyse du projet : mini_projet ===
...
```

### 02_01 - datetime base
```
=== Date et heure actuelles ===
...
=== Formatage (strftime) ===
...
```

### 02_02 - date, time, timedelta
```
=== La classe date ===
Date du jour : YYYY-MM-DD
...
=== timedelta - Durées ===
...
```

### 02_03 - Module time
```
=== Timestamps ===
...
=== Mesurer les performances ===
...
=== Chronomètre (context manager) ===
...
```

### 02_04 - Fuseaux horaires
```
=== Fuseaux horaires avec ZoneInfo ===
...
```

### 02_05 - Exemples pratiques datetime
```
=== Système de rappels ===
...
=== Journal (avec fichier temporaire) ===
...
=== Calculateur de temps de travail ===
Durée travaillée : 8:00:00
Salaire : 120.00 EUR
...
```

### 03_01 - math base
```
=== Constantes mathématiques ===
Pi = 3.141592653589793
...
=== Arrondis et troncature ===
...
```

### 03_02 - math avancé
```
=== Racines et puissances ===
...
=== Intérêts composés ===
Capital après 10 ans : 13,439.16 EUR
...
```

### 03_03 - random
```
=== Nombres aléatoires de base (seed=42) ===
...
```

### 03_04 - statistics
```
=== Moyennes ===
Moyenne arithmétique : ...
...
```

### 03_05 - Casino et Monte Carlo
```
=== Simulation de casino ===
...
=== Estimation de Pi par Monte Carlo ===
...
```

### 04_01 - itertools infinis
```
=== count() ===
count(0) : [0, 1, 2, 3, 4]
...
```

### 04_02 - itertools filtrage
```
=== chain() ===
chain : [1, 2, 3, 4, 5, 6, 7, 8, 9]
...
=== groupby() ===
...
```

### 04_03 - itertools combinatoires
```
=== product() - Produit cartésien ===
...
=== permutations() ===
...
=== accumulate() ===
...
```

### 04_04 - functools reduce et partial
```
=== reduce() ===
Somme : 15
Produit : 120
...
=== partial() ===
carre(5) = 25
cube(3) = 27
...
```

### 04_05 - functools cache et classes
```
=== lru_cache() - Fibonacci ===
Sans cache : fibonacci(30) = 832040 en X.XXXXs
Avec cache : fibonacci(30) = 832040 en 0.XXXXXXs
...
=== Triangle de Pascal ===
...
```

### 04_06 - Exemple complet transactions
```
=== Analyse de transactions e-commerce ===
Transactions par catégorie :
...
Top 3 clients :
...
```

### 05_01 - logging base
```
=== Logging vs print() ===
...
=== Niveaux de log ===
DEBUG    = 10
INFO     = 20
WARNING  = 30
ERROR    = 40
CRITICAL = 50
...
```

### 05_02 - logging fichiers et handlers
```
=== Écrire dans un fichier ===
Contenu de app.log :
  ... - INFO - Ce message va dans le fichier
  ... - ERROR - Cette erreur aussi
...
=== RotatingFileHandler ===
Fichiers créés par rotation :
  app_rotating.log (... octets)
  app_rotating.log.1 (... octets)
  ...
```

### 05_03 - Loggers nommés et hiérarchie
```
auth - INFO - Utilisateur connecté
database - DEBUG - Connexion à la base de données
api - WARNING - Taux de requêtes élevé
app - INFO - Log de l'application
app.module - INFO - Log du module
app.module.fonction - INFO - Log de la fonction
...
```

### 05_04 - dictConfig
```
=== Configuration par dictionnaire (dictConfig) ===
INFO - Message d'information
WARNING - Message d'avertissement
ERROR - Message d'erreur
...
```

### 05_05 - Application utilisateurs
```
... - INFO - Tentative d'ajout de l'utilisateur: alice
... - INFO - Utilisateur alice ajouté avec succès
... - WARNING - L'utilisateur alice existe déjà
... - ERROR - Email invalide pour charlie: invalide
... - INFO - Utilisateur bob supprimé
... - ERROR - L'utilisateur david n'existe pas
Utilisateurs: ['alice']
```

### 05_06 - logging exceptions
```
INFO - Division réussie: 10 / 2 = 5.0
ERROR - Division par zéro!
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
...
```

### 05_07 - Exemple complet e-commerce
```
... [INFO] ecommerce.main: Démarrage de l'application e-commerce
... [INFO] ecommerce.panier: Panier créé pour le client client_001
... [WARNING] ecommerce.produit: Stock insuffisant pour Clavier mécanique: demandé=5, stock=3
Total du panier: 1081.96 EUR
... [INFO] ecommerce.commandes: Commande #1 créée avec succès: 1081.96 EUR
Commande #1
   Total: 1081.96 EUR
   Statut: confirmée
```

### 05_08 - Exemple webapp
```
... [INFO] app - Application web démarrée
... [INFO] app - Connexion réussie: admin
... [WARNING] app - Mot de passe incorrect pour: admin
... [WARNING] app - Utilisateur inconnu: hacker
... [WARNING] app - Accès refusé à /admin/settings pour user
... [INFO] app - Traitement réussi: somme = 15
... [ERROR] app - Erreur lors du traitement des données
--- Contenu de access.log ---
  ... POST /login - 200 - user=admin
  ... POST /login - 401 - user=admin
  ... GET /admin/settings - 403 - user=user
  ... POST /process - 500 - anonymous
```

### 06_01 - Annotations base
```
=== Variables avec annotations ===
nom: Alice (type: str)
age: 25 (type: int)
...
=== list[type] ===
Moyenne de [15.0, 12.5, 18.0, 14.0] = 14.875
...
=== tuple[types...] ===
diviser(10, 3) = quotient=3, reste=1
```

### 06_02 - Union, Optional, Any
```
=== Union avec | (Python 3.10+) ===
Entier: 42
Flottant: 3.14
Chaîne: test
...
=== TypeAlias ===
Utilisateur créé: {'id': '1', 'email': 'alice@example.com'}
Position: (48.8566, 2.3522)
```

### 06_03 - Callable et TypeVar
```
=== Callable ===
additionner(5, 3) = 8
multiplier(5, 3) = 15
Transformation: ['bonjour', 'monde'] -> ['BONJOUR', 'MONDE']
...
=== TypeVar avec contraintes ===
doubler(5) = 10
doubler(3.14) = 6.28
```

### 06_04 - Classes génériques
```
=== Pile générique (Generic[T]) ===
Pile d'entiers - taille: 3
  depiler: 3
  depiler: 2
...
=== Cache générique (Generic[K, V]) ===
Utilisateur 1: Alice
Config 'db': {'host': 'localhost', 'port': 5432}
```

### 06_05 - Literal, Final, Protocol
```
=== Literal ===
  Code 200: Succès
  Code 404: Non trouvé
...
=== Protocol ===
  Cercle de rayon 5
  Carré de côté 10
...
=== @overload ===
  traiter(5) = 10
  traiter('hello') = HELLO
  obtenir_elements([0, 2, 4]) = ['a', 'c', 'e']
```

### 06_06 - Exemple complet tâches
```
=== Système de Gestion de Tâches ===
  [Email] -> Utilisateur 1: Nouvelle tâche assignée: Implémenter l'API
  [Email] -> Utilisateur 2: Nouvelle tâche assignée: Écrire les tests
...
Statistiques:
  total: 4
  a_faire: 2
  en_cours: 1
  terminee: 1
  en_retard: 1
Tâches en retard: 1
  - Revue de code
```

## Notes

- Les exemples `05_*` (logging) utilisent des dossiers temporaires pour les fichiers de log, nettoyés automatiquement à la fin de l'exécution.
- Les exemples `05_01` utilisent des sous-processus pour contourner la limitation de `basicConfig()` (un seul appel effectif par processus).
- Les exemples `03_03` et `03_05` (random) utilisent `seed(42)` pour des résultats reproductibles.
- Les exemples `06_*` (typing) sont des annotations qui n'affectent pas l'exécution mais rendent le code plus clair pour les outils d'analyse (mypy).
- Tous les exemples créant des fichiers/dossiers temporaires nettoient leurs résidus à la fin.
