# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : Semaphore avec threading - limiter les accès
#                 simultanés, pool de connexions
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import threading
import time

# ==========================================
# 1. Semaphore basique
# ==========================================
print("=== Semaphore (max 3 simultanés) ===")

semaphore = threading.Semaphore(3)

def acceder_ressource(thread_id):
    """Accède à une ressource limitée"""
    with semaphore:
        print(f"  [Thread {thread_id}] Accès obtenu")
        time.sleep(0.2)
        print(f"  [Thread {thread_id}] Libère l'accès")

threads = [threading.Thread(target=acceder_ressource, args=(i,)) for i in range(8)]

debut = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
duree = time.time() - debut

print(f"Tous les threads ont terminé en {duree:.2f}s")
print(f"  (8 threads, max 3 en parallèle, ~{0.2 * (8/3):.2f}s minimum)")

# ==========================================
# 2. Pool de connexions
# ==========================================
print("\n=== Pool de connexions (max 3) ===")

class PoolConnexions:
    """Gère un pool limité de connexions"""

    def __init__(self, max_connexions):
        self.semaphore = threading.Semaphore(max_connexions)
        self.connexions_actives = 0
        self.verrou_compteur = threading.Lock()

    def executer_requete(self, requete, thread_id):
        with self.semaphore:
            with self.verrou_compteur:
                self.connexions_actives += 1
                actives = self.connexions_actives

            print(f"  [Thread {thread_id}] Connexion ({actives} actives) - {requete}")
            time.sleep(0.2)

            with self.verrou_compteur:
                self.connexions_actives -= 1

pool = PoolConnexions(max_connexions=3)

def worker(thread_id):
    pool.executer_requete(f"SELECT * FROM table WHERE id={thread_id}", thread_id)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(6)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Toutes les requêtes sont terminées")
