# ============================================================================
#   conftest.py : fixtures partagees, decouvertes automatiquement par pytest
#                 pour tous les tests de ce dossier (sans import).
# ============================================================================

import pytest

from compte import Compte


@pytest.fixture
def compte():
    """Fixture partagee : disponible dans tous les tests du dossier."""
    return Compte("Alice", solde=1000)
