# ============================================================================
#   Section 6.10-6.11 : Literal et Final
#   Description : Literal pour valeurs exactes acceptables,
#                 Final pour constantes non réassignables
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import Literal, Final

# --- Literal ---
def definir_mode(mode: Literal["debug", "production"]) -> None:
    """Le mode doit être exactement 'debug' ou 'production'."""
    print(f"Mode : {mode}")

definir_mode("debug")
definir_mode("production")
# definir_mode("test")  # Erreur détectée par mypy !

# Avec des nombres
def definir_niveau(niveau: Literal[1, 2, 3]) -> None:
    print(f"Niveau : {niveau}")

definir_niveau(1)
definir_niveau(2)
definir_niveau(3)

# --- Final ---
PI: Final = 3.14159
MAX_TENTATIVES: Final[int] = 3

# PI = 3.14  # mypy détectera cette erreur !

def utiliser_constante() -> None:
    print(f"Pi vaut {PI}")
    print(f"Max tentatives : {MAX_TENTATIVES}")

utiliser_constante()
