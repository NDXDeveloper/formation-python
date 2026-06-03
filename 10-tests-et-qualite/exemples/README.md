# Chapitre 10 - Tests et qualité du code : Exemples

Ce dossier contient les exemples exécutables du chapitre 10, numérotés selon la section du cours (`01_*` → 10.1, `02_*` → 10.2, … `06_*` → 10.6). Chaque fichier reprend un exemple du `.md` de la section correspondante.

**Exécution** : selon le fichier, on utilise `unittest`, `pytest` ou l'exécution directe `python3` (voir la commande dans chaque tableau). Les tests `pytest` ajoutent `-o "addopts="` pour ignorer une éventuelle configuration globale du dépôt.

> Les sorties annoncées (nombres de tests, pourcentages de couverture) ont été vérifiées avec pytest 9, coverage 7 et mypy sur Python 3.12.

## Modules source (utilisés par les tests)

| Fichier | Description | Section |
|---------|-------------|---------|
| `calculatrice.py` | Fonctions additionner, soustraire, diviser | 10.1 |
| `utilisateur.py` | Classe Utilisateur (nom, email, actif) | 10.1 |
| `panier.py` | Classe Panier d'achat (ajouter, total, vider) | 10.1 |
| `meteo.py` | Obtenir température et recommander vêtements (API) | 10.2 |
| `utilisateurs_db.py` | BaseDeDonnees et ServiceUtilisateur | 10.2 |
| `evenements.py` | Classe Evenement avec gestion du temps | 10.2 |
| `config.py` | Classe Configuration (chargement JSON) | 10.2 |
| `notification.py` | ServiceNotification (envoi email SMTP) | 10.2 |
| `paiement.py` | ServicePaiement (API + base de données) | 10.2 |

---

## Section 10.1 : Tests unitaires avec unittest et pytest

Source : `01-tests-unitaires-unittest-pytest.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `01_01_test_calculatrice_unittest.py` | Tests unittest pour la calculatrice (addition, soustraction, division, division par zéro) | `python3 -m unittest 01_01_test_calculatrice_unittest -v` | 4 tests OK |
| `01_02_test_assertions_unittest.py` | Assertions unittest (assertEqual, assertNotEqual, assertTrue, assertIsNone, assertIn, assertGreater, assertAlmostEqual, setUp/tearDown) | `python3 -m unittest 01_02_test_assertions_unittest -v` | 9 tests OK |
| `01_03_test_utilisateur_unittest.py` | Tests unittest pour Utilisateur (création, activation, désactivation, changement d'email, représentation) | `python3 -m unittest 01_03_test_utilisateur_unittest -v` | 6 tests OK |
| `01_04_test_panier_unittest.py` | Tests unittest pour Panier (panier vide, ajout, total, prix négatif, quantité zéro, vidage, totaux paramétrés) | `python3 -m unittest 01_04_test_panier_unittest -v` | 9 tests OK |
| `01_05_skip_xfail_pytest.py` | Marqueurs pytest pour contrôler l'exécution : `skip`, `skipif`, `xfail` (et `xpass`) | `pytest 01_05_skip_xfail_pytest.py -v -o "addopts="` | 2 passed, 1 skipped, 1 xfailed, 1 xpassed |

---

## Section 10.2 : Mocking et fixtures

Source : `02-mocking-et-fixtures.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `02_01_fixtures_pytest.py` | Fixtures pytest (basique, objet Compte, yield/teardown, scope, paramétrées, dépendantes) | `pytest 02_01_fixtures_pytest.py -v -o "addopts="` | 12 tests OK |
| `02_02_fixtures_unittest.py` | Fixtures unittest (setUp/tearDown, setUpClass/tearDownClass) | `python3 -m unittest 02_02_fixtures_unittest -v` | 4 tests OK |
| `02_03_mock_bases.py` | Mock : bases (création, return_value, side_effect, exceptions) | `python3 02_03_mock_bases.py` | Affichage des appels mock, valeurs successives, exception capturée |
| `02_04_magicmock.py` | MagicMock (\_\_len\_\_, \_\_iter\_\_, \_\_eq\_\_, simulation de BDD) | `python3 02_04_magicmock.py` | len=5, itération 1 2 3, eq=True, query=[{id:1}], len=10 |
| `02_05_mock_assertions.py` | Assertions sur mocks (called, call_count, assert_called_with, assert_has_calls, spec) | `python3 02_05_mock_assertions.py` | Vérifications OK, spec AttributeError |
| `02_06_patch.py` | Patch (décorateur, context manager, patch.object, multi-patch) | `python3 02_06_patch.py` | Démonstrations de patch avec restauration |
| `02_07_test_meteo.py` | Tests mocking API météo (requests.get mocké) | `pytest 02_07_test_meteo.py -v -o "addopts="` | 5 tests OK |
| `02_08_test_utilisateurs_db.py` | Tests mocking base de données (Mock spec, créer/obtenir utilisateur) | `pytest 02_08_test_utilisateurs_db.py -v -o "addopts="` | 3 tests OK |
| `02_09_test_evenements.py` | Tests mocking du temps (patch datetime.now) | `pytest 02_09_test_evenements.py -v -o "addopts="` | 3 tests OK |
| `02_10_test_config.py` | Tests mocking fichiers (mock_open, configuration JSON) | `pytest 02_10_test_config.py -v -o "addopts="` | 3 tests OK |
| `02_11_test_notification.py` | Tests mocking SMTP (envoi email, notification d'inscription) | `pytest 02_11_test_notification.py -v -o "addopts="` | 2 tests OK |
| `02_12_test_paiement.py` | Cas pratique complet : service de paiement (API + DB + datetime mockés) | `pytest 02_12_test_paiement.py -v -o "addopts="` | 5 tests OK |
| `02_13_monkeypatch.py` | `monkeypatch` (setenv, delenv, setattr, setitem) avec restauration automatique | `pytest 02_13_monkeypatch.py -v -o "addopts="` | 4 tests OK |
| `02_14_conftest_demo/` | Partage de fixtures via `conftest.py` (sous-dossier : `compte.py`, `conftest.py`, `test_depot.py`) | `cd 02_14_conftest_demo && pytest -v -o "addopts="` | 2 tests OK (fixture trouvée sans import) |

---

## Section 10.3 : Couverture de code

Source : `03-couverture-de-code.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `03_01_calculatrice_cov.py` | Calculatrice étendue (additionner, soustraire, multiplier, diviser, calculer_moyenne) | Module source | - |
| `03_02_test_calculatrice_cov.py` | Tests complets pour 100% de couverture (7 tests) | `pytest 03_02_test_calculatrice_cov.py --cov=03_01_calculatrice_cov --cov-branch -o "addopts="` | 7 tests OK, 100% de couverture |
| `03_03_validation.py` | Module validation (valider_note, calculer_mention) avec branches | Module source | - |
| `03_04_test_validation.py` | Tests complets avec toutes les branches (9 tests) | `pytest 03_04_test_validation.py --cov=03_03_validation --cov-branch -o "addopts="` | 9 tests OK, 100% de couverture des branches |
| `03_05_utilisateur_cov.py` | Utilisateur étendu avec rôles + GestionnaireUtilisateurs | Module source | - |
| `03_06_test_utilisateur_cov.py` | Tests complets (22 tests, toutes méthodes et branches) | `pytest 03_06_test_utilisateur_cov.py --cov=03_05_utilisateur_cov --cov-branch -o "addopts="` | 22 tests OK, 100% de couverture |

---

## Section 10.4 : Documentation avec docstrings

Source : `04-documentation-docstrings.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `04_01_docstrings_bases.py` | Bases des docstrings (\_\_doc\_\_, help(), inspect.signature) | `python3 04_01_docstrings_bases.py` | Docstrings, signatures, help() |
| `04_02_styles_docstrings.py` | 3 styles de docstrings (Google, NumPy, Sphinx) avec exemples fonctionnels | `python3 04_02_styles_docstrings.py` | diviser, calculer_statistiques, creer_utilisateur |
| `04_03_fonctions_documentees.py` | Fonctions documentées (est_pair, calculer_prix_total, analyser_texte, formater_prix) | `python3 04_03_fonctions_documentees.py` | Résultats de chaque fonction |
| `04_04_classes_documentees.py` | Classes documentées (CompteBancaire, Vehicule, Voiture avec héritage) | `python3 04_04_classes_documentees.py` | Dépôt/retrait, descriptions des véhicules |
| `04_05_api_taches.py` | Cas pratique complet : API Tache + GestionnaireTaches (doctests inclus) | `python3 04_05_api_taches.py` | CRUD tâches, priorités, compteurs |

> Astuce : les docstrings de `04_05_api_taches.py` contiennent des exemples `>>>`. On peut les exécuter comme des tests avec `python3 -m doctest 04_05_api_taches.py -v`.

---

## Section 10.5 : PEP 8 et outils de linting

Source : `05-pep8-et-linting.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `05_01_pep8_regles.py` | Démonstration des règles PEP 8 (indentation, nommage, espaces, comparaisons) | `python3 05_01_pep8_regles.py` | Exemples de bon style PEP 8 |
| `05_02_refactorisation.py` | Cas pratique de refactorisation (code corrigé selon PEP 8 : sans import inutilisé, sans `else` après `return`) | `python3 05_02_refactorisation.py` | Fonctions et classes refactorisées |

> `05_02_refactorisation.py` est volontairement « propre » : `flake8` et `ruff check` ne signalent aucune erreur.

---

## Section 10.6 : Validation de types avec mypy

Source : `06-validation-types-mypy.md`

| Fichier | Description | Exécution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `06_01_types_bases.py` | Types de base (typage dynamique, type hints, variables annotées) | `python3 06_01_types_bases.py` | Types, fonctions typées, TypeError |
| `06_02_types_complexes.py` | Types complexes (list, dict, Optional, Union, Callable, Iterable, Sequence, Mapping) | `python3 06_02_types_complexes.py` | Collections typées, fonctions génériques |
| `06_03_classes_typees.py` | Classes typées (annotations, TypeAlias, Generic[T]) **et syntaxe PEP 695** (`type`, `class C[T]`, 3.12+) | `python3 06_03_classes_typees.py` | Utilisateur, Boite générique, variante PEP 695 |
| `06_04_types_avances.py` | Types avancés (Literal, TypedDict, Final, Protocol) | `python3 06_04_types_avances.py` | Démonstrations de chaque type avancé |
| `06_05_api_taches_typee.py` | Cas pratique complet : API tâches avec types (Enum, TypedDict) | `python3 06_05_api_taches_typee.py` | CRUD tâches typées, statistiques |

> Les fichiers `06_02` à `06_05` passent `mypy` sans erreur. `06_01_types_bases.py` contient **volontairement** une fonction non typée (`additionner_dynamique`) pour illustrer le typage dynamique : `mypy` la signale sous `disallow_untyped_defs` (configuration du dépôt), ce qui est attendu.

---

## Exécution groupée

```bash
# Tous les tests des sections 01 à 03 en une fois.
# (pytest collecte aussi les classes unittest ; `unittest discover` ne peut
#  pas importer ces fichiers à cause de leur préfixe numérique — utiliser
#  alors la commande explicite par fichier indiquée dans les tableaux.)
pytest 01_*.py 02_*.py 03_*.py -v -o "addopts="

# Démonstration conftest.py (sous-dossier isolé)
(cd 02_14_conftest_demo && pytest -v -o "addopts=")

# Démos en exécution directe (sections 02 à 06)
for f in 02_03*.py 02_04*.py 02_05*.py 02_06*.py 04_*.py 05_*.py 06_*.py; do
    echo "--- $f ---"
    python3 "$f"
    echo
done

# Couverture complète (sections 03)
pytest 03_02_test_calculatrice_cov.py 03_04_test_validation.py 03_06_test_utilisateur_cov.py \
    --cov=03_01_calculatrice_cov --cov=03_03_validation --cov=03_05_utilisateur_cov \
    --cov-branch --cov-report=term-missing -o "addopts="

# Vérification de types (section 06)
mypy 06_01_types_bases.py 06_02_types_complexes.py 06_03_classes_typees.py \
    06_04_types_avances.py 06_05_api_taches_typee.py
```
