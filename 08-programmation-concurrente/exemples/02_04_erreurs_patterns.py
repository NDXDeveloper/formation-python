# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Gestion des erreurs en asynchrone, return_exceptions,
#                 try/except dans les coroutines, nommage des tâches
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio

# ==========================================
# 1. gather avec return_exceptions=True
# ==========================================
print("=== gather avec return_exceptions ===")

async def operation_risquee(numero):
    """Opération qui peut échouer"""
    await asyncio.sleep(0.1)
    if numero == 3:
        raise ValueError(f"Erreur avec le numéro {numero}")
    return f"Succès {numero}"

async def main_exceptions():
    taches = [operation_risquee(i) for i in range(1, 6)]
    resultats = await asyncio.gather(*taches, return_exceptions=True)

    for i, resultat in enumerate(resultats, 1):
        if isinstance(resultat, Exception):
            print(f"  Tâche {i}: Erreur - {resultat}")
        else:
            print(f"  Tâche {i}: {resultat}")

asyncio.run(main_exceptions())

# ==========================================
# 2. Try/except dans les coroutines
# ==========================================
print("\n=== Try/except dans les coroutines ===")

async def tache_avec_gestion_erreur(numero):
    """Gère ses propres erreurs"""
    try:
        await asyncio.sleep(0.05)
        if numero % 2 == 0:
            raise ValueError(f"Nombre pair non autorisé: {numero}")
        return f"Traitement réussi pour {numero}"
    except ValueError as e:
        print(f"  Erreur gérée: {e}")
        return f"Erreur traitée pour {numero}"

async def main_try_except():
    taches = [tache_avec_gestion_erreur(i) for i in range(1, 6)]
    resultats = await asyncio.gather(*taches)

    print("\nRésultats finaux:")
    for resultat in resultats:
        print(f"  - {resultat}")

asyncio.run(main_try_except())

# ==========================================
# 3. Nommer les tâches pour le débogage
# ==========================================
print("\n=== Nommer les tâches ===")

async def ma_tache(numero):
    await asyncio.sleep(0.1)
    return numero

async def main_nommage():
    taches = [
        asyncio.create_task(ma_tache(i), name=f"tache-{i}")
        for i in range(5)
    ]

    for tache in taches:
        print(f"  Nom de la tâche: {tache.get_name()}")

    resultats = await asyncio.gather(*taches)
    print(f"  Résultats: {resultats}")

asyncio.run(main_nommage())
