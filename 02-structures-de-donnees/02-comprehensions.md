🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.2 Compréhensions de Listes et Dictionnaires

## Introduction

Les **compréhensions** (ou *comprehensions* en anglais) sont une fonctionnalité élégante et puissante de Python qui permet de créer des collections (listes, dictionnaires, sets) de manière concise et lisible. Au lieu d'utiliser plusieurs lignes avec des boucles `for`, vous pouvez créer une collection en une seule ligne expressive.

Les compréhensions rendent votre code :
- **Plus court** : moins de lignes à écrire
- **Plus lisible** : une fois maîtrisées, elles sont très expressives
- **Plus rapide** : légèrement plus performant que les boucles équivalentes

Dans cette section, nous allons explorer :
- Les compréhensions de listes
- Les compréhensions de dictionnaires
- Les compréhensions de sets
- Les compréhensions imbriquées

---

## Compréhensions de Listes

### Concept de base

Une compréhension de liste permet de créer une nouvelle liste en transformant ou filtrant une séquence existante.

**Syntaxe générale :**
```python
[expression for element in iterable]
```

### Premier exemple : transformer une liste

Imaginons que vous voulez créer une liste avec les carrés des nombres de 0 à 4.

**Méthode traditionnelle avec une boucle :**
```python
# Méthode classique
carres = []
for i in range(5):
    carres.append(i ** 2)

print(carres)  # [0, 1, 4, 9, 16]
```

**Avec une compréhension de liste :**
```python
# Avec une compréhension de liste
carres = [i ** 2 for i in range(5)]

print(carres)  # [0, 1, 4, 9, 16]
```

C'est beaucoup plus concis ! On lit cette ligne ainsi : "crée une liste contenant `i ** 2` pour chaque `i` dans `range(5)`".

### Exemples de base

```python
# Créer une liste de nombres
nombres = [x for x in range(10)]
print(nombres)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplier chaque nombre par 2
doubles = [x * 2 for x in range(5)]
print(doubles)  # [0, 2, 4, 6, 8]

# Convertir des températures Celsius en Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# Mettre tous les mots en majuscules
mots = ["python", "est", "génial"]
mots_majuscules = [mot.upper() for mot in mots]
print(mots_majuscules)  # ['PYTHON', 'EST', 'GÉNIAL']

# Extraire la première lettre de chaque mot
premieres_lettres = [mot[0] for mot in mots]
print(premieres_lettres)  # ['p', 'e', 'g']
```

### Compréhensions avec condition (filtre)

Vous pouvez ajouter une condition `if` pour filtrer les éléments.

**Syntaxe :**
```python
[expression for element in iterable if condition]
```

**Exemples :**

```python
# Garder seulement les nombres pairs
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = [x for x in nombres if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]

# Garder seulement les nombres positifs
nombres = [-2, -1, 0, 1, 2, 3]
positifs = [x for x in nombres if x > 0]
print(positifs)  # [1, 2, 3]

# Filtrer les mots courts (moins de 5 lettres)
mots = ["chat", "éléphant", "oiseau", "souris"]
mots_courts = [mot for mot in mots if len(mot) < 5]
print(mots_courts)  # ['chat']

# Extraire les nombres pairs et les mettre au carré
nombres = range(10)
carres_pairs = [x ** 2 for x in nombres if x % 2 == 0]
print(carres_pairs)  # [0, 4, 16, 36, 64]
```

### Comparaison : boucle vs compréhension

Prenons un exemple concret pour bien voir la différence.

**Objectif :** Créer une liste des longueurs des mots qui contiennent la lettre 'a'.

**Avec une boucle traditionnelle :**
```python
mots = ["chat", "chien", "oiseau", "poisson"]
longueurs = []

for mot in mots:
    if 'a' in mot:
        longueurs.append(len(mot))

print(longueurs)  # [4, 6]
```

**Avec une compréhension de liste :**
```python
mots = ["chat", "chien", "oiseau", "poisson"]
longueurs = [len(mot) for mot in mots if 'a' in mot]

print(longueurs)  # [4, 6]
```

La compréhension est plus concise : 4 lignes deviennent 1 ligne !

### Compréhensions avec if-else

Vous pouvez aussi utiliser `if-else` pour appliquer une transformation conditionnelle (notez que la syntaxe est différente).

**Syntaxe :**
```python
[expression_if_true if condition else expression_if_false for element in iterable]
```

**Exemples :**

```python
# Remplacer les nombres négatifs par 0
nombres = [-2, -1, 0, 1, 2, 3]
positifs_ou_zero = [x if x >= 0 else 0 for x in nombres]
print(positifs_ou_zero)  # [0, 0, 0, 1, 2, 3]

# Classifier les nombres en "pair" ou "impair"
nombres = [1, 2, 3, 4, 5]
classification = ["pair" if x % 2 == 0 else "impair" for x in nombres]
print(classification)  # ['impair', 'pair', 'impair', 'pair', 'impair']

# Appliquer une réduction aux produits en stock
prix = [100, 200, 150, 300]
prix_soldes = [p * 0.8 if p > 150 else p for p in prix]
print(prix_soldes)  # [100, 160.0, 150, 240.0]

# Convertir des notes en appréciation
notes = [18, 12, 8, 15]
appreciations = ["Excellent" if n >= 16 else "Bien" if n >= 12 else "Passable" for n in notes]
print(appreciations)  # ['Excellent', 'Bien', 'Passable', 'Bien']
```

### Compréhensions avec plusieurs boucles

Vous pouvez imbriquer plusieurs boucles `for` dans une compréhension.

```python
# Créer toutes les paires possibles
couleurs = ["rouge", "vert", "bleu"]
tailles = ["S", "M", "L"]

combinaisons = [(couleur, taille) for couleur in couleurs for taille in tailles]
print(combinaisons)
# [('rouge', 'S'), ('rouge', 'M'), ('rouge', 'L'),
#  ('vert', 'S'), ('vert', 'M'), ('vert', 'L'),
#  ('bleu', 'S'), ('bleu', 'M'), ('bleu', 'L')]

# Multiplication de matrices (liste de listes)
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elements = [element for ligne in matrice for element in ligne]
print(elements)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Créer des paires de coordonnées
coordonnees = [(x, y) for x in range(3) for y in range(3)]
print(coordonnees)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

**Note :** L'ordre des boucles dans la compréhension est le même que dans les boucles imbriquées traditionnelles :

```python
# Équivalent traditionnel de la compréhension ci-dessus
coordonnees = []
for x in range(3):
    for y in range(3):
        coordonnees.append((x, y))
```

### Compréhensions imbriquées (listes de listes)

Vous pouvez créer des listes de listes avec des compréhensions imbriquées.

```python
# Créer une matrice 3x3 remplie de zéros
matrice = [[0 for _ in range(3)] for _ in range(3)]
print(matrice)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Créer une table de multiplication
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for ligne in table:
    print(ligne)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]

# Transposer une matrice
matrice = [[1, 2, 3], [4, 5, 6]]
transposee = [[ligne[i] for ligne in matrice] for i in range(len(matrice[0]))]
print(transposee)
# [[1, 4], [2, 5], [3, 6]]
```

### Cas d'usage pratiques

```python
# 1. Extraire des données structurées
etudiants = [
    {"nom": "Alice", "age": 20, "note": 18},
    {"nom": "Bob", "age": 22, "note": 14},
    {"nom": "Charlie", "age": 21, "note": 16}
]

# Extraire seulement les noms
noms = [etudiant["nom"] for etudiant in etudiants]
print(noms)  # ['Alice', 'Bob', 'Charlie']

# Extraire les noms des étudiants ayant plus de 15
bons_etudiants = [e["nom"] for e in etudiants if e["note"] >= 15]
print(bons_etudiants)  # ['Alice', 'Charlie']

# 2. Traiter des fichiers
lignes = ["  ligne 1  ", "  ligne 2\n", "ligne 3  "]
lignes_nettoyees = [ligne.strip() for ligne in lignes]
print(lignes_nettoyees)  # ['ligne 1', 'ligne 2', 'ligne 3']

# 3. Filtrer et transformer en une étape
texte = "Python Est Un Langage Génial"
voyelles = [c.lower() for c in texte if c.lower() in 'aeiouy']
print(voyelles)  # ['o', 'e', 'u', 'a', 'a', 'e', 'e', 'i', 'a']

# 4. Aplatir une structure imbriquée
listes_imbriquees = [[1, 2], [3, 4], [5, 6]]
liste_plate = [element for sous_liste in listes_imbriquees for element in sous_liste]
print(liste_plate)  # [1, 2, 3, 4, 5, 6]
```

---

## Compréhensions de Dictionnaires

Les compréhensions de dictionnaires permettent de créer des dictionnaires de manière concise.

**Syntaxe générale :**
```python
{key_expression: value_expression for element in iterable}
```

### Exemples de base

```python
# Créer un dictionnaire de carrés
carres = {x: x**2 for x in range(5)}
print(carres)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Créer un dictionnaire à partir de deux listes
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
personnes = {nom: age for nom, age in zip(noms, ages)}
print(personnes)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Créer un dictionnaire de longueurs de mots
mots = ["chat", "chien", "oiseau"]
longueurs = {mot: len(mot) for mot in mots}
print(longueurs)  # {'chat': 4, 'chien': 5, 'oiseau': 6}

# Inverser un dictionnaire (échanger clés et valeurs)
original = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in original.items()}
print(inverse)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Compréhensions de dictionnaires avec conditions

```python
# Filtrer les notes supérieures à 12
notes = {"Alice": 18, "Bob": 10, "Charlie": 15, "David": 8}
bonnes_notes = {nom: note for nom, note in notes.items() if note > 12}
print(bonnes_notes)  # {'Alice': 18, 'Charlie': 15}

# Garder seulement les nombres pairs
nombres = {f"n{i}": i for i in range(10) if i % 2 == 0}
print(nombres)  # {'n0': 0, 'n2': 2, 'n4': 4, 'n6': 6, 'n8': 8}

# Créer un dictionnaire de mots avec plus de 4 lettres
mots = ["le", "chat", "et", "le", "chien"]
mots_longs = {mot: len(mot) for mot in mots if len(mot) > 2}
print(mots_longs)  # {'chat': 4, 'chien': 5}
```

### Transformer les valeurs d'un dictionnaire

```python
# Appliquer une réduction de 20% sur tous les prix
prix = {"pomme": 2.5, "banane": 1.8, "orange": 3.0}
prix_soldes = {produit: prix * 0.8 for produit, prix in prix.items()}
print(prix_soldes)  # {'pomme': 2.0, 'banane': 1.44, 'orange': 2.4}

# Convertir toutes les valeurs en chaînes de caractères
donnees = {"a": 1, "b": 2, "c": 3}
donnees_str = {cle: str(valeur) for cle, valeur in donnees.items()}
print(donnees_str)  # {'a': '1', 'b': '2', 'c': '3'}

# Mettre les clés en majuscules
original = {"nom": "Alice", "age": 25, "ville": "Paris"}
majuscules = {cle.upper(): valeur for cle, valeur in original.items()}
print(majuscules)  # {'NOM': 'Alice', 'AGE': 25, 'VILLE': 'Paris'}
```

### Compréhensions avec conditions if-else

```python
# Classifier les notes
notes = {"Alice": 18, "Bob": 10, "Charlie": 15}
appreciations = {nom: "Admis" if note >= 12 else "Refusé"
                 for nom, note in notes.items()}
print(appreciations)  # {'Alice': 'Admis', 'Bob': 'Refusé', 'Charlie': 'Admis'}

# Ajuster les prix en fonction du stock
produits = {"laptop": 1000, "souris": 20, "clavier": 50}
stock = {"laptop": 5, "souris": 100, "clavier": 30}

prix_ajustes = {
    produit: prix * 1.1 if stock[produit] < 10 else prix * 0.9
    for produit, prix in produits.items()
}
print(prix_ajustes)  # {'laptop': 1100.0, 'souris': 18.0, 'clavier': 45.0}
```

### Cas d'usage pratiques

```python
# 1. Compter les occurrences de caractères
texte = "hello"
occurrences = {lettre: texte.count(lettre) for lettre in set(texte)}
print(occurrences)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 2. Grouper des données
etudiants = [
    {"nom": "Alice", "classe": "A"},
    {"nom": "Bob", "classe": "B"},
    {"nom": "Charlie", "classe": "A"}
]

# Créer un index par classe (version simplifiée)
index_classes = {
    classe: [e["nom"] for e in etudiants if e["classe"] == classe]
    for classe in set(e["classe"] for e in etudiants)
}
print(index_classes)  # {'A': ['Alice', 'Charlie'], 'B': ['Bob']}

# 3. Créer un dictionnaire de configuration
parametres = ["debug", "verbose", "log"]
config = {param: True for param in parametres}
print(config)  # {'debug': True, 'verbose': True, 'log': True}

# 4. Convertir des données
temperatures_c = {"Paris": 20, "Londres": 15, "Berlin": 18}
temperatures_f = {
    ville: (temp * 9/5) + 32
    for ville, temp in temperatures_c.items()
}
print(temperatures_f)  # {'Paris': 68.0, 'Londres': 59.0, 'Berlin': 64.4}
```

### Créer un dictionnaire à partir d'une liste de tuples

```python
# Méthode 1 : avec dict()
donnees = [("a", 1), ("b", 2), ("c", 3)]
dictionnaire = dict(donnees)
print(dictionnaire)  # {'a': 1, 'b': 2, 'c': 3}

# Méthode 2 : avec une compréhension
dictionnaire = {cle: valeur for cle, valeur in donnees}
print(dictionnaire)  # {'a': 1, 'b': 2, 'c': 3}

# Avec transformation
dictionnaire = {cle.upper(): valeur * 2 for cle, valeur in donnees}
print(dictionnaire)  # {'A': 2, 'B': 4, 'C': 6}
```

---

## Compréhensions de Sets

Les compréhensions de sets fonctionnent comme celles des listes, mais créent des ensembles (éléments uniques, non ordonnés).

**Syntaxe générale :**
```python
{expression for element in iterable}
```

**Attention :** Notez que la syntaxe utilise des accolades `{}` comme les dictionnaires, mais sans les `:` pour séparer clés et valeurs.

### Exemples

```python
# Créer un set de carrés
carres = {x**2 for x in range(5)}
print(carres)  # {0, 1, 4, 9, 16}

# Extraire les caractères uniques d'une chaîne
texte = "hello world"
caracteres_uniques = {c for c in texte if c != ' '}
print(caracteres_uniques)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Obtenir les longueurs uniques des mots
mots = ["chat", "chien", "oiseau", "chat", "lion"]
longueurs_uniques = {len(mot) for mot in mots}
print(longueurs_uniques)  # {4, 5, 6}

# Extraire les premières lettres (en minuscules)
prenoms = ["Alice", "Bob", "Charlie", "Anne"]
premieres_lettres = {nom[0].lower() for nom in prenoms}
print(premieres_lettres)  # {'a', 'b', 'c'}
```

### Compréhensions de sets avec conditions

```python
# Nombres pairs uniques
nombres = [1, 2, 2, 3, 4, 4, 5, 6, 6]
pairs_uniques = {x for x in nombres if x % 2 == 0}
print(pairs_uniques)  # {2, 4, 6}

# Voyelles présentes dans un texte
texte = "Python est un excellent langage"
voyelles = {c.lower() for c in texte if c.lower() in 'aeiouy'}
print(voyelles)  # {'e', 'a', 'o', 'u'}

# Domaines uniques d'emails
emails = ["alice@example.com", "bob@test.com", "charlie@example.com"]
domaines = {email.split('@')[1] for email in emails}
print(domaines)  # {'example.com', 'test.com'}
```

### Cas d'usage : éliminer les doublons avec transformation

```python
# Mots uniques en minuscules
texte = "Le Chat et le Chien jouent avec le Chat"
mots_uniques = {mot.lower() for mot in texte.split()}
print(mots_uniques)  # {'le', 'chat', 'et', 'chien', 'jouent', 'avec'}

# Valeurs absolues uniques
nombres = [-2, -1, 0, 1, 2, 3]
absolues_uniques = {abs(x) for x in nombres}
print(absolues_uniques)  # {0, 1, 2, 3}
```

---

## Comparaison : Listes vs Dictionnaires vs Sets

Voici un exemple qui montre les trois types de compréhensions pour le même problème :

```python
nombres = [1, 2, 3, 4, 5]

# Compréhension de liste : créer une liste de carrés
carres_liste = [x**2 for x in nombres]
print(carres_liste)  # [1, 4, 9, 16, 25]

# Compréhension de dictionnaire : associer nombre → carré
carres_dict = {x: x**2 for x in nombres}
print(carres_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Compréhension de set : ensemble de carrés (uniques)
nombres_avec_doublons = [1, 2, 2, 3, 3, 4, 5]
carres_set = {x**2 for x in nombres_avec_doublons}
print(carres_set)  # {1, 4, 9, 16, 25}
```

---

## Compréhensions imbriquées avancées

Les compréhensions imbriquées peuvent devenir complexes. Utilisez-les avec précaution pour maintenir la lisibilité.

### Exemple 1 : Matrice

```python
# Créer une matrice identité 4x4
taille = 4
identite = [[1 if i == j else 0 for j in range(taille)] for i in range(taille)]

for ligne in identite:
    print(ligne)
# [1, 0, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
```

### Exemple 2 : Filtrer des listes imbriquées

```python
# Liste de listes de nombres
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Extraire seulement les nombres pairs
pairs = [x for ligne in matrice for x in ligne if x % 2 == 0]
print(pairs)  # [2, 4, 6, 8]

# Garder seulement les lignes qui contiennent au moins un nombre > 5
lignes_filtrees = [ligne for ligne in matrice if any(x > 5 for x in ligne)]
print(lignes_filtrees)  # [[4, 5, 6], [7, 8, 9]]
```

### Exemple 3 : Dictionnaires imbriqués

```python
# Créer un dictionnaire de dictionnaires
categories = ["fruits", "legumes"]
items = {"fruits": ["pomme", "banane"], "legumes": ["carotte", "tomate"]}

# Créer un dictionnaire avec les longueurs de chaque item
longueurs = {
    categorie: {item: len(item) for item in items[categorie]}
    for categorie in categories
}
print(longueurs)
# {'fruits': {'pomme': 5, 'banane': 6}, 'legumes': {'carotte': 7, 'tomate': 6}}
```

---

## Expressions génératrices (Generator Expressions)

Les expressions génératrices ressemblent aux compréhensions de listes, mais utilisent des parenthèses `()` au lieu de crochets `[]`. Elles créent des générateurs qui produisent des valeurs à la demande, ce qui est plus efficace en mémoire.

```python
# Compréhension de liste : crée toute la liste en mémoire
carres_liste = [x**2 for x in range(1000000)]

# Expression génératrice : génère les valeurs à la demande
carres_gen = (x**2 for x in range(1000000))

# Utiliser le générateur
for carre in carres_gen:
    if carre > 100:
        break
    print(carre)

# Expressions génératrices avec des fonctions
nombres = [1, 2, 3, 4, 5]
somme = sum(x**2 for x in nombres)  # Pas besoin de [] supplémentaires
print(somme)  # 55

# Maximum des valeurs absolues
nombres = [-5, 2, -8, 3]
max_abs = max(abs(x) for x in nombres)
print(max_abs)  # 8
```

**Quand utiliser les expressions génératrices ?**
- Quand vous traitez de grandes quantités de données
- Quand vous n'avez besoin de parcourir les éléments qu'une seule fois
- Quand vous utilisez la séquence dans une fonction comme `sum()`, `max()`, `min()`, `any()`, `all()`

---

## Bonnes pratiques et conseils

### 1. Privilégiez la lisibilité

```python
# ❌ Difficile à lire
resultat = [x*2 for x in [y**2 for y in range(10) if y%2==0] if x>10]

# ✅ Plus lisible avec des étapes intermédiaires
carres_pairs = [y**2 for y in range(10) if y % 2 == 0]
resultat = [x * 2 for x in carres_pairs if x > 10]

# Ou même avec des boucles traditionnelles si c'est plus clair
carres_pairs = []
for y in range(10):
    if y % 2 == 0:
        carre = y ** 2
        if carre > 5:
            carres_pairs.append(carre * 2)
```

### 2. Limitez la complexité

Si votre compréhension nécessite plus de deux niveaux d'imbrication ou plusieurs conditions, envisagez d'utiliser une boucle traditionnelle ou de décomposer en plusieurs étapes.

```python
# ❌ Trop complexe
resultat = {k: [x*2 for x in v if x > 0] for k, v in donnees.items() if len(v) > 2}

# ✅ Plus clair
resultat = {}
for k, v in donnees.items():
    if len(v) > 2:
        resultat[k] = [x * 2 for x in v if x > 0]
```

### 3. Utilisez des noms de variables expressifs

```python
# ❌ Peu clair
r = [x for x in l if x > 10]

# ✅ Plus clair
prix_eleves = [prix for prix in liste_prix if prix > 10]
```

### 4. Quand ne PAS utiliser les compréhensions

N'utilisez pas les compréhensions quand :
- La logique est trop complexe
- Vous avez besoin de gérer des exceptions
- Vous effectuez des opérations avec effets de bord (print, écriture dans des fichiers, etc.)
- La lisibilité en souffre

```python
# ❌ Mauvaise utilisation : effet de bord
[print(x) for x in nombres]  # N'utilisez pas de compréhension pour cela !

# ✅ Utilisez une boucle normale
for x in nombres:
    print(x)
```

### 5. Performances

Les compréhensions sont généralement plus rapides que les boucles équivalentes, mais la différence n'est significative que pour de grandes quantités de données. Privilégiez toujours la lisibilité.

---

## Exemples pratiques complets

### Exemple 1 : Analyse de texte

```python
texte = "Python est un langage de programmation. Python est facile à apprendre."

# Nettoyer et séparer les mots
mots = texte.lower().replace(".", "").split()

# Compter la fréquence des mots avec une compréhension de dictionnaire
frequence = {mot: mots.count(mot) for mot in set(mots)}
print(frequence)

# Garder seulement les mots qui apparaissent plus d'une fois
mots_frequents = {mot: freq for mot, freq in frequence.items() if freq > 1}
print(mots_frequents)  # {'python': 2, 'est': 2}
```

### Exemple 2 : Transformation de données

```python
# Données brutes
employes = [
    "Alice:25:50000",
    "Bob:30:60000",
    "Charlie:35:70000"
]

# Convertir en liste de dictionnaires
employes_dict = [
    {
        "nom": ligne.split(':')[0],
        "age": int(ligne.split(':')[1]),
        "salaire": int(ligne.split(':')[2])
    }
    for ligne in employes
]

print(employes_dict)
# [{'nom': 'Alice', 'age': 25, 'salaire': 50000},
#  {'nom': 'Bob', 'age': 30, 'salaire': 60000},
#  {'nom': 'Charlie', 'age': 35, 'salaire': 70000}]

# Augmenter le salaire de 10% pour les personnes de plus de 30 ans
salaires_augmentes = {
    e["nom"]: e["salaire"] * 1.1 if e["age"] > 30 else e["salaire"]
    for e in employes_dict
}
print(salaires_augmentes)
# {'Alice': 50000, 'Bob': 60000, 'Charlie': 77000.0}
```

### Exemple 3 : Filtrage et regroupement

```python
# Liste de produits avec catégories
produits = [
    {"nom": "Pomme", "categorie": "Fruits", "prix": 2.5},
    {"nom": "Carotte", "categorie": "Légumes", "prix": 1.8},
    {"nom": "Banane", "categorie": "Fruits", "prix": 1.5},
    {"nom": "Tomate", "categorie": "Légumes", "prix": 2.0}
]

# Créer un dictionnaire : catégorie → liste de noms de produits
produits_par_categorie = {
    categorie: [p["nom"] for p in produits if p["categorie"] == categorie]
    for categorie in set(p["categorie"] for p in produits)
}
print(produits_par_categorie)
# {'Fruits': ['Pomme', 'Banane'], 'Légumes': ['Carotte', 'Tomate']}

# Prix moyen par catégorie
prix_moyens = {
    categorie: sum(p["prix"] for p in produits if p["categorie"] == categorie) /
               len([p for p in produits if p["categorie"] == categorie])
    for categorie in set(p["categorie"] for p in produits)
}
print(prix_moyens)
# {'Fruits': 2.0, 'Légumes': 1.9}
```

### Exemple 4 : Opérations matricielles

```python
# Addition de matrices
matrice_a = [[1, 2, 3], [4, 5, 6]]
matrice_b = [[7, 8, 9], [10, 11, 12]]

# Additionner élément par élément
somme = [
    [matrice_a[i][j] + matrice_b[i][j] for j in range(len(matrice_a[0]))]
    for i in range(len(matrice_a))
]
print(somme)
# [[8, 10, 12], [14, 16, 18]]

# Transposition
matrice = [[1, 2, 3], [4, 5, 6]]
transposee = [[ligne[i] for ligne in matrice] for i in range(len(matrice[0]))]
print(transposee)
# [[1, 4], [2, 5], [3, 6]]
```

---

## Récapitulatif

| Type | Syntaxe | Résultat | Utilisation |
|------|---------|----------|-------------|
| **Liste** | `[expr for x in iter]` | `list` | Collection ordonnée |
| **Dictionnaire** | `{k: v for x in iter}` | `dict` | Paires clé-valeur |
| **Set** | `{expr for x in iter}` | `set` | Éléments uniques |
| **Générateur** | `(expr for x in iter)` | `generator` | Itération paresseuse |

### Syntaxe avec filtres

```python
# Filtre simple
[expr for x in iter if condition]

# Transformation conditionnelle
[expr_if if condition else expr_else for x in iter]

# Plusieurs boucles
[expr for x in iter1 for y in iter2]

# Combinaison
[expr for x in iter1 for y in iter2 if condition]
```

---

## Conclusion

Les compréhensions sont un outil puissant qui rend votre code Python plus concis et élégant. Cependant, n'oubliez jamais que **la lisibilité compte plus que la concision**.

**Points clés à retenir :**
- Les compréhensions sont idéales pour transformer et filtrer des collections
- Elles sont plus performantes que les boucles équivalentes
- Utilisez-les quand elles améliorent la lisibilité, pas systématiquement
- Pour des logiques complexes, une boucle traditionnelle est souvent plus claire
- Les expressions génératrices sont utiles pour économiser de la mémoire

Avec de la pratique, vous développerez une intuition pour savoir quand utiliser les compréhensions et quand opter pour des boucles traditionnelles. L'objectif est toujours d'écrire du code que vous et d'autres développeurs pourrez comprendre facilement !

⏭️ [Collections spécialisées (namedtuple, defaultdict, Counter)](/02-structures-de-donnees/03-collections-specialisees.md)
