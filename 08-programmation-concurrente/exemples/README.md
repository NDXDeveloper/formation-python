# Chapitre 08 - Programmation Concurrente : Exemples

## Section 8.1 : Threading et Multiprocessing

### 01_01_threading_base.py
- **Section** : 8.1 - Threading et Multiprocessing
- **Description** : Thread simple, plusieurs threads simultanes, Thread avec classe (heritage), gestion des exceptions dans les threads
- **Fichier source** : `01-threading-et-multiprocessing.md`
- **Sortie attendue** :
  - Thread simple affiche nombres 0-4
  - 3 fichiers telecharges en parallele (~0.30s vs 0.90s sequentiel)
  - MonThread herite de threading.Thread
  - Exception capturee dans un thread

### 01_02_threading_lock.py
- **Section** : 8.1 - Threading et Multiprocessing
- **Description** : Race condition (sans Lock) et correction avec Lock (compteur 500000)
- **Fichier source** : `01-threading-et-multiprocessing.md`
- **Sortie attendue** :
  - Sans lock : compteur potentiellement incorrect (race condition, le GIL peut proteger)
  - Avec lock : compteur = 500000 (correct)

### 01_03_multiprocessing_base.py
- **Section** : 8.1 - Threading et Multiprocessing
- **Description** : Process simple, Pool avec map (cubes), comparaison sequentiel vs parallele
- **Fichier source** : `01-threading-et-multiprocessing.md`
- **Sortie attendue** :
  - Carre de 5 = 25
  - Cubes : [1, 8, 27, 64, 125, 216, 343, 512]
  - Sequentiel ~0.35s, Parallele ~0.10s

### 01_04_multiprocessing_queue.py
- **Section** : 8.1 - Threading et Multiprocessing
- **Description** : Communication inter-processus avec multiprocessing.Queue (producteur/consommateur)
- **Fichier source** : `01-threading-et-multiprocessing.md`
- **Sortie attendue** :
  - 5 items produits et consommes via Queue

### 01_05_exemple_complet_telechargeur.py
- **Section** : 8.1 - Threading et Multiprocessing
- **Description** : Exemple complet - TelechargeParallele avec max_threads, Lock pour resultats, 5 fichiers
- **Fichier source** : `01-threading-et-multiprocessing.md`
- **Sortie attendue** :
  - 5 fichiers telecharges en parallele (max 3 threads), ~0.60s
  - Resultats affiches avec taille et duree

## Section 8.2 : Programmation Asynchrone (asyncio)

### 02_01_asyncio_base.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : Coroutine vs fonction normale, dire_bonjour async, create_task parallele
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - Coroutine simple
  - 3 cafes prepares en parallele (~0.30s vs 0.90s sequentiel)

### 02_02_gather_timeout.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : asyncio.gather() pour telecharger 4 fichiers, wait_for avec timeout
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - 4 fichiers telecharges en ~0.50s
  - Timeout de 0.5s sur operation de 5s : TimeoutError capture

### 02_03_scraper_comparaison.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : Comparaison scraping synchrone vs asynchrone
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - Synchrone : ~1.00s
  - Asynchrone : ~0.40s
  - Gain ~2.5x

### 02_04_erreurs_patterns.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : gather avec return_exceptions, try/except dans coroutines, taches nommees
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - Erreurs capturees dans gather (return_exceptions=True)
  - Exceptions gerees dans coroutines individuelles
  - Taches avec noms personnalises

### 02_05_queue_semaphore.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : asyncio.Queue producteur-consommateur, Semaphore limitant a 3 taches simultanees
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - Queue : items produits et consommes
  - Semaphore : 8 taches, max 3 simultanees, ~0.60s

### 02_06_asyncio_vs_threading.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : Comparaison asyncio vs threading pour 50 operations I/O
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - Threading : ~0.11s pour 50 operations
  - Asyncio : ~0.10s pour 50 operations
  - Resultats identiques

### 02_07_exemple_complet_gestionnaire.py
- **Section** : 8.2 - Programmation asynchrone avec asyncio
- **Description** : Exemple complet - GestionnaireTelechargement avec semaphore, timeout, statistiques
- **Fichier source** : `02-programmation-asynchrone-asyncio.md`
- **Sortie attendue** :
  - 8 fichiers telecharges avec semaphore(3)
  - Statistiques : succes, echecs, duree totale, vitesse

## Section 8.3 : Gestion des Verrous et Synchronisation

### 03_01_lock_rlock.py
- **Section** : 8.3 - Gestion des Verrous et Synchronisation
- **Description** : Race condition, Lock threading, asyncio.Lock, RLock avec CompteBancaire
- **Fichier source** : `03-verrous-et-synchronisation.md`
- **Sortie attendue** :
  - Sans lock : race condition possible
  - Avec Lock threading : compteur = 500000
  - Avec asyncio.Lock : compteur = 500000
  - RLock : compte1 = 800 EUR, compte2 = 700 EUR

### 03_02_semaphore.py
- **Section** : 8.3 - Gestion des Verrous et Synchronisation
- **Description** : Semaphore limitant a 3 acces simultanes, pool de connexions
- **Fichier source** : `03-verrous-et-synchronisation.md`
- **Sortie attendue** :
  - 8 threads avec Semaphore(3) en ~0.60s
  - Pool de 3 connexions max pour 6 requetes

### 03_03_event_condition.py
- **Section** : 8.3 - Gestion des Verrous et Synchronisation
- **Description** : Event threading/asyncio (signaler evenement), Condition producteur/consommateur avec buffer
- **Fichier source** : `03-verrous-et-synchronisation.md`
- **Sortie attendue** :
  - 3 workers attendent un signal puis demarrent
  - Event asyncio avec 3 taches
  - Buffer partage : 6 items produits et consommes

### 03_04_barrier.py
- **Section** : 8.3 - Gestion des Verrous et Synchronisation
- **Description** : Barrier synchronisant 4 threads, simulation parallele en phases
- **Fichier source** : `03-verrous-et-synchronisation.md`
- **Sortie attendue** :
  - 4 threads se synchronisent a la barriere puis demarrent ensemble
  - Simulation : 3 iterations synchronisees entre 3 composants

### 03_05_exemple_complet_cache.py
- **Section** : 8.3 - Gestion des Verrous et Synchronisation
- **Description** : Cache thread-safe avec expiration et statistiques, Singleton thread-safe, ReadWriteLock
- **Fichier source** : `03-verrous-et-synchronisation.md`
- **Sortie attendue** :
  - Cache : ~77.8% taux de hit (35 hits, 10 misses)
  - Singleton : s1 is s2 = True
  - ReadWriteLock : lectures paralleles, ecriture exclusive

## Section 8.4 : Patterns de Concurrence

### 04_01_producteur_consommateur.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Pattern Producer-Consumer avec threading (queue.Queue) et asyncio (asyncio.Queue)
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - Threading : 2 producteurs x 5 items = 10 items produits et consommes par 3 consommateurs
  - Asyncio : meme schema, 10 items produits et consommes

### 04_02_worker_pool.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Worker Pool avec concurrent.futures (submit, as_completed, map) et asyncio
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - ThreadPoolExecutor(3) : 10 taches traitees
  - map() : carres de 1-10 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  - Asyncio : 5 workers traitent 15 taches, 15 resultats

### 04_03_pipeline.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Pipeline en 4 etapes (collecte, nettoyage, traitement, sauvegarde) avec queues
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - 10 items passent par 4 etapes : Data -> Clean-Data -> Processed-Clean-Data -> sauvegarde
  - 10 items sauvegardes au final

### 04_04_fan_out_fan_in.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Fan-Out/Fan-In - dispatcher distribue 12 taches en round-robin a 4 workers, collecteur rassemble les resultats
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - 12 taches distribuees a 4 workers (3 taches chacun)
  - 12 resultats collectes

### 04_05_future_promise.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Future/Promise avec concurrent.futures (submit/result, gestion d'erreurs, as_completed)
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - 3 futures soumises et resolues
  - Tache 3 leve une ValueError capturee
  - 8 fichiers telecharges au fur et a mesure (as_completed)

### 04_06_map_reduce.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Map-Reduce - somme des carres (1-100 = 338350), analyse de texte (comptage de mots)
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - Somme des carres 1-100 = 338350
  - Top 5 mots : est (6), python (5), langage (3), un (2), programmation (2)

### 04_07_actor_model.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Actor Model - acteurs avec queue de messages (CalculatorActor, LoggerActor)
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - CalculatorActor : 5 + 3 = 8, 4 x 7 = 28
  - LoggerActor : messages avec timestamp
  - Acteurs demarres puis arretes proprement

### 04_08_scatter_gather.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Scatter-Gather - interroger 4 services, collecter toutes les reponses ou la premiere
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - Strategie "toutes" : 4 reponses recues, meilleur prix affiche
  - Strategie "premiere" : premiere reponse retournee, autres annulees

### 04_09_rate_limiting.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Rate Limiting simple (max appels par periode) et Token Bucket
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - RateLimiter : 12 appels avec limite 5/s, pauses de ~1s entre lots
  - TokenBucket : 12 taches executees avec debit controle

### 04_10_exemple_complet_scraper.py
- **Section** : 8.4 - Patterns de Concurrence
- **Description** : Exemple complet combinant Rate Limiting, Worker Pool, Pipeline, Fan-Out/Fan-In et Map-Reduce
- **Fichier source** : `04-patterns-de-concurrence.md`
- **Sortie attendue** :
  - 20 URLs scrapees avec semaphore(5) et rate limit 10/s
  - 20 succes, 0 echecs
  - Analyse Map-Reduce : 80 mots, top 5 affiches
