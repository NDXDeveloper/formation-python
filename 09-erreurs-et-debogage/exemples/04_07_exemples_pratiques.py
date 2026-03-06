# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Exemples pratiques d'optimisation - doublons (O(n2) vs O(n)),
#                 somme des carres (5 methodes), filtrage et transformation
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import timeit
import numpy as np

# ==========================================
# 1. Trouver les doublons
# ==========================================
print("=== Trouver les doublons ===\n")

def trouver_doublons_lent(liste):
    """Methode lente avec boucles imbriquees O(n2)."""
    doublons = []
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if liste[i] == liste[j] and liste[i] not in doublons:
                doublons.append(liste[i])
    return doublons

def trouver_doublons_rapide(liste):
    """Methode rapide avec un set O(n)."""
    vus = set()
    doublons = set()
    for element in liste:
        if element in vus:
            doublons.add(element)
        else:
            vus.add(element)
    return list(doublons)

test_liste = list(range(1000)) * 2

temps_lent = timeit.timeit(lambda: trouver_doublons_lent(test_liste), number=10)
temps_rapide = timeit.timeit(lambda: trouver_doublons_rapide(test_liste), number=10)

print(f"  Methode lente (O(n2))  : {temps_lent:.4f} secondes")
print(f"  Methode rapide (O(n)) : {temps_rapide:.4f} secondes")
print(f"  Amelioration   : {temps_lent/temps_rapide:.2f}x plus rapide")

# Verification
doublons_lent = sorted(trouver_doublons_lent(test_liste))
doublons_rapide = sorted(trouver_doublons_rapide(test_liste))
assert doublons_lent == doublons_rapide
print(f"  Doublons trouves : {len(doublons_rapide)} (verifie)")

# ==========================================
# 2. Somme des carres - 5 methodes
# ==========================================
print("\n=== Somme des carres (5 methodes) ===\n")

n = 100000

def methode_boucle(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def methode_comprehension(n):
    return sum([i ** 2 for i in range(n)])

def methode_generateur(n):
    return sum(i ** 2 for i in range(n))

def methode_numpy(n):
    return int(np.sum(np.arange(n) ** 2))

def methode_formule(n):
    # Formule : somme des carres de 0 a n-1 = (n-1)*n*(2n-1)/6
    return (n - 1) * n * (2 * n - 1) // 6

methodes = {
    "Boucle for": methode_boucle,
    "Comprehension": methode_comprehension,
    "Generateur": methode_generateur,
    "NumPy": methode_numpy,
    "Formule math": methode_formule
}

print(f"Somme des carres de 0 a {n-1}:\n")
resultats = {}

for nom, methode in methodes.items():
    temps = timeit.timeit(lambda m=methode: m(n), number=100)
    resultats[nom] = temps
    print(f"  {nom:20} : {temps:.6f} secondes")

plus_rapide = min(resultats, key=resultats.get)
print(f"\n  La methode '{plus_rapide}' est la plus rapide !")

# Verification que toutes les methodes donnent le meme resultat
resultats_valeurs = [m(n) for m in methodes.values()]
assert all(r == resultats_valeurs[0] for r in resultats_valeurs)
print(f"  Resultat verifie : {resultats_valeurs[0]}")

# ==========================================
# 3. Filtrer et transformer
# ==========================================
print("\n=== Filtrer et transformer ===\n")

donnees = list(range(100000))

def methode1(donnees):
    resultat = []
    for x in donnees:
        if x % 2 == 0:
            resultat.append(x ** 2)
    return resultat

def methode2(donnees):
    return [x ** 2 for x in donnees if x % 2 == 0]

def methode3(donnees):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, donnees)))

temps1 = timeit.timeit(lambda: methode1(donnees), number=100)
temps2 = timeit.timeit(lambda: methode2(donnees), number=100)
temps3 = timeit.timeit(lambda: methode3(donnees), number=100)

print("Filtrer les pairs et calculer leur carre :")
print(f"  Boucle for      : {temps1:.4f} secondes")
print(f"  Comprehension   : {temps2:.4f} secondes")
print(f"  filter() + map(): {temps3:.4f} secondes")

# Verification
assert methode1(donnees) == methode2(donnees) == methode3(donnees)
print(f"  Resultats identiques : {len(methode2(donnees))} elements")
