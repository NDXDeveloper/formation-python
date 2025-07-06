🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 8 : Programmation concurrente

## Introduction

La programmation concurrente est l'art de faire exécuter plusieurs tâches "en même temps" pour améliorer les performances et la réactivité de vos applications. Python offre plusieurs approches pour gérer la concurrence, chacune adaptée à des situations spécifiques.

## Qu'est-ce que la programmation concurrente ?

La **programmation concurrente** permet d'exécuter plusieurs tâches de manière apparemment simultanée. Au lieu d'attendre qu'une tâche se termine avant de commencer la suivante, vous pouvez faire progresser plusieurs tâches en parallèle.

### Analogie simple
Imaginez une **cuisine de restaurant** :
- **Séquentiel** : Un seul cuisinier prépare un plat complètement avant de commencer le suivant
- **Concurrent** : Plusieurs cuisiniers travaillent simultanément, ou un cuisinier jongle entre plusieurs plats
- **Parallèle** : Plusieurs cuisiniers travaillent réellement en même temps sur des plats différents

## Pourquoi utiliser la programmation concurrente ?

### 1. **Améliorer les performances**
- Utiliser plusieurs cœurs de processeur
- Réduire le temps d'attente (I/O)
- Traiter plus de données simultanément

### 2. **Améliorer la réactivité**
- Interface utilisateur qui reste fluide
- Serveurs web qui gèrent plusieurs requêtes
- Applications qui répondent pendant les calculs longs

### 3. **Optimiser l'utilisation des ressources**
- Pendant qu'un thread attend une réponse réseau, un autre peut calculer
- Paralléliser les tâches indépendantes
- Équilibrer la charge entre les ressources disponibles

## Types de concurrence en Python

### **1. Threading (Threads)**
Plusieurs **fils d'exécution** dans le même processus, partageant la mémoire.

**Avantages :**
- Partage facile de données
- Moins de consommation mémoire
- Création rapide

**Inconvénients :**
- GIL (Global Interpreter Lock) limite le parallélisme réel
- Risques de conditions de course (race conditions)
- Synchronisation complexe

**Idéal pour :** I/O intensif (réseau, fichiers, bases de données)

### **2. Multiprocessing (Processus)**
Plusieurs **processus** séparés, chacun avec sa propre mémoire.

**Avantages :**
- Vrai parallélisme (pas de GIL)
- Isolation complète entre processus
- Utilisation de tous les cœurs CPU

**Inconvénients :**
- Plus de consommation mémoire
- Communication plus complexe
- Création plus lente

**Idéal pour :** CPU intensif (calculs, traitement d'images, analyses)

### **3. Asyncio (Programmation asynchrone)**
Exécution **coopérative** avec un seul thread qui alterne entre tâches.

**Avantages :**
- Très efficace pour I/O
- Pas de problèmes de synchronisation
- Gestion de milliers de connexions

**Inconvénients :**
- Courbe d'apprentissage plus raide
- Nécessite des bibliothèques async
- Un seul thread (pas de parallélisme CPU)

**Idéal pour :** Serveurs web, clients réseau, APIs

## Concepts fondamentaux

### **Concurrence vs Parallélisme**

```
CONCURRENCE (Threading/Asyncio)
Thread 1: ===|    |===|    |===
Thread 2:    |====|   |====|
             ↑ Alternance entre tâches

PARALLÉLISME (Multiprocessing)
Core 1:   ================
Core 2:   ================
          ↑ Exécution simultanée réelle
```

### **Le GIL (Global Interpreter Lock)**

Le GIL est un verrou qui empêche l'exécution simultanée de code Python dans plusieurs threads.

**Impact :**
- Les threads Python ne peuvent pas vraiment s'exécuter en parallèle pour les calculs
- Cependant, ils restent utiles pour l'I/O (le GIL est libéré pendant les attentes)
- C'est pourquoi multiprocessing est nécessaire pour le parallélisme CPU réel

### **Synchronisation**

Quand plusieurs tâches accèdent aux mêmes ressources, il faut coordonner leurs accès :

- **Lock** : Un seul thread à la fois peut accéder à la ressource
- **Queue** : Communication sécurisée entre threads/processus
- **Event** : Signaler des événements entre tâches
- **Semaphore** : Limiter le nombre de tâches simultanées

## Défis de la programmation concurrente

### **1. Conditions de course (Race Conditions)**
Quand le résultat dépend de l'ordre d'exécution imprévisible des threads.

```python
# Problème : deux threads modifient la même variable
counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1  # Pas atomique !

# Résultat imprévisible si plusieurs threads exécutent increment()
```

### **2. Interblocage (Deadlock)**
Quand deux ou plusieurs threads s'attendent mutuellement.

```python
# Thread 1 a lock A, veut lock B
# Thread 2 a lock B, veut lock A
# → Blocage !
```

### **3. Famine (Starvation)**
Quand certains threads n'obtiennent jamais accès aux ressources.

### **4. Complexité de débogage**
- Bugs non déterministes
- Difficile à reproduire
- Outils de débogage spécialisés nécessaires

## Quand utiliser chaque approche ?

### **Threading** 🧵
```python
# Bon pour :
- Téléchargement de fichiers
- Requêtes bases de données
- Interfaces utilisateur
- Serveurs avec peu de clients

# Exemple typique :
# Télécharger plusieurs URLs en parallèle
```

### **Multiprocessing** ⚡
```python
# Bon pour :
- Calculs mathématiques intensifs
- Traitement d'images/vidéos
- Analyse de gros datasets
- Machine learning

# Exemple typique :
# Traiter chaque image d'un dossier sur un cœur différent
```

### **Asyncio** 🔄
```python
# Bon pour :
- Serveurs web haute performance
- Clients API nombreuses requêtes
- WebSockets
- Applications temps réel

# Exemple typique :
# Serveur chat gérant 10000 connexions simultanées
```

## Tableau de comparaison

| Aspect | Threading | Multiprocessing | Asyncio |
|--------|-----------|-----------------|---------|
| **Parallélisme réel** | ❌ (GIL) | ✅ | ❌ |
| **Mémoire partagée** | ✅ | ❌ | ✅ |
| **Simplicité** | 🟡 | 🟡 | 🔴 |
| **I/O intensif** | ✅ | 🟡 | ✅ |
| **CPU intensif** | ❌ | ✅ | ❌ |
| **Scalabilité** | 🟡 | 🟡 | ✅ |
| **Débogage** | 🔴 | 🔴 | 🟡 |

## Exemples de cas d'usage concrets

### **E-commerce**
- **Threading** : Traitement des commandes, envoi d'emails
- **Multiprocessing** : Génération de rapports, analyse de données
- **Asyncio** : API REST, gestion des sessions utilisateurs

### **Analyse de données**
- **Threading** : Collecte de données depuis APIs
- **Multiprocessing** : Calculs statistiques sur datasets
- **Asyncio** : Streaming de données en temps réel

### **Jeux vidéo**
- **Threading** : Chargement d'assets, sauvegarde
- **Multiprocessing** : IA des NPCs, physique complexe
- **Asyncio** : Multijoueur en ligne, chat

### **Applications scientifiques**
- **Threading** : Interface utilisateur, logging
- **Multiprocessing** : Simulations, calculs parallèles
- **Asyncio** : Collecte de données capteurs

## Structure du module

Dans ce module, nous explorerons en détail chaque approche :

### **8.1 : Threading et multiprocessing**
- Création et gestion de threads
- Communication entre threads
- Processus parallèles
- Pools de workers
- Synchronisation

### **8.2 : Programmation asynchrone avec asyncio**
- Concepts async/await
- Coroutines et tâches
- Boucles d'événements
- Clients et serveurs async

### **8.3 : Gestion des verrous et synchronisation**
- Locks, RLocks, Semaphores
- Conditions et événements
- Queues thread-safe
- Patterns de synchronisation

### **8.4 : Patterns de concurrence**
- Producer-Consumer
- Worker Pool
- Pipeline de traitement
- Map-Reduce
- Circuit Breaker

## Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. **Choisir la bonne approche** selon le type de problème
2. **Implémenter des solutions concurrentes** robustes et efficaces
3. **Éviter les pièges** courants de la programmation concurrente
4. **Déboguer et optimiser** du code concurrent
5. **Concevoir des architectures** scalables et performantes

## Prérequis

Avant d'aborder ce module, vous devez maîtriser :

- **Programmation orientée objet** : classes, héritage, exceptions
- **Fonctions avancées** : décorateurs, gestionnaires de contexte
- **Gestion d'erreurs** : try/except, types d'exceptions
- **Modules et packages** : imports, organisation du code

## Méthodologie d'apprentissage

### **Approche progressive**
1. Concepts théoriques avec analogies
2. Exemples simples et isolés
3. Cas d'usage réels et complexes
4. Projets d'intégration

### **Focus sur la pratique**
- Nombreux exemples de code
- Exercices hands-on
- Projets concrets
- Mesures de performance

### **Sécurité et robustesse**
- Patterns éprouvés
- Gestion d'erreurs
- Tests de code concurrent
- Monitoring et débogage

## Outils et ressources

### **Modules Python**
- `threading` : Threads natifs
- `multiprocessing` : Processus parallèles
- `asyncio` : Programmation asynchrone
- `concurrent.futures` : Interface haut niveau
- `queue` : Communication thread-safe

### **Outils de développement**
- Profileurs pour mesurer les performances
- Debuggers spécialisés pour le code concurrent
- Outils de détection de race conditions
- Frameworks de test pour code asynchrone

### **Monitoring**
- Surveillance de l'utilisation CPU/mémoire
- Détection de deadlocks
- Métriques de performance
- Alertes de surcharge

---

*La programmation concurrente est un domaine complexe mais puissant. Une fois maîtrisée, elle vous permettra de créer des applications significativement plus performantes et réactives. Nous allons progresser étape par étape pour que vous deveniez à l'aise avec ces concepts avancés.*

⏭️
