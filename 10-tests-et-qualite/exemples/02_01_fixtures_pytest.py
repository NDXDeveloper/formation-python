# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Fixtures pytest - fixture basique, fixture objet (Compte),
#                 fixture avec setup/teardown (yield), portee (scope),
#                 fixtures parametrees, fixtures dependantes
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import pytest
import tempfile
import os


# --- Fixture basique ---

@pytest.fixture
def nombre():
    """Fixture simple qui retourne un nombre."""
    return 42


def test_avec_fixture(nombre):
    """Test qui utilise la fixture."""
    assert nombre == 42
    assert nombre * 2 == 84


# --- Fixture qui cree un objet ---

class Compte:
    """Represente un compte bancaire."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Depose de l'argent."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant

    def retirer(self, montant):
        """Retire de l'argent."""
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant


@pytest.fixture
def compte():
    """Fixture qui cree un compte de test."""
    return Compte("Alice", solde=1000)


def test_deposer(compte):
    """Teste le depot d'argent."""
    compte.deposer(500)
    assert compte.solde == 1500


def test_retirer(compte):
    """Teste le retrait d'argent."""
    compte.retirer(300)
    assert compte.solde == 700


def test_retrait_impossible(compte):
    """Teste qu'on ne peut pas retirer plus que le solde."""
    with pytest.raises(ValueError, match="insuffisant"):
        compte.retirer(2000)


# --- Fixture avec setup et teardown (yield) ---

@pytest.fixture
def fichier_temp():
    """Cree un fichier temporaire et le supprime apres."""
    fd, chemin = tempfile.mkstemp(suffix=".txt")
    os.write(fd, b"Contenu initial")
    os.close(fd)
    print(f"\n[Setup] Fichier cree : {chemin}")

    yield chemin

    if os.path.exists(chemin):
        os.remove(chemin)
        print(f"[Teardown] Fichier supprime : {chemin}")


def test_lecture_fichier(fichier_temp):
    """Teste la lecture du fichier temporaire."""
    with open(fichier_temp, "r", encoding="utf-8") as f:
        contenu = f.read()
    assert contenu == "Contenu initial"


def test_modification_fichier(fichier_temp):
    """Teste la modification du fichier temporaire."""
    with open(fichier_temp, "w", encoding="utf-8") as f:
        f.write("Nouveau contenu")

    with open(fichier_temp, "r", encoding="utf-8") as f:
        contenu = f.read()
    assert contenu == "Nouveau contenu"


# --- Portee des fixtures (scope) ---

@pytest.fixture(scope="function")
def fixture_fonction():
    """Creee pour chaque test."""
    print("\nCreation fixture fonction")
    return {"data": "fonction"}


@pytest.fixture(scope="module")
def fixture_module():
    """Creee une fois par fichier de test."""
    print("\nCreation fixture module")
    return {"data": "module"}


def test_scope_1(fixture_fonction, fixture_module):
    assert fixture_fonction["data"] == "fonction"
    assert fixture_module["data"] == "module"


def test_scope_2(fixture_fonction, fixture_module):
    # fixture_fonction est recreee, fixture_module est reutilisee
    assert fixture_fonction["data"] == "fonction"
    assert fixture_module["data"] == "module"


# --- Fixtures parametrees ---

@pytest.fixture(params=[
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
])
def utilisateur_param(request):
    """Fixture parametree qui cree plusieurs utilisateurs."""
    return request.param


def test_utilisateur_valide(utilisateur_param):
    """Ce test sera execute 3 fois, une fois par utilisateur."""
    assert "nom" in utilisateur_param
    assert "age" in utilisateur_param
    assert utilisateur_param["age"] > 0


# --- Fixtures qui utilisent d'autres fixtures ---

@pytest.fixture
def base_de_donnees():
    """Simule une connexion a la base de donnees."""
    print("\nConnexion a la base de donnees")
    db = {"users": [], "posts": []}
    yield db
    print("\nDeconnexion de la base de donnees")


@pytest.fixture
def utilisateur_dans_db(base_de_donnees):
    """Cree un utilisateur dans la base de donnees."""
    utilisateur = {"id": 1, "nom": "Alice"}
    base_de_donnees["users"].append(utilisateur)
    return utilisateur


def test_utilisateur_existe(utilisateur_dans_db, base_de_donnees):
    """Teste que l'utilisateur est bien dans la base."""
    assert len(base_de_donnees["users"]) == 1
    assert base_de_donnees["users"][0]["nom"] == "Alice"
