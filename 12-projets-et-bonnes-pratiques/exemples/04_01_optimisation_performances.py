# ============================================================================
#   Section 12.4 : Optimisation des performances
#   Description : Mesure du temps (time, timeit, decorateur), profiling (cProfile),
#                 structures de donnees (list vs set vs dict), list comprehensions,
#                 concatenation strings, generateurs vs listes, caching (lru_cache),
#                 optimisation boucles, __slots__, duplicates O(n) vs O(n2),
#                 asyncio gather
#   Fichier source : 04-optimisation-performances.md
# ============================================================================

"""Optimisation des performances Python."""

import sys
import time
import timeit
import cProfile
import pstats
from collections import defaultdict, Counter, deque
from functools import wraps, lru_cache, cache
from io import StringIO


# ============================================================
# MESURE DU TEMPS
# ============================================================
print("=" * 50)
print("MESURE DU TEMPS")
print("=" * 50)

# --- Mesure simple ---
start = time.time()
result = sum(range(1000000))
end = time.time()
print(f"\n  sum(range(1000000)) = {result}")
print(f"  Temps : {end - start:.4f} secondes")


# --- timeit ---
temps = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"\n  timeit join : {temps / 10000:.6f} secondes/appel")


def approche1():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result


def approche2():
    return [i * 2 for i in range(1000)]


temps1 = timeit.timeit(approche1, number=10000)
temps2 = timeit.timeit(approche2, number=10000)

print(f"\n  Boucle for : {temps1:.4f}s")
print(f"  Comprehension : {temps2:.4f}s")
print(f"  Comprehension est {temps1 / temps2:.2f}x plus rapide")


# --- Decorateur de mesure ---

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper


@measure_time
def traiter_donnees(n):
    return sum(range(n))


print()
traiter_donnees(1000000)


# ============================================================
# PROFILING
# ============================================================
print(f"\n{'=' * 50}")
print("PROFILING (cProfile)")
print("=" * 50)


def fonction_complexe():
    result = []
    for i in range(10000):
        for j in range(100):
            result.append(i * j)
    return result


def autre_fonction():
    return sum(range(1000000))


def main_profile():
    fonction_complexe()
    autre_fonction()


profiler = cProfile.Profile()
profiler.enable()
main_profile()
profiler.disable()

stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(5)
print(f"\n  Top 5 fonctions (profiling) :")
for line in stream.getvalue().split('\n')[5:12]:
    if line.strip():
        print(f"  {line}")


# ============================================================
# STRUCTURES DE DONNEES
# ============================================================
print(f"\n{'=' * 50}")
print("STRUCTURES DE DONNEES")
print("=" * 50)

# --- Liste vs Set ---
data = list(range(10000))
data_set = set(data)

start = time.time()
for i in range(1000):
    _ = 9999 in data
temps_liste = time.time() - start

start = time.time()
for i in range(1000):
    _ = 9999 in data_set
temps_set = time.time() - start

print(f"\n  Recherche 'in' (1000 fois) :")
print(f"  Liste : {temps_liste:.4f}s")
print(f"  Set : {temps_set:.6f}s")
print(f"  Set est {temps_liste / temps_set:.0f}x plus rapide")


# --- Collections specialisees ---

# defaultdict
word_count_dd = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count_dd[word] += 1
print(f"\n  defaultdict : {dict(word_count_dd)}")

# Counter
word_count_c = Counter(["apple", "banana", "apple", "cherry", "banana", "apple"])
print(f"  Counter : {word_count_c}")
print(f"  Most common : {word_count_c.most_common(2)}")

# deque
file = deque(maxlen=5)
for i in range(7):
    file.append(i)
print(f"\n  deque(maxlen=5) apres 7 append : {list(file)}")

file2 = deque()
file2.appendleft("premier")
file2.appendleft("deuxieme")
file2.append("dernier")
print(f"  deque appendleft : {list(file2)}")


# ============================================================
# OPTIMISATIONS CODE
# ============================================================
print(f"\n{'=' * 50}")
print("OPTIMISATIONS CODE")
print("=" * 50)

# --- Comprehensions vs boucles vs map ---

def avec_boucle():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result


def avec_comprehension():
    return [i * 2 for i in range(1000)]


def avec_map():
    return list(map(lambda x: x * 2, range(1000)))


t1 = timeit.timeit(avec_boucle, number=10000)
t2 = timeit.timeit(avec_comprehension, number=10000)
t3 = timeit.timeit(avec_map, number=10000)

print(f"\n  Boucle : {t1:.4f}s")
print(f"  Comprehension : {t2:.4f}s")
print(f"  Map : {t3:.4f}s")


# --- Concatenation strings ---

def concat_slow(words):
    result = ""
    for word in words:
        result += word + " "
    return result


def concat_fast(words):
    return " ".join(words)


words = ["mot"] * 10000
ts = timeit.timeit(lambda: concat_slow(words), number=10)
tf = timeit.timeit(lambda: concat_fast(words), number=10)
print(f"\n  Concat '+=' : {ts:.4f}s")
print(f"  Concat join : {tf:.4f}s")
print(f"  join est {ts / tf:.1f}x plus rapide")


# --- Deduplication ---

def find_duplicates_slow(items):
    duplicates = []
    for i, item in enumerate(items):
        for j, other in enumerate(items):
            if i != j and item == other and item not in duplicates:
                duplicates.append(item)
    return duplicates


def find_duplicates_fast(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


test_data = list(range(500)) + list(range(250))

start = time.time()
r1 = find_duplicates_slow(test_data)
t_slow = time.time() - start

start = time.time()
r2 = find_duplicates_fast(test_data)
t_fast = time.time() - start

print(f"\n  Deduplication O(n2) : {t_slow:.4f}s ({len(r1)} doublons)")
print(f"  Deduplication O(n) : {t_fast:.6f}s ({len(r2)} doublons)")


# ============================================================
# GENERATEURS vs LISTES
# ============================================================
print(f"\n{'=' * 50}")
print("GENERATEURS vs LISTES")
print("=" * 50)


def get_numbers_list(n):
    return [i for i in range(n)]


def get_numbers_generator(n):
    for i in range(n):
        yield i


liste = get_numbers_list(1000000)
generateur = get_numbers_generator(1000000)

print(f"\n  Taille liste (1M) : {sys.getsizeof(liste) / 1024 / 1024:.2f} MB")
print(f"  Taille generateur : {sys.getsizeof(generateur)} bytes")

# Generator expression
squares_gen = (x ** 2 for x in range(1000000))
total = sum(squares_gen)
print(f"\n  Sum squares (generateur) : {total}")


# ============================================================
# CACHING
# ============================================================
print(f"\n{'=' * 50}")
print("CACHING")
print("=" * 50)

# --- Fibonacci sans cache ---

def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


# --- Fibonacci avec cache dict ---

fibonacci_cache = {}


def fibonacci_fast(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_fast(n - 1) + fibonacci_fast(n - 2)
    fibonacci_cache[n] = result
    return result


start = time.time()
r1 = fibonacci_slow(30)
t1 = time.time() - start

start = time.time()
r2 = fibonacci_fast(30)
t2 = time.time() - start

print(f"\n  fibonacci(30) sans cache : {r1} en {t1:.4f}s")
print(f"  fibonacci(30) avec cache : {r2} en {t2:.6f}s")


# --- lru_cache ---

@lru_cache(maxsize=128)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


result = fibonacci_lru(100)
print(f"\n  fibonacci(100) avec lru_cache : {result}")
print(f"  Cache info : {fibonacci_lru.cache_info()}")
fibonacci_lru.cache_clear()


# --- @cache ---

@cache
def calcul_lourd(a, b, c):
    return a ** b + c ** 2


r1 = calcul_lourd(2, 10, 5)
r2 = calcul_lourd(2, 10, 5)
print(f"\n  calcul_lourd(2, 10, 5) = {r1}")
print(f"  Meme resultat depuis cache : {r1 == r2}")


# ============================================================
# OPTIMISATION MEMOIRE : __slots__
# ============================================================
print(f"\n{'=' * 50}")
print("OPTIMISATION MEMOIRE : __slots__")
print("=" * 50)


class PersonNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = PersonNormal("Alice", 30)
p2 = PersonSlots("Alice", 30)

print(f"\n  Sans slots (__dict__) : {sys.getsizeof(p1.__dict__)} bytes")
print(f"  Avec slots : {sys.getsizeof(p2)} bytes")


# ============================================================
# ASYNCIO
# ============================================================
print(f"\n{'=' * 50}")
print("ASYNCIO")
print("=" * 50)

import asyncio


async def fetch_data(url):
    await asyncio.sleep(0.5)
    return f"Donnees de {url}"


async def main_async():
    urls = [f"http://api.example.com/{i}" for i in range(5)]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


start = time.time()
results = asyncio.run(main_async())
elapsed = time.time() - start
print(f"\n  5 fetches paralleles en {elapsed:.2f}s (au lieu de ~2.5s)")
print(f"  Resultats : {len(results)} reponses")
for r in results[:2]:
    print(f"    {r}")
print(f"    ...")


# ============================================================
# RESUME
# ============================================================
print(f"\n{'=' * 50}")
print("RESUME DES OPTIMISATIONS")
print("=" * 50)

resume = [
    ("Recherche", "list -> set", "O(n) -> O(1)"),
    ("Comprehension", "boucle -> [...]", "~1.5x plus rapide"),
    ("Strings", "+= -> join()", "~10x plus rapide"),
    ("Cache", "recalcul -> lru_cache", "N fois plus rapide"),
    ("Memoire", "list -> generator", "MB -> bytes"),
    ("Classes", "normal -> __slots__", "~40% moins memoire"),
    ("Parallele", "sequentiel -> asyncio", "Nx plus rapide (I/O)"),
]

print(f"\n  {'Technique':20s} {'Changement':25s} {'Gain'}")
print(f"  {'-' * 65}")
for tech, change, gain in resume:
    print(f"  {tech:20s} {change:25s} {gain}")
