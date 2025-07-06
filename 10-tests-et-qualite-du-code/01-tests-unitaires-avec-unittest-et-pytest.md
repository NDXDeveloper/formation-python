🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.1 : Tests unitaires avec unittest et pytest

## Introduction

Imaginez que vous êtes chef cuisinier et que vous préparez un plat complexe. Avant de servir le plat final, vous goûtez chaque sauce, vérifiez la cuisson de chaque ingrédient, testez l'assaisonnement. Les tests unitaires, c'est exactement la même chose : vous testez chaque "ingrédient" de votre code (chaque fonction) individuellement pour vous assurer qu'il fonctionne parfaitement.

Un test unitaire vérifie qu'une petite partie de votre code (généralement une fonction ou une méthode) fonctionne comme prévu dans différentes situations.

## Qu'est-ce qu'un test unitaire ?

### Définition simple
Un test unitaire est un petit programme qui :
1. **Appelle** une fonction avec des données spécifiques
2. **Vérifie** que le résultat correspond à ce qui est attendu
3. **Signale** si quelque chose ne va pas

### Exemple concret
```python
# Fonction à tester
def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

# Test unitaire pour cette fonction
def test_additionner():
    # On teste avec des valeurs connues
    resultat = additionner(2, 3)
    # On vérifie que le résultat est correct
    assert resultat == 5, f"Attendu 5, mais obtenu {resultat}"
    print("✅ Test réussi !")

# Exécution du test
test_additionner()
```

### Anatomie d'un bon test unitaire
Un bon test unitaire suit le pattern **AAA** :

- **Arrange** (Préparer) : Mettre en place les données de test
- **Act** (Agir) : Exécuter la fonction à tester
- **Assert** (Vérifier) : Contrôler que le résultat est correct

```python
def test_exemple_aaa():
    # ARRANGE - Préparer les données
    nombre1 = 10
    nombre2 = 5
    resultat_attendu = 15

    # ACT - Exécuter la fonction
    resultat_obtenu = additionner(nombre1, nombre2)

    # ASSERT - Vérifier le résultat
    assert resultat_obtenu == resultat_attendu
```

## Le module unittest (intégré à Python)

### Introduction à unittest
`unittest` est le framework de test intégré à Python. Il s'inspire de JUnit (Java) et suit le paradigme orienté objet.

### Premier test avec unittest

```python
import unittest

class TestCalculatrice(unittest.TestCase):
    """Tests pour les fonctions de calcul"""

    def test_additionner(self):
        """Test de l'addition"""
        # Test avec des nombres positifs
        self.assertEqual(additionner(2, 3), 5)

        # Test avec des nombres négatifs
        self.assertEqual(additionner(-1, -1), -2)

        # Test avec zéro
        self.assertEqual(additionner(0, 5), 5)

    def test_soustraire(self):
        """Test de la soustraction"""
        self.assertEqual(soustraire(10, 3), 7)
        self.assertEqual(soustraire(5, 10), -5)
        self.assertEqual(soustraire(0, 0), 0)

# Fonctions à tester
def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

# Exécution des tests
if __name__ == '__main__':
    unittest.main()
```

### Les assertions unittest les plus utiles

```python
import unittest

class TestAssertions(unittest.TestCase):

    def test_egalite(self):
        """Tests d'égalité"""
        self.assertEqual(2 + 2, 4)                    # Égalité
        self.assertNotEqual(2 + 2, 5)                 # Inégalité
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)  # Égalité avec flottants

    def test_verite(self):
        """Tests de vérité"""
        self.assertTrue(5 > 3)                        # Doit être True
        self.assertFalse(5 < 3)                       # Doit être False

    def test_presence(self):
        """Tests de présence"""
        self.assertIn('hello', 'hello world')         # Contient
        self.assertNotIn('bye', 'hello world')        # Ne contient pas

    def test_types(self):
        """Tests de types"""
        self.assertIsInstance(42, int)                # Vérifie le type
        self.assertIsNone(None)                       # Vérifie None
        self.assertIsNotNone("quelque chose")         # Vérifie not None

    def test_exceptions(self):
        """Tests d'exceptions"""
        with self.assertRaises(ZeroDivisionError):    # Doit lever une exception
            10 / 0

        with self.assertRaises(ValueError):
            int("pas_un_nombre")

if __name__ == '__main__':
    unittest.main()
```

### Organisation des tests avec unittest

```python
import unittest

class TestStringUtils(unittest.TestCase):
    """Tests pour les utilitaires de chaînes"""

    def setUp(self):
        """Méthode appelée avant chaque test"""
        self.test_string = "Hello World"
        self.empty_string = ""
        print("🔧 Préparation du test")

    def tearDown(self):
        """Méthode appelée après chaque test"""
        print("🧹 Nettoyage après le test")

    def test_mettre_en_majuscules(self):
        """Test de mise en majuscules"""
        resultat = mettre_en_majuscules(self.test_string)
        self.assertEqual(resultat, "HELLO WORLD")

    def test_compter_mots(self):
        """Test de comptage de mots"""
        self.assertEqual(compter_mots("hello world"), 2)
        self.assertEqual(compter_mots(""), 0)
        self.assertEqual(compter_mots("un"), 1)

    def test_inverser_chaine(self):
        """Test d'inversion de chaîne"""
        self.assertEqual(inverser_chaine("abc"), "cba")
        self.assertEqual(inverser_chaine(""), "")

# Fonctions à tester
def mettre_en_majuscules(texte):
    return texte.upper()

def compter_mots(texte):
    if not texte.strip():
        return 0
    return len(texte.split())

def inverser_chaine(texte):
    return texte[::-1]

if __name__ == '__main__':
    unittest.main(verbosity=2)  # Mode verbose pour plus de détails
```

## Pytest : Le framework moderne

### Pourquoi pytest ?
Pytest est plus moderne et plus simple qu'unittest :
- **Syntaxe plus simple** : Pas besoin de classes
- **Assertions plus claires** : `assert` standard de Python
- **Découverte automatique** des tests
- **Fixtures puissantes** pour la préparation des tests
- **Plugins riches** pour étendre les fonctionnalités

### Installation et premier test

```bash
pip install pytest
```

```python
# test_calculatrice_pytest.py

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustrait deux nombres"""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres"""
    return a * b

def diviser(a, b):
    """Divise deux nombres"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

# Tests avec pytest (plus simple !)
def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0
    assert additionner(0, 0) == 0

def test_soustraire():
    assert soustraire(5, 3) == 2
    assert soustraire(10, 15) == -5

def test_multiplier():
    assert multiplier(3, 4) == 12
    assert multiplier(0, 100) == 0
    assert multiplier(-2, 3) == -6

def test_diviser():
    assert diviser(10, 2) == 5
    assert diviser(9, 3) == 3

    # Test d'exception avec pytest
    import pytest
    with pytest.raises(ValueError):
        diviser(10, 0)
```

Exécution :
```bash
pytest test_calculatrice_pytest.py -v
```

### Tests paramétrés avec pytest

```python
import pytest

@pytest.mark.parametrize("a,b,attendu", [
    (2, 3, 5),      # Cas normal
    (0, 0, 0),      # Cas avec zéros
    (-1, 1, 0),     # Cas avec négatif
    (100, 200, 300) # Cas avec grands nombres
])
def test_additionner_parametres(a, b, attendu):
    """Test paramétré pour tester plusieurs cas d'un coup"""
    assert additionner(a, b) == attendu

@pytest.mark.parametrize("texte,attendu", [
    ("hello", "HELLO"),
    ("", ""),
    ("MiXeD cAsE", "MIXED CASE"),
    ("123", "123")
])
def test_majuscules_parametres(texte, attendu):
    assert mettre_en_majuscules(texte) == attendu

def mettre_en_majuscules(texte):
    return texte.upper()
```

### Fixtures pytest

Les fixtures permettent de préparer des données de test réutilisables :

```python
import pytest

# Fixture simple
@pytest.fixture
def donnees_test():
    """Fournit des données de test réutilisables"""
    return {
        'utilisateurs': ['Alice', 'Bob', 'Charlie'],
        'scores': [95, 87, 92],
        'actif': True
    }

# Fixture avec setup/teardown
@pytest.fixture
def fichier_temporaire():
    """Crée un fichier temporaire pour les tests"""
    import tempfile
    import os

    # Setup : création du fichier
    fd, nom_fichier = tempfile.mkstemp(suffix='.txt')
    with os.fdopen(fd, 'w') as f:
        f.write("Contenu de test")

    print(f"📄 Fichier créé : {nom_fichier}")
    yield nom_fichier  # Fournit le nom du fichier au test

    # Teardown : nettoyage
    os.unlink(nom_fichier)
    print(f"🗑️ Fichier supprimé : {nom_fichier}")

# Utilisation des fixtures
def test_avec_donnees(donnees_test):
    """Test utilisant la fixture donnees_test"""
    assert len(donnees_test['utilisateurs']) == 3
    assert donnees_test['actif'] == True
    assert max(donnees_test['scores']) == 95

def test_avec_fichier(fichier_temporaire):
    """Test utilisant la fixture fichier_temporaire"""
    with open(fichier_temporaire, 'r') as f:
        contenu = f.read()
    assert contenu == "Contenu de test"

# Fixture de classe (partagée entre tous les tests de la classe)
@pytest.fixture(scope="class")
def connexion_db():
    """Simule une connexion base de données (coûteuse à créer)"""
    print("🔌 Connexion à la base de données")
    connexion = {"status": "connected", "db": "test_db"}
    yield connexion
    print("🔌 Fermeture de la connexion")

class TestAvecDB:
    def test_lecture(self, connexion_db):
        assert connexion_db["status"] == "connected"

    def test_ecriture(self, connexion_db):
        assert connexion_db["db"] == "test_db"
```

## Exemple complet : Tests pour une classe

```python
# calculator.py - Code à tester
class Calculatrice:
    """Une calculatrice simple avec historique"""

    def __init__(self):
        self.historique = []

    def additionner(self, a, b):
        resultat = a + b
        self.historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def soustraire(self, a, b):
        resultat = a - b
        self.historique.append(f"{a} - {b} = {resultat}")
        return resultat

    def diviser(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro impossible")
        resultat = a / b
        self.historique.append(f"{a} / {b} = {resultat}")
        return resultat

    def obtenir_historique(self):
        return self.historique.copy()

    def effacer_historique(self):
        self.historique.clear()

    def dernier_calcul(self):
        if not self.historique:
            return None
        return self.historique[-1]
```

### Tests avec unittest

```python
# test_calculator_unittest.py
import unittest
from calculator import Calculatrice

class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        """Prépare une calculatrice propre pour chaque test"""
        self.calc = Calculatrice()

    def test_addition(self):
        """Test de l'addition"""
        resultat = self.calc.additionner(3, 7)
        self.assertEqual(resultat, 10)

    def test_soustraction(self):
        """Test de la soustraction"""
        resultat = self.calc.soustraire(10, 4)
        self.assertEqual(resultat, 6)

    def test_division_normale(self):
        """Test de division normale"""
        resultat = self.calc.diviser(15, 3)
        self.assertEqual(resultat, 5)

    def test_division_par_zero(self):
        """Test de division par zéro"""
        with self.assertRaises(ValueError) as context:
            self.calc.diviser(10, 0)
        self.assertIn("Division par zéro", str(context.exception))

    def test_historique(self):
        """Test de l'historique des calculs"""
        self.calc.additionner(2, 3)
        self.calc.soustraire(10, 5)

        historique = self.calc.obtenir_historique()
        self.assertEqual(len(historique), 2)
        self.assertIn("2 + 3 = 5", historique[0])
        self.assertIn("10 - 5 = 5", historique[1])

    def test_effacer_historique(self):
        """Test d'effacement de l'historique"""
        self.calc.additionner(1, 1)
        self.calc.effacer_historique()
        self.assertEqual(len(self.calc.obtenir_historique()), 0)

    def test_dernier_calcul(self):
        """Test du dernier calcul"""
        # Aucun calcul effectué
        self.assertIsNone(self.calc.dernier_calcul())

        # Après un calcul
        self.calc.additionner(5, 5)
        self.assertEqual(self.calc.dernier_calcul(), "5 + 5 = 10")

if __name__ == '__main__':
    unittest.main()
```

### Tests avec pytest

```python
# test_calculator_pytest.py
import pytest
from calculator import Calculatrice

@pytest.fixture
def calc():
    """Fixture qui fournit une calculatrice propre"""
    return Calculatrice()

def test_addition(calc):
    """Test de l'addition"""
    assert calc.additionner(3, 7) == 10

def test_soustraction(calc):
    """Test de la soustraction"""
    assert calc.soustraire(10, 4) == 6

def test_division_normale(calc):
    """Test de division normale"""
    assert calc.diviser(15, 3) == 5

def test_division_par_zero(calc):
    """Test de division par zéro"""
    with pytest.raises(ValueError, match="Division par zéro"):
        calc.diviser(10, 0)

def test_historique(calc):
    """Test de l'historique des calculs"""
    calc.additionner(2, 3)
    calc.soustraire(10, 5)

    historique = calc.obtenir_historique()
    assert len(historique) == 2
    assert "2 + 3 = 5" in historique[0]
    assert "10 - 5 = 5" in historique[1]

def test_effacer_historique(calc):
    """Test d'effacement de l'historique"""
    calc.additionner(1, 1)
    calc.effacer_historique()
    assert len(calc.obtenir_historique()) == 0

def test_dernier_calcul(calc):
    """Test du dernier calcul"""
    # Aucun calcul effectué
    assert calc.dernier_calcul() is None

    # Après un calcul
    calc.additionner(5, 5)
    assert calc.dernier_calcul() == "5 + 5 = 10"

# Tests paramétrés
@pytest.mark.parametrize("a,b,attendu", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50)
])
def test_addition_parametree(calc, a, b, attendu):
    """Test paramétré de l'addition"""
    assert calc.additionner(a, b) == attendu
```

## Comparaison unittest vs pytest

| Aspect | unittest | pytest |
|--------|----------|--------|
| **Syntaxe** | Classes + méthodes | Fonctions simples |
| **Assertions** | `self.assertEqual()` | `assert` standard |
| **Setup/Teardown** | `setUp()`/`tearDown()` | Fixtures |
| **Découverte** | `unittest.main()` | Automatique |
| **Paramétrage** | Complexe | `@pytest.mark.parametrize` |
| **Extensibilité** | Limitée | Plugins nombreux |
| **Courbe d'apprentissage** | Plus raide | Plus douce |

## Bonnes pratiques pour les tests unitaires

### 1. Nommage des tests

```python
# ✅ Bon nommage - décrit ce qui est testé
def test_additionner_nombres_positifs_retourne_somme():
    pass

def test_diviser_par_zero_leve_exception():
    pass

def test_liste_vide_retourne_zero_elements():
    pass

# ❌ Mauvais nommage - peu informatif
def test_fonction1():
    pass

def test_cas_special():
    pass
```

### 2. Tests indépendants

```python
# ✅ Bon - chaque test est indépendant
def test_ajouter_utilisateur():
    users = []
    ajouter_utilisateur(users, "Alice")
    assert len(users) == 1

def test_supprimer_utilisateur():
    users = ["Alice", "Bob"]  # Données propres
    supprimer_utilisateur(users, "Alice")
    assert "Alice" not in users

# ❌ Mauvais - tests dépendants
users_global = []

def test_ajouter_utilisateur_dependant():
    ajouter_utilisateur(users_global, "Alice")
    assert len(users_global) == 1

def test_supprimer_utilisateur_dependant():
    # Ce test échoue si le précédent n'a pas tourné !
    supprimer_utilisateur(users_global, "Alice")
    assert len(users_global) == 0
```

### 3. Tests lisibles et maintenables

```python
# ✅ Test clair et bien structuré
def test_calculer_prix_avec_remise():
    # ARRANGE
    prix_initial = 100
    taux_remise = 0.1  # 10%
    prix_attendu = 90

    # ACT
    prix_final = calculer_prix_avec_remise(prix_initial, taux_remise)

    # ASSERT
    assert prix_final == prix_attendu, f"Attendu {prix_attendu}, obtenu {prix_final}"

# ❌ Test confus
def test_prix():
    assert calculer_prix_avec_remise(100, 0.1) == 90
```

## Exercices pratiques

### Exercice 1 : Testez une fonction simple

```python
def est_palindrome(texte):
    """
    Vérifie si un texte est un palindrome (se lit pareil dans les deux sens)
    Ignore la casse et les espaces
    """
    # À vous de compléter cette fonction !
    pass

# Écrivez des tests pour cette fonction :
# - Testez avec "radar" (doit retourner True)
# - Testez avec "hello" (doit retourner False)
# - Testez avec "A man a plan a canal Panama" (True)
# - Testez avec une chaîne vide
# - Testez avec un seul caractère
```

### Exercice 2 : Testez une classe

```python
class CompteBancaire:
    def __init__(self, solde_initial=0):
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")
        self.solde = solde_initial
        self.historique = []

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant
        self.historique.append(f"Dépôt: +{montant}")
        return self.solde

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
        self.historique.append(f"Retrait: -{montant}")
        return self.solde

    def obtenir_solde(self):
        return self.solde

# Écrivez des tests complets pour cette classe !
# Testez tous les cas : normaux, limites, et d'erreur
```

### Exercice 3 : Tests paramétrés

```python
def calculer_imc(poids, taille):
    """
    Calcule l'Indice de Masse Corporelle
    IMC = poids (kg) / taille (m)²
    """
    if poids <= 0 or taille <= 0:
        raise ValueError("Le poids et la taille doivent être positifs")
    return round(poids / (taille ** 2), 2)

# Créez des tests paramétrés avec pytest pour tester :
# Plusieurs combinaisons de poids/taille
# Les cas d'erreur (valeurs négatives ou nulles)
```

## Résumé

Les tests unitaires sont essentiels pour créer du code fiable :

### **Concepts clés :**
- **Tests unitaires** : Vérifient une unité de code isolément
- **Pattern AAA** : Arrange, Act, Assert
- **Indépendance** : Chaque test doit être autonome
- **Lisibilité** : Les tests sont aussi de la documentation

### **unittest vs pytest :**
- **unittest** : Intégré à Python, orienté objet, plus verbeux
- **pytest** : Plus moderne, syntaxe simple, fixtures puissantes

### **Bonnes pratiques :**
- Noms de tests descriptifs
- Tests indépendants et reproductibles
- Tester les cas normaux ET les cas d'erreur
- Un test = une seule chose vérifiée

### **Workflow de test :**
1. Écrire du code
2. Écrire des tests
3. Exécuter les tests
4. Corriger si nécessaire
5. Refactorer en confiance

Les tests unitaires vous donnent la confiance nécessaire pour modifier et améliorer votre code. Ils sont votre filet de sécurité !

Dans la section suivante, nous verrons comment gérer les dépendances externes avec les mocks et fixtures avancées.

---

**À retenir :** Un code sans tests, c'est comme conduire sans ceinture de sécurité. Ça peut marcher, mais quand ça casse, ça fait mal !

⏭️
