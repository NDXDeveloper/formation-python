# ============================================================================
#   Section 3.4 : Décorateurs avec paramètres
#   Description : Décorateur repeter(n), décorateur debug avec niveau de log
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- Décorateur repeter ---
def repeter(nombre_fois):
    """Décorateur qui répète l'exécution d'une fonction"""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for i in range(nombre_fois):
                print(f"Exécution {i+1}/{nombre_fois}")
                resultat = fonction(*args, **kwargs)
            return resultat
        return wrapper
    return decorateur

@repeter(nombre_fois=3)
def afficher_message(message):
    print(f"Message : {message}")

afficher_message("Bonjour !")

# --- Décorateur debug avec niveau ---
print()

def debug(niveau="INFO"):
    """Décorateur de debug avec niveau de log"""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            print(f"[{niveau}] Appel de {fonction.__name__}")
            print(f"[{niveau}] Arguments : args={args}, kwargs={kwargs}")
            resultat = fonction(*args, **kwargs)
            print(f"[{niveau}] Résultat : {resultat}")
            return resultat
        return wrapper
    return decorateur

@debug(niveau="DEBUG")
def multiplier(a, b):
    return a * b

@debug(niveau="INFO")
def diviser(a, b):
    return a / b

resultat1 = multiplier(5, 3)
print()
resultat2 = diviser(10, 2)
