🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.1 Fonctions lambda et fonctions d'ordre supérieur

## Introduction

Dans ce chapitre, nous allons découvrir deux concepts importants de la programmation fonctionnelle en Python : les **fonctions lambda** (ou fonctions anonymes) et les **fonctions d'ordre supérieur**. Ces concepts permettent d'écrire du code plus concis et expressif.

Ne vous inquiétez pas si ces termes semblent compliqués, nous allons les découvrir étape par étape avec des exemples simples !

---

## Les fonctions lambda

### Qu'est-ce qu'une fonction lambda ?

Une **fonction lambda** est une petite fonction anonyme (sans nom) qui peut être définie en une seule ligne. Elle est particulièrement utile pour des opérations simples que vous n'avez besoin d'utiliser qu'une seule fois.

### Syntaxe de base

```python
lambda arguments: expression
```

- `lambda` : le mot-clé pour déclarer une fonction lambda
- `arguments` : les paramètres de la fonction (comme dans une fonction normale)
- `expression` : une seule expression dont le résultat sera retourné automatiquement

### Comparaison avec une fonction classique

Prenons un exemple simple : une fonction qui additionne deux nombres.

**Avec une fonction classique :**

```python
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # Affiche : 8
```

**Avec une fonction lambda :**

```python
additionner = lambda a, b: a + b

resultat = additionner(5, 3)
print(resultat)  # Affiche : 8
```

Les deux approches donnent le même résultat, mais la lambda est plus concise.

### Exemples de fonctions lambda

#### Exemple 1 : Doubler un nombre

```python
doubler = lambda x: x * 2

print(doubler(5))   # Affiche : 10
print(doubler(12))  # Affiche : 24
```

#### Exemple 2 : Vérifier si un nombre est pair

```python
est_pair = lambda n: n % 2 == 0

print(est_pair(4))   # Affiche : True
print(est_pair(7))   # Affiche : False
```

#### Exemple 3 : Concaténer deux chaînes

```python
saluer = lambda prenom, nom: f"Bonjour {prenom} {nom} !"

print(saluer("Marie", "Dupont"))  # Affiche : Bonjour Marie Dupont !
```

#### Exemple 4 : Trouver le maximum entre deux nombres

```python
maximum = lambda a, b: a if a > b else b

print(maximum(10, 25))  # Affiche : 25
print(maximum(50, 30))  # Affiche : 50
```

### Quand utiliser les fonctions lambda ?

**✅ Utilisez les lambda quand :**
- Vous avez besoin d'une fonction simple et courte
- La fonction n'est utilisée qu'une seule fois
- Vous passez la fonction comme argument à une autre fonction

**❌ Évitez les lambda quand :**
- La logique est complexe (plusieurs lignes nécessaires)
- Vous devez réutiliser la fonction à plusieurs endroits
- Le code devient difficile à lire

---

## Les fonctions d'ordre supérieur

### Qu'est-ce qu'une fonction d'ordre supérieur ?

Une **fonction d'ordre supérieur** est une fonction qui peut :
1. **Prendre une ou plusieurs fonctions comme arguments**
2. **Retourner une fonction comme résultat**

Ce concept est au cœur de la programmation fonctionnelle et permet de créer du code très flexible et réutilisable.

### 1. Fonctions qui prennent d'autres fonctions en argument

C'est le cas le plus courant. Voici un exemple simple :

```python
def appliquer_operation(nombre, operation):
    """Applique une opération sur un nombre."""
    return operation(nombre)

# Utilisation avec différentes opérations
doubler = lambda x: x * 2
tripler = lambda x: x * 3
carre = lambda x: x ** 2

print(appliquer_operation(5, doubler))   # Affiche : 10
print(appliquer_operation(5, tripler))   # Affiche : 15
print(appliquer_operation(5, carre))     # Affiche : 25
```

Dans cet exemple, `appliquer_operation` est une fonction d'ordre supérieur car elle prend une fonction (`operation`) comme argument.

### 2. Fonctions qui retournent d'autres fonctions

Voici un exemple où une fonction crée et retourne une autre fonction :

```python
def creer_multiplicateur(n):
    """Crée une fonction qui multiplie par n."""
    return lambda x: x * n

# Création de différentes fonctions
multiplier_par_2 = creer_multiplicateur(2)
multiplier_par_5 = creer_multiplicateur(5)
multiplier_par_10 = creer_multiplicateur(10)

# Utilisation
print(multiplier_par_2(7))   # Affiche : 14
print(multiplier_par_5(7))   # Affiche : 35
print(multiplier_par_10(7))  # Affiche : 70
```

Ici, `creer_multiplicateur` retourne une fonction lambda différente selon la valeur de `n`.

### Exemple pratique : Filtrer une liste

Créons une fonction d'ordre supérieur pour filtrer une liste selon un critère :

```python
def filtrer(liste, condition):
    """Filtre une liste selon une condition."""
    resultat = []
    for element in liste:
        if condition(element):
            resultat.append(element)
    return resultat

# Liste de nombres
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrer les nombres pairs
pairs = filtrer(nombres, lambda x: x % 2 == 0)
print(f"Nombres pairs : {pairs}")  # Affiche : [2, 4, 6, 8, 10]

# Filtrer les nombres supérieurs à 5
superieurs_a_5 = filtrer(nombres, lambda x: x > 5)
print(f"Nombres > 5 : {superieurs_a_5}")  # Affiche : [6, 7, 8, 9, 10]

# Filtrer les multiples de 3
multiples_de_3 = filtrer(nombres, lambda x: x % 3 == 0)
print(f"Multiples de 3 : {multiples_de_3}")  # Affiche : [3, 6, 9]
```

### Exemple pratique : Transformer une liste

```python
def transformer(liste, transformation):
    """Applique une transformation à chaque élément d'une liste."""
    resultat = []
    for element in liste:
        resultat.append(transformation(element))
    return resultat

nombres = [1, 2, 3, 4, 5]

# Doubler chaque nombre
doubles = transformer(nombres, lambda x: x * 2)
print(f"Doublés : {doubles}")  # Affiche : [2, 4, 6, 8, 10]

# Mettre au carré
carres = transformer(nombres, lambda x: x ** 2)
print(f"Carrés : {carres}")  # Affiche : [1, 4, 9, 16, 25]

# Transformer en chaînes
chaines = transformer(nombres, lambda x: f"Numéro {x}")
print(f"Chaînes : {chaines}")  # Affiche : ['Numéro 1', 'Numéro 2', ...]
```

### Exemple avancé : Composition de fonctions

Les fonctions d'ordre supérieur permettent de composer des fonctions :

```python
def composer(f, g):
    """Crée une nouvelle fonction qui applique g puis f."""
    return lambda x: f(g(x))

# Fonctions de base
ajouter_5 = lambda x: x + 5
multiplier_par_2 = lambda x: x * 2

# Composition : d'abord multiplier par 2, puis ajouter 5
fonction_composee = composer(ajouter_5, multiplier_par_2)

print(fonction_composee(3))  # (3 * 2) + 5 = 11
print(fonction_composee(10)) # (10 * 2) + 5 = 25
```

---

## Cas d'usage pratiques

### 1. Tri personnalisé

Les fonctions lambda sont très utiles pour trier des listes avec des critères personnalisés :

```python
# Liste de personnes
personnes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
    {"nom": "David", "age": 28}
]

# Trier par âge
personnes_par_age = sorted(personnes, key=lambda p: p["age"])
print("Triées par âge :")
for p in personnes_par_age:
    print(f"  {p['nom']} : {p['age']} ans")

# Trier par nom
personnes_par_nom = sorted(personnes, key=lambda p: p["nom"])
print("\nTriées par nom :")
for p in personnes_par_nom:
    print(f"  {p['nom']} : {p['age']} ans")
```

### 2. Traitement de données

```python
# Liste de produits avec leurs prix
produits = [
    {"nom": "Pomme", "prix": 2.5},
    {"nom": "Banane", "prix": 1.8},
    {"nom": "Orange", "prix": 3.2},
    {"nom": "Poire", "prix": 2.9}
]

# Fonction d'ordre supérieur pour calculer une réduction
def appliquer_reduction(produits, calculer_nouveau_prix):
    """Applique une réduction sur tous les produits."""
    return [
        {
            "nom": p["nom"],
            "prix_original": p["prix"],
            "prix_reduit": calculer_nouveau_prix(p["prix"])
        }
        for p in produits
    ]

# Réduction de 20%
avec_reduction = appliquer_reduction(
    produits,
    lambda prix: prix * 0.8
)

print("Produits avec réduction de 20% :")
for p in avec_reduction:
    print(f"{p['nom']}: {p['prix_original']}€ → {p['prix_reduit']:.2f}€")
```

### 3. Validation de données

```python
def valider_donnees(donnees, validateurs):
    """Vérifie si les données passent tous les validateurs."""
    for validateur in validateurs:
        if not validateur(donnees):
            return False
    return True

# Validateurs pour un mot de passe
validateurs_mdp = [
    lambda mdp: len(mdp) >= 8,              # Au moins 8 caractères
    lambda mdp: any(c.isupper() for c in mdp),  # Au moins une majuscule
    lambda mdp: any(c.isdigit() for c in mdp),  # Au moins un chiffre
]

# Tests
mot_de_passe_1 = "Password123"
mot_de_passe_2 = "faible"

print(f"'{mot_de_passe_1}' est valide : {valider_donnees(mot_de_passe_1, validateurs_mdp)}")
print(f"'{mot_de_passe_2}' est valide : {valider_donnees(mot_de_passe_2, validateurs_mdp)}")
```

---

## Avantages et limitations

### Avantages des fonctions lambda

✅ **Concision** : Permet d'écrire du code court pour des opérations simples
✅ **Lisibilité** : Dans certains contextes (tri, filtrage), rend le code plus clair
✅ **Pas de pollution** : Ne nécessite pas de définir une fonction nommée pour un usage unique

### Limitations des fonctions lambda

❌ **Une seule expression** : On ne peut pas écrire de code sur plusieurs lignes
❌ **Pas de documentation** : Impossible d'ajouter une docstring
❌ **Débogage difficile** : Les erreurs sont plus difficiles à identifier
❌ **Lisibilité réduite** : Si l'expression devient trop complexe

### Avantages des fonctions d'ordre supérieur

✅ **Réutilisabilité** : Permet de créer du code générique et flexible
✅ **Abstraction** : Sépare la logique d'itération de la logique métier
✅ **Composition** : Permet de combiner des fonctions simples pour créer des comportements complexes

---

## Bonnes pratiques

### 1. Gardez les lambda simples

```python
# ✅ Bon : lambda simple et claire
nombres = [1, 2, 3, 4, 5]
pairs = list(filter(lambda x: x % 2 == 0, nombres))

# ❌ Mauvais : lambda trop complexe
resultat = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3 if x % 3 == 0 else x, nombres))
```

### 2. Préférez une fonction nommée si la logique est complexe

```python
# ❌ Difficile à lire
produits_filtres = filter(
    lambda p: p['prix'] < 50 and p['stock'] > 0 and p['categorie'] == 'electronique',
    produits
)

# ✅ Plus clair
def est_produit_disponible(produit):
    """Vérifie si un produit est disponible et abordable."""
    return (
        produit['prix'] < 50 and
        produit['stock'] > 0 and
        produit['categorie'] == 'electronique'
    )

produits_filtres = filter(est_produit_disponible, produits)
```

### 3. Documentez vos fonctions d'ordre supérieur

```python
def appliquer_a_tous(liste, fonction):
    """
    Applique une fonction à tous les éléments d'une liste.

    Args:
        liste: La liste d'éléments à traiter
        fonction: La fonction à appliquer à chaque élément

    Returns:
        Une nouvelle liste avec les résultats
    """
    return [fonction(element) for element in liste]
```

---

## Résumé

Dans ce chapitre, nous avons découvert :

**Les fonctions lambda** :
- Syntaxe : `lambda arguments: expression`
- Fonctions anonymes d'une seule ligne
- Utiles pour des opérations simples et ponctuelles
- À utiliser avec modération pour maintenir la lisibilité

**Les fonctions d'ordre supérieur** :
- Fonctions qui prennent d'autres fonctions en arguments
- Fonctions qui retournent d'autres fonctions
- Permettent de créer du code flexible et réutilisable
- Facilitent la composition et l'abstraction

**Points clés à retenir** :
- Les lambda sont pratiques mais doivent rester simples
- Les fonctions d'ordre supérieur augmentent la flexibilité du code
- Privilégiez la lisibilité : si une lambda devient complexe, utilisez une fonction classique
- Ces concepts sont fondamentaux en programmation fonctionnelle

Dans le prochain chapitre, nous verrons comment utiliser les fonctions d'ordre supérieur natives de Python : `map()`, `filter()`, et `reduce()`.

⏭️ [map(), filter(), reduce()](/05-programmation-fonctionnelle/02-map-filter-reduce.md)
