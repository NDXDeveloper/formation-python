# ============================================================================
#   Section 3.4 : Décorateur de cache (mémoïsation)
#   Description : Cache des résultats précédents, appliqué à fibonacci
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

def cache(fonction):
    """Mémorise les résultats des appels précédents"""
    resultats_sauvegardes = {}

    def wrapper(*args):
        if args in resultats_sauvegardes:
            print(f"Résultat en cache pour {args}")
            return resultats_sauvegardes[args]

        print(f"Calcul pour {args}")
        resultat = fonction(*args)
        resultats_sauvegardes[args] = resultat
        return resultat

    return wrapper

@cache
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Premier appel : calcul complet
print(f"fibonacci(5) = {fibonacci(5)}")
print()

# Deuxième appel : résultats en cache
print(f"fibonacci(5) = {fibonacci(5)}")
