# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Tests mocking API - mocker requests.get pour tester
#                 obtenir_temperature et recommander_vetements
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import Mock, patch
from meteo import obtenir_temperature, recommander_vetements


def test_obtenir_temperature():
    """Teste l'obtention de la temperature avec un mock."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 25}

    with patch('meteo.requests.get', return_value=mock_response):
        temperature = obtenir_temperature("Paris")
        assert temperature == 25


def test_obtenir_temperature_erreur_api():
    """Teste la gestion d'erreur API."""
    mock_response = Mock()
    mock_response.status_code = 404

    with patch('meteo.requests.get', return_value=mock_response):
        with pytest.raises(Exception, match="Erreur API"):
            obtenir_temperature("VilleInconnue")


def test_recommander_vetements_froid():
    """Teste la recommandation par temps froid."""
    with patch('meteo.obtenir_temperature', return_value=5):
        recommandation = recommander_vetements("Oslo")
        assert recommandation == "Manteau et écharpe"


def test_recommander_vetements_tempere():
    """Teste la recommandation par temps tempere."""
    with patch('meteo.obtenir_temperature', return_value=15):
        recommandation = recommander_vetements("Paris")
        assert recommandation == "Pull léger"


def test_recommander_vetements_chaud():
    """Teste la recommandation par temps chaud."""
    with patch('meteo.obtenir_temperature', return_value=28):
        recommandation = recommander_vetements("Marseille")
        assert recommandation == "T-shirt"
