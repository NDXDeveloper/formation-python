🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.2 : map(), filter(), reduce()

## Introduction

Dans cette section, nous allons découvrir trois fonctions essentielles de la programmation fonctionnelle en Python : `map()`, `filter()` et `reduce()`. Ces fonctions permettent de traiter des collections de données de manière élégante et efficace, en évitant les boucles traditionnelles.

Ces trois fonctions suivent un principe simple :
- **`map()`** : Transforme chaque élément d'une collection
- **`filter()`** : Sélectionne certains éléments d'une collection selon un critère
- **`reduce()`** : Combine tous les éléments d'une collection en une seule valeur

## La fonction map()

### Qu'est-ce que map() ?

La fonction `map()` applique une fonction à chaque élément d'une collection (liste, tuple, etc.) et retourne un objet map (que l'on convertit généralement en liste).

### Syntaxe

```python
map(fonction, iterable)
```

### Exemple de base

```python
# Méthode traditionnelle avec une boucle
nombres = [1, 2, 3, 4, 5]
carres = []
for nombre in nombres:
    carres.append(nombre ** 2)
print(carres)  # [1, 4, 9, 16, 25]

# Méthode avec map()
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))
print(carres)  # [1, 4, 9, 16, 25]
```

### Exemples pratiques avec map()

#### 1. Transformation de nombres

```python
# Doubler tous les nombres
nombres = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nombres))
print(doubles)  # [2, 4, 6, 8, 10]

# Convertir en valeurs absolues
nombres = [-3, -1, 0, 1, 5]
absolus = list(map(abs, nombres))  # abs est une fonction intégrée
print(absolus)  # [3, 1, 0, 1, 5]

# Arrondir des nombres décimaux
decimaux = [3.7, 2.1, 8.9, 1.2]
arrondis = list(map(round, decimaux))
print(arrondis)  # [4, 2, 9, 1]
```

#### 2. Transformation de chaînes

```python
# Convertir en majuscules
mots = ["python", "java", "javascript"]
majuscules = list(map(str.upper, mots))
print(majuscules)  # ['PYTHON', 'JAVA', 'JAVASCRIPT']

# Calculer la longueur de chaque chaîne
longueurs = list(map(len, mots))
print(longueurs)  # [6, 4, 10]

# Ajouter un préfixe
prefixer = lambda mot: "Langage: " + mot
avec_prefixe = list(map(prefixer, mots))
print(avec_prefixe)  # ['Langage: python', 'Langage: java', 'Langage: javascript']
```

#### 3. Utilisation avec plusieurs itérables

```python
# Additionner deux listes élément par élément
liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]
sommes = list(map(lambda x, y: x + y, liste1, liste2))
print(sommes)  # [11, 22, 33, 44]

# Calculer la puissance
bases = [2, 3, 4, 5]
exposants = [1, 2, 3, 4]
puissances = list(map(lambda b, e: b ** e, bases, exposants))
print(puissances)  # [2, 9, 64, 625]
```

## La fonction filter()

### Qu'est-ce que filter() ?

La fonction `filter()` sélectionne les éléments d'une collection qui satisfont une condition donnée (fonction qui retourne True ou False).

### Syntaxe

```python
filter(fonction_condition, iterable)
```

### Exemple de base

```python
# Méthode traditionnelle avec une boucle
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []
for nombre in nombres:
    if nombre % 2 == 0:
        pairs.append(nombre)
print(pairs)  # [2, 4, 6, 8, 10]

# Méthode avec filter()
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4, 6, 8, 10]
```

### Exemples pratiques avec filter()

#### 1. Filtrage de nombres

```python
nombres = [-5, -2, 0, 3, 7, -1, 8, 12]

# Nombres positifs
positifs = list(filter(lambda x: x > 0, nombres))
print(positifs)  # [3, 7, 8, 12]

# Nombres supérieurs à 5
superieurs_5 = list(filter(lambda x: x > 5, nombres))
print(superieurs_5)  # [7, 8, 12]

# Nombres impairs
impairs = list(filter(lambda x: x % 2 != 0, nombres))
print(impairs)  # [-5, 3, 7, -1]
```

#### 2. Filtrage de chaînes

```python
mots = ["python", "java", "html", "css", "javascript", "go"]

# Mots de plus de 4 caractères
mots_longs = list(filter(lambda mot: len(mot) > 4, mots))
print(mots_longs)  # ['python', 'javascript']

# Mots commençant par 'j'
mots_j = list(filter(lambda mot: mot.startswith('j'), mots))
print(mots_j)  # ['java', 'javascript']

# Mots contenant 'a'
mots_avec_a = list(filter(lambda mot: 'a' in mot, mots))
print(mots_avec_a)  # ['java', 'javascript']
```

#### 3. Filtrage d'objets complexes

```python
# Liste d'étudiants avec leurs notes
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 17},
    {"nom": "Diana", "note": 12}
]

# Étudiants ayant réussi (note >= 10)
reussis = list(filter(lambda e: e["note"] >= 10, etudiants))
print(reussis)
# [{'nom': 'Alice', 'note': 15}, {'nom': 'Charlie', 'note': 17}, {'nom': 'Diana', 'note': 12}]

# Étudiants avec mention (note >= 14)
mentions = list(filter(lambda e: e["note"] >= 14, etudiants))
print(mentions)
# [{'nom': 'Alice', 'note': 15}, {'nom': 'Charlie', 'note': 17}]
```

## La fonction reduce()

### Qu'est-ce que reduce() ?

La fonction `reduce()` applique une fonction de façon cumulative aux éléments d'une collection, de gauche à droite, pour réduire la collection à une seule valeur.

**Important :** `reduce()` doit être importée du module `functools`.

### Syntaxe

```python
from functools import reduce
reduce(fonction, iterable, valeur_initiale_optionnelle)
```

### Exemple de base

```python
from functools import reduce

# Méthode traditionnelle avec une boucle
nombres = [1, 2, 3, 4, 5]
somme = 0
for nombre in nombres:
    somme += nombre
print(somme)  # 15

# Méthode avec reduce()
nombres = [1, 2, 3, 4, 5]
somme = reduce(lambda x, y: x + y, nombres)
print(somme)  # 15
```

### Exemples pratiques avec reduce()

#### 1. Opérations mathématiques

```python
from functools import reduce

nombres = [2, 3, 4, 5]

# Somme
somme = reduce(lambda x, y: x + y, nombres)
print(somme)  # 14

# Produit
produit = reduce(lambda x, y: x * y, nombres)
print(produit)  # 120

# Maximum
maximum = reduce(lambda x, y: x if x > y else y, nombres)
print(maximum)  # 5
# Note : on peut aussi utiliser max(nombres) qui est plus simple
```

#### 2. Avec valeur initiale

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

# Somme avec valeur initiale
somme_avec_init = reduce(lambda x, y: x + y, nombres, 100)
print(somme_avec_init)  # 115 (100 + 15)

# Concaténation de chaînes
mots = ["Python", "est", "génial"]
phrase = reduce(lambda x, y: x + " " + y, mots)
print(phrase)  # "Python est génial"

# Avec valeur initiale pour commencer proprement
phrase_avec_init = reduce(lambda x, y: x + " " + y, mots, "Langage:")
print(phrase_avec_init)  # "Langage: Python est génial"
```

#### 3. Opérations complexes

```python
from functools import reduce

# Compter les occurrences dans une liste
fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

compteur = reduce(
    lambda acc, fruit: {**acc, fruit: acc.get(fruit, 0) + 1},
    fruits,
    {}
)
print(compteur)  # {'pomme': 3, 'banane': 2, 'orange': 1}

# Aplatir une liste de listes
listes = [[1, 2], [3, 4], [5, 6]]
liste_aplatie = reduce(lambda x, y: x + y, listes)
print(liste_aplatie)  # [1, 2, 3, 4, 5, 6]
```

## Combiner map(), filter() et reduce()

### Exemple pratique complet

Imaginons que nous voulons :
1. Filtrer les nombres pairs d'une liste
2. Calculer leur carré
3. Faire la somme de ces carrés

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Méthode traditionnelle
resultat = 0
for nombre in nombres:
    if nombre % 2 == 0:  # Filtrer les pairs
        carre = nombre ** 2  # Calculer le carré
        resultat += carre    # Additionner
print(resultat)  # 220

# Méthode fonctionnelle (étape par étape)
pairs = filter(lambda x: x % 2 == 0, nombres)
carres = map(lambda x: x ** 2, pairs)
somme = reduce(lambda x, y: x + y, carres)
print(somme)  # 220

# Méthode fonctionnelle (en une ligne)
resultat = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nombres))
)
print(resultat)  # 220
```

### Autre exemple : Analyse de données texte

```python
from functools import reduce

# Analyser une liste de phrases
phrases = [
    "Python est formidable",
    "J'aime programmer en Python",
    "Les fonctions lambda sont utiles",
    "La programmation fonctionnelle est puissante"
]

# 1. Récupérer tous les mots
tous_les_mots = reduce(
    lambda acc, phrase: acc + phrase.split(),
    phrases,
    []
)
print(tous_les_mots)

# 2. Filtrer les mots de plus de 5 caractères
mots_longs = list(filter(lambda mot: len(mot) > 5, tous_les_mots))
print(mots_longs)

# 3. Convertir en majuscules
mots_majuscules = list(map(str.upper, mots_longs))
print(mots_majuscules)

# Tout en une fois
resultat_final = list(
    map(str.upper,
        filter(lambda mot: len(mot) > 5,
               reduce(lambda acc, phrase: acc + phrase.split(), phrases, [])
               )
        )
)
print(resultat_final)
```

## Comparaison avec les compréhensions de liste

Les compréhensions de liste peuvent souvent remplacer `map()` et `filter()` de manière plus lisible :

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec map() et filter()
pairs_doubles = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nombres)))

# Avec compréhension de liste (plus lisible)
pairs_doubles = [x * 2 for x in nombres if x % 2 == 0]

print(pairs_doubles)  # [4, 8, 12, 16, 20]
```

## Quand utiliser chaque fonction ?

### Utilisez map() quand :
- Vous voulez transformer chaque élément d'une collection
- La transformation est simple et peut être exprimée en une fonction
- Vous travaillez avec plusieurs itérables en parallèle

### Utilisez filter() quand :
- Vous voulez sélectionner certains éléments selon un critère
- Le critère peut être exprimé par une fonction retournant True/False
- Vous voulez garder la structure originale des éléments

### Utilisez reduce() quand :
- Vous voulez combiner tous les éléments en une seule valeur
- Vous avez besoin d'un calcul cumulatif
- Les fonctions intégrées comme `sum()`, `max()`, `min()` ne suffisent pas

## Exercices pratiques

### Exercice 1 : Utilisation de map()
Vous avez une liste de températures en Celsius. Convertissez-les en Fahrenheit.

```python
temperatures_celsius = [0, 10, 20, 30, 40]

# Formule : F = (C * 9/5) + 32
temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))
print(temperatures_fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Exercice 2 : Utilisation de filter()
Filtrez une liste de mots pour ne garder que ceux qui sont des palindromes.

```python
mots = ["radar", "python", "niveau", "ordinateur", "kayak", "java"]

palindromes = list(filter(lambda mot: mot == mot[::-1], mots))
print(palindromes)  # ['radar', 'niveau', 'kayak']
```

### Exercice 3 : Utilisation de reduce()
Calculez le factoriel d'un nombre en utilisant reduce().

```python
from functools import reduce

def factoriel(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(factoriel(5))  # 120 (5! = 5 * 4 * 3 * 2 * 1)
print(factoriel(0))  # 1
```

### Exercice 4 : Combinaison des trois fonctions
Vous avez une liste de nombres. Trouvez la somme des carrés des nombres impairs.

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution
resultat = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, nombres))
)
print(resultat)  # 165 (1² + 3² + 5² + 7² + 9² = 1 + 9 + 25 + 49 + 81)

# Vérification avec compréhension de liste
verification = sum(x ** 2 for x in nombres if x % 2 != 0)
print(verification)  # 165
```

## Avantages et inconvénients

### ✅ Avantages
- **Code plus concis** : Moins de lignes que les boucles traditionnelles
- **Expressivité** : Le code exprime clairement l'intention
- **Composabilité** : Facile à combiner avec d'autres fonctions
- **Immutabilité** : N'modifie pas les données originales

### ❌ Inconvénients
- **Lisibilité** : Peut être moins lisible pour les débutants
- **Performance** : Peut être plus lent que les boucles pour des opérations simples
- **Débogage** : Plus difficile à déboguer que des boucles explicites
- **Mémoire** : Crée des objets intermédiaires

## Bonnes pratiques

1. **Privilégiez la lisibilité** : Si le code devient trop complexe, utilisez des boucles
2. **Utilisez les compréhensions** : Souvent plus lisibles que map() et filter()
3. **Évitez les reduce() complexes** : Préférez des fonctions nommées pour la logique complexe
4. **Convertissez les objets map/filter** : N'oubliez pas `list()` si vous voulez une liste

## Résumé

- **`map()`** transforme chaque élément d'une collection
- **`filter()`** sélectionne les éléments qui respectent une condition
- **`reduce()`** combine tous les éléments en une seule valeur
- Ces fonctions peuvent être combinées pour créer des pipelines de traitement de données
- Elles sont particulièrement utiles avec les fonctions lambda
- Dans de nombreux cas, les compréhensions de liste sont plus lisibles

Dans la prochaine section, nous découvrirons les décorateurs avancés, qui nous permettront de modifier le comportement des fonctions de manière élégante.

⏭️
