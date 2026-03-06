# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Tests mocking base de donnees - Mock(spec=BaseDeDonnees),
#                 creer utilisateur, obtenir profil existant/inexistant
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import Mock
from utilisateurs_db import BaseDeDonnees, ServiceUtilisateur


@pytest.fixture
def mock_db():
    """Fixture qui cree un mock de base de donnees."""
    return Mock(spec=BaseDeDonnees)


@pytest.fixture
def service(mock_db):
    """Fixture qui cree un service avec une base mockee."""
    return ServiceUtilisateur(mock_db)


def test_creer_utilisateur(service, mock_db):
    """Teste la creation d'un utilisateur."""
    utilisateur = service.creer_utilisateur("Alice", "alice@test.com")

    assert utilisateur["nom"] == "Alice"
    assert utilisateur["email"] == "alice@test.com"
    assert utilisateur["actif"] is True

    mock_db.sauvegarder_utilisateur.assert_called_once()

    args = mock_db.sauvegarder_utilisateur.call_args[0][0]
    assert args["nom"] == "Alice"


def test_obtenir_profil_existant(service, mock_db):
    """Teste l'obtention d'un profil existant."""
    utilisateur_mock = {"id": 1, "nom": "Bob", "email": "bob@test.com"}
    mock_db.obtenir_utilisateur.return_value = utilisateur_mock

    profil = service.obtenir_profil(1)

    assert profil["nom"] == "Bob"
    mock_db.obtenir_utilisateur.assert_called_once_with(1)


def test_obtenir_profil_inexistant(service, mock_db):
    """Teste l'obtention d'un profil inexistant."""
    mock_db.obtenir_utilisateur.return_value = None

    with pytest.raises(ValueError, match="introuvable"):
        service.obtenir_profil(999)
