🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 11.2 : Requêtes HTTP avec requests

## Introduction

La bibliothèque `requests` est l'outil de référence pour faire des requêtes HTTP en Python. Elle permet de communiquer facilement avec des APIs, télécharger des données depuis des sites web, ou envoyer des informations à des serveurs distants.

Imaginez `requests` comme un navigateur web programmable : au lieu de cliquer sur des liens, vous écrivez du code pour récupérer des données depuis Internet.

## Installation et import

### Installation

```bash
pip install requests
```

### Import de base

```python
import requests
```

## Comprendre les requêtes HTTP

### Qu'est-ce qu'une requête HTTP ?

Une requête HTTP est comme envoyer une lettre :
- **Destinataire** : l'URL du serveur
- **Type de demande** : GET (lire), POST (créer), PUT (modifier), DELETE (supprimer)
- **Contenu** : les données que vous voulez envoyer
- **En-têtes** : informations supplémentaires (comme le type de contenu)

### Anatomie d'une URL

```
https://api.exemple.com/utilisateurs/123?format=json
│      │                │            │   │
│      │                │            │   └── Paramètres de requête
│      │                │            └────── Ressource spécifique
│      │                └─────────────────── Chemin
│      └──────────────────────────────────── Domaine
└─────────────────────────────────────────── Protocole
```

## Requêtes GET : récupérer des données

### Requête GET simple

```python
import requests

# Faire une requête GET
response = requests.get('https://httpbin.org/get')

# Vérifier le statut
print(f"Code de statut : {response.status_code}")

# Afficher le contenu
print(response.text)
```

### Gestion des codes de statut

```python
import requests

def faire_requete(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("✅ Succès !")
            return response.json()  # Convertir JSON en dictionnaire Python
        elif response.status_code == 404:
            print("❌ Page non trouvée")
        elif response.status_code == 500:
            print("❌ Erreur serveur")
        else:
            print(f"⚠️ Code de statut : {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion : {e}")
        return None

# Utilisation
data = faire_requete('https://httpbin.org/get')
if data:
    print(data)
```

### Paramètres de requête

```python
import requests

# Méthode 1 : paramètres dans l'URL
url = 'https://httpbin.org/get?nom=Marie&age=25'
response = requests.get(url)

# Méthode 2 : paramètres séparés (recommandée)
url = 'https://httpbin.org/get'
parametres = {
    'nom': 'Marie',
    'age': 25,
    'ville': 'Paris'
}
response = requests.get(url, params=parametres)

print(f"URL finale : {response.url}")
print(response.json())
```

### En-têtes personnalisés

```python
import requests

# Définir des en-têtes
headers = {
    'User-Agent': 'Mon Application Python/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer votre-token-ici'
}

response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

## Exemple pratique : API météo

```python
import requests

def obtenir_meteo(ville, cle_api):
    """Récupère les données météo pour une ville donnée"""

    url = 'http://api.openweathermap.org/data/2.5/weather'
    parametres = {
        'q': ville,
        'appid': cle_api,
        'units': 'metric',  # Températures en Celsius
        'lang': 'fr'        # Descriptions en français
    }

    try:
        response = requests.get(url, params=parametres)

        if response.status_code == 200:
            data = response.json()

            # Extraire les informations importantes
            meteo = {
                'ville': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidite': data['main']['humidity'],
                'pression': data['main']['pressure']
            }

            return meteo
        else:
            print(f"Erreur API : {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return None

# Utilisation (vous devez obtenir une clé API gratuite sur openweathermap.org)
# cle_api = "votre_cle_api_ici"
# meteo = obtenir_meteo("Paris", cle_api)
# if meteo:
#     print(f"Météo à {meteo['ville']} :")
#     print(f"🌡️  Température : {meteo['temperature']}°C")
#     print(f"☁️  Description : {meteo['description']}")
#     print(f"💧 Humidité : {meteo['humidite']}%")
```

## Requêtes POST : envoyer des données

### POST avec données de formulaire

```python
import requests

# Données à envoyer
donnees = {
    'nom': 'Dupont',
    'prenom': 'Jean',
    'email': 'jean.dupont@email.com'
}

# Envoyer une requête POST
response = requests.post('https://httpbin.org/post', data=donnees)

print(f"Statut : {response.status_code}")
print("Réponse :", response.json())
```

### POST avec JSON

```python
import requests
import json

# Données JSON
utilisateur = {
    'nom': 'Martin',
    'age': 30,
    'ville': 'Lyon',
    'competences': ['Python', 'Flask', 'SQL']
}

# En-têtes pour JSON
headers = {'Content-Type': 'application/json'}

# Envoyer du JSON
response = requests.post(
    'https://httpbin.org/post',
    json=utilisateur,  # requests convertit automatiquement en JSON
    headers=headers
)

print("Données envoyées :", response.json()['json'])
```

### Upload de fichiers

```python
import requests

# Préparer le fichier
with open('document.txt', 'rb') as fichier:
    files = {'file': fichier}
    data = {'description': 'Mon document important'}

    response = requests.post(
        'https://httpbin.org/post',
        files=files,
        data=data
    )

print("Upload terminé :", response.status_code)
```

## Autres méthodes HTTP

### PUT : mettre à jour

```python
import requests

# Données de mise à jour
utilisateur_modifie = {
    'nom': 'Martin',
    'age': 31,  # Âge mis à jour
    'ville': 'Marseille'  # Ville changée
}

response = requests.put(
    'https://httpbin.org/put',
    json=utilisateur_modifie
)

print("Mise à jour :", response.json())
```

### DELETE : supprimer

```python
import requests

response = requests.delete('https://httpbin.org/delete')
print(f"Suppression : {response.status_code}")
```

### PATCH : mise à jour partielle

```python
import requests

# Seulement les champs à modifier
modifications = {
    'ville': 'Nice'  # Changer seulement la ville
}

response = requests.patch(
    'https://httpbin.org/patch',
    json=modifications
)

print("Modification partielle :", response.json())
```

## Gestion des sessions

### Pourquoi utiliser une session ?

Une session maintient certains paramètres entre plusieurs requêtes (cookies, en-têtes, authentification).

```python
import requests

# Créer une session
session = requests.Session()

# Configurer des en-têtes pour toute la session
session.headers.update({
    'User-Agent': 'Mon App/1.0',
    'Accept': 'application/json'
})

# Toutes les requêtes utiliseront ces en-têtes
response1 = session.get('https://httpbin.org/headers')
response2 = session.get('https://httpbin.org/user-agent')

# Fermer la session (optionnel)
session.close()
```

### Authentification avec session

```python
import requests

def connecter_api(nom_utilisateur, mot_de_passe):
    """Se connecter à une API et maintenir la session"""

    session = requests.Session()

    # Données de connexion
    login_data = {
        'username': nom_utilisateur,
        'password': mot_de_passe
    }

    # Se connecter
    response = session.post('https://exemple.com/login', data=login_data)

    if response.status_code == 200:
        print("✅ Connexion réussie")
        return session
    else:
        print("❌ Échec de la connexion")
        return None

# Utilisation
# session = connecter_api('utilisateur', 'motdepasse')
# if session:
#     # Utiliser la session pour d'autres requêtes
#     profile = session.get('https://exemple.com/profile')
```

## Téléchargement de fichiers

### Télécharger un petit fichier

```python
import requests

def telecharger_fichier(url, nom_fichier):
    """Télécharge un fichier depuis une URL"""

    try:
        response = requests.get(url)

        if response.status_code == 200:
            with open(nom_fichier, 'wb') as fichier:
                fichier.write(response.content)
            print(f"✅ Fichier téléchargé : {nom_fichier}")
        else:
            print(f"❌ Erreur {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de téléchargement : {e}")

# Utilisation
telecharger_fichier(
    'https://httpbin.org/robots.txt',
    'robots.txt'
)
```

### Télécharger un gros fichier (avec barre de progression)

```python
import requests
from tqdm import tqdm  # pip install tqdm

def telecharger_gros_fichier(url, nom_fichier):
    """Télécharge un gros fichier avec barre de progression"""

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Obtenir la taille du fichier
        taille_totale = int(response.headers.get('content-length', 0))

        with open(nom_fichier, 'wb') as fichier:
            with tqdm(total=taille_totale, unit='B', unit_scale=True) as barre:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        fichier.write(chunk)
                        barre.update(len(chunk))

        print(f"✅ Téléchargement terminé : {nom_fichier}")
    else:
        print(f"❌ Erreur {response.status_code}")

# Utilisation
# telecharger_gros_fichier('https://exemple.com/gros-fichier.zip', 'fichier.zip')
```

## Gestion des timeouts et retry

### Timeout

```python
import requests

try:
    # Timeout de 5 secondes
    response = requests.get('https://httpbin.org/delay/3', timeout=5)
    print("Requête réussie")
except requests.exceptions.Timeout:
    print("❌ Timeout : la requête a pris trop de temps")
except requests.exceptions.RequestException as e:
    print(f"❌ Autre erreur : {e}")
```

### Retry automatique

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def creer_session_avec_retry():
    """Crée une session avec retry automatique"""

    session = requests.Session()

    # Configuration du retry
    retry_strategy = Retry(
        total=3,  # Nombre total de tentatives
        backoff_factor=1,  # Délai entre les tentatives
        status_forcelist=[429, 500, 502, 503, 504]  # Codes d'erreur à retry
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session

# Utilisation
session = creer_session_avec_retry()
response = session.get('https://httpbin.org/status/500', timeout=5)
```

## Exemple complet : Client API

```python
import requests
import json

class ClientAPI:
    """Client simple pour interagir avec une API REST"""

    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

        # En-têtes par défaut
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

        # Authentification si fournie
        if token:
            self.session.headers['Authorization'] = f'Bearer {token}'

    def get(self, endpoint, params=None):
        """Effectue une requête GET"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()  # Lève une exception si erreur HTTP
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur GET {url}: {e}")
            return None

    def post(self, endpoint, data=None):
        """Effectue une requête POST"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur POST {url}: {e}")
            return None

    def put(self, endpoint, data=None):
        """Effectue une requête PUT"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.put(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur PUT {url}: {e}")
            return None

    def delete(self, endpoint):
        """Effectue une requête DELETE"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.delete(url, timeout=10)
            response.raise_for_status()
            return response.status_code == 204  # No Content
        except requests.exceptions.RequestException as e:
            print(f"Erreur DELETE {url}: {e}")
            return False

# Utilisation du client
def exemple_utilisation():
    # Créer le client
    api = ClientAPI('https://jsonplaceholder.typicode.com')

    # Récupérer tous les utilisateurs
    utilisateurs = api.get('/users')
    if utilisateurs:
        print(f"Nombre d'utilisateurs : {len(utilisateurs)}")
        print(f"Premier utilisateur : {utilisateurs[0]['name']}")

    # Récupérer un utilisateur spécifique
    utilisateur = api.get('/users/1')
    if utilisateur:
        print(f"Utilisateur 1 : {utilisateur['name']} - {utilisateur['email']}")

    # Créer un nouvel utilisateur
    nouvel_utilisateur = {
        'name': 'Marie Dupont',
        'username': 'marie.dupont',
        'email': 'marie@example.com'
    }

    resultat = api.post('/users', nouvel_utilisateur)
    if resultat:
        print(f"Utilisateur créé avec l'ID : {resultat['id']}")

# Exécuter l'exemple
exemple_utilisation()
```

## Exercices pratiques

### Exercice 1 : Récupérateur de citations

Créez un programme qui :
1. Récupère une citation aléatoire depuis l'API `https://api.quotable.io/random`
2. Affiche la citation et son auteur
3. Permet de récupérer plusieurs citations
4. Gère les erreurs de connexion

### Exercice 2 : Vérificateur de site web

Créez un programme qui :
1. Prend une liste d'URLs
2. Vérifie si chaque site est accessible (code 200)
3. Mesure le temps de réponse
4. Affiche un rapport de statut

### Exercice 3 : Client API GitHub

Créez un client simple pour l'API GitHub qui :
1. Récupère les informations d'un utilisateur
2. Liste ses repositories publics
3. Affiche les statistiques (nombre de repos, followers, etc.)

## Solutions des exercices

### Solution Exercice 1 : Récupérateur de citations

```python
import requests
import time

def obtenir_citation():
    """Récupère une citation aléatoire"""
    try:
        response = requests.get('https://api.quotable.io/random', timeout=5)

        if response.status_code == 200:
            data = response.json()
            return {
                'citation': data['content'],
                'auteur': data['author'],
                'longueur': data['length']
            }
        else:
            print(f"❌ Erreur API : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion : {e}")
        return None

def afficher_citation(citation_data):
    """Affiche une citation de manière formatée"""
    if citation_data:
        print("\n" + "="*50)
        print(f'"{citation_data["citation"]}"')
        print(f"\n— {citation_data['auteur']}")
        print(f"({citation_data['longueur']} caractères)")
        print("="*50)

def main():
    print("🎯 Récupérateur de citations inspirantes")
    print("Appuyez sur Entrée pour une nouvelle citation, 'q' pour quitter")

    while True:
        commande = input("\n➤ ").strip().lower()

        if commande == 'q':
            print("Au revoir ! 👋")
            break

        print("📥 Récupération d'une citation...")
        citation = obtenir_citation()
        afficher_citation(citation)

if __name__ == "__main__":
    main()
```

### Solution Exercice 2 : Vérificateur de site web

```python
import requests
import time
from datetime import datetime

def verifier_site(url, timeout=5):
    """Vérifie l'état d'un site web"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        debut = time.time()
        response = requests.get(url, timeout=timeout)
        temps_reponse = time.time() - debut

        return {
            'url': url,
            'statut': response.status_code,
            'temps_reponse': round(temps_reponse * 1000, 2),  # en ms
            'accessible': response.status_code == 200,
            'erreur': None
        }
    except requests.exceptions.RequestException as e:
        return {
            'url': url,
            'statut': None,
            'temps_reponse': None,
            'accessible': False,
            'erreur': str(e)
        }

def verifier_sites(liste_urls):
    """Vérifie une liste de sites"""
    resultats = []

    print(f"🔍 Vérification de {len(liste_urls)} sites...")
    print(f"⏰ Démarré à {datetime.now().strftime('%H:%M:%S')}\n")

    for i, url in enumerate(liste_urls, 1):
        print(f"[{i}/{len(liste_urls)}] Vérification de {url}...")
        resultat = verifier_site(url)
        resultats.append(resultat)

        # Affichage immédiat du résultat
        if resultat['accessible']:
            print(f"✅ OK ({resultat['temps_reponse']}ms)")
        else:
            print(f"❌ Échec - {resultat['erreur'] or f'Code {resultat['statut']}'}")

        time.sleep(0.5)  # Pause pour éviter de surcharger

    return resultats

def afficher_rapport(resultats):
    """Affiche un rapport détaillé"""
    print("\n" + "="*60)
    print("📊 RAPPORT DE VÉRIFICATION")
    print("="*60)

    sites_ok = sum(1 for r in resultats if r['accessible'])
    sites_ko = len(resultats) - sites_ok

    print(f"Total des sites : {len(resultats)}")
    print(f"✅ Accessibles : {sites_ok}")
    print(f"❌ Non accessibles : {sites_ko}")

    if sites_ok > 0:
        temps_moyen = sum(r['temps_reponse'] for r in resultats
                         if r['temps_reponse']) / sites_ok
        print(f"⚡ Temps de réponse moyen : {temps_moyen:.2f}ms")

    print("\nDétails :")
    print("-" * 60)

    for resultat in resultats:
        statut_icon = "✅" if resultat['accessible'] else "❌"
        temps = f"{resultat['temps_reponse']}ms" if resultat['temps_reponse'] else "N/A"

        print(f"{statut_icon} {resultat['url']:<30} | {temps:>8} | {resultat['statut'] or 'Erreur'}")

def main():
    sites_a_verifier = [
        'google.com',
        'github.com',
        'stackoverflow.com',
        'python.org',
        'site-inexistant-123456.com'  # Pour tester les erreurs
    ]

    resultats = verifier_sites(sites_a_verifier)
    afficher_rapport(resultats)

if __name__ == "__main__":
    main()
```

### Solution Exercice 3 : Client API GitHub

```python
import requests

class GitHubClient:
    """Client simple pour l'API GitHub"""

    def __init__(self):
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Python-GitHub-Client/1.0'
        })

    def obtenir_utilisateur(self, nom_utilisateur):
        """Récupère les informations d'un utilisateur"""
        url = f"{self.base_url}/users/{nom_utilisateur}"

        try:
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"❌ Utilisateur '{nom_utilisateur}' non trouvé")
                return None
            else:
                print(f"❌ Erreur {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion : {e}")
            return None

    def obtenir_repositories(self, nom_utilisateur, limite=10):
        """Récupère les repositories d'un utilisateur"""
        url = f"{self.base_url}/users/{nom_utilisateur}/repos"
        params = {
            'sort': 'updated',
            'per_page': limite
        }

        try:
            response = self.session.get(url, params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Erreur lors de la récupération des repos : {response.status_code}")
                return []

        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion : {e}")
            return []

def afficher_profil_utilisateur(client, nom_utilisateur):
    """Affiche le profil complet d'un utilisateur GitHub"""

    print(f"🔍 Recherche de l'utilisateur '{nom_utilisateur}'...")

    # Récupérer les infos utilisateur
    utilisateur = client.obtenir_utilisateur(nom_utilisateur)
    if not utilisateur:
        return

    # Afficher les informations
    print("\n" + "="*50)
    print(f"👤 {utilisateur['name'] or utilisateur['login']}")
    print("="*50)

    if utilisateur['bio']:
        print(f"📝 Bio : {utilisateur['bio']}")

    if utilisateur['location']:
        print(f"📍 Localisation : {utilisateur['location']}")

    if utilisateur['company']:
        print(f"🏢 Entreprise : {utilisateur['company']}")

    if utilisateur['blog']:
        print(f"🌐 Site web : {utilisateur['blog']}")

    print(f"\n📊 Statistiques :")
    print(f"   • Repositories publics : {utilisateur['public_repos']}")
    print(f"   • Followers : {utilisateur['followers']}")
    print(f"   • Following : {utilisateur['following']}")
    print(f"   • Membre depuis : {utilisateur['created_at'][:10]}")

    # Récupérer et afficher les repositories
    print(f"\n📚 Repositories récents :")
    repos = client.obtenir_repositories(nom_utilisateur, 5)

    if repos:
        for repo in repos:
            stars = repo['stargazers_count']
            langage = repo['language'] or 'Non spécifié'
            description = repo['description'] or 'Pas de description'

            print(f"\n   📁 {repo['name']}")
            print(f"      ⭐ {stars} stars | 🔤 {langage}")
            print(f"      💬 {description[:60]}{'...' if len(description) > 60 else ''}")
    else:
        print("   Aucun repository trouvé")

def main():
    client = GitHubClient()

    print("🐙 Client API GitHub")
    print("Entrez un nom d'utilisateur GitHub pour voir son profil")

    while True:
        nom_utilisateur = input("\n👤 Nom d'utilisateur (ou 'quit' pour quitter) : ").strip()

        if nom_utilisateur.lower() in ['quit', 'q', 'exit']:
            print("Au revoir ! 👋")
            break

        if nom_utilisateur:
            afficher_profil_utilisateur(client, nom_utilisateur)
        else:
            print("❌ Veuillez entrer un nom d'utilisateur valide")

if __name__ == "__main__":
    main()
```

## Bonnes pratiques

### Gestion des erreurs

```python
import requests

def requete_robuste(url, max_tentatives=3):
    """Fait une requête avec gestion d'erreurs robuste"""

    for tentative in range(max_tentatives):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Lève une exception si code d'erreur HTTP
            return response.json()

        except requests.exceptions.Timeout:
            print(f"⏰ Timeout (tentative {tentative + 1}/{max_tentatives})")
        except requests.exceptions.ConnectionError:
            print(f"🔌 Erreur de connexion (tentative {tentative + 1}/{max_tentatives})")
        except requests.exceptions.HTTPError as e:
            print(f"❌ Erreur HTTP {e.response.status_code}")
            break  # Pas la peine de réessayer pour les erreurs HTTP
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur générale : {e}")
            break

    return None
```

### Variables d'environnement pour les clés API

```python
import os
import requests

# Récupérer la clé API depuis les variables d'environnement
API_KEY = os.getenv('WEATHER_API_KEY')

if not API_KEY:
    raise ValueError("La variable d'environnement WEATHER_API_KEY n'est pas définie")

headers = {'Authorization': f'Bearer {API_KEY}'}
response = requests.get('https://api.exemple.com/data', headers=headers)
```

## Limitation du taux de requêtes

```python
import requests
import time

class APIClient:
    def __init__(self, delai_entre_requetes=1):
        self.session = requests.Session()
        self.derniere_requete = 0
        self.delai = delai_entre_requetes

    def get(self, url, **kwargs):
        # Attendre si nécessaire
        temps_ecoule = time.time() - self.derniere_requete
        if temps_ecoule < self.delai:
            time.sleep(self.delai - temps_ecoule)

        response = self.session.get(url, **kwargs)
        self.derniere_requete = time.time()
        return response

    def post(self, url, **kwargs):
        # Même logique pour POST
        temps_ecoule = time.time() - self.derniere_requete
        if temps_ecoule < self.delai:
            time.sleep(self.delai - temps_ecoule)

        response = self.session.post(url, **kwargs)
        self.derniere_requete = time.time()
        return response

# Utilisation : maximum 1 requête par seconde
client = APIClient(delai_entre_requetes=1)

# Ces requêtes respecteront automatiquement le délai
response1 = client.get('https://api.exemple.com/data1')
response2 = client.get('https://api.exemple.com/data2')  # Attendra 1 seconde
```

### Cache simple pour éviter les requêtes répétitives

```python
import requests
import time
from functools import wraps

def cache_requete(duree_cache=300):  # 5 minutes par défaut
    """Décorateur pour mettre en cache les réponses"""
    cache = {}

    def decorateur(func):
        @wraps(func)
        def wrapper(url, *args, **kwargs):
            maintenant = time.time()

            # Vérifier si on a une réponse en cache et si elle est encore valide
            if url in cache:
                reponse, timestamp = cache[url]
                if maintenant - timestamp < duree_cache:
                    print(f"📦 Réponse en cache pour {url}")
                    return reponse

            # Faire la requête si pas en cache ou expirée
            reponse = func(url, *args, **kwargs)
            cache[url] = (reponse, maintenant)
            print(f"🌐 Nouvelle requête pour {url}")
            return reponse

        return wrapper
    return decorateur

@cache_requete(duree_cache=60)  # Cache pendant 1 minute
def get_avec_cache(url):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Utilisation
data1 = get_avec_cache('https://api.quotable.io/random')  # Requête réseau
data2 = get_avec_cache('https://api.quotable.io/random')  # Depuis le cache
```

## Authentification avancée

### Authentification Basic

```python
import requests
from requests.auth import HTTPBasicAuth

# Méthode 1 : avec l'objet HTTPBasicAuth
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=HTTPBasicAuth('user', 'pass')
)

# Méthode 2 : avec un tuple (plus simple)
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=('user', 'pass')
)

print(f"Statut : {response.status_code}")
print(response.json())
```

### Authentification avec Token Bearer

```python
import requests

class APIClientAvecAuth:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                'Authorization': f'Bearer {token}'
            })

    def se_connecter(self, email, mot_de_passe):
        """Se connecter et récupérer un token"""
        login_data = {
            'email': email,
            'password': mot_de_passe
        }

        response = self.session.post(f'{self.base_url}/login', json=login_data)

        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                self.session.headers.update({
                    'Authorization': f'Bearer {token}'
                })
                print("✅ Connexion réussie")
                return True

        print("❌ Échec de la connexion")
        return False

    def get_donnees_protegees(self, endpoint):
        """Récupérer des données nécessitant une authentification"""
        response = self.session.get(f'{self.base_url}/{endpoint}')

        if response.status_code == 401:
            print("❌ Non autorisé : token invalide ou expiré")
            return None
        elif response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Erreur {response.status_code}")
            return None

# Utilisation
# client = APIClientAvecAuth('https://api.monsite.com')
# if client.se_connecter('user@email.com', 'monmotdepasse'):
#     donnees = client.get_donnees_protegees('profile')
```

### Authentification OAuth 2.0 (exemple simplifié)

```python
import requests
import webbrowser
from urllib.parse import urlparse, parse_qs

class OAuthClient:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None

    def obtenir_url_autorisation(self, authorization_url, scope=None):
        """Génère l'URL d'autorisation"""
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'scope': scope or 'read'
        }

        # Construire l'URL
        param_string = '&'.join([f'{k}={v}' for k, v in params.items()])
        url = f'{authorization_url}?{param_string}'

        print(f"🔗 Ouvrez cette URL dans votre navigateur :")
        print(url)
        webbrowser.open(url)

        return url

    def echanger_code_contre_token(self, token_url, authorization_code):
        """Échange le code d'autorisation contre un access token"""
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': authorization_code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

        response = requests.post(token_url, data=data)

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data.get('access_token')
            print("✅ Token obtenu avec succès")
            return True
        else:
            print(f"❌ Erreur lors de l'obtention du token : {response.status_code}")
            return False

    def faire_requete_authentifiee(self, url):
        """Faire une requête avec le token OAuth"""
        if not self.access_token:
            print("❌ Pas de token d'accès")
            return None

        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)

        return response.json() if response.status_code == 200 else None

# Exemple d'utilisation (GitHub OAuth)
# oauth = OAuthClient('your_client_id', 'your_client_secret', 'http://localhost:8000/callback')
# oauth.obtenir_url_autorisation('https://github.com/login/oauth/authorize', 'user:email')
# Après autorisation, récupérer le code et l'échanger
# oauth.echanger_code_contre_token('https://github.com/login/oauth/access_token', 'authorization_code')
```

## Proxies et configuration réseau

### Utilisation de proxies

```python
import requests

# Configuration des proxies
proxies = {
    'http': 'http://proxy.entreprise.com:8080',
    'https': 'https://proxy.entreprise.com:8080'
}

# Avec authentification proxy
proxies_avec_auth = {
    'http': 'http://utilisateur:motdepasse@proxy.entreprise.com:8080',
    'https': 'https://utilisateur:motdepasse@proxy.entreprise.com:8080'
}

# Utilisation
response = requests.get('https://httpbin.org/ip', proxies=proxies)
print("Votre IP via proxy :", response.json())

# Configurer pour toute une session
session = requests.Session()
session.proxies.update(proxies)
```

### Certificats SSL personnalisés

```python
import requests

# Ignorer la vérification SSL (pas recommandé en production)
response = requests.get('https://site-avec-certificat-invalide.com', verify=False)

# Utiliser un certificat personnalisé
response = requests.get('https://monsite.com', verify='/chemin/vers/certificat.pem')

# Configurer pour une session
session = requests.Session()
session.verify = '/chemin/vers/certificat.pem'
```

## Debugging et monitoring

### Logging des requêtes

```python
import requests
import logging

# Activer le logging détaillé
logging.basicConfig(level=logging.DEBUG)

# Logger spécifique pour requests
logger = logging.getLogger('requests.packages.urllib3')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# Maintenant toutes les requêtes seront loggées
response = requests.get('https://httpbin.org/get')
```

### Middleware de debugging personnalisé

```python
import requests
import time
from functools import wraps

def debug_requete(func):
    """Décorateur pour debugger les requêtes"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0] if args else kwargs.get('url', 'URL inconnue')

        print(f"🚀 Début de requête : {func.__name__.upper()} {url}")
        debut = time.time()

        try:
            response = func(*args, **kwargs)
            duree = time.time() - debut

            print(f"✅ Requête terminée en {duree:.2f}s - Statut : {response.status_code}")
            return response

        except Exception as e:
            duree = time.time() - debut
            print(f"❌ Erreur après {duree:.2f}s : {e}")
            raise

    return wrapper

# Appliquer le décorateur
requests.get = debug_requete(requests.get)
requests.post = debug_requete(requests.post)

# Maintenant toutes les requêtes seront debuggées
response = requests.get('https://httpbin.org/get')
```

### Métriques et monitoring

```python
import requests
import time
from collections import defaultdict

class MonitoringClient:
    def __init__(self):
        self.session = requests.Session()
        self.statistiques = {
            'total_requetes': 0,
            'erreurs': 0,
            'temps_total': 0,
            'par_statut': defaultdict(int),
            'par_domaine': defaultdict(int)
        }

    def _enregistrer_metriques(self, response, duree, erreur=None):
        """Enregistre les métriques de la requête"""
        self.statistiques['total_requetes'] += 1
        self.statistiques['temps_total'] += duree

        if erreur:
            self.statistiques['erreurs'] += 1
        else:
            self.statistiques['par_statut'][response.status_code] += 1

            # Extraire le domaine de l'URL
            from urllib.parse import urlparse
            domaine = urlparse(response.url).netloc
            self.statistiques['par_domaine'][domaine] += 1

    def get(self, url, **kwargs):
        """GET avec monitoring"""
        debut = time.time()

        try:
            response = self.session.get(url, **kwargs)
            duree = time.time() - debut
            self._enregistrer_metriques(response, duree)
            return response
        except Exception as e:
            duree = time.time() - debut
            self._enregistrer_metriques(None, duree, erreur=e)
            raise

    def afficher_statistiques(self):
        """Affiche les statistiques collectées"""
        stats = self.statistiques

        print("\n📊 Statistiques des requêtes")
        print("=" * 40)
        print(f"Total requêtes    : {stats['total_requetes']}")
        print(f"Erreurs          : {stats['erreurs']}")
        print(f"Taux de succès   : {((stats['total_requetes'] - stats['erreurs']) / max(stats['total_requetes'], 1) * 100):.1f}%")

        if stats['total_requetes'] > 0:
            temps_moyen = stats['temps_total'] / stats['total_requetes']
            print(f"Temps moyen      : {temps_moyen:.2f}s")

        if stats['par_statut']:
            print("\nCodes de statut :")
            for statut, count in sorted(stats['par_statut'].items()):
                print(f"  {statut}: {count}")

        if stats['par_domaine']:
            print("\nDomaines :")
            for domaine, count in sorted(stats['par_domaine'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {domaine}: {count}")

# Utilisation
client = MonitoringClient()

# Faire plusieurs requêtes
urls = [
    'https://httpbin.org/get',
    'https://httpbin.org/status/200',
    'https://httpbin.org/status/404',
    'https://api.github.com/users/octocat'
]

for url in urls:
    try:
        response = client.get(url)
        print(f"✅ {url} - {response.status_code}")
    except Exception as e:
        print(f"❌ {url} - {e}")

# Afficher les statistiques
client.afficher_statistiques()
```

## Cas d'usage avancés

### Scraping respectueux avec robots.txt

```python
import requests
from urllib.robotparser import RobotFileParser
import time

class ScrapeurRespectueux:
    def __init__(self, user_agent='*'):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mon Bot Respectueux/1.0'
        })
        self.robots_cache = {}
        self.delai_defaut = 1  # 1 seconde entre les requêtes

    def verifier_robots_txt(self, url):
        """Vérifie si l'URL est autorisée par robots.txt"""
        from urllib.parse import urljoin, urlparse

        domaine = f"{urlparse(url).scheme}://{urlparse(url).netloc}"

        if domaine not in self.robots_cache:
            robots_url = urljoin(domaine, '/robots.txt')

            try:
                rp = RobotFileParser()
                rp.set_url(robots_url)
                rp.read()
                self.robots_cache[domaine] = rp
            except:
                # Si robots.txt n'est pas accessible, on autorise
                self.robots_cache[domaine] = None

        robots = self.robots_cache[domaine]
        if robots:
            return robots.can_fetch('*', url)
        return True  # Autoriser si pas de robots.txt

    def scraper_page(self, url, delai=None):
        """Scrape une page en respectant robots.txt et les délais"""
        if not self.verifier_robots_txt(url):
            print(f"❌ Accès interdit par robots.txt : {url}")
            return None

        # Respecter le délai
        time.sleep(delai or self.delai_defaut)

        try:
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                print(f"✅ Page récupérée : {url}")
                return response.text
            else:
                print(f"❌ Erreur {response.status_code} : {url}")
                return None
        except Exception as e:
            print(f"❌ Erreur de connexion : {e}")
            return None

# Utilisation
scraper = ScrapeurRespectueux()
contenu = scraper.scraper_page('https://example.com')
```

### API avec pagination

```python
import requests

def recuperer_toutes_pages(url_base, params=None, limite_pages=None):
    """Récupère toutes les pages d'une API paginée"""

    tous_resultats = []
    page_courante = 1
    params = params or {}

    while True:
        # Ajouter le numéro de page aux paramètres
        params_page = params.copy()
        params_page['page'] = page_courante

        print(f"📄 Récupération de la page {page_courante}...")

        try:
            response = requests.get(url_base, params=params_page, timeout=10)

            if response.status_code != 200:
                print(f"❌ Erreur {response.status_code}")
                break

            data = response.json()

            # Adapter selon la structure de votre API
            if 'results' in data:
                resultats_page = data['results']
            elif 'data' in data:
                resultats_page = data['data']
            else:
                resultats_page = data

            if not resultats_page:  # Plus de résultats
                print("✅ Toutes les pages récupérées")
                break

            tous_resultats.extend(resultats_page)
            print(f"   → {len(resultats_page)} éléments récupérés")

            # Vérifier s'il y a une page suivante
            if 'next' in data and not data['next']:
                break

            # Limite de sécurité
            if limite_pages and page_courante >= limite_pages:
                print(f"⚠️ Limite de {limite_pages} pages atteinte")
                break

            page_courante += 1
            time.sleep(0.5)  # Pause entre les requêtes

        except Exception as e:
            print(f"❌ Erreur page {page_courante} : {e}")
            break

    print(f"📊 Total récupéré : {len(tous_resultats)} éléments")
    return tous_resultats

# Utilisation avec l'API JSONPlaceholder
def exemple_pagination():
    # Cette API ne supporte pas vraiment la pagination, c'est juste un exemple
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Simuler une pagination en récupérant les posts par petits groupes
    tous_posts = []

    for page in range(1, 4):  # Pages 1 à 3
        params = {'_page': page, '_limit': 10}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            posts = response.json()
            if posts:
                tous_posts.extend(posts)
                print(f"Page {page} : {len(posts)} posts")
            else:
                break

    print(f"Total : {len(tous_posts)} posts récupérés")
    return tous_posts

# Exécuter l'exemple
posts = exemple_pagination()
```

## Intégration avec Flask

### Créer un proxy API avec Flask

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/proxy/<path:url>')
def proxy_api(url):
    """Proxy pour contourner les problèmes CORS"""

    # Reconstituer l'URL complète
    url_complete = f"https://{url}"

    # Transmettre les paramètres de la requête originale
    params = request.args.to_dict()

    try:
        # Faire la requête vers l'API externe
        response = requests.get(url_complete, params=params, timeout=10)

        # Retourner la réponse JSON
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                'error': f'API error {response.status_code}'
            }), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather/<ville>')
def meteo_ville(ville):
    """Endpoint pour récupérer la météo d'une ville"""

    # Remplacez par votre vraie clé API
    API_KEY = "your_api_key_here"

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': ville,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # Simplifier la réponse
            meteo_simple = {
                'ville': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidite': data['main']['humidity']
            }

            return jsonify(meteo_simple)
        else:
            return jsonify({'error': 'Ville non trouvée'}), 404

    except Exception as e:
        return jsonify({'error': 'Erreur de service'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Consommer des APIs depuis Flask

```python
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('api_dashboard.html')

@app.route('/citations')
def citations():
    """Page affichant des citations aléatoires"""

    citations = []

    # Récupérer 5 citations
    for _ in range(5):
        try:
            response = requests.get('https://api.quotable.io/random', timeout=5)
            if response.status_code == 200:
                citation_data = response.json()
                citations.append({
                    'texte': citation_data['content'],
                    'auteur': citation_data['author']
                })
        except:
            continue  # Ignorer les erreurs

    return render_template('citations.html', citations=citations)

@app.route('/github/<nom_utilisateur>')
def profil_github(nom_utilisateur):
    """Afficher le profil GitHub d'un utilisateur"""

    try:
        # Récupérer les infos utilisateur
        user_response = requests.get(f'https://api.github.com/users/{nom_utilisateur}', timeout=10)

        if user_response.status_code == 404:
            return render_template('error.html', message="Utilisateur non trouvé"), 404

        if user_response.status_code != 200:
            return render_template('error.html', message="Erreur API GitHub"), 500

        utilisateur = user_response.json()

        # Récupérer les repositories
        repos_response = requests.get(f'https://api.github.com/users/{nom_utilisateur}/repos',
                                    params={'sort': 'updated', 'per_page': 10}, timeout=10)

        repositories = repos_response.json() if repos_response.status_code == 200 else []

        return render_template('github_profile.html',
                             utilisateur=utilisateur,
                             repositories=repositories)

    except Exception as e:
        return render_template('error.html', message=f"Erreur : {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## Résumé des concepts clés

### Points essentiels à retenir

1. **Requests est simple** : `requests.get(url)` pour récupérer des données
2. **Gestion d'erreurs** : Toujours utiliser `try/except` et vérifier `status_code`
3. **Sessions** : Pour maintenir des paramètres entre requêtes multiples
4. **Respect des APIs** : Gérer les timeouts, rate limiting et robots.txt
5. **Sécurité** : Ne jamais exposer les clés API dans le code

### Checklist pour requêtes robustes

```python
def requete_robuste_exemple(url, data=None):
    """Modèle de requête robuste"""

    try:
        # Configuration de la requête
        headers = {'User-Agent': 'Mon App/1.0'}
        timeout = 10

        # Choisir la méthode appropriée
        if data:
            response = requests.post(url, json=data, headers=headers, timeout=timeout)
        else:
            response = requests.get(url, headers=headers, timeout=timeout)

        # Vérifier le statut
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Ressource non trouvée")
            return None
        else:
            print(f"Erreur HTTP {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("Requête trop lente")
        return None
    except requests.exceptions.ConnectionError:
        print("Problème de connexion")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

# ✅ Utilise des headers appropriés
# ✅ Gère les timeouts
# ✅ Vérifie les codes de statut
# ✅ Gère les exceptions
# ✅ Retourne des valeurs cohérentes
```

La maîtrise de `requests` vous permet de créer des applications qui communiquent efficacement avec le web. Dans la prochaine section, nous verrons comment créer vos propres APIs REST pour que d'autres applications puissent communiquer avec la vôtre !

---

*Pratiquez en appelant différentes APIs publiques pour vous familiariser avec les concepts.*

⏭️
