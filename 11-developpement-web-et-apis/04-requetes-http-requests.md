🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.4 Requêtes HTTP avec requests

## Introduction

Jusqu'à présent, vous avez appris à **créer** des APIs et des applications web avec Flask et FastAPI. Maintenant, nous allons voir l'autre côté de la médaille : comment **consommer** des APIs existantes, c'est-à-dire comment envoyer des requêtes HTTP vers d'autres serveurs et récupérer leurs données.

La bibliothèque **requests** est l'outil standard en Python pour faire des requêtes HTTP. Elle est simple, élégante et incroyablement populaire. Son slogan : "HTTP for Humans" résume bien sa philosophie - rendre les requêtes HTTP aussi simples que possible.

## Qu'est-ce que requests ?

**requests** est une bibliothèque Python qui permet d'envoyer des requêtes HTTP de manière simple et intuitive. Elle encapsule toute la complexité du protocole HTTP et vous offre une interface claire et pythonique.

### Pourquoi requests ?

Python possède déjà une bibliothèque intégrée pour faire des requêtes HTTP (`urllib`), mais elle est complexe et peu intuitive. C'est pourquoi `requests` a été créé.

**Comparaison rapide :**

```python
# Avec urllib (bibliothèque standard)
import urllib.request  
import json  

req = urllib.request.Request('https://api.example.com/data')  
req.add_header('Content-Type', 'application/json')  
response = urllib.request.urlopen(req)  
data = json.loads(response.read().decode('utf-8'))  

# Avec requests (beaucoup plus simple !)
import requests

response = requests.get('https://api.example.com/data')  
data = response.json()  
```

La différence est frappante ! `requests` rend le code beaucoup plus lisible et maintenable.

### Utilisations courantes de requests

- 🌐 **Consommer des APIs REST** : Récupérer des données depuis des services web
- 📊 **Web scraping** : Extraire des données de sites web
- 🔗 **Intégration de services** : Connecter votre application à des services tiers
- 🧪 **Tester des APIs** : Vérifier que vos endpoints fonctionnent correctement
- 📥 **Télécharger des fichiers** : Images, documents, données
- 🤖 **Créer des bots** : Automatiser des interactions web

## Installation

requests n'est pas inclus dans Python par défaut, mais son installation est très simple :

```bash
pip install requests
```

### Vérifier l'installation

```python
import requests  
print(requests.__version__)  
```

Vous devriez voir la version installée (par exemple, 2.31.0).

## Votre première requête

Commençons par l'exemple le plus simple : faire une requête GET.

```python
import requests

# Faire une requête GET
response = requests.get('https://api.github.com')

# Afficher le code de statut
print(f"Code de statut : {response.status_code}")

# Afficher le contenu
print(response.text)
```

C'est tout ! Vous venez de faire votre première requête HTTP avec Python.

### Décortiquons le code

```python
response = requests.get('https://api.github.com')
```

- `requests.get()` : Fonction qui envoie une requête GET
- L'URL est le seul argument obligatoire
- La fonction retourne un objet `Response` contenant la réponse du serveur

```python
response.status_code
```

Le code de statut HTTP (200 = OK, 404 = Not Found, etc.)

```python
response.text
```

Le contenu de la réponse sous forme de texte.

## Les méthodes HTTP

requests supporte toutes les méthodes HTTP standards.

### GET : Récupérer des données

La méthode GET est utilisée pour récupérer des données sans les modifier.

```python
import requests

# Requête GET simple
response = requests.get('https://api.github.com/users/torvalds')

# Vérifier le succès
if response.status_code == 200:
    print("Requête réussie !")
    user_data = response.json()
    print(f"Nom d'utilisateur : {user_data['login']}")
else:
    print(f"Erreur {response.status_code}")
```

### POST : Envoyer des données

La méthode POST est utilisée pour créer de nouvelles ressources ou soumettre des données.

```python
import requests

# Données à envoyer
data = {
    'username': 'alice',
    'email': 'alice@example.com',
    'age': 25
}

# Requête POST
response = requests.post('https://httpbin.org/post', json=data)

print(f"Code de statut : {response.status_code}")  
print(response.json())  
```

**Note :** Le paramètre `json=data` convertit automatiquement le dictionnaire en JSON et définit le bon header Content-Type.

### PUT : Mettre à jour complètement

La méthode PUT est utilisée pour remplacer complètement une ressource.

```python
import requests

# Données de mise à jour
data = {
    'username': 'alice_updated',
    'email': 'alice.new@example.com',
    'age': 26
}

# Requête PUT
response = requests.put('https://httpbin.org/put', json=data)

print(f"Mise à jour effectuée : {response.status_code}")
```

### PATCH : Mettre à jour partiellement

La méthode PATCH est utilisée pour modifier partiellement une ressource.

```python
import requests

# Seul l'email est modifié
data = {
    'email': 'alice.nouveau@example.com'
}

# Requête PATCH
response = requests.patch('https://httpbin.org/patch', json=data)

print("Email mis à jour")
```

### DELETE : Supprimer

La méthode DELETE est utilisée pour supprimer une ressource.

```python
import requests

# Requête DELETE
response = requests.delete('https://httpbin.org/delete')

if response.status_code == 200:
    print("Ressource supprimée avec succès")
```

### Tableau récapitulatif

| Méthode | Usage | Exemple |
|---------|-------|---------|
| **GET** | Récupérer des données | Lire un article, obtenir une liste |
| **POST** | Créer une ressource | Créer un compte, soumettre un formulaire |
| **PUT** | Remplacer complètement | Mettre à jour tout un profil |
| **PATCH** | Modifier partiellement | Changer juste l'email |
| **DELETE** | Supprimer | Supprimer un compte |

## Paramètres de requête (Query Parameters)

Les paramètres de requête sont ajoutés à l'URL après un `?`.

### Méthode manuelle (pas recommandé)

```python
response = requests.get('https://api.example.com/search?q=python&limit=10')
```

### Méthode recommandée avec params

```python
import requests

# Paramètres dans un dictionnaire
params = {
    'q': 'python',
    'limit': 10,
    'sort': 'date'
}

# requests construit l'URL automatiquement
response = requests.get('https://api.example.com/search', params=params)

# L'URL finale sera : https://api.example.com/search?q=python&limit=10&sort=date
print(f"URL complète : {response.url}")
```

**Avantages :**
- Plus lisible
- Gère automatiquement l'encodage des caractères spéciaux
- Plus facile à maintenir

### Exemple pratique : API GitHub

```python
import requests

# Rechercher des repositories Python
params = {
    'q': 'language:python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 5
}

response = requests.get('https://api.github.com/search/repositories', params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Nombre total de résultats : {data['total_count']}")

    for repo in data['items']:
        print(f"- {repo['name']} : {repo['stargazers_count']} étoiles")
```

## Headers HTTP

Les headers contiennent des métadonnées sur la requête ou la réponse.

### Lire les headers de la réponse

```python
import requests

response = requests.get('https://api.github.com')

# Afficher tous les headers
print(response.headers)

# Accéder à un header spécifique
print(f"Content-Type : {response.headers['Content-Type']}")  
print(f"Date : {response.headers['Date']}")  
```

### Envoyer des headers personnalisés

```python
import requests

# Headers personnalisés
headers = {
    'User-Agent': 'Mon Application Python/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer mon-token-secret'
}

response = requests.get('https://api.example.com/data', headers=headers)
```

### Headers courants

| Header | Usage |
|--------|-------|
| **Content-Type** | Type de données envoyées (application/json, etc.) |
| **Authorization** | Authentification (Bearer token, API key) |
| **User-Agent** | Identification du client |
| **Accept** | Type de réponse acceptée |
| **Accept-Language** | Langue préférée |

## Gérer les réponses

L'objet `Response` contient toutes les informations sur la réponse du serveur.

### Propriétés principales

```python
import requests

response = requests.get('https://api.github.com')

# Code de statut
print(f"Status Code : {response.status_code}")

# Texte brut de la réponse
print(f"Texte : {response.text[:100]}...")

# Contenu en bytes
print(f"Bytes : {response.content[:50]}")

# JSON automatiquement parsé
if 'application/json' in response.headers.get('Content-Type', ''):
    data = response.json()
    print(f"JSON : {data}")

# Headers de la réponse
print(f"Headers : {response.headers}")

# URL finale (après redirections éventuelles)
print(f"URL : {response.url}")

# Temps de réponse
print(f"Temps : {response.elapsed.total_seconds()} secondes")

# Encodage
print(f"Encodage : {response.encoding}")
```

### Vérifier le succès de la requête

```python
import requests

response = requests.get('https://api.example.com/data')

# Méthode 1 : Vérifier le code manuellement
if response.status_code == 200:
    print("Succès !")
elif response.status_code == 404:
    print("Ressource non trouvée")
else:
    print(f"Erreur {response.status_code}")

# Méthode 2 : Utiliser ok (True si code 200-299)
if response.ok:
    print("Requête réussie")

# Méthode 3 : Lever une exception si erreur
try:
    response.raise_for_status()
    print("Requête réussie")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e}")
```

### Parser le JSON

```python
import requests

response = requests.get('https://api.github.com/users/torvalds')

# Parser le JSON
data = response.json()

# Accéder aux données
print(f"Nom : {data['name']}")  
print(f"Bio : {data['bio']}")  
print(f"Repos publics : {data['public_repos']}")  
print(f"Followers : {data['followers']}")  
```

**Attention :** Si la réponse n'est pas du JSON valide, `response.json()` lèvera une exception.

```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("La réponse n'est pas du JSON valide")
```

## Envoyer des données

Il existe plusieurs façons d'envoyer des données avec requests.

### Envoyer du JSON

```python
import requests

# Données à envoyer
data = {
    'nom': 'Alice',
    'age': 25,
    'ville': 'Paris'
}

# Méthode recommandée : json=
response = requests.post('https://httpbin.org/post', json=data)

print(response.json())
```

Le paramètre `json=` :
- Convertit automatiquement le dictionnaire en JSON
- Définit le header `Content-Type: application/json`

### Envoyer des données de formulaire

```python
import requests

# Données de formulaire
data = {
    'username': 'alice',
    'password': 'secret123'
}

# data= envoie en format form-encoded
response = requests.post('https://httpbin.org/post', data=data)

print(response.json())
```

Le paramètre `data=` envoie les données en format `application/x-www-form-urlencoded`, comme un formulaire HTML classique.

### Envoyer des fichiers

**Avec context manager (recommandé) :**

```python
import requests

with open('document.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://httpbin.org/post', files=files)

print("Fichier envoyé")
```

### Envoyer plusieurs fichiers

```python
import requests

with open('document1.pdf', 'rb') as f1, \
     open('document2.pdf', 'rb') as f2, \
     open('image.jpg', 'rb') as f3:
    files = {
        'file1': f1,
        'file2': f2,
        'photo': f3
    }
    response = requests.post('https://httpbin.org/post', files=files)
```

### Spécifier le nom du fichier

```python
import requests

with open('document.pdf', 'rb') as f:
    files = {
        'file': ('mon_document.pdf', f, 'application/pdf')
    }
    response = requests.post('https://httpbin.org/post', files=files)
```

## Authentification

De nombreuses APIs nécessitent une authentification.

### Basic Authentication

```python
import requests  
from requests.auth import HTTPBasicAuth  

# Méthode 1 : Avec HTTPBasicAuth
response = requests.get(
    'https://api.example.com/user',
    auth=HTTPBasicAuth('username', 'password')
)

# Méthode 2 : Tuple (plus simple)
response = requests.get(
    'https://api.example.com/user',
    auth=('username', 'password')
)
```

### Bearer Token (JWT)

Très courant avec les APIs modernes :

```python
import requests

token = 'votre-token-jwt'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.example.com/protected', headers=headers)
```

### API Key

Certaines APIs utilisent des clés d'API :

```python
import requests

# Dans les headers
headers = {
    'X-API-Key': 'votre-cle-api'
}

response = requests.get('https://api.example.com/data', headers=headers)

# Ou dans les paramètres
params = {
    'api_key': 'votre-cle-api',
    'query': 'python'
}

response = requests.get('https://api.example.com/search', params=params)
```

### OAuth2

Pour OAuth2, vous devez généralement :

1. Obtenir un token d'accès
2. L'utiliser dans vos requêtes

```python
import requests

# Étape 1 : Obtenir le token
auth_response = requests.post('https://api.example.com/oauth/token', data={
    'grant_type': 'client_credentials',
    'client_id': 'votre_client_id',
    'client_secret': 'votre_client_secret'
})

token = auth_response.json()['access_token']

# Étape 2 : Utiliser le token
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.example.com/data', headers=headers)
```

## Sessions

Les sessions permettent de persister certains paramètres entre plusieurs requêtes.

### Pourquoi utiliser une session ?

Sans session, vous devez répéter les mêmes paramètres :

```python
import requests

headers = {'Authorization': 'Bearer token123'}

response1 = requests.get('https://api.example.com/users', headers=headers)  
response2 = requests.get('https://api.example.com/posts', headers=headers)  
response3 = requests.get('https://api.example.com/comments', headers=headers)  
```

Avec une session, c'est plus simple :

```python
import requests

session = requests.Session()  
session.headers.update({'Authorization': 'Bearer token123'})  

response1 = session.get('https://api.example.com/users')  
response2 = session.get('https://api.example.com/posts')  
response3 = session.get('https://api.example.com/comments')  
```

### Avantages des sessions

1. **Réutilisation des connexions** : Plus rapide (connection pooling)
2. **Persistance des cookies** : Maintient automatiquement les cookies
3. **Configuration partagée** : Headers, auth, etc. définis une fois

### Exemple complet avec session

```python
import requests

# Créer une session
session = requests.Session()

# Configurer la session
session.headers.update({
    'User-Agent': 'Mon Application/1.0',
    'Accept': 'application/json'
})

# Se connecter
login_data = {
    'username': 'alice',
    'password': 'secret'
}

response = session.post('https://api.example.com/login', json=login_data)

if response.ok:
    print("Connecté !")

    # Les cookies de session sont automatiquement conservés
    # Faire d'autres requêtes authentifiées
    profile = session.get('https://api.example.com/profile')
    posts = session.get('https://api.example.com/my-posts')

    # Se déconnecter
    session.post('https://api.example.com/logout')

# Fermer la session
session.close()
```

### Context manager pour les sessions

```python
import requests

with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token123'})

    response = session.get('https://api.example.com/data')
    print(response.json())

# La session est automatiquement fermée
```

## Timeouts

Il est important de définir des timeouts pour éviter que votre programme reste bloqué indéfiniment.

### Timeout simple

```python
import requests

try:
    # Timeout de 5 secondes
    response = requests.get('https://api.example.com/data', timeout=5)
except requests.exceptions.Timeout:
    print("La requête a pris trop de temps")
```

### Timeouts séparés (connexion et lecture)

```python
import requests

# (timeout_connexion, timeout_lecture)
response = requests.get('https://api.example.com/data', timeout=(3, 10))
```

- `3` secondes pour établir la connexion
- `10` secondes pour recevoir la réponse

### Timeout infini (déconseillé)

```python
# Ne JAMAIS faire ça en production !
response = requests.get('https://api.example.com/data', timeout=None)
```

## Gestion des erreurs

requests peut lever plusieurs types d'exceptions.

### Hiérarchie des exceptions

```
RequestException (classe de base)
├── ConnectionError (erreurs de connexion)
├── Timeout (délai dépassé)
├── TooManyRedirects (trop de redirections)
└── HTTPError (erreurs HTTP 4xx, 5xx)
```

### Gestion complète des erreurs

```python
import requests  
from requests.exceptions import RequestException, ConnectionError, Timeout, HTTPError  

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Lève HTTPError si 4xx ou 5xx
        return response.json()

    except Timeout:
        print("Erreur : La requête a pris trop de temps")

    except ConnectionError:
        print("Erreur : Impossible de se connecter au serveur")

    except HTTPError as e:
        print(f"Erreur HTTP : {e.response.status_code}")

    except requests.exceptions.JSONDecodeError:
        print("Erreur : La réponse n'est pas du JSON valide")

    except RequestException as e:
        print(f"Erreur inattendue : {e}")

    return None

# Utilisation
data = fetch_data('https://api.example.com/data')  
if data:  
    print("Données récupérées avec succès")
```

### Pattern try/except recommandé

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()

    # Traiter les données
    print(data)

except requests.exceptions.RequestException as e:
    # Gérer toutes les erreurs requests
    print(f"Erreur lors de la requête : {e}")
```

## Redirections

requests gère automatiquement les redirections HTTP.

### Comportement par défaut

```python
import requests

# Suit automatiquement les redirections
response = requests.get('https://github.com')

print(f"URL finale : {response.url}")  
print(f"Nombre de redirections : {len(response.history)}")  

# Historique des redirections
for resp in response.history:
    print(f"{resp.status_code} -> {resp.url}")
```

### Désactiver les redirections

```python
import requests

response = requests.get('https://github.com', allow_redirects=False)

if response.status_code in (301, 302, 303, 307, 308):
    print(f"Redirection vers : {response.headers['Location']}")
```

### Limiter le nombre de redirections

```python
import requests

session = requests.Session()  
session.max_redirects = 3  

try:
    response = session.get('https://example.com')
except requests.exceptions.TooManyRedirects:
    print("Trop de redirections")
```

## Cookies

requests gère automatiquement les cookies.

### Lire les cookies

```python
import requests

response = requests.get('https://www.example.com')

# Afficher tous les cookies
print(response.cookies)

# Accéder à un cookie spécifique
session_id = response.cookies.get('session_id')  
print(f"Session ID : {session_id}")  
```

### Envoyer des cookies

```python
import requests

# Cookies dans un dictionnaire
cookies = {
    'session_id': 'abc123',
    'user_token': 'xyz789'
}

response = requests.get('https://api.example.com/data', cookies=cookies)
```

### Cookies avec une session

```python
import requests

session = requests.Session()

# Les cookies sont automatiquement conservés
response1 = session.get('https://api.example.com/login')
# Le serveur envoie des cookies

response2 = session.get('https://api.example.com/profile')
# Les cookies sont automatiquement renvoyés
```

## Proxies

Si vous devez passer par un proxy :

```python
import requests

proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

response = requests.get('https://api.example.com', proxies=proxies)
```

### Proxy avec authentification

```python
import requests

proxies = {
    'http': 'http://user:password@proxy.example.com:8080',
    'https': 'http://user:password@proxy.example.com:8080'
}

response = requests.get('https://api.example.com', proxies=proxies)
```

## Télécharger des fichiers

### Télécharger en mémoire (petits fichiers)

```python
import requests

response = requests.get('https://example.com/image.jpg')

with open('image.jpg', 'wb') as f:
    f.write(response.content)

print("Image téléchargée")
```

### Télécharger en streaming (gros fichiers)

Pour les gros fichiers, utilisez le streaming pour ne pas saturer la mémoire :

```python
import requests

url = 'https://example.com/big_file.zip'

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    with open('big_file.zip', 'wb') as f:
        # Télécharger par blocs de 8 Ko
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

print("Fichier téléchargé")
```

### Avec barre de progression

```python
import requests  
from tqdm import tqdm  

url = 'https://example.com/big_file.zip'

response = requests.get(url, stream=True)  
total_size = int(response.headers.get('content-length', 0))  

with open('big_file.zip', 'wb') as f:
    with tqdm(total=total_size, unit='B', unit_scale=True) as progress_bar:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            progress_bar.update(len(chunk))

print("Téléchargement terminé !")
```

## Exemple pratique : Consommer une API publique

Créons un script qui utilise l'API publique de GitHub pour obtenir des informations.

```python
import requests  
import json  

class GitHubAPI:
    def __init__(self, token=None):
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                'Authorization': f'token {token}'
            })

        self.session.headers.update({
            'Accept': 'application/vnd.github+json'
        })

    def get_user(self, username):
        """Récupérer les informations d'un utilisateur"""
        url = f'{self.base_url}/users/{username}'
        response = self.session.get(url)

        if response.ok:
            return response.json()
        else:
            print(f"Erreur {response.status_code}")
            return None

    def get_user_repos(self, username, sort='updated'):
        """Récupérer les repositories d'un utilisateur"""
        url = f'{self.base_url}/users/{username}/repos'
        params = {
            'sort': sort,
            'per_page': 10
        }

        response = self.session.get(url, params=params)

        if response.ok:
            return response.json()
        else:
            return []

    def search_repositories(self, query, language=None, sort='stars'):
        """Rechercher des repositories"""
        url = f'{self.base_url}/search/repositories'

        # Construire la requête de recherche
        search_query = query
        if language:
            search_query += f' language:{language}'

        params = {
            'q': search_query,
            'sort': sort,
            'order': 'desc',
            'per_page': 5
        }

        response = self.session.get(url, params=params)

        if response.ok:
            return response.json()
        else:
            return None

# Utilisation
api = GitHubAPI()

# Obtenir les infos d'un utilisateur
user = api.get_user('torvalds')  
if user:  
    print(f"Nom : {user['name']}")
    print(f"Bio : {user['bio']}")
    print(f"Repos publics : {user['public_repos']}")
    print(f"Followers : {user['followers']}")
    print()

# Obtenir les repos d'un utilisateur
print("Repositories récents de torvalds :")  
repos = api.get_user_repos('torvalds')  
for repo in repos[:5]:  
    print(f"- {repo['name']} : {repo['description']}")
print()

# Rechercher des repos Python
print("Repos Python les plus populaires :")  
search_results = api.search_repositories('machine learning', language='python')  
if search_results:  
    for repo in search_results['items']:
        print(f"- {repo['full_name']} : {repo['stargazers_count']} ⭐")
```

## Exemple pratique : API de météo

```python
import requests  
from datetime import datetime  

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5'

    def get_current_weather(self, city):
        """Obtenir la météo actuelle"""
        url = f'{self.base_url}/weather'
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',  # Celsius
            'lang': 'fr'
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur : {e}")
            return None

    def display_weather(self, city):
        """Afficher la météo de manière formatée"""
        data = self.get_current_weather(city)

        if not data:
            print("Impossible de récupérer la météo")
            return

        print(f"\n🌍 Météo à {data['name']}, {data['sys']['country']}")
        print(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"🌡️  Température : {data['main']['temp']}°C")
        print(f"🤔 Ressenti : {data['main']['feels_like']}°C")
        print(f"☁️  Conditions : {data['weather'][0]['description']}")
        print(f"💧 Humidité : {data['main']['humidity']}%")
        print(f"💨 Vent : {data['wind']['speed']} m/s")

# Utilisation
api = WeatherAPI('VOTRE_CLE_API')  
api.display_weather('Paris')  
api.display_weather('London')  
api.display_weather('Tokyo')  
```

## Bonnes pratiques

### 1. Toujours définir un timeout

```python
# ✅ Bon
response = requests.get(url, timeout=5)

# ❌ Mauvais
response = requests.get(url)
```

### 2. Gérer les erreurs correctement

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")
```

### 3. Utiliser des sessions pour plusieurs requêtes

```python
# ✅ Bon - Plus rapide
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token'})
    response1 = session.get(url1)
    response2 = session.get(url2)

# ❌ Moins efficace
response1 = requests.get(url1, headers={'Authorization': 'Bearer token'})  
response2 = requests.get(url2, headers={'Authorization': 'Bearer token'})  
```

### 4. Ne pas exposer les clés API dans le code

```python
import os

# ✅ Bon - Utiliser des variables d'environnement
api_key = os.environ.get('API_KEY')

# ❌ Mauvais - Hardcoder la clé
api_key = 'ma-cle-secrete-123'
```

### 5. Vérifier le content-type avant de parser

```python
response = requests.get(url)

if 'application/json' in response.headers.get('Content-Type', ''):
    data = response.json()
else:
    print("La réponse n'est pas du JSON")
```

### 6. Utiliser raise_for_status()

```python
# ✅ Bon
response = requests.get(url)  
response.raise_for_status()  # Lève une exception si erreur  
data = response.json()  

# ❌ Moins robuste
response = requests.get(url)  
data = response.json()  # Peut échouer si erreur HTTP  
```

### 7. Respecter les limites de taux (rate limiting)

```python
import time  
import requests  

def api_call_with_rate_limit(url, delay=1):
    response = requests.get(url)
    time.sleep(delay)  # Attendre entre les requêtes
    return response

# Ou utiliser une bibliothèque dédiée
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=10, period=60)  # 10 appels par minute max
def call_api(url):
    return requests.get(url)
```

### 8. Logger les requêtes en développement

```python
import requests  
import logging  

# Activer les logs HTTP
import http.client as http_client  
http_client.HTTPConnection.debuglevel = 1  

logging.basicConfig()  
logging.getLogger().setLevel(logging.DEBUG)  
requests_log = logging.getLogger("urllib3")  
requests_log.setLevel(logging.DEBUG)  
requests_log.propagate = True  

# Maintenant, toutes les requêtes sont loggées
response = requests.get('https://api.github.com')
```

## Alternatives à requests

Bien que requests soit excellent, il existe des alternatives pour des cas spécifiques :

### httpx : requests avec support async

```python
import httpx

# Synchrone (comme requests)
response = httpx.get('https://api.example.com')

# Asynchrone
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com')
        return response.json()
```

### aiohttp : Complètement asynchrone

```python
import aiohttp  
import asyncio  

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com') as response:
            return await response.json()

asyncio.run(fetch_data())
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ Comment installer et utiliser la bibliothèque requests  
✅ Les différentes méthodes HTTP (GET, POST, PUT, PATCH, DELETE)  
✅ Comment envoyer des paramètres de requête et des headers  
✅ Comment gérer les réponses et parser le JSON  
✅ Comment envoyer des données (JSON, formulaires, fichiers)  
✅ Les différents types d'authentification (Basic, Bearer, API Key)  
✅ Comment utiliser les sessions pour optimiser les requêtes  
✅ L'importance des timeouts et la gestion des erreurs  
✅ Comment télécharger des fichiers  
✅ Les bonnes pratiques pour des requêtes HTTP robustes

La bibliothèque requests est un outil essentiel pour tout développeur Python travaillant avec des APIs web. Elle vous permet de consommer facilement n'importe quelle API REST et d'intégrer des services externes dans vos applications.

---


⏭️ [Création et consommation d'APIs REST](/11-developpement-web-et-apis/05-creation-consommation-apis-rest.md)
