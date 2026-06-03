# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Marqueurs pytest pour controler l'execution des tests
#                 (skip, skipif, xfail, xpass)
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
#   Execution : pytest 01_05_skip_xfail_pytest.py -v -o "addopts="
# ============================================================================

import sys

import pytest


def fonction_existante():
    """Fonction de demonstration."""
    return 42


@pytest.mark.skip(reason="fonctionnalite pas encore implementee")
def test_a_venir():
    # Jamais execute : le corps peut meme appeler du code inexistant.
    assert fonction_pas_encore_ecrite() == 0  # noqa: F821


@pytest.mark.skipif(sys.version_info < (3, 10), reason="reserve a Python 3.10+")
def test_reserve_aux_versions_recentes():
    # 'int | str' (operateur | sur les types) est une fonctionnalite 3.10+.
    union_type = int | str
    assert isinstance(5, union_type)


@pytest.mark.xfail(reason="bug connu, correctif en cours")
def test_bug_connu():
    # On s'attend a un echec : marque 'xfail' (et non une erreur).
    assert fonction_existante() == 0


@pytest.mark.xfail(reason="devrait deja etre corrige")
def test_deja_corrige():
    # Reussit malgre xfail : marque 'xpass' (signal a verifier).
    assert fonction_existante() == 42


def test_normal():
    """Test classique, sans marqueur."""
    assert fonction_existante() == 42
