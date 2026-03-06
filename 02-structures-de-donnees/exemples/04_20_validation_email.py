# ============================================================================
#   Section 2.4 : Regex - Validation d'email
#   Description : Pattern de validation d'email avec tests
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

def valider_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Tests
emails = [
    "utilisateur@example.com",    # Valide
    "nom.prenom@example.fr",      # Valide
    "invalide@.com",              # Invalide
    "pas-un-email",               # Invalide
    "test@example.co.uk"          # Valide
]

for email in emails:
    status = "Valide" if valider_email(email) else "Invalide"
    print(f"{email}: {status}")
