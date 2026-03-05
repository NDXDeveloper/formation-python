🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.4 Fonctions et portée des variables

## Introduction

Les fonctions sont l'un des concepts les plus importants en programmation. Elles permettent de :
- **Réutiliser du code** : écrire une fois, utiliser plusieurs fois
- **Organiser le code** : diviser un programme complexe en parties plus petites
- **Rendre le code plus lisible** : donner des noms significatifs à des blocs de code
- **Faciliter la maintenance** : modifier une seule fonction plutôt que du code dispersé

Imaginez les fonctions comme des recettes de cuisine : au lieu de répéter toutes les étapes chaque fois que vous voulez faire un gâteau, vous créez une recette "faire_gateau()" que vous pouvez réutiliser à volonté !

---

## Qu'est-ce qu'une Fonction ?

Une **fonction** est un bloc de code réutilisable qui effectue une tâche spécifique. Elle peut :
- Recevoir des données en entrée (paramètres)
- Effectuer des opérations
- Retourner un résultat (optionnel)

En Python, vous utilisez déjà des fonctions sans le savoir : `print()`, `len()`, `input()`, `range()`, etc. Ce sont des fonctions **intégrées** (built-in). Maintenant, vous allez apprendre à créer vos propres fonctions !

---

## Créer une Fonction Simple

### Syntaxe de base

```python
def nom_fonction():
    # Code de la fonction
    instruction1
    instruction2
```

**Éléments** :
- `def` : mot-clé pour définir une fonction
- `nom_fonction` : le nom que vous donnez à la fonction
- `()` : parenthèses pour les paramètres (vides si aucun paramètre)
- `:` : deux points obligatoires
- **Indentation** : le corps de la fonction doit être indenté (4 espaces)

### Premier exemple

```python
def dire_bonjour():
    print("Bonjour !")
    print("Comment allez-vous ?")

# Appeler (exécuter) la fonction
dire_bonjour()
```

**Résultat** :
```
Bonjour !  
Comment allez-vous ?  
```

### Réutilisation

La force des fonctions est qu'on peut les appeler plusieurs fois :

```python
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()  
dire_bonjour()  
dire_bonjour()  
```

**Résultat** :
```
Bonjour !  
Bonjour !  
Bonjour !  
```

---

## Fonctions avec Paramètres

Les **paramètres** permettent de passer des informations à une fonction.

### Un seul paramètre

```python
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Alice")  
saluer("Bob")  
saluer("Charlie")  
```

**Résultat** :
```
Bonjour Alice !  
Bonjour Bob !  
Bonjour Charlie !  
```

Ici, `nom` est un **paramètre** : une variable qui reçoit une valeur quand on appelle la fonction.

### Plusieurs paramètres

```python
def saluer_complet(prenom, nom):
    print(f"Bonjour {prenom} {nom} !")

saluer_complet("Alice", "Dupont")  
saluer_complet("Bob", "Martin")  
```

**Résultat** :
```
Bonjour Alice Dupont !  
Bonjour Bob Martin !  
```

### Paramètres et calculs

```python
def additionner(a, b):
    somme = a + b
    print(f"{a} + {b} = {somme}")

additionner(5, 3)  
additionner(10, 20)  
```

**Résultat** :
```
5 + 3 = 8
10 + 20 = 30
```

### Attention à l'ordre des paramètres

```python
def diviser(dividende, diviseur):
    resultat = dividende / diviseur
    print(f"{dividende} / {diviseur} = {resultat}")

diviser(10, 2)  # 10 / 2 = 5.0  
diviser(2, 10)  # 2 / 10 = 0.2 (ordre différent !)  
```

---

## L'instruction `return` (Retourner une Valeur)

Au lieu d'afficher un résultat avec `print()`, une fonction peut **retourner** une valeur avec `return`. Cette valeur peut ensuite être utilisée ailleurs dans le programme.

### Syntaxe

```python
def nom_fonction():
    # Code
    return valeur
```

### Exemple simple

```python
def additionner(a, b):
    resultat = a + b
    return resultat

# Utiliser la valeur retournée
somme = additionner(5, 3)  
print(somme)  # Affiche : 8  

# On peut l'utiliser dans un calcul
total = additionner(10, 20) + additionner(5, 5)  
print(total)  # Affiche : 40 (30 + 10)  
```

### Différence entre print() et return

**Avec print()** : affiche mais ne renvoie rien
```python
def additionner_print(a, b):
    print(a + b)

resultat = additionner_print(5, 3)  # Affiche : 8  
print(resultat)  # Affiche : None (la fonction ne retourne rien !)  
```

**Avec return** : renvoie une valeur utilisable
```python
def additionner_return(a, b):
    return a + b

resultat = additionner_return(5, 3)  # Ne s'affiche pas automatiquement  
print(resultat)  # Affiche : 8  
```

### Retourner différents types

```python
def est_majeur(age):
    return age >= 18

def obtenir_info():
    return "Alice", 25, "France"

# Utilisation
majeur = est_majeur(20)  
print(majeur)  # Affiche : True  

nom, age, pays = obtenir_info()  
print(f"{nom}, {age} ans, {pays}")  # Affiche : Alice, 25 ans, France  
```

### Return arrête l'exécution de la fonction

```python
def verifier_age(age):
    if age < 0:
        return "Âge invalide"

    if age < 18:
        return "Mineur"

    return "Majeur"

print(verifier_age(25))   # Affiche : Majeur  
print(verifier_age(15))   # Affiche : Mineur  
print(verifier_age(-5))   # Affiche : Âge invalide  
```

Une fois qu'un `return` est exécuté, la fonction s'arrête immédiatement et aucun code après n'est exécuté.

### Fonction sans return explicite

Si une fonction n'a pas de `return`, elle retourne automatiquement `None` :

```python
def dire_bonjour():
    print("Bonjour !")

resultat = dire_bonjour()  
print(resultat)  # Affiche : None  
```

---

## Paramètres par Défaut

Vous pouvez donner des valeurs par défaut aux paramètres. Si aucune valeur n'est fournie lors de l'appel, la valeur par défaut est utilisée.

### Syntaxe

```python
def saluer(nom, message="Bonjour"):
    print(f"{message} {nom} !")

saluer("Alice")              # Utilise la valeur par défaut  
saluer("Bob", "Bonsoir")     # Remplace la valeur par défaut  
```

**Résultat** :
```
Bonjour Alice !  
Bonsoir Bob !  
```

### Exemples pratiques

```python
def puissance(nombre, exposant=2):
    return nombre ** exposant

print(puissance(5))        # 5^2 = 25  
print(puissance(5, 3))     # 5^3 = 125  
print(puissance(2, 10))    # 2^10 = 1024  
```

```python
def afficher_info(nom, age, ville="Paris"):
    print(f"{nom}, {age} ans, habite à {ville}")

afficher_info("Alice", 25)              # Paris par défaut  
afficher_info("Bob", 30, "Lyon")        # Ville spécifiée  
```

### Règle importante

Les paramètres **avec** valeur par défaut doivent venir **après** les paramètres **sans** valeur par défaut :

```python
# ✅ Correct
def fonction(a, b, c=10):
    pass

# ❌ Incorrect
def fonction(a, b=10, c):  # SyntaxError !
    pass
```

---

## Arguments Nommés (Keyword Arguments)

Lors de l'appel d'une fonction, vous pouvez spécifier les paramètres par leur nom. Cela rend le code plus lisible et permet de changer l'ordre des arguments.

### Syntaxe

```python
def presenter(nom, age, ville):
    print(f"{nom}, {age} ans, {ville}")

# Appel avec arguments positionnels (ordre important)
presenter("Alice", 25, "Paris")

# Appel avec arguments nommés (ordre n'importe pas)
presenter(ville="Lyon", nom="Bob", age=30)  
presenter(age=35, ville="Marseille", nom="Charlie")  
```

**Résultat** :
```
Alice, 25 ans, Paris  
Bob, 30 ans, Lyon  
Charlie, 35 ans, Marseille  
```

### Mélanger positionnels et nommés

Vous pouvez combiner les deux, mais les **arguments positionnels doivent venir en premier** :

```python
def creer_profil(nom, age, ville="Paris", pays="France"):
    print(f"{nom}, {age} ans, {ville}, {pays}")

# ✅ Correct
creer_profil("Alice", 25)  
creer_profil("Bob", 30, ville="Lyon")  
creer_profil("Charlie", 35, pays="Belgique")  
creer_profil("David", 40, "Marseille", pays="France")  

# ❌ Incorrect
# creer_profil(nom="Eve", 28)  # SyntaxError (argument positionnel après nommé)
```

---

## Nombre Variable d'Arguments

### *args : Arguments positionnels variables

Si vous ne savez pas combien d'arguments seront passés, utilisez `*args` :

```python
def additionner(*nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total

print(additionner(1, 2, 3))           # Affiche : 6  
print(additionner(10, 20, 30, 40))    # Affiche : 100  
print(additionner(5))                  # Affiche : 5  
```

`*args` crée un **tuple** contenant tous les arguments positionnels.

### **kwargs : Arguments nommés variables

Pour un nombre variable d'arguments **nommés**, utilisez `**kwargs` :

```python
def afficher_infos(**informations):
    for cle, valeur in informations.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=25, ville="Paris")
```

**Résultat** :
```
nom: Alice  
age: 25  
ville: Paris  
```

`**kwargs` crée un **dictionnaire** contenant tous les arguments nommés.

### Combiner paramètres normaux, *args et **kwargs

```python
def fonction_complete(param1, param2, *args, option1="défaut", **kwargs):
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    print(f"args: {args}")
    print(f"option1: {option1}")
    print(f"kwargs: {kwargs}")

fonction_complete(1, 2, 3, 4, 5, option1="test", extra1="a", extra2="b")
```

**Résultat** :
```
param1: 1  
param2: 2  
args: (3, 4, 5)  
option1: test  
kwargs: {'extra1': 'a', 'extra2': 'b'}  
```

**Ordre obligatoire** : paramètres normaux, `*args`, paramètres avec défaut, `**kwargs`

---

## Documentation des Fonctions (Docstrings)

Une **docstring** est une chaîne de documentation qui décrit ce que fait une fonction. Elle se place juste après la définition de la fonction, entre triple guillemets.

### Syntaxe

```python
def ma_fonction(parametre):
    """
    Description de ce que fait la fonction.

    Paramètres:
        parametre: description du paramètre

    Retourne:
        description de la valeur de retour
    """
    # Code de la fonction
    pass
```

### Exemples

```python
def calculer_aire_rectangle(longueur, largeur):
    """
    Calcule l'aire d'un rectangle.

    Paramètres:
        longueur (float): La longueur du rectangle
        largeur (float): La largeur du rectangle

    Retourne:
        float: L'aire du rectangle
    """
    return longueur * largeur
```

```python
def est_palindrome(texte):
    """
    Vérifie si un texte est un palindrome.

    Un palindrome est un mot qui se lit de la même façon
    dans les deux sens (ex: "kayak", "radar").

    Paramètres:
        texte (str): Le texte à vérifier

    Retourne:
        bool: True si le texte est un palindrome, False sinon
    """
    texte = texte.lower().replace(" ", "")
    return texte == texte[::-1]
```

### Accéder à la docstring

```python
def dire_bonjour(nom):
    """Affiche un message de salutation."""
    print(f"Bonjour {nom} !")

# Afficher la docstring
print(dire_bonjour.__doc__)
# Ou utiliser help()
help(dire_bonjour)
```

---

## Portée des Variables (Scope)

La **portée** (scope) d'une variable détermine où cette variable peut être utilisée dans votre programme.

### Variables Locales

Une variable créée **à l'intérieur** d'une fonction est **locale** : elle n'existe que dans cette fonction.

```python
def ma_fonction():
    x = 10  # Variable locale
    print(f"Dans la fonction : x = {x}")

ma_fonction()
# print(x)  # ❌ Erreur ! x n'existe pas en dehors de la fonction
```

### Variables Globales

Une variable créée **en dehors** de toute fonction est **globale** : elle peut être lue partout.

```python
x = 10  # Variable globale

def afficher_x():
    print(f"x = {x}")  # On peut lire x

afficher_x()  # Affiche : x = 10  
print(x)      # Affiche : 10  
```

### Modification d'une variable globale

Par défaut, on ne peut pas **modifier** une variable globale depuis une fonction. Python créera une nouvelle variable locale à la place :

```python
x = 10  # Variable globale

def modifier_x():
    x = 20  # Crée une nouvelle variable LOCALE x
    print(f"Dans la fonction : x = {x}")

modifier_x()  # Affiche : Dans la fonction : x = 20  
print(f"En dehors : x = {x}")  # Affiche : En dehors : x = 10 (inchangé !)  
```

Pour **vraiment modifier** une variable globale, utilisez le mot-clé `global` :

```python
x = 10  # Variable globale

def modifier_x_global():
    global x  # Indique qu'on veut modifier la variable globale
    x = 20
    print(f"Dans la fonction : x = {x}")

modifier_x_global()  # Affiche : Dans la fonction : x = 20  
print(f"En dehors : x = {x}")  # Affiche : En dehors : x = 20 (modifié !)  
```

### Bonne pratique : éviter les variables globales

L'utilisation de `global` est généralement **déconseillée** car elle rend le code difficile à comprendre et à déboguer. Préférez passer des paramètres et retourner des valeurs :

```python
# ❌ Avec variable globale (pas recommandé)
compteur = 0

def incrementer():
    global compteur
    compteur += 1

# ✅ Avec paramètres et retour (recommandé)
def incrementer(compteur):
    return compteur + 1

compteur = 0  
compteur = incrementer(compteur)  
```

### Règles de résolution des noms (LEGB)

Python cherche les variables dans cet ordre :
1. **L**ocal : dans la fonction actuelle
2. **E**nclosing : dans les fonctions englobantes (si imbriquées)
3. **G**lobal : au niveau du module
4. **B**uilt-in : fonctions intégrées de Python

```python
x = "global"

def externe():
    x = "enclosing"

    def interne():
        x = "local"
        print(x)

    interne()
    print(x)

externe()  
print(x)  
```

**Résultat** :
```
local  
enclosing  
global  
```

---

## Fonctions Imbriquées

Vous pouvez définir des fonctions **à l'intérieur** d'autres fonctions.

```python
def fonction_externe():
    print("Dans fonction_externe")

    def fonction_interne():
        print("Dans fonction_interne")

    fonction_interne()  # Appel de la fonction interne

fonction_externe()
# fonction_interne()  # ❌ Erreur ! fonction_interne n'existe qu'à l'intérieur
```

**Résultat** :
```
Dans fonction_externe  
Dans fonction_interne  
```

### Utilité des fonctions imbriquées

Les fonctions imbriquées sont utiles pour :
- Organiser le code
- Créer des fonctions auxiliaires privées
- Créer des closures (concept avancé)

```python
def creer_salutation(salut):
    def saluer(nom):
        return f"{salut} {nom} !"

    return saluer

# Créer des fonctions personnalisées
bonjour = creer_salutation("Bonjour")  
bonsoir = creer_salutation("Bonsoir")  
hello = creer_salutation("Hello")  

print(bonjour("Alice"))   # Affiche : Bonjour Alice !  
print(bonsoir("Bob"))     # Affiche : Bonsoir Bob !  
print(hello("Charlie"))   # Affiche : Hello Charlie !  
```

---

## Fonctions comme Objets de Première Classe

En Python, les fonctions sont des **objets**. Cela signifie qu'on peut :
- Assigner une fonction à une variable
- Passer une fonction en paramètre
- Retourner une fonction depuis une fonction

### Assigner une fonction à une variable

```python
def dire_bonjour(nom):
    return f"Bonjour {nom} !"

# Assigner la fonction à une variable
salutation = dire_bonjour

# Utiliser la variable comme une fonction
print(salutation("Alice"))  # Affiche : Bonjour Alice !
```

### Passer une fonction en paramètre

```python
def appliquer_operation(fonction, valeur):
    return fonction(valeur)

def doubler(x):
    return x * 2

def tripler(x):
    return x * 3

print(appliquer_operation(doubler, 5))  # Affiche : 10  
print(appliquer_operation(tripler, 5))  # Affiche : 15  
```

### Exemple pratique : fonction de transformation

```python
def transformer_liste(liste, fonction):
    resultat = []
    for element in liste:
        resultat.append(fonction(element))
    return resultat

def carre(x):
    return x ** 2

def double(x):
    return x * 2

nombres = [1, 2, 3, 4, 5]

print(transformer_liste(nombres, carre))   # [1, 4, 9, 16, 25]  
print(transformer_liste(nombres, double))  # [2, 4, 6, 8, 10]  
```

---

## Fonctions Récursives

Une fonction **récursive** est une fonction qui s'appelle elle-même. C'est utile pour résoudre certains problèmes de manière élégante.

### Structure d'une fonction récursive

Toute fonction récursive doit avoir :
1. **Un cas de base** : condition d'arrêt
2. **Un appel récursif** : la fonction s'appelle elle-même avec des paramètres différents

### Exemple : Factorielle

```python
def factorielle(n):
    # Cas de base
    if n == 0 or n == 1:
        return 1

    # Appel récursif
    return n * factorielle(n - 1)

print(factorielle(5))  # 5! = 5 × 4 × 3 × 2 × 1 = 120  
print(factorielle(0))  # 0! = 1  
```

**Comment ça marche ?**
```
factorielle(5)
= 5 * factorielle(4)
= 5 * (4 * factorielle(3))
= 5 * (4 * (3 * factorielle(2)))
= 5 * (4 * (3 * (2 * factorielle(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

### Exemple : Suite de Fibonacci

```python
def fibonacci(n):
    # Cas de base
    if n <= 1:
        return n

    # Appel récursif
    return fibonacci(n - 1) + fibonacci(n - 2)

# Afficher les 10 premiers nombres de Fibonacci
for i in range(10):
    print(fibonacci(i), end=" ")
# Affiche : 0 1 1 2 3 5 8 13 21 34
```

### Exemple : Somme des éléments d'une liste

```python
def somme_recursive(liste):
    # Cas de base : liste vide
    if len(liste) == 0:
        return 0

    # Appel récursif : premier élément + somme du reste
    return liste[0] + somme_recursive(liste[1:])

nombres = [1, 2, 3, 4, 5]  
print(somme_recursive(nombres))  # Affiche : 15  
```

### ⚠️ Attention : limite de récursion

Python a une limite au nombre d'appels récursifs (par défaut environ 1000). Pour des valeurs élevées, préférez une approche itérative :

```python
# Version récursive (limitée)
def factorielle_recursive(n):
    if n <= 1:
        return 1
    return n * factorielle_recursive(n - 1)

# Version itérative (pas de limite)
def factorielle_iterative(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat
```

---

## Fonctions Lambda (Fonctions Anonymes)

Une **fonction lambda** est une petite fonction anonyme (sans nom) définie sur une seule ligne.

### Syntaxe

```python
lambda parametres: expression
```

### Exemples simples

```python
# Fonction normale
def doubler(x):
    return x * 2

# Équivalent en lambda
doubler_lambda = lambda x: x * 2

print(doubler(5))         # Affiche : 10  
print(doubler_lambda(5))  # Affiche : 10  
```

### Lambda avec plusieurs paramètres

```python
additionner = lambda a, b: a + b  
print(additionner(3, 5))  # Affiche : 8  

maximum = lambda a, b: a if a > b else b  
print(maximum(10, 20))  # Affiche : 20  
```

### Utilisation typique : avec des fonctions d'ordre supérieur

Les lambdas sont souvent utilisées comme arguments de fonctions comme `map()`, `filter()`, `sorted()` :

```python
nombres = [1, 2, 3, 4, 5]

# Doubler chaque nombre
doubles = list(map(lambda x: x * 2, nombres))  
print(doubles)  # [2, 4, 6, 8, 10]  

# Garder seulement les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))  
print(pairs)  # [2, 4]  

# Trier des tuples par le deuxième élément
personnes = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]  
par_age = sorted(personnes, key=lambda p: p[1])  
print(par_age)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]  
```

### Quand utiliser lambda ?

✅ **Bon usage** : fonction simple et courte utilisée une seule fois
```python
nombres.sort(key=lambda x: x % 10)  # Trier par dernier chiffre
```

❌ **Mauvais usage** : fonction complexe ou réutilisée plusieurs fois
```python
# Trop complexe pour un lambda
# calcul = lambda x: x ** 2 + 2 * x + 1 if x > 0 else -x

# Mieux : fonction normale
def calcul(x):
    if x > 0:
        return x ** 2 + 2 * x + 1
    else:
        return -x
```

---

## Annotations de Type (Type Hints)

Python permet d'ajouter des **annotations de type** pour indiquer le type attendu des paramètres et du retour. Ces annotations n'ont **aucun effet** sur l'exécution (Python reste dynamique), mais elles améliorent la lisibilité et permettent aux outils (comme mypy) de détecter des erreurs.

### Syntaxe de base

```python
def fonction(parametre: type) -> type_retour:
    pass
```

### Exemples

```python
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres entiers."""
    return a + b

def saluer(nom: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {nom} !"

def diviser(a: float, b: float) -> float:
    """Divise deux nombres."""
    return a / b
```

### Types complexes

Depuis Python 3.10, les types génériques s'écrivent directement avec les types natifs (plus besoin d'importer depuis `typing`) :

```python
def traiter_nombres(nombres: list[int]) -> int:
    """Retourne la somme d'une liste d'entiers."""
    return sum(nombres)

def obtenir_info() -> tuple[str, int]:
    """Retourne un tuple (nom, age)."""
    return "Alice", 25

def chercher_utilisateur(id: int) -> dict[str, str] | None:
    """
    Cherche un utilisateur par ID.
    Retourne un dictionnaire ou None si non trouvé.
    """
    # ... code de recherche ...
    return None  # ou un dictionnaire
```

> 💡 La syntaxe `X | None` remplace l'ancien `Optional[X]` depuis Python 3.10. Elle se lit "X ou None".

### Types pour paramètres avec valeur par défaut

```python
def creer_message(texte: str, majuscules: bool = False) -> str:
    if majuscules:
        return texte.upper()
    return texte
```

### Types pour *args et **kwargs

```python
def somme(*nombres: int) -> int:
    return sum(nombres)

def afficher_info(**infos: str) -> None:
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")
```

**Note** : `None` comme type de retour indique que la fonction ne retourne rien (ou retourne `None`).

---

## Bonnes Pratiques pour les Fonctions

### 1. Une fonction = une tâche

Chaque fonction devrait faire **une seule chose** et la faire bien.

✅ **Bon**
```python
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

def afficher_moyenne(moyenne):
    print(f"Moyenne : {moyenne:.2f}")
```

❌ **Mauvais** (fait trop de choses)
```python
def calculer_et_afficher(notes):
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne : {moyenne:.2f}")
    if moyenne >= 10:
        print("Admis")
    else:
        print("Recalé")
```

### 2. Noms descriptifs

Utilisez des verbes pour les noms de fonctions :

✅ **Bon**
```python
def calculer_total(prix, quantite):
    return prix * quantite

def valider_email(email):
    return "@" in email
```

❌ **Mauvais**
```python
def total(p, q):
    return p * q

def email(e):
    return "@" in e
```

### 3. Limiter le nombre de paramètres

Idéalement, une fonction ne devrait pas avoir plus de 3-4 paramètres. Au-delà, considérez regrouper les paramètres dans un dictionnaire ou une classe.

✅ **Bon**
```python
def creer_utilisateur(infos: dict):
    nom = infos["nom"]
    age = infos["age"]
    email = infos["email"]
    # ...
```

❌ **Moins bon** (trop de paramètres)
```python
def creer_utilisateur(nom, prenom, age, email, telephone, adresse, ville, code_postal):
    # ...
```

### 4. Utiliser des valeurs par défaut intelligentes

```python
def lire_fichier(chemin, encodage="utf-8", mode="r"):
    with open(chemin, mode, encoding=encodage) as f:
        return f.read()
```

### 5. Éviter les effets de bord

Une fonction devrait idéalement ne pas modifier les variables globales ou les objets mutables passés en paramètre.

✅ **Bon** (pas d'effet de bord)
```python
def ajouter_element(liste, element):
    nouvelle_liste = liste.copy()
    nouvelle_liste.append(element)
    return nouvelle_liste
```

❌ **À éviter** (modifie l'argument)
```python
def ajouter_element(liste, element):
    liste.append(element)  # Modifie la liste originale !
    return liste
```

### 6. Retourner tôt (early return)

Si possible, traitez les cas d'erreur en premier avec des `return` précoces :

✅ **Bon**
```python
def calculer_moyenne(notes):
    if not notes:
        return 0

    if any(note < 0 or note > 20 for note in notes):
        return None

    return sum(notes) / len(notes)
```

❌ **Moins lisible**
```python
def calculer_moyenne(notes):
    if notes:
        if all(0 <= note <= 20 for note in notes):
            return sum(notes) / len(notes)
        else:
            return None
    else:
        return 0
```

### 7. Documentation avec docstrings

Toute fonction non triviale devrait avoir une docstring :

```python
def calculer_imc(poids: float, taille: float) -> float:
    """
    Calcule l'Indice de Masse Corporelle.

    Paramètres:
        poids (float): Poids en kilogrammes
        taille (float): Taille en mètres

    Retourne:
        float: L'IMC calculé

    Exemple:
        >>> calculer_imc(70, 1.75)
        22.86
    """
    return poids / (taille ** 2)
```

---

## Exemples Pratiques Complets

### Exemple 1 : Validateur d'email

```python
def valider_email(email: str) -> bool:
    """
    Vérifie si un email est valide (vérification basique).

    Paramètres:
        email (str): L'adresse email à valider

    Retourne:
        bool: True si l'email semble valide, False sinon
    """
    if not email:
        return False

    if email.count("@") != 1:
        return False

    parties = email.split("@")
    if not parties[0] or not parties[1]:
        return False

    if "." not in parties[1]:
        return False

    return True

# Tests
print(valider_email("alice@example.com"))  # True  
print(valider_email("bob@"))               # False  
print(valider_email("charlie"))            # False  
```

### Exemple 2 : Calculateur de prix avec remise

```python
def calculer_prix_final(prix_ht: float,
                       quantite: int = 1,
                       taux_remise: float = 0,
                       taux_tva: float = 0.20) -> dict:
    """
    Calcule le prix final avec remise et TVA.

    Paramètres:
        prix_ht (float): Prix unitaire hors taxe
        quantite (int): Nombre d'articles
        taux_remise (float): Taux de remise (0.1 = 10%)
        taux_tva (float): Taux de TVA (0.2 = 20%)

    Retourne:
        dict: Détails du calcul (prix_ht, remise, prix_ttc, etc.)
    """
    montant_ht = prix_ht * quantite
    montant_remise = montant_ht * taux_remise
    montant_ht_apres_remise = montant_ht - montant_remise
    montant_tva = montant_ht_apres_remise * taux_tva
    montant_ttc = montant_ht_apres_remise + montant_tva

    return {
        "prix_unitaire_ht": prix_ht,
        "quantite": quantite,
        "montant_ht": montant_ht,
        "taux_remise": taux_remise,
        "montant_remise": montant_remise,
        "montant_ht_apres_remise": montant_ht_apres_remise,
        "montant_tva": montant_tva,
        "montant_ttc": montant_ttc
    }

# Utilisation
resultat = calculer_prix_final(100, quantite=5, taux_remise=0.1)  
print(f"Prix TTC : {resultat['montant_ttc']:.2f}€")  
```

### Exemple 3 : Générateur de mot de passe

```python
import random  
import string  

def generer_mot_de_passe(longueur: int = 12,
                         avec_majuscules: bool = True,
                         avec_chiffres: bool = True,
                         avec_symboles: bool = True) -> str:
    """
    Génère un mot de passe aléatoire.

    Paramètres:
        longueur (int): Longueur du mot de passe
        avec_majuscules (bool): Inclure des majuscules
        avec_chiffres (bool): Inclure des chiffres
        avec_symboles (bool): Inclure des symboles

    Retourne:
        str: Le mot de passe généré
    """
    caracteres = string.ascii_lowercase

    if avec_majuscules:
        caracteres += string.ascii_uppercase

    if avec_chiffres:
        caracteres += string.digits

    if avec_symboles:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

# Tests
print(generer_mot_de_passe())  
print(generer_mot_de_passe(8, avec_symboles=False))  
print(generer_mot_de_passe(16))  
```

### Exemple 4 : Calculateur de statistiques

```python
def calculer_statistiques(nombres: list) -> dict:
    """
    Calcule diverses statistiques sur une liste de nombres.

    Paramètres:
        nombres (list): Liste de nombres

    Retourne:
        dict: Dictionnaire contenant les statistiques
    """
    if not nombres:
        return None

    nombres_tries = sorted(nombres)
    n = len(nombres)

    # Moyenne
    moyenne = sum(nombres) / n

    # Médiane
    if n % 2 == 0:
        mediane = (nombres_tries[n//2 - 1] + nombres_tries[n//2]) / 2
    else:
        mediane = nombres_tries[n//2]

    # Min et Max
    minimum = min(nombres)
    maximum = max(nombres)

    # Étendue
    etendue = maximum - minimum

    return {
        "nombre_valeurs": n,
        "moyenne": moyenne,
        "mediane": mediane,
        "minimum": minimum,
        "maximum": maximum,
        "etendue": etendue
    }

# Utilisation
notes = [12, 15, 10, 18, 14, 16, 11, 13]  
stats = calculer_statistiques(notes)  

for cle, valeur in stats.items():
    print(f"{cle}: {valeur}")
```

---

## Erreurs Courantes à Éviter

### 1. Oublier le return

❌ **Erreur**
```python
def additionner(a, b):
    somme = a + b
    # Oublié de retourner la somme !

resultat = additionner(5, 3)  
print(resultat)  # Affiche : None  
```

✅ **Correct**
```python
def additionner(a, b):
    return a + b
```

### 2. Modifier un argument mutable

❌ **Problème** (modifie l'original)
```python
def ajouter_element(liste, element):
    liste.append(element)
    return liste

ma_liste = [1, 2, 3]  
nouvelle_liste = ajouter_element(ma_liste, 4)  
print(ma_liste)  # [1, 2, 3, 4] - modifié !  
```

✅ **Mieux**
```python
def ajouter_element(liste, element):
    nouvelle = liste.copy()
    nouvelle.append(element)
    return nouvelle
```

### 3. Valeur par défaut mutable

❌ **Erreur classique**
```python
def ajouter_a_liste(element, liste=[]):
    liste.append(element)
    return liste

print(ajouter_a_liste(1))  # [1]  
print(ajouter_a_liste(2))  # [1, 2] - la liste est partagée !  
```

✅ **Correct**
```python
def ajouter_a_liste(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste
```

### 4. Variables globales mal utilisées

❌ **Mauvais**
```python
compteur = 0

def incrementer():
    global compteur
    compteur += 1
```

✅ **Mieux**
```python
def incrementer(valeur):
    return valeur + 1

compteur = 0  
compteur = incrementer(compteur)  
```

---

## Récapitulatif

Dans cette section, nous avons appris :

✅ **Définir des fonctions** : avec `def`, paramètres et `return`  
✅ **Paramètres** : positionnels, par défaut, nommés, *args, **kwargs  
✅ **Portée des variables** : locales vs globales, règle LEGB  
✅ **Fonctions imbriquées** : fonctions dans des fonctions  
✅ **Fonctions de première classe** : passer et retourner des fonctions  
✅ **Récursivité** : fonctions qui s'appellent elles-mêmes  
✅ **Fonctions lambda** : fonctions anonymes courtes  
✅ **Annotations de type** : type hints pour améliorer la lisibilité  
✅ **Docstrings** : documenter vos fonctions  
✅ **Bonnes pratiques** : code propre et maintenable

---

## Points Clés à Retenir

1. **Les fonctions réutilisent le code** : écrivez une fois, utilisez partout
2. **return retourne une valeur** : différent de print()
3. **Les paramètres permettent de personnaliser** : fonctions flexibles
4. **Préférez des fonctions pures** : évitez les effets de bord
5. **Une fonction = une tâche** : gardez vos fonctions simples et focalisées
6. **Documentez avec docstrings** : aidez les autres (et vous-même) à comprendre
7. **Les variables locales sont préférables** : évitez global
8. **Les annotations de type aident** : mais ne sont pas obligatoires

---

Vous maîtrisez maintenant les fonctions et la portée des variables ! Dans la prochaine section, nous découvrirons comment gérer les erreurs de manière élégante avec les exceptions.


⏭️ [Gestion des erreurs avec try/except](/01-fondamentaux-et-syntaxe/05-gestion-des-erreurs.md)
