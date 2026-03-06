# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Fan-Out/Fan-In - dispatcher distribue les taches
#                 a plusieurs workers, collecteur rassemble les resultats
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import threading
import queue
import time
import random

random.seed(42)

# ==========================================
# Fan-Out / Fan-In
# ==========================================
print("=== Fan-Out / Fan-In ===\n")

def dispatcher(taches, queues_workers):
    """Fan-Out: Distribue les taches aux workers"""
    print("Dispatcher: Distribution des taches")
    for i, tache in enumerate(taches):
        worker_id = i % len(queues_workers)
        queues_workers[worker_id].put(tache)
        print(f"  -> Tache {tache} -> Worker {worker_id}")
    for q in queues_workers:
        q.put(None)
    print("Dispatcher: Termine")

def worker(worker_id, queue_entree, queue_resultats):
    """Worker qui traite des taches"""
    print(f"Worker {worker_id}: Demarre")
    while True:
        tache = queue_entree.get()
        if tache is None:
            break
        time.sleep(random.uniform(0.1, 0.3))
        resultat = f"Resultat-{tache}-by-W{worker_id}"
        queue_resultats.put(resultat)
        print(f"  Worker {worker_id}: {tache} -> {resultat}")
    print(f"Worker {worker_id}: Termine")

def collecteur(queue_resultats, nombre_taches):
    """Fan-In: Collecte tous les resultats"""
    print("Collecteur: En attente des resultats")
    resultats = []
    for _ in range(nombre_taches):
        resultat = queue_resultats.get()
        resultats.append(resultat)
        print(f"  <- Recu: {resultat}")
    print(f"Collecteur: Termine ({len(resultats)} resultats)")
    return resultats

# Configuration
taches = [f"Tache-{i}" for i in range(12)]
nombre_workers = 4

# Creer les queues
queues_workers = [queue.Queue() for _ in range(nombre_workers)]
queue_resultats = queue.Queue()

# Creer les threads
thread_dispatcher = threading.Thread(
    target=dispatcher,
    args=(taches, queues_workers)
)

threads_workers = [
    threading.Thread(target=worker, args=(i, queues_workers[i], queue_resultats))
    for i in range(nombre_workers)
]

thread_collecteur = threading.Thread(
    target=collecteur,
    args=(queue_resultats, len(taches))
)

# Demarrer
print("Demarrage Fan-Out/Fan-In\n")
debut = time.time()

thread_dispatcher.start()
for t in threads_workers:
    t.start()
thread_collecteur.start()

# Attendre la fin
thread_dispatcher.join()
for t in threads_workers:
    t.join()
thread_collecteur.join()

duree = time.time() - debut
print(f"\nFan-Out/Fan-In complet en {duree:.2f}s")
