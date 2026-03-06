# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Assertions unittest - assertEqual, assertNotEqual,
#                 assertTrue/False, assertIsNone, assertIn, assertGreater,
#                 assertAlmostEqual, setUp/tearDown
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

import unittest


class TestAssertions(unittest.TestCase):

    def test_egalite(self):
        """Verifie l'egalite."""
        self.assertEqual(2 + 2, 4)
        self.assertEqual("hello", "hello")

    def test_inegalite(self):
        """Verifie l'inegalite."""
        self.assertNotEqual(5, 3)

    def test_booleen(self):
        """Verifie les valeurs booleennes."""
        self.assertTrue(1 < 2)
        self.assertFalse(5 < 3)

    def test_none(self):
        """Verifie les valeurs None."""
        valeur = None
        self.assertIsNone(valeur)
        autre_valeur = "quelque chose"
        self.assertIsNotNone(autre_valeur)

    def test_appartenance(self):
        """Verifie l'appartenance a une collection."""
        liste = [1, 2, 3, 4, 5]
        self.assertIn(3, liste)
        self.assertNotIn(10, liste)

    def test_comparaison_numerique(self):
        """Verifie les comparaisons numeriques."""
        self.assertGreater(5, 3)
        self.assertLess(2, 10)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(3, 4)

    def test_approximation(self):
        """Verifie l'egalite approximative pour les nombres flottants."""
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)


class TestAvecPreparation(unittest.TestCase):

    def setUp(self):
        """Appelee AVANT chaque test."""
        self.liste = [1, 2, 3, 4, 5]
        self.dictionnaire = {"nom": "Alice", "age": 30}

    def tearDown(self):
        """Appelee APRES chaque test."""
        self.liste = None
        self.dictionnaire = None

    def test_liste(self):
        """Teste la liste preparee."""
        self.assertEqual(len(self.liste), 5)
        self.assertIn(3, self.liste)

    def test_dictionnaire(self):
        """Teste le dictionnaire prepare."""
        self.assertEqual(self.dictionnaire["nom"], "Alice")
        self.assertEqual(self.dictionnaire["age"], 30)


if __name__ == '__main__':
    unittest.main()
