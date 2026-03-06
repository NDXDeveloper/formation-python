# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Worker Pool avec concurrent.futures (ThreadPoolExecutor,
#                 map, as_completed) et asyncio
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import asyncio
import time
import random

random.seed(42)

# ==========================================
# 1. Worker Pool avec concurrent.futures
# ==========================================
print("=== Worker Pool (concurrent.futures) ===\n")

def traiter_tache(tache_id):
    """Traite une tache"""
    print(f"  Worker {threading.current_thread().name}: demarre tache {tache_id}")
    duree = random.uniform(0.1, 0.3)
    time.sleep(duree)
    resultat = f"Resultat-{tache_id}"
    print(f"  Worker {threading.current_thread().name}: termine tache {tache_id}")
    return resultat

with ThreadPoolExecutor(max_workers=3) as executor:
    print("Pool de workers demarre (3 workers)\n")
    futures = [executor.submit(traiter_tache, i) for i in range(10)]
    for future in as_completed(futures):
        resultat = future.result()
        print(f"  Resultat recu: {resultat}")

print("\nToutes les taches sont terminees")

# ==========================================
# 2. Worker Pool avec map()
# ==========================================
print("\n=== Worker Pool avec map() ===\n")

def calculer_carre(nombre):
    """Calcule le carre d'un nombre"""
    time.sleep(0.05)
    return nombre ** 2

nombres = list(range(1, 11))

with ThreadPoolExecutor(max_workers=4) as executor:
    resultats = list(executor.map(calculer_carre, nombres))

print(f"Nombres: {nombres}")
print(f"Carres: {resultats}")

# ==========================================
# 3. Worker Pool avec Asyncio
# ==========================================
print("\n=== Worker Pool (Asyncio) ===\n")

async def worker_async(nom, queue_taches, queue_resultats):
    """Worker asynchrone qui traite des taches"""
    while True:
        try:
            tache = await asyncio.wait_for(queue_taches.get(), timeout=1.0)
            print(f"  {nom}: traite tache {tache}")
            await asyncio.sleep(random.uniform(0.05, 0.15))
            resultat = f"Resultat-{tache}"
            await queue_resultats.put(resultat)
            queue_taches.task_done()
        except asyncio.TimeoutError:
            print(f"  {nom}: aucune tache, arret")
            break

async def main():
    """Gestionnaire de pool"""
    queue_taches = asyncio.Queue()
    queue_resultats = asyncio.Queue()

    for i in range(15):
        await queue_taches.put(f"Tache-{i}")

    workers = [
        asyncio.create_task(worker_async(f"Worker-{i}", queue_taches, queue_resultats))
        for i in range(5)
    ]

    await queue_taches.join()
    await asyncio.gather(*workers)

    print(f"\n{queue_resultats.qsize()} resultats obtenus")

asyncio.run(main())
