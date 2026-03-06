# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Module calculatrice etendu - additionner, soustraire,
#                 multiplier, diviser, calculer_moyenne (pour demo couverture)
#   Fichier source : 03-couverture-de-code.md
# ============================================================================


def additionner(a, b):
    """Additionne deux nombres."""
    return a + b


def soustraire(a, b):
    """Soustrait b de a."""
    return a - b


def multiplier(a, b):
    """Multiplie deux nombres."""
    return a * b


def diviser(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b


def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres."""
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)
