# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module utilisateurs_db - BaseDeDonnees et ServiceUtilisateur
#                 (utilise par les tests de mocking base de donnees)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================


class BaseDeDonnees:
    """Simule une base de donnees."""

    def __init__(self):
        self.connexion = None

    def se_connecter(self):
        """Se connecte a la base de donnees."""
        self.connexion = "connexion_active"

    def obtenir_utilisateur(self, user_id):
        """Recupere un utilisateur."""
        pass

    def sauvegarder_utilisateur(self, utilisateur):
        """Sauvegarde un utilisateur."""
        pass


class ServiceUtilisateur:
    """Service pour gerer les utilisateurs."""

    def __init__(self, base_de_donnees):
        self.db = base_de_donnees

    def creer_utilisateur(self, nom, email):
        """Cree un nouvel utilisateur."""
        utilisateur = {
            "nom": nom,
            "email": email,
            "actif": True
        }
        self.db.sauvegarder_utilisateur(utilisateur)
        return utilisateur

    def obtenir_profil(self, user_id):
        """Obtient le profil d'un utilisateur."""
        utilisateur = self.db.obtenir_utilisateur(user_id)
        if not utilisateur:
            raise ValueError("Utilisateur introuvable")
        return utilisateur
