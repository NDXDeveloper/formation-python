# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Profiling memoire - sys.getsizeof, comparaison de
#                 structures (liste, tuple, set, generateur), generateurs
#                 vs listes pour economiser la memoire
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import sys

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
