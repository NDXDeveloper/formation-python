# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Tests complets pour la calculatrice etendue - couvre
#                 toutes les fonctions et branches pour 100% de couverture
#   Fichier source : 03-couverture-de-code.md
# ============================================================================

import pytest
import importlib
_mod = importlib.import_module("03_01_calculatrice_cov")
additionner = _mod.additionner
soustraire = _mod.soustraire
multiplier = _mod.multiplier
diviser = _mod.diviser
calculer_moyenne = _mod.calculer_moyenne


def test_additionner():
    """Teste l'addition."""
    assert additionner(5, 3) == 8
    assert additionner(-1, 1) == 0


def test_soustraire():
    """Teste la soustraction."""
    assert soustraire(10, 4) == 6
    assert soustraire(5, 10) == -5


def test_multiplier():
    """Teste la multiplication."""
    assert multiplier(4, 5) == 20
    assert multiplier(-3, 3) == -9


def test_diviser():
    """Teste la division normale."""
    assert diviser(10, 2) == 5
    assert diviser(9, 3) == 3


def test_diviser_par_zero():
    """Teste la division par zero."""
    with pytest.raises(ValueError, match="Division par zéro"):
        diviser(10, 0)


def test_calculer_moyenne():
    """Teste le calcul de moyenne."""
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3
    assert calculer_moyenne([10, 20]) == 15


def test_calculer_moyenne_liste_vide():
    """Teste la moyenne avec une liste vide."""
    assert calculer_moyenne([]) == 0
