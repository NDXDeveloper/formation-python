# ============================================================================
#   Section 2.4 : Regex - Validation de formats divers
#   Description : Code postal français, plaque d'immatriculation, ISBN
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

def valider_code_postal_fr(code):
    """Code postal français : 5 chiffres"""
    return re.match(r'^\d{5}$', code) is not None

def valider_plaque_immatriculation_fr(plaque):
    """Format : AB-123-CD"""
    return re.match(r'^[A-Z]{2}-\d{3}-[A-Z]{2}$', plaque) is not None

def valider_isbn(isbn):
    """ISBN-10 ou ISBN-13"""
    pattern = r'^(?:\d{9}[\dX]|\d{13})$'
    isbn_clean = isbn.replace('-', '').replace(' ', '')
    return re.match(pattern, isbn_clean) is not None

# Tests
print(valider_code_postal_fr("75001"))  # True
print(valider_code_postal_fr("7500"))   # False

print(valider_plaque_immatriculation_fr("AB-123-CD"))  # True
print(valider_plaque_immatriculation_fr("AB123CD"))    # False

print(valider_isbn("978-0-13-110362-7"))  # True
print(valider_isbn("0-13-110362-8"))      # True
