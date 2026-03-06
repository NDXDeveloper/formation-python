# ============================================================================
#   Section 5.3 : Le module functools.wraps
#   Description : Problème de perte de métadonnées, solution avec @wraps,
#                 préserver __name__, __doc__, __module__
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

from functools import wraps

# --- Le problème : perte de métadonnées ---
print("=== Sans @wraps ===")

def mon_decorateur_sans_wraps(fonction):
    def fonction_modifiee(*args, **kwargs):
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur_sans_wraps
def ma_fonction():
    """Ceci est ma fonction."""
    pass

print(ma_fonction.__name__)  # fonction_modifiee
print(ma_fonction.__doc__)   # None

# --- La solution : @wraps ---
print("\n=== Avec @wraps ===")

def mon_decorateur(fonction):
    @wraps(fonction)
    def fonction_modifiee(*args, **kwargs):
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur
def ma_fonction():
    """Ceci est ma fonction."""
    pass

print(ma_fonction.__name__)  # ma_fonction
print(ma_fonction.__doc__)   # Ceci est ma fonction.

# --- Pourquoi c'est important ---
print("\n=== Métadonnées préservées ===")

def mon_decorateur_propre(fonction):
    @wraps(fonction)
    def fonction_modifiee(*args, **kwargs):
        """Wrapper ajouté par le décorateur."""
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur_propre
def calculer_carre(x):
    """Calcule le carré d'un nombre."""
    return x ** 2

print(f"Nom : {calculer_carre.__name__}")        # Nom : calculer_carre
print(f"Doc : {calculer_carre.__doc__}")          # Doc : Calcule le carré d'un nombre.
print(f"Module : {calculer_carre.__module__}")    # Module : __main__
