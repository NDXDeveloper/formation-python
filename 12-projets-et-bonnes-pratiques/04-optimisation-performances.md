🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.4 Optimisation des performances

## Introduction

> "Premature optimization is the root of all evil" - Donald Knuth

Cette célèbre citation signifie qu'il ne faut pas **optimiser trop tôt**. Avant d'optimiser, vous devez :
1. **Faire fonctionner** votre code correctement
2. **Mesurer** où sont les vrais problèmes de performance
3. **Optimiser** seulement les parties critiques

L'optimisation prématurée peut rendre votre code complexe et difficile à maintenir pour des gains marginaux. Mais une fois que votre code fonctionne et que vous avez identifié les goulots d'étranglement, il est temps d'optimiser !

### Pourquoi optimiser ?

✅ **Améliorer l'expérience utilisateur** : application plus rapide et réactive

✅ **Réduire les coûts** : moins de ressources serveur nécessaires

✅ **Scalabilité** : gérer plus d'utilisateurs avec les mêmes ressources

✅ **Énergie** : moins de consommation électrique

### Les trois dimensions de l'optimisation

1. **Temps d'exécution** : combien de temps prend votre code ?
2. **Mémoire** : combien de RAM votre code utilise ?
3. **Lisibilité** : votre code reste-t-il compréhensible ?

Il faut souvent trouver un **équilibre** entre ces trois aspects.

---

## Règle d'or : Mesurez avant d'optimiser !

Avant toute optimisation, vous devez **mesurer** pour savoir :
- Quelle partie du code est lente ?
- Combien de temps prend chaque fonction ?
- Où sont les vrais goulots d'étranglement ?

### Mesure simple avec `time`

```python
import time

def fonction_lente():
    time.sleep(1)  # Simule un traitement long
    return "Terminé"

# Mesurer le temps d'exécution
start = time.time()
resultat = fonction_lente()
end = time.time()

print(f"Temps d'exécution : {end - start:.4f} secondes")
# Temps d'exécution : 1.0001 secondes
```

### Mesure avec `timeit` (plus précis)

```python
import timeit

# Mesurer une ligne de code
temps = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Temps moyen : {temps/10000:.6f} secondes")

# Comparer deux approches
def approche1():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result

def approche2():
    return [i * 2 for i in range(1000)]

# Comparer
temps1 = timeit.timeit(approche1, number=10000)
temps2 = timeit.timeit(approche2, number=10000)

print(f"Approche 1 : {temps1:.4f}s")
print(f"Approche 2 : {temps2:.4f}s")
print(f"Approche 2 est {temps1/temps2:.2f}x plus rapide")
```

### Décorateur pour mesurer facilement

```python
import time
from functools import wraps

def measure_time(func):
    """Décorateur qui mesure le temps d'exécution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper

@measure_time
def traiter_donnees(n):
    return sum(range(n))

traiter_donnees(1000000)
# traiter_donnees a pris 0.0234 secondes
```

---

## Profiling : Trouver les goulots d'étranglement

Le **profiling** permet d'analyser en détail où votre programme passe son temps.

### Profiling avec `cProfile`

```python
import cProfile
import pstats
from io import StringIO

def fonction_complexe():
    result = []
    for i in range(10000):
        for j in range(100):
            result.append(i * j)
    return result

def autre_fonction():
    return sum(range(1000000))

def main():
    fonction_complexe()
    autre_fonction()

# Profiler le code
profiler = cProfile.Profile()
profiler.enable()

main()

profiler.disable()

# Afficher les résultats
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 des fonctions les plus lentes
```

### Profiling ligne par ligne avec `line_profiler`

Installation :
```bash
pip install line_profiler
```

Utilisation :
```python
# Ajouter le décorateur @profile (fourni par line_profiler)
@profile
def ma_fonction():
    total = 0
    for i in range(1000):
        total += i ** 2
    return total

# Exécuter avec :
# kernprof -l -v script.py
```

### Memory Profiler

Pour analyser l'utilisation de la mémoire :

```bash
pip install memory_profiler
```

```python
from memory_profiler import profile

@profile
def fonction_gourmande():
    # Créer une grande liste
    big_list = [i for i in range(1000000)]
    return sum(big_list)

# Exécuter avec :
# python -m memory_profiler script.py
```

---

## Optimisation des structures de données

Le choix de la **bonne structure de données** peut transformer un code O(n²) en O(n) !

### Listes vs Sets vs Dictionnaires

```python
import time

# Données de test
data = list(range(10000))

# ❌ Recherche dans une liste : O(n)
def recherche_liste(item):
    return item in data

# ✅ Recherche dans un set : O(1)
data_set = set(data)
def recherche_set(item):
    return item in data_set

# Comparer
start = time.time()
for i in range(1000):
    recherche_liste(9999)
print(f"Liste : {time.time() - start:.4f}s")

start = time.time()
for i in range(1000):
    recherche_set(9999)
print(f"Set : {time.time() - start:.4f}s")
# Set est BEAUCOUP plus rapide !
```

### Quand utiliser quelle structure ?

| Structure | Recherche | Insertion | Suppression | Usage |
|-----------|-----------|-----------|-------------|-------|
| **Liste** | O(n) | O(1)* | O(n) | Ordre important, accès par index |
| **Set** | O(1) | O(1) | O(1) | Valeurs uniques, tests d'appartenance |
| **Dict** | O(1) | O(1) | O(1) | Paires clé-valeur, lookups rapides |
| **Tuple** | O(n) | - | - | Données immuables |
| **deque** | O(n) | O(1) | O(1) | Files, piles (ajout/retrait aux extrémités) |

*O(1) uniquement pour append, O(n) pour insertion au milieu

### Exemple pratique : Optimisation avec un dictionnaire

```python
# ❌ Lent : recherche O(n) à chaque fois
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

def get_user_slow(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# ✅ Rapide : recherche O(1)
users_dict = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
    3: {"id": 3, "name": "Charlie"}
}

def get_user_fast(user_id):
    return users_dict.get(user_id)

# Encore mieux : créer l'index une seule fois
users_indexed = {user["id"]: user for user in users}
```

### Collections spécialisées

```python
from collections import defaultdict, Counter, deque

# defaultdict : évite les vérifications d'existence
# ❌ Avec dict normal
word_count = {}
for word in ["apple", "banana", "apple"]:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# ✅ Avec defaultdict
from collections import defaultdict
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1  # Plus simple !

# Counter : encore plus simple pour compter
from collections import Counter
word_count = Counter(["apple", "banana", "apple"])
print(word_count)  # Counter({'apple': 2, 'banana': 1})

# deque : optimisé pour ajout/retrait aux extrémités
from collections import deque

# ❌ Liste : insert(0) est lent O(n)
liste = []
liste.insert(0, "élément")  # Doit déplacer tous les éléments !

# ✅ deque : appendleft est rapide O(1)
file = deque()
file.appendleft("élément")  # Rapide !
```

---

## Optimisation du code Python

### List comprehensions vs boucles for

Les list comprehensions sont généralement **plus rapides** que les boucles for équivalentes.

```python
import timeit

# ❌ Boucle for classique
def avec_boucle():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result

# ✅ List comprehension
def avec_comprehension():
    return [i * 2 for i in range(1000)]

# ✅ Encore plus rapide : map
def avec_map():
    return list(map(lambda x: x * 2, range(1000)))

print(f"Boucle : {timeit.timeit(avec_boucle, number=10000):.4f}s")
print(f"Comprehension : {timeit.timeit(avec_comprehension, number=10000):.4f}s")
print(f"Map : {timeit.timeit(avec_map, number=10000):.4f}s")
```

### Éviter les recherches répétées

```python
# ❌ Lent : recherche dans la liste à chaque itération
def slow_function(items):
    result = []
    for item in items:
        if item in result:  # O(n) à chaque fois !
            continue
        result.append(item)
    return result

# ✅ Rapide : utiliser un set
def fast_function(items):
    seen = set()
    result = []
    for item in items:
        if item in seen:  # O(1) !
            continue
        seen.add(item)
        result.append(item)
    return result

# ✅ Encore plus simple
def fastest_function(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# ✅✅ Le plus pythonique (préserve l'ordre depuis Python 3.7+)
def pythonic_function(items):
    return list(dict.fromkeys(items))
```

### Utiliser les fonctions built-in

Les fonctions Python built-in (écrites en C) sont **très rapides**.

```python
# ❌ Lent
def sum_manually(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# ✅ Rapide : utiliser sum()
def sum_builtin(numbers):
    return sum(numbers)

# Autres fonctions built-in rapides
numbers = [1, 2, 3, 4, 5]

max_value = max(numbers)      # Plus rapide qu'une boucle
min_value = min(numbers)      # Plus rapide qu'une boucle
all_true = all(numbers)       # Plus rapide qu'une boucle
any_true = any(numbers)       # Plus rapide qu'une boucle
```

### Éviter les concaténations de strings dans les boucles

```python
# ❌ Très lent : les strings sont immuables en Python !
def concat_slow(words):
    result = ""
    for word in words:
        result += word + " "  # Crée une nouvelle string à chaque fois !
    return result

# ✅ Rapide : utiliser join()
def concat_fast(words):
    return " ".join(words)

# Test
words = ["mot"] * 10000
import timeit
print(f"Lent : {timeit.timeit(lambda: concat_slow(words), number=10):.4f}s")
print(f"Rapide : {timeit.timeit(lambda: concat_fast(words), number=10):.4f}s")
```

### Variables locales vs globales

L'accès aux variables locales est plus rapide que l'accès aux variables globales.

```python
# ❌ Plus lent : accès global
CONSTANT = 100

def with_global():
    total = 0
    for i in range(1000000):
        total += CONSTANT  # Accès global
    return total

# ✅ Plus rapide : variable locale
def with_local():
    constant = 100  # Variable locale
    total = 0
    for i in range(1000000):
        total += constant  # Accès local
    return total

# Encore mieux : passer en paramètre
def with_parameter(constant=100):
    total = 0
    for i in range(1000000):
        total += constant
    return total
```

---

## Générateurs : Économiser de la mémoire

Les **générateurs** permettent de traiter des données **à la volée** sans tout charger en mémoire.

### Liste vs Générateur

```python
import sys

# ❌ Liste : tout en mémoire
def get_numbers_list(n):
    return [i for i in range(n)]

# ✅ Générateur : un élément à la fois
def get_numbers_generator(n):
    for i in range(n):
        yield i

# Comparaison mémoire
liste = get_numbers_list(1000000)
print(f"Taille liste : {sys.getsizeof(liste) / 1024 / 1024:.2f} MB")

generateur = get_numbers_generator(1000000)
print(f"Taille générateur : {sys.getsizeof(generateur)} bytes")

# Le générateur est BEAUCOUP plus petit !
```

### Exemple pratique : Traiter un gros fichier

```python
# ❌ Lent et gourmand en mémoire
def process_file_slow(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()  # Charge TOUT en mémoire !

    for line in lines:
        process_line(line)

# ✅ Rapide et efficace
def process_file_fast(filename):
    with open(filename, 'r') as f:
        for line in f:  # Lit ligne par ligne
            process_line(line)

def process_line(line):
    # Traitement de la ligne
    pass
```

### Generator expressions

```python
# Liste : tout calculé immédiatement
squares_list = [x**2 for x in range(1000000)]

# Générateur : calculé à la demande
squares_gen = (x**2 for x in range(1000000))

# Utilisation
total = sum(squares_gen)  # Calcule à la volée, économise la mémoire
```

---

## Caching : Mémoriser les résultats

Le **caching** (mise en cache) évite de recalculer les mêmes choses plusieurs fois.

### Cache simple avec dictionnaire

```python
# Fonction coûteuse à calculer
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# Avec cache
fibonacci_cache = {}

def fibonacci_fast(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        result = n
    else:
        result = fibonacci_fast(n-1) + fibonacci_fast(n-2)

    fibonacci_cache[n] = result
    return result

# Test
import time
start = time.time()
print(fibonacci_slow(35))  # Très lent !
print(f"Sans cache : {time.time() - start:.4f}s")

start = time.time()
print(fibonacci_fast(35))  # Très rapide !
print(f"Avec cache : {time.time() - start:.4f}s")
```

### Cache avec `@lru_cache`

Python fournit un décorateur pratique pour le caching :

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache les 128 derniers appels
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Utilisation
print(fibonacci(100))  # Instantané grâce au cache !

# Voir les statistiques du cache
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Vider le cache si nécessaire
fibonacci.cache_clear()
```

### Cache avec `@cache` (Python 3.9+)

```python
from functools import cache

@cache  # Cache illimité (équivalent à lru_cache(maxsize=None))
def calcul_lourd(a, b, c):
    # Calcul complexe
    return a ** b + c ** 2

# Première fois : calcule
result1 = calcul_lourd(2, 10, 5)

# Deuxième fois : retourne la valeur en cache (instantané)
result2 = calcul_lourd(2, 10, 5)
```

### Exemple pratique : Cache pour API

```python
import time
from functools import lru_cache
from datetime import datetime, timedelta

@lru_cache(maxsize=100)
def fetch_user_data(user_id):
    """Simule un appel API lent"""
    print(f"Appel API pour user {user_id}...")
    time.sleep(2)  # Simule latence réseau
    return {"id": user_id, "name": f"User {user_id}"}

# Premier appel : lent (2 secondes)
start = time.time()
data = fetch_user_data(123)
print(f"Premier appel : {time.time() - start:.2f}s")

# Deuxième appel : instantané (cache)
start = time.time()
data = fetch_user_data(123)
print(f"Deuxième appel : {time.time() - start:.2f}s")
```

---

## Optimisation des boucles

### Déplacer le code invariant hors de la boucle

```python
import math

# ❌ Lent : calcule sqrt(2) à chaque itération
def slow_loop():
    result = []
    for i in range(1000):
        result.append(i * math.sqrt(2))  # sqrt(2) recalculé 1000 fois !
    return result

# ✅ Rapide : calcule sqrt(2) une seule fois
def fast_loop():
    sqrt_2 = math.sqrt(2)  # Calculé une seule fois
    result = []
    for i in range(1000):
        result.append(i * sqrt_2)
    return result

# ✅✅ Encore mieux : list comprehension
def fastest_loop():
    sqrt_2 = math.sqrt(2)
    return [i * sqrt_2 for i in range(1000)]
```

### Éviter les appels de méthodes dans les conditions

```python
# ❌ Lent : appelle len() à chaque itération
def slow_iteration(items):
    i = 0
    while i < len(items):  # len() appelé à chaque fois !
        print(items[i])
        i += 1

# ✅ Rapide : calcule len() une fois
def fast_iteration(items):
    length = len(items)
    i = 0
    while i < length:
        print(items[i])
        i += 1

# ✅✅ Pythonique : utiliser for
def pythonic_iteration(items):
    for item in items:
        print(item)
```

### Utiliser enumerate au lieu des indices

```python
items = ["a", "b", "c", "d"]

# ❌ Lent
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# ✅ Rapide et lisible
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

---

## NumPy pour les calculs numériques

Pour les **calculs numériques intensifs**, NumPy est **10-100x plus rapide** que le Python pur !

```python
import numpy as np
import time

# ❌ Lent : boucle Python pure
def python_sum(n):
    numbers = list(range(n))
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# ✅ Rapide : NumPy vectorisé
def numpy_sum(n):
    numbers = np.arange(n)
    return np.sum(numbers ** 2)

# Comparaison
n = 1000000

start = time.time()
result1 = python_sum(n)
print(f"Python pur : {time.time() - start:.4f}s")

start = time.time()
result2 = numpy_sum(n)
print(f"NumPy : {time.time() - start:.4f}s")
# NumPy est BEAUCOUP plus rapide !
```

### Opérations vectorisées

```python
import numpy as np

# ❌ Lent : boucle
data = [1, 2, 3, 4, 5]
result = []
for x in data:
    result.append(x * 2 + 10)

# ✅ Rapide : vectorisé
data_np = np.array([1, 2, 3, 4, 5])
result_np = data_np * 2 + 10  # Appliqué à tous les éléments en une fois !

print(result_np)  # [12 14 16 18 20]
```

---

## Multiprocessing et Threading

Python a le **GIL** (Global Interpreter Lock) qui empêche le vrai parallélisme avec des threads pour le code Python pur. Solutions :

### Threading pour les opérations I/O

Bon pour : requêtes réseau, lecture/écriture fichiers

```python
import time
import threading

def download_file(url):
    """Simule un téléchargement"""
    print(f"Début téléchargement : {url}")
    time.sleep(2)  # Simule latence réseau
    print(f"Fin téléchargement : {url}")

urls = [f"http://example.com/file{i}" for i in range(5)]

# ❌ Séquentiel : 10 secondes
start = time.time()
for url in urls:
    download_file(url)
print(f"Séquentiel : {time.time() - start:.2f}s")

# ✅ Avec threads : ~2 secondes
start = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Avec threads : {time.time() - start:.2f}s")
```

### Multiprocessing pour le CPU intensif

Bon pour : calculs mathématiques, traitement d'images, machine learning

```python
from multiprocessing import Pool
import time

def calcul_lourd(n):
    """Calcul CPU-intensif"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

numbers = [10000000, 10000000, 10000000, 10000000]

# ❌ Séquentiel
start = time.time()
results = [calcul_lourd(n) for n in numbers]
print(f"Séquentiel : {time.time() - start:.2f}s")

# ✅ Parallèle
start = time.time()
with Pool(processes=4) as pool:
    results = pool.map(calcul_lourd, numbers)
print(f"Parallèle : {time.time() - start:.2f}s")
```

### Quand utiliser quoi ?

| Type de tâche | Solution | Raison |
|---------------|----------|--------|
| **I/O (réseau, fichiers)** | `threading` | GIL n'est pas un problème |
| **CPU intensif** | `multiprocessing` | Contourne le GIL |
| **Async I/O** | `asyncio` | Plus efficace que threads |
| **Simple** | Séquentiel | Pas de complexité ajoutée |

---

## Asyncio pour l'I/O asynchrone

`asyncio` est encore plus efficace que `threading` pour l'I/O car il utilise moins de ressources.

```python
import asyncio
import time

async def fetch_data(url):
    """Simule une requête asynchrone"""
    print(f"Début fetch : {url}")
    await asyncio.sleep(2)  # I/O non-bloquant
    print(f"Fin fetch : {url}")
    return f"Données de {url}"

async def main():
    urls = [f"http://api.example.com/{i}" for i in range(5)]

    # Lancer toutes les requêtes en parallèle
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)

    return results

# Exécution
start = time.time()
results = asyncio.run(main())
print(f"Temps total : {time.time() - start:.2f}s")
# ~2 secondes au lieu de 10 !
```

---

## Optimisation de la mémoire

### Utiliser __slots__ pour les classes

```python
import sys

# ❌ Classe normale : utilise un dict interne
class PersonNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ✅ Avec __slots__ : plus compact
class PersonSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Comparaison mémoire
p1 = PersonNormal("Alice", 30)
p2 = PersonSlots("Alice", 30)

print(f"Sans slots : {sys.getsizeof(p1.__dict__)} bytes")
print(f"Avec slots : {sys.getsizeof(p2)} bytes")

# Avec des milliers d'instances, l'économie est significative !
```

### Générateurs au lieu de listes

```python
# ❌ Liste : tout en mémoire
def get_squares_list(n):
    return [i**2 for i in range(n)]

# ✅ Générateur : économise la mémoire
def get_squares_gen(n):
    return (i**2 for i in range(n))

# Pour de grandes valeurs de n, la différence est énorme
```

### Libérer la mémoire explicitement

```python
import gc

# Traiter de grandes données
def process_large_data():
    large_list = [i for i in range(10000000)]
    result = sum(large_list)

    # Libérer la mémoire
    del large_list
    gc.collect()  # Force le garbage collector

    return result
```

---

## Outils d'optimisation Python

### PyPy : Interpréteur Python plus rapide

**PyPy** est un interpréteur Python alternatif avec un compilateur JIT (Just-In-Time) qui peut être **2-10x plus rapide** que CPython.

Installation :
```bash
# Linux/Mac
pip install pypy

# Ou télécharger depuis pypy.org
```

Utilisation :
```bash
pypy mon_script.py  # Au lieu de python mon_script.py
```

**Quand utiliser PyPy ?**
- Calculs intensifs
- Boucles longues
- Code pur Python (pas compatible avec tous les packages C)

### Cython : Compiler Python en C

**Cython** permet de compiler du code Python en C pour des gains de performance énormes.

```python
# fichier: calcul.pyx
def calcul_lourd(int n):
    cdef int i
    cdef long result = 0

    for i in range(n):
        result += i * i

    return result
```

```bash
# Compiler
cython calcul.pyx
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
    -I/usr/include/python3.9 -o calcul.so calcul.c
```

### Numba : JIT compilation

**Numba** compile les fonctions Python en code machine à la volée.

```python
from numba import jit
import numpy as np

# Sans Numba
def function_slow(x):
    result = 0
    for i in range(len(x)):
        result += x[i] ** 2
    return result

# Avec Numba
@jit(nopython=True)
def function_fast(x):
    result = 0
    for i in range(len(x)):
        result += x[i] ** 2
    return result

x = np.arange(1000000)

# function_fast sera beaucoup plus rapide après le premier appel
```

---

## Bonnes pratiques d'optimisation

### 1. Profiler d'abord, optimiser ensuite

```python
# Ne faites JAMAIS d'optimisation sans mesurer
import cProfile

cProfile.run('ma_fonction()')
# Identifiez les vrais goulots d'étranglement
```

### 2. Commencer par les algorithmes

Un meilleur algorithme bat toujours les micro-optimisations.

```python
# ❌ O(n²) : lent même optimisé
def find_duplicates_slow(items):
    duplicates = []
    for i, item in enumerate(items):
        for j, other in enumerate(items):
            if i != j and item == other and item not in duplicates:
                duplicates.append(item)
    return duplicates

# ✅ O(n) : rapide
def find_duplicates_fast(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
```

### 3. Utiliser les bonnes structures de données

```python
# Choisir la structure adaptée au cas d'usage
if need_fast_lookup:
    use_dict_or_set()
elif need_ordered:
    use_list()
elif need_unique_ordered:
    use_dict()  # Python 3.7+
elif need_fast_queue:
    use_deque()
```

### 4. Lazy evaluation

Ne calculez que ce dont vous avez besoin.

```python
# ❌ Calcule tout
def get_all_results():
    return [expensive_operation(i) for i in range(1000)]

# ✅ Calcule à la demande
def get_results_lazy():
    return (expensive_operation(i) for i in range(1000))

# Utilisation
for result in get_results_lazy():
    if condition_met(result):
        break  # Arrête tôt, n'a pas tout calculé !
```

### 5. Éviter les optimisations prématurées

```python
# ❌ Trop optimisé, illisible
def complex_optimized(data):
    return reduce(lambda x, y: x + y[0] * y[1],
                  zip(data, range(len(data))), 0)

# ✅ Simple et lisible (optimiser seulement si nécessaire)
def simple_readable(data):
    total = 0
    for i, value in enumerate(data):
        total += value * i
    return total

# Si vraiment nécessaire après profiling :
def optimized_if_needed(data):
    return sum(value * i for i, value in enumerate(data))
```

---

## Checklist d'optimisation

Suivez cette checklist dans l'ordre :

### ✅ Étape 1 : Fonctionnalité
- [ ] Mon code fonctionne correctement ?
- [ ] J'ai des tests ?
- [ ] Le code est lisible ?

### ✅ Étape 2 : Mesure
- [ ] J'ai identifié que j'ai un problème de performance ?
- [ ] J'ai profilé mon code (cProfile, line_profiler) ?
- [ ] Je connais les fonctions/lignes lentes ?

### ✅ Étape 3 : Algorithme
- [ ] Mon algorithme est-il optimal (complexité) ?
- [ ] Puis-je utiliser une meilleure structure de données ?
- [ ] Y a-t-il des calculs redondants ?

### ✅ Étape 4 : Python
- [ ] J'utilise les built-ins quand possible ?
- [ ] J'utilise des comprehensions ?
- [ ] J'évite les concaténations de strings ?
- [ ] Mes variables locales au lieu de globales ?

### ✅ Étape 5 : Caching
- [ ] Puis-je mettre en cache des résultats ?
- [ ] @lru_cache serait-il utile ?

### ✅ Étape 6 : Mémoire
- [ ] Puis-je utiliser des générateurs ?
- [ ] __slots__ pour les classes ?
- [ ] Libération explicite de mémoire ?

### ✅ Étape 7 : Parallélisme
- [ ] Threading pour I/O ?
- [ ] Multiprocessing pour CPU ?
- [ ] Asyncio pour I/O async ?

### ✅ Étape 8 : Outils avancés
- [ ] NumPy pour calculs numériques ?
- [ ] PyPy comme interpréteur ?
- [ ] Cython/Numba pour code critique ?

---

## Exemples d'optimisations réelles

### Exemple 1 : Traitement de fichier CSV

```python
import csv
import pandas as pd

# ❌ Lent : charge tout en mémoire
def process_csv_slow(filename):
    with open(filename, 'r') as f:
        data = list(csv.reader(f))

    total = 0
    for row in data:
        total += int(row[2])  # Colonne prix
    return total

# ✅ Rapide : traitement ligne par ligne
def process_csv_fast(filename):
    total = 0
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            total += int(row[2])
    return total

# ✅✅ Le plus rapide : pandas (optimisé en C)
def process_csv_pandas(filename):
    df = pd.read_csv(filename)
    return df.iloc[:, 2].sum()
```

### Exemple 2 : Recherche dans des données

```python
# Données : liste de transactions
transactions = [
    {"id": 1, "user_id": 101, "amount": 50},
    {"id": 2, "user_id": 102, "amount": 75},
    # ... des milliers ...
]

# ❌ O(n) à chaque recherche
def get_user_total_slow(user_id):
    total = 0
    for transaction in transactions:
        if transaction["user_id"] == user_id:
            total += transaction["amount"]
    return total

# ✅ O(1) après indexation
from collections import defaultdict

# Créer un index une seule fois
user_totals = defaultdict(int)
for transaction in transactions:
    user_totals[transaction["user_id"]] += transaction["amount"]

def get_user_total_fast(user_id):
    return user_totals[user_id]
```

### Exemple 3 : Génération de rapport

```python
# ❌ Lent et gourmand
def generate_report_slow(data):
    report = ""
    for item in data:
        report += f"Nom: {item['name']}\n"  # Concaténation lente !
        report += f"Valeur: {item['value']}\n"
        report += "-" * 40 + "\n"
    return report

# ✅ Rapide
def generate_report_fast(data):
    lines = []
    for item in data:
        lines.append(f"Nom: {item['name']}")
        lines.append(f"Valeur: {item['value']}")
        lines.append("-" * 40)
    return "\n".join(lines)

# ✅✅ Plus pythonique
def generate_report_pythonic(data):
    return "\n".join(
        f"Nom: {item['name']}\nValeur: {item['value']}\n{'-'*40}"
        for item in data
    )
```

---

## Résumé

L'optimisation en Python suit cette philosophie :

1. **Faites fonctionner** votre code d'abord ✅
2. **Mesurez** les performances 📊
3. **Optimisez** les vrais goulots 🚀
4. **Mesurez** à nouveau pour vérifier 📈

### Règles d'or

✅ **Profiler avant d'optimiser** : ne devinez pas, mesurez !

✅ **Algorithme d'abord** : O(n) bat toujours O(n²) optimisé

✅ **Bonnes structures de données** : dict/set pour lookup, list pour ordre

✅ **Built-ins et stdlib** : ils sont écrits en C et très rapides

✅ **Éviter les pièges** : concaténation de strings, recherches répétées

✅ **Générateurs** : économisez la mémoire pour les grands volumes

✅ **Caching** : @lru_cache pour éviter les recalculs

✅ **Parallélisme** : threading (I/O), multiprocessing (CPU), asyncio (async I/O)

✅ **Outils spécialisés** : NumPy (calcul), Pandas (données), PyPy (interpréteur)

### N'oubliez pas

> "Premature optimization is the root of all evil" - Donald Knuth

**Mais** :

> "Premature pessimization is equally evil" - Herb Sutter

Écrivez du code propre et lisible. Optimisez seulement quand nécessaire, là où ça compte vraiment ! 🎯

⏭️ [Déploiement et distribution](/12-projets-et-bonnes-pratiques/05-deploiement-et-distribution.md)
