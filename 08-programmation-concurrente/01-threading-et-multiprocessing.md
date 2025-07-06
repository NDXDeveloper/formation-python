🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.1 : Threading et multiprocessing

## Introduction

Dans cette section, nous allons explorer les deux principales approches pour la programmation concurrente en Python : les threads et les processus. Nous verrons comment créer, gérer et synchroniser ces tâches concurrentes.

### Analogie pratique
Imaginez que vous devez **nettoyer une maison** :
- **Séquentiel** : Vous nettoyez pièce par pièce, une à la fois
- **Threading** : Vous et votre famille nettoyez en même temps, en vous passant les outils
- **Multiprocessing** : Chaque personne nettoie avec ses propres outils, indépendamment

## Module threading : Threads en Python

Les threads permettent d'exécuter plusieurs tâches de façon concurrente dans le même processus.

### Création d'un thread simple

```python
import threading
import time

def tache_longue(nom, duree):
    """Simule une tâche qui prend du temps."""
    print(f"🚀 {nom} commencée")

    for i in range(duree):
        print(f"⏳ {nom}: étape {i+1}/{duree}")
        time.sleep(1)

    print(f"✅ {nom} terminée")

# Exécution séquentielle (lente)
print("=== EXÉCUTION SÉQUENTIELLE ===")
start_time = time.time()

tache_longue("Tâche A", 3)
tache_longue("Tâche B", 3)

sequential_time = time.time() - start_time
print(f"Temps total séquentiel: {sequential_time:.1f}s\n")

# Exécution avec threads (plus rapide)
print("=== EXÉCUTION AVEC THREADS ===")
start_time = time.time()

# Créer les threads
thread1 = threading.Thread(target=tache_longue, args=("Tâche A", 3))
thread2 = threading.Thread(target=tache_longue, args=("Tâche B", 3))

# Démarrer les threads
thread1.start()
thread2.start()

# Attendre que tous les threads se terminent
thread1.join()
thread2.join()

concurrent_time = time.time() - start_time
print(f"Temps total concurrent: {concurrent_time:.1f}s")
print(f"Accélération: {sequential_time/concurrent_time:.1f}x")
```

### Thread avec classe personnalisée

```python
import threading
import time
import random

class TelechargerFichier(threading.Thread):
    """Thread personnalisé pour télécharger un fichier."""

    def __init__(self, nom_fichier, taille_mo):
        super().__init__()
        self.nom_fichier = nom_fichier
        self.taille_mo = taille_mo
        self.progression = 0
        self.termine = False

    def run(self):
        """Méthode principale du thread."""
        print(f"📥 Début téléchargement: {self.nom_fichier}")

        # Simuler le téléchargement
        for i in range(self.taille_mo):
            time.sleep(random.uniform(0.1, 0.3))  # Vitesse variable
            self.progression = (i + 1) / self.taille_mo * 100
            print(f"📊 {self.nom_fichier}: {self.progression:.1f}%")

        self.termine = True
        print(f"✅ {self.nom_fichier} téléchargé!")

    def get_statut(self):
        """Retourne le statut actuel du téléchargement."""
        if self.termine:
            return "Terminé"
        elif self.progression > 0:
            return f"En cours ({self.progression:.1f}%)"
        else:
            return "En attente"

# Test des téléchargements concurrents
def demo_telechargements():
    fichiers = [
        ("video.mp4", 5),
        ("document.pdf", 2),
        ("image.jpg", 1),
        ("archive.zip", 3)
    ]

    threads = []

    # Créer et démarrer les threads
    for nom, taille in fichiers:
        thread = TelechargerFichier(nom, taille)
        threads.append(thread)
        thread.start()

    # Surveillance périodique
    while any(not t.termine for t in threads):
        time.sleep(1)
        print(f"\n📋 Statut des téléchargements:")
        for t in threads:
            print(f"  {t.nom_fichier}: {t.get_statut()}")

    # Attendre la fin de tous les threads
    for t in threads:
        t.join()

    print("\n🎉 Tous les téléchargements terminés!")

demo_telechargements()
```

### Synchronisation avec Lock

```python
import threading
import time

# Variable partagée (dangereuse sans synchronisation)
compteur = 0
lock = threading.Lock()

def incrementer_dangereux(nb_iterations):
    """Incrémente sans protection (race condition)."""
    global compteur
    for _ in range(nb_iterations):
        # Opération non-atomique ! Danger !
        temp = compteur
        temp += 1
        compteur = temp

def incrementer_securise(nb_iterations):
    """Incrémente avec protection par lock."""
    global compteur
    for _ in range(nb_iterations):
        with lock:  # Acquisition automatique du verrou
            temp = compteur
            temp += 1
            compteur = temp

def test_synchronisation():
    """Teste la différence avec et sans synchronisation."""
    global compteur

    # Test sans synchronisation
    print("🔥 Test SANS synchronisation (race condition)")
    compteur = 0
    threads = []

    for i in range(5):
        t = threading.Thread(target=incrementer_dangereux, args=(1000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Résultat attendu: 5000")
    print(f"Résultat obtenu: {compteur}")
    print(f"Différence: {5000 - compteur} (race condition!)\n")

    # Test avec synchronisation
    print("🔒 Test AVEC synchronisation (sécurisé)")
    compteur = 0
    threads = []

    for i in range(5):
        t = threading.Thread(target=incrementer_securise, args=(1000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Résultat attendu: 5000")
    print(f"Résultat obtenu: {compteur}")
    print("✅ Résultat correct avec synchronisation!")

test_synchronisation()
```

### Communication avec Queue

```python
import threading
import queue
import time
import random

def producteur(q, nom, nb_items):
    """Produit des éléments et les place dans la queue."""
    for i in range(nb_items):
        item = f"{nom}_item_{i+1}"

        # Simuler du travail
        time.sleep(random.uniform(0.1, 0.5))

        q.put(item)
        print(f"📦 Produit: {item}")

    print(f"✅ {nom} a terminé la production")

def consommateur(q, nom):
    """Consomme des éléments de la queue."""
    while True:
        try:
            # Attendre un élément (timeout pour éviter de bloquer)
            item = q.get(timeout=2)

            print(f"🔄 {nom} traite: {item}")

            # Simuler le traitement
            time.sleep(random.uniform(0.2, 0.8))

            print(f"✅ {nom} a terminé: {item}")
            q.task_done()

        except queue.Empty:
            print(f"⏰ {nom}: timeout, arrêt")
            break

def demo_producer_consumer():
    """Démonstration du pattern Producteur-Consommateur."""
    print("🏭 PATTERN PRODUCTEUR-CONSOMMATEUR")
    print("-" * 40)

    # Créer une queue thread-safe
    q = queue.Queue(maxsize=5)  # Limite de 5 éléments

    # Créer les producteurs
    producteur1 = threading.Thread(target=producteur, args=(q, "Prod1", 3))
    producteur2 = threading.Thread(target=producteur, args=(q, "Prod2", 4))

    # Créer les consommateurs
    consommateur1 = threading.Thread(target=consommateur, args=(q, "Cons1"))
    consommateur2 = threading.Thread(target=consommateur, args=(q, "Cons2"))

    # Démarrer tous les threads
    producteur1.start()
    producteur2.start()
    consommateur1.start()
    consommateur2.start()

    # Attendre que les producteurs terminent
    producteur1.join()
    producteur2.join()

    # Attendre que tous les éléments soient traités
    q.join()

    print("🎉 Tous les éléments ont été traités!")

demo_producer_consumer()
```

## Module multiprocessing : Processus parallèles

Le multiprocessing permet un vrai parallélisme en créant des processus séparés.

### Processus simple

```python
import multiprocessing
import time
import os

def calcul_intensif(nom, debut, fin):
    """Calcul CPU-intensif (somme des carrés)."""
    pid = os.getpid()
    print(f"🔄 {nom} (PID {pid}): calcul de {debut} à {fin}")

    total = 0
    for i in range(debut, fin):
        total += i * i

    print(f"✅ {nom} (PID {pid}): résultat = {total}")
    return total

def demo_multiprocessing():
    """Compare séquentiel vs parallèle pour calculs CPU."""

    # Tâches à effectuer
    taches = [
        ("Tâche 1", 0, 1000000),
        ("Tâche 2", 1000000, 2000000),
        ("Tâche 3", 2000000, 3000000),
        ("Tâche 4", 3000000, 4000000)
    ]

    print("💻 COMPARAISON SÉQUENTIEL vs PARALLÈLE")
    print("-" * 45)

    # Exécution séquentielle
    print("\n🐌 Exécution séquentielle:")
    start_time = time.time()

    resultats_seq = []
    for nom, debut, fin in taches:
        resultat = calcul_intensif(nom, debut, fin)
        resultats_seq.append(resultat)

    temps_seq = time.time() - start_time
    print(f"Temps séquentiel: {temps_seq:.2f}s")

    # Exécution parallèle
    print(f"\n🚀 Exécution parallèle:")
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        # Lancer tous les calculs en parallèle
        resultats_par = pool.starmap(calcul_intensif, taches)

    temps_par = time.time() - start_time
    print(f"Temps parallèle: {temps_par:.2f}s")
    print(f"Accélération: {temps_seq/temps_par:.1f}x")

    # Vérifier que les résultats sont identiques
    print(f"\nRésultats identiques: {resultats_seq == resultats_par}")

if __name__ == "__main__":
    demo_multiprocessing()
```

### Communication entre processus

```python
import multiprocessing
import time
import random

def travailleur(nom, queue_entree, queue_sortie):
    """Processus travailleur qui traite des tâches."""
    pid = multiprocessing.current_process().pid
    print(f"👷 {nom} (PID {pid}) démarré")

    while True:
        try:
            tache = queue_entree.get(timeout=2)

            if tache is None:  # Signal d'arrêt
                print(f"🛑 {nom} arrêté")
                break

            print(f"🔄 {nom} traite: {tache}")

            # Simuler du travail
            temps_travail = random.uniform(1, 3)
            time.sleep(temps_travail)

            resultat = f"Résultat de {tache}"
            queue_sortie.put((nom, resultat))

            print(f"✅ {nom} terminé: {tache}")

        except multiprocessing.TimeoutError:
            print(f"⏰ {nom} timeout")
            break

def demo_communication_processus():
    """Démonstration de communication entre processus."""
    print("🔄 COMMUNICATION ENTRE PROCESSUS")
    print("-" * 35)

    # Créer les queues pour communication
    queue_entree = multiprocessing.Queue()
    queue_sortie = multiprocessing.Queue()

    # Ajouter des tâches
    taches = [f"Tâche_{i}" for i in range(1, 8)]
    for tache in taches:
        queue_entree.put(tache)

    # Créer et démarrer les processus
    nb_workers = 3
    processus = []

    for i in range(nb_workers):
        p = multiprocessing.Process(
            target=travailleur,
            args=(f"Worker-{i+1}", queue_entree, queue_sortie)
        )
        processus.append(p)
        p.start()

    # Collecter les résultats
    resultats = []
    for _ in range(len(taches)):
        worker, resultat = queue_sortie.get()
        resultats.append((worker, resultat))
        print(f"📥 Reçu de {worker}: {resultat}")

    # Arrêter les processus
    for _ in range(nb_workers):
        queue_entree.put(None)  # Signal d'arrêt

    # Attendre la fin de tous les processus
    for p in processus:
        p.join()

    print(f"\n🎉 Traitement terminé! {len(resultats)} résultats collectés")

if __name__ == "__main__":
    demo_communication_processus()
```

## Exercices pratiques

### Exercice 1 : Téléchargeur d'URLs

```python
import threading
import requests
import time

def telecharger_url(url, resultats, index):
    """Télécharge une URL et stocke le résultat."""
    try:
        print(f"📥 Téléchargement de {url}")
        start_time = time.time()

        response = requests.get(url, timeout=10)
        duree = time.time() - start_time

        resultats[index] = {
            'url': url,
            'status': response.status_code,
            'taille': len(response.content),
            'duree': duree
        }

        print(f"✅ {url}: {response.status_code} ({len(response.content)} bytes)")

    except Exception as e:
        print(f"❌ {url}: Erreur - {e}")
        resultats[index] = {'url': url, 'erreur': str(e)}

def telecharger_urls_concurrent(urls):
    """Télécharge plusieurs URLs en parallèle."""
    resultats = [None] * len(urls)
    threads = []

    # Créer et démarrer les threads
    for i, url in enumerate(urls):
        t = threading.Thread(target=telecharger_url, args=(url, resultats, i))
        threads.append(t)
        t.start()

    # Attendre tous les threads
    for t in threads:
        t.join()

    return resultats

# Test
urls_test = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/200",
    "https://httpbin.org/json",
    "https://httpbin.org/user-agent"
]

print("🌐 Téléchargement concurrent d'URLs")
resultats = telecharger_urls_concurrent(urls_test)

print("\n📊 Résultats:")
for r in resultats:
    if 'erreur' in r:
        print(f"  ❌ {r['url']}: {r['erreur']}")
    else:
        print(f"  ✅ {r['url']}: {r['status']} ({r['duree']:.2f}s)")
```

### Exercice 2 : Processeur d'images parallèle

```python
import multiprocessing
from PIL import Image
import os

def redimensionner_image(info_image):
    """Redimensionne une image (fonction pour multiprocessing)."""
    chemin_entree, chemin_sortie, taille = info_image

    try:
        # Ouvrir et redimensionner l'image
        with Image.open(chemin_entree) as img:
            img_redimensionnee = img.resize(taille, Image.Resampling.LANCZOS)
            img_redimensionnee.save(chemin_sortie)

        return f"✅ {os.path.basename(chemin_entree)} → {taille}"

    except Exception as e:
        return f"❌ {os.path.basename(chemin_entree)}: {e}"

def traiter_images_parallele(dossier_images, taille_cible=(800, 600)):
    """Traite toutes les images d'un dossier en parallèle."""

    if not os.path.exists(dossier_images):
        print(f"❌ Dossier non trouvé: {dossier_images}")
        return

    # Préparer les tâches
    taches = []
    dossier_sortie = os.path.join(dossier_images, "redimensionnees")
    os.makedirs(dossier_sortie, exist_ok=True)

    for fichier in os.listdir(dossier_images):
        if fichier.lower().endswith(('.png', '.jpg', '.jpeg')):
            chemin_entree = os.path.join(dossier_images, fichier)
            chemin_sortie = os.path.join(dossier_sortie, f"thumb_{fichier}")
            taches.append((chemin_entree, chemin_sortie, taille_cible))

    if not taches:
        print("❌ Aucune image trouvée")
        return

    print(f"🖼️ Traitement de {len(taches)} images...")

    # Traitement parallèle
    with multiprocessing.Pool() as pool:
        resultats = pool.map(redimensionner_image, taches)

    # Afficher les résultats
    for resultat in resultats:
        print(f"  {resultat}")

# Test (créer d'abord quelques images de test)
# traiter_images_parallele("./images")
```

### Exercice 3 : Monitor de système

```python
import threading
import time
import psutil
from collections import deque

class MonitorSysteme:
    """Monitor système avec threads pour collecte continue."""

    def __init__(self):
        self.actif = False
        self.donnees = {
            'cpu': deque(maxlen=60),      # 60 dernières mesures
            'memoire': deque(maxlen=60),
            'disque': deque(maxlen=60)
        }
        self.lock = threading.Lock()

    def collecter_metriques(self):
        """Thread de collecte des métriques."""
        while self.actif:
            cpu = psutil.cpu_percent(interval=1)
            memoire = psutil.virtual_memory().percent
            disque = psutil.disk_usage('/').percent

            with self.lock:
                self.donnees['cpu'].append(cpu)
                self.donnees['memoire'].append(memoire)
                self.donnees['disque'].append(disque)

            print(f"📊 CPU: {cpu:5.1f}% | RAM: {memoire:5.1f}% | Disque: {disque:5.1f}%")

    def detecter_alertes(self):
        """Thread de détection d'alertes."""
        seuils = {'cpu': 80, 'memoire': 85, 'disque': 90}

        while self.actif:
            time.sleep(5)  # Vérifier toutes les 5 secondes

            with self.lock:
                for metrique, valeurs in self.donnees.items():
                    if valeurs and valeurs[-1] > seuils[metrique]:
                        print(f"🚨 ALERTE {metrique.upper()}: {valeurs[-1]:.1f}%")

    def demarrer(self, duree=30):
        """Démarre le monitoring."""
        print(f"🖥️ Démarrage du monitoring ({duree}s)...")
        self.actif = True

        # Démarrer les threads
        thread_collecte = threading.Thread(target=self.collecter_metriques)
        thread_alertes = threading.Thread(target=self.detecter_alertes)

        thread_collecte.start()
        thread_alertes.start()

        # Arrêter après la durée spécifiée
        time.sleep(duree)
        self.actif = False

        thread_collecte.join()
        thread_alertes.join()

        print("✅ Monitoring terminé")

        # Afficher un résumé
        with self.lock:
            for metrique, valeurs in self.donnees.items():
                if valeurs:
                    moyenne = sum(valeurs) / len(valeurs)
                    maximum = max(valeurs)
                    print(f"  {metrique.capitalize()}: moy={moyenne:.1f}%, max={maximum:.1f}%")

# Test
# monitor = MonitorSysteme()
# monitor.demarrer(15)  # 15 secondes de monitoring
```

## Bonnes pratiques

### **1. Threading**
```python
# ✅ Bon : Utiliser with pour les locks
with lock:
    shared_data += 1

# ✅ Bon : join() pour attendre les threads
for thread in threads:
    thread.join()

# ❌ Éviter : accès non protégé aux données partagées
# shared_counter += 1  # Race condition !
```

### **2. Multiprocessing**
```python
# ✅ Bon : Protection avec if __name__ == "__main__"
if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        results = pool.map(worker_function, tasks)

# ✅ Bon : Utiliser des queues pour la communication
queue = multiprocessing.Queue()

# ❌ Éviter : partage direct de variables
# global_var = 0  # Ne fonctionne pas entre processus
```

### **3. Gestion d'erreurs**
```python
def worker_securise(task):
    try:
        return process_task(task)
    except Exception as e:
        logging.error(f"Erreur dans worker: {e}")
        return None
```

## Quand utiliser quoi ?

### **Threading** 🧵
- **I/O-bound** : fichiers, réseau, bases de données
- **Interfaces utilisateur** : garder la responsivité
- **Tâches courtes** et fréquentes

### **Multiprocessing** ⚡
- **CPU-bound** : calculs, traitement d'images, ML
- **Isolation** : tâches indépendantes
- **Utiliser tous les cœurs** du processeur

## Résumé

Dans cette section, nous avons appris :

1. **Threading** : Concurrence pour I/O-bound tasks
2. **Multiprocessing** : Parallélisme pour CPU-bound tasks
3. **Synchronisation** : Locks, Queues pour éviter les race conditions
4. **Patterns** : Producer-Consumer, Worker Pool
5. **Bonnes pratiques** : Sécurité, gestion d'erreurs

La programmation concurrente peut grandement améliorer les performances, mais nécessite attention et rigueur pour éviter les pièges.

Dans la prochaine section, nous explorerons `asyncio` pour la programmation asynchrone.

⏭️
