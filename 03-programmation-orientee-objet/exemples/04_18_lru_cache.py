# ============================================================================
#   Section 3.4 : Cache standard avec functools (cache / lru_cache)
#   Description : Équivalent standard du décorateur de cache maison ;
#                 functools.cache (3.9+) et lru_cache(maxsize=...) + cache_info
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

from functools import cache, lru_cache


# --- functools.cache : mémorise TOUS les appels (= lru_cache(maxsize=None)) ---
@cache
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


print(f"fibonacci(30) = {fibonacci(30)}")   # 832040, calculé en un éclair
print(f"fibonacci(35) = {fibonacci(35)}")   # 9227465 (réutilise le cache)
print("Cache fibonacci :", fibonacci.cache_info())
# CacheInfo(hits=..., misses=36, maxsize=None, currsize=36)


# --- lru_cache(maxsize=N) : borne la mémoire (éviction des moins récents) ---
@lru_cache(maxsize=128)
def carre(n):
    print(f"  (calcul de carre({n}))")
    return n * n


print("\nAvec lru_cache(maxsize=128) :")
print("carre(4) =", carre(4))   # calculé
print("carre(4) =", carre(4))   # en cache : aucun recalcul
print("carre(5) =", carre(5))   # calculé
print("Statistiques :", carre.cache_info())   # hits=1, misses=2, currsize=2

# Vider le cache si besoin
carre.cache_clear()
print("Après cache_clear :", carre.cache_info())   # hits=0, misses=0, currsize=0
