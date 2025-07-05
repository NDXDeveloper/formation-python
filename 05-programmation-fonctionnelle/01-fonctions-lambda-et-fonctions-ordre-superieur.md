🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.1 : Fonctions lambda et fonctions d'ordre supérieur

## Introduction

Dans cette section, nous allons découvrir deux concepts fondamentaux de la programmation fonctionnelle : les fonctions lambda et les fonctions d'ordre supérieur. Ces outils vous permettront d'écrire du code plus concis et plus expressif.

## Les fonctions lambda

### Qu'est-ce qu'une fonction lambda ?

Une fonction lambda est une fonction anonyme (sans nom) qui peut être définie en une seule ligne. Elle est particulièrement utile pour créer de petites fonctions simples sans avoir besoin de les nommer.

### Syntaxe de base

```python
lambda arguments: expression
```

**Exemple simple :**
```python
# Fonction normale
def carre(x):
    return x * x

# Fonction lambda équivalente
carre_lambda = lambda x: x * x

# Utilisation
print(carre(5))        # 25
print(carre_lambda(5)) # 25
```

### Pourquoi utiliser les fonctions lambda ?

Les fonctions lambda sont utiles quand vous avez besoin d'une fonction simple et temporaire. Elles rendent le code plus lisible en évitant de définir des fonctions séparées pour des opérations simples.

## Exemples pratiques de fonctions lambda

### 1. Fonctions lambda avec un seul paramètre

```python
# Doubler un nombre
doubler = lambda x: x * 2
print(doubler(4))  # 8

# Vérifier si un nombre est pair
est_pair = lambda x: x % 2 == 0
print(est_pair(4))  # True
print(est_pair(5))  # False

# Calculer la longueur d'une chaîne
longueur = lambda s: len(s)
print(longueur("Python"))  # 6
```

### 2. Fonctions lambda avec plusieurs paramètres

```python
# Addition de deux nombres
additionner = lambda x, y: x + y
print(additionner(3, 5))  # 8

# Calculer l'aire d'un rectangle
aire_rectangle = lambda longueur, largeur: longueur * largeur
print(aire_rectangle(4, 3))  # 12

# Trouver le maximum de trois nombres
max_trois = lambda a, b, c: max(a, b, c)
print(max_trois(10, 25, 7))  # 25
```

### 3. Fonctions lambda avec des conditions

```python
# Valeur absolue
valeur_absolue = lambda x: x if x >= 0 else -x
print(valeur_absolue(-5))  # 5
print(valeur_absolue(3))   # 3

# Note avec mention
note_mention = lambda note: "Très bien" if note >= 16 else "Bien" if note >= 12 else "Assez bien" if note >= 10 else "Insuffisant"
print(note_mention(17))  # Très bien
print(note_mention(8))   # Insuffisant
```

## Les fonctions d'ordre supérieur

### Qu'est-ce qu'une fonction d'ordre supérieur ?

Une fonction d'ordre supérieur est une fonction qui :
- Prend une ou plusieurs fonctions comme paramètres, ET/OU
- Retourne une fonction comme résultat

### Exemple 1 : Fonction qui prend une fonction comme paramètre

```python
def appliquer_operation(liste, operation):
    """Applique une opération à chaque élément d'une liste"""
    resultat = []
    for element in liste:
        resultat.append(operation(element))
    return resultat

# Utilisation avec des fonctions lambda
nombres = [1, 2, 3, 4, 5]

# Doubler chaque nombre
doubles = appliquer_operation(nombres, lambda x: x * 2)
print(doubles)  # [2, 4, 6, 8, 10]

# Calculer le carré de chaque nombre
carres = appliquer_operation(nombres, lambda x: x ** 2)
print(carres)  # [1, 4, 9, 16, 25]
```

### Exemple 2 : Fonction qui retourne une fonction

```python
def creer_multiplicateur(facteur):
    """Crée une fonction qui multiplie par le facteur donné"""
    return lambda x: x * facteur

# Créer différents multiplicateurs
multiplier_par_2 = creer_multiplicateur(2)
multiplier_par_10 = creer_multiplicateur(10)

# Utilisation
print(multiplier_par_2(5))   # 10
print(multiplier_par_10(3))  # 30
```

### Exemple 3 : Fonction qui prend ET retourne une fonction

```python
def creer_validateur(condition):
    """Crée une fonction de validation basée sur une condition"""
    def validateur(liste):
        return [x for x in liste if condition(x)]
    return validateur

# Créer des validateurs
valider_pairs = creer_validateur(lambda x: x % 2 == 0)
valider_positifs = creer_validateur(lambda x: x > 0)

nombres = [-2, -1, 0, 1, 2, 3, 4, 5]

print(valider_pairs(nombres))     # [-2, 0, 2, 4]
print(valider_positifs(nombres))  # [1, 2, 3, 4, 5]
```

## Cas d'usage pratiques

### 1. Tri personnalisé avec `sorted()`

```python
# Liste d'étudiants avec leurs notes
etudiants = [
    ("Alice", 15),
    ("Bob", 12),
    ("Charlie", 18),
    ("Diana", 16)
]

# Trier par note (croissant)
par_note = sorted(etudiants, key=lambda etudiant: etudiant[1])
print(par_note)
# [('Bob', 12), ('Alice', 15), ('Diana', 16), ('Charlie', 18)]

# Trier par nom alphabétique
par_nom = sorted(etudiants, key=lambda etudiant: etudiant[0])
print(par_nom)
# [('Alice', 15), ('Bob', 12), ('Charlie', 18), ('Diana', 16)]
```

### 2. Avec la fonction `max()` et `min()`

```python
mots = ["Python", "Java", "C++", "JavaScript", "Go"]

# Mot le plus long
plus_long = max(mots, key=lambda mot: len(mot))
print(plus_long)  # JavaScript

# Mot le plus court
plus_court = min(mots, key=lambda mot: len(mot))
print(plus_court)  # Go
```

### 3. Transformation de données

```python
# Liste de températures en Celsius
temperatures_celsius = [0, 10, 20, 30, 40]

# Convertir en Fahrenheit
celsius_vers_fahrenheit = lambda c: (c * 9/5) + 32
temperatures_fahrenheit = [celsius_vers_fahrenheit(temp) for temp in temperatures_celsius]
print(temperatures_fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

## Bonnes pratiques et limitations

### ✅ Bonnes pratiques

1. **Utilisez les lambda pour des opérations simples** (une seule expression)
2. **Gardez-les courtes et lisibles**
3. **Utilisez-les avec les fonctions intégrées** comme `map()`, `filter()`, `sorted()`
4. **Privilégiez la lisibilité** : si la lambda devient complexe, créez une fonction normale

### ❌ À éviter

1. **Fonctions lambda trop complexes** :
```python
# Évitez ceci
complexe = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0

# Préférez ceci
def traiter_nombre(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    else:
        return 0
```

2. **Assigner des lambda à des variables** quand une fonction normale serait plus claire :
```python
# Évitez ceci
calculer = lambda x, y: x * y + x / y

# Préférez ceci
def calculer(x, y):
    return x * y + x / y
```

## Exercices pratiques

### Exercice 1 : Fonctions lambda de base
Créez des fonctions lambda pour :
1. Calculer le cube d'un nombre
2. Vérifier si un nombre est négatif
3. Concaténer deux chaînes avec un espace entre elles

```python
# Vos solutions :
cube = lambda x: x ** 3
est_negatif = lambda x: x < 0
concat_avec_espace = lambda a, b: a + " " + b

# Tests
print(cube(3))  # 27
print(est_negatif(-5))  # True
print(concat_avec_espace("Bonjour", "monde"))  # Bonjour monde
```

### Exercice 2 : Fonctions d'ordre supérieur
Créez une fonction qui prend une liste de nombres et une fonction, puis applique cette fonction à chaque nombre :

```python
def transformer_liste(liste, fonction):
    return [fonction(x) for x in liste]

# Test
nombres = [1, 2, 3, 4, 5]
result = transformer_liste(nombres, lambda x: x * 3)
print(result)  # [3, 6, 9, 12, 15]
```

### Exercice 3 : Tri avancé
Triez cette liste de dictionnaires par âge décroissant :

```python
personnes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35}
]

# Solution
personnes_triees = sorted(personnes, key=lambda p: p["age"], reverse=True)
print(personnes_triees)
# [{'nom': 'Charlie', 'age': 35}, {'nom': 'Alice', 'age': 30}, {'nom': 'Bob', 'age': 25}]
```

## Résumé

Les fonctions lambda et les fonctions d'ordre supérieur sont des outils puissants qui permettent :

- **Fonctions lambda** : Créer des fonctions anonymes courtes pour des opérations simples
- **Fonctions d'ordre supérieur** : Créer des fonctions flexibles et réutilisables qui travaillent avec d'autres fonctions

Ces concepts préparent le terrain pour les sections suivantes où nous verrons `map()`, `filter()`, et `reduce()` qui utilisent intensivement ces principes.

Dans la prochaine section, nous découvrirons comment utiliser ces concepts avec les fonctions intégrées de Python pour manipuler des collections de données de manière élégante et efficace.

⏭️
