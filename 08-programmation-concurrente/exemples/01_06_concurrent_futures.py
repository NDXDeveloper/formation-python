# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : concurrent.futures - l'API unifiee : ThreadPoolExecutor,
#                 ProcessPoolExecutor, map(), submit()/Future, as_completed()
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time

# Fonctions definies au niveau du module : indispensable pour ProcessPoolExecutor
# avec les methodes de demarrage spawn/forkserver (defaut Windows/macOS, et Linux
# a partir de Python 3.14), ou le processus enfant reimporte le module.

def traiter(n):
    """Tache simple : carre d'un nombre"""
    return n * n

def tache_lente(duree):
    """Tache I/O simulee : attend puis renvoie un message"""
    time.sleep(duree)
    return f"termine apres {duree}s"

def calcul_cpu(n):
    """Tache CPU-bound : somme des carres jusqu'a n"""
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    # ==========================================
    # 1. ThreadPoolExecutor.map() - I/O-bound
    # ==========================================
    print("=== ThreadPoolExecutor.map() ===")
    with ThreadPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(traiter, [1, 2, 3, 4, 5]))
    print(f"map(traiter, 1..5) = {resultats}")

    # ==========================================
    # 2. submit() et objets Future
    # ==========================================
    print("\n=== submit() et Future ===")
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(tache_lente, d): d for d in (0.3, 0.1, 0.2)}
        for future in futures:
            print(f"  Future(duree={futures[future]}) -> {future.result()}")

    # ==========================================
    # 3. as_completed() - resultats au fil de l'eau
    # ==========================================
    print("\n=== as_completed() (ordre d'arrivee) ===")
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(tache_lente, d) for d in (0.3, 0.1, 0.2)]
        for future in as_completed(futures):
            print(f"  arrive: {future.result()}")

    # ==========================================
    # 4. ProcessPoolExecutor - CPU-bound (vrai parallelisme)
    # ==========================================
    print("\n=== ProcessPoolExecutor.map() (CPU-bound) ===")
    nombres = [100000, 200000, 300000, 400000]
    debut = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        totaux = list(executor.map(calcul_cpu, nombres))
    duree = time.perf_counter() - debut
    print(f"Sommes des carres : {len(totaux)} resultats calcules")
    print(f"Pour passer des threads aux processus : ThreadPoolExecutor -> ProcessPoolExecutor")
    print(f"Calcul parallele en {duree:.3f}s")
