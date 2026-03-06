# Chapitre 10 - Tests et qualite : Exemples

## Modules source (utilises par les tests)

| Fichier | Description | Section |
|---------|-------------|---------|
| `calculatrice.py` | Fonctions additionner, soustraire, diviser | 10.1 |
| `utilisateur.py` | Classe Utilisateur (nom, email, actif) | 10.1 |
| `panier.py` | Classe Panier d'achat (ajouter, total, vider) | 10.1 |
| `meteo.py` | Obtenir temperature et recommander vetements (API) | 10.2 |
| `utilisateurs_db.py` | BaseDeDonnees et ServiceUtilisateur | 10.2 |
| `evenements.py` | Classe Evenement avec gestion du temps | 10.2 |
| `config.py` | Classe Configuration (chargement JSON) | 10.2 |
| `notification.py` | ServiceNotification (envoi email SMTP) | 10.2 |
| `paiement.py` | ServicePaiement (API + base de donnees) | 10.2 |

---

## Section 10.1 : Tests unitaires avec unittest et pytest

Source : `01-tests-unitaires-unittest-pytest.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `01_01_test_calculatrice_unittest.py` | Tests unittest pour la calculatrice (addition, soustraction, division, division par zero) | `python3 -m unittest 01_01_test_calculatrice_unittest -v` | 4 tests OK |
| `01_02_test_assertions_unittest.py` | Assertions unittest (assertEqual, assertNotEqual, assertTrue, assertIsNone, assertIn, assertGreater, assertAlmostEqual, setUp/tearDown) | `python3 -m unittest 01_02_test_assertions_unittest -v` | 9 tests OK |
| `01_03_test_utilisateur_unittest.py` | Tests unittest pour Utilisateur (creation, activation, desactivation, changement email, representation) | `python3 -m unittest 01_03_test_utilisateur_unittest -v` | 6 tests OK |
| `01_04_test_panier_unittest.py` | Tests unittest pour Panier (panier vide, ajout, total, prix negatif, quantite zero, vidage, totaux parametres) | `python3 -m unittest 01_04_test_panier_unittest -v` | 9 tests OK |

---

## Section 10.2 : Mocking et fixtures

Source : `02-mocking-et-fixtures.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `02_01_fixtures_pytest.py` | Fixtures pytest (basique, objet Compte, yield/teardown, scope, parametrees, dependantes) | `pytest 02_01_fixtures_pytest.py -v -o "addopts="` | 12 tests OK |
| `02_02_fixtures_unittest.py` | Fixtures unittest (setUp/tearDown, setUpClass/tearDownClass) | `python3 -m unittest 02_02_fixtures_unittest -v` | 4 tests OK |
| `02_03_mock_bases.py` | Mock bases (creation, return_value, side_effect, exceptions) | `python3 02_03_mock_bases.py` | Affichage des appels mock, valeurs successives, exception capturee |
| `02_04_magicmock.py` | MagicMock (\_\_len\_\_, \_\_iter\_\_, \_\_eq\_\_, simulation de BDD) | `python3 02_04_magicmock.py` | len=5, iteration 1 2 3, eq=True, query=[{id:1}], len=10 |
| `02_05_mock_assertions.py` | Assertions sur mocks (called, call_count, assert_called_with, assert_has_calls, spec) | `python3 02_05_mock_assertions.py` | Verifications OK, spec AttributeError |
| `02_06_patch.py` | Patch (decorateur, context manager, patch.object, multi-patch) | `python3 02_06_patch.py` | Demonstrations de patch avec restauration |
| `02_07_test_meteo.py` | Tests mocking API meteo (requests.get mocke) | `pytest 02_07_test_meteo.py -v -o "addopts="` | 5 tests OK |
| `02_08_test_utilisateurs_db.py` | Tests mocking base de donnees (Mock spec, creer/obtenir utilisateur) | `pytest 02_08_test_utilisateurs_db.py -v -o "addopts="` | 3 tests OK |
| `02_09_test_evenements.py` | Tests mocking du temps (patch datetime.now) | `pytest 02_09_test_evenements.py -v -o "addopts="` | 3 tests OK |
| `02_10_test_config.py` | Tests mocking fichiers (mock_open, configuration JSON) | `pytest 02_10_test_config.py -v -o "addopts="` | 3 tests OK |
| `02_11_test_notification.py` | Tests mocking SMTP (envoi email, notification inscription) | `pytest 02_11_test_notification.py -v -o "addopts="` | 2 tests OK |
| `02_12_test_paiement.py` | Cas pratique complet : service de paiement (API + DB + datetime mockes) | `pytest 02_12_test_paiement.py -v -o "addopts="` | 5 tests OK |

---

## Section 10.3 : Couverture de code

Source : `03-couverture-de-code.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `03_01_calculatrice_cov.py` | Calculatrice etendue (additionner, soustraire, multiplier, diviser, calculer_moyenne) | Module source | - |
| `03_02_test_calculatrice_cov.py` | Tests complets pour 100% de couverture (7 tests) | `pytest 03_02_test_calculatrice_cov.py --cov=03_01_calculatrice_cov --cov-branch -o "addopts="` | 7 tests OK, 100% couverture |
| `03_03_validation.py` | Module validation (valider_note, calculer_mention) avec branches | Module source | - |
| `03_04_test_validation.py` | Tests complets avec toutes les branches (9 tests) | `pytest 03_04_test_validation.py --cov=03_03_validation --cov-branch -o "addopts="` | 9 tests OK, 100% couverture branches |
| `03_05_utilisateur_cov.py` | Utilisateur etendu avec roles + GestionnaireUtilisateurs | Module source | - |
| `03_06_test_utilisateur_cov.py` | Tests complets (22 tests, toutes methodes et branches) | `pytest 03_06_test_utilisateur_cov.py --cov=03_05_utilisateur_cov --cov-branch -o "addopts="` | 22 tests OK, 100% couverture |

---

## Section 10.4 : Documentation avec docstrings

Source : `04-documentation-docstrings.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `04_01_docstrings_bases.py` | Bases des docstrings (\_\_doc\_\_, help(), inspect.signature) | `python3 04_01_docstrings_bases.py` | Docstrings, signatures, help() |
| `04_02_styles_docstrings.py` | 3 styles de docstrings (Google, NumPy, Sphinx) avec exemples fonctionnels | `python3 04_02_styles_docstrings.py` | diviser, calculer_statistiques, creer_utilisateur |
| `04_03_fonctions_documentees.py` | Fonctions documentees (est_pair, calculer_prix_total, analyser_texte, formater_prix) | `python3 04_03_fonctions_documentees.py` | Resultats de chaque fonction |
| `04_04_classes_documentees.py` | Classes documentees (CompteBancaire, Vehicule, Voiture avec heritage) | `python3 04_04_classes_documentees.py` | Depot/retrait, descriptions vehicules |
| `04_05_api_taches.py` | Cas pratique complet : API Tache + GestionnaireTaches | `python3 04_05_api_taches.py` | CRUD taches, priorites, compteurs |

---

## Section 10.5 : PEP 8 et outils de linting

Source : `05-pep8-et-linting.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `05_01_pep8_regles.py` | Demonstration des regles PEP 8 (indentation, nommage, espaces, comparaisons) | `python3 05_01_pep8_regles.py` | Exemples de bon style PEP 8 |
| `05_02_refactorisation.py` | Cas pratique de refactorisation (code corrige selon PEP 8) | `python3 05_02_refactorisation.py` | Fonctions et classes refactorisees |

---

## Section 10.6 : Validation de types avec mypy

Source : `06-validation-types-mypy.md`

| Fichier | Description | Execution | Sortie attendue |
|---------|-------------|-----------|-----------------|
| `06_01_types_bases.py` | Types de base (typage dynamique, type hints, variables annotees) | `python3 06_01_types_bases.py` | Types, fonctions typees, TypeError |
| `06_02_types_complexes.py` | Types complexes (list, dict, Optional, Union, Callable, Iterable, Sequence, Mapping) | `python3 06_02_types_complexes.py` | Collections typees, fonctions generiques |
| `06_03_classes_typees.py` | Classes typees (annotations, TypeAlias, Generic[T]) | `python3 06_03_classes_typees.py` | Utilisateur, Boite generique |
| `06_04_types_avances.py` | Types avances (Literal, TypedDict, Final, Protocol) | `python3 06_04_types_avances.py` | Demonstrations de chaque type avance |
| `06_05_api_taches_typee.py` | Cas pratique complet : API taches avec types (Enum, TypedDict) | `python3 06_05_api_taches_typee.py` | CRUD taches typees, statistiques |

---

## Execution

```bash
# Executer tous les tests unittest (section 01)
python3 -m unittest discover -p "01_*" -v

# Executer tous les tests pytest (sections 02-03)
pytest 02_*.py 03_*.py -v -o "addopts="

# Executer les demos (sections 02-06)
for f in 02_03*.py 02_04*.py 02_05*.py 02_06*.py 04_*.py 05_*.py 06_*.py; do
    echo "--- $f ---"
    python3 "$f"
    echo
done

# Couverture complete
pytest 03_02_test_calculatrice_cov.py 03_04_test_validation.py 03_06_test_utilisateur_cov.py \
    --cov=03_01_calculatrice_cov --cov=03_03_validation --cov=03_05_utilisateur_cov \
    --cov-branch --cov-report=term-missing -o "addopts="
```
