# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Threads de base - thread simple, plusieurs threads
#                 simultanés, thread avec classe
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

import threading
import time

# ==========================================
# 1. Premier thread simple
# ==========================================
print("=== Premier thread simple ===")

def afficher_nombres():
    """Fonction qui affiche des nombres"""
    for i in range(5):
        print(f"  Nombre: {i}")
        time.sleep(0.1)

thread = threading.Thread(target=afficher_nombres)
thread.start()
print("Le thread a été lancé!")
thread.join()
print("Le thread est terminé")

# ==========================================
# 2. Plusieurs threads simultanés
# ==========================================
print("\n=== Plusieurs threads simultanés ===")

def telecharger_fichier(nom_fichier):
    """Simule le téléchargement d'un fichier"""
    print(f"  Début du téléchargement de {nom_fichier}")
    time.sleep(0.3)  # Simule le temps de téléchargement
    print(f"  Téléchargement de {nom_fichier} terminé")

fichiers = ["image1.jpg", "image2.jpg", "image3.jpg"]
threads = []

debut = time.time()
for fichier in fichiers:
    thread = threading.Thread(target=telecharger_fichier, args=(fichier,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

duree = time.time() - debut
print(f"Tous les téléchargements sont terminés en {duree:.2f}s")
print(f"  (séquentiel aurait pris ~{0.3 * len(fichiers):.2f}s)")

# ==========================================
# 3. Thread avec classe
# ==========================================
print("\n=== Thread avec classe ===")

class MonThread(threading.Thread):
    def __init__(self, nom, duree):
        super().__init__()
        self.nom = nom
        self.duree = duree

    def run(self):
        """Méthode exécutée quand le thread démarre"""
        print(f"  {self.nom} commence")
        time.sleep(self.duree)
        print(f"  {self.nom} termine")

thread1 = MonThread("Thread-1", 0.2)
thread2 = MonThread("Thread-2", 0.3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Tous les threads sont terminés")

# ==========================================
# 4. Gestion des exceptions dans les threads
# ==========================================
print("\n=== Gestion des exceptions ===")

def fonction_avec_erreur():
    try:
        resultat = 1 / 0
    except Exception as e:
        print(f"  Erreur dans le thread: {e}")

thread = threading.Thread(target=fonction_avec_erreur)
thread.start()
thread.join()
print("Thread avec erreur géré correctement")
