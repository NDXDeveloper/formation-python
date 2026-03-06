# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Tests unittest pour la calculatrice - assertEqual,
#                 assertRaises, pattern AAA (Arrange, Act, Assert)
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

import unittest
from calculatrice import additionner, soustraire, diviser


class TestCalculatrice(unittest.TestCase):
    """Tests pour les fonctions de calculatrice."""

    def test_additionner(self):
        """Teste l'addition de deux nombres."""
        # Arrange
        a = 5
        b = 3
        # Act
        resultat = additionner(a, b)
        # Assert
        self.assertEqual(resultat, 8)

    def test_soustraire(self):
        """Teste la soustraction de deux nombres."""
        resultat = soustraire(10, 4)
        self.assertEqual(resultat, 6)

    def test_diviser(self):
        """Teste la division de deux nombres."""
        resultat = diviser(10, 2)
        self.assertEqual(resultat, 5.0)

    def test_diviser_par_zero(self):
        """Teste que diviser par zero leve une exception."""
        with self.assertRaises(ValueError):
            diviser(10, 0)


if __name__ == '__main__':
    unittest.main()
