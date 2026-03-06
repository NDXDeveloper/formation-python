# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Producer-Consumer avec threading et asyncio,
#                 file d'attente partagee, production/consommation decouplees
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import threading
import queue
import time
import random
import asyncio

random.seed(42)

# ==========================================
# 1. Producer-Consumer avec Threading
# ==========================================
print("=== Producer-Consumer (Threading) ===\n")

def producteur(q, producteur_id, nombre_items):
    """Produit des items et les met dans la queue"""
    for i in range(nombre_items):
        item = f"P{producteur_id}-Item{i}"
        time.sleep(random.uniform(0.05, 0.15))
        q.put(item)
        print(f"  Producteur {producteur_id}: produit {item} (queue: {q.qsize()})")
    print(f"  Producteur {producteur_id}: termine")

def consommateur(q, consommateur_id):
    """Consomme des items de la queue"""
    while True:
        try:
            item = q.get(timeout=1)
            print(f"  Consommateur {consommateur_id}: traite {item}")
            time.sleep(random.uniform(0.08, 0.2))
            q.task_done()
        except queue.Empty:
            print(f"  Consommateur {consommateur_id}: queue vide, arret")
            break

file_attente = queue.Queue(maxsize=10)

producteurs = [
    threading.Thread(target=producteur, args=(file_attente, i, 5))
    for i in range(2)
]

consommateurs = [
    threading.Thread(target=consommateur, args=(file_attente, i))
    for i in range(3)
]

print("Demarrage du systeme Producer-Consumer\n")
for p in producteurs:
    p.start()
for c in consommateurs:
    c.start()

for p in producteurs:
    p.join()
file_attente.join()

# Attendre que les consommateurs detectent la queue vide
for c in consommateurs:
    c.join()

print("\nTous les items ont ete produits et consommes")

# ==========================================
# 2. Producer-Consumer avec Asyncio
# ==========================================
print("\n=== Producer-Consumer (Asyncio) ===\n")

async def producteur_async(q, producteur_id, nombre_items):
    """Producteur asynchrone"""
    for i in range(nombre_items):
        item = f"P{producteur_id}-Item{i}"
        await asyncio.sleep(random.uniform(0.05, 0.15))
        await q.put(item)
        print(f"  Producteur {producteur_id}: produit {item}")
    print(f"  Producteur {producteur_id}: termine")

async def consommateur_async(q, consommateur_id, nb_producteurs):
    """Consommateur asynchrone"""
    items_traites = 0
    while True:
        try:
            item = await asyncio.wait_for(q.get(), timeout=1.0)
            print(f"  Consommateur {consommateur_id}: traite {item}")
            await asyncio.sleep(random.uniform(0.08, 0.2))
            items_traites += 1
            q.task_done()
        except asyncio.TimeoutError:
            print(f"  Consommateur {consommateur_id}: arret ({items_traites} items)")
            break

async def main():
    """Point d'entree principal"""
    q = asyncio.Queue(maxsize=10)
    nb_producteurs = 2
    producteurs = [producteur_async(q, i, 5) for i in range(nb_producteurs)]
    consommateurs = [consommateur_async(q, i, nb_producteurs) for i in range(3)]
    await asyncio.gather(*producteurs, *consommateurs)
    print("\nPipeline termine")

asyncio.run(main())
