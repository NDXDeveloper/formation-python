# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Profiling memoire - sys.getsizeof, comparaison de
#                 structures (liste, tuple, set, generateur), generateurs
#                 vs listes pour economiser la memoire
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import sys
import tracemalloc

# ==========================================
# 1. Mesurer la taille d'objets en memoire
# ==========================================
print("=== Mesurer la taille des objets ===\n")

def mesurer_taille(objet, nom="Objet"):
    """Affiche la taille d'un objet en memoire."""
    taille = sys.getsizeof(objet)
    if taille < 1024:
        unite = "octets"
        val = taille
    elif taille < 1024**2:
        val = taille / 1024
        unite = "Ko"
    else:
        val = taille / (1024**2)
        unite = "Mo"
    print(f"  {nom}: {val:.2f} {unite}")

liste_petite = [1, 2, 3, 4, 5]
liste_grande = list(range(1000000))
dictionnaire = {i: i**2 for i in range(1000)}
texte = "Python" * 10000

mesurer_taille(liste_petite, "Petite liste")
mesurer_taille(liste_grande, "Grande liste")
mesurer_taille(dictionnaire, "Dictionnaire")
mesurer_taille(texte, "Texte")

# ==========================================
# 2. Comparer les structures de donnees
# ==========================================
print("\n=== Comparaison des structures ===\n")

def comparer_structures(n=1000):
    """Compare l'utilisation memoire de differentes structures."""
    ma_liste = list(range(n))
    mon_tuple = tuple(range(n))
    mon_set = set(range(n))
    mon_generateur = (x for x in range(n))

    print(f"Comparaison pour {n} elements:")
    print(f"  Liste      : {sys.getsizeof(ma_liste):,} octets")
    print(f"  Tuple      : {sys.getsizeof(mon_tuple):,} octets")
    print(f"  Set        : {sys.getsizeof(mon_set):,} octets")
    print(f"  Generateur : {sys.getsizeof(mon_generateur):,} octets")

comparer_structures(10000)

# ==========================================
# 3. Liste vs generateur
# ==========================================
print("\n=== Liste vs Generateur ===\n")

def avec_liste(n):
    """Cree une liste complete."""
    return [x**2 for x in range(n)]

def avec_generateur(n):
    """Cree un generateur."""
    return (x**2 for x in range(n))

n = 1000000

ma_liste = avec_liste(n)
mon_gen = avec_generateur(n)

taille_liste = sys.getsizeof(ma_liste)
taille_gen = sys.getsizeof(mon_gen)

print(f"  Liste      : {taille_liste:,} octets")
print(f"  Generateur : {taille_gen:,} octets")
print(f"  Le generateur utilise {taille_liste/taille_gen:.0f}x moins de memoire !")

# ==========================================
# 4. tracemalloc - profiler les allocations (bibliotheque standard)
# ==========================================
print("\n=== tracemalloc (allocations memoire) ===\n")

tracemalloc.start()  # Demarrer le suivi des allocations

donnees = [i ** 2 for i in range(100000)]
mapping = {i: str(i) for i in range(100000)}

# Photographier l'etat de la memoire et trier par ligne de code
snapshot = tracemalloc.take_snapshot()
top = snapshot.statistics('lineno')
print("Top 2 des allocations :")
for stat in top[:2]:
    print(f"  {stat}")

actuel, pic = tracemalloc.get_traced_memory()
print(f"Memoire actuelle : {actuel / 1024:.1f} Ko ; pic : {pic / 1024:.1f} Ko")
tracemalloc.stop()

# ==========================================
# 5. memory_profiler - profiling ligne par ligne (outil tiers)
# ==========================================
print("\n=== memory_profiler (optionnel, tiers) ===\n")

# memory_profiler (pip install memory_profiler) mesure la memoire LIGNE PAR
# LIGNE. C'est un outil tiers ; la bibliotheque standard offre tracemalloc
# (section 4 ci-dessus). On le charge donc de maniere optionnelle.
try:
    from memory_profiler import profile

    @profile
    def fonction_gourmande():
        liste1 = [i for i in range(1000000)]
        liste2 = [i ** 2 for i in range(1000000)]
        return sum(liste1) + sum(liste2)

    fonction_gourmande()  # @profile imprime un rapport memoire ligne par ligne
except ImportError:
    print("  memory_profiler n'est pas installe (pip install memory_profiler).")
    print("  La bibliotheque standard fournit tracemalloc, montre ci-dessus.")
