# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Optimisation avec NumPy - operations vectorisees,
#                 comparaison listes Python vs NumPy arrays
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import numpy as np
import timeit

# ==========================================
# 1. Addition de sequences : listes vs NumPy
# ==========================================
print("=== Listes Python vs NumPy ===\n")

n = 1000000

def operation_liste():
    liste1 = list(range(n))
    liste2 = list(range(n))
    resultat = [a + b for a, b in zip(liste1, liste2)]
    return resultat

def operation_numpy():
    array1 = np.arange(n)
    array2 = np.arange(n)
    resultat = array1 + array2
    return resultat

temps_liste = timeit.timeit(operation_liste, number=10)
temps_numpy = timeit.timeit(operation_numpy, number=10)

print(f"Addition de deux sequences de {n:,} elements :")
print(f"  Listes Python : {temps_liste:.4f} secondes")
print(f"  NumPy arrays  : {temps_numpy:.4f} secondes")
print(f"  NumPy est {temps_liste/temps_numpy:.2f}x plus rapide !")

# ==========================================
# 2. Operations vectorisees
# ==========================================
print("\n=== Operations vectorisees ===\n")

def calcul_avec_boucle(n):
    valeurs = list(range(n))
    resultats = []
    for v in valeurs:
        resultat = (v ** 2 + 2 * v + 1) ** 0.5
        resultats.append(resultat)
    return resultats

def calcul_vectorise(n):
    valeurs = np.arange(n, dtype=float)
    resultats = np.sqrt(valeurs ** 2 + 2 * valeurs + 1)
    return resultats

n_calc = 100000
temps_boucle = timeit.timeit(lambda: calcul_avec_boucle(n_calc), number=10)
temps_vect = timeit.timeit(lambda: calcul_vectorise(n_calc), number=10)

print(f"  Calcul avec boucle  : {temps_boucle:.4f} secondes")
print(f"  Calcul vectorise    : {temps_vect:.4f} secondes")
print(f"  Amelioration        : {temps_boucle/temps_vect:.2f}x plus rapide")

# Verification que les resultats sont identiques
res_boucle = calcul_avec_boucle(10)
res_numpy = calcul_vectorise(10)
print(f"\n  Verification (10 premiers):")
print(f"  Boucle : {[round(x, 2) for x in res_boucle[:5]]}")
print(f"  NumPy  : {[round(x, 2) for x in res_numpy[:5].tolist()]}")
