🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.2 : Programmation asynchrone avec asyncio

## Introduction

La programmation asynchrone avec `asyncio` permet de gérer des milliers de tâches I/O-bound de façon efficace avec un seul thread. C'est parfait pour les serveurs web, les clients API, et les applications qui font beaucoup d'attente (réseau, fichiers).

### Analogie simple
Imaginez un **serveur de restaurant** :
- **Synchrone** : Le serveur prend une commande, va en cuisine, attend que le plat soit prêt, le sert, puis passe au client suivant
- **Asynchrone** : Le serveur prend une commande, la donne à la cuisine, et pendant que le plat se prépare, il prend d'autres commandes

## Concepts de base

### Coroutines et async/await

```python
import asyncio
import time

# Fonction synchrone classique
def tache_synchrone(nom, duree):
    """Tâche synchrone qui bloque."""
    print(f"🚀 {nom} commencée (synchrone)")
    time.sleep(duree)  # Bloque tout !
    print(f"✅ {nom} terminée")
    return f"Résultat de {nom}"

# Coroutine asynchrone
async def tache_asynchrone(nom, duree):
    """Coroutine asynchrone qui ne bloque pas."""
    print(f"🚀 {nom} commencée (asynchrone)")
    await asyncio.sleep(duree)  # Libère le contrôle
    print(f"✅ {nom} terminée")
    return f"Résultat de {nom}"

# Comparaison des performances
async def demo_async_vs_sync():
    """Compare l'exécution synchrone vs asynchrone."""

    print("=== EXÉCUTION SYNCHRONE ===")
    start_time = time.time()

    # Exécution séquentielle
    tache_synchrone("Tâche 1", 1)
    tache_synchrone("Tâche 2", 1)
    tache_synchrone("Tâche 3", 1)

    sync_time = time.time() - start_time
    print(f"Temps synchrone: {sync_time:.1f}s\n")

    print("=== EXÉCUTION ASYNCHRONE ===")
    start_time = time.time()

    # Exécution concurrente
    await asyncio.gather(
        tache_asynchrone("Tâche 1", 1),
        tache_asynchrone("Tâche 2", 1),
        tache_asynchrone("Tâche 3", 1)
    )

    async_time = time.time() - start_time
    print(f"Temps asynchrone: {async_time:.1f}s")
    print(f"Accélération: {sync_time/async_time:.1f}x")

# Lancer la démonstration
asyncio.run(demo_async_vs_sync())
```

### Gestion des tâches asynchrones

```python
import asyncio
import random

async def telechargement_fichier(nom, taille_mo):
    """Simule le téléchargement d'un fichier."""
    print(f"📥 Début téléchargement: {nom} ({taille_mo}MB)")

    # Simuler le téléchargement avec progression
    for progression in range(0, 101, 20):
        await asyncio.sleep(random.uniform(0.1, 0.3))
        print(f"📊 {nom}: {progression}%")

    print(f"✅ {nom} téléchargé!")
    return {"nom": nom, "taille": taille_mo, "statut": "succès"}

async def gestion_telechargements():
    """Gère plusieurs téléchargements concurrents."""

    fichiers = [
        ("video.mp4", 50),
        ("document.pdf", 10),
        ("archive.zip", 30),
        ("image.jpg", 5)
    ]

    print("🌐 Lancement des téléchargements concurrents")

    # Créer les tâches
    taches = [
        asyncio.create_task(telechargement_fichier(nom, taille))
        for nom, taille in fichiers
    ]

    # Attendre que toutes les tâches se terminent
    resultats = await asyncio.gather(*taches)

    print(f"\n🎉 Tous les téléchargements terminés!")
    for resultat in resultats:
        print(f"  ✅ {resultat['nom']}: {resultat['statut']}")

# Lancer la gestion
asyncio.run(gestion_telechargements())
```

### Gestion des erreurs asynchrones

```python
import asyncio
import random

async def tache_risquee(nom, taux_echec=0.3):
    """Tâche qui peut échouer."""
    print(f"🎲 {nom} démarrée (risque d'échec: {taux_echec*100}%)")

    await asyncio.sleep(random.uniform(0.5, 2))

    if random.random() < taux_echec:
        raise Exception(f"Échec de {nom}")

    print(f"✅ {nom} réussie")
    return f"Résultat de {nom}"

async def executeur_robuste(nom, taux_echec=0.3, max_tentatives=3):
    """Exécute une tâche avec retry automatique."""

    for tentative in range(1, max_tentatives + 1):
        try:
            print(f"🔄 {nom} - Tentative {tentative}/{max_tentatives}")
            resultat = await tache_risquee(nom, taux_echec)
            return {"nom": nom, "resultat": resultat, "tentatives": tentative}

        except Exception as e:
            print(f"❌ {nom} - Tentative {tentative} échouée: {e}")

            if tentative == max_tentatives:
                return {"nom": nom, "erreur": str(e), "tentatives": tentative}

            # Attendre avant de retenter (backoff exponentiel)
            delai = 2 ** (tentative - 1)
            await asyncio.sleep(delai)

async def demo_gestion_erreurs():
    """Démonstration de la gestion d'erreurs robuste."""

    taches = [
        executeur_robuste("API_1", taux_echec=0.2),
        executeur_robuste("API_2", taux_echec=0.4),
        executeur_robuste("API_3", taux_echec=0.6),
        executeur_robuste("API_4", taux_echec=0.1)
    ]

    print("🔧 Test de robustesse avec retry automatique")
    resultats = await asyncio.gather(*taches, return_exceptions=True)

    print(f"\n📊 Résultats:")
    for resultat in resultats:
        if isinstance(resultat, dict):
            if "erreur" in resultat:
                print(f"  ❌ {resultat['nom']}: {resultat['erreur']} (après {resultat['tentatives']} tentatives)")
            else:
                print(f"  ✅ {resultat['nom']}: succès (tentative {resultat['tentatives']})")
        else:
            print(f"  💥 Erreur inattendue: {resultat}")

asyncio.run(demo_gestion_erreurs())
```

## Client HTTP asynchrone

### Utilisation d'aiohttp pour les requêtes

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """Récupère une URL de façon asynchrone."""
    try:
        print(f"📡 Requête vers: {url}")
        async with session.get(url) as response:
            content = await response.text()
            return {
                "url": url,
                "status": response.status,
                "taille": len(content),
                "success": True
            }
    except Exception as e:
        return {
            "url": url,
            "erreur": str(e),
            "success": False
        }

async def client_http_concurrent(urls):
    """Client HTTP concurrent pour plusieurs URLs."""

    print(f"🌐 Téléchargement de {len(urls)} URLs en parallèle")
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        # Lancer toutes les requêtes en parallèle
        taches = [fetch_url(session, url) for url in urls]
        resultats = await asyncio.gather(*taches)

    duree = time.time() - start_time

    # Analyser les résultats
    succes = sum(1 for r in resultats if r["success"])
    echecs = len(resultats) - succes

    print(f"\n📊 Résultats en {duree:.2f}s:")
    print(f"  ✅ Succès: {succes}")
    print(f"  ❌ Échecs: {echecs}")

    for resultat in resultats:
        if resultat["success"]:
            print(f"  ✅ {resultat['url']}: {resultat['status']} ({resultat['taille']} chars)")
        else:
            print(f"  ❌ {resultat['url']}: {resultat['erreur']}")

    return resultats

# Test avec des URLs d'exemple
urls_test = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/200",
    "https://httpbin.org/json",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers"
]

# Décommenter pour tester (nécessite aiohttp: pip install aiohttp)
# asyncio.run(client_http_concurrent(urls_test))
```

### Serveur HTTP asynchrone simple

```python
import asyncio
from datetime import datetime

class ServeurHTTPSimple:
    """Serveur HTTP asynchrone basique."""

    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.routes = {}
        self.stats = {"requetes": 0, "demarrage": datetime.now()}

    def route(self, path):
        """Décorateur pour enregistrer une route."""
        def decorator(handler):
            self.routes[path] = handler
            return handler
        return decorator

    async def traiter_requete(self, reader, writer):
        """Traite une requête HTTP."""
        try:
            # Lire la requête
            data = await reader.read(1024)
            request = data.decode('utf-8')

            # Parser la première ligne
            lines = request.split('\n')
            if lines:
                method, path, version = lines[0].split(' ')

                self.stats["requetes"] += 1
                print(f"📨 {method} {path} (requête #{self.stats['requetes']})")

                # Trouver le handler
                if path in self.routes:
                    response_body = await self.routes[path]()
                else:
                    response_body = f"<h1>404 - Page non trouvée</h1><p>Chemin: {path}</p>"

                # Construire la réponse HTTP
                response = f"""HTTP/1.1 200 OK\r
Content-Type: text/html; charset=utf-8\r
Content-Length: {len(response_body.encode('utf-8'))}\r
\r
{response_body}"""

                # Envoyer la réponse
                writer.write(response.encode('utf-8'))
                await writer.drain()

        except Exception as e:
            print(f"❌ Erreur: {e}")
            error_response = """HTTP/1.1 500 Internal Server Error\r
Content-Type: text/html\r
\r
<h1>500 - Erreur interne</h1>"""
            writer.write(error_response.encode('utf-8'))
            await writer.drain()

        finally:
            writer.close()
            await writer.wait_closed()

    async def demarrer(self):
        """Démarre le serveur."""
        server = await asyncio.start_server(
            self.traiter_requete,
            self.host,
            self.port
        )

        print(f"🚀 Serveur démarré sur http://{self.host}:{self.port}")
        print("📝 Routes disponibles:")
        for route in self.routes:
            print(f"  - http://{self.host}:{self.port}{route}")
        print("🛑 Ctrl+C pour arrêter\n")

        async with server:
            await server.serve_forever()

# Création et configuration du serveur
serveur = ServeurHTTPSimple()

@serveur.route('/')
async def accueil():
    uptime = datetime.now() - serveur.stats["demarrage"]
    return f"""
    <h1>🚀 Serveur Asynchrone Python</h1>
    <p><strong>Statut:</strong> En ligne</p>
    <p><strong>Requêtes traitées:</strong> {serveur.stats["requetes"]}</p>
    <p><strong>Uptime:</strong> {uptime}</p>
    <p><a href="/stats">📊 Statistiques</a></p>
    <p><a href="/test">🧪 Page de test</a></p>
    """

@serveur.route('/stats')
async def stats():
    # Simuler une requête async (ex: base de données)
    await asyncio.sleep(0.1)

    return f"""
    <h1>📊 Statistiques du serveur</h1>
    <ul>
        <li>Requêtes totales: {serveur.stats["requetes"]}</li>
        <li>Démarrage: {serveur.stats["demarrage"].strftime("%Y-%m-%d %H:%M:%S")}</li>
        <li>Uptime: {datetime.now() - serveur.stats["demarrage"]}</li>
    </ul>
    <p><a href="/">🏠 Retour accueil</a></p>
    """

@serveur.route('/test')
async def test():
    # Simuler une opération longue
    await asyncio.sleep(2)

    return f"""
    <h1>🧪 Page de test</h1>
    <p>Cette page simule une opération de 2 secondes.</p>
    <p>Grâce à l'asynchrone, le serveur peut traiter d'autres requêtes pendant ce temps!</p>
    <p>Timestamp: {datetime.now().strftime("%H:%M:%S")}</p>
    <p><a href="/">🏠 Retour accueil</a></p>
    """

# Démarrer le serveur (décommenter pour tester)
# try:
#     asyncio.run(serveur.demarrer())
# except KeyboardInterrupt:
#     print("\n🛑 Serveur arrêté")
```

## Exercices pratiques

### Exercice 1 : Moniteur de sites web

```python
import asyncio
import aiohttp
import time
from datetime import datetime

async def verifier_site(session, url, timeout=5):
    """Vérifie la disponibilité d'un site web."""
    start_time = time.time()

    try:
        async with session.get(url, timeout=timeout) as response:
            duree = time.time() - start_time

            return {
                "url": url,
                "status": response.status,
                "temps_reponse": duree,
                "disponible": response.status < 400,
                "timestamp": datetime.now()
            }

    except asyncio.TimeoutError:
        return {
            "url": url,
            "erreur": "Timeout",
            "disponible": False,
            "timestamp": datetime.now()
        }
    except Exception as e:
        return {
            "url": url,
            "erreur": str(e),
            "disponible": False,
            "timestamp": datetime.now()
        }

async def monitorer_sites(sites, intervalle=30, iterations=3):
    """Monitore plusieurs sites à intervalles réguliers."""

    print(f"🔍 Monitoring de {len(sites)} sites (intervalle: {intervalle}s)")

    async with aiohttp.ClientSession() as session:
        for iteration in range(iterations):
            print(f"\n📊 Vérification #{iteration + 1}")

            # Vérifier tous les sites en parallèle
            taches = [verifier_site(session, site) for site in sites]
            resultats = await asyncio.gather(*taches)

            # Afficher les résultats
            for resultat in resultats:
                if resultat["disponible"]:
                    temps = resultat.get("temps_reponse", 0)
                    print(f"  ✅ {resultat['url']}: {resultat['status']} ({temps:.2f}s)")
                else:
                    erreur = resultat.get("erreur", "Erreur inconnue")
                    print(f"  ❌ {resultat['url']}: {erreur}")

            # Attendre avant la prochaine vérification
            if iteration < iterations - 1:
                print(f"⏳ Attente {intervalle}s...")
                await asyncio.sleep(intervalle)

    print("✅ Monitoring terminé")

# Test
sites_test = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/500",  # Simuler une erreur
    "https://google.com"
]

# Décommenter pour tester
# asyncio.run(monitorer_sites(sites_test, intervalle=10, iterations=2))
```

### Exercice 2 : Gestionnaire de tâches asynchrones

```python
import asyncio
import random
from enum import Enum

class StatutTache(Enum):
    EN_ATTENTE = "en_attente"
    EN_COURS = "en_cours"
    TERMINEE = "terminee"
    ECHOUEE = "echouee"

class Tache:
    """Représente une tâche asynchrone."""

    def __init__(self, nom, duree, taux_echec=0.1):
        self.nom = nom
        self.duree = duree
        self.taux_echec = taux_echec
        self.statut = StatutTache.EN_ATTENTE
        self.resultat = None
        self.erreur = None

    async def executer(self):
        """Exécute la tâche."""
        self.statut = StatutTache.EN_COURS
        print(f"🔄 Démarrage: {self.nom}")

        try:
            # Simuler le travail
            await asyncio.sleep(self.duree)

            # Simuler un échec possible
            if random.random() < self.taux_echec:
                raise Exception(f"Échec simulé de {self.nom}")

            self.statut = StatutTache.TERMINEE
            self.resultat = f"Résultat de {self.nom}"
            print(f"✅ Terminé: {self.nom}")

        except Exception as e:
            self.statut = StatutTache.ECHOUEE
            self.erreur = str(e)
            print(f"❌ Échec: {self.nom} - {e}")

class GestionnaireTaches:
    """Gestionnaire de tâches asynchrones avec limite de concurrence."""

    def __init__(self, max_concurrent=3):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.taches = []

    def ajouter_tache(self, nom, duree, taux_echec=0.1):
        """Ajoute une tâche à la liste."""
        tache = Tache(nom, duree, taux_echec)
        self.taches.append(tache)
        return tache

    async def executer_tache_limitee(self, tache):
        """Exécute une tâche avec limite de concurrence."""
        async with self.semaphore:  # Limite le nombre de tâches simultanées
            await tache.executer()

    async def executer_toutes(self):
        """Exécute toutes les tâches avec gestion de la concurrence."""
        if not self.taches:
            print("Aucune tâche à exécuter")
            return

        print(f"🚀 Exécution de {len(self.taches)} tâches (max {self.max_concurrent} simultanées)")

        # Créer les tâches asyncio
        taches_async = [
            asyncio.create_task(self.executer_tache_limitee(tache))
            for tache in self.taches
        ]

        # Attendre toutes les tâches
        await asyncio.gather(*taches_async, return_exceptions=True)

        # Afficher le résumé
        self.afficher_resume()

    def afficher_resume(self):
        """Affiche un résumé de l'exécution."""
        stats = {
            StatutTache.TERMINEE: 0,
            StatutTache.ECHOUEE: 0
        }

        for tache in self.taches:
            stats[tache.statut] = stats.get(tache.statut, 0) + 1

        print(f"\n📊 Résumé:")
        print(f"  ✅ Réussites: {stats[StatutTache.TERMINEE]}")
        print(f"  ❌ Échecs: {stats[StatutTache.ECHOUEE]}")
        print(f"  📈 Taux de réussite: {stats[StatutTache.TERMINEE]/len(self.taches)*100:.1f}%")

# Test du gestionnaire
async def demo_gestionnaire():
    gestionnaire = GestionnaireTaches(max_concurrent=3)

    # Ajouter des tâches
    gestionnaire.ajouter_tache("Traitement_1", 2, 0.1)
    gestionnaire.ajouter_tache("Traitement_2", 1.5, 0.2)
    gestionnaire.ajouter_tache("Traitement_3", 3, 0.05)
    gestionnaire.ajouter_tache("Traitement_4", 1, 0.3)
    gestionnaire.ajouter_tache("Traitement_5", 2.5, 0.15)
    gestionnaire.ajouter_tache("Traitement_6", 1.8, 0.1)

    await gestionnaire.executer_toutes()

# Lancer la démonstration
asyncio.run(demo_gestionnaire())
```

### Exercice 3 : Chat server basique

```python
import asyncio
import json
from datetime import datetime

class ChatServer:
    """Serveur de chat asynchrone simple."""

    def __init__(self, host='localhost', port=8889):
        self.host = host
        self.port = port
        self.clients = set()
        self.historique = []

    async def diffuser_message(self, message, expediteur=None):
        """Diffuse un message à tous les clients connectés."""
        if not self.clients:
            return

        # Ajouter à l'historique
        self.historique.append({
            "timestamp": datetime.now().isoformat(),
            "expediteur": expediteur,
            "message": message
        })

        # Garder seulement les 100 derniers messages
        self.historique = self.historique[-100:]

        # Diffuser aux clients connectés
        message_formate = json.dumps({
            "type": "message",
            "expediteur": expediteur,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })

        # Envoyer à tous les clients (en parallèle)
        if self.clients:
            await asyncio.gather(
                *[self.envoyer_message(client, message_formate) for client in self.clients],
                return_exceptions=True
            )

    async def envoyer_message(self, writer, message):
        """Envoie un message à un client spécifique."""
        try:
            writer.write(f"{message}\n".encode())
            await writer.drain()
        except Exception:
            # Client déconnecté, l'enlever de la liste
            self.clients.discard(writer)

    async def gerer_client(self, reader, writer):
        """Gère un client connecté."""
        client_addr = writer.get_extra_info('peername')
        print(f"👤 Nouveau client connecté: {client_addr}")

        self.clients.add(writer)

        # Envoyer l'historique au nouveau client
        if self.historique:
            historique_json = json.dumps({
                "type": "historique",
                "messages": self.historique[-10:]  # 10 derniers messages
            })
            await self.envoyer_message(writer, historique_json)

        # Annoncer l'arrivée
        await self.diffuser_message(f"Un nouvel utilisateur s'est connecté", "Système")

        try:
            while True:
                # Lire les messages du client
                data = await reader.readline()
                if not data:
                    break

                message = data.decode().strip()
                if message:
                    print(f"💬 {client_addr}: {message}")
                    await self.diffuser_message(message, str(client_addr))

        except Exception as e:
            print(f"❌ Erreur avec {client_addr}: {e}")

        finally:
            # Nettoyer lors de la déconnexion
            self.clients.discard(writer)
            writer.close()
            await writer.wait_closed()

            await self.diffuser_message(f"Un utilisateur s'est déconnecté", "Système")
            print(f"👋 Client déconnecté: {client_addr}")

    async def demarrer(self):
        """Démarre le serveur de chat."""
        server = await asyncio.start_server(
            self.gerer_client,
            self.host,
            self.port
        )

        print(f"💬 Serveur de chat démarré sur {self.host}:{self.port}")
        print("🔌 Les clients peuvent se connecter avec: telnet localhost 8889")
        print("🛑 Ctrl+C pour arrêter\n")

        async with server:
            await server.serve_forever()

# Client de test simple
async def client_test():
    """Client de test pour le serveur de chat."""
    try:
        reader, writer = await asyncio.open_connection('localhost', 8889)

        print("🔌 Connecté au serveur de chat")
        print("💬 Tapez vos messages (Ctrl+C pour quitter)\n")

        # Tâche pour recevoir les messages
        async def recevoir_messages():
            while True:
                try:
                    data = await reader.readline()
                    if not data:
                        break

                    message = json.loads(data.decode().strip())

                    if message["type"] == "message":
                        print(f"[{message['timestamp'][:19]}] {message['expediteur']}: {message['message']}")
                    elif message["type"] == "historique":
                        print("📜 Historique des messages:")
                        for msg in message["messages"]:
                            print(f"[{msg['timestamp'][:19]}] {msg['expediteur']}: {msg['message']}")
                        print()

                except Exception as e:
                    print(f"Erreur réception: {e}")
                    break

        # Démarrer la réception de messages
        receive_task = asyncio.create_task(recevoir_messages())

        # Envoyer des messages de test
        messages_test = [
            "Bonjour tout le monde!",
            "Comment ça va?",
            "Test du serveur asynchrone",
            "Au revoir!"
        ]

        for message in messages_test:
            await asyncio.sleep(2)
            writer.write(f"{message}\n".encode())
            await writer.drain()

        await asyncio.sleep(2)
        writer.close()
        await writer.wait_closed()
        receive_task.cancel()

    except Exception as e:
        print(f"Erreur client: {e}")

# Démarrer le serveur (décommenter pour tester)
# chat_server = ChatServer()
# try:
#     asyncio.run(chat_server.demarrer())
# except KeyboardInterrupt:
#     print("\n🛑 Serveur arrêté")

# Ou tester le client
# asyncio.run(client_test())
```

## Bonnes pratiques asyncio

### **1. Gestion des ressources**
```python
# ✅ Bon : Utiliser async with pour les ressources
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.text()

# ✅ Bon : Nettoyer les tâches
task = asyncio.create_task(ma_coroutine())
try:
    result = await task
finally:
    if not task.done():
        task.cancel()
```

### **2. Limitation de concurrence**
```python
# ✅ Bon : Utiliser un semaphore pour limiter
semaphore = asyncio.Semaphore(10)

async def tache_limitee():
    async with semaphore:
        # Travail limité à 10 simultanés
        pass
```

### **3. Gestion d'erreurs**
```python
# ✅ Bon : Gérer les exceptions dans gather
results = await asyncio.gather(*tasks, return_exceptions=True)
for result in results:
    if isinstance(result, Exception):
        print(f"Erreur: {result}")
    else:
        print(f"Résultat: {result}")

# ✅ Bon : Try-except dans les coroutines
async def tache_securisee():
    try:
        return await operation_risquee()
    except SpecificException as e:
        logger.error(f"Erreur spécifique: {e}")
        return None
    except Exception as e:
        logger.error(f"Erreur inattendue: {e}")
        raise
```

### **4. Éviter les blocages**
```python
# ❌ Éviter : Opérations bloquantes
def mauvaise_fonction():
    time.sleep(1)  # Bloque tout le loop !
    return "résultat"

# ✅ Bon : Utiliser run_in_executor pour les opérations bloquantes
async def bonne_fonction():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, operation_bloquante)

# ✅ Bon : Version asynchrone native
async def excellente_fonction():
    await asyncio.sleep(1)  # Non-bloquant
    return "résultat"
```

### **5. Timeout et annulation**
```python
# ✅ Bon : Utiliser timeout
async def avec_timeout():
    try:
        result = await asyncio.wait_for(operation_lente(), timeout=5.0)
        return result
    except asyncio.TimeoutError:
        print("Opération trop lente, annulée")
        return None

# ✅ Bon : Annulation propre
async def gestionnaire_taches():
    task = asyncio.create_task(longue_operation())

    try:
        return await task
    except KeyboardInterrupt:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("Tâche annulée proprement")
        raise
```

## Patterns asyncio avancés

### **1. Context Manager asynchrone**
```python
class ConnexionDB:
    """Context manager asynchrone pour base de données."""

    async def __aenter__(self):
        print("🔌 Connexion à la base de données")
        await asyncio.sleep(0.1)  # Simulation connexion
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("🔌 Fermeture connexion base de données")
        await asyncio.sleep(0.1)  # Simulation fermeture

    async def executer_requete(self, sql):
        """Simule l'exécution d'une requête."""
        await asyncio.sleep(0.2)
        return f"Résultat de: {sql}"

async def utiliser_db():
    """Utilisation du context manager asynchrone."""
    async with ConnexionDB() as db:
        resultat = await db.executer_requete("SELECT * FROM users")
        print(f"📊 {resultat}")

asyncio.run(utiliser_db())
```

### **2. Iterator asynchrone**
```python
class GenerateurDonnees:
    """Générateur de données asynchrone."""

    def __init__(self, max_items=5):
        self.max_items = max_items
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.max_items:
            raise StopAsyncIteration

        # Simuler la récupération de données
        await asyncio.sleep(0.5)
        self.current += 1
        return f"Données #{self.current}"

async def traiter_donnees_async():
    """Traite des données de façon asynchrone."""
    print("📥 Traitement de données asynchrone:")

    async for donnee in GenerateurDonnees(3):
        print(f"  🔄 Traitement: {donnee}")
        await asyncio.sleep(0.1)  # Simulation traitement

    print("✅ Traitement terminé")

asyncio.run(traiter_donnees_async())
```

### **3. Producer-Consumer asynchrone**
```python
import asyncio
import random

class ProducteurConsommateur:
    """Pattern Producer-Consumer avec asyncio."""

    def __init__(self, taille_queue=5):
        self.queue = asyncio.Queue(maxsize=taille_queue)
        self.actif = True

    async def producteur(self, nom, nb_items):
        """Produit des éléments de façon asynchrone."""
        for i in range(nb_items):
            if not self.actif:
                break

            item = f"{nom}_item_{i+1}"

            # Simuler la production
            await asyncio.sleep(random.uniform(0.1, 0.5))

            await self.queue.put(item)
            print(f"📦 {nom} a produit: {item}")

        print(f"✅ {nom} terminé")

    async def consommateur(self, nom):
        """Consomme des éléments de façon asynchrone."""
        while self.actif:
            try:
                # Attendre un élément avec timeout
                item = await asyncio.wait_for(self.queue.get(), timeout=2.0)

                print(f"🔄 {nom} traite: {item}")

                # Simuler le traitement
                await asyncio.sleep(random.uniform(0.2, 0.8))

                self.queue.task_done()
                print(f"✅ {nom} a terminé: {item}")

            except asyncio.TimeoutError:
                print(f"⏰ {nom}: timeout, vérification d'arrêt")
                if self.queue.empty():
                    break

    async def executer(self, duree=10):
        """Exécute le système producer-consumer."""
        print(f"🏭 Démarrage du système (durée: {duree}s)")

        # Créer les tâches
        taches = [
            asyncio.create_task(self.producteur("Prod1", 5)),
            asyncio.create_task(self.producteur("Prod2", 4)),
            asyncio.create_task(self.consommateur("Cons1")),
            asyncio.create_task(self.consommateur("Cons2"))
        ]

        # Arrêter après la durée spécifiée
        await asyncio.sleep(duree)
        self.actif = False

        # Attendre que toutes les tâches se terminent
        await asyncio.gather(*taches, return_exceptions=True)

        print("🎉 Système arrêté")

# Test du système
pc = ProducteurConsommateur()
asyncio.run(pc.executer(8))
```

## Performance et optimisation

### **Mesure de performance asyncio**
```python
import asyncio
import time
from functools import wraps

def mesurer_async(func):
    """Décorateur pour mesurer les performances des fonctions async."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            end = time.perf_counter()
            print(f"⏱️ {func.__name__}: {end - start:.3f}s")
    return wrapper

@mesurer_async
async def operation_lente():
    """Opération qui prend du temps."""
    await asyncio.sleep(1)
    return "Terminé"

@mesurer_async
async def operations_concurrentes():
    """Plusieurs opérations en parallèle."""
    tasks = [operation_lente() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    return results

# Test de performance
async def test_performance():
    print("🧪 Test de performance asyncio")

    # Séquentiel
    print("\n1. Exécution séquentielle:")
    for i in range(3):
        await operation_lente()

    # Concurrent
    print("\n2. Exécution concurrente:")
    await operations_concurrentes()

asyncio.run(test_performance())
```

### **Optimisation mémoire**
```python
import asyncio
import weakref

class GestionnaireRessources:
    """Gestionnaire de ressources avec nettoyage automatique."""

    def __init__(self):
        self.connexions = weakref.WeakSet()
        self.taches_actives = set()

    async def creer_connexion(self, url):
        """Crée une connexion avec suivi automatique."""
        print(f"🔌 Création connexion: {url}")

        # Simuler la connexion
        connexion = {"url": url, "active": True}
        self.connexions.add(connexion)

        return connexion

    async def creer_tache_suivie(self, coro):
        """Crée une tâche avec nettoyage automatique."""
        task = asyncio.create_task(coro)
        self.taches_actives.add(task)

        def nettoyer(task):
            self.taches_actives.discard(task)

        task.add_done_callback(nettoyer)
        return task

    async def nettoyer_ressources(self):
        """Nettoie toutes les ressources."""
        print("🧹 Nettoyage des ressources")

        # Annuler les tâches actives
        for task in list(self.taches_actives):
            if not task.done():
                task.cancel()

        if self.taches_actives:
            await asyncio.gather(*self.taches_actives, return_exceptions=True)

        print(f"✅ Nettoyage terminé ({len(self.connexions)} connexions actives)")

# Test du gestionnaire
async def test_gestionnaire():
    gestionnaire = GestionnaireRessources()

    try:
        # Créer des ressources
        connexion = await gestionnaire.creer_connexion("db://localhost")

        task1 = await gestionnaire.creer_tache_suivie(asyncio.sleep(2))
        task2 = await gestionnaire.creer_tache_suivie(asyncio.sleep(3))

        await asyncio.sleep(1)

    finally:
        await gestionnaire.nettoyer_ressources()

asyncio.run(test_gestionnaire())
```

## Quand utiliser asyncio ?

### **✅ Excellents cas d'usage**
- **Serveurs web** haute concurrence
- **Clients API** avec nombreuses requêtes
- **WebSockets** et temps réel
- **Crawling/Scraping** de sites web
- **Microservices** avec I/O intensif

### **❌ Cas moins adaptés**
- **Calculs intensifs** (utiliser multiprocessing)
- **Applications simples** sans concurrence
- **Scripts one-shot** rapides
- **Legacy code** difficile à convertir

### **Exemple de choix d'architecture**
```python
# ✅ Bon pour asyncio : serveur API
async def serveur_api():
    """Serveur API qui gère de nombreuses requêtes I/O."""
    # Chaque requête peut faire des appels DB, cache, autres APIs
    # Pendant qu'une requête attend, d'autres peuvent être traitées
    pass

# ❌ Mauvais pour asyncio : calcul intensif
def calcul_complexe():
    """Calcul mathématique intensif."""
    # Utilise 100% CPU, pas d'I/O
    # asyncio n'apporte rien, utiliser multiprocessing
    pass

# 🤔 Cas mixte : traitement de fichiers
async def traitement_mixte():
    """Traitement avec I/O et calculs."""
    # Lecture fichier: async (I/O)
    # Traitement: run_in_executor (CPU)
    # Sauvegarde: async (I/O)
    pass
```

## Débogage et monitoring

### **Outils de débogage asyncio**
```python
import asyncio
import logging

# Activer le mode debug
asyncio.get_event_loop().set_debug(True)

# Logging détaillé
logging.basicConfig(level=logging.DEBUG)

async def debug_example():
    """Exemple avec debugging activé."""
    print("🐛 Mode debug activé")

    # Cette opération sera tracée
    await asyncio.sleep(0.1)

    # Cette tâche sera surveillée
    task = asyncio.create_task(asyncio.sleep(1))
    await task

# asyncio.run(debug_example())
```

### **Monitoring des performances**
```python
import asyncio
import time
from collections import defaultdict

class MonitorAsyncio:
    """Monitor pour surveiller les performances asyncio."""

    def __init__(self):
        self.stats = defaultdict(list)
        self.start_time = time.time()

    def log_operation(self, nom, duree):
        """Enregistre une opération."""
        self.stats[nom].append(duree)

    async def operation_surveillee(self, nom, coro):
        """Surveille l'exécution d'une coroutine."""
        start = time.perf_counter()
        try:
            result = await coro
            return result
        finally:
            duree = time.perf_counter() - start
            self.log_operation(nom, duree)

    def rapport(self):
        """Génère un rapport de performance."""
        print("📊 RAPPORT DE PERFORMANCE ASYNCIO")
        print("-" * 40)

        for nom, durees in self.stats.items():
            if durees:
                moyenne = sum(durees) / len(durees)
                minimum = min(durees)
                maximum = max(durees)
                total = sum(durees)

                print(f"{nom}:")
                print(f"  Exécutions: {len(durees)}")
                print(f"  Temps total: {total:.3f}s")
                print(f"  Moyenne: {moyenne:.3f}s")
                print(f"  Min/Max: {minimum:.3f}s / {maximum:.3f}s")
                print()

# Test du monitor
async def test_monitoring():
    monitor = MonitorAsyncio()

    # Simuler des opérations surveillées
    await monitor.operation_surveillee("db_query", asyncio.sleep(0.1))
    await monitor.operation_surveillee("api_call", asyncio.sleep(0.2))
    await monitor.operation_surveillee("db_query", asyncio.sleep(0.15))
    await monitor.operation_surveillee("file_read", asyncio.sleep(0.05))

    monitor.rapport()

asyncio.run(test_monitoring())
```

## Résumé

La programmation asynchrone avec `asyncio` est idéale pour :

### **Points clés**
1. **I/O-bound tasks** : réseau, fichiers, bases de données
2. **Haute concurrence** : milliers de connexions simultanées
3. **Réactivité** : interfaces qui restent fluides
4. **Efficacité mémoire** : un seul thread pour de nombreuses tâches

### **Concepts essentiels**
- **async/await** : définir et appeler des coroutines
- **asyncio.gather()** : exécuter plusieurs tâches en parallèle
- **asyncio.Queue()** : communication entre coroutines
- **asyncio.Semaphore()** : limiter la concurrence

### **Patterns utiles**
- **Producer-Consumer** asynchrone
- **Context managers** async (`async with`)
- **Iterators** async (`async for`)
- **Retry** avec backoff exponentiel

### **Bonnes pratiques**
- Gérer les ressources avec `async with`
- Limiter la concurrence avec `Semaphore`
- Utiliser `timeout` pour éviter les blocages
- Nettoyer les tâches avec `cancel()`

L'asyncio ouvre la voie à des applications très performantes pour les tâches I/O-intensives. Une fois maîtrisé, il permet de créer des serveurs web, des clients API et des applications temps réel remarquablement efficaces.

Dans la prochaine section, nous explorerons la gestion des verrous et la synchronisation avancée.

⏭️
