# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Module validation - valider_note et calculer_mention
#                 (pour demo couverture de branches)
#   Fichier source : 03-couverture-de-code.md
# ============================================================================


def valider_note(note):
    """Valide une note et retourne un message."""
    if note < 0 or note > 20:
        return "Note invalide"

    if note >= 10:
        return "Réussi"
    else:
        return "Échoué"


def calculer_mention(moyenne):
    """Calcule la mention selon la moyenne."""
    if moyenne < 10:
        return "Échec"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Assez bien"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Très bien"
