# ============================================================================
#   Section 2.4 : Regex - Remplacer avec des groupes de capture
#   Description : Reformatage de dates, anonymisation d'emails
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# Formater des dates
texte = "Les dates importantes sont : 2024/10/27 et 2024/12/25"

# Convertir du format YYYY/MM/DD au format DD-MM-YYYY
nouveau = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\3-\2-\1', texte)
print(nouveau)
# Les dates importantes sont : 27-10-2024 et 25-12-2024

# Anonymiser des emails
texte = "Contactez alice@example.com ou bob@test.com"
anonymise = re.sub(r'(\w+)@(\w+\.\w+)', r'****@\2', texte)
print(anonymise)
# Contactez ****@example.com ou ****@test.com
