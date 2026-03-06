# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Techniques d'optimisation - structures de donnees (set vs
#                 liste), calculs repetitifs, comprehensions, fonctions
#                 built-in, lru_cache (memoization), join() vs +
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import timeit
from functools import lru_cache

# ==========================================
# 1. Set vs Liste pour la recherche
# ==========================================
print("=== Set vs Liste (recherche) ===\n")

def test_liste(n=10000):
    ma_liste = list(range(n))
    return 9999 in ma_liste

def test_set(n=10000):
    mon_set = set(range(n))
    return 9999 in mon_set

temps_liste = timeit.timeit(test_liste, number=1000)
temps_set = timeit.timeit(test_set, number=1000)

print(f"  Liste : {temps_liste:.4f} secondes")
print(f"  Set   : {temps_set:.4f} secondes")
print(f"  Amelioration : {temps_liste/temps_set:.0f}x plus rapide avec un set !")

# ==========================================
# 2. Eviter les calculs repetitifs
# ==========================================
print("\n=== Eviter les calculs repetitifs ===\n")

def calculer_distances_lente(points):
    distances = []
    for i in range(len(points)):
        for j in range(len(points)):
            distance = abs(points[i] - points[j])
            distances.append(distance)
    return distances

def calculer_distances_rapide(points):
    distances = []
    n = len(points)
    for i in range(n):
        point_i = points[i]
        for j in range(n):
            distance = abs(point_i - points[j])
            distances.append(distance)
    return distances

points = list(range(1000))
temps_lent = timeit.timeit(lambda: calculer_distances_lente(points), number=10)
temps_rapide = timeit.timeit(lambda: calculer_distances_rapide(points), number=10)

print(f"  Version lente  : {temps_lent:.4f} secondes")
print(f"  Version rapide : {temps_rapide:.4f} secondes")
print(f"  Amelioration   : {(temps_lent-temps_rapide)/temps_lent*100:.1f}%")

# ==========================================
# 3. Comprehensions vs boucles
# ==========================================
print("\n=== Comprehensions vs boucles ===\n")

def avec_boucle(n):
    resultat = []
    for i in range(n):
        if i % 2 == 0:
            resultat.append(i**2)
    return resultat

def avec_comprehension(n):
    return [i**2 for i in range(n) if i % 2 == 0]

n = 10000
temps_boucle = timeit.timeit(lambda: avec_boucle(n), number=1000)
temps_comp = timeit.timeit(lambda: avec_comprehension(n), number=1000)

print(f"  Boucle for       : {temps_boucle:.4f} secondes")
print(f"  Comprehension    : {temps_comp:.4f} secondes")
print(f"  Amelioration     : {temps_boucle/temps_comp:.2f}x plus rapide")

# ==========================================
# 4. Fonctions built-in vs boucles manuelles
# ==========================================
print("\n=== Built-in vs boucles manuelles ===\n")

nombres = list(range(100000))

def somme_manuelle(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

def somme_builtin(liste):
    return sum(liste)

temps_manuel = timeit.timeit(lambda: somme_manuelle(nombres), number=100)
temps_builtin = timeit.timeit(lambda: somme_builtin(nombres), number=100)

print(f"  Boucle manuelle : {temps_manuel:.4f} secondes")
print(f"  Fonction sum()  : {temps_builtin:.4f} secondes")
print(f"  Amelioration    : {temps_manuel/temps_builtin:.2f}x plus rapide")

# ==========================================
# 5. Memoization avec lru_cache
# ==========================================
print("\n=== lru_cache (memoization) ===\n")

def fibonacci_sans_cache(n):
    if n <= 1:
        return n
    return fibonacci_sans_cache(n-1) + fibonacci_sans_cache(n-2)

@lru_cache(maxsize=None)
def fibonacci_avec_cache(n):
    if n <= 1:
        return n
    return fibonacci_avec_cache(n-1) + fibonacci_avec_cache(n-2)

print("Calcul de Fibonacci(30) :")

temps_sans = timeit.timeit(lambda: fibonacci_sans_cache(30), number=1)
print(f"  Sans cache : {temps_sans:.4f} secondes")

temps_avec = timeit.timeit(lambda: fibonacci_avec_cache(30), number=1)
print(f"  Avec cache : {temps_avec:.6f} secondes")

print(f"  Amelioration : {temps_sans/temps_avec:.0f}x plus rapide !")

# Verification
assert fibonacci_sans_cache(30) == fibonacci_avec_cache(30) == 832040
print(f"  Fibonacci(30) = {fibonacci_avec_cache(30)}")

# ==========================================
# 6. join() vs + pour concatenation
# ==========================================
print("\n=== join() vs + (concatenation) ===\n")

def concatenation_avec_plus(n):
    resultat = ""
    for i in range(n):
        resultat = resultat + str(i)
    return resultat

def concatenation_avec_join(n):
    return "".join(str(i) for i in range(n))

n = 5000
temps_plus = timeit.timeit(lambda: concatenation_avec_plus(n), number=10)
temps_join = timeit.timeit(lambda: concatenation_avec_join(n), number=10)

print(f"  Operateur +  : {temps_plus:.4f} secondes")
print(f"  Methode join : {temps_join:.4f} secondes")
print(f"  Amelioration : {temps_plus/temps_join:.2f}x plus rapide")
