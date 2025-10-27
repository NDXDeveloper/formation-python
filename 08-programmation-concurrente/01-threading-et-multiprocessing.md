🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.1 Threading et Multiprocessing

## Introduction à la programmation concurrente

La **programmation concurrente** permet à votre programme d'exécuter plusieurs tâches en même temps (ou presque). C'est particulièrement utile pour :
- Effectuer plusieurs opérations d'entrée/sortie simultanément (téléchargements, requêtes réseau)
- Exploiter plusieurs cœurs de processeur pour des calculs intensifs
- Améliorer la réactivité de vos applications

Python propose deux approches principales pour la concurrence : **Threading** et **Multiprocessing**.

---

## Comprendre la différence : Threading vs Multiprocessing

### Threading (Threads)

Les **threads** sont des "fils d'exécution" qui partagent le même espace mémoire au sein d'un même processus.

**Analogie** : Imaginez une cuisine avec plusieurs cuisiniers qui partagent les mêmes ustensiles, le même réfrigérateur et le même plan de travail.

**Caractéristiques** :
- Partage la mémoire entre les threads
- Plus léger et rapide à créer
- Limité par le **GIL** (Global Interpreter Lock) en Python
- Idéal pour les tâches I/O (entrées/sorties) : lecture de fichiers, requêtes réseau, etc.

### Multiprocessing (Processus)

Le **multiprocessing** crée plusieurs processus indépendants, chacun avec sa propre mémoire.

**Analogie** : Imaginez plusieurs cuisines séparées, chacune avec son propre équipement et ses propres ressources.

**Caractéristiques** :
- Chaque processus a sa propre mémoire
- Plus lourd à créer et gérer
- Contourne le GIL et peut utiliser plusieurs cœurs CPU
- Idéal pour les calculs intensifs (CPU-bound)

---

## Le GIL (Global Interpreter Lock) - Pourquoi est-ce important ?

Le GIL est un verrou dans CPython (l'implémentation standard de Python) qui empêche plusieurs threads d'exécuter du code Python en même temps.

**Conséquence** : Pour les calculs intensifs, les threads ne sont pas vraiment parallèles en Python. C'est pourquoi on utilise le multiprocessing pour les tâches CPU-bound.

**Exception** : Les opérations I/O libèrent le GIL, donc les threads sont efficaces pour ces tâches.

---

## Threading - Exécution avec des Threads

### Module `threading`

Le module `threading` permet de créer et gérer des threads facilement.

### Exemple 1 : Premier thread simple

```python
import threading
import time

def afficher_nombres():
    """Fonction qui affiche des nombres"""
    for i in range(5):
        print(f"Nombre: {i}")
        time.sleep(1)

# Créer un thread
thread = threading.Thread(target=afficher_nombres)

# Démarrer le thread
thread.start()

# Le programme principal continue son exécution
print("Le thread a été lancé!")

# Attendre que le thread se termine
thread.join()
print("Le thread est terminé")
```

**Explication** :
- `Thread(target=...)` crée un nouveau thread qui exécutera la fonction spécifiée
- `start()` lance l'exécution du thread
- `join()` attend que le thread se termine avant de continuer

### Exemple 2 : Plusieurs threads simultanés

```python
import threading
import time

def telecharger_fichier(nom_fichier):
    """Simule le téléchargement d'un fichier"""
    print(f"Début du téléchargement de {nom_fichier}")
    time.sleep(2)  # Simule le temps de téléchargement
    print(f"Téléchargement de {nom_fichier} terminé")

# Créer plusieurs threads
fichiers = ["image1.jpg", "image2.jpg", "image3.jpg"]
threads = []

for fichier in fichiers:
    thread = threading.Thread(target=telecharger_fichier, args=(fichier,))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()

print("Tous les téléchargements sont terminés")
```

**Avantage** : Les trois "téléchargements" se font en parallèle, économisant du temps par rapport à une exécution séquentielle.

### Exemple 3 : Thread avec classe

```python
import threading
import time

class MonThread(threading.Thread):
    def __init__(self, nom, duree):
        super().__init__()
        self.nom = nom
        self.duree = duree

    def run(self):
        """Méthode exécutée quand le thread démarre"""
        print(f"{self.nom} commence")
        time.sleep(self.duree)
        print(f"{self.nom} termine")

# Créer et lancer des threads
thread1 = MonThread("Thread-1", 2)
thread2 = MonThread("Thread-2", 3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Tous les threads sont terminés")
```

### Exemple 4 : Partage de données entre threads (avec Lock)

Lorsque plusieurs threads accèdent aux mêmes données, il faut utiliser un **Lock** pour éviter les conflits.

```python
import threading

# Variable partagée
compteur = 0
# Verrou pour protéger l'accès
lock = threading.Lock()

def incrementer():
    global compteur
    for _ in range(100000):
        # Acquérir le verrou avant de modifier la variable
        with lock:
            compteur += 1

# Créer plusieurs threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=incrementer)
    threads.append(thread)
    thread.start()

# Attendre tous les threads
for thread in threads:
    thread.join()

print(f"Valeur finale du compteur: {compteur}")
# Sans lock, le résultat serait imprévisible
# Avec lock, on obtient toujours 500000
```

**Point important** : Le `with lock:` garantit qu'un seul thread à la fois peut modifier le compteur.

---

## Multiprocessing - Exécution avec des Processus

### Module `multiprocessing`

Le module `multiprocessing` permet de créer des processus indépendants, idéal pour les calculs intensifs.

### Exemple 1 : Premier processus simple

```python
import multiprocessing
import time

def calculer_carre(nombre):
    """Calcule le carré d'un nombre"""
    print(f"Calcul du carré de {nombre}")
    time.sleep(1)
    resultat = nombre ** 2
    print(f"Résultat: {resultat}")

if __name__ == '__main__':
    # Créer un processus
    processus = multiprocessing.Process(target=calculer_carre, args=(5,))

    # Démarrer le processus
    processus.start()

    print("Le processus a été lancé!")

    # Attendre que le processus se termine
    processus.join()
    print("Le processus est terminé")
```

**Note importante** : Le `if __name__ == '__main__':` est nécessaire sous Windows pour éviter des erreurs.

### Exemple 2 : Calculs parallèles avec Pool

La classe `Pool` permet de distribuer facilement des tâches sur plusieurs processus.

```python
import multiprocessing

def calculer_cube(nombre):
    """Calcule le cube d'un nombre"""
    return nombre ** 3

if __name__ == '__main__':
    nombres = [1, 2, 3, 4, 5, 6, 7, 8]

    # Créer un pool de 4 processus
    with multiprocessing.Pool(processes=4) as pool:
        resultats = pool.map(calculer_cube, nombres)

    print(f"Nombres: {nombres}")
    print(f"Cubes: {resultats}")
```

**Explication** :
- `Pool(processes=4)` crée 4 processus workers
- `map()` distribue automatiquement les calculs entre les processus
- C'est l'équivalent parallèle de la fonction `map()` standard

### Exemple 3 : Calcul intensif - Comparaison séquentiel vs parallèle

```python
import multiprocessing
import time

def calcul_intensif(n):
    """Fonction qui effectue un calcul coûteux"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def execution_sequentielle(nombres):
    """Exécution séquentielle"""
    debut = time.time()
    resultats = [calcul_intensif(n) for n in nombres]
    duree = time.time() - debut
    print(f"Séquentiel: {duree:.2f} secondes")
    return resultats

def execution_parallele(nombres):
    """Exécution parallèle"""
    debut = time.time()
    with multiprocessing.Pool() as pool:
        resultats = pool.map(calcul_intensif, nombres)
    duree = time.time() - debut
    print(f"Parallèle: {duree:.2f} secondes")
    return resultats

if __name__ == '__main__':
    nombres = [5000000] * 8  # 8 calculs identiques

    print("Calculs intensifs:")
    execution_sequentielle(nombres)
    execution_parallele(nombres)
```

**Résultat typique** : L'exécution parallèle est significativement plus rapide sur un CPU multi-cœurs.

### Exemple 4 : Communication entre processus avec Queue

Les processus ne partagent pas la mémoire, il faut utiliser des mécanismes de communication comme `Queue`.

```python
import multiprocessing
import time

def producteur(queue, nombre_items):
    """Produit des données et les met dans la queue"""
    for i in range(nombre_items):
        item = f"Item-{i}"
        queue.put(item)
        print(f"Produit: {item}")
        time.sleep(0.5)
    queue.put(None)  # Signal de fin

def consommateur(queue):
    """Consomme les données de la queue"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consommé: {item}")
        time.sleep(1)

if __name__ == '__main__':
    # Créer une queue partagée
    queue = multiprocessing.Queue()

    # Créer les processus
    proc_producteur = multiprocessing.Process(target=producteur, args=(queue, 5))
    proc_consommateur = multiprocessing.Process(target=consommateur, args=(queue,))

    # Démarrer les processus
    proc_producteur.start()
    proc_consommateur.start()

    # Attendre la fin
    proc_producteur.join()
    proc_consommateur.join()

    print("Communication terminée")
```

---

## Quand utiliser Threading ou Multiprocessing ?

### Utilisez **Threading** pour :

✅ **Opérations I/O** (Entrées/Sorties)
- Téléchargement de fichiers
- Requêtes réseau/API
- Lecture/écriture de fichiers
- Connexions bases de données

✅ **Tâches qui attendent beaucoup**
- Serveurs web qui gèrent plusieurs connexions
- Applications avec interface graphique

**Exemple typique** : Un scraper web qui télécharge 100 pages simultanément.

### Utilisez **Multiprocessing** pour :

✅ **Calculs intensifs** (CPU-bound)
- Traitement d'images
- Calculs mathématiques complexes
- Analyse de données volumineuses
- Encodage vidéo/audio

✅ **Besoin de vraie parallélisation**
- Exploitation de plusieurs cœurs CPU
- Calculs scientifiques

**Exemple typique** : Traiter 1000 images pour appliquer des filtres.

---

## Tableau récapitulatif

| Critère | Threading | Multiprocessing |
|---------|-----------|-----------------|
| **Mémoire** | Partagée | Séparée |
| **Création** | Rapide | Plus lent |
| **GIL** | Limité par le GIL | Contourne le GIL |
| **Idéal pour** | I/O-bound | CPU-bound |
| **Communication** | Simple (mémoire partagée) | Plus complexe (Queue, Pipe) |
| **Overhead** | Faible | Plus élevé |
| **Multi-cœurs** | Non exploité pour calculs | Pleinement exploité |

---

## Bonnes pratiques

### 1. Toujours utiliser `if __name__ == '__main__':`

Avec multiprocessing, c'est essentiel pour éviter des erreurs, surtout sous Windows :

```python
if __name__ == '__main__':
    # Code multiprocessing ici
    pass
```

### 2. Utiliser des gestionnaires de contexte

Préférez `with` pour gérer automatiquement la fermeture des ressources :

```python
# Bon
with multiprocessing.Pool() as pool:
    resultats = pool.map(fonction, donnees)

# Moins bon (il faut fermer manuellement)
pool = multiprocessing.Pool()
resultats = pool.map(fonction, donnees)
pool.close()
pool.join()
```

### 3. Limiter le nombre de threads/processus

Ne créez pas un thread/processus par élément. Utilisez un Pool avec un nombre raisonnable :

```python
# Bon - pool de 4 processus pour traiter 1000 items
with multiprocessing.Pool(processes=4) as pool:
    resultats = pool.map(fonction, mes_1000_items)

# Mauvais - créer 1000 processus
for item in mes_1000_items:
    Process(target=fonction, args=(item,)).start()  # ❌
```

### 4. Protéger les données partagées avec Lock

En threading, utilisez toujours des verrous pour les variables partagées :

```python
lock = threading.Lock()

def modifier_variable_partagee():
    with lock:
        # Modification sécurisée
        variable_globale += 1
```

### 5. Gérer les exceptions

Les exceptions dans les threads/processus peuvent être silencieuses. Gérez-les :

```python
import threading

def fonction_avec_erreur():
    try:
        # Code qui peut échouer
        resultat = 1 / 0
    except Exception as e:
        print(f"Erreur dans le thread: {e}")

thread = threading.Thread(target=fonction_avec_erreur)
thread.start()
thread.join()
```

---

## Exemple pratique complet : Téléchargeur parallèle

Voici un exemple réaliste qui combine les concepts vus :

```python
import threading
import time
from typing import List

class TelechargeParallele:
    """Gestionnaire de téléchargements parallèles"""

    def __init__(self, max_threads: int = 5):
        self.max_threads = max_threads
        self.resultats = []
        self.lock = threading.Lock()

    def telecharger_fichier(self, url: str):
        """Simule le téléchargement d'un fichier"""
        print(f"[Début] Téléchargement de {url}")

        # Simulation du téléchargement
        duree = 2  # Secondes
        time.sleep(duree)

        # Sauvegarder le résultat de manière sécurisée
        with self.lock:
            self.resultats.append({
                'url': url,
                'statut': 'succès',
                'duree': duree
            })

        print(f"[Terminé] {url}")

    def telecharger_liste(self, urls: List[str]):
        """Télécharge une liste d'URLs en parallèle"""
        threads = []

        print(f"Démarrage de {len(urls)} téléchargements...")
        debut = time.time()

        # Créer et démarrer les threads
        for url in urls:
            thread = threading.Thread(target=self.telecharger_fichier, args=(url,))
            threads.append(thread)
            thread.start()

            # Limiter le nombre de threads simultanés
            if len(threads) >= self.max_threads:
                threads[0].join()
                threads.pop(0)

        # Attendre tous les threads restants
        for thread in threads:
            thread.join()

        duree_totale = time.time() - debut
        print(f"\n✓ Tous les téléchargements terminés en {duree_totale:.2f}s")
        return self.resultats

# Utilisation
if __name__ == '__main__':
    urls = [
        "http://example.com/fichier1.pdf",
        "http://example.com/fichier2.pdf",
        "http://example.com/fichier3.pdf",
        "http://example.com/fichier4.pdf",
        "http://example.com/fichier5.pdf",
    ]

    telechargeur = TelechargeParallele(max_threads=3)
    resultats = telechargeur.telecharger_liste(urls)

    print(f"\nRésumé: {len(resultats)} fichiers téléchargés")
```

---

## Points clés à retenir

1. **Threading** = Idéal pour les tâches I/O (réseau, fichiers)
2. **Multiprocessing** = Idéal pour les calculs intensifs (CPU)
3. Le **GIL** limite le threading pour les calculs, pas pour l'I/O
4. Utilisez **Lock** pour protéger les données partagées en threading
5. Utilisez **Queue** pour la communication entre processus
6. **Pool** simplifie la parallélisation de listes de tâches
7. Toujours mesurer les performances avant/après parallélisation

---

## Ressources et prochaines étapes

Dans la section suivante (8.2), nous explorerons la **programmation asynchrone avec asyncio**, une alternative moderne au threading pour les opérations I/O.

**Pour aller plus loin** :
- Documentation officielle : `threading` et `multiprocessing`
- Explorez `concurrent.futures` pour une API unifiée
- Apprenez `asyncio` pour une approche asynchrone moderne

⏭️ [Programmation asynchrone avec asyncio](/08-programmation-concurrente/02-programmation-asynchrone-asyncio.md)
