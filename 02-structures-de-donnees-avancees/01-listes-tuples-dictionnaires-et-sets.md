🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.1 : Listes, tuples, dictionnaires et sets

## Introduction

Python propose quatre structures de données fondamentales qui permettent de stocker et organiser des informations de différentes manières. Chacune a ses propres caractéristiques et cas d'usage. Dans cette section, nous allons explorer ces structures en détail avec des exemples pratiques.

## Les Listes

### Qu'est-ce qu'une liste ?

Une liste est une collection **ordonnée** et **modifiable** d'éléments. Elle peut contenir des éléments de différents types et permet les doublons.

```python
# Création d'une liste
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
melange = ["texte", 42, True, 3.14]
liste_vide = []

print(fruits)  # ['pomme', 'banane', 'orange']
```

### Opérations sur les listes

```python
# Accès aux éléments (indexation commence à 0)
fruits = ["pomme", "banane", "orange"]
print(fruits[0])    # pomme
print(fruits[-1])   # orange (dernier élément)

# Modification d'éléments
fruits[1] = "poire"
print(fruits)  # ['pomme', 'poire', 'orange']

# Ajout d'éléments
fruits.append("kiwi")           # Ajoute à la fin
fruits.insert(1, "mangue")      # Insère à la position 1
print(fruits)  # ['pomme', 'mangue', 'poire', 'orange', 'kiwi']

# Suppression d'éléments
fruits.remove("poire")          # Supprime par valeur
element_supprime = fruits.pop() # Supprime et retourne le dernier
print(fruits)  # ['pomme', 'mangue', 'orange']
print(element_supprime)  # kiwi
```

### Découpage (slicing)

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nombres[2:5])    # [2, 3, 4] (de l'index 2 à 4)
print(nombres[:3])     # [0, 1, 2] (du début à l'index 2)
print(nombres[7:])     # [7, 8, 9] (de l'index 7 à la fin)
print(nombres[::2])    # [0, 2, 4, 6, 8] (tous les 2 éléments)
print(nombres[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inversé)
```

### Méthodes utiles des listes

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nombres))      # 8 (longueur)
print(max(nombres))      # 9 (valeur maximale)
print(min(nombres))      # 1 (valeur minimale)
print(sum(nombres))      # 31 (somme)
print(nombres.count(1))  # 2 (nombre d'occurrences de 1)

nombres.sort()           # Trie la liste
print(nombres)           # [1, 1, 2, 3, 4, 5, 6, 9]
```

## Les Tuples

### Qu'est-ce qu'un tuple ?

Un tuple est une collection **ordonnée** et **non modifiable** d'éléments. Une fois créé, on ne peut pas le modifier.

```python
# Création d'un tuple
coordonnees = (3, 4)
couleurs = ("rouge", "vert", "bleu")
tuple_mixte = ("nom", 25, True)
tuple_vide = ()

# Tuple avec un seul élément (attention à la virgule !)
singleton = (42,)  # ou singleton = 42,

print(coordonnees)  # (3, 4)
```

### Opérations sur les tuples

```python
coordonnees = (3, 4, 5)

# Accès aux éléments
print(coordonnees[0])   # 3
print(coordonnees[-1])  # 5

# Déballage (unpacking)
x, y, z = coordonnees
print(f"x={x}, y={y}, z={z}")  # x=3, y=4, z=5

# Les tuples sont immuables
# coordonnees[0] = 10  # Erreur ! TypeError

# Mais on peut créer un nouveau tuple
nouvelles_coordonnees = coordonnees + (6,)
print(nouvelles_coordonnees)  # (3, 4, 5, 6)
```

### Pourquoi utiliser des tuples ?

```python
# Coordonnées géographiques
position = (48.8566, 2.3522)  # Latitude, Longitude de Paris

# Valeur de retour multiple d'une fonction
def calculer_rectangle(longueur, largeur):
    perimetre = 2 * (longueur + largeur)
    aire = longueur * largeur
    return perimetre, aire  # Retourne un tuple

p, a = calculer_rectangle(5, 3)
print(f"Périmètre: {p}, Aire: {a}")  # Périmètre: 16, Aire: 15
```

## Les Dictionnaires

### Qu'est-ce qu'un dictionnaire ?

Un dictionnaire est une collection **non ordonnée** et **modifiable** de paires clé-valeur. Chaque clé doit être unique.

```python
# Création d'un dictionnaire
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Autre façon de créer un dictionnaire
produit = dict(nom="Ordinateur", prix=800, disponible=True)

dictionnaire_vide = {}

print(personne)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

### Opérations sur les dictionnaires

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

# Accès aux valeurs
print(personne["nom"])          # Alice
print(personne.get("age"))      # 25
print(personne.get("pays", "France"))  # France (valeur par défaut)

# Modification et ajout
personne["age"] = 26            # Modification
personne["profession"] = "Développeur"  # Ajout
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris', 'profession': 'Développeur'}

# Suppression
del personne["ville"]           # Supprime la clé "ville"
profession = personne.pop("profession")  # Supprime et retourne la valeur
print(personne)  # {'nom': 'Alice', 'age': 26}
print(profession)  # Développeur
```

### Parcours des dictionnaires

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

# Parcours des clés
for cle in personne:
    print(cle, ":", personne[cle])

# Parcours des valeurs
for valeur in personne.values():
    print(valeur)

# Parcours des paires clé-valeur
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

### Méthodes utiles des dictionnaires

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

print(list(personne.keys()))    # ['nom', 'age', 'ville']
print(list(personne.values()))  # ['Alice', 25, 'Paris']
print(list(personne.items()))   # [('nom', 'Alice'), ('age', 25), ('ville', 'Paris')]

# Vérifier l'existence d'une clé
print("nom" in personne)        # True
print("pays" in personne)       # False

# Fusionner des dictionnaires
infos_supplementaires = {"profession": "Développeur", "salaire": 50000}
personne.update(infos_supplementaires)
print(personne)
```

## Les Sets (Ensembles)

### Qu'est-ce qu'un set ?

Un set est une collection **non ordonnée** et **modifiable** d'éléments **uniques**. Il ne peut pas contenir de doublons.

```python
# Création d'un set
fruits = {"pomme", "banane", "orange"}
nombres = {1, 2, 3, 4, 5}
set_vide = set()  # Attention : {} crée un dictionnaire vide !

print(fruits)  # {'orange', 'banane', 'pomme'} (ordre non garanti)

# Création à partir d'une liste (supprime automatiquement les doublons)
liste_avec_doublons = [1, 2, 2, 3, 3, 3, 4]
set_unique = set(liste_avec_doublons)
print(set_unique)  # {1, 2, 3, 4}
```

### Opérations sur les sets

```python
fruits = {"pomme", "banane", "orange"}

# Ajout d'éléments
fruits.add("kiwi")
print(fruits)  # {'kiwi', 'orange', 'banane', 'pomme'}

# Suppression d'éléments
fruits.remove("banane")     # Erreur si l'élément n'existe pas
fruits.discard("poire")     # Pas d'erreur si l'élément n'existe pas
print(fruits)  # {'kiwi', 'orange', 'pomme'}

# Vérifier l'appartenance
print("pomme" in fruits)    # True
print("banane" in fruits)   # False
```

### Opérations ensemblistes

```python
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Union (tous les éléments)
print(ensemble1 | ensemble2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(ensemble1.union(ensemble2))  # Même résultat

# Intersection (éléments communs)
print(ensemble1 & ensemble2)  # {4, 5}
print(ensemble1.intersection(ensemble2))  # Même résultat

# Différence (éléments de ensemble1 qui ne sont pas dans ensemble2)
print(ensemble1 - ensemble2)  # {1, 2, 3}
print(ensemble1.difference(ensemble2))  # Même résultat

# Différence symétrique (éléments qui ne sont pas dans les deux)
print(ensemble1 ^ ensemble2)  # {1, 2, 3, 6, 7, 8}
print(ensemble1.symmetric_difference(ensemble2))  # Même résultat
```

## Comparaison des structures de données

| Structure | Ordonnée | Modifiable | Doublons | Cas d'usage |
|-----------|----------|------------|----------|-------------|
| **Liste** | ✅ | ✅ | ✅ | Séquences d'éléments, ordre important |
| **Tuple** | ✅ | ❌ | ✅ | Données immuables, coordonnées |
| **Dictionnaire** | ❌* | ✅ | ❌ (clés) | Associations clé-valeur |
| **Set** | ❌ | ✅ | ❌ | Éléments uniques, opérations ensemblistes |

*Les dictionnaires conservent l'ordre d'insertion depuis Python 3.7+

## Exemples pratiques

### Gestion d'un inventaire

```python
# Utilisation d'un dictionnaire pour un inventaire
inventaire = {
    "pommes": 50,
    "bananes": 30,
    "oranges": 25
}

# Vendre des fruits
def vendre_fruit(nom, quantite):
    if nom in inventaire and inventaire[nom] >= quantite:
        inventaire[nom] -= quantite
        print(f"Vendu {quantite} {nom}")
    else:
        print(f"Stock insuffisant pour {nom}")

vendre_fruit("pommes", 10)
print(inventaire)  # {'pommes': 40, 'bananes': 30, 'oranges': 25}
```

### Suppression des doublons

```python
# Utilisation d'un set pour supprimer les doublons
emails = [
    "alice@email.com",
    "bob@email.com",
    "alice@email.com",  # Doublon
    "charlie@email.com",
    "bob@email.com"     # Doublon
]

emails_uniques = list(set(emails))
print(emails_uniques)  # ['charlie@email.com', 'alice@email.com', 'bob@email.com']
```

### Coordonnées et calculs

```python
# Utilisation de tuples pour les coordonnées
def distance(point1, point2):
    """Calcule la distance entre deux points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

pointA = (0, 0)
pointB = (3, 4)
print(f"Distance: {distance(pointA, pointB)}")  # Distance: 5.0
```

## Conseils et bonnes pratiques

### Choisir la bonne structure

1. **Utilisez une liste** quand vous avez besoin d'une séquence modifiable avec un ordre important
2. **Utilisez un tuple** pour des données immuables ou des coordonnées
3. **Utilisez un dictionnaire** pour des associations clé-valeur
4. **Utilisez un set** pour des éléments uniques ou des opérations ensemblistes

### Optimisation des performances

```python
# Vérification d'appartenance
liste = [1, 2, 3, 4, 5] * 1000    # Liste de 5000 éléments
ensemble = set(liste)              # Set des mêmes éléments

# La vérification dans un set est beaucoup plus rapide
# "if element in ensemble" est O(1) en moyenne
# "if element in liste" est O(n) dans le pire cas
```

### Éviter les erreurs courantes

```python
# Erreur : Modifier une liste pendant qu'on la parcourt
nombres = [1, 2, 3, 4, 5]
# MAUVAIS
for nombre in nombres:
    if nombre % 2 == 0:
        nombres.remove(nombre)  # Peut causer des problèmes

# BON
nombres = [nombre for nombre in nombres if nombre % 2 != 0]
```

## Exercices pratiques

### Exercice 1 : Gestion d'une bibliothèque
Créez un programme qui gère une bibliothèque avec :
- Une liste des livres disponibles
- Un dictionnaire des livres empruntés (nom de l'emprunteur → liste des livres)
- Un set des genres disponibles

### Exercice 2 : Analyse de texte
Écrivez une fonction qui prend un texte et retourne :
- Un dictionnaire avec le nombre d'occurrences de chaque mot
- Un set des mots uniques
- Une liste des mots triés par ordre alphabétique

### Exercice 3 : Coordonnées géographiques
Créez un programme qui :
- Stocke des villes avec leurs coordonnées (tuples)
- Calcule la distance entre deux villes
- Trouve la ville la plus proche d'une position donnée

## Résumé

Les structures de données de Python sont des outils puissants qui permettent d'organiser et de manipuler les informations efficacement. Chaque structure a ses spécificités :

- **Listes** : Flexibles et ordonnées, parfaites pour les séquences modifiables
- **Tuples** : Immuables et ordonnés, idéals pour les données fixes
- **Dictionnaires** : Efficaces pour les associations clé-valeur
- **Sets** : Optimisés pour les éléments uniques et les opérations ensemblistes

La maîtrise de ces structures est essentielle pour écrire du code Python efficace et lisible.

⏭️

