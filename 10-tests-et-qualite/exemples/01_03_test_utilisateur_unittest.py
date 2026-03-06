# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Tests unittest pour la classe Utilisateur - creation,
#                 activation/desactivation, changement d'email, __str__
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

import unittest
from utilisateur import Utilisateur


class TestUtilisateur(unittest.TestCase):

    def setUp(self):
        """Cree un utilisateur pour chaque test."""
        self.utilisateur = Utilisateur("Alice", "alice@example.com")

    def test_creation_utilisateur(self):
        """Teste la creation d'un utilisateur."""
        self.assertEqual(self.utilisateur.nom, "Alice")
        self.assertEqual(self.utilisateur.email, "alice@example.com")
        self.assertTrue(self.utilisateur.actif)

    def test_desactiver_utilisateur(self):
        """Teste la desactivation d'un utilisateur."""
        self.utilisateur.desactiver()
        self.assertFalse(self.utilisateur.actif)

    def test_activer_utilisateur(self):
        """Teste l'activation d'un utilisateur."""
        self.utilisateur.desactiver()
        self.utilisateur.activer()
        self.assertTrue(self.utilisateur.actif)

    def test_changer_email_valide(self):
        """Teste le changement d'email avec un email valide."""
        nouvel_email = "alice.nouveau@example.com"
        self.utilisateur.changer_email(nouvel_email)
        self.assertEqual(self.utilisateur.email, nouvel_email)

    def test_changer_email_invalide(self):
        """Teste que changer l'email avec un email invalide leve une exception."""
        with self.assertRaises(ValueError):
            self.utilisateur.changer_email("email_invalide")

    def test_representation_string(self):
        """Teste la representation en chaine de caracteres."""
        resultat = str(self.utilisateur)
        self.assertIn("Alice", resultat)
        self.assertIn("actif", resultat)


if __name__ == '__main__':
    unittest.main()
