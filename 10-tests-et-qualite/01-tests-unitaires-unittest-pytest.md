🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.1 Tests unitaires avec unittest et pytest

## Introduction aux tests unitaires

### Qu'est-ce qu'un test unitaire ?

Un **test unitaire** est un morceau de code qui vérifie qu'une petite partie de votre programme (une "unité") fonctionne correctement. Cette unité peut être une fonction, une méthode ou une classe.

**Analogie simple** : Imaginez que vous construisez une voiture. Avant d'assembler toutes les pièces, vous testez chaque composant individuellement (les freins, le moteur, les phares, etc.). Les tests unitaires font la même chose avec votre code.

### Pourquoi écrire des tests ?

Les tests unitaires offrent plusieurs avantages importants :

1. **Confiance** : Vous savez que votre code fonctionne comme prévu
2. **Documentation** : Les tests montrent comment utiliser votre code
3. **Détection précoce des bugs** : Les erreurs sont trouvées rapidement
4. **Facilite les modifications** : Vous pouvez modifier du code sans craindre de tout casser
5. **Qualité du code** : Écrire du code testable encourage les bonnes pratiques

### Principe de base

Un test unitaire suit généralement trois étapes (pattern AAA) :

1. **Arrange** (Préparer) : Configurer les données et l'environnement
2. **Act** (Agir) : Exécuter le code à tester
3. **Assert** (Vérifier) : Vérifier que le résultat est correct

---

## unittest : Le module intégré de Python

`unittest` est le framework de tests inclus dans la bibliothèque standard de Python. Vous n'avez rien à installer, il est déjà disponible !

### Structure de base avec unittest

Voici un exemple simple pour comprendre la structure :

```python
# fichier: calculatrice.py
def additionner(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraire(a, b):
    """Soustrait b de a."""
    return a - b

def diviser(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
```

Maintenant, créons les tests :

```python
# fichier: test_calculatrice.py
import unittest
from calculatrice import additionner, soustraire, diviser

class TestCalculatrice(unittest.TestCase):
    """Tests pour les fonctions de calculatrice."""

    def test_additionner(self):
        """Teste l'addition de deux nombres."""
        # Arrange
        a = 5
        b = 3

        # Act
        resultat = additionner(a, b)

        # Assert
        self.assertEqual(resultat, 8)

    def test_soustraire(self):
        """Teste la soustraction de deux nombres."""
        resultat = soustraire(10, 4)
        self.assertEqual(resultat, 6)

    def test_diviser(self):
        """Teste la division de deux nombres."""
        resultat = diviser(10, 2)
        self.assertEqual(resultat, 5.0)

    def test_diviser_par_zero(self):
        """Teste que diviser par zéro lève une exception."""
        with self.assertRaises(ValueError):
            diviser(10, 0)

# Permet d'exécuter les tests si le fichier est lancé directement
if __name__ == '__main__':
    unittest.main()
```

### Exécuter les tests unittest

Pour exécuter vos tests, utilisez l'une de ces commandes dans votre terminal :

```bash
# Exécuter un fichier de tests spécifique
python test_calculatrice.py

# Découvrir et exécuter tous les tests
python -m unittest discover

# Exécuter avec plus de détails (mode verbose)
python -m unittest test_calculatrice.py -v
```

### Les assertions principales de unittest

Les assertions sont les méthodes qui vérifient vos résultats :

```python
import unittest

class TestAssertions(unittest.TestCase):

    def test_egalite(self):
        """Vérifie l'égalité."""
        self.assertEqual(2 + 2, 4)
        self.assertEqual("hello", "hello")

    def test_inegalite(self):
        """Vérifie l'inégalité."""
        self.assertNotEqual(5, 3)

    def test_booleen(self):
        """Vérifie les valeurs booléennes."""
        self.assertTrue(1 < 2)
        self.assertFalse(5 < 3)

    def test_none(self):
        """Vérifie les valeurs None."""
        valeur = None
        self.assertIsNone(valeur)

        autre_valeur = "quelque chose"
        self.assertIsNotNone(autre_valeur)

    def test_appartenance(self):
        """Vérifie l'appartenance à une collection."""
        liste = [1, 2, 3, 4, 5]
        self.assertIn(3, liste)
        self.assertNotIn(10, liste)

    def test_comparaison_numerique(self):
        """Vérifie les comparaisons numériques."""
        self.assertGreater(5, 3)  # 5 > 3
        self.assertLess(2, 10)    # 2 < 10
        self.assertGreaterEqual(5, 5)  # 5 >= 5
        self.assertLessEqual(3, 4)     # 3 <= 4

    def test_approximation(self):
        """Vérifie l'égalité approximative pour les nombres flottants."""
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
```

### setUp et tearDown : Préparer et nettoyer

Souvent, vous devez préparer des données avant chaque test et nettoyer après. Les méthodes `setUp()` et `tearDown()` sont là pour ça :

```python
import unittest

class TestAvecPreparation(unittest.TestCase):

    def setUp(self):
        """Appelée AVANT chaque test."""
        print("Préparation du test...")
        self.liste = [1, 2, 3, 4, 5]
        self.dictionnaire = {"nom": "Alice", "age": 30}

    def tearDown(self):
        """Appelée APRÈS chaque test."""
        print("Nettoyage après le test...")
        self.liste = None
        self.dictionnaire = None

    def test_liste(self):
        """Teste la liste préparée."""
        self.assertEqual(len(self.liste), 5)
        self.assertIn(3, self.liste)

    def test_dictionnaire(self):
        """Teste le dictionnaire préparé."""
        self.assertEqual(self.dictionnaire["nom"], "Alice")
        self.assertEqual(self.dictionnaire["age"], 30)
```

### Exemple complet : Tester une classe

Voici un exemple plus réaliste avec une classe :

```python
# fichier: utilisateur.py
class Utilisateur:
    """Représente un utilisateur."""

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.actif = True

    def desactiver(self):
        """Désactive l'utilisateur."""
        self.actif = False

    def activer(self):
        """Active l'utilisateur."""
        self.actif = True

    def changer_email(self, nouvel_email):
        """Change l'email de l'utilisateur."""
        if "@" not in nouvel_email:
            raise ValueError("Email invalide")
        self.email = nouvel_email

    def __str__(self):
        statut = "actif" if self.actif else "inactif"
        return f"{self.nom} ({self.email}) - {statut}"
```

Tests correspondants :

```python
# fichier: test_utilisateur.py
import unittest
from utilisateur import Utilisateur

class TestUtilisateur(unittest.TestCase):

    def setUp(self):
        """Crée un utilisateur pour chaque test."""
        self.utilisateur = Utilisateur("Alice", "alice@example.com")

    def test_creation_utilisateur(self):
        """Teste la création d'un utilisateur."""
        self.assertEqual(self.utilisateur.nom, "Alice")
        self.assertEqual(self.utilisateur.email, "alice@example.com")
        self.assertTrue(self.utilisateur.actif)

    def test_desactiver_utilisateur(self):
        """Teste la désactivation d'un utilisateur."""
        self.utilisateur.desactiver()
        self.assertFalse(self.utilisateur.actif)

    def test_activer_utilisateur(self):
        """Teste l'activation d'un utilisateur."""
        self.utilisateur.desactiver()
        self.utilisateur.activer()
        self.assertTrue(self.utilisateur.actif)

    def test_changer_email_valide(self):
        """Teste le changement d'email avec un email valide."""
        nouvel_email = "alice.nouveau@example.com"
        self.utilisateur.changer_email(nouvel_email)
        self.assertEqual(self.utilisateur.email, nouvel_email)

    def test_changer_email_invalide(self):
        """Teste que changer l'email avec un email invalide lève une exception."""
        with self.assertRaises(ValueError):
            self.utilisateur.changer_email("email_invalide")

    def test_representation_string(self):
        """Teste la représentation en chaîne de caractères."""
        resultat = str(self.utilisateur)
        self.assertIn("Alice", resultat)
        self.assertIn("actif", resultat)

if __name__ == '__main__':
    unittest.main()
```

---

## pytest : Un framework de tests moderne

`pytest` est un framework de tests externe très populaire qui simplifie l'écriture de tests avec une syntaxe plus simple et des fonctionnalités puissantes.

### Installation de pytest

```bash
# Installation avec pip
pip install pytest

# Vérifier l'installation
pytest --version
```

### Pourquoi choisir pytest ?

1. **Syntaxe plus simple** : Pas besoin de classes ou de self
2. **Assertions naturelles** : Utilisez simplement `assert`
3. **Meilleurs messages d'erreur** : Plus détaillés et clairs
4. **Fixtures puissantes** : Gestion avancée des données de test
5. **Plugins riches** : Écosystème étendu

### Structure de base avec pytest

Reprenons notre calculatrice avec pytest :

```python
# fichier: calculatrice.py (identique)
def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
```

Tests avec pytest (beaucoup plus simple !) :

```python
# fichier: test_calculatrice_pytest.py
import pytest
from calculatrice import additionner, soustraire, diviser

def test_additionner():
    """Teste l'addition de deux nombres."""
    assert additionner(5, 3) == 8
    assert additionner(-1, 1) == 0
    assert additionner(0, 0) == 0

def test_soustraire():
    """Teste la soustraction de deux nombres."""
    assert soustraire(10, 4) == 6
    assert soustraire(5, 10) == -5

def test_diviser():
    """Teste la division de deux nombres."""
    assert diviser(10, 2) == 5.0
    assert diviser(9, 3) == 3.0

def test_diviser_par_zero():
    """Teste que diviser par zéro lève une exception."""
    with pytest.raises(ValueError):
        diviser(10, 0)
```

### Exécuter les tests pytest

```bash
# Exécuter tous les tests
pytest

# Exécuter avec plus de détails
pytest -v

# Exécuter un fichier spécifique
pytest test_calculatrice_pytest.py

# Exécuter un test spécifique
pytest test_calculatrice_pytest.py::test_additionner

# Afficher les print() dans les tests
pytest -s
```

### Assertions avec pytest

Avec pytest, vous utilisez simplement le mot-clé `assert` de Python :

```python
def test_assertions_basiques():
    """Démontre les assertions de base avec pytest."""
    # Égalité
    assert 2 + 2 == 4
    assert "hello" == "hello"

    # Inégalité
    assert 5 != 3

    # Booléens
    assert True
    assert not False

    # Appartenance
    assert 3 in [1, 2, 3, 4]
    assert "a" in "abcd"

    # Comparaisons
    assert 5 > 3
    assert 2 < 10

    # None
    assert None is None
    assert "something" is not None

def test_approximation():
    """Teste l'égalité approximative."""
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 3.141592 == pytest.approx(3.14, abs=0.01)
```

### Fixtures : Préparer des données réutilisables

Les **fixtures** sont la façon dont pytest gère la préparation des données de test. Elles sont plus flexibles que `setUp()` et `tearDown()` :

```python
import pytest

@pytest.fixture
def liste_nombres():
    """Fixture qui fournit une liste de nombres."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def utilisateur_test():
    """Fixture qui crée un utilisateur de test."""
    from utilisateur import Utilisateur
    return Utilisateur("Bob", "bob@example.com")

def test_avec_liste(liste_nombres):
    """Teste en utilisant la fixture liste_nombres."""
    assert len(liste_nombres) == 5
    assert sum(liste_nombres) == 15

def test_avec_utilisateur(utilisateur_test):
    """Teste en utilisant la fixture utilisateur_test."""
    assert utilisateur_test.nom == "Bob"
    assert utilisateur_test.actif is True
```

### Fixtures avec setup et teardown

Vous pouvez créer des fixtures qui font du nettoyage après utilisation :

```python
import pytest

@pytest.fixture
def fichier_temporaire():
    """Crée un fichier temporaire et le supprime après le test."""
    # Setup : créer le fichier
    nom_fichier = "test_temp.txt"
    with open(nom_fichier, "w") as f:
        f.write("contenu de test")

    # Fournir le nom du fichier au test
    yield nom_fichier

    # Teardown : supprimer le fichier
    import os
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)

def test_lecture_fichier(fichier_temporaire):
    """Teste la lecture du fichier temporaire."""
    with open(fichier_temporaire, "r") as f:
        contenu = f.read()
    assert contenu == "contenu de test"
```

### Paramétrer vos tests

pytest permet de tester facilement plusieurs cas avec le même code :

```python
import pytest
from calculatrice import additionner

@pytest.mark.parametrize("a, b, attendu", [
    (1, 1, 2),
    (2, 3, 5),
    (10, -5, 5),
    (0, 0, 0),
    (-3, -7, -10),
])
def test_additionner_plusieurs_cas(a, b, attendu):
    """Teste l'addition avec plusieurs jeux de données."""
    assert additionner(a, b) == attendu
```

Ce test sera exécuté 5 fois avec des valeurs différentes !

### Exemple complet avec pytest

Voici notre classe Utilisateur testée avec pytest :

```python
# fichier: test_utilisateur_pytest.py
import pytest
from utilisateur import Utilisateur

@pytest.fixture
def utilisateur():
    """Fixture qui crée un utilisateur de test."""
    return Utilisateur("Alice", "alice@example.com")

def test_creation_utilisateur(utilisateur):
    """Teste la création d'un utilisateur."""
    assert utilisateur.nom == "Alice"
    assert utilisateur.email == "alice@example.com"
    assert utilisateur.actif is True

def test_desactiver_utilisateur(utilisateur):
    """Teste la désactivation d'un utilisateur."""
    utilisateur.desactiver()
    assert utilisateur.actif is False

def test_activer_utilisateur(utilisateur):
    """Teste l'activation d'un utilisateur."""
    utilisateur.desactiver()
    utilisateur.activer()
    assert utilisateur.actif is True

def test_changer_email_valide(utilisateur):
    """Teste le changement d'email avec un email valide."""
    nouvel_email = "alice.nouveau@example.com"
    utilisateur.changer_email(nouvel_email)
    assert utilisateur.email == nouvel_email

def test_changer_email_invalide(utilisateur):
    """Teste que changer l'email avec un email invalide lève une exception."""
    with pytest.raises(ValueError, match="Email invalide"):
        utilisateur.changer_email("email_invalide")

def test_representation_string(utilisateur):
    """Teste la représentation en chaîne de caractères."""
    resultat = str(utilisateur)
    assert "Alice" in resultat
    assert "actif" in resultat

@pytest.mark.parametrize("nom, email", [
    ("Bob", "bob@test.com"),
    ("Charlie", "charlie@example.org"),
    ("Diana", "diana@mail.net"),
])
def test_creation_plusieurs_utilisateurs(nom, email):
    """Teste la création de plusieurs utilisateurs."""
    utilisateur = Utilisateur(nom, email)
    assert utilisateur.nom == nom
    assert utilisateur.email == email
    assert utilisateur.actif is True
```

---

## unittest vs pytest : Comparaison

### Tableau comparatif

| Aspect | unittest | pytest |
|--------|----------|--------|
| Installation | Inclus dans Python | Nécessite installation |
| Syntaxe | Classes + méthodes | Fonctions simples |
| Assertions | self.assertEqual() | assert == |
| Setup/Teardown | Méthodes setUp/tearDown | Fixtures avec yield |
| Messages d'erreur | Basiques | Très détaillés |
| Paramétrage | Complexe | Simple avec @parametrize |
| Courbe d'apprentissage | Plus raide | Plus douce |

### Exemple côte à côte

**unittest :**
```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.nombre = 10

    def test_addition(self):
        self.assertEqual(self.nombre + 5, 15)
```

**pytest :**
```python
import pytest

@pytest.fixture
def nombre():
    return 10

def test_addition(nombre):
    assert nombre + 5 == 15
```

---

## Bonnes pratiques pour les tests

### 1. Nommage des tests

Utilisez des noms descriptifs qui expliquent ce qui est testé :

```python
# ✅ Bon
def test_utilisateur_peut_se_connecter_avec_credentials_valides():
    pass

def test_diviser_par_zero_leve_value_error():
    pass

# ❌ Moins bon
def test_login():
    pass

def test_1():
    pass
```

### 2. Un test = Une vérification

Chaque test devrait vérifier une seule chose :

```python
# ✅ Bon - tests séparés
def test_utilisateur_creation_nom():
    utilisateur = Utilisateur("Alice", "alice@test.com")
    assert utilisateur.nom == "Alice"

def test_utilisateur_creation_email():
    utilisateur = Utilisateur("Alice", "alice@test.com")
    assert utilisateur.email == "alice@test.com"

# ❌ Moins bon - tout dans un test
def test_utilisateur_creation():
    utilisateur = Utilisateur("Alice", "alice@test.com")
    assert utilisateur.nom == "Alice"
    assert utilisateur.email == "alice@test.com"
    assert utilisateur.actif is True
    # ... trop de vérifications
```

### 3. Tests indépendants

Chaque test doit pouvoir s'exécuter seul, dans n'importe quel ordre :

```python
# ✅ Bon - chaque test est indépendant
def test_addition():
    assert additionner(2, 3) == 5

def test_soustraction():
    assert soustraire(5, 3) == 2

# ❌ Mauvais - les tests dépendent l'un de l'autre
compteur = 0

def test_incrementer():
    global compteur
    compteur += 1
    assert compteur == 1

def test_incrementer_encore():  # Dépend du test précédent !
    global compteur
    compteur += 1
    assert compteur == 2
```

### 4. Organisation des fichiers

Structure recommandée pour votre projet :

```
mon_projet/
├── src/
│   ├── __init__.py
│   ├── calculatrice.py
│   └── utilisateur.py
├── tests/
│   ├── __init__.py
│   ├── test_calculatrice.py
│   └── test_utilisateur.py
├── requirements.txt
└── README.md
```

### 5. Couverture des cas limites

N'oubliez pas de tester les cas spéciaux :

```python
def test_cas_normaux():
    """Teste les cas d'utilisation normaux."""
    assert additionner(2, 3) == 5

def test_cas_limites():
    """Teste les cas limites."""
    assert additionner(0, 0) == 0  # Zéros
    assert additionner(-5, 5) == 0  # Nombres opposés
    assert additionner(1000000, 1000000) == 2000000  # Grands nombres

def test_cas_erreur():
    """Teste les cas d'erreur."""
    with pytest.raises(TypeError):
        additionner("texte", 5)  # Type invalide
```

---

## Quand utiliser unittest et quand utiliser pytest ?

### Utilisez unittest si :

- Vous travaillez sur un projet existant qui utilise déjà unittest
- Vous ne voulez pas ajouter de dépendances externes
- Vous préférez une approche orientée objet pour vos tests
- Votre équipe est plus à l'aise avec unittest

### Utilisez pytest si :

- Vous démarrez un nouveau projet
- Vous voulez une syntaxe plus simple et claire
- Vous avez besoin de fixtures avancées
- Vous voulez de meilleurs messages d'erreur
- Vous souhaitez utiliser le paramétrage de tests facilement

**Conseil pour débutants** : Commencez avec **pytest** ! Sa syntaxe est plus simple et intuitive, ce qui facilite l'apprentissage des concepts de tests.

---

## Mini-projet : Application de la théorie

Imaginons une classe simple pour gérer un panier d'achat :

```python
# fichier: panier.py
class Panier:
    """Représente un panier d'achat."""

    def __init__(self):
        self.articles = []

    def ajouter(self, article, prix, quantite=1):
        """Ajoute un article au panier."""
        if prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        if quantite < 1:
            raise ValueError("La quantité doit être au moins 1")

        self.articles.append({
            "article": article,
            "prix": prix,
            "quantite": quantite
        })

    def total(self):
        """Calcule le total du panier."""
        return sum(item["prix"] * item["quantite"] for item in self.articles)

    def nombre_articles(self):
        """Retourne le nombre total d'articles."""
        return sum(item["quantite"] for item in self.articles)

    def vider(self):
        """Vide le panier."""
        self.articles = []
```

Tests correspondants avec pytest :

```python
# fichier: test_panier.py
import pytest
from panier import Panier

@pytest.fixture
def panier():
    """Fixture qui crée un panier vide."""
    return Panier()

def test_panier_vide_au_depart(panier):
    """Teste qu'un nouveau panier est vide."""
    assert len(panier.articles) == 0
    assert panier.total() == 0
    assert panier.nombre_articles() == 0

def test_ajouter_un_article(panier):
    """Teste l'ajout d'un article."""
    panier.ajouter("Pomme", 2.50, 3)
    assert len(panier.articles) == 1
    assert panier.nombre_articles() == 3

def test_calculer_total(panier):
    """Teste le calcul du total."""
    panier.ajouter("Pomme", 2.50, 2)  # 5.00
    panier.ajouter("Orange", 3.00, 1)  # 3.00
    assert panier.total() == 8.00

def test_ajouter_prix_negatif(panier):
    """Teste qu'on ne peut pas ajouter un article avec un prix négatif."""
    with pytest.raises(ValueError, match="prix"):
        panier.ajouter("Article", -10, 1)

def test_ajouter_quantite_zero(panier):
    """Teste qu'on ne peut pas ajouter une quantité nulle."""
    with pytest.raises(ValueError, match="quantité"):
        panier.ajouter("Article", 10, 0)

def test_vider_panier(panier):
    """Teste le vidage du panier."""
    panier.ajouter("Pomme", 2.50, 2)
    panier.ajouter("Orange", 3.00, 1)
    panier.vider()
    assert len(panier.articles) == 0
    assert panier.total() == 0

@pytest.mark.parametrize("article, prix, quantite, total_attendu", [
    ("Pomme", 2.00, 1, 2.00),
    ("Orange", 3.50, 2, 7.00),
    ("Banane", 1.50, 5, 7.50),
])
def test_calcul_total_parametrise(panier, article, prix, quantite, total_attendu):
    """Teste le calcul du total avec différents articles."""
    panier.ajouter(article, prix, quantite)
    assert panier.total() == total_attendu
```

---

## Résumé

### Points clés à retenir

1. **Les tests unitaires** vérifient que chaque partie de votre code fonctionne correctement
2. **unittest** est inclus dans Python, orienté objet, utilise des assertions spéciales
3. **pytest** nécessite une installation, plus simple, utilise `assert` directement
4. **Les fixtures** (pytest) ou `setUp/tearDown` (unittest) préparent les données de test
5. **Un bon test** est indépendant, clair, et teste une seule chose
6. **Testez les cas normaux, limites et d'erreur** pour une couverture complète

### Commandes essentielles

```bash
# unittest
python -m unittest discover
python -m unittest test_fichier.py -v

# pytest
pytest
pytest -v
pytest test_fichier.py::test_nom
pytest -s  # Affiche les print()
```

### Prochaines étapes

Une fois à l'aise avec les tests unitaires, vous pourrez explorer :

- Le **mocking** pour simuler des dépendances (section 10.2)
- La **couverture de code** pour mesurer ce qui est testé (section 10.3)
- Les tests d'intégration qui testent plusieurs composants ensemble
- Le TDD (Test-Driven Development) - écrire les tests avant le code

---

## Ressources complémentaires

- Documentation officielle unittest : https://docs.python.org/3/library/unittest.html
- Documentation officielle pytest : https://docs.pytest.org/
- Real Python - Guide sur les tests : https://realpython.com/python-testing/
- PEP 8 (guide de style Python) : https://pep8.org/

Bonne continuation dans votre apprentissage des tests ! 🚀

⏭️ [Mocking et fixtures](/10-tests-et-qualite/02-mocking-et-fixtures.md)
