# ============================================================================
#   Section 2.4 : Regex - Extraction de données structurées
#   Description : Extraire numéro de facture, date, montant d'une facture
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# Extraire des informations d'une facture
facture = """
Facture N° 2024-001
Date: 27/10/2024
Client: Marie Dupont
Total: 1,234.56 EUR
"""

# Extraire le numéro de facture
numero = re.search(r'N° (\d{4}-\d{3})', facture)
print(f"Numéro : {numero.group(1)}")  # 2024-001

# Extraire la date
date = re.search(r'Date: (\d{2}/\d{2}/\d{4})', facture)
print(f"Date : {date.group(1)}")  # 27/10/2024

# Extraire le montant
montant = re.search(r'Total: ([\d,]+\.?\d*)', facture)
print(f"Montant : {montant.group(1)}")  # 1,234.56
