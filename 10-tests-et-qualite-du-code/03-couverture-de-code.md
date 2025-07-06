🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.3 : Couverture de code

## Introduction

Imaginez que vous êtes architecte et que vous venez de terminer les plans d'une maison. Avant de commencer la construction, vous voulez vérifier que tous les aspects ont été pensés : la plomberie, l'électricité, la ventilation, l'isolation... La **couverture de code** fonctionne de la même manière : elle vous indique quelles parties de votre code ont été "visitées" par vos tests et lesquelles ont été oubliées.

C'est un outil précieux pour s'assurer que vos tests examinent bien tout votre code, mais attention : 100% de couverture ne garantit pas 100% de qualité !

## Qu'est-ce que la couverture de code ?

### Définition simple
La couverture de code mesure le pourcentage de votre code qui est exécuté pendant les tests. Si votre programme fait 100 lignes et que vos tests en exécutent 80, vous avez 80% de couverture.

### Exemple visuel
```python
def calculer_remise(prix, age_client):
    """Calcule la remise selon l'âge du client"""
    if prix < 0:                    # Ligne 1 ✅ Testée
        raise ValueError("Prix invalide")  # Ligne 2 ✅ Testée

    if age_client < 18:             # Ligne 3 ✅ Testée
        return prix * 0.9           # Ligne 4 ❌ PAS testée
    elif age_client >= 65:          # Ligne 5 ✅ Testée
        return prix * 0.8           # Ligne 6 ❌ PAS testée
    else:
        return prix                 # Ligne 7 ✅ Testée

# Test existant (incomplet)
def test_calculer_remise():
    # Cas normal
    assert calculer_remise(100, 30) == 100

    # Cas d'erreur
    try:
        calculer_remise(-10, 30)
    except ValueError:
        pass

# Couverture : 4 lignes testées sur 6 = 67%
```

### Types de couverture

#### 1. Couverture de lignes (Line Coverage)
Mesure quelles lignes de code ont été exécutées.

#### 2. Couverture de branches (Branch Coverage)
Mesure quelles branches des conditions ont été prises.

```python
def evaluer_note(note):
    if note >= 10:        # Branche: True ET False testées ?
        return "Réussi"   # Exécuté si note >= 10
    else:
        return "Échoué"   # Exécuté si note < 10

# Pour 100% de couverture de branches, il faut tester :
# - Un cas où note >= 10 (branche True)
# - Un cas où note < 10 (branche False)
```

#### 3. Couverture de fonctions (Function Coverage)
Mesure quelles fonctions ont été appelées au moins une fois.

## Installation et utilisation de coverage.py

### Installation
```bash
pip install coverage
```

### Utilisation basique

```python
# math_utils.py - Code à tester
def additionner(a, b):
    """Addition de deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustraction de deux nombres"""
    return a - b

def diviser(a, b):
    """Division de deux nombres"""
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return a / b

def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0
```

```python
# test_math_utils.py - Tests (incomplets pour l'exemple)
import pytest
from math_utils import additionner, soustraire, diviser, calculer_moyenne

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0

def test_soustraire():
    assert soustraire(5, 3) == 2

def test_diviser():
    assert diviser(10, 2) == 5
    # Note : on ne teste pas la division par zéro

def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3]) == 2
    # Note : on ne teste pas la liste vide

# Note : est_pair() n'est pas testée du tout
```

### Commandes coverage

```bash
# Exécuter les tests avec mesure de couverture
coverage run -m pytest test_math_utils.py

# Afficher le rapport de couverture
coverage report

# Générer un rapport HTML
coverage html

# Afficher les lignes manquantes
coverage report --show-missing
```

### Résultat typique
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
math_utils.py        12      4    67%   8, 12, 16, 20
test_math_utils.py    8      0   100%
-----------------------------------------------
TOTAL                20      4    80%
```

## Rapport HTML détaillé

Le rapport HTML est très utile pour visualiser la couverture :

```bash
coverage html
# Ouvre htmlcov/index.html dans votre navigateur
```

Le rapport montre :
- **Lignes vertes** : Code testé
- **Lignes rouges** : Code non testé
- **Lignes jaunes** : Branches partiellement testées

## Améliorer la couverture

### Tests complets pour l'exemple précédent

```python
# test_math_utils_complet.py
import pytest
from math_utils import additionner, soustraire, diviser, calculer_moyenne, est_pair

class TestMathUtils:

    def test_additionner(self):
        """Tests complets pour l'addition"""
        assert additionner(2, 3) == 5
        assert additionner(-1, 1) == 0
        assert additionner(0, 0) == 0
        assert additionner(-5, -3) == -8

    def test_soustraire(self):
        """Tests complets pour la soustraction"""
        assert soustraire(5, 3) == 2
        assert soustraire(0, 0) == 0
        assert soustraire(-2, -5) == 3

    def test_diviser_cas_normaux(self):
        """Tests de division normaux"""
        assert diviser(10, 2) == 5
        assert diviser(9, 3) == 3
        assert diviser(-10, 2) == -5

    def test_diviser_par_zero(self):
        """Test de division par zéro"""
        with pytest.raises(ZeroDivisionError, match="Division par zéro"):
            diviser(10, 0)

    def test_calculer_moyenne_liste_normale(self):
        """Test de moyenne avec liste normale"""
        assert calculer_moyenne([1, 2, 3]) == 2
        assert calculer_moyenne([10]) == 10
        assert calculer_moyenne([1, 2, 3, 4]) == 2.5

    def test_calculer_moyenne_liste_vide(self):
        """Test de moyenne avec liste vide"""
        assert calculer_moyenne([]) == 0

    def test_est_pair(self):
        """Tests pour la fonction est_pair"""
        assert est_pair(2) == True
        assert est_pair(4) == True
        assert est_pair(1) == False
        assert est_pair(3) == False
        assert est_pair(0) == True
        assert est_pair(-2) == True
        assert est_pair(-1) == False

# Maintenant : 100% de couverture !
```

## Configuration avancée de coverage

### Fichier .coveragerc

```ini
# .coveragerc - Configuration de coverage
[run]
source = .
omit =
    */tests/*
    */venv/*
    setup.py
    */migrations/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

[html]
directory = htmlcov
```

### Exclusion de code avec pragma

```python
def fonction_critique():
    """Fonction principale"""
    try:
        # Code important testé
        return traiter_donnees()
    except Exception:  # pragma: no cover
        # Code d'urgence difficile à tester
        log_emergency("Erreur critique!")
        sys.exit(1)

def fonction_debug():  # pragma: no cover
    """Fonction de debug non testée"""
    print("Debug info...")
```

## Intégration avec pytest

### Plugin pytest-cov

```bash
pip install pytest-cov
```

```bash
# Exécution directe avec pytest
pytest --cov=math_utils test_math_utils.py

# Avec rapport HTML
pytest --cov=math_utils --cov-report=html test_math_utils.py

# Avec seuil de couverture minimum
pytest --cov=math_utils --cov-fail-under=90 test_math_utils.py
```

### Configuration dans pytest.ini

```ini
# pytest.ini
[tool:pytest]
addopts = --cov=src --cov-report=html --cov-report=term-missing --cov-fail-under=80
```

## Exemple complet : Système de gestion d'utilisateurs

```python
# user_manager.py
class User:
    def __init__(self, nom, email, age):
        self.nom = nom
        self.email = email
        self.age = age
        self.actif = True

    def est_adulte(self):
        return self.age >= 18

    def est_senior(self):
        return self.age >= 65

class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def ajouter_user(self, nom, email, age):
        """Ajoute un utilisateur"""
        if not nom or not email:
            raise ValueError("Nom et email requis")

        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")

        if age > 150:
            raise ValueError("L'âge ne peut pas dépasser 150 ans")

        # Vérifier si l'email existe déjà
        for user in self.users.values():
            if user.email == email:
                raise ValueError("Email déjà utilisé")

        user = User(nom, email, age)
        user_id = self.next_id
        self.users[user_id] = user
        self.next_id += 1
        return user_id

    def obtenir_user(self, user_id):
        """Récupère un utilisateur"""
        return self.users.get(user_id)

    def supprimer_user(self, user_id):
        """Supprime un utilisateur"""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def desactiver_user(self, user_id):
        """Désactive un utilisateur"""
        user = self.users.get(user_id)
        if user:
            user.actif = False
            return True
        return False

    def obtenir_users_actifs(self):
        """Retourne les utilisateurs actifs"""
        return [user for user in self.users.values() if user.actif]

    def obtenir_users_adultes(self):
        """Retourne les utilisateurs adultes"""
        return [user for user in self.users.values() if user.est_adulte()]

    def obtenir_statistiques(self):
        """Retourne des statistiques"""
        total = len(self.users)
        if total == 0:
            return {"total": 0, "adultes": 0, "seniors": 0, "actifs": 0}

        adultes = len([u for u in self.users.values() if u.est_adulte()])
        seniors = len([u for u in self.users.values() if u.est_senior()])
        actifs = len([u for u in self.users.values() if u.actif])

        return {
            "total": total,
            "adultes": adultes,
            "seniors": seniors,
            "actifs": actifs
        }
```

### Tests avec couverture complète

```python
# test_user_manager.py
import pytest
from user_manager import User, UserManager

class TestUser:

    def test_creation_user(self):
        """Test de création d'utilisateur"""
        user = User("Alice", "alice@test.com", 25)
        assert user.nom == "Alice"
        assert user.email == "alice@test.com"
        assert user.age == 25
        assert user.actif == True

    def test_est_adulte(self):
        """Test de la méthode est_adulte"""
        # Adulte
        user_adulte = User("Bob", "bob@test.com", 25)
        assert user_adulte.est_adulte() == True

        # Mineur
        user_mineur = User("Charlie", "charlie@test.com", 16)
        assert user_mineur.est_adulte() == False

        # Cas limite : exactement 18 ans
        user_limite = User("David", "david@test.com", 18)
        assert user_limite.est_adulte() == True

    def test_est_senior(self):
        """Test de la méthode est_senior"""
        # Senior
        user_senior = User("Eve", "eve@test.com", 70)
        assert user_senior.est_senior() == True

        # Non senior
        user_jeune = User("Frank", "frank@test.com", 30)
        assert user_jeune.est_senior() == False

        # Cas limite : exactement 65 ans
        user_limite = User("Grace", "grace@test.com", 65)
        assert user_limite.est_senior() == True

class TestUserManager:

    @pytest.fixture
    def manager(self):
        """Fixture pour un gestionnaire propre"""
        return UserManager()

    def test_ajouter_user_valide(self, manager):
        """Test d'ajout d'utilisateur valide"""
        user_id = manager.ajouter_user("Alice", "alice@test.com", 25)
        assert user_id == 1

        user = manager.obtenir_user(user_id)
        assert user.nom == "Alice"
        assert user.email == "alice@test.com"
        assert user.age == 25

    def test_ajouter_user_nom_manquant(self, manager):
        """Test d'ajout avec nom manquant"""
        with pytest.raises(ValueError, match="Nom et email requis"):
            manager.ajouter_user("", "test@test.com", 25)

        with pytest.raises(ValueError, match="Nom et email requis"):
            manager.ajouter_user(None, "test@test.com", 25)

    def test_ajouter_user_email_manquant(self, manager):
        """Test d'ajout avec email manquant"""
        with pytest.raises(ValueError, match="Nom et email requis"):
            manager.ajouter_user("Alice", "", 25)

        with pytest.raises(ValueError, match="Nom et email requis"):
            manager.ajouter_user("Alice", None, 25)

    def test_ajouter_user_age_negatif(self, manager):
        """Test d'ajout avec âge négatif"""
        with pytest.raises(ValueError, match="L'âge ne peut pas être négatif"):
            manager.ajouter_user("Alice", "alice@test.com", -1)

    def test_ajouter_user_age_trop_eleve(self, manager):
        """Test d'ajout avec âge trop élevé"""
        with pytest.raises(ValueError, match="L'âge ne peut pas dépasser 150 ans"):
            manager.ajouter_user("Alice", "alice@test.com", 151)

    def test_ajouter_user_email_duplique(self, manager):
        """Test d'ajout avec email déjà utilisé"""
        manager.ajouter_user("Alice", "same@test.com", 25)

        with pytest.raises(ValueError, match="Email déjà utilisé"):
            manager.ajouter_user("Bob", "same@test.com", 30)

    def test_obtenir_user_existant(self, manager):
        """Test d'obtention d'utilisateur existant"""
        user_id = manager.ajouter_user("Alice", "alice@test.com", 25)
        user = manager.obtenir_user(user_id)
        assert user is not None
        assert user.nom == "Alice"

    def test_obtenir_user_inexistant(self, manager):
        """Test d'obtention d'utilisateur inexistant"""
        user = manager.obtenir_user(999)
        assert user is None

    def test_supprimer_user_existant(self, manager):
        """Test de suppression d'utilisateur existant"""
        user_id = manager.ajouter_user("Alice", "alice@test.com", 25)

        resultat = manager.supprimer_user(user_id)
        assert resultat == True

        user = manager.obtenir_user(user_id)
        assert user is None

    def test_supprimer_user_inexistant(self, manager):
        """Test de suppression d'utilisateur inexistant"""
        resultat = manager.supprimer_user(999)
        assert resultat == False

    def test_desactiver_user_existant(self, manager):
        """Test de désactivation d'utilisateur existant"""
        user_id = manager.ajouter_user("Alice", "alice@test.com", 25)

        resultat = manager.desactiver_user(user_id)
        assert resultat == True

        user = manager.obtenir_user(user_id)
        assert user.actif == False

    def test_desactiver_user_inexistant(self, manager):
        """Test de désactivation d'utilisateur inexistant"""
        resultat = manager.desactiver_user(999)
        assert resultat == False

    def test_obtenir_users_actifs(self, manager):
        """Test d'obtention des utilisateurs actifs"""
        user_id1 = manager.ajouter_user("Alice", "alice@test.com", 25)
        user_id2 = manager.ajouter_user("Bob", "bob@test.com", 30)

        # Désactiver un utilisateur
        manager.desactiver_user(user_id1)

        users_actifs = manager.obtenir_users_actifs()
        assert len(users_actifs) == 1
        assert users_actifs[0].nom == "Bob"

    def test_obtenir_users_adultes(self, manager):
        """Test d'obtention des utilisateurs adultes"""
        manager.ajouter_user("Alice", "alice@test.com", 25)  # Adulte
        manager.ajouter_user("Bob", "bob@test.com", 16)     # Mineur
        manager.ajouter_user("Charlie", "charlie@test.com", 18)  # Adulte

        users_adultes = manager.obtenir_users_adultes()
        assert len(users_adultes) == 2
        noms = [user.nom for user in users_adultes]
        assert "Alice" in noms
        assert "Charlie" in noms
        assert "Bob" not in noms

    def test_statistiques_avec_users(self, manager):
        """Test des statistiques avec utilisateurs"""
        manager.ajouter_user("Alice", "alice@test.com", 25)    # Adulte, actif
        manager.ajouter_user("Bob", "bob@test.com", 16)       # Mineur, actif
        manager.ajouter_user("Charlie", "charlie@test.com", 70)  # Senior, actif

        # Désactiver un utilisateur
        user_id = manager.ajouter_user("David", "david@test.com", 30)
        manager.desactiver_user(user_id)

        stats = manager.obtenir_statistiques()
        assert stats["total"] == 4
        assert stats["adultes"] == 3  # Alice, Charlie, David
        assert stats["seniors"] == 1  # Charlie
        assert stats["actifs"] == 3   # Alice, Bob, Charlie

    def test_statistiques_sans_users(self, manager):
        """Test des statistiques sans utilisateurs"""
        stats = manager.obtenir_statistiques()
        assert stats["total"] == 0
        assert stats["adultes"] == 0
        assert stats["seniors"] == 0
        assert stats["actifs"] == 0

# Exécution avec couverture
# pytest --cov=user_manager --cov-report=html test_user_manager.py
```

## Analyse de la couverture

### Commandes utiles

```bash
# Rapport basique
coverage report

# Rapport avec lignes manquantes
coverage report --show-missing

# Rapport pour un fichier spécifique
coverage report user_manager.py

# Pourcentage uniquement
coverage report --format=total

# Échec si couverture < seuil
coverage report --fail-under=90
```

### Interprétation des résultats

```
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
user_manager.py    45      0   100%
---------------------------------------------
TOTAL              45      0   100%
```

- **Stmts** : Nombre total de lignes exécutables
- **Miss** : Nombre de lignes non testées
- **Cover** : Pourcentage de couverture
- **Missing** : Numéros des lignes non testées

## Couverture de branches

### Activation de la couverture de branches

```bash
coverage run --branch -m pytest
coverage report --show-missing
```

### Exemple avec branches

```python
def evaluer_etudiant(note, presence):
    """Évalue un étudiant selon sa note et sa présence"""
    if note >= 10 and presence >= 0.8:
        return "Admis"
    elif note >= 8 and presence >= 0.6:
        return "Rattrapage"
    else:
        return "Refusé"

# Tests couvrant toutes les branches
def test_evaluer_etudiant_complet():
    # Branche 1 : Admis
    assert evaluer_etudiant(15, 0.9) == "Admis"

    # Branche 2 : Rattrapage
    assert evaluer_etudiant(9, 0.7) == "Rattrapage"

    # Branche 3 : Refusé (note insuffisante)
    assert evaluer_etudiant(5, 0.9) == "Refusé"

    # Branche 4 : Refusé (présence insuffisante)
    assert evaluer_etudiant(15, 0.5) == "Refusé"

    # Branche 5 : Refusé (les deux insuffisants)
    assert evaluer_etudiant(5, 0.3) == "Refusé"
```

## Limites et bonnes pratiques

### Limites de la couverture

```python
# ❌ 100% de couverture mais bug présent !
def diviser_mal(a, b):
    if b != 0:
        return a / b
    return a / b  # Bug : division par zéro !

def test_diviser_mal():
    # Ce test donne 100% de couverture mais ne trouve pas le bug
    assert diviser_mal(10, 2) == 5
```

### Bonnes pratiques

#### 1. Viser 80-90% de couverture

```python
# ✅ Couverture raisonnable avec tests de qualité
def calculer_prix_total(articles, code_promo=None):
    if not articles:
        return 0

    total = sum(article.prix for article in articles)

    if code_promo == "REDUC10":
        total *= 0.9
    elif code_promo == "REDUC20":  # pragma: no cover
        # Code promo rare, difficile à tester
        total *= 0.8

    return round(total, 2)
```

#### 2. Se concentrer sur le code critique

```python
# ✅ Tests intensifs pour code critique
def traiter_paiement(montant, carte):
    """Fonction critique - tests exhaustifs requis"""
    # Validation stricte
    if montant <= 0:
        raise ValueError("Montant invalide")

    # Logique métier critique
    # ... tests complets nécessaires

def afficher_debug():  # pragma: no cover
    """Fonction de debug - peut être exclue"""
    print("Info de debug...")
```

#### 3. Qualité avant quantité

```python
# ✅ Tests de qualité avec assertions significatives
def test_fonction_critique():
    # Test du cas normal
    resultat = fonction_critique("input_valide")
    assert resultat.status == "success"
    assert resultat.data is not None

    # Test des cas d'erreur
    with pytest.raises(ValueError):
        fonction_critique("input_invalide")

    # Test des cas limites
    resultat_limite = fonction_critique("")
    assert resultat_limite.status == "empty"
```

## Intégration dans le workflow

### Pre-commit hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: coverage-check
        name: coverage check
        entry: coverage
        args: ['report', '--fail-under=80']
        language: system
        pass_filenames: false
```

### CI/CD avec GitHub Actions

```yaml
# .github/workflows/test.yml
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
        python-version: 3.9

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install coverage pytest-cov

    - name: Run tests with coverage
      run: |
        pytest --cov=src --cov-report=xml --cov-fail-under=80

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
```

## Exercices pratiques

### Exercice 1 : Analyser la couverture

```python
# calculator_advanced.py
import math

class CalculatriceAvancee:
    def __init__(self):
        self.historique = []

    def calculer(self, operation, a, b=None):
        """Effectue une opération mathématique"""
        if operation == "add":
            resultat = a + b
        elif operation == "sub":
            resultat = a - b
        elif operation == "mul":
            resultat = a * b
        elif operation == "div":
            if b == 0:
                raise ZeroDivisionError("Division par zéro")
            resultat = a / b
        elif operation == "sqrt":
            if a < 0:
                raise ValueError("Racine d'un nombre négatif")
            resultat = math.sqrt(a)
        elif operation == "pow":
            resultat = a ** b
        else:
            raise ValueError(f"Opération inconnue: {operation}")

        self.historique.append(f"{operation}: {resultat}")
        return resultat

    def obtenir_historique(self):
        return self.historique.copy()

    def effacer_historique(self):
        if self.historique:
            self.historique.clear()
            return True
        return False

# À vous !
# 1. Écrivez des tests pour cette classe
# 2. Mesurez la couverture
# 3. Identifiez les parties non testées
# 4. Complétez les tests pour atteindre 100%
```

### Exercice 2 : Optimiser les tests

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.code_promo = None

    def ajouter_item(self, nom, prix, quantite=1):
        if prix < 0:
            raise ValueError("Prix négatif")
        if quantite <= 0:
            raise ValueError("Quantité invalide")

        if nom in self.items:
            self.items[nom]['quantite'] += quantite
        else:
            self.items[nom] = {'prix': prix, 'quantite': quantite}

    def appliquer_promo(self, code):
        codes_valides = ["REDUC10", "REDUC20", "NOEL25"]
        if code in codes_valides:
            self.code_promo = code
            return True
        return False

    def calculer_total(self):
        total = sum(item['prix'] * item['quantite']
                   for item in self.items.values())

        if self.code_promo == "REDUC10":
            total *= 0.9
        elif self.code_promo == "REDUC20":
            total *= 0.8
        elif self.code_promo == "NOEL25":
            total *= 0.75

        return round(total, 2)

# À vous !
# 1. Analysez le code et identifiez tous les cas à tester
# 2. Écrivez des tests complets
# 3. Mesurez la couverture (devrait être 100%)
# 4. Vérifiez la couverture de branches
```

## Résumé

La couverture de code est un outil précieux mais qui doit être utilisé intelligemment :

### **Points clés :**
- **Mesure** : Pourcentage de code exécuté par les tests
- **Types** : Lignes, branches, fonctions
- **Outil** : coverage.py avec pytest-cov
- **Objectif** : 80-90% de couverture pour la plupart des projets

### **Bonnes pratiques :**
- **Qualité avant quantité** : 80% de tests excellents valent mieux que 100% de tests médiocres
- **Focus sur le critique** : Priorisez les parties importantes de votre code
- **Exclusions raisonnables** : Utilisez `pragma: no cover` pour le code de debug/logging
- **Couverture de branches** : Plus importante que la simple couverture de lignes
- **Intégration CI/CD** : Automatisez la vérification de couverture

### **Métriques utiles :**
- **80-90%** : Couverture cible pour la plupart des projets
- **95%+** : Pour le code critique (paiements, sécurité)
- **Moins important** : Code de logging, debug, scripts one-shot

### **Workflow recommandé :**
1. **Écrire** les tests pour les cas principaux
2. **Mesurer** la couverture initiale
3. **Identifier** les parties manquantes importantes
4. **Compléter** les tests pour ces parties
5. **Exclure** le code non critique si nécessaire
6. **Automatiser** la vérification en CI/CD

### **Outils essentiels :**
- `coverage run` : Exécuter avec mesure
- `coverage report` : Rapport textuel
- `coverage html` : Rapport visuel
- `pytest --cov` : Intégration avec pytest
- Configuration `.coveragerc` : Personnalisation

### **Signaux d'alarme :**
- Couverture qui diminue soudainement
- Nouveau code sans tests
- Branches importantes non testées
- Tests qui passent mais ne testent rien de significatif

## Cas d'usage avancés

### Couverture différentielle

Mesurer seulement les changements récents :

```bash
# Couverture depuis le dernier commit
coverage run -m pytest
git diff HEAD~1 --name-only | grep "\.py$" | xargs coverage report --include

# Avec diff-cover (outil externe)
pip install diff-cover
diff-cover coverage.xml --compare-branch=main
```

### Couverture par environnement

```python
# conftest.py
import pytest
import os

def pytest_configure(config):
    """Configuration différente selon l'environnement"""
    env = os.getenv('TEST_ENV', 'local')

    if env == 'ci':
        # En CI : couverture stricte
        config.option.cov_fail_under = 90
    elif env == 'local':
        # En local : plus permissif
        config.option.cov_fail_under = 80
```

### Couverture avec parallélisation

```bash
# Tests parallèles avec couverture
pytest -n auto --cov=src --cov-append

# Combinaison des rapports
coverage combine
coverage report
```

## Anti-patterns à éviter

### 1. L'obsession du 100%

```python
# ❌ Test inutile juste pour la couverture
def fonction_evidente(x):
    return x + 1

def test_fonction_evidente_inutile():
    # Test qui n'apporte aucune valeur
    assert fonction_evidente(1) == 2
    assert fonction_evidente(2) == 3
    assert fonction_evidente(0) == 1
    # ... 50 autres assertions identiques
```

### 2. Tests sans assertions

```python
# ❌ Couverture sans vérification
def test_sans_valeur():
    # Ce test atteint 100% de couverture mais ne teste rien !
    try:
        fonction_complexe()
    except:
        pass  # On ignore tout
```

### 3. Exclusions abusives

```python
# ❌ Trop d'exclusions pour "améliorer" les métriques
def fonction_importante(data):  # pragma: no cover
    # Cette fonction est importante mais difficile à tester
    # L'exclure n'est pas la solution !
    return process_critical_data(data)
```

## Couverture et refactoring

### Avant le refactoring

```bash
# Mesurer la couverture existante
coverage run -m pytest
coverage report > coverage_before.txt
```

### Pendant le refactoring

```python
# Garder les tests verts pendant les modifications
class TestsRegression:
    def test_comportement_preserve(self):
        """S'assurer que le comportement ne change pas"""
        # Tests qui vérifient que l'ancien et nouveau code
        # produisent les mêmes résultats
        assert nouvelle_fonction(input) == ancienne_fonction(input)
```

### Après le refactoring

```bash
# Vérifier que la couverture n'a pas régressé
coverage run -m pytest
coverage report > coverage_after.txt
diff coverage_before.txt coverage_after.txt
```

## Couverture et code legacy

### Stratégie d'amélioration progressive

```python
# legacy_code.py - Code existant sans tests
class LegacyProcessor:
    def __init__(self):
        self.config = load_complex_config()  # Difficile à tester
        self.cache = {}

    def process_data(self, data):
        # Fonction complexe de 200 lignes
        # Mélange logique métier et appels externes
        result = self.validate_data(data)
        if result:
            return self.transform_and_save(data)
        return None

    def validate_data(self, data):
        # 50 lignes de validation
        pass

    def transform_and_save(self, data):
        # 100 lignes de transformation + sauvegarde
        pass

# Stratégie : extraire et tester petit à petit
class DataValidator:
    """Nouvelle classe extraite, facile à tester"""

    def validate(self, data):
        # Logique de validation extraite
        if not data:
            return False
        if not isinstance(data, dict):
            return False
        return 'required_field' in data

# Tests pour la partie extraite
class TestDataValidator:
    def test_validate_data_valide(self):
        validator = DataValidator()
        data = {'required_field': 'value'}
        assert validator.validate(data) == True

    def test_validate_data_invalide(self):
        validator = DataValidator()
        assert validator.validate(None) == False
        assert validator.validate("not_dict") == False
        assert validator.validate({}) == False
```

### Couverture de régression

```python
# Tests de caractérisation pour code legacy
class TestLegacyBehavior:
    """Tests qui documentent le comportement actuel"""

    def test_process_data_comportement_actuel(self):
        """Test qui capture le comportement existant"""
        processor = LegacyProcessor()

        # Input/output connus du système existant
        input_data = load_test_data("legacy_input.json")
        expected_output = load_test_data("legacy_output.json")

        actual_output = processor.process_data(input_data)

        # On documente ce que fait actuellement le système
        assert actual_output == expected_output
```

## Métriques avancées

### Couverture pondérée par complexité

```python
# Mesure la couverture en tenant compte de la complexité
def complexite_cyclomatique(fonction):
    """Calcule la complexité d'une fonction"""
    # Plus une fonction est complexe, plus elle a besoin de tests
    pass

def calculer_couverture_ponderee(module):
    """Couverture pondérée par la complexité"""
    total_complexity = 0
    covered_complexity = 0

    for fonction in module.fonctions:
        complexity = complexite_cyclomatique(fonction)
        total_complexity += complexity

        if fonction.is_covered:
            covered_complexity += complexity

    return covered_complexity / total_complexity if total_complexity > 0 else 0
```

### Tendances de couverture

```python
# scripts/track_coverage.py
import json
import datetime
from pathlib import Path

def enregistrer_couverture(pourcentage):
    """Enregistre l'évolution de la couverture"""
    historique_file = Path("coverage_history.json")

    if historique_file.exists():
        with open(historique_file) as f:
            historique = json.load(f)
    else:
        historique = []

    historique.append({
        "date": datetime.datetime.now().isoformat(),
        "coverage": pourcentage,
        "commit": get_current_commit()
    })

    with open(historique_file, 'w') as f:
        json.dump(historique, f, indent=2)

def analyser_tendance():
    """Analyse la tendance de couverture"""
    with open("coverage_history.json") as f:
        historique = json.load(f)

    if len(historique) >= 2:
        derniere = historique[-1]["coverage"]
        precedente = historique[-2]["coverage"]

        if derniere < precedente:
            print(f"⚠️ Couverture en baisse : {precedente}% → {derniere}%")
        elif derniere > precedente:
            print(f"✅ Couverture en hausse : {precedente}% → {derniere}%")
        else:
            print(f"➡️ Couverture stable : {derniere}%")
```

## Configuration projet complète

### Structure de projet avec couverture

```
mon_projet/
├── src/
│   └── mon_app/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── .coveragerc
├── pytest.ini
├── requirements.txt
└── setup.py
```

### Configuration complète

```ini
# .coveragerc
[run]
source = src
branch = True
omit =
    */tests/*
    */venv/*
    */virtualenv/*
    setup.py
    */site-packages/*

[report]
precision = 2
show_missing = True
skip_covered = False
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:

[html]
directory = htmlcov
title = Mon Projet - Couverture de Code

[xml]
output = coverage.xml
```

```ini
# pytest.ini
[tool:pytest]
minversion = 6.0
addopts =
    -ra
    --strict-markers
    --strict-config
    --cov=src
    --cov-branch
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
    --cov-fail-under=85
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### Makefile pour automatisation

```makefile
# Makefile
.PHONY: test coverage coverage-html coverage-report clean

test:
	pytest

coverage:
	pytest --cov=src --cov-report=term-missing

coverage-html:
	pytest --cov=src --cov-report=html
	@echo "Rapport HTML généré dans htmlcov/index.html"

coverage-report:
	coverage report --show-missing

coverage-xml:
	pytest --cov=src --cov-report=xml

clean:
	rm -rf htmlcov/
	rm -f coverage.xml
	rm -f .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

check-coverage:
	@coverage report --fail-under=85 || (echo "❌ Couverture insuffisante" && exit 1)
	@echo "✅ Couverture suffisante"
```

## Intégration complète CI/CD

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests et Couverture

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest-cov codecov

    - name: Run tests with coverage
      run: |
        pytest --cov=src --cov-report=xml --cov-report=term

    - name: Check coverage threshold
      run: |
        coverage report --fail-under=85

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

    - name: Comment PR with coverage
      if: github.event_name == 'pull_request'
      uses: orgoro/coverage@v3
      with:
        coverageFile: coverage.xml
        token: ${{ secrets.GITHUB_TOKEN }}
```

### Pre-commit hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest-coverage
        name: pytest with coverage
        entry: pytest
        args: [--cov=src, --cov-fail-under=85]
        language: system
        pass_filenames: false
        always_run: true
```

## Monitoring et alertes

### Script de monitoring

```python
# scripts/coverage_monitor.py
import subprocess
import json
import sys
from pathlib import Path

def obtenir_couverture_actuelle():
    """Obtient le pourcentage de couverture actuel"""
    result = subprocess.run(
        ['coverage', 'json'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        data = json.loads(result.stdout)
        return data['totals']['percent_covered']
    return None

def verifier_seuils():
    """Vérifie les seuils de couverture"""
    couverture = obtenir_couverture_actuelle()

    if couverture is None:
        print("❌ Impossible d'obtenir la couverture")
        return False

    seuils = {
        'critique': 90,
        'avertissement': 80,
        'minimum': 70
    }

    print(f"📊 Couverture actuelle : {couverture:.1f}%")

    if couverture >= seuils['critique']:
        print("🟢 Excellente couverture !")
        return True
    elif couverture >= seuils['avertissement']:
        print("🟡 Bonne couverture")
        return True
    elif couverture >= seuils['minimum']:
        print("🟠 Couverture acceptable mais peut être améliorée")
        return True
    else:
        print("🔴 Couverture insuffisante")
        return False

if __name__ == '__main__':
    success = verifier_seuils()
    sys.exit(0 if success else 1)
```

### Webhook pour Slack/Discord

```python
# scripts/coverage_notification.py
import requests
import json

def notifier_couverture(webhook_url, couverture, precedente=None):
    """Envoie une notification de couverture"""

    if precedente is not None:
        if couverture > precedente:
            emoji = "📈"
            message = f"Couverture en hausse : {precedente:.1f}% → {couverture:.1f}%"
        elif couverture < precedente:
            emoji = "📉"
            message = f"Couverture en baisse : {precedente:.1f}% → {couverture:.1f}%"
        else:
            emoji = "➡️"
            message = f"Couverture stable : {couverture:.1f}%"
    else:
        emoji = "📊"
        message = f"Couverture actuelle : {couverture:.1f}%"

    payload = {
        "text": f"{emoji} {message}",
        "username": "Coverage Bot"
    }

    requests.post(webhook_url, json=payload)
```

## Conclusion

La couverture de code est un outil puissant mais qui doit être utilisé avec sagesse :

### **Points essentiels à retenir :**

1. **Qualité > Quantité** : Un test qui vérifie vraiment quelque chose vaut mieux que 10 tests superficiels

2. **Contexte important** : 100% n'est pas toujours nécessaire, 80-90% est souvent suffisant

3. **Outil, pas objectif** : La couverture guide mais ne remplace pas la réflexion

4. **Automatisation** : Intégrez la vérification dans votre workflow de développement

5. **Évolution** : Surveillez les tendances, pas seulement les valeurs absolues

### **Workflow recommandé :**
- Tests d'abord pour les fonctionnalités principales
- Mesure de couverture pour identifier les oublis
- Ajout de tests pour les parties critiques manquantes
- Exclusion raisonnée du code non-critique
- Intégration en CI/CD avec seuils appropriés

### **Erreurs à éviter :**
- Obsession du 100% sans considération de la valeur
- Tests écrits uniquement pour la métrique
- Exclusions abusives pour "améliorer" les chiffres
- Ignorer la couverture de branches
- Ne pas surveiller l'évolution dans le temps

La couverture de code vous aide à construire un code robuste et fiable. Utilisée intelligemment, elle devient un allié précieux pour la qualité de votre projet !

---

**À retenir :** La couverture de code, c'est comme un contrôle technique pour votre voiture : important pour la sécurité, mais ce n'est pas parce que tous les voyants sont au vert que vous êtes un bon conducteur !

⏭️
