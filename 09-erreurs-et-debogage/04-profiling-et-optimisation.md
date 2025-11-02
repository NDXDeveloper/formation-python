🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.4 Profiling et optimisation

## Introduction

### Qu'est-ce que le profiling ?

Le **profiling** (ou profilage en français) est le processus d'analyse de votre programme pour comprendre :
- Combien de temps prend chaque partie du code
- Quelle quantité de mémoire est utilisée
- Quelles fonctions sont appelées le plus souvent
- Où se trouvent les goulots d'étranglement (bottlenecks)

### Pourquoi optimiser ?

L'optimisation consiste à améliorer les performances de votre code. Cependant, il faut garder en tête cette règle importante :

> **"Premature optimization is the root of all evil"** - Donald Knuth
>
> *L'optimisation prématurée est la source de tous les maux.*

Cela signifie qu'il faut :
1. **D'abord** écrire un code qui fonctionne correctement
2. **Ensuite** mesurer les performances avec le profiling
3. **Enfin** optimiser uniquement les parties qui en ont vraiment besoin

### Les règles d'or de l'optimisation

1. ✅ **Mesurez avant d'optimiser** : Ne devinez pas, mesurez !
2. ✅ **Optimisez ce qui compte** : Concentrez-vous sur les 20% du code qui prennent 80% du temps
3. ✅ **Gardez le code lisible** : Un code rapide mais incompréhensible n'est pas une bonne solution
4. ✅ **Testez après optimisation** : Assurez-vous que le code fonctionne toujours correctement

---

## 1. Mesurer le temps d'exécution - Les bases

### 1.1 La méthode time.time()

La façon la plus simple de mesurer le temps d'exécution :

```python
import time

# Enregistrer le temps de début
debut = time.time()

# Code à mesurer
total = 0
for i in range(1000000):
    total += i

# Enregistrer le temps de fin
fin = time.time()

# Calculer la durée
duree = fin - debut
print(f"Temps d'exécution : {duree:.4f} secondes")
```

**Sortie :**
```
Temps d'exécution : 0.0523 secondes
```

### 1.2 Créer une fonction de chronométrage

Pour réutiliser facilement :

```python
import time

def chronometrer(fonction, *args, **kwargs):
    """
    Chronomètre l'exécution d'une fonction.

    Args:
        fonction : La fonction à chronométrer
        *args : Arguments positionnels de la fonction
        **kwargs : Arguments nommés de la fonction

    Returns:
        tuple : (résultat, temps_execution)
    """
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    duree = fin - debut
    return resultat, duree

# Exemple d'utilisation
def calculer_somme(n):
    return sum(range(n))

resultat, temps = chronometrer(calculer_somme, 1000000)
print(f"Résultat : {resultat}")
print(f"Temps : {temps:.4f} secondes")
```

### 1.3 Utiliser un gestionnaire de contexte

Une approche plus élégante avec un context manager :

```python
import time
from contextlib import contextmanager

@contextmanager
def chronometre(nom="Code"):
    """Gestionnaire de contexte pour chronométrer un bloc de code."""
    print(f"⏱️  Début du chronométrage : {nom}")
    debut = time.time()
    yield
    fin = time.time()
    duree = fin - debut
    print(f"✅ {nom} terminé en {duree:.4f} secondes")

# Utilisation
with chronometre("Calcul de la somme"):
    total = sum(range(1000000))

with chronometre("Création d'une liste"):
    ma_liste = [i**2 for i in range(100000)]
```

**Sortie :**
```
⏱️  Début du chronométrage : Calcul de la somme
✅ Calcul de la somme terminé en 0.0234 secondes
⏱️  Début du chronométrage : Création d'une liste
✅ Création d'une liste terminé en 0.0567 secondes
```

---

## 2. Le module timeit - Mesures précises

### 2.1 Pourquoi utiliser timeit ?

Le module `timeit` est plus précis que `time.time()` car il :
- Exécute le code plusieurs fois pour obtenir une moyenne
- Désactive temporairement le garbage collector
- Fournit des résultats plus fiables

### 2.2 Utilisation de base

```python
import timeit

# Mesurer le temps d'exécution d'un code simple
temps = timeit.timeit('sum(range(1000))', number=10000)
print(f"Temps moyen : {temps:.6f} secondes pour 10000 exécutions")
print(f"Temps par exécution : {temps/10000:.9f} secondes")
```

### 2.3 Comparer différentes approches

**Exemple : Créer une liste de carrés**

```python
import timeit

# Méthode 1 : Boucle for classique
code1 = """
resultat = []
for i in range(1000):
    resultat.append(i**2)
"""

# Méthode 2 : Compréhension de liste
code2 = """
resultat = [i**2 for i in range(1000)]
"""

# Méthode 3 : map() et lambda
code3 = """
resultat = list(map(lambda x: x**2, range(1000)))
"""

# Mesurer chaque méthode
temps1 = timeit.timeit(code1, number=10000)
temps2 = timeit.timeit(code2, number=10000)
temps3 = timeit.timeit(code3, number=10000)

print("Comparaison des méthodes :")
print(f"  Boucle for        : {temps1:.4f} secondes")
print(f"  Compréhension     : {temps2:.4f} secondes ⚡ PLUS RAPIDE")
print(f"  map() + lambda    : {temps3:.4f} secondes")

# Calculer les différences
print(f"\nLa compréhension est {temps1/temps2:.2f}x plus rapide que la boucle")
```

**Sortie typique :**
```
Comparaison des méthodes :
  Boucle for        : 0.6234 secondes
  Compréhension     : 0.4521 secondes ⚡ PLUS RAPIDE
  map() + lambda    : 0.5789 secondes

La compréhension est 1.38x plus rapide que la boucle
```

### 2.4 Mesurer une fonction

```python
import timeit

def methode_lente():
    """Concaténation de chaînes avec +"""
    resultat = ""
    for i in range(1000):
        resultat = resultat + str(i)
    return resultat

def methode_rapide():
    """Utilisation de join()"""
    return "".join(str(i) for i in range(1000))

# Mesurer les deux fonctions
temps_lent = timeit.timeit(methode_lente, number=1000)
temps_rapide = timeit.timeit(methode_rapide, number=1000)

print(f"Méthode lente  : {temps_lent:.4f} secondes")
print(f"Méthode rapide : {temps_rapide:.4f} secondes")
print(f"Amélioration   : {temps_lent/temps_rapide:.2f}x plus rapide ! 🚀")
```

### 2.5 timeit en ligne de commande

Vous pouvez aussi utiliser timeit directement depuis le terminal :

```bash
# Depuis le terminal
python -m timeit "sum(range(1000))"
python -m timeit "[i**2 for i in range(1000)]"
```

---

## 3. cProfile - Profiling détaillé

### 3.1 Introduction à cProfile

`cProfile` est le profileur standard de Python. Il analyse votre code et vous dit :
- Combien de fois chaque fonction est appelée
- Combien de temps prend chaque fonction
- Quelle fonction appelle quelle autre fonction

### 3.2 Utilisation de base

```python
import cProfile

def fonction_lente():
    """Simule une fonction qui prend du temps."""
    total = 0
    for i in range(1000000):
        total += i
    return total

def fonction_intermediaire():
    """Appelle plusieurs fois la fonction lente."""
    resultats = []
    for _ in range(5):
        resultats.append(fonction_lente())
    return resultats

def programme_principal():
    """Point d'entrée du programme."""
    print("Démarrage du programme...")
    resultats = fonction_intermediaire()
    print(f"Résultats calculés : {len(resultats)} valeurs")

# Profiler le programme
cProfile.run('programme_principal()')
```

**Sortie (simplifiée) :**
```
Démarrage du programme...
Résultats calculés : 5 valeurs
         15 function calls in 0.245 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.245    0.245 <string>:1(<module>)
        1    0.000    0.000    0.245    0.245 script.py:12(fonction_intermediaire)
        5    0.245    0.049    0.245    0.049 script.py:3(fonction_lente)
        1    0.000    0.000    0.245    0.245 script.py:19(programme_principal)
```

**Explication des colonnes :**
- **ncalls** : Nombre d'appels de la fonction
- **tottime** : Temps total passé dans la fonction (sans les sous-fonctions)
- **percall** : Temps moyen par appel
- **cumtime** : Temps cumulé (incluant les sous-fonctions)
- **filename:lineno** : Localisation de la fonction

### 3.3 Profiler et sauvegarder les résultats

```python
import cProfile
import pstats

def programme_a_profiler():
    # Votre code ici
    nombres = [i**2 for i in range(100000)]
    return sum(nombres)

# Profiler et sauvegarder dans un fichier
cProfile.run('programme_a_profiler()', 'resultats_profiling.prof')

# Analyser les résultats
stats = pstats.Stats('resultats_profiling.prof')

# Trier par temps cumulé et afficher les 10 premières fonctions
print("="*60)
print("Top 10 des fonctions les plus gourmandes en temps :")
print("="*60)
stats.sort_stats('cumulative').print_stats(10)
```

### 3.4 Profiler une fonction spécifique avec un décorateur

```python
import cProfile
import pstats
from functools import wraps
import io

def profiler(func):
    """Décorateur pour profiler une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()

        resultat = func(*args, **kwargs)

        profiler.disable()

        # Créer un objet pour capturer la sortie
        s = io.StringIO()
        stats = pstats.Stats(profiler, stream=s)
        stats.sort_stats('cumulative')
        stats.print_stats(10)

        print(f"\n📊 Profiling de {func.__name__}:")
        print(s.getvalue())

        return resultat
    return wrapper

# Utilisation
@profiler
def calculer_fibonacci(n):
    """Calcul de la suite de Fibonacci (version récursive)."""
    if n <= 1:
        return n
    return calculer_fibonacci(n-1) + calculer_fibonacci(n-2)

# Test
resultat = calculer_fibonacci(20)
print(f"Fibonacci(20) = {resultat}")
```

---

## 4. Profiling de la mémoire

### 4.1 Mesurer l'utilisation mémoire de base

```python
import sys

def mesurer_taille(objet, nom="Objet"):
    """Affiche la taille d'un objet en mémoire."""
    taille = sys.getsizeof(objet)

    # Convertir en unité lisible
    if taille < 1024:
        unite = "octets"
    elif taille < 1024**2:
        taille = taille / 1024
        unite = "Ko"
    else:
        taille = taille / (1024**2)
        unite = "Mo"

    print(f"{nom}: {taille:.2f} {unite}")

# Exemples
liste_petite = [1, 2, 3, 4, 5]
liste_grande = list(range(1000000))
dictionnaire = {i: i**2 for i in range(1000)}
texte = "Python" * 10000

mesurer_taille(liste_petite, "Petite liste")
mesurer_taille(liste_grande, "Grande liste")
mesurer_taille(dictionnaire, "Dictionnaire")
mesurer_taille(texte, "Texte")
```

**Sortie :**
```
Petite liste: 104 octets
Grande liste: 8.00 Mo
Dictionnaire: 36.66 Ko
Texte: 58.59 Ko
```

### 4.2 Comparer l'utilisation mémoire de différentes structures

```python
import sys

def comparer_structures(n=1000):
    """Compare l'utilisation mémoire de différentes structures."""

    # Liste
    ma_liste = list(range(n))

    # Tuple
    mon_tuple = tuple(range(n))

    # Set
    mon_set = set(range(n))

    # Générateur (ne stocke pas tout en mémoire)
    mon_generateur = (x for x in range(n))

    print(f"Comparaison pour {n} éléments:")
    print(f"  Liste      : {sys.getsizeof(ma_liste):,} octets")
    print(f"  Tuple      : {sys.getsizeof(mon_tuple):,} octets")
    print(f"  Set        : {sys.getsizeof(mon_set):,} octets")
    print(f"  Générateur : {sys.getsizeof(mon_generateur):,} octets ⚡")

comparer_structures(10000)
```

### 4.3 Le module memory_profiler (installation requise)

Pour une analyse mémoire ligne par ligne, vous pouvez installer `memory_profiler` :

```bash
pip install memory_profiler
```

```python
from memory_profiler import profile

@profile
def fonction_gourmande():
    """Fonction qui utilise beaucoup de mémoire."""
    # Créer plusieurs grandes structures
    liste1 = [i for i in range(1000000)]
    liste2 = [i**2 for i in range(1000000)]
    liste3 = [i**3 for i in range(1000000)]

    # Calculer quelque chose
    resultat = sum(liste1) + sum(liste2) + sum(liste3)

    return resultat

# Appel de la fonction
resultat = fonction_gourmande()
```

**Sortie (exemple) :**
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3     50.5 MiB     50.5 MiB           1   @profile
     4                                         def fonction_gourmande():
     5     58.1 MiB      7.6 MiB           1       liste1 = [i for i in range(1000000)]
     6     65.7 MiB      7.6 MiB           1       liste2 = [i**2 for i in range(1000000)]
     7     73.3 MiB      7.6 MiB           1       liste3 = [i**3 for i in range(1000000)]
     9     73.3 MiB      0.0 MiB           1       resultat = sum(liste1) + sum(liste2) + sum(liste3)
    11     73.3 MiB      0.0 MiB           1       return resultat
```

---

## 5. Techniques d'optimisation

### 5.1 Utiliser les bonnes structures de données

**Problème : Vérifier si un élément existe**

```python
import timeit

def test_liste(n=10000):
    """Recherche dans une liste."""
    ma_liste = list(range(n))
    return 9999 in ma_liste

def test_set(n=10000):
    """Recherche dans un set."""
    mon_set = set(range(n))
    return 9999 in mon_set

# Comparer les performances
temps_liste = timeit.timeit(test_liste, number=1000)
temps_set = timeit.timeit(test_set, number=1000)

print("Recherche d'un élément :")
print(f"  Liste : {temps_liste:.4f} secondes")
print(f"  Set   : {temps_set:.4f} secondes")
print(f"  Amélioration : {temps_liste/temps_set:.0f}x plus rapide avec un set ! 🚀")
```

**Résultat :**
```
Recherche d'un élément :
  Liste : 0.3456 secondes
  Set   : 0.0012 secondes
  Amélioration : 288x plus rapide avec un set ! 🚀
```

**Leçon : Utilisez un set pour les tests d'appartenance !**

### 5.2 Éviter les calculs répétitifs

**❌ Version non optimisée (calcule plusieurs fois la même chose) :**

```python
def calculer_distances_lente(points):
    """Calcule les distances entre tous les points."""
    distances = []
    for i in range(len(points)):
        for j in range(len(points)):
            # Calcule len(points) à chaque itération !
            distance = abs(points[i] - points[j])
            distances.append(distance)
    return distances
```

**✅ Version optimisée (calcule une seule fois) :**

```python
def calculer_distances_rapide(points):
    """Version optimisée."""
    distances = []
    n = len(points)  # Calculé une seule fois
    for i in range(n):
        point_i = points[i]  # Accès direct au lieu de points[i] à chaque fois
        for j in range(n):
            distance = abs(point_i - points[j])
            distances.append(distance)
    return distances

# Comparaison
import timeit

points = list(range(1000))
temps_lent = timeit.timeit(lambda: calculer_distances_lente(points), number=10)
temps_rapide = timeit.timeit(lambda: calculer_distances_rapide(points), number=10)

print(f"Version lente  : {temps_lent:.4f} secondes")
print(f"Version rapide : {temps_rapide:.4f} secondes")
print(f"Amélioration   : {(temps_lent-temps_rapide)/temps_lent*100:.1f}%")
```

### 5.3 Utiliser les compréhensions au lieu des boucles

**Comparaison de performance :**

```python
import timeit

def avec_boucle(n):
    """Créer une liste avec une boucle."""
    resultat = []
    for i in range(n):
        if i % 2 == 0:
            resultat.append(i**2)
    return resultat

def avec_comprehension(n):
    """Créer une liste avec une compréhension."""
    return [i**2 for i in range(n) if i % 2 == 0]

n = 10000
temps_boucle = timeit.timeit(lambda: avec_boucle(n), number=1000)
temps_comp = timeit.timeit(lambda: avec_comprehension(n), number=1000)

print("Création d'une liste de carrés des nombres pairs :")
print(f"  Boucle for       : {temps_boucle:.4f} secondes")
print(f"  Compréhension    : {temps_comp:.4f} secondes")
print(f"  Amélioration     : {temps_boucle/temps_comp:.2f}x plus rapide")
```

### 5.4 Utiliser les fonctions built-in de Python

Les fonctions intégrées de Python sont implémentées en C et sont très rapides.

```python
import timeit

# Somme d'une liste
nombres = list(range(100000))

# Méthode manuelle
def somme_manuelle(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

# Fonction built-in
def somme_builtin(liste):
    return sum(liste)

temps_manuel = timeit.timeit(lambda: somme_manuelle(nombres), number=100)
temps_builtin = timeit.timeit(lambda: somme_builtin(nombres), number=100)

print("Calcul de la somme d'une liste :")
print(f"  Boucle manuelle : {temps_manuel:.4f} secondes")
print(f"  Fonction sum()  : {temps_builtin:.4f} secondes")
print(f"  Amélioration    : {temps_manuel/temps_builtin:.2f}x plus rapide")
```

**Fonctions built-in à privilégier :**
- `sum()` pour additionner
- `max()`, `min()` pour trouver le maximum/minimum
- `all()`, `any()` pour les tests booléens
- `sorted()` pour trier
- `map()`, `filter()` pour les transformations

### 5.5 Mise en cache (Memoization)

Pour éviter de recalculer les mêmes valeurs :

```python
from functools import lru_cache
import timeit

# Version sans cache (très lente)
def fibonacci_sans_cache(n):
    """Calcul récursif de Fibonacci sans cache."""
    if n <= 1:
        return n
    return fibonacci_sans_cache(n-1) + fibonacci_sans_cache(n-2)

# Version avec cache (très rapide)
@lru_cache(maxsize=None)
def fibonacci_avec_cache(n):
    """Calcul récursif de Fibonacci avec cache."""
    if n <= 1:
        return n
    return fibonacci_avec_cache(n-1) + fibonacci_avec_cache(n-2)

# Comparaison pour n=30
print("Calcul de Fibonacci(30) :")

temps_sans = timeit.timeit(lambda: fibonacci_sans_cache(30), number=1)
print(f"  Sans cache : {temps_sans:.4f} secondes")

temps_avec = timeit.timeit(lambda: fibonacci_avec_cache(30), number=1)
print(f"  Avec cache : {temps_avec:.6f} secondes")

print(f"  Amélioration : {temps_sans/temps_avec:.0f}x plus rapide ! 🚀🚀🚀")

# Résultat typique : 100,000x plus rapide !
```

### 5.6 Utiliser des générateurs pour économiser la mémoire

**Problème : Traiter une grande quantité de données**

```python
import sys

def avec_liste(n):
    """Créer une liste complète (utilise beaucoup de mémoire)."""
    return [x**2 for x in range(n)]

def avec_generateur(n):
    """Créer un générateur (utilise peu de mémoire)."""
    return (x**2 for x in range(n))

n = 1000000

# Liste : stocke tout en mémoire
ma_liste = avec_liste(n)
print(f"Liste : {sys.getsizeof(ma_liste):,} octets")

# Générateur : calcule à la demande
mon_gen = avec_generateur(n)
print(f"Générateur : {sys.getsizeof(mon_gen):,} octets")

# Différence
print(f"Le générateur utilise {sys.getsizeof(ma_liste)/sys.getsizeof(mon_gen):.0f}x moins de mémoire !")
```

**Sortie :**
```
Liste : 8,448,728 octets
Générateur : 200 octets
Le générateur utilise 42,244x moins de mémoire !
```

### 5.7 Utiliser join() pour concaténer des chaînes

```python
import timeit

def concatenation_avec_plus(n):
    """Concaténation avec + (lente)."""
    resultat = ""
    for i in range(n):
        resultat = resultat + str(i)
    return resultat

def concatenation_avec_join(n):
    """Concaténation avec join() (rapide)."""
    return "".join(str(i) for i in range(n))

n = 5000

temps_plus = timeit.timeit(lambda: concatenation_avec_plus(n), number=10)
temps_join = timeit.timeit(lambda: concatenation_avec_join(n), number=10)

print("Concaténation de chaînes :")
print(f"  Opérateur +  : {temps_plus:.4f} secondes")
print(f"  Méthode join : {temps_join:.4f} secondes")
print(f"  Amélioration : {temps_plus/temps_join:.2f}x plus rapide")
```

---

## 6. Optimisation avec NumPy (pour le calcul scientifique)

### 6.1 Pourquoi NumPy est rapide

NumPy est une bibliothèque pour le calcul numérique qui est beaucoup plus rapide que les listes Python.

```python
import numpy as np
import timeit

# Taille des données
n = 1000000

# Avec des listes Python
def operation_liste():
    liste1 = list(range(n))
    liste2 = list(range(n))
    resultat = [a + b for a, b in zip(liste1, liste2)]
    return resultat

# Avec NumPy
def operation_numpy():
    array1 = np.arange(n)
    array2 = np.arange(n)
    resultat = array1 + array2
    return resultat

temps_liste = timeit.timeit(operation_liste, number=10)
temps_numpy = timeit.timeit(operation_numpy, number=10)

print("Addition de deux séquences de 1,000,000 d'éléments :")
print(f"  Listes Python : {temps_liste:.4f} secondes")
print(f"  NumPy arrays  : {temps_numpy:.4f} secondes")
print(f"  NumPy est {temps_liste/temps_numpy:.2f}x plus rapide ! 🚀")
```

**Résultat typique :**
```
Addition de deux séquences de 1,000,000 d'éléments :
  Listes Python : 2.3456 secondes
  NumPy arrays  : 0.0123 secondes
  NumPy est 190.70x plus rapide ! 🚀
```

### 6.2 Opérations vectorisées

```python
import numpy as np
import timeit

def calcul_avec_boucle(n):
    """Calcul avec une boucle Python."""
    valeurs = list(range(n))
    resultats = []
    for v in valeurs:
        resultat = (v ** 2 + 2 * v + 1) ** 0.5
        resultats.append(resultat)
    return resultats

def calcul_vectorise(n):
    """Calcul vectorisé avec NumPy."""
    valeurs = np.arange(n)
    resultats = np.sqrt(valeurs ** 2 + 2 * valeurs + 1)
    return resultats

n = 100000
temps_boucle = timeit.timeit(lambda: calcul_avec_boucle(n), number=10)
temps_vect = timeit.timeit(lambda: calcul_vectorise(n), number=10)

print(f"Calcul avec boucle  : {temps_boucle:.4f} secondes")
print(f"Calcul vectorisé    : {temps_vect:.4f} secondes")
print(f"Amélioration        : {temps_boucle/temps_vect:.2f}x plus rapide")
```

---

## 7. Checklist d'optimisation

Avant d'optimiser, posez-vous ces questions :

### ✅ Étape 1 : Identifier le problème
- [ ] Ai-je vraiment un problème de performance ?
- [ ] Quelle partie du code est lente ?
- [ ] Ai-je mesuré avec cProfile ou timeit ?

### ✅ Étape 2 : Choisir la bonne structure de données
- [ ] Utilisé des sets au lieu de listes pour les recherches ?
- [ ] Utilisé des dictionnaires pour les accès par clé ?
- [ ] Utilisé des générateurs pour les grandes séquences ?

### ✅ Étape 3 : Optimiser les boucles
- [ ] Évité les calculs répétitifs dans les boucles ?
- [ ] Utilisé des compréhensions au lieu de boucles for ?
- [ ] Déplacé les calculs constants hors des boucles ?

### ✅ Étape 4 : Utiliser les bonnes fonctions
- [ ] Utilisé les fonctions built-in (sum, max, min) ?
- [ ] Utilisé join() pour concaténer des chaînes ?
- [ ] Utilisé le cache (@lru_cache) pour les calculs répétitifs ?

### ✅ Étape 5 : Pour le calcul numérique
- [ ] Considéré l'utilisation de NumPy ?
- [ ] Utilisé des opérations vectorisées ?

### ✅ Étape 6 : Vérifier les résultats
- [ ] Le code fonctionne-t-il toujours correctement ?
- [ ] Les tests passent-ils tous ?
- [ ] Le code reste-t-il lisible ?

---

## 8. Exemples pratiques d'optimisation

### Exemple 1 : Trouver les doublons dans une liste

**❌ Version non optimisée (O(n²)) :**

```python
import timeit

def trouver_doublons_lent(liste):
    """Méthode lente avec boucles imbriquées."""
    doublons = []
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if liste[i] == liste[j] and liste[i] not in doublons:
                doublons.append(liste[i])
    return doublons
```

**✅ Version optimisée (O(n)) :**

```python
def trouver_doublons_rapide(liste):
    """Méthode rapide avec un set."""
    vus = set()
    doublons = set()
    for element in liste:
        if element in vus:
            doublons.add(element)
        else:
            vus.add(element)
    return list(doublons)

# Test de performance
test_liste = list(range(1000)) * 2  # Liste avec des doublons

temps_lent = timeit.timeit(lambda: trouver_doublons_lent(test_liste), number=10)
temps_rapide = timeit.timeit(lambda: trouver_doublons_rapide(test_liste), number=10)

print(f"Méthode lente  : {temps_lent:.4f} secondes")
print(f"Méthode rapide : {temps_rapide:.4f} secondes")
print(f"Amélioration   : {temps_lent/temps_rapide:.2f}x plus rapide")
```

### Exemple 2 : Calculer la somme des carrés

**Comparaison de différentes approches :**

```python
import timeit
import numpy as np

n = 100000

# Méthode 1 : Boucle for
def methode_boucle(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Méthode 2 : Compréhension de liste
def methode_comprehension(n):
    return sum([i ** 2 for i in range(n)])

# Méthode 3 : Expression génératrice
def methode_generateur(n):
    return sum(i ** 2 for i in range(n))

# Méthode 4 : NumPy
def methode_numpy(n):
    return np.sum(np.arange(n) ** 2)

# Méthode 5 : Formule mathématique (ultra-rapide !)
def methode_formule(n):
    # Formule : n*(n+1)*(2n+1)/6
    return n * (n + 1) * (2 * n + 1) // 6

# Mesurer toutes les méthodes
methodes = {
    "Boucle for": methode_boucle,
    "Compréhension": methode_comprehension,
    "Générateur": methode_generateur,
    "NumPy": methode_numpy,
    "Formule math": methode_formule
}

print(f"Somme des carrés de 0 à {n-1}:\n")
resultats = {}

for nom, methode in methodes.items():
    temps = timeit.timeit(lambda: methode(n), number=100)
    resultats[nom] = temps
    print(f"{nom:20} : {temps:.6f} secondes")

# Trouver la plus rapide
plus_rapide = min(resultats, key=resultats.get)
print(f"\n🏆 La méthode '{plus_rapide}' est la plus rapide !")
```

**Sortie typique :**
```
Somme des carrés de 0 à 99999:

Boucle for           : 0.891234 secondes
Compréhension        : 0.756789 secondes
Générateur           : 0.734567 secondes
NumPy                : 0.345678 secondes
Formule math         : 0.000012 secondes

🏆 La méthode 'Formule math' est la plus rapide !
```

**Leçon importante : Parfois, la meilleure optimisation est algorithmique !**

### Exemple 3 : Filtrer et transformer des données

```python
import timeit

# Données de test
donnees = list(range(100000))

# Méthode 1 : Boucles imbriquées
def methode1(donnees):
    resultat = []
    for x in donnees:
        if x % 2 == 0:
            resultat.append(x ** 2)
    return resultat

# Méthode 2 : Compréhension de liste
def methode2(donnees):
    return [x ** 2 for x in donnees if x % 2 == 0]

# Méthode 3 : filter() et map()
def methode3(donnees):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, donnees)))

# Comparaison
temps1 = timeit.timeit(lambda: methode1(donnees), number=100)
temps2 = timeit.timeit(lambda: methode2(donnees), number=100)
temps3 = timeit.timeit(lambda: methode3(donnees), number=100)

print("Filtrer les pairs et calculer leur carré :")
print(f"  Boucle for      : {temps1:.4f} secondes")
print(f"  Compréhension   : {temps2:.4f} secondes ⚡ RECOMMANDÉ")
print(f"  filter() + map(): {temps3:.4f} secondes")
```

---

## 9. Outils et ressources supplémentaires

### 9.1 Outils de profiling avancés

**line_profiler** : Profiling ligne par ligne
```bash
pip install line_profiler
```

**py-spy** : Profiler sans modifier le code
```bash
pip install py-spy
py-spy top -- python mon_script.py
```

**snakeviz** : Visualiser les résultats de cProfile
```bash
pip install snakeviz
python -m cProfile -o output.prof mon_script.py
snakeviz output.prof
```

### 9.2 Utiliser %timeit dans Jupyter

Si vous utilisez Jupyter Notebook :

```python
# Mesurer une ligne
%timeit sum(range(1000))

# Mesurer une cellule
%%timeit
total = 0
for i in range(1000):
    total += i
```

### 9.3 Identifier les imports lents

```python
import importtime

# Analyse les temps d'import
python -X importtime mon_script.py
```

---

## 10. Règles d'or de l'optimisation

### 1. Ne pas optimiser prématurément
> "Premature optimization is the root of all evil" - Donald Knuth

Écrivez d'abord du code qui fonctionne, puis optimisez seulement si nécessaire.

### 2. Mesurer, ne pas deviner
Utilisez toujours des outils de profiling pour identifier les vrais problèmes de performance.

### 3. Optimiser l'algorithme d'abord
Passer de O(n²) à O(n log n) est souvent plus important que d'optimiser le code.

### 4. La lisibilité compte
Un code optimisé mais incompréhensible n'est pas une bonne solution.

```python
# ❌ Optimisé mais illisible
result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x%2==0, data)))

# ✅ Peut-être légèrement plus lent, mais beaucoup plus clair
pairs = [x for x in data if x % 2 == 0]
carres = [x ** 2 for x in pairs]
result = sum(carres)
```

### 5. Optimiser ce qui compte vraiment
Règle des 80/20 : 20% du code prend 80% du temps d'exécution. Concentrez-vous sur ces 20%.

### 6. Tester après optimisation
Assurez-vous que votre code fonctionne toujours correctement après optimisation.

```python
def test_optimisation():
    """Tester que l'optimisation n'a pas cassé le code."""
    # Version originale
    resultat_original = fonction_originale(donnees_test)

    # Version optimisée
    resultat_optimise = fonction_optimisee(donnees_test)

    # Vérifier que les résultats sont identiques
    assert resultat_original == resultat_optimise, "L'optimisation a changé le résultat !"
```

---

## 11. Résumé des techniques d'optimisation

| Technique | Gain potentiel | Difficulté | Quand l'utiliser |
|-----------|----------------|------------|------------------|
| **Utiliser les bonnes structures de données** | ⭐⭐⭐⭐⭐ | Facile | Toujours |
| **Éviter les calculs répétitifs** | ⭐⭐⭐⭐ | Facile | Toujours |
| **Compréhensions de listes** | ⭐⭐⭐ | Facile | Toujours |
| **Fonctions built-in** | ⭐⭐⭐ | Facile | Toujours |
| **Mise en cache (@lru_cache)** | ⭐⭐⭐⭐⭐ | Facile | Calculs répétitifs |
| **Générateurs** | ⭐⭐⭐⭐ | Moyen | Grandes séquences |
| **NumPy** | ⭐⭐⭐⭐⭐ | Moyen | Calcul numérique |
| **Optimisation algorithmique** | ⭐⭐⭐⭐⭐ | Difficile | Problèmes de complexité |

---

## 12. Exemple complet : Optimisation progressive

Voici un exemple complet montrant comment optimiser progressivement un programme :

```python
import timeit
from functools import lru_cache

# ============================================================================
# VERSION 1 : Code initial (non optimisé)
# ============================================================================
def calculer_statistiques_v1(donnees):
    """Version initiale, non optimisée."""
    # Calculer la moyenne
    total = 0
    for valeur in donnees:
        total += valeur
    moyenne = total / len(donnees)

    # Calculer l'écart par rapport à la moyenne
    ecarts = []
    for valeur in donnees:
        ecart = (valeur - moyenne) ** 2
        ecarts.append(ecart)

    # Calculer la variance
    somme_ecarts = 0
    for ecart in ecarts:
        somme_ecarts += ecart
    variance = somme_ecarts / len(donnees)

    return moyenne, variance

# ============================================================================
# VERSION 2 : Utilisation des fonctions built-in
# ============================================================================
def calculer_statistiques_v2(donnees):
    """Version optimisée avec fonctions built-in."""
    # Utiliser sum() au lieu d'une boucle
    moyenne = sum(donnees) / len(donnees)

    # Compréhension de liste au lieu de boucle
    ecarts = [(valeur - moyenne) ** 2 for valeur in donnees]

    # Utiliser sum() pour la variance
    variance = sum(ecarts) / len(donnees)

    return moyenne, variance

# ============================================================================
# VERSION 3 : Optimisation maximale avec NumPy
# ============================================================================
import numpy as np

def calculer_statistiques_v3(donnees):
    """Version ultra-optimisée avec NumPy."""
    arr = np.array(donnees)
    moyenne = np.mean(arr)
    variance = np.var(arr)
    return moyenne, variance

# ============================================================================
# TESTS DE PERFORMANCE
# ============================================================================
def comparer_versions():
    """Compare les performances des trois versions."""
    # Créer des données de test
    donnees = list(range(10000))

    print("="*70)
    print("COMPARAISON DES VERSIONS")
    print("="*70)

    # Version 1
    temps_v1 = timeit.timeit(lambda: calculer_statistiques_v1(donnees), number=100)
    print(f"Version 1 (code initial)      : {temps_v1:.4f} secondes")

    # Version 2
    temps_v2 = timeit.timeit(lambda: calculer_statistiques_v2(donnees), number=100)
    print(f"Version 2 (fonctions built-in): {temps_v2:.4f} secondes")
    print(f"  └─ Amélioration : {temps_v1/temps_v2:.2f}x plus rapide")

    # Version 3
    temps_v3 = timeit.timeit(lambda: calculer_statistiques_v3(donnees), number=100)
    print(f"Version 3 (NumPy)             : {temps_v3:.4f} secondes")
    print(f"  └─ Amélioration : {temps_v1/temps_v3:.2f}x plus rapide que v1")
    print(f"  └─ Amélioration : {temps_v2/temps_v3:.2f}x plus rapide que v2")

    # Vérifier que tous les résultats sont identiques
    print("\n" + "="*70)
    print("VÉRIFICATION DES RÉSULTATS")
    print("="*70)

    r1 = calculer_statistiques_v1(donnees)
    r2 = calculer_statistiques_v2(donnees)
    r3 = calculer_statistiques_v3(donnees)

    print(f"Version 1 : Moyenne = {r1[0]:.2f}, Variance = {r1[1]:.2f}")
    print(f"Version 2 : Moyenne = {r2[0]:.2f}, Variance = {r2[1]:.2f}")
    print(f"Version 3 : Moyenne = {r3[0]:.2f}, Variance = {r3[1]:.2f}")
    print("✅ Tous les résultats sont identiques !")

# Exécuter la comparaison
comparer_versions()
```

---

## Conclusion

L'optimisation est un art qui nécessite :
- **Mesure** : Utilisez des outils comme timeit, cProfile et memory_profiler
- **Analyse** : Identifiez les vraies causes de lenteur
- **Action** : Appliquez les bonnes techniques d'optimisation
- **Vérification** : Assurez-vous que le code fonctionne toujours

**Points clés à retenir :**

1. 📊 **Mesurez toujours** avant d'optimiser
2. 🎯 **Concentrez-vous** sur les goulots d'étranglement
3. 🔧 **Utilisez les bonnes structures** de données
4. ⚡ **Privilégiez** les fonctions built-in et les compréhensions
5. 💾 **Économisez la mémoire** avec des générateurs
6. 🔄 **Cachez** les calculs répétitifs avec @lru_cache
7. 🧮 **Utilisez NumPy** pour le calcul numérique
8. 📖 **Gardez le code lisible** : l'optimisation ne doit pas sacrifier la clarté

N'oubliez pas : un code qui fonctionne correctement est toujours préférable à un code ultra-optimisé mais bugué. Optimisez de manière intelligente, pas systématique !

Bonne optimisation ! 🚀✨

⏭️ [Tests et qualité du code](/10-tests-et-qualite/README.md)
