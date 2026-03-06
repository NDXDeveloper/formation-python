# ============================================================================
#   Section 7.2 : Les modules datetime et time
#   Description : Module time - timestamp, localtime, sleep, perf_counter,
#                 conversion datetime<->timestamp, chronomètre
#   Fichier source : 02-datetime-et-time.md
# ============================================================================

import time
from datetime import datetime

# --- Timestamp ---
print("=== Timestamp ===")

timestamp = time.time()
print(f"Timestamp actuel : {timestamp:.2f}")

# Convertir en structure locale
temps_local = time.localtime(timestamp)
print(f"Structure locale : {temps_local}")
print(f"Formaté : {time.strftime('%Y-%m-%d %H:%M:%S', temps_local)}")

# --- Conversion datetime <-> timestamp ---
print("\n=== Conversion datetime <-> timestamp ===")

maintenant = datetime.now()
ts = maintenant.timestamp()
print(f"datetime -> timestamp : {ts:.2f}")

# Timestamp fixe pour résultat prévisible
timestamp_fixe = 1698415845
date_depuis_ts = datetime.fromtimestamp(timestamp_fixe)
print(f"timestamp 1698415845 -> {date_depuis_ts}")

# --- sleep ---
print("\n=== time.sleep() ===")

print("Début")
debut = time.perf_counter()
time.sleep(0.5)  # Pause de 0.5 seconde (court pour le test)
fin = time.perf_counter()
print(f"Après sleep(0.5) : {fin - debut:.2f} secondes écoulées")

# --- Mesurer le temps d'exécution ---
print("\n=== Mesurer le temps d'exécution ===")

# Méthode 1 : time.time()
debut = time.time()
total = 0
for i in range(1_000_000):
    total += i
fin = time.time()
print(f"time.time()        : {fin - debut:.4f} secondes (somme={total})")

# Méthode 2 : time.perf_counter() (plus précis)
debut = time.perf_counter()
resultat = sum(range(1_000_000))
fin = time.perf_counter()
print(f"time.perf_counter(): {fin - debut:.6f} secondes (somme={resultat})")

# --- Chronomètre (classe) ---
print("\n=== Chronomètre ===")

class Chronometre:
    """Classe simple pour chronométrer des opérations"""

    def __init__(self):
        self.debut = None
        self.fin = None

    def demarrer(self):
        self.debut = time.perf_counter()
        print("Chronometre demarre")

    def arreter(self):
        if self.debut is None:
            print("Le chronometre n'a pas ete demarre!")
            return None
        self.fin = time.perf_counter()
        duree = self.fin - self.debut
        print(f"Temps ecoule : {duree:.4f} secondes")
        return duree

    def __enter__(self):
        self.demarrer()
        return self

    def __exit__(self, *args):
        self.arreter()

# Utilisation classique
chrono = Chronometre()
chrono.demarrer()
time.sleep(0.3)
chrono.arreter()

# Utilisation avec context manager
print("\nAvec context manager :")
with Chronometre():
    time.sleep(0.2)
    resultat = sum(range(1_000_000))

# --- Compte à rebours (rapide) ---
print("\n=== Compte à rebours (rapide) ===")

def compte_a_rebours(n):
    """Compte à rebours rapide sans sleep"""
    for i in range(n, 0, -1):
        print(f"{i}...", end=" ", flush=True)
    print("C'est parti !")

compte_a_rebours(5)
