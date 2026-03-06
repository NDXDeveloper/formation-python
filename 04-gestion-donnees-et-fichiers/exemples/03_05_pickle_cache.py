# ============================================================================
#   Section 4.3 : Pickle - Cache de résultats
#   Description : Système de cache avec pickle pour éviter de recalculer
#                 des résultats coûteux
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

def calcul_long(n):
    """Simule un calcul long (sans sleep pour l'exécution rapide)"""
    print(f"Calcul en cours pour n={n}...")
    # Calcul réel au lieu de sleep
    resultat = sum(range(n * 100000))
    return n ** 2

def calcul_avec_cache(n, fichier_cache='cache.pkl'):
    """Calcul avec système de cache"""

    # Essayer de charger depuis le cache
    try:
        with open(fichier_cache, 'rb') as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    # Si le résultat est en cache, le retourner
    if n in cache:
        print(f"Résultat trouvé en cache pour n={n}")
        return cache[n]

    # Sinon, calculer et sauvegarder
    resultat = calcul_long(n)
    cache[n] = resultat

    with open(fichier_cache, 'wb') as f:
        pickle.dump(cache, f)

    return resultat

# Premier appel : calcul effectué
print("Premier appel :")
resultat = calcul_avec_cache(10)
print(f"Résultat : {resultat}\n")

# Deuxième appel : instantané (depuis le cache)
print("Deuxième appel :")
resultat = calcul_avec_cache(10)
print(f"Résultat : {resultat}")

# Nettoyage
os.remove('cache.pkl')
