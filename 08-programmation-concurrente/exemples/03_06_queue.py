# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : queue.Queue - file thread-safe prete a l'emploi, et ses
#                 variantes LifoQueue (pile) et PriorityQueue (par priorite)
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import queue
import threading

def producteur(file, nb_items):
    """Produit des items dans la file (thread-safe, sans verrou manuel)."""
    for i in range(nb_items):
        file.put(f"tache-{i}")
    file.put(None)  # sentinelle de fin

def consommateur(file, resultats):
    """Consomme les items jusqu'a la sentinelle."""
    while True:
        item = file.get()
        if item is None:
            break
        resultats.append(item)
        file.task_done()

# ==========================================
# 1. queue.Queue : producteur-consommateur
# ==========================================
print("=== queue.Queue (producteur-consommateur) ===")

file = queue.Queue(maxsize=10)
resultats = []

t_prod = threading.Thread(target=producteur, args=(file, 5))
t_cons = threading.Thread(target=consommateur, args=(file, resultats))
t_prod.start()
t_cons.start()
t_prod.join()
t_cons.join()

print(f"{len(resultats)} items traites : {resultats}")

# ==========================================
# 2. Variantes : LifoQueue et PriorityQueue
# ==========================================
print("\n=== Variantes ===")

# LifoQueue : pile (dernier entre, premier sorti)
pile = queue.LifoQueue()
for x in [1, 2, 3]:
    pile.put(x)
print(f"LifoQueue (LIFO) : {pile.get()}, {pile.get()}, {pile.get()}")

# PriorityQueue : tri par priorite (plus petit en premier)
prio = queue.PriorityQueue()
for priorite, nom in [(3, "basse"), (1, "haute"), (2, "moyenne")]:
    prio.put((priorite, nom))
print(f"PriorityQueue : {prio.get()[1]}, {prio.get()[1]}, {prio.get()[1]} (par priorite)")
