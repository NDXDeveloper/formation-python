# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Annulation de taches (cancel / CancelledError) et delegation
#                 de code bloquant a un thread (asyncio.to_thread)
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import time

# ==========================================
# 1. Annulation : cancel() et CancelledError
# ==========================================

async def tache_longue():
    """Tache qui peut etre annulee ; elle nettoie puis relance l'annulation."""
    try:
        print("  Tache : demarrage")
        await asyncio.sleep(10)
        print("  Tache : terminee")  # jamais atteint si annulee
    except asyncio.CancelledError:
        print("  Tache : annulation recue, nettoyage...")
        raise  # IMPORTANT : on relance pour confirmer l'annulation

async def demo_annulation():
    print("=== Annulation (cancel / CancelledError) ===")
    tache = asyncio.create_task(tache_longue())
    await asyncio.sleep(0.2)        # on la laisse demarrer
    tache.cancel()                  # on demande l'annulation
    try:
        await tache
    except asyncio.CancelledError:
        print("  Main : la tache a bien ete annulee")

# ==========================================
# 2. to_thread : executer du code bloquant sans geler l'event loop
# ==========================================

def fonction_bloquante():
    """Code synchrone qui prend du temps (lib sans equivalent async, etc.)"""
    time.sleep(0.3)
    return "resultat (calcule dans un thread separe)"

async def demo_to_thread():
    print("\n=== asyncio.to_thread (code bloquant) ===")
    resultat = await asyncio.to_thread(fonction_bloquante)
    print(f"  {resultat}")

async def main():
    await demo_annulation()
    await demo_to_thread()

asyncio.run(main())
