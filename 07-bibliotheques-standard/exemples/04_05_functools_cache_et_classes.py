# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Module functools - lru_cache, wraps, total_ordering,
#                 singledispatch, triangle de Pascal
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

from functools import lru_cache, wraps, total_ordering, singledispatch
import time

# --- lru_cache() ---
print("=== lru_cache() - Fibonacci ===")

def fibonacci_lent(n):
    if n < 2:
        return n
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)

@lru_cache(maxsize=None)
def fibonacci_rapide(n):
    if n < 2:
        return n
    return fibonacci_rapide(n-1) + fibonacci_rapide(n-2)

# Sans cache
debut = time.time()
resultat = fibonacci_lent(30)
duree = time.time() - debut
print(f"Sans cache : fibonacci(30) = {resultat} en {duree:.4f}s")

# Avec cache
debut = time.time()
resultat = fibonacci_rapide(30)
duree = time.time() - debut
print(f"Avec cache : fibonacci(30) = {resultat} en {duree:.6f}s")

print(f"Cache info : {fibonacci_rapide.cache_info()}")
fibonacci_rapide.cache_clear()

# --- Factorielle et Triangle de Pascal ---
print("\n=== Triangle de Pascal (avec cache) ===")

@lru_cache(maxsize=128)
def factorielle(n):
    if n < 2:
        return 1
    return n * factorielle(n - 1)

@lru_cache(maxsize=128)
def combinaison(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorielle(n) // (factorielle(k) * factorielle(n - k))

print(f"10! = {factorielle(10):,}")
print(f"C(10, 3) = {combinaison(10, 3)}")

print("\nTriangle de Pascal :")
for n in range(7):
    ligne = [combinaison(n, k) for k in range(n + 1)]
    print(" ".join(f"{c:3d}" for c in ligne).center(30))

# --- wraps() ---
print("\n=== wraps() ===")

def chronometrer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        duree = time.time() - debut
        print(f"  Durée de {func.__name__} : {duree:.4f}s")
        return resultat
    return wrapper

@chronometrer
def calcul_long(n):
    """Effectue un calcul long"""
    return sum(range(n))

resultat = calcul_long(1_000_000)
print(f"  Nom : {calcul_long.__name__}")
print(f"  Doc : {calcul_long.__doc__}")
print(f"  Résultat : {resultat}")

# --- total_ordering() ---
print("\n=== total_ordering() ===")

@total_ordering
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, autre):
        return self.age == autre.age

    def __lt__(self, autre):
        return self.age < autre.age

    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"

alice = Personne("Alice", 25)
bob = Personne("Bob", 30)
charlie = Personne("Charlie", 25)

print(f"alice == charlie : {alice == charlie}")
print(f"alice < bob : {alice < bob}")
print(f"bob > alice : {bob > alice}")
print(f"alice <= charlie : {alice <= charlie}")

personnes = [bob, alice, charlie]
personnes_triees = sorted(personnes)
print(f"Triées : {personnes_triees}")

# --- singledispatch() ---
print("\n=== singledispatch() ===")

@singledispatch
def traiter(donnee):
    print(f"  Type non supporté : {type(donnee).__name__}")

@traiter.register(int)
def _(donnee):
    print(f"  Entier : {donnee} x 2 = {donnee * 2}")

@traiter.register(str)
def _(donnee):
    print(f"  Chaîne : '{donnee}' -> '{donnee.upper()}'")

@traiter.register(list)
def _(donnee):
    print(f"  Liste : {len(donnee)} éléments, somme = {sum(donnee)}")

traiter(10)
traiter("bonjour")
traiter([1, 2, 3, 4, 5])
traiter(3.14)
