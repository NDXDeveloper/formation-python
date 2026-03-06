# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Application pratique - GestionnaireUtilisateurs avec
#                 logging, niveaux adaptés, logger nommé (__name__)
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
from datetime import datetime

class GestionnaireUtilisateurs:
    """Gestionnaire d'utilisateurs avec logging"""

    def __init__(self):
        # Créer un logger pour cette classe
        self.logger = logging.getLogger(__name__)
        self.utilisateurs = {}

    def ajouter_utilisateur(self, username, email):
        """Ajoute un nouvel utilisateur"""
        self.logger.info(f"Tentative d'ajout de l'utilisateur: {username}")

        if username in self.utilisateurs:
            self.logger.warning(f"L'utilisateur {username} existe déjà")
            return False

        if '@' not in email:
            self.logger.error(f"Email invalide pour {username}: {email}")
            return False

        self.utilisateurs[username] = {
            'email': email,
            'created_at': datetime.now()
        }

        self.logger.info(f"Utilisateur {username} ajouté avec succès")
        self.logger.debug(f"Détails: {self.utilisateurs[username]}")
        return True

    def supprimer_utilisateur(self, username):
        """Supprime un utilisateur"""
        self.logger.info(f"Tentative de suppression de l'utilisateur: {username}")

        if username not in self.utilisateurs:
            self.logger.error(f"L'utilisateur {username} n'existe pas")
            return False

        del self.utilisateurs[username]
        self.logger.info(f"Utilisateur {username} supprimé")
        return True

    def lister_utilisateurs(self):
        """Liste tous les utilisateurs"""
        self.logger.debug(f"Listage de {len(self.utilisateurs)} utilisateurs")
        return list(self.utilisateurs.keys())


# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Utilisation
gestionnaire = GestionnaireUtilisateurs()

gestionnaire.ajouter_utilisateur("alice", "alice@example.com")
gestionnaire.ajouter_utilisateur("bob", "bob@example.com")
gestionnaire.ajouter_utilisateur("alice", "alice2@example.com")  # Doublon
gestionnaire.ajouter_utilisateur("charlie", "invalide")  # Email invalide
gestionnaire.supprimer_utilisateur("bob")
gestionnaire.supprimer_utilisateur("david")  # N'existe pas

print("\nUtilisateurs:", gestionnaire.lister_utilisateurs())
