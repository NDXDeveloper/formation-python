🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.4 Générateurs et expressions génératrices

## Introduction

Les **générateurs** sont l'une des fonctionnalités les plus puissantes et élégantes de Python. Ils permettent de créer des itérateurs de manière simple et efficace, en économisant de la mémoire.

Dans ce chapitre, nous allons découvrir comment créer et utiliser des générateurs, comprendre leurs avantages, et explorer les expressions génératrices. Ces concepts sont essentiels pour écrire du code Python performant et élégant.

---

## Qu'est-ce qu'un générateur ?

Un **générateur** est une fonction spéciale qui **produit une séquence de valeurs** au lieu de retourner une seule valeur. Contrairement à une fonction normale qui utilise `return`, un générateur utilise le mot-clé `yield`.

### Fonction normale vs Générateur

**Fonction normale :**

```python
def creer_liste_nombres(n):
    """Crée une liste de nombres de 0 à n-1."""
    liste = []
    for i in range(n):
        liste.append(i)
    return liste

nombres = creer_liste_nombres(5)  
print(nombres)  # [0, 1, 2, 3, 4]  
print(type(nombres))  # <class 'list'>  
```

**Générateur :**

```python
def generer_nombres(n):
    """Génère des nombres de 0 à n-1."""
    for i in range(n):
        yield i

nombres = generer_nombres(5)  
print(nombres)  # <generator object generer_nombres at 0x...>  
print(type(nombres))  # <class 'generator'>  

# Pour voir les valeurs, il faut itérer
for nombre in nombres:
    print(nombre)  # 0, 1, 2, 3, 4
```

### Le mot-clé yield

Le mot-clé `yield` :
- **Produit** une valeur
- **Suspend** l'exécution de la fonction
- **Reprend** là où elle s'était arrêtée lors du prochain appel

```python
def mon_generateur():
    print("Première valeur")
    yield 1
    print("Deuxième valeur")
    yield 2
    print("Troisième valeur")
    yield 3
    print("Fin")

# Créer le générateur
gen = mon_generateur()

# Récupérer les valeurs une par une
print(next(gen))
# Affiche : Première valeur
# Affiche : 1

print(next(gen))
# Affiche : Deuxième valeur
# Affiche : 2

print(next(gen))
# Affiche : Troisième valeur
# Affiche : 3

# print(next(gen))
# Affiche : Fin
# Lève : StopIteration
```

---

## Créer des générateurs simples

### Exemple 1 : Générateur de carrés

```python
def generer_carres(n):
    """Génère les carrés des nombres de 0 à n-1."""
    for i in range(n):
        yield i ** 2

# Utilisation
for carre in generer_carres(5):
    print(carre, end=" ")  # 0 1 4 9 16
```

### Exemple 2 : Générateur de nombres pairs

```python
def generer_pairs(debut, fin):
    """Génère tous les nombres pairs entre debut et fin."""
    for nombre in range(debut, fin + 1):
        if nombre % 2 == 0:
            yield nombre

# Utilisation
pairs = generer_pairs(1, 10)  
print(list(pairs))  # [2, 4, 6, 8, 10]  
```

### Exemple 3 : Générateur de Fibonacci

```python
def fibonacci(n):
    """Génère les n premiers nombres de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Utilisation
print("Suite de Fibonacci (10 premiers) :")  
for nombre in fibonacci(10):  
    print(nombre, end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

---

## Avantages des générateurs

### 1. Économie de mémoire

**Avec une liste (tout en mémoire) :**

```python
def creer_grands_nombres():
    """Crée une liste de 1 million de nombres."""
    return [i for i in range(1000000)]

# Crée une liste de 1 million d'éléments en mémoire
liste = creer_grands_nombres()  
print(f"Taille en mémoire : ~{liste.__sizeof__()} bytes")  
# Taille en mémoire : ~8000000 bytes (environ 8 MB)
```

**Avec un générateur (valeurs à la demande) :**

```python
def generer_grands_nombres():
    """Génère 1 million de nombres à la demande."""
    for i in range(1000000):
        yield i

# Ne crée qu'un objet générateur, pas les valeurs
gen = generer_grands_nombres()  
print(f"Taille en mémoire : ~{gen.__sizeof__()} bytes")  
# Taille en mémoire : ~200 bytes
```

### 2. Évaluation paresseuse (lazy evaluation)

Les valeurs sont produites **uniquement quand nécessaire** :

```python
def generer_avec_traitement(n):
    """Génère des nombres avec un traitement coûteux."""
    for i in range(n):
        print(f"  Traitement de {i}...")
        yield i * 2

# Le générateur est créé, mais aucun traitement n'est effectué
gen = generer_avec_traitement(5)  
print("Générateur créé")  

# Les traitements n'ont lieu que lors de l'itération
print("\nItération :")  
for valeur in gen:  
    print(f"Reçu : {valeur}")
    if valeur >= 4:  # On peut s'arrêter tôt
        break

# Affiche :
# Générateur créé
#
# Itération :
#   Traitement de 0...
# Reçu : 0
#   Traitement de 1...
# Reçu : 2
#   Traitement de 2...
# Reçu : 4
```

### 3. Séquences infinies

Les générateurs peuvent produire des séquences infinies sans problème de mémoire :

```python
def compteur_infini(debut=0):
    """Génère une séquence infinie de nombres."""
    nombre = debut
    while True:
        yield nombre
        nombre += 1

# Utilisation avec limitation
compteur = compteur_infini(10)  
for i, valeur in enumerate(compteur):  
    print(valeur, end=" ")
    if i >= 9:  # Afficher seulement 10 valeurs
        break
# Affiche : 10 11 12 13 14 15 16 17 18 19
```

---

## Expressions génératrices

Une **expression génératrice** est une syntaxe compacte pour créer un générateur, similaire aux compréhensions de listes mais avec des parenthèses.

### Syntaxe

```python
# Compréhension de liste (crée une liste)
liste = [x ** 2 for x in range(5)]

# Expression génératrice (crée un générateur)
generateur = (x ** 2 for x in range(5))
```

### Comparaison

```python
# Compréhension de liste
carres_liste = [x ** 2 for x in range(5)]  
print(carres_liste)  # [0, 1, 4, 9, 16]  
print(type(carres_liste))  # <class 'list'>  

# Expression génératrice
carres_gen = (x ** 2 for x in range(5))  
print(carres_gen)  # <generator object <genexpr> at 0x...>  
print(type(carres_gen))  # <class 'generator'>  

# Convertir en liste
print(list(carres_gen))  # [0, 1, 4, 9, 16]
```

### Exemples pratiques

#### Exemple 1 : Filtrage et transformation

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec compréhension de liste
pairs_doubles_liste = [x * 2 for x in nombres if x % 2 == 0]

# Avec expression génératrice
pairs_doubles_gen = (x * 2 for x in nombres if x % 2 == 0)

print(list(pairs_doubles_gen))  # [4, 8, 12, 16, 20]
```

#### Exemple 2 : Somme sans créer de liste

```python
# ❌ Crée inutilement une liste
somme = sum([x ** 2 for x in range(1000000)])

# ✅ Plus efficace : utilise un générateur
somme = sum(x ** 2 for x in range(1000000))

# Note : pas besoin de parenthèses supplémentaires dans sum()
```

#### Exemple 3 : Chaîner des générateurs

```python
nombres = range(20)

# Filtrer les pairs
pairs = (x for x in nombres if x % 2 == 0)

# Mettre au carré
carres = (x ** 2 for x in pairs)

# Filtrer ceux supérieurs à 50
grands = (x for x in carres if x > 50)

# Seules les valeurs nécessaires sont calculées
print(list(grands))  # [64, 100, 144, 196, 256, 324]
```

---

## Fonctions natives utilisant des générateurs

Python intègre plusieurs fonctions qui fonctionnent bien avec les générateurs :

### 1. map() et filter()

```python
nombres = range(10)

# map() retourne un itérateur (similaire à un générateur)
doubles = map(lambda x: x * 2, nombres)  
print(list(doubles))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]  

# filter() aussi
pairs = filter(lambda x: x % 2 == 0, nombres)  
print(list(pairs))  # [0, 2, 4, 6, 8]  
```

### 2. zip()

```python
prenoms = ["Alice", "Bob", "Charlie"]  
ages = [25, 30, 35]  

# zip() retourne un itérateur
couples = zip(prenoms, ages)

for prenom, age in couples:
    print(f"{prenom} a {age} ans")
# Alice a 25 ans
# Bob a 30 ans
# Charlie a 35 ans
```

### 3. enumerate()

```python
fruits = ["pomme", "banane", "orange"]

# enumerate() retourne un itérateur
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. pomme
# 2. banane
# 3. orange
```

### 4. reversed()

```python
nombres = [1, 2, 3, 4, 5]

# reversed() retourne un itérateur
for n in reversed(nombres):
    print(n, end=" ")  # 5 4 3 2 1
```

---

## Cas d'usage pratiques

### 1. Lecture de fichiers volumineux

```python
def lire_lignes(nom_fichier):
    """Génère les lignes d'un fichier une par une."""
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            yield ligne.strip()

# Utilisation efficace en mémoire
# for ligne in lire_lignes('grand_fichier.txt'):
#     if 'erreur' in ligne.lower():
#         print(ligne)
```

### 2. Pagination de résultats

```python
def paginer(elements, taille_page):
    """Génère des pages d'éléments."""
    for i in range(0, len(elements), taille_page):
        yield elements[i:i + taille_page]

# Exemple
items = list(range(1, 26))  # 25 items

for numero_page, page in enumerate(paginer(items, taille_page=5), start=1):
    print(f"Page {numero_page}: {page}")

# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]
# Page 4: [16, 17, 18, 19, 20]
# Page 5: [21, 22, 23, 24, 25]
```

### 3. Pipeline de traitement de données

```python
def lire_nombres():
    """Simule la lecture de données."""
    for i in range(1, 11):
        yield i

def filtrer_pairs(nombres):
    """Filtre les nombres pairs."""
    for n in nombres:
        if n % 2 == 0:
            yield n

def multiplier_par_10(nombres):
    """Multiplie chaque nombre par 10."""
    for n in nombres:
        yield n * 10

# Pipeline de traitement
donnees = lire_nombres()  
pairs = filtrer_pairs(donnees)  
resultat = multiplier_par_10(pairs)  

print(list(resultat))  # [20, 40, 60, 80, 100]
```

### 4. Génération de données de test

```python
def generer_utilisateurs(n):
    """Génère n utilisateurs de test."""
    for i in range(1, n + 1):
        yield {
            "id": i,
            "nom": f"Utilisateur_{i}",
            "email": f"user{i}@example.com",
            "actif": i % 2 == 0
        }

# Utilisation
for utilisateur in generer_utilisateurs(5):
    print(utilisateur)

# {'id': 1, 'nom': 'Utilisateur_1', 'email': 'user1@example.com', 'actif': False}
# {'id': 2, 'nom': 'Utilisateur_2', 'email': 'user2@example.com', 'actif': True}
# ...
```

### 5. Parcours d'arborescence

```python
import os

def parcourir_fichiers(repertoire, extension=None):
    """Génère tous les fichiers d'un répertoire et ses sous-répertoires."""
    for racine, dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if extension is None or fichier.endswith(extension):
                yield os.path.join(racine, fichier)

# Utilisation
# for fichier_python in parcourir_fichiers('.', '.py'):
#     print(fichier_python)
```

---

## Générateurs infinis

Les générateurs peuvent créer des séquences infinies de manière élégante :

### Exemple 1 : Compteur infini

```python
def compteur(debut=0, pas=1):
    """Générateur de compteur infini."""
    valeur = debut
    while True:
        yield valeur
        valeur += pas

# Utilisation avec limite
c = compteur(10, 2)  
for _ in range(5):  
    print(next(c), end=" ")  # 10 12 14 16 18
```

### Exemple 2 : Cycle

```python
def cycle(iterable):
    """Répète indéfiniment les éléments d'un itérable."""
    while True:
        for element in iterable:
            yield element

# Utilisation
couleurs = cycle(['rouge', 'vert', 'bleu'])  
for _ in range(8):  
    print(next(couleurs), end=" ")
# rouge vert bleu rouge vert bleu rouge vert
```

### Exemple 3 : Répétition

```python
def repeter(valeur, n=None):
    """Répète une valeur n fois (ou indéfiniment si n=None)."""
    if n is None:
        while True:
            yield valeur
    else:
        for _ in range(n):
            yield valeur

# Répétition infinie
# zeros = repeter(0)

# Répétition limitée
cinq_fois = repeter("Python", 5)  
print(list(cinq_fois))  # ['Python', 'Python', 'Python', 'Python', 'Python']  
```

---

## Méthodes avancées des générateurs

Les générateurs ont des méthodes spéciales pour contrôler leur exécution :

### 1. send() - Envoyer des valeurs au générateur

```python
def generateur_avec_send():
    """Générateur qui peut recevoir des valeurs."""
    total = 0
    while True:
        valeur = yield total
        if valeur is not None:
            total += valeur

gen = generateur_avec_send()

# Démarrer le générateur
print(next(gen))  # 0

# Envoyer des valeurs
print(gen.send(10))  # 10  
print(gen.send(5))   # 15  
print(gen.send(3))   # 18  
```

### 2. close() - Fermer un générateur

```python
def mon_generateur():
    """Générateur avec gestion de la fermeture."""
    try:
        for i in range(10):
            yield i
    finally:
        print("Générateur fermé")

gen = mon_generateur()

print(next(gen))  # 0  
print(next(gen))  # 1  

# Fermer le générateur
gen.close()  # Affiche : Générateur fermé

# Essayer d'obtenir une autre valeur lève StopIteration
# print(next(gen))  # StopIteration
```

### 3. throw() - Envoyer une exception

```python
def generateur_resilient():
    """Générateur qui gère les exceptions."""
    while True:
        try:
            valeur = yield
            print(f"Reçu : {valeur}")
        except ValueError:
            print("Erreur ValueError capturée !")

gen = generateur_resilient()  
next(gen)  # Démarrer  

gen.send(10)  # Reçu : 10  
gen.throw(ValueError, "Une erreur")  # Erreur ValueError capturée !  
gen.send(20)  # Reçu : 20  
```

---

## yield from - Délégation de générateurs

`yield from` permet à un générateur de déléguer une partie de ses opérations à un autre générateur :

### Exemple basique

```python
def generateur1():
    yield 1
    yield 2

def generateur2():
    yield 3
    yield 4

# Sans yield from
def combine_manuel():
    for valeur in generateur1():
        yield valeur
    for valeur in generateur2():
        yield valeur

# Avec yield from (plus élégant)
def combine_auto():
    yield from generateur1()
    yield from generateur2()

print(list(combine_auto()))  # [1, 2, 3, 4]
```

### Exemple pratique : aplatir des listes

```python
def aplatir(liste_imbriquee):
    """Aplatit une liste de listes."""
    for element in liste_imbriquee:
        if isinstance(element, list):
            yield from aplatir(element)  # Récursion
        else:
            yield element

# Utilisation
donnees = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]  
print(list(aplatir(donnees)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]  
```

### Exemple : parcourir un arbre

```python
class Noeud:
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        self.enfants = enfants or []

def parcourir_arbre(noeud):
    """Parcourt un arbre en profondeur."""
    yield noeud.valeur
    for enfant in noeud.enfants:
        yield from parcourir_arbre(enfant)

# Création d'un arbre
#       1
#      / \
#     2   3
#    / \
#   4   5

arbre = Noeud(1, [
    Noeud(2, [Noeud(4), Noeud(5)]),
    Noeud(3)
])

print(list(parcourir_arbre(arbre)))  # [1, 2, 4, 5, 3]
```

---

## Comparaison : Listes vs Générateurs

### Quand utiliser une liste ?

✅ **Utilisez une liste quand :**
- Vous devez accéder aux éléments plusieurs fois
- Vous avez besoin d'accéder à des éléments par index
- Vous devez connaître la longueur (`len()`)
- Vous devez modifier les éléments
- La collection est petite et tient en mémoire

```python
# Liste appropriée ici
nombres = [1, 2, 3, 4, 5]  
print(nombres[2])  # Accès par index  
print(len(nombres))  # Longueur  
print(nombres * 2)  # Duplication  
```

### Quand utiliser un générateur ?

✅ **Utilisez un générateur quand :**
- Vous parcourez les éléments une seule fois
- Vous traitez de grandes quantités de données
- Vous voulez économiser la mémoire
- Vous travaillez avec des séquences infinies
- Vous créez un pipeline de traitement

```python
# Générateur approprié ici
def lire_grand_fichier():
    with open('huge_file.txt', encoding='utf-8') as f:
        for ligne in f:
            yield ligne.strip()

# Économise énormément de mémoire
# for ligne in lire_grand_fichier():
#     traiter(ligne)
```

### Comparaison de performance

```python
import sys

# Liste : toutes les valeurs en mémoire
liste = [i for i in range(1000000)]  
print(f"Liste : {sys.getsizeof(liste) / 1024 / 1024:.2f} MB")  

# Générateur : seulement l'objet générateur
gen = (i for i in range(1000000))  
print(f"Générateur : {sys.getsizeof(gen) / 1024:.2f} KB")  

# Différence massive !
```

---

## Le module itertools

Python fournit le module `itertools` avec des outils puissants pour travailler avec des itérateurs :

### Fonctions utiles

```python
import itertools

# count() - Compteur infini
compteur = itertools.count(10, 2)  # Commence à 10, incrémente de 2  
for i in range(5):  
    print(next(compteur), end=" ")  # 10 12 14 16 18
print()

# cycle() - Répète indéfiniment
couleurs = itertools.cycle(['R', 'G', 'B'])  
for i in range(7):  
    print(next(couleurs), end=" ")  # R G B R G B R
print()

# repeat() - Répète une valeur
for x in itertools.repeat("Python", 3):
    print(x, end=" ")  # Python Python Python
print()

# chain() - Enchaîne des itérables
liste1 = [1, 2, 3]  
liste2 = [4, 5, 6]  
for x in itertools.chain(liste1, liste2):  
    print(x, end=" ")  # 1 2 3 4 5 6
print()

# islice() - Découpe un itérable
nombres = range(100)  
for x in itertools.islice(nombres, 5, 10):  # Éléments 5 à 9  
    print(x, end=" ")  # 5 6 7 8 9
print()

# takewhile() - Prend tant qu'une condition est vraie
nombres = [1, 4, 6, 4, 1]  
for x in itertools.takewhile(lambda x: x < 5, nombres):  
    print(x, end=" ")  # 1 4
print()

# dropwhile() - Ignore tant qu'une condition est vraie
nombres = [1, 4, 6, 4, 1]  
for x in itertools.dropwhile(lambda x: x < 5, nombres):  
    print(x, end=" ")  # 6 4 1
print()
```

---

## Bonnes pratiques

### 1. Nommage explicite

```python
# ✅ Bon : nom explicite
def generer_utilisateurs_actifs(utilisateurs):
    for user in utilisateurs:
        if user.actif:
            yield user

# ❌ Moins clair
def get_users(users):
    for u in users:
        if u.actif:
            yield u
```

### 2. Documentation

```python
def generer_fibonacci(n):
    """
    Génère les n premiers nombres de Fibonacci.

    Args:
        n (int): Nombre de termes à générer

    Yields:
        int: Prochain nombre de Fibonacci

    Example:
        >>> list(generer_fibonacci(5))
        [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### 3. Gérer proprement les ressources

```python
def lire_fichier_securise(nom_fichier):
    """Lit un fichier ligne par ligne de manière sécurisée."""
    try:
        fichier = open(nom_fichier, 'r', encoding='utf-8')
        try:
            for ligne in fichier:
                yield ligne.strip()
        finally:
            fichier.close()
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} introuvable")
        return

# Ou mieux, avec with :
def lire_fichier_securise_v2(nom_fichier):
    """Version améliorée avec context manager."""
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            yield ligne.strip()
```

### 4. Convertir en liste uniquement si nécessaire

```python
# ❌ Inutile de convertir en liste si on itère une fois
nombres = (x ** 2 for x in range(1000))  
liste_nombres = list(nombres)  # Consomme la mémoire  
for n in liste_nombres:  
    print(n)

# ✅ Mieux : itérer directement
nombres = (x ** 2 for x in range(1000))  
for n in nombres:  
    print(n)
```

### 5. Attention : les générateurs s'épuisent

```python
gen = (x for x in range(5))

# Premier parcours : fonctionne
print(list(gen))  # [0, 1, 2, 3, 4]

# Deuxième parcours : vide !
print(list(gen))  # []

# Solution : recréer le générateur ou utiliser une liste
gen = (x for x in range(5))  # Recréer
```

---

## Erreurs courantes

### 1. Oublier que les générateurs s'épuisent

```python
# ❌ Erreur
gen = (x for x in range(5))  
somme = sum(gen)  
liste = list(gen)  # Vide !  

# ✅ Solution
gen = (x for x in range(5))  
liste = list(gen)  # Convertir d'abord  
somme = sum(liste)  
```

### 2. Essayer d'accéder par index

```python
gen = (x for x in range(10))

# ❌ Erreur : les générateurs ne supportent pas l'indexation
# print(gen[5])  # TypeError

# ✅ Solution : convertir en liste
liste = list(gen)  
print(liste[5])  
```

### 3. Essayer d'obtenir la longueur

```python
gen = (x for x in range(10))

# ❌ Erreur : pas de len() pour les générateurs
# print(len(gen))  # TypeError

# ✅ Solution : convertir en liste (si vraiment nécessaire)
liste = list(gen)  
print(len(liste))  
```

---

## Résumé

Dans ce chapitre, nous avons exploré les générateurs en profondeur :

### Concepts clés

**Générateurs** :
- Fonctions qui utilisent `yield` au lieu de `return`
- Produisent des valeurs à la demande (lazy evaluation)
- Économisent énormément de mémoire
- Permettent de créer des séquences infinies

**Expressions génératrices** :
- Syntaxe compacte : `(expression for item in iterable)`
- Alternative légère aux compréhensions de listes
- Idéales pour un usage unique

**yield from** :
- Délègue à un sous-générateur
- Utile pour la composition et la récursion
- Rend le code plus lisible

### Avantages principaux

✅ **Efficacité mémoire** : Ne stocke pas toutes les valeurs  
✅ **Performance** : Calcul à la demande  
✅ **Élégance** : Code plus lisible et expressif  
✅ **Flexibilité** : Séquences infinies possibles  
✅ **Pipeline** : Facile à chaîner et composer

### Quand les utiliser ?

- Traitement de fichiers volumineux
- Flux de données continus
- Pipelines de transformation
- Économie de mémoire critique
- Séquences potentiellement infinies

### Points à retenir

- Les générateurs s'épuisent après utilisation
- Pas d'accès par index ou `len()`
- Utiliser `list()` uniquement si nécessaire
- Le module `itertools` offre des outils puissants
- Toujours documenter les générateurs

Les générateurs sont un outil essentiel pour écrire du code Python performant et élégant, particulièrement pour le traitement de grandes quantités de données !

Dans le prochain chapitre, nous explorerons les closures et la programmation fonctionnelle, pour compléter notre maîtrise des concepts avancés de Python.

⏭️ [Closures et programmation fonctionnelle](/05-programmation-fonctionnelle/05-closures-et-prog-fonctionnelle.md)
