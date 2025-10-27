🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.2 map(), filter(), reduce()

## Introduction

Dans le chapitre précédent, nous avons découvert les fonctions lambda et les fonctions d'ordre supérieur. Maintenant, nous allons explorer trois fonctions d'ordre supérieur très puissantes intégrées à Python : `map()`, `filter()` et `reduce()`.

Ces fonctions permettent de traiter des collections de données (listes, tuples, etc.) de manière élégante et concise. Elles sont au cœur de la programmation fonctionnelle en Python.

---

## La fonction map()

### Qu'est-ce que map() ?

La fonction `map()` **applique une fonction à chaque élément** d'une séquence (liste, tuple, etc.) et retourne un itérateur avec les résultats transformés.

### Syntaxe

```python
map(fonction, iterable)
```

- `fonction` : la fonction à appliquer à chaque élément
- `iterable` : la séquence à traiter (liste, tuple, etc.)

### Exemple de base : doubler des nombres

**Approche classique avec une boucle :**

```python
nombres = [1, 2, 3, 4, 5]
nombres_doubles = []

for nombre in nombres:
    nombres_doubles.append(nombre * 2)

print(nombres_doubles)  # [2, 4, 6, 8, 10]
```

**Avec map() :**

```python
nombres = [1, 2, 3, 4, 5]
nombres_doubles = list(map(lambda x: x * 2, nombres))

print(nombres_doubles)  # [2, 4, 6, 8, 10]
```

> **Note importante** : `map()` retourne un objet map (un itérateur), il faut le convertir en liste avec `list()` pour voir les résultats.

### Exemples pratiques

#### Exemple 1 : Convertir des températures

```python
# Convertir des Celsius en Fahrenheit
temperatures_celsius = [0, 10, 20, 30, 40]

celsius_vers_fahrenheit = lambda c: (c * 9/5) + 32

temperatures_fahrenheit = list(map(celsius_vers_fahrenheit, temperatures_celsius))

print(f"Celsius : {temperatures_celsius}")
print(f"Fahrenheit : {temperatures_fahrenheit}")
# Fahrenheit : [32.0, 50.0, 68.0, 86.0, 104.0]
```

#### Exemple 2 : Mettre des chaînes en majuscules

```python
mots = ["python", "javascript", "java", "ruby"]

mots_majuscules = list(map(str.upper, mots))

print(mots_majuscules)  # ['PYTHON', 'JAVASCRIPT', 'JAVA', 'RUBY']
```

> **Astuce** : On peut passer directement une méthode comme `str.upper` sans lambda !

#### Exemple 3 : Calculer la longueur de plusieurs chaînes

```python
phrases = ["Bonjour", "Comment allez-vous ?", "Python", "Programmation"]

longueurs = list(map(len, phrases))

print(longueurs)  # [7, 19, 6, 13]
```

#### Exemple 4 : Formatter des données

```python
prenoms = ["alice", "bob", "charlie"]

# Capitaliser la première lettre
prenoms_formatte = list(map(lambda nom: nom.capitalize(), prenoms))

print(prenoms_formatte)  # ['Alice', 'Bob', 'Charlie']
```

### map() avec plusieurs itérables

On peut passer **plusieurs listes** à `map()`. La fonction recevra alors un élément de chaque liste :

```python
nombres1 = [1, 2, 3, 4]
nombres2 = [10, 20, 30, 40]

# Additionner les éléments correspondants
sommes = list(map(lambda x, y: x + y, nombres1, nombres2))

print(sommes)  # [11, 22, 33, 44]
```

Autre exemple :

```python
prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Créer des phrases descriptives
descriptions = list(map(
    lambda nom, age: f"{nom} a {age} ans",
    prenoms,
    ages
))

for desc in descriptions:
    print(desc)
# Alice a 25 ans
# Bob a 30 ans
# Charlie a 35 ans
```

---

## La fonction filter()

### Qu'est-ce que filter() ?

La fonction `filter()` **filtre les éléments** d'une séquence en ne gardant que ceux qui satisfont une condition (retournent `True`).

### Syntaxe

```python
filter(fonction_condition, iterable)
```

- `fonction_condition` : une fonction qui retourne `True` ou `False`
- `iterable` : la séquence à filtrer

### Exemple de base : filtrer les nombres pairs

**Approche classique avec une boucle :**

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = []

for nombre in nombres:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)

print(nombres_pairs)  # [2, 4, 6, 8, 10]
```

**Avec filter() :**

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))

print(nombres_pairs)  # [2, 4, 6, 8, 10]
```

### Exemples pratiques

#### Exemple 1 : Filtrer les nombres positifs

```python
nombres = [-5, 3, -2, 8, -1, 0, 7, -9]

positifs = list(filter(lambda x: x > 0, nombres))

print(positifs)  # [3, 8, 7]
```

#### Exemple 2 : Filtrer les chaînes longues

```python
mots = ["chat", "chien", "éléphant", "oiseau", "papillon", "rat"]

# Garder seulement les mots de plus de 5 lettres
mots_longs = list(filter(lambda mot: len(mot) > 5, mots))

print(mots_longs)  # ['éléphant', 'oiseau', 'papillon']
```

#### Exemple 3 : Filtrer des dictionnaires

```python
produits = [
    {"nom": "Pomme", "prix": 2.5},
    {"nom": "Banane", "prix": 1.8},
    {"nom": "Mangue", "prix": 5.2},
    {"nom": "Orange", "prix": 3.0},
]

# Produits à moins de 3€
produits_pas_chers = list(filter(lambda p: p["prix"] < 3, produits))

print("Produits à moins de 3€ :")
for p in produits_pas_chers:
    print(f"  - {p['nom']}: {p['prix']}€")
# Pomme: 2.5€
# Banane: 1.8€
```

#### Exemple 4 : Filtrer les chaînes non vides

```python
textes = ["Bonjour", "", "Python", "   ", "Monde", ""]

# Supprimer les chaînes vides ou ne contenant que des espaces
textes_valides = list(filter(lambda t: t.strip() != "", textes))

print(textes_valides)  # ['Bonjour', 'Python', 'Monde']
```

#### Exemple 5 : Filtrer avec une fonction personnalisée

```python
def est_adulte(personne):
    """Vérifie si une personne est majeure."""
    return personne["age"] >= 18

personnes = [
    {"nom": "Alice", "age": 25},
    {"nom": "Bob", "age": 17},
    {"nom": "Charlie", "age": 30},
    {"nom": "David", "age": 16},
]

adultes = list(filter(est_adulte, personnes))

print("Adultes :")
for p in adultes:
    print(f"  - {p['nom']} ({p['age']} ans)")
# Alice (25 ans)
# Charlie (30 ans)
```

---

## La fonction reduce()

### Qu'est-ce que reduce() ?

La fonction `reduce()` **réduit une séquence à une seule valeur** en appliquant de manière cumulative une fonction sur les éléments.

> **Important** : `reduce()` n'est pas une fonction native de Python. Elle doit être importée depuis le module `functools`.

### Syntaxe

```python
from functools import reduce

reduce(fonction, iterable[, valeur_initiale])
```

- `fonction` : une fonction qui prend 2 arguments (accumulateur, élément actuel)
- `iterable` : la séquence à réduire
- `valeur_initiale` : (optionnel) valeur de départ pour l'accumulateur

### Comment fonctionne reduce() ?

`reduce()` applique la fonction de manière itérative :

1. Applique la fonction aux deux premiers éléments
2. Applique la fonction au résultat et au troisième élément
3. Continue jusqu'à épuiser tous les éléments

### Exemple de base : somme de nombres

**Approche classique avec une boucle :**

```python
nombres = [1, 2, 3, 4, 5]
somme = 0

for nombre in nombres:
    somme = somme + nombre

print(somme)  # 15
```

**Avec reduce() :**

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

somme = reduce(lambda acc, x: acc + x, nombres)

print(somme)  # 15
```

**Explication du processus :**
```
Étape 1 : 1 + 2 = 3
Étape 2 : 3 + 3 = 6
Étape 3 : 6 + 4 = 10
Étape 4 : 10 + 5 = 15
```

### Exemples pratiques

#### Exemple 1 : Produit de nombres

```python
from functools import reduce

nombres = [2, 3, 4, 5]

produit = reduce(lambda acc, x: acc * x, nombres)

print(f"Produit : {produit}")  # 2 * 3 * 4 * 5 = 120
```

#### Exemple 2 : Trouver le maximum

```python
from functools import reduce

nombres = [45, 12, 89, 34, 67, 23]

maximum = reduce(lambda acc, x: acc if acc > x else x, nombres)

print(f"Maximum : {maximum}")  # 89
```

> **Note** : Pour trouver le maximum, il est plus simple d'utiliser `max(nombres)`, mais cet exemple illustre le fonctionnement de `reduce()`.

#### Exemple 3 : Concaténer des chaînes

```python
from functools import reduce

mots = ["Python", "est", "génial"]

phrase = reduce(lambda acc, mot: acc + " " + mot, mots)

print(phrase)  # Python est génial
```

Avec une valeur initiale :

```python
from functools import reduce

mots = ["Python", "est", "génial"]

phrase = reduce(lambda acc, mot: acc + " " + mot, mots, "Langage:")

print(phrase)  # Langage: Python est génial
```

#### Exemple 4 : Compter les occurrences

```python
from functools import reduce

fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

compteur = reduce(
    lambda acc, fruit: {**acc, fruit: acc.get(fruit, 0) + 1},
    fruits,
    {}
)

print(compteur)  # {'pomme': 3, 'banane': 2, 'orange': 1}
```

#### Exemple 5 : Aplatir une liste de listes

```python
from functools import reduce

listes = [[1, 2], [3, 4], [5, 6], [7, 8]]

liste_aplatie = reduce(lambda acc, liste: acc + liste, listes)

print(liste_aplatie)  # [1, 2, 3, 4, 5, 6, 7, 8]
```

#### Exemple 6 : Calculer une factorielle

```python
from functools import reduce

def factorielle(n):
    """Calcule la factorielle de n."""
    if n == 0 or n == 1:
        return 1
    return reduce(lambda acc, x: acc * x, range(1, n + 1))

print(f"5! = {factorielle(5)}")  # 5! = 120
print(f"7! = {factorielle(7)}")  # 7! = 5040
```

---

## Combiner map(), filter() et reduce()

La vraie puissance de ces fonctions apparaît quand on les combine !

### Exemple 1 : Somme des carrés des nombres pairs

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Étape 1 : Filtrer les nombres pairs
pairs = filter(lambda x: x % 2 == 0, nombres)

# Étape 2 : Calculer le carré de chaque nombre
carres = map(lambda x: x ** 2, pairs)

# Étape 3 : Faire la somme
resultat = reduce(lambda acc, x: acc + x, carres)

print(f"Somme des carrés des pairs : {resultat}")
# 2² + 4² + 6² + 8² + 10² = 4 + 16 + 36 + 64 + 100 = 220
```

Ou de manière plus compacte :

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultat = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, nombres))
)

print(f"Somme des carrés des pairs : {resultat}")  # 220
```

### Exemple 2 : Prix total des produits en promotion

```python
from functools import reduce

produits = [
    {"nom": "Ordinateur", "prix": 800, "en_promo": True},
    {"nom": "Souris", "prix": 25, "en_promo": False},
    {"nom": "Clavier", "prix": 75, "en_promo": True},
    {"nom": "Écran", "prix": 300, "en_promo": True},
    {"nom": "Webcam", "prix": 50, "en_promo": False},
]

# Filtrer les produits en promotion
produits_promo = filter(lambda p: p["en_promo"], produits)

# Extraire les prix
prix = map(lambda p: p["prix"], produits_promo)

# Calculer le total
total = reduce(lambda acc, prix: acc + prix, prix, 0)

print(f"Prix total des produits en promotion : {total}€")  # 1175€
```

### Exemple 3 : Moyenne des notes supérieures à 10

```python
from functools import reduce

notes = [8, 15, 12, 9, 18, 14, 7, 16, 11]

# Filtrer les notes > 10
notes_valides = list(filter(lambda x: x > 10, notes))

# Calculer la somme
somme = reduce(lambda acc, x: acc + x, notes_valides)

# Calculer la moyenne
moyenne = somme / len(notes_valides)

print(f"Notes > 10 : {notes_valides}")
print(f"Moyenne : {moyenne:.2f}")  # Moyenne : 14.33
```

---

## Comparaison avec les compréhensions de listes

Python offre aussi les **compréhensions de listes** qui peuvent remplacer `map()` et `filter()` de manière plus pythonique.

### map() vs compréhension de liste

```python
nombres = [1, 2, 3, 4, 5]

# Avec map()
doubles_map = list(map(lambda x: x * 2, nombres))

# Avec compréhension de liste
doubles_comp = [x * 2 for x in nombres]

print(doubles_map)  # [2, 4, 6, 8, 10]
print(doubles_comp)  # [2, 4, 6, 8, 10]
```

### filter() vs compréhension de liste

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec filter()
pairs_filter = list(filter(lambda x: x % 2 == 0, nombres))

# Avec compréhension de liste
pairs_comp = [x for x in nombres if x % 2 == 0]

print(pairs_filter)  # [2, 4, 6, 8, 10]
print(pairs_comp)    # [2, 4, 6, 8, 10]
```

### map() + filter() vs compréhension de liste

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec map() et filter()
resultat_func = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, nombres)
))

# Avec compréhension de liste
resultat_comp = [x ** 2 for x in nombres if x % 2 == 0]

print(resultat_func)  # [4, 16, 36, 64, 100]
print(resultat_comp)  # [4, 16, 36, 64, 100]
```

### Quand utiliser quoi ?

**Utilisez les compréhensions de listes quand :**
- ✅ L'opération est simple et lisible
- ✅ Vous travaillez avec une seule séquence
- ✅ Vous voulez un code plus "pythonique"

**Utilisez map()/filter() quand :**
- ✅ Vous avez déjà une fonction définie
- ✅ Vous travaillez avec plusieurs séquences en parallèle
- ✅ Vous voulez un style plus fonctionnel

**Utilisez reduce() quand :**
- ✅ Vous devez agréger/réduire une séquence à une valeur
- ✅ Il n'y a pas d'alternative plus simple (comme `sum()`, `max()`, etc.)

---

## Cas d'usage avancés

### Exemple 1 : Pipeline de traitement de données

```python
from functools import reduce

# Données brutes
ventes = [
    {"produit": "Laptop", "quantite": 2, "prix_unitaire": 800},
    {"produit": "Souris", "quantite": 5, "prix_unitaire": 25},
    {"produit": "Clavier", "quantite": 3, "prix_unitaire": 75},
    {"produit": "Écran", "quantite": 1, "prix_unitaire": 300},
]

# Pipeline de traitement
def traiter_ventes(ventes):
    # 1. Calculer le montant total de chaque vente
    avec_montants = list(map(
        lambda v: {**v, "montant_total": v["quantite"] * v["prix_unitaire"]},
        ventes
    ))

    # 2. Filtrer les ventes de plus de 200€
    ventes_importantes = list(filter(
        lambda v: v["montant_total"] > 200,
        avec_montants
    ))

    # 3. Calculer le chiffre d'affaires total
    ca_total = reduce(
        lambda acc, v: acc + v["montant_total"],
        ventes_importantes,
        0
    )

    return ventes_importantes, ca_total

ventes_importantes, ca = traiter_ventes(ventes)

print("Ventes importantes (>200€) :")
for v in ventes_importantes:
    print(f"  {v['produit']}: {v['montant_total']}€")
print(f"\nChiffre d'affaires : {ca}€")
```

### Exemple 2 : Transformation de données structurées

```python
# Données d'étudiants
etudiants = [
    {"nom": "Alice", "notes": [15, 18, 16]},
    {"nom": "Bob", "notes": [12, 14, 13]},
    {"nom": "Charlie", "notes": [17, 19, 18]},
]

# Calculer la moyenne de chaque étudiant
etudiants_avec_moyennes = list(map(
    lambda e: {
        "nom": e["nom"],
        "notes": e["notes"],
        "moyenne": sum(e["notes"]) / len(e["notes"])
    },
    etudiants
))

# Filtrer ceux qui ont la moyenne >= 15
mentions_bien = list(filter(
    lambda e: e["moyenne"] >= 15,
    etudiants_avec_moyennes
))

print("Étudiants avec mention Bien (>=15) :")
for e in mentions_bien:
    print(f"  {e['nom']}: {e['moyenne']:.2f}")
```

### Exemple 3 : Analyse de texte

```python
from functools import reduce

texte = "Python est un langage de programmation puissant et facile à apprendre"

# Compter le nombre total de caractères (sans espaces)
mots = texte.split()

# Extraire la longueur de chaque mot
longueurs = list(map(len, mots))

# Calculer la longueur totale
longueur_totale = reduce(lambda acc, x: acc + x, longueurs)

# Calculer la longueur moyenne
longueur_moyenne = longueur_totale / len(mots)

print(f"Nombre de mots : {len(mots)}")
print(f"Longueur totale : {longueur_totale} caractères")
print(f"Longueur moyenne : {longueur_moyenne:.2f} caractères/mot")
```

---

## Performances et optimisation

### Les itérateurs sont paresseux (lazy)

`map()` et `filter()` retournent des **itérateurs**, pas des listes. Cela signifie que les calculs ne sont effectués que lorsque nécessaire.

```python
nombres = range(1, 1000000)  # 1 million de nombres

# Ceci est instantané (pas de calcul)
doubles = map(lambda x: x * 2, nombres)

# Le calcul n'a lieu que quand on convertit en liste
# liste_doubles = list(doubles)  # Ceci prendrait du temps
```

### Quand utiliser list() ?

```python
nombres = [1, 2, 3, 4, 5]

# ❌ Pas besoin de list() si on itère une seule fois
for n in map(lambda x: x * 2, nombres):
    print(n)

# ✅ Utilisez list() si vous devez :
# - Réutiliser le résultat
# - Accéder à des éléments spécifiques
# - Connaître la longueur
doubles = list(map(lambda x: x * 2, nombres))
print(len(doubles))  # Nécessite une liste
print(doubles[2])    # Nécessite une liste
```

---

## Alternatives natives de Python

Python propose des alternatives souvent plus simples pour certains cas :

### sum() au lieu de reduce() pour les sommes

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

# Avec reduce()
somme_reduce = reduce(lambda acc, x: acc + x, nombres)

# Plus simple et plus rapide
somme_native = sum(nombres)

print(somme_reduce)  # 15
print(somme_native)  # 15
```

### max() et min() au lieu de reduce()

```python
from functools import reduce

nombres = [45, 12, 89, 34, 67]

# Avec reduce()
max_reduce = reduce(lambda acc, x: acc if acc > x else x, nombres)

# Plus simple et plus rapide
max_native = max(nombres)

print(max_reduce)  # 89
print(max_native)  # 89
```

### any() et all() pour les conditions

```python
nombres = [2, 4, 6, 8, 10]

# Vérifier si tous les nombres sont pairs
tous_pairs = all(map(lambda x: x % 2 == 0, nombres))

# Ou plus simple avec compréhension
tous_pairs = all(x % 2 == 0 for x in nombres)

print(tous_pairs)  # True
```

---

## Bonnes pratiques

### 1. Privilégiez la lisibilité

```python
# ❌ Difficile à lire
resultat = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, map(lambda x: x + 1, range(10)))))

# ✅ Plus clair avec des étapes
nombres = range(10)
increments = map(lambda x: x + 1, nombres)
pairs = filter(lambda x: x % 2 == 0, increments)
doubles = map(lambda x: x * 2, pairs)
resultat = list(doubles)

# ✅✅ Encore mieux avec compréhension
resultat = [2 * (x + 1) for x in range(10) if (x + 1) % 2 == 0]
```

### 2. Utilisez des fonctions nommées pour la clarté

```python
def calculer_montant_tva(prix, taux_tva=0.20):
    """Calcule le montant TTC."""
    return prix * (1 + taux_tva)

prix_ht = [100, 200, 150, 300]

# ✅ Clair et réutilisable
prix_ttc = list(map(calculer_montant_tva, prix_ht))

# ❌ Moins clair avec lambda
prix_ttc = list(map(lambda p: p * 1.20, prix_ht))
```

### 3. N'abusez pas de reduce()

```python
nombres = [1, 2, 3, 4, 5]

# ❌ Compliqué avec reduce()
from functools import reduce
somme = reduce(lambda acc, x: acc + x, nombres)

# ✅ Simple et clair
somme = sum(nombres)
```

### 4. Considérez les compréhensions de listes

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec map/filter (style fonctionnel)
resultat = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nombres)))

# Avec compréhension (style pythonique)
resultat = [x ** 2 for x in nombres if x % 2 == 0]

# Les deux sont corrects, choisissez selon votre préférence
```

---

## Résumé

Dans ce chapitre, nous avons exploré trois fonctions fondamentales de la programmation fonctionnelle :

### map()
- **Objectif** : Transformer chaque élément d'une séquence
- **Syntaxe** : `map(fonction, iterable)`
- **Retourne** : Un itérateur (convertir avec `list()` si nécessaire)
- **Usage** : Appliquer une même opération à tous les éléments

### filter()
- **Objectif** : Filtrer les éléments selon une condition
- **Syntaxe** : `filter(fonction_condition, iterable)`
- **Retourne** : Un itérateur avec les éléments qui satisfont la condition
- **Usage** : Sélectionner certains éléments d'une séquence

### reduce()
- **Objectif** : Réduire une séquence à une seule valeur
- **Syntaxe** : `reduce(fonction, iterable[, valeur_initiale])`
- **Import** : `from functools import reduce`
- **Usage** : Agréger, accumuler, combiner des éléments

### Points clés à retenir

✅ Ces fonctions permettent un style de programmation fonctionnel
✅ Elles peuvent être combinées pour créer des pipelines de traitement
✅ Les compréhensions de listes sont souvent plus pythoniques
✅ Privilégiez toujours la lisibilité du code
✅ Utilisez les alternatives natives quand elles existent (`sum()`, `max()`, etc.)

### Quand les utiliser ?

- **map()** : Transformation de données, conversion de formats
- **filter()** : Sélection, validation, nettoyage de données
- **reduce()** : Agrégation, calculs cumulatifs (avec parcimonie)

Dans le prochain chapitre, nous explorerons les décorateurs avancés, une autre facette puissante de la programmation fonctionnelle en Python !

⏭️ [Décorateurs avancés](/05-programmation-fonctionnelle/03-decorateurs-avances.md)
