# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : pytest-mock - la fixture `mocker`, wrapper de unittest.mock
#                 avec restauration automatique (sans 'with' ni decorateur).
#                 Illustre patch (return_value, side_effect), les assertions
#                 d'appel, et spy (espionner sans empecher l'execution reelle).
#   Fichier source : 02-mocking-et-fixtures.md
#   Necessite : pip install pytest-mock
#   Execution : pytest 02_15_pytest_mock.py -v -o "addopts="
# ============================================================================

import sys


# ---- Code applicatif (normalement dans un module separe) -------------------

def obtenir_taux_change():
    """Simule un appel reseau couteux (interdit pendant les tests)."""
    raise RuntimeError("Vrai appel réseau interdit dans les tests")


def convertir_en_euros(montant_usd):
    """Convertit un montant USD en EUR via le taux de change courant."""
    taux = obtenir_taux_change()
    return round(montant_usd * taux, 2)


def additionner(a, b):
    """Addition simple, utilisee pour illustrer mocker.spy()."""
    return a + b


# Le nom de ce fichier commence par un chiffre : il n'est pas importable par
# un chemin texte ("02_15_...obtenir_taux_change"). On passe donc l'OBJET
# module a patch.object. Dans un vrai projet, on ecrirait simplement :
#     mocker.patch("banque.obtenir_taux_change", return_value=0.90)
_module = sys.modules[__name__]


# ---- Tests utilisant la fixture `mocker` (fournie par pytest-mock) ----------

def test_patch_return_value(mocker):
    """patch + return_value : ni 'with' ni decorateur, restaure apres le test."""
    faux_taux = mocker.patch.object(
        _module, "obtenir_taux_change", return_value=0.90
    )
    assert convertir_en_euros(100) == 90.0
    faux_taux.assert_called_once()


def test_patch_side_effect(mocker):
    """side_effect : une valeur differente a chaque appel successif."""
    mocker.patch.object(
        _module, "obtenir_taux_change", side_effect=[0.90, 0.80]
    )
    assert convertir_en_euros(100) == 90.0   # 1er appel -> taux 0.90
    assert convertir_en_euros(100) == 80.0   # 2e appel  -> taux 0.80


def test_spy(mocker):
    """spy : on espionne `additionner` SANS empecher son execution reelle."""
    espion = mocker.spy(_module, "additionner")
    resultat = additionner(2, 3)
    assert resultat == 5                     # la vraie fonction a bien tourne
    espion.assert_called_once_with(2, 3)
