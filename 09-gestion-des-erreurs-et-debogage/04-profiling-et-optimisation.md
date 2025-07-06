🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.4 : Profiling et optimisation

## Introduction

Imaginez que votre code Python soit une voiture. Elle fonctionne, mais elle consomme beaucoup d'essence et roule lentement sur l'autoroute. Comment savoir quel composant pose problème ? Il faut faire un diagnostic !

Le **profiling** (profilage en français) est exactement cela : un diagnostic de performance de votre code. Il vous montre où votre programme passe le plus de temps et utilise le plus de ressources.

L'**optimisation**, c'est la réparation qui suit : une fois qu'on sait où sont les problèmes, on peut les corriger pour rendre le code plus rapide et plus efficace.

## Pourquoi s'intéresser aux performances ?

### Quand optimiser ?

> "L'optimisation prématurée est la racine de tous les maux" - Donald Knuth

Cette citation célèbre signifie qu'il ne faut pas optimiser avant d'avoir un problème réel. Mais quand faut-il s'en préoccuper ?

**❌ N'optimisez PAS quand :**
- Votre code fonctionne assez vite pour vos besoins
- Vous n'avez pas fini de développer toutes les fonctionnalités
- Vous optimisez "au feeling" sans mesurer

**✅ Optimisez quand :**
- Votre programme est trop lent pour vos utilisateurs
- Vous traitez de gros volumes de données
- Vous avez mesuré et identifié les goulots d'étranglement

### Types de performances

```python
import time

def exemple_performances():
    # Performance en TEMPS (vitesse d'exécution)
    start = time.time()
    resultat = sum(range(1000000))
    temps_ecoule = time.time() - start
    print(f"⏱️ Temps d'exécution: {temps_ecoule:.4f} secondes")

    # Performance en MÉMOIRE (consommation RAM)
    import sys
    grande_liste = list(range(1000000))
    taille_memoire = sys.getsizeof(grande_liste) / 1024 / 1024  # MB
    print(f"💾 Mémoire utilisée: {taille_memoire:.2f} MB")

exemple_performances()
```

## Mesurer les performances : les bases

### 1. Le module time

```python
import time

def mesurer_temps(fonction, *args, **kwargs):
    """Mesure le temps d'exécution d'une fonction"""
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()

    temps_ecoule = fin - debut
    print(f"⏱️ {fonction.__name__} a pris {temps_ecoule:.4f} secondes")
    return resultat

def calcul_lent():
    """Simulation d'un calcul lent"""
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# Test
resultat = mesurer_temps(calcul_lent)
```

### 2. Le module timeit (plus précis)

```python
import timeit

# Mesure d'une petite opération (plus précis que time)
def comparer_methodes():
    # Méthode 1: boucle classique
    temps1 = timeit.timeit(
        'total = 0\nfor i in range(1000): total += i',
        number=1000
    )

    # Méthode 2: fonction sum()
    temps2 = timeit.timeit(
        'total = sum(range(1000))',
        number=1000
    )

    print(f"🔄 Boucle classique: {temps1:.4f} secondes")
    print(f"⚡ Fonction sum(): {temps2:.4f} secondes")
    print(f"📊 sum() est {temps1/temps2:.1f}x plus rapide")

comparer_methodes()
```

### 3. Décorateur pour mesurer automatiquement

```python
import functools
import time

def mesurer_performance(func):
    """Décorateur qui mesure automatiquement les performances"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()

        temps = fin - debut
        print(f"⏱️ {func.__name__}: {temps:.4f}s")
        return resultat
    return wrapper

@mesurer_performance
def traiter_donnees(donnees):
    # Simulation de traitement
    return [x * 2 for x in donnees if x > 0]

@mesurer_performance
def traiter_donnees_optimisee(donnees):
    # Version optimisée avec filter et map
    return list(map(lambda x: x * 2, filter(lambda x: x > 0, donnees)))

# Tests comparatifs
donnees_test = list(range(-500, 500))
resultat1 = traiter_donnees(donnees_test)
resultat2 = traiter_donnees_optimisee(donnees_test)
```

## Le profiling avec cProfile

### Profiling basique

```python
import cProfile
import pstats
from io import StringIO

def fonction_complexe():
    """Fonction avec plusieurs sous-fonctions pour démonstration"""

    def calcul_a():
        return sum(range(100000))

    def calcul_b():
        return sum(x ** 2 for x in range(50000))

    def calcul_c():
        time.sleep(0.1)  # Simulation d'une opération I/O

    # Appels multiples
    for _ in range(3):
        calcul_a()

    for _ in range(2):
        calcul_b()

    calcul_c()

# Profiling de la fonction
print("🔬 Profiling avec cProfile:")
cProfile.run('fonction_complexe()')
```

### Profiling avec sauvegarde et analyse

```python
def analyser_performances():
    """Analyse détaillée des performances"""

    # Création du profiler
    profiler = cProfile.Profile()

    # Démarrage du profiling
    profiler.enable()

    # Code à analyser
    fonction_complexe()

    # Arrêt du profiling
    profiler.disable()

    # Analyse des résultats
    s = StringIO()
    stats = pstats.Stats(profiler, stream=s)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 des fonctions les plus lentes

    print("📊 Rapport de performance:")
    print(s.getvalue())

analyser_performances()
```

## Optimisation : les techniques courantes

### 1. Optimisation des boucles

```python
import time

def exemple_optimisation_boucles():
    donnees = list(range(100000))

    # ❌ Version lente
    def version_lente(donnees):
        resultat = []
        for i in range(len(donnees)):
            if donnees[i] % 2 == 0:
                resultat.append(donnees[i] * 2)
        return resultat

    # ✅ Version rapide
    def version_rapide(donnees):
        return [x * 2 for x in donnees if x % 2 == 0]

    # ⚡ Version très rapide avec générateur
    def version_generateur(donnees):
        return (x * 2 for x in donnees if x % 2 == 0)

    # Comparaison
    start = time.time()
    res1 = version_lente(donnees)
    temps1 = time.time() - start

    start = time.time()
    res2 = version_rapide(donnees)
    temps2 = time.time() - start

    start = time.time()
    res3 = list(version_generateur(donnees))  # Conversion pour comparer
    temps3 = time.time() - start

    print(f"❌ Version lente: {temps1:.4f}s")
    print(f"✅ List comprehension: {temps2:.4f}s ({temps1/temps2:.1f}x plus rapide)")
    print(f"⚡ Générateur: {temps3:.4f}s ({temps1/temps3:.1f}x plus rapide)")

exemple_optimisation_boucles()
```

### 2. Éviter les recalculs inutiles

```python
# ❌ Fonction lente avec recalculs
def fibonacci_lent(n):
    """Calcul de Fibonacci sans mémorisation"""
    if n <= 1:
        return n
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)

# ✅ Version optimisée avec mémorisation
def fibonacci_optimise():
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]

        if n <= 1:
            result = n
        else:
            result = fib(n-1) + fib(n-2)

        cache[n] = result
        return result

    return fib

# Comparaison des performances
@mesurer_performance
def test_fibonacci_lent():
    return fibonacci_lent(30)

@mesurer_performance
def test_fibonacci_optimise():
    fib = fibonacci_optimise()
    return fib(30)

print("Comparaison Fibonacci:")
print("❌ Version lente (30):")
# test_fibonacci_lent()  # Trop lent, on commente

print("✅ Version optimisée (30):")
test_fibonacci_optimise()

# Test avec un nombre plus grand
fib_opt = fibonacci_optimise()
print(f"⚡ Fibonacci(100) optimisé: {fib_opt(100)}")
```

### 3. Optimisation des structures de données

```python
def comparer_structures_donnees():
    # Données de test
    donnees = list(range(10000))

    # Test 1: Recherche dans une liste vs set
    print("🔍 Test de recherche:")

    @mesurer_performance
    def recherche_liste(donnees, element):
        return element in donnees  # O(n)

    @mesurer_performance
    def recherche_set(donnees_set, element):
        return element in donnees_set  # O(1)

    donnees_set = set(donnees)

    # Recherche d'un élément à la fin
    element_recherche = 9999

    print("❌ Recherche dans liste:")
    recherche_liste(donnees, element_recherche)

    print("✅ Recherche dans set:")
    recherche_set(donnees_set, element_recherche)

    # Test 2: Ajout d'éléments
    print("\n➕ Test d'ajout d'éléments:")

    @mesurer_performance
    def ajout_liste():
        resultat = []
        for i in range(1000):
            resultat.append(i)
        return resultat

    @mesurer_performance
    def ajout_comprehension():
        return [i for i in range(1000)]

    print("❌ Ajout avec append:")
    ajout_liste()

    print("✅ List comprehension:")
    ajout_comprehension()

comparer_structures_donnees()
```

### 4. Optimisation des chaînes de caractères

```python
def optimisation_chaines():
    mots = ["hello", "world", "python", "optimization"] * 1000

    # ❌ Concaténation lente
    @mesurer_performance
    def concatenation_lente(mots):
        resultat = ""
        for mot in mots:
            resultat += mot + " "
        return resultat.strip()

    # ✅ Join rapide
    @mesurer_performance
    def concatenation_rapide(mots):
        return " ".join(mots)

    # 🚀 Avec f-strings pour format complexe
    @mesurer_performance
    def format_complexe(mots):
        return " | ".join(f"[{mot.upper()}]" for mot in mots)

    print("Optimisation des chaînes:")
    print("❌ Concaténation avec +=:")
    concatenation_lente(mots)

    print("✅ Méthode join():")
    concatenation_rapide(mots)

    print("🚀 Join avec f-strings:")
    format_complexe(mots)

optimisation_chaines()
```

## Profiling de la mémoire

### Mesurer l'utilisation mémoire

```python
import sys
import gc

def analyser_memoire():
    """Analyse de l'utilisation mémoire"""

    def taille_objet(obj, nom):
        taille = sys.getsizeof(obj)
        print(f"💾 {nom}: {taille} bytes ({taille/1024:.2f} KB)")
        return taille

    # Comparaison de structures
    print("Comparaison mémoire des structures:")

    # Liste vs Tuple
    ma_liste = list(range(1000))
    mon_tuple = tuple(range(1000))

    taille_objet(ma_liste, "Liste de 1000 éléments")
    taille_objet(mon_tuple, "Tuple de 1000 éléments")

    # String vs List de caractères
    ma_chaine = "hello" * 200
    ma_liste_chars = list("hello" * 200)

    taille_objet(ma_chaine, "Chaîne 'hello' * 200")
    taille_objet(ma_liste_chars, "Liste de caractères")

    # Générateur vs Liste
    ma_liste_range = list(range(1000))
    mon_generateur = range(1000)

    taille_objet(ma_liste_range, "Liste range(1000)")
    taille_objet(mon_generateur, "Générateur range(1000)")

analyser_memoire()
```

### Optimisation mémoire avec générateurs

```python
def demo_generateurs():
    """Démonstration de l'efficacité mémoire des générateurs"""

    # ❌ Version qui consomme beaucoup de mémoire
    def traiter_gros_fichier_v1():
        # Simulation: charger tout en mémoire
        toutes_les_lignes = [f"ligne {i}" for i in range(1000000)]
        lignes_filtrees = [ligne for ligne in toutes_les_lignes if "5" in ligne]
        return len(lignes_filtrees)

    # ✅ Version économe en mémoire avec générateurs
    def traiter_gros_fichier_v2():
        # Traitement ligne par ligne
        def generer_lignes():
            for i in range(1000000):
                yield f"ligne {i}"

        def filtrer_lignes(lignes):
            for ligne in lignes:
                if "5" in ligne:
                    yield ligne

        lignes = generer_lignes()
        lignes_filtrees = filtrer_lignes(lignes)
        return sum(1 for _ in lignes_filtrees)  # Compte sans stocker

    print("Comparaison mémoire - traitement de gros volume:")

    # Mesure mémoire avant
    import psutil
    import os
    process = psutil.Process(os.getpid())

    print("🚀 Test avec générateurs:")
    mem_avant = process.memory_info().rss / 1024 / 1024
    resultat2 = mesurer_temps(traiter_gros_fichier_v2)
    mem_apres = process.memory_info().rss / 1024 / 1024
    print(f"💾 Mémoire utilisée: {mem_apres - mem_avant:.2f} MB")

    # Note: On évite la version v1 car elle consommerait trop de mémoire

demo_generateurs()
```

## Optimisations avancées

### 1. Utilisation des modules optimisés

```python
# Comparaison entre solutions Python pures et modules optimisés
def comparaison_modules():
    import random
    import statistics
    import math

    # Données de test
    donnees = [random.random() for _ in range(100000)]

    # Calcul de moyenne
    @mesurer_performance
    def moyenne_manuelle(donnees):
        return sum(donnees) / len(donnees)

    @mesurer_performance
    def moyenne_statistics(donnees):
        return statistics.mean(donnees)

    print("Calcul de moyenne:")
    print("🐌 Version manuelle:")
    moyenne_manuelle(donnees)

    print("⚡ Module statistics:")
    moyenne_statistics(donnees)

    # Racine carrée
    nombres = list(range(100000))

    @mesurer_performance
    def sqrt_manuelle(nombres):
        return [x ** 0.5 for x in nombres]

    @mesurer_performance
    def sqrt_math(nombres):
        return [math.sqrt(x) for x in nombres]

    print("\nCalcul de racine carrée:")
    print("🐌 Puissance 0.5:")
    sqrt_manuelle(nombres)

    print("⚡ math.sqrt:")
    sqrt_math(nombres)

comparaison_modules()
```

### 2. Compilation avec Numba (si disponible)

```python
def exemple_numba():
    """Exemple d'optimisation avec Numba (nécessite: pip install numba)"""

    # Version Python pure
    def calcul_intensif_python(n):
        total = 0
        for i in range(n):
            for j in range(n):
                total += i * j
        return total

    # Version avec Numba (décommentez si numba est installé)
    # try:
    #     from numba import jit
    #
    #     @jit
    #     def calcul_intensif_numba(n):
    #         total = 0
    #         for i in range(n):
    #             for j in range(n):
    #                 total += i * j
    #         return total
    #
    #     print("Comparaison avec Numba:")
    #     n = 1000
    #
    #     print("🐌 Python pur:")
    #     mesurer_temps(calcul_intensif_python, n)
    #
    #     print("🚀 Numba JIT:")
    #     mesurer_temps(calcul_intensif_numba, n)
    #
    # except ImportError:
    #     print("⚠️ Numba non installé - pip install numba pour tester")

    print("💡 Numba peut accélérer les boucles intensives de 10x à 100x !")
    print("   Installation: pip install numba")

exemple_numba()
```

## Bonnes pratiques d'optimisation

### 1. Mesurer avant d'optimiser

```python
class OptimisationWorkflow:
    """Workflow d'optimisation structuré"""

    def __init__(self, nom_fonction):
        self.nom_fonction = nom_fonction
        self.mesures = {}

    def mesurer_baseline(self, fonction, *args, **kwargs):
        """Mesure la performance de base"""
        print(f"📊 Mesure baseline pour {self.nom_fonction}")
        temps = timeit.timeit(lambda: fonction(*args, **kwargs), number=10)
        self.mesures['baseline'] = temps
        print(f"⏱️ Temps baseline: {temps:.4f}s")
        return temps

    def mesurer_optimisation(self, nom_version, fonction, *args, **kwargs):
        """Mesure une version optimisée"""
        print(f"🚀 Test de {nom_version}")
        temps = timeit.timeit(lambda: fonction(*args, **kwargs), number=10)
        self.mesures[nom_version] = temps

        if 'baseline' in self.mesures:
            amelioration = self.mesures['baseline'] / temps
            print(f"⏱️ Temps {nom_version}: {temps:.4f}s ({amelioration:.1f}x plus rapide)")
        else:
            print(f"⏱️ Temps {nom_version}: {temps:.4f}s")

    def rapport_final(self):
        """Affiche un rapport final"""
        print(f"\n📈 Rapport final pour {self.nom_fonction}:")
        for version, temps in self.mesures.items():
            if version != 'baseline':
                if 'baseline' in self.mesures:
                    ratio = self.mesures['baseline'] / temps
                    print(f"  {version}: {ratio:.1f}x plus rapide que baseline")

# Exemple d'utilisation
def demo_workflow():
    workflow = OptimisationWorkflow("tri de liste")

    donnees = [random.randint(1, 1000) for _ in range(1000)]

    # Version baseline
    def tri_bubble_sort(arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # Version optimisée 1
    def tri_python_builtin(arr):
        return sorted(arr)

    # Version optimisée 2
    def tri_quicksort_simple(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return tri_quicksort_simple(left) + middle + tri_quicksort_simple(right)

    # Tests
    workflow.mesurer_baseline(tri_bubble_sort, donnees)
    workflow.mesurer_optimisation("builtin_sorted", tri_python_builtin, donnees)
    workflow.mesurer_optimisation("quicksort", tri_quicksort_simple, donnees)
    workflow.rapport_final()

# demo_workflow()  # Décommentez pour tester
```

### 2. Liste de vérifications pour l'optimisation

```python
def checklist_optimisation():
    """Checklist des optimisations courantes"""

    print("✅ Checklist d'optimisation Python:")
    print()
    print("🔍 1. Profiling et mesures:")
    print("   ▢ Mesuré les performances actuelles")
    print("   ▢ Identifié les goulots d'étranglement")
    print("   ▢ Défini des objectifs de performance")
    print()
    print("🏗️ 2. Structures de données:")
    print("   ▢ Utilisé set() pour les recherches fréquentes")
    print("   ▢ Utilisé dict() pour les mappages")
    print("   ▢ Considéré les générateurs pour gros volumes")
    print()
    print("🔄 3. Algorithmes:")
    print("   ▢ Évité les boucles imbriquées inutiles")
    print("   ▢ Utilisé les compréhensions de liste")
    print("   ▢ Implémenté la mémorisation si besoin")
    print()
    print("📚 4. Bibliothèques:")
    print("   ▢ Utilisé les fonctions built-in (sum, max, min...)")
    print("   ▢ Considéré NumPy pour calculs numériques")
    print("   ▢ Évalué Pandas pour manipulation de données")
    print()
    print("💾 5. Mémoire:")
    print("   ▢ Utilisé des générateurs pour économiser la mémoire")
    print("   ▢ Libéré les références inutiles")
    print("   ▢ Évité les copies inutiles de données")
    print()
    print("⚡ 6. Optimisations avancées:")
    print("   ▢ Considéré Numba pour calculs intensifs")
    print("   ▢ Évalué Cython si nécessaire")
    print("   ▢ Testé le multiprocessing pour parallélisation")

checklist_optimisation()
```

## Exercices pratiques

### Exercice 1 : Optimiser une fonction de recherche

```python
def exercice_optimisation_recherche():
    """
    Optimisez cette fonction de recherche !
    """

    # ❌ Version à optimiser
    def rechercher_mots_lente(texte, mots_recherches):
        """Recherche des mots dans un texte - VERSION LENTE"""
        resultats = []
        mots_texte = texte.lower().split()

        for mot_recherche in mots_recherches:
            count = 0
            for mot in mots_texte:
                if mot_recherche.lower() in mot:
                    count += 1
            resultats.append((mot_recherche, count))

        return resultats

    # ✅ Version optimisée (à compléter !)
    def rechercher_mots_rapide(texte, mots_recherches):
        """Recherche des mots dans un texte - VERSION RAPIDE"""
        # TODO: Optimisez cette fonction !
        # Indices:
        # - Évitez les conversions répétées en minuscules
        # - Utilisez des structures de données appropriées
        # - Considérez les compréhensions de liste
        pass

    # Test
    texte_test = " ".join(["python", "programmation", "optimisation"] * 1000)
    mots_test = ["python", "optim", "prog"]

    print("Test de l'exercice d'optimisation:")
    print("❌ Version lente:")
    mesurer_temps(rechercher_mots_lente, texte_test, mots_test)

# exercice_optimisation_recherche()
```

### Exercice 2 : Cache intelligent

```python
def exercice_cache():
    """
    Implémentez un système de cache intelligent
    """

    class CacheIntelligent:
        def __init__(self, taille_max=100):
            self.cache = {}
            self.taille_max = taille_max
            self.access_count = {}
            # TODO: Ajoutez d'autres attributs si nécessaire

        def get(self, cle, fonction_calcul, *args):
            """
            Récupère une valeur du cache ou la calcule
            """
            # TODO: Implémentez la logique de cache
            # - Si la clé existe, la retourner
            # - Sinon, calculer avec fonction_calcul(*args)
            # - Gérer la taille maximale du cache
            # - Implémenter une stratégie d'éviction (LRU, LFU, etc.)
            pass

        def stats(self):
            """Affiche les statistiques du cache"""
            # TODO: Implémentez les statistiques
            pass

    # Test du cache
    cache = CacheIntelligent(taille_max=3)

    def calcul_lourd(n):
        """Simulation d'un calcul coûteux"""
        time.sleep(0.1)
        return n ** 2

    print("Test du cache intelligent:")
    # TODO: Testez votre implémentation

# exercice_cache()
```

## Résumé

L'optimisation est un art qui combine mesure et technique :

### **Règles d'or :**
1. **Mesurez d'abord** - Ne devinez jamais, profilez !
2. **Optimisez les goulots** - 80% du temps dans 20% du code
3. **Restez lisible** - Un code illisible n'est jamais une bonne optimisation
4. **Testez après** - Vérifiez que l'optimisation fonctionne

### **Outils essentiels :**
- **time/timeit** : Mesures simples de performance
- **cProfile** : Profiling détaillé du code
- **sys.getsizeof** : Mesure de la mémoire
- **Générateurs** : Économie de mémoire

### **Techniques courantes :**
- **List comprehensions** au lieu de boucles
- **Sets** pour les recherches fréquentes
- **join()** pour concaténer des chaînes
- **Mémorisation** pour éviter les recalculs
- **Modules optimisés** (statistics, math, etc.)

### **Workflow d'optimisation :**
1. 📊 **Profiler** le code existant
2. 🎯 **Identifier** les goulots d'étranglement
3. 🔧 **Optimiser** une partie à la fois
4. ⏱️ **Mesurer** l'amélioration
5. ✅ **Valider** que tout fonctionne encore

**Rappelez-vous :** Un code qui fonctionne correctement est plus important qu'un code ultra-optimisé ! L'optimisation vient après la fonctionnalité.

---

**À retenir :** L'optimisation, c'est comme régler un moteur : on mesure d'abord, on ajuste précisément, et on vérifie que ça roule toujours !

⏭️
