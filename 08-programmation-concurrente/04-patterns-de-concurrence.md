🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.4 Patterns de Concurrence

## Introduction aux patterns de concurrence

Les **patterns de concurrence** sont des solutions éprouvées pour résoudre des problèmes courants en programmation parallèle. Ce sont des "recettes" que vous pouvez réutiliser dans vos projets.

**Analogie** : Comme les recettes de cuisine, les patterns de concurrence fournissent une structure testée pour résoudre un problème spécifique. Vous n'avez pas à réinventer la roue !

### Pourquoi utiliser des patterns ?

✅ **Avantages** :
- Solutions éprouvées et testées
- Code plus maintenable et compréhensible
- Évitent les erreurs courantes
- Facilitent la communication entre développeurs

❌ **Sans patterns** :
- Code complexe et difficile à déboguer
- Risques de deadlocks et race conditions
- Réinvention de solutions existantes

---

## Pattern 1 : Producer-Consumer (Producteur-Consommateur)

Le pattern **Producer-Consumer** sépare la production de données de leur consommation via une file d'attente (queue).

### Analogie

Imaginez une chaîne de production :
- **Producteurs** : Ouvriers qui fabriquent des pièces
- **Queue** : Tapis roulant qui stocke les pièces
- **Consommateurs** : Ouvriers qui assemblent les pièces

Les producteurs et consommateurs travaillent à leur propre rythme sans se bloquer mutuellement.

### Quand l'utiliser ?

✅ Utilisez Producer-Consumer quand :
- Les tâches de production et consommation ont des vitesses différentes
- Vous voulez découpler la création de données de leur traitement
- Vous avez besoin d'un buffer entre deux parties du système

### Implémentation avec Threading

```python
import threading
import queue
import time
import random

def producteur(q, producteur_id, nombre_items):
    """Produit des items et les met dans la queue"""
    for i in range(nombre_items):
        item = f"P{producteur_id}-Item{i}"

        # Simuler le temps de production
        time.sleep(random.uniform(0.1, 0.5))

        q.put(item)
        print(f"✅ Producteur {producteur_id}: produit {item} (queue: {q.qsize()})")

    print(f"🏁 Producteur {producteur_id}: terminé")

def consommateur(q, consommateur_id):
    """Consomme des items de la queue"""
    while True:
        try:
            # Timeout pour éviter de bloquer indéfiniment
            item = q.get(timeout=2)

            print(f"🔧 Consommateur {consommateur_id}: traite {item}")

            # Simuler le temps de traitement
            time.sleep(random.uniform(0.2, 0.8))

            q.task_done()

        except queue.Empty:
            print(f"⏸️  Consommateur {consommateur_id}: queue vide, arrêt")
            break

# Utilisation
file_attente = queue.Queue(maxsize=10)

# Créer les threads
producteurs = [
    threading.Thread(target=producteur, args=(file_attente, i, 5))
    for i in range(2)
]

consommateurs = [
    threading.Thread(target=consommateur, args=(file_attente, i))
    for i in range(3)
]

# Démarrer tous les threads
print("🚀 Démarrage du système Producer-Consumer\n")
for p in producteurs:
    p.start()
for c in consommateurs:
    c.start()

# Attendre la fin
for p in producteurs:
    p.join()
file_attente.join()  # Attendre que tous les items soient traités

print("\n✅ Tous les items ont été produits et consommés")
```

### Implémentation avec Asyncio

```python
import asyncio
import random

async def producteur_async(q, producteur_id, nombre_items):
    """Producteur asynchrone"""
    for i in range(nombre_items):
        item = f"P{producteur_id}-Item{i}"
        await asyncio.sleep(random.uniform(0.1, 0.5))
        await q.put(item)
        print(f"✅ Producteur {producteur_id}: produit {item}")

    print(f"🏁 Producteur {producteur_id}: terminé")

async def consommateur_async(q, consommateur_id, nb_producteurs):
    """Consommateur asynchrone"""
    items_traites = 0

    while True:
        try:
            item = await asyncio.wait_for(q.get(), timeout=2.0)
            print(f"🔧 Consommateur {consommateur_id}: traite {item}")
            await asyncio.sleep(random.uniform(0.2, 0.8))
            items_traites += 1
            q.task_done()

        except asyncio.TimeoutError:
            print(f"⏸️  Consommateur {consommateur_id}: arrêt ({items_traites} items)")
            break

async def main():
    """Point d'entrée principal"""
    q = asyncio.Queue(maxsize=10)

    # Créer producteurs et consommateurs
    nb_producteurs = 2
    producteurs = [producteur_async(q, i, 5) for i in range(nb_producteurs)]
    consommateurs = [consommateur_async(q, i, nb_producteurs) for i in range(3)]

    # Exécuter
    await asyncio.gather(*producteurs, *consommateurs)
    print("\n✅ Pipeline terminé")

asyncio.run(main())
```

---

## Pattern 2 : Worker Pool (Pool de Workers)

Le **Worker Pool** maintient un ensemble de workers prêts à traiter des tâches.

### Analogie

Un centre d'appels avec plusieurs opérateurs :
- **Manager** : Distribue les appels entrants
- **Workers** : Opérateurs qui répondent aux appels
- **Queue** : File d'attente des appels

Quand un opérateur est libre, il prend le prochain appel dans la file.

### Quand l'utiliser ?

✅ Utilisez Worker Pool quand :
- Vous avez beaucoup de tâches similaires à exécuter
- Vous voulez limiter le nombre de threads/processus
- Les tâches sont indépendantes les unes des autres

### Implémentation avec concurrent.futures

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def traiter_tache(tache_id):
    """Traite une tâche"""
    print(f"🔧 Worker {threading.current_thread().name}: démarre tâche {tache_id}")

    # Simuler le traitement
    duree = random.uniform(1, 3)
    time.sleep(duree)

    resultat = f"Résultat-{tache_id}"
    print(f"✅ Worker {threading.current_thread().name}: terminé tâche {tache_id}")

    return resultat

# Créer un pool de 3 workers
with ThreadPoolExecutor(max_workers=3) as executor:
    print("🚀 Pool de workers démarré (3 workers)\n")

    # Soumettre 10 tâches
    futures = [executor.submit(traiter_tache, i) for i in range(10)]

    # Récupérer les résultats au fur et à mesure
    for future in as_completed(futures):
        resultat = future.result()
        print(f"📦 Résultat reçu: {resultat}")

print("\n✅ Toutes les tâches sont terminées")
```

### Worker Pool avec map()

```python
from concurrent.futures import ThreadPoolExecutor
import time

def calculer_carre(nombre):
    """Calcule le carré d'un nombre"""
    time.sleep(0.5)  # Simule un calcul
    return nombre ** 2

nombres = list(range(1, 11))

# Utiliser map pour traiter la liste
with ThreadPoolExecutor(max_workers=4) as executor:
    resultats = list(executor.map(calculer_carre, nombres))

print(f"Nombres: {nombres}")
print(f"Carrés: {resultats}")
```

### Worker Pool avec Asyncio

```python
import asyncio
import random

async def worker(nom, queue_taches, queue_resultats):
    """Worker asynchrone qui traite des tâches"""
    while True:
        try:
            tache = await asyncio.wait_for(queue_taches.get(), timeout=1.0)

            print(f"🔧 {nom}: traite tâche {tache}")
            await asyncio.sleep(random.uniform(0.5, 1.5))

            resultat = f"Résultat-{tache}"
            await queue_resultats.put(resultat)

            queue_taches.task_done()

        except asyncio.TimeoutError:
            print(f"⏸️  {nom}: aucune tâche, arrêt")
            break

async def main():
    """Gestionnaire de pool"""
    queue_taches = asyncio.Queue()
    queue_resultats = asyncio.Queue()

    # Remplir la queue de tâches
    for i in range(15):
        await queue_taches.put(f"Tâche-{i}")

    # Créer un pool de 5 workers
    workers = [
        asyncio.create_task(worker(f"Worker-{i}", queue_taches, queue_resultats))
        for i in range(5)
    ]

    # Attendre que toutes les tâches soient traitées
    await queue_taches.join()

    # Attendre que tous les workers terminent
    await asyncio.gather(*workers)

    # Afficher les résultats
    print(f"\n📊 {queue_resultats.qsize()} résultats obtenus")

asyncio.run(main())
```

---

## Pattern 3 : Pipeline

Le **Pipeline** enchaîne plusieurs étapes de traitement, où la sortie d'une étape devient l'entrée de la suivante.

### Analogie

Une chaîne d'assemblage automobile :
1. **Étape 1** : Construire le châssis
2. **Étape 2** : Installer le moteur
3. **Étape 3** : Peindre la voiture
4. **Étape 4** : Installer les roues

Chaque étape travaille en parallèle sur différentes voitures.

### Quand l'utiliser ?

✅ Utilisez Pipeline quand :
- Vous avez plusieurs étapes de traitement séquentielles
- Chaque étape peut travailler indépendamment
- Vous voulez maximiser le débit (throughput)

### Implémentation

```python
import threading
import queue
import time
import random

def etape_1_collecte(queue_sortie, nombre_items):
    """Étape 1: Collecte des données"""
    print("📥 Étape 1: Collecte des données")
    for i in range(nombre_items):
        donnee = f"Data-{i}"
        time.sleep(random.uniform(0.1, 0.3))
        queue_sortie.put(donnee)
        print(f"  → Collecté: {donnee}")

    queue_sortie.put(None)  # Signal de fin
    print("🏁 Étape 1: Terminée")

def etape_2_nettoyage(queue_entree, queue_sortie):
    """Étape 2: Nettoyage des données"""
    print("🧹 Étape 2: Nettoyage des données")
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            queue_sortie.put(None)
            break

        time.sleep(random.uniform(0.2, 0.4))
        donnee_nettoyee = f"Clean-{donnee}"
        queue_sortie.put(donnee_nettoyee)
        print(f"  → Nettoyé: {donnee_nettoyee}")

    print("🏁 Étape 2: Terminée")

def etape_3_traitement(queue_entree, queue_sortie):
    """Étape 3: Traitement des données"""
    print("⚙️  Étape 3: Traitement des données")
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            queue_sortie.put(None)
            break

        time.sleep(random.uniform(0.3, 0.5))
        donnee_traitee = f"Processed-{donnee}"
        queue_sortie.put(donnee_traitee)
        print(f"  → Traité: {donnee_traitee}")

    print("🏁 Étape 3: Terminée")

def etape_4_sauvegarde(queue_entree):
    """Étape 4: Sauvegarde des résultats"""
    print("💾 Étape 4: Sauvegarde des résultats")
    resultats = []
    while True:
        donnee = queue_entree.get()
        if donnee is None:
            break

        time.sleep(random.uniform(0.1, 0.2))
        resultats.append(donnee)
        print(f"  → Sauvegardé: {donnee}")

    print(f"🏁 Étape 4: Terminée ({len(resultats)} items)")
    return resultats

# Créer les queues entre les étapes
q1_to_2 = queue.Queue(maxsize=5)
q2_to_3 = queue.Queue(maxsize=5)
q3_to_4 = queue.Queue(maxsize=5)

# Créer les threads pour chaque étape
threads = [
    threading.Thread(target=etape_1_collecte, args=(q1_to_2, 10)),
    threading.Thread(target=etape_2_nettoyage, args=(q1_to_2, q2_to_3)),
    threading.Thread(target=etape_3_traitement, args=(q2_to_3, q3_to_4)),
    threading.Thread(target=etape_4_sauvegarde, args=(q3_to_4,))
]

# Démarrer le pipeline
print("🚀 Démarrage du pipeline\n")
debut = time.time()

for t in threads:
    t.start()
for t in threads:
    t.join()

duree = time.time() - debut
print(f"\n✅ Pipeline complet en {duree:.2f}s")
```

---

## Pattern 4 : Fan-Out / Fan-In

**Fan-Out** : Une tâche distribue le travail à plusieurs workers
**Fan-In** : Plusieurs workers envoient leurs résultats à un collecteur

### Analogie

Un restaurant :
- **Fan-Out** : Le chef (dispatcher) distribue les commandes à plusieurs cuisiniers
- **Fan-In** : Tous les plats préparés arrivent au même serveur

### Quand l'utiliser ?

✅ Utilisez Fan-Out/Fan-In quand :
- Une tâche peut être divisée en sous-tâches indépendantes
- Vous voulez paralléliser puis agréger les résultats
- Exemple : Recherche dans plusieurs sources puis fusion

### Implémentation

```python
import threading
import queue
import time
import random

def dispatcher(taches, queues_workers):
    """Fan-Out: Distribue les tâches aux workers"""
    print("📤 Dispatcher: Distribution des tâches")

    for i, tache in enumerate(taches):
        # Distribuer en round-robin
        worker_id = i % len(queues_workers)
        queues_workers[worker_id].put(tache)
        print(f"  → Tâche {tache} → Worker {worker_id}")

    # Signal de fin pour tous les workers
    for q in queues_workers:
        q.put(None)

    print("🏁 Dispatcher: Terminé")

def worker(worker_id, queue_entree, queue_resultats):
    """Worker qui traite des tâches"""
    print(f"🔧 Worker {worker_id}: Démarré")

    while True:
        tache = queue_entree.get()
        if tache is None:
            break

        # Traiter la tâche
        time.sleep(random.uniform(0.5, 1.5))
        resultat = f"Résultat-{tache}-by-W{worker_id}"

        queue_resultats.put(resultat)
        print(f"  ✅ Worker {worker_id}: {tache} → {resultat}")

    print(f"🏁 Worker {worker_id}: Terminé")

def collecteur(queue_resultats, nombre_taches):
    """Fan-In: Collecte tous les résultats"""
    print("📥 Collecteur: En attente des résultats")
    resultats = []

    for _ in range(nombre_taches):
        resultat = queue_resultats.get()
        resultats.append(resultat)
        print(f"  ← Reçu: {resultat}")

    print(f"🏁 Collecteur: Terminé ({len(resultats)} résultats)")
    return resultats

# Configuration
taches = [f"Tâche-{i}" for i in range(12)]
nombre_workers = 4

# Créer les queues
queues_workers = [queue.Queue() for _ in range(nombre_workers)]
queue_resultats = queue.Queue()

# Créer les threads
thread_dispatcher = threading.Thread(
    target=dispatcher,
    args=(taches, queues_workers)
)

threads_workers = [
    threading.Thread(target=worker, args=(i, queues_workers[i], queue_resultats))
    for i in range(nombre_workers)
]

thread_collecteur = threading.Thread(
    target=collecteur,
    args=(queue_resultats, len(taches))
)

# Démarrer
print("🚀 Démarrage Fan-Out/Fan-In\n")
debut = time.time()

thread_dispatcher.start()
for t in threads_workers:
    t.start()
thread_collecteur.start()

# Attendre la fin
thread_dispatcher.join()
for t in threads_workers:
    t.join()
thread_collecteur.join()

duree = time.time() - debut
print(f"\n✅ Fan-Out/Fan-In complet en {duree:.2f}s")
```

---

## Pattern 5 : Future / Promise

Le pattern **Future** représente le résultat d'une opération asynchrone qui sera disponible dans le futur.

### Analogie

Comme un ticket de pressing :
- Vous déposez vos vêtements (soumission de la tâche)
- On vous donne un ticket (Future)
- Vous revenez plus tard avec le ticket pour récupérer vos vêtements (résultat)

### Quand l'utiliser ?

✅ Utilisez Future quand :
- Vous lancez une tâche longue et voulez continuer autre chose
- Vous voulez récupérer le résultat plus tard
- Vous avez besoin de gérer plusieurs tâches asynchrones

### Implémentation avec concurrent.futures

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def tache_longue(nom, duree):
    """Simule une tâche qui prend du temps"""
    print(f"🔧 Démarrage: {nom}")
    time.sleep(duree)
    resultat = f"Résultat de {nom}"
    print(f"✅ Terminé: {nom}")
    return resultat

# Créer un executor
executor = ThreadPoolExecutor(max_workers=3)

# Soumettre plusieurs tâches et obtenir des Futures
print("📤 Soumission des tâches\n")
future1 = executor.submit(tache_longue, "Tâche-A", 2)
future2 = executor.submit(tache_longue, "Tâche-B", 1)
future3 = executor.submit(tache_longue, "Tâche-C", 3)

print("💼 Les tâches sont lancées, on peut faire autre chose...\n")
time.sleep(0.5)
print("💼 Autre travail en cours...\n")

# Récupérer les résultats quand ils sont prêts
print("📥 Récupération des résultats:")
print(f"  • Future1 terminé? {future1.done()}")
print(f"  • Future2 terminé? {future2.done()}")

# Attendre et récupérer les résultats
print(f"  • Résultat 1: {future1.result()}")  # Bloque si pas encore prêt
print(f"  • Résultat 2: {future2.result()}")
print(f"  • Résultat 3: {future3.result()}")

executor.shutdown()
print("\n✅ Toutes les futures résolues")
```

### Gestion d'erreurs avec Future

```python
from concurrent.futures import ThreadPoolExecutor
import time

def tache_avec_erreur(numero):
    """Tâche qui peut échouer"""
    time.sleep(1)
    if numero == 3:
        raise ValueError(f"Erreur avec le numéro {numero}")
    return f"Succès {numero}"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(tache_avec_erreur, i) for i in range(1, 6)]

    for i, future in enumerate(futures, 1):
        try:
            resultat = future.result()
            print(f"✅ Tâche {i}: {resultat}")
        except Exception as e:
            print(f"❌ Tâche {i}: Erreur - {e}")
```

### Avec as_completed() - Traiter au fur et à mesure

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def telecharger_fichier(url):
    """Simule le téléchargement d'un fichier"""
    duree = random.uniform(1, 4)
    time.sleep(duree)
    return f"{url} téléchargé en {duree:.1f}s"

urls = [f"https://example.com/file{i}.zip" for i in range(8)]

with ThreadPoolExecutor(max_workers=4) as executor:
    # Soumettre toutes les tâches
    futures = {executor.submit(telecharger_fichier, url): url for url in urls}

    # Traiter les résultats au fur et à mesure qu'ils arrivent
    for future in as_completed(futures):
        url = futures[future]
        try:
            resultat = future.result()
            print(f"✅ {resultat}")
        except Exception as e:
            print(f"❌ {url}: Erreur - {e}")
```

---

## Pattern 6 : Map-Reduce

**Map-Reduce** traite de grandes quantités de données en deux phases :
1. **Map** : Transforme chaque élément en parallèle
2. **Reduce** : Agrège les résultats

### Analogie

Comptage des votes dans une élection :
- **Map** : Chaque bureau de vote compte ses bulletins
- **Reduce** : Les totaux de tous les bureaux sont additionnés

### Quand l'utiliser ?

✅ Utilisez Map-Reduce quand :
- Vous traitez de grandes collections de données
- Les traitements sont indépendants (embarrassingly parallel)
- Vous avez besoin d'agréger les résultats

### Implémentation simple

```python
from concurrent.futures import ProcessPoolExecutor
import time

def map_function(nombre):
    """Phase Map: Calcule le carré"""
    return nombre ** 2

def reduce_function(resultats):
    """Phase Reduce: Somme tous les carrés"""
    return sum(resultats)

# Données
nombres = list(range(1, 101))

# Phase Map (parallèle)
with ProcessPoolExecutor() as executor:
    debut = time.time()
    carres = list(executor.map(map_function, nombres))
    duree_map = time.time() - debut

# Phase Reduce
debut = time.time()
total = reduce_function(carres)
duree_reduce = time.time() - debut

print(f"📊 Map-Reduce:")
print(f"  • Nombres: 1-100")
print(f"  • Somme des carrés: {total}")
print(f"  • Temps Map: {duree_map:.3f}s")
print(f"  • Temps Reduce: {duree_reduce:.3f}s")
```

### Exemple avancé : Analyse de texte

```python
from concurrent.futures import ProcessPoolExecutor
from collections import Counter
import re

def compter_mots(texte):
    """Phase Map: Compte les mots dans un texte"""
    mots = re.findall(r'\w+', texte.lower())
    return Counter(mots)

def fusionner_compteurs(compteurs):
    """Phase Reduce: Fusionne tous les compteurs"""
    resultat = Counter()
    for compteur in compteurs:
        resultat.update(compteur)
    return resultat

# Données: plusieurs documents
documents = [
    "Python est un langage de programmation. Python est facile.",
    "La programmation est amusante. Python est populaire.",
    "Le langage Python est utilisé en science des données.",
    "Python est un excellent langage pour débuter.",
]

# Phase Map: Compter les mots de chaque document en parallèle
with ProcessPoolExecutor() as executor:
    compteurs = list(executor.map(compter_mots, documents))

# Phase Reduce: Fusionner tous les compteurs
compteur_total = fusionner_compteurs(compteurs)

# Afficher les 5 mots les plus fréquents
print("📊 Analyse Map-Reduce:")
print("\nTop 5 des mots les plus fréquents:")
for mot, compte in compteur_total.most_common(5):
    print(f"  • {mot}: {compte} fois")
```

---

## Pattern 7 : Actor Model (Modèle d'Acteur)

Le **Actor Model** encapsule l'état et la logique dans des "acteurs" qui communiquent par messages.

### Analogie

Des employés dans une entreprise :
- Chaque acteur est un employé avec sa propre boîte de réception
- Les acteurs communiquent en s'envoyant des emails (messages)
- Chaque acteur traite ses messages dans l'ordre

### Quand l'utiliser ?

✅ Utilisez Actor Model quand :
- Vous avez besoin d'entités avec leur propre état
- La communication par messages est naturelle
- Vous voulez isoler les états pour éviter les race conditions

### Implémentation simple

```python
import threading
import queue
import time
from typing import Any

class Actor:
    """Acteur simple avec sa propre queue de messages"""

    def __init__(self, nom):
        self.nom = nom
        self.queue = queue.Queue()
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        """Boucle principale de l'acteur"""
        print(f"🎭 {self.nom}: Démarré")
        while self.running:
            try:
                message = self.queue.get(timeout=0.5)
                self._handle_message(message)
            except queue.Empty:
                continue
        print(f"🏁 {self.nom}: Arrêté")

    def _handle_message(self, message):
        """Traite un message (à surcharger)"""
        print(f"📨 {self.nom} reçoit: {message}")

    def send(self, message):
        """Envoie un message à cet acteur"""
        self.queue.put(message)

    def stop(self):
        """Arrête l'acteur"""
        self.running = False
        self.thread.join()

# Exemple d'acteur spécialisé
class CalculatorActor(Actor):
    """Acteur qui effectue des calculs"""

    def _handle_message(self, message):
        operation, a, b = message
        if operation == "add":
            resultat = a + b
            print(f"🔢 {self.nom}: {a} + {b} = {resultat}")
        elif operation == "multiply":
            resultat = a * b
            print(f"🔢 {self.nom}: {a} × {b} = {resultat}")

class LoggerActor(Actor):
    """Acteur qui log des messages"""

    def _handle_message(self, message):
        timestamp = time.strftime("%H:%M:%S")
        print(f"📝 [{timestamp}] {message}")

# Utilisation
calculator = CalculatorActor("Calculatrice")
logger = LoggerActor("Logger")

# Envoyer des messages
logger.send("Système démarré")
calculator.send(("add", 5, 3))
calculator.send(("multiply", 4, 7))
logger.send("Calculs terminés")

time.sleep(2)

# Arrêter les acteurs
calculator.stop()
logger.stop()
```

---

## Pattern 8 : Scatter-Gather

**Scatter-Gather** envoie une requête à plusieurs services et collecte toutes les réponses.

### Analogie

Comparer les prix dans plusieurs magasins :
- **Scatter** : Demander le prix à tous les magasins en même temps
- **Gather** : Attendre toutes les réponses et choisir la meilleure

### Quand l'utiliser ?

✅ Utilisez Scatter-Gather quand :
- Vous interrogez plusieurs sources de données
- Vous voulez la réponse la plus rapide ou toutes les réponses
- Exemple : Recherche dans plusieurs APIs

### Implémentation

```python
import asyncio
import random

async def interroger_service(nom_service, requete):
    """Interroge un service distant"""
    print(f"📤 Requête vers {nom_service}")

    # Simuler la latence du réseau
    latence = random.uniform(0.5, 3.0)
    await asyncio.sleep(latence)

    # Simuler une réponse
    reponse = {
        'service': nom_service,
        'resultat': f"Données de {nom_service}",
        'latence': latence,
        'prix': random.randint(50, 150)
    }

    print(f"📥 Réponse de {nom_service} ({latence:.2f}s)")
    return reponse

async def scatter_gather_all(requete, services):
    """Scatter-Gather: Attend toutes les réponses"""
    print(f"🚀 Scatter: Envoi vers {len(services)} services\n")

    # Scatter: Lancer toutes les requêtes en parallèle
    taches = [interroger_service(service, requete) for service in services]

    # Gather: Attendre toutes les réponses
    reponses = await asyncio.gather(*taches)

    print(f"\n✅ Gather: {len(reponses)} réponses reçues")
    return reponses

async def scatter_gather_first(requete, services):
    """Retourne la première réponse"""
    print(f"🚀 Scatter: Envoi vers {len(services)} services\n")

    taches = [interroger_service(service, requete) for service in services]

    # Attendre la première réponse
    done, pending = await asyncio.wait(taches, return_when=asyncio.FIRST_COMPLETED)

    # Annuler les tâches restantes
    for tache in pending:
        tache.cancel()

    reponse = done.pop().result()
    print(f"\n⚡ Première réponse: {reponse['service']}")
    return reponse

# Utilisation
async def main():
    services = ["ServiceA", "ServiceB", "ServiceC", "ServiceD"]
    requete = "Chercher produit XYZ"

    # Stratégie 1: Attendre toutes les réponses
    print("=== Stratégie: Toutes les réponses ===")
    reponses = await scatter_gather_all(requete, services)

    # Trouver le meilleur prix
    meilleur = min(reponses, key=lambda r: r['prix'])
    print(f"\n💰 Meilleur prix: {meilleur['prix']}€ ({meilleur['service']})")

    print("\n" + "="*50 + "\n")

    # Stratégie 2: Première réponse seulement
    print("=== Stratégie: Première réponse ===")
    reponse = await scatter_gather_first(requete, services)
    print(f"📦 Résultat: {reponse['resultat']}")

asyncio.run(main())
```

---

## Pattern 9 : Rate Limiting (Limitation de débit)

Le **Rate Limiting** contrôle le nombre d'opérations par unité de temps.

### Analogie

Un barrage qui régule le débit d'eau :
- Trop d'eau d'un coup → inondation (surcharge)
- Le barrage laisse passer un débit contrôlé

### Quand l'utiliser ?

✅ Utilisez Rate Limiting quand :
- Vous appelez une API avec des limites de requêtes
- Vous voulez éviter de surcharger un service
- Vous devez respecter des quotas

### Implémentation simple

```python
import asyncio
import time

class RateLimiter:
    """Limiteur de débit simple"""

    def __init__(self, max_calls, period):
        """
        Args:
            max_calls: Nombre max d'appels
            period: Période en secondes
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        """Acquiert le droit de faire un appel"""
        async with self.lock:
            now = time.time()

            # Nettoyer les anciens appels
            self.calls = [c for c in self.calls if now - c < self.period]

            if len(self.calls) >= self.max_calls:
                # Attendre
                sleep_time = self.period - (now - self.calls[0])
                print(f"⏳ Rate limit atteint, attente de {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)
                self.calls = []

            self.calls.append(time.time())

async def appeler_api(api_id, rate_limiter):
    """Appelle une API avec rate limiting"""
    await rate_limiter.acquire()
    print(f"📞 Appel API {api_id} à {time.strftime('%H:%M:%S')}")
    await asyncio.sleep(0.1)  # Simule l'appel
    return f"Résultat-{api_id}"

async def main():
    # Limite: 5 appels par 2 secondes
    rate_limiter = RateLimiter(max_calls=5, period=2.0)

    # Faire 15 appels
    taches = [appeler_api(i, rate_limiter) for i in range(15)]
    resultats = await asyncio.gather(*taches)

    print(f"\n✅ {len(resultats)} appels effectués avec respect du rate limit")

asyncio.run(main())
```

### Implémentation avec Semaphore et délai

```python
import asyncio
import time

class TokenBucket:
    """Implémentation Token Bucket pour rate limiting"""

    def __init__(self, rate, capacity):
        self.rate = rate  # Tokens par seconde
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.time()
        self.lock = asyncio.Lock()

    async def acquire(self, tokens=1):
        """Acquiert des tokens"""
        async with self.lock:
            await self._refill()

            while self.tokens < tokens:
                sleep_time = (tokens - self.tokens) / self.rate
                await asyncio.sleep(sleep_time)
                await self._refill()

            self.tokens -= tokens

    async def _refill(self):
        """Remplit le bucket avec de nouveaux tokens"""
        now = time.time()
        elapsed = now - self.last_update
        new_tokens = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_update = now

async def tache_limitee(task_id, bucket):
    """Tâche avec rate limiting"""
    await bucket.acquire()
    print(f"✅ Tâche {task_id} exécutée à {time.strftime('%H:%M:%S')}")
    await asyncio.sleep(0.1)

async def main():
    # 3 tokens par seconde, capacité max 5
    bucket = TokenBucket(rate=3.0, capacity=5)

    taches = [tache_limitee(i, bucket) for i in range(12)]
    await asyncio.gather(*taches)

asyncio.run(main())
```

---

## Choisir le bon pattern

Voici un guide pour choisir le pattern approprié selon votre situation :

| Situation | Pattern recommandé |
|-----------|-------------------|
| Produire et consommer à des vitesses différentes | Producer-Consumer |
| Beaucoup de tâches similaires, limiter les threads | Worker Pool |
| Plusieurs étapes séquentielles de traitement | Pipeline |
| Distribuer puis collecter des résultats | Fan-Out/Fan-In |
| Lancer des tâches et récupérer résultats plus tard | Future/Promise |
| Traiter de grandes collections de données | Map-Reduce |
| Entités avec état et communication par messages | Actor Model |
| Interroger plusieurs sources simultanément | Scatter-Gather |
| Respecter des limites d'API | Rate Limiting |

---

## Exemple complet : Système de scraping web

Voici un exemple réaliste qui combine plusieurs patterns :

```python
import asyncio
import aiohttp
import time
from typing import List, Dict
from collections import Counter

class WebScraperSystem:
    """Système de scraping combinant plusieurs patterns"""

    def __init__(self, max_concurrent=5, rate_limit=10):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.rate_limiter = RateLimiter(rate_limit, period=1.0)
        self.resultats = []
        self.lock = asyncio.Lock()

    async def fetch_url(self, session, url):
        """
        Fetch une URL avec rate limiting et semaphore
        Pattern: Rate Limiting + Worker Pool
        """
        async with self.semaphore:
            await self.rate_limiter.acquire()

            try:
                print(f"📥 Téléchargement: {url}")
                await asyncio.sleep(0.5)  # Simule le téléchargement

                # Simuler le contenu
                contenu = f"Contenu simulé de {url}"
                return {'url': url, 'contenu': contenu, 'status': 'success'}

            except Exception as e:
                return {'url': url, 'erreur': str(e), 'status': 'error'}

    async def extraire_donnees(self, page_data):
        """
        Extrait les données d'une page
        Pattern: Pipeline (étape 2)
        """
        await asyncio.sleep(0.2)  # Simule l'extraction

        # Simuler l'extraction de mots
        mots = page_data['contenu'].split()
        return {
            'url': page_data['url'],
            'mots': mots,
            'nb_mots': len(mots)
        }

    async def worker_pipeline(self, session, url):
        """
        Worker complet qui fait fetch + extraction
        Pattern: Pipeline
        """
        # Étape 1: Télécharger
        page_data = await self.fetch_url(session, url)

        if page_data['status'] == 'error':
            return page_data

        # Étape 2: Extraire
        donnees_extraites = await self.extraire_donnees(page_data)

        # Stocker les résultats
        async with self.lock:
            self.resultats.append(donnees_extraites)

        return donnees_extraites

    async def scraper_urls(self, urls: List[str]):
        """
        Scrape plusieurs URLs
        Pattern: Fan-Out/Fan-In + Worker Pool
        """
        print(f"🚀 Démarrage du scraping de {len(urls)} URLs")
        print(f"📊 Config: max {self.semaphore._value} concurrent, rate limit {self.rate_limiter.max_calls}/s\n")

        debut = time.time()

        # Simuler une session HTTP
        session = None  # En vrai: aiohttp.ClientSession()

        # Fan-Out: Créer toutes les tâches
        taches = [self.worker_pipeline(session, url) for url in urls]

        # Fan-In: Collecter tous les résultats
        resultats = await asyncio.gather(*taches, return_exceptions=True)

        duree = time.time() - debut

        # Statistiques
        succes = sum(1 for r in resultats if isinstance(r, dict) and r.get('status') != 'error')
        echecs = len(resultats) - succes

        print(f"\n✅ Scraping terminé en {duree:.2f}s")
        print(f"📊 Résultats: {succes} succès, {echecs} échecs")

        return resultats

    def analyser_resultats(self):
        """
        Analyse les résultats collectés
        Pattern: Map-Reduce
        """
        print("\n📊 Analyse des résultats (Map-Reduce):")

        # Map: Extraire tous les mots
        tous_les_mots = []
        for resultat in self.resultats:
            if 'mots' in resultat:
                tous_les_mots.extend(resultat['mots'])

        # Reduce: Compter les occurrences
        compteur = Counter(tous_les_mots)

        print(f"  • Total de mots: {len(tous_les_mots)}")
        print(f"  • Mots uniques: {len(compteur)}")
        print(f"  • Top 5 mots:")
        for mot, count in compteur.most_common(5):
            print(f"    - {mot}: {count} fois")

class RateLimiter:
    """Rate limiter simple pour l'exemple"""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.time()
            self.calls = [c for c in self.calls if now - c < self.period]

            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                await asyncio.sleep(sleep_time)
                self.calls = []

            self.calls.append(time.time())

async def main():
    """Démonstration du système complet"""

    # Créer les URLs à scraper
    urls = [f"https://example.com/page{i}" for i in range(20)]

    # Créer le système
    scraper = WebScraperSystem(max_concurrent=5, rate_limit=10)

    # Lancer le scraping
    resultats = await scraper.scraper_urls(urls)

    # Analyser les résultats
    scraper.analyser_resultats()

if __name__ == '__main__':
    asyncio.run(main())
```

---

## Bonnes pratiques pour les patterns

### 1. Commencez simple

```python
# ✅ Bon - Commencer avec le plus simple
def traiter_donnees_simple(donnees):
    return [traiter_item(item) for item in donnees]

# Si nécessaire, ajouter la parallélisation
from concurrent.futures import ThreadPoolExecutor

def traiter_donnees_parallele(donnees):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(traiter_item, donnees))
```

### 2. Mesurez avant d'optimiser

```python
import time

def mesurer_performance(fonction, *args):
    """Mesure le temps d'exécution"""
    debut = time.time()
    resultat = fonction(*args)
    duree = time.time() - debut
    print(f"⏱️  {fonction.__name__}: {duree:.2f}s")
    return resultat

# Comparer les approches
donnees = list(range(1000))
mesurer_performance(traiter_sequentiel, donnees)
mesurer_performance(traiter_parallele, donnees)
```

### 3. Gérez les erreurs proprement

```python
async def worker_robuste(tache):
    """Worker avec gestion d'erreurs"""
    try:
        resultat = await traiter_tache(tache)
        return {'status': 'success', 'resultat': resultat}
    except Exception as e:
        return {'status': 'error', 'erreur': str(e), 'tache': tache}
```

### 4. Utilisez des timeouts

```python
import asyncio

async def avec_timeout(coroutine, timeout=10.0):
    """Ajoute un timeout à une coroutine"""
    try:
        return await asyncio.wait_for(coroutine, timeout=timeout)
    except asyncio.TimeoutError:
        print(f"⏱️  Timeout après {timeout}s")
        return None
```

### 5. Limitez la concurrence

```python
# ✅ Bon - Limiter la concurrence
semaphore = asyncio.Semaphore(10)

async def tache_limitee():
    async with semaphore:
        await traiter()

# ❌ Mauvais - Concurrence illimitée
# Peut créer des milliers de connexions
for i in range(10000):
    asyncio.create_task(traiter())
```

---

## Résumé des patterns

| Pattern | Complexité | Performance | Cas d'usage typique |
|---------|-----------|-------------|-------------------|
| Producer-Consumer | ⭐⭐ | ✅✅ | Découpler production/consommation |
| Worker Pool | ⭐ | ✅✅ | Traiter beaucoup de tâches similaires |
| Pipeline | ⭐⭐⭐ | ✅✅✅ | Traitement en plusieurs étapes |
| Fan-Out/Fan-In | ⭐⭐ | ✅✅✅ | Distribuer et collecter |
| Future/Promise | ⭐ | ✅✅ | Résultats asynchrones |
| Map-Reduce | ⭐⭐ | ✅✅✅ | Traitement de grandes données |
| Actor Model | ⭐⭐⭐ | ✅✅ | Entités avec état isolé |
| Scatter-Gather | ⭐⭐ | ✅✅ | Interroger plusieurs sources |
| Rate Limiting | ⭐⭐ | ✅ | Respecter quotas API |

---

## Points clés à retenir

1. **Choisir le bon pattern** selon le problème spécifique
2. **Commencer simple** puis optimiser si nécessaire
3. **Mesurer les performances** avant et après
4. **Gérer les erreurs** dans tous les workers
5. **Limiter la concurrence** pour éviter les surcharges
6. **Utiliser des timeouts** pour éviter les blocages
7. **Documenter** quel pattern vous utilisez et pourquoi
8. **Combiner les patterns** quand c'est approprié

---

## Ressources et prochaines étapes

**Pour aller plus loin** :
- Explorez `asyncio` pour des patterns asynchrones
- Étudiez `concurrent.futures` pour des abstractions de haut niveau
- Regardez les frameworks : Celery (tâches distribuées), Ray (calcul distribué)
- Apprenez les queues distribuées : RabbitMQ, Redis

**Chapitres liés** :
- 8.1 Threading et Multiprocessing (bases de la concurrence)
- 8.2 Programmation asynchrone avec asyncio
- 8.3 Gestion des verrous et synchronisation

---

## Conclusion

Les patterns de concurrence sont des outils puissants qui, une fois maîtrisés, vous permettront de construire des systèmes performants et robustes. Commencez par les patterns simples comme Worker Pool et Producer-Consumer, puis progressez vers des patterns plus avancés selon vos besoins.

**Règle d'or** : Toujours privilégier la simplicité et la clarté du code, sauf si les mesures de performance justifient l'ajout de complexité.

⏭️ [Gestion des erreurs et débogage](/09-erreurs-et-debogage/README.md)
