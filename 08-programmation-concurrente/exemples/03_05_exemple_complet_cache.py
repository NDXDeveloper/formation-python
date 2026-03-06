# ============================================================================
#   Section 8.3 : Gestion des Verrous et Synchronisation
#   Description : Exemple complet - Cache thread-safe avec expiration,
#                 statistiques hits/misses, patterns avancés (Singleton,
#                 ReadWriteLock)
#   Fichier source : 03-verrous-et-synchronisation.md
# ============================================================================

import threading
import time
from typing import Any

class CacheThreadSafe:
    """Cache thread-safe avec expiration automatique"""

    def __init__(self, duree_vie: int = 60):
        self.cache = {}
        self.duree_vie = duree_vie
        self.verrou = threading.RLock()
        self.stats = {'hits': 0, 'misses': 0, 'expirations': 0}
        self.verrou_stats = threading.Lock()

    def get(self, cle: str) -> Any | None:
        with self.verrou:
            if cle not in self.cache:
                self._incrementer_stat('misses')
                return None

            valeur, timestamp = self.cache[cle]

            if time.time() - timestamp > self.duree_vie:
                del self.cache[cle]
                self._incrementer_stat('expirations')
                self._incrementer_stat('misses')
                return None

            self._incrementer_stat('hits')
            return valeur

    def set(self, cle: str, valeur: Any):
        with self.verrou:
            self.cache[cle] = (valeur, time.time())

    def clear(self):
        with self.verrou:
            self.cache.clear()

    def get_stats(self) -> dict:
        with self.verrou_stats:
            return self.stats.copy()

    def _incrementer_stat(self, stat: str):
        with self.verrou_stats:
            self.stats[stat] += 1


def travailleur_cache(cache, worker_id, operations):
    """Thread qui utilise le cache"""
    for i in range(operations):
        cle = f"data_{i % 10}"

        valeur = cache.get(cle)

        if valeur is None:
            valeur = f"Résultat_{worker_id}_{i}"
            cache.set(cle, valeur)
            print(f"  [Worker {worker_id}] Miss - Calculé: {cle}")
        else:
            print(f"  [Worker {worker_id}] Hit - Trouvé: {cle}")

        time.sleep(0.02)


# ==========================================
# 1. Cache thread-safe en action
# ==========================================
print("=== Cache thread-safe ===")

cache = CacheThreadSafe(duree_vie=5)

threads = [
    threading.Thread(target=travailleur_cache, args=(cache, i, 15))
    for i in range(3)
]

debut = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
duree = time.time() - debut

stats = cache.get_stats()
total_ops = stats['hits'] + stats['misses']
print(f"\nStatistiques finales:")
print(f"  Hits: {stats['hits']}")
print(f"  Misses: {stats['misses']}")
print(f"  Expirations: {stats['expirations']}")
if total_ops > 0:
    print(f"  Taux de hit: {stats['hits']/total_ops*100:.1f}%")
print(f"  Durée totale: {duree:.2f}s")

# ==========================================
# 2. Pattern Singleton thread-safe
# ==========================================
print("\n=== Singleton thread-safe ===")

class Singleton:
    """Singleton thread-safe avec double-checked locking"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"s1 is s2: {s1 is s2}")
print(f"id(s1) == id(s2): {id(s1) == id(s2)}")

# ==========================================
# 3. Read-Write Lock
# ==========================================
print("\n=== Read-Write Lock ===")

class ReadWriteLock:
    """Lock optimisé pour lectures multiples, écriture exclusive"""

    def __init__(self):
        self.lecteurs = 0
        self.verrou_lecteurs = threading.Lock()
        self.verrou_ecrivain = threading.Lock()

    def acquire_read(self):
        with self.verrou_lecteurs:
            self.lecteurs += 1
            if self.lecteurs == 1:
                self.verrou_ecrivain.acquire()

    def release_read(self):
        with self.verrou_lecteurs:
            self.lecteurs -= 1
            if self.lecteurs == 0:
                self.verrou_ecrivain.release()

    def acquire_write(self):
        self.verrou_ecrivain.acquire()

    def release_write(self):
        self.verrou_ecrivain.release()

rwlock = ReadWriteLock()
donnees = ["valeur_initiale"]

def lecteur(reader_id):
    rwlock.acquire_read()
    try:
        print(f"  [Lecteur {reader_id}] Lecture: {donnees[0]}")
        time.sleep(0.1)
    finally:
        rwlock.release_read()

def ecrivain(writer_id, nouvelle_valeur):
    rwlock.acquire_write()
    try:
        print(f"  [Ecrivain {writer_id}] Écriture: {nouvelle_valeur}")
        donnees[0] = nouvelle_valeur
        time.sleep(0.1)
    finally:
        rwlock.release_write()

# Plusieurs lecteurs peuvent lire en parallèle
threads = [
    threading.Thread(target=lecteur, args=(0,)),
    threading.Thread(target=lecteur, args=(1,)),
    threading.Thread(target=ecrivain, args=(0, "nouvelle_valeur")),
    threading.Thread(target=lecteur, args=(2,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Valeur finale: {donnees[0]}")
