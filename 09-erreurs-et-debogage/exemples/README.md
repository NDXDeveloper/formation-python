# Chapitre 09 - Erreurs et Debogage : Exemples

Ce dossier contient les exemples exécutables du chapitre 9, un fichier `.py` par thème, numérotés selon la section du cours (`01_*` → 9.1, `02_*` → 9.2, `03_*` → 9.3, `04_*` → 9.4).

**Exécution** : chaque fichier est autonome.

```bash
python3 01_01_hierarchie_exceptions.py
```

> Les exemples de profiling affichent des **durées et tailles variables** selon la machine ; seules les valeurs déterministes (résultats calculés) sont indiquées comme « Sortie attendue ».

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

### 01_02_exception_groups.py
- **Section** : 9.1 - Hierarchie des exceptions
- **Description** : Groupes d'exceptions (ExceptionGroup) pour regrouper plusieurs erreurs levees ensemble ; la syntaxe `except*` est citee en commentaire (Python 3.11+)
- **Fichier source** : `01-hierarchie-des-exceptions.md`
- **Sortie attendue** :
  - Sur Python 3.11+ : groupe de 2 ValueError + 1 TypeError, inspectees via `.exceptions`
  - Sur Python < 3.11 : message indiquant que ExceptionGroup necessite 3.11+

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

### 02_03_chainage_exceptions.py
- **Section** : 9.2 - Creation d'exceptions personnalisees
- **Description** : Chainage d'exceptions (`raise ... from ...`, cause preservee dans `__cause__`) et `add_note()` pour ajouter du contexte (Python 3.11+)
- **Fichier source** : `02-exceptions-personnalisees.md`
- **Sortie attendue** :
  - ConfigError leve depuis un FileNotFoundError, avec la cause d'origine affichee
  - add_note (3.11+) : notes attachees a l'exception ; sinon message de repli

### 02_04_hierarchie_personnalisee.py
- **Section** : 9.2 - Creation d'exceptions personnalisees
- **Description** : Hierarchie d'exceptions a plusieurs niveaux (ErreurApplication -> ErreurBaseDeDonnees/ErreurReseau/ErreurValidation -> exceptions specifiques) et capture a differents niveaux de la hierarchie
- **Fichier source** : `02-exceptions-personnalisees.md`
- **Sortie attendue** :
  - 3 scenarios captures au bon niveau : specifique, categorie, global
  - Verifications de sous-classes : toutes True (chaine d'heritage)

## Section 9.3 : Techniques de debogage

### 03_01_print_assert.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Debogage avec print() (moyenne, types, f-string auto-documentee {x=}, separateurs), assertions (racine carree, types, liste vide)
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - Moyenne de [15, 18, 12, 16] = 15.25
  - Type de "123" = <class 'str'>
  - racine(16) = 4.0, racine(-5) -> AssertionError
  - concatener("Bonjour", 123) -> AssertionError
  - premier([]) -> AssertionError

### 03_02_logging.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Module logging - 5 niveaux (DEBUG, INFO, WARNING, ERROR, CRITICAL), fonction avec logging, logging.exception (trace complete), ecriture dans un fichier log
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

### 03_05_warnings.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Module warnings - `warnings.warn` (UserWarning), depreciation (DeprecationWarning, `stacklevel`), `simplefilter('error')` pour transformer un avertissement en exception
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - UserWarning emis (diviser par zero -> None)
  - DeprecationWarning rendu visible (ancienne_api -> 42)
  - simplefilter('error') : le warning suivant est capture comme exception

### 03_06_pdb.py
- **Section** : 9.3 - Techniques de debogage
- **Description** : Debogueur pdb - points d'arret avec breakpoint() (calculer_prix_total, calculer_factorielle). Les breakpoint() sont neutralises par defaut via PYTHONBREAKPOINT=0 pour une execution non interactive
- **Fichier source** : `03-techniques-de-debogage.md`
- **Sortie attendue** :
  - Par defaut (breakpoint neutralise) : Prix total = 360.0EUR, factorielle(5) = 120
  - Avec `PYTHONBREAKPOINT=1 python 03_06_pdb.py` : ouvre pdb a chaque breakpoint()

## Section 9.4 : Profiling et optimisation

### 04_01_mesurer_temps.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Mesurer le temps d'execution avec time.perf_counter() (horloge monotone), fonction de chronometrage, gestionnaire de contexte
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
- **Description** : Profiling memoire - sys.getsizeof, comparaison structures (liste, tuple, set, generateur), tracemalloc (allocations), memory_profiler (tiers, optionnel)
- **Fichier source** : `04-profiling-et-optimisation.md`
- **Sortie attendue** :
  - Petite liste : 104.00 octets
  - Grande liste : ~7-8 Mo
  - Generateur : ~200 octets (42000x moins que la liste)

### 04_05_optimisation_techniques.py
- **Section** : 9.4 - Profiling et optimisation
- **Description** : Techniques d'optimisation - set vs liste, calculs repetitifs, comprehensions, fonctions built-in, lru_cache et functools.cache (Fibonacci), join()
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

## Notes

- **Style des fichiers** : les accents français sont conservés (é, è, à…), mais les émojis et le symbole € sont rendus en ASCII (`EUR`…). Les démonstrations d'erreurs (assertions, exceptions) sont **encadrées par `try/except`** pour que les fichiers s'exécutent jusqu'au bout.
- **Mesure du temps** : on utilise `time.perf_counter()` (horloge monotone, adaptée aux durées), comme dans le cours, et non `time.time()`.
- **Dépendances tierces** : `04_06`, `04_07`, `04_08` nécessitent **NumPy** (`pip install numpy`). `04_04` utilise **memory_profiler** s'il est installé, sinon il l'indique et renvoie vers `tracemalloc` (stdlib). Tous les autres exemples n'utilisent que la bibliothèque standard.
- **Débogueur pdb** : `03_06` contient de vrais `breakpoint()`, **neutralisés par défaut** (`PYTHONBREAKPOINT=0`) pour que le fichier s'exécute d'un trait. Relancez-le avec `PYTHONBREAKPOINT=1 python 03_06_pdb.py` pour ouvrir le débogueur et explorer pas à pas.
- **Fonctionnalités Python 3.11+** : `01_02` (ExceptionGroup) et la 2ᵉ partie de `02_03` (`add_note`) sont protégées par un test `sys.version_info` et affichent un message de repli avant 3.11. La syntaxe `except*` (montrée dans le `.md`) est du **3.11+ au niveau de la *syntaxe*** : impossible à inclure dans un fichier exécutable sur 3.10 — `01_02` en montre donc l'équivalent par inspection de l'attribut `.exceptions`.
- **Compatibilité** : hors NumPy, les exemples s'exécutent sur **Python 3.10 à 3.14** (vérifié ; les blocs 3.11+ affichent un repli sur 3.10).
