# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Module timeit - mesures precises, comparaison de methodes
#                 (boucle, comprehension, map, concatenation + vs join)
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import timeit

# ==========================================
# 1. timeit basique
# ==========================================
print("=== timeit basique ===\n")

temps = timeit.timeit('sum(range(1000))', number=10000)
print(f"  Temps moyen : {temps:.6f} secondes pour 10000 executions")
print(f"  Temps par execution : {temps/10000:.9f} secondes")

# ==========================================
# 2. Comparer differentes approches (carres)
# ==========================================
print("\n=== Comparaison: creation de liste de carres ===\n")

code1 = """
resultat = []
for i in range(1000):
    resultat.append(i**2)
"""

code2 = """
resultat = [i**2 for i in range(1000)]
"""

code3 = """
resultat = list(map(lambda x: x**2, range(1000)))
"""

temps1 = timeit.timeit(code1, number=10000)
temps2 = timeit.timeit(code2, number=10000)
temps3 = timeit.timeit(code3, number=10000)

print("Comparaison des methodes :")
print(f"  Boucle for        : {temps1:.4f} secondes")
print(f"  Comprehension     : {temps2:.4f} secondes")
print(f"  map() + lambda    : {temps3:.4f} secondes")

plus_rapide = min(temps1, temps2, temps3)
if plus_rapide == temps2:
    print(f"\nLa comprehension est {temps1/temps2:.2f}x plus rapide que la boucle")
elif plus_rapide == temps3:
    print(f"\nmap+lambda est {temps1/temps3:.2f}x plus rapide que la boucle")

# ==========================================
# 3. Concatenation + vs join()
# ==========================================
print("\n=== Concatenation: + vs join() ===\n")

def methode_lente():
    """Concatenation de chaines avec +"""
    resultat = ""
    for i in range(1000):
        resultat = resultat + str(i)
    return resultat

def methode_rapide():
    """Utilisation de join()"""
    return "".join(str(i) for i in range(1000))

temps_lent = timeit.timeit(methode_lente, number=1000)
temps_rapide = timeit.timeit(methode_rapide, number=1000)

print(f"  Methode lente (+) : {temps_lent:.4f} secondes")
print(f"  Methode rapide (join) : {temps_rapide:.4f} secondes")
print(f"  Amelioration   : {temps_lent/temps_rapide:.2f}x plus rapide")
