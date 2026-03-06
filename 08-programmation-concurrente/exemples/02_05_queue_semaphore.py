# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Patterns courants - Queue asynchrone (producteur-
#                 consommateur), Semaphore pour limiter la concurrence
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import random

# ==========================================
# 1. Queue asynchrone (Producer-Consumer)
# ==========================================
print("=== Queue asynchrone (Producer-Consumer) ===")

random.seed(42)

async def producteur(queue, nom, nb_items):
    """Produit des items dans la queue"""
    for i in range(nb_items):
        item = f"{nom}-item-{i}"
        await asyncio.sleep(random.uniform(0.05, 0.15))
        await queue.put(item)
        print(f"  Produit: {item}")

async def consommateur(queue, nom):
    """Consomme des items de la queue"""
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"  {nom} consomme: {item}")
        await asyncio.sleep(random.uniform(0.03, 0.08))
        queue.task_done()

async def main_queue():
    queue = asyncio.Queue(maxsize=5)

    producteurs = [
        asyncio.create_task(producteur(queue, f"Prod-{i}", 3))
        for i in range(2)
    ]

    consommateurs = [
        asyncio.create_task(consommateur(queue, f"Cons-{i}"))
        for i in range(3)
    ]

    await asyncio.gather(*producteurs)
    await queue.join()

    for _ in consommateurs:
        await queue.put(None)

    await asyncio.gather(*consommateurs)
    print("\nTraitement terminé")

asyncio.run(main_queue())

# ==========================================
# 2. Semaphore - Limiter la concurrence
# ==========================================
print("\n=== Semaphore - Limiter la concurrence ===")

async def tache_longue(numero, semaphore):
    """Tâche qui utilise un sémaphore pour limiter la concurrence"""
    async with semaphore:
        print(f"  Tâche {numero} démarre")
        await asyncio.sleep(0.2)
        print(f"  Tâche {numero} termine")
        return numero

async def main_semaphore():
    # Sémaphore qui permet max 3 tâches en parallèle
    semaphore = asyncio.Semaphore(3)

    # Créer 8 tâches
    taches = [tache_longue(i, semaphore) for i in range(1, 9)]

    import time
    debut = time.time()
    resultats = await asyncio.gather(*taches)
    duree = time.time() - debut

    print(f"\n  Toutes les tâches terminées: {resultats}")
    print(f"  Durée: {duree:.2f}s (8 tâches, max 3 en parallèle)")
    print(f"  (sans semaphore: ~0.20s, avec: ~{0.2 * (8 / 3):.2f}s)")

asyncio.run(main_semaphore())
