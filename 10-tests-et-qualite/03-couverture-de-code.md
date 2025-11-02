🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.3 Couverture de code

## Introduction à la couverture de code

### Qu'est-ce que la couverture de code ?

La **couverture de code** (ou *code coverage* en anglais) est une métrique qui mesure quelle proportion de votre code est exécutée lorsque vous lancez vos tests.

**Analogie simple** : Imaginez que votre code est une maison avec plusieurs pièces. La couverture de code vous dit dans combien de pièces vous êtes entré pendant vos tests. Si vous n'êtes jamais entré dans la cuisine, vous ne savez pas si elle fonctionne correctement !

### Pourquoi mesurer la couverture ?

La couverture de code vous aide à :

1. **Identifier le code non testé** : Découvrir les parties de votre code sans tests
2. **Détecter le code mort** : Trouver du code qui n'est jamais exécuté
3. **Améliorer la qualité** : S'assurer que les fonctionnalités importantes sont testées
4. **Avoir confiance** : Savoir que votre code a été vérifié
5. **Suivre la progression** : Mesurer l'évolution de vos tests dans le temps

### Ce que la couverture NE garantit PAS

**Important** : Une couverture de 100% ne signifie pas que votre code est parfait !

```python
def diviser(a, b):
    return a / b

# Ce test donne 100% de couverture
def test_diviser():
    assert diviser(10, 2) == 5

# Mais il ne teste pas la division par zéro !
# diviser(10, 0) lèverait une erreur
```

**La couverture mesure ce qui est exécuté, pas ce qui est bien testé.**

### Les types de couverture

Il existe plusieurs types de couverture :

1. **Couverture de lignes** : Quelles lignes ont été exécutées ?
2. **Couverture de branches** : Tous les chemins if/else ont-ils été testés ?
3. **Couverture de fonctions** : Toutes les fonctions ont-elles été appelées ?
4. **Couverture de conditions** : Toutes les conditions ont-elles été évaluées ?

Nous nous concentrerons principalement sur la **couverture de lignes** et la **couverture de branches**.

---

## Installation des outils de couverture

### coverage.py : L'outil standard

`coverage.py` est l'outil le plus utilisé pour mesurer la couverture en Python :

```bash
# Installation
pip install coverage
```

### pytest-cov : Extension pour pytest

Si vous utilisez pytest, `pytest-cov` simplifie l'utilisation :

```bash
# Installation
pip install pytest-cov
```

---

## Utilisation de coverage.py

### Exemple de base

Commençons avec un module simple :

```python
# fichier: calculatrice.py
def additionner(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraire(a, b):
    """Soustrait b de a."""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres."""
    return a * b

def diviser(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres."""
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)
```

Tests incomplets :

```python
# fichier: test_calculatrice.py
from calculatrice import additionner, soustraire, diviser

def test_additionner():
    assert additionner(5, 3) == 8

def test_soustraire():
    assert soustraire(10, 4) == 6

def test_diviser():
    assert diviser(10, 2) == 5
```

**Remarque** : Ces tests ne couvrent pas `multiplier()` ni `calculer_moyenne()` !

### Lancer coverage.py

```bash
# Exécuter les tests avec coverage
coverage run -m pytest test_calculatrice.py

# Afficher le rapport dans le terminal
coverage report

# Générer un rapport HTML détaillé
coverage html
```

### Interpréter le rapport

Sortie typique de `coverage report` :

```
Name                  Stmts   Miss  Cover
-----------------------------------------
calculatrice.py          15      6    60%
test_calculatrice.py      6      0   100%
-----------------------------------------
TOTAL                    21      6    71%
```

**Explication** :
- **Stmts** : Nombre total de lignes exécutables
- **Miss** : Nombre de lignes non exécutées
- **Cover** : Pourcentage de couverture

Dans notre exemple : 6 lignes de `calculatrice.py` n'ont jamais été exécutées (les fonctions `multiplier()` et `calculer_moyenne()` et leurs branches).

### Rapport HTML détaillé

Le rapport HTML est beaucoup plus informatif :

```bash
# Générer le rapport HTML
coverage html

# Ouvrir le rapport (Linux/Mac)
open htmlcov/index.html

# Ouvrir le rapport (Windows)
start htmlcov/index.html
```

Le rapport HTML montre :
- Les lignes couvertes en **vert**
- Les lignes non couvertes en **rouge**
- Les branches partiellement couvertes en **jaune**

---

## Utilisation de pytest-cov

### Commandes de base

Avec pytest-cov, tout est plus simple :

```bash
# Lancer les tests avec rapport de couverture
pytest --cov=calculatrice test_calculatrice.py

# Avec un rapport détaillé
pytest --cov=calculatrice --cov-report=term-missing test_calculatrice.py

# Générer un rapport HTML
pytest --cov=calculatrice --cov-report=html test_calculatrice.py

# Combiner rapport terminal et HTML
pytest --cov=calculatrice --cov-report=term --cov-report=html
```

### Options utiles

```bash
# Afficher les lignes manquantes
pytest --cov=module --cov-report=term-missing

# Exiger un minimum de couverture (échoue si < 80%)
pytest --cov=module --cov-fail-under=80

# Couvrir plusieurs modules
pytest --cov=module1 --cov=module2

# Couvrir tout le projet
pytest --cov=.

# Exclure certains fichiers
pytest --cov=module --cov-report=term --cov-config=.coveragerc
```

### Rapport détaillé

Avec `--cov-report=term-missing`, vous voyez les lignes manquantes :

```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
calculatrice.py          15      6    60%   12-13, 16-19
test_calculatrice.py      6      0   100%
---------------------------------------------------
TOTAL                    21      6    71%
```

Les numéros dans "Missing" indiquent les lignes non couvertes.

---

## Améliorer la couverture

### Compléter les tests

Ajoutons des tests pour atteindre une meilleure couverture :

```python
# fichier: test_calculatrice.py (version améliorée)
import pytest
from calculatrice import (
    additionner,
    soustraire,
    multiplier,
    diviser,
    calculer_moyenne
)

def test_additionner():
    """Teste l'addition."""
    assert additionner(5, 3) == 8
    assert additionner(-1, 1) == 0

def test_soustraire():
    """Teste la soustraction."""
    assert soustraire(10, 4) == 6
    assert soustraire(5, 10) == -5

def test_multiplier():
    """Teste la multiplication."""
    assert multiplier(4, 5) == 20
    assert multiplier(-3, 3) == -9

def test_diviser():
    """Teste la division normale."""
    assert diviser(10, 2) == 5
    assert diviser(9, 3) == 3

def test_diviser_par_zero():
    """Teste la division par zéro."""
    with pytest.raises(ValueError, match="Division par zéro"):
        diviser(10, 0)

def test_calculer_moyenne():
    """Teste le calcul de moyenne."""
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3
    assert calculer_moyenne([10, 20]) == 15

def test_calculer_moyenne_liste_vide():
    """Teste la moyenne avec une liste vide."""
    assert calculer_moyenne([]) == 0
```

Nouveau rapport de couverture :

```bash
pytest --cov=calculatrice --cov-report=term-missing
```

```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
calculatrice.py          15      0   100%
test_calculatrice.py     20      0   100%
---------------------------------------------------
TOTAL                    35      0   100%
```

**Nous avons atteint 100% de couverture ! 🎉**

---

## Couverture de branches

### Qu'est-ce que la couverture de branches ?

La couverture de branches vérifie que tous les chemins possibles (if/else, and/or) ont été testés.

Exemple :

```python
def verifier_age(age):
    """Vérifie si une personne est majeure."""
    if age >= 18:
        return "Majeur"
    else:
        return "Mineur"
```

Pour une couverture de branches complète, vous devez tester :
- Le cas où `age >= 18` (branche True)
- Le cas où `age < 18` (branche False)

### Activer la couverture de branches

```bash
# Avec coverage.py
coverage run --branch -m pytest
coverage report

# Avec pytest-cov
pytest --cov=module --cov-branch
```

### Exemple avec branches

```python
# fichier: validation.py
def valider_note(note):
    """Valide une note et retourne un message."""
    if note < 0 or note > 20:
        return "Note invalide"

    if note >= 10:
        return "Réussi"
    else:
        return "Échoué"

def calculer_mention(moyenne):
    """Calcule la mention selon la moyenne."""
    if moyenne < 10:
        return "Échec"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Assez bien"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Très bien"
```

Tests incomplets :

```python
# fichier: test_validation.py
from validation import valider_note, calculer_mention

def test_valider_note_valide():
    assert valider_note(15) == "Réussi"
    assert valider_note(5) == "Échoué"

def test_calculer_mention():
    assert calculer_mention(18) == "Très bien"
    assert calculer_mention(8) == "Échec"
```

Rapport avec branches :

```bash
pytest --cov=validation --cov-branch --cov-report=term-missing
```

```
Name               Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------
validation.py         13      0      8      2    88%   3->5, 10->12
test_validation.py     6      0      0      0   100%
--------------------------------------------------------------
TOTAL                 19      0      8      2    90%
```

**BrPart** (Branches Partielles) : 2 branches n'ont pas été testées
- `3->5` : La branche "note invalide" (note < 0 ou note > 20)
- `10->12` : Certaines mentions n'ont pas été testées

Tests complets avec toutes les branches :

```python
# fichier: test_validation.py (version complète)
from validation import valider_note, calculer_mention

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
```

Maintenant la couverture de branches est à 100% !

---

## Configuration avec .coveragerc

Vous pouvez configurer coverage avec un fichier `.coveragerc` :

```ini
# fichier: .coveragerc
[run]
# Inclure la couverture de branches
branch = True

# Fichiers à analyser
source = .

# Fichiers/dossiers à ignorer
omit =
    */tests/*
    */test_*.py
    */__pycache__/*
    */venv/*
    */env/*
    setup.py

[report]
# Ignorer ces lignes dans les rapports
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:
    @abstractmethod

# Précision des pourcentages
precision = 2

# Afficher les lignes manquantes
show_missing = True

[html]
# Répertoire pour le rapport HTML
directory = htmlcov
```

Utilisation :

```bash
# coverage.py utilise automatiquement .coveragerc
coverage run -m pytest
coverage report

# Ou avec pytest-cov
pytest --cov --cov-config=.coveragerc
```

---

## Configuration avec pyproject.toml

Si vous utilisez `pyproject.toml`, vous pouvez y configurer coverage :

```toml
# fichier: pyproject.toml
[tool.coverage.run]
branch = true
source = ["."]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
    "*/venv/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
show_missing = true
precision = 2

[tool.coverage.html]
directory = "htmlcov"
```

---

## Exclure du code de la couverture

### Avec des commentaires

Vous pouvez exclure certaines lignes de la couverture :

```python
def fonction_complexe():
    """Fonction avec du code qu'on ne peut pas tester."""

    # Code normal (couvert)
    resultat = calcul_simple()

    # Code impossible à tester (exclu)
    if DEBUG_MODE:  # pragma: no cover
        print("Mode debug activé")
        log_debug(resultat)

    return resultat

def code_pour_python_ancien():  # pragma: no cover
    """Code pour Python < 3.6 qu'on ne teste pas."""
    # ... code legacy ...
    pass
```

### Exclure des fichiers entiers

Dans `.coveragerc` :

```ini
[run]
omit =
    */migrations/*
    */settings.py
    */manage.py
    */wsgi.py
```

---

## Cas pratique : Système de gestion d'utilisateurs

### Code initial (incomplet)

```python
# fichier: utilisateur.py
class Utilisateur:
    """Représente un utilisateur du système."""

    def __init__(self, nom, email, age):
        self.nom = nom
        self.email = email
        self.age = age
        self.actif = True
        self.roles = []

    def est_majeur(self):
        """Vérifie si l'utilisateur est majeur."""
        return self.age >= 18

    def desactiver(self):
        """Désactive l'utilisateur."""
        self.actif = False

    def activer(self):
        """Active l'utilisateur."""
        self.actif = True

    def ajouter_role(self, role):
        """Ajoute un rôle à l'utilisateur."""
        if role not in self.roles:
            self.roles.append(role)

    def retirer_role(self, role):
        """Retire un rôle à l'utilisateur."""
        if role in self.roles:
            self.roles.remove(role)

    def a_role(self, role):
        """Vérifie si l'utilisateur a un rôle."""
        return role in self.roles

    def est_admin(self):
        """Vérifie si l'utilisateur est administrateur."""
        return "admin" in self.roles

class GestionnaireUtilisateurs:
    """Gère une collection d'utilisateurs."""

    def __init__(self):
        self.utilisateurs = {}
        self._prochain_id = 1

    def ajouter(self, utilisateur):
        """Ajoute un utilisateur."""
        user_id = self._prochain_id
        self.utilisateurs[user_id] = utilisateur
        self._prochain_id += 1
        return user_id

    def obtenir(self, user_id):
        """Obtient un utilisateur par son ID."""
        return self.utilisateurs.get(user_id)

    def supprimer(self, user_id):
        """Supprime un utilisateur."""
        if user_id in self.utilisateurs:
            del self.utilisateurs[user_id]
            return True
        return False

    def lister_actifs(self):
        """Liste tous les utilisateurs actifs."""
        return [u for u in self.utilisateurs.values() if u.actif]

    def lister_admins(self):
        """Liste tous les administrateurs."""
        return [u for u in self.utilisateurs.values() if u.est_admin()]

    def compter(self):
        """Compte le nombre d'utilisateurs."""
        return len(self.utilisateurs)
```

### Tests initiaux (incomplets)

```python
# fichier: test_utilisateur.py
import pytest
from utilisateur import Utilisateur, GestionnaireUtilisateurs

def test_creation_utilisateur():
    """Teste la création d'un utilisateur."""
    user = Utilisateur("Alice", "alice@test.com", 25)
    assert user.nom == "Alice"
    assert user.email == "alice@test.com"
    assert user.age == 25
    assert user.actif is True

def test_ajouter_utilisateur():
    """Teste l'ajout d'un utilisateur."""
    gestionnaire = GestionnaireUtilisateurs()
    user = Utilisateur("Bob", "bob@test.com", 30)

    user_id = gestionnaire.ajouter(user)
    assert user_id == 1
    assert gestionnaire.compter() == 1
```

Vérifions la couverture :

```bash
pytest --cov=utilisateur --cov-report=term-missing --cov-branch
```

```
Name                   Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------
test_utilisateur.py        9      0      0      0   100%
utilisateur.py            42     29     12      0    25%   12-15, 18-21, 24-29, 32-35, 38-48, 55-60
------------------------------------------------------------------
TOTAL                     51     29     12      0    37%
```

**Seulement 25% de couverture !** Beaucoup de fonctionnalités ne sont pas testées.

### Tests complets

```python
# fichier: test_utilisateur.py (version complète)
import pytest
from utilisateur import Utilisateur, GestionnaireUtilisateurs

# ============= Tests Utilisateur =============

@pytest.fixture
def utilisateur():
    """Fixture pour créer un utilisateur de test."""
    return Utilisateur("Alice", "alice@test.com", 25)

@pytest.fixture
def utilisateur_mineur():
    """Fixture pour créer un utilisateur mineur."""
    return Utilisateur("Charlie", "charlie@test.com", 16)

def test_creation_utilisateur(utilisateur):
    """Teste la création d'un utilisateur."""
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
    """Teste la désactivation d'un utilisateur."""
    utilisateur.desactiver()
    assert utilisateur.actif is False

def test_activer_utilisateur(utilisateur):
    """Teste l'activation d'un utilisateur."""
    utilisateur.desactiver()
    utilisateur.activer()
    assert utilisateur.actif is True

def test_ajouter_role(utilisateur):
    """Teste l'ajout d'un rôle."""
    utilisateur.ajouter_role("admin")
    assert "admin" in utilisateur.roles
    assert len(utilisateur.roles) == 1

def test_ajouter_role_deja_present(utilisateur):
    """Teste qu'on ne peut pas ajouter deux fois le même rôle."""
    utilisateur.ajouter_role("admin")
    utilisateur.ajouter_role("admin")
    assert len(utilisateur.roles) == 1

def test_retirer_role(utilisateur):
    """Teste le retrait d'un rôle."""
    utilisateur.ajouter_role("admin")
    utilisateur.retirer_role("admin")
    assert "admin" not in utilisateur.roles

def test_retirer_role_inexistant(utilisateur):
    """Teste le retrait d'un rôle inexistant."""
    # Ne doit pas lever d'erreur
    utilisateur.retirer_role("inexistant")
    assert len(utilisateur.roles) == 0

def test_a_role_vrai(utilisateur):
    """Teste la vérification d'un rôle présent."""
    utilisateur.ajouter_role("editeur")
    assert utilisateur.a_role("editeur") is True

def test_a_role_faux(utilisateur):
    """Teste la vérification d'un rôle absent."""
    assert utilisateur.a_role("admin") is False

def test_est_admin_vrai(utilisateur):
    """Teste qu'un utilisateur avec le rôle admin est admin."""
    utilisateur.ajouter_role("admin")
    assert utilisateur.est_admin() is True

def test_est_admin_faux(utilisateur):
    """Teste qu'un utilisateur sans le rôle admin n'est pas admin."""
    assert utilisateur.est_admin() is False

# ============= Tests GestionnaireUtilisateurs =============

@pytest.fixture
def gestionnaire():
    """Fixture pour créer un gestionnaire."""
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

    # Désactiver un utilisateur
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

    # Seulement user1 et user3 sont admins
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
```

Nouvelle couverture :

```bash
pytest --cov=utilisateur --cov-report=term-missing --cov-branch
```

```
Name                   Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------
test_utilisateur.py       90      0      0      0   100%
utilisateur.py            42      0     12      0   100%
--------------------------------------------------------
TOTAL                    132      0     12      0   100%
```

**100% de couverture atteinte ! 🎉**

---

## Bonnes pratiques de couverture

### 1. Viser une couverture élevée, mais réaliste

```python
# Objectifs raisonnables par type de projet
# - Librairie : 90-100%
# - Application web : 80-90%
# - Script utilitaire : 60-80%
# - Prototype : 40-60%
```

**Ne sacrifiez pas la qualité des tests pour atteindre 100%.**

### 2. Tester les branches critiques

Concentrez-vous sur :
- La logique métier importante
- Les fonctions publiques de l'API
- Les cas d'erreur
- Les branches de conditions

```python
# ✅ Bon - teste les branches importantes
def calculer_remise(prix, client_premium):
    """Calcule une remise."""
    if client_premium:
        return prix * 0.20  # Important à tester
    return 0

# Tests
def test_remise_client_premium():
    assert calculer_remise(100, True) == 20

def test_pas_de_remise_client_normal():
    assert calculer_remise(100, False) == 0
```

### 3. Ne pas tester le code trivial

Certains code n'ont pas besoin de tests :

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom  # Pas besoin de tester

    def __repr__(self):  # pragma: no cover
        return f"Personne({self.nom})"

    def calculer_age_retraite(self):
        # Ceci mérite un test !
        return 65 - self.age if self.age < 65 else 0
```

### 4. Intégrer la couverture dans CI/CD

Dans votre pipeline d'intégration continue :

```yaml
# fichier: .github/workflows/tests.yml (exemple GitHub Actions)
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install pytest pytest-cov
        pip install -r requirements.txt

    - name: Run tests with coverage
      run: |
        pytest --cov=src --cov-report=term --cov-fail-under=80

    - name: Upload coverage report
      uses: codecov/codecov-action@v2
```

### 5. Suivre l'évolution de la couverture

Créez un badge de couverture dans votre README :

```markdown
# Mon Projet

[![Coverage](https://img.shields.io/codecov/c/github/username/repo)](https://codecov.io/gh/username/repo)

...
```

### 6. Exclure intelligemment

N'incluez pas dans la couverture :
- Le code de configuration
- Les migrations de base de données
- Les fichiers de tests eux-mêmes
- Le code legacy qu'on ne modifie pas

```ini
# .coveragerc
[run]
omit =
    */tests/*
    */migrations/*
    */config/*
    setup.py
    */venv/*
```

---

## Rapport de couverture dans différents formats

### Format terminal (par défaut)

```bash
pytest --cov=module --cov-report=term
```

Affiche un tableau dans le terminal.

### Format HTML (interactif)

```bash
pytest --cov=module --cov-report=html
```

Crée un site web dans `htmlcov/` avec :
- Vue d'ensemble des fichiers
- Code source annoté (lignes vertes/rouges)
- Statistiques détaillées

### Format XML (pour outils CI/CD)

```bash
pytest --cov=module --cov-report=xml
```

Génère `coverage.xml` pour les outils comme Jenkins, GitLab CI, etc.

### Format JSON (pour traitement automatique)

```bash
pytest --cov=module --cov-report=json
```

Génère `coverage.json` pour analyse programmatique.

### Combiner plusieurs formats

```bash
pytest --cov=module \
       --cov-report=term \
       --cov-report=html \
       --cov-report=xml
```

---

## Outils et services de couverture

### Codecov

Service cloud pour suivre la couverture :

```bash
# Installation
pip install codecov

# Upload après les tests
codecov
```

Configuration `.codecov.yml` :

```yaml
coverage:
  status:
    project:
      default:
        target: 80%
        threshold: 5%
```

### Coveralls

Alternative à Codecov :

```bash
pip install coveralls
coveralls
```

### Coverage.py avec tox

Pour tester sur plusieurs versions de Python :

```ini
# fichier: tox.ini
[tox]
envlist = py38,py39,py310,py311

[testenv]
deps =
    pytest
    pytest-cov
commands =
    pytest --cov=src --cov-report=term

[coverage:run]
branch = True
```

---

## Exemple : Projet complet avec couverture

### Structure du projet

```
mon_projet/
├── src/
│   ├── __init__.py
│   ├── calculatrice.py
│   ├── utilisateur.py
│   └── validation.py
├── tests/
│   ├── __init__.py
│   ├── test_calculatrice.py
│   ├── test_utilisateur.py
│   └── test_validation.py
├── .coveragerc
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Fichier .coveragerc

```ini
[run]
branch = True
source = src
omit =
    */tests/*
    */__pycache__/*
    */venv/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:
show_missing = True
precision = 2

[html]
directory = htmlcov
```

### Commandes courantes

```bash
# Lancer les tests avec couverture
pytest --cov=src --cov-report=html --cov-report=term

# Voir le rapport HTML
open htmlcov/index.html

# Exiger 80% minimum de couverture
pytest --cov=src --cov-fail-under=80

# Voir seulement les fichiers avec couverture < 100%
coverage report --skip-covered
```

### Script Makefile

```makefile
# fichier: Makefile
.PHONY: test coverage clean

test:
	pytest -v

coverage:
	pytest --cov=src --cov-report=html --cov-report=term-missing
	@echo "Rapport HTML généré dans htmlcov/"

coverage-report:
	open htmlcov/index.html

clean:
	rm -rf htmlcov/
	rm -f .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
```

Utilisation :

```bash
make test           # Lance les tests
make coverage       # Lance les tests avec rapport de couverture
make coverage-report # Ouvre le rapport HTML
make clean          # Nettoie les fichiers générés
```

---

## Interpréter et agir sur les résultats

### Que faire si la couverture est basse ?

1. **Identifier les zones non couvertes** avec `--cov-report=term-missing`
2. **Prioriser** : Commencer par le code critique
3. **Écrire des tests** pour les fonctionnalités importantes
4. **Refactorer** si le code est difficile à tester
5. **Exclure** le code non testable (avec `# pragma: no cover`)

### Analyser un rapport

```
Name               Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------
src/core.py           45      5     12      2    85%   23-25, 67->70
src/utils.py          20      0      4      0   100%
src/legacy.py         30     30      0      0     0%
--------------------------------------------------------------
TOTAL                 95     35     16      2    61%
```

**Analyse** :
- `core.py` : Bon (85%), mais lignes 23-25 et branche 67->70 non couvertes
- `utils.py` : Excellent (100%)
- `legacy.py` : À revoir ou exclure (0%)
- **Action** : Ajouter des tests pour core.py, décider du sort de legacy.py

### Red flags (signaux d'alerte)

🚩 **Couverture très basse (<50%)** : Tests insuffisants
🚩 **Beaucoup de branches partielles** : Cas limites non testés
🚩 **Code critique non couvert** : Risque élevé de bugs
🚩 **Couverture qui baisse** : Nouveau code sans tests

---

## Résumé

### Points clés à retenir

1. **La couverture mesure ce qui est exécuté**, pas ce qui est bien testé
2. **100% de couverture ≠ code parfait**, mais c'est un bon indicateur
3. **Couverture de branches** > couverture de lignes (plus complète)
4. **Utilisez pytest-cov** pour une intégration simple avec pytest
5. **Configurez .coveragerc** pour personnaliser la mesure
6. **Intégrez dans CI/CD** pour suivre l'évolution
7. **Visez 80-90%** pour la plupart des projets
8. **Excluez intelligemment** le code non testable

### Commandes essentielles

```bash
# Mesurer la couverture
pytest --cov=module

# Avec détails des lignes manquantes
pytest --cov=module --cov-report=term-missing

# Avec couverture de branches
pytest --cov=module --cov-branch

# Générer rapport HTML
pytest --cov=module --cov-report=html

# Exiger un minimum
pytest --cov=module --cov-fail-under=80

# Voir seulement ce qui n'est pas à 100%
coverage report --skip-covered
```

### Ordre de priorité pour améliorer la couverture

1. **Code métier critique** : Logique importante de l'application
2. **API publique** : Fonctions/classes exposées aux utilisateurs
3. **Gestion d'erreurs** : Tous les cas d'exception
4. **Branches conditionnelles** : Tous les if/else
5. **Code utilitaire** : Fonctions helper
6. **Code de présentation** : UI, formatage (moins critique)

### Objectifs raisonnables

| Type de projet | Couverture cible |
|----------------|------------------|
| Bibliothèque publique | 90-100% |
| Application critique | 85-95% |
| Application standard | 75-85% |
| API/Backend | 80-90% |
| Script/outil | 60-80% |
| Prototype/POC | 40-60% |

---

## Ressources complémentaires

- Documentation coverage.py : https://coverage.readthedocs.io/
- Documentation pytest-cov : https://pytest-cov.readthedocs.io/
- Codecov : https://codecov.io/
- Article Martin Fowler sur la couverture : https://martinfowler.com/bliki/TestCoverage.html
- Guide des bonnes pratiques : https://testing.googleblog.com/

**La couverture est un outil, pas un objectif.** Utilisez-la pour améliorer la qualité de vos tests, pas juste pour atteindre un pourcentage ! 🎯

⏭️ [Documentation avec docstrings](/10-tests-et-qualite/04-documentation-docstrings.md)
