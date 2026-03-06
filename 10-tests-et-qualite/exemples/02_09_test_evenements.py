# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Tests mocking du temps - patch datetime.now() pour
#                 tester est_recent et age_en_jours
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
from unittest.mock import patch
from datetime import datetime, timedelta
from evenements import Evenement


def test_evenement_recent():
    """Teste qu'un evenement cree aujourd'hui est recent."""
    date_fixe = datetime(2024, 1, 15, 10, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        mock_datetime.now.return_value = date_fixe

        evenement = Evenement("Test")

        assert evenement.est_recent()


def test_evenement_ancien():
    """Teste qu'un evenement vieux de 10 jours n'est pas recent."""
    date_creation = datetime(2024, 1, 1, 10, 0, 0)
    date_maintenant = datetime(2024, 1, 15, 10, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        mock_datetime.now.return_value = date_creation
        evenement = Evenement("Test Ancien")

        mock_datetime.now.return_value = date_maintenant

        assert not evenement.est_recent(jours=7)
        assert evenement.age_en_jours() == 14


def test_age_evenement():
    """Teste le calcul de l'age d'un evenement."""
    date_creation = datetime(2024, 1, 1, 12, 0, 0)
    date_maintenant = datetime(2024, 1, 10, 12, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        mock_datetime.now.return_value = date_creation
        evenement = Evenement("Test Age")

        mock_datetime.now.return_value = date_maintenant
        assert evenement.age_en_jours() == 9
