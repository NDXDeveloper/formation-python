# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Exemple complet - Téléchargeur parallèle avec threading,
#                 limitation du nombre de threads, résultats avec Lock
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

import threading
import time

class TelechargeParallele:
    """Gestionnaire de téléchargements parallèles"""

    def __init__(self, max_threads: int = 5):
        self.max_threads = max_threads
        self.resultats: list[dict] = []
        self.lock = threading.Lock()

    def telecharger_fichier(self, url: str):
        """Simule le téléchargement d'un fichier"""
        print(f"  [Début] Téléchargement de {url}")

        # Simulation du téléchargement (réduit pour le test)
        duree = 0.3
        time.sleep(duree)

        # Sauvegarder le résultat de manière sécurisée
        with self.lock:
            self.resultats.append({
                'url': url,
                'statut': 'succès',
                'duree': duree
            })

        print(f"  [Terminé] {url}")

    def telecharger_liste(self, urls: list[str]):
        """Télécharge une liste d'URLs en parallèle"""
        threads = []

        print(f"Démarrage de {len(urls)} téléchargements...")
        debut = time.time()

        # Créer et démarrer les threads
        for url in urls:
            thread = threading.Thread(target=self.telecharger_fichier, args=(url,))
            threads.append(thread)
            thread.start()

            # Limiter le nombre de threads simultanés
            if len(threads) >= self.max_threads:
                threads[0].join()
                threads.pop(0)

        # Attendre tous les threads restants
        for thread in threads:
            thread.join()

        duree_totale = time.time() - debut
        print(f"\nTous les téléchargements terminés en {duree_totale:.2f}s")
        return self.resultats


if __name__ == '__main__':
    print("=== Téléchargeur parallèle ===\n")

    urls = [
        "http://example.com/fichier1.pdf",
        "http://example.com/fichier2.pdf",
        "http://example.com/fichier3.pdf",
        "http://example.com/fichier4.pdf",
        "http://example.com/fichier5.pdf",
    ]

    telechargeur = TelechargeParallele(max_threads=3)
    resultats = telechargeur.telecharger_liste(urls)

    print(f"\nRésumé: {len(resultats)} fichiers téléchargés")
    for r in resultats:
        print(f"  {r['url']} - {r['statut']} ({r['duree']}s)")
