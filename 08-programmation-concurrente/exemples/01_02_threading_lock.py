# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Partage de données entre threads avec Lock,
#                 démonstration du problème sans Lock
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

import threading

# ==========================================
# 1. Compteur AVEC Lock (correct)
# ==========================================
print("=== Compteur avec Lock ===")

compteur = 0
lock = threading.Lock()

def incrementer_avec_lock():
    global compteur
    for _ in range(100000):
        with lock:
            compteur += 1

threads = []
for _ in range(5):
    thread = threading.Thread(target=incrementer_avec_lock)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Valeur finale du compteur (avec lock): {compteur}")
print(f"  Attendu: 500000")
print(f"  Correct: {compteur == 500000}")

# ==========================================
# 2. Compteur SANS Lock (potentiellement incorrect)
# ==========================================
print("\n=== Compteur sans Lock (problème potentiel) ===")

compteur_sans_lock = 0

def incrementer_sans_lock():
    global compteur_sans_lock
    for _ in range(100000):
        compteur_sans_lock += 1

threads = []
for _ in range(5):
    thread = threading.Thread(target=incrementer_sans_lock)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Valeur finale du compteur (sans lock): {compteur_sans_lock}")
print(f"  Attendu: 500000")
print(f"  Correct: {compteur_sans_lock == 500000}")
if compteur_sans_lock != 500000:
    print(f"  Erreur de {500000 - compteur_sans_lock} incréments perdus (race condition)")
else:
    print("  (Le GIL a peut-être protégé cette fois, mais ce n'est pas garanti)")
