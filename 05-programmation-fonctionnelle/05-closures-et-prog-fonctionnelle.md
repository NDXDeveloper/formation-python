🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.5 Closures et programmation fonctionnelle

## Introduction

Les **closures** (fermetures) sont un concept puissant de la programmation fonctionnelle qui permet à une fonction de "se souvenir" de l'environnement dans lequel elle a été créée. Dans ce chapitre, nous allons explorer les closures et découvrir comment Python supporte la programmation fonctionnelle.

Ces concepts peuvent sembler abstraits au début, mais avec des exemples concrets, vous verrez qu'ils sont très utiles et élégants !

---

## Qu'est-ce qu'une closure ?

Une **closure** est une fonction qui :
1. Est définie à l'intérieur d'une autre fonction
2. Référence des variables de la fonction parente
3. Conserve l'accès à ces variables même après que la fonction parente a terminé son exécution

### Premier exemple simple

```python
def creer_salutation(salut):
    """Fonction externe qui crée une closure."""

    def saluer(nom):
        """Fonction interne (la closure)."""
        return f"{salut} {nom} !"

    return saluer

# Créer deux fonctions avec des salutations différentes
saluer_fr = creer_salutation("Bonjour")  
saluer_en = creer_salutation("Hello")  

# Utilisation
print(saluer_fr("Alice"))  # Bonjour Alice !  
print(saluer_en("Bob"))    # Hello Bob !  
```

**Ce qui se passe :**
- `saluer_fr` "se souvient" que `salut` vaut "Bonjour"
- `saluer_en` "se souvient" que `salut` vaut "Hello"
- Chaque closure garde sa propre copie de `salut`

### Visualiser le fonctionnement

```python
def creer_multiplicateur(facteur):
    """Crée une fonction qui multiplie par un facteur donné."""

    def multiplier(nombre):
        return nombre * facteur  # facteur vient de la fonction parente

    return multiplier

# Créer différents multiplicateurs
double = creer_multiplicateur(2)  
triple = creer_multiplicateur(3)  
dizaine = creer_multiplicateur(10)  

# Chaque fonction se souvient de son propre facteur
print(double(5))    # 10 (5 * 2)  
print(triple(5))    # 15 (5 * 3)  
print(dizaine(5))   # 50 (5 * 10)  
```

---

## Variables libres

Les variables de la fonction externe utilisées par la closure sont appelées **variables libres**.

### Inspecter les variables libres

```python
def creer_compteur(debut):
    def incrementer():
        return debut + 1
    return incrementer

compteur = creer_compteur(10)

# Inspecter la closure
print(compteur.__closure__)  # (<cell at 0x...: int object at 0x...>,)  
print(compteur.__code__.co_freevars)  # ('debut',)  

# La valeur de la variable libre
print(compteur.__closure__[0].cell_contents)  # 10
```

### Variables locales vs variables libres

```python
def fonction_externe(x):  # x sera une variable libre
    y = 10  # y sera aussi une variable libre

    def fonction_interne(z):  # z est une variable locale
        return x + y + z  # x et y sont des variables libres

    return fonction_interne

f = fonction_externe(5)  
print(f(3))  # 18 (5 + 10 + 3)  

# Variables libres de la closure
print(f.__code__.co_freevars)  # ('x', 'y')
```

---

## Closures avec état modifiable

Les closures peuvent maintenir et modifier un état interne.

### Compteur simple

```python
def creer_compteur():
    """Crée un compteur qui s'incrémente."""
    compte = 0  # Variable capturée par la closure

    def incrementer():
        nonlocal compte  # Nécessaire pour modifier la variable
        compte += 1
        return compte

    return incrementer

compteur1 = creer_compteur()  
print(compteur1())  # 1  
print(compteur1())  # 2  
print(compteur1())  # 3  

# Chaque compteur est indépendant
compteur2 = creer_compteur()  
print(compteur2())  # 1  
print(compteur1())  # 4  
```

### Le mot-clé nonlocal

Le mot-clé `nonlocal` est essentiel pour modifier une variable de la portée externe :

```python
def exemple_nonlocal():
    x = 10

    def modifier_sans_nonlocal():
        x = 20  # Crée une nouvelle variable locale
        print(f"Dans la fonction : x = {x}")

    modifier_sans_nonlocal()
    print(f"Après la fonction : x = {x}")  # x vaut toujours 10

exemple_nonlocal()
# Dans la fonction : x = 20
# Après la fonction : x = 10

print()

def exemple_avec_nonlocal():
    x = 10

    def modifier_avec_nonlocal():
        nonlocal x  # Modifie la variable de la portée externe
        x = 20
        print(f"Dans la fonction : x = {x}")

    modifier_avec_nonlocal()
    print(f"Après la fonction : x = {x}")  # x vaut maintenant 20

exemple_avec_nonlocal()
# Dans la fonction : x = 20
# Après la fonction : x = 20
```

---

## Cas d'usage pratiques des closures

### 1. Fabrique de fonctions

```python
def creer_puissance(exposant):
    """Crée une fonction qui élève à une puissance donnée."""
    def calculer(base):
        return base ** exposant
    return calculer

carre = creer_puissance(2)  
cube = creer_puissance(3)  
puissance_quatre = creer_puissance(4)  

print(carre(5))           # 25  
print(cube(3))            # 27  
print(puissance_quatre(2)) # 16  
```

### 2. Configuration de fonctions

```python
def creer_formateur(prefixe, suffixe):
    """Crée une fonction de formatage personnalisée."""
    def formater(texte):
        return f"{prefixe}{texte}{suffixe}"
    return formater

# Différents formatages
html_bold = creer_formateur("<b>", "</b>")  
html_italic = creer_formateur("<i>", "</i>")  
parentheses = creer_formateur("(", ")")  

print(html_bold("Important"))      # <b>Important</b>  
print(html_italic("Emphase"))      # <i>Emphase</i>  
print(parentheses("note"))         # (note)  
```

### 3. Encapsulation de données privées

```python
def creer_compte_bancaire(solde_initial):
    """Crée un compte bancaire avec encapsulation."""
    solde = solde_initial  # "Variable privée"

    def deposer(montant):
        nonlocal solde
        if montant > 0:
            solde += montant
            return f"Dépôt de {montant}€. Nouveau solde : {solde}€"
        return "Montant invalide"

    def retirer(montant):
        nonlocal solde
        if 0 < montant <= solde:
            solde -= montant
            return f"Retrait de {montant}€. Nouveau solde : {solde}€"
        return "Montant invalide ou insuffisant"

    def consulter_solde():
        return f"Solde actuel : {solde}€"

    # Retourner un dictionnaire de fonctions
    return {
        'deposer': deposer,
        'retirer': retirer,
        'solde': consulter_solde
    }

# Utilisation
compte = creer_compte_bancaire(1000)  
print(compte['solde']())           # Solde actuel : 1000€  
print(compte['deposer'](500))      # Dépôt de 500€. Nouveau solde : 1500€  
print(compte['retirer'](200))      # Retrait de 200€. Nouveau solde : 1300€  
print(compte['solde']())           # Solde actuel : 1300€  
```

### 4. Décorateurs (utilisation avancée des closures)

```python
def compteur_appels(fonction):
    """Décorateur qui compte les appels d'une fonction."""
    nombre_appels = 0  # Variable capturée

    def wrapper(*args, **kwargs):
        nonlocal nombre_appels
        nombre_appels += 1
        print(f"Appel n°{nombre_appels} de {fonction.__name__}")
        return fonction(*args, **kwargs)

    wrapper.nombre_appels = lambda: nombre_appels  # Accès au compteur
    return wrapper

@compteur_appels
def dire_bonjour(nom):
    return f"Bonjour {nom} !"

print(dire_bonjour("Alice"))  # Appel n°1  
print(dire_bonjour("Bob"))    # Appel n°2  
print(dire_bonjour("Charlie")) # Appel n°3  
print(f"Total d'appels : {dire_bonjour.nombre_appels()}")  # 3  
```

### 5. Callbacks avec contexte

```python
def creer_gestionnaire_evenement(nom_evenement):
    """Crée un gestionnaire d'événement avec contexte."""
    compteur = 0

    def gestionnaire(message):
        nonlocal compteur
        compteur += 1
        print(f"[{nom_evenement}] Événement #{compteur}: {message}")

    return gestionnaire

# Créer différents gestionnaires
on_click = creer_gestionnaire_evenement("CLICK")  
on_hover = creer_gestionnaire_evenement("HOVER")  

# Simulation d'événements
on_click("Bouton pressé")      # [CLICK] Événement #1: Bouton pressé  
on_hover("Souris sur élément") # [HOVER] Événement #1: Souris sur élément  
on_click("Nouveau clic")       # [CLICK] Événement #2: Nouveau clic  
```

---

## Introduction à la programmation fonctionnelle

La **programmation fonctionnelle** est un paradigme de programmation qui traite le calcul comme l'évaluation de fonctions mathématiques. Python supporte ce style de programmation.

### Principes clés

1. **Fonctions comme citoyens de première classe**
2. **Fonctions pures**
3. **Immuabilité**
4. **Composition de fonctions**
5. **Absence d'effets de bord**

---

## Fonctions comme citoyens de première classe

En Python, les fonctions sont des "citoyens de première classe", ce qui signifie qu'elles peuvent être :

### 1. Assignées à des variables

```python
def saluer(nom):
    return f"Bonjour {nom} !"

# Assigner la fonction à une variable
ma_fonction = saluer  
print(ma_fonction("Alice"))  # Bonjour Alice !  
```

### 2. Passées comme arguments

```python
def executer_operation(operation, a, b):
    """Exécute une opération sur deux nombres."""
    return operation(a, b)

def additionner(x, y):
    return x + y

def multiplier(x, y):
    return x * y

print(executer_operation(additionner, 5, 3))  # 8  
print(executer_operation(multiplier, 5, 3))   # 15  
```

### 3. Retournées par d'autres fonctions

```python
def choisir_operation(type_operation):
    """Retourne une fonction selon le type d'opération."""

    def additionner(x, y):
        return x + y

    def soustraire(x, y):
        return x - y

    if type_operation == "addition":
        return additionner
    elif type_operation == "soustraction":
        return soustraire
    else:
        return lambda x, y: 0

operation = choisir_operation("addition")  
print(operation(10, 5))  # 15  
```

### 4. Stockées dans des structures de données

```python
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else None
}

print(operations['+'](10, 5))  # 15  
print(operations['*'](10, 5))  # 50  
```

---

## Fonctions pures

Une **fonction pure** est une fonction qui :
1. Retourne toujours le même résultat pour les mêmes arguments
2. N'a pas d'effets de bord (ne modifie rien en dehors d'elle)

### Exemples de fonctions pures

```python
# ✅ Fonction pure
def additionner(a, b):
    """Toujours le même résultat, pas d'effets de bord."""
    return a + b

print(additionner(3, 4))  # Toujours 7  
print(additionner(3, 4))  # Toujours 7  

# ✅ Fonction pure
def calculer_carre(n):
    """Pure : pas de modification externe."""
    return n * n

# ✅ Fonction pure
def concatener(texte1, texte2):
    """Ne modifie pas les arguments."""
    return texte1 + texte2
```

### Exemples de fonctions impures

```python
compteur_global = 0

# ❌ Fonction impure : modifie une variable globale
def incrementer_impure():
    global compteur_global
    compteur_global += 1
    return compteur_global

# ❌ Fonction impure : résultat dépend de l'état externe
def lire_compteur_impure():
    return compteur_global

# ❌ Fonction impure : effet de bord (print)
def afficher_resultat(x):
    print(f"Résultat : {x}")  # Effet de bord
    return x
```

### Convertir une fonction impure en pure

```python
# ❌ Impure
liste_globale = []

def ajouter_impure(element):
    liste_globale.append(element)  # Modifie l'état externe
    return liste_globale

# ✅ Pure
def ajouter_pure(liste, element):
    """Retourne une nouvelle liste sans modifier l'originale."""
    return liste + [element]

# Utilisation de la version pure
ma_liste = [1, 2, 3]  
nouvelle_liste = ajouter_pure(ma_liste, 4)  
print(ma_liste)         # [1, 2, 3] - Non modifiée  
print(nouvelle_liste)   # [1, 2, 3, 4]  
```

### Avantages des fonctions pures

✅ **Testabilité** : Plus faciles à tester  
✅ **Prévisibilité** : Comportement déterministe  
✅ **Parallélisation** : Peuvent être exécutées en parallèle sans danger  
✅ **Mémorisation** : Résultats peuvent être mis en cache  
✅ **Débogage** : Plus simples à déboguer

---

## Immuabilité

L'**immuabilité** signifie que les données ne peuvent pas être modifiées après leur création.

### Types immuables en Python

```python
# Immuables (ne peuvent pas être modifiés)
nombre = 42  
texte = "Python"  
tuple_exemple = (1, 2, 3)  

# Tentative de modification
# texte[0] = 'p'  # TypeError: 'str' object does not support item assignment
```

### Types mutables en Python

```python
# Mutables (peuvent être modifiés)
liste = [1, 2, 3]  
dictionnaire = {'a': 1}  

# Modification en place
liste.append(4)  # Modifie la liste originale  
dictionnaire['b'] = 2  # Modifie le dictionnaire original  
```

### Travailler de manière immuable

```python
# ❌ Style mutable (modifie en place)
def augmenter_prix_mutable(produits, pourcentage):
    for produit in produits:
        produit['prix'] *= (1 + pourcentage / 100)
    return produits

# ✅ Style immuable (crée de nouveaux objets)
def augmenter_prix_immuable(produits, pourcentage):
    return [
        {**produit, 'prix': produit['prix'] * (1 + pourcentage / 100)}
        for produit in produits
    ]

# Test
produits_originaux = [
    {'nom': 'Pomme', 'prix': 2.5},
    {'nom': 'Banane', 'prix': 1.8}
]

# Version immuable
nouveaux_produits = augmenter_prix_immuable(produits_originaux, 10)  
print("Originaux :", produits_originaux)  # Non modifiés  
print("Nouveaux :", nouveaux_produits)    # Prix augmentés de 10%  
```

### Créer des copies

```python
import copy

# Copie superficielle
liste_originale = [1, 2, [3, 4]]  
copie_superficielle = liste_originale.copy()  
copie_superficielle[2][0] = 99  
print(liste_originale)  # [1, 2, [99, 4]] - La sous-liste est modifiée !  

# Copie profonde
liste_originale = [1, 2, [3, 4]]  
copie_profonde = copy.deepcopy(liste_originale)  
copie_profonde[2][0] = 99  
print(liste_originale)  # [1, 2, [3, 4]] - Non modifiée  
```

---

## Composition de fonctions

La **composition** consiste à combiner plusieurs fonctions pour en créer une nouvelle.

### Composition manuelle

```python
def ajouter_5(x):
    return x + 5

def multiplier_par_2(x):
    return x * 2

def mettre_au_carre(x):
    return x ** 2

# Composer manuellement
nombre = 3  
resultat = mettre_au_carre(multiplier_par_2(ajouter_5(nombre)))  
print(resultat)  # ((3 + 5) * 2)² = (16)² = 256  
```

### Fonction de composition

```python
def composer(*fonctions):
    """Compose plusieurs fonctions de droite à gauche."""
    def fonction_composee(x):
        resultat = x
        for fonction in reversed(fonctions):
            resultat = fonction(resultat)
        return resultat
    return fonction_composee

# Créer une fonction composée
traitement = composer(mettre_au_carre, multiplier_par_2, ajouter_5)  
print(traitement(3))  # 256  
```

### Pipeline de traitement

```python
def creer_pipeline(*fonctions):
    """Crée un pipeline de fonctions (gauche à droite)."""
    def executer(valeur_initiale):
        resultat = valeur_initiale
        for fonction in fonctions:
            resultat = fonction(resultat)
        return resultat
    return executer

# Fonctions de traitement de texte
def mettre_en_majuscules(texte):
    return texte.upper()

def ajouter_points_exclamation(texte):
    return f"{texte}!!!"

def entourer_etoiles(texte):
    return f"*** {texte} ***"

# Créer le pipeline
pipeline_texte = creer_pipeline(
    mettre_en_majuscules,
    ajouter_points_exclamation,
    entourer_etoiles
)

resultat = pipeline_texte("python")  
print(resultat)  # *** PYTHON!!! ***  
```

---

## Curryfication (Currying)

La **curryfication** transforme une fonction à plusieurs arguments en une série de fonctions à un seul argument.

### Concept de base

```python
# Fonction normale
def additionner(a, b):
    return a + b

print(additionner(3, 5))  # 8

# Version currifiée
def additionner_currifie(a):
    def ajouter_b(b):
        return a + b
    return ajouter_b

ajouter_3 = additionner_currifie(3)  
print(ajouter_3(5))  # 8  
print(ajouter_3(10))  # 13  
```

### Curryfication générique

```python
def curryfier(fonction, *args_fixes):
    """Transforme une fonction en version currifiée."""
    def fonction_currifiee(*args_supplementaires):
        return fonction(*args_fixes, *args_supplementaires)
    return fonction_currifiee

# Exemple
def multiplier(a, b, c):
    return a * b * c

# Currification partielle
multiplier_par_2 = curryfier(multiplier, 2)  
print(multiplier_par_2(3, 4))  # 2 * 3 * 4 = 24  

multiplier_par_2_et_3 = curryfier(multiplier, 2, 3)  
print(multiplier_par_2_et_3(5))  # 2 * 3 * 5 = 30  
```

### Application pratique

```python
def creer_url(protocole, domaine, chemin):
    """Construit une URL."""
    return f"{protocole}://{domaine}/{chemin}"

# Créer des fonctions spécialisées
creer_url_https = curryfier(creer_url, "https")  
creer_url_site = curryfier(creer_url, "https", "example.com")  

print(creer_url_https("example.com", "api/users"))  # https://example.com/api/users  
print(creer_url_site("products"))  # https://example.com/products  
```

---

## Application partielle avec functools.partial

Python fournit `functools.partial` pour l'application partielle de fonctions :

```python
from functools import partial

def puissance(base, exposant):
    return base ** exposant

# Créer des fonctions spécialisées
carre = partial(puissance, exposant=2)  
cube = partial(puissance, exposant=3)  

print(carre(5))  # 25  
print(cube(3))   # 27  

# Exemple pratique avec print
print_avec_prefix = partial(print, "[LOG]", sep=" - ")  
print_avec_prefix("Message important")  # [LOG] - Message important  
```

---

## Récursion en programmation fonctionnelle

La **récursion** est naturelle en programmation fonctionnelle.

### Factorielle

```python
def factorielle(n):
    """Calcule la factorielle de manière récursive."""
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # 120
```

### Fibonacci

```python
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Somme d'une liste

```python
def somme_recursive(liste):
    """Calcule la somme des éléments d'une liste."""
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:])

print(somme_recursive([1, 2, 3, 4, 5]))  # 15
```

### Récursion terminale (tail recursion)

```python
def factorielle_tail(n, acc=1):
    """Factorielle avec récursion terminale."""
    if n <= 1:
        return acc
    return factorielle_tail(n - 1, n * acc)

print(factorielle_tail(5))  # 120
```

> ⚠️ **Attention** : contrairement à des langages comme Scheme ou Haskell, Python **n'optimise pas** la récursion terminale. La pile d'appels croît à chaque appel récursif, et la limite par défaut est d'environ 1 000 appels (`sys.getrecursionlimit()`). Pour les grandes valeurs, préférez une version itérative.

---

## Techniques fonctionnelles en Python

### 1. Éviter les boucles avec des fonctions d'ordre supérieur

```python
nombres = [1, 2, 3, 4, 5]

# ❌ Style impératif avec boucle
carres = []  
for n in nombres:  
    carres.append(n ** 2)

# ✅ Style fonctionnel avec map
carres = list(map(lambda x: x ** 2, nombres))

# ✅✅ Style pythonique avec compréhension
carres = [x ** 2 for x in nombres]
```

### 2. Réduire les effets de bord

```python
# ❌ Avec effets de bord
total = 0  
def ajouter_au_total(x):  
    global total
    total += x
    return total

# ✅ Sans effets de bord
def calculer_somme(liste):
    return sum(liste)

print(calculer_somme([1, 2, 3, 4, 5]))  # 15
```

### 3. Utiliser des structures immuables

```python
from collections import namedtuple

# Créer un type immuable
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(3, 4)
# p1.x = 5  # AttributeError: impossible de modifier

# Pour "modifier", créer un nouveau point
p2 = Point(p1.x + 1, p1.y)  
print(p1)  # Point(x=3, y=4)  
print(p2)  # Point(x=4, y=4)  
```

---

## Exemple complet : Traitement fonctionnel de données

```python
from functools import reduce

# Données d'étudiants
etudiants = [
    {"nom": "Alice", "notes": [15, 18, 16, 17]},
    {"nom": "Bob", "notes": [12, 14, 13, 15]},
    {"nom": "Charlie", "notes": [17, 19, 18, 16]},
    {"nom": "David", "notes": [10, 11, 9, 12]},
]

# Style fonctionnel : pipeline de transformations

# 1. Ajouter la moyenne
def ajouter_moyenne(etudiant):
    notes = etudiant['notes']
    moyenne = sum(notes) / len(notes)
    return {**etudiant, 'moyenne': moyenne}

# 2. Filtrer les admis (moyenne >= 12)
def est_admis(etudiant):
    return etudiant['moyenne'] >= 12

# 3. Extraire le nom
def extraire_nom(etudiant):
    return etudiant['nom']

# Pipeline complet
etudiants_avec_moyenne = list(map(ajouter_moyenne, etudiants))  
etudiants_admis = list(filter(est_admis, etudiants_avec_moyenne))  
noms_admis = list(map(extraire_nom, etudiants_admis))  

print("Étudiants admis :", noms_admis)
# Étudiants admis : ['Alice', 'Bob', 'Charlie']

# Version encore plus fonctionnelle
noms_admis = list(map(
    extraire_nom,
    filter(est_admis, map(ajouter_moyenne, etudiants))
))

# Ou avec compréhension (style pythonique)
noms_admis = [
    etudiant['nom']
    for etudiant in etudiants
    if sum(etudiant['notes']) / len(etudiant['notes']) >= 12
]
```

---

## Avantages de la programmation fonctionnelle

### 1. Code plus prévisible

```python
# Fonction pure : toujours le même résultat
def calculer_prix_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva)

# Facile à tester et prévisible
assert calculer_prix_ttc(100, 0.20) == 120
```

### 2. Meilleure testabilité

```python
# Fonctions pures sont faciles à tester
def filtrer_pairs(nombres):
    return [n for n in nombres if n % 2 == 0]

# Tests simples
assert filtrer_pairs([1, 2, 3, 4]) == [2, 4]  
assert filtrer_pairs([]) == []  
```

### 3. Parallélisation simplifiée

```python
from multiprocessing import Pool

def calculer_carre(n):
    """Fonction pure : peut être parallélisée sans danger."""
    return n ** 2

# Parallélisation facile car pas d'effets de bord
# with Pool() as pool:
#     resultats = pool.map(calculer_carre, range(10))
```

### 4. Code plus modulaire

```python
# Petites fonctions réutilisables
def est_pair(n):
    return n % 2 == 0

def est_positif(n):
    return n > 0

def combiner_predicats(pred1, pred2):
    return lambda x: pred1(x) and pred2(x)

est_pair_et_positif = combiner_predicats(est_pair, est_positif)  
nombres = [-2, -1, 0, 1, 2, 3, 4]  
print(list(filter(est_pair_et_positif, nombres)))  # [2, 4]  
```

---

## Limites et compromis

### 1. Performance

```python
# Récursion vs itération
def somme_recursive(liste):
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def somme_iterative(liste):
    total = 0
    for element in liste:
        total += element
    return total

# Pour de grandes listes, la version itérative est plus rapide
```

### 2. Lisibilité

```python
# ❌ Trop fonctionnel peut nuire à la lisibilité
resultat = reduce(
    lambda acc, x: acc + x,
    filter(
        lambda x: x > 0,
        map(lambda x: x ** 2, range(-5, 5))
    ),
    0
)

# ✅ Plus clair avec des étapes
nombres = range(-5, 5)  
carres = [x ** 2 for x in nombres]  
positifs = [x for x in carres if x > 0]  
resultat = sum(positifs)  
```

### 3. Python n'est pas purement fonctionnel

Python supporte la programmation fonctionnelle mais n'est pas un langage purement fonctionnel comme Haskell ou Clojure. Il encourage un style multi-paradigme.

---

## Bonnes pratiques

### 1. Équilibrer fonctionnel et pythonique

```python
# ✅ Bon équilibre
def traiter_donnees(donnees):
    """Traite les données de manière fonctionnelle mais lisible."""
    nettoyees = [d.strip().lower() for d in donnees if d]
    uniques = list(set(nettoyees))
    triees = sorted(uniques)
    return triees
```

### 2. Utiliser les outils de Python

```python
from functools import reduce, partial  
from itertools import chain, starmap  

# Python fournit des outils pour la programmation fonctionnelle
# Utilisez-les quand approprié
```

### 3. Privilégier la clarté

```python
# ❌ Trop dense
f = lambda x: reduce(lambda a, b: a + b, map(lambda y: y ** 2, x))

# ✅ Plus clair
def somme_des_carres(nombres):
    """Calcule la somme des carrés."""
    return sum(n ** 2 for n in nombres)
```

---

## Résumé

Dans ce chapitre, nous avons exploré les closures et la programmation fonctionnelle :

### Closures

**Définition** :
- Fonction interne qui capture des variables de la fonction externe
- "Se souvient" de son environnement de création
- Utilise le mot-clé `nonlocal` pour modifier des variables capturées

**Cas d'usage** :
- Fabrique de fonctions
- Encapsulation de données
- Décorateurs
- Callbacks avec contexte

### Programmation fonctionnelle

**Principes clés** :
- Fonctions comme citoyens de première classe
- Fonctions pures (pas d'effets de bord)
- Immuabilité des données
- Composition de fonctions
- Récursion

**Avantages** :
✅ Code prévisible et testable  
✅ Meilleure modularité  
✅ Parallélisation facilitée  
✅ Raisonnement simplifié

**Techniques** :
- map(), filter(), reduce()
- Compréhensions de listes
- functools.partial pour curryfication
- Composition de fonctions
- Récursion

### Points à retenir

- Python supporte la programmation fonctionnelle mais n'est pas purement fonctionnel
- Privilégier la lisibilité avant tout
- Combiner les paradigmes selon les besoins
- Les closures sont puissantes pour l'encapsulation
- Les fonctions pures facilitent les tests et la maintenance

La programmation fonctionnelle en Python offre des outils puissants pour écrire du code élégant et maintenable, à utiliser avec discernement selon le contexte !

Ce chapitre conclut notre exploration de la programmation fonctionnelle en Python. Dans les prochains chapitres, nous aborderons les modules et packages pour organiser efficacement votre code.

⏭️ [Modules et packages](/06-modules-et-packages/README.md)
