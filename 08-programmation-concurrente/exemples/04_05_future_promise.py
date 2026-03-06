# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Future/Promise - soumission de taches avec
#                 concurrent.futures, gestion d'erreurs, as_completed
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

random.seed(42)

# ==========================================
# 1. Future basique avec submit/result
# ==========================================
print("=== Future/Promise (basique) ===\n")

def tache_longue(nom, duree):
    """Simule une tache qui prend du temps"""
    print(f"  Demarrage: {nom}")
    time.sleep(duree)
    resultat = f"Resultat de {nom}"
    print(f"  Termine: {nom}")
    return resultat

executor = ThreadPoolExecutor(max_workers=3)

print("Soumission des taches\n")
future1 = executor.submit(tache_longue, "Tache-A", 0.4)
future2 = executor.submit(tache_longue, "Tache-B", 0.2)
future3 = executor.submit(tache_longue, "Tache-C", 0.6)

print("Les taches sont lancees, on peut faire autre chose...\n")
time.sleep(0.1)
print("Autre travail en cours...\n")

print("Recuperation des resultats:")
print(f"  Future1 termine? {future1.done()}")
print(f"  Future2 termine? {future2.done()}")

print(f"  Resultat 1: {future1.result()}")
print(f"  Resultat 2: {future2.result()}")
print(f"  Resultat 3: {future3.result()}")

executor.shutdown()
print("\nToutes les futures resolues")

# ==========================================
# 2. Gestion d'erreurs avec Future
# ==========================================
print("\n=== Future - Gestion d'erreurs ===\n")

def tache_avec_erreur(numero):
    """Tache qui peut echouer"""
    time.sleep(0.1)
    if numero == 3:
        raise ValueError(f"Erreur avec le numero {numero}")
    return f"Succes {numero}"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(tache_avec_erreur, i) for i in range(1, 6)]

    for i, future in enumerate(futures, 1):
        try:
            resultat = future.result()
            print(f"  Tache {i}: {resultat}")
        except Exception as e:
            print(f"  Tache {i}: Erreur - {e}")

# ==========================================
# 3. as_completed - Traiter au fur et a mesure
# ==========================================
print("\n=== Future - as_completed ===\n")

def telecharger_fichier(url):
    """Simule le telechargement d'un fichier"""
    duree = random.uniform(0.1, 0.4)
    time.sleep(duree)
    return f"{url} telecharge en {duree:.1f}s"

urls = [f"https://example.com/file{i}.zip" for i in range(8)]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(telecharger_fichier, url): url for url in urls}

    for future in as_completed(futures):
        url = futures[future]
        try:
            resultat = future.result()
            print(f"  {resultat}")
        except Exception as e:
            print(f"  {url}: Erreur - {e}")
