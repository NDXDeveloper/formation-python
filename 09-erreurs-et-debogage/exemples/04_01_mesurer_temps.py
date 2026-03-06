# ============================================================================
#   Section 9.4 : Profiling et optimisation
#   Description : Mesurer le temps d'execution avec time.time(), fonction
#                 de chronometrage, gestionnaire de contexte
#   Fichier source : 04-profiling-et-optimisation.md
# ============================================================================

import time
from contextlib import contextmanager

# ==========================================
# 1. time.time() basique
# ==========================================
print("=== time.time() ===\n")

debut = time.time()
total = 0
for i in range(1000000):
    total += i
fin = time.time()
duree = fin - debut
print(f"  Temps d'execution : {duree:.4f} secondes")

# ==========================================
# 2. Fonction de chronometrage
# ==========================================
print("\n=== Fonction chronometrer() ===\n")

def chronometrer(fonction, *args, **kwargs):
    """Chronometre l'execution d'une fonction."""
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
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
    debut = time.time()
    yield
    fin = time.time()
    duree = fin - debut
    print(f"  {nom} termine en {duree:.4f} secondes")

with chronometre("Calcul de la somme"):
    total = sum(range(1000000))

print()

with chronometre("Creation d'une liste"):
    ma_liste = [i**2 for i in range(100000)]
