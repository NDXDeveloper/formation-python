# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Fixtures unittest - setUp/tearDown par test,
#                 setUpClass/tearDownClass par classe
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import unittest


class Compte:
    """Represente un compte bancaire."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Depose de l'argent."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant

    def retirer(self, montant):
        """Retire de l'argent."""
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant


class TestCompte(unittest.TestCase):
    """Tests pour la classe Compte."""

    def setUp(self):
        """Appelee avant CHAQUE test."""
        print("\nSetup : creation du compte")
        self.compte = Compte("Alice", solde=1000)

    def tearDown(self):
        """Appelee apres CHAQUE test."""
        print("Teardown : nettoyage")
        self.compte = None

    def test_deposer(self):
        """Teste le depot."""
        self.compte.deposer(500)
        self.assertEqual(self.compte.solde, 1500)

    def test_retirer(self):
        """Teste le retrait."""
        self.compte.retirer(300)
        self.assertEqual(self.compte.solde, 700)


class TestCompteAvecSetupUnique(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Appelee UNE FOIS avant tous les tests de la classe."""
        print("\nSetup classe : preparation globale")
        cls.taux_interet = 0.03

    @classmethod
    def tearDownClass(cls):
        """Appelee UNE FOIS apres tous les tests de la classe."""
        print("\nTeardown classe : nettoyage global")

    def setUp(self):
        """Appelee avant chaque test."""
        self.compte = Compte("Bob", solde=1000)

    def test_calcul_interet(self):
        """Teste le calcul d'interet."""
        interet = self.compte.solde * self.taux_interet
        self.assertEqual(interet, 30.0)

    def test_solde_initial(self):
        """Teste le solde initial."""
        self.assertEqual(self.compte.solde, 1000)


if __name__ == '__main__':
    unittest.main()
