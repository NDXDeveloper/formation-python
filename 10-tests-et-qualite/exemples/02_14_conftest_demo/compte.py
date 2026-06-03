# ============================================================================
#   Section 10.2 : Mocking et fixtures - demonstration de conftest.py
#   Module source : classe Compte utilisee par la fixture partagee.
# ============================================================================


class Compte:
    """Represente un compte bancaire simple."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Depose de l'argent sur le compte."""
        if montant <= 0:
            raise ValueError("Le montant doit etre positif")
        self.solde += montant
