# ============================================================================
#   Section 5.3 : Décorateurs pratiques
#   Description : Mesurer le temps d'exécution, logger les appels,
#                 cache (mémorisation), contrôle d'accès
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

import time

# --- Mesurer le temps d'exécution ---
print("=== Mesurer le temps ===")

def mesurer_temps(fonction):
    """Mesure le temps d'exécution d'une fonction."""
    def fonction_modifiee(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        duree = fin - debut
        print(f"[temps] {fonction.__name__} a pris {duree:.4f} secondes")
        return resultat
    return fonction_modifiee

@mesurer_temps
def calculer_somme(n):
    """Calcule la somme des n premiers nombres."""
    total = sum(range(n))
    return total

resultat = calculer_somme(1000000)
print(f"Somme : {resultat}")
# Somme : 499999500000

# --- Logger les appels ---
print("\n=== Logger les appels ===")

def logger(fonction):
    """Enregistre les appels de fonction avec leurs arguments."""
    def fonction_modifiee(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        tous_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"[log] Appel de {fonction.__name__}({tous_args})")
        resultat = fonction(*args, **kwargs)
        print(f"[ok] {fonction.__name__} a retourné {repr(resultat)}")
        return resultat
    return fonction_modifiee

@logger
def multiplier(a, b):
    return a * b

@logger
def saluer(nom, message="Bonjour"):
    return f"{message} {nom} !"

resultat1 = multiplier(5, 3)
# [log] Appel de multiplier(5, 3)
# [ok] multiplier a retourné 15

print()

resultat2 = saluer("Alice", message="Salut")
# [log] Appel de saluer('Alice', message='Salut')
# [ok] saluer a retourné 'Salut Alice !'

# --- Cache (mémorisation) ---
print("\n=== Cache ===")

def cache(fonction):
    """Mémorise les résultats d'une fonction pour éviter les recalculs."""
    resultats_sauvegardes = {}

    def fonction_modifiee(*args):
        if args in resultats_sauvegardes:
            print(f"[cache] Résultat en cache pour {args}")
            return resultats_sauvegardes[args]

        print(f"[calcul] Calcul en cours pour {args}")
        resultat = fonction(*args)
        resultats_sauvegardes[args] = resultat
        return resultat

    return fonction_modifiee

@cache
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
# Affiche les étapes de calcul et cache
# 5

print(fibonacci(5))  # Deuxième appel
# [cache] Résultat en cache pour (5,)
# 5

# --- Contrôle d'accès ---
print("\n=== Contrôle d'accès ===")

def necessite_authentification(fonction):
    """Vérifie qu'un utilisateur est authentifié avant d'exécuter."""
    def fonction_modifiee(*args, **kwargs):
        utilisateur_connecte = True  # Simulation

        if not utilisateur_connecte:
            print("[refus] Accès refusé : vous devez être connecté")
            return None

        print("[auth] Authentification réussie")
        return fonction(*args, **kwargs)

    return fonction_modifiee

@necessite_authentification
def voir_profil(nom):
    print(f"Profil de {nom}")
    return {"nom": nom, "age": 30}

profil = voir_profil("Alice")
# [auth] Authentification réussie
# Profil de Alice
