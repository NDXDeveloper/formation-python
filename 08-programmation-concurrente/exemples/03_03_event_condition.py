# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : Event (signaler un événement), Condition (producteur/
#                 consommateur avec buffer), Event asyncio
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import threading
import asyncio
import time
import random

random.seed(42)

# ==========================================
# 1. Event - Signaler un événement
# ==========================================
print("=== Event (threading) ===")

event = threading.Event()

def attendre_signal(thread_id):
    print(f"  [Thread {thread_id}] En attente du signal...")
    event.wait()
    print(f"  [Thread {thread_id}] Signal reçu! Démarrage du travail")

def envoyer_signal():
    print("  [Contrôleur] Préparation...")
    time.sleep(0.3)
    print("  [Contrôleur] Envoi du signal!")
    event.set()

workers = [threading.Thread(target=attendre_signal, args=(i,)) for i in range(3)]
controleur = threading.Thread(target=envoyer_signal)

for w in workers:
    w.start()
controleur.start()

for w in workers:
    w.join()
controleur.join()

print("Tous les threads ont terminé")

# ==========================================
# 2. Event avec asyncio
# ==========================================
print("\n=== Event (asyncio) ===")

async def attendre_async(event, numero):
    print(f"  [Tâche {numero}] En attente...")
    await event.wait()
    print(f"  [Tâche {numero}] Événement reçu!")

async def declencher_async(event):
    await asyncio.sleep(0.2)
    print("  Déclenchement de l'événement!")
    event.set()

async def main_event():
    event = asyncio.Event()
    taches = [attendre_async(event, i) for i in range(3)]
    taches.append(declencher_async(event))
    await asyncio.gather(*taches)

asyncio.run(main_event())

# ==========================================
# 3. Condition - Producteur/Consommateur
# ==========================================
print("\n=== Condition (Producteur/Consommateur) ===")

class BufferPartage:
    """Buffer partagé avec producteur/consommateur"""

    def __init__(self, taille_max=3):
        self.buffer = []
        self.taille_max = taille_max
        self.condition = threading.Condition()

    def produire(self, item):
        with self.condition:
            while len(self.buffer) >= self.taille_max:
                print(f"  Buffer plein, producteur attend...")
                self.condition.wait()

            self.buffer.append(item)
            print(f"  Produit: {item} (buffer: {len(self.buffer)}/{self.taille_max})")
            self.condition.notify()

    def consommer(self):
        with self.condition:
            while len(self.buffer) == 0:
                print(f"  Buffer vide, consommateur attend...")
                self.condition.wait()

            item = self.buffer.pop(0)
            print(f"  Consommé: {item} (buffer: {len(self.buffer)}/{self.taille_max})")
            self.condition.notify()
            return item

def producteur(buffer, nombre_items):
    for i in range(nombre_items):
        time.sleep(random.uniform(0.05, 0.1))
        buffer.produire(f"Item-{i}")

def consommateur(buffer, nombre_items):
    for _ in range(nombre_items):
        time.sleep(random.uniform(0.08, 0.15))
        buffer.consommer()

buffer = BufferPartage(taille_max=3)

# 1 producteur produit 6 items, 1 consommateur consomme 6 items
prod = threading.Thread(target=producteur, args=(buffer, 6))
cons = threading.Thread(target=consommateur, args=(buffer, 6))

prod.start()
cons.start()
prod.join()
cons.join()

print("Production/consommation terminée")
