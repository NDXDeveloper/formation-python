# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Scatter-Gather - envoi de requetes a plusieurs
#                 services, collecte de toutes les reponses ou premiere reponse
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import asyncio
import random

random.seed(42)

# ==========================================
# Scatter-Gather
# ==========================================

async def interroger_service(nom_service, requete):
    """Interroge un service distant"""
    print(f"  Requete vers {nom_service}")
    latence = random.uniform(0.1, 0.5)
    await asyncio.sleep(latence)
    reponse = {
        'service': nom_service,
        'resultat': f"Donnees de {nom_service}",
        'latence': latence,
        'prix': random.randint(50, 150)
    }
    print(f"  Reponse de {nom_service} ({latence:.2f}s)")
    return reponse

async def scatter_gather_all(requete, services):
    """Scatter-Gather: Attend toutes les reponses"""
    print(f"Scatter: Envoi vers {len(services)} services\n")
    taches = [interroger_service(service, requete) for service in services]
    reponses = await asyncio.gather(*taches)
    print(f"\nGather: {len(reponses)} reponses recues")
    return reponses

async def scatter_gather_first(requete, services):
    """Retourne la premiere reponse"""
    print(f"Scatter: Envoi vers {len(services)} services\n")
    taches = [asyncio.create_task(interroger_service(service, requete))
              for service in services]
    done, pending = await asyncio.wait(taches, return_when=asyncio.FIRST_COMPLETED)
    for tache in pending:
        tache.cancel()
    # Attendre l'annulation des taches pending
    for tache in pending:
        try:
            await tache
        except asyncio.CancelledError:
            pass
    reponse = done.pop().result()
    print(f"\nPremiere reponse: {reponse['service']}")
    return reponse

async def main():
    services = ["ServiceA", "ServiceB", "ServiceC", "ServiceD"]
    requete = "Chercher produit XYZ"

    # Strategie 1: Attendre toutes les reponses
    print("=== Strategie: Toutes les reponses ===\n")
    reponses = await scatter_gather_all(requete, services)
    meilleur = min(reponses, key=lambda r: r['prix'])
    print(f"\nMeilleur prix: {meilleur['prix']}EUR ({meilleur['service']})")

    print("\n" + "=" * 50 + "\n")

    # Strategie 2: Premiere reponse seulement
    print("=== Strategie: Premiere reponse ===\n")
    reponse = await scatter_gather_first(requete, services)
    print(f"Resultat: {reponse['resultat']}")

asyncio.run(main())
