🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Annexe A — Glossaire

Ce glossaire rassemble les **termes essentiels** rencontrés tout au long de la formation. Chaque définition renvoie au(x) chapitre(s) où le concept est traité en détail.

> 💡 Les termes sont classés par ordre alphabétique. Les renvois `(ch. X)` pointent vers le chapitre correspondant du [sommaire](/SOMMAIRE.md).

---

## A

**Annotation de type (*type hint*)** — Indication facultative du type attendu d'une variable, d'un paramètre ou d'une valeur de retour (`def f(x: int) -> str`). Elle n'est pas vérifiée à l'exécution, mais exploitée par les outils (mypy, IDE). *(ch. 1.6, 7.6, 10.6)*

**ABC (*Abstract Base Class*)** — Classe de base abstraite (module `abc`) qui définit une interface via des méthodes `@abstractmethod` que les sous-classes doivent implémenter. *(ch. 3, 12.3)*

**API / Endpoint** — Une *API* expose des fonctionnalités via des points d'accès (*endpoints*), chacun étant une URL associée à un verbe HTTP (GET, POST…). *(ch. 11)*

**Argument / Paramètre** — Le *paramètre* est le nom déclaré dans la signature d'une fonction ; l'*argument* est la valeur réellement passée à l'appel. *(ch. 1.4)*

**`async` / `await`** — Mots-clés définissant des coroutines et suspendant leur exécution en attendant une opération d'E/S non bloquante. *(ch. 8.2)*

---

## B

**Boucle d'événements (*event loop*)** — Cœur d'`asyncio` : elle ordonnance les coroutines et reprend chacune lorsque son `await` est prêt. *(ch. 8.2)*

**Broadcasting (*diffusion*)** — Mécanisme NumPy permettant d'appliquer une opération entre des tableaux de formes différentes (ex. matrice + vecteur) sans boucle explicite. *(ch. 13.1.1)*

---

## C

**CI/CD (*intégration et déploiement continus*)** — Automatisation des tests à chaque modification (CI) et de la mise en production (CD). *(ch. 12.5)*

**Closure (*fermeture*)** — Fonction interne qui « capture » et mémorise les variables de sa portée englobante, même après la fin de la fonction externe. *(ch. 5.5)*

**Compréhension (*comprehension*)** — Syntaxe concise pour construire une liste, un dictionnaire ou un set à partir d'un itérable : `[x*2 for x in xs]`. *(ch. 2.2)*

**Context manager (*gestionnaire de contexte*)** — Objet utilisable avec `with`, qui garantit l'acquisition et la libération propre d'une ressource via `__enter__`/`__exit__` (ou `@contextmanager`). *(ch. 4.1, 12.3)*

**Coroutine** — Fonction définie avec `async def`, dont l'exécution peut être suspendue et reprise ; brique de base d'`asyncio`. *(ch. 8.2)*

**Conteneur (Docker)** — Unité logicielle isolée empaquetant une application et ses dépendances, exécutable à l'identique partout. *(ch. 12.5)*

**Copy-on-Write (CoW)** — Stratégie (activée par défaut depuis pandas 3.0) où une copie n'est réellement effectuée qu'au moment d'une modification, ce qui rend l'assignation chaînée silencieusement inopérante. *(ch. 13.2)*

**Couverture de code (*coverage*)** — Pourcentage du code réellement exécuté par les tests, mesuré avec `pytest-cov`/`coverage`. *(ch. 10.3)*

---

## D

**Dataclass** — Classe générée par le décorateur `@dataclass` qui crée automatiquement `__init__`, `__repr__`, `__eq__`… pour les classes de données. *(ch. 3, 12.3)*

**DataFrame** — Structure tabulaire 2D de pandas (lignes × colonnes étiquetées), comparable à une feuille de calcul. *(ch. 13.2.1)*

**Décorateur** — Fonction (ou classe) qui en enveloppe une autre pour en modifier le comportement, appliquée avec la syntaxe `@`. *(ch. 3.4, 5.3, 12.3)*

**Docstring** — Chaîne de documentation placée en première instruction d'un module, d'une fonction ou d'une classe, accessible via `help()` ou `__doc__`. *(ch. 10.4)*

**Duck typing** — Style Python où la compatibilité d'un objet dépend de ses méthodes/attributs (« si ça fait coin-coin, c'est un canard ») plutôt que de son type déclaré. *(ch. 3, 12.3)*

---

## E

**EDA (*Exploratory Data Analysis*)** — Analyse exploratoire : première phase d'investigation d'un jeu de données (structure, valeurs manquantes, distributions, corrélations). *(ch. 13.4)*

**Encapsulation** — Principe de la POO : regrouper données et méthodes dans une classe et restreindre l'accès direct à l'état interne. *(ch. 3)*

**Exception** — Objet signalant une erreur ou un événement particulier, propagé jusqu'à un bloc `try/except` qui le gère. *(ch. 1.5, 9)*

---

## F

**f-string** — Littéral de chaîne préfixé par `f` permettant l'interpolation d'expressions : `f"{nom} a {age} ans"`. *(ch. 1.2)*

**Fixture** — En pytest, fonction qui prépare un contexte de test (données, ressources) réutilisable et injecté par dépendance. *(ch. 10.2)*

**Fonction d'ordre supérieur** — Fonction qui prend une fonction en argument et/ou en retourne une (`map`, `filter`, décorateurs). *(ch. 5.1)*

---

## G

**Générateur** — Fonction utilisant `yield` pour produire des valeurs à la demande (*lazy*), économisant la mémoire. *(ch. 5.4, 12.4)*

**GIL (*Global Interpreter Lock*)** — Verrou de CPython n'autorisant qu'un seul thread à exécuter du bytecode Python à la fois ; il limite le parallélisme CPU des threads (contourné par `multiprocessing`, et par le mode *free-threading* expérimental depuis Python 3.13). *(ch. 8.1, 12.4)*

---

## H

**Héritage** — Mécanisme par lequel une classe (fille) réutilise et spécialise les attributs et méthodes d'une autre (parente). *(ch. 3.2)*

---

## I

**Immuable / Mutable** — Un objet *immuable* (int, str, tuple) ne peut être modifié après création ; un objet *mutable* (list, dict, set) le peut. *(ch. 2.1)*

**Itérateur / Itérable** — Un *itérable* peut être parcouru (`for`) ; un *itérateur* produit les éléments un à un via `__next__`. *(ch. 5.4, 12.3)*

---

## L

**Lambda** — Petite fonction anonyme d'une seule expression : `lambda x: x * 2`. *(ch. 5.1)*

**Linter** — Outil d'analyse statique signalant erreurs et écarts de style (Ruff, Flake8, Pylint). *(ch. 10.5, 12.1)*

---

## M

**Métaclasse** — « Classe d'une classe » : contrôle la création des classes elles-mêmes (`type` par défaut). *(ch. 3.5)*

**Méthode de classe / statique** — `@classmethod` reçoit la classe (`cls`) ; `@staticmethod` ne reçoit ni `self` ni `cls` (fonction rangée dans la classe). *(ch. 3.4)*

**Mocking** — Remplacement d'une dépendance par un objet simulé (`unittest.mock`) pour isoler le code testé. *(ch. 10.2)*

**Module / Package** — Un *module* est un fichier `.py` ; un *package* est un dossier de modules (avec `__init__.py`). *(ch. 6)*

---

## N

**Namespace (*espace de noms*)** — Table associant des noms à des objets (local, englobant, global, *built-in* : règle **LEGB**). *(ch. 1.4)*

**ndarray** — Tableau N-dimensionnel de NumPy, homogène et contigu en mémoire, base des calculs vectorisés. *(ch. 13.1)*

---

## O

**ORM (*Object-Relational Mapping*)** — Couche (ex. SQLAlchemy) qui fait correspondre des classes/objets Python à des tables/lignes de base de données. *(ch. 11.6)*

---

## P

**Paramètres variadiques (`*args` / `**kwargs`)** — `*args` collecte les arguments positionnels supplémentaires (en tuple), `**kwargs` les arguments nommés (en dict). *(ch. 1.4)*

**PEP (*Python Enhancement Proposal*)** — Document de proposition d'évolution de Python (voir [Annexe B](02-pep-et-standards.md)). *(transversal)*

**Polymorphisme** — Capacité d'objets de types différents à répondre à la même interface/méthode. *(ch. 3.2)*

**Profilage (*profiling*)** — Mesure des temps d'exécution et des ressources par fonction (`cProfile`, `timeit`) pour cibler les optimisations. *(ch. 9.4, 12.4)*

**Propriété (*property*)** — Attribut « calculé » exposant un *getter*/*setter* via `@property`, sans changer l'interface. *(ch. 3.4)*

**Pydantic** — Bibliothèque de validation de données par les annotations de types, au cœur de FastAPI. *(ch. 11.2)*

---

## R

**Récursion** — Technique où une fonction s'appelle elle-même, avec un *cas de base* qui arrête la descente. *(ch. 1.4)*

**REST** — Style d'architecture d'API web fondé sur les ressources et les verbes HTTP (GET/POST/PUT/DELETE). *(ch. 11.5)*

---

## S

**Sérialisation** — Conversion d'un objet en un format stockable/transmissible (JSON, pickle) et inversement (*désérialisation*). *(ch. 4.2, 4.3)*

**Series** — Tableau 1D étiqueté de pandas (l'équivalent d'une colonne de DataFrame). *(ch. 13.2.1)*

**Slicing (*découpage*)** — Extraction d'une sous-partie d'une séquence/tableau via `[début:fin:pas]`. *(ch. 2.1, 13.1.2)*

---

## T

**Thread / Processus** — Un *thread* partage la mémoire de son processus (idéal pour l'E/S) ; un *processus* a sa propre mémoire (idéal pour le CPU). *(ch. 8.1)*

**Tuple nommé (*namedtuple*)** — Tuple dont les champs sont accessibles par nom. *(ch. 2.3)*

---

## V

**Vectorisation** — Application d'une opération à un tableau entier en une instruction (code C optimisé) au lieu d'une boucle Python. *(ch. 13.1.1)*

**venv (*environnement virtuel*)** — Environnement Python isolé propre à un projet, avec ses propres dépendances. *(ch. 6.4)*

**Verrou (*lock*) / Condition de course (*race condition*)** — Un *verrou* protège une ressource partagée entre threads ; une *condition de course* est un bug dû à un accès concurrent non synchronisé. *(ch. 8.3)*

**Vue vs Copie** — En NumPy/pandas, une *vue* partage les données de l'original (la modifier le modifie) ; une *copie* est indépendante. *(ch. 13.1.2)*

---

## W

**Walrus (`:=`)** — Opérateur d'affectation dans une expression (`if (n := len(xs)) > 5:`) : il affecte *et* renvoie une valeur. Introduit par la PEP 572. *(ch. 1.3)*

**Wheel (`.whl`) / PyPI** — Le *wheel* est le format de paquet installable ; *PyPI* est le dépôt public où l'on publie (`uv publish`/`twine`) et installe (`pip`) les paquets. *(ch. 6.3, 12.5)*

---

🔝 Retour au [Sommaire](/SOMMAIRE.md) · Annexe suivante : [Récapitulatif des PEP et standards](02-pep-et-standards.md) ⏭️
