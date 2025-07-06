🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 11.3 : Création et consommation d'APIs REST

## Introduction

Une API REST (Representational State Transfer) est comme un serveur de restaurant : vous passez une commande (requête) avec des instructions précises, et le serveur vous apporte ce que vous avez demandé (réponse). C'est le moyen standard pour que les applications communiquent entre elles sur Internet.

Dans cette section, nous allons apprendre à créer nos propres APIs avec Flask et à les consommer correctement.

## Qu'est-ce qu'une API REST ?

### Concepts fondamentaux

**API** = Interface de Programmation d'Application
- C'est un contrat qui définit comment communiquer avec une application
- Permet d'accéder aux données et fonctionnalités sans connaître le code interne

**REST** = Style architectural avec des règles précises :
1. **Stateless** : chaque requête est indépendante
2. **Ressources** : tout est identifié par des URLs
3. **Méthodes HTTP** : GET, POST, PUT, DELETE pour différentes actions
4. **Représentations** : données échangées en JSON/XML

### Structure d'une API REST

```
GET    /api/utilisateurs        # Liste tous les utilisateurs
POST   /api/utilisateurs        # Crée un nouvel utilisateur
GET    /api/utilisateurs/123    # Récupère l'utilisateur 123
PUT    /api/utilisateurs/123    # Met à jour l'utilisateur 123
DELETE /api/utilisateurs/123    # Supprime l'utilisateur 123
```

### Codes de statut HTTP essentiels

- **200 OK** : Succès
- **201 Created** : Ressource créée
- **400 Bad Request** : Requête invalide
- **401 Unauthorized** : Non authentifié
- **403 Forbidden** : Non autorisé
- **404 Not Found** : Ressource non trouvée
- **500 Internal Server Error** : Erreur serveur

## Création d'une API REST simple avec Flask

### Structure de base

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Données simulées (en production, utilisez une vraie base de données)
utilisateurs = [
    {
        'id': 1,
        'nom': 'Dupont',
        'prenom': 'Jean',
        'email': 'jean.dupont@email.com',
        'date_creation': '2024-01-15'
    },
    {
        'id': 2,
        'nom': 'Martin',
        'prenom': 'Marie',
        'email': 'marie.martin@email.com',
        'date_creation': '2024-01-20'
    }
]

# Variable pour générer des IDs uniques
prochain_id = 3

@app.route('/api/utilisateurs', methods=['GET'])
def obtenir_tous_utilisateurs():
    """Récupère la liste de tous les utilisateurs"""
    return jsonify({
        'success': True,
        'data': utilisateurs,
        'count': len(utilisateurs)
    })

@app.route('/api/utilisateurs/<int:user_id>', methods=['GET'])
def obtenir_utilisateur(user_id):
    """Récupère un utilisateur spécifique par son ID"""
    utilisateur = next((u for u in utilisateurs if u['id'] == user_id), None)

    if utilisateur:
        return jsonify({
            'success': True,
            'data': utilisateur
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Ajouter des utilisateurs (POST)

```python
@app.route('/api/utilisateurs', methods=['POST'])
def creer_utilisateur():
    """Crée un nouvel utilisateur"""
    global prochain_id

    # Récupérer les données JSON de la requête
    donnees = request.get_json()

    # Validation basique
    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Aucune donnée fournie'
        }), 400

    champs_requis = ['nom', 'prenom', 'email']
    for champ in champs_requis:
        if champ not in donnees or not donnees[champ]:
            return jsonify({
                'success': False,
                'error': f'Le champ {champ} est obligatoire'
            }), 400

    # Vérifier que l'email n'existe pas déjà
    email_existe = any(u['email'] == donnees['email'] for u in utilisateurs)
    if email_existe:
        return jsonify({
            'success': False,
            'error': 'Cet email existe déjà'
        }), 400

    # Créer le nouvel utilisateur
    nouvel_utilisateur = {
        'id': prochain_id,
        'nom': donnees['nom'],
        'prenom': donnees['prenom'],
        'email': donnees['email'],
        'date_creation': datetime.now().strftime('%Y-%m-%d')
    }

    utilisateurs.append(nouvel_utilisateur)
    prochain_id += 1

    return jsonify({
        'success': True,
        'data': nouvel_utilisateur,
        'message': 'Utilisateur créé avec succès'
    }), 201
```

### Modifier des utilisateurs (PUT)

```python
@app.route('/api/utilisateurs/<int:user_id>', methods=['PUT'])
def modifier_utilisateur(user_id):
    """Modifie un utilisateur existant"""

    # Trouver l'utilisateur
    utilisateur = next((u for u in utilisateurs if u['id'] == user_id), None)

    if not utilisateur:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

    # Récupérer les nouvelles données
    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Aucune donnée fournie'
        }), 400

    # Mettre à jour les champs fournis
    champs_modifiables = ['nom', 'prenom', 'email']

    for champ in champs_modifiables:
        if champ in donnees:
            # Vérification spéciale pour l'email
            if champ == 'email':
                email_existe = any(u['email'] == donnees['email'] and u['id'] != user_id
                                 for u in utilisateurs)
                if email_existe:
                    return jsonify({
                        'success': False,
                        'error': 'Cet email est déjà utilisé'
                    }), 400

            utilisateur[champ] = donnees[champ]

    return jsonify({
        'success': True,
        'data': utilisateur,
        'message': 'Utilisateur modifié avec succès'
    })
```

### Supprimer des utilisateurs (DELETE)

```python
@app.route('/api/utilisateurs/<int:user_id>', methods=['DELETE'])
def supprimer_utilisateur(user_id):
    """Supprime un utilisateur"""
    global utilisateurs

    # Trouver l'index de l'utilisateur
    index = next((i for i, u in enumerate(utilisateurs) if u['id'] == user_id), None)

    if index is None:
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404

    # Supprimer l'utilisateur
    utilisateur_supprime = utilisateurs.pop(index)

    return jsonify({
        'success': True,
        'message': f'Utilisateur {utilisateur_supprime["prenom"]} {utilisateur_supprime["nom"]} supprimé',
        'data': utilisateur_supprime
    })
```

## API complète avec gestion d'erreurs

```python
from flask import Flask, jsonify, request
from datetime import datetime
import re

app = Flask(__name__)

# Configuration
app.config['JSON_SORT_KEYS'] = False  # Garder l'ordre des clés JSON

# Données simulées
utilisateurs = [
    {'id': 1, 'nom': 'Dupont', 'prenom': 'Jean', 'email': 'jean.dupont@email.com', 'age': 25, 'date_creation': '2024-01-15'},
    {'id': 2, 'nom': 'Martin', 'prenom': 'Marie', 'email': 'marie.martin@email.com', 'age': 30, 'date_creation': '2024-01-20'}
]
prochain_id = 3

def valider_email(email):
    """Valide le format d'un email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def valider_utilisateur(donnees, modification=False):
    """Valide les données d'un utilisateur"""
    erreurs = []

    # Champs obligatoires pour création
    if not modification:
        champs_requis = ['nom', 'prenom', 'email']
        for champ in champs_requis:
            if champ not in donnees or not str(donnees[champ]).strip():
                erreurs.append(f'Le champ {champ} est obligatoire')

    # Validation de l'email si fourni
    if 'email' in donnees:
        if not valider_email(donnees['email']):
            erreurs.append('Format d\'email invalide')

    # Validation de l'âge si fourni
    if 'age' in donnees:
        try:
            age = int(donnees['age'])
            if age < 0 or age > 120:
                erreurs.append('L\'âge doit être entre 0 et 120 ans')
        except (ValueError, TypeError):
            erreurs.append('L\'âge doit être un nombre entier')

    # Validation des noms si fournis
    for champ in ['nom', 'prenom']:
        if champ in donnees:
            if len(str(donnees[champ]).strip()) < 2:
                erreurs.append(f'Le {champ} doit contenir au moins 2 caractères')

    return erreurs

def formater_reponse(success=True, data=None, message=None, error=None):
    """Formate une réponse API standard"""
    reponse = {'success': success}

    if data is not None:
        reponse['data'] = data

    if message:
        reponse['message'] = message

    if error:
        reponse['error'] = error

    return reponse

# === ROUTES DE L'API ===

@app.route('/api/utilisateurs', methods=['GET'])
def obtenir_tous_utilisateurs():
    """Récupère tous les utilisateurs avec options de filtrage et pagination"""

    # Paramètres de requête
    page = request.args.get('page', 1, type=int)
    limite = request.args.get('limit', 10, type=int)
    recherche = request.args.get('search', '', type=str)

    # Filtrer par recherche si spécifiée
    utilisateurs_filtres = utilisateurs
    if recherche:
        recherche = recherche.lower()
        utilisateurs_filtres = [
            u for u in utilisateurs
            if recherche in u['nom'].lower()
            or recherche in u['prenom'].lower()
            or recherche in u['email'].lower()
        ]

    # Pagination
    debut = (page - 1) * limite
    fin = debut + limite
    utilisateurs_page = utilisateurs_filtres[debut:fin]

    return jsonify(formater_reponse(
        data=utilisateurs_page,
        message=f'{len(utilisateurs_page)} utilisateurs trouvés'
    ))

@app.route('/api/utilisateurs/<int:user_id>', methods=['GET'])
def obtenir_utilisateur(user_id):
    """Récupère un utilisateur spécifique"""
    utilisateur = next((u for u in utilisateurs if u['id'] == user_id), None)

    if utilisateur:
        return jsonify(formater_reponse(data=utilisateur))
    else:
        return jsonify(formater_reponse(
            success=False,
            error='Utilisateur non trouvé'
        )), 404

@app.route('/api/utilisateurs', methods=['POST'])
def creer_utilisateur():
    """Crée un nouvel utilisateur"""
    global prochain_id

    donnees = request.get_json()

    if not donnees:
        return jsonify(formater_reponse(
            success=False,
            error='Aucune donnée JSON fournie'
        )), 400

    # Validation
    erreurs = valider_utilisateur(donnees)
    if erreurs:
        return jsonify(formater_reponse(
            success=False,
            error='Données invalides',
            data={'erreurs': erreurs}
        )), 400

    # Vérifier unicité de l'email
    if any(u['email'] == donnees['email'] for u in utilisateurs):
        return jsonify(formater_reponse(
            success=False,
            error='Un utilisateur avec cet email existe déjà'
        )), 400

    # Créer l'utilisateur
    nouvel_utilisateur = {
        'id': prochain_id,
        'nom': donnees['nom'].strip(),
        'prenom': donnees['prenom'].strip(),
        'email': donnees['email'].lower().strip(),
        'age': donnees.get('age'),
        'date_creation': datetime.now().strftime('%Y-%m-%d')
    }

    utilisateurs.append(nouvel_utilisateur)
    prochain_id += 1

    return jsonify(formater_reponse(
        data=nouvel_utilisateur,
        message='Utilisateur créé avec succès'
    )), 201

@app.route('/api/utilisateurs/<int:user_id>', methods=['PUT'])
def modifier_utilisateur(user_id):
    """Modifie un utilisateur existant"""

    utilisateur = next((u for u in utilisateurs if u['id'] == user_id), None)

    if not utilisateur:
        return jsonify(formater_reponse(
            success=False,
            error='Utilisateur non trouvé'
        )), 404

    donnees = request.get_json()

    if not donnees:
        return jsonify(formater_reponse(
            success=False,
            error='Aucune donnée JSON fournie'
        )), 400

    # Validation
    erreurs = valider_utilisateur(donnees, modification=True)
    if erreurs:
        return jsonify(formater_reponse(
            success=False,
            error='Données invalides',
            data={'erreurs': erreurs}
        )), 400

    # Vérifier unicité de l'email si modifié
    if 'email' in donnees:
        if any(u['email'] == donnees['email'] and u['id'] != user_id for u in utilisateurs):
            return jsonify(formater_reponse(
                success=False,
                error='Un autre utilisateur utilise déjà cet email'
            )), 400

    # Mettre à jour les champs
    champs_modifiables = ['nom', 'prenom', 'email', 'age']
    for champ in champs_modifiables:
        if champ in donnees:
            if champ in ['nom', 'prenom']:
                utilisateur[champ] = donnees[champ].strip()
            elif champ == 'email':
                utilisateur[champ] = donnees[champ].lower().strip()
            else:
                utilisateur[champ] = donnees[champ]

    return jsonify(formater_reponse(
        data=utilisateur,
        message='Utilisateur modifié avec succès'
    ))

@app.route('/api/utilisateurs/<int:user_id>', methods=['DELETE'])
def supprimer_utilisateur(user_id):
    """Supprime un utilisateur"""
    global utilisateurs

    index = next((i for i, u in enumerate(utilisateurs) if u['id'] == user_id), None)

    if index is None:
        return jsonify(formater_reponse(
            success=False,
            error='Utilisateur non trouvé'
        )), 404

    utilisateur_supprime = utilisateurs.pop(index)

    return jsonify(formater_reponse(
        message=f'Utilisateur {utilisateur_supprime["prenom"]} {utilisateur_supprime["nom"]} supprimé avec succès'
    ))

# === GESTION DES ERREURS GLOBALES ===

@app.errorhandler(400)
def bad_request(error):
    return jsonify(formater_reponse(
        success=False,
        error='Requête invalide'
    )), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify(formater_reponse(
        success=False,
        error='Endpoint non trouvé'
    )), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify(formater_reponse(
        success=False,
        error='Erreur interne du serveur'
    )), 500

@app.before_request
def before_request():
    """Traitement avant chaque requête"""
    # Vérifier que les requêtes POST/PUT contiennent du JSON
    if request.method in ['POST', 'PUT']:
        if not request.is_json:
            return jsonify(formater_reponse(
                success=False,
                error='Content-Type doit être application/json'
            )), 400

if __name__ == '__main__':
    app.run(debug=True)
```

## Test de l'API

### Avec curl (ligne de commande)

```bash
# Récupérer tous les utilisateurs
curl -X GET http://localhost:5000/api/utilisateurs

# Récupérer un utilisateur spécifique
curl -X GET http://localhost:5000/api/utilisateurs/1

# Créer un nouvel utilisateur
curl -X POST http://localhost:5000/api/utilisateurs \
  -H "Content-Type: application/json" \
  -d '{"nom": "Durand", "prenom": "Pierre", "email": "pierre.durand@email.com", "age": 28}'

# Modifier un utilisateur
curl -X PUT http://localhost:5000/api/utilisateurs/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 26}'

# Supprimer un utilisateur
curl -X DELETE http://localhost:5000/api/utilisateurs/1
```

### Avec Python et requests

```python
import requests
import json

# URL de base de votre API
BASE_URL = 'http://localhost:5000/api'

def tester_api():
    """Teste toutes les fonctionnalités de l'API"""

    print("🧪 Test de l'API REST")
    print("=" * 40)

    # 1. Récupérer tous les utilisateurs
    print("\n1. 📋 Récupération de tous les utilisateurs")
    response = requests.get(f'{BASE_URL}/utilisateurs')
    print(f"   Statut: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Nombre d'utilisateurs: {len(data['data'])}")
        for user in data['data']:
            print(f"   - {user['prenom']} {user['nom']} ({user['email']})")

    # 2. Créer un nouvel utilisateur
    print("\n2. ➕ Création d'un nouvel utilisateur")
    nouvel_utilisateur = {
        'nom': 'Dubois',
        'prenom': 'Sophie',
        'email': 'sophie.dubois@email.com',
        'age': 27
    }

    response = requests.post(f'{BASE_URL}/utilisateurs', json=nouvel_utilisateur)
    print(f"   Statut: {response.status_code}")
    if response.status_code == 201:
        data = response.json()
        print(f"   ✅ Utilisateur créé avec l'ID: {data['data']['id']}")
        user_id = data['data']['id']
    else:
        print(f"   ❌ Erreur: {response.json()}")
        return

    # 3. Récupérer l'utilisateur créé
    print(f"\n3. 🔍 Récupération de l'utilisateur {user_id}")
    response = requests.get(f'{BASE_URL}/utilisateurs/{user_id}')
    print(f"   Statut: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        user = data['data']
        print(f"   ✅ {user['prenom']} {user['nom']} - {user['email']}")

    # 4. Modifier l'utilisateur
    print(f"\n4. ✏️ Modification de l'utilisateur {user_id}")
    modifications = {'age': 28, 'email': 'sophie.dubois.new@email.com'}

    response = requests.put(f'{BASE_URL}/utilisateurs/{user_id}', json=modifications)
    print(f"   Statut: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ {data['message']}")
        print(f"   Nouvel âge: {data['data']['age']}")
        print(f"   Nouvel email: {data['data']['email']}")

    # 5. Tester une erreur (email déjà existant)
    print(f"\n5. ❌ Test d'erreur - Email déjà existant")
    utilisateur_erreur = {
        'nom': 'Test',
        'prenom': 'Erreur',
        'email': 'jean.dupont@email.com'  # Email déjà existant
    }

    response = requests.post(f'{BASE_URL}/utilisateurs', json=utilisateur_erreur)
    print(f"   Statut: {response.status_code}")
    if response.status_code == 400:
        data = response.json()
        print(f"   ✅ Erreur correctement gérée: {data['error']}")

    # 6. Supprimer l'utilisateur
    print(f"\n6. 🗑️ Suppression de l'utilisateur {user_id}")
    response = requests.delete(f'{BASE_URL}/utilisateurs/{user_id}')
    print(f"   Statut: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ {data['message']}")

    # 7. Vérifier que l'utilisateur n'existe plus
    print(f"\n7. 🔍 Vérification de la suppression")
    response = requests.get(f'{BASE_URL}/utilisateurs/{user_id}')
    print(f"   Statut: {response.status_code}")
    if response.status_code == 404:
        print("   ✅ Utilisateur correctement supprimé")

    print("\n🎉 Tests terminés !")

if __name__ == '__main__':
    tester_api()
```

## Consommation d'APIs externes

### Client API générique

```python
import requests
import json
from typing import Optional, Dict, Any

class APIClient:
    """Client générique pour consommer des APIs REST"""

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

        # En-têtes par défaut
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Python API Client/1.0'
        })

        # Authentification si fournie
        if api_key:
            self.session.headers['Authorization'] = f'Bearer {api_key}'

    def _faire_requete(self, method: str, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """Méthode interne pour faire des requêtes"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(method, url, timeout=10, **kwargs)

            # Log de la requête
            print(f"🌐 {method} {url} - Statut: {response.status_code}")

            if response.status_code == 204:  # No Content
                return {'success': True}

            if response.headers.get('content-type', '').startswith('application/json'):
                return response.json()
            else:
                return {'content': response.text, 'status_code': response.status_code}

        except requests.exceptions.Timeout:
            print(f"❌ Timeout pour {method} {url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de requête: {e}")
            return None

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """Effectue une requête GET"""
        return self._faire_requete('GET', endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Optional[Dict]:
        """Effectue une requête POST"""
        return self._faire_requete('POST', endpoint, json=data)

    def put(self, endpoint: str, data: Optional[Dict] = None) -> Optional[Dict]:
        """Effectue une requête PUT"""
        return self._faire_requete('PUT', endpoint, json=data)

    def delete(self, endpoint: str) -> Optional[Dict]:
        """Effectue une requête DELETE"""
        return self._faire_requete('DELETE', endpoint)

# Exemple d'utilisation avec l'API JSONPlaceholder
def exemple_consommation_api():
    """Exemple de consommation d'une API externe"""

    print("📡 Consommation de l'API JSONPlaceholder")
    print("=" * 45)

    # Créer le client
    client = APIClient('https://jsonplaceholder.typicode.com')

    # 1. Récupérer quelques posts
    print("\n1. 📋 Récupération des posts")
    posts = client.get('/posts', params={'_limit': 5})

    if posts:
        print(f"   Récupéré {len(posts)} posts:")
        for post in posts:
            print(f"   - {post['id']}: {post['title'][:50]}...")

    # 2. Récupérer un post spécifique
    print("\n2. 🔍 Récupération du post #1")
    post = client.get('/posts/1')

    if post:
        print(f"   Titre: {post['title']}")
        print(f"   Contenu: {post['body'][:100]}...")

    # 3. Créer un nouveau post
    print("\n3. ➕ Création d'un nouveau post")
    nouveau_post = {
        'title': 'Mon nouveau post',
        'body': 'Ceci est le contenu de mon nouveau post créé via API.',
        'userId': 1
    }

    resultat = client.post('/posts', nouveau_post)

    if resultat:
        print(f"   ✅ Post créé avec l'ID: {resultat['id']}")

    # 4. Récupérer les utilisateurs
    print("\n4. 👥 Récupération des utilisateurs")
    utilisateurs = client.get('/users', params={'_limit': 3})

    if utilisateurs:
        print(f"   Récupéré {len(utilisateurs)} utilisateurs:")
        for user in utilisateurs:
            print(f"   - {user['name']} ({user['email']})")

if __name__ == '__main__':
    exemple_consommation_api()
```

## Exemple pratique : API de gestion de tâches

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Base de données simulée
taches = [
    {
        'id': str(uuid.uuid4()),
        'titre': 'Apprendre Flask',
        'description': 'Suivre le tutoriel sur les APIs REST',
        'terminee': False,
        'priorite': 'haute',
        'date_creation': datetime.now().isoformat(),
        'date_echeance': (datetime.now() + timedelta(days=7)).isoformat()
    },
    {
        'id': str(uuid.uuid4()),
        'titre': 'Faire les courses',
        'description': 'Acheter des légumes et du pain',
        'terminee': True,
        'priorite': 'moyenne',
        'date_creation': (datetime.now() - timedelta(days=1)).isoformat(),
        'date_echeance': datetime.now().isoformat()
    }
]

def valider_tache(donnees):
    """Valide les données d'une tâche"""
    erreurs = []

    if 'titre' in donnees:
        if not donnees['titre'] or len(donnees['titre'].strip()) < 3:
            erreurs.append('Le titre doit contenir au moins 3 caractères')

    if 'priorite' in donnees:
        if donnees['priorite'] not in ['basse', 'moyenne', 'haute']:
            erreurs.append('La priorité doit être: basse, moyenne ou haute')

    if 'date_echeance' in donnees:
        try:
            datetime.fromisoformat(donnees['date_echeance'])
        except ValueError:
            erreurs.append('Format de date invalide (utilisez ISO format: YYYY-MM-DD)')

    return erreurs

def trouver_tache(tache_id):
    """Trouve une tâche par son ID"""
    return next((t for t in taches if t['id'] == tache_id), None)

def formater_tache(tache):
    """Formate une tâche pour l'affichage"""
    tache_formatee = tache.copy()

    # Ajouter des champs calculés
    date_creation = datetime.fromisoformat(tache['date_creation'])
    tache_formatee['age_jours'] = (datetime.now() - date_creation).days

    if tache['date_echeance']:
        date_echeance = datetime.fromisoformat(tache['date_echeance'])
        jours_restants = (date_echeance - datetime.now()).days
        tache_formatee['jours_restants'] = jours_restants
        tache_formatee['en_retard'] = jours_restants < 0 and not tache['terminee']

    return tache_formatee

# === ROUTES DE L'API TÂCHES ===

@app.route('/api/taches', methods=['GET'])
def obtenir_taches():
    """Récupère les tâches avec filtres optionnels"""

    # Paramètres de filtrage
    terminee = request.args.get('terminee')
    priorite = request.args.get('priorite')
    en_retard = request.args.get('en_retard')

    # Filtrer les tâches
    taches_filtrees = taches.copy()

    if terminee is not None:
        terminee_bool = terminee.lower() == 'true'
        taches_filtrees = [t for t in taches_filtrees if t['terminee'] == terminee_bool]

    if priorite:
        taches_filtrees = [t for t in taches_filtrees if t['priorite'] == priorite]

    # Formater et ajouter des informations calculées
    taches_formatees = [formater_tache(t) for t in taches_filtrees]

    if en_retard is not None:
        en_retard_bool = en_retard.lower() == 'true'
        taches_formatees = [t for t in taches_formatees if t.get('en_retard', False) == en_retard_bool]

    # Statistiques
    total = len(taches)
    terminees = len([t for t in taches if t['terminee']])
    en_cours = total - terminees
    en_retard_count = len([t for t in taches_formatees if t.get('en_retard', False)])

    return jsonify({
        'success': True,
        'data': taches_formatees,
        'statistiques': {
            'total': total,
            'terminees': terminees,
            'en_cours': en_cours,
            'en_retard': en_retard_count
        }
    })

@app.route('/api/taches/<tache_id>', methods=['GET'])
def obtenir_tache(tache_id):
    """Récupère une tâche spécifique"""
    tache = trouver_tache(tache_id)

    if not tache:
        return jsonify({
            'success': False,
            'error': 'Tâche non trouvée'
        }), 404

    return jsonify({
        'success': True,
        'data': formater_tache(tache)
    })

@app.route('/api/taches', methods=['POST'])
def creer_tache():
    """Crée une nouvelle tâche"""
    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Aucune donnée fournie'
        }), 400

    # Validation
    erreurs = valider_tache(donnees)
    if 'titre' not in donnees:
        erreurs.append('Le titre est obligatoire')

    if erreurs:
        return jsonify({
            'success': False,
            'error': 'Données invalides',
            'details': erreurs
        }), 400

    # Créer la nouvelle tâche
    nouvelle_tache = {
        'id': str(uuid.uuid4()),
        'titre': donnees['titre'].strip(),
        'description': donnees.get('description', '').strip(),
        'terminee': False,
        'priorite': donnees.get('priorite', 'moyenne'),
        'date_creation': datetime.now().isoformat(),
        'date_echeance': donnees.get('date_echeance')
    }

    taches.append(nouvelle_tache)

    return jsonify({
        'success': True,
        'data': formater_tache(nouvelle_tache),
        'message': 'Tâche créée avec succès'
    }), 201

@app.route('/api/taches/<tache_id>', methods=['PUT'])
def modifier_tache(tache_id):
    """Modifie une tâche existante"""
    tache = trouver_tache(tache_id)

    if not tache:
        return jsonify({
            'success': False,
            'error': 'Tâche non trouvée'
        }), 404

    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Aucune donnée fournie'
        }), 400

    # Validation
    erreurs = valider_tache(donnees)
    if erreurs:
        return jsonify({
            'success': False,
            'error': 'Données invalides',
            'details': erreurs
        }), 400

    # Mettre à jour les champs
    champs_modifiables = ['titre', 'description', 'terminee', 'priorite', 'date_echeance']

    for champ in champs_modifiables:
        if champ in donnees:
            if champ in ['titre', 'description']:
                tache[champ] = donnees[champ].strip()
            else:
                tache[champ] = donnees[champ]

    return jsonify({
        'success': True,
        'data': formater_tache(tache),
        'message': 'Tâche modifiée avec succès'
    })

@app.route('/api/taches/<tache_id>', methods=['DELETE'])
def supprimer_tache(tache_id):
    """Supprime une tâche"""
    global taches

    index = next((i for i, t in enumerate(taches) if t['id'] == tache_id), None)

    if index is None:
        return jsonify({
            'success': False,
            'error': 'Tâche non trouvée'
        }), 404

    tache_supprimee = taches.pop(index)

    return jsonify({
        'success': True,
        'message': f'Tâche "{tache_supprimee["titre"]}" supprimée avec succès'
    })

@app.route('/api/taches/<tache_id>/terminer', methods=['PATCH'])
def terminer_tache(tache_id):
    """Marque une tâche comme terminée"""
    tache = trouver_tache(tache_id)

    if not tache:
        return jsonify({
            'success': False,
            'error': 'Tâche non trouvée'
        }), 404

    tache['terminee'] = True

    return jsonify({
        'success': True,
        'data': formater_tache(tache),
        'message': f'Tâche "{tache["titre"]}" marquée comme terminée'
    })

@app.route('/api/statistiques', methods=['GET'])
def obtenir_statistiques():
    """Retourne les statistiques globales"""

    total = len(taches)
    terminees = len([t for t in taches if t['terminee']])
    en_cours = total - terminees

    # Statistiques par priorité
    par_priorite = {}
    for priorite in ['basse', 'moyenne', 'haute']:
        par_priorite[priorite] = len([t for t in taches if t['priorite'] == priorite])

    # Tâches en retard
    taches_formatees = [formater_tache(t) for t in taches]
    en_retard = len([t for t in taches_formatees if t.get('en_retard', False)])

    # Tâches créées cette semaine
    il_y_a_une_semaine = datetime.now() - timedelta(days=7)
    cette_semaine = len([
        t for t in taches
        if datetime.fromisoformat(t['date_creation']) > il_y_a_une_semaine
    ])

    return jsonify({
        'success': True,
        'data': {
            'total': total,
            'terminees': terminees,
            'en_cours': en_cours,
            'en_retard': en_retard,
            'cette_semaine': cette_semaine,
            'par_priorite': par_priorite,
            'taux_completion': round((terminees / total * 100) if total > 0 else 0, 1)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## Client pour l'API de tâches

```python
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class GestionnaireTaches:
    """Client pour interagir avec l'API de gestion de tâches"""

    def __init__(self, base_url: str = 'http://localhost:5000'):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def _faire_requete(self, method: str, endpoint: str, **kwargs):
        """Méthode interne pour les requêtes"""
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(method, url, timeout=10, **kwargs)

            if response.status_code in [200, 201]:
                return response.json()
            elif response.status_code == 404:
                print(f"❌ Ressource non trouvée: {endpoint}")
                return None
            else:
                error_data = response.json() if response.headers.get('content-type', '').startswith('application/json') else {}
                print(f"❌ Erreur {response.status_code}: {error_data.get('error', 'Erreur inconnue')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion: {e}")
            return None

    def lister_taches(self, terminee: Optional[bool] = None,
                     priorite: Optional[str] = None,
                     en_retard: Optional[bool] = None) -> List[Dict]:
        """Liste les tâches avec filtres optionnels"""

        params = {}
        if terminee is not None:
            params['terminee'] = str(terminee).lower()
        if priorite:
            params['priorite'] = priorite
        if en_retard is not None:
            params['en_retard'] = str(en_retard).lower()

        response = self._faire_requete('GET', '/api/taches', params=params)
        return response['data'] if response else []

    def obtenir_tache(self, tache_id: str) -> Optional[Dict]:
        """Récupère une tâche spécifique"""
        response = self._faire_requete('GET', f'/api/taches/{tache_id}')
        return response['data'] if response else None

    def creer_tache(self, titre: str, description: str = '',
                   priorite: str = 'moyenne',
                   date_echeance: Optional[str] = None) -> Optional[Dict]:
        """Crée une nouvelle tâche"""

        donnees = {
            'titre': titre,
            'description': description,
            'priorite': priorite
        }

        if date_echeance:
            donnees['date_echeance'] = date_echeance

        response = self._faire_requete('POST', '/api/taches', json=donnees)
        return response['data'] if response else None

    def modifier_tache(self, tache_id: str, **modifications) -> Optional[Dict]:
        """Modifie une tâche existante"""
        response = self._faire_requete('PUT', f'/api/taches/{tache_id}', json=modifications)
        return response['data'] if response else None

    def supprimer_tache(self, tache_id: str) -> bool:
        """Supprime une tâche"""
        response = self._faire_requete('DELETE', f'/api/taches/{tache_id}')
        return response is not None

    def terminer_tache(self, tache_id: str) -> Optional[Dict]:
        """Marque une tâche comme terminée"""
        response = self._faire_requete('PATCH', f'/api/taches/{tache_id}/terminer')
        return response['data'] if response else None

    def obtenir_statistiques(self) -> Optional[Dict]:
        """Récupère les statistiques"""
        response = self._faire_requete('GET', '/api/statistiques')
        return response['data'] if response else None

    def afficher_taches(self, taches: List[Dict]):
        """Affiche les tâches de manière formatée"""
        if not taches:
            print("📝 Aucune tâche trouvée")
            return

        print(f"\n📝 {len(taches)} tâche(s) trouvée(s)")
        print("-" * 60)

        for tache in taches:
            # Icônes selon l'état
            if tache['terminee']:
                icone = "✅"
            elif tache.get('en_retard', False):
                icone = "🔴"
            else:
                icone = "⭕"

            # Couleur de priorité
            priorite_icons = {'basse': '🟢', 'moyenne': '🟡', 'haute': '🔴'}
            priorite_icone = priorite_icons.get(tache['priorite'], '⚪')

            print(f"{icone} {tache['titre']}")
            print(f"   {priorite_icone} Priorité: {tache['priorite']}")

            if tache['description']:
                print(f"   📄 {tache['description']}")

            if tache.get('jours_restants') is not None:
                jours = tache['jours_restants']
                if jours < 0:
                    print(f"   ⏰ En retard de {abs(jours)} jour(s)")
                elif jours == 0:
                    print(f"   ⏰ Échéance aujourd'hui")
                else:
                    print(f"   ⏰ Dans {jours} jour(s)")

            print(f"   🆔 ID: {tache['id'][:8]}...")
            print()

def exemple_utilisation():
    """Exemple d'utilisation du client API"""

    print("🎯 Gestionnaire de tâches - Client API")
    print("=" * 50)

    # Créer le client
    client = GestionnaireTaches()

    # 1. Afficher les statistiques actuelles
    print("\n📊 Statistiques actuelles")
    stats = client.obtenir_statistiques()
    if stats:
        print(f"   Total: {stats['total']} tâches")
        print(f"   Terminées: {stats['terminees']} ({stats['taux_completion']}%)")
        print(f"   En cours: {stats['en_cours']}")
        print(f"   En retard: {stats['en_retard']}")

    # 2. Créer quelques tâches d'exemple
    print("\n➕ Création de nouvelles tâches")

    taches_exemple = [
        {
            'titre': 'Réviser Python',
            'description': 'Revoir les concepts des APIs REST',
            'priorite': 'haute',
            'date_echeance': (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        },
        {
            'titre': 'Faire du sport',
            'description': 'Séance de course à pied',
            'priorite': 'moyenne',
            'date_echeance': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        },
        {
            'titre': 'Appeler grand-mère',
            'description': 'Prendre des nouvelles',
            'priorite': 'basse'
        }
    ]

    taches_creees = []
    for tache_data in taches_exemple:
        tache = client.creer_tache(**tache_data)
        if tache:
            print(f"   ✅ Créé: {tache['titre']}")
            taches_creees.append(tache)

    # 3. Afficher toutes les tâches
    print("\n📋 Toutes les tâches")
    toutes_taches = client.lister_taches()
    client.afficher_taches(toutes_taches)

    # 4. Filtrer par priorité haute
    print("\n🔴 Tâches priorité haute")
    taches_haute_priorite = client.lister_taches(priorite='haute')
    client.afficher_taches(taches_haute_priorite)

    # 5. Terminer une tâche
    if taches_creees:
        tache_a_terminer = taches_creees[0]
        print(f"\n✅ Terminer la tâche: {tache_a_terminer['titre']}")
        tache_terminee = client.terminer_tache(tache_a_terminer['id'])
        if tache_terminee:
            print(f"   ✅ Tâche terminée!")

    # 6. Modifier une tâche
    if len(taches_creees) > 1:
        tache_a_modifier = taches_creees[1]
        print(f"\n✏️ Modification de: {tache_a_modifier['titre']}")
        tache_modifiee = client.modifier_tache(
            tache_a_modifier['id'],
            priorite='haute',
            description='Description mise à jour'
        )
        if tache_modifiee:
            print(f"   ✅ Tâche modifiée!")

    # 7. Afficher les statistiques finales
    print("\n📊 Statistiques finales")
    stats_finales = client.obtenir_statistiques()
    if stats_finales:
        print(f"   Total: {stats_finales['total']} tâches")
        print(f"   Terminées: {stats_finales['terminees']} ({stats_finales['taux_completion']}%)")
        print(f"   En cours: {stats_finales['en_cours']}")

if __name__ == '__main__':
    exemple_utilisation()
```

## Documentation d'API avec Swagger/OpenAPI

### Ajout de la documentation automatique

```python
from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)

# Configuration Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/api/utilisateurs', methods=['GET'])
@swag_from({
    'tags': ['Utilisateurs'],
    'summary': 'Liste tous les utilisateurs',
    'description': 'Récupère la liste complète des utilisateurs avec pagination optionnelle',
    'parameters': [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'default': 1,
            'description': 'Numéro de page'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'default': 10,
            'description': 'Nombre d\'éléments par page'
        }
    ],
    'responses': {
        200: {
            'description': 'Liste des utilisateurs récupérée avec succès',
            'schema': {
                'type': 'object',
                'properties': {
                    'success': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'nom': {'type': 'string'},
                                'prenom': {'type': 'string'},
                                'email': {'type': 'string'},
                                'date_creation': {'type': 'string', 'format': 'date'}
                            }
                        }
                    }
                }
            }
        }
    }
})
def obtenir_utilisateurs():
    # Implementation ici
    pass

@app.route('/api/utilisateurs', methods=['POST'])
@swag_from({
    'tags': ['Utilisateurs'],
    'summary': 'Crée un nouvel utilisateur',
    'parameters': [
        {
            'name': 'utilisateur',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['nom', 'prenom', 'email'],
                'properties': {
                    'nom': {'type': 'string', 'example': 'Dupont'},
                    'prenom': {'type': 'string', 'example': 'Jean'},
                    'email': {'type': 'string', 'format': 'email', 'example': 'jean.dupont@email.com'},
                    'age': {'type': 'integer', 'minimum': 0, 'maximum': 120}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Utilisateur créé avec succès'
        },
        400: {
            'description': 'Données invalides'
        }
    }
})
def creer_utilisateur():
    # Implementation ici
    pass
```

## Exercices pratiques

### Exercice 1 : API de bibliothèque

Créez une API REST pour gérer une bibliothèque avec :
- **Livres** : titre, auteur, ISBN, année, disponible
- **Emprunts** : qui a emprunté quoi et quand

**Endpoints requis :**
- `GET /api/livres` - Liste des livres
- `POST /api/livres` - Ajouter un livre
- `GET /api/livres/<isbn>` - Détails d'un livre
- `POST /api/emprunts` - Emprunter un livre
- `DELETE /api/emprunts/<id>` - Retourner un livre

### Exercice 2 : API météo personnalisée

Créez une API qui :
1. Récupère les données d'une API météo externe
2. Les stocke en cache pendant 10 minutes
3. Ajoute des informations personnalisées (conseils vestimentaires)
4. Propose des endpoints pour différentes villes

### Exercice 3 : API de blog simple

Créez une API de blog avec :
- **Articles** : titre, contenu, auteur, date
- **Commentaires** : contenu, auteur, article associé
- Système de pagination
- Recherche dans les articles

## Solutions des exercices

### Solution Exercice 1 : API de bibliothèque

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Base de données simulée
livres = [
    {
        'isbn': '978-2-1234-5678-9',
        'titre': 'Apprendre Python',
        'auteur': 'Jean Martin',
        'annee': 2023,
        'disponible': True
    },
    {
        'isbn': '978-2-9876-5432-1',
        'titre': 'Flask pour débutants',
        'auteur': 'Marie Dubois',
        'annee': 2024,
        'disponible': False
    }
]

emprunts = [
    {
        'id': str(uuid.uuid4()),
        'isbn': '978-2-9876-5432-1',
        'emprunteur': 'Pierre Durand',
        'date_emprunt': '2024-01-15',
        'date_retour_prevue': '2024-02-15'
    }
]

@app.route('/api/livres', methods=['GET'])
def obtenir_livres():
    """Liste tous les livres"""
    disponible = request.args.get('disponible')

    livres_filtres = livres
    if disponible is not None:
        disponible_bool = disponible.lower() == 'true'
        livres_filtres = [l for l in livres if l['disponible'] == disponible_bool]

    return jsonify({
        'success': True,
        'data': livres_filtres,
        'count': len(livres_filtres)
    })

@app.route('/api/livres', methods=['POST'])
def ajouter_livre():
    """Ajoute un nouveau livre"""
    donnees = request.get_json()

    if not donnees:
        return jsonify({'success': False, 'error': 'Données manquantes'}), 400

    # Validation
    champs_requis = ['isbn', 'titre', 'auteur', 'annee']
    for champ in champs_requis:
        if champ not in donnees:
            return jsonify({'success': False, 'error': f'{champ} requis'}), 400

    # Vérifier que l'ISBN n'existe pas déjà
    if any(l['isbn'] == donnees['isbn'] for l in livres):
        return jsonify({'success': False, 'error': 'ISBN déjà existant'}), 400

    nouveau_livre = {
        'isbn': donnees['isbn'],
        'titre': donnees['titre'],
        'auteur': donnees['auteur'],
        'annee': donnees['annee'],
        'disponible': True
    }

    livres.append(nouveau_livre)

    return jsonify({
        'success': True,
        'data': nouveau_livre,
        'message': 'Livre ajouté avec succès'
    }), 201

@app.route('/api/livres/<isbn>', methods=['GET'])
def obtenir_livre(isbn):
    """Récupère les détails d'un livre"""
    livre = next((l for l in livres if l['isbn'] == isbn), None)

    if not livre:
        return jsonify({'success': False, 'error': 'Livre non trouvé'}), 404

    # Ajouter les informations d'emprunt si le livre est emprunté
    emprunt_actuel = next((e for e in emprunts if e['isbn'] == isbn), None)

    livre_details = livre.copy()
    if emprunt_actuel:
        livre_details['emprunt'] = emprunt_actuel

    return jsonify({
        'success': True,
        'data': livre_details
    })

@app.route('/api/emprunts', methods=['POST'])
def emprunter_livre():
    """Emprunte un livre"""
    donnees = request.get_json()

    if not donnees or 'isbn' not in donnees or 'emprunteur' not in donnees:
        return jsonify({'success': False, 'error': 'ISBN et emprunteur requis'}), 400

    # Vérifier que le livre existe et est disponible
    livre = next((l for l in livres if l['isbn'] == donnees['isbn']), None)

    if not livre:
        return jsonify({'success': False, 'error': 'Livre non trouvé'}), 404

    if not livre['disponible']:
        return jsonify({'success': False, 'error': 'Livre non disponible'}), 400

    # Créer l'emprunt
    nouvel_emprunt = {
        'id': str(uuid.uuid4()),
        'isbn': donnees['isbn'],
        'emprunteur': donnees['emprunteur'],
        'date_emprunt': datetime.now().strftime('%Y-%m-%d'),
        'date_retour_prevue': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    }

    emprunts.append(nouvel_emprunt)
    livre['disponible'] = False

    return jsonify({
        'success': True,
        'data': nouvel_emprunt,
        'message': f'Livre "{livre["titre"]}" emprunté avec succès'
    }), 201

@app.route('/api/emprunts/<emprunt_id>', methods=['DELETE'])
def retourner_livre(emprunt_id):
    """Retourne un livre emprunté"""
    global emprunts

    # Trouver l'emprunt
    emprunt = next((e for e in emprunts if e['id'] == emprunt_id), None)

    if not emprunt:
        return jsonify({'success': False, 'error': 'Emprunt non trouvé'}), 404

    # Trouver le livre correspondant
    livre = next((l for l in livres if l['isbn'] == emprunt['isbn']), None)

    if livre:
        livre['disponible'] = True

    # Supprimer l'emprunt
    emprunts = [e for e in emprunts if e['id'] != emprunt_id]

    return jsonify({
        'success': True,
        'message': f'Livre retourné avec succès',
        'data': {
            'livre': livre['titre'] if livre else 'Livre inconnu',
            'emprunteur': emprunt['emprunteur'],
            'date_retour': datetime.now().strftime('%Y-%m-%d')
        }
    })

@app.route('/api/emprunts', methods=['GET'])
def obtenir_emprunts():
    """Liste tous les emprunts en cours"""
    emprunts_enrichis = []

    for emprunt in emprunts:
        livre = next((l for l in livres if l['isbn'] == emprunt['isbn']), None)

        emprunt_enrichi = emprunt.copy()
        if livre:
            emprunt_enrichi['livre'] = {
                'titre': livre['titre'],
                'auteur': livre['auteur']
            }

        # Calculer si en retard
        date_retour_prevue = datetime.strptime(emprunt['date_retour_prevue'], '%Y-%m-%d')
        emprunt_enrichi['en_retard'] = datetime.now() > date_retour_prevue
        emprunt_enrichi['jours_retard'] = max(0, (datetime.now() - date_retour_prevue).days)

        emprunts_enrichis.append(emprunt_enrichi)

    return jsonify({
        'success': True,
        'data': emprunts_enrichis,
        'count': len(emprunts_enrichis)
    })

@app.route('/api/statistiques', methods=['GET'])
def statistiques_bibliotheque():
    """Statistiques de la bibliothèque"""
    total_livres = len(livres)
    livres_disponibles = len([l for l in livres if l['disponible']])
    emprunts_actifs = len(emprunts)

    # Emprunts en retard
    emprunts_retard = 0
    for emprunt in emprunts:
        date_retour_prevue = datetime.strptime(emprunt['date_retour_prevue'], '%Y-%m-%d')
        if datetime.now() > date_retour_prevue:
            emprunts_retard += 1

    return jsonify({
        'success': True,
        'data': {
            'total_livres': total_livres,
            'livres_disponibles': livres_disponibles,
            'livres_empruntes': total_livres - livres_disponibles,
            'emprunts_actifs': emprunts_actifs,
            'emprunts_en_retard': emprunts_retard,
            'taux_disponibilite': round((livres_disponibles / total_livres * 100) if total_livres > 0 else 0, 1)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Client pour tester l'API bibliothèque

```python
import requests
from datetime import datetime

class BibliothequeClient:
    """Client pour interagir avec l'API de bibliothèque"""

    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def lister_livres(self, disponible=None):
        """Liste les livres"""
        params = {}
        if disponible is not None:
            params['disponible'] = str(disponible).lower()

        response = self.session.get(f'{self.base_url}/api/livres', params=params)
        return response.json() if response.status_code == 200 else None

    def ajouter_livre(self, isbn, titre, auteur, annee):
        """Ajoute un nouveau livre"""
        data = {
            'isbn': isbn,
            'titre': titre,
            'auteur': auteur,
            'annee': annee
        }

        response = self.session.post(f'{self.base_url}/api/livres', json=data)
        return response.json() if response.status_code == 201 else None

    def obtenir_livre(self, isbn):
        """Récupère les détails d'un livre"""
        response = self.session.get(f'{self.base_url}/api/livres/{isbn}')
        return response.json() if response.status_code == 200 else None

    def emprunter_livre(self, isbn, emprunteur):
        """Emprunte un livre"""
        data = {
            'isbn': isbn,
            'emprunteur': emprunteur
        }

        response = self.session.post(f'{self.base_url}/api/emprunts', json=data)
        return response.json() if response.status_code == 201 else None

    def retourner_livre(self, emprunt_id):
        """Retourne un livre"""
        response = self.session.delete(f'{self.base_url}/api/emprunts/{emprunt_id}')
        return response.json() if response.status_code == 200 else None

    def lister_emprunts(self):
        """Liste les emprunts en cours"""
        response = self.session.get(f'{self.base_url}/api/emprunts')
        return response.json() if response.status_code == 200 else None

    def obtenir_statistiques(self):
        """Récupère les statistiques"""
        response = self.session.get(f'{self.base_url}/api/statistiques')
        return response.json() if response.status_code == 200 else None

def demo_bibliotheque():
    """Démonstration de l'API bibliothèque"""

    print("📚 Démonstration API Bibliothèque")
    print("=" * 40)

    client = BibliothequeClient()

    # 1. Afficher les statistiques initiales
    print("\n📊 Statistiques initiales")
    stats = client.obtenir_statistiques()
    if stats and stats['success']:
        data = stats['data']
        print(f"   Total livres: {data['total_livres']}")
        print(f"   Disponibles: {data['livres_disponibles']}")
        print(f"   Empruntés: {data['livres_empruntes']}")

    # 2. Ajouter un nouveau livre
    print("\n➕ Ajout d'un nouveau livre")
    nouveau_livre = client.ajouter_livre(
        isbn='978-2-1111-2222-3',
        titre='Maîtriser les APIs REST',
        auteur='Sophie Programmer',
        annee=2024
    )
    if nouveau_livre and nouveau_livre['success']:
        print(f"   ✅ Livre ajouté: {nouveau_livre['data']['titre']}")

    # 3. Lister tous les livres
    print("\n📋 Liste des livres")
    livres = client.lister_livres()
    if livres and livres['success']:
        for livre in livres['data']:
            statut = "📗" if livre['disponible'] else "📕"
            print(f"   {statut} {livre['titre']} - {livre['auteur']} ({livre['annee']})")

    # 4. Emprunter un livre
    print("\n📖 Emprunt d'un livre")
    if livres and livres['success']:
        livre_disponible = next((l for l in livres['data'] if l['disponible']), None)
        if livre_disponible:
            emprunt = client.emprunter_livre(livre_disponible['isbn'], 'Alice Martin')
            if emprunt and emprunt['success']:
                print(f"   ✅ {emprunt['message']}")
                emprunt_id = emprunt['data']['id']

    # 5. Lister les emprunts
    print("\n📝 Emprunts en cours")
    emprunts = client.lister_emprunts()
    if emprunts and emprunts['success']:
        for emprunt in emprunts['data']:
            retard_info = f" (⏰ {emprunt['jours_retard']} jours de retard)" if emprunt['en_retard'] else ""
            livre_info = emprunt.get('livre', {})
            print(f"   📖 {livre_info.get('titre', 'Titre inconnu')} - {emprunt['emprunteur']}{retard_info}")

    # 6. Statistiques finales
    print("\n📊 Statistiques finales")
    stats_finales = client.obtenir_statistiques()
    if stats_finales and stats_finales['success']:
        data = stats_finales['data']
        print(f"   Total livres: {data['total_livres']}")
        print(f"   Taux de disponibilité: {data['taux_disponibilite']}%")
        print(f"   Emprunts actifs: {data['emprunts_actifs']}")

if __name__ == '__main__':
    demo_bibliotheque()
```

## Solution Exercice 2 : API météo personnalisée

```python
from flask import Flask, jsonify, request
import requests
from datetime import datetime, timedelta
import time

app = Flask(__name__)

# Cache pour stocker les données météo
cache_meteo = {}
DUREE_CACHE = 600  # 10 minutes en secondes

# Clé API (à remplacer par votre vraie clé)
WEATHER_API_KEY = "your_api_key_here"

def obtenir_donnees_meteo_externe(ville):
    """Récupère les données météo depuis une API externe"""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': ville,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

def generer_conseils_vestimentaires(temperature, description):
    """Génère des conseils vestimentaires basés sur la météo"""
    conseils = []

    if temperature < 0:
        conseils.append("🧥 Portez un manteau d'hiver")
        conseils.append("🧤 N'oubliez pas gants et bonnet")
    elif temperature < 10:
        conseils.append("🧥 Une veste chaude est recommandée")
        conseils.append("🧣 Pensez à une écharpe")
    elif temperature < 20:
        conseils.append("👕 Un pull ou une veste légère")
    else:
        conseils.append("👕 Vêtements légers recommandés")

    if 'rain' in description.lower() or 'pluie' in description.lower():
        conseils.append("☔ Prenez un parapluie")
        conseils.append("👢 Chaussures imperméables conseillées")

    if 'snow' in description.lower() or 'neige' in description.lower():
        conseils.append("❄️ Chaussures antidérapantes")
        conseils.append("🧥 Protégez-vous bien du froid")

    return conseils

def meteo_depuis_cache(ville):
    """Récupère les données météo depuis le cache si disponibles"""
    ville_key = ville.lower()
    maintenant = time.time()

    if ville_key in cache_meteo:
        donnees_cache, timestamp = cache_meteo[ville_key]
        if maintenant - timestamp < DUREE_CACHE:
            print(f"📦 Données récupérées depuis le cache pour {ville}")
            return donnees_cache

    # Cache expiré ou inexistant, récupérer depuis l'API
    print(f"🌐 Récupération depuis l'API externe pour {ville}")
    donnees_api = obtenir_donnees_meteo_externe(ville)

    if donnees_api:
        # Sauvegarder en cache
        cache_meteo[ville_key] = (donnees_api, maintenant)
        return donnees_api

    return None

@app.route('/api/meteo/<ville>', methods=['GET'])
def obtenir_meteo(ville):
    """Récupère la météo pour une ville avec conseils personnalisés"""

    donnees_brutes = meteo_depuis_cache(ville)

    if not donnees_brutes:
        return jsonify({
            'success': False,
            'error': f'Impossible de récupérer la météo pour {ville}'
        }), 404

    # Extraire les informations importantes
    temperature = donnees_brutes['main']['temp']
    description = donnees_brutes['weather'][0]['description']
    humidite = donnees_brutes['main']['humidity']
    pression = donnees_brutes['main']['pressure']
    vent = donnees_brutes.get('wind', {}).get('speed', 0)

    # Générer les conseils personnalisés
    conseils = generer_conseils_vestimentaires(temperature, description)

    # Déterminer l'activité recommandée
    if temperature > 20 and 'clear' in donnees_brutes['weather'][0]['main'].lower():
        activite = "🌞 Parfait pour une activité en extérieur"
    elif temperature < 0:
        activite = "🏠 Restez au chaud à l'intérieur"
    elif 'rain' in description.lower():
        activite = "☔ Activités en intérieur recommandées"
    else:
        activite = "👍 Conditions correctes pour sortir"

    meteo_personnalisee = {
        'ville': donnees_brutes['name'],
        'pays': donnees_brutes['sys']['country'],
        'temperature': round(temperature, 1),
        'temperature_ressentie': round(donnees_brutes['main']['feels_like'], 1),
        'description': description.capitalize(),
        'humidite': humidite,
        'pression': pression,
        'vent_vitesse': round(vent * 3.6, 1),  # Conversion m/s vers km/h
        'conseils_vestimentaires': conseils,
        'activite_recommandee': activite,
        'heure_mise_a_jour': datetime.now().strftime('%H:%M:%S'),
        'donnees_depuis_cache': ville.lower() in cache_meteo
    }

    return jsonify({
        'success': True,
        'data': meteo_personnalisee
    })

@app.route('/api/meteo/comparaison', methods=['POST'])
def comparer_meteo():
    """Compare la météo entre plusieurs villes"""
    donnees = request.get_json()

    if not donnees or 'villes' not in donnees:
        return jsonify({
            'success': False,
            'error': 'Liste de villes requise'
        }), 400

    villes = donnees['villes']

    if len(villes) < 2:
        return jsonify({
            'success': False,
            'error': 'Au moins 2 villes requises pour comparaison'
        }), 400

    comparaison = []

    for ville in villes:
        donnees_brutes = meteo_depuis_cache(ville)

        if donnees_brutes:
            comparaison.append({
                'ville': donnees_brutes['name'],
                'temperature': round(donnees_brutes['main']['temp'], 1),
                'description': donnees_brutes['weather'][0]['description'],
                'humidite': donnees_brutes['main']['humidity']
            })

    if not comparaison:
        return jsonify({
            'success': False,
            'error': 'Aucune donnée météo récupérée'
        }), 404

    # Trouver la ville la plus chaude/froide
    ville_plus_chaude = max(comparaison, key=lambda x: x['temperature'])
    ville_plus_froide = min(comparaison, key=lambda x: x['temperature'])

    return jsonify({
        'success': True,
        'data': {
            'villes': comparaison,
            'statistiques': {
                'plus_chaude': ville_plus_chaude,
                'plus_froide': ville_plus_froide,
                'ecart_temperature': round(ville_plus_chaude['temperature'] - ville_plus_froide['temperature'], 1)
            }
        }
    })

@app.route('/api/meteo/cache/status', methods=['GET'])
def status_cache():
    """Affiche le statut du cache"""
    maintenant = time.time()
    cache_info = []

    for ville, (donnees, timestamp) in cache_meteo.items():
        age_secondes = maintenant - timestamp
        expire_dans = max(0, DUREE_CACHE - age_secondes)

        cache_info.append({
            'ville': ville,
            'age_secondes': round(age_secondes),
            'expire_dans_secondes': round(expire_dans),
            'valide': expire_dans > 0
        })

    return jsonify({
        'success': True,
        'data': {
            'cache_entries': len(cache_meteo),
            'duree_cache_secondes': DUREE_CACHE,
            'details': cache_info
        }
    })

@app.route('/api/meteo/cache/clear', methods=['DELETE'])
def vider_cache():
    """Vide le cache météo"""
    global cache_meteo
    ancien_count = len(cache_meteo)
    cache_meteo.clear()

    return jsonify({
        'success': True,
        'message': f'Cache vidé ({ancien_count} entrées supprimées)'
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## Solution Exercice 3 : API de blog simple

```python
from flask import Flask, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# Base de données simulée
articles = [
    {
        'id': str(uuid.uuid4()),
        'titre': 'Introduction aux APIs REST',
        'contenu': 'Les APIs REST sont essentielles pour le développement web moderne...',
        'auteur': 'Jean Développeur',
        'date_creation': '2024-01-15T10:30:00',
        'date_modification': '2024-01-15T10:30:00',
        'tags': ['api', 'rest', 'web'],
        'publie': True
    },
    {
        'id': str(uuid.uuid4()),
        'titre': 'Flask pour débutants',
        'contenu': 'Flask est un micro-framework Python parfait pour commencer...',
        'auteur': 'Marie Codeuse',
        'date_creation': '2024-01-20T14:15:00',
        'date_modification': '2024-01-20T14:15:00',
        'tags': ['flask', 'python', 'tutorial'],
        'publie': True
    }
]

commentaires = [
    {
        'id': str(uuid.uuid4()),
        'article_id': articles[0]['id'],
        'auteur': 'Pierre Lecteur',
        'contenu': 'Excellent article, très clair !',
        'date_creation': '2024-01-16T09:00:00'
    }
]

def valider_article(donnees):
    """Valide les données d'un article"""
    erreurs = []

    if 'titre' in donnees:
        if not donnees['titre'] or len(donnees['titre'].strip()) < 5:
            erreurs.append('Le titre doit contenir au moins 5 caractères')

    if 'contenu' in donnees:
        if not donnees['contenu'] or len(donnees['contenu'].strip()) < 20:
            erreurs.append('Le contenu doit contenir au moins 20 caractères')

    if 'auteur' in donnees:
        if not donnees['auteur'] or len(donnees['auteur'].strip()) < 2:
            erreurs.append('Le nom d\'auteur doit contenir au moins 2 caractères')

    return erreurs

def rechercher_articles(terme):
    """Recherche dans les articles"""
    terme = terme.lower()
    resultats = []

    for article in articles:
        if not article['publie']:
            continue

        # Rechercher dans le titre, contenu et tags
        if (terme in article['titre'].lower() or
            terme in article['contenu'].lower() or
            any(terme in tag.lower() for tag in article.get('tags', []))):
            resultats.append(article)

    return resultats

def paginer_resultats(resultats, page, limite):
    """Applique la pagination aux résultats"""
    debut = (page - 1) * limite
    fin = debut + limite

    return {
        'resultats': resultats[debut:fin],
        'pagination': {
            'page_courante': page,
            'par_page': limite,
            'total': len(resultats),
            'total_pages': (len(resultats) + limite - 1) // limite,
            'a_suivante': fin < len(resultats),
            'a_precedente': page > 1
        }
    }

@app.route('/api/articles', methods=['GET'])
def obtenir_articles():
    """Liste les articles avec recherche et pagination"""

    # Paramètres de requête
    page = request.args.get('page', 1, type=int)
    limite = request.args.get('limit', 10, type=int)
    recherche = request.args.get('search', '', type=str)
    tag = request.args.get('tag', '', type=str)
    auteur = request.args.get('auteur', '', type=str)

    # Filtrer les articles publiés
    articles_publies = [a for a in articles if a['publie']]

    # Appliquer les filtres
    if recherche:
        articles_publies = rechercher_articles(recherche)

    if tag:
        articles_publies = [a for a in articles_publies
                          if tag.lower() in [t.lower() for t in a.get('tags', [])]]

    if auteur:
        articles_publies = [a for a in articles_publies
                          if auteur.lower() in a['auteur'].lower()]

    # Trier par date (plus récent en premier)
    articles_publies.sort(key=lambda x: x['date_creation'], reverse=True)

    # Appliquer la pagination
    resultats_pagines = paginer_resultats(articles_publies, page, limite)

    # Ajouter le nombre de commentaires à chaque article
    for article in resultats_pagines['resultats']:
        nb_commentaires = len([c for c in commentaires if c['article_id'] == article['id']])
        article['nb_commentaires'] = nb_commentaires

    return jsonify({
        'success': True,
        'data': resultats_pagines['resultats'],
        'pagination': resultats_pagines['pagination']
    })

@app.route('/api/articles/<article_id>', methods=['GET'])
def obtenir_article(article_id):
    """Récupère un article spécifique avec ses commentaires"""
    article = next((a for a in articles if a['id'] == article_id), None)

    if not article or not article['publie']:
        return jsonify({
            'success': False,
            'error': 'Article non trouvé'
        }), 404

    # Récupérer les commentaires de l'article
    commentaires_article = [c for c in commentaires if c['article_id'] == article_id]
    commentaires_article.sort(key=lambda x: x['date_creation'])

    article_avec_commentaires = article.copy()
    article_avec_commentaires['commentaires'] = commentaires_article

    return jsonify({
        'success': True,
        'data': article_avec_commentaires
    })

@app.route('/api/articles', methods=['POST'])
def creer_article():
    """Crée un nouvel article"""
    donnees = request.get_json()

    if not donnees:
        return jsonify({
            'success': False,
            'error': 'Données manquantes'
        }), 400

    # Validation
    erreurs = valider_article(donnees)
    champs_requis = ['titre', 'contenu', 'auteur']

    for champ in champs_requis:
        if champ not in donnees:
            erreurs.append(f'{champ} requis')

    if erreurs:
        return jsonify({
            'success': False,
            'error': 'Données invalides',
            'details': erreurs
        }), 400

    # Créer l'article
    nouvel_article = {
        'id': str(uuid.uuid4()),
        'titre': donnees['titre'].strip(),
        'contenu': donnees['contenu'].strip(),
        'auteur': donnees['auteur'].strip(),
        'date_creation': datetime.now().isoformat(),
        'date_modification': datetime.now().isoformat(),
        'tags': donnees.get('tags', []),
        'publie': donnees.get('publie', True)
    }

    articles.append(nouvel_article)

    return jsonify({
        'success': True,
        'data': nouvel_article,
        'message': 'Article créé avec succès'
    }), 201

@app.route('/api/articles/<article_id>/commentaires', methods=['POST'])
def ajouter_commentaire(article_id):
    """Ajoute un commentaire à un article"""

    # Vérifier que l'article existe
    article = next((a for a in articles if a['id'] == article_id), None)

    if not article or not article['publie']:
        return jsonify({
            'success': False,
            'error': 'Article non trouvé'
        }), 404

    donnees = request.get_json()

    if not donnees or 'contenu' not in donnees or 'auteur' not in donnees:
        return jsonify({
            'success': False,
            'error': 'Contenu et auteur requis'
        }), 400

    # Validation
    if len(donnees['contenu'].strip()) < 5:
        return jsonify({
            'success': False,
            'error': 'Le commentaire doit contenir au moins 5 caractères'
        }), 400

    # Créer le commentaire
    nouveau_commentaire = {
        'id': str(uuid.uuid4()),
        'article_id': article_id,
        'auteur': donnees['auteur'].strip(),
        'contenu': donnees['contenu'].strip(),
        'date_creation': datetime.now().isoformat()
    }

    commentaires.append(nouveau_commentaire)

    return jsonify({
        'success': True,
        'data': nouveau_commentaire,
        'message': 'Commentaire ajouté avec succès'
    }), 201

@app.route('/api/tags', methods=['GET'])
def obtenir_tags():
    """Récupère tous les tags utilisés"""
    tous_tags = []

    for article in articles:
        if article['publie']:
            tous_tags.extend(article.get('tags', []))

    # Compter les occurrences de chaque tag
    compteur_tags = {}
    for tag in tous_tags:
        compteur_tags[tag] = compteur_tags.get(tag, 0) + 1

    # Trier par popularité
    tags_populaires = sorted(compteur_tags.items(), key=lambda x: x[1], reverse=True)

    return jsonify({
        'success': True,
        'data': {
            'tags': [{'nom': tag, 'count': count} for tag, count in tags_populaires],
            'total_tags_uniques': len(compteur_tags)
        }
    })

@app.route('/api/auteurs', methods=['GET'])
def obtenir_auteurs():
    """Récupère tous les auteurs avec leurs statistiques"""
    compteur_auteurs = {}

    for article in articles:
        if article['publie']:
            auteur = article['auteur']
            if auteur not in compteur_auteurs:
                compteur_auteurs[auteur] = {
                    'nom': auteur,
                    'nb_articles': 0,
                    'premier_article': article['date_creation'],
                    'dernier_article': article['date_creation']
                }

            compteur_auteurs[auteur]['nb_articles'] += 1

            # Mettre à jour les dates
            if article['date_creation'] < compteur_auteurs[auteur]['premier_article']:
                compteur_auteurs[auteur]['premier_article'] = article['date_creation']
            if article['date_creation'] > compteur_auteurs[auteur]['dernier_article']:
                compteur_auteurs[auteur]['dernier_article'] = article['date_creation']

    # Trier par nombre d'articles
    auteurs_tries = sorted(compteur_auteurs.values(),
                          key=lambda x: x['nb_articles'], reverse=True)

    return jsonify({
        'success': True,
        'data': auteurs_tries
    })

@app.route('/api/statistiques/blog', methods=['GET'])
def statistiques_blog():
    """Statistiques générales du blog"""

    articles_publies = [a for a in articles if a['publie']]

    # Articles par mois
    articles_par_mois = {}
    for article in articles_publies:
        mois = article['date_creation'][:7]  # YYYY-MM
        articles_par_mois[mois] = articles_par_mois.get(mois, 0) + 1

    # Top tags
    tous_tags = []
    for article in articles_publies:
        tous_tags.extend(article.get('tags', []))

    compteur_tags = {}
    for tag in tous_tags:
        compteur_tags[tag] = compteur_tags.get(tag, 0) + 1

    top_tags = sorted(compteur_tags.items(), key=lambda x: x[1], reverse=True)[:5]

    return jsonify({
        'success': True,
        'data': {
            'total_articles': len(articles_publies),
            'total_commentaires': len(commentaires),
            'total_auteurs': len(set(a['auteur'] for a in articles_publies)),
            'articles_par_mois': articles_par_mois,
            'top_tags': [{'tag': tag, 'count': count} for tag, count in top_tags],
            'moyenne_commentaires_par_article': round(len(commentaires) / len(articles_publies) if articles_publies else 0, 1)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Client pour tester l'API blog

```python
import requests
from datetime import datetime

class BlogClient:
    """Client pour interagir avec l'API de blog"""

    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def lister_articles(self, page=1, limite=10, recherche=None, tag=None):
        """Liste les articles avec filtres"""
        params = {'page': page, 'limit': limite}

        if recherche:
            params['search'] = recherche
        if tag:
            params['tag'] = tag

        response = self.session.get(f'{self.base_url}/api/articles', params=params)
        return response.json() if response.status_code == 200 else None

    def obtenir_article(self, article_id):
        """Récupère un article avec ses commentaires"""
        response = self.session.get(f'{self.base_url}/api/articles/{article_id}')
        return response.json() if response.status_code == 200 else None

    def creer_article(self, titre, contenu, auteur, tags=None):
        """Crée un nouvel article"""
        data = {
            'titre': titre,
            'contenu': contenu,
            'auteur': auteur,
            'tags': tags or []
        }

        response = self.session.post(f'{self.base_url}/api/articles', json=data)
        return response.json() if response.status_code == 201 else None

    def ajouter_commentaire(self, article_id, auteur, contenu):
        """Ajoute un commentaire à un article"""
        data = {
            'auteur': auteur,
            'contenu': contenu
        }

        response = self.session.post(f'{self.base_url}/api/articles/{article_id}/commentaires', json=data)
        return response.json() if response.status_code == 201 else None

    def obtenir_tags(self):
        """Récupère tous les tags"""
        response = self.session.get(f'{self.base_url}/api/tags')
        return response.json() if response.status_code == 200 else None

    def obtenir_statistiques(self):
        """Récupère les statistiques du blog"""
        response = self.session.get(f'{self.base_url}/api/statistiques/blog')
        return response.json() if response.status_code == 200 else None

def demo_blog():
    """Démonstration de l'API de blog"""

    print("📝 Démonstration API Blog")
    print("=" * 30)

    client = BlogClient()

    # 1. Afficher les statistiques initiales
    print("\n📊 Statistiques du blog")
    stats = client.obtenir_statistiques()
    if stats and stats['success']:
        data = stats['data']
        print(f"   Articles: {data['total_articles']}")
        print(f"   Commentaires: {data['total_commentaires']}")
        print(f"   Auteurs: {data['total_auteurs']}")

    # 2. Créer un nouvel article
    print("\n✍️ Création d'un nouvel article")
    nouvel_article = client.creer_article(
        titre="Guide complet des APIs REST avec Python",
        contenu="Dans ce guide, nous allons explorer en détail comment créer et consommer des APIs REST avec Python et Flask. Nous verrons les bonnes pratiques, la gestion d'erreurs, l'authentification et bien plus encore...",
        auteur="Alex Tutorial",
        tags=["python", "api", "rest", "tutorial", "flask"]
    )

    if nouvel_article and nouvel_article['success']:
        print(f"   ✅ Article créé: {nouvel_article['data']['titre']}")
        article_id = nouvel_article['data']['id']

    # 3. Lister les articles
    print("\n📋 Articles du blog")
    articles = client.lister_articles(limite=5)
    if articles and articles['success']:
        for article in articles['data']:
            print(f"   📄 {article['titre']} - {article['auteur']}")
            print(f"      💬 {article['nb_commentaires']} commentaire(s)")
            if article['tags']:
                print(f"      🏷️ Tags: {', '.join(article['tags'])}")

    # 4. Ajouter des commentaires
    if nouvel_article and nouvel_article['success']:
        print(f"\n💬 Ajout de commentaires")

        commentaires_test = [
            {"auteur": "Marie Lectrice", "contenu": "Excellent tutoriel ! Très bien expliqué."},
            {"auteur": "Paul Développeur", "contenu": "Merci pour ce guide, ça va m'aider dans mon projet."},
            {"auteur": "Sophie Codeuse", "contenu": "J'aimerais voir plus d'exemples pratiques."}
        ]

        for comm in commentaires_test:
            resultat = client.ajouter_commentaire(article_id, comm['auteur'], comm['contenu'])
            if resultat and resultat['success']:
                print(f"   ✅ Commentaire de {comm['auteur']} ajouté")

    # 5. Récupérer l'article avec commentaires
    if nouvel_article and nouvel_article['success']:
        print(f"\n📖 Article avec commentaires")
        article_complet = client.obtenir_article(article_id)
        if article_complet and article_complet['success']:
            article = article_complet['data']
            print(f"   Titre: {article['titre']}")
            print(f"   Auteur: {article['auteur']}")
            print(f"   Commentaires ({len(article['commentaires'])}):")

            for comm in article['commentaires']:
                print(f"      💬 {comm['auteur']}: {comm['contenu'][:50]}...")

    # 6. Recherche d'articles
    print(f"\n🔍 Recherche d'articles")
    resultats_recherche = client.lister_articles(recherche="python")
    if resultats_recherche and resultats_recherche['success']:
        print(f"   Trouvé {len(resultats_recherche['data'])} article(s) contenant 'python'")
        for article in resultats_recherche['data']:
            print(f"      📄 {article['titre']}")

    # 7. Top tags
    print(f"\n🏷️ Tags populaires")
    tags = client.obtenir_tags()
    if tags and tags['success']:
        print("   Top 5 tags:")
        for i, tag in enumerate(tags['data']['tags'][:5], 1):
            print(f"      {i}. {tag['nom']} ({tag['count']} articles)")

if __name__ == '__main__':
    demo_blog()
```

## Bonnes pratiques pour les APIs REST

### 1. Versioning d'API

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Version dans l'URL
@app.route('/api/v1/utilisateurs', methods=['GET'])
def obtenir_utilisateurs_v1():
    """Version 1 de l'API utilisateurs"""
    return jsonify({
        'version': '1.0',
        'data': []
    })

@app.route('/api/v2/utilisateurs', methods=['GET'])
def obtenir_utilisateurs_v2():
    """Version 2 avec plus d'informations"""
    return jsonify({
        'version': '2.0',
        'data': [],
        'metadata': {
            'total': 0,
            'page': 1
        }
    })

# Version dans les headers
@app.before_request
def verifier_version():
    version = request.headers.get('API-Version', 'v1')
    request.api_version = version

@app.route('/api/utilisateurs', methods=['GET'])
def obtenir_utilisateurs():
    """API avec version basée sur header"""
    if request.api_version == 'v2':
        return obtenir_utilisateurs_v2()
    else:
        return obtenir_utilisateurs_v1()
```

### 2. Limitation du taux de requêtes (Rate Limiting)

```python
from flask import Flask, jsonify, request
from functools import wraps
import time
from collections import defaultdict

app = Flask(__name__)

# Stockage simple des limites (en production, utilisez Redis)
limite_requetes = defaultdict(list)
LIMITE_PAR_MINUTE = 60

def limiter_requetes(limite=LIMITE_PAR_MINUTE):
    """Décorateur pour limiter le nombre de requêtes"""
    def decorateur(f):
        @wraps(f)
        def fonction_limitee(*args, **kwargs):
            # Identifier le client (IP ou token)
            client_id = request.remote_addr
            maintenant = time.time()

            # Nettoyer les anciennes requêtes (plus d'une minute)
            limite_requetes[client_id] = [
                timestamp for timestamp in limite_requetes[client_id]
                if maintenant - timestamp < 60
            ]

            # Vérifier la limite
            if len(limite_requetes[client_id]) >= limite:
                return jsonify({
                    'success': False,
                    'error': 'Trop de requêtes',
                    'retry_after': 60
                }), 429

            # Enregistrer la requête actuelle
            limite_requetes[client_id].append(maintenant)

            # Ajouter les headers de limite
            response = f(*args, **kwargs)
            if hasattr(response, 'headers'):
                response.headers['X-RateLimit-Limit'] = str(limite)
                response.headers['X-RateLimit-Remaining'] = str(limite - len(limite_requetes[client_id]))

            return response
        return fonction_limitee
    return decorateur

@app.route('/api/donnees', methods=['GET'])
@limiter_requetes(limite=10)  # 10 requêtes par minute
def obtenir_donnees():
    return jsonify({'data': 'Données importantes'})
```

### 3. Authentification JWT

```python
from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre-clé-secrète-très-sécurisée'

def generer_token(user_id):
    """Génère un token JWT"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24),  # Expire dans 24h
        'iat': datetime.utcnow()
    }

    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def verifier_token(f):
    """Décorateur pour vérifier le token JWT"""
    @wraps(f)
    def fonction_protegee(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({
                'success': False,
                'error': 'Token manquant'
            }), 401

        try:
            # Retirer "Bearer " du début
            if token.startswith('Bearer '):
                token = token[7:]

            # Décoder le token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.user_id = payload['user_id']

        except jwt.ExpiredSignatureError:
            return jsonify({
                'success': False,
                'error': 'Token expiré'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'success': False,
                'error': 'Token invalide'
            }), 401

        return f(*args, **kwargs)
    return fonction_protegee

@app.route('/api/login', methods=['POST'])
def connexion():
    """Connexion et génération de token"""
    donnees = request.get_json()

    # Vérification simple (en production, vérifiez contre une vraie base de données)
    if donnees.get('username') == 'admin' and donnees.get('password') == 'secret':
        token = generer_token(user_id=1)
        return jsonify({
            'success': True,
            'token': token,
            'expires_in': 24 * 3600  # 24 heures en secondes
        })

    return jsonify({
        'success': False,
        'error': 'Identifiants incorrects'
    }), 401

@app.route('/api/profil', methods=['GET'])
@verifier_token
def obtenir_profil():
    """Endpoint protégé nécessitant une authentification"""
    return jsonify({
        'success': True,
        'data': {
            'user_id': request.user_id,
            'message': 'Voici votre profil'
        }
    })
```

### 4. Validation avancée avec schemas

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

class UtilisateurSchema(Schema):
    """Schema de validation pour les utilisateurs"""
    nom = fields.Str(required=True, validate=lambda x: len(x) >= 2)
    prenom = fields.Str(required=True, validate=lambda x: len(x) >= 2)
    email = fields.Email(required=True)
    age = fields.Int(validate=lambda x: 0 <= x <= 120)
    telephone = fields.Str(validate=lambda x: len(x.replace(' ', '')) >= 10)

def valider_donnees(schema_class):
    """Décorateur pour valider automatiquement les données JSON"""
    def decorateur(f):
        @wraps(f)
        def fonction_validee(*args, **kwargs):
            schema = schema_class()

            try:
                # Valider et nettoyer les données
                donnees_validees = schema.load(request.get_json())
                request.donnees_validees = donnees_validees

            except ValidationError as e:
                return jsonify({
                    'success': False,
                    'error': 'Données invalides',
                    'details': e.messages
                }), 400

            return f(*args, **kwargs)
        return fonction_validee
    return decorateur

@app.route('/api/utilisateurs', methods=['POST'])
@valider_donnees(UtilisateurSchema)
def creer_utilisateur_valide():
    """Crée un utilisateur avec validation automatique"""
    donnees = request.donnees_validees

    # Ici, les données sont garanties valides
    nouvel_utilisateur = {
        'id': 123,
        **donnees
    }

    return jsonify({
        'success': True,
        'data': nouvel_utilisateur
    }), 201
```

## Résumé et conseils finaux

### Points clés à retenir

1. **REST est un style, pas une technologie** : Respectez les principes REST pour créer des APIs cohérentes

2. **HTTP est votre ami** : Utilisez correctement les méthodes HTTP et codes de statut

3. **Validation est cruciale** : Validez toujours les données d'entrée

4. **Gestion d'erreurs** : Retournez des messages d'erreur clairs et cohérents

5. **Documentation** : Documentez votre API pour faciliter son adoption

6. **Sécurité** : Implémentez l'authentification et l'autorisation appropriées

### Checklist pour une API de qualité

```python
# ✅ Structure de réponse cohérente
{
    "success": True/False,
    "data": {...},
    "message": "...",
    "error": "..."
}

# ✅ Codes de statut appropriés
200: OK
201: Created
400: Bad Request
401: Unauthorized
404: Not Found
500: Internal Server Error

# ✅ Validation des données
def valider_entree(donnees):
    erreurs = []
    # Validation logique
    return erreurs

# ✅ Gestion d'erreurs
try:
    # Logique métier
    pass
except Exception as e:
    return jsonify({'error': str(e)}), 500

# ✅ Documentation
@swag_from('documentation.yml')
def mon_endpoint():
    """Documentation claire de l'endpoint"""
    pass
```

### Évolutions possibles

Une fois que vous maîtrisez les APIs REST basiques, vous pouvez explorer :

- **GraphQL** : Alternative à REST pour des requêtes plus flexibles
- **WebSockets** : Communication temps réel
- **Microservices** : Architecture distribuée
- **API Gateway** : Gestion centralisée des APIs
- **Tests automatisés** : Garantir la qualité de votre API

### Ressources pour aller plus loin

- **Outils de test** : Postman, Insomnia, curl
- **Documentation** : Swagger/OpenAPI, API Blueprint
- **Monitoring** : Logs, métriques, alertes
- **Déploiement** : Docker, CI/CD, cloud providers

Les APIs REST sont la fondation du web moderne. Avec les concepts et exemples de ce module, vous avez maintenant les outils pour créer des APIs robustes et professionnelles !

---

*Pratiquez en créant vos propres APIs et en consommant des APIs publiques pour consolider vos acquis.*

⏭️
