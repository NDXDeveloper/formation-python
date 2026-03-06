# ============================================================================
#   Section 3.4 : Décorateur compteur d'appels
#   Description : Compter le nombre de fois qu'une fonction est appelée
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

def compteur_appels(fonction):
    """Compte le nombre de fois qu'une fonction est appelée"""
    def wrapper(*args, **kwargs):
        wrapper.nombre_appels += 1
        print(f"Appel n°{wrapper.nombre_appels} de {fonction.__name__}")
        return fonction(*args, **kwargs)

    wrapper.nombre_appels = 0
    return wrapper

@compteur_appels
def saluer(nom):
    return f"Bonjour {nom} !"

print(saluer("Alice"))
print(saluer("Bob"))
print(saluer("Charlie"))
print(f"\nLa fonction a été appelée {saluer.nombre_appels} fois")
