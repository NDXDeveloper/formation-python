# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module config - classe Configuration avec chargement JSON
#                 (utilise par les tests de mocking fichiers avec mock_open)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import json


class Configuration:
    """Gere la configuration de l'application."""

    def __init__(self, fichier_config):
        self.fichier_config = fichier_config
        self.config = {}

    def charger(self):
        """Charge la configuration depuis un fichier."""
        with open(self.fichier_config, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def obtenir(self, cle, defaut=None):
        """Obtient une valeur de configuration."""
        return self.config.get(cle, defaut)

    def est_mode_debug(self):
        """Verifie si le mode debug est active."""
        return self.config.get('debug', False)
