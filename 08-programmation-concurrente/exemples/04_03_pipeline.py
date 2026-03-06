# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Pipeline - 4 etapes de traitement en chaine
#                 (collecte, nettoyage, traitement, sauvegarde) avec queues
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

import threading
import queue
import time
import random

random.seed(42)

# ==========================================
# Pipeline en 4 etapes
# ==========================================
print("=== Pipeline (4 etapes) ===\n")

def etape_1_collecte(queue_sortie, nombre_items):
    """Etape 1: Collecte des donnees"""
    print("Etape 1: Collecte des donnees")
    for i in range(nombre_items):
        donnee = f"Data-{i}"
        time.sleep(random.uniform(0.05, 0.1))
        queue_sortie.put(donnee)
        print(f"  -> Collecte: {donnee}")
    queue_sortie.put(None)  # Signal de fin
    print("Etape 1: Terminee")

def etape_2_nettoyage(queue_entree, queue_sortie):
    """Etape 2: Nettoyage des donnees"""
    print("Etape 2: Nettoyage des donnees")
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            queue_sortie.put(None)
            break
        time.sleep(random.uniform(0.05, 0.1))
        donnee_nettoyee = f"Clean-{donnee}"
        queue_sortie.put(donnee_nettoyee)
        print(f"  -> Nettoye: {donnee_nettoyee}")
    print("Etape 2: Terminee")

def etape_3_traitement(queue_entree, queue_sortie):
    """Etape 3: Traitement des donnees"""
    print("Etape 3: Traitement des donnees")
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            queue_sortie.put(None)
            break
        time.sleep(random.uniform(0.08, 0.15))
        donnee_traitee = f"Processed-{donnee}"
        queue_sortie.put(donnee_traitee)
        print(f"  -> Traite: {donnee_traitee}")
    print("Etape 3: Terminee")

def etape_4_sauvegarde(queue_entree):
    """Etape 4: Sauvegarde des resultats"""
    print("Etape 4: Sauvegarde des resultats")
    resultats = []
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            break
        time.sleep(random.uniform(0.03, 0.08))
        resultats.append(donnee)
        print(f"  -> Sauvegarde: {donnee}")
    print(f"Etape 4: Terminee ({len(resultats)} items)")
    return resultats

# Creer les queues entre les etapes
q1_to_2 = queue.Queue(maxsize=5)
q2_to_3 = queue.Queue(maxsize=5)
q3_to_4 = queue.Queue(maxsize=5)

# Creer les threads pour chaque etape
threads = [
    threading.Thread(target=etape_1_collecte, args=(q1_to_2, 10)),
    threading.Thread(target=etape_2_nettoyage, args=(q1_to_2, q2_to_3)),
    threading.Thread(target=etape_3_traitement, args=(q2_to_3, q3_to_4)),
    threading.Thread(target=etape_4_sauvegarde, args=(q3_to_4,))
]

# Demarrer le pipeline
print("Demarrage du pipeline\n")
debut = time.time()

for t in threads:
    t.start()
for t in threads:
    t.join()

duree = time.time() - debut
print(f"\nPipeline complet en {duree:.2f}s")
