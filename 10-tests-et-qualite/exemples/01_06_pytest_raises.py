# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Tester les exceptions avec pytest.raises -- verifier qu'une
#                 exception est levee, controler son message avec `match`
#                 (expression reguliere), et inspecter l'objet via `as excinfo`.
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
#   Execution : pytest 01_06_pytest_raises.py -v -o "addopts="
# ============================================================================

import pytest


def retirer(solde, montant):
    """Retire un montant d'un solde ; leve ValueError si fonds insuffisants."""
    if montant > solde:
        raise ValueError("Solde insuffisant pour ce retrait")
    return solde - montant


def test_raises_simple():
    """pytest.raises : verifie qu'une exception est bien levee."""
    with pytest.raises(ValueError):
        retirer(100, 500)


def test_raises_match():
    """match : le message doit correspondre (sous-chaine / regex, via re.search)."""
    with pytest.raises(ValueError, match="insuffisant"):
        retirer(100, 500)


def test_raises_excinfo():
    """as excinfo : inspecter le type et le message de l'exception capturee."""
    with pytest.raises(ValueError) as excinfo:
        retirer(100, 500)

    assert excinfo.type is ValueError
    assert "insuffisant" in str(excinfo.value)


def test_pas_d_exception_si_solde_suffisant():
    """Cas nominal : aucune exception levee, le retrait est effectue."""
    assert retirer(100, 30) == 70
