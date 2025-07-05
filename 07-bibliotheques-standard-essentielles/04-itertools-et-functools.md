🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.4 : itertools et functools

## Introduction

Les modules `itertools` et `functools` sont des outils puissants pour la programmation fonctionnelle en Python. Ils permettent d'écrire du code plus élégant, efficace et expressif en manipulant des itérateurs et des fonctions.

### Analogie simple
Imaginez une **chaîne de production** :
- **itertools** : les **convoyeurs et machines** qui transforment, combinent et organisent les éléments
- **functools** : les **outils de configuration** qui modifient et optimisent le comportement des machines

## Module itertools : Itérateurs avancés

Le module `itertools` fournit des fonctions pour créer des itérateurs efficaces et élégants.

### Itérateurs infinis

```python
import itertools

# count() - Compteur infini
print("Compteur infini (5 premiers) :")
compteur = itertools.count(start=10, step=2)
for i, valeur in enumerate(compteur):
    if i >= 5:
        break
    print(f"  {valeur}")

# cycle() - Répétition cyclique
print("\nCycle de couleurs (10 premiers) :")
couleurs = ['rouge', 'vert', 'bleu']
cycle_couleurs = itertools.cycle(couleurs)
for i, couleur in enumerate(cycle_couleurs):
    if i >= 10:
        break
    print(f"  Position {i}: {couleur}")

# repeat() - Répétition d'une valeur
print("\nRépétition (5 fois) :")
repetition = itertools.repeat('Python', 5)
for valeur in repetition:
    print(f"  {valeur}")
```

### Itérateurs de terminaison

```python
import itertools

# Données d'exemple
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lettres = ['a', 'b', 'c', 'd', 'e']

# takewhile() - Prendre tant que la condition est vraie
print("takewhile (< 6) :")
resultats = list(itertools.takewhile(lambda x: x < 6, nombres))
print(f"  {resultats}")

# dropwhile() - Ignorer tant que la condition est vraie
print("\ndropwhile (< 6) :")
resultats = list(itertools.dropwhile(lambda x: x < 6, nombres))
print(f"  {resultats}")

# filterfalse() - Inverse de filter()
print("\nfilterfalse (pairs) :")
resultats = list(itertools.filterfalse(lambda x: x % 2 == 0, nombres))
print(f"  {resultats}")

# islice() - Découpage comme une slice
print("\nislice [2:7:2] :")
resultats = list(itertools.islice(nombres, 2, 7, 2))
print(f"  {resultats}")
```

### Combinaisons et permutations

```python
import itertools

# Données d'exemple
elements = ['A', 'B', 'C']
nombres = [1, 2, 3, 4]

print("🔄 COMBINAISONS ET PERMUTATIONS")
print("-" * 35)

# Produit cartésien
print("Produit cartésien (A,B,C) × (1,2) :")
produit = list(itertools.product(elements[:3], [1, 2]))
for item in produit:
    print(f"  {item}")

# Permutations
print(f"\nPermutations de {elements} (longueur 2) :")
perms = list(itertools.permutations(elements, 2))
for perm in perms:
    print(f"  {perm}")

# Combinaisons (sans répétition)
print(f"\nCombinaisons de {nombres[:4]} (longueur 2) :")
combs = list(itertools.combinations(nombres[:4], 2))
for comb in combs:
    print(f"  {comb}")

# Combinaisons avec répétition
print(f"\nCombinaisons avec répétition de {elements[:2]} (longueur 3) :")
combs_rep = list(itertools.combinations_with_replacement(elements[:2], 3))
for comb in combs_rep:
    print(f"  {comb}")
```

### Regroupement et chaînage

```python
import itertools

# groupby() - Regrouper par clé
print("📊 REGROUPEMENT")
print("-" * 20)

# Grouper des nombres par parité
nombres = [1, 3, 5, 2, 4, 6, 7, 9, 8]
groupes = itertools.groupby(sorted(nombres), key=lambda x: x % 2)

for clé, groupe in groupes:
    type_nombre = "impairs" if clé else "pairs"
    elements = list(groupe)
    print(f"{type_nombre}: {elements}")

# chain() - Chaîner plusieurs itérables
print(f"\n🔗 CHAÎNAGE")
print("-" * 15)

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
liste3 = [10, 20]

chaine = list(itertools.chain(liste1, liste2, liste3))
print(f"Chaînage: {chaine}")

# chain.from_iterable() - Chaîner depuis un itérable de listes
listes = [[1, 2], [3, 4], [5, 6]]
chaine_aplatie = list(itertools.chain.from_iterable(listes))
print(f"Aplatissement: {chaine_aplatie}")
```

### Exemple pratique : Générateur de combinaisons de mots de passe

```python
import itertools
import string

def generer_mots_de_passe(longueur=4, alphabet=None):
    """Génère tous les mots de passe possibles d'une longueur donnée."""
    if alphabet is None:
        alphabet = string.ascii_lowercase

    print(f"Génération de mots de passe de {longueur} caractères")
    print(f"Alphabet: {alphabet}")

    # Calcul du nombre total de combinaisons
    total = len(alphabet) ** longueur
    print(f"Total possible: {total:,} combinaisons")

    # Générer et afficher les 10 premiers
    mots_de_passe = itertools.product(alphabet, repeat=longueur)

    print("\n10 premiers mots de passe:")
    for i, mot_de_passe in enumerate(mots_de_passe):
        if i >= 10:
            break
        print(f"  {''.join(mot_de_passe)}")

# Test avec un petit alphabet
generer_mots_de_passe(3, 'abc')
```

## Module functools : Outils fonctionnels

Le module `functools` fournit des utilitaires pour travailler avec des fonctions d'ordre supérieur.

### Décorateurs utiles

```python
import functools
import time

# lru_cache - Cache LRU (Least Recently Used)
@functools.lru_cache(maxsize=128)
def fibonacci_cache(n):
    """Fibonacci avec cache pour éviter les recalculs."""
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

def fibonacci_simple(n):
    """Fibonacci sans cache (lent pour grands n)."""
    if n < 2:
        return n
    return fibonacci_simple(n-1) + fibonacci_simple(n-2)

# Comparaison de performance
def comparer_fibonacci(n=30):
    print(f"🚀 COMPARAISON FIBONACCI({n})")
    print("-" * 30)

    # Avec cache
    start = time.time()
    result_cache = fibonacci_cache(n)
    time_cache = time.time() - start

    # Sans cache (attention: très lent pour n > 35)
    start = time.time()
    result_simple = fibonacci_simple(n) if n <= 30 else "Trop lent"
    time_simple = time.time() - start if n <= 30 else float('inf')

    print(f"Avec cache: {result_cache} en {time_cache:.4f}s")
    print(f"Sans cache: {result_simple} en {time_simple:.4f}s")

    if n <= 30:
        print(f"Accélération: {time_simple/time_cache:.1f}x")

    # Informations sur le cache
    print(f"Cache info: {fibonacci_cache.cache_info()}")

comparer_fibonacci(35)
```

### Fonctions de réduction

```python
import functools
import operator

# reduce() - Réduction d'une séquence
print("📉 FONCTIONS DE RÉDUCTION")
print("-" * 30)

nombres = [1, 2, 3, 4, 5]

# Somme avec reduce
somme = functools.reduce(operator.add, nombres)
print(f"Somme de {nombres}: {somme}")

# Produit avec reduce
produit = functools.reduce(operator.mul, nombres)
print(f"Produit de {nombres}: {produit}")

# Maximum avec reduce
maximum = functools.reduce(max, nombres)
print(f"Maximum de {nombres}: {maximum}")

# Concaténation de chaînes
mots = ['Python', 'est', 'génial']
phrase = functools.reduce(lambda a, b: a + ' ' + b, mots)
print(f"Concaténation: '{phrase}'")

# Exemple plus complexe: PGCD de plusieurs nombres
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

nombres_pgcd = [48, 18, 24, 36]
pgcd_multiple = functools.reduce(pgcd, nombres_pgcd)
print(f"PGCD de {nombres_pgcd}: {pgcd_multiple}")
```

### Fonctions partielles

```python
import functools

# partial() - Application partielle de fonction
print("🔧 FONCTIONS PARTIELLES")
print("-" * 25)

def puissance(base, exposant):
    """Calcule base^exposant."""
    return base ** exposant

# Créer des fonctions spécialisées
carre = functools.partial(puissance, exposant=2)
cube = functools.partial(puissance, exposant=3)
puissance_de_2 = functools.partial(puissance, base=2)

print(f"Carré de 5: {carre(5)}")
print(f"Cube de 3: {cube(3)}")
print(f"2^10: {puissance_de_2(10)}")

# Exemple pratique: configuration de logging
import logging

def log_message(level, message, logger_name="app"):
    """Fonction de logging générique."""
    logger = logging.getLogger(logger_name)
    getattr(logger, level)(message)

# Créer des fonctions de logging spécialisées
log_error = functools.partial(log_message, "error")
log_info = functools.partial(log_message, "info")
log_debug = functools.partial(log_message, "debug")

# Configuration du logging pour la démo
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

log_info("Application démarrée")
log_error("Erreur simulée")
```

### Décorateurs personnalisés avec functools

```python
import functools
import time

def mesurer_temps(func):
    """Décorateur pour mesurer le temps d'exécution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} exécutée en {end-start:.4f}s")
        return result
    return wrapper

def retry(max_attempts=3, delay=1):
    """Décorateur pour relancer une fonction en cas d'échec."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Tentative {attempt + 1} échouée: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

# Test des décorateurs
@mesurer_temps
@retry(max_attempts=2)
def fonction_test(x):
    """Fonction de test qui peut échouer."""
    if x < 0.5:
        raise ValueError("Valeur trop petite")
    time.sleep(0.1)  # Simulation de travail
    return x * 2

# Tests
print("🧪 TEST DES DÉCORATEURS")
print("-" * 25)

try:
    result = fonction_test(0.8)
    print(f"Résultat: {result}")
except Exception as e:
    print(f"Échec final: {e}")
```

## Exemples pratiques combinés

### Exercice 1 : Générateur de séquences

```python
import itertools
import functools

def generer_sequences_numeriques():
    """Génère différentes séquences numériques intéressantes."""

    print("🔢 SÉQUENCES NUMÉRIQUES")
    print("-" * 25)

    # Nombres pairs
    pairs = itertools.islice(itertools.count(0, 2), 10)
    print(f"10 premiers pairs: {list(pairs)}")

    # Carrés parfaits
    carres = itertools.islice(map(lambda x: x**2, itertools.count(1)), 8)
    print(f"8 premiers carrés: {list(carres)}")

    # Fibonacci avec itertools
    def fibonacci_itertools():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib = itertools.islice(fibonacci_itertools(), 12)
    print(f"12 premiers Fibonacci: {list(fib)}")

    # Nombres premiers (simple)
    def est_premier(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    premiers = itertools.islice(filter(est_premier, itertools.count(2)), 10)
    print(f"10 premiers premiers: {list(premiers)}")

generer_sequences_numeriques()
```

### Exercice 2 : Analyse de données avec groupby

```python
import itertools
import functools

def analyser_ventes():
    """Analyse des données de vente avec groupby."""

    # Données simulées (date, vendeur, montant)
    ventes = [
        ('2024-01', 'Alice', 1500),
        ('2024-01', 'Bob', 2000),
        ('2024-01', 'Alice', 1200),
        ('2024-02', 'Alice', 1800),
        ('2024-02', 'Bob', 2200),
        ('2024-02', 'Charlie', 1000),
        ('2024-03', 'Alice', 1600),
        ('2024-03', 'Bob', 1900),
    ]

    print("📊 ANALYSE DES VENTES")
    print("-" * 25)

    # Grouper par mois
    ventes_par_mois = itertools.groupby(ventes, key=lambda x: x[0])

    for mois, groupe_ventes in ventes_par_mois:
        liste_ventes = list(groupe_ventes)
        total_mois = sum(vente[2] for vente in liste_ventes)
        nb_ventes = len(liste_ventes)

        print(f"\n{mois}:")
        print(f"  Total: {total_mois}€")
        print(f"  Nombre de ventes: {nb_ventes}")
        print(f"  Moyenne: {total_mois/nb_ventes:.0f}€")

        # Vendeurs du mois
        vendeurs = {vente[1] for vente in liste_ventes}
        print(f"  Vendeurs actifs: {', '.join(vendeurs)}")

analyser_ventes()
```

### Exercice 3 : Optimiseur de cache

```python
import functools
import time
import random

class CacheOptimise:
    """Classe pour tester différentes stratégies de cache."""

    @staticmethod
    @functools.lru_cache(maxsize=100)
    def calcul_lourd_cache(n):
        """Simulation d'un calcul lourd avec cache."""
        time.sleep(0.01)  # Simulation
        return sum(i**2 for i in range(n))

    @staticmethod
    def calcul_lourd_sans_cache(n):
        """Même calcul sans cache."""
        time.sleep(0.01)  # Simulation
        return sum(i**2 for i in range(n))

    def tester_performance(self, nb_tests=50):
        """Compare les performances avec et sans cache."""

        # Générer des valeurs de test (certaines répétées)
        valeurs_test = [random.randint(1, 20) for _ in range(nb_tests)]

        print("🏎️ TEST DE PERFORMANCE DU CACHE")
        print("-" * 35)

        # Test avec cache
        start = time.time()
        for valeur in valeurs_test:
            self.calcul_lourd_cache(valeur)
        temps_cache = time.time() - start

        # Test sans cache
        start = time.time()
        for valeur in valeurs_test:
            self.calcul_lourd_sans_cache(valeur)
        temps_sans_cache = time.time() - start

        print(f"Avec cache: {temps_cache:.3f}s")
        print(f"Sans cache: {temps_sans_cache:.3f}s")
        print(f"Accélération: {temps_sans_cache/temps_cache:.1f}x")
        print(f"Cache info: {self.calcul_lourd_cache.cache_info()}")

# Test
optimiseur = CacheOptimise()
optimiseur.tester_performance()
```

## Bonnes pratiques

### **1. Utilisation efficace d'itertools**
```python
# ✅ Bon: itérateurs paresseux (lazy)
import itertools

# Évite de créer toute la liste en mémoire
grands_nombres = itertools.islice(itertools.count(1000000), 10)

# ❌ Éviter: créer des listes énormes
# mauvais = list(itertools.count(1000000))  # Infini!
```

### **2. Cache intelligent avec functools**
```python
# ✅ Bon: cache pour fonctions pures et coûteuses
@functools.lru_cache(maxsize=128)
def calcul_complexe(x, y):
    # Fonction pure, résultat dépend uniquement des paramètres
    return x**3 + y**2

# ❌ Éviter: cache sur fonctions avec effets de bord
# @functools.lru_cache()  # Mauvaise idée
# def fonction_avec_effet_de_bord():
#     print("Side effect!")  # Ne devrait pas être cachée
```

### **3. Combinaison efficace des modules**
```python
import itertools
import functools

# Exemple: traitement de données par batch
@functools.lru_cache(maxsize=32)
def traiter_batch(batch):
    # Conversion tuple pour la cache (les listes ne sont pas hashables)
    return sum(batch) / len(batch)

def traiter_donnees_par_batch(donnees, taille_batch=10):
    batches = [donnees[i:i+taille_batch]
               for i in range(0, len(donnees), taille_batch)]

    return [traiter_batch(tuple(batch)) for batch in batches]
```

## Cas d'usage courants

### **Data processing**
- Regroupement et agrégation de données
- Traitement par lots (batching)
- Génération de séquences

### **Optimisation de performance**
- Cache de résultats coûteux
- Mémorisation de calculs récurrents
- Réduction de la complexité

### **Programmation fonctionnelle**
- Composition de fonctions
- Applications partielles
- Transformations de données

### **Combinatoire et mathématiques**
- Génération de permutations/combinaisons
- Analyse statistique
- Algorithmes de recherche

## Résumé

Les modules `itertools` et `functools` sont essentiels pour :

1. **itertools** : Créer des itérateurs efficaces, combiner des séquences, générer des permutations
2. **functools** : Optimiser les fonctions avec le cache, créer des applications partielles, construire des décorateurs

Ces outils permettent d'écrire du code plus expressif, efficace et maintenable en adoptant un style de programmation fonctionnelle.

Dans la prochaine section, nous explorerons le module `logging` pour la journalisation professionnelle des applications.

⏭️
