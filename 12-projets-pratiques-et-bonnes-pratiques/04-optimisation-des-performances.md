🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.4 : Optimisation des performances

## Introduction

Imaginez une voiture qui met 30 minutes pour faire 1 kilomètre. Techniquement, elle fonctionne, mais personne ne voudrait l'utiliser ! En programmation, c'est pareil : un programme qui fonctionne mais qui est lent peut être inutilisable en pratique.

L'optimisation des performances consiste à rendre votre code plus rapide et plus efficace en mémoire. Mais attention : l'optimisation prématurée est souvent contre-productive. La règle d'or est :

> **"D'abord, faites fonctionner votre code. Ensuite, mesurez. Enfin, optimisez uniquement ce qui en a besoin."**

## Pourquoi optimiser ?

### Les enjeux de performance

1. **Expérience utilisateur** : Personne n'aime attendre
2. **Coûts d'infrastructure** : Moins de serveurs nécessaires
3. **Scalabilité** : Gérer plus d'utilisateurs
4. **Énergie** : Code plus efficace = moins de consommation

### Quand NE PAS optimiser

❌ **Évitez l'optimisation quand :**
- Votre code n'est pas encore fonctionnel
- Vous n'avez pas mesuré les performances
- L'amélioration est négligeable
- Cela rend le code incompréhensible

✅ **Optimisez quand :**
- Vous avez identifié un vrai goulot d'étranglement
- L'impact utilisateur est significatif
- Vous avez des métriques précises

## Mesurer les performances

### Le module `time`

La première étape est de mesurer pour savoir où sont les problèmes :

```python
import time

def mesurer_temps(func):
    """Décorateur pour mesurer le temps d'exécution."""
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()

        duree = fin - debut
        print(f"⏱️  {func.__name__} executée en {duree:.4f} secondes")
        return resultat

    return wrapper

# Exemple d'utilisation
@mesurer_temps
def somme_lente(n):
    """Calcule la somme de 1 à n de manière inefficace."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

@mesurer_temps
def somme_rapide(n):
    """Calcule la somme de 1 à n avec la formule."""
    return n * (n + 1) // 2

# Test de comparaison
print("=== Comparaison des algorithmes ===")
n = 1000000

resultat1 = somme_lente(n)
resultat2 = somme_rapide(n)

print(f"Résultats identiques: {resultat1 == resultat2}")
```

### Le module `timeit` pour des mesures précises

```python
import timeit

def comparer_approches():
    """Compare différentes approches avec timeit."""

    # Code à tester
    code_boucle = """
total = 0
for i in range(1000):
    total += i
"""

    code_sum = """
total = sum(range(1000))
"""

    code_formule = """
n = 999
total = n * (n + 1) // 2
"""

    # Mesurer les performances
    temps_boucle = timeit.timeit(code_boucle, number=10000)
    temps_sum = timeit.timeit(code_sum, number=10000)
    temps_formule = timeit.timeit(code_formule, number=10000)

    print("📊 Comparaison des performances (10000 exécutions):")
    print(f"Boucle for    : {temps_boucle:.4f} secondes")
    print(f"Fonction sum(): {temps_sum:.4f} secondes")
    print(f"Formule math  : {temps_formule:.4f} secondes")

    # Calculer les gains
    base = temps_boucle
    print(f"\n🚀 Gains de performance:")
    print(f"sum() est {base/temps_sum:.1f}x plus rapide")
    print(f"Formule est {base/temps_formule:.1f}x plus rapide")

comparer_approches()
```

### Profiling avec `cProfile`

Pour analyser en détail les performances d'un programme :

```python
import cProfile
import pstats

def fibonacci_recursif(n):
    """Fibonacci récursif (inefficace)."""
    if n <= 1:
        return n
    return fibonacci_recursif(n-1) + fibonacci_recursif(n-2)

def fibonacci_iteratif(n):
    """Fibonacci itératif (efficace)."""
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def tester_fibonacci():
    """Teste les deux implémentations."""
    print("=== Test Fibonacci ===")

    n = 30

    # Version récursive
    print("Version récursive:")
    cProfile.run('fibonacci_recursif(30)', 'profile_recursif.prof')

    # Version itérative
    print("Version itérative:")
    cProfile.run('fibonacci_iteratif(30)', 'profile_iteratif.prof')

    # Analyser les résultats
    print("\n📈 Analyse de la version récursive:")
    stats_recursif = pstats.Stats('profile_recursif.prof')
    stats_recursif.sort_stats('cumulative').print_stats(5)

    print("\n📈 Analyse de la version itérative:")
    stats_iteratif = pstats.Stats('profile_iteratif.prof')
    stats_iteratif.sort_stats('cumulative').print_stats(5)

# Uncomment to run profiling
# tester_fibonacci()
```

## Optimisation algorithmique

### Choisir la bonne structure de données

Le choix de la structure de données peut dramatiquement affecter les performances :

```python
import time
import random

def test_structures_donnees():
    """Compare les performances de différentes structures."""

    # Préparer les données
    donnees = list(range(100000))
    random.shuffle(donnees)

    elements_a_chercher = random.sample(donnees, 1000)

    # Test avec une liste
    def test_liste():
        liste = donnees.copy()
        debut = time.time()

        for element in elements_a_chercher:
            if element in liste:  # O(n) pour chaque recherche !
                pass

        return time.time() - debut

    # Test avec un set
    def test_set():
        ensemble = set(donnees)
        debut = time.time()

        for element in elements_a_chercher:
            if element in ensemble:  # O(1) pour chaque recherche !
                pass

        return time.time() - debut

    # Test avec un dictionnaire
    def test_dict():
        dictionnaire = {x: True for x in donnees}
        debut = time.time()

        for element in elements_a_chercher:
            if element in dictionnaire:  # O(1) pour chaque recherche !
                pass

        return time.time() - debut

    # Mesurer les performances
    temps_liste = test_liste()
    temps_set = test_set()
    temps_dict = test_dict()

    print("🔍 Recherche de 1000 éléments dans 100000:")
    print(f"Liste (O(n))  : {temps_liste:.4f} secondes")
    print(f"Set (O(1))    : {temps_set:.4f} secondes")
    print(f"Dict (O(1))   : {temps_dict:.4f} secondes")

    print(f"\n🚀 Le set est {temps_liste/temps_set:.0f}x plus rapide que la liste!")

test_structures_donnees()
```

### Complexité algorithmique

Comprendre la complexité Big O vous aide à choisir les bons algorithmes :

```python
def exemples_complexite():
    """Exemples de différentes complexités."""

    print("📚 Exemples de complexité Big O:")
    print()

    # O(1) - Constant
    def acces_constant(ma_liste, index):
        """O(1) - Accès par index."""
        return ma_liste[index]

    # O(log n) - Logarithmique
    def recherche_binaire(liste_triee, valeur):
        """O(log n) - Recherche binaire."""
        gauche, droite = 0, len(liste_triee) - 1

        while gauche <= droite:
            milieu = (gauche + droite) // 2
            if liste_triee[milieu] == valeur:
                return milieu
            elif liste_triee[milieu] < valeur:
                gauche = milieu + 1
            else:
                droite = milieu - 1

        return -1

    # O(n) - Linéaire
    def recherche_lineaire(ma_liste, valeur):
        """O(n) - Parcours de toute la liste."""
        for i, element in enumerate(ma_liste):
            if element == valeur:
                return i
        return -1

    # O(n²) - Quadratique
    def tri_bulle(ma_liste):
        """O(n²) - Tri à bulles (inefficace)."""
        liste_copiee = ma_liste.copy()
        n = len(liste_copiee)

        for i in range(n):
            for j in range(0, n - i - 1):
                if liste_copiee[j] > liste_copiee[j + 1]:
                    liste_copiee[j], liste_copiee[j + 1] = liste_copiee[j + 1], liste_copiee[j]

        return liste_copiee

    # Test de performance
    @mesurer_temps
    def test_recherche_lineaire():
        ma_liste = list(range(10000))
        return recherche_lineaire(ma_liste, 9999)

    @mesurer_temps
    def test_recherche_binaire():
        ma_liste = list(range(10000))
        return recherche_binaire(ma_liste, 9999)

    print("Recherche du dernier élément dans une liste de 10000:")
    print("Recherche linéaire O(n):")
    test_recherche_lineaire()

    print("Recherche binaire O(log n):")
    test_recherche_binaire()

exemples_complexite()
```

## Optimisation Python spécifique

### List Comprehensions vs boucles

```python
def comparer_creation_listes():
    """Compare différentes façons de créer des listes."""

    n = 100000

    # Méthode 1: Boucle for avec append
    @mesurer_temps
    def avec_boucle():
        resultat = []
        for i in range(n):
            if i % 2 == 0:
                resultat.append(i * 2)
        return resultat

    # Méthode 2: List comprehension
    @mesurer_temps
    def avec_comprehension():
        return [i * 2 for i in range(n) if i % 2 == 0]

    # Méthode 3: Avec filter et map
    @mesurer_temps
    def avec_filter_map():
        return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, range(n))))

    print("🏗️  Création d'une liste de 50000 éléments:")

    resultat1 = avec_boucle()
    resultat2 = avec_comprehension()
    resultat3 = avec_filter_map()

    print(f"Tous identiques: {resultat1 == resultat2 == resultat3}")

comparer_creation_listes()
```

### Utiliser les bonnes méthodes intégrées

```python
def utiliser_fonctions_integrees():
    """Montre l'importance d'utiliser les fonctions intégrées."""

    nombres = list(range(1000000))

    # Somme manuelle
    @mesurer_temps
    def somme_manuelle():
        total = 0
        for nombre in nombres:
            total += nombre
        return total

    # Fonction sum() intégrée
    @mesurer_temps
    def somme_integree():
        return sum(nombres)

    # Maximum manuel
    @mesurer_temps
    def maximum_manuel():
        maximum = nombres[0]
        for nombre in nombres:
            if nombre > maximum:
                maximum = nombre
        return maximum

    # Fonction max() intégrée
    @mesurer_temps
    def maximum_integre():
        return max(nombres)

    print("🔧 Comparaison fonctions manuelles vs intégrées:")

    print("Somme:")
    s1 = somme_manuelle()
    s2 = somme_integree()
    print(f"Résultats identiques: {s1 == s2}")

    print("\nMaximum:")
    m1 = maximum_manuel()
    m2 = maximum_integre()
    print(f"Résultats identiques: {m1 == m2}")

utiliser_fonctions_integrees()
```

### Éviter les créations d'objets inutiles

```python
def eviter_creations_inutiles():
    """Montre comment éviter les créations d'objets coûteuses."""

    # Mauvais: Création de strings répétée
    @mesurer_temps
    def concatenation_lente():
        resultat = ""
        for i in range(10000):
            resultat += str(i) + " "  # Crée une nouvelle string à chaque fois !
        return resultat

    # Bon: Utiliser join()
    @mesurer_temps
    def concatenation_rapide():
        parties = []
        for i in range(10000):
            parties.append(str(i))
        return " ".join(parties)

    # Encore mieux: List comprehension + join
    @mesurer_temps
    def concatenation_optimale():
        return " ".join(str(i) for i in range(10000))

    print("🔗 Concaténation de 10000 nombres:")

    r1 = concatenation_lente()
    r2 = concatenation_rapide()
    r3 = concatenation_optimale()

    # Vérifier que les résultats sont identiques (sans afficher car trop long)
    print(f"Longueurs identiques: {len(r1) == len(r2) == len(r3)}")

eviter_creations_inutiles()
```

## Optimisation mémoire

### Générateurs vs listes

Les générateurs permettent d'économiser beaucoup de mémoire :

```python
import sys

def comparer_memoire():
    """Compare l'utilisation mémoire entre listes et générateurs."""

    # Liste en mémoire
    def creer_liste(n):
        return [x * x for x in range(n)]

    # Générateur
    def creer_generateur(n):
        return (x * x for x in range(n))

    n = 100000

    # Créer et mesurer
    ma_liste = creer_liste(n)
    mon_generateur = creer_generateur(n)

    taille_liste = sys.getsizeof(ma_liste)
    taille_generateur = sys.getsizeof(mon_generateur)

    print("💾 Utilisation mémoire:")
    print(f"Liste de {n} éléments: {taille_liste:,} bytes")
    print(f"Générateur: {taille_generateur:,} bytes")
    print(f"Économie: {taille_liste // taille_generateur}x moins de mémoire!")

    # Test de performance pour le traitement
    @mesurer_temps
    def traiter_liste():
        total = 0
        for x in ma_liste:
            total += x
        return total

    @mesurer_temps
    def traiter_generateur():
        total = 0
        for x in creer_generateur(n):
            total += x
        return total

    print("\n⚡ Performance de traitement:")
    total1 = traiter_liste()
    total2 = traiter_generateur()

    print(f"Résultats identiques: {total1 == total2}")

comparer_memoire()
```

### Slots pour économiser la mémoire

```python
import sys

class PersonneNormale:
    """Classe normale avec __dict__."""

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class PersonneAvecSlots:
    """Classe optimisée avec __slots__."""

    __slots__ = ['nom', 'age']

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

def comparer_slots():
    """Compare l'utilisation mémoire avec et sans slots."""

    # Créer des instances
    p1 = PersonneNormale("Alice", 30)
    p2 = PersonneAvecSlots("Alice", 30)

    # Mesurer la mémoire
    taille_normale = sys.getsizeof(p1) + sys.getsizeof(p1.__dict__)
    taille_slots = sys.getsizeof(p2)

    print("🎯 Optimisation avec __slots__:")
    print(f"Personne normale: {taille_normale} bytes")
    print(f"Personne avec slots: {taille_slots} bytes")
    print(f"Économie: {((taille_normale - taille_slots) / taille_normale * 100):.1f}%")

    # Test avec beaucoup d'instances
    @mesurer_temps
    def creer_personnes_normales():
        return [PersonneNormale(f"Personne{i}", i) for i in range(10000)]

    @mesurer_temps
    def creer_personnes_slots():
        return [PersonneAvecSlots(f"Personne{i}", i) for i in range(10000)]

    print("\n⚡ Création de 10000 instances:")
    personnes1 = creer_personnes_normales()
    personnes2 = creer_personnes_slots()

comparer_slots()
```

## Mise en cache (Memoization)

### Cache simple avec décorateur

```python
import functools

def cache_simple(func):
    """Décorateur de cache simple."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Créer une clé unique
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache:
            print(f"💾 Cache hit pour {func.__name__}{args}")
            return cache[key]

        print(f"🔄 Calcul de {func.__name__}{args}")
        resultat = func(*args, **kwargs)
        cache[key] = resultat
        return resultat

    return wrapper

@cache_simple
def fibonacci_avec_cache(n):
    """Fibonacci avec cache maison."""
    if n <= 1:
        return n
    return fibonacci_avec_cache(n-1) + fibonacci_avec_cache(n-2)

def tester_cache():
    """Teste l'efficacité du cache."""

    print("🧪 Test du cache Fibonacci:")

    # Sans cache (pour comparaison)
    @mesurer_temps
    def fibonacci_sans_cache(n):
        if n <= 1:
            return n
        return fibonacci_sans_cache(n-1) + fibonacci_sans_cache(n-2)

    # Avec cache
    @mesurer_temps
    def test_avec_cache():
        return fibonacci_avec_cache(30)

    print("Sans cache (n=25):")
    resultat1 = fibonacci_sans_cache(25)

    print("\nAvec cache (n=30):")
    resultat2 = test_avec_cache()

    print("\nDeuxième appel (devrait utiliser le cache):")
    resultat3 = test_avec_cache()

tester_cache()
```

### Cache avec LRU (Least Recently Used)

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_lru(n):
    """Fibonacci avec cache LRU intégré."""
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

def tester_lru_cache():
    """Teste le cache LRU intégré."""

    print("🔄 Test du cache LRU:")

    @mesurer_temps
    def calculer_fibonacci_lru():
        return fibonacci_lru(35)

    # Premier calcul
    print("Premier calcul:")
    resultat1 = calculer_fibonacci_lru()

    # Deuxième calcul (devrait être instantané)
    print("Deuxième calcul:")
    resultat2 = calculer_fibonacci_lru()

    # Informations sur le cache
    print(f"\n📊 Statistiques du cache:")
    print(f"Hits: {fibonacci_lru.cache_info().hits}")
    print(f"Misses: {fibonacci_lru.cache_info().misses}")
    print(f"Taille actuelle: {fibonacci_lru.cache_info().currsize}")
    print(f"Taille max: {fibonacci_lru.cache_info().maxsize}")

tester_lru_cache()
```

## Parallélisation

### Threading pour les tâches I/O

```python
import threading
import time
import requests

def tache_io_lente():
    """Simule une tâche I/O lente."""
    time.sleep(1)  # Simule un appel réseau
    return f"Résultat du thread {threading.current_thread().name}"

def comparer_sequential_vs_threading():
    """Compare exécution séquentielle vs threading."""

    # Exécution séquentielle
    @mesurer_temps
    def execution_sequentielle():
        resultats = []
        for i in range(5):
            resultat = tache_io_lente()
            resultats.append(resultat)
        return resultats

    # Exécution avec threading
    @mesurer_temps
    def execution_avec_threading():
        threads = []
        resultats = [None] * 5

        def worker(index):
            resultats[index] = tache_io_lente()

        # Créer et lancer les threads
        for i in range(5):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()

        # Attendre que tous se terminent
        for thread in threads:
            thread.join()

        return resultats

    print("🚄 Comparaison séquentiel vs threading:")

    print("Exécution séquentielle (5 tâches × 1s):")
    resultats1 = execution_sequentielle()

    print("Exécution avec threading (5 tâches en parallèle):")
    resultats2 = execution_avec_threading()

    print(f"Même nombre de résultats: {len(resultats1) == len(resultats2)}")

comparer_sequential_vs_threading()
```

### Multiprocessing pour les tâches CPU

```python
import multiprocessing
import math

def tache_cpu_intensive(n):
    """Tâche intensive pour le CPU."""
    total = 0
    for i in range(n):
        total += math.sqrt(i) * math.sin(i)
    return total

def comparer_sequential_vs_multiprocessing():
    """Compare exécution séquentielle vs multiprocessing."""

    nombres = [1000000] * 4  # 4 tâches intensives

    # Exécution séquentielle
    @mesurer_temps
    def execution_sequentielle():
        return [tache_cpu_intensive(n) for n in nombres]

    # Exécution avec multiprocessing
    @mesurer_temps
    def execution_avec_multiprocessing():
        with multiprocessing.Pool() as pool:
            return pool.map(tache_cpu_intensive, nombres)

    print("🖥️  Comparaison séquentiel vs multiprocessing:")

    print("Exécution séquentielle:")
    resultats1 = execution_sequentielle()

    print("Exécution avec multiprocessing:")
    resultats2 = execution_avec_multiprocessing()

    print(f"Résultats identiques: {resultats1 == resultats2}")

# Note: Uncomment to test (peut être lent)
# comparer_sequential_vs_multiprocessing()
```

## Optimisation avec NumPy

### NumPy vs Python pur

```python
import numpy as np

def comparer_numpy_vs_python():
    """Compare NumPy avec Python pur pour les calculs numériques."""

    # Données de test
    taille = 1000000

    # Python pur
    @mesurer_temps
    def calcul_python_pur():
        a = list(range(taille))
        b = list(range(taille, taille * 2))
        c = []

        for i in range(taille):
            c.append(a[i] * b[i] + a[i])

        return sum(c)

    # Avec NumPy
    @mesurer_temps
    def calcul_numpy():
        a = np.arange(taille)
        b = np.arange(taille, taille * 2)
        c = a * b + a
        return np.sum(c)

    print("🔢 Calculs numériques sur 1 million d'éléments:")

    resultat1 = calcul_python_pur()
    resultat2 = calcul_numpy()

    print(f"Résultats identiques: {abs(resultat1 - resultat2) < 0.001}")

# Note: Uncomment if NumPy is installed
# comparer_numpy_vs_python()
```

## Outils de profiling avancés

### Memory profiler

```python
# Code d'exemple pour memory_profiler
# Installation: pip install memory-profiler

def exemple_memory_profiler():
    """Exemple d'utilisation de memory_profiler."""

    code_exemple = '''
# fichier: exemple_memoire.py
from memory_profiler import profile

@profile
def fonction_gourmande():
    # Créer une grande liste
    grande_liste = [i**2 for i in range(100000)]

    # Créer un dictionnaire
    grand_dict = {i: i**3 for i in range(50000)}

    # Libérer la mémoire
    del grande_liste
    del grand_dict

    return "Terminé"

if __name__ == "__main__":
    fonction_gourmande()
'''

    print("🧠 Exemple d'utilisation de memory_profiler:")
    print(code_exemple)
    print("\nPour utiliser:")
    print("1. pip install memory-profiler")
    print("2. python -m memory_profiler exemple_memoire.py")

exemple_memory_profiler()
```

### Line profiler

```python
def exemple_line_profiler():
    """Exemple d'utilisation de line_profiler."""

    code_exemple = '''
# Installation: pip install line_profiler

@profile  # Décorateur pour line_profiler
def fonction_a_optimiser():
    # Ligne 1: Opération rapide
    a = [1, 2, 3, 4, 5]

    # Ligne 2: Opération lente
    b = [x**2 for x in range(10000)]

    # Ligne 3: Opération très lente
    c = [sum(range(i)) for i in range(1000)]

    return len(a) + len(b) + len(c)

if __name__ == "__main__":
    fonction_a_optimiser()
'''

    print("⚡ Exemple d'utilisation de line_profiler:")
    print(code_exemple)
    print("\nPour utiliser:")
    print("1. pip install line_profiler")
    print("2. kernprof -l -v script.py")

exemple_line_profiler()
```

## Bonnes pratiques d'optimisation

### 1. Mesurez avant d'optimiser

```python
def principe_mesurer_avant():
    """Illustre l'importance de mesurer avant d'optimiser."""

    def fonction_supposee_lente():
        """Fonction qu'on suppose lente."""
        return sum(x**2 for x in range(1000))

    def fonction_supposee_rapide():
        """Fonction qu'on suppose rapide."""
        total = 0
        for x in range(1000):
            total += x * x
        return total

    # Mesurer les deux
    temps1 = timeit.timeit(fonction_supposee_lente, number=10000)
    temps2 = timeit.timeit(fonction_supposee_rapide, number=10000)

    print("📏 Importance de mesurer:")
    print(f"Fonction 'supposée lente': {temps1:.4f}s")
    print(f"Fonction 'supposée rapide': {temps2:.4f}s")

    if temps1 < temps2:
        print("⚠️  Surprise! La 'lente' est plus rapide!")
    else:
        print("✅ L'intuition était correcte")

principe_mesurer_avant()
```

### 2. Optimisez les goulots d'étranglement

```python
def principe_goulets_etranglement():
    """Montre l'importance de cibler les vrais goulots d'étranglement."""

    def traitement_complet():
        """Fonction avec plusieurs étapes de vitesses différentes."""

        # Étape 1: Rapide (5% du temps)
        debut = time.time()
        donnees = list(range(1000))
        etape1 = time.time() - debut

        # Étape 2: Très lente (90% du temps) - LE GOULOT !
        debut = time.time()
        for i in range(len(donnees)):
            for j in range(len(donnees)):
                if i != j:
                    _ = donnees[i] + donnees[j]  # Opération O(n²)
        etape2 = time.time() - debut

        # Étape 3: Rapide (5% du temps)
        debut = time.time()
        resultat = sum(donnees)
        etape3 = time.time() - debut

        return etape1, etape2, etape3, resultat

    print("🎯 Identification des goulots d'étranglement:")

    etape1, etape2, etape3, resultat = traitement_complet()
    total = etape1 + etape2 + etape3

    print(f"Étape 1 (initialisation): {etape1:.4f}s ({etape1/total*100:.1f}%)")
    print(f"Étape 2 (calcul O(n²)):   {etape2:.4f}s ({etape2/total*100:.1f}%)")
    print(f"Étape 3 (somme):          {etape3:.4f}s ({etape3/total*100:.1f}%)")
    print(f"Total:                    {total:.4f}s")

    print("\n💡 Leçon: Optimiser l'étape 2 aura le plus gros impact!")
    print("   Optimiser les étapes 1 et 3 ne changera presque rien.")

principe_goulets_etranglement()
```

### 3. La règle des 80/20

```python
def regle_80_20():
    """Illustre la règle des 80/20 en optimisation."""

    def analyser_performance():
        """Simule l'analyse de performance d'une application."""

        fonctions = {
            'chargement_donnees': 0.1,      # 2% du temps
            'validation': 0.05,             # 1% du temps
            'calcul_principal': 4.0,        # 80% du temps
            'mise_en_cache': 0.2,           # 4% du temps
            'generation_rapport': 0.6,      # 12% du temps
            'nettoyage': 0.05               # 1% du temps
        }

        total = sum(fonctions.values())

        print("📊 Analyse de performance (règle 80/20):")
        print("Fonction                 | Temps  | % du total")
        print("-" * 45)

        # Trier par temps décroissant
        for nom, temps in sorted(fonctions.items(), key=lambda x: x[1], reverse=True):
            pourcentage = (temps / total) * 100
            print(f"{nom:<20} | {temps:>4.1f}s | {pourcentage:>6.1f}%")

        print(f"\nTotal: {total:.1f}s")
        print("\n💎 Priorités d'optimisation:")
        print("1. 🔥 calcul_principal (80% du temps) - IMPACT MAJEUR")
        print("2. 📈 generation_rapport (12% du temps) - Impact modéré")
        print("3. 🔧 Autres fonctions (8% du temps) - Impact mineur")

        return fonctions

    analyser_performance()

regle_80_20()
```

### 4. Optimisation incrémentale

```python
def optimisation_incrementale():
    """Montre l'approche d'optimisation étape par étape."""

    # Version 1: Code initial (naïf)
    @mesurer_temps
    def version_1_naive():
        """Version initiale - code simple mais lent."""
        resultat = []
        for i in range(10000):
            if i % 2 == 0:  # Nombre pair
                for j in range(i):
                    if j % 3 == 0:  # Multiple de 3
                        resultat.append(i + j)
        return len(resultat)

    # Version 2: Éliminer la boucle interne
    @mesurer_temps
    def version_2_optimisee():
        """Version optimisée - éviter la boucle interne."""
        resultat = []
        for i in range(0, 10000, 2):  # Directement les pairs
            # Calculer combien de multiples de 3 il y a entre 0 et i
            nb_multiples = i // 3
            resultat.extend([i + j for j in range(0, i, 3)])
        return len(resultat)

    # Version 3: Calcul mathématique
    @mesurer_temps
    def version_3_mathematique():
        """Version mathématique - calcul direct."""
        total = 0
        for i in range(0, 10000, 2):  # Nombres pairs
            nb_multiples = i // 3
            total += nb_multiples
        return total

    print("🔄 Optimisation incrémentale:")

    print("Version 1 (naïve):")
    r1 = version_1_naive()

    print("Version 2 (optimisée):")
    r2 = version_2_optimisee()

    print("Version 3 (mathématique):")
    r3 = version_3_mathematique()

    print(f"\nRésultats cohérents: {r1}, {r2}, {r3}")

optimisation_incrementale()
```

## Cas pratiques d'optimisation

### Cas 1: Traitement de fichiers volumineux

```python
def optimiser_traitement_fichier():
    """Optimise le traitement d'un gros fichier."""

    # Créer un fichier de test
    nom_fichier = "test_gros_fichier.txt"

    # Générer le fichier (simulé)
    def creer_fichier_test():
        print("📝 Création du fichier de test...")
        # Simulé - en réalité on écrirait vraiment le fichier
        return ["ligne " + str(i) for i in range(100000)]

    lignes = creer_fichier_test()

    # Version 1: Charger tout en mémoire
    @mesurer_temps
    def traitement_v1_tout_en_memoire():
        """Charge tout le fichier en mémoire."""
        # Simuler la lecture complète
        toutes_les_lignes = lignes  # En réalité: open(fichier).readlines()

        compteur = 0
        for ligne in toutes_les_lignes:
            if "5" in ligne:  # Condition simple
                compteur += 1

        return compteur

    # Version 2: Lecture ligne par ligne
    @mesurer_temps
    def traitement_v2_ligne_par_ligne():
        """Lit le fichier ligne par ligne."""
        compteur = 0

        # Simuler la lecture ligne par ligne
        for ligne in lignes:  # En réalité: for ligne in open(fichier):
            if "5" in ligne:
                compteur += 1

        return compteur

    # Version 3: Lecture par chunks avec générateur
    @mesurer_temps
    def traitement_v3_par_chunks():
        """Traite le fichier par blocs."""

        def lire_par_chunks(donnees, taille_chunk=1000):
            """Générateur qui lit par chunks."""
            for i in range(0, len(donnees), taille_chunk):
                yield donnees[i:i + taille_chunk]

        compteur = 0
        for chunk in lire_par_chunks(lignes):
            for ligne in chunk:
                if "5" in ligne:
                    compteur += 1

        return compteur

    print("📁 Optimisation traitement de fichier (100k lignes):")

    r1 = traitement_v1_tout_en_memoire()
    r2 = traitement_v2_ligne_par_ligne()
    r3 = traitement_v3_par_chunks()

    print(f"Résultats identiques: {r1 == r2 == r3}")
    print(f"Lignes contenant '5': {r1}")

optimiser_traitement_fichier()
```

### Cas 2: Optimisation de requêtes de données

```python
def optimiser_requetes_donnees():
    """Optimise les requêtes sur des données."""

    # Simuler une base de données
    utilisateurs = [
        {'id': i, 'nom': f'User{i}', 'age': 20 + (i % 50), 'ville': f'Ville{i % 10}'}
        for i in range(10000)
    ]

    # Version 1: Recherche linéaire répétée
    @mesurer_temps
    def requetes_v1_lineaire():
        """Recherche linéaire pour chaque requête."""
        ids_recherches = [100, 500, 1000, 5000, 9999]
        resultats = []

        for user_id in ids_recherches:
            for user in utilisateurs:  # O(n) pour chaque recherche !
                if user['id'] == user_id:
                    resultats.append(user)
                    break

        return len(resultats)

    # Version 2: Index avec dictionnaire
    @mesurer_temps
    def requetes_v2_avec_index():
        """Utilise un index pour des recherches O(1)."""
        # Créer l'index une fois
        index_users = {user['id']: user for user in utilisateurs}

        ids_recherches = [100, 500, 1000, 5000, 9999]
        resultats = []

        for user_id in ids_recherches:
            if user_id in index_users:  # O(1) pour chaque recherche !
                resultats.append(index_users[user_id])

        return len(resultats)

    # Version 3: Recherche par lot
    @mesurer_temps
    def requetes_v3_par_lot():
        """Recherche plusieurs éléments en une fois."""
        ids_recherches = {100, 500, 1000, 5000, 9999}  # Set pour recherche O(1)
        resultats = []

        # Un seul passage sur les données
        for user in utilisateurs:
            if user['id'] in ids_recherches:
                resultats.append(user)
                ids_recherches.remove(user['id'])
                if not ids_recherches:  # Optimisation: arrêter si tout trouvé
                    break

        return len(resultats)

    print("🔍 Optimisation de requêtes (10k utilisateurs):")

    r1 = requetes_v1_lineaire()
    r2 = requetes_v2_avec_index()
    r3 = requetes_v3_par_lot()

    print(f"Résultats identiques: {r1 == r2 == r3}")

optimiser_requetes_donnees()
```

### Cas 3: Optimisation d'algorithmes

```python
def optimiser_algorithme_tri():
    """Compare différents algorithmes de tri."""

    import random

    # Données de test
    donnees_petites = random.sample(range(1000), 100)
    donnees_moyennes = random.sample(range(10000), 1000)

    # Tri à bulles O(n²)
    def tri_bulle(arr):
        """Tri à bulles - simple mais lent."""
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # Tri rapide O(n log n)
    def tri_rapide(arr):
        """Tri rapide - efficace."""
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        gauche = [x for x in arr if x < pivot]
        milieu = [x for x in arr if x == pivot]
        droite = [x for x in arr if x > pivot]

        return tri_rapide(gauche) + milieu + tri_rapide(droite)

    # Tri Python natif O(n log n) optimisé
    def tri_python(arr):
        """Tri Python natif (Timsort)."""
        return sorted(arr)

    def comparer_tris(donnees, nom):
        """Compare les performances des tris."""
        print(f"\n📊 Tri de {len(donnees)} éléments ({nom}):")

        # Mesurer chaque algorithme
        temps_bulle = timeit.timeit(lambda: tri_bulle(donnees), number=1)
        temps_rapide = timeit.timeit(lambda: tri_rapide(donnees), number=10) / 10
        temps_python = timeit.timeit(lambda: tri_python(donnees), number=100) / 100

        print(f"Tri à bulles:  {temps_bulle:.6f}s")
        print(f"Tri rapide:    {temps_rapide:.6f}s")
        print(f"Tri Python:    {temps_python:.6f}s")

        # Gains de performance
        print(f"Tri rapide est {temps_bulle/temps_rapide:.1f}x plus rapide que bulle")
        print(f"Tri Python est {temps_bulle/temps_python:.1f}x plus rapide que bulle")

        # Vérifier que les résultats sont identiques
        r1 = tri_bulle(donnees)
        r2 = tri_rapide(donnees)
        r3 = tri_python(donnees)
        print(f"Résultats identiques: {r1 == r2 == r3}")

    print("🚀 Comparaison d'algorithmes de tri:")
    comparer_tris(donnees_petites, "petites données")
    comparer_tris(donnees_moyennes, "données moyennes")

optimiser_algorithme_tri()
```

## Outils de monitoring en production

### Mesure continue des performances

```python
import time
import logging
from functools import wraps
from collections import defaultdict

class PerformanceMonitor:
    """Moniteur de performance pour applications en production."""

    def __init__(self):
        self.stats = defaultdict(list)
        self.logger = logging.getLogger(__name__)

    def monitor(self, fonction_nom=None):
        """Décorateur pour monitorer les performances."""
        def decorator(func):
            nom = fonction_nom or func.__name__

            @wraps(func)
            def wrapper(*args, **kwargs):
                debut = time.time()
                try:
                    resultat = func(*args, **kwargs)
                    return resultat
                except Exception as e:
                    self.logger.error(f"Erreur dans {nom}: {e}")
                    raise
                finally:
                    duree = time.time() - debut
                    self.stats[nom].append(duree)

                    # Log si trop lent
                    if duree > 1.0:  # Plus d'1 seconde
                        self.logger.warning(f"{nom} lente: {duree:.2f}s")

            return wrapper
        return decorator

    def get_stats(self, nom_fonction):
        """Retourne les statistiques d'une fonction."""
        if nom_fonction not in self.stats:
            return None

        temps = self.stats[nom_fonction]
        return {
            'nb_appels': len(temps),
            'temps_total': sum(temps),
            'temps_moyen': sum(temps) / len(temps),
            'temps_min': min(temps),
            'temps_max': max(temps)
        }

    def rapport_complet(self):
        """Génère un rapport complet des performances."""
        print("📈 Rapport de performance:")
        print("-" * 60)
        print(f"{'Fonction':<20} {'Appels':<8} {'Moy.':<8} {'Min':<8} {'Max':<8}")
        print("-" * 60)

        for nom in sorted(self.stats.keys()):
            stats = self.get_stats(nom)
            print(f"{nom:<20} {stats['nb_appels']:<8} "
                  f"{stats['temps_moyen']:<8.3f} {stats['temps_min']:<8.3f} "
                  f"{stats['temps_max']:<8.3f}")

# Configuration du logging
logging.basicConfig(level=logging.INFO)

# Utilisation du moniteur
monitor = PerformanceMonitor()

@monitor.monitor("calcul_complexe")
def fonction_surveillee_1():
    """Fonction à surveiller."""
    time.sleep(0.1)  # Simule du travail
    return sum(range(1000))

@monitor.monitor("acces_donnees")
def fonction_surveillee_2():
    """Autre fonction à surveiller."""
    time.sleep(0.05)  # Simule un accès BD
    return "données"

def demo_monitoring():
    """Démonstration du monitoring."""

    print("🔍 Démonstration du monitoring de performance:")

    # Simuler des appels
    for i in range(10):
        fonction_surveillee_1()
        fonction_surveillee_2()
        if i == 5:
            # Simuler un appel lent
            time.sleep(1.1)
            fonction_surveillee_1()

    # Afficher le rapport
    monitor.rapport_complet()

demo_monitoring()
```

### Alertes de performance

```python
class AlertePerformance:
    """Système d'alerte pour les problèmes de performance."""

    def __init__(self, seuils=None):
        self.seuils = seuils or {
            'temps_reponse_max': 2.0,      # Secondes
            'utilisation_memoire_max': 80,  # Pourcentage
            'nb_erreurs_max': 5            # Par minute
        }
        self.erreurs_recentes = []

    def verifier_temps_reponse(self, duree, fonction):
        """Vérifie si le temps de réponse est acceptable."""
        if duree > self.seuils['temps_reponse_max']:
            self._envoyer_alerte(
                f"🚨 ALERTE: {fonction} trop lente ({duree:.2f}s)"
            )

    def verifier_memoire(self):
        """Vérifie l'utilisation mémoire."""
        # Simulation - en réalité utiliser psutil
        utilisation_simulee = 85  # %

        if utilisation_simulee > self.seuils['utilisation_memoire_max']:
            self._envoyer_alerte(
                f"🚨 ALERTE: Mémoire élevée ({utilisation_simulee}%)"
            )

    def enregistrer_erreur(self, erreur):
        """Enregistre une erreur et vérifie les seuils."""
        maintenant = time.time()
        self.erreurs_recentes.append(maintenant)

        # Nettoyer les erreurs anciennes (plus d'1 minute)
        self.erreurs_recentes = [
            t for t in self.erreurs_recentes
            if maintenant - t <= 60
        ]

        if len(self.erreurs_recentes) > self.seuils['nb_erreurs_max']:
            self._envoyer_alerte(
                f"🚨 ALERTE: Trop d'erreurs ({len(self.erreurs_recentes)} en 1 min)"
            )

    def _envoyer_alerte(self, message):
        """Envoie une alerte (simulation)."""
        print(f"📧 {message}")
        # En réalité: envoyer un email, SMS, webhook, etc.

# Démonstration du système d'alerte
alerte = AlertePerformance()

def demo_alertes():
    """Démonstration du système d'alerte."""

    print("🚨 Démonstration du système d'alerte:")

    # Simuler différents scénarios
    alerte.verifier_temps_reponse(3.5, "fonction_lente")
    alerte.verifier_memoire()

    # Simuler plusieurs erreurs
    for i in range(7):
        alerte.enregistrer_erreur(f"Erreur {i}")

demo_alertes()
```

## Checklist d'optimisation

### Avant d'optimiser

```python
def checklist_pre_optimisation():
    """Checklist à suivre avant d'optimiser."""

    checklist = [
        "✅ Le code fonctionne-t-il correctement ?",
        "✅ Avez-vous des tests pour vérifier que l'optimisation ne casse rien ?",
        "✅ Avez-vous mesuré les performances actuelles ?",
        "✅ Avez-vous identifié les vrais goulots d'étranglement ?",
        "✅ L'optimisation en vaut-elle la peine (impact utilisateur) ?",
        "✅ Avez-vous une stratégie de rollback si ça se passe mal ?"
    ]

    print("📋 Checklist pré-optimisation:")
    for item in checklist:
        print(f"  {item}")

    print("\n⚠️  Ne procédez à l'optimisation que si toutes les réponses sont OUI!")

checklist_pre_optimisation()
```

### Pendant l'optimisation

```python
def bonnes_pratiques_optimisation():
    """Bonnes pratiques pendant l'optimisation."""

    principes = [
        "🎯 Ciblez une métrique spécifique (temps, mémoire, CPU)",
        "📏 Mesurez avant et après chaque changement",
        "🔬 Optimisez une chose à la fois",
        "🧪 Testez sur des données réalistes",
        "📊 Documentez vos changements et leurs impacts",
        "🔄 Gardez le code lisible et maintenable",
        "⚖️  Attention aux compromis (vitesse vs mémoire)",
        "🚫 Arrêtez quand le gain devient négligeable"
    ]

    print("🛠️  Bonnes pratiques pendant l'optimisation:")
    for principe in principes:
        print(f"  {principe}")

bonnes_pratiques_optimisation()
```

## Résumé et conclusion

### Points clés à retenir

```python
def resume_optimisation():
    """Résumé des points clés de l'optimisation."""

    print("🎓 Résumé - Optimisation des performances:")
    print()

    sections = {
        "🔍 Mesure": [
            "Toujours mesurer avant d'optimiser",
            "Utiliser les bons outils (timeit, cProfile)",
            "Identifier les vrais goulots d'étranglement"
        ],

        "🧠 Algorithmes": [
            "Choisir la bonne complexité (O(1) > O(log n) > O(n) > O(n²))",
            "Utiliser les structures de données appropriées",
            "Préférer les fonctions intégrées Python"
        ],

        "💾 Mémoire": [
            "Utiliser des générateurs pour les gros volumes",
            "Éviter les créations d'objets inutiles",
            "Considérer __slots__ pour les classes simples"
        ],

        "🚀 Parallélisation": [
            "Threading pour les tâches I/O",
            "Multiprocessing pour les tâches CPU",
            "NumPy pour les calculs numériques"
        ],

        "🎯 Stratégie": [
            "Règle 80/20: optimiser ce qui compte",
            "Optimisation incrémentale",
            "Maintenir la lisibilité du code"
        ]
    }

    for titre, points in sections.items():
        print(f"{titre}")
        for point in points:
            print(f"  • {point}")
        print()

    print("🏆 Règle d'or: Un code correct et lisible vaut mieux qu'un code")
    print("   rapide mais bugué ou incompréhensible!")

resume_optimisation()
```

### Quand arrêter d'optimiser

```python
def quand_arreter_optimisation():
    """Critères pour arrêter l'optimisation."""

    criteres_arret = [
        "✅ Les performances sont acceptables pour les utilisateurs",
        "✅ Le gain supplémentaire est négligeable (< 10%)",
        "✅ Le code devient trop complexe à maintenir",
        "✅ Le temps d'optimisation coûte plus que le gain",
        "✅ Vous atteignez les limites physiques (réseau, disque)",
        "✅ D'autres priorités sont plus importantes"
    ]

    print("🛑 Quand arrêter d'optimiser:")
    for critere in criteres_arret:
        print(f"  {critere}")

    print("\n💡 Rappelez-vous: L'optimisation parfaite n'existe pas!")
    print("   L'objectif est d'avoir des performances 'suffisamment bonnes'.")

quand_arreter_optimisation()
```

## Exercices pratiques

### Exercice 1: Optimiser une fonction lente
```python
def exercice_optimisation():
    """Exercice: optimisez cette fonction lente."""

    def fonction_a_optimiser(donnees):
        """
        Cette fonction est lente. À vous de l'optimiser !

        Objectif: Trouve tous les nombres pairs et calcule leur somme.
        """
        resultats = []

        # Étape 1: Filtrer les pairs (lent!)
        for i in range(len(donnees)):
            for j in range(len(donnees)):
                if i != j and donnees[i] % 2 == 0:
                    resultats.append(donnees[i])

        # Étape 2: Supprimer les doublons (lent!)
        resultats_uniques = []
        for item in resultats:
            if item not in resultats_uniques:
                resultats_uniques.append(item)

        # Étape 3: Calculer la somme
        somme = 0
        for item in resultats_uniques:
            somme += item

        return somme

    # Version optimisée (à implémenter par l'étudiant)
    def fonction_optimisee(donnees):
        """Version optimisée de la fonction."""
        # À IMPLÉMENTER !
        # Indices:
        # 1. Éliminer les boucles imbriquées
        # 2. Utiliser set() pour les doublons
        # 3. Utiliser sum() et une compréhension de liste
        pass

    # Test
    test_donnees = list(range(1000)) * 2  # Avec doublons

    print("🧪 Exercice d'optimisation:")
    print("Optimisez la fonction_a_optimiser!")
    print(f"Données de test: {len(test_donnees)} éléments")

    # Mesurer la version lente
    resultat_lent = fonction_a_optimiser(test_donnees[:100])  # Seulement 100 pour éviter l'attente
    print(f"Résultat attendu: {resultat_lent}")

exercice_optimisation()
```

### Solution de l'exercice
```python
def solution_exercice():
    """Solution de l'exercice d'optimisation."""

    def fonction_optimisee(donnees):
        """Version optimisée."""
        # Une seule ligne suffit !
        return sum(set(x for x in donnees if x % 2 == 0))

    # Test de performance
    test_donnees = list(range(1000)) * 2

    @mesurer_temps
    def test_optimise():
        return fonction_optimisee(test_donnees)

    print("✅ Solution optimisée:")
    resultat = test_optimise()
    print(f"Résultat: {resultat}")
    print("Optimisations appliquées:")
    print("• Élimination des boucles imbriquées O(n²) → O(n)")
    print("• Utilisation de set() pour éliminer les doublons")
    print("• Compréhension de générateur + sum()")
    print("• Code plus lisible et maintenable")

solution_exercice()
```

L'optimisation des performances est un art qui demande de l'expérience. Commencez par maîtriser les bases (mesure, structures de données, algorithmes) avant de vous aventurer dans les optimisations avancées. Et n'oubliez jamais : un code qui fonctionne correctement est toujours préférable à un code rapide mais bugué !

La prochaine étape sera d'apprendre à déployer et distribuer vos applications Python de manière professionnelle.

⏭️
