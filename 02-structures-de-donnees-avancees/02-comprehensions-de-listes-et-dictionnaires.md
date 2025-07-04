🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.2 : Compréhensions de listes et dictionnaires

## Introduction

Les compréhensions (ou "comprehensions" en anglais) sont une façon élégante et concise d'écrire en Python. Elles permettent de créer des listes, des dictionnaires et d'autres structures de données en une seule ligne de code, de manière plus lisible et souvent plus rapide que les boucles traditionnelles.

## Compréhensions de listes

### Syntaxe de base

La syntaxe générale d'une compréhension de liste est :
```python
nouvelle_liste = [expression for element in iterable]
```

### Exemple simple

Au lieu d'écrire :
```python
# Méthode traditionnelle avec une boucle
nombres = [1, 2, 3, 4, 5]
carres = []
for nombre in nombres:
    carres.append(nombre ** 2)
print(carres)  # [1, 4, 9, 16, 25]
```

Vous pouvez écrire :
```python
# Avec une compréhension de liste
nombres = [1, 2, 3, 4, 5]
carres = [nombre ** 2 for nombre in nombres]
print(carres)  # [1, 4, 9, 16, 25]
```

### Compréhensions avec conditions

Vous pouvez ajouter des conditions avec `if` :
```python
# Filtrer les nombres pairs et les mettre au carré
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres_pairs = [nombre ** 2 for nombre in nombres if nombre % 2 == 0]
print(carres_pairs)  # [4, 16, 36, 64, 100]
```

### Exemples pratiques

#### Transformer des chaînes de caractères
```python
# Convertir en majuscules
mots = ["python", "est", "génial"]
mots_majuscules = [mot.upper() for mot in mots]
print(mots_majuscules)  # ['PYTHON', 'EST', 'GÉNIAL']

# Obtenir la longueur de chaque mot
longueurs = [len(mot) for mot in mots]
print(longueurs)  # [6, 3, 6]
```

#### Travailler avec des nombres
```python
# Créer une liste de nombres pairs de 0 à 20
pairs = [x for x in range(21) if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Température : convertir Celsius en Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Compréhensions imbriquées

Vous pouvez créer des listes à partir de listes de listes :
```python
# Aplatir une liste de listes
liste_de_listes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
liste_aplatie = [nombre for sous_liste in liste_de_listes for nombre in sous_liste]
print(liste_aplatie)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Compréhensions de dictionnaires

### Syntaxe de base

La syntaxe générale d'une compréhension de dictionnaire est :
```python
nouveau_dict = {cle: valeur for element in iterable}
```

### Exemple simple

Au lieu d'écrire :
```python
# Méthode traditionnelle
nombres = [1, 2, 3, 4, 5]
dict_carres = {}
for nombre in nombres:
    dict_carres[nombre] = nombre ** 2
print(dict_carres)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Vous pouvez écrire :
```python
# Avec une compréhension de dictionnaire
nombres = [1, 2, 3, 4, 5]
dict_carres = {nombre: nombre ** 2 for nombre in nombres}
print(dict_carres)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Exemples pratiques

#### Créer un dictionnaire à partir de deux listes
```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
personnes = {nom: age for nom, age in zip(noms, ages)}
print(personnes)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

#### Transformer les clés et valeurs
```python
# Inverser clés et valeurs
original = {'a': 1, 'b': 2, 'c': 3}
inverse = {valeur: cle for cle, valeur in original.items()}
print(inverse)  # {1: 'a', 2: 'b', 3: 'c'}

# Mettre les clés en majuscules
majuscules = {cle.upper(): valeur for cle, valeur in original.items()}
print(majuscules)  # {'A': 1, 'B': 2, 'C': 3}
```

#### Filtrer un dictionnaire
```python
# Garder seulement les valeurs supérieures à 2
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 91, 'David': 68}
bons_scores = {nom: score for nom, score in scores.items() if score > 80}
print(bons_scores)  # {'Alice': 85, 'Charlie': 91}
```

## Compréhensions d'ensembles (sets)

Vous pouvez aussi créer des ensembles avec des compréhensions :
```python
# Créer un ensemble des carrés des nombres pairs
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres_pairs = {nombre ** 2 for nombre in nombres if nombre % 2 == 0}
print(carres_pairs)  # {64, 4, 36, 16, 100}
```

## Exercices pratiques

### Exercice 1 : Compréhensions de listes basiques
```python
# 1. Créez une liste des cubes des nombres de 1 à 10
cubes = [x ** 3 for x in range(1, 11)]
print(cubes)

# 2. Créez une liste des mots de plus de 4 lettres
mots = ["chat", "chien", "oiseau", "poisson", "hamster"]
mots_longs = [mot for mot in mots if len(mot) > 4]
print(mots_longs)

# 3. Créez une liste des nombres négatifs d'une liste mixte
nombres_mixtes = [-3, 5, -1, 8, -7, 2, -4]
negatifs = [x for x in nombres_mixtes if x < 0]
print(negatifs)
```

### Exercice 2 : Compréhensions de dictionnaires
```python
# 1. Créez un dictionnaire mot -> longueur
mots = ["python", "programmation", "code", "développement"]
longueurs = {mot: len(mot) for mot in mots}
print(longueurs)

# 2. Créez un dictionnaire des nombres et leurs factorielles (jusqu'à 5)
import math
factorielles = {n: math.factorial(n) for n in range(1, 6)}
print(factorielles)

# 3. Filtrez un dictionnaire pour garder seulement les valeurs paires
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
pairs = {cle: valeur for cle, valeur in original.items() if valeur % 2 == 0}
print(pairs)
```

## Bonnes pratiques

### Lisibilité avant tout
```python
# ✅ Bon : compréhension simple et lisible
nombres_pairs = [x for x in range(10) if x % 2 == 0]

# ❌ Évitez : trop complexe, préférez une boucle classique
resultat = [x**2 + y**2 for x in range(10) for y in range(10) if x > y and x**2 + y**2 < 50]
```

### Utilisez des noms de variables explicites
```python
# ✅ Bon
prix_reduits = [prix * 0.8 for prix in prix_originaux if prix > 100]

# ❌ Moins bon
resultat = [x * 0.8 for x in liste if x > 100]
```

### N'abusez pas des compréhensions imbriquées
```python
# ✅ Bon : compréhension simple
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatie = [element for ligne in matrice for element in ligne]

# ❌ Évitez : trop complexe
resultat = [[x*y for x in range(3)] for y in range(3) if y % 2 == 0]
```

## Comparaison des performances

Les compréhensions sont généralement plus rapides que les boucles équivalentes :

```python
import time

# Méthode avec boucle
start = time.time()
resultat1 = []
for i in range(100000):
    resultat1.append(i ** 2)
temps_boucle = time.time() - start

# Méthode avec compréhension
start = time.time()
resultat2 = [i ** 2 for i in range(100000)]
temps_comprehension = time.time() - start

print(f"Boucle: {temps_boucle:.4f} secondes")
print(f"Compréhension: {temps_comprehension:.4f} secondes")
```

## Résumé

Les compréhensions sont un outil puissant de Python qui permet de :
- Écrire du code plus concis et lisible
- Améliorer les performances dans de nombreux cas
- Créer des listes, dictionnaires et ensembles de manière élégante

**Points clés à retenir :**
- Utilisez les compréhensions pour les opérations simples
- Préférez les boucles classiques pour la logique complexe
- La lisibilité est plus importante que la concision
- Les compréhensions sont souvent plus rapides que les boucles équivalentes

**Syntaxes à mémoriser :**
- Liste : `[expression for element in iterable if condition]`
- Dictionnaire : `{cle: valeur for element in iterable if condition}`
- Ensemble : `{expression for element in iterable if condition}`

⏭️

