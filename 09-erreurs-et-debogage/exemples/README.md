# Chapitre 09 - Erreurs et Debogage : Exemples

## Section 9.1 : Hierarchie des exceptions

### 01_01_hierarchie_exceptions.py
- **Section** : 9.1 - Hierarchie des exceptions
- **Description** : Exceptions courantes (ZeroDivisionError, OverflowError, IndexError, KeyError, TypeError, ValueError, NameError, AttributeError, FileNotFoundError, PermissionError, ModuleNotFoundError), capture multiple, ordre de capture
- **Fichier source** : `01-hierarchie-des-exceptions.md`
- **Sortie attendue** :
  - Chaque exception est capturee avec le bon message
  - PermissionError sur /root/fichier_protege.txt
  - Mauvais ordre : LookupError capture avant IndexError
  - Bon ordre : IndexError (specifique) capture en premier

## Section 9.2 : Creation d'exceptions personnalisees

### 02_01_exceptions_personnalisees.py
- **Section** : 9.2 - Creation d'exceptions personnalisees
- **Description** : Exceptions simples, constructeur personnalise, application bancaire (SoldeInsuffisantError), validation (EmailInvalideError, MotDePasseFaibleError), API HTTP (404/403/400), attributs supplementaires avec rapport
- **Fichier source** : `02-exceptions-personnalisees.md`
- **Sortie attendue** :
  - MonException capturee
  - AgeInvalideError : -5
  - SoldeInsuffisantError : 100EUR disponible, 150EUR requis
  - MotDePasseFaibleError : mot de passe < 8 caracteres
  - RessourceNonTrouveeError : 404
  - Rapport de transfert avec date, comptes, montant

### 02_02_exemple_complet_bibliotheque.py
- **Section** : 9.2 - Creation d'exceptions personnalisees
- **Description** : Systeme de gestion de bibliotheque avec hierarchie d'exceptions (LivreNonDisponibleError, LimiteEmpruntsDepasseeError, RetardRetourError)
- **Fichier source** : `02-exceptions-personnalisees.md`
- **Sortie attendue** :
  - Test 1 : emprunt reussi
  - Test 2 : livre non disponible (retour prevu dans 14 jours)
  - Test 3 : limite de 3 emprunts atteinte
  - Test 4 : livre inexistant (ValueError)
  - Test 5 : retard de 5 jours, amende 2.5EUR

## Section 9.3 : Techniques de debogage

### 03_01_print_assert.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Debogage avec print() (moyenne, types, separateurs), assertions (racine carree, types, liste vide)
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - Moyenne de [15, 18, 12, 16] = 15.25
  - Type de "123" = <class 'str'>
  - racine(16) = 4.0, racine(-5) -> AssertionError
  - concatener("Bonjour", 123) -> AssertionError
  - premier([]) -> AssertionError

### 03_02_logging.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Module logging - 5 niveaux (DEBUG, INFO, WARNING, ERROR, CRITICAL), fonction avec logging, ecriture dans un fichier log
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - 5 messages de niveaux differents sur stderr
  - diviser(10, 2) = 5.0, diviser(10, 0) = None
  - Fichier mon_application.log cree puis nettoye

### 03_03_traceback_pprint_inspect.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Traceback (trace d'execution), pprint (affichage elegant), decorateur de debogage, module inspect (introspection)
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - Traceback : fonction_a -> fonction_b -> fonction_c -> ZeroDivisionError
  - pprint : affichage formate des donnees complexes
  - Decorateur : addition(5,3)=8, saluer("Alice",message="Salut")="Salut Alice"
  - inspect : fonction actuelle = ma_fonction, appelee depuis fonction_principale

### 03_04_erreurs_courantes.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Erreurs courantes et strategies de debogage (TypeError, IndexError, KeyError, NameError), correction de bugs
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - TypeError : age = int("25"), nouvelle_age = 26
  - IndexError : index 10 trop grand (max: 2)
  - KeyError : cle 'ville' n'existe pas, get() retourne "Non specifie"
  - moyenne([10,20,30]) = 20.0, moyenne_v2([]) = None

## Section 9.4 : Profiling et optimisation

### 04_01_mesurer_temps.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Mesurer le temps d'execution avec time.time(), fonction de chronometrage, gestionnaire de contexte
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - Temps d'execution de la boucle ~0.05-0.15s
  - sum(range(1000000)) = 499999500000
  - Context manager affiche debut et fin du chronometrage

### 04_02_timeit.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Module timeit - mesures precises, comparaison boucle/comprehension/map, concatenation + vs join()
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - Comprehension plus rapide que boucle for
  - join() plus rapide que operateur +

### 04_03_cprofile.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : cProfile - profiling detaille, pstats, decorateur de profiling, Fibonacci recursif
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - fonction_lente appelee 5 fois
  - Fibonacci(20) = 6765, ~21891 appels recursifs
  - Fichier .prof cree et nettoye

### 04_04_memoire.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Profiling memoire - sys.getsizeof, comparaison structures (liste, tuple, set, generateur)
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - Petite liste : 104 octets
  - Grande liste : ~7-8 Mo
  - Generateur : ~200 octets (42000x moins que la liste)

### 04_05_optimisation_techniques.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Techniques d'optimisation - set vs liste, calculs repetitifs, comprehensions, fonctions built-in, lru_cache (Fibonacci), join()
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - sum() ~4-5x plus rapide que boucle manuelle
  - lru_cache : ~10000x plus rapide pour Fibonacci(30)
  - Fibonacci(30) = 832040

### 04_06_optimisation_numpy.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Optimisation avec NumPy - operations vectorisees, listes Python vs NumPy arrays
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - NumPy ~10-200x plus rapide pour addition de 1M elements
  - Operations vectorisees ~20-100x plus rapides
  - Resultats identiques entre boucle et vectorise

### 04_07_exemples_pratiques.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Exemples pratiques - doublons O(n2) vs O(n), somme des carres (5 methodes), filtrage et transformation
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - Doublons : set ~100-800x plus rapide, 1000 doublons trouves
  - Somme des carres : formule math la plus rapide, resultat = 333328333350000
  - Filtrage : comprehension recommandee, 50000 elements

### 04_08_exemple_complet_optimisation.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Exemple complet - Optimisation progressive (v1: boucles, v2: built-in, v3: NumPy) pour calcul de statistiques
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - v1 -> v2 : ~1.3x plus rapide
  - v1 -> v3 : ~3x plus rapide
  - Moyenne = 4999.50, Variance = 8333333.25 (identiques pour les 3 versions)
