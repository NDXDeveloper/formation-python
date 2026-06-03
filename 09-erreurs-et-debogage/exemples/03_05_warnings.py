# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Module warnings - signaler sans planter (warnings.warn),
#                 deprecier une fonction, transformer les warnings en erreurs
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

import warnings

# ==========================================
# 1. Emettre un avertissement (UserWarning)
# ==========================================
print("=== warnings.warn (UserWarning) ===\n")

def diviser(a, b):
    if b == 0:
        warnings.warn("Division par zero evitee, retour de None", UserWarning)
        return None
    return a / b

print(f"  diviser(10, 0) = {diviser(10, 0)}")

# ==========================================
# 2. Deprecier une fonction (DeprecationWarning)
# ==========================================
print("\n=== Deprecation (DeprecationWarning) ===\n")

def ancienne_api():
    warnings.warn(
        "ancienne_api() est obsolete, utilisez nouvelle_api()",
        DeprecationWarning,
        stacklevel=2,  # pointe vers l'appelant, pas vers cette ligne
    )
    return 42

# DeprecationWarning est masque par defaut ; on le rend visible pour la demo :
warnings.simplefilter("always", DeprecationWarning)
print(f"  ancienne_api() = {ancienne_api()}")

# ==========================================
# 3. Transformer les avertissements en erreurs (debogage / tests)
# ==========================================
print("\n=== simplefilter('error') : un warning devient une exception ===\n")

warnings.simplefilter("error")
try:
    warnings.warn("ceci devient une exception")
except UserWarning as e:
    print(f"  Capture comme exception : {e}")
