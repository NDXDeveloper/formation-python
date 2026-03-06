# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Module utilisateur - classe Utilisateur avec activation,
#                 desactivation, changement d'email (utilisee par les tests)
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

class Utilisateur:
    """Represente un utilisateur."""

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.actif = True

    def desactiver(self):
        """Desactive l'utilisateur."""
        self.actif = False

    def activer(self):
        """Active l'utilisateur."""
        self.actif = True

    def changer_email(self, nouvel_email):
        """Change l'email de l'utilisateur."""
        if "@" not in nouvel_email:
            raise ValueError("Email invalide")
        self.email = nouvel_email

    def __str__(self):
        statut = "actif" if self.actif else "inactif"
        return f"{self.nom} ({self.email}) - {statut}"
