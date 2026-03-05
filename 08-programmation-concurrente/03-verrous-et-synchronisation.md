🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.3 Gestion des Verrous et Synchronisation

## Introduction à la synchronisation

Quand plusieurs threads ou processus travaillent ensemble, ils doivent parfois se **coordonner** pour éviter des problèmes. C'est ce qu'on appelle la **synchronisation**.

### Pourquoi synchroniser ?

Imaginez une banque avec plusieurs guichets qui accèdent au même compte bancaire :

**Sans synchronisation** :
1. Guichet A lit le solde : 1000€
2. Guichet B lit le solde : 1000€
3. Guichet A retire 100€ et écrit : 900€
4. Guichet B retire 200€ et écrit : 800€

**Résultat** : Le solde est 800€ mais devrait être 700€ ! 😱

**Avec synchronisation** :
1. Guichet A **verrouille** le compte
2. Guichet A lit : 1000€, retire 100€, écrit : 900€
3. Guichet A **déverrouille**
4. Guichet B **verrouille** le compte
5. Guichet B lit : 900€, retire 200€, écrit : 700€
6. Guichet B **déverrouille**

**Résultat** : Le solde est correct : 700€ ✅

---

## Les problèmes de concurrence

### Race Condition (Condition de course)

Une **race condition** se produit quand le résultat dépend de l'ordre d'exécution des threads.

```python
import threading

compteur = 0

def incrementer():
    global compteur
    for _ in range(100000):
        # Cette opération n'est pas atomique!
        compteur += 1  # Lecture, addition, écriture

# Sans synchronisation
threads = [threading.Thread(target=incrementer) for _ in range(5)]  
for t in threads:  
    t.start()
for t in threads:
    t.join()

print(f"Compteur: {compteur}")  # Résultat imprévisible!
# Devrait être 500000, mais sera probablement moins
```

**Résultat typique** : `Compteur: 347823` (au lieu de 500000)

### Deadlock (Interblocage)

Un **deadlock** se produit quand deux threads attendent chacun une ressource détenue par l'autre.

**Analogie** : Deux personnes veulent passer une porte étroite, chacune attend que l'autre recule.

```python
import threading  
import time  

verrou_a = threading.Lock()  
verrou_b = threading.Lock()  

def thread1():
    with verrou_a:
        print("Thread 1: verrou A acquis")
        time.sleep(0.1)
        with verrou_b:  # Attend verrou B
            print("Thread 1: verrou B acquis")

def thread2():
    with verrou_b:
        print("Thread 2: verrou B acquis")
        time.sleep(0.1)
        with verrou_a:  # Attend verrou A
            print("Thread 2: verrou A acquis")

# Les deux threads se bloquent mutuellement! ⚠️
```

---

## Les mécanismes de synchronisation

Python propose plusieurs outils pour synchroniser les threads et les coroutines :

| Mécanisme | Usage | Threading | Asyncio |
|-----------|-------|-----------|---------|
| **Lock** | Accès exclusif à une ressource | ✅ | ✅ |
| **RLock** | Lock réentrant (même thread) | ✅ | ❌ |
| **Semaphore** | Limiter le nombre d'accès | ✅ | ✅ |
| **Event** | Signaler un événement | ✅ | ✅ |
| **Condition** | Attendre une condition | ✅ | ✅ |
| **Barrier** | Synchroniser plusieurs threads | ✅ | ❌ |

---

## Lock (Verrou simple)

Le **Lock** est le mécanisme de synchronisation le plus basique. Il garantit qu'un seul thread à la fois peut exécuter une section de code.

### Avec Threading

```python
import threading  
import time  

compteur = 0  
verrou = threading.Lock()  # Créer un verrou  

def incrementer_avec_lock():
    global compteur
    for _ in range(100000):
        with verrou:  # Acquérir le verrou
            compteur += 1
        # Le verrou est automatiquement libéré

# Avec synchronisation
threads = [threading.Thread(target=incrementer_avec_lock) for _ in range(5)]  
for t in threads:  
    t.start()
for t in threads:
    t.join()

print(f"Compteur avec lock: {compteur}")  # Toujours 500000 ✅
```

### Syntaxe alternative (moins recommandée)

```python
verrou = threading.Lock()

def incrementer_manuel():
    global compteur
    verrou.acquire()  # Acquérir manuellement
    try:
        compteur += 1
    finally:
        verrou.release()  # Toujours libérer!
```

**Recommandation** : Utilisez toujours `with verrou:` pour éviter d'oublier de libérer.

### Exemple pratique : Gestion de fichier partagé

```python
import threading  
import time  

class GestionnaireFichier:
    """Gère l'écriture dans un fichier par plusieurs threads"""

    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.verrou = threading.Lock()

    def ecrire(self, message, thread_id):
        """Écrit dans le fichier de manière sécurisée"""
        with self.verrou:
            # Section critique protégée
            print(f"[Thread {thread_id}] Écriture en cours...")
            with open(self.nom_fichier, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
            time.sleep(0.1)  # Simule une opération lente
            print(f"[Thread {thread_id}] Écriture terminée")

def worker(gestionnaire, thread_id):
    """Thread qui écrit dans le fichier"""
    for i in range(3):
        gestionnaire.ecrire(f"Message {i} du thread {thread_id}", thread_id)

# Utilisation
gestionnaire = GestionnaireFichier("log.txt")  
threads = [threading.Thread(target=worker, args=(gestionnaire, i)) for i in range(3)]  

for t in threads:
    t.start()
for t in threads:
    t.join()

print("✅ Toutes les écritures sont terminées")
```

### Avec Asyncio

```python
import asyncio

compteur = 0  
verrou = asyncio.Lock()  # Verrou asynchrone  

async def incrementer_async():
    global compteur
    for _ in range(100000):
        async with verrou:  # async with pour asyncio
            compteur += 1

async def main():
    # Créer plusieurs tâches
    taches = [incrementer_async() for _ in range(5)]
    await asyncio.gather(*taches)
    print(f"Compteur avec asyncio.Lock: {compteur}")

asyncio.run(main())
```

---

## RLock (Verrou Réentrant)

Un **RLock** (Reentrant Lock) peut être acquis plusieurs fois par le **même thread** sans se bloquer.

### Quand utiliser RLock ?

Utilisez RLock quand une fonction qui utilise un verrou peut appeler une autre fonction qui utilise le même verrou.

```python
import threading

class CompteBancaire:
    """Compte bancaire avec méthodes synchronisées"""

    def __init__(self, solde):
        self.solde = solde
        self.verrou = threading.RLock()  # RLock au lieu de Lock

    def retirer(self, montant):
        """Retire de l'argent"""
        with self.verrou:
            if self.solde >= montant:
                self.solde -= montant
                return True
            return False

    def transferer(self, autre_compte, montant):
        """Transfère vers un autre compte"""
        with self.verrou:  # Premier lock
            if self.retirer(montant):  # Appelle retirer qui utilise aussi le lock!
                autre_compte.deposer(montant)
                return True
            return False

    def deposer(self, montant):
        """Dépose de l'argent"""
        with self.verrou:
            self.solde += montant

# Utilisation
compte1 = CompteBancaire(1000)  
compte2 = CompteBancaire(500)  

# Sans RLock, ceci causerait un deadlock car transferer()
# et retirer() tentent d'acquérir le même lock
compte1.transferer(compte2, 200)  
print(f"Compte 1: {compte1.solde}€")  # 800€  
print(f"Compte 2: {compte2.solde}€")  # 700€  
```

**Avec un Lock normal**, `transferer()` se serait bloqué en essayant d'acquérir le lock une deuxième fois.

---

## Semaphore (Sémaphore)

Un **Semaphore** limite le nombre de threads qui peuvent accéder simultanément à une ressource.

**Analogie** : Un parking avec 5 places. Quand il est plein, les voitures attendent qu'une place se libère.

### Avec Threading

```python
import threading  
import time  
import random  

# Sémaphore qui autorise max 3 threads simultanés
semaphore = threading.Semaphore(3)

def acceder_ressource(thread_id):
    """Accède à une ressource limitée"""
    print(f"[Thread {thread_id}] Attend l'accès...")

    with semaphore:
        print(f"[Thread {thread_id}] 🟢 Accès obtenu")
        duree = random.uniform(1, 3)
        time.sleep(duree)  # Utilise la ressource
        print(f"[Thread {thread_id}] 🔴 Libère l'accès")

# Créer 10 threads mais max 3 peuvent accéder en même temps
threads = [threading.Thread(target=acceder_ressource, args=(i,)) for i in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("✅ Tous les threads ont terminé")
```

### Exemple pratique : Pool de connexions

```python
import threading  
import time  

class PoolConnexions:
    """Gère un pool limité de connexions à une base de données"""

    def __init__(self, max_connexions):
        self.semaphore = threading.Semaphore(max_connexions)
        self.connexions_actives = 0
        self.verrou_compteur = threading.Lock()

    def executer_requete(self, requete, thread_id):
        """Exécute une requête avec une connexion du pool"""
        print(f"[Thread {thread_id}] Demande de connexion...")

        with self.semaphore:
            # Obtenir une connexion (max atteint = attendre)
            with self.verrou_compteur:
                self.connexions_actives += 1
                print(f"[Thread {thread_id}] ✅ Connexion obtenue ({self.connexions_actives} actives)")

            # Exécuter la requête
            print(f"[Thread {thread_id}] Exécution: {requete}")
            time.sleep(2)  # Simule le temps de la requête

            # Libérer la connexion
            with self.verrou_compteur:
                self.connexions_actives -= 1
                print(f"[Thread {thread_id}] 🔴 Connexion libérée ({self.connexions_actives} actives)")

# Pool avec maximum 3 connexions
pool = PoolConnexions(max_connexions=3)

def worker(thread_id):
    """Thread qui exécute une requête"""
    pool.executer_requete(f"SELECT * FROM table WHERE id={thread_id}", thread_id)

# 8 threads veulent accéder, mais max 3 en même temps
threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("✅ Toutes les requêtes sont terminées")
```

### Avec Asyncio

```python
import asyncio  
import random  

async def tache_limitee(semaphore, numero):
    """Tâche qui utilise un sémaphore"""
    async with semaphore:
        print(f"[Tâche {numero}] Démarrage")
        await asyncio.sleep(random.uniform(1, 2))
        print(f"[Tâche {numero}] Terminée")

async def main():
    # Maximum 3 tâches simultanées
    semaphore = asyncio.Semaphore(3)

    # Créer 10 tâches
    taches = [tache_limitee(semaphore, i) for i in range(10)]
    await asyncio.gather(*taches)

asyncio.run(main())
```

---

## Event (Événement)

Un **Event** permet à un thread d'attendre qu'un événement se produise, signalé par un autre thread.

**Analogie** : Un feu de signalisation. Les threads attendent que le feu passe au vert.

### Avec Threading

```python
import threading  
import time  

# Créer un événement
event = threading.Event()

def attendre_signal(thread_id):
    """Thread qui attend un signal"""
    print(f"[Thread {thread_id}] En attente du signal...")
    event.wait()  # Bloque jusqu'à ce que l'event soit set
    print(f"[Thread {thread_id}] 🟢 Signal reçu! Démarrage du travail")
    time.sleep(1)
    print(f"[Thread {thread_id}] Travail terminé")

def envoyer_signal():
    """Thread qui envoie le signal"""
    print("[Contrôleur] Préparation...")
    time.sleep(3)  # Simule une préparation
    print("[Contrôleur] 📢 Envoi du signal!")
    event.set()  # Déclenche l'événement

# Créer les threads
workers = [threading.Thread(target=attendre_signal, args=(i,)) for i in range(3)]  
controleur = threading.Thread(target=envoyer_signal)  

# Démarrer tous les threads
for w in workers:
    w.start()
controleur.start()

# Attendre la fin
for w in workers:
    w.join()
controleur.join()

print("✅ Tous les threads ont terminé")
```

### Exemple pratique : Système de téléchargement

```python
import threading  
import time  

class GestionnaireTelechargement:
    """Gère le téléchargement et le traitement de fichiers"""

    def __init__(self):
        self.fichier_pret = threading.Event()
        self.fichier = None

    def telecharger(self):
        """Télécharge un fichier"""
        print("📥 Téléchargement en cours...")
        time.sleep(3)  # Simule le téléchargement

        self.fichier = "data.csv"
        print(f"✅ Téléchargement terminé: {self.fichier}")

        # Signaler que le fichier est prêt
        self.fichier_pret.set()

    def traiter(self, traitement_id):
        """Attend le fichier puis le traite"""
        print(f"[Traitement {traitement_id}] En attente du fichier...")

        # Attendre que le fichier soit téléchargé
        self.fichier_pret.wait()

        print(f"[Traitement {traitement_id}] 🔧 Traitement de {self.fichier}")
        time.sleep(2)
        print(f"[Traitement {traitement_id}] ✅ Traitement terminé")

# Utilisation
gestionnaire = GestionnaireTelechargement()

# Thread de téléchargement
thread_download = threading.Thread(target=gestionnaire.telecharger)

# Threads de traitement (attendent le téléchargement)
threads_traitement = [
    threading.Thread(target=gestionnaire.traiter, args=(i,))
    for i in range(3)
]

# Démarrer tous les threads
thread_download.start()  
for t in threads_traitement:  
    t.start()

# Attendre la fin
thread_download.join()  
for t in threads_traitement:  
    t.join()

print("✅ Pipeline complet terminé")
```

### Méthodes d'Event

| Méthode | Description |
|---------|-------------|
| `set()` | Active l'événement (feu vert) |
| `clear()` | Désactive l'événement (feu rouge) |
| `wait(timeout)` | Attend l'événement (bloque jusqu'à set()) |
| `is_set()` | Vérifie si l'événement est actif |

### Avec Asyncio

```python
import asyncio

async def attendre_async(event, numero):
    """Attend un événement asynchrone"""
    print(f"[Tâche {numero}] En attente...")
    await event.wait()
    print(f"[Tâche {numero}] 🟢 Événement reçu!")

async def declencher_async(event):
    """Déclenche l'événement après un délai"""
    await asyncio.sleep(2)
    print("📢 Déclenchement de l'événement!")
    event.set()

async def main():
    event = asyncio.Event()

    # Créer les tâches
    taches = [attendre_async(event, i) for i in range(3)]
    taches.append(declencher_async(event))

    await asyncio.gather(*taches)

asyncio.run(main())
```

---

## Condition (Variable conditionnelle)

Une **Condition** permet d'attendre qu'une condition spécifique soit vraie.

**Analogie** : Une salle d'attente où les patients attendent que leur nom soit appelé.

### Avec Threading

```python
import threading  
import time  
import random  

class BufferPartage:
    """Buffer partagé avec producteur/consommateur"""

    def __init__(self, taille_max=5):
        self.buffer = []
        self.taille_max = taille_max
        self.condition = threading.Condition()

    def produire(self, item):
        """Ajoute un item au buffer"""
        with self.condition:
            # Attendre que le buffer ne soit pas plein
            while len(self.buffer) >= self.taille_max:
                print(f"📦 Buffer plein, producteur attend...")
                self.condition.wait()

            self.buffer.append(item)
            print(f"✅ Produit: {item} (buffer: {len(self.buffer)})")

            # Notifier les consommateurs
            self.condition.notify()

    def consommer(self):
        """Retire un item du buffer"""
        with self.condition:
            # Attendre que le buffer ne soit pas vide
            while len(self.buffer) == 0:
                print(f"📭 Buffer vide, consommateur attend...")
                self.condition.wait()

            item = self.buffer.pop(0)
            print(f"🔧 Consommé: {item} (buffer: {len(self.buffer)})")

            # Notifier les producteurs
            self.condition.notify()

            return item

def producteur(buffer, nombre_items):
    """Produit des items"""
    for i in range(nombre_items):
        time.sleep(random.uniform(0.1, 0.5))
        buffer.produire(f"Item-{i}")

def consommateur(buffer, nombre_items):
    """Consomme des items"""
    for _ in range(nombre_items):
        time.sleep(random.uniform(0.2, 0.8))
        buffer.consommer()

# Utilisation
buffer = BufferPartage(taille_max=3)

# 2 producteurs, 2 consommateurs
prod1 = threading.Thread(target=producteur, args=(buffer, 5))  
prod2 = threading.Thread(target=producteur, args=(buffer, 5))  
cons1 = threading.Thread(target=consommateur, args=(buffer, 5))  
cons2 = threading.Thread(target=consommateur, args=(buffer, 5))  

prod1.start()  
prod2.start()  
cons1.start()  
cons2.start()  

prod1.join()  
prod2.join()  
cons1.join()  
cons2.join()  

print("✅ Production/consommation terminée")
```

### Méthodes de Condition

| Méthode | Description |
|---------|-------------|
| `wait()` | Libère le lock et attend une notification |
| `notify()` | Réveille un thread en attente |
| `notify_all()` | Réveille tous les threads en attente |

---

## Barrier (Barrière)

Une **Barrier** synchronise plusieurs threads pour qu'ils atteignent un point en même temps.

**Analogie** : Une course où tous les coureurs doivent attendre que tout le monde soit prêt avant le départ.

### Avec Threading

```python
import threading  
import time  
import random  

def travailleur(barrier, thread_id):
    """Thread qui travaille puis attend les autres"""
    # Phase 1: Préparation
    duree = random.uniform(1, 3)
    print(f"[Thread {thread_id}] Préparation pendant {duree:.1f}s...")
    time.sleep(duree)
    print(f"[Thread {thread_id}] ✅ Préparation terminée, attente des autres...")

    # Attendre que tous les threads soient prêts
    barrier.wait()

    # Phase 2: Exécution synchrone
    print(f"[Thread {thread_id}] 🚀 Démarrage synchronisé!")
    time.sleep(1)
    print(f"[Thread {thread_id}] ✅ Travail terminé")

# Créer une barrière pour 5 threads
barrier = threading.Barrier(5)

threads = [threading.Thread(target=travailleur, args=(barrier, i)) for i in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("✅ Tous les threads ont terminé de manière synchronisée")
```

### Exemple pratique : Simulation parallèle

```python
import threading  
import time  

class SimulationParallele:
    """Simule un système avec plusieurs composants synchronisés"""

    def __init__(self, nombre_composants):
        self.barrier = threading.Barrier(nombre_composants)
        self.iteration = 0

    def composant(self, nom, nombre_iterations):
        """Simule un composant"""
        for i in range(nombre_iterations):
            # Calculer l'état du composant
            print(f"[{nom}] Calcul itération {i+1}...")
            time.sleep(0.5)

            # Attendre que tous les composants finissent l'itération
            print(f"[{nom}] Attente synchronisation...")
            self.barrier.wait()

            # Tous les composants sont synchronisés
            if threading.current_thread().name == "Thread-1":
                self.iteration += 1
                print(f"\n🔄 === Itération {self.iteration} terminée ===\n")

# Simulation avec 3 composants
sim = SimulationParallele(3)

threads = [
    threading.Thread(target=sim.composant, args=(f"Composant-{i}", 3), name=f"Thread-{i}")
    for i in range(3)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("✅ Simulation terminée")
```

---

## Comparaison Threading vs Asyncio

### Synchronisation en Threading

```python
import threading  
import time  

verrou = threading.Lock()  
compteur = 0  

def incrementer_threading():
    global compteur
    for _ in range(10000):
        with verrou:
            compteur += 1

threads = [threading.Thread(target=incrementer_threading) for _ in range(5)]  
debut = time.time()  

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Threading: {compteur} en {time.time() - debut:.2f}s")
```

### Synchronisation en Asyncio

```python
import asyncio

verrou_async = asyncio.Lock()  
compteur_async = 0  

async def incrementer_asyncio():
    global compteur_async
    for _ in range(10000):
        async with verrou_async:
            compteur_async += 1

async def main():
    debut = time.time()

    taches = [incrementer_asyncio() for _ in range(5)]
    await asyncio.gather(*taches)

    print(f"Asyncio: {compteur_async} en {time.time() - debut:.2f}s")

asyncio.run(main())
```

### Tableau comparatif

| Mécanisme | Threading | Asyncio |
|-----------|-----------|---------|
| **Lock** | `threading.Lock()` | `asyncio.Lock()` |
| **Semaphore** | `threading.Semaphore(n)` | `asyncio.Semaphore(n)` |
| **Event** | `threading.Event()` | `asyncio.Event()` |
| **Condition** | `threading.Condition()` | `asyncio.Condition()` |
| **Syntaxe** | `with lock:` | `async with lock:` |
| **Attente** | `event.wait()` | `await event.wait()` |

---

## Bonnes pratiques

### 1. Toujours utiliser des gestionnaires de contexte

```python
# ✅ Bon - libération automatique
with verrou:
    # Section critique
    pass

# ❌ Mauvais - risque d'oublier release()
verrou.acquire()
# Section critique
verrou.release()
```

### 2. Limiter la taille des sections critiques

```python
# ✅ Bon - section critique minimale
def traiter_donnees():
    # Travail sans lock
    resultat = calcul_complexe()

    # Lock uniquement pour la modification
    with verrou:
        donnees_partagees.append(resultat)

# ❌ Mauvais - section critique trop large
def traiter_donnees_mauvais():
    with verrou:
        # Tout est locké, même le calcul
        resultat = calcul_complexe()
        donnees_partagees.append(resultat)
```

### 3. Ordre d'acquisition cohérent pour éviter les deadlocks

```python
# Définir un ordre fixe pour les locks
def transfert_securise(compte_a, compte_b, montant):
    """Transfert sans risque de deadlock"""
    # Toujours acquérir les locks dans le même ordre
    premier = min(compte_a, compte_b, key=id)
    second = max(compte_a, compte_b, key=id)

    with premier.verrou:
        with second.verrou:
            if compte_a.solde >= montant:
                compte_a.solde -= montant
                compte_b.solde += montant
```

### 4. Utiliser des timeout

```python
import threading

verrou = threading.Lock()

def tentative_avec_timeout():
    """Essaie d'acquérir avec timeout"""
    if verrou.acquire(timeout=5.0):
        try:
            # Section critique
            pass
        finally:
            verrou.release()
    else:
        print("❌ Impossible d'acquérir le verrou dans le délai")
```

### 5. Documenter les invariants

```python
class CompteBancaire:
    """Compte bancaire thread-safe

    Invariant: self.solde >= 0 toujours maintenu sous le verrou
    """

    def __init__(self, solde):
        self.solde = solde
        self.verrou = threading.Lock()

    def retirer(self, montant):
        """Retire de l'argent (thread-safe)"""
        with self.verrou:
            # L'invariant est vérifié sous le verrou
            if self.solde >= montant:
                self.solde -= montant
                return True
            return False
```

---

## Erreurs courantes et solutions

### Erreur 1 : Oublier de libérer un verrou

```python
# ❌ Problème
verrou = threading.Lock()

def mauvaise_fonction():
    verrou.acquire()
    if condition_erreur:
        return  # Verrou jamais libéré!
    verrou.release()

# ✅ Solution
def bonne_fonction():
    with verrou:
        if condition_erreur:
            return  # Verrou automatiquement libéré
```

### Erreur 2 : Deadlock par ordre d'acquisition

```python
# ❌ Problème - deadlock possible
def thread_1():
    with lock_a:
        with lock_b:
            pass

def thread_2():
    with lock_b:  # Ordre différent!
        with lock_a:
            pass

# ✅ Solution - ordre cohérent
def thread_1():
    with lock_a:
        with lock_b:
            pass

def thread_2():
    with lock_a:  # Même ordre
        with lock_b:
            pass
```

### Erreur 3 : Race condition subtile

```python
# ❌ Problème
if len(liste_partagee) > 0:  # Check sans lock
    with verrou:
        element = liste_partagee.pop()  # Peut échouer!

# ✅ Solution
with verrou:
    if len(liste_partagee) > 0:  # Check sous le lock
        element = liste_partagee.pop()
```

### Erreur 4 : Utiliser Lock au lieu de RLock

```python
# ❌ Problème avec Lock
class Compteur:
    def __init__(self):
        self.valeur = 0
        self.verrou = threading.Lock()

    def incrementer(self):
        with self.verrou:
            self.valeur += 1

    def incrementer_deux_fois(self):
        with self.verrou:
            self.incrementer()  # Deadlock! Tente d'acquérir le lock 2x
            self.incrementer()

# ✅ Solution avec RLock
class Compteur:
    def __init__(self):
        self.valeur = 0
        self.verrou = threading.RLock()  # RLock au lieu de Lock

    def incrementer(self):
        with self.verrou:
            self.valeur += 1

    def incrementer_deux_fois(self):
        with self.verrou:
            self.incrementer()  # OK avec RLock
            self.incrementer()
```

---

## Exemple complet : Système de cache thread-safe

```python
import threading  
import time  
from typing import Any  

class CacheThreadSafe:
    """Cache thread-safe avec expiration automatique"""

    def __init__(self, duree_vie: int = 60):
        self.cache = {}  # {clé: (valeur, timestamp)}
        self.duree_vie = duree_vie
        self.verrou = threading.RLock()
        self.stats = {'hits': 0, 'misses': 0, 'expirations': 0}
        self.verrou_stats = threading.Lock()

    def get(self, cle: str) -> Any | None:
        """Récupère une valeur du cache"""
        with self.verrou:
            if cle not in self.cache:
                self._incrementer_stat('misses')
                return None

            valeur, timestamp = self.cache[cle]

            # Vérifier l'expiration
            if time.time() - timestamp > self.duree_vie:
                del self.cache[cle]
                self._incrementer_stat('expirations')
                self._incrementer_stat('misses')
                return None

            self._incrementer_stat('hits')
            return valeur

    def set(self, cle: str, valeur: Any):
        """Ajoute une valeur au cache"""
        with self.verrou:
            self.cache[cle] = (valeur, time.time())

    def clear(self):
        """Vide le cache"""
        with self.verrou:
            self.cache.clear()

    def get_stats(self) -> dict:
        """Récupère les statistiques"""
        with self.verrou_stats:
            return self.stats.copy()

    def _incrementer_stat(self, stat: str):
        """Incrémente une statistique (thread-safe)"""
        with self.verrou_stats:
            self.stats[stat] += 1

    def nettoyer_expires(self):
        """Nettoie les entrées expirées"""
        with self.verrou:
            cles_a_supprimer = []
            temps_actuel = time.time()

            for cle, (_, timestamp) in self.cache.items():
                if temps_actuel - timestamp > self.duree_vie:
                    cles_a_supprimer.append(cle)

            for cle in cles_a_supprimer:
                del self.cache[cle]

            return len(cles_a_supprimer)

def travailleur_cache(cache, worker_id, operations):
    """Thread qui utilise le cache"""
    for i in range(operations):
        cle = f"data_{i % 10}"  # 10 clés différentes

        # Tenter de récupérer
        valeur = cache.get(cle)

        if valeur is None:
            # Cache miss - calculer et stocker
            valeur = f"Résultat_calculé_par_{worker_id}_{i}"
            cache.set(cle, valeur)
            print(f"[Worker {worker_id}] Miss - Calculé: {cle}")
        else:
            print(f"[Worker {worker_id}] Hit - Trouvé: {cle}")

        time.sleep(0.1)

# Utilisation
cache = CacheThreadSafe(duree_vie=5)

# Créer plusieurs workers
threads = [
    threading.Thread(target=travailleur_cache, args=(cache, i, 20))
    for i in range(3)
]

print("🚀 Démarrage des workers")  
debut = time.time()  

for t in threads:
    t.start()
for t in threads:
    t.join()

duree = time.time() - debut

# Afficher les statistiques
stats = cache.get_stats()  
print(f"\n📊 Statistiques finales:")  
print(f"  • Hits: {stats['hits']}")  
print(f"  • Misses: {stats['misses']}")  
print(f"  • Expirations: {stats['expirations']}")  
print(f"  • Taux de hit: {stats['hits']/(stats['hits']+stats['misses'])*100:.1f}%")  
print(f"  • Durée totale: {duree:.2f}s")  
```

---

## Patterns avancés

### Pattern 1 : Double-checked locking

```python
import threading

class Singleton:
    """Singleton thread-safe avec double-checked locking"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Premier check sans lock (rapide)
        if cls._instance is None:
            # Second check avec lock (sûr)
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

### Pattern 2 : Read-Write Lock

```python
import threading

class ReadWriteLock:
    """Lock optimisé pour lectures multiples, écriture exclusive"""

    def __init__(self):
        self.lecteurs = 0
        self.verrou_lecteurs = threading.Lock()
        self.verrou_ecrivain = threading.Lock()

    def acquire_read(self):
        """Acquiert en lecture (partageable)"""
        with self.verrou_lecteurs:
            self.lecteurs += 1
            if self.lecteurs == 1:
                self.verrou_ecrivain.acquire()

    def release_read(self):
        """Libère la lecture"""
        with self.verrou_lecteurs:
            self.lecteurs -= 1
            if self.lecteurs == 0:
                self.verrou_ecrivain.release()

    def acquire_write(self):
        """Acquiert en écriture (exclusif)"""
        self.verrou_ecrivain.acquire()

    def release_write(self):
        """Libère l'écriture"""
        self.verrou_ecrivain.release()

# Utilisation
rwlock = ReadWriteLock()

def lecteur(donnees, reader_id):
    """Lit les données (plusieurs lecteurs ok)"""
    rwlock.acquire_read()
    try:
        print(f"[Lecteur {reader_id}] Lecture: {donnees}")
        time.sleep(0.5)
    finally:
        rwlock.release_read()

def ecrivain(donnees, writer_id, nouvelle_valeur):
    """Écrit les données (exclusif)"""
    rwlock.acquire_write()
    try:
        print(f"[Écrivain {writer_id}] Écriture: {nouvelle_valeur}")
        donnees.clear()
        donnees.append(nouvelle_valeur)
        time.sleep(1)
    finally:
        rwlock.release_write()
```

---

## Résumé des mécanismes

| Mécanisme | Quand l'utiliser | Exemple d'usage |
|-----------|------------------|-----------------|
| **Lock** | Accès exclusif simple | Modifier une variable partagée |
| **RLock** | Lock réentrant (appels imbriqués) | Méthodes qui s'appellent mutuellement |
| **Semaphore** | Limiter le nombre d'accès | Pool de connexions, bande passante |
| **Event** | Signaler un événement | Notification de fin de tâche |
| **Condition** | Attendre une condition spécifique | Producer/Consumer avec buffer |
| **Barrier** | Synchroniser plusieurs threads | Simulation en phases |

---

## Points clés à retenir

1. **Lock** = Protection basique pour l'accès exclusif à une ressource
2. **RLock** = Lock qui peut être acquis plusieurs fois par le même thread
3. **Semaphore** = Limite le nombre d'accès concurrent
4. **Event** = Notification simple entre threads
5. **Condition** = Attente d'une condition avec notification
6. **Barrier** = Synchronisation de groupe
7. **Toujours utiliser `with`** pour garantir la libération
8. **Minimiser les sections critiques** pour les performances
9. **Ordre cohérent** d'acquisition pour éviter les deadlocks
10. **Documenter** les invariants et les contraintes de synchronisation

---

## Ressources et prochaines étapes

**Pour aller plus loin** :
- Documentation officielle : `threading` et `asyncio.locks`
- Explorez `concurrent.futures` pour une abstraction plus haute
- Étudiez les patterns de concurrence avancés
- Apprenez les structures de données thread-safe : `queue.Queue`

**Dans la prochaine section** (8.4), nous explorerons les **patterns de concurrence** pour construire des systèmes robustes et scalables.

---

## Glossaire

- **Synchronisation** : Coordination entre threads/processus
- **Race Condition** : Résultat dépendant de l'ordre d'exécution
- **Deadlock** : Blocage mutuel de threads
- **Section Critique** : Code nécessitant un accès exclusif
- **Verrou (Lock)** : Mécanisme d'exclusion mutuelle
- **Atomicité** : Opération indivisible
- **Réentrant** : Peut être appelé récursivement par le même thread
- **Invariant** : Condition toujours vraie (sous protection)

⏭️ [Patterns de concurrence](/08-programmation-concurrente/04-patterns-de-concurrence.md)
