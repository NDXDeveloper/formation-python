# ============================================================================
#   Section 3.4 : Décorateur avec arguments
#   Description : Logger qui affiche les arguments et résultats des fonctions
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

def logger(fonction):
    """Décorateur qui affiche les appels de fonction"""
    def wrapper(*args, **kwargs):
        print(f"Appel de {fonction.__name__} avec args={args}, kwargs={kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"Résultat : {resultat}")
        return resultat
    return wrapper

@logger
def additionner(a, b):
    return a + b

@logger
def saluer(nom, message="Bonjour"):
    return f"{message} {nom} !"

# Utilisation
resultat1 = additionner(5, 3)
print()
resultat2 = saluer("Alice", message="Salut")
