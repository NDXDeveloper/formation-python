# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : monkeypatch, la fixture native de pytest pour remplacer
#                 attributs, variables d'environnement et entrees de dict.
#                 Toutes les modifications sont annulees apres chaque test.
#   Fichier source : 02-mocking-et-fixtures.md
#   Execution : pytest 02_13_monkeypatch.py -v -o "addopts="
# ============================================================================

import os


def lire_cle_api():
    """Lit la cle API depuis l'environnement."""
    return os.environ.get("API_KEY", "absente")


PARAMETRES = {"timeout": 30}


def test_setenv(monkeypatch):
    """setenv : definit une variable d'environnement (annulee apres le test)."""
    monkeypatch.setenv("API_KEY", "cle_de_test")
    assert lire_cle_api() == "cle_de_test"


def test_delenv(monkeypatch):
    """delenv : supprime une variable d'environnement."""
    monkeypatch.setenv("API_KEY", "valeur")
    monkeypatch.delenv("API_KEY")
    assert lire_cle_api() == "absente"


def test_setattr(monkeypatch):
    """setattr : remplace un attribut (ici une fonction d'un module)."""
    monkeypatch.setattr(os, "getcwd", lambda: "/chemin/simule")
    assert os.getcwd() == "/chemin/simule"


def test_setitem(monkeypatch):
    """setitem : modifie une entree de dictionnaire (annulee apres le test)."""
    monkeypatch.setitem(PARAMETRES, "timeout", 60)
    assert PARAMETRES["timeout"] == 60
