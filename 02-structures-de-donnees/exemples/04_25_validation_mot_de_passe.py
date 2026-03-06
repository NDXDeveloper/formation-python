# ============================================================================
#   Section 2.4 : Regex - Validation de mot de passe
#   Description : Vérifier longueur, majuscule, minuscule, chiffre, caractère
#                 spécial
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

def valider_mot_de_passe(mdp):
    """
    Règles:
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial
    """
    if len(mdp) < 8:
        return False, "Doit contenir au moins 8 caractères"

    if not re.search(r'[A-Z]', mdp):
        return False, "Doit contenir au moins une majuscule"

    if not re.search(r'[a-z]', mdp):
        return False, "Doit contenir au moins une minuscule"

    if not re.search(r'\d', mdp):
        return False, "Doit contenir au moins un chiffre"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', mdp):
        return False, "Doit contenir au moins un caractère spécial"

    return True, "Mot de passe valide"

# Tests
mots_de_passe = [
    "faible",
    "Faible123",
    "Faible123!",
    "F@ible1"
]

for mdp in mots_de_passe:
    valide, message = valider_mot_de_passe(mdp)
    print(f"{mdp}: {message}")
