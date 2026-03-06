# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : Lock (verrou simple) avec threading et asyncio,
#                 RLock (verrou réentrant), race condition
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import threading
import asyncio
import time

# ==========================================
# 1. Race condition (sans Lock)
# ==========================================
print("=== Race condition (sans Lock) ===")

compteur = 0

def incrementer_sans_lock():
    global compteur
    for _ in range(100000):
        compteur += 1

threads = [threading.Thread(target=incrementer_sans_lock) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Compteur sans lock: {compteur} (attendu: 500000)")
if compteur != 500000:
    print(f"  Race condition! Perdu {500000 - compteur} incréments")
else:
    print("  (Le GIL a protégé cette fois, mais ce n'est pas garanti)")

# ==========================================
# 2. Lock avec threading (correct)
# ==========================================
print("\n=== Lock avec threading ===")

compteur = 0
verrou = threading.Lock()

def incrementer_avec_lock():
    global compteur
    for _ in range(100000):
        with verrou:
            compteur += 1

threads = [threading.Thread(target=incrementer_avec_lock) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Compteur avec lock: {compteur} (attendu: 500000)")
print(f"  Correct: {compteur == 500000}")

# ==========================================
# 3. Lock avec asyncio
# ==========================================
print("\n=== Lock avec asyncio ===")

compteur_async = 0
verrou_async = asyncio.Lock()

async def incrementer_async():
    global compteur_async
    for _ in range(100000):
        async with verrou_async:
            compteur_async += 1

async def main_asyncio_lock():
    taches = [incrementer_async() for _ in range(5)]
    await asyncio.gather(*taches)
    print(f"Compteur avec asyncio.Lock: {compteur_async} (attendu: 500000)")
    print(f"  Correct: {compteur_async == 500000}")

asyncio.run(main_asyncio_lock())

# ==========================================
# 4. RLock (verrou réentrant)
# ==========================================
print("\n=== RLock (verrou réentrant) ===")

class CompteBancaire:
    """Compte bancaire avec méthodes synchronisées"""

    def __init__(self, solde):
        self.solde = solde
        self.verrou = threading.RLock()

    def retirer(self, montant):
        with self.verrou:
            if self.solde >= montant:
                self.solde -= montant
                return True
            return False

    def deposer(self, montant):
        with self.verrou:
            self.solde += montant

    def transferer(self, autre_compte, montant):
        with self.verrou:  # Premier lock
            if self.retirer(montant):  # Appelle retirer qui utilise aussi le lock!
                autre_compte.deposer(montant)
                return True
            return False

compte1 = CompteBancaire(1000)
compte2 = CompteBancaire(500)

# Sans RLock, ceci causerait un deadlock
compte1.transferer(compte2, 200)
print(f"Compte 1: {compte1.solde} EUR (attendu: 800)")
print(f"Compte 2: {compte2.solde} EUR (attendu: 700)")
