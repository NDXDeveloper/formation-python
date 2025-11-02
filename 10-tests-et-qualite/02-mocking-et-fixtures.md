🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.2 Mocking et fixtures

## Introduction : Pourquoi le mocking ?

### Le problème des dépendances externes

Imaginez que vous testez une fonction qui :
- Envoie un email
- Fait un appel à une API externe
- Lit/écrit dans une base de données
- Télécharge un fichier depuis Internet

**Le problème** : Vous ne voulez pas que vos tests :
- Envoient vraiment des emails à chaque exécution
- Consomment des quotas d'API
- Modifient une vraie base de données
- Dépendent d'une connexion Internet

**La solution** : Le **mocking** !

### Qu'est-ce que le mocking ?

Le **mocking** (ou "simulation" en français) consiste à remplacer temporairement des parties de votre code par des versions "factices" pendant les tests.

**Analogie** : Imaginez que vous testez une voiture. Vous n'allez pas conduire sur une vraie autoroute à 130 km/h ! À la place, vous utilisez un simulateur qui imite la route, le vent, les autres voitures, etc. C'est exactement ce que fait le mocking pour votre code.

### Qu'est-ce qu'une fixture ?

Une **fixture** est un ensemble de données ou d'objets préparés pour être utilisés dans vos tests. C'est comme préparer tous les ingrédients avant de cuisiner.

**Analogie** : Avant de tourner une scène de film, on prépare le décor, les costumes, l'éclairage. Les fixtures font la même chose pour vos tests : elles préparent l'environnement.

---

## Les fixtures en détail

### Fixtures avec pytest

Les fixtures pytest sont la manière la plus élégante et puissante de préparer des données de test.

#### Fixture basique

```python
import pytest

@pytest.fixture
def nombre():
    """Fixture simple qui retourne un nombre."""
    return 42

def test_avec_fixture(nombre):
    """Test qui utilise la fixture."""
    assert nombre == 42
    assert nombre * 2 == 84
```

#### Fixture qui crée un objet

```python
import pytest

class Compte:
    """Représente un compte bancaire."""

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Dépose de l'argent."""
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
    """Fixture qui crée un compte de test."""
    return Compte("Alice", solde=1000)

def test_deposer(compte):
    """Teste le dépôt d'argent."""
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
```

#### Fixtures avec setup et teardown

Les fixtures peuvent effectuer du nettoyage après le test :

```python
import pytest
import tempfile
import os

@pytest.fixture
def fichier_temp():
    """Crée un fichier temporaire et le supprime après."""
    # Setup : création du fichier
    fd, chemin = tempfile.mkstemp(suffix=".txt")
    os.write(fd, b"Contenu initial")
    os.close(fd)

    print(f"\n[Setup] Fichier créé : {chemin}")

    # Fournir le chemin au test
    yield chemin

    # Teardown : nettoyage
    if os.path.exists(chemin):
        os.remove(chemin)
        print(f"[Teardown] Fichier supprimé : {chemin}")

def test_lecture_fichier(fichier_temp):
    """Teste la lecture du fichier temporaire."""
    with open(fichier_temp, "r") as f:
        contenu = f.read()
    assert contenu == "Contenu initial"

def test_modification_fichier(fichier_temp):
    """Teste la modification du fichier temporaire."""
    with open(fichier_temp, "w") as f:
        f.write("Nouveau contenu")

    with open(fichier_temp, "r") as f:
        contenu = f.read()
    assert contenu == "Nouveau contenu"
```

#### Portée des fixtures (scope)

Les fixtures peuvent avoir différentes durées de vie :

```python
import pytest

@pytest.fixture(scope="function")  # Par défaut : une nouvelle instance par test
def fixture_fonction():
    """Créée pour chaque test."""
    print("\nCréation fixture fonction")
    return {"data": "fonction"}

@pytest.fixture(scope="class")  # Une instance par classe de test
def fixture_classe():
    """Créée une fois par classe."""
    print("\nCréation fixture classe")
    return {"data": "classe"}

@pytest.fixture(scope="module")  # Une instance par fichier
def fixture_module():
    """Créée une fois par fichier de test."""
    print("\nCréation fixture module")
    return {"data": "module"}

@pytest.fixture(scope="session")  # Une seule instance pour toute la session
def fixture_session():
    """Créée une fois pour tous les tests."""
    print("\nCréation fixture session")
    return {"data": "session"}

# Tests utilisant ces fixtures
def test_1(fixture_fonction, fixture_module):
    assert fixture_fonction["data"] == "fonction"
    assert fixture_module["data"] == "module"

def test_2(fixture_fonction, fixture_module):
    # fixture_fonction est recréée, fixture_module est réutilisée
    assert fixture_fonction["data"] == "fonction"
    assert fixture_module["data"] == "module"
```

#### Fixtures paramétrées

Vous pouvez créer plusieurs versions d'une même fixture :

```python
import pytest

@pytest.fixture(params=[
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
])
def utilisateur(request):
    """Fixture paramétrée qui crée plusieurs utilisateurs."""
    return request.param

def test_utilisateur_valide(utilisateur):
    """Ce test sera exécuté 3 fois, une fois par utilisateur."""
    assert "nom" in utilisateur
    assert "age" in utilisateur
    assert utilisateur["age"] > 0
```

#### Fixtures qui utilisent d'autres fixtures

Les fixtures peuvent dépendre d'autres fixtures :

```python
import pytest

@pytest.fixture
def base_de_donnees():
    """Simule une connexion à la base de données."""
    print("\nConnexion à la base de données")
    db = {"users": [], "posts": []}
    yield db
    print("\nDéconnexion de la base de données")

@pytest.fixture
def utilisateur_dans_db(base_de_donnees):
    """Crée un utilisateur dans la base de données."""
    utilisateur = {"id": 1, "nom": "Alice"}
    base_de_donnees["users"].append(utilisateur)
    return utilisateur

def test_utilisateur_existe(utilisateur_dans_db, base_de_donnees):
    """Teste que l'utilisateur est bien dans la base."""
    assert len(base_de_donnees["users"]) == 1
    assert base_de_donnees["users"][0]["nom"] == "Alice"
```

### Fixtures avec unittest

Avec unittest, on utilise les méthodes `setUp()` et `tearDown()` :

```python
import unittest

class TestCompte(unittest.TestCase):
    """Tests pour la classe Compte."""

    def setUp(self):
        """Appelée avant CHAQUE test."""
        print("\nSetup : création du compte")
        self.compte = Compte("Alice", solde=1000)

    def tearDown(self):
        """Appelée après CHAQUE test."""
        print("Teardown : nettoyage")
        self.compte = None

    def test_deposer(self):
        """Teste le dépôt."""
        self.compte.deposer(500)
        self.assertEqual(self.compte.solde, 1500)

    def test_retirer(self):
        """Teste le retrait."""
        self.compte.retirer(300)
        self.assertEqual(self.compte.solde, 700)

# Pour setup/teardown une seule fois pour toute la classe :
class TestCompteAvecSetupUnique(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Appelée UNE FOIS avant tous les tests de la classe."""
        print("\nSetup classe : préparation globale")
        cls.taux_interet = 0.03

    @classmethod
    def tearDownClass(cls):
        """Appelée UNE FOIS après tous les tests de la classe."""
        print("\nTeardown classe : nettoyage global")

    def setUp(self):
        """Appelée avant chaque test."""
        self.compte = Compte("Bob", solde=1000)

    def test_calcul_interet(self):
        """Teste le calcul d'intérêt."""
        interet = self.compte.solde * self.taux_interet
        assert interet == 30.0
```

---

## Introduction au Mocking

### Cas d'usage typiques du mocking

Le mocking est particulièrement utile pour :

1. **Appels API** : Simuler des réponses d'API sans faire de vraies requêtes
2. **Base de données** : Tester la logique sans toucher à une vraie base
3. **Fichiers** : Simuler la lecture/écriture de fichiers
4. **Temps** : Contrôler le temps dans vos tests
5. **Fonctions coûteuses** : Éviter des calculs longs ou coûteux

### Le module unittest.mock

Python fournit le module `unittest.mock` qui est inclus dans la bibliothèque standard :

```python
from unittest.mock import Mock, MagicMock, patch
```

---

## Mock : Les bases

### Créer un mock simple

Un mock est un objet qui enregistre comment il est utilisé :

```python
from unittest.mock import Mock

# Créer un mock
mon_mock = Mock()

# Utiliser le mock
resultat = mon_mock.ma_methode(1, 2, 3)
autre_resultat = mon_mock.autre_methode(nom="Alice")

# Vérifier les appels
print(mon_mock.ma_methode.called)  # True
print(mon_mock.ma_methode.call_count)  # 1
print(mon_mock.autre_methode.call_count)  # 1

# Le mock peut être appelé comme une fonction
mon_mock(42)
print(mon_mock.called)  # True
```

### Configurer le retour d'un mock

Vous pouvez définir ce qu'un mock doit retourner :

```python
from unittest.mock import Mock

# Mock avec une valeur de retour
mock_addition = Mock(return_value=10)
resultat = mock_addition(5, 5)
print(resultat)  # 10 (peu importe les arguments)

# Mock avec plusieurs valeurs de retour successives
mock_compteur = Mock(side_effect=[1, 2, 3, 4])
print(mock_compteur())  # 1
print(mock_compteur())  # 2
print(mock_compteur())  # 3
print(mock_compteur())  # 4
```

### Mock qui lève une exception

```python
from unittest.mock import Mock

# Mock qui lève une exception
mock_erreur = Mock(side_effect=ValueError("Erreur de test"))

try:
    mock_erreur()
except ValueError as e:
    print(f"Exception capturée : {e}")
```

---

## Exemples pratiques de mocking

### Exemple 1 : Mocker un appel API

Imaginons une fonction qui appelle une API météo :

```python
# fichier: meteo.py
import requests

def obtenir_temperature(ville):
    """Obtient la température d'une ville via une API."""
    url = f"https://api.meteo.com/ville/{ville}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erreur API")

    data = response.json()
    return data["temperature"]

def recommander_vetements(ville):
    """Recommande des vêtements selon la température."""
    temp = obtenir_temperature(ville)

    if temp < 10:
        return "Manteau et écharpe"
    elif temp < 20:
        return "Pull léger"
    else:
        return "T-shirt"
```

Tests avec mock :

```python
# fichier: test_meteo.py
import pytest
from unittest.mock import Mock, patch
from meteo import obtenir_temperature, recommander_vetements

def test_obtenir_temperature():
    """Teste l'obtention de la température avec un mock."""

    # Créer un mock pour la réponse
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 25}

    # Utiliser patch pour remplacer requests.get
    with patch('meteo.requests.get', return_value=mock_response):
        temperature = obtenir_temperature("Paris")
        assert temperature == 25

def test_obtenir_temperature_erreur_api():
    """Teste la gestion d'erreur API."""

    mock_response = Mock()
    mock_response.status_code = 404

    with patch('meteo.requests.get', return_value=mock_response):
        with pytest.raises(Exception, match="Erreur API"):
            obtenir_temperature("VilleInconnue")

def test_recommander_vetements_froid():
    """Teste la recommandation par temps froid."""

    # Mock la fonction obtenir_temperature directement
    with patch('meteo.obtenir_temperature', return_value=5):
        recommandation = recommander_vetements("Oslo")
        assert recommandation == "Manteau et écharpe"

def test_recommander_vetements_chaud():
    """Teste la recommandation par temps chaud."""

    with patch('meteo.obtenir_temperature', return_value=28):
        recommandation = recommander_vetements("Marseille")
        assert recommandation == "T-shirt"
```

### Exemple 2 : Mocker une base de données

```python
# fichier: utilisateurs.py
class BaseDeDonnees:
    """Simule une base de données."""

    def __init__(self):
        self.connexion = None

    def se_connecter(self):
        """Se connecte à la base de données."""
        # En réalité, ça se connecterait à une vraie base
        self.connexion = "connexion_active"

    def obtenir_utilisateur(self, user_id):
        """Récupère un utilisateur."""
        # En réalité, ça ferait une requête SQL
        pass

    def sauvegarder_utilisateur(self, utilisateur):
        """Sauvegarde un utilisateur."""
        # En réalité, ça ferait un INSERT ou UPDATE
        pass

class ServiceUtilisateur:
    """Service pour gérer les utilisateurs."""

    def __init__(self, base_de_donnees):
        self.db = base_de_donnees

    def creer_utilisateur(self, nom, email):
        """Crée un nouvel utilisateur."""
        utilisateur = {
            "nom": nom,
            "email": email,
            "actif": True
        }
        self.db.sauvegarder_utilisateur(utilisateur)
        return utilisateur

    def obtenir_profil(self, user_id):
        """Obtient le profil d'un utilisateur."""
        utilisateur = self.db.obtenir_utilisateur(user_id)
        if not utilisateur:
            raise ValueError("Utilisateur introuvable")
        return utilisateur
```

Tests avec mock :

```python
# fichier: test_utilisateurs.py
import pytest
from unittest.mock import Mock, MagicMock
from utilisateurs import BaseDeDonnees, ServiceUtilisateur

@pytest.fixture
def mock_db():
    """Fixture qui crée un mock de base de données."""
    return Mock(spec=BaseDeDonnees)

@pytest.fixture
def service(mock_db):
    """Fixture qui crée un service avec une base mockée."""
    return ServiceUtilisateur(mock_db)

def test_creer_utilisateur(service, mock_db):
    """Teste la création d'un utilisateur."""
    # Créer l'utilisateur
    utilisateur = service.creer_utilisateur("Alice", "alice@test.com")

    # Vérifier que l'utilisateur est correct
    assert utilisateur["nom"] == "Alice"
    assert utilisateur["email"] == "alice@test.com"
    assert utilisateur["actif"] is True

    # Vérifier que la méthode sauvegarder a été appelée
    mock_db.sauvegarder_utilisateur.assert_called_once()

    # Vérifier avec quel argument elle a été appelée
    args = mock_db.sauvegarder_utilisateur.call_args[0][0]
    assert args["nom"] == "Alice"

def test_obtenir_profil_existant(service, mock_db):
    """Teste l'obtention d'un profil existant."""
    # Configurer le mock pour retourner un utilisateur
    utilisateur_mock = {"id": 1, "nom": "Bob", "email": "bob@test.com"}
    mock_db.obtenir_utilisateur.return_value = utilisateur_mock

    # Obtenir le profil
    profil = service.obtenir_profil(1)

    # Vérifications
    assert profil["nom"] == "Bob"
    mock_db.obtenir_utilisateur.assert_called_once_with(1)

def test_obtenir_profil_inexistant(service, mock_db):
    """Teste l'obtention d'un profil inexistant."""
    # Configurer le mock pour retourner None
    mock_db.obtenir_utilisateur.return_value = None

    # Vérifier qu'une exception est levée
    with pytest.raises(ValueError, match="introuvable"):
        service.obtenir_profil(999)
```

### Exemple 3 : Mocker le temps

```python
# fichier: evenements.py
from datetime import datetime

class Evenement:
    """Représente un événement."""

    def __init__(self, nom, date_creation=None):
        self.nom = nom
        self.date_creation = date_creation or datetime.now()

    def est_recent(self, jours=7):
        """Vérifie si l'événement a moins de X jours."""
        maintenant = datetime.now()
        difference = maintenant - self.date_creation
        return difference.days < jours

    def age_en_jours(self):
        """Retourne l'âge de l'événement en jours."""
        maintenant = datetime.now()
        return (maintenant - self.date_creation).days
```

Tests avec mock du temps :

```python
# fichier: test_evenements.py
import pytest
from unittest.mock import patch
from datetime import datetime, timedelta
from evenements import Evenement

def test_evenement_recent():
    """Teste qu'un événement créé aujourd'hui est récent."""
    # Fixer le temps à une date spécifique
    date_fixe = datetime(2024, 1, 15, 10, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        # Configurer le mock pour retourner toujours la même date
        mock_datetime.now.return_value = date_fixe

        # Créer l'événement
        evenement = Evenement("Test")

        # Vérifier qu'il est récent
        assert evenement.est_recent()

def test_evenement_ancien():
    """Teste qu'un événement vieux de 10 jours n'est pas récent."""
    date_creation = datetime(2024, 1, 1, 10, 0, 0)
    date_maintenant = datetime(2024, 1, 15, 10, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        # Premier appel pour la création
        mock_datetime.now.return_value = date_creation
        evenement = Evenement("Test Ancien")

        # Deuxième appel pour la vérification
        mock_datetime.now.return_value = date_maintenant

        assert not evenement.est_recent(jours=7)
        assert evenement.age_en_jours() == 14

def test_age_evenement():
    """Teste le calcul de l'âge d'un événement."""
    date_creation = datetime(2024, 1, 1, 12, 0, 0)
    date_maintenant = datetime(2024, 1, 10, 12, 0, 0)

    with patch('evenements.datetime') as mock_datetime:
        mock_datetime.now.return_value = date_creation
        evenement = Evenement("Test Age")

        mock_datetime.now.return_value = date_maintenant
        assert evenement.age_en_jours() == 9
```

### Exemple 4 : Mocker la lecture de fichiers

```python
# fichier: config.py
import json

class Configuration:
    """Gère la configuration de l'application."""

    def __init__(self, fichier_config):
        self.fichier_config = fichier_config
        self.config = {}

    def charger(self):
        """Charge la configuration depuis un fichier."""
        with open(self.fichier_config, 'r') as f:
            self.config = json.load(f)

    def obtenir(self, cle, defaut=None):
        """Obtient une valeur de configuration."""
        return self.config.get(cle, defaut)

    def est_mode_debug(self):
        """Vérifie si le mode debug est activé."""
        return self.config.get('debug', False)
```

Tests avec mock :

```python
# fichier: test_config.py
import pytest
from unittest.mock import mock_open, patch
import json
from config import Configuration

def test_charger_configuration():
    """Teste le chargement de la configuration."""
    # Données de configuration simulées
    config_data = {
        "debug": True,
        "api_key": "test_key_123",
        "timeout": 30
    }

    # mock_open simule l'ouverture de fichier
    mock_file = mock_open(read_data=json.dumps(config_data))

    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()

        # Vérifications
        assert config.obtenir("debug") is True
        assert config.obtenir("api_key") == "test_key_123"
        assert config.obtenir("timeout") == 30

def test_obtenir_avec_valeur_defaut():
    """Teste l'obtention d'une valeur avec défaut."""
    config_data = {"debug": True}
    mock_file = mock_open(read_data=json.dumps(config_data))

    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()

        # Clé existante
        assert config.obtenir("debug") is True

        # Clé inexistante avec défaut
        assert config.obtenir("inexistant", "valeur_defaut") == "valeur_defaut"

def test_mode_debug():
    """Teste la vérification du mode debug."""
    config_debug = {"debug": True}
    config_prod = {"debug": False}

    # Test avec debug activé
    mock_file = mock_open(read_data=json.dumps(config_debug))
    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()
        assert config.est_mode_debug() is True

    # Test avec debug désactivé
    mock_file = mock_open(read_data=json.dumps(config_prod))
    with patch('builtins.open', mock_file):
        config = Configuration("config.json")
        config.charger()
        assert config.est_mode_debug() is False
```

---

## Assertions avancées sur les mocks

### Vérifier les appels

Les mocks enregistrent comment ils sont utilisés, ce qui permet de faire des vérifications détaillées :

```python
from unittest.mock import Mock, call

# Créer un mock
mock = Mock()

# Utiliser le mock
mock.methode(1, 2, 3)
mock.methode(4, 5, 6)
mock.autre_methode(nom="Alice")

# Vérifier qu'une méthode a été appelée
assert mock.methode.called
assert mock.autre_methode.called

# Vérifier le nombre d'appels
assert mock.methode.call_count == 2
assert mock.autre_methode.call_count == 1

# Vérifier les arguments du dernier appel
mock.methode.assert_called_with(4, 5, 6)

# Vérifier tous les appels
mock.methode.assert_has_calls([
    call(1, 2, 3),
    call(4, 5, 6)
])

# Vérifier qu'une méthode n'a PAS été appelée
mock_non_appele = Mock()
mock_non_appele.methode.assert_not_called()
```

### Exemple pratique : Vérifier l'envoi d'email

```python
# fichier: notification.py
import smtplib
from email.message import EmailMessage

class ServiceNotification:
    """Service pour envoyer des notifications."""

    def __init__(self, serveur_smtp):
        self.serveur_smtp = serveur_smtp

    def envoyer_email(self, destinataire, sujet, corps):
        """Envoie un email."""
        msg = EmailMessage()
        msg['Subject'] = sujet
        msg['From'] = 'noreply@example.com'
        msg['To'] = destinataire
        msg.set_content(corps)

        # Connexion au serveur SMTP
        with smtplib.SMTP(self.serveur_smtp, 587) as smtp:
            smtp.send_message(msg)

    def notifier_inscription(self, utilisateur):
        """Notifie un utilisateur de son inscription."""
        sujet = "Bienvenue !"
        corps = f"Bonjour {utilisateur['nom']}, bienvenue sur notre plateforme !"
        self.envoyer_email(utilisateur['email'], sujet, corps)
```

Tests :

```python
# fichier: test_notification.py
import pytest
from unittest.mock import Mock, patch, MagicMock
from notification import ServiceNotification

@pytest.fixture
def service():
    """Fixture qui crée un service de notification."""
    return ServiceNotification("smtp.example.com")

def test_envoyer_email(service):
    """Teste l'envoi d'un email."""
    with patch('notification.smtplib.SMTP') as mock_smtp:
        # Configurer le mock
        mock_connexion = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_connexion

        # Envoyer l'email
        service.envoyer_email(
            "user@example.com",
            "Test",
            "Ceci est un test"
        )

        # Vérifier que SMTP a été appelé avec les bons paramètres
        mock_smtp.assert_called_once_with("smtp.example.com", 587)

        # Vérifier que send_message a été appelé
        assert mock_connexion.send_message.called

def test_notifier_inscription(service):
    """Teste la notification d'inscription."""
    utilisateur = {
        "nom": "Alice",
        "email": "alice@example.com"
    }

    with patch.object(service, 'envoyer_email') as mock_envoyer:
        # Notifier l'utilisateur
        service.notifier_inscription(utilisateur)

        # Vérifier que envoyer_email a été appelé correctement
        mock_envoyer.assert_called_once()

        # Vérifier les arguments
        args, kwargs = mock_envoyer.call_args
        assert args[0] == "alice@example.com"  # destinataire
        assert "Bienvenue" in args[1]  # sujet
        assert "Alice" in args[2]  # corps
```

---

## MagicMock : Mock avec méthodes magiques

`MagicMock` est une version de `Mock` qui supporte les méthodes spéciales Python (dunder methods) :

```python
from unittest.mock import MagicMock

# MagicMock supporte les opérations Python
mock = MagicMock()

# On peut l'utiliser comme un conteneur
mock.__len__.return_value = 5
print(len(mock))  # 5

# Comme un itérable
mock.__iter__.return_value = iter([1, 2, 3])
for item in mock:
    print(item)  # 1, 2, 3

# Avec des comparaisons
mock.__eq__.return_value = True
print(mock == "quelque chose")  # True

# Exemple plus réaliste : simuler une classe
class FausseBaseDeDonnees(MagicMock):
    """Simule une base de données pour les tests."""
    pass

db = FausseBaseDeDonnees()
db.query.return_value = [{"id": 1, "nom": "Alice"}]
db.__len__.return_value = 10

resultats = db.query("SELECT * FROM users")
print(resultats)  # [{'id': 1, 'nom': 'Alice'}]
print(len(db))  # 10
```

---

## Patch : Remplacer temporairement

`patch` est le moyen le plus courant de mocker en Python. Il remplace temporairement un objet dans votre code.

### patch comme décorateur

```python
from unittest.mock import patch

@patch('module.fonction_a_mocker')
def test_avec_patch(mock_fonction):
    """Test avec patch en décorateur."""
    mock_fonction.return_value = 42

    # Le code ici voit fonction_a_mocker comme le mock
    # ...

# Exemple concret
@patch('requests.get')
def test_api_call(mock_get):
    """Teste un appel API."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "test"}

    # Votre code qui utilise requests.get
    # ...
```

### patch comme context manager

```python
from unittest.mock import patch

def test_avec_context_manager():
    """Test avec patch en context manager."""
    with patch('module.fonction_a_mocker') as mock_fonction:
        mock_fonction.return_value = 42

        # Le code ici voit fonction_a_mocker comme le mock
        # ...

    # Ici, fonction_a_mocker est revenue à la normale
```

### Patcher plusieurs choses

```python
from unittest.mock import patch

@patch('module.fonction2')
@patch('module.fonction1')
def test_multi_patch(mock_fonction1, mock_fonction2):
    """Attention : l'ordre est inversé !"""
    mock_fonction1.return_value = "A"
    mock_fonction2.return_value = "B"
    # ...

# Ou avec context manager
def test_multi_patch_context():
    with patch('module.fonction1') as mock1, \
         patch('module.fonction2') as mock2:
        mock1.return_value = "A"
        mock2.return_value = "B"
        # ...
```

### patch.object : Patcher un attribut spécifique

```python
from unittest.mock import patch

class MaClasse:
    def methode_originale(self):
        return "original"

def test_patch_object():
    """Teste le patch d'une méthode spécifique."""
    obj = MaClasse()

    with patch.object(obj, 'methode_originale', return_value="mocké"):
        resultat = obj.methode_originale()
        assert resultat == "mocké"

    # Après le contexte, la méthode est restaurée
    assert obj.methode_originale() == "original"
```

---

## Bonnes pratiques

### 1. Ne mocquez que ce qui est nécessaire

```python
# ❌ Mauvais - tout est mocké
@patch('module.fonction1')
@patch('module.fonction2')
@patch('module.fonction3')
@patch('module.fonction4')
def test_trop_de_mocks(m1, m2, m3, m4):
    # Difficile à maintenir
    pass

# ✅ Bon - seulement les dépendances externes
@patch('module.appel_api_externe')
def test_avec_mock_necessaire(mock_api):
    # On teste vraiment notre logique
    pass
```

### 2. Utilisez spec pour éviter les erreurs

```python
from unittest.mock import Mock

class VraieClasse:
    def methode_existante(self):
        pass

# ❌ Sans spec, tout est permis
mock_sans_spec = Mock()
mock_sans_spec.methode_qui_nexiste_pas()  # Pas d'erreur !

# ✅ Avec spec, les erreurs sont détectées
mock_avec_spec = Mock(spec=VraieClasse)
# mock_avec_spec.methode_qui_nexiste_pas()  # AttributeError !
mock_avec_spec.methode_existante()  # OK
```

### 3. Nommez vos mocks clairement

```python
# ❌ Mauvais
mock = Mock()

# ✅ Bon
mock_base_de_donnees = Mock()
mock_api_meteo = Mock()
mock_service_email = Mock()
```

### 4. Testez le comportement, pas l'implémentation

```python
# ❌ Mauvais - teste trop l'implémentation
def test_implementation(mock_db):
    service.creer_utilisateur("Alice", "alice@test.com")

    # Vérifie trop de détails internes
    assert mock_db.verifier_email.called
    assert mock_db.hasher_mot_de_passe.called
    assert mock_db.sauvegarder.called
    # ...

# ✅ Bon - teste le comportement
def test_comportement(mock_db):
    utilisateur = service.creer_utilisateur("Alice", "alice@test.com")

    # Vérifie seulement le résultat
    assert utilisateur["nom"] == "Alice"
    assert utilisateur["email"] == "alice@test.com"
    mock_db.sauvegarder.assert_called_once()
```

### 5. Évitez les fixtures trop complexes

```python
# ❌ Mauvais - fixture qui fait trop
@pytest.fixture
def systeme_complet():
    db = creer_base()
    cache = initialiser_cache()
    api = configurer_api()
    service = ServiceComplet(db, cache, api)
    # ... beaucoup trop de configuration
    return service

# ✅ Bon - fixtures modulaires
@pytest.fixture
def mock_db():
    return Mock(spec=BaseDeDonnees)

@pytest.fixture
def mock_cache():
    return Mock(spec=Cache)

@pytest.fixture
def service(mock_db, mock_cache):
    return ServiceComplet(mock_db, mock_cache)
```

---

## Cas pratique complet : Service de paiement

Voici un exemple réaliste qui combine fixtures et mocking :

```python
# fichier: paiement.py
import requests
from datetime import datetime

class ServicePaiement:
    """Gère les paiements."""

    def __init__(self, api_url, api_key, base_de_donnees):
        self.api_url = api_url
        self.api_key = api_key
        self.db = base_de_donnees

    def traiter_paiement(self, utilisateur_id, montant):
        """Traite un paiement."""
        # Valider le montant
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        # Vérifier l'utilisateur dans la base
        utilisateur = self.db.obtenir_utilisateur(utilisateur_id)
        if not utilisateur:
            raise ValueError("Utilisateur introuvable")

        # Appeler l'API de paiement
        response = requests.post(
            f"{self.api_url}/charge",
            json={
                "user_id": utilisateur_id,
                "amount": montant,
                "currency": "EUR"
            },
            headers={"Authorization": f"Bearer {self.api_key}"}
        )

        if response.status_code != 200:
            raise Exception("Échec du paiement")

        # Enregistrer la transaction
        transaction = {
            "utilisateur_id": utilisateur_id,
            "montant": montant,
            "date": datetime.now(),
            "statut": "réussi",
            "transaction_id": response.json()["transaction_id"]
        }

        self.db.sauvegarder_transaction(transaction)

        return transaction
```

Tests complets :

```python
# fichier: test_paiement.py
import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from paiement import ServicePaiement

@pytest.fixture
def mock_db():
    """Mock de la base de données."""
    db = Mock()
    db.obtenir_utilisateur.return_value = {
        "id": 1,
        "nom": "Alice",
        "email": "alice@test.com"
    }
    return db

@pytest.fixture
def service_paiement(mock_db):
    """Service de paiement avec dépendances mockées."""
    return ServicePaiement(
        api_url="https://api.paiement.test",
        api_key="test_key_123",
        base_de_donnees=mock_db
    )

def test_traiter_paiement_reussi(service_paiement, mock_db):
    """Teste un paiement réussi."""
    # Mock de la réponse API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"transaction_id": "txn_123"}

    with patch('paiement.requests.post', return_value=mock_response):
        # Fixer le temps pour le test
        date_fixe = datetime(2024, 1, 15, 10, 0, 0)
        with patch('paiement.datetime') as mock_datetime:
            mock_datetime.now.return_value = date_fixe

            # Traiter le paiement
            transaction = service_paiement.traiter_paiement(
                utilisateur_id=1,
                montant=50.00
            )

    # Vérifications
    assert transaction["utilisateur_id"] == 1
    assert transaction["montant"] == 50.00
    assert transaction["statut"] == "réussi"
    assert transaction["transaction_id"] == "txn_123"
    assert transaction["date"] == date_fixe

    # Vérifier que la transaction a été sauvegardée
    mock_db.sauvegarder_transaction.assert_called_once()

def test_traiter_paiement_montant_negatif(service_paiement):
    """Teste qu'un montant négatif est rejeté."""
    with pytest.raises(ValueError, match="positif"):
        service_paiement.traiter_paiement(1, -10)

def test_traiter_paiement_utilisateur_inexistant(service_paiement, mock_db):
    """Teste avec un utilisateur inexistant."""
    mock_db.obtenir_utilisateur.return_value = None

    with pytest.raises(ValueError, match="introuvable"):
        service_paiement.traiter_paiement(999, 50.00)

def test_traiter_paiement_echec_api(service_paiement, mock_db):
    """Teste l'échec de l'API de paiement."""
    mock_response = Mock()
    mock_response.status_code = 400

    with patch('paiement.requests.post', return_value=mock_response):
        with pytest.raises(Exception, match="Échec"):
            service_paiement.traiter_paiement(1, 50.00)

    # Vérifier qu'aucune transaction n'a été sauvegardée
    mock_db.sauvegarder_transaction.assert_not_called()

def test_appel_api_avec_bons_parametres(service_paiement, mock_db):
    """Vérifie que l'API est appelée avec les bons paramètres."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"transaction_id": "txn_456"}

    with patch('paiement.requests.post', return_value=mock_response) as mock_post:
        service_paiement.traiter_paiement(1, 100.00)

        # Vérifier l'appel à l'API
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args

        # Vérifier l'URL
        assert args[0] == "https://api.paiement.test/charge"

        # Vérifier le body
        assert kwargs["json"]["user_id"] == 1
        assert kwargs["json"]["amount"] == 100.00
        assert kwargs["json"]["currency"] == "EUR"

        # Vérifier les headers
        assert "Authorization" in kwargs["headers"]
        assert "test_key_123" in kwargs["headers"]["Authorization"]
```

---

## Résumé

### Fixtures - Points clés

- Les **fixtures** préparent les données et l'environnement pour vos tests
- **pytest.fixture** : Décorateur pour créer des fixtures réutilisables
- **yield** : Permet de faire du nettoyage après le test
- **scope** : Contrôle la durée de vie (function, class, module, session)
- Les fixtures peuvent utiliser d'autres fixtures

### Mocking - Points clés

- Le **mocking** remplace temporairement des parties de code par des simulations
- **unittest.mock** : Module standard pour le mocking
- **Mock** : Objet qui enregistre comment il est utilisé
- **MagicMock** : Mock avec support des méthodes magiques
- **patch** : Remplace temporairement une fonction/classe
- **mock_open** : Simule l'ouverture de fichiers

### Quand utiliser quoi

| Situation | Outil |
|-----------|-------|
| Préparer des données | Fixtures |
| Remplacer un appel API | Mock + patch |
| Simuler une base de données | Mock |
| Contrôler le temps | patch sur datetime |
| Simuler des fichiers | mock_open |
| Vérifier qu'une fonction a été appelée | Assertions sur mock |

### Commandes pytest utiles

```bash
# Exécuter les tests avec affichage détaillé
pytest -v

# Voir les print() et logs
pytest -s

# Afficher les fixtures disponibles
pytest --fixtures

# Exécuter seulement les tests qui utilisent une fixture
pytest -k "nom_fixture"
```

---

## Ressources complémentaires

- Documentation unittest.mock : https://docs.python.org/3/library/unittest.mock.html
- Documentation pytest fixtures : https://docs.pytest.org/en/stable/fixture.html
- Guide Real Python sur le mocking : https://realpython.com/python-mock-library/
- Article sur les bonnes pratiques de testing : https://testdriven.io/blog/testing-best-practices/

Avec les fixtures et le mocking, vous pouvez maintenant écrire des tests pour n'importe quel code, même celui qui dépend de services externes ! 🎯

⏭️ [Couverture de code](/10-tests-et-qualite/03-couverture-de-code.md)
