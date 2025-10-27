🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.1 Listes, Tuples, Dictionnaires et Sets

## Introduction

En Python, les structures de données sont des moyens d'organiser et de stocker plusieurs valeurs. Imaginez-les comme différents types de conteneurs : certains sont modifiables, d'autres non ; certains sont ordonnés, d'autres ne le sont pas. Choisir la bonne structure de données rend votre code plus efficace et plus lisible.

Dans cette section, nous allons découvrir les quatre structures de données fondamentales en Python :
- **Les listes** : collections ordonnées et modifiables
- **Les tuples** : collections ordonnées mais immuables
- **Les dictionnaires** : associations clé-valeur
- **Les sets** : collections non ordonnées d'éléments uniques

---

## Les Listes

### Qu'est-ce qu'une liste ?

Une liste est une collection ordonnée et modifiable d'éléments. C'est probablement la structure de données la plus utilisée en Python. Les listes peuvent contenir n'importe quel type de données, et même des types différents dans la même liste.

### Créer une liste

```python
# Liste vide
ma_liste = []
autre_liste = list()

# Liste avec des éléments
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = [1, "texte", 3.14, True]

print(fruits)  # ['pomme', 'banane', 'orange']
```

### Accéder aux éléments

Les éléments d'une liste sont indexés à partir de 0. On peut aussi utiliser des indices négatifs pour accéder aux éléments depuis la fin.

```python
fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# Accès par index positif
print(fruits[0])   # 'pomme' (premier élément)
print(fruits[2])   # 'orange'

# Accès par index négatif
print(fruits[-1])  # 'kiwi' (dernier élément)
print(fruits[-2])  # 'fraise' (avant-dernier)
```

### Slicing (tranches)

Le slicing permet d'extraire une portion de la liste.

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntaxe : liste[début:fin:pas]
print(nombres[2:5])      # [2, 3, 4] (de l'index 2 à 4)
print(nombres[:3])       # [0, 1, 2] (du début jusqu'à l'index 2)
print(nombres[5:])       # [5, 6, 7, 8, 9] (de l'index 5 jusqu'à la fin)
print(nombres[::2])      # [0, 2, 4, 6, 8] (tous les 2 éléments)
print(nombres[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverse la liste)
```

### Modifier une liste

Les listes sont modifiables (mutables), vous pouvez donc changer, ajouter ou supprimer des éléments.

```python
fruits = ["pomme", "banane", "orange"]

# Modifier un élément
fruits[1] = "mangue"
print(fruits)  # ['pomme', 'mangue', 'orange']

# Ajouter un élément à la fin
fruits.append("fraise")
print(fruits)  # ['pomme', 'mangue', 'orange', 'fraise']

# Insérer un élément à une position spécifique
fruits.insert(1, "kiwi")
print(fruits)  # ['pomme', 'kiwi', 'mangue', 'orange', 'fraise']

# Étendre la liste avec une autre liste
fruits.extend(["cerise", "raisin"])
print(fruits)  # ['pomme', 'kiwi', 'mangue', 'orange', 'fraise', 'cerise', 'raisin']
```

### Supprimer des éléments

```python
fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# Supprimer par valeur
fruits.remove("banane")
print(fruits)  # ['pomme', 'orange', 'fraise', 'kiwi']

# Supprimer par index et récupérer la valeur
fruit_supprime = fruits.pop(2)
print(fruit_supprime)  # 'fraise'
print(fruits)          # ['pomme', 'orange', 'kiwi']

# Supprimer le dernier élément
dernier = fruits.pop()
print(dernier)  # 'kiwi'

# Supprimer un élément par index sans récupérer la valeur
del fruits[0]
print(fruits)  # ['orange']

# Vider complètement la liste
fruits.clear()
print(fruits)  # []
```

### Opérations courantes sur les listes

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Longueur de la liste
print(len(nombres))  # 8

# Vérifier si un élément est dans la liste
print(4 in nombres)   # True
print(10 in nombres)  # False

# Compter les occurrences d'un élément
print(nombres.count(1))  # 2

# Trouver l'index d'un élément
print(nombres.index(5))  # 4

# Trier la liste (modifie la liste originale)
nombres.sort()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Trier en ordre décroissant
nombres.sort(reverse=True)
print(nombres)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Créer une copie triée sans modifier l'original
nombres_originaux = [3, 1, 4, 1, 5]
nombres_tries = sorted(nombres_originaux)
print(nombres_originaux)  # [3, 1, 4, 1, 5]
print(nombres_tries)      # [1, 1, 3, 4, 5]

# Inverser l'ordre de la liste
nombres.reverse()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

### Copier une liste

Attention : l'affectation simple ne crée pas une copie !

```python
# Mauvaise méthode : crée une référence
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] - liste1 est aussi modifiée !

# Bonnes méthodes pour copier
liste1 = [1, 2, 3]
liste2 = liste1.copy()
# ou
liste3 = liste1[:]
# ou
liste4 = list(liste1)

liste2.append(4)
print(liste1)  # [1, 2, 3] - liste1 n'est pas modifiée
print(liste2)  # [1, 2, 3, 4]
```

### Listes imbriquées

Les listes peuvent contenir d'autres listes, ce qui permet de créer des structures de données plus complexes.

```python
# Matrice (tableau 2D)
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[0])      # [1, 2, 3]
print(matrice[1][2])   # 6

# Liste de listes avec des données variées
etudiants = [
    ["Alice", 20, "Informatique"],
    ["Bob", 22, "Mathématiques"],
    ["Charlie", 21, "Physique"]
]

for etudiant in etudiants:
    nom, age, specialite = etudiant
    print(f"{nom} a {age} ans et étudie {specialite}")
```

---

## Les Tuples

### Qu'est-ce qu'un tuple ?

Un tuple est similaire à une liste, mais il est **immuable** (non modifiable). Une fois créé, vous ne pouvez pas modifier, ajouter ou supprimer ses éléments. Les tuples sont plus rapides que les listes et protègent vos données contre les modifications accidentelles.

### Créer un tuple

```python
# Tuple vide
mon_tuple = ()
autre_tuple = tuple()

# Tuple avec des éléments
coordonnees = (10, 20)
informations = ("Alice", 25, "Paris")

# Tuple avec un seul élément (attention à la virgule !)
un_element = (5,)  # Correct
pas_un_tuple = (5)  # Ceci est juste un entier entre parenthèses

# Création sans parenthèses (packing)
point = 3, 4
print(point)  # (3, 4)
print(type(point))  # <class 'tuple'>
```

### Accéder aux éléments

L'accès aux éléments d'un tuple fonctionne exactement comme pour les listes.

```python
informations = ("Alice", 25, "Paris", "Ingénieure")

print(informations[0])   # 'Alice'
print(informations[-1])  # 'Ingénieure'
print(informations[1:3]) # (25, 'Paris')
```

### Immuabilité des tuples

```python
coordonnees = (10, 20)

# Ceci provoquera une erreur
# coordonnees[0] = 15  # TypeError: 'tuple' object does not support item assignment

# On ne peut pas non plus ajouter ou supprimer des éléments
# coordonnees.append(30)  # AttributeError
```

### Unpacking (déballage)

Le unpacking permet d'assigner les éléments d'un tuple à plusieurs variables en une seule ligne.

```python
# Unpacking simple
coordonnees = (10, 20)
x, y = coordonnees
print(x)  # 10
print(y)  # 20

# Unpacking avec plusieurs valeurs
personne = ("Alice", 25, "Paris", "Ingénieure")
nom, age, ville, profession = personne
print(nom)  # Alice

# Unpacking partiel avec *
nombres = (1, 2, 3, 4, 5)
premier, *milieu, dernier = nombres
print(premier)  # 1
print(milieu)   # [2, 3, 4]
print(dernier)  # 5

# Échanger des variables facilement
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5
```

### Opérations sur les tuples

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concaténation
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Répétition
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Longueur
print(len(tuple1))  # 3

# Vérifier la présence d'un élément
print(2 in tuple1)  # True

# Compter les occurrences
nombres = (1, 2, 3, 2, 4, 2)
print(nombres.count(2))  # 3

# Trouver l'index
print(nombres.index(3))  # 2
```

### Quand utiliser les tuples ?

```python
# 1. Pour des données qui ne doivent pas changer
DATE_NAISSANCE = (15, 8, 1990)  # jour, mois, année

# 2. Comme clés de dictionnaire (les listes ne peuvent pas être des clés)
positions = {
    (0, 0): "origine",
    (1, 0): "droite",
    (0, 1): "haut"
}

# 3. Pour retourner plusieurs valeurs d'une fonction
def obtenir_coordonnees():
    return 10, 20  # Retourne un tuple

x, y = obtenir_coordonnees()

# 4. Pour garantir l'intégrité des données
JOURS_SEMAINE = ("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")
```

---

## Les Dictionnaires

### Qu'est-ce qu'un dictionnaire ?

Un dictionnaire est une collection non ordonnée de paires **clé-valeur**. Chaque clé est unique et permet d'accéder rapidement à sa valeur associée. C'est l'équivalent des objets en JavaScript ou des maps dans d'autres langages.

### Créer un dictionnaire

```python
# Dictionnaire vide
mon_dict = {}
autre_dict = dict()

# Dictionnaire avec des éléments
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Utiliser dict() avec des paires clé-valeur
etudiant = dict(nom="Bob", age=22, specialite="Informatique")

# Dictionnaire avec différents types de valeurs
produit = {
    "nom": "Ordinateur",
    "prix": 999.99,
    "en_stock": True,
    "caracteristiques": ["16GB RAM", "SSD 512GB"],
    "dimensions": (30, 20, 2)
}
```

### Accéder aux valeurs

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès direct par clé
print(personne["nom"])  # 'Alice'

# Accès avec get() (plus sûr, ne lève pas d'erreur si la clé n'existe pas)
print(personne.get("age"))        # 25
print(personne.get("profession")) # None
print(personne.get("profession", "Non spécifiée"))  # 'Non spécifiée' (valeur par défaut)

# Attention : accéder à une clé inexistante avec [] lève une erreur
# print(personne["profession"])  # KeyError
```

### Modifier un dictionnaire

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Modifier une valeur existante
personne["age"] = 26
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris'}

# Ajouter une nouvelle paire clé-valeur
personne["profession"] = "Ingénieure"
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris', 'profession': 'Ingénieure'}

# Mettre à jour plusieurs valeurs à la fois
personne.update({"age": 27, "ville": "Lyon", "telephone": "0123456789"})
print(personne)
```

### Supprimer des éléments

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "profession": "Ingénieure"
}

# Supprimer une clé spécifique avec del
del personne["profession"]
print(personne)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}

# Supprimer avec pop() et récupérer la valeur
age = personne.pop("age")
print(age)       # 25
print(personne)  # {'nom': 'Alice', 'ville': 'Paris'}

# Supprimer avec pop() avec valeur par défaut
telephone = personne.pop("telephone", "Non renseigné")
print(telephone)  # 'Non renseigné'

# Supprimer et récupérer un élément arbitraire
# item = personne.popitem()

# Vider complètement le dictionnaire
personne.clear()
print(personne)  # {}
```

### Parcourir un dictionnaire

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Parcourir les clés
for cle in personne:
    print(cle)
# ou explicitement
for cle in personne.keys():
    print(cle)

# Parcourir les valeurs
for valeur in personne.values():
    print(valeur)

# Parcourir les paires clé-valeur
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
# Affiche :
# nom: Alice
# age: 25
# ville: Paris
```

### Opérations courantes

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Nombre de paires clé-valeur
print(len(personne))  # 3

# Vérifier si une clé existe
print("nom" in personne)        # True
print("profession" in personne) # False

# Obtenir toutes les clés
print(personne.keys())    # dict_keys(['nom', 'age', 'ville'])
print(list(personne.keys()))  # ['nom', 'age', 'ville']

# Obtenir toutes les valeurs
print(personne.values())  # dict_values(['Alice', 25, 'Paris'])

# Obtenir toutes les paires clé-valeur
print(personne.items())   # dict_items([('nom', 'Alice'), ('age', 25), ('ville', 'Paris')])
```

### Copier un dictionnaire

```python
# Mauvaise méthode : crée une référence
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2, 'c': 3} - dict1 est aussi modifié !

# Bonne méthode : copie superficielle
dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()
# ou
dict3 = dict(dict1)

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2}
print(dict2)  # {'a': 1, 'b': 2, 'c': 3}
```

### Dictionnaires imbriqués

```python
# Dictionnaire contenant d'autres dictionnaires
entreprise = {
    "nom": "Tech Corp",
    "employes": {
        "dev1": {
            "nom": "Alice",
            "poste": "Développeuse",
            "salaire": 50000
        },
        "dev2": {
            "nom": "Bob",
            "poste": "Développeur",
            "salaire": 55000
        }
    },
    "localisation": "Paris"
}

# Accès aux valeurs imbriquées
print(entreprise["employes"]["dev1"]["nom"])  # Alice

# Parcourir les employés
for id_employe, infos in entreprise["employes"].items():
    print(f"{id_employe}: {infos['nom']} - {infos['poste']}")
```

### Valeur par défaut avec setdefault()

```python
personne = {"nom": "Alice", "age": 25}

# Si la clé existe, retourne sa valeur
print(personne.setdefault("nom", "Inconnu"))  # 'Alice'

# Si la clé n'existe pas, l'ajoute avec la valeur par défaut
print(personne.setdefault("ville", "Paris"))  # 'Paris'
print(personne)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

---

## Les Sets (Ensembles)

### Qu'est-ce qu'un set ?

Un set est une collection **non ordonnée** d'éléments **uniques**. Les sets sont très utiles pour éliminer les doublons et effectuer des opérations mathématiques d'ensembles (union, intersection, différence).

### Créer un set

```python
# Set vide (attention : {} crée un dictionnaire vide, pas un set)
mon_set = set()

# Set avec des éléments
nombres = {1, 2, 3, 4, 5}
fruits = {"pomme", "banane", "orange"}

# Créer un set à partir d'une liste (élimine les doublons)
liste_avec_doublons = [1, 2, 2, 3, 3, 3, 4]
nombres_uniques = set(liste_avec_doublons)
print(nombres_uniques)  # {1, 2, 3, 4}

# Créer un set à partir d'une chaîne
lettres = set("hello")
print(lettres)  # {'h', 'e', 'l', 'o'}
```

### Caractéristiques importantes

```python
# Les sets ne conservent pas l'ordre
nombres = {3, 1, 4, 1, 5, 9, 2}
print(nombres)  # Affichage dans un ordre arbitraire : {1, 2, 3, 4, 5, 9}

# Les doublons sont automatiquement éliminés
nombres = {1, 2, 2, 3, 3, 3}
print(nombres)  # {1, 2, 3}

# Les éléments doivent être immuables (hashables)
# Vous pouvez avoir des nombres, des chaînes, des tuples
valide = {1, "texte", (1, 2), True}

# Mais pas de listes ou de dictionnaires
# invalide = {[1, 2, 3]}  # TypeError
```

### Ajouter et supprimer des éléments

```python
fruits = {"pomme", "banane"}

# Ajouter un élément
fruits.add("orange")
print(fruits)  # {'pomme', 'banane', 'orange'}

# Ajouter plusieurs éléments
fruits.update(["fraise", "kiwi"])
print(fruits)  # {'pomme', 'banane', 'orange', 'fraise', 'kiwi'}

# Supprimer un élément (lève une erreur si l'élément n'existe pas)
fruits.remove("banane")
print(fruits)  # {'pomme', 'orange', 'fraise', 'kiwi'}

# Supprimer un élément (ne lève pas d'erreur si l'élément n'existe pas)
fruits.discard("mangue")  # Pas d'erreur
print(fruits)  # Inchangé

# Supprimer et retourner un élément arbitraire
fruit = fruits.pop()
print(fruit)   # Par exemple : 'pomme'
print(fruits)

# Vider le set
fruits.clear()
print(fruits)  # set()
```

### Opérations sur les sets

```python
nombres = {1, 2, 3, 4, 5}

# Nombre d'éléments
print(len(nombres))  # 5

# Vérifier si un élément est dans le set
print(3 in nombres)   # True
print(10 in nombres)  # False

# Parcourir les éléments
for nombre in nombres:
    print(nombre)
```

### Opérations mathématiques d'ensembles

Les sets permettent d'effectuer facilement des opérations d'ensembles.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (tous les éléments des deux sets)
union = set1 | set2
# ou
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (éléments présents dans les deux sets)
intersection = set1 & set2
# ou
intersection = set1.intersection(set2)
print(intersection)  # {4, 5}

# Différence (éléments dans set1 mais pas dans set2)
difference = set1 - set2
# ou
difference = set1.difference(set2)
print(difference)  # {1, 2, 3}

# Différence symétrique (éléments dans l'un ou l'autre, mais pas dans les deux)
diff_sym = set1 ^ set2
# ou
diff_sym = set1.symmetric_difference(set2)
print(diff_sym)  # {1, 2, 3, 6, 7, 8}
```

### Comparaisons de sets

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# Égalité
print(set1 == set3)  # True

# Sous-ensemble (subset)
print(set1.issubset(set2))     # True (set1 est inclus dans set2)
print(set1 <= set2)            # True

# Sous-ensemble strict
print(set1 < set2)             # True

# Sur-ensemble (superset)
print(set2.issuperset(set1))   # True (set2 contient set1)
print(set2 >= set1)            # True

# Sets disjoints (aucun élément en commun)
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.isdisjoint(set_b))  # True
```

### Cas d'usage pratiques

```python
# 1. Éliminer les doublons d'une liste
liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
liste_sans_doublons = list(set(liste))
print(liste_sans_doublons)  # [1, 2, 3, 4]

# 2. Trouver les éléments uniques entre deux listes
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
uniques = list(set(liste1) ^ set(liste2))
print(uniques)  # [1, 2, 3, 6, 7, 8]

# 3. Vérifier si tous les éléments d'une liste sont uniques
def tous_uniques(liste):
    return len(liste) == len(set(liste))

print(tous_uniques([1, 2, 3, 4]))     # True
print(tous_uniques([1, 2, 2, 3]))     # False

# 4. Trouver les mots uniques dans un texte
texte = "le chat et le chien jouent avec le chat"
mots = texte.split()
mots_uniques = set(mots)
print(mots_uniques)  # {'le', 'chat', 'et', 'chien', 'jouent', 'avec'}
print(f"Nombre de mots uniques : {len(mots_uniques)}")  # 6
```

### Frozenset (set immuable)

Si vous avez besoin d'un set qui ne peut pas être modifié, utilisez `frozenset`.

```python
# Créer un frozenset
nombres_immutables = frozenset([1, 2, 3, 4, 5])

# On peut lire mais pas modifier
print(3 in nombres_immutables)  # True

# Ceci provoque une erreur
# nombres_immutables.add(6)  # AttributeError

# Utile comme clé de dictionnaire ou élément d'un autre set
dict_avec_frozenset = {
    frozenset([1, 2]): "ensemble A",
    frozenset([3, 4]): "ensemble B"
}

set_de_sets = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6])
}
```

---

## Tableau récapitulatif

| Structure | Ordonné | Modifiable | Doublons | Syntaxe | Cas d'usage principal |
|-----------|---------|------------|----------|---------|----------------------|
| **Liste** | Oui | Oui | Oui | `[1, 2, 3]` | Collection générale d'éléments |
| **Tuple** | Oui | Non | Oui | `(1, 2, 3)` | Données immuables, unpacking |
| **Dictionnaire** | Non* | Oui | Non (clés) | `{"a": 1}` | Association clé-valeur |
| **Set** | Non | Oui | Non | `{1, 2, 3}` | Éléments uniques, opérations d'ensembles |

*Depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion, mais ce n'est pas leur caractéristique principale.

---

## Choisir la bonne structure de données

### Utilisez une **liste** quand :
- Vous avez besoin d'une collection ordonnée
- Vous devez modifier les éléments
- Les doublons sont acceptables
- Vous devez accéder aux éléments par index

### Utilisez un **tuple** quand :
- Vous avez besoin d'une collection ordonnée immuable
- Vous voulez protéger les données contre les modifications
- Vous retournez plusieurs valeurs d'une fonction
- Vous avez besoin d'utiliser la collection comme clé de dictionnaire

### Utilisez un **dictionnaire** quand :
- Vous associez des clés à des valeurs
- Vous avez besoin d'un accès rapide par clé
- Vous travaillez avec des données structurées (comme JSON)

### Utilisez un **set** quand :
- Vous devez garantir l'unicité des éléments
- Vous effectuez des opérations d'ensembles (union, intersection, etc.)
- L'ordre n'a pas d'importance
- Vous voulez éliminer les doublons rapidement

---

## Exemples pratiques combinés

### Exemple 1 : Gestion d'un inventaire

```python
# Dictionnaire pour stocker les produits avec leurs quantités
inventaire = {
    "pommes": 50,
    "bananes": 30,
    "oranges": 40
}

# Liste des commandes reçues (tuples)
commandes = [
    ("pommes", 10),
    ("bananes", 5),
    ("oranges", 15),
    ("pommes", 5)
]

# Traiter les commandes
for produit, quantite in commandes:
    if produit in inventaire:
        inventaire[produit] -= quantite
        print(f"Commande traitée : {quantite} {produit}")

print("Inventaire mis à jour :", inventaire)
# {'pommes': 35, 'bananes': 25, 'oranges': 25}
```

### Exemple 2 : Analyse de texte

```python
texte = "Python est un langage de programmation. Python est facile à apprendre."

# Convertir en minuscules et séparer en mots
mots = texte.lower().replace(".", "").split()

# Compter les occurrences avec un dictionnaire
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

print("Fréquence des mots :")
for mot, count in compteur.items():
    print(f"{mot}: {count}")

# Mots uniques avec un set
mots_uniques = set(mots)
print(f"\nNombre de mots uniques : {len(mots_uniques)}")
```

### Exemple 3 : Gestion d'étudiants

```python
# Liste de tuples pour les étudiants
etudiants = [
    ("Alice", 18, ["Math", "Physique", "Informatique"]),
    ("Bob", 19, ["Math", "Chimie"]),
    ("Charlie", 18, ["Physique", "Informatique", "Chimie"])
]

# Extraire toutes les matières uniques avec un set
toutes_matieres = set()
for nom, age, matieres in etudiants:
    toutes_matieres.update(matieres)

print("Matières enseignées :", toutes_matieres)

# Créer un dictionnaire : matière -> liste d'étudiants
matieres_etudiants = {matiere: [] for matiere in toutes_matieres}

for nom, age, matieres in etudiants:
    for matiere in matieres:
        matieres_etudiants[matiere].append(nom)

print("\nÉtudiants par matière :")
for matiere, noms in matieres_etudiants.items():
    print(f"{matiere}: {', '.join(noms)}")
```

---

## Conclusion

Les structures de données en Python sont des outils puissants qui vous permettent d'organiser et de manipuler vos données efficacement. Voici les points clés à retenir :

- **Les listes** sont polyvalentes et modifiables, idéales pour la plupart des collections
- **Les tuples** sont immuables et parfaits pour protéger les données
- **Les dictionnaires** permettent d'associer des clés à des valeurs pour un accès rapide
- **Les sets** garantissent l'unicité et permettent des opérations d'ensembles

Avec la pratique, vous développerez une intuition pour choisir la structure la plus adaptée à chaque situation. N'hésitez pas à combiner ces structures pour créer des organisations de données plus complexes et plus puissantes !

⏭️ [Compréhensions de listes et dictionnaires](/02-structures-de-donnees/02-comprehensions.md)
