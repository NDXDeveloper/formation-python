# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Concepts fondamentaux - coroutines, await, event loop,
#                 asyncio.run(), premier programme asynchrone
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio

# ==========================================
# 1. Coroutine vs fonction normale
# ==========================================
print("=== Coroutine vs fonction normale ===")

def fonction_normale():
    return "Bonjour"

async def fonction_asynchrone():
    return "Bonjour asynchrone"

print(f"Fonction normale: {fonction_normale()}")
# Pour exécuter une coroutine, il faut asyncio.run() ou await
print(f"Coroutine: {asyncio.run(fonction_asynchrone())}")

# ==========================================
# 2. Hello World asynchrone
# ==========================================
print("\n=== Hello World asynchrone ===")

async def dire_bonjour(nom, delai):
    """Fonction asynchrone simple"""
    print(f"  Bonjour {nom}! (attente de {delai}s)")
    await asyncio.sleep(delai)
    print(f"  Au revoir {nom}!")

asyncio.run(dire_bonjour("Alice", 0.2))

# ==========================================
# 3. Plusieurs tâches en parallèle (create_task)
# ==========================================
print("\n=== Plusieurs tâches en parallèle (create_task) ===")

import time

async def faire_cafe(nom):
    """Simule la préparation d'un café"""
    print(f"  {nom}: Début préparation café")
    await asyncio.sleep(0.3)
    print(f"  {nom}: Café prêt!")
    return f"Café pour {nom}"

async def main_cafe():
    debut = time.time()

    tache1 = asyncio.create_task(faire_cafe("Alice"))
    tache2 = asyncio.create_task(faire_cafe("Bob"))
    tache3 = asyncio.create_task(faire_cafe("Charlie"))

    resultat1 = await tache1
    resultat2 = await tache2
    resultat3 = await tache3

    duree = time.time() - debut
    print(f"\n  Tous les cafés prêts en {duree:.2f}s")
    print(f"  Résultats: {resultat1}, {resultat2}, {resultat3}")
    print(f"  (séquentiel aurait pris ~{0.3 * 3:.2f}s)")

asyncio.run(main_cafe())
