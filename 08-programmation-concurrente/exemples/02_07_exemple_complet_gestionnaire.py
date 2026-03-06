# ============================================================================
#   Section 8.2 : Programmation Asynchrone avec Asyncio
#   Description : Exemple complet - Gestionnaire de téléchargements
#                 asynchrones avec semaphore, timeout, statistiques
#   Fichier source : 02-programmation-asynchrone-asyncio.md
# ============================================================================

import asyncio
import time

class GestionnaireTelechargement:
    """Gestionnaire de téléchargements asynchrones avec contrôle"""

    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.statistiques = {
            'reussis': 0,
            'echoues': 0,
            'total': 0
        }

    async def telecharger_fichier(self, url: str, timeout: float = 10.0) -> dict:
        """Télécharge un fichier avec gestion d'erreurs et timeout"""
        async with self.semaphore:
            self.statistiques['total'] += 1
            debut = time.time()

            try:
                print(f"  Début: {url}")

                await asyncio.wait_for(
                    self._simuler_telechargement(url),
                    timeout=timeout
                )

                duree = time.time() - debut
                self.statistiques['reussis'] += 1

                print(f"  Succès: {url} ({duree:.2f}s)")
                return {
                    'url': url,
                    'statut': 'succès',
                    'duree': duree
                }

            except asyncio.TimeoutError:
                self.statistiques['echoues'] += 1
                print(f"  Timeout: {url}")
                return {
                    'url': url,
                    'statut': 'timeout',
                    'erreur': 'Timeout dépassé'
                }

            except Exception as e:
                self.statistiques['echoues'] += 1
                print(f"  Erreur: {url} - {e}")
                return {
                    'url': url,
                    'statut': 'erreur',
                    'erreur': str(e)
                }

    async def _simuler_telechargement(self, url: str):
        """Simule le téléchargement"""
        # Durée variable basée sur l'URL (réduite pour le test)
        duree = (len(url) % 5 + 1) * 0.1
        await asyncio.sleep(duree)

    async def telecharger_liste(self, urls: list[str]) -> list[dict]:
        """Télécharge une liste d'URLs"""
        print(f"Lancement de {len(urls)} téléchargements")
        print(f"Concurrence max: {self.max_concurrent}")
        print("-" * 50)

        debut_total = time.time()

        taches = [self.telecharger_fichier(url) for url in urls]
        resultats = await asyncio.gather(*taches, return_exceptions=True)

        duree_totale = time.time() - debut_total

        print("-" * 50)
        print(f"\nStatistiques:")
        print(f"  Total: {self.statistiques['total']}")
        print(f"  Réussis: {self.statistiques['reussis']}")
        print(f"  Échoués: {self.statistiques['echoues']}")
        print(f"  Durée totale: {duree_totale:.2f}s")
        print(f"  Vitesse: {len(urls)/duree_totale:.2f} téléchargements/s")

        return resultats


async def main():
    """Fonction principale"""
    urls = [
        "https://example.com/fichier1.pdf",
        "https://example.com/fichier2.pdf",
        "https://example.com/fichier3.pdf",
        "https://example.com/fichier4.pdf",
        "https://example.com/fichier5.pdf",
        "https://example.com/fichier6.pdf",
        "https://example.com/fichier7.pdf",
        "https://example.com/fichier8.pdf",
    ]

    gestionnaire = GestionnaireTelechargement(max_concurrent=3)
    resultats = await gestionnaire.telecharger_liste(urls)

    print("\nRésultats détaillés:")
    for resultat in resultats:
        if isinstance(resultat, dict):
            statut = resultat['statut']
            url = resultat['url']
            symbole = "OK" if statut == 'succès' else "FAIL"
            print(f"  [{symbole}] {url}: {statut}")

if __name__ == '__main__':
    asyncio.run(main())
