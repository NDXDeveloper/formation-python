🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.3 : Gestion des verrous et synchronisation

## Introduction

Quand plusieurs threads ou processus accèdent aux mêmes ressources, il faut coordonner leurs accès pour éviter les conflits. La synchronisation garantit que vos programmes concurrents fonctionnent correctement et de manière prévisible.

### Analogie simple
Imaginez une **salle de bain partagée** dans un appartement :
- **Sans verrou** : Deux personnes peuvent entrer en même temps → problème !
- **Avec verrou** : Une seule personne à la fois, les autres attendent
- **File d'attente** : Ordre d'attente équitable
- **Signal** : "C'est libre !" pour prévenir les autres

## Problèmes de concurrence

### Race Condition (Condition de course)

```python
import threading
import time

# Variable partagée dangereuse
compteur_dangereux = 0

def incrementer_dangereux():
    """Fonction dangereuse sans synchronisation."""
    global compteur_dangereux

    # Cette opération n'est PAS atomique !
    for _ in range(100000):
        temp = compteur_dangereux  # 1. Lire
        temp += 1                  # 2. Modifier
        compteur_dangereux = temp  # 3. Écrire
        # Un autre thread peut s'exécuter entre ces étapes !

def demo_race_condition():
    """Démontre le problème de race condition."""
    global compteur_dangereux

    print("🔥 DÉMONSTRATION RACE CONDITION")
    print("-" * 35)

    # Reset
    compteur_dangereux = 0

    # Créer plusieurs threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=incrementer_dangereux)
        threads.append(t)

    # Démarrer tous les threads
    start_time = time.time()
    for t in threads:
        t.start()

    # Attendre la fin
    for t in threads:
        t.join()

    duree = time.time() - start_time

    print(f"Résultat attendu: {3 * 100000}")
    print(f"Résultat obtenu: {compteur_dangereux}")
    print(f"Différence: {3 * 100000 - compteur_dangereux}")
    print(f"Temps d'exécution: {duree:.2f}s")
    print("❌ Résultat imprévisible à cause de la race condition!")

demo_race_condition()
```

## Locks (Verrous)

### Lock simple

```python
import threading
import time

# Variable partagée sécurisée
compteur_securise = 0
lock = threading.Lock()

def incrementer_securise():
    """Fonction sécurisée avec lock."""
    global compteur_securise

    for _ in range(100000):
        with lock:  # Acquisition automatique du verrou
            temp = compteur_securise
            temp += 1
            compteur_securise = temp
        # Libération automatique du verrou

def demo_lock():
    """Démontre la solution avec lock."""
    global compteur_securise

    print("\n🔒 SOLUTION AVEC LOCK")
    print("-" * 25)

    # Reset
    compteur_securise = 0

    # Créer plusieurs threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=incrementer_securise)
        threads.append(t)

    # Démarrer tous les threads
    start_time = time.time()
    for t in threads:
        t.start()

    # Attendre la fin
    for t in threads:
        t.join()

    duree = time.time() - start_time

    print(f"Résultat attendu: {3 * 100000}")
    print(f"Résultat obtenu: {compteur_securise}")
    print(f"Différence: {3 * 100000 - compteur_securise}")
    print(f"Temps d'exécution: {duree:.2f}s")
    print("✅ Résultat correct avec synchronisation!")

demo_lock()
```

### RLock (Reentrant Lock)

```python
import threading

class CompteurAvecLog:
    """Compteur thread-safe avec logging."""

    def __init__(self):
        self._valeur = 0
        self._lock = threading.RLock()  # Lock réentrant
        self._historique = []

    def incrementer(self):
        """Incrémente le compteur."""
        with self._lock:
            self._valeur += 1
            self._log_operation(f"Incrémenté à {self._valeur}")

    def decrementer(self):
        """Décrémente le compteur."""
        with self._lock:
            self._valeur -= 1
            self._log_operation(f"Décrémenté à {self._valeur}")

    def _log_operation(self, operation):
        """Log une opération (nécessite aussi le lock)."""
        with self._lock:  # RLock permet l'acquisition multiple
            thread_id = threading.current_thread().ident
            self._historique.append(f"Thread {thread_id}: {operation}")

    def get_valeur(self):
        """Retourne la valeur actuelle."""
        with self._lock:
            return self._valeur

    def get_historique(self):
        """Retourne l'historique des opérations."""
        with self._lock:
            return self._historique.copy()

def worker_compteur(compteur, nom, nb_operations):
    """Worker qui utilise le compteur."""
    for i in range(nb_operations):
        if i % 2 == 0:
            compteur.incrementer()
        else:
            compteur.decrementer()

def demo_rlock():
    """Démontre l'utilisation d'un RLock."""
    print("\n🔄 DÉMONSTRATION RLOCK")
    print("-" * 25)

    compteur = CompteurAvecLog()

    # Créer des workers
    threads = []
    for i in range(3):
        t = threading.Thread(
            target=worker_compteur,
            args=(compteur, f"Worker-{i+1}", 5)
        )
        threads.append(t)

    # Démarrer et attendre
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Valeur finale: {compteur.get_valeur()}")
    print(f"Nombre d'opérations: {len(compteur.get_historique())}")

    # Afficher l'historique
    print("\nHistorique des opérations:")
    for operation in compteur.get_historique()[:10]:  # 10 premières
        print(f"  {operation}")

demo_rlock()
```

## Semaphores

### Limitation de ressources

```python
import threading
import time
import random

# Semaphore pour limiter l'accès à une ressource
semaphore_connexions = threading.Semaphore(3)  # Max 3 connexions simultanées

def simuler_connexion_db(nom, duree):
    """Simule une connexion à la base de données."""
    print(f"🔄 {nom}: Tentative de connexion...")

    # Acquérir une "place" de connexion
    semaphore_connexions.acquire()

    try:
        print(f"🔌 {nom}: Connecté à la DB")

        # Simuler le travail
        time.sleep(duree)

        print(f"✅ {nom}: Travail terminé")

    finally:
        # Libérer la "place" de connexion
        semaphore_connexions.release()
        print(f"🔓 {nom}: Connexion fermée")

def demo_semaphore():
    """Démontre l'utilisation d'un semaphore."""
    print("\n🎯 LIMITATION AVEC SEMAPHORE")
    print("-" * 30)
    print("Max 3 connexions DB simultanées")

    # Créer 6 workers (plus que la limite)
    threads = []
    for i in range(6):
        duree = random.uniform(1, 3)
        t = threading.Thread(
            target=simuler_connexion_db,
            args=(f"Client-{i+1}", duree)
        )
        threads.append(t)

    # Démarrer tous les threads
    for t in threads:
        t.start()
        time.sleep(0.2)  # Décalage pour voir l'effet

    # Attendre la fin
    for t in threads:
        t.join()

    print("🎉 Tous les clients terminés")

demo_semaphore()
```

### Context manager pour Semaphore

```python
import threading
import time
from contextlib import contextmanager

class RessourcePartagee:
    """Gestionnaire de ressource partagée avec semaphore."""

    def __init__(self, nom, max_utilisateurs=2):
        self.nom = nom
        self.max_utilisateurs = max_utilisateurs
        self.semaphore = threading.Semaphore(max_utilisateurs)
        self.utilisateurs_actifs = 0
        self.lock = threading.Lock()

    @contextmanager
    def utiliser(self, nom_utilisateur):
        """Context manager pour utiliser la ressource."""
        print(f"⏳ {nom_utilisateur}: En attente de {self.nom}")

        # Acquérir l'accès
        self.semaphore.acquire()

        with self.lock:
            self.utilisateurs_actifs += 1
            print(f"🔌 {nom_utilisateur}: Utilise {self.nom} ({self.utilisateurs_actifs}/{self.max_utilisateurs})")

        try:
            yield self
        finally:
            with self.lock:
                self.utilisateurs_actifs -= 1
                print(f"🔓 {nom_utilisateur}: Libère {self.nom} ({self.utilisateurs_actifs}/{self.max_utilisateurs})")

            self.semaphore.release()

def utiliser_ressource(ressource, nom_utilisateur, duree_utilisation):
    """Utilise une ressource partagée."""
    with ressource.utiliser(nom_utilisateur):
        # Simuler l'utilisation
        time.sleep(duree_utilisation)

def demo_ressource_partagee():
    """Démonstration de ressource partagée."""
    print("\n🏢 RESSOURCE PARTAGÉE (IMPRIMANTE)")
    print("-" * 35)

    imprimante = RessourcePartagee("Imprimante", max_utilisateurs=2)

    # Plusieurs utilisateurs veulent imprimer
    utilisateurs = [
        ("Alice", 2),
        ("Bob", 1.5),
        ("Charlie", 1),
        ("Diana", 2.5),
        ("Eve", 1.2)
    ]

    threads = []
    for nom, duree in utilisateurs:
        t = threading.Thread(
            target=utiliser_ressource,
            args=(imprimante, nom, duree)
        )
        threads.append(t)

    # Démarrer tous les threads
    for t in threads:
        t.start()
        time.sleep(0.1)

    # Attendre la fin
    for t in threads:
        t.join()

    print("📄 Toutes les impressions terminées")

demo_ressource_partagee()
```

## Events et Conditions

### Event pour signalisation

```python
import threading
import time
import random

# Event pour coordonner les threads
event_debut = threading.Event()
event_fin = threading.Event()

def travailleur(nom, duree_travail):
    """Worker qui attend un signal pour commencer."""
    print(f"👷 {nom}: Prêt, en attente du signal de début")

    # Attendre le signal de début
    event_debut.wait()

    print(f"🚀 {nom}: Début du travail!")

    # Simuler le travail
    time.sleep(duree_travail)

    print(f"✅ {nom}: Travail terminé en {duree_travail}s")

def coordinateur():
    """Coordonne le démarrage des workers."""
    print("📋 Coordinateur: Préparation...")
    time.sleep(2)  # Simulation préparation

    print("📢 Coordinateur: Signal de début envoyé!")
    event_debut.set()  # Déclencher l'événement

    # Attendre un peu puis signaler la fin
    time.sleep(3)
    print("📢 Coordinateur: Signal de fin envoyé!")
    event_fin.set()

def demo_event():
    """Démonstration de synchronisation avec Event."""
    print("\n📡 SYNCHRONISATION AVEC EVENT")
    print("-" * 30)

    # Créer les workers
    workers = []
    for i in range(3):
        duree = random.uniform(1, 4)
        t = threading.Thread(target=travailleur, args=(f"Worker-{i+1}", duree))
        workers.append(t)

    # Créer le coordinateur
    coord = threading.Thread(target=coordinateur)

    # Démarrer tous les threads
    for w in workers:
        w.start()

    coord.start()

    # Attendre la fin
    coord.join()
    for w in workers:
        w.join()

    print("🎉 Synchronisation terminée")

demo_event()
```

### Condition pour coordination complexe

```python
import threading
import time
import random
from collections import deque

class Buffer:
    """Buffer thread-safe avec condition."""

    def __init__(self, taille_max=5):
        self.buffer = deque()
        self.taille_max = taille_max
        self.condition = threading.Condition()

    def produire(self, item):
        """Ajoute un élément au buffer."""
        with self.condition:
            # Attendre que le buffer ne soit plus plein
            while len(self.buffer) >= self.taille_max:
                print(f"📦 Buffer plein, producteur en attente...")
                self.condition.wait()

            # Ajouter l'élément
            self.buffer.append(item)
            print(f"➕ Produit: {item} (buffer: {len(self.buffer)}/{self.taille_max})")

            # Notifier les consommateurs
            self.condition.notify_all()

    def consommer(self):
        """Retire un élément du buffer."""
        with self.condition:
            # Attendre qu'il y ait quelque chose à consommer
            while len(self.buffer) == 0:
                print(f"📭 Buffer vide, consommateur en attente...")
                self.condition.wait()

            # Retirer l'élément
            item = self.buffer.popleft()
            print(f"➖ Consommé: {item} (buffer: {len(self.buffer)}/{self.taille_max})")

            # Notifier les producteurs
            self.condition.notify_all()

            return item

def producteur(buffer, nom, nb_items):
    """Produit des éléments."""
    for i in range(nb_items):
        item = f"{nom}_item_{i+1}"
        buffer.produire(item)
        time.sleep(random.uniform(0.5, 1.5))

def consommateur(buffer, nom, nb_items):
    """Consomme des éléments."""
    for i in range(nb_items):
        item = buffer.consommer()
        print(f"🔄 {nom} traite: {item}")
        time.sleep(random.uniform(0.3, 1.0))

def demo_condition():
    """Démonstration avec Condition."""
    print("\n🔄 PRODUCER-CONSUMER AVEC CONDITION")
    print("-" * 40)

    buffer = Buffer(taille_max=3)

    # Créer producteurs et consommateurs
    threads = [
        threading.Thread(target=producteur, args=(buffer, "Prod1", 4)),
        threading.Thread(target=producteur, args=(buffer, "Prod2", 3)),
        threading.Thread(target=consommateur, args=(buffer, "Cons1", 4)),
        threading.Thread(target=consommateur, args=(buffer, "Cons2", 3))
    ]

    # Démarrer tous les threads
    for t in threads:
        t.start()

    # Attendre la fin
    for t in threads:
        t.join()

    print("🎉 Producer-Consumer terminé")

demo_condition()
```

## Queue thread-safe

### Queue standard

```python
import threading
import queue
import time
import random

def producteur_queue(q, nom, nb_items):
    """Producteur utilisant une queue thread-safe."""
    for i in range(nb_items):
        item = {
            'id': f"{nom}_{i+1}",
            'timestamp': time.time(),
            'data': random.randint(1, 100)
        }

        # put() est thread-safe
        q.put(item)
        print(f"📦 {nom}: Produit {item['id']}")

        time.sleep(random.uniform(0.1, 0.5))

    print(f"✅ {nom}: Production terminée")

def consommateur_queue(q, nom):
    """Consommateur utilisant une queue thread-safe."""
    items_traites = 0

    while True:
        try:
            # get() avec timeout pour éviter d'attendre indéfiniment
            item = q.get(timeout=2)

            print(f"🔄 {nom}: Traite {item['id']}")

            # Simuler le traitement
            time.sleep(random.uniform(0.2, 0.8))

            # Marquer la tâche comme terminée
            q.task_done()

            items_traites += 1
            print(f"✅ {nom}: Terminé {item['id']} (total: {items_traites})")

        except queue.Empty:
            print(f"⏰ {nom}: Timeout, arrêt")
            break

def demo_queue():
    """Démonstration avec Queue thread-safe."""
    print("\n📋 QUEUE THREAD-SAFE")
    print("-" * 20)

    # Créer une queue avec taille limitée
    q = queue.Queue(maxsize=5)

    # Créer les threads
    threads = [
        threading.Thread(target=producteur_queue, args=(q, "Prod1", 3)),
        threading.Thread(target=producteur_queue, args=(q, "Prod2", 4)),
        threading.Thread(target=consommateur_queue, args=(q, "Cons1")),
        threading.Thread(target=consommateur_queue, args=(q, "Cons2"))
    ]

    # Démarrer tous les threads
    for t in threads:
        t.start()

    # Attendre que tous les producteurs terminent
    threads[0].join()  # Prod1
    threads[1].join()  # Prod2

    # Attendre que toutes les tâches soient traitées
    q.join()

    print("🎉 Toutes les tâches traitées")

    # Les consommateurs vont s'arrêter par timeout

demo_queue()
```

## Exercices pratiques

### Exercice 1 : Pool de connexions thread-safe

```python
import threading
import time
import random
from contextlib import contextmanager

class PoolConnexions:
    """Pool de connexions thread-safe."""

    def __init__(self, taille_pool=3):
        self.taille_pool = taille_pool
        self.connexions_libres = queue.Queue()
        self.lock = threading.Lock()
        self.connexions_totales = 0

        # Créer les connexions initiales
        for i in range(taille_pool):
            self._creer_connexion()

    def _creer_connexion(self):
        """Crée une nouvelle connexion."""
        with self.lock:
            conn_id = self.connexions_totales + 1
            self.connexions_totales += 1

        connexion = {
            'id': conn_id,
            'created_at': time.time(),
            'used_count': 0
        }

        self.connexions_libres.put(connexion)
        print(f"🔌 Connexion {conn_id} créée")
        return connexion

    @contextmanager
    def obtenir_connexion(self, timeout=5):
        """Obtient une connexion du pool."""
        try:
            connexion = self.connexions_libres.get(timeout=timeout)
            connexion['used_count'] += 1
            print(f"📲 Connexion {connexion['id']} empruntée (usage #{connexion['used_count']})")

            yield connexion

        except queue.Empty:
            raise TimeoutError("Pas de connexion disponible")

        finally:
            # Remettre la connexion dans le pool
            self.connexions_libres.put(connexion)
            print(f"📲 Connexion {connexion['id']} retournée au pool")

def utiliser_base_donnees(pool, nom_client, nb_requetes):
    """Simule l'utilisation de la base de données."""
    for i in range(nb_requetes):
        try:
            with pool.obtenir_connexion() as conn:
                print(f"💾 {nom_client}: Exécute requête #{i+1} avec connexion {conn['id']}")

                # Simuler la requête
                duree = random.uniform(0.5, 2.0)
                time.sleep(duree)

                print(f"✅ {nom_client}: Requête #{i+1} terminée ({duree:.1f}s)")

        except TimeoutError:
            print(f"❌ {nom_client}: Timeout - pas de connexion disponible")

        # Petite pause entre les requêtes
        time.sleep(random.uniform(0.1, 0.3))

def demo_pool_connexions():
    """Test du pool de connexions."""
    print("🏊 POOL DE CONNEXIONS THREAD-SAFE")
    print("-" * 35)

    pool = PoolConnexions(taille_pool=2)

    # Créer plusieurs clients
    clients = [
        ("Client-A", 3),
        ("Client-B", 2),
        ("Client-C", 4),
        ("Client-D", 2)
    ]

    threads = []
    for nom, nb_req in clients:
        t = threading.Thread(target=utiliser_base_donnees, args=(pool, nom, nb_req))
        threads.append(t)

    # Démarrer tous les clients
    for t in threads:
        t.start()

    # Attendre la fin
    for t in threads:
        t.join()

    print("🎉 Tous les clients terminés")

demo_pool_connexions()
```

### Exercice 2 : Cache thread-safe avec expiration

```python
import threading
import time
from datetime import datetime, timedelta

class CacheThreadSafe:
    """Cache thread-safe avec expiration automatique."""

    def __init__(self, ttl_default=300):  # 5 minutes par défaut
        self.cache = {}
        self.lock = threading.RLock()
        self.ttl_default = ttl_default
        self.stats = {'hits': 0, 'misses': 0, 'expirations': 0}

    def put(self, key, value, ttl=None):
        """Ajoute un élément au cache."""
        if ttl is None:
            ttl = self.ttl_default

        expiration = datetime.now() + timedelta(seconds=ttl)

        with self.lock:
            self.cache[key] = {
                'value': value,
                'expiration': expiration,
                'created_at': datetime.now()
            }

        print(f"💾 Cache: Ajouté '{key}' (expire dans {ttl}s)")

    def get(self, key):
        """Récupère un élément du cache."""
        with self.lock:
            if key not in self.cache:
                self.stats['misses'] += 1
                print(f"❌ Cache miss: '{key}'")
                return None

            entry = self.cache[key]

            # Vérifier l'expiration
            if datetime.now() > entry['expiration']:
                del self.cache[key]
                self.stats['expirations'] += 1
                self.stats['misses'] += 1
                print(f"⏰ Cache expiré: '{key}'")
                return None

            self.stats['hits'] += 1
            print(f"✅ Cache hit: '{key}'")
            return entry['value']

    def clear_expired(self):
        """Nettoie les entrées expirées."""
        with self.lock:
            now = datetime.now()
            keys_to_remove = []

            for key, entry in self.cache.items():
                if now > entry['expiration']:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del self.cache[key]
                self.stats['expirations'] += 1

            if keys_to_remove:
                print(f"🧹 Nettoyage: {len(keys_to_remove)} entrées expirées supprimées")

    def get_stats(self):
        """Retourne les statistiques du cache."""
        with self.lock:
            total = self.stats['hits'] + self.stats['misses']
            hit_rate = (self.stats['hits'] / total * 100) if total > 0 else 0

            return {
                'size': len(self.cache),
                'hits': self.stats['hits'],
                'misses': self.stats['misses'],
                'expirations': self.stats['expirations'],
                'hit_rate': hit_rate
            }

def simuler_requetes_cache(cache, nom_client, nb_requetes):
    """Simule des requêtes de cache."""
    keys = ['user_1', 'user_2', 'config', 'session_abc', 'temp_data']

    for i in range(nb_requetes):
        key = random.choice(keys)

        # 70% chance de lecture, 30% chance d'écriture
        if random.random() < 0.7:
            # Lecture
            value = cache.get(key)
            print(f"📖 {nom_client}: Lecture '{key}' → {value}")
        else:
            # Écriture
            value = f"valeur_{i}_{time.time():.0f}"
            ttl = random.randint(2, 8)  # 2-8 secondes
            cache.put(key, value, ttl)
            print(f"📝 {nom_client}: Écriture '{key}' = {value}")

        time.sleep(random.uniform(0.2, 1.0))

def demo_cache_thread_safe():
    """Test du cache thread-safe."""
    print("🗄️ CACHE THREAD-SAFE AVEC EXPIRATION")
    print("-" * 40)

    cache = CacheThreadSafe(ttl_default=5)

    # Créer plusieurs clients
    clients = ["Client-A", "Client-B", "Client-C"]
    threads = []

    for nom in clients:
        t = threading.Thread(target=simuler_requetes_cache, args=(cache, nom, 8))
        threads.append(t)

    # Thread de nettoyage périodique
    def nettoyage_periodique():
        for _ in range(10):
            time.sleep(2)
            cache.clear_expired()

    nettoyage_thread = threading.Thread(target=nettoyage_periodique)
    threads.append(nettoyage_thread)

    # Démarrer tous les threads
    for t in threads:
        t.start()

    # Attendre la fin
    for t in threads:
        t.join()

    # Afficher les statistiques finales
    stats = cache.get_stats()
    print(f"\n📊 STATISTIQUES FINALES:")
    print(f"  Taille du cache: {stats['size']}")
    print(f"  Hits: {stats['hits']}")
    print(f"  Misses: {stats['misses']}")
    print(f"  Expirations: {stats['expirations']}")
    print(f"  Taux de hit: {stats['hit_rate']:.1f}%")

demo_cache_thread_safe()
```

## Bonnes pratiques

### **1. Toujours utiliser des context managers**
```python
# ✅ Bon : context manager automatique
with lock:
    shared_data += 1

# ❌ Éviter : gestion manuelle
lock.acquire()
try:
    shared_data += 1
finally:
    lock.release()
```

### **2. Éviter les deadlocks**
```python
# ✅ Bon : ordre cohérent des locks
def transfer(from_account, to_account, amount):
    # Toujours acquérir les locks dans le même ordre
    first_lock = min(from_account, to_account, key=id)
    second_lock = max(from_account, to_account, key=id)

    with first_lock:
        with second_lock:
            # Transfer logic
            pass
```

### **3. Timeout sur les opérations**
```python
# ✅ Bon : timeout pour éviter les blocages
try:
    item = queue.get(timeout=5)
except queue.Empty:
    print("Timeout dépassé")
```

## Résumé

La synchronisation est cruciale pour :

1. **Éviter les race conditions** avec des locks
2. **Coordonner l'accès aux ressources** avec des semaphores
3. **Synchroniser les événements** avec Events et Conditions
4. **Gérer les communications** avec des Queues thread-safe

### Outils de synchronisation par cas d'usage

| Outil | Usage | Exemple typique |
|-------|-------|-----------------|
| **Lock** | Protection mutuelle exclusive | Accès à variable partagée |
| **RLock** | Lock réentrant | Méthodes qui s'appellent |
| **Semaphore** | Limitation de ressources | Pool de connexions |
| **Event** | Signalisation simple | Démarrage coordonné |
| **Condition** | Coordination complexe | Producer-Consumer |
| **Queue** | Communication thread-safe | Transfert de données |

### Exercice récapitulatif : Système de monitoring complet

```python
import threading
import queue
import time
import random
from datetime import datetime
from collections import defaultdict

class SystemeMonitoring:
    """Système de monitoring complet avec synchronisation."""

    def __init__(self, max_workers=3):
        # Synchronisation
        self.queue_taches = queue.Queue()
        self.queue_resultats = queue.Queue()
        self.lock_stats = threading.Lock()
        self.event_arret = threading.Event()
        self.semaphore_ressources = threading.Semaphore(max_workers)

        # Données partagées
        self.statistiques = defaultdict(int)
        self.alertes = []

        # État
        self.actif = False
        self.workers = []

    def ajouter_tache(self, type_tache, cible, seuil=80):
        """Ajoute une tâche de monitoring."""
        tache = {
            'id': f"{type_tache}_{cible}_{time.time():.0f}",
            'type': type_tache,
            'cible': cible,
            'seuil': seuil,
            'timestamp': datetime.now()
        }

        self.queue_taches.put(tache)

        with self.lock_stats:
            self.statistiques['taches_ajoutees'] += 1

        print(f"📋 Tâche ajoutée: {tache['id']}")

    def worker_monitoring(self, nom_worker):
        """Worker qui exécute les tâches de monitoring."""
        print(f"👷 {nom_worker} démarré")

        while not self.event_arret.is_set():
            try:
                # Prendre une tâche avec timeout
                tache = self.queue_taches.get(timeout=1)

                # Utiliser le semaphore pour limiter les ressources
                with self.semaphore_ressources:
                    resultat = self.executer_tache(tache, nom_worker)
                    self.queue_resultats.put(resultat)

                self.queue_taches.task_done()

            except queue.Empty:
                continue  # Timeout, vérifier l'arrêt
            except Exception as e:
                print(f"❌ {nom_worker}: Erreur - {e}")

        print(f"🛑 {nom_worker} arrêté")

    def executer_tache(self, tache, worker_name):
        """Exécute une tâche de monitoring."""
        print(f"🔄 {worker_name}: Exécute {tache['id']}")

        # Simuler différents types de monitoring
        if tache['type'] == 'cpu':
            valeur = random.uniform(10, 95)
            metrique = 'CPU'
        elif tache['type'] == 'memoire':
            valeur = random.uniform(30, 90)
            metrique = 'Mémoire'
        elif tache['type'] == 'disque':
            valeur = random.uniform(40, 95)
            metrique = 'Disque'
        else:
            valeur = random.uniform(0, 100)
            metrique = 'Autre'

        # Simuler le temps de monitoring
        time.sleep(random.uniform(0.5, 2.0))

        # Créer le résultat
        resultat = {
            'tache_id': tache['id'],
            'cible': tache['cible'],
            'metrique': metrique,
            'valeur': valeur,
            'seuil': tache['seuil'],
            'alerte': valeur > tache['seuil'],
            'worker': worker_name,
            'timestamp': datetime.now()
        }

        with self.lock_stats:
            self.statistiques['taches_executees'] += 1
            if resultat['alerte']:
                self.statistiques['alertes_generees'] += 1

        print(f"✅ {worker_name}: {tache['id']} → {metrique}: {valeur:.1f}%")

        return resultat

    def gestionnaire_resultats(self):
        """Gestionnaire des résultats de monitoring."""
        print("📊 Gestionnaire de résultats démarré")

        while not self.event_arret.is_set():
            try:
                resultat = self.queue_resultats.get(timeout=1)

                # Traiter le résultat
                if resultat['alerte']:
                    alerte = {
                        'timestamp': resultat['timestamp'],
                        'cible': resultat['cible'],
                        'metrique': resultat['metrique'],
                        'valeur': resultat['valeur'],
                        'seuil': resultat['seuil']
                    }

                    with self.lock_stats:
                        self.alertes.append(alerte)

                    print(f"🚨 ALERTE: {resultat['cible']} - {resultat['metrique']}: {resultat['valeur']:.1f}% > {resultat['seuil']}%")

                self.queue_resultats.task_done()

            except queue.Empty:
                continue

        print("🛑 Gestionnaire de résultats arrêté")

    def demarrer(self, nb_workers=3):
        """Démarre le système de monitoring."""
        if self.actif:
            print("⚠️ Système déjà actif")
            return

        print(f"🚀 Démarrage du système ({nb_workers} workers)")
        self.actif = True
        self.event_arret.clear()

        # Démarrer les workers
        for i in range(nb_workers):
            worker = threading.Thread(
                target=self.worker_monitoring,
                args=(f"Worker-{i+1}",)
            )
            worker.start()
            self.workers.append(worker)

        # Démarrer le gestionnaire de résultats
        gestionnaire = threading.Thread(target=self.gestionnaire_resultats)
        gestionnaire.start()
        self.workers.append(gestionnaire)

        print("✅ Système démarré")

    def arreter(self):
        """Arrête le système de monitoring."""
        if not self.actif:
            print("⚠️ Système déjà arrêté")
            return

        print("🛑 Arrêt du système...")
        self.actif = False
        self.event_arret.set()

        # Attendre que tous les workers se terminent
        for worker in self.workers:
            worker.join()

        self.workers.clear()
        print("✅ Système arrêté")

    def afficher_statistiques(self):
        """Affiche les statistiques du système."""
        with self.lock_stats:
            stats = dict(self.statistiques)
            nb_alertes = len(self.alertes)

        print("\n📊 STATISTIQUES DU SYSTÈME")
        print("-" * 30)
        print(f"Tâches ajoutées: {stats.get('taches_ajoutees', 0)}")
        print(f"Tâches exécutées: {stats.get('taches_executees', 0)}")
        print(f"Alertes générées: {stats.get('alertes_generees', 0)}")
        print(f"Alertes en mémoire: {nb_alertes}")

        if nb_alertes > 0:
            print(f"\n🚨 Dernières alertes:")
            with self.lock_stats:
                for alerte in self.alertes[-3:]:  # 3 dernières
                    print(f"  {alerte['timestamp'].strftime('%H:%M:%S')} - "
                          f"{alerte['cible']}: {alerte['metrique']} "
                          f"{alerte['valeur']:.1f}% > {alerte['seuil']}%")

def demo_systeme_monitoring():
    """Démonstration du système de monitoring complet."""
    print("🖥️ SYSTÈME DE MONITORING COMPLET")
    print("="*40)

    systeme = SystemeMonitoring(max_workers=2)

    try:
        # Démarrer le système
        systeme.demarrer(nb_workers=2)

        # Ajouter des tâches de monitoring
        serveurs = ['serveur-web-1', 'serveur-db-1', 'serveur-cache-1']
        types_monitoring = ['cpu', 'memoire', 'disque']

        print("\n📋 Ajout de tâches de monitoring...")
        for _ in range(12):
            serveur = random.choice(serveurs)
            type_tache = random.choice(types_monitoring)
            seuil = random.choice([70, 80, 85, 90])

            systeme.ajouter_tache(type_tache, serveur, seuil)
            time.sleep(0.2)

        # Laisser le système fonctionner
        print(f"\n⏳ Système en fonctionnement...")
        time.sleep(8)

        # Afficher les statistiques
        systeme.afficher_statistiques()

    finally:
        # Arrêter proprement
        systeme.arreter()
        print("\n🎉 Démonstration terminée")

# Lancer la démonstration
demo_systeme_monitoring()
```

## Comparaison des outils de synchronisation

### **Performance et usage**

```python
import threading
import time

def benchmark_synchronisation():
    """Compare les performances des outils de synchronisation."""

    iterations = 100000

    # Test Lock
    lock = threading.Lock()
    compteur = 0

    def test_lock():
        global compteur
        for _ in range(iterations):
            with lock:
                compteur += 1

    start = time.perf_counter()
    test_lock()
    temps_lock = time.perf_counter() - start

    # Test RLock
    rlock = threading.RLock()
    compteur = 0

    def test_rlock():
        global compteur
        for _ in range(iterations):
            with rlock:
                compteur += 1

    start = time.perf_counter()
    test_rlock()
    temps_rlock = time.perf_counter() - start

    # Test Semaphore
    semaphore = threading.Semaphore(1)
    compteur = 0

    def test_semaphore():
        global compteur
        for _ in range(iterations):
            with semaphore:
                compteur += 1

    start = time.perf_counter()
    test_semaphore()
    temps_semaphore = time.perf_counter() - start

    print("⚡ BENCHMARK SYNCHRONISATION")
    print("-" * 30)
    print(f"Lock:      {temps_lock:.3f}s")
    print(f"RLock:     {temps_rlock:.3f}s ({temps_rlock/temps_lock:.1f}x plus lent)")
    print(f"Semaphore: {temps_semaphore:.3f}s ({temps_semaphore/temps_lock:.1f}x plus lent)")

benchmark_synchronisation()
```

## Antipatterns à éviter

### **1. Deadlock classique**
```python
# ❌ Dangereux : peut causer un deadlock
lock_a = threading.Lock()
lock_b = threading.Lock()

def fonction_1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:  # Thread 1 veut lock_b
            pass

def fonction_2():
    with lock_b:
        time.sleep(0.1)
        with lock_a:  # Thread 2 veut lock_a → DEADLOCK !
            pass
```

### **2. Lock trop large**
```python
# ❌ Inefficace : lock trop global
big_lock = threading.Lock()

def traitement_long():
    with big_lock:  # Bloque tout pendant longtemps
        time.sleep(5)  # Calcul long
        shared_data.append("result")

# ✅ Mieux : lock minimal
def traitement_optimise():
    result = calcul_long()  # Sans lock

    with small_lock:  # Lock minimal
        shared_data.append(result)
```

### **3. Forget de task_done()**
```python
# ❌ Dangereux : queue.join() attendra indéfiniment
def mauvais_consommateur(q):
    while True:
        item = q.get()
        process(item)
        # Oubli de q.task_done() !

# ✅ Correct
def bon_consommateur(q):
    while True:
        item = q.get()
        try:
            process(item)
        finally:
            q.task_done()  # Toujours marquer comme fait
```

## Conseils de débogage

### **Détection de deadlocks**
```python
import threading
import time

def detecter_deadlock():
    """Outil simple de détection de deadlock."""
    print("🔍 Détection de deadlock...")

    threads_actifs = threading.active_count()
    print(f"Threads actifs: {threads_actifs}")

    # Vérifier les threads bloqués
    for thread in threading.enumerate():
        print(f"  {thread.name}: {thread.is_alive()}")

    # Si tous les threads sont bloqués → probable deadlock
    time.sleep(2)
    nouveaux_threads = threading.active_count()

    if nouveaux_threads == threads_actifs:
        print("⚠️ Possible deadlock détecté!")
    else:
        print("✅ Threads progressent normalement")
```

### **Monitoring des locks**
```python
import threading
import time
from collections import defaultdict

class LockMonitor:
    """Monitor pour surveiller l'utilisation des locks."""

    def __init__(self):
        self.stats = defaultdict(lambda: {'acquisitions': 0, 'temps_total': 0})
        self.lock_stats = threading.Lock()

    def monitored_lock(self, name):
        """Crée un lock monitoré."""
        lock = threading.Lock()
        original_enter = lock.__enter__
        original_exit = lock.__exit__

        def enter_monitored():
            start = time.perf_counter()
            result = original_enter()

            with self.lock_stats:
                self.stats[name]['acquisitions'] += 1
                self.stats[name]['derniere_acquisition'] = start

            return result

        def exit_monitored(exc_type, exc_val, exc_tb):
            duree = time.perf_counter() - self.stats[name]['derniere_acquisition']

            with self.lock_stats:
                self.stats[name]['temps_total'] += duree

            return original_exit(exc_type, exc_val, exc_tb)

        lock.__enter__ = enter_monitored
        lock.__exit__ = exit_monitored

        return lock

    def rapport(self):
        """Affiche un rapport des locks."""
        print("📊 RAPPORT D'UTILISATION DES LOCKS")
        print("-" * 35)

        with self.lock_stats:
            for name, stats in self.stats.items():
                acq = stats['acquisitions']
                temps = stats['temps_total']
                moyenne = temps / acq if acq > 0 else 0

                print(f"{name}:")
                print(f"  Acquisitions: {acq}")
                print(f"  Temps total: {temps:.3f}s")
                print(f"  Temps moyen: {moyenne:.3f}s")
                print()

# Test du monitor
monitor = LockMonitor()
lock_a = monitor.monitored_lock("lock_critique")
lock_b = monitor.monitored_lock("lock_stats")

def test_monitored_locks():
    for i in range(5):
        with lock_a:
            time.sleep(0.1)

        with lock_b:
            time.sleep(0.05)

threads = [threading.Thread(target=test_monitored_locks) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

monitor.rapport()
```

## Conclusion

La synchronisation est un aspect critique de la programmation concurrente. Les points clés à retenir :

### **Règles d'or**
1. **Utilisez les outils appropriés** selon le cas d'usage
2. **Minimisez la durée des locks** pour éviter les blocages
3. **Respectez un ordre cohérent** pour éviter les deadlocks
4. **Gérez toujours les exceptions** dans les sections critiques
5. **Testez sous charge** pour détecter les race conditions

### **Outils par situation**
- **Données partagées simples** → Lock
- **Méthodes récursives** → RLock
- **Limitation de ressources** → Semaphore
- **Coordination d'événements** → Event
- **Communication complexe** → Queue
- **Attente conditionnelle** → Condition

La maîtrise de ces outils vous permettra de créer des applications concurrentes robustes et performantes.

Dans la prochaine section, nous explorerons les patterns de concurrence avancés.

⏭️
