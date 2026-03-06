# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Communication entre processus avec Queue
#                 (producteur/consommateur)
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

import multiprocessing
import time

def producteur(queue, nombre_items):
    """Produit des données et les met dans la queue"""
    for i in range(nombre_items):
        item = f"Item-{i}"
        queue.put(item)
        print(f"  Produit: {item}")
        time.sleep(0.1)
    queue.put(None)  # Signal de fin

def consommateur(queue):
    """Consomme les données de la queue"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"  Consommé: {item}")
        time.sleep(0.2)

if __name__ == '__main__':
    print("=== Communication avec Queue ===")

    # Créer une queue partagée
    queue = multiprocessing.Queue()

    # Créer les processus
    proc_producteur = multiprocessing.Process(target=producteur, args=(queue, 5))
    proc_consommateur = multiprocessing.Process(target=consommateur, args=(queue,))

    # Démarrer les processus
    proc_producteur.start()
    proc_consommateur.start()

    # Attendre la fin
    proc_producteur.join()
    proc_consommateur.join()

    print("Communication terminée")
