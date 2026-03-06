# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : Barrier (barrière) pour synchroniser plusieurs threads,
#                 simulation parallèle en phases
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import threading
import time
import random

random.seed(42)

# ==========================================
# 1. Barrier basique
# ==========================================
print("=== Barrier (synchronisation de groupe) ===")

barrier = threading.Barrier(4)

def travailleur(thread_id):
    # Phase 1: Préparation (durée variable)
    duree = random.uniform(0.1, 0.3)
    print(f"  [Thread {thread_id}] Préparation ({duree:.1f}s)...")
    time.sleep(duree)
    print(f"  [Thread {thread_id}] Prêt, attente des autres...")

    # Attendre que tous les threads soient prêts
    barrier.wait()

    # Phase 2: Exécution synchrone
    print(f"  [Thread {thread_id}] Démarrage synchronisé!")

threads = [threading.Thread(target=travailleur, args=(i,)) for i in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Tous les threads ont terminé de manière synchronisée")

# ==========================================
# 2. Simulation parallèle en phases
# ==========================================
print("\n=== Simulation parallèle en phases ===")

class SimulationParallele:
    """Simule un système avec plusieurs composants synchronisés"""

    def __init__(self, nombre_composants):
        self.barrier = threading.Barrier(nombre_composants)
        self.iteration = 0
        self.lock = threading.Lock()

    def composant(self, nom, nombre_iterations):
        for i in range(nombre_iterations):
            # Calculer l'état du composant
            print(f"  [{nom}] Calcul itération {i+1}...")
            time.sleep(0.1)

            # Attendre que tous les composants finissent l'itération
            index = self.barrier.wait()

            # Un seul thread (le dernier) affiche le résumé
            if index == 0:
                with self.lock:
                    self.iteration += 1
                    print(f"  --- Itération {self.iteration} terminée ---")

sim = SimulationParallele(3)

threads = [
    threading.Thread(target=sim.composant, args=(f"Comp-{i}", 3))
    for i in range(3)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Simulation terminée")
