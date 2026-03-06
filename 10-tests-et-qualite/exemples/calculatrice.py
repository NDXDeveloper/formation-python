# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Module calculatrice - fonctions additionner, soustraire,
#                 diviser (utilisee par les fichiers de tests)
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

def additionner(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraire(a, b):
    """Soustrait b de a."""
    return a - b

def diviser(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b
