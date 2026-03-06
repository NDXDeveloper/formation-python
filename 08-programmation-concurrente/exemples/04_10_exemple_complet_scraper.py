# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Exemple complet - Systeme de scraping web combinant
#                 plusieurs patterns (Rate Limiting, Worker Pool, Pipeline,
#                 Fan-Out/Fan-In, Map-Reduce)
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import asyncio
import time
from collections import Counter


class RateLimiter:
    """Rate limiter simple pour l'exemple"""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.time()
            self.calls = [c for c in self.calls if now - c < self.period]

            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                await asyncio.sleep(sleep_time)
                self.calls = []

            self.calls.append(time.time())


class WebScraperSystem:
    """Systeme de scraping combinant plusieurs patterns"""

    def __init__(self, max_concurrent=5, rate_limit=10):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.rate_limiter = RateLimiter(rate_limit, period=1.0)
        self.resultats = []
        self.lock = asyncio.Lock()

    async def fetch_url(self, session, url):
        """
        Fetch une URL avec rate limiting et semaphore
        Pattern: Rate Limiting + Worker Pool
        """
        async with self.semaphore:
            await self.rate_limiter.acquire()

            try:
                print(f"  Telechargement: {url}")
                await asyncio.sleep(0.05)  # Simule le telechargement

                contenu = f"Contenu simule de {url}"
                return {'url': url, 'contenu': contenu, 'status': 'success'}

            except Exception as e:
                return {'url': url, 'erreur': str(e), 'status': 'error'}

    async def extraire_donnees(self, page_data):
        """
        Extrait les donnees d'une page
        Pattern: Pipeline (etape 2)
        """
        await asyncio.sleep(0.02)  # Simule l'extraction

        mots = page_data['contenu'].split()
        return {
            'url': page_data['url'],
            'mots': mots,
            'nb_mots': len(mots)
        }

    async def worker_pipeline(self, session, url):
        """
        Worker complet qui fait fetch + extraction
        Pattern: Pipeline
        """
        # Etape 1: Telecharger
        page_data = await self.fetch_url(session, url)

        if page_data['status'] == 'error':
            return page_data

        # Etape 2: Extraire
        donnees_extraites = await self.extraire_donnees(page_data)

        # Stocker les resultats
        async with self.lock:
            self.resultats.append(donnees_extraites)

        return donnees_extraites

    async def scraper_urls(self, urls: list[str]):
        """
        Scrape plusieurs URLs
        Pattern: Fan-Out/Fan-In + Worker Pool
        """
        print(f"Demarrage du scraping de {len(urls)} URLs")
        print(f"Config: max {self.semaphore._value} concurrent, rate limit {self.rate_limiter.max_calls}/s\n")

        debut = time.time()

        session = None  # En vrai: aiohttp.ClientSession()

        # Fan-Out: Creer toutes les taches
        taches = [self.worker_pipeline(session, url) for url in urls]

        # Fan-In: Collecter tous les resultats
        resultats = await asyncio.gather(*taches, return_exceptions=True)

        duree = time.time() - debut

        # Statistiques
        succes = sum(1 for r in resultats if isinstance(r, dict) and r.get('status') != 'error')
        echecs = len(resultats) - succes

        print(f"\nScraping termine en {duree:.2f}s")
        print(f"Resultats: {succes} succes, {echecs} echecs")

        return resultats

    def analyser_resultats(self):
        """
        Analyse les resultats collectes
        Pattern: Map-Reduce
        """
        print("\nAnalyse des resultats (Map-Reduce):")

        # Map: Extraire tous les mots
        tous_les_mots = []
        for resultat in self.resultats:
            if 'mots' in resultat:
                tous_les_mots.extend(resultat['mots'])

        # Reduce: Compter les occurrences
        compteur = Counter(tous_les_mots)

        print(f"  Total de mots: {len(tous_les_mots)}")
        print(f"  Mots uniques: {len(compteur)}")
        print(f"  Top 5 mots:")
        for mot, count in compteur.most_common(5):
            print(f"    - {mot}: {count} fois")


async def main():
    """Demonstration du systeme complet"""

    urls = [f"https://example.com/page{i}" for i in range(20)]

    scraper = WebScraperSystem(max_concurrent=5, rate_limit=10)

    resultats = await scraper.scraper_urls(urls)

    scraper.analyser_resultats()

if __name__ == '__main__':
    asyncio.run(main())
