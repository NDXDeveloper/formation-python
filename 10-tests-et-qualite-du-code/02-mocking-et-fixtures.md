🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.2 : Mocking et fixtures

## Introduction

Imaginez que vous voulez tester une recette de cuisine, mais l'un des ingrédients coûte très cher, n'est disponible qu'en saison, ou met des heures à préparer. Que faites-vous ? Vous utilisez un substitut ! En programmation, c'est exactement le principe du **mocking** : remplacer temporairement des parties complexes ou coûteuses de votre code par des "doublures" contrôlées.

Les **fixtures**, quant à elles, sont comme votre mise en place en cuisine : tous les ingrédients préparés, les ustensiles sortis, le plan de travail nettoyé. Elles préparent l'environnement parfait pour vos tests.

## Qu'est-ce que le mocking ?

### Le problème des dépendances externes

Votre code interagit souvent avec des éléments externes :
- Bases de données
- APIs web
- Fichiers système
- Services de paiement
- Envoi d'emails

Tester directement avec ces éléments pose des problèmes :

```python
# ❌ Code difficile à tester
import requests
import smtplib

def traiter_commande(commande_id):
    # Appel à une API externe (lent, peut échouer)
    response = requests.get(f"https://api.shop.com/orders/{commande_id}")
    commande = response.json()

    # Calcul du prix (logique métier à tester)
    prix_total = commande['prix'] * (1 + commande['tax_rate'])

    # Envoi d'email (coûteux, peut échouer)
    envoyer_email_confirmation(commande['email'], prix_total)

    return prix_total

def envoyer_email_confirmation(email, prix):
    # Connexion SMTP réelle (lente, complexe à configurer)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # ... configuration complexe
    server.send_message(...)
```

### La solution : les mocks

Un **mock** est un objet factice qui imite le comportement d'un objet réel :

```python
# ✅ Version testable avec mocks
def test_traiter_commande_avec_mocks():
    # On remplace les appels externes par des mocks
    with mock.patch('requests.get') as mock_get:
        with mock.patch('main.envoyer_email_confirmation') as mock_email:

            # Configuration du mock pour l'API
            mock_get.return_value.json.return_value = {
                'prix': 100,
                'tax_rate': 0.20,
                'email': 'client@example.com'
            }

            # Test de la logique métier
            prix_total = traiter_commande('123')

            # Vérifications
            assert prix_total == 120  # 100 * (1 + 0.20)
            mock_email.assert_called_once_with('client@example.com', 120)
```

## Introduction aux mocks avec unittest.mock

### Mock basique

```python
from unittest.mock import Mock

def test_premier_mock():
    # Création d'un mock
    mon_mock = Mock()

    # Configuration du comportement
    mon_mock.methode.return_value = 42

    # Utilisation
    resultat = mon_mock.methode()

    # Vérifications
    assert resultat == 42
    mon_mock.methode.assert_called_once()

# Test
test_premier_mock()
print("✅ Premier mock réussi !")
```

### Mock avec spécifications

```python
from unittest.mock import Mock

class UtilisateurService:
    def obtenir_utilisateur(self, user_id):
        # Simulation d'appel base de données
        pass

    def sauvegarder_utilisateur(self, utilisateur):
        # Simulation de sauvegarde
        pass

def test_avec_specification():
    # Mock qui respecte l'interface de la classe
    mock_service = Mock(spec=UtilisateurService)

    # Configuration
    mock_service.obtenir_utilisateur.return_value = {
        'id': 1,
        'nom': 'Alice',
        'email': 'alice@example.com'
    }

    # Test
    utilisateur = mock_service.obtenir_utilisateur(1)
    assert utilisateur['nom'] == 'Alice'

    # Cette ligne provoquerait une erreur car la méthode n'existe pas
    # mock_service.methode_inexistante()  # AttributeError

test_avec_specification()
```

## Patch : Remplacer temporairement

### Patch avec décorateur

```python
from unittest.mock import patch
import datetime

def obtenir_age_utilisateur(annee_naissance):
    """Calcule l'âge basé sur l'année actuelle"""
    annee_actuelle = datetime.datetime.now().year
    return annee_actuelle - annee_naissance

# Test avec patch pour contrôler la date
@patch('datetime.datetime')
def test_calcul_age(mock_datetime):
    # On simule qu'on est en 2025
    mock_datetime.now.return_value.year = 2025

    # Test
    age = obtenir_age_utilisateur(1990)

    # Vérification
    assert age == 35

test_calcul_age()
print("✅ Test avec patch réussi !")
```

### Patch avec gestionnaire de contexte

```python
import json
from unittest.mock import patch, mock_open

def sauvegarder_configuration(config, nom_fichier):
    """Sauvegarde la configuration dans un fichier JSON"""
    with open(nom_fichier, 'w') as f:
        json.dump(config, f)

def charger_configuration(nom_fichier):
    """Charge la configuration depuis un fichier JSON"""
    with open(nom_fichier, 'r') as f:
        return json.load(f)

def test_sauvegarde_configuration():
    config = {'debug': True, 'port': 8080}

    # Mock de l'ouverture de fichier
    with patch('builtins.open', mock_open()) as mock_file:
        sauvegarder_configuration(config, 'config.json')

        # Vérifications
        mock_file.assert_called_once_with('config.json', 'w')
        # Vérifie que json.dump a été appelé avec les bons arguments
        handle = mock_file.return_value
        handle.write.assert_called()

def test_chargement_configuration():
    config_json = '{"debug": true, "port": 8080}'

    with patch('builtins.open', mock_open(read_data=config_json)):
        config = charger_configuration('config.json')

        assert config['debug'] == True
        assert config['port'] == 8080

test_sauvegarde_configuration()
test_chargement_configuration()
print("✅ Tests avec mock_open réussis !")
```

## Mocking des appels réseau

### Mock d'API REST

```python
from unittest.mock import patch, Mock
import requests

class ClientAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def obtenir_utilisateur(self, user_id):
        """Récupère un utilisateur via l'API"""
        response = requests.get(f"{self.base_url}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            raise Exception(f"Erreur API: {response.status_code}")

    def creer_utilisateur(self, donnees_utilisateur):
        """Crée un nouvel utilisateur"""
        response = requests.post(f"{self.base_url}/users", json=donnees_utilisateur)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Erreur création: {response.status_code}")

# Tests avec mocks
@patch('requests.get')
def test_obtenir_utilisateur_existant(mock_get):
    # Configuration du mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'id': 1,
        'nom': 'Alice',
        'email': 'alice@example.com'
    }
    mock_get.return_value = mock_response

    # Test
    client = ClientAPI('https://api.example.com')
    utilisateur = client.obtenir_utilisateur(1)

    # Vérifications
    assert utilisateur['nom'] == 'Alice'
    mock_get.assert_called_once_with('https://api.example.com/users/1')

@patch('requests.get')
def test_utilisateur_inexistant(mock_get):
    # Configuration pour un utilisateur inexistant
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Test
    client = ClientAPI('https://api.example.com')
    utilisateur = client.obtenir_utilisateur(999)

    # Vérification
    assert utilisateur is None

@patch('requests.post')
def test_creer_utilisateur(mock_post):
    # Configuration du mock
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        'id': 2,
        'nom': 'Bob',
        'email': 'bob@example.com'
    }
    mock_post.return_value = mock_response

    # Test
    client = ClientAPI('https://api.example.com')
    donnees = {'nom': 'Bob', 'email': 'bob@example.com'}
    utilisateur = client.creer_utilisateur(donnees)

    # Vérifications
    assert utilisateur['id'] == 2
    mock_post.assert_called_once_with(
        'https://api.example.com/users',
        json=donnees
    )

# Exécution des tests
test_obtenir_utilisateur_existant()
test_utilisateur_inexistant()
test_creer_utilisateur()
print("✅ Tests API avec mocks réussis !")
```

## Fixtures avancées avec pytest

### Fixtures avec différents scopes

```python
import pytest
import tempfile
import os
import sqlite3

# Fixture de session (créée une fois pour tous les tests)
@pytest.fixture(scope="session")
def db_connection():
    """Connexion base de données partagée pour tous les tests"""
    print("🔌 Création de la connexion DB")

    # Création d'une base temporaire
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    conn = sqlite3.connect(db_path)

    # Création des tables
    conn.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')
    conn.commit()

    yield conn

    # Nettoyage
    conn.close()
    os.close(db_fd)
    os.unlink(db_path)
    print("🗑️ Connexion DB fermée")

# Fixture de classe (créée une fois par classe de tests)
@pytest.fixture(scope="class")
def donnees_test():
    """Données de test pour une classe"""
    print("📊 Préparation des données de test")
    return {
        'utilisateurs': [
            {'nom': 'Alice', 'email': 'alice@test.com'},
            {'nom': 'Bob', 'email': 'bob@test.com'},
        ]
    }

# Fixture de fonction (créée pour chaque test - par défaut)
@pytest.fixture
def utilisateur_temporaire(db_connection):
    """Crée un utilisateur temporaire pour un test"""
    print("👤 Création utilisateur temporaire")

    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO users (nom, email) VALUES (?, ?)",
        ('Test User', 'test@example.com')
    )
    db_connection.commit()
    user_id = cursor.lastrowid

    yield user_id

    # Nettoyage après le test
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db_connection.commit()
    print("🗑️ Utilisateur temporaire supprimé")

# Tests utilisant les fixtures
class TestUtilisateurs:
    def test_lecture_utilisateur(self, db_connection, utilisateur_temporaire):
        """Test de lecture d'un utilisateur"""
        cursor = db_connection.cursor()
        cursor.execute("SELECT nom FROM users WHERE id = ?", (utilisateur_temporaire,))
        result = cursor.fetchone()

        assert result is not None
        assert result[0] == 'Test User'

    def test_creation_utilisateur(self, db_connection, donnees_test):
        """Test de création d'utilisateur"""
        cursor = db_connection.cursor()

        # Utilisation des données de test
        utilisateur = donnees_test['utilisateurs'][0]
        cursor.execute(
            "INSERT INTO users (nom, email) VALUES (?, ?)",
            (utilisateur['nom'], utilisateur['email'])
        )
        db_connection.commit()

        # Vérification
        cursor.execute("SELECT COUNT(*) FROM users WHERE nom = ?", (utilisateur['nom'],))
        count = cursor.fetchone()[0]
        assert count == 1
```

### Fixtures paramétrées

```python
import pytest

@pytest.fixture(params=[
    {'nom': 'Alice', 'age': 30, 'ville': 'Paris'},
    {'nom': 'Bob', 'age': 25, 'ville': 'Lyon'},
    {'nom': 'Charlie', 'age': 35, 'ville': 'Marseille'}
])
def utilisateur_parametree(request):
    """Fixture qui fournit différents utilisateurs"""
    return request.param

def test_validation_utilisateur(utilisateur_parametree):
    """Ce test sera exécuté 3 fois, une pour chaque paramètre"""
    assert len(utilisateur_parametree['nom']) > 0
    assert utilisateur_parametree['age'] > 0
    assert len(utilisateur_parametree['ville']) > 0

# Fixture avec paramètres conditionnels
@pytest.fixture(params=[
    pytest.param('production', marks=pytest.mark.slow),
    pytest.param('test', marks=pytest.mark.fast),
    pytest.param('developpement')
])
def environnement(request):
    """Fixture pour différents environnements"""
    return request.param

def test_configuration(environnement):
    """Test adapté selon l'environnement"""
    if environnement == 'production':
        # Tests plus stricts en production
        assert True
    elif environnement == 'test':
        # Tests rapides
        assert True
    else:
        # Tests de développement
        assert True
```

### Fixtures factory

```python
import pytest

@pytest.fixture
def user_factory():
    """Factory pour créer des utilisateurs personnalisés"""
    created_users = []

    def _create_user(nom="User", email=None, age=25):
        if email is None:
            email = f"{nom.lower()}@example.com"

        user = {
            'nom': nom,
            'email': email,
            'age': age,
            'id': len(created_users) + 1
        }
        created_users.append(user)
        return user

    yield _create_user

    # Nettoyage
    print(f"🗑️ Suppression de {len(created_users)} utilisateurs créés")
    created_users.clear()

def test_avec_factory(user_factory):
    """Test utilisant la factory"""
    # Création d'utilisateurs personnalisés
    alice = user_factory(nom="Alice", age=30)
    bob = user_factory(nom="Bob", email="bob.special@test.com")

    assert alice['nom'] == "Alice"
    assert alice['age'] == 30
    assert bob['email'] == "bob.special@test.com"
```

## Exemple complet : Service de notifications

```python
# notification_service.py
import smtplib
import requests
from email.mime.text import MIMEText

class NotificationService:
    def __init__(self, smtp_server, api_key):
        self.smtp_server = smtp_server
        self.api_key = api_key

    def envoyer_email(self, destinataire, sujet, message):
        """Envoie un email via SMTP"""
        try:
            server = smtplib.SMTP(self.smtp_server, 587)
            server.starttls()

            msg = MIMEText(message)
            msg['Subject'] = sujet
            msg['To'] = destinataire

            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Erreur email: {e}")
            return False

    def envoyer_sms(self, numero, message):
        """Envoie un SMS via API"""
        try:
            response = requests.post(
                'https://api.sms.com/send',
                headers={'Authorization': f'Bearer {self.api_key}'},
                json={
                    'to': numero,
                    'message': message
                }
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Erreur SMS: {e}")
            return False

    def notifier_utilisateur(self, utilisateur, type_notification, message):
        """Notifie un utilisateur selon ses préférences"""
        if type_notification == 'email':
            return self.envoyer_email(
                utilisateur['email'],
                'Notification',
                message
            )
        elif type_notification == 'sms':
            return self.envoyer_sms(
                utilisateur['telephone'],
                message
            )
        else:
            raise ValueError(f"Type de notification non supporté: {type_notification}")
```

### Tests avec mocks et fixtures

```python
# test_notification_service.py
import pytest
from unittest.mock import patch, Mock, MagicMock
from notification_service import NotificationService

@pytest.fixture
def service():
    """Fixture pour le service de notification"""
    return NotificationService(
        smtp_server='smtp.test.com',
        api_key='test_key_123'
    )

@pytest.fixture
def utilisateur_test():
    """Fixture pour un utilisateur de test"""
    return {
        'nom': 'Alice Test',
        'email': 'alice@test.com',
        'telephone': '+33123456789'
    }

class TestNotificationService:

    @patch('smtplib.SMTP')
    def test_envoyer_email_succes(self, mock_smtp, service):
        """Test d'envoi d'email réussi"""
        # Configuration du mock
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        # Test
        resultat = service.envoyer_email(
            'test@example.com',
            'Test Subject',
            'Test Message'
        )

        # Vérifications
        assert resultat == True
        mock_smtp.assert_called_once_with('smtp.test.com', 587)
        mock_server.starttls.assert_called_once()
        mock_server.send_message.assert_called_once()
        mock_server.quit.assert_called_once()

    @patch('smtplib.SMTP')
    def test_envoyer_email_echec(self, mock_smtp, service):
        """Test d'échec d'envoi d'email"""
        # Configuration du mock pour lever une exception
        mock_smtp.side_effect = Exception("Connexion refusée")

        # Test
        resultat = service.envoyer_email(
            'test@example.com',
            'Test Subject',
            'Test Message'
        )

        # Vérification
        assert resultat == False

    @patch('requests.post')
    def test_envoyer_sms_succes(self, mock_post, service):
        """Test d'envoi de SMS réussi"""
        # Configuration du mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Test
        resultat = service.envoyer_sms('+33123456789', 'Test SMS')

        # Vérifications
        assert resultat == True
        mock_post.assert_called_once_with(
            'https://api.sms.com/send',
            headers={'Authorization': 'Bearer test_key_123'},
            json={
                'to': '+33123456789',
                'message': 'Test SMS'
            }
        )

    @patch('requests.post')
    def test_envoyer_sms_echec(self, mock_post, service):
        """Test d'échec d'envoi de SMS"""
        # Configuration du mock
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        # Test
        resultat = service.envoyer_sms('+33123456789', 'Test SMS')

        # Vérification
        assert resultat == False

    @patch.object(NotificationService, 'envoyer_email')
    def test_notifier_utilisateur_email(self, mock_email, service, utilisateur_test):
        """Test de notification par email"""
        # Configuration du mock
        mock_email.return_value = True

        # Test
        resultat = service.notifier_utilisateur(
            utilisateur_test,
            'email',
            'Message de test'
        )

        # Vérifications
        assert resultat == True
        mock_email.assert_called_once_with(
            'alice@test.com',
            'Notification',
            'Message de test'
        )

    @patch.object(NotificationService, 'envoyer_sms')
    def test_notifier_utilisateur_sms(self, mock_sms, service, utilisateur_test):
        """Test de notification par SMS"""
        # Configuration du mock
        mock_sms.return_value = True

        # Test
        resultat = service.notifier_utilisateur(
            utilisateur_test,
            'sms',
            'Message de test'
        )

        # Vérifications
        assert resultat == True
        mock_sms.assert_called_once_with(
            '+33123456789',
            'Message de test'
        )

    def test_notifier_type_invalide(self, service, utilisateur_test):
        """Test avec type de notification invalide"""
        with pytest.raises(ValueError, match="Type de notification non supporté"):
            service.notifier_utilisateur(
                utilisateur_test,
                'pigeon_voyageur',
                'Message de test'
            )

# Exécution avec pytest
# pytest test_notification_service.py -v
```

## Bonnes pratiques pour mocks et fixtures

### 1. Ne pas sur-mocker

```python
# ❌ Trop de mocks - on ne teste plus rien
@patch('module.fonction_a')
@patch('module.fonction_b')
@patch('module.fonction_c')
def test_trop_de_mocks(mock_c, mock_b, mock_a):
    # Si tout est mocké, que teste-t-on vraiment ?
    pass

# ✅ Mock seulement les dépendances externes
@patch('requests.get')  # Mock seulement l'appel réseau
def test_avec_mock_utile(mock_get):
    # On teste la logique métier, pas l'appel réseau
    pass
```

### 2. Fixtures réutilisables

```python
# ✅ Fixtures dans conftest.py pour réutilisation
# conftest.py
import pytest

@pytest.fixture
def db_connection():
    """Connexion DB réutilisable dans tous les tests"""
    # Setup
    yield connection
    # Teardown

@pytest.fixture
def utilisateur_admin():
    """Utilisateur admin pour les tests d'autorisation"""
    return {'role': 'admin', 'permissions': ['read', 'write', 'delete']}
```

### 3. Noms expressifs

```python
# ✅ Noms clairs pour mocks et fixtures
@pytest.fixture
def client_api_avec_auth():
    """Client API avec authentification configurée"""
    pass

@patch('payment_service.process_payment')
def test_commande_avec_paiement_mock(mock_payment):
    """Test avec mock du service de paiement"""
    pass
```

## Exercices pratiques

### Exercice 1 : Mock d'un service météo

```python
import requests

class ServiceMeteo:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com"

    def obtenir_temperature(self, ville):
        """Obtient la température actuelle d'une ville"""
        response = requests.get(
            f"{self.base_url}/current",
            params={'q': ville, 'appid': self.api_key}
        )
        if response.status_code == 200:
            data = response.json()
            return data['main']['temp']
        return None

    def prevoir_pluie(self, ville):
        """Prévoit s'il va pleuvoir"""
        response = requests.get(
            f"{self.base_url}/forecast",
            params={'q': ville, 'appid': self.api_key}
        )
        if response.status_code == 200:
            data = response.json()
            return 'rain' in data['weather'][0]['description'].lower()
        return False

# À vous ! Écrivez des tests avec mocks pour :
# 1. Test de obtenir_temperature avec succès
# 2. Test de obtenir_temperature avec ville inexistante
# 3. Test de prevoir_pluie avec pluie prévue
# 4. Test de prevoir_pluie sans pluie
```

### Exercice 2 : Fixtures pour un blog

```python
class Article:
    def __init__(self, titre, contenu, auteur):
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
        self.date_creation = datetime.now()
        self.publié = False

    def publier(self):
        self.publié = True

    def est_long(self):
        return len(self.contenu) > 1000

class BlogService:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, article):
        self.articles.append(article)

    def obtenir_articles_publies(self):
        return [a for a in self.articles if a.publié]

    def obtenir_articles_longs(self):
        return [a for a in self.articles if a.est_long()]

# À vous ! Créez des fixtures pour :
# 1. Un article court non publié
# 2. Un article long publié
# 3. Un blog service avec plusieurs articles
# 4. Écrivez des tests utilisant ces fixtures
```

## Résumé

Les mocks et fixtures sont essentiels pour des tests efficaces :

### **Mocking :**
- **Mock** : Remplace des dépendances externes
- **Patch** : Remplace temporairement des objets
- **Avantages** : Tests rapides, isolés, reproductibles
- **Règle d'or** : Mock les dépendances, pas la logique métier

### **Fixtures :**
- **Préparation** : Environnement propre pour chaque test
- **Scopes** : function, class, module, session
- **Factory** : Création d'objets personnalisés
- **Nettoyage** : Automatique avec yield

### **Bonnes pratiques :**
- Mock seulement ce qui est nécessaire
- Noms expressifs pour mocks et fixtures
- Fixtures réutilisables dans conftest.py
- Tests indépendants et reproductibles

### **Workflow :**
1. Identifier les dépendances externes
2. Créer des mocks appropriés
3. Préparer l'environnement avec des fixtures
4. Tester la logique métier isolément
5. Vérifier les interactions avec les mocks

Les mocks et fixtures vous permettent de tester n'importe quel code, même le plus complexe, en contrôlant parfaitement l'environnement de test !

Dans la section suivante, nous verrons comment mesurer l'efficacité de nos tests avec la couverture de code.

---

**À retenir :** Un bon mock, c'est comme un bon acteur de doublure : il joue parfaitement son rôle sans que personne ne s'en aperçoive !

⏭️
