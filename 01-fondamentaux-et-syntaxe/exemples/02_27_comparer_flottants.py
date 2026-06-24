# ============================================================================
#   Section 2.27 : Comparer des nombres flottants
#   Description : ne pas comparer des floats avec == ; math.isclose() ;
#                 decimal.Decimal pour des calculs décimaux exacts
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

import math
from decimal import Decimal

# --- Le piège : == sur des flottants ---
print(0.1 + 0.2)                       # 0.30000000000000004
print(0.1 + 0.2 == 0.3)                # False (le piège !)

# --- La bonne façon : math.isclose() ---
print(math.isclose(0.1 + 0.2, 0.3))    # True

# --- Calculs décimaux exacts : module decimal (ex. sommes d'argent) ---
print(Decimal("0.1") + Decimal("0.2"))                    # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
