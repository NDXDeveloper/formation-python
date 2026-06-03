# ============================================================================
#   Section 9.2 : Creation d'exceptions personnalisees
#   Description : Chainer les exceptions avec 'raise ... from ...' (preserver la
#                 cause d'origine) et add_note() pour ajouter du contexte (3.11+)
#   Fichier source : 02-exceptions-personnalisees.md
# ============================================================================

import sys

class ConfigError(Exception):
    """Erreur de configuration de l'application."""
    pass

# ==========================================
# 1. Chainer une exception (raise ... from ...)
# ==========================================
print("=== Chainage : raise ... from ... ===\n")

def charger_config(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            return int(f.read())
    except FileNotFoundError as e:
        # Traduit l'erreur technique en erreur metier, en gardant la cause
        raise ConfigError(f"Configuration introuvable : {chemin}") from e

try:
    charger_config("absent.txt")
except ConfigError as e:
    print(f"  Erreur metier : {e}")
    print(f"  Cause d'origine (__cause__) : {type(e.__cause__).__name__}: {e.__cause__}")

# ==========================================
# 2. add_note() - ajouter du contexte (Python 3.11+)
# ==========================================
print("\n=== add_note() (Python 3.11+) ===\n")

if sys.version_info >= (3, 11):
    try:
        erreur = ValueError("donnee invalide")
        erreur.add_note("Verifier le format du fichier d'entree")
        erreur.add_note("Ligne 42 du CSV")
        raise erreur
    except ValueError as exc:
        print(f"  Message : {exc}")
        print(f"  Notes   : {exc.__notes__}")
else:
    print("  add_note() necessite Python 3.11+")
    print(f"  Version actuelle : {sys.version_info.major}.{sys.version_info.minor}")
