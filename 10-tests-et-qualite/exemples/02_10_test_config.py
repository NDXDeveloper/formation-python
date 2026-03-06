# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Tests mocking fichiers - mock_open pour tester
#                 chargement de configuration JSON, valeurs par defaut,
#                 mode debug
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import mock_open, patch
import json
from config import Configuration


def test_charger_configuration():
    """Teste le chargement de la configuration."""
    config_data = {
        "debug": True,
        "api_key": "test_key_123",
        "timeout": 30
    }

    mock_file = mock_open(read_data=json.dumps(config_data))

    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()

        assert config.obtenir("debug") is True
        assert config.obtenir("api_key") == "test_key_123"
        assert config.obtenir("timeout") == 30


def test_obtenir_avec_valeur_defaut():
    """Teste l'obtention d'une valeur avec defaut."""
    config_data = {"debug": True}
    mock_file = mock_open(read_data=json.dumps(config_data))

    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()

        assert config.obtenir("debug") is True
        assert config.obtenir("inexistant", "valeur_defaut") == "valeur_defaut"


def test_mode_debug():
    """Teste la verification du mode debug."""
    config_debug = {"debug": True}
    config_prod = {"debug": False}

    # Test avec debug active
    mock_file = mock_open(read_data=json.dumps(config_debug))
    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()
        assert config.est_mode_debug() is True

    # Test avec debug desactive
    mock_file = mock_open(read_data=json.dumps(config_prod))
    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()
        assert config.est_mode_debug() is False
