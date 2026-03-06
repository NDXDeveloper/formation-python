# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Exemple complet - Optimisation progressive d'un calcul
#                 de statistiques (v1: boucles, v2: built-in, v3: NumPy)
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import timeit
import numpy as np

# ============================================================================
# VERSION 1 : Code initial (non optimise)
# ============================================================================
def calculer_statistiques_v1(donnees):
    """Version initiale, non optimisee."""
    total = 0
    for valeur in donnees:
        total += valeur
    moyenne = total / len(donnees)

    ecarts = []
    for valeur in donnees:
        ecart = (valeur - moyenne) ** 2
        ecarts.append(ecart)

    somme_ecarts = 0
    for ecart in ecarts:
        somme_ecarts += ecart
    variance = somme_ecarts / len(donnees)

    return moyenne, variance

# ============================================================================
# VERSION 2 : Utilisation des fonctions built-in
# ============================================================================
def calculer_statistiques_v2(donnees):
    """Version optimisee avec fonctions built-in."""
    moyenne = sum(donnees) / len(donnees)
    ecarts = [(valeur - moyenne) ** 2 for valeur in donnees]
    variance = sum(ecarts) / len(donnees)
    return moyenne, variance

# ============================================================================
# VERSION 3 : Optimisation maximale avec NumPy
# ============================================================================
def calculer_statistiques_v3(donnees):
    """Version ultra-optimisee avec NumPy."""
    arr = np.array(donnees)
    moyenne = np.mean(arr)
    variance = np.var(arr)
    return float(moyenne), float(variance)

# ============================================================================
# TESTS DE PERFORMANCE
# ============================================================================
def comparer_versions():
    """Compare les performances des trois versions."""
    donnees = list(range(10000))

    print("=" * 70)
    print("COMPARAISON DES VERSIONS")
    print("=" * 70)

    # Version 1
    temps_v1 = timeit.timeit(lambda: calculer_statistiques_v1(donnees), number=100)
    print(f"Version 1 (code initial)      : {temps_v1:.4f} secondes")

    # Version 2
    temps_v2 = timeit.timeit(lambda: calculer_statistiques_v2(donnees), number=100)
    print(f"Version 2 (fonctions built-in): {temps_v2:.4f} secondes")
    print(f"  Amelioration : {temps_v1/temps_v2:.2f}x plus rapide")

    # Version 3
    temps_v3 = timeit.timeit(lambda: calculer_statistiques_v3(donnees), number=100)
    print(f"Version 3 (NumPy)             : {temps_v3:.4f} secondes")
    print(f"  Amelioration : {temps_v1/temps_v3:.2f}x plus rapide que v1")
    print(f"  Amelioration : {temps_v2/temps_v3:.2f}x plus rapide que v2")

    # Verification des resultats
    print("\n" + "=" * 70)
    print("VERIFICATION DES RESULTATS")
    print("=" * 70)

    r1 = calculer_statistiques_v1(donnees)
    r2 = calculer_statistiques_v2(donnees)
    r3 = calculer_statistiques_v3(donnees)

    print(f"Version 1 : Moyenne = {r1[0]:.2f}, Variance = {r1[1]:.2f}")
    print(f"Version 2 : Moyenne = {r2[0]:.2f}, Variance = {r2[1]:.2f}")
    print(f"Version 3 : Moyenne = {r3[0]:.2f}, Variance = {r3[1]:.2f}")

    # Verifier l'exactitude (tolerance pour les flottants)
    assert abs(r1[0] - r2[0]) < 0.01
    assert abs(r1[1] - r2[1]) < 0.01
    assert abs(r1[0] - r3[0]) < 0.01
    assert abs(r1[1] - r3[1]) < 0.01
    print("Tous les resultats sont identiques !")

comparer_versions()
