# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Cas pratique complet - service de paiement avec mocking
#                 API, base de donnees et datetime
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from paiement import ServicePaiement


@pytest.fixture
def mock_db():
    """Mock de la base de donnees."""
    db = Mock()
    db.obtenir_utilisateur.return_value = {
        "id": 1,
        "nom": "Alice",
        "email": "alice@test.com"
    }
    return db


@pytest.fixture
def service_paiement(mock_db):
    """Service de paiement avec dependances mockees."""
    return ServicePaiement(
        api_url="https://api.paiement.test",
        api_key="test_key_123",
        base_de_donnees=mock_db
    )


def test_traiter_paiement_reussi(service_paiement, mock_db):
    """Teste un paiement reussi."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"transaction_id": "txn_123"}

    with patch('paiement.requests.post', return_value=mock_response):
        date_fixe = datetime(2024, 1, 15, 10, 0, 0)
        with patch('paiement.datetime') as mock_datetime:
            mock_datetime.now.return_value = date_fixe

            transaction = service_paiement.traiter_paiement(
                utilisateur_id=1,
                montant=50.00
            )

    assert transaction["utilisateur_id"] == 1
    assert transaction["montant"] == 50.00
    assert transaction["statut"] == "réussi"
    assert transaction["transaction_id"] == "txn_123"
    assert transaction["date"] == date_fixe

    mock_db.sauvegarder_transaction.assert_called_once()


def test_traiter_paiement_montant_negatif(service_paiement):
    """Teste qu'un montant negatif est rejete."""
    with pytest.raises(ValueError, match="positif"):
        service_paiement.traiter_paiement(1, -10)


def test_traiter_paiement_utilisateur_inexistant(service_paiement, mock_db):
    """Teste avec un utilisateur inexistant."""
    mock_db.obtenir_utilisateur.return_value = None

    with pytest.raises(ValueError, match="introuvable"):
        service_paiement.traiter_paiement(999, 50.00)


def test_traiter_paiement_echec_api(service_paiement, mock_db):
    """Teste l'echec de l'API de paiement."""
    mock_response = Mock()
    mock_response.status_code = 400

    with patch('paiement.requests.post', return_value=mock_response):
        with pytest.raises(Exception, match="Échec"):
            service_paiement.traiter_paiement(1, 50.00)

    mock_db.sauvegarder_transaction.assert_not_called()


def test_appel_api_avec_bons_parametres(service_paiement, mock_db):
    """Verifie que l'API est appelee avec les bons parametres."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"transaction_id": "txn_456"}

    with patch('paiement.requests.post', return_value=mock_response) as mock_post:
        service_paiement.traiter_paiement(1, 100.00)

        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args

        assert args[0] == "https://api.paiement.test/charge"
        assert kwargs["json"]["user_id"] == 1
        assert kwargs["json"]["amount"] == 100.00
        assert kwargs["json"]["currency"] == "EUR"
        assert "Authorization" in kwargs["headers"]
        assert "test_key_123" in kwargs["headers"]["Authorization"]
