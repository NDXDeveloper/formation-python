# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Tests mocking SMTP - mocker smtplib.SMTP pour tester
#                 envoi d'email et notification d'inscription
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import Mock, patch, MagicMock
from notification import ServiceNotification


@pytest.fixture
def service():
    """Fixture qui cree un service de notification."""
    return ServiceNotification("smtp.example.com")


def test_envoyer_email(service):
    """Teste l'envoi d'un email."""
    with patch('notification.smtplib.SMTP') as mock_smtp:
        mock_connexion = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_connexion

        service.envoyer_email(
            "user@example.com",
            "Test",
            "Ceci est un test"
        )

        mock_smtp.assert_called_once_with("smtp.example.com", 587)
        assert mock_connexion.send_message.called


def test_notifier_inscription(service):
    """Teste la notification d'inscription."""
    utilisateur = {
        "nom": "Alice",
        "email": "alice@example.com"
    }

    with patch.object(service, 'envoyer_email') as mock_envoyer:
        service.notifier_inscription(utilisateur)

        mock_envoyer.assert_called_once()

        args, kwargs = mock_envoyer.call_args
        assert args[0] == "alice@example.com"  # destinataire
        assert "Bienvenue" in args[1]  # sujet
        assert "Alice" in args[2]  # corps
