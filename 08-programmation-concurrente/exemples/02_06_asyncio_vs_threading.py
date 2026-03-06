# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Comparaison asyncio vs threading - performances I/O,
#                 avantages de chaque approche
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import threading
import time

# === VERSION THREADING ===
def operation_io_thread(numero):
    """Simulation I/O avec threading"""
    time.sleep(0.1)
    return numero * 2

def executer_avec_threads(nombre):
    """Exécute avec threads"""
    debut = time.time()
    threads = []
    resultats = [None] * nombre

    def wrapper(i):
        resultats[i] = operation_io_thread(i)

    for i in range(nombre):
        thread = threading.Thread(target=wrapper, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    duree = time.time() - debut
    print(f"  Threading: {duree:.2f}s pour {nombre} opérations")
    return resultats

# === VERSION ASYNCIO ===
async def operation_io_async(numero):
    """Simulation I/O avec asyncio"""
    await asyncio.sleep(0.1)
    return numero * 2

async def executer_avec_asyncio(nombre):
    """Exécute avec asyncio"""
    debut = time.time()

    taches = [operation_io_async(i) for i in range(nombre)]
    resultats = await asyncio.gather(*taches)

    duree = time.time() - debut
    print(f"  Asyncio:   {duree:.2f}s pour {nombre} opérations")
    return resultats

# === COMPARAISON ===
async def main():
    """Compare les deux approches"""
    nombre_operations = 50

    print(f"=== Comparaison avec {nombre_operations} opérations I/O ===")

    # Threading
    r_thread = executer_avec_threads(nombre_operations)

    # Asyncio
    r_async = await executer_avec_asyncio(nombre_operations)

    # Vérifier que les résultats sont identiques
    print(f"\n  Résultats identiques: {r_thread == list(r_async)}")
    print(f"\n  Avantages d'asyncio :")
    print(f"  - Moins de mémoire (pas de stack par tâche)")
    print(f"  - Plus scalable (milliers de connexions)")
    print(f"  - Code plus lisible avec async/await")

asyncio.run(main())
