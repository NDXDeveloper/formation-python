# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Concurrence structuree avec asyncio.TaskGroup et delai global
#                 avec asyncio.timeout (Python 3.11+)
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import sys

async def telecharger(nom, duree):
    """Simule un telechargement"""
    await asyncio.sleep(duree)
    return nom

async def operation_longue():
    """Operation qui prend du temps"""
    await asyncio.sleep(5)
    return "termine"

async def demo_taskgroup():
    """TaskGroup : toutes les taches du bloc sont terminees a la sortie ;
    si l'une echoue, les autres sont annulees automatiquement."""
    print("=== asyncio.TaskGroup (3.11+) ===")
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(telecharger("video", 0.2))
        t2 = tg.create_task(telecharger("image", 0.1))
        t3 = tg.create_task(telecharger("document", 0.15))
    print(f"  Tous termines : {t1.result()}, {t2.result()}, {t3.result()}")

async def demo_timeout():
    """asyncio.timeout : impose un delai a tout un bloc (plusieurs await)."""
    print("\n=== asyncio.timeout (3.11+) ===")
    try:
        async with asyncio.timeout(0.5):
            await operation_longue()
    except TimeoutError:
        print("  Timeout ! Le bloc a ete interrompu apres 0.5s")

async def main():
    await demo_taskgroup()
    await demo_timeout()

if __name__ == '__main__':
    # TaskGroup et asyncio.timeout sont des constructions d'execution (3.11+) :
    # on peut donc les proteger par un simple test de version.
    if sys.version_info >= (3, 11):
        asyncio.run(main())
    else:
        v = f"{sys.version_info.major}.{sys.version_info.minor}"
        print("asyncio.TaskGroup et asyncio.timeout necessitent Python 3.11+")
        print(f"Version actuelle : {v} -> equivalents 3.10 : asyncio.gather et asyncio.wait_for")
