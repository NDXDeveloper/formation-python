# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Tests unittest pour le panier d'achat - ajout, total,
#                 nombre d'articles, vidage, prix negatif, quantite zero,
#                 cas parametres
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

import unittest
from panier import Panier


class TestPanier(unittest.TestCase):

    def setUp(self):
        """Cree un panier vide pour chaque test."""
        self.panier = Panier()

    def test_panier_vide_au_depart(self):
        """Teste qu'un nouveau panier est vide."""
        self.assertEqual(len(self.panier.articles), 0)
        self.assertEqual(self.panier.total(), 0)
        self.assertEqual(self.panier.nombre_articles(), 0)

    def test_ajouter_un_article(self):
        """Teste l'ajout d'un article."""
        self.panier.ajouter("Pomme", 2.50, 3)
        self.assertEqual(len(self.panier.articles), 1)
        self.assertEqual(self.panier.nombre_articles(), 3)

    def test_calculer_total(self):
        """Teste le calcul du total."""
        self.panier.ajouter("Pomme", 2.50, 2)   # 5.00
        self.panier.ajouter("Orange", 3.00, 1)  # 3.00
        self.assertEqual(self.panier.total(), 8.00)

    def test_ajouter_prix_negatif(self):
        """Teste qu'on ne peut pas ajouter un article avec un prix negatif."""
        with self.assertRaises(ValueError):
            self.panier.ajouter("Article", -10, 1)

    def test_ajouter_quantite_zero(self):
        """Teste qu'on ne peut pas ajouter une quantite nulle."""
        with self.assertRaises(ValueError):
            self.panier.ajouter("Article", 10, 0)

    def test_vider_panier(self):
        """Teste le vidage du panier."""
        self.panier.ajouter("Pomme", 2.50, 2)
        self.panier.ajouter("Orange", 3.00, 1)
        self.panier.vider()
        self.assertEqual(len(self.panier.articles), 0)
        self.assertEqual(self.panier.total(), 0)

    def test_calcul_total_pomme(self):
        """Teste le total pour des pommes."""
        self.panier.ajouter("Pomme", 2.00, 1)
        self.assertEqual(self.panier.total(), 2.00)

    def test_calcul_total_orange(self):
        """Teste le total pour des oranges."""
        self.panier.ajouter("Orange", 3.50, 2)
        self.assertEqual(self.panier.total(), 7.00)

    def test_calcul_total_banane(self):
        """Teste le total pour des bananes."""
        self.panier.ajouter("Banane", 1.50, 5)
        self.assertEqual(self.panier.total(), 7.50)


if __name__ == '__main__':
    unittest.main()
