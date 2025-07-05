🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 5 : Programmation fonctionnelle

## Introduction à la programmation fonctionnelle

La programmation fonctionnelle est un paradigme de programmation qui traite les calculs comme l'évaluation de fonctions mathématiques. Elle évite les changements d'état et les données mutables, privilégiant l'utilisation de fonctions pures et l'immutabilité.

Python, bien qu'étant un langage multi-paradigme, offre de nombreuses fonctionnalités qui permettent d'adopter un style de programmation fonctionnelle. Ce module vous permettra de maîtriser ces concepts et d'enrichir votre boîte à outils de développeur.

## Concepts clés de la programmation fonctionnelle

### 1. Fonctions pures
Une fonction pure est une fonction qui :
- Produit toujours le même résultat pour les mêmes arguments
- N'a pas d'effets de bord (ne modifie pas l'état externe)
- Ne dépend que de ses paramètres d'entrée

```python
# Fonction pure
def add(x, y):
    return x + y

# Fonction impure (effet de bord)
counter = 0
def increment():
    global counter
    counter += 1
    return counter
```

### 2. Immutabilité
L'immutabilité consiste à ne pas modifier les données après leur création. En Python, certains types sont naturellement immutables (tuples, strings, nombres).

```python
# Approche mutable
def modify_list(lst):
    lst.append(4)
    return lst

# Approche immutable
def add_to_list(lst, item):
    return lst + [item]
```

### 3. Fonctions comme citoyens de première classe
En Python, les fonctions peuvent être :
- Assignées à des variables
- Passées comme arguments
- Retournées par d'autres fonctions
- Stockées dans des structures de données

```python
# Assigner une fonction à une variable
operation = add

# Passer une fonction comme argument
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(add, 5, 3)
```

## Avantages de la programmation fonctionnelle

### 1. Lisibilité et maintenabilité
Le code fonctionnel est souvent plus prévisible et plus facile à comprendre car il évite les effets de bord.

### 2. Testabilité
Les fonctions pures sont plus faciles à tester car elles ne dépendent que de leurs paramètres d'entrée.

### 3. Parallélisation
L'absence d'effets de bord facilite l'exécution parallèle et concurrente.

### 4. Réutilisabilité
Les fonctions peuvent être facilement composées et réutilisées dans différents contextes.

## Quand utiliser la programmation fonctionnelle

La programmation fonctionnelle est particulièrement utile pour :

- **Traitement de données** : Transformation, filtrage et agrégation de collections
- **Pipelines de traitement** : Enchaînement d'opérations sur des données
- **Calculs mathématiques** : Opérations qui nécessitent des fonctions pures
- **Programmation concurrente** : Éviter les problèmes de synchronisation
- **Configuration et validation** : Fonctions de validation composables

## Exemple pratique : Traitement d'une liste de nombres

Approche impérative traditionnelle :
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num * 2)

print(result)  # [4, 8, 12, 16, 20]
```

Approche fonctionnelle (que nous verrons en détail) :
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 8, 12, 16, 20]
```

## Contenu du module

Ce module couvre les aspects suivants de la programmation fonctionnelle en Python :

**5.1 : Fonctions lambda et fonctions d'ordre supérieur**
- Syntaxe et utilisation des fonctions lambda
- Fonctions qui prennent d'autres fonctions comme paramètres
- Fonctions qui retournent des fonctions

**5.2 : map(), filter(), reduce()**
- Transformation de données avec map()
- Filtrage avec filter()
- Agrégation avec reduce()

**5.3 : Décorateurs avancés**
- Création de décorateurs personnalisés
- Décorateurs avec paramètres
- Décorateurs de classe

**5.4 : Générateurs et expressions génératrices**
- Création de générateurs avec yield
- Expressions génératrices
- Avantages en termes de mémoire

**5.5 : Closures et programmation fonctionnelle**
- Concept de closure
- Variables capturées
- Patterns fonctionnels avancés

## Prérequis

Avant d'aborder ce module, assurez-vous de maîtriser :
- Les fonctions de base en Python (Module 1.4)
- Les structures de données (Module 2)
- Les concepts de base de la programmation orientée objet (Module 3)

## Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :
- Comprendre et appliquer les principes de la programmation fonctionnelle
- Utiliser les fonctions lambda de manière appropriée
- Maîtriser les fonctions map(), filter() et reduce()
- Créer des décorateurs avancés
- Utiliser les générateurs pour optimiser la mémoire
- Implémenter des patterns fonctionnels complexes

---

*La programmation fonctionnelle vous permettra d'écrire du code plus élégant, plus maintenable et souvent plus performant. Préparez-vous à découvrir une nouvelle façon de penser la programmation !*

⏭️
