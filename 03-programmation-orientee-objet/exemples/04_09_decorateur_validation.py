# ============================================================================
#   Section 3.4 : Décorateur de validation
#   Description : Vérifier que tous les arguments sont positifs
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

def valider_positif(fonction):
    """Vérifie que tous les arguments sont positifs"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument négatif non autorisé : {arg}")

        for valeur in kwargs.values():
            if isinstance(valeur, (int, float)) and valeur < 0:
                raise ValueError(f"Argument négatif non autorisé : {valeur}")

        return fonction(*args, **kwargs)
    return wrapper

@valider_positif
def calculer_surface_rectangle(largeur, hauteur):
    return largeur * hauteur

print(calculer_surface_rectangle(5, 3))   # 15

try:
    print(calculer_surface_rectangle(-5, 3))  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")
