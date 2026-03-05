🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 8.2 Programmation Asynchrone avec Asyncio

## Introduction à la programmation asynchrone

La **programmation asynchrone** est une façon d'écrire du code qui peut "mettre en pause" certaines opérations pendant qu'elles attendent, et continuer à faire autre chose en attendant.

### Analogie du restaurant

Imaginez un serveur dans un restaurant :

**Approche synchrone (classique)** :
1. Prendre la commande du client 1
2. Attendre que le plat soit prêt ⏳ (le serveur reste planté en cuisine)
3. Servir le client 1
4. Prendre la commande du client 2
5. Attendre... ⏳

**Approche asynchrone** :
1. Prendre la commande du client 1
2. Pendant que le plat se prépare, prendre la commande du client 2
3. Pendant que les deux plats cuisent, prendre la commande du client 3
4. Dès qu'un plat est prêt, le servir
5. Continue de jongler entre les clients

Le serveur ne reste jamais inactif ! C'est exactement ce que fait `asyncio`.

---

## Pourquoi utiliser asyncio ?

### Comparaison des approches

| Approche | Idéal pour | Complexité | Performance I/O |
|----------|-----------|------------|-----------------|
| **Synchrone** | Code simple, tâches séquentielles | ⭐ Très simple | ❌ Lent |
| **Threading** | I/O avec partage de mémoire | ⭐⭐ Moyen | ✅ Bon |
| **Asyncio** | Nombreuses opérations I/O | ⭐⭐⭐ Plus complexe | ✅✅ Excellent |
| **Multiprocessing** | Calculs intensifs CPU | ⭐⭐ Moyen | ❌ Non pertinent |

### Quand utiliser asyncio ?

✅ **Parfait pour** :
- Serveurs web avec nombreuses connexions simultanées
- Scraping de nombreux sites web
- Applications de chat en temps réel
- APIs avec nombreuses requêtes parallèles
- Clients de bases de données avec beaucoup de requêtes

❌ **Pas recommandé pour** :
- Calculs intensifs (CPU-bound)
- Code très simple avec peu d'I/O
- Quand vous débutez en Python (commencez par le code synchrone)

---

## Concepts fondamentaux

### 1. Coroutine (Fonction asynchrone)

Une **coroutine** est une fonction qui peut être mise en pause et reprise.

```python
import asyncio

# Fonction normale
def fonction_normale():
    return "Bonjour"

# Coroutine (fonction asynchrone)
async def fonction_asynchrone():
    return "Bonjour asynchrone"
```

Le mot-clé `async` devant `def` transforme une fonction en coroutine.

### 2. await - Attendre sans bloquer

Le mot-clé `await` permet d'attendre le résultat d'une coroutine **sans bloquer** le reste du programme.

```python
async def dire_bonjour():
    await asyncio.sleep(1)  # Attend 1 seconde sans bloquer
    print("Bonjour!")
```

**Important** : On ne peut utiliser `await` que dans une fonction `async`.

### 3. Event Loop - La boucle d'événements

L'**event loop** est le chef d'orchestre qui gère toutes les coroutines. C'est lui qui décide quoi exécuter et quand.

```python
import asyncio

async def main():
    print("Programme asynchrone")

# Lancer l'event loop
asyncio.run(main())
```

`asyncio.run()` crée l'event loop, exécute la coroutine, puis ferme proprement l'event loop.

---

## Premier programme asynchrone

### Exemple 1 : Hello World asynchrone

```python
import asyncio

async def dire_bonjour(nom, delai):
    """Fonction asynchrone simple"""
    print(f"Bonjour {nom}! (attente de {delai}s)")
    await asyncio.sleep(delai)  # Pause non-bloquante
    print(f"Au revoir {nom}!")

async def main():
    """Fonction principale"""
    await dire_bonjour("Alice", 2)

# Point d'entrée
asyncio.run(main())
```

**Sortie** :
```
Bonjour Alice! (attente de 2s)
[attend 2 secondes]
Au revoir Alice!
```

Pour l'instant, c'est séquentiel. Voyons comment exécuter plusieurs choses en parallèle.

---

## Exécution concurrente avec asyncio

### asyncio.create_task() - Créer une tâche

Pour exécuter plusieurs coroutines en même temps, on crée des **tâches** (tasks).

### Exemple 2 : Plusieurs tâches en parallèle

```python
import asyncio  
import time  

async def faire_cafe(nom):
    """Simule la préparation d'un café"""
    print(f"☕ {nom}: Début préparation café")
    await asyncio.sleep(2)  # Prend 2 secondes
    print(f"☕ {nom}: Café prêt!")
    return f"Café pour {nom}"

async def main():
    """Exécute plusieurs préparations en parallèle"""
    debut = time.time()

    # Créer plusieurs tâches
    tache1 = asyncio.create_task(faire_cafe("Alice"))
    tache2 = asyncio.create_task(faire_cafe("Bob"))
    tache3 = asyncio.create_task(faire_cafe("Charlie"))

    # Attendre que toutes les tâches soient terminées
    resultat1 = await tache1
    resultat2 = await tache2
    resultat3 = await tache3

    duree = time.time() - debut
    print(f"\n✅ Tous les cafés prêts en {duree:.2f}s")
    print(f"Résultats: {resultat1}, {resultat2}, {resultat3}")

asyncio.run(main())
```

**Sortie** :
```
☕ Alice: Début préparation café
☕ Bob: Début préparation café
☕ Charlie: Début préparation café
[attend ~2 secondes]
☕ Alice: Café prêt!
☕ Bob: Café prêt!
☕ Charlie: Café prêt!

✅ Tous les cafés prêts en 2.00s
```

**Magie** : Les 3 cafés sont préparés en 2 secondes au lieu de 6 ! Ils se préparent en parallèle.

---

## asyncio.gather() - Attendre plusieurs coroutines

`asyncio.gather()` est une façon plus élégante d'exécuter plusieurs coroutines en parallèle.

### Exemple 3 : Utilisation de gather()

```python
import asyncio

async def telecharger_fichier(nom, taille_mo):
    """Simule le téléchargement d'un fichier"""
    duree = taille_mo * 0.5  # 0.5s par Mo
    print(f"📥 Début téléchargement: {nom} ({taille_mo} Mo)")
    await asyncio.sleep(duree)
    print(f"✅ Téléchargé: {nom}")
    return f"{nom} ({taille_mo} Mo)"

async def main():
    """Télécharge plusieurs fichiers en parallèle"""
    fichiers = [
        ("video.mp4", 10),
        ("image.jpg", 2),
        ("document.pdf", 5),
        ("musique.mp3", 3)
    ]

    # Lancer tous les téléchargements en parallèle
    resultats = await asyncio.gather(
        *[telecharger_fichier(nom, taille) for nom, taille in fichiers]
    )

    print(f"\n📦 Tous les fichiers téléchargés: {len(resultats)}")
    for resultat in resultats:
        print(f"  - {resultat}")

asyncio.run(main())
```

**Avantages de gather()** :
- Syntaxe plus concise
- Retourne tous les résultats dans une liste
- Gère les exceptions de manière centralisée

---

## asyncio.wait_for() - Timeout

Parfois, on veut limiter le temps d'attente d'une opération.

### Exemple 4 : Utiliser un timeout

```python
import asyncio

async def operation_longue():
    """Opération qui prend du temps"""
    print("Début de l'opération longue...")
    await asyncio.sleep(10)  # Prend 10 secondes
    return "Opération terminée"

async def main():
    """Teste avec un timeout de 3 secondes"""
    try:
        resultat = await asyncio.wait_for(operation_longue(), timeout=3.0)
        print(f"Résultat: {resultat}")
    except asyncio.TimeoutError:
        print("❌ Timeout! L'opération a pris trop de temps")

asyncio.run(main())
```

**Sortie** :
```
Début de l'opération longue...
[attend 3 secondes]
❌ Timeout! L'opération a pris trop de temps
```

---

## Exemple pratique : Scraper web asynchrone

Voici un exemple réaliste qui montre la puissance d'asyncio.

### Exemple 5 : Télécharger plusieurs pages web

```python
import asyncio  
import time  

# Simulation d'une bibliothèque de requêtes HTTP asynchrone
async def fetch_page(url, duree):
    """Simule le téléchargement d'une page web"""
    print(f"🌐 GET {url}")
    await asyncio.sleep(duree)  # Simule la latence réseau
    print(f"✅ {url} - 200 OK")
    return f"Contenu de {url}"

async def scraper_synchrone(urls):
    """Version synchrone (une page après l'autre)"""
    print("=== VERSION SYNCHRONE ===")
    debut = time.time()

    resultats = []
    for url, duree in urls:
        resultat = await fetch_page(url, duree)
        resultats.append(resultat)

    duree_totale = time.time() - debut
    print(f"⏱️  Temps total: {duree_totale:.2f}s\n")
    return resultats

async def scraper_asynchrone(urls):
    """Version asynchrone (toutes les pages en parallèle)"""
    print("=== VERSION ASYNCHRONE ===")
    debut = time.time()

    # Lancer toutes les requêtes en parallèle
    taches = [fetch_page(url, duree) for url, duree in urls]
    resultats = await asyncio.gather(*taches)

    duree_totale = time.time() - debut
    print(f"⏱️  Temps total: {duree_totale:.2f}s\n")
    return resultats

async def main():
    """Compare les deux approches"""
    urls = [
        ("https://example.com/page1", 2),
        ("https://example.com/page2", 1.5),
        ("https://example.com/page3", 2.5),
        ("https://example.com/page4", 1),
    ]

    # Version synchrone
    await scraper_synchrone(urls)

    # Version asynchrone
    await scraper_asynchrone(urls)

asyncio.run(main())
```

**Sortie attendue** :
```
=== VERSION SYNCHRONE ===
🌐 GET https://example.com/page1
✅ https://example.com/page1 - 200 OK
🌐 GET https://example.com/page2
✅ https://example.com/page2 - 200 OK
🌐 GET https://example.com/page3
✅ https://example.com/page3 - 200 OK
🌐 GET https://example.com/page4
✅ https://example.com/page4 - 200 OK
⏱️  Temps total: 7.00s

=== VERSION ASYNCHRONE ===
🌐 GET https://example.com/page1
🌐 GET https://example.com/page2
🌐 GET https://example.com/page3
🌐 GET https://example.com/page4
✅ https://example.com/page4 - 200 OK
✅ https://example.com/page2 - 200 OK
✅ https://example.com/page1 - 200 OK
✅ https://example.com/page3 - 200 OK
⏱️  Temps total: 2.50s
```

**Gain de performance** : Presque 3x plus rapide ! 🚀

---

## Bibliothèques asynchrones courantes

Pour utiliser pleinement asyncio, vous aurez besoin de bibliothèques qui supportent l'asynchrone.

### Bibliothèques populaires

| Bibliothèque | Usage | Installation |
|--------------|-------|--------------|
| **aiohttp** | Requêtes HTTP asynchrones | `pip install aiohttp` |
| **aiofiles** | Lecture/écriture fichiers async | `pip install aiofiles` |
| **asyncpg** | Client PostgreSQL asynchrone | `pip install asyncpg` |
| **motor** | Client MongoDB asynchrone | `pip install motor` |
| **websockets** | WebSockets asynchrones | `pip install websockets` |
| **httpx** | Client HTTP moderne (sync & async) | `pip install httpx` |

### Exemple 6 : Utiliser aiohttp pour de vraies requêtes HTTP

```python
import asyncio  
import aiohttp  

async def telecharger_url(session, url):
    """Télécharge le contenu d'une URL"""
    async with session.get(url) as response:
        contenu = await response.text()
        print(f"✅ {url} - {len(contenu)} caractères")
        return contenu

async def main():
    """Télécharge plusieurs URLs en parallèle"""
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
    ]

    # Créer une session HTTP asynchrone
    async with aiohttp.ClientSession() as session:
        taches = [telecharger_url(session, url) for url in urls]
        resultats = await asyncio.gather(*taches)

    print(f"\n📦 {len(resultats)} pages téléchargées")

# Note: cet exemple nécessite: pip install aiohttp
# asyncio.run(main())
```

---

## Gestion des erreurs en asynchrone

### Exemple 7 : Gérer les exceptions

```python
import asyncio

async def operation_risquee(numero):
    """Opération qui peut échouer"""
    await asyncio.sleep(1)
    if numero == 3:
        raise ValueError(f"Erreur avec le numéro {numero}")
    return f"Succès {numero}"

async def main():
    """Gère les exceptions dans les tâches"""
    taches = [operation_risquee(i) for i in range(1, 6)]

    # Méthode 1: gather avec return_exceptions=True
    resultats = await asyncio.gather(*taches, return_exceptions=True)

    for i, resultat in enumerate(resultats, 1):
        if isinstance(resultat, Exception):
            print(f"❌ Tâche {i}: Erreur - {resultat}")
        else:
            print(f"✅ Tâche {i}: {resultat}")

asyncio.run(main())
```

**Sortie** :
```
✅ Tâche 1: Succès 1
✅ Tâche 2: Succès 2
❌ Tâche 3: Erreur - Erreur avec le numéro 3
✅ Tâche 4: Succès 4
✅ Tâche 5: Succès 5
```

### Exemple 8 : Try/except dans les coroutines

```python
import asyncio

async def tache_avec_gestion_erreur(numero):
    """Gère ses propres erreurs"""
    try:
        await asyncio.sleep(0.5)
        if numero % 2 == 0:
            raise ValueError(f"Nombre pair non autorisé: {numero}")
        return f"Traitement réussi pour {numero}"
    except ValueError as e:
        print(f"⚠️  Erreur gérée: {e}")
        return f"Erreur traitée pour {numero}"

async def main():
    """Lance plusieurs tâches"""
    taches = [tache_avec_gestion_erreur(i) for i in range(1, 6)]
    resultats = await asyncio.gather(*taches)

    print("\nRésultats finaux:")
    for resultat in resultats:
        print(f"  - {resultat}")

asyncio.run(main())
```

---

## Patterns courants avec asyncio

### Pattern 1 : Queue asynchrone (Producer-Consumer)

```python
import asyncio  
import random  

async def producteur(queue, nom, nb_items):
    """Produit des items dans la queue"""
    for i in range(nb_items):
        item = f"{nom}-item-{i}"
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await queue.put(item)
        print(f"📤 {nom} a produit: {item}")

async def consommateur(queue, nom):
    """Consomme des items de la queue"""
    while True:
        item = await queue.get()
        if item is None:  # Signal de fin
            break
        print(f"📥 {nom} consomme: {item}")
        await asyncio.sleep(random.uniform(0.3, 0.8))
        queue.task_done()

async def main():
    """Lance producteurs et consommateurs"""
    queue = asyncio.Queue(maxsize=5)

    # Créer les tâches
    producteurs = [
        asyncio.create_task(producteur(queue, f"Producteur-{i}", 3))
        for i in range(2)
    ]

    consommateurs = [
        asyncio.create_task(consommateur(queue, f"Consommateur-{i}"))
        for i in range(3)
    ]

    # Attendre que tous les producteurs finissent
    await asyncio.gather(*producteurs)

    # Attendre que la queue soit vide
    await queue.join()

    # Arrêter les consommateurs
    for _ in consommateurs:
        await queue.put(None)

    await asyncio.gather(*consommateurs)
    print("\n✅ Traitement terminé")

asyncio.run(main())
```

### Pattern 2 : Limiter le nombre de tâches concurrentes

```python
import asyncio

async def tache_longue(numero, semaphore):
    """Tâche qui utilise un sémaphore pour limiter la concurrence"""
    async with semaphore:
        print(f"🔵 Tâche {numero} démarre")
        await asyncio.sleep(2)
        print(f"✅ Tâche {numero} termine")
        return numero

async def main():
    """Limite à 3 tâches simultanées maximum"""
    # Sémaphore qui permet max 3 tâches en parallèle
    semaphore = asyncio.Semaphore(3)

    # Créer 10 tâches
    taches = [tache_longue(i, semaphore) for i in range(1, 11)]

    resultats = await asyncio.gather(*taches)
    print(f"\n✅ Toutes les tâches terminées: {resultats}")

asyncio.run(main())
```

**Comportement** : Au maximum 3 tâches s'exécutent en même temps, les autres attendent.

---

## asyncio vs threading : Comparaison pratique

### Exemple 9 : Comparaison des performances

```python
import asyncio  
import threading  
import time  

# === VERSION THREADING ===
def operation_io_thread(numero):
    """Simulation I/O avec threading"""
    time.sleep(1)  # Bloque le thread
    return numero * 2

def executer_avec_threads(nombre):
    """Exécute avec threads"""
    debut = time.time()
    threads = []
    resultats = [None] * nombre

    def wrapper(i):
        resultats[i] = operation_io_thread(i)

    for i in range(nombre):
        thread = threading.Thread(target=wrapper, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    duree = time.time() - debut
    print(f"🧵 Threading: {duree:.2f}s pour {nombre} opérations")
    return resultats

# === VERSION ASYNCIO ===
async def operation_io_async(numero):
    """Simulation I/O avec asyncio"""
    await asyncio.sleep(1)  # Non-bloquant
    return numero * 2

async def executer_avec_asyncio(nombre):
    """Exécute avec asyncio"""
    debut = time.time()

    taches = [operation_io_async(i) for i in range(nombre)]
    resultats = await asyncio.gather(*taches)

    duree = time.time() - debut
    print(f"⚡ Asyncio: {duree:.2f}s pour {nombre} opérations")
    return resultats

# === COMPARAISON ===
async def main():
    """Compare les deux approches"""
    nombre_operations = 100

    print(f"Comparaison avec {nombre_operations} opérations I/O:")

    # Threading
    executer_avec_threads(nombre_operations)

    # Asyncio
    await executer_avec_asyncio(nombre_operations)

asyncio.run(main())
```

**Résultat typique** :
```
🧵 Threading: 1.02s pour 100 opérations
⚡ Asyncio: 1.00s pour 100 opérations
```

**Avantages d'asyncio** :
- Moins de mémoire (pas de stack par tâche)
- Plus scalable (peut gérer des milliers de connexions)
- Code plus lisible avec async/await

---

## Bonnes pratiques asyncio

### 1. Toujours utiliser `asyncio.run()` comme point d'entrée

```python
# ✅ Bon
async def main():
    # Code asynchrone
    pass

asyncio.run(main())

# ❌ Mauvais (ancien style)
loop = asyncio.get_event_loop()  
loop.run_until_complete(main())  
```

### 2. Ne jamais bloquer l'event loop

```python
import asyncio  
import time  

async def mauvaise_pratique():
    """❌ Ne fait pas ça!"""
    time.sleep(5)  # Bloque tout le programme!
    print("Terminé")

async def bonne_pratique():
    """✅ Fais ça à la place"""
    await asyncio.sleep(5)  # Non-bloquant
    print("Terminé")
```

**Règle** : N'utilisez jamais `time.sleep()` dans du code asynchrone, utilisez `await asyncio.sleep()`.

### 3. Utiliser des bibliothèques asynchrones

```python
# ❌ Mauvais - utilise une bibliothèque synchrone
import requests

async def mauvais_download():
    response = requests.get("https://example.com")  # Bloque!
    return response.text

# ✅ Bon - utilise une bibliothèque asynchrone
import aiohttp

async def bon_download():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com") as response:
            return await response.text()
```

### 4. Gérer proprement les ressources

```python
import asyncio

async def utiliser_ressource():
    """✅ Utilise un context manager asynchrone"""
    async with ressource_async() as res:
        await res.faire_quelquechose()
    # La ressource est automatiquement fermée

# Ou pour plusieurs ressources
async def utiliser_plusieurs_ressources():
    """✅ Gère plusieurs ressources proprement"""
    async with ressource1() as r1, ressource2() as r2:
        await r1.operation()
        await r2.operation()
```

### 5. Attention aux listes de compréhension

```python
# ❌ Mauvais - crée les tâches mais ne les exécute pas en parallèle
async def mauvais():
    resultats = [await ma_coroutine(i) for i in range(10)]

# ✅ Bon - exécute vraiment en parallèle
async def bon():
    taches = [ma_coroutine(i) for i in range(10)]
    resultats = await asyncio.gather(*taches)
```

### 6. Nommer les tâches pour le débogage

```python
import asyncio

async def ma_tache(numero):
    await asyncio.sleep(1)
    return numero

async def main():
    # Créer des tâches avec des noms
    taches = [
        asyncio.create_task(ma_tache(i), name=f"tache-{i}")
        for i in range(5)
    ]

    # Utile pour le débogage
    for tache in taches:
        print(f"Nom de la tâche: {tache.get_name()}")

    await asyncio.gather(*taches)

asyncio.run(main())
```

---

## Erreurs courantes et solutions

### Erreur 1 : RuntimeError: asyncio.run() cannot be called from a running event loop

**Problème** :
```python
async def fonction():
    asyncio.run(autre_fonction())  # ❌ Erreur!
```

**Solution** :
```python
async def fonction():
    await autre_fonction()  # ✅ Correct
```

### Erreur 2 : Oublier await

**Problème** :
```python
async def fonction():
    resultat = ma_coroutine()  # ❌ Retourne un objet coroutine, pas le résultat
    print(resultat)
```

**Solution** :
```python
async def fonction():
    resultat = await ma_coroutine()  # ✅ Attend et obtient le résultat
    print(resultat)
```

### Erreur 3 : Mélanger code synchrone et asynchrone

**Problème** :
```python
def fonction_normale():
    await ma_coroutine()  # ❌ await hors d'une fonction async
```

**Solution** :
```python
async def fonction_asynchrone():
    await ma_coroutine()  # ✅ await dans une fonction async
```

### Erreur 4 : Ne pas attendre toutes les tâches

**Problème** :
```python
async def probleme():
    asyncio.create_task(ma_coroutine())
    # La tâche n'a pas le temps de s'exécuter!
```

**Solution** :
```python
async def solution():
    tache = asyncio.create_task(ma_coroutine())
    await tache  # ✅ Attend que la tâche se termine
```

---

## Exemple complet : Application de téléchargement

Voici un exemple réaliste et complet qui combine tous les concepts :

```python
import asyncio  
import time  

class GestionnaireTelechargement:
    """Gestionnaire de téléchargements asynchrones avec contrôle"""

    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.statistiques = {
            'reussis': 0,
            'echoues': 0,
            'total': 0
        }

    async def telecharger_fichier(self, url: str, timeout: float = 10.0) -> dict:
        """Télécharge un fichier avec gestion d'erreurs et timeout"""
        async with self.semaphore:
            self.statistiques['total'] += 1
            debut = time.time()

            try:
                print(f"⬇️  Début: {url}")

                # Simulation du téléchargement avec timeout
                await asyncio.wait_for(
                    self._simuler_telechargement(url),
                    timeout=timeout
                )

                duree = time.time() - debut
                self.statistiques['reussis'] += 1

                print(f"✅ Succès: {url} ({duree:.2f}s)")
                return {
                    'url': url,
                    'statut': 'succès',
                    'duree': duree
                }

            except asyncio.TimeoutError:
                self.statistiques['echoues'] += 1
                print(f"⏱️  Timeout: {url}")
                return {
                    'url': url,
                    'statut': 'timeout',
                    'erreur': 'Timeout dépassé'
                }

            except Exception as e:
                self.statistiques['echoues'] += 1
                print(f"❌ Erreur: {url} - {e}")
                return {
                    'url': url,
                    'statut': 'erreur',
                    'erreur': str(e)
                }

    async def _simuler_telechargement(self, url: str):
        """Simule le téléchargement (à remplacer par vrai code)"""
        # Simulation de durée variable
        duree = len(url) % 5 + 1
        await asyncio.sleep(duree)

    async def telecharger_liste(self, urls: list[str]) -> list[dict]:
        """Télécharge une liste d'URLs"""
        print(f"🚀 Lancement de {len(urls)} téléchargements")
        print(f"📊 Concurrence max: {self.max_concurrent}")
        print("-" * 50)

        debut_total = time.time()

        # Créer toutes les tâches
        taches = [self.telecharger_fichier(url) for url in urls]

        # Exécuter avec progression
        resultats = await asyncio.gather(*taches, return_exceptions=True)

        duree_totale = time.time() - debut_total

        # Afficher les statistiques
        print("-" * 50)
        print(f"\n📈 Statistiques:")
        print(f"  • Total: {self.statistiques['total']}")
        print(f"  • Réussis: {self.statistiques['reussis']}")
        print(f"  • Échoués: {self.statistiques['echoues']}")
        print(f"  • Durée totale: {duree_totale:.2f}s")
        print(f"  • Vitesse: {len(urls)/duree_totale:.2f} téléchargements/s")

        return resultats

async def main():
    """Fonction principale"""
    # Liste d'URLs à télécharger
    urls = [
        "https://example.com/fichier1.pdf",
        "https://example.com/fichier2.pdf",
        "https://example.com/fichier3.pdf",
        "https://example.com/fichier4.pdf",
        "https://example.com/fichier5.pdf",
        "https://example.com/fichier6.pdf",
        "https://example.com/fichier7.pdf",
        "https://example.com/fichier8.pdf",
    ]

    # Créer le gestionnaire avec max 3 téléchargements simultanés
    gestionnaire = GestionnaireTelechargement(max_concurrent=3)

    # Lancer les téléchargements
    resultats = await gestionnaire.telecharger_liste(urls)

    # Analyser les résultats
    print("\n📋 Résultats détaillés:")
    for resultat in resultats:
        if isinstance(resultat, dict):
            statut = resultat['statut']
            url = resultat['url']
            symbole = "✅" if statut == 'succès' else "❌"
            print(f"  {symbole} {url}: {statut}")

if __name__ == '__main__':
    asyncio.run(main())
```

---

## Quand NE PAS utiliser asyncio

Asyncio n'est pas toujours la meilleure solution. **Évitez asyncio** dans ces cas :

1. **Code simple sans beaucoup d'I/O** : La complexité supplémentaire n'en vaut pas la peine
2. **Calculs intensifs (CPU-bound)** : Utilisez multiprocessing à la place
3. **Bibliothèques uniquement synchrones** : Si vous ne pouvez pas utiliser de version asynchrone
4. **Débutants en Python** : Maîtrisez d'abord le code synchrone

---

## Résumé des concepts clés

| Concept | Description | Syntaxe |
|---------|-------------|---------|
| **Coroutine** | Fonction asynchrone | `async def fonction():` |
| **await** | Attend sans bloquer | `await ma_coroutine()` |
| **Task** | Coroutine planifiée | `asyncio.create_task(coro)` |
| **gather** | Exécute plusieurs coroutines | `await asyncio.gather(*coros)` |
| **sleep** | Pause non-bloquante | `await asyncio.sleep(1)` |
| **run** | Lance l'event loop | `asyncio.run(main())` |
| **Queue** | File asynchrone | `asyncio.Queue()` |
| **Semaphore** | Limite la concurrence | `asyncio.Semaphore(n)` |

---

## Points clés à retenir

1. **asyncio** = Parfait pour gérer beaucoup d'opérations I/O simultanées
2. **async/await** = Syntaxe pour écrire du code asynchrone lisible
3. **Event loop** = Orchestre l'exécution des coroutines
4. **create_task()** = Lance une coroutine en arrière-plan
5. **gather()** = Attend plusieurs coroutines en parallèle
6. **Ne jamais bloquer l'event loop** = Utilisez des versions asynchrones
7. **Gérez les erreurs** = Utilisez try/except et return_exceptions
8. **Semaphore** = Contrôle le nombre de tâches simultanées

---

## Ressources et prochaines étapes

**Pour aller plus loin** :
- Documentation officielle Python asyncio
- Bibliothèque `aiohttp` pour les requêtes HTTP asynchrones
- Framework `FastAPI` qui utilise asyncio nativement
- Explorez `asyncio.Queue`, `asyncio.Event`, `asyncio.Lock`

**Dans la prochaine section** (8.3), nous verrons la **gestion des verrous et la synchronisation** pour coordonner les tâches concurrentes de manière avancée.

---

## Glossaire

- **Asynchrone** : Qui ne bloque pas en attendant
- **Coroutine** : Fonction pouvant être mise en pause et reprise
- **Event Loop** : Boucle qui gère l'exécution des coroutines
- **Task** : Coroutine planifiée pour exécution
- **await** : Attend le résultat d'une coroutine
- **GIL** : Global Interpreter Lock (verrou de Python)
- **I/O-bound** : Limité par les entrées/sorties
- **CPU-bound** : Limité par le processeur

⏭️ [Gestion des verrous et synchronisation](/08-programmation-concurrente/03-verrous-et-synchronisation.md)
