🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.4 : Patterns de concurrence

## Introduction

Les patterns de concurrence sont des solutions éprouvées pour résoudre des problèmes récurrents en programmation parallèle. Ces modèles vous aident à structurer vos applications concurrentes de manière efficace et maintenable.

### Analogie simple
Imaginez les patterns comme des **recettes de cuisine éprouvées** :
- **Producer-Consumer** : Une chaîne de production (fabricant → convoyeur → emballeur)
- **Worker Pool** : Une équipe de cuisiniers qui se partagent les commandes
- **Pipeline** : Une chaîne de montage où chaque station a une fonction
- **Map-Reduce** : Diviser une grosse tâche, traiter en parallèle, puis combiner

## Pattern Producer-Consumer

Le pattern le plus fondamental : des producteurs créent des données, des consommateurs les traitent.

### Implementation basique

```python
import threading
import queue
import time
import random

class ProducerConsumer:
    """Implementation du pattern Producer-Consumer."""

    def __init__(self, queue_size=10):
        self.queue = queue.Queue(maxsize=queue_size)
        self.active = True
        self.stats = {
            'produced': 0,
            'consumed': 0,
            'errors': 0
        }
        self.stats_lock = threading.Lock()

    def producer(self, name, items_count, delay_range=(0.1, 0.5)):
        """Produit des éléments à intervalles réguliers."""
        print(f"🏭 {name} démarré (production de {items_count} éléments)")

        for i in range(items_count):
            if not self.active:
                break

            # Créer un élément
            item = {
                'id': f"{name}_{i+1}",
                'data': random.randint(1, 100),
                'timestamp': time.time(),
                'producer': name
            }

            try:
                # Ajouter à la queue (bloque si pleine)
                self.queue.put(item, timeout=2)

                with self.stats_lock:
                    self.stats['produced'] += 1

                print(f"📦 {name}: Produit {item['id']} (data={item['data']})")

                # Délai variable
                time.sleep(random.uniform(*delay_range))

            except queue.Full:
                print(f"⚠️ {name}: Queue pleine, élément perdu")
                with self.stats_lock:
                    self.stats['errors'] += 1

        print(f"✅ {name}: Production terminée")

    def consumer(self, name, processing_time_range=(0.2, 0.8)):
        """Consomme et traite des éléments."""
        print(f"🔄 {name} démarré")

        while self.active:
            try:
                # Récupérer un élément (bloque si vide)
                item = self.queue.get(timeout=1)

                print(f"📥 {name}: Traite {item['id']}")

                # Simuler le traitement
                processing_time = random.uniform(*processing_time_range)
                time.sleep(processing_time)

                # Marquer comme terminé
                self.queue.task_done()

                with self.stats_lock:
                    self.stats['consumed'] += 1

                print(f"✅ {name}: Terminé {item['id']} ({processing_time:.2f}s)")

            except queue.Empty:
                # Timeout, vérifier si on doit continuer
                continue
            except Exception as e:
                print(f"❌ {name}: Erreur - {e}")
                with self.stats_lock:
                    self.stats['errors'] += 1

        print(f"🛑 {name}: Arrêté")

    def run(self, producers_config, consumers_config, duration=10):
        """Lance le système producer-consumer."""
        print("🚀 Démarrage du système Producer-Consumer")
        print(f"Producteurs: {len(producers_config)}, Consommateurs: {len(consumers_config)}")
        print(f"Durée: {duration}s\n")

        threads = []

        # Démarrer les producteurs
        for name, items_count in producers_config:
            t = threading.Thread(target=self.producer, args=(name, items_count))
            t.start()
            threads.append(t)

        # Démarrer les consommateurs
        for name in consumers_config:
            t = threading.Thread(target=self.consumer, args=(name,))
            t.start()
            threads.append(t)

        # Laisser fonctionner
        time.sleep(duration)

        # Arrêter le système
        print("\n🛑 Arrêt du système...")
        self.active = False

        # Attendre les producteurs
        for t in threads[:len(producers_config)]:
            t.join()

        # Vider la queue restante
        try:
            while True:
                self.queue.get_nowait()
                self.queue.task_done()
        except queue.Empty:
            pass

        # Attendre les consommateurs
        for t in threads[len(producers_config):]:
            t.join(timeout=2)

        self.print_stats()

    def print_stats(self):
        """Affiche les statistiques finales."""
        with self.stats_lock:
            stats = self.stats.copy()

        print(f"\n📊 STATISTIQUES FINALES")
        print(f"Produits: {stats['produced']}")
        print(f"Consommés: {stats['consumed']}")
        print(f"Erreurs: {stats['errors']}")
        print(f"Queue restante: {self.queue.qsize()}")

# Test du pattern
def demo_producer_consumer():
    """Démonstration du pattern Producer-Consumer."""
    pc = ProducerConsumer(queue_size=5)

    producers = [("Prod-A", 8), ("Prod-B", 6)]
    consumers = ["Cons-1", "Cons-2", "Cons-3"]

    pc.run(producers, consumers, duration=12)

demo_producer_consumer()
```

## Pattern Worker Pool

Pool de workers qui se partagent les tâches d'une queue commune.

### Worker Pool avec ThreadPoolExecutor

```python
import concurrent.futures
import time
import random

def tache_worker(task_data):
    """Fonction exécutée par un worker."""
    task_id = task_data['id']
    complexity = task_data['complexity']

    print(f"🔄 Worker traite tâche {task_id} (complexité: {complexity})")

    # Simuler le travail (plus c'est complexe, plus c'est long)
    work_time = complexity * random.uniform(0.1, 0.3)
    time.sleep(work_time)

    # Simuler des erreurs occasionnelles
    if random.random() < 0.1:
        raise Exception(f"Erreur simulée pour tâche {task_id}")

    result = {
        'task_id': task_id,
        'result': f"Résultat_{task_id}",
        'work_time': work_time,
        'worker_thread': threading.current_thread().name
    }

    print(f"✅ Tâche {task_id} terminée ({work_time:.2f}s)")
    return result

class WorkerPool:
    """Gestionnaire de pool de workers."""

    def __init__(self, max_workers=4):
        self.max_workers = max_workers

    def process_tasks(self, tasks):
        """Traite une liste de tâches avec le pool."""
        print(f"🏊 Pool de {self.max_workers} workers pour {len(tasks)} tâches")

        results = []
        errors = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Soumettre toutes les tâches
            future_to_task = {
                executor.submit(tache_worker, task): task
                for task in tasks
            }

            # Récupérer les résultats au fur et à mesure
            for future in concurrent.futures.as_completed(future_to_task):
                task = future_to_task[future]

                try:
                    result = future.result()
                    results.append(result)

                except Exception as e:
                    error_info = {
                        'task_id': task['id'],
                        'error': str(e)
                    }
                    errors.append(error_info)
                    print(f"❌ Erreur tâche {task['id']}: {e}")

        return results, errors

    def process_with_timeout(self, tasks, timeout_per_task=5):
        """Traite avec timeout par tâche."""
        print(f"⏰ Pool avec timeout de {timeout_per_task}s par tâche")

        results = []
        errors = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Soumettre toutes les tâches
            futures = [executor.submit(tache_worker, task) for task in tasks]

            # Attendre avec timeout
            for i, future in enumerate(futures):
                try:
                    result = future.result(timeout=timeout_per_task)
                    results.append(result)

                except concurrent.futures.TimeoutError:
                    future.cancel()
                    error_info = {
                        'task_id': tasks[i]['id'],
                        'error': 'Timeout'
                    }
                    errors.append(error_info)
                    print(f"⏰ Timeout tâche {tasks[i]['id']}")

                except Exception as e:
                    error_info = {
                        'task_id': tasks[i]['id'],
                        'error': str(e)
                    }
                    errors.append(error_info)

        return results, errors

def demo_worker_pool():
    """Démonstration du pattern Worker Pool."""
    print("👥 PATTERN WORKER POOL")
    print("-" * 25)

    # Créer des tâches variées
    tasks = [
        {'id': f'task_{i}', 'complexity': random.randint(1, 5)}
        for i in range(1, 13)
    ]

    pool = WorkerPool(max_workers=3)

    start_time = time.time()
    results, errors = pool.process_tasks(tasks)
    total_time = time.time() - start_time

    print(f"\n📊 RÉSULTATS")
    print(f"Tâches réussies: {len(results)}")
    print(f"Erreurs: {len(errors)}")
    print(f"Temps total: {total_time:.2f}s")

    # Afficher qui a fait quoi
    worker_stats = {}
    for result in results:
        worker = result['worker_thread']
        worker_stats[worker] = worker_stats.get(worker, 0) + 1

    print(f"\nRépartition par worker:")
    for worker, count in worker_stats.items():
        print(f"  {worker}: {count} tâches")

demo_worker_pool()
```

## Pattern Pipeline

Traitement en pipeline où chaque étape transforme les données.

### Pipeline de traitement d'images

```python
import threading
import queue
import time
import random

class PipelineStage:
    """Étape générique d'un pipeline."""

    def __init__(self, name, process_func, input_queue=None, output_queue=None):
        self.name = name
        self.process_func = process_func
        self.input_queue = input_queue or queue.Queue()
        self.output_queue = output_queue
        self.active = True
        self.stats = {'processed': 0, 'errors': 0}

    def run(self):
        """Exécute l'étape du pipeline."""
        print(f"🔧 {self.name} démarré")

        while self.active:
            try:
                # Récupérer un élément à traiter
                item = self.input_queue.get(timeout=1)

                if item is None:  # Signal d'arrêt
                    break

                # Traiter l'élément
                print(f"🔄 {self.name}: Traite {item.get('id', 'item')}")

                try:
                    result = self.process_func(item)

                    # Envoyer à l'étape suivante
                    if self.output_queue:
                        self.output_queue.put(result)

                    self.stats['processed'] += 1
                    print(f"✅ {self.name}: Terminé {item.get('id', 'item')}")

                except Exception as e:
                    print(f"❌ {self.name}: Erreur - {e}")
                    self.stats['errors'] += 1

                self.input_queue.task_done()

            except queue.Empty:
                continue

        print(f"🛑 {self.name} arrêté")

class ImagePipeline:
    """Pipeline de traitement d'images."""

    def __init__(self):
        # Queues entre les étapes
        self.queue_load = queue.Queue()
        self.queue_resize = queue.Queue()
        self.queue_filter = queue.Queue()
        self.queue_save = queue.Queue()

        # Étapes du pipeline
        self.stages = [
            PipelineStage("Loader", self.load_image, self.queue_load, self.queue_resize),
            PipelineStage("Resizer", self.resize_image, self.queue_resize, self.queue_filter),
            PipelineStage("Filter", self.apply_filter, self.queue_filter, self.queue_save),
            PipelineStage("Saver", self.save_image, self.queue_save, None)
        ]

        self.threads = []

    def load_image(self, request):
        """Étape 1: Charger l'image."""
        time.sleep(random.uniform(0.1, 0.3))  # Simuler I/O

        return {
            'id': request['id'],
            'filename': request['filename'],
            'data': f"raw_data_{request['id']}",
            'stage': 'loaded'
        }

    def resize_image(self, image):
        """Étape 2: Redimensionner."""
        time.sleep(random.uniform(0.2, 0.4))  # Simuler traitement

        image['data'] = f"resized_{image['data']}"
        image['stage'] = 'resized'
        return image

    def apply_filter(self, image):
        """Étape 3: Appliquer un filtre."""
        time.sleep(random.uniform(0.1, 0.2))  # Simuler traitement

        image['data'] = f"filtered_{image['data']}"
        image['stage'] = 'filtered'
        return image

    def save_image(self, image):
        """Étape 4: Sauvegarder."""
        time.sleep(random.uniform(0.1, 0.3))  # Simuler I/O

        image['data'] = f"saved_{image['data']}"
        image['stage'] = 'saved'
        return image

    def start(self):
        """Démarre le pipeline."""
        print("🚀 Démarrage du pipeline de traitement")

        # Démarrer chaque étape dans son propre thread
        for stage in self.stages:
            thread = threading.Thread(target=stage.run)
            thread.start()
            self.threads.append(thread)

        print("✅ Pipeline démarré")

    def process_images(self, image_requests):
        """Traite une liste de demandes d'images."""
        print(f"📸 Traitement de {len(image_requests)} images")

        # Injecter les demandes dans le pipeline
        for request in image_requests:
            self.queue_load.put(request)

        # Attendre que toutes les images soient chargées
        self.queue_load.join()

        # Attendre que toutes les étapes suivantes se terminent
        for queue in [self.queue_resize, self.queue_filter, self.queue_save]:
            queue.join()

    def stop(self):
        """Arrête le pipeline."""
        print("🛑 Arrêt du pipeline...")

        # Envoyer signal d'arrêt à chaque étape
        for stage in self.stages:
            stage.active = False
            stage.input_queue.put(None)  # Signal d'arrêt

        # Attendre la fin des threads
        for thread in self.threads:
            thread.join(timeout=2)

        self.print_stats()

    def print_stats(self):
        """Affiche les statistiques du pipeline."""
        print(f"\n📊 STATISTIQUES DU PIPELINE")
        for stage in self.stages:
            print(f"{stage.name}: {stage.stats['processed']} traités, {stage.stats['errors']} erreurs")

def demo_pipeline():
    """Démonstration du pattern Pipeline."""
    print("🏭 PATTERN PIPELINE")
    print("-" * 20)

    # Créer des demandes d'images
    image_requests = [
        {'id': f'img_{i}', 'filename': f'photo_{i}.jpg'}
        for i in range(1, 9)
    ]

    pipeline = ImagePipeline()

    try:
        pipeline.start()
        time.sleep(1)  # Laisser le pipeline se stabiliser

        start_time = time.time()
        pipeline.process_images(image_requests)
        total_time = time.time() - start_time

        print(f"\n⏱️ Traitement terminé en {total_time:.2f}s")

    finally:
        pipeline.stop()

demo_pipeline()
```

## Pattern Map-Reduce

Diviser une tâche en sous-tâches, les traiter en parallèle, puis combiner les résultats.

### Map-Reduce pour analyse de texte

```python
import concurrent.futures
import time
import random
from collections import defaultdict, Counter
import re

class MapReduce:
    """Implémentation générique du pattern Map-Reduce."""

    def __init__(self, max_workers=4):
        self.max_workers = max_workers

    def map_phase(self, data_chunks, map_func):
        """Phase Map: traite les chunks en parallèle."""
        print(f"🗺️ Phase MAP: {len(data_chunks)} chunks avec {self.max_workers} workers")

        map_results = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            # Soumettre tous les chunks
            futures = [executor.submit(map_func, chunk) for chunk in data_chunks]

            # Récupérer les résultats
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                try:
                    result = future.result()
                    map_results.append(result)
                    print(f"✅ Chunk {i+1} traité")
                except Exception as e:
                    print(f"❌ Erreur chunk {i+1}: {e}")

        return map_results

    def reduce_phase(self, map_results, reduce_func):
        """Phase Reduce: combine les résultats."""
        print(f"🔄 Phase REDUCE: Combinaison de {len(map_results)} résultats")

        if not map_results:
            return None

        # Réduction séquentielle (peut être parallélisée pour de gros volumes)
        result = map_results[0]
        for other_result in map_results[1:]:
            result = reduce_func(result, other_result)

        return result

    def execute(self, data, chunk_size, map_func, reduce_func):
        """Exécute le processus Map-Reduce complet."""
        print(f"🚀 DÉBUT MAP-REDUCE")
        print(f"Données: {len(data)} éléments, chunks de {chunk_size}")

        start_time = time.time()

        # 1. Diviser les données en chunks
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        print(f"📦 {len(chunks)} chunks créés")

        # 2. Phase Map
        map_results = self.map_phase(chunks, map_func)

        # 3. Phase Reduce
        final_result = self.reduce_phase(map_results, reduce_func)

        total_time = time.time() - start_time
        print(f"⏱️ Map-Reduce terminé en {total_time:.2f}s")

        return final_result

# Fonctions pour l'analyse de texte
def map_word_count(text_chunk):
    """Fonction Map: compte les mots dans un chunk de texte."""
    word_count = defaultdict(int)

    for line in text_chunk:
        # Nettoyer et diviser en mots
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_count[word] += 1

    return dict(word_count)

def reduce_word_count(count1, count2):
    """Fonction Reduce: combine deux dictionnaires de comptage."""
    result = defaultdict(int)

    # Additionner les comptages
    for word, count in count1.items():
        result[word] += count

    for word, count in count2.items():
        result[word] += count

    return dict(result)

def demo_map_reduce():
    """Démonstration du pattern Map-Reduce."""
    print("🌍 PATTERN MAP-REDUCE")
    print("-" * 25)

    # Créer un corpus de texte d'exemple
    sample_texts = [
        "Python est un langage de programmation puissant et facile à apprendre.",
        "La programmation concurrente améliore les performances des applications.",
        "Les patterns de concurrence sont des solutions éprouvées et efficaces.",
        "Python offre plusieurs outils pour la programmation parallèle et asynchrone.",
        "Map-Reduce est un pattern populaire pour traiter de gros volumes de données.",
        "Les threads et les processus permettent d'exécuter du code en parallèle.",
        "La synchronisation est cruciale pour éviter les conditions de course.",
        "Les queues facilitent la communication entre threads et processus.",
    ] * 100  # Multiplier pour avoir plus de données

    # Ajouter du bruit pour rendre plus réaliste
    for i in range(200):
        words = ["données", "traitement", "performance", "code", "système", "application"]
        sample_texts.append(" ".join(random.choices(words, k=random.randint(3, 8))))

    print(f"📖 Corpus: {len(sample_texts)} lignes de texte")

    # Exécuter Map-Reduce
    mr = MapReduce(max_workers=3)
    word_counts = mr.execute(
        data=sample_texts,
        chunk_size=100,
        map_func=map_word_count,
        reduce_func=reduce_word_count
    )

    # Analyser les résultats
    if word_counts:
        total_words = sum(word_counts.values())
        unique_words = len(word_counts)

        print(f"\n📊 RÉSULTATS D'ANALYSE")
        print(f"Mots uniques: {unique_words}")
        print(f"Total des mots: {total_words}")

        # Top 10 des mots les plus fréquents
        top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"\nTop 10 des mots:")
        for word, count in top_words:
            print(f"  {word}: {count}")

if __name__ == "__main__":
    demo_map_reduce()
```

## Pattern Circuit Breaker

Protection contre les défaillances en cascade en "coupant le circuit" quand un service est défaillant.

### Circuit Breaker pour services externes

```python
import threading
import time
import random
from enum import Enum
from datetime import datetime, timedelta

class CircuitState(Enum):
    CLOSED = "closed"      # Normal: requêtes passent
    OPEN = "open"          # Défaillant: requêtes bloquées
    HALF_OPEN = "half_open"  # Test: quelques requêtes passent

class CircuitBreaker:
    """Implémentation du pattern Circuit Breaker."""

    def __init__(self, failure_threshold=5, timeout=60, expected_exception=Exception):
        self.failure_threshold = failure_threshold  # Seuil d'échecs
        self.timeout = timeout  # Temps avant retry (secondes)
        self.expected_exception = expected_exception

        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

        self.lock = threading.Lock()
        self.stats = {
            'total_calls': 0,
            'successful_calls': 0,
            'failed_calls': 0,
            'circuit_open_calls': 0
        }

    def call(self, func, *args, **kwargs):
        """Exécute une fonction protégée par le circuit breaker."""
        with self.lock:
            self.stats['total_calls'] += 1

            # Vérifier l'état du circuit
            if self.state == CircuitState.OPEN:
                if self._should_attempt_reset():
                    self.state = CircuitState.HALF_OPEN
                    print(f"🔄 Circuit HALF-OPEN: Test de récupération")
                else:
                    self.stats['circuit_open_calls'] += 1
                    print(f"⚡ Circuit OPEN: Appel bloqué")
                    raise Exception("Circuit breaker OPEN")

            # Tenter l'appel
            try:
                result = func(*args, **kwargs)
                self._on_success()
                return result

            except self.expected_exception as e:
                self._on_failure()
                raise e

    def _should_attempt_reset(self):
        """Vérifie si on peut tenter de réinitialiser le circuit."""
        if self.last_failure_time is None:
            return True

        return datetime.now() - self.last_failure_time > timedelta(seconds=self.timeout)

    def _on_success(self):
        """Appelé lors d'un succès."""
        self.stats['successful_calls'] += 1

        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            self.failure_count = 0
            print(f"✅ Circuit CLOSED: Service récupéré")

    def _on_failure(self):
        """Appelé lors d'un échec."""
        self.stats['failed_calls'] += 1
        self.failure_count += 1
        self.last_failure_time = datetime.now()

        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            print(f"⚡ Circuit OPEN: Trop d'échecs ({self.failure_count})")

    def get_stats(self):
        """Retourne les statistiques."""
        with self.lock:
            stats = self.stats.copy()
            stats['state'] = self.state.value
            stats['failure_count'] = self.failure_count
            return stats

class ServiceExterne:
    """Simule un service externe instable."""

    def __init__(self, nom, taux_echec=0.3):
        self.nom = nom
        self.taux_echec = taux_echec
        self.appels = 0

    def appeler_api(self, donnees):
        """Simule un appel API qui peut échouer."""
        self.appels += 1

        # Simuler latence réseau
        time.sleep(random.uniform(0.1, 0.3))

        # Simuler des échecs
        if random.random() < self.taux_echec:
            raise Exception(f"{self.nom}: Service temporairement indisponible")

        return f"{self.nom}: Données traitées - {donnees}"

def demo_circuit_breaker():
    """Démonstration du pattern Circuit Breaker."""
    print("⚡ PATTERN CIRCUIT BREAKER")
    print("-" * 30)

    # Créer un service instable
    service = ServiceExterne("API-Externe", taux_echec=0.4)

    # Créer un circuit breaker
    circuit = CircuitBreaker(
        failure_threshold=3,
        timeout=5,
        expected_exception=Exception
    )

    # Simuler des appels clients
    def client_worker(nom_client, nb_appels):
        """Simule un client qui fait des appels."""
        print(f"👤 {nom_client} démarré")

        for i in range(nb_appels):
            try:
                donnees = f"requete_{nom_client}_{i+1}"
                result = circuit.call(service.appeler_api, donnees)
                print(f"✅ {nom_client}: {result}")

            except Exception as e:
                print(f"❌ {nom_client}: {e}")

            time.sleep(random.uniform(0.5, 1.5))

        print(f"🏁 {nom_client} terminé")

   # Lancer plusieurs clients
    clients = ["Client-A", "Client-B", "Client-C"]
    threads = []

    for client in clients:
        t = threading.Thread(target=client_worker, args=(client, 8))
        t.start()
        threads.append(t)

    # Attendre la fin
    for t in threads:
        t.join()

    # Afficher les statistiques finales
    stats = circuit.get_stats()
    print(f"\n📊 STATISTIQUES CIRCUIT BREAKER")
    print(f"État final: {stats['state'].upper()}")
    print(f"Appels totaux: {stats['total_calls']}")
    print(f"Succès: {stats['successful_calls']}")
    print(f"Échecs: {stats['failed_calls']}")
    print(f"Bloqués (circuit ouvert): {stats['circuit_open_calls']}")
    print(f"Taux de succès: {stats['successful_calls']/stats['total_calls']*100:.1f}%")

demo_circuit_breaker()
```

## Pattern Scatter-Gather

Diffuser une requête vers plusieurs services, puis rassembler les réponses.

### Scatter-Gather pour recherche distribuée

```python
import concurrent.futures
import time
import random
import threading

class SearchService:
    """Service de recherche simulé."""

    def __init__(self, name, latency_range=(0.1, 1.0), error_rate=0.1):
        self.name = name
        self.latency_range = latency_range
        self.error_rate = error_rate

    def search(self, query):
        """Effectue une recherche."""
        # Simuler latence variable
        time.sleep(random.uniform(*self.latency_range))

        # Simuler des erreurs occasionnelles
        if random.random() < self.error_rate:
            raise Exception(f"{self.name}: Service temporairement indisponible")

        # Générer des résultats simulés
        results = []
        num_results = random.randint(0, 5)

        for i in range(num_results):
            results.append({
                'title': f"Résultat {i+1} pour '{query}'",
                'url': f"https://{self.name.lower()}.com/result_{i+1}",
                'score': random.uniform(0.1, 1.0),
                'source': self.name
            })

        return {
            'service': self.name,
            'query': query,
            'results': results,
            'count': len(results)
        }

class ScatterGather:
    """Implémentation du pattern Scatter-Gather."""

    def __init__(self, services, timeout=3.0):
        self.services = services
        self.timeout = timeout

    def search_all(self, query, min_responses=1):
        """Lance une recherche sur tous les services."""
        print(f"🔍 Recherche '{query}' sur {len(self.services)} services")

        start_time = time.time()
        results = []
        errors = []

        # Phase Scatter: lancer toutes les requêtes en parallèle
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.services)) as executor:
            # Soumettre toutes les recherches
            future_to_service = {
                executor.submit(service.search, query): service
                for service in self.services
            }

            # Phase Gather: collecter les réponses
            completed = 0
            for future in concurrent.futures.as_completed(future_to_service, timeout=self.timeout):
                service = future_to_service[future]

                try:
                    result = future.result()
                    results.append(result)
                    completed += 1

                    print(f"✅ {service.name}: {result['count']} résultats "
                          f"({time.time() - start_time:.2f}s)")

                    # Arrêter dès qu'on a assez de réponses (optionnel)
                    if completed >= min_responses and len(results) >= len(self.services) // 2:
                        break

                except Exception as e:
                    errors.append({
                        'service': service.name,
                        'error': str(e)
                    })
                    print(f"❌ {service.name}: {e}")

        total_time = time.time() - start_time

        return {
            'query': query,
            'results': results,
            'errors': errors,
            'total_time': total_time,
            'services_responded': len(results),
            'services_failed': len(errors)
        }

    def aggregate_results(self, search_response):
        """Agrège et trie les résultats de tous les services."""
        all_results = []

        # Collecter tous les résultats
        for service_response in search_response['results']:
            for result in service_response['results']:
                all_results.append(result)

        # Trier par score décroissant
        all_results.sort(key=lambda x: x['score'], reverse=True)

        return {
            'query': search_response['query'],
            'total_results': len(all_results),
            'results': all_results[:10],  # Top 10
            'services_used': len(search_response['results']),
            'response_time': search_response['total_time']
        }

def demo_scatter_gather():
    """Démonstration du pattern Scatter-Gather."""
    print("📡 PATTERN SCATTER-GATHER")
    print("-" * 30)

    # Créer plusieurs services de recherche avec caractéristiques différentes
    services = [
        SearchService("GoogleSearch", latency_range=(0.1, 0.3), error_rate=0.05),
        SearchService("BingSearch", latency_range=(0.2, 0.5), error_rate=0.1),
        SearchService("DuckDuckGo", latency_range=(0.3, 0.8), error_rate=0.15),
        SearchService("YahooSearch", latency_range=(0.4, 1.2), error_rate=0.2),
        SearchService("LocalSearch", latency_range=(0.1, 0.2), error_rate=0.3)
    ]

    scatter_gather = ScatterGather(services, timeout=2.0)

    # Effectuer plusieurs recherches
    queries = ["python concurrence", "machine learning", "web development"]

    for query in queries:
        print(f"\n{'='*50}")

        # Recherche distribuée
        search_response = scatter_gather.search_all(query, min_responses=2)

        # Agrégation des résultats
        aggregated = scatter_gather.aggregate_results(search_response)

        print(f"\n📊 RÉSULTATS POUR '{query}'")
        print(f"Services répondus: {search_response['services_responded']}/{len(services)}")
        print(f"Temps de réponse: {search_response['total_time']:.2f}s")
        print(f"Total résultats: {aggregated['total_results']}")

        if aggregated['results']:
            print(f"\nTop 3 résultats:")
            for i, result in enumerate(aggregated['results'][:3], 1):
                print(f"  {i}. {result['title']} (score: {result['score']:.2f}) - {result['source']}")

        if search_response['errors']:
            print(f"\nErreurs:")
            for error in search_response['errors']:
                print(f"  ❌ {error['service']}: {error['error']}")

        time.sleep(1)  # Pause entre les recherches

demo_scatter_gather()
```

## Exercices pratiques intégrés

### Exercice 1 : Système de cache distribué

```python
import threading
import time
import random
import hashlib
from collections import defaultdict

class DistributedCache:
    """Cache distribué utilisant plusieurs patterns."""

    def __init__(self, num_shards=3, max_size_per_shard=100):
        self.num_shards = num_shards
        self.max_size_per_shard = max_size_per_shard

        # Shards du cache (pattern partitioning)
        self.shards = [
            {'data': {}, 'lock': threading.RLock(), 'access_count': 0}
            for _ in range(num_shards)
        ]

        # Pool de workers pour les opérations asynchrones
        self.task_queue = queue.Queue()
        self.workers = []
        self.active = True

        # Statistiques globales
        self.global_stats = {
            'hits': 0,
            'misses': 0,
            'sets': 0,
            'evictions': 0
        }
        self.stats_lock = threading.Lock()

    def _hash_key(self, key):
        """Hash une clé pour déterminer le shard."""
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % self.num_shards

    def _get_shard(self, key):
        """Retourne le shard approprié pour une clé."""
        shard_id = self._hash_key(key)
        return self.shards[shard_id], shard_id

    def get(self, key):
        """Récupère une valeur du cache."""
        shard, shard_id = self._get_shard(key)

        with shard['lock']:
            shard['access_count'] += 1

            if key in shard['data']:
                entry = shard['data'][key]

                # Vérifier l'expiration
                if entry['expires_at'] > time.time():
                    with self.stats_lock:
                        self.global_stats['hits'] += 1

                    print(f"💾 Cache HIT: {key} (shard {shard_id})")
                    return entry['value']
                else:
                    # Expiré, supprimer
                    del shard['data'][key]

            with self.stats_lock:
                self.global_stats['misses'] += 1

            print(f"❌ Cache MISS: {key} (shard {shard_id})")
            return None

    def set(self, key, value, ttl=300):
        """Stocke une valeur dans le cache."""
        shard, shard_id = self._get_shard(key)

        with shard['lock']:
            # Éviction si nécessaire
            if len(shard['data']) >= self.max_size_per_shard and key not in shard['data']:
                self._evict_lru(shard)

            # Stocker la valeur
            shard['data'][key] = {
                'value': value,
                'expires_at': time.time() + ttl,
                'created_at': time.time()
            }

            with self.stats_lock:
                self.global_stats['sets'] += 1

            print(f"💾 Cache SET: {key} (shard {shard_id}, TTL: {ttl}s)")

    def _evict_lru(self, shard):
        """Évicte l'élément le moins récemment utilisé."""
        if not shard['data']:
            return

        # Trouver l'entrée la plus ancienne
        oldest_key = min(shard['data'].keys(),
                        key=lambda k: shard['data'][k]['created_at'])

        del shard['data'][oldest_key]

        with self.stats_lock:
            self.global_stats['evictions'] += 1

        print(f"🗑️ Éviction LRU: {oldest_key}")

    def start_background_workers(self, num_workers=2):
        """Démarre les workers pour les tâches de maintenance."""
        for i in range(num_workers):
            worker = threading.Thread(
                target=self._background_worker,
                args=(f"Worker-{i+1}",)
            )
            worker.start()
            self.workers.append(worker)

        print(f"🔧 {num_workers} workers de maintenance démarrés")

    def _background_worker(self, name):
        """Worker qui nettoie les entrées expirées."""
        while self.active:
            try:
                # Nettoyer périodiquement
                time.sleep(5)
                self._cleanup_expired()

            except Exception as e:
                print(f"❌ {name}: Erreur - {e}")

    def _cleanup_expired(self):
        """Nettoie les entrées expirées."""
        now = time.time()
        total_cleaned = 0

        for shard_id, shard in enumerate(self.shards):
            with shard['lock']:
                expired_keys = [
                    key for key, entry in shard['data'].items()
                    if entry['expires_at'] <= now
                ]

                for key in expired_keys:
                    del shard['data'][key]
                    total_cleaned += 1

        if total_cleaned > 0:
            print(f"🧹 Nettoyage: {total_cleaned} entrées expirées supprimées")

    def get_stats(self):
        """Retourne les statistiques du cache."""
        with self.stats_lock:
            stats = self.global_stats.copy()

        # Ajouter les stats par shard
        shard_stats = []
        for i, shard in enumerate(self.shards):
            with shard['lock']:
                shard_stats.append({
                    'shard_id': i,
                    'size': len(shard['data']),
                    'access_count': shard['access_count']
                })

        stats['shards'] = shard_stats
        stats['total_size'] = sum(s['size'] for s in shard_stats)

        return stats

    def stop(self):
        """Arrête le cache et ses workers."""
        self.active = False

        for worker in self.workers:
            worker.join(timeout=1)

        print("🛑 Cache arrêté")

def demo_distributed_cache():
    """Test du cache distribué."""
    print("🗄️ CACHE DISTRIBUÉ")
    print("-" * 20)

    cache = DistributedCache(num_shards=3, max_size_per_shard=5)
    cache.start_background_workers(2)

    def cache_user(name, operations):
        """Simule un utilisateur du cache."""
        for i in range(operations):
            # 70% lecture, 30% écriture
            if random.random() < 0.7:
                # Lecture
                key = f"key_{random.randint(1, 10)}"
                value = cache.get(key)
            else:
                # Écriture
                key = f"key_{random.randint(1, 15)}"
                value = f"value_{name}_{i}"
                ttl = random.randint(5, 20)
                cache.set(key, value, ttl)

            time.sleep(random.uniform(0.1, 0.3))

    # Lancer plusieurs utilisateurs
    users = ["User-A", "User-B", "User-C"]
    threads = []

    for user in users:
        t = threading.Thread(target=cache_user, args=(user, 12))
        t.start()
        threads.append(t)

    # Attendre et afficher les stats périodiquement
    for i in range(3):
        time.sleep(4)
        stats = cache.get_stats()

        print(f"\n📊 STATS après {(i+1)*4}s:")
        print(f"Hits/Misses: {stats['hits']}/{stats['misses']}")
        print(f"Sets/Evictions: {stats['sets']}/{stats['evictions']}")
        print(f"Taille totale: {stats['total_size']}")

        for shard in stats['shards']:
            print(f"  Shard {shard['shard_id']}: {shard['size']} entrées, {shard['access_count']} accès")

    # Attendre la fin
    for t in threads:
        t.join()

    cache.stop()

demo_distributed_cache()
```

### Exercice 2 : Orchestrateur de tâches

```python
import threading
import queue
import time
import random
from enum import Enum
from dataclasses import dataclass
from typing import List, Callable, Any

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    """Représente une tâche dans l'orchestrateur."""
    id: str
    func: Callable
    args: tuple = ()
    kwargs: dict = None
    dependencies: List[str] = None
    priority: int = 0
    timeout: float = 30.0
    retry_count: int = 0
    max_retries: int = 2

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}
        if self.dependencies is None:
            self.dependencies = []

class TaskOrchestrator:
    """Orchestrateur de tâches avec gestion des dépendances."""

    def __init__(self, max_workers=4):
        self.max_workers = max_workers
        self.tasks = {}  # task_id -> Task
        self.task_status = {}  # task_id -> TaskStatus
        self.task_results = {}  # task_id -> result
        self.ready_queue = queue.PriorityQueue()

        self.workers = []
        self.active = False
        self.lock = threading.RLock()

        # Événements pour notification
        self.task_completed_event = threading.Event()

    def add_task(self, task: Task):
        """Ajoute une tâche à l'orchestrateur."""
        with self.lock:
            self.tasks[task.id] = task
            self.task_status[task.id] = TaskStatus.PENDING

            print(f"📋 Tâche ajoutée: {task.id} (priorité: {task.priority})")

            # Vérifier si la tâche peut être exécutée immédiatement
            self._check_ready_tasks()

    def _check_ready_tasks(self):
        """Vérifie quelles tâches peuvent être exécutées."""
        for task_id, task in self.tasks.items():
            if self.task_status[task_id] == TaskStatus.PENDING:
                if self._dependencies_satisfied(task):
                    # Ajouter à la queue de priorité (négatif pour ordre décroissant)
                    self.ready_queue.put((-task.priority, task_id))
                    self.task_status[task_id] = TaskStatus.PENDING
                    print(f"✅ Tâche prête: {task_id}")

    def _dependencies_satisfied(self, task: Task) -> bool:
        """Vérifie si toutes les dépendances sont satisfaites."""
        for dep_id in task.dependencies:
            if dep_id not in self.task_status:
                return False
            if self.task_status[dep_id] != TaskStatus.COMPLETED:
                return False
        return True

    def start(self):
        """Démarre l'orchestrateur."""
        if self.active:
            return

        print(f"🚀 Démarrage orchestrateur ({self.max_workers} workers)")
        self.active = True

        # Démarrer les workers
        for i in range(self.max_workers):
            worker = threading.Thread(target=self._worker, args=(f"Worker-{i+1}",))
            worker.start()
            self.workers.append(worker)

        # Thread de monitoring des dépendances
        monitor = threading.Thread(target=self._dependency_monitor)
        monitor.start()
        self.workers.append(monitor)

    def _worker(self, name):
        """Worker qui exécute les tâches."""
        print(f"👷 {name} démarré")

        while self.active:
            try:
                # Prendre une tâche (timeout pour vérifier l'arrêt)
                try:
                    priority, task_id = self.ready_queue.get(timeout=1)
                except queue.Empty:
                    continue

                # Exécuter la tâche
                self._execute_task(task_id, name)
                self.ready_queue.task_done()

            except Exception as e:
                print(f"❌ {name}: Erreur - {e}")

        print(f"🛑 {name} arrêté")

    def _execute_task(self, task_id, worker_name):
        """Exécute une tâche spécifique."""
        with self.lock:
            if self.task_status[task_id] != TaskStatus.PENDING:
                return  # Tâche déjà prise par un autre worker

            self.task_status[task_id] = TaskStatus.RUNNING
            task = self.tasks[task_id]

        print(f"🔄 {worker_name}: Exécute {task_id}")

        try:
            # Préparer les arguments avec les résultats des dépendances
            kwargs = task.kwargs.copy()

            # Ajouter les résultats des dépendances
            for dep_id in task.dependencies:
                if dep_id in self.task_results:
                    kwargs[f"dep_{dep_id}"] = self.task_results[dep_id]

            # Exécuter avec timeout
            start_time = time.time()
            result = task.func(*task.args, **kwargs)
            execution_time = time.time() - start_time

            # Marquer comme terminée
            with self.lock:
                self.task_status[task_id] = TaskStatus.COMPLETED
                self.task_results[task_id] = result

            print(f"✅ {worker_name}: {task_id} terminée ({execution_time:.2f}s)")

            # Notifier que des tâches peuvent être débloquées
            self.task_completed_event.set()

        except Exception as e:
            print(f"❌ {worker_name}: {task_id} échouée - {e}")

            # Gestion des retry
            task.retry_count += 1
            if task.retry_count <= task.max_retries:
                print(f"🔄 {task_id}: Retry {task.retry_count}/{task.max_retries}")
                with self.lock:
                    self.task_status[task_id] = TaskStatus.PENDING
                    self.ready_queue.put((-task.priority, task_id))
            else:
                with self.lock:
                    self.task_status[task_id] = TaskStatus.FAILED
                print(f"💥 {task_id}: Échec définitif après {task.max_retries} tentatives")

    def _dependency_monitor(self):
        """Monitore les changements pour débloquer de nouvelles tâches."""
        while self.active:
            self.task_completed_event.wait(timeout=1)
            self.task_completed_event.clear()

            # Vérifier s'il y a de nouvelles tâches à débloquer
            with self.lock:
                self._check_ready_tasks()

    def wait_all(self, timeout=None):
        """Attend que toutes les tâches se terminent."""
        start_time = time.time()

        while self.active:
            with self.lock:
                pending = sum(1 for status in self.task_status.values()
                            if status in [TaskStatus.PENDING, TaskStatus.RUNNING])

                if pending == 0:
                    break

            if timeout and (time.time() - start_time) > timeout:
                print("⏰ Timeout atteint")
                break

            time.sleep(0.5)

        self.stop()

    def stop(self):
        """Arrête l'orchestrateur."""
        print("🛑 Arrêt de l'orchestrateur...")
        self.active = False

        for worker in self.workers:
            worker.join(timeout=2)

        self.print_summary()

    def print_summary(self):
        """Affiche un résumé de l'exécution."""
        with self.lock:
            status_counts = {}
            for status in self.task_status.values():
                status_counts[status] = status_counts.get(status, 0) + 1

        print(f"\n📊 RÉSUMÉ DE L'ORCHESTRATION")
        print(f"Total tâches: {len(self.tasks)}")
        for status, count in status_counts.items():
            print(f"{status.value}: {count}")

# Fonctions de test pour l'orchestrateur
def task_a():
    """Tâche A - Pas de dépendances."""
    time.sleep(random.uniform(1, 2))
    return "Résultat de A"

def task_b():
    """Tâche B - Pas de dépendances."""
    time.sleep(random.uniform(0.5, 1.5))
    return "Résultat de B"

def task_c(dep_task_a, dep_task_b):
    """Tâche C - Dépend de A et B."""
    time.sleep(random.uniform(0.8, 1.2))
    return f"Résultat de C (utilise {dep_task_a} et {dep_task_b})"

def task_d(dep_task_c):
    """Tâche D - Dépend de C."""
    time.sleep(random.uniform(0.3, 0.8))

    # Simuler un échec occasionnel
    if random.random() < 0.3:
        raise Exception("Échec simulé de la tâche D")

    return f"Résultat de D (utilise {dep_task_c})"

def demo_task_orchestrator():
    """Démonstration de l'orchestrateur de tâches."""
    print("🎭 ORCHESTRATEUR DE TÂCHES")
    print("-" * 30)

    orchestrator = TaskOrchestrator(max_workers=2)

    # Définir les tâches avec dépendances
    tasks = [
        Task("task_a", task_a, priority=1),
        Task("task_b", task_b, priority=1),
        Task("task_c", task_c, dependencies=["task_a", "task_b"], priority=2),
        Task("task_d", task_d, dependencies=["task_c"], priority=3, max_retries=3),
        Task("task_e", lambda: "Résultat E", priority=1),  # Tâche indépendante
    ]

    # Démarrer l'orchestrateur
    orchestrator.start()

    # Ajouter les tâches
    for task in tasks:
        orchestrator.add_task(task)
        time.sleep(0.2)  # Petit délai pour voir l'ordre

    # Attendre la fin
    orchestrator.wait_all(timeout=30)

demo_task_orchestrator()
```

## Récapitulatif des patterns

### Tableau de comparaison

| Pattern | Usage principal | Avantages | Inconvénients |
|---------|-----------------|-----------|---------------|
| **Producer-Consumer** | Communication async | Découplage, gestion de charge | Complexité de synchronisation |
| **Worker Pool** | Traitement parallèle | Utilisation optimale des ressources | Pas de dépendances entre tâches |
| **Pipeline** | Traitement séquentiel | Débit élevé, spécialisation | Séquentiel, point de bottleneck |
| **Map-Reduce** | Gros volumes de données | Scalabilité horizontale | Overhead de coordination |
| **Circuit Breaker** | Résilience des services | Protection contre les cascades | Faux positifs possibles |
| **Scatter-Gather** | Recherche distribuée | Latence réduite, redondance | Complexité de gestion |

### Conseils de choix

```python
# ✅ Producer-Consumer : Communication asynchrone
if "communication" in requirements and "découplage" in requirements:
    use_producer_consumer()

# ✅ Worker Pool : Tâches indépendantes parallèles
if "parallélisme" in requirements and "tâches_indépendantes" in requirements:
    use_worker_pool()

# ✅ Pipeline : Traitement en étapes
if "étapes_séquentielles" in requirements and "débit" in requirements:
    use_pipeline()

# ✅ Map-Reduce : Gros volumes de données
if "big_data" in requirements and "calcul_distribué" in requirements:
    use_map_reduce()
```

## Bonnes pratiques générales

### **1. Choisir le bon pattern**
```python
# Analyser le problème avant de choisir
- Type de données (flux vs batch)
- Dépendances entre tâches
- Contraintes de performance
- Niveau de parallélisme souhaité
```

### **2. Monitoring et observabilité**
```python
# Toujours inclure des métriques
class PatternWithMetrics:
    def __init__(self):
        self.metrics = {
            'processed': 0,
            'errors': 0,
            'avg_time': 0
        }

    def track_operation(self, duration, success):
        self.metrics['processed'] += 1
        if not success:
            self.metrics['errors'] += 1
```

### **3. Gestion d'erreurs robuste**
```python
# Gérer les pannes gracieusement
try:
    result = process_task(task)
except RecoverableError:
    retry_task(task)
except FatalError:
    mark_failed(task)
    notify_admin()
```

### **4. Timeouts et annulation**
```python
# Toujours inclure des timeouts
import signal
from contextlib import contextmanager

@contextmanager
def timeout(seconds):
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Opération dépassée ({seconds}s)")

    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

# Usage
try:
    with timeout(30):
        result = long_running_operation()
except TimeoutError:
    print("Opération annulée (timeout)")
```

### **5. Backpressure et contrôle de flux**
```python
# Éviter la surcharge avec backpressure
class BackpressureQueue:
    def __init__(self, maxsize, backpressure_threshold=0.8):
        self.queue = queue.Queue(maxsize)
        self.threshold = int(maxsize * backpressure_threshold)

    def put(self, item, timeout=None):
        if self.queue.qsize() > self.threshold:
            print("⚠️ Backpressure activée - ralentissement")
            time.sleep(0.1)  # Ralentir le producteur

        return self.queue.put(item, timeout=timeout)
```

## Projet final : Système de traitement de données distribué

Créons un système complet qui combine tous les patterns appris.

### Architecture du système

```python
import threading
import queue
import time
import random
import json
import logging
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Callable
import concurrent.futures

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class JobType(Enum):
    DATA_INGESTION = "data_ingestion"
    DATA_PROCESSING = "data_processing"
    DATA_ANALYSIS = "data_analysis"
    REPORT_GENERATION = "report_generation"

class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class Job:
    """Représente un job de traitement."""
    id: str
    type: JobType
    data: Dict[str, Any]
    priority: int = 0
    dependencies: List[str] = None
    timeout: float = 60.0
    max_retries: int = 2
    created_at: float = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.created_at is None:
            self.created_at = time.time()

class DistributedDataProcessor:
    """Système de traitement de données distribué."""

    def __init__(self,
                 ingestion_workers=2,
                 processing_workers=3,
                 analysis_workers=2,
                 report_workers=1):

        self.logger = logging.getLogger(self.__class__.__name__)

        # Configuration des workers par type
        self.worker_config = {
            JobType.DATA_INGESTION: ingestion_workers,
            JobType.DATA_PROCESSING: processing_workers,
            JobType.DATA_ANALYSIS: analysis_workers,
            JobType.REPORT_GENERATION: report_workers
        }

        # Queues spécialisées pour chaque type de job
        self.job_queues = {
            job_type: queue.PriorityQueue()
            for job_type in JobType
        }

        # État global du système
        self.jobs = {}  # job_id -> Job
        self.job_status = {}  # job_id -> JobStatus
        self.job_results = {}  # job_id -> result
        self.job_errors = {}  # job_id -> error_info

        # Workers par type
        self.workers = {job_type: [] for job_type in JobType}
        self.active = False

        # Synchronisation
        self.lock = threading.RLock()
        self.job_completed_event = threading.Event()

        # Statistiques
        self.stats = {
            'jobs_submitted': 0,
            'jobs_completed': 0,
            'jobs_failed': 0,
            'total_processing_time': 0
        }

        # Circuit breakers pour chaque type de job
        self.circuit_breakers = {
            job_type: CircuitBreaker(failure_threshold=3, timeout=30)
            for job_type in JobType
        }

    def submit_job(self, job: Job) -> bool:
        """Soumet un job pour traitement."""
        with self.lock:
            # Vérifier les dépendances
            for dep_id in job.dependencies:
                if dep_id not in self.jobs:
                    self.logger.error(f"Dépendance manquante pour {job.id}: {dep_id}")
                    return False

            # Enregistrer le job
            self.jobs[job.id] = job
            self.job_status[job.id] = JobStatus.PENDING
            self.stats['jobs_submitted'] += 1

            self.logger.info(f"Job soumis: {job.id} ({job.type.value})")

            # Vérifier si le job peut être exécuté immédiatement
            self._check_ready_jobs()

            return True

    def _check_ready_jobs(self):
        """Vérifie quels jobs peuvent être exécutés."""
        for job_id, job in self.jobs.items():
            if self.job_status[job_id] == JobStatus.PENDING:
                if self._dependencies_satisfied(job):
                    # Ajouter à la queue appropriée
                    priority_item = (-job.priority, time.time(), job_id)
                    self.job_queues[job.type].put(priority_item)
                    self.logger.info(f"Job prêt: {job_id}")

    def _dependencies_satisfied(self, job: Job) -> bool:
        """Vérifie si toutes les dépendances sont satisfaites."""
        for dep_id in job.dependencies:
            if (dep_id not in self.job_status or
                self.job_status[dep_id] != JobStatus.COMPLETED):
                return False
        return True

    def start(self):
        """Démarre le système de traitement."""
        if self.active:
            self.logger.warning("Système déjà démarré")
            return

        self.logger.info("🚀 Démarrage du système de traitement distribué")
        self.active = True

        # Démarrer les workers pour chaque type de job
        for job_type, worker_count in self.worker_config.items():
            for i in range(worker_count):
                worker_name = f"{job_type.value}-worker-{i+1}"
                worker = threading.Thread(
                    target=self._worker,
                    args=(worker_name, job_type)
                )
                worker.start()
                self.workers[job_type].append(worker)

        # Démarrer le moniteur de dépendances
        monitor = threading.Thread(target=self._dependency_monitor)
        monitor.start()

        # Démarrer le collecteur de métriques
        metrics_collector = threading.Thread(target=self._metrics_collector)
        metrics_collector.start()

        self.logger.info("✅ Système démarré")

    def _worker(self, worker_name: str, job_type: JobType):
        """Worker spécialisé pour un type de job."""
        logger = logging.getLogger(f"Worker.{worker_name}")
        logger.info(f"Worker {worker_name} démarré")

        job_queue = self.job_queues[job_type]

        while self.active:
            try:
                # Prendre un job avec timeout
                try:
                    priority, submit_time, job_id = job_queue.get(timeout=1)
                except queue.Empty:
                    continue

                # Vérifier que le job est toujours valide
                with self.lock:
                    if (job_id not in self.job_status or
                        self.job_status[job_id] != JobStatus.PENDING):
                        job_queue.task_done()
                        continue

                    self.job_status[job_id] = JobStatus.RUNNING
                    job = self.jobs[job_id]

                # Exécuter le job avec circuit breaker
                try:
                    circuit_breaker = self.circuit_breakers[job_type]
                    result = circuit_breaker.call(
                        self._execute_job_by_type,
                        job, worker_name
                    )

                    # Job réussi
                    with self.lock:
                        self.job_status[job_id] = JobStatus.COMPLETED
                        self.job_results[job_id] = result
                        self.stats['jobs_completed'] += 1

                    logger.info(f"✅ Job {job_id} terminé avec succès")
                    self.job_completed_event.set()

                except Exception as e:
                    # Job échoué
                    logger.error(f"❌ Job {job_id} échoué: {e}")

                    with self.lock:
                        if job_id not in self.job_errors:
                            self.job_errors[job_id] = []

                        self.job_errors[job_id].append({
                            'error': str(e),
                            'timestamp': time.time(),
                            'worker': worker_name
                        })

                        # Gestion des retry
                        retry_count = len(self.job_errors[job_id])
                        if retry_count <= job.max_retries:
                            logger.info(f"🔄 Retry {retry_count}/{job.max_retries} pour {job_id}")
                            self.job_status[job_id] = JobStatus.PENDING
                            # Remettre en queue avec priorité réduite
                            retry_priority = (-max(job.priority - retry_count, 0), time.time(), job_id)
                            job_queue.put(retry_priority)
                        else:
                            self.job_status[job_id] = JobStatus.FAILED
                            self.stats['jobs_failed'] += 1
                            logger.error(f"💥 Job {job_id} échec définitif")

                job_queue.task_done()

            except Exception as e:
                logger.error(f"Erreur worker {worker_name}: {e}")

        logger.info(f"Worker {worker_name} arrêté")

    def _execute_job_by_type(self, job: Job, worker_name: str) -> Any:
        """Exécute un job selon son type."""
        start_time = time.time()

        # Préparer les données avec les résultats des dépendances
        job_data = job.data.copy()
        for dep_id in job.dependencies:
            if dep_id in self.job_results:
                job_data[f'dep_{dep_id}'] = self.job_results[dep_id]

        # Exécuter selon le type
        if job.type == JobType.DATA_INGESTION:
            result = self._process_ingestion(job_data)
        elif job.type == JobType.DATA_PROCESSING:
            result = self._process_data_processing(job_data)
        elif job.type == JobType.DATA_ANALYSIS:
            result = self._process_analysis(job_data)
        elif job.type == JobType.REPORT_GENERATION:
            result = self._process_report_generation(job_data)
        else:
            raise ValueError(f"Type de job non supporté: {job.type}")

        # Enregistrer le temps de traitement
        processing_time = time.time() - start_time
        with self.lock:
            self.stats['total_processing_time'] += processing_time

        return result

    def _process_ingestion(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Simule l'ingestion de données."""
        time.sleep(random.uniform(0.5, 2.0))  # Simuler I/O

        # Simuler une erreur occasionnelle
        if random.random() < 0.1:
            raise Exception("Erreur d'ingestion de données")

        return {
            'type': 'ingestion_result',
            'records_ingested': random.randint(100, 1000),
            'source': data.get('source', 'unknown'),
            'timestamp': time.time()
        }

    def _process_data_processing(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Simule le traitement de données."""
        time.sleep(random.uniform(1.0, 3.0))  # Simuler calculs

        # Simuler une erreur occasionnelle
        if random.random() < 0.15:
            raise Exception("Erreur de traitement")

        # Utiliser les données d'ingestion si disponibles
        base_records = 500
        for key, value in data.items():
            if key.startswith('dep_') and isinstance(value, dict):
                base_records = value.get('records_ingested', base_records)
                break

        return {
            'type': 'processing_result',
            'records_processed': base_records,
            'records_valid': int(base_records * random.uniform(0.8, 0.95)),
            'processing_time': time.time()
        }

    def _process_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Simule l'analyse de données."""
        time.sleep(random.uniform(2.0, 4.0))  # Simuler analyse complexe

        # Simuler une erreur occasionnelle
        if random.random() < 0.05:
            raise Exception("Erreur d'analyse")

        # Utiliser les données traitées si disponibles
        base_records = 400
        for key, value in data.items():
            if key.startswith('dep_') and isinstance(value, dict):
                base_records = value.get('records_valid', base_records)
                break

        return {
            'type': 'analysis_result',
            'insights_generated': random.randint(5, 15),
            'anomalies_detected': random.randint(0, 3),
            'confidence_score': random.uniform(0.7, 0.95),
            'analyzed_records': base_records
        }

    def _process_report_generation(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Simule la génération de rapport."""
        time.sleep(random.uniform(1.0, 2.0))  # Simuler génération

        # Agréger les données des dépendances
        total_records = 0
        total_insights = 0

        for key, value in data.items():
            if key.startswith('dep_') and isinstance(value, dict):
                total_records += value.get('analyzed_records', 0)
                total_insights += value.get('insights_generated', 0)

        return {
            'type': 'report_result',
            'report_id': f"report_{int(time.time())}",
            'total_records_analyzed': total_records,
            'total_insights': total_insights,
            'report_size_mb': random.uniform(1.0, 10.0),
            'generated_at': time.time()
        }

    def _dependency_monitor(self):
        """Monitore les changements pour débloquer de nouveaux jobs."""
        while self.active:
            self.job_completed_event.wait(timeout=2)
            self.job_completed_event.clear()

            with self.lock:
                self._check_ready_jobs()

    def _metrics_collector(self):
        """Collecte les métriques du système."""
        while self.active:
            time.sleep(10)  # Collecter toutes les 10 secondes

            with self.lock:
                stats = self.get_stats()

            self.logger.info(f"📊 Métriques: {stats['jobs_completed']} complétés, "
                           f"{stats['jobs_failed']} échoués, "
                           f"{stats['pending_jobs']} en attente")

    def get_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques du système."""
        with self.lock:
            stats = self.stats.copy()

            # Compter les jobs par statut
            status_counts = {}
            for status in self.job_status.values():
                status_counts[status.value] = status_counts.get(status.value, 0) + 1

            stats.update(status_counts)
            stats['pending_jobs'] = status_counts.get('pending', 0)
            stats['running_jobs'] = status_counts.get('running', 0)

            # Calculer les temps moyens
            if stats['jobs_completed'] > 0:
                stats['avg_processing_time'] = (
                    stats['total_processing_time'] / stats['jobs_completed']
                )
            else:
                stats['avg_processing_time'] = 0

            # État des queues
            queue_sizes = {}
            for job_type, job_queue in self.job_queues.items():
                queue_sizes[f'{job_type.value}_queue_size'] = job_queue.qsize()

            stats.update(queue_sizes)

            return stats

    def wait_completion(self, timeout: float = None) -> bool:
        """Attend que tous les jobs se terminent."""
        start_time = time.time()

        while self.active:
            with self.lock:
                pending = sum(1 for status in self.job_status.values()
                            if status in [JobStatus.PENDING, JobStatus.RUNNING])

                if pending == 0:
                    self.logger.info("✅ Tous les jobs terminés")
                    return True

            if timeout and (time.time() - start_time) > timeout:
                self.logger.warning("⏰ Timeout atteint")
                return False

            time.sleep(1)

        return True

    def stop(self, timeout: float = 30):
        """Arrête le système."""
        self.logger.info("🛑 Arrêt du système...")
        self.active = False

        # Attendre que tous les workers se terminent
        all_workers = []
        for workers in self.workers.values():
            all_workers.extend(workers)

        for worker in all_workers:
            worker.join(timeout=timeout/len(all_workers))

        self.print_final_stats()

    def print_final_stats(self):
        """Affiche les statistiques finales."""
        stats = self.get_stats()

        print(f"\n{'='*50}")
        print("📊 STATISTIQUES FINALES DU SYSTÈME")
        print(f"{'='*50}")
        print(f"Jobs soumis: {stats['jobs_submitted']}")
        print(f"Jobs complétés: {stats['jobs_completed']}")
        print(f"Jobs échoués: {stats['jobs_failed']}")
        print(f"Temps de traitement moyen: {stats['avg_processing_time']:.2f}s")

        success_rate = 0
        if stats['jobs_submitted'] > 0:
            success_rate = (stats['jobs_completed'] / stats['jobs_submitted']) * 100
        print(f"Taux de succès: {success_rate:.1f}%")

        # Détail par statut
        print(f"\nRépartition des jobs:")
        for status in JobStatus:
            count = stats.get(status.value, 0)
            if count > 0:
                print(f"  {status.value}: {count}")

def demo_distributed_system():
    """Démonstration du système distribué complet."""
    print("🌐 SYSTÈME DE TRAITEMENT DISTRIBUÉ")
    print("="*50)

    # Créer le système
    system = DistributedDataProcessor(
        ingestion_workers=2,
        processing_workers=2,
        analysis_workers=2,
        report_workers=1
    )

    try:
        # Démarrer le système
        system.start()
        time.sleep(1)  # Laisser le système se stabiliser

        # Créer un pipeline de jobs interdépendants
        jobs = [
            # Phase 1: Ingestion de données (parallèle)
            Job("ingest_sales", JobType.DATA_INGESTION,
                {"source": "sales_db"}, priority=3),
            Job("ingest_customers", JobType.DATA_INGESTION,
                {"source": "customer_db"}, priority=3),
            Job("ingest_products", JobType.DATA_INGESTION,
                {"source": "product_db"}, priority=2),

            # Phase 2: Traitement (dépend de l'ingestion)
            Job("process_sales", JobType.DATA_PROCESSING,
                {"operation": "clean_sales"},
                dependencies=["ingest_sales"], priority=2),
            Job("process_customers", JobType.DATA_PROCESSING,
                {"operation": "clean_customers"},
                dependencies=["ingest_customers"], priority=2),

            # Phase 3: Analyse (dépend du traitement)
            Job("analyze_trends", JobType.DATA_ANALYSIS,
                {"analysis_type": "trend_analysis"},
                dependencies=["process_sales", "process_customers"], priority=1),
            Job("analyze_segments", JobType.DATA_ANALYSIS,
                {"analysis_type": "customer_segmentation"},
                dependencies=["process_customers"], priority=1),

            # Phase 4: Génération de rapports (dépend de l'analyse)
            Job("generate_monthly_report", JobType.REPORT_GENERATION,
                {"report_type": "monthly_summary"},
                dependencies=["analyze_trends", "analyze_segments"], priority=1),
        ]

        # Soumettre tous les jobs
        print(f"\n📋 Soumission de {len(jobs)} jobs...")
        for job in jobs:
            success = system.submit_job(job)
            if success:
                print(f"✅ Job soumis: {job.id}")
            else:
                print(f"❌ Échec soumission: {job.id}")
            time.sleep(0.2)

        # Surveiller le progrès
        print(f"\n⏳ Traitement en cours...")

        # Attendre la completion avec timeout
        completed = system.wait_completion(timeout=60)

        if not completed:
            print("⏰ Certains jobs n'ont pas terminé dans les temps")

    finally:
        # Arrêter le système
        system.stop()

if __name__ == "__main__":
    demo_distributed_system()
```

## Conclusion du Module 8

### Récapitulatif des patterns appris

1. **Producer-Consumer** : Communication asynchrone découplée
2. **Worker Pool** : Parallélisation de tâches indépendantes
3. **Pipeline** : Traitement en étapes séquentielles
4. **Map-Reduce** : Traitement distribué de gros volumes
5. **Circuit Breaker** : Protection contre les défaillances
6. **Scatter-Gather** : Requêtes distribuées avec agrégation

### Compétences acquises

- ✅ **Analyser un problème** de concurrence
- ✅ **Choisir le pattern approprié** selon le contexte
- ✅ **Implémenter des solutions robustes** avec gestion d'erreurs
- ✅ **Gérer la synchronisation** et éviter les race conditions
- ✅ **Monitorer et déboguer** du code concurrent
- ✅ **Combiner plusieurs patterns** dans un système complexe

### Projet final : Points clés

Le système distribué que nous avons construit démontre :

- **Architecture modulaire** avec workers spécialisés
- **Gestion des dépendances** entre jobs
- **Circuit breakers** pour la résilience
- **Monitoring et métriques** en temps réel
- **Retry et recovery** automatiques
- **Scalabilité** par type de tâche

### Conseils pour vos projets

1. **Commencez simple** : Un seul pattern à la fois
2. **Mesurez d'abord** : Profilez avant d'optimiser
3. **Gérez les erreurs** : La concurrence amplifie les bugs
4. **Testez sous charge** : Les bugs de concurrence sont sournois
5. **Documentez l'architecture** : Essentiel pour la maintenance

La programmation concurrente est un domaine complexe mais puissant. Avec les patterns et techniques que nous avons explorés, vous êtes maintenant équipés pour créer des applications performantes et scalables !

🎉 **Félicitations pour avoir terminé le Module 8 sur la programmation concurrente !**

⏭️
