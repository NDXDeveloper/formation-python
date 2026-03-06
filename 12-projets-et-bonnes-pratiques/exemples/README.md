# Chapitre 12 : Projets et bonnes pratiques - Exemples

Ce dossier contient les exemples executables extraits des fichiers du chapitre 12.

> **Note** : Les fichiers `01-architecture-projet-outils-modernes.md`, `02-gestion-version-git.md` et `05-deploiement-et-distribution.md` sont essentiellement conceptuels (configurations, commandes shell, templates). Aucun code Python executable autonome n'en a ete extrait.

---

## Fichiers

### 03_01_patterns_creation.py

- **Section** : 12.3 - Patterns de conception courants
- **Description** : Patterns de creation - Singleton (classique avec `__new__` et decorateur), Factory (animaux et exporteurs de documents), Builder (Pizza et requete SQL)
- **Fichier source** : `03-patterns-de-conception.md`
- **Sortie attendue** :
```
==================================================
PATTERN 1 : SINGLETON
==================================================

  db1 is db2 : True
  id(db1) == id(db2) : True

  config2.get('database') : postgresql
  config1 is config2 : True
  [HH:MM:SS] Application demarree
  [HH:MM:SS] Traitement des donnees
  Nombre total de logs : 2

==================================================
PATTERN 2 : FACTORY
==================================================

  Chien : Wouf wouf!
  Chat : Miaou!
  Vache : Meuh!
  Erreur : Type d'animal inconnu : dragon

  --- Exporteurs ---
  Export PDF : {'nom': 'Rapport', 'date': '2024-01-15'}
  Export Excel : {'nom': 'Rapport', 'date': '2024-01-15'}
  Export CSV : {'nom': 'Rapport', 'date': '2024-01-15'}

==================================================
PATTERN 3 : BUILDER
==================================================

  Pizza grande avec fromage, pepperoni, champignons

  SQL : SELECT nom, email, age FROM users WHERE age > 18 AND pays = 'France' ORDER BY nom LIMIT 10
  SQL : SELECT * FROM products
```

---

### 03_02_patterns_comportementaux.py

- **Section** : 12.3 - Patterns de conception courants
- **Description** : Patterns comportementaux - Observer (notifications et blog avec abonnement/desabonnement), Strategy (paiement et compression), Iterator (playlist, countdown, pagination, generateurs)
- **Fichier source** : `03-patterns-de-conception.md`
- **Sortie attendue** :
```
==================================================
PATTERN 4 : OBSERVER
==================================================

  --- Notification commande ---
  [Email] Votre commande a ete expediee !
  [SMS] Votre commande a ete expediee !
  [Push] Votre commande a ete expediee !

  --- Publication ---
  Alice a recu : Nouvel article publie : Introduction a Python
  Bob a recu : Nouvel article publie : Introduction a Python
  Charlie a recu : Nouvel article publie : Introduction a Python

  --- Modification (Bob desabonne) ---
  Alice a recu : Article modifie : Introduction a Python
  Charlie a recu : Article modifie : Introduction a Python

==================================================
PATTERN 5 : STRATEGY
==================================================

  Paiement de 109.98 EUR par carte 3456
  Paiement de 109.98 EUR via PayPal (user@example.com)
  Paiement de 109.98 EUR en crypto (wallet: 0xABC123)

  --- Compression ---
  Fichier document.txt : [ZIP] Beaucoup de donnees ... (compresse)
  Fichier image.jpg : [GZIP] Beaucoup de donnees ... (compresse)
  Fichier archive.dat : [RAR] Beaucoup de donnees ... (compresse)

==================================================
PATTERN 7 : ITERATOR
==================================================

  --- Ma playlist ---
  > Song 1
  > Song 2
  > Song 3

  --- CountDown ---
  5
  4
  3
  2
  1

  --- Pagination ---
  Page 1: [1, 2, ..., 10]
  Page 2: [11, 12, ..., 20]
  Page 3: [21, 22, 23, 24, 25]

  --- Generateur countdown ---
  [5, 4, 3, 2, 1]

  --- Generateur pagination ---
  [1, 2, 3, 4, 5]
  [6, 7, 8, 9, 10]
  [11, 12, 13, 14, 15]
```

---

### 03_03_patterns_structurels.py

- **Section** : 12.3 - Patterns de conception courants
- **Description** : Patterns structurels et pythoniques - Decorator (classe cafe avec MilkDecorator/SugarDecorator/WhippedCreamDecorator, decorateurs de fonctions timer/logger/validator, decorateurs de permissions), Adapter (media player et APIs meteo), Repository (InMemoryUserRepository avec UserService), Context Manager (timer, transaction base de donnees, fichier temporaire)
- **Fichier source** : `03-patterns-de-conception.md`
- **Sortie attendue** :
```
==================================================
PATTERN 6 : DECORATOR
==================================================

  --- Cafe avec decorateurs ---
  Cafe simple: 2.0 EUR
  Cafe simple, lait: 2.5 EUR
  Cafe simple, lait, sucre: 2.7 EUR
  Cafe simple, lait, sucre, chantilly: 3.4 EUR

  --- Decorateurs de fonctions ---
  Appel de calculer_moyenne avec args=(10, 20, 30)
  calculer_moyenne a retourne 20.0
  calculer_moyenne a pris X.XXXX secondes

  --- Permissions ---
  Action supprimer_utilisateur par Alice
  Suppression de l'utilisateur 123
  Action supprimer_utilisateur par Bob
  Erreur : Droits admin requis

==================================================
PATTERN 8 : ADAPTER
==================================================

  --- Media Adapter ---
  Lecture MP3 : musique.mp3
  Lecture MP4 : video.mp4

  --- Weather Adapter ---
  Temperature a Paris : 20.0 C
  Temperature a Paris : 20.0 C

==================================================
PATTERN 9 : REPOSITORY
==================================================

  Utilisateurs crees :
    User(id=1, name='Alice', email='alice@example.com')
    User(id=2, name='Bob', email='bob@example.com')

  Recherche id=1 : User(id=1, name='Alice', email='alice@example.com')
  Apres suppression id=2 : 1 utilisateur(s)

==================================================
PATTERN 10 : CONTEXT MANAGER
==================================================

  Debut de operation
  Traitement en cours...
  operation termine en X.XXXXs

  Connexion a postgresql://localhost/mydb
  Debut de la transaction
  Insertion de donnees...
  Mise a jour de donnees...
  Commit de la transaction
  Fin de la transaction
  Deconnexion de la base de donnees

  Creation du fichier temporaire /tmp/temp_pattern_test.txt
  Utilisation de /tmp/temp_pattern_test.txt
  Contenu : Contenu temporaire
  Suppression du fichier /tmp/temp_pattern_test.txt
  Fichier existe encore ? False
```

---

### 04_01_optimisation_performances.py

- **Section** : 12.4 - Optimisation des performances
- **Description** : Mesure du temps (time, timeit, decorateur), profiling (cProfile avec pstats), structures de donnees (list vs set, defaultdict, Counter, deque), optimisations de code (comprehensions vs boucles vs map, concatenation strings join vs +=, deduplication O(n^2) vs O(n)), generateurs vs listes (comparaison memoire), caching (cache dict, lru_cache, @cache pour fibonacci), optimisation memoire avec __slots__, asyncio.gather, resume des optimisations
- **Fichier source** : `04-optimisation-performances.md`
- **Sortie attendue** :
```
==================================================
MESURE DU TEMPS
==================================================

  sum(range(1000000)) = 499999500000
  Temps : X.XXXX secondes

  timeit join : X.XXXXXX secondes/appel

  Boucle for : X.XXXXs
  Comprehension : X.XXXXs
  Comprehension est X.XXx plus rapide

  traiter_donnees a pris X.XXXX secondes

==================================================
PROFILING (cProfile)
==================================================

  Top 5 fonctions (profiling) :
  [lignes de profiling cProfile]

==================================================
STRUCTURES DE DONNEES
==================================================

  Recherche 'in' (1000 fois) :
  Liste : X.XXXXs
  Set : X.XXXXXXs
  Set est Nx plus rapide

  defaultdict : {'apple': 3, 'banana': 2, 'cherry': 1}
  Counter : Counter({'apple': 3, 'banana': 2, 'cherry': 1})
  Most common : [('apple', 3), ('banana', 2)]

  deque(maxlen=5) apres 7 append : [2, 3, 4, 5, 6]
  deque appendleft : ['deuxieme', 'premier', 'dernier']

==================================================
OPTIMISATIONS CODE
==================================================

  Boucle : X.XXXXs
  Comprehension : X.XXXXs
  Map : X.XXXXs

  Concat '+=' : X.XXXXs
  Concat join : X.XXXXs
  join est X.Xx plus rapide

  Deduplication O(n2) : X.XXXXs (250 doublons)
  Deduplication O(n) : X.XXXXXXs (250 doublons)

==================================================
GENERATEURS vs LISTES
==================================================

  Taille liste (1M) : X.XX MB
  Taille generateur : XXX bytes

  Sum squares (generateur) : 333332833333500000

==================================================
CACHING
==================================================

  fibonacci(30) sans cache : 832040 en X.XXXXs
  fibonacci(30) avec cache : 832040 en X.XXXXXXs

  fibonacci(100) avec lru_cache : 354224848179261915075
  Cache info : CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

  calcul_lourd(2, 10, 5) = 1049
  Meme resultat depuis cache : True

==================================================
OPTIMISATION MEMOIRE : __slots__
==================================================

  Sans slots (__dict__) : XXX bytes
  Avec slots : XX bytes

==================================================
ASYNCIO
==================================================

  5 fetches paralleles en 0.50s (au lieu de ~2.5s)
  Resultats : 5 reponses
    Donnees de http://api.example.com/0
    Donnees de http://api.example.com/1
    ...

==================================================
RESUME DES OPTIMISATIONS
==================================================

  Technique             Changement                Gain
  -----------------------------------------------------------------
  Recherche             list -> set               O(n) -> O(1)
  Comprehension         boucle -> [...]           ~1.5x plus rapide
  Strings               += -> join()              ~10x plus rapide
  Cache                 recalcul -> lru_cache     N fois plus rapide
  Memoire               list -> generator         MB -> bytes
  Classes               normal -> __slots__       ~40% moins memoire
  Parallele             sequentiel -> asyncio     Nx plus rapide (I/O)
```

---


