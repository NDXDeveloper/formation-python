# ============================================================================
#   Section 2.4 : Regex - Extraction de numéros de téléphone
#   Description : Patterns pour différents formats de téléphone français
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

texte = """
Contactez-nous:
Bureau: 01-23-45-67-89
Mobile: 06.12.34.56.78
Support: 0987654321
"""

# Pattern pour différents formats
patterns = [
    r'\d{2}-\d{2}-\d{2}-\d{2}-\d{2}',      # Format: 01-23-45-67-89
    r'\d{2}\.\d{2}\.\d{2}\.\d{2}\.\d{2}',   # Format: 01.23.45.67.89
    r'\d{10}'                                 # Format: 0123456789
]

for pattern in patterns:
    telephones = re.findall(pattern, texte)
    if telephones:
        print(f"Trouvés avec le pattern '{pattern}':", telephones)
