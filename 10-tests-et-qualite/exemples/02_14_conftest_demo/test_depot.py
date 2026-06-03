# ============================================================================
#   Tests utilisant la fixture 'compte' definie dans conftest.py.
#   Remarquez : aucun import de la fixture n'est necessaire.
#   Execution : depuis ce dossier -> pytest -v -o "addopts="
# ============================================================================


def test_solde_initial(compte):
    """La fixture fournit un compte avec un solde de 1000."""
    assert compte.solde == 1000


def test_deposer(compte):
    """Chaque test recoit une instance neuve de la fixture."""
    compte.deposer(500)
    assert compte.solde == 1500
