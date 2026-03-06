# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : asyncio.gather() pour attendre plusieurs coroutines,
#                 asyncio.wait_for() avec timeout
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import time

# ==========================================
# 1. asyncio.gather()
# ==========================================
print("=== asyncio.gather() ===")

async def telecharger_fichier(nom, taille_mo):
    """Simule le téléchargement d'un fichier"""
    duree = taille_mo * 0.05  # 0.05s par Mo (accéléré)
    print(f"  Début téléchargement: {nom} ({taille_mo} Mo)")
    await asyncio.sleep(duree)
    print(f"  Téléchargé: {nom}")
    return f"{nom} ({taille_mo} Mo)"

async def main_gather():
    fichiers = [
        ("video.mp4", 10),
        ("image.jpg", 2),
        ("document.pdf", 5),
        ("musique.mp3", 3)
    ]

    debut = time.time()

    resultats = await asyncio.gather(
        *[telecharger_fichier(nom, taille) for nom, taille in fichiers]
    )

    duree = time.time() - debut
    print(f"\n  Tous les fichiers téléchargés: {len(resultats)} en {duree:.2f}s")
    for resultat in resultats:
        print(f"    - {resultat}")

asyncio.run(main_gather())

# ==========================================
# 2. asyncio.wait_for() - Timeout
# ==========================================
print("\n=== asyncio.wait_for() - Timeout ===")

async def operation_longue():
    """Opération qui prend du temps"""
    print("  Début de l'opération longue...")
    await asyncio.sleep(5)  # Prend 5 secondes
    return "Opération terminée"

async def main_timeout():
    try:
        resultat = await asyncio.wait_for(operation_longue(), timeout=0.5)
        print(f"  Résultat: {resultat}")
    except asyncio.TimeoutError:
        print("  Timeout! L'opération a pris trop de temps")

asyncio.run(main_timeout())
