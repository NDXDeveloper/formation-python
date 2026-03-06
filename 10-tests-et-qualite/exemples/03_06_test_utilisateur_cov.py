# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Tests complets pour utilisateur etendu - couvre toutes
#                 les methodes et branches (roles, gestionnaire, actifs, admins)
#   Fichier source : 03-couverture-de-code.md
# ============================================================================

import pytest
import importlib
_mod = importlib.import_module("03_05_utilisateur_cov")
Utilisateur = _mod.Utilisateur
GestionnaireUtilisateurs = _mod.GestionnaireUtilisateurs


# ============= Tests Utilisateur =============

@pytest.fixture
def utilisateur():
    """Fixture pour creer un utilisateur de test."""
    return Utilisateur("Alice", "alice@test.com", 25)


@pytest.fixture
def utilisateur_mineur():
    """Fixture pour creer un utilisateur mineur."""
    return Utilisateur("Charlie", "charlie@test.com", 16)


def test_creation_utilisateur(utilisateur):
    """Teste la creation d'un utilisateur."""
    assert utilisateur.nom == "Alice"
    assert utilisateur.email == "alice@test.com"
    assert utilisateur.age == 25
    assert utilisateur.actif is True
    assert utilisateur.roles == []


def test_est_majeur_vrai(utilisateur):
    """Teste qu'un utilisateur de 25 ans est majeur."""
    assert utilisateur.est_majeur() is True


def test_est_majeur_faux(utilisateur_mineur):
    """Teste qu'un utilisateur de 16 ans n'est pas majeur."""
    assert utilisateur_mineur.est_majeur() is False


def test_desactiver_utilisateur(utilisateur):
    """Teste la desactivation d'un utilisateur."""
    utilisateur.desactiver()
    assert utilisateur.actif is False


def test_activer_utilisateur(utilisateur):
    """Teste l'activation d'un utilisateur."""
    utilisateur.desactiver()
    utilisateur.activer()
    assert utilisateur.actif is True


def test_ajouter_role(utilisateur):
    """Teste l'ajout d'un role."""
    utilisateur.ajouter_role("admin")
    assert "admin" in utilisateur.roles
    assert len(utilisateur.roles) == 1


def test_ajouter_role_deja_present(utilisateur):
    """Teste qu'on ne peut pas ajouter deux fois le meme role."""
    utilisateur.ajouter_role("admin")
    utilisateur.ajouter_role("admin")
    assert len(utilisateur.roles) == 1


def test_retirer_role(utilisateur):
    """Teste le retrait d'un role."""
    utilisateur.ajouter_role("admin")
    utilisateur.retirer_role("admin")
    assert "admin" not in utilisateur.roles


def test_retirer_role_inexistant(utilisateur):
    """Teste le retrait d'un role inexistant."""
    utilisateur.retirer_role("inexistant")
    assert len(utilisateur.roles) == 0


def test_a_role_vrai(utilisateur):
    """Teste la verification d'un role present."""
    utilisateur.ajouter_role("editeur")
    assert utilisateur.a_role("editeur") is True


def test_a_role_faux(utilisateur):
    """Teste la verification d'un role absent."""
    assert utilisateur.a_role("admin") is False


def test_est_admin_vrai(utilisateur):
    """Teste qu'un utilisateur avec le role admin est admin."""
    utilisateur.ajouter_role("admin")
    assert utilisateur.est_admin() is True


def test_est_admin_faux(utilisateur):
    """Teste qu'un utilisateur sans le role admin n'est pas admin."""
    assert utilisateur.est_admin() is False


# ============= Tests GestionnaireUtilisateurs =============

@pytest.fixture
def gestionnaire():
    """Fixture pour creer un gestionnaire."""
    return GestionnaireUtilisateurs()


def test_gestionnaire_vide_au_depart(gestionnaire):
    """Teste qu'un nouveau gestionnaire est vide."""
    assert gestionnaire.compter() == 0


def test_ajouter_utilisateur(gestionnaire):
    """Teste l'ajout d'un utilisateur."""
    user = Utilisateur("Bob", "bob@test.com", 30)
    user_id = gestionnaire.ajouter(user)

    assert user_id == 1
    assert gestionnaire.compter() == 1


def test_ajouter_plusieurs_utilisateurs(gestionnaire):
    """Teste l'ajout de plusieurs utilisateurs."""
    user1 = Utilisateur("Alice", "alice@test.com", 25)
    user2 = Utilisateur("Bob", "bob@test.com", 30)

    id1 = gestionnaire.ajouter(user1)
    id2 = gestionnaire.ajouter(user2)

    assert id1 == 1
    assert id2 == 2
    assert gestionnaire.compter() == 2


def test_obtenir_utilisateur_existant(gestionnaire):
    """Teste l'obtention d'un utilisateur existant."""
    user = Utilisateur("Charlie", "charlie@test.com", 28)
    user_id = gestionnaire.ajouter(user)

    utilisateur_obtenu = gestionnaire.obtenir(user_id)
    assert utilisateur_obtenu is user
    assert utilisateur_obtenu.nom == "Charlie"


def test_obtenir_utilisateur_inexistant(gestionnaire):
    """Teste l'obtention d'un utilisateur inexistant."""
    utilisateur = gestionnaire.obtenir(999)
    assert utilisateur is None


def test_supprimer_utilisateur_existant(gestionnaire):
    """Teste la suppression d'un utilisateur existant."""
    user = Utilisateur("Diana", "diana@test.com", 22)
    user_id = gestionnaire.ajouter(user)

    resultat = gestionnaire.supprimer(user_id)
    assert resultat is True
    assert gestionnaire.compter() == 0


def test_supprimer_utilisateur_inexistant(gestionnaire):
    """Teste la suppression d'un utilisateur inexistant."""
    resultat = gestionnaire.supprimer(999)
    assert resultat is False


def test_lister_actifs(gestionnaire):
    """Teste le listage des utilisateurs actifs."""
    user1 = Utilisateur("Eve", "eve@test.com", 27)
    user2 = Utilisateur("Frank", "frank@test.com", 35)
    user3 = Utilisateur("Grace", "grace@test.com", 29)

    gestionnaire.ajouter(user1)
    gestionnaire.ajouter(user2)
    gestionnaire.ajouter(user3)

    user2.desactiver()

    actifs = gestionnaire.lister_actifs()
    assert len(actifs) == 2
    assert user1 in actifs
    assert user2 not in actifs
    assert user3 in actifs


def test_lister_admins(gestionnaire):
    """Teste le listage des administrateurs."""
    user1 = Utilisateur("Henry", "henry@test.com", 30)
    user2 = Utilisateur("Iris", "iris@test.com", 28)
    user3 = Utilisateur("Jack", "jack@test.com", 32)

    user1.ajouter_role("admin")
    user2.ajouter_role("editeur")
    user3.ajouter_role("admin")

    gestionnaire.ajouter(user1)
    gestionnaire.ajouter(user2)
    gestionnaire.ajouter(user3)

    admins = gestionnaire.lister_admins()
    assert len(admins) == 2
    assert user1 in admins
    assert user2 not in admins
    assert user3 in admins
