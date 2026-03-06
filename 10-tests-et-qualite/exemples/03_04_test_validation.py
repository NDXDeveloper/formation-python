# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Tests complets pour validation - couvre toutes les branches
#                 (note invalide, reussi, echoue, toutes les mentions)
#   Fichier source : 03-couverture-de-code.md
# ============================================================================

import importlib
_mod = importlib.import_module("03_03_validation")
valider_note = _mod.valider_note
calculer_mention = _mod.calculer_mention


# Tests pour valider_note
def test_valider_note_reussi():
    assert valider_note(15) == "Réussi"
    assert valider_note(10) == "Réussi"


def test_valider_note_echoue():
    assert valider_note(5) == "Échoué"
    assert valider_note(9) == "Échoué"


def test_valider_note_invalide_negative():
    assert valider_note(-5) == "Note invalide"


def test_valider_note_invalide_superieure():
    assert valider_note(25) == "Note invalide"


# Tests pour calculer_mention
def test_mention_echec():
    assert calculer_mention(8) == "Échec"


def test_mention_passable():
    assert calculer_mention(11) == "Passable"


def test_mention_assez_bien():
    assert calculer_mention(13) == "Assez bien"


def test_mention_bien():
    assert calculer_mention(15) == "Bien"


def test_mention_tres_bien():
    assert calculer_mention(18) == "Très bien"
