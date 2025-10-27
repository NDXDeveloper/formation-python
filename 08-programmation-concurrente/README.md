🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8. Programmation Concurrente

## Introduction

Bienvenue dans le chapitre sur la **programmation concurrente** ! C'est un sujet qui peut sembler intimidant au premier abord, mais qui est essentiel pour créer des programmes modernes, rapides et efficaces.

### Qu'est-ce que la programmation concurrente ?

La **programmation concurrente** permet à un programme d'exécuter plusieurs tâches "en même temps" (ou presque). C'est un peu comme jongler avec plusieurs balles : vous ne tenez jamais toutes les balles en même temps, mais vous créez l'illusion de le faire en les manipulant très rapidement.

**En termes simples** : Au lieu de faire les choses une par une (séquentiellement), la programmation concurrente vous permet de faire plusieurs choses à la fois (en parallèle).

---

## Pourquoi la programmation concurrente ?

### Le monde est concurrent

Dans la vie réelle, les choses se passent en parallèle :
- Dans un restaurant, plusieurs serveurs s'occupent de différents clients en même temps
- Sur une route, des centaines de voitures circulent simultanément
- Dans une entreprise, les employés travaillent tous en parallèle

Vos programmes doivent souvent refléter cette réalité !

### Exemples concrets d'utilisation

**1. Serveur web**
```
Utilisateur A fait une requête → En traitement
Utilisateur B fait une requête → En traitement (en même temps!)
Utilisateur C fait une requête → En traitement (en même temps!)
```

Sans concurrence, l'utilisateur B devrait attendre que A soit servi, puis C devrait attendre B, etc. Avec concurrence, tous sont traités simultanément.

**2. Téléchargement de fichiers**
```
Fichier 1: ████████░░░░░░░░ 50%
Fichier 2: ███████████░░░░░ 70%
Fichier 3: █████░░░░░░░░░░░ 30%
```

Au lieu de télécharger les fichiers un par un, vous les téléchargez tous en même temps.

**3. Interface graphique**
```
Thread principal: Gère l'interface (boutons, fenêtres)
Thread secondaire: Effectue un calcul long
```

Sans concurrence, votre interface "gèlerait" pendant les calculs longs. Avec concurrence, l'interface reste réactive.

---

## Concepts fondamentaux

### 1. Programmation séquentielle (classique)

C'est la façon dont vous avez probablement toujours programmé jusqu'ici.

```python
# Programmation séquentielle
def preparer_petit_dejeuner():
    faire_cafe()      # 3 minutes
    faire_toasts()    # 2 minutes
    faire_oeufs()     # 4 minutes
    # Total: 9 minutes
```

**Caractéristiques** :
- Simple à comprendre et à déboguer
- Les instructions s'exécutent dans l'ordre
- Une instruction à la fois

### 2. Programmation concurrente

Plusieurs tâches progressent en même temps (ou semblent le faire).

```python
# Programmation concurrente
def preparer_petit_dejeuner_concurrent():
    # Tout démarre en même temps!
    lancer_cafe()     # En parallèle
    lancer_toasts()   # En parallèle
    lancer_oeufs()    # En parallèle
    # Total: 4 minutes (le temps de la tâche la plus longue)
```

**Caractéristiques** :
- Plus complexe mais plus efficace
- Plusieurs choses se passent "en même temps"
- Peut être plus rapide

---

## Concurrence vs Parallélisme

Ces deux termes sont souvent confondus, mais ils sont différents :

### Concurrence

**Définition** : Gérer plusieurs tâches en même temps (mais pas nécessairement en les exécutant simultanément).

**Analogie** : Un seul jongleur qui jongle avec plusieurs balles. Il ne tient jamais toutes les balles en même temps, mais il passe rapidement de l'une à l'autre.

```
Processeur unique qui bascule entre les tâches:
Temps: |--A--|--B--|--A--|--C--|--B--|--A--|
```

### Parallélisme

**Définition** : Exécuter plusieurs tâches **vraiment** en même temps, sur plusieurs processeurs.

**Analogie** : Plusieurs jongleurs, chacun jonglant avec ses propres balles.

```
Plusieurs processeurs travaillant simultanément:
CPU 1: |------A------|------A------|
CPU 2: |------B------|------B------|
CPU 3: |------C------|------C------|
```

### Tableau comparatif

| Aspect | Concurrence | Parallélisme |
|--------|------------|--------------|
| **Définition** | Gérer plusieurs tâches | Exécuter plusieurs tâches simultanément |
| **Exécution** | Une tâche à la fois (bascule rapide) | Plusieurs tâches vraiment en même temps |
| **Matériel** | Fonctionne sur 1 CPU | Nécessite plusieurs CPUs/cœurs |
| **Exemple** | Serveur web gérant 1000 connexions | Calcul scientifique sur 8 cœurs |
| **But** | Gérer plusieurs choses, ne pas bloquer | Accélérer les calculs |

---

## Les différentes approches en Python

Python offre plusieurs outils pour la programmation concurrente. Voici un aperçu :

### 1. Threading (Fils d'exécution)

**Qu'est-ce que c'est ?** Des "fils" d'exécution qui partagent la même mémoire.

**Idéal pour** :
- ✅ Opérations d'entrée/sortie (I/O) : fichiers, réseau, bases de données
- ✅ Tâches qui attendent beaucoup (téléchargements, requêtes API)

**Pas idéal pour** :
- ❌ Calculs intensifs (limité par le GIL de Python)

```python
import threading

def tache():
    print("Tâche exécutée")

# Créer un thread
thread = threading.Thread(target=tache)
thread.start()
```

### 2. Multiprocessing (Multi-processus)

**Qu'est-ce que c'est ?** Plusieurs processus indépendants, chacun avec sa propre mémoire.

**Idéal pour** :
- ✅ Calculs intensifs (CPU-bound)
- ✅ Exploiter plusieurs cœurs du processeur

**Pas idéal pour** :
- ❌ Tâches avec beaucoup de partage de données (communication coûteuse)

```python
import multiprocessing

def tache():
    print("Tâche exécutée dans un processus")

# Créer un processus
process = multiprocessing.Process(target=tache)
process.start()
```

### 3. Asyncio (Asynchrone)

**Qu'est-ce que c'est ?** Programmation asynchrone avec `async`/`await`.

**Idéal pour** :
- ✅ Beaucoup d'opérations I/O simultanées
- ✅ Applications réseau (serveurs, clients)
- ✅ Scalabilité (des milliers de connexions)

**Pas idéal pour** :
- ❌ Calculs intensifs

```python
import asyncio

async def tache():
    print("Tâche asynchrone")
    await asyncio.sleep(1)

# Exécuter
asyncio.run(tache())
```

---

## Comprendre le GIL (Global Interpreter Lock)

Le **GIL** est un verrou dans Python qui empêche plusieurs threads d'exécuter du code Python en même temps.

### Pourquoi le GIL existe ?

Le GIL protège les structures de données internes de Python et rend l'implémentation plus simple. C'est une caractéristique de CPython (l'implémentation standard de Python).

### Impact du GIL

```python
# Threading avec calculs (limité par le GIL)
# Les threads s'exécutent l'un après l'autre pour les calculs
def calcul_intensif():
    for i in range(10000000):
        x = i * i

# ❌ Pas vraiment parallèle à cause du GIL
threads = [threading.Thread(target=calcul_intensif) for _ in range(4)]

# Multiprocessing (contourne le GIL)
# ✅ Vraiment parallèle car chaque processus a son propre interpréteur
processes = [multiprocessing.Process(target=calcul_intensif) for _ in range(4)]
```

### Tableau récapitulatif du GIL

| Type d'opération | Threading | Multiprocessing |
|------------------|-----------|-----------------|
| **I/O** (fichiers, réseau) | ✅ Efficace (GIL libéré) | ✅ Efficace (mais overhead) |
| **Calculs** (CPU-bound) | ❌ Limité par le GIL | ✅ Vraiment parallèle |
| **Création** | Rapide | Plus lent |
| **Mémoire** | Partagée | Séparée |

---

## Types de tâches : I/O-bound vs CPU-bound

Comprendre la différence est crucial pour choisir la bonne approche.

### I/O-bound (Limité par les entrées/sorties)

**Définition** : Le programme passe la majorité de son temps à **attendre** des données.

**Exemples** :
- Télécharger des fichiers depuis Internet
- Lire/écrire dans des fichiers
- Requêtes à une base de données
- Appels API

**Caractéristique** : Le CPU est souvent inactif, en attente.

**Solution recommandée** : Threading ou Asyncio

```python
import time

# Exemple I/O-bound
def telecharger_fichier(url):
    print(f"Téléchargement de {url}...")
    time.sleep(2)  # Simule l'attente réseau
    print(f"{url} téléchargé")
```

### CPU-bound (Limité par le processeur)

**Définition** : Le programme passe la majorité de son temps à **calculer**.

**Exemples** :
- Calculs mathématiques complexes
- Traitement d'images
- Encodage vidéo
- Algorithmes de machine learning

**Caractéristique** : Le CPU travaille à 100%.

**Solution recommandée** : Multiprocessing

```python
# Exemple CPU-bound
def calculer():
    total = 0
    for i in range(10000000):
        total += i * i  # Calcul intensif
    return total
```

---

## Quand utiliser quoi ? Guide de décision

Voici un arbre de décision simple pour choisir la bonne approche :

```
Vous avez besoin de concurrence ?
│
├─ Votre tâche est I/O-bound (beaucoup d'attente) ?
│  │
│  ├─ Oui → Beaucoup de connexions simultanées ?
│  │  ├─ Oui → Asyncio (milliers de connexions)
│  │  └─ Non → Threading (dizaines de connexions)
│  │
│  └─ Non → Votre tâche est CPU-bound (calculs) ?
│     └─ Oui → Multiprocessing
│
└─ Besoin de synchronisation complexe ?
   └─ Patterns de concurrence (chapitre 8.4)
```

### Tableau récapitulatif

| Critère | Threading | Multiprocessing | Asyncio |
|---------|-----------|-----------------|---------|
| **Type de tâche** | I/O-bound | CPU-bound | I/O-bound |
| **Nombre de tâches** | Dizaines | Limité par CPUs | Milliers |
| **Complexité** | ⭐⭐ Moyenne | ⭐⭐ Moyenne | ⭐⭐⭐ Plus élevée |
| **Overhead** | Faible | Élevé | Très faible |
| **Partage mémoire** | ✅ Facile | ❌ Difficile | ✅ Facile |
| **Débogage** | ⭐⭐ Moyen | ⭐⭐ Moyen | ⭐⭐⭐ Plus difficile |

---

## Les défis de la programmation concurrente

La programmation concurrente n'est pas magique. Elle apporte son lot de défis :

### 1. Race Conditions (Conditions de course)

Quand plusieurs threads accèdent aux mêmes données sans coordination.

```python
# Problème potentiel
compteur = 0

def incrementer():
    global compteur
    compteur += 1  # Pas atomique!

# Deux threads peuvent lire la même valeur et écraser leurs modifications
```

### 2. Deadlocks (Interblocages)

Quand des threads s'attendent mutuellement et se bloquent.

```
Thread A détient la ressource 1, veut la ressource 2
Thread B détient la ressource 2, veut la ressource 1
→ Les deux threads sont bloqués indéfiniment!
```

### 3. Complexité du débogage

Les bugs concurrents sont difficiles à reproduire car ils dépendent du timing.

```python
# Ce bug peut apparaître 1 fois sur 1000 exécutions
# Très difficile à déboguer!
```

### 4. Overhead (Surcharge)

Créer des threads/processus a un coût en temps et en mémoire.

```python
# ❌ Mauvais : Créer 10000 threads
for i in range(10000):
    Thread(target=tache).start()

# ✅ Bon : Pool de workers
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(tache, range(10000))
```

---

## Exemples comparatifs

Pour bien comprendre l'impact de la concurrence, voici quelques exemples comparatifs.

### Exemple 1 : Téléchargement de fichiers

**Sans concurrence** :
```python
import time

def telecharger_sequentiel(urls):
    for url in urls:
        print(f"Téléchargement {url}...")
        time.sleep(2)  # Simule le téléchargement
    # 5 URLs × 2s = 10 secondes
```

**Avec threading** :
```python
import threading
import time

def telecharger_concurrent(urls):
    threads = []
    for url in urls:
        t = threading.Thread(target=telecharger_un, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    # 5 URLs en parallèle = ~2 secondes!
```

### Exemple 2 : Calculs intensifs

**Sans concurrence** :
```python
def calculer_sequentiel(nombres):
    resultats = []
    for n in nombres:
        resultats.append(n ** 2)
    # 100 calculs en séquence
```

**Avec multiprocessing** :
```python
from multiprocessing import Pool

def calculer_parallele(nombres):
    with Pool() as pool:
        resultats = pool.map(lambda x: x ** 2, nombres)
    # 100 calculs répartis sur 8 cœurs = 8× plus rapide!
```

---

## Performance : Mesurer l'amélioration

Il est important de **mesurer** avant d'optimiser. La concurrence n'est pas toujours plus rapide !

### Loi d'Amdahl

**Principe** : Le gain de performance est limité par la partie séquentielle du programme.

Si seulement 50% de votre programme peut être parallélisé, vous ne pourrez jamais obtenir plus de 2× d'amélioration, même avec 1000 CPUs.

```
Speedup maximal = 1 / (S + P/N)

Où:
S = Partie séquentielle (0.5 = 50%)
P = Partie parallélisable (0.5 = 50%)
N = Nombre de processeurs
```

### Quand la concurrence est contre-productive

```python
# ❌ Mauvais : Overhead plus coûteux que le gain
def tache_rapide():
    return 2 + 2

# Créer un thread pour ça est plus lent que l'exécution directe!
```

**Règle d'or** : La concurrence est utile quand le temps de la tâche >> temps de création du thread/processus.

---

## Structure du chapitre

Ce chapitre est organisé en 4 sections principales :

### 8.1 Threading et Multiprocessing
- Les bases du threading
- Utilisation du multiprocessing
- Quand utiliser l'un ou l'autre
- Pool de workers avec `concurrent.futures`

### 8.2 Programmation asynchrone avec asyncio
- Concepts : async/await
- Event loop
- Coroutines et tâches
- Bibliothèques asynchrones

### 8.3 Gestion des verrous et synchronisation
- Lock, RLock, Semaphore
- Event et Condition
- Éviter les race conditions et deadlocks
- Patterns de synchronisation

### 8.4 Patterns de concurrence
- Producer-Consumer
- Worker Pool
- Pipeline
- Map-Reduce
- Et plus encore...

---

## Conseils pour débuter

### 1. Commencez simple

Ne vous lancez pas directement dans la programmation concurrente pour tout. Commencez par du code séquentiel, puis optimisez si nécessaire.

```python
# Étape 1: Version simple qui fonctionne
def traiter_donnees(donnees):
    return [traiter_item(item) for item in donnees]

# Étape 2: Identifier le goulot d'étranglement
# Étape 3: Ajouter la concurrence seulement si bénéfique
```

### 2. Mesurez toujours

Utilisez des outils pour mesurer les performances :

```python
import time

def mesurer_temps(fonction):
    debut = time.time()
    resultat = fonction()
    duree = time.time() - debut
    print(f"Temps: {duree:.2f}s")
    return resultat
```

### 3. Comprenez le type de votre tâche

Avant de choisir une approche :
- ❓ Ma tâche est-elle I/O-bound ou CPU-bound ?
- ❓ Combien de tâches ai-je besoin d'exécuter ?
- ❓ Ai-je besoin de partager des données ?

### 4. Utilisez des abstractions de haut niveau

Préférez les outils modernes qui cachent la complexité :

```python
# ✅ Bon : Utilise concurrent.futures
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    resultats = executor.map(fonction, donnees)

# ❌ Moins bon : Gestion manuelle des threads
threads = []
for donnee in donnees:
    t = threading.Thread(target=fonction, args=(donnee,))
    threads.append(t)
    t.start()
# ... gérer la synchronisation manuellement
```

### 5. Gérez les erreurs

La gestion d'erreurs est encore plus importante en concurrent :

```python
def worker_robuste():
    try:
        # Code qui peut échouer
        resultat = tache_risquee()
    except Exception as e:
        print(f"Erreur: {e}")
        # Log, notification, retry...
```

---

## Vocabulaire essentiel

Avant de continuer, voici les termes clés que vous rencontrerez :

| Terme | Définition |
|-------|------------|
| **Thread** | Fil d'exécution au sein d'un processus |
| **Processus** | Programme en cours d'exécution avec sa propre mémoire |
| **Concurrence** | Gérer plusieurs tâches (pas forcément simultanées) |
| **Parallélisme** | Exécuter plusieurs tâches vraiment en même temps |
| **I/O-bound** | Limité par les entrées/sorties (attente) |
| **CPU-bound** | Limité par la puissance de calcul |
| **Race condition** | Résultat dépendant de l'ordre d'exécution |
| **Deadlock** | Blocage mutuel de threads/processus |
| **Lock** | Verrou pour protéger l'accès à une ressource |
| **Coroutine** | Fonction qui peut être mise en pause et reprise |
| **Event loop** | Boucle qui gère l'exécution des tâches asynchrones |
| **GIL** | Global Interpreter Lock (limite le threading en Python) |

---

## Cas d'usage réels

Pour vous inspirer, voici quelques applications concrètes de la programmation concurrente :

### Applications web
- **Flask/Django** : Gérer des milliers de requêtes HTTP simultanées
- **FastAPI** : API haute performance avec asyncio

### Traitement de données
- **Web scraping** : Télécharger des centaines de pages en parallèle
- **ETL** : Extract, Transform, Load de données

### Calcul scientifique
- **NumPy/Pandas** : Opérations vectorisées sur de grandes matrices
- **Machine Learning** : Entraînement de modèles sur plusieurs cœurs

### Systèmes temps-réel
- **Jeux vidéo** : Rendu graphique, physique, IA en parallèle
- **Trading** : Traiter des millions de transactions par seconde

### IoT et automatisation
- **Monitoring** : Surveiller des centaines de capteurs simultanément
- **Domotique** : Gérer plusieurs appareils en temps réel

---

## À quoi s'attendre dans ce chapitre

### Ce que vous allez apprendre

✅ Les trois approches principales : Threading, Multiprocessing, Asyncio
✅ Comment choisir la bonne approche pour votre problème
✅ Les mécanismes de synchronisation (locks, semaphores, etc.)
✅ Des patterns éprouvés pour résoudre des problèmes courants
✅ Comment éviter les pièges et les bugs concurrents
✅ Des exemples pratiques et réalistes

### Ce que vous serez capable de faire

À la fin de ce chapitre, vous pourrez :
- Accélérer vos programmes avec threading et multiprocessing
- Créer des applications web asynchrones performantes
- Gérer correctement le partage de données entre threads
- Implémenter des patterns de concurrence courants
- Déboguer les problèmes concurrents basiques

---

## Prérequis

Avant de plonger dans ce chapitre, assurez-vous d'être à l'aise avec :

✅ **Python de base** : fonctions, classes, modules
✅ **Gestion d'erreurs** : try/except
✅ **Compréhension des boucles** : for, while
✅ **Concepts de programmation** : variables, types de données

**Pas besoin** :
❌ Connaissances en systèmes d'exploitation
❌ Expérience préalable en concurrence
❌ Mathématiques avancées

---

## Ressources complémentaires

Pour approfondir vos connaissances en programmation concurrente :

### Documentation officielle Python
- `threading` : https://docs.python.org/3/library/threading.html
- `multiprocessing` : https://docs.python.org/3/library/multiprocessing.html
- `asyncio` : https://docs.python.org/3/library/asyncio.html
- `concurrent.futures` : https://docs.python.org/3/library/concurrent.futures.html

### Livres recommandés
- "Python Concurrency with asyncio" de Matthew Fowler
- "High Performance Python" de Micha Gorelick et Ian Ozsvald

### Outils de mesure de performance
- `time` : Mesure de temps basique
- `cProfile` : Profilage de code
- `line_profiler` : Profilage ligne par ligne

---

## Prêt à commencer ?

La programmation concurrente peut sembler complexe, mais avec une approche progressive et des exemples concrets, vous maîtriserez rapidement ces concepts puissants.

**Conseil final** : Ne vous précipitez pas. Prenez le temps de comprendre chaque concept avant de passer au suivant. La programmation concurrente demande une réflexion différente, mais une fois que vous "l'avez", c'est un super-pouvoir qui transformera vos programmes !

Dans la section suivante (8.1), nous commencerons par les bases du **Threading et Multiprocessing** avec des exemples pratiques et progressifs.

**Bonne lecture et bon codage ! 🚀**

⏭️ [Threading et multiprocessing](/08-programmation-concurrente/01-threading-et-multiprocessing.md)
