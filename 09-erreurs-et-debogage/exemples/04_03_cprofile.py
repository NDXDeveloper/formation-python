# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : cProfile - profiling detaille (nombre d'appels, temps
#                 par fonction), pstats, decorateur de profiling, Fibonacci
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import cProfile
import pstats
import io
import os
from functools import wraps

# ==========================================
# 1. cProfile basique
# ==========================================
print("=== cProfile basique ===\n")

def fonction_lente():
    """Simule une fonction qui prend du temps."""
    total = 0
    for i in range(1000000):
        total += i
    return total

def fonction_intermediaire():
    """Appelle plusieurs fois la fonction lente."""
    resultats = []
    for _ in range(5):
        resultats.append(fonction_lente())
    return resultats

def programme_principal():
    """Point d'entree du programme."""
    print("Demarrage du programme...")
    resultats = fonction_intermediaire()
    print(f"Resultats calcules : {len(resultats)} valeurs")

cProfile.run('programme_principal()')

# ==========================================
# 2. Profiler et sauvegarder les resultats
# ==========================================
print("\n=== cProfile avec pstats ===\n")

def programme_a_profiler():
    nombres = [i**2 for i in range(100000)]
    return sum(nombres)

fichier_prof = 'resultats_profiling.prof'
cProfile.run('programme_a_profiler()', fichier_prof)

stats = pstats.Stats(fichier_prof)
print("=" * 60)
print("Top 10 des fonctions les plus gourmandes en temps :")
print("=" * 60)
stats.sort_stats('cumulative').print_stats(10)

os.remove(fichier_prof)

# ==========================================
# 3. Decorateur de profiling
# ==========================================
print("\n=== Decorateur de profiling (Fibonacci) ===\n")

def profiler(func):
    """Decorateur pour profiler une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if getattr(wrapper, '_profiling', False):
            return func(*args, **kwargs)

        wrapper._profiling = True
        pr = cProfile.Profile()
        pr.enable()

        resultat = func(*args, **kwargs)

        pr.disable()
        wrapper._profiling = False

        s = io.StringIO()
        stats = pstats.Stats(pr, stream=s)
        stats.sort_stats('cumulative')
        stats.print_stats(10)

        print(f"Profiling de {func.__name__}:")
        print(s.getvalue())

        return resultat
    return wrapper

@profiler
def calculer_fibonacci(n):
    """Calcul de la suite de Fibonacci (version recursive)."""
    if n <= 1:
        return n
    return calculer_fibonacci(n-1) + calculer_fibonacci(n-2)

resultat = calculer_fibonacci(20)
print(f"Fibonacci(20) = {resultat}")
