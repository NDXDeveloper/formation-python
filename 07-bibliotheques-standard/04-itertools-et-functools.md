🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.4 Les modules itertools et functools

## Introduction

Python propose deux modules puissants qui permettent d'écrire du code plus élégant et efficace :

- **itertools** : Fournit des itérateurs pour créer des boucles efficaces et manipuler des séquences de manière élégante
- **functools** : Offre des outils pour la programmation fonctionnelle, notamment pour travailler avec des fonctions d'ordre supérieur

Ces modules sont particulièrement utiles pour écrire du code concis et performant. Bien qu'ils puissent sembler avancés, nous allons les découvrir progressivement avec des exemples pratiques.

---

## Le module `itertools` - Itérateurs puissants

Le module `itertools` fournit des fonctions qui créent des itérateurs pour des boucles efficaces. Un itérateur est un objet qui produit des valeurs une par une, ce qui est très efficace en mémoire.

### Import du module

```python
import itertools

# Ou importer des fonctions spécifiques
from itertools import count, cycle, repeat
```

---

## Itérateurs infinis

Ces itérateurs génèrent des valeurs indéfiniment. Attention à toujours définir une condition d'arrêt !

### count() - Compteur infini

```python
import itertools

# Compte à partir de 10, par pas de 1
compteur = itertools.count(10)

# Obtenir les 5 premières valeurs
for i in range(5):
    print(next(compteur))  # 10, 11, 12, 13, 14

# Avec un pas personnalisé
compteur_pas = itertools.count(0, 5)  # 0, 5, 10, 15...  
for i in range(4):  
    print(next(compteur_pas))  # 0, 5, 10, 15

# Avec des floats
compteur_float = itertools.count(0.5, 0.5)  
for i in range(3):  
    print(next(compteur_float))  # 0.5, 1.0, 1.5
```

### cycle() - Cycle infini sur une séquence

```python
import itertools

# Répète indéfiniment une séquence
couleurs = itertools.cycle(['rouge', 'vert', 'bleu'])

for i in range(7):
    print(next(couleurs))
# Affiche : rouge, vert, bleu, rouge, vert, bleu, rouge
```

### repeat() - Répéter une valeur

```python
import itertools

# Répète une valeur indéfiniment
repetition_infinie = itertools.repeat('bonjour')

# Répète un nombre de fois précis
repetition_limitee = itertools.repeat('salut', 3)

for mot in repetition_limitee:
    print(mot)  # salut, salut, salut
```

### Exemple pratique : Numérotation automatique

```python
import itertools

class GestionnaireID:
    """Génère des IDs uniques automatiquement"""

    def __init__(self, prefixe="ID", debut=1):
        self.prefixe = prefixe
        self.compteur = itertools.count(debut)

    def generer_id(self):
        """Génère un nouvel ID"""
        return f"{self.prefixe}_{next(self.compteur):04d}"

# Utilisation
gestionnaire = GestionnaireID("USER", 1)

for i in range(5):
    print(gestionnaire.generer_id())
# USER_0001, USER_0002, USER_0003, USER_0004, USER_0005
```

---

## Itérateurs qui se terminent

Ces itérateurs s'arrêtent automatiquement quand leurs données sont épuisées.

### chain() - Chaîner plusieurs itérables

```python
import itertools

# Concatène plusieurs séquences
liste1 = [1, 2, 3]  
liste2 = [4, 5, 6]  
liste3 = [7, 8, 9]  

chaine = itertools.chain(liste1, liste2, liste3)  
print(list(chaine))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]  

# Avec des types différents
resultat = itertools.chain([1, 2], "abc", (7, 8))  
print(list(resultat))  # [1, 2, 'a', 'b', 'c', 7, 8]  

# chain.from_iterable() : à partir d'un itérable d'itérables
listes = [[1, 2], [3, 4], [5, 6]]  
chaine = itertools.chain.from_iterable(listes)  
print(list(chaine))  # [1, 2, 3, 4, 5, 6]  
```

### compress() - Filtrer avec un sélecteur

```python
import itertools

# Garde les éléments où le sélecteur est True
donnees = ['A', 'B', 'C', 'D', 'E']  
selecteur = [1, 0, 1, 0, 1]  # 1 = True, 0 = False  

resultat = itertools.compress(donnees, selecteur)  
print(list(resultat))  # ['A', 'C', 'E']  

# Exemple pratique : filtrer par condition
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
est_pair = [n % 2 == 0 for n in nombres]  
pairs = itertools.compress(nombres, est_pair)  
print(list(pairs))  # [2, 4, 6, 8, 10]  
```

### dropwhile() et takewhile() - Filtrer selon une condition

```python
import itertools

# dropwhile() : Ignore les éléments tant que la condition est vraie
nombres = [1, 3, 5, 7, 10, 12, 14, 2, 4]  
resultat = itertools.dropwhile(lambda x: x < 10, nombres)  
print(list(resultat))  # [10, 12, 14, 2, 4] (commence dès qu'on trouve >= 10)  

# takewhile() : Prend les éléments tant que la condition est vraie
nombres = [1, 3, 5, 7, 10, 12, 14, 2, 4]  
resultat = itertools.takewhile(lambda x: x < 10, nombres)  
print(list(resultat))  # [1, 3, 5, 7] (s'arrête au premier >= 10)  
```

### filterfalse() - Inverse de filter()

```python
import itertools

# filterfalse() : Garde les éléments où la condition est False
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() garde les pairs
pairs = filter(lambda x: x % 2 == 0, nombres)  
print(list(pairs))  # [2, 4, 6, 8, 10]  

# filterfalse() garde les impairs (inverse)
impairs = itertools.filterfalse(lambda x: x % 2 == 0, nombres)  
print(list(impairs))  # [1, 3, 5, 7, 9]  
```

### islice() - Découper un itérable

```python
import itertools

# islice(iterable, stop)
nombres = range(10)  
resultat = itertools.islice(nombres, 5)  
print(list(resultat))  # [0, 1, 2, 3, 4]  

# islice(iterable, start, stop)
resultat = itertools.islice(nombres, 2, 7)  
print(list(resultat))  # [2, 3, 4, 5, 6]  

# islice(iterable, start, stop, step)
resultat = itertools.islice(nombres, 0, 10, 2)  
print(list(resultat))  # [0, 2, 4, 6, 8]  

# Utile pour limiter un itérateur infini
compteur = itertools.count(1)  
premiers = itertools.islice(compteur, 5)  
print(list(premiers))  # [1, 2, 3, 4, 5]  
```

### groupby() - Grouper des éléments consécutifs

```python
import itertools

# Groupe les éléments consécutifs identiques
donnees = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'A']

for cle, groupe in itertools.groupby(donnees):
    print(f"{cle}: {list(groupe)}")
# A: ['A', 'A', 'A']
# B: ['B', 'B']
# C: ['C', 'C', 'C']
# A: ['A']

# Avec une fonction de clé
personnes = [
    {'nom': 'Alice', 'age': 25},
    {'nom': 'Bob', 'age': 25},
    {'nom': 'Charlie', 'age': 30},
    {'nom': 'David', 'age': 30},
    {'nom': 'Emma', 'age': 25}
]

# IMPORTANT : Trier d'abord par la clé de regroupement
personnes_triees = sorted(personnes, key=lambda p: p['age'])

for age, groupe in itertools.groupby(personnes_triees, key=lambda p: p['age']):
    liste_personnes = list(groupe)
    print(f"Âge {age}: {[p['nom'] for p in liste_personnes]}")
# Âge 25: ['Alice', 'Bob', 'Emma']
# Âge 30: ['Charlie', 'David']
```

### Exemple pratique : Traitement de logs

```python
import itertools  
from datetime import datetime  

def analyser_logs(lignes_log):
    """Analyse des logs en groupant par niveau"""

    # Extraire le niveau de log de chaque ligne
    def get_niveau(ligne):
        if 'ERROR' in ligne:
            return 'ERROR'
        elif 'WARNING' in ligne:
            return 'WARNING'
        else:
            return 'INFO'

    # Trier par niveau
    lignes_triees = sorted(lignes_log, key=get_niveau)

    # Grouper par niveau
    print("📋 Analyse des logs :")
    print("=" * 50)

    for niveau, groupe in itertools.groupby(lignes_triees, key=get_niveau):
        liste_logs = list(groupe)
        print(f"\n{niveau} ({len(liste_logs)} entrées):")
        for log in liste_logs[:3]:  # Afficher max 3 par niveau
            print(f"  • {log}")
        if len(liste_logs) > 3:
            print(f"  ... et {len(liste_logs) - 3} autres")

# Exemple d'utilisation
logs = [
    "[2025-10-27 10:00:00] INFO: Application démarrée",
    "[2025-10-27 10:01:00] ERROR: Connexion échouée",
    "[2025-10-27 10:02:00] WARNING: Mémoire faible",
    "[2025-10-27 10:03:00] INFO: Utilisateur connecté",
    "[2025-10-27 10:04:00] ERROR: Fichier introuvable",
    "[2025-10-27 10:05:00] INFO: Traitement terminé"
]

analyser_logs(logs)
```

---

## Itérateurs combinatoires

Ces fonctions créent des combinaisons, permutations et produits cartésiens.

### product() - Produit cartésien

```python
import itertools

# Produit cartésien de deux listes
couleurs = ['rouge', 'bleu']  
tailles = ['S', 'M', 'L']  

produit = itertools.product(couleurs, tailles)  
for item in produit:  
    print(item)
# ('rouge', 'S'), ('rouge', 'M'), ('rouge', 'L')
# ('bleu', 'S'), ('bleu', 'M'), ('bleu', 'L')

# Équivalent à des boucles imbriquées
for couleur in couleurs:
    for taille in tailles:
        print((couleur, taille))

# Avec repeat : produit cartésien avec soi-même
des = itertools.product(range(1, 7), repeat=2)  
print(f"Nombre de combinaisons pour 2 dés : {len(list(des))}")  # 36  

# Exemple : toutes les coordonnées d'une grille 3x3
coordonnees = itertools.product(range(3), range(3))  
print(list(coordonnees))  
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

### permutations() - Permutations

```python
import itertools

# Toutes les permutations possibles
elements = ['A', 'B', 'C']  
perms = itertools.permutations(elements)  

for p in perms:
    print(p)
# ('A', 'B', 'C'), ('A', 'C', 'B')
# ('B', 'A', 'C'), ('B', 'C', 'A')
# ('C', 'A', 'B'), ('C', 'B', 'A')

# Permutations de longueur 2
perms_2 = itertools.permutations(elements, 2)  
print(list(perms_2))  
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Nombre de permutations : n! / (n-r)!
import math  
n, r = 3, 2  
nb_perms = math.factorial(n) // math.factorial(n - r)  
print(f"Nombre de permutations de {r} parmi {n} : {nb_perms}")  # 6  
```

### combinations() - Combinaisons sans répétition

```python
import itertools

# Combinaisons de 2 éléments parmi 4
elements = ['A', 'B', 'C', 'D']  
combos = itertools.combinations(elements, 2)  

for c in combos:
    print(c)
# ('A', 'B'), ('A', 'C'), ('A', 'D')
# ('B', 'C'), ('B', 'D')
# ('C', 'D')

# Nombre de combinaisons : n! / (r! × (n-r)!)
import math  
n, r = 4, 2  
nb_combos = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))  
print(f"Nombre de combinaisons : {nb_combos}")  # 6  
```

### combinations_with_replacement() - Combinaisons avec répétition

```python
import itertools

# Combinaisons avec répétition autorisée
elements = ['A', 'B', 'C']  
combos = itertools.combinations_with_replacement(elements, 2)  

for c in combos:
    print(c)
# ('A', 'A'), ('A', 'B'), ('A', 'C')
# ('B', 'B'), ('B', 'C')
# ('C', 'C')
```

### Exemple pratique : Générateur de mots de passe

```python
import itertools  
import random  

def generer_mots_de_passe(longueur=4, quantite=5):
    """Génère des mots de passe à partir de combinaisons de caractères"""

    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Générer toutes les combinaisons possibles
    # Attention : peut être très long pour de grandes longueurs !
    combinaisons = itertools.product(caracteres, repeat=longueur)

    # Convertir en liste et mélanger
    toutes_combos = [''.join(combo) for combo in itertools.islice(combinaisons, 10000)]
    random.shuffle(toutes_combos)

    # Prendre les n premières
    return toutes_combos[:quantite]

# Générer des mots de passe
mots_de_passe = generer_mots_de_passe(4, 5)  
print("🔐 Mots de passe générés :")  
for mdp in mots_de_passe:  
    print(f"  • {mdp}")
```

### Exemple pratique : Tirages de loterie

```python
import itertools

def generer_grilles_loto(nb_grilles=5):
    """Génère des grilles de loto (5 numéros parmi 49)"""

    # Tous les numéros possibles
    numeros = range(1, 50)

    # Générer toutes les combinaisons possibles de 5 numéros
    toutes_combinaisons = itertools.combinations(numeros, 5)

    # Prendre les n premières (en pratique, on choisirait aléatoirement)
    grilles = list(itertools.islice(toutes_combinaisons, nb_grilles))

    return grilles

print("🎰 Grilles de loto :")  
for i, grille in enumerate(generer_grilles_loto(5), 1):  
    numeros_tries = sorted(grille)
    print(f"Grille {i}: {numeros_tries}")
```

---

## Autres fonctions utiles d'itertools

### accumulate() - Accumulation de valeurs

```python
import itertools  
import operator  

# Somme cumulative (par défaut)
nombres = [1, 2, 3, 4, 5]  
cumul = itertools.accumulate(nombres)  
print(list(cumul))  # [1, 3, 6, 10, 15]  

# Produit cumulatif
nombres = [1, 2, 3, 4, 5]  
produit_cumul = itertools.accumulate(nombres, operator.mul)  
print(list(produit_cumul))  # [1, 2, 6, 24, 120]  

# Maximum cumulatif
nombres = [5, 1, 8, 3, 9, 2]  
max_cumul = itertools.accumulate(nombres, max)  
print(list(max_cumul))  # [5, 5, 8, 8, 9, 9]  

# Avec une fonction personnalisée
mots = ['Hello', ' ', 'World', '!']  
concatenation = itertools.accumulate(mots, lambda a, b: a + b)  
print(list(concatenation))  # ['Hello', 'Hello ', 'Hello World', 'Hello World!']  
```

### tee() - Dupliquer un itérateur

```python
import itertools

# Créer plusieurs itérateurs indépendants depuis un seul
nombres = [1, 2, 3, 4, 5]  
iter1, iter2, iter3 = itertools.tee(nombres, 3)  

print(list(iter1))  # [1, 2, 3, 4, 5]  
print(list(iter2))  # [1, 2, 3, 4, 5]  
print(list(iter3))  # [1, 2, 3, 4, 5]  

# Utile pour parcourir plusieurs fois sans stocker en mémoire
data = range(1000000)  
iter_pairs, iter_impairs = itertools.tee(data, 2)  

pairs = (x for x in iter_pairs if x % 2 == 0)  
impairs = (x for x in iter_impairs if x % 2 == 1)  
```

### zip_longest() - Zip avec remplissage

```python
import itertools

# zip() standard s'arrête à la plus courte séquence
liste1 = [1, 2, 3]  
liste2 = ['a', 'b']  

resultat = list(zip(liste1, liste2))  
print(resultat)  # [(1, 'a'), (2, 'b')]  

# zip_longest() continue jusqu'à la plus longue, avec une valeur par défaut
resultat = list(itertools.zip_longest(liste1, liste2, fillvalue='X'))  
print(resultat)  # [(1, 'a'), (2, 'b'), (3, 'X')]  

# Exemple pratique : combiner des listes de longueurs différentes
noms = ['Alice', 'Bob', 'Charlie']  
ages = [25, 30]  
villes = ['Paris', 'Lyon', 'Marseille', 'Nice']  

personnes = itertools.zip_longest(noms, ages, villes, fillvalue='N/A')  
for nom, age, ville in personnes:  
    print(f"{nom} - {age} ans - {ville}")
```

---

## Le module `functools` - Outils de programmation fonctionnelle

Le module `functools` fournit des outils pour travailler avec des fonctions d'ordre supérieur (fonctions qui prennent ou retournent d'autres fonctions).

### Import du module

```python
import functools

# Ou importer des fonctions spécifiques
from functools import reduce, partial, lru_cache
```

---

## reduce() - Réduction d'un itérable

`reduce()` applique une fonction de manière cumulative aux éléments d'une séquence.

```python
from functools import reduce  
import operator  

# Somme de tous les éléments
nombres = [1, 2, 3, 4, 5]  
somme = reduce(lambda x, y: x + y, nombres)  
print(somme)  # 15  

# Équivalent à
resultat = 1  
for nombre in [2, 3, 4, 5]:  
    resultat = resultat + nombre

# Avec operator.add (plus lisible)
somme = reduce(operator.add, nombres)  
print(somme)  # 15  

# Produit de tous les éléments
produit = reduce(operator.mul, nombres)  
print(produit)  # 120 (1 × 2 × 3 × 4 × 5)  

# Trouver le maximum
maximum = reduce(lambda x, y: x if x > y else y, nombres)  
print(maximum)  # 5  

# Avec une valeur initiale
somme_plus_10 = reduce(operator.add, nombres, 10)  
print(somme_plus_10)  # 25 (10 + 1 + 2 + 3 + 4 + 5)  
```

### Exemple pratique : Calculs sur des dictionnaires

```python
from functools import reduce  
import operator  

def fusionner_dictionnaires(liste_dicts):
    """Fusionne plusieurs dictionnaires en additionnant les valeurs communes"""
    return reduce(
        lambda d1, d2: {k: d1.get(k, 0) + d2.get(k, 0)
                       for k in set(d1) | set(d2)},
        liste_dicts
    )

# Ventes par magasin et par jour
ventes_jour1 = {'pommes': 10, 'bananes': 5, 'oranges': 8}  
ventes_jour2 = {'pommes': 12, 'bananes': 7, 'poires': 6}  
ventes_jour3 = {'pommes': 8, 'oranges': 10, 'poires': 4}  

ventes_totales = fusionner_dictionnaires([ventes_jour1, ventes_jour2, ventes_jour3])  
print("🛒 Ventes totales :")  
for fruit, quantite in ventes_totales.items():  
    print(f"  {fruit}: {quantite}")
```

---

## partial() - Application partielle de fonctions

`partial()` permet de fixer certains arguments d'une fonction et de créer une nouvelle fonction.

```python
from functools import partial

# Fonction de base
def puissance(base, exposant):
    return base ** exposant

# Créer des fonctions spécialisées
carre = partial(puissance, exposant=2)  
cube = partial(puissance, exposant=3)  

print(carre(5))  # 25 (5²)  
print(cube(3))   # 27 (3³)  

# Autre exemple : fonction de multiplication
def multiplier(x, y):
    return x * y

doubler = partial(multiplier, 2)  
tripler = partial(multiplier, 3)  

print(doubler(5))  # 10  
print(tripler(5))  # 15  

# Exemple avec print
from functools import partial

print_erreur = partial(print, "[ERREUR]", sep=" - ")  
print_info = partial(print, "[INFO]", sep=" - ")  

print_erreur("Fichier introuvable")  # [ERREUR] - Fichier introuvable  
print_info("Connexion établie")      # [INFO] - Connexion établie  
```

### Exemple pratique : Conversion d'unités

```python
from functools import partial

def convertir(valeur, facteur):
    """Convertit une valeur selon un facteur"""
    return valeur * facteur

# Créer des fonctions de conversion spécifiques
km_vers_miles = partial(convertir, facteur=0.621371)  
miles_vers_km = partial(convertir, facteur=1.60934)  
celsius_vers_kelvin = partial(convertir, facteur=1)  # Nécessite ajustement  

# Pour Celsius vers Kelvin, on a besoin d'une fonction différente
def convertir_temperature(valeur, formule):
    return formule(valeur)

celsius_vers_kelvin = partial(convertir_temperature, formule=lambda c: c + 273.15)  
fahrenheit_vers_celsius = partial(convertir_temperature, formule=lambda f: (f - 32) * 5/9)  

# Utilisation
print(f"100 km = {km_vers_miles(100):.2f} miles")  
print(f"50 miles = {miles_vers_km(50):.2f} km")  
print(f"25°C = {celsius_vers_kelvin(25):.2f}K")  
print(f"77°F = {fahrenheit_vers_celsius(77):.2f}°C")  
```

---

## lru_cache() - Mémorisation de résultats

`lru_cache()` est un décorateur qui met en cache les résultats d'une fonction pour éviter de recalculer les mêmes valeurs.

```python
from functools import lru_cache  
import time  

# Sans cache
def fibonacci_lent(n):
    """Calcule le n-ième nombre de Fibonacci (lent)"""
    if n < 2:
        return n
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)

# Avec cache
@lru_cache(maxsize=None)  # ou @cache (Python 3.9+, équivalent)
def fibonacci_rapide(n):
    """Calcule le n-ième nombre de Fibonacci (rapide avec cache)"""
    if n < 2:
        return n
    return fibonacci_rapide(n-1) + fibonacci_rapide(n-2)

# Comparaison de performance
print("Sans cache :")  
debut = time.time()  
resultat = fibonacci_lent(30)  
duree = time.time() - debut  
print(f"fibonacci(30) = {resultat} en {duree:.4f}s")  

print("\nAvec cache :")  
debut = time.time()  
resultat = fibonacci_rapide(30)  
duree = time.time() - debut  
print(f"fibonacci(30) = {resultat} en {duree:.6f}s")  

# Informations sur le cache
print(f"\nInfos cache : {fibonacci_rapide.cache_info()}")

# Vider le cache
fibonacci_rapide.cache_clear()
```

### Exemple pratique : Calcul de factorielles avec cache

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def factorielle(n):
    """Calcule la factorielle de n avec mémorisation"""
    if n < 2:
        return 1
    return n * factorielle(n - 1)

@lru_cache(maxsize=128)
def combinaison(n, k):
    """Calcule C(n, k) = n! / (k! × (n-k)!)"""
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorielle(n) // (factorielle(k) * factorielle(n - k))

# Utilisation
print(f"10! = {factorielle(10):,}")  
print(f"C(10, 3) = {combinaison(10, 3)}")  

# Triangle de Pascal
print("\nTriangle de Pascal :")  
for n in range(7):  
    ligne = [combinaison(n, k) for k in range(n + 1)]
    print(" ".join(f"{c:3d}" for c in ligne).center(30))
```

---

## wraps() - Préserver les métadonnées de fonction

Quand on crée un décorateur, `wraps()` préserve les informations de la fonction originale.

```python
from functools import wraps  
import time  

# Sans wraps (mauvaise pratique)
def chronometrer_mauvais(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        duree = time.time() - debut
        print(f"Durée : {duree:.4f}s")
        return resultat
    return wrapper

# Avec wraps (bonne pratique)
def chronometrer(func):
    @wraps(func)  # Préserve __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        duree = time.time() - debut
        print(f"Durée de {func.__name__} : {duree:.4f}s")
        return resultat
    return wrapper

@chronometrer
def calcul_long(n):
    """Effectue un calcul long"""
    time.sleep(0.1)
    return sum(range(n))

# Sans wraps, on perdrait le nom et la doc de la fonction
resultat = calcul_long(1000)  
print(f"Nom : {calcul_long.__name__}")  # calcul_long (grâce à wraps)  
print(f"Doc : {calcul_long.__doc__}")   # La docstring originale  
```

---

## total_ordering() - Simplifier les comparaisons

`total_ordering()` génère automatiquement les méthodes de comparaison manquantes.

```python
from functools import total_ordering

@total_ordering
class Personne:
    """Classe Personne avec comparaisons automatiques"""

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    # Il suffit de définir __eq__ et une autre méthode de comparaison
    def __eq__(self, autre):
        return self.age == autre.age

    def __lt__(self, autre):
        return self.age < autre.age

    # Les méthodes __le__, __gt__, __ge__ sont générées automatiquement !

    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"

# Utilisation
alice = Personne("Alice", 25)  
bob = Personne("Bob", 30)  
charlie = Personne("Charlie", 25)  

print(alice == charlie)  # True  
print(alice < bob)       # True  
print(bob > alice)       # True (généré automatiquement)  
print(alice <= charlie)  # True (généré automatiquement)  

# Tri
personnes = [bob, alice, charlie]  
personnes_triees = sorted(personnes)  
print(personnes_triees)  # Triées par âge  
```

---

## singledispatch() - Surcharge de fonctions selon le type

`singledispatch()` permet de créer des fonctions génériques qui se comportent différemment selon le type d'argument.

```python
from functools import singledispatch

@singledispatch
def traiter(donnee):
    """Fonction générique par défaut"""
    print(f"Type non supporté : {type(donnee)}")

@traiter.register(int)
def _(donnee):
    """Traitement pour les entiers"""
    print(f"Entier : {donnee} × 2 = {donnee * 2}")

@traiter.register(str)
def _(donnee):
    """Traitement pour les chaînes"""
    print(f"Chaîne : '{donnee}' en majuscules = '{donnee.upper()}'")

@traiter.register(list)
def _(donnee):
    """Traitement pour les listes"""
    print(f"Liste : {len(donnee)} éléments, somme = {sum(donnee)}")

# Utilisation
traiter(10)                    # Entier  
traiter("bonjour")             # Chaîne  
traiter([1, 2, 3, 4, 5])       # Liste  
traiter(3.14)                  # Type non supporté  
```

---

## Exemple complet : Système de traitement de données

Combinons itertools et functools pour créer un système de traitement de données efficace.

```python
import itertools  
import functools  
from operator import itemgetter  

# Données : transactions e-commerce
transactions = [
    {'id': 1, 'client': 'Alice', 'categorie': 'Livres', 'montant': 25.50},
    {'id': 2, 'client': 'Bob', 'categorie': 'Électronique', 'montant': 450.00},
    {'id': 3, 'client': 'Alice', 'categorie': 'Livres', 'montant': 15.00},
    {'id': 4, 'client': 'Charlie', 'categorie': 'Vêtements', 'montant': 89.99},
    {'id': 5, 'client': 'Alice', 'categorie': 'Électronique', 'montant': 120.00},
    {'id': 6, 'client': 'Bob', 'categorie': 'Livres', 'montant': 30.00},
    {'id': 7, 'client': 'Charlie', 'categorie': 'Électronique', 'montant': 199.99},
]

class AnalyseurTransactions:
    """Analyse des transactions avec itertools et functools"""

    def __init__(self, transactions):
        self.transactions = transactions

    @functools.lru_cache(maxsize=None)
    def total_par_client(self, client):
        """Calcule le total dépensé par un client (avec cache)"""
        transactions_client = [t for t in self.transactions if t['client'] == client]
        return functools.reduce(
            lambda total, t: total + t['montant'],
            transactions_client,
            0
        )

    def grouper_par_categorie(self):
        """Groupe les transactions par catégorie"""
        # Trier d'abord par catégorie
        transactions_triees = sorted(self.transactions, key=itemgetter('categorie'))

        print("\n📊 Transactions par catégorie :")
        print("=" * 60)

        for categorie, groupe in itertools.groupby(transactions_triees, key=itemgetter('categorie')):
            liste_trans = list(groupe)
            total = sum(t['montant'] for t in liste_trans)
            print(f"\n{categorie} ({len(liste_trans)} transactions) :")
            for t in liste_trans:
                print(f"  • {t['client']:10s} - {t['montant']:7.2f}€")
            print(f"  Total : {total:.2f}€")

    def top_clients(self, n=3):
        """Affiche les n meilleurs clients"""
        # Obtenir tous les clients uniques
        clients = set(t['client'] for t in self.transactions)

        # Calculer les totaux
        totaux = [(client, self.total_par_client(client)) for client in clients]

        # Trier par montant décroissant
        totaux_tries = sorted(totaux, key=itemgetter(1), reverse=True)

        print(f"\n🏆 Top {n} clients :")
        print("=" * 60)
        for i, (client, total) in enumerate(itertools.islice(totaux_tries, n), 1):
            print(f"{i}. {client:15s} - {total:7.2f}€")

    def statistiques_globales(self):
        """Calcule des statistiques globales"""
        montants = [t['montant'] for t in self.transactions]

        # Utiliser itertools.accumulate pour montrer l'évolution
        cumul = list(itertools.accumulate(montants))

        print("\n📈 Statistiques globales :")
        print("=" * 60)
        print(f"Nombre de transactions : {len(self.transactions)}")
        print(f"Montant total : {sum(montants):.2f}€")
        print(f"Montant moyen : {sum(montants) / len(montants):.2f}€")
        print(f"Montant min : {min(montants):.2f}€")
        print(f"Montant max : {max(montants):.2f}€")

        print(f"\n💰 Évolution du chiffre d'affaires cumulé :")
        for i, total in enumerate(cumul, 1):
            barre = "█" * int(total / 10)
            print(f"Transaction {i}: {total:7.2f}€ {barre}")

# Utilisation
analyseur = AnalyseurTransactions(transactions)

analyseur.grouper_par_categorie()  
analyseur.top_clients(3)  
analyseur.statistiques_globales()  

# Afficher les informations de cache
print(f"\n🔍 Cache info : {analyseur.total_par_client.cache_info()}")
```

---

## Exemple pratique : Pipeline de traitement de texte

```python
import itertools  
import functools  
from collections import Counter  

def nettoyer_texte(texte):
    """Nettoie le texte"""
    return texte.lower().strip()

def tokeniser(texte):
    """Découpe en mots"""
    return texte.split()

def filtrer_mots_courts(mots, longueur_min=3):
    """Garde seulement les mots assez longs"""
    return [mot for mot in mots if len(mot) >= longueur_min]

# Créer un pipeline avec partial
pipeline_texte = functools.partial(filtrer_mots_courts, longueur_min=4)

def analyser_textes(textes):
    """Analyse plusieurs textes"""
    print("📖 Analyse de textes")
    print("=" * 60)

    # Nettoyer et tokeniser tous les textes
    tous_les_mots = []
    for texte in textes:
        texte_propre = nettoyer_texte(texte)
        mots = tokeniser(texte_propre)
        mots_filtres = pipeline_texte(mots)
        tous_les_mots.extend(mots_filtres)

    # Compter les occurrences
    compteur = Counter(tous_les_mots)

    # Top 5 des mots les plus fréquents
    print("\n🔤 Mots les plus fréquents :")
    for mot, freq in itertools.islice(compteur.most_common(), 5):
        print(f"  {mot:15s} : {freq} fois")

    # Statistiques
    print(f"\n📊 Statistiques :")
    print(f"  Nombre total de mots : {len(tous_les_mots)}")
    print(f"  Mots uniques : {len(compteur)}")
    print(f"  Mots apparaissant une seule fois : {sum(1 for freq in compteur.values() if freq == 1)}")

# Exemples de textes
textes = [
    "Python est un langage de programmation puissant",
    "Python est facile à apprendre et très populaire",
    "La programmation Python est utilisée partout",
    "Apprendre Python ouvre de nombreuses opportunités"
]

analyser_textes(textes)
```

---

## Bonnes pratiques

### 1. Utiliser itertools pour l'efficacité mémoire

```python
import itertools

# ❌ Crée une grande liste en mémoire
grandes_donnees = list(range(1000000))  
for i in grandes_donnees[:100]:  
    print(i)

# ✅ Utilise un itérateur (pas de liste en mémoire)
grandes_donnees = range(1000000)  
for i in itertools.islice(grandes_donnees, 100):  
    print(i)
```

### 2. Utiliser lru_cache pour les fonctions coûteuses

```python
from functools import lru_cache

# ✅ Bon : utiliser le cache pour éviter les recalculs
@lru_cache(maxsize=128)
def fonction_couteuse(n):
    # Calcul long...
    return resultat
```

### 3. Utiliser wraps dans les décorateurs

```python
from functools import wraps

# ✅ Bon : préserver les métadonnées
def mon_decorateur(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 4. Combiner les outils pour plus de puissance

```python
import itertools  
import functools  

# Combiner chain et reduce
listes = [[1, 2], [3, 4], [5, 6]]  
somme_totale = functools.reduce(  
    lambda x, y: x + y,
    itertools.chain.from_iterable(listes)
)
```

### 5. Attention aux itérateurs infinis

```python
import itertools

# ❌ Ceci ne se termine jamais !
# for i in itertools.count():
#     print(i)

# ✅ Toujours définir une condition d'arrêt
for i in itertools.count():
    if i > 10:
        break
    print(i)

# ✅ Ou utiliser islice
for i in itertools.islice(itertools.count(), 10):
    print(i)
```

---

## Résumé

### Module itertools

| Catégorie | Fonctions | Usage |
|-----------|-----------|-------|
| **Infinis** | `count()`, `cycle()`, `repeat()` | Itérateurs sans fin |
| **Terminaison** | `chain()`, `compress()`, `dropwhile()`, `filterfalse()`, `islice()`, `takewhile()` | Filtrage et transformation |
| **Groupement** | `groupby()` | Regrouper éléments consécutifs |
| **Combinatoires** | `product()`, `permutations()`, `combinations()` | Combinaisons et permutations |
| **Autres** | `accumulate()`, `tee()`, `zip_longest()` | Outils divers |

### Module functools

| Fonction | Usage | Exemple |
|----------|-------|---------|
| `reduce()` | Réduction cumulative | Somme, produit |
| `partial()` | Application partielle | Créer fonctions spécialisées |
| `lru_cache()` | Mémorisation | Cache pour performances |
| `wraps()` | Préserver métadonnées | Décorateurs propres |
| `total_ordering()` | Générer comparaisons | Classes comparables |
| `singledispatch()` | Surcharge de fonctions | Comportement selon type |

### Exemples d'utilisation courante

```python
import itertools  
import functools  

# Créer des combinaisons
combos = itertools.combinations([1, 2, 3], 2)

# Accumuler des valeurs
cumul = itertools.accumulate([1, 2, 3, 4, 5])

# Réduire une liste
somme = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# Créer une fonction spécialisée
doubler = functools.partial(lambda x, y: x * y, 2)

# Mettre en cache
@functools.lru_cache(maxsize=128)
def calcul_lent(n):
    return n ** 2
```

Les modules `itertools` et `functools` sont des outils puissants qui permettent d'écrire du code Python plus élégant, efficace et fonctionnel !

⏭️ [logging et configuration](/07-bibliotheques-standard/05-logging-et-configuration.md)
