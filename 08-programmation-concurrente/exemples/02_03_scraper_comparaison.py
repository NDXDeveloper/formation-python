# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Scraper web asynchrone - comparaison synchrone vs
#                 asynchrone, gain de performance
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import time

async def fetch_page(url, duree):
    """Simule le téléchargement d'une page web"""
    print(f"  GET {url}")
    await asyncio.sleep(duree)
    print(f"  {url} - 200 OK")
    return f"Contenu de {url}"

async def scraper_synchrone(urls):
    """Version synchrone (une page après l'autre)"""
    print("=== VERSION SYNCHRONE ===")
    debut = time.time()

    resultats = []
    for url, duree in urls:
        resultat = await fetch_page(url, duree)
        resultats.append(resultat)

    duree_totale = time.time() - debut
    print(f"  Temps total: {duree_totale:.2f}s\n")
    return resultats

async def scraper_asynchrone(urls):
    """Version asynchrone (toutes les pages en parallèle)"""
    print("=== VERSION ASYNCHRONE ===")
    debut = time.time()

    taches = [fetch_page(url, duree) for url, duree in urls]
    resultats = await asyncio.gather(*taches)

    duree_totale = time.time() - debut
    print(f"  Temps total: {duree_totale:.2f}s\n")
    return resultats

async def main():
    """Compare les deux approches"""
    urls = [
        ("https://example.com/page1", 0.3),
        ("https://example.com/page2", 0.2),
        ("https://example.com/page3", 0.4),
        ("https://example.com/page4", 0.1),
    ]

    # Version synchrone
    await scraper_synchrone(urls)

    # Version asynchrone
    await scraper_asynchrone(urls)

    total_sync = sum(d for _, d in urls)
    total_async = max(d for _, d in urls)
    print(f"Gain: {total_sync:.2f}s -> {total_async:.2f}s ({total_sync/total_async:.1f}x plus rapide)")

asyncio.run(main())
