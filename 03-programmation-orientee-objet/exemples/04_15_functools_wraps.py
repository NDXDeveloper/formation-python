# ============================================================================
#   Section 3.4 : Préserver les métadonnées avec functools.wraps
#   Description : Utiliser @wraps pour conserver __name__ et __doc__ d'une
#                 fonction décorée
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

from functools import wraps

def mon_decorateur(fonction):
    @wraps(fonction)  # Préserve les métadonnées
    def wrapper(*args, **kwargs):
        print("Avant")
        resultat = fonction(*args, **kwargs)
        print("Après")
        return resultat
    return wrapper

@mon_decorateur
def ma_fonction():
    """Ceci est ma fonction"""
    print("Ma fonction")

print(ma_fonction.__name__)  # ma_fonction (au lieu de wrapper)
print(ma_fonction.__doc__)   # Ceci est ma fonction
