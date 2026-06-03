# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Mesurer le temps d'execution avec time.perf_counter(), fonction
#                 de chronometrage, gestionnaire de contexte
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import time
from contextlib import contextmanager

# ==========================================
# 1. time.perf_counter() basique
# ==========================================
print("=== time.perf_counter() ===\n")

debut = time.perf_counter()
total = 0
for i in range(1000000):
    total += i
fin = time.perf_counter()
duree = fin - debut
print(f"  Temps d'execution : {duree:.4f} secondes")

# ==========================================
# 2. Fonction de chronometrage
# ==========================================
print("\n=== Fonction chronometrer() ===\n")

def chronometrer(fonction, *args, **kwargs):
    """Chronometre l'execution d'une fonction."""
    debut = time.perf_counter()
    resultat = fonction(*args, **kwargs)
    fin = time.perf_counter()
    duree = fin - debut
    return resultat, duree

def calculer_somme(n):
    return sum(range(n))

resultat, temps = chronometrer(calculer_somme, 1000000)
print(f"  Resultat : {resultat}")
print(f"  Temps : {temps:.4f} secondes")

# ==========================================
# 3. Gestionnaire de contexte
# ==========================================
print("\n=== Gestionnaire de contexte ===\n")

@contextmanager
def chronometre(nom="Code"):
    """Gestionnaire de contexte pour chronometrer un bloc de code."""
    print(f"  Debut du chronometrage : {nom}")
    debut = time.perf_counter()
    yield
    fin = time.perf_counter()
    duree = fin - debut
    print(f"  {nom} termine en {duree:.4f} secondes")

with chronometre("Calcul de la somme"):
    total = sum(range(1000000))

print()

with chronometre("Creation d'une liste"):
    ma_liste = [i**2 for i in range(100000)]
