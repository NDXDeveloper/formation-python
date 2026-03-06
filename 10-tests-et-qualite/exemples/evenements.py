# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module evenements - classe Evenement avec gestion du temps
#                 (utilise par les tests de mocking du temps)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

from datetime import datetime


class Evenement:
    """Represente un evenement."""

    def __init__(self, nom, date_creation=None):
        self.nom = nom
        self.date_creation = date_creation or datetime.now()

    def est_recent(self, jours=7):
        """Verifie si l'evenement a moins de X jours."""
        maintenant = datetime.now()
        difference = maintenant - self.date_creation
        return difference.days < jours

    def age_en_jours(self):
        """Retourne l'age de l'evenement en jours."""
        maintenant = datetime.now()
        return (maintenant - self.date_creation).days
