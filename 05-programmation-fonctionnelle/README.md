🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5. Programmation fonctionnelle

## Introduction au chapitre

Bienvenue dans le chapitre sur la **programmation fonctionnelle** ! Si vous êtes arrivé jusqu'ici, vous maîtrisez déjà les fondamentaux de Python : variables, fonctions, structures de contrôle, et programmation orientée objet. Il est maintenant temps de découvrir un paradigme de programmation puissant et élégant qui transformera votre façon d'écrire du code.

La programmation fonctionnelle peut sembler intimidante au début, mais ne vous inquiétez pas ! Nous allons explorer ces concepts progressivement, avec des exemples concrets et accessibles. À la fin de ce chapitre, vous serez capable d'écrire du code Python plus expressif, plus maintenable et souvent plus performant.

---

## Qu'est-ce que la programmation fonctionnelle ?

La **programmation fonctionnelle** est un **paradigme de programmation** - c'est-à-dire une manière de penser et d'organiser le code - qui traite le calcul comme l'évaluation de fonctions mathématiques.

### Comparaison avec d'autres paradigmes

Pour mieux comprendre, comparons trois approches pour résoudre le même problème :

**Problème** : Calculer le carré de tous les nombres pairs d'une liste.

#### Approche impérative (procédurale)

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
carres_pairs = []  

for nombre in nombres:
    if nombre % 2 == 0:
        carre = nombre ** 2
        carres_pairs.append(carre)

print(carres_pairs)  # [4, 16, 36, 64, 100]
```

**Caractéristiques** : Instructions séquentielles, modification d'état (la liste `carres_pairs` est modifiée)

#### Approche orientée objet

```python
class CalculateurCarres:
    def __init__(self):
        self.resultats = []

    def est_pair(self, nombre):
        return nombre % 2 == 0

    def calculer_carre(self, nombre):
        return nombre ** 2

    def traiter(self, nombres):
        for nombre in nombres:
            if self.est_pair(nombre):
                self.resultats.append(self.calculer_carre(nombre))
        return self.resultats

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
calculateur = CalculateurCarres()  
print(calculateur.traiter(nombres))  # [4, 16, 36, 64, 100]  
```

**Caractéristiques** : Encapsulation dans des objets, état interne

#### Approche fonctionnelle

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec fonctions et compréhension de liste
carres_pairs = [n ** 2 for n in nombres if n % 2 == 0]

# Ou avec des fonctions d'ordre supérieur
est_pair = lambda n: n % 2 == 0  
mettre_au_carre = lambda n: n ** 2  

carres_pairs = list(map(mettre_au_carre, filter(est_pair, nombres)))

print(carres_pairs)  # [4, 16, 36, 64, 100]
```

**Caractéristiques** : Composition de fonctions, pas de modification d'état, expressions plutôt qu'instructions

### Les trois approches sont valides !

Python est un langage **multi-paradigme** : vous pouvez mélanger ces approches selon vos besoins. La programmation fonctionnelle n'est pas "meilleure" que les autres, c'est simplement un outil supplémentaire dans votre boîte à outils.

---

## Pourquoi apprendre la programmation fonctionnelle ?

### 1. Code plus concis et expressif

La programmation fonctionnelle permet souvent d'écrire du code plus court et plus clair :

```python
# Style impératif
nombres = [1, 2, 3, 4, 5]  
somme = 0  
for n in nombres:  
    somme += n * 2

# Style fonctionnel
somme = sum(n * 2 for n in nombres)
```

### 2. Moins de bugs

Les fonctions "pures" (sans effets de bord) sont plus faciles à tester et à déboguer :

```python
# ❌ Fonction avec effet de bord (plus difficile à tester)
total = 0  
def ajouter(x):  
    global total
    total += x
    return total

# ✅ Fonction pure (facile à tester)
def calculer_somme(liste):
    return sum(liste)

# Test simple et prévisible
assert calculer_somme([1, 2, 3]) == 6
```

### 3. Code plus réutilisable

Les fonctions peuvent être composées et réutilisées de multiples façons :

```python
# Fonctions réutilisables
def est_pair(n):
    return n % 2 == 0

def est_positif(n):
    return n > 0

def est_petit(n):
    return n < 10

# Réutilisation dans différents contextes
nombres = [-5, -2, 0, 1, 3, 8, 12, 15]

print(list(filter(est_pair, nombres)))          # [-2, 0, 8, 12]  
print(list(filter(est_positif, nombres)))       # [1, 3, 8, 12, 15]  
print(list(filter(est_petit, nombres)))         # [-5, -2, 0, 1, 3, 8]  
```

### 4. Parallélisation facilitée

Les fonctions sans effets de bord peuvent être exécutées en parallèle sans danger :

```python
# Fonction pure : peut être parallélisée facilement
def calculer_carre(n):
    return n ** 2

# Pas de risque de conflit car pas de modification d'état partagé
# from multiprocessing import Pool
# with Pool() as pool:
#     resultats = pool.map(calculer_carre, range(1000))
```

### 5. Compétence valorisée

La programmation fonctionnelle est de plus en plus populaire et demandée :
- JavaScript moderne (React, fonctions fléchées)
- Traitement de données (Spark, Pandas)
- Langages fonctionnels purs (Haskell, Elixir, Clojure)

---

## Concepts clés de la programmation fonctionnelle

Voici les principaux concepts que nous allons explorer dans ce chapitre :

### 1. Fonctions comme citoyens de première classe

En Python, les fonctions sont des objets comme les autres : on peut les assigner à des variables, les passer en arguments, et les retourner.

```python
# Assigner une fonction à une variable
ma_fonction = print  
ma_fonction("Bonjour !")  # Bonjour !  

# Passer une fonction en argument
def executer_deux_fois(fonction, valeur):
    fonction(valeur)
    fonction(valeur)

executer_deux_fois(print, "Python")
# Python
# Python
```

### 2. Fonctions d'ordre supérieur

Une fonction d'ordre supérieur est une fonction qui :
- Prend une ou plusieurs fonctions en paramètre, ET/OU
- Retourne une fonction

```python
# map() prend une fonction en paramètre
nombres = [1, 2, 3, 4, 5]  
doubles = list(map(lambda x: x * 2, nombres))  
print(doubles)  # [2, 4, 6, 8, 10]  

# Fonction qui retourne une fonction
def creer_multiplicateur(facteur):
    def multiplier(x):
        return x * facteur
    return multiplier

fois_trois = creer_multiplicateur(3)  
print(fois_trois(10))  # 30  
```

### 3. Fonctions pures

Une fonction pure :
- Retourne toujours le même résultat pour les mêmes arguments
- N'a pas d'effets de bord (ne modifie rien en dehors d'elle)

```python
# ✅ Fonction pure
def additionner(a, b):
    return a + b

print(additionner(3, 5))  # Toujours 8

# ❌ Fonction impure (modifie un état externe)
compteur = 0  
def incrementer():  
    global compteur
    compteur += 1
    return compteur
```

### 4. Immuabilité

Préférer créer de nouvelles données plutôt que de modifier les données existantes :

```python
# ❌ Style mutable
liste = [1, 2, 3]  
liste.append(4)  # Modifie la liste  

# ✅ Style immuable
liste = [1, 2, 3]  
nouvelle_liste = liste + [4]  # Crée une nouvelle liste  
```

### 5. Composition de fonctions

Combiner plusieurs fonctions simples pour créer des fonctions plus complexes :

```python
def ajouter_10(x):
    return x + 10

def multiplier_par_2(x):
    return x * 2

# Composer les fonctions
def traiter(x):
    return multiplier_par_2(ajouter_10(x))

print(traiter(5))  # (5 + 10) * 2 = 30
```

---

## Python et la programmation fonctionnelle

### Python n'est pas un langage purement fonctionnel

Contrairement à des langages comme Haskell ou Elixir, Python est **multi-paradigme**. Cela signifie que :

✅ Python **supporte** la programmation fonctionnelle  
✅ Python **encourage** un mélange de paradigmes  
❌ Python **n'impose pas** la programmation fonctionnelle

### Ce que Python offre

Python fournit de nombreux outils pour la programmation fonctionnelle :

**Fonctions natives** :
- `map()` : applique une fonction à chaque élément
- `filter()` : filtre les éléments selon une condition
- `reduce()` : réduit une séquence à une valeur unique
- `zip()` : combine plusieurs séquences
- `enumerate()` : itère avec des indices

**Fonctionnalités du langage** :
- Fonctions lambda (anonymes)
- Compréhensions de listes
- Générateurs
- Décorateurs
- Closures

**Modules standard** :
- `functools` : outils pour la programmation fonctionnelle
- `itertools` : itérateurs avancés
- `operator` : fonctions pour les opérateurs standards

### L'approche pythonique

En Python, on privilégie souvent la **lisibilité** à la "pureté" fonctionnelle :

```python
# Style fonctionnel pur (peut être moins lisible)
from functools import reduce  
somme = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0)  

# Style pythonique (plus clair)
somme = sum([1, 2, 3, 4, 5])
```

**La règle d'or** : Utilisez la programmation fonctionnelle quand elle rend le code plus clair, pas par dogmatisme !

---

## Ce que vous allez apprendre dans ce chapitre

### 5.1 Fonctions lambda et fonctions d'ordre supérieur

Vous découvrirez comment créer des fonctions anonymes compactes et comment utiliser des fonctions qui prennent d'autres fonctions en paramètres ou les retournent.

**Exemple de ce que vous saurez faire** :
```python
# Créer une fonction qui génère des multiplicateurs
def creer_multiplicateur(n):
    return lambda x: x * n

double = creer_multiplicateur(2)  
triple = creer_multiplicateur(3)  

print(double(5))  # 10  
print(triple(5))  # 15  
```

### 5.2 map(), filter(), reduce()

Vous maîtriserez les trois fonctions fondamentales pour transformer et traiter des collections de données.

**Exemple de ce que vous saurez faire** :
```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrer les pairs, les mettre au carré, et faire la somme
from functools import reduce  
resultat = reduce(  
    lambda acc, x: acc + x,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nombres))
)
print(resultat)  # 220
```

### 5.3 Décorateurs avancés

Vous apprendrez à créer des décorateurs puissants pour ajouter des fonctionnalités à vos fonctions sans modifier leur code.

**Exemple de ce que vous saurez faire** :
```python
def mesurer_temps(fonction):
    import time
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        print(f"Temps : {time.time() - debut:.4f}s")
        return resultat
    return wrapper

@mesurer_temps
def calculer_somme(n):
    return sum(range(n))

calculer_somme(1000000)  # Affiche le temps d'exécution
```

### 5.4 Générateurs et expressions génératrices

Vous découvrirez comment créer des séquences de données efficaces en mémoire qui produisent des valeurs à la demande.

**Exemple de ce que vous saurez faire** :
```python
# Générateur de nombres de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Utilisation efficace en mémoire
for nombre in fibonacci(10):
    print(nombre, end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

### 5.5 Closures et programmation fonctionnelle

Vous comprendrez comment les fonctions peuvent "capturer" leur environnement et vous explorerez les principes fondamentaux de la programmation fonctionnelle.

**Exemple de ce que vous saurez faire** :
```python
def creer_compteur():
    compte = 0

    def incrementer():
        nonlocal compte
        compte += 1
        return compte

    return incrementer

compteur = creer_compteur()  
print(compteur())  # 1  
print(compteur())  # 2  
print(compteur())  # 3  
```

---

## Comment aborder ce chapitre

### 1. Progressez étape par étape

La programmation fonctionnelle introduit de nouveaux concepts. Prenez le temps de :
- Lire attentivement chaque section
- Tester les exemples vous-même
- Expérimenter avec vos propres variations

### 2. N'ayez pas peur de mélanger les paradigmes

Vous n'êtes **pas obligé** d'écrire tout votre code de manière fonctionnelle. Python encourage le pragmatisme :

```python
# Mélange de styles selon les besoins
class Calculateur:
    def __init__(self):
        self.historique = []

    def calculer(self, nombres):
        # Style fonctionnel pour le traitement
        resultats = list(map(lambda x: x ** 2, filter(lambda x: x > 0, nombres)))

        # Style impératif pour l'historique
        self.historique.append(resultats)

        return resultats
```

### 3. Privilégiez toujours la lisibilité

Un code fonctionnel n'est utile que s'il est compréhensible :

```python
# ❌ Trop dense, difficile à lire
r = list(map(lambda x: x**2, filter(lambda x: x%2==0, [i for i in range(10)])))

# ✅ Plus clair
nombres = range(10)  
pairs = [n for n in nombres if n % 2 == 0]  
carres = [n ** 2 for n in pairs]  
```

### 4. Appliquez progressivement

Commencez par incorporer des éléments simples dans votre code :
1. Utilisez des compréhensions de listes
2. Explorez `map()` et `filter()`
3. Créez des fonctions pures quand possible
4. Puis progressez vers les concepts plus avancés

---

## Exemples motivants

Avant de commencer, voici quelques exemples qui montrent la puissance de la programmation fonctionnelle :

### Traitement de données élégant

```python
# Analyser des données de ventes
ventes = [
    {"produit": "A", "quantite": 5, "prix": 10},
    {"produit": "B", "quantite": 3, "prix": 20},
    {"produit": "C", "quantite": 7, "prix": 15},
]

# Style fonctionnel : pipeline de transformations
chiffre_affaires = sum(
    vente["quantite"] * vente["prix"]
    for vente in ventes
)
print(f"CA total : {chiffre_affaires}€")  # 215€

# Produits vendus à plus de 50€
gros_montants = [
    vente["produit"]
    for vente in ventes
    if vente["quantite"] * vente["prix"] > 50
]
print(f"Gros montants : {gros_montants}")  # ['B', 'C']
```

### Pipeline de traitement

```python
# Nettoyer et analyser du texte
def pipeline_texte(texte):
    return (texte
            .lower()              # En minuscules
            .strip()              # Supprimer espaces
            .replace(",", "")     # Supprimer ponctuation
            .split())             # Découper en mots

mots = pipeline_texte("  Hello, World  ")  
print(mots)  # ['hello', 'world']  

# Compter les mots
texte = "Python est génial et Python est puissant"  
mots = pipeline_texte(texte)  
compte_mots = {mot: mots.count(mot) for mot in set(mots)}  
print(compte_mots)  # {'python': 2, 'est': 2, 'génial': 1, ...}  
```

### Composition élégante

```python
# Valider des données avec composition
def valide_email(email):
    return "@" in email and "." in email.split("@")[1]

def valide_age(age):
    return 18 <= age <= 120

def valide_nom(nom):
    return len(nom) >= 2

# Composer les validations
utilisateurs = [
    {"nom": "Alice", "email": "alice@example.com", "age": 25},
    {"nom": "B", "email": "bob@com", "age": 17},
    {"nom": "Charlie", "email": "charlie@example.com", "age": 30},
]

utilisateurs_valides = [
    u for u in utilisateurs
    if valide_nom(u["nom"]) and valide_email(u["email"]) and valide_age(u["age"])
]

print(f"{len(utilisateurs_valides)} utilisateurs valides")
```

---

## Prérequis

Pour profiter pleinement de ce chapitre, vous devriez être à l'aise avec :

✅ Les fonctions Python de base (définition, paramètres, return)  
✅ Les structures de données (listes, dictionnaires, tuples)  
✅ Les boucles et conditions  
✅ Les compréhensions de listes (utile mais pas obligatoire)

Si vous avez besoin de revoir ces concepts, n'hésitez pas à consulter les chapitres précédents.

---

## À retenir

Avant de commencer, gardez en tête ces points importants :

🎯 **La programmation fonctionnelle est un outil, pas une religion**
Utilisez-la quand elle améliore votre code, pas par principe.

🎯 **Python n'est pas purement fonctionnel**
Vous pouvez (et devriez) mélanger les paradigmes.

🎯 **La lisibilité avant tout**
Un code fonctionnel obscur est pire qu'un code impératif clair.

🎯 **Progressez graduellement**
Commencez simple, puis montez en complexité.

🎯 **Pratiquez régulièrement**
Les concepts deviendront naturels avec la pratique.

---

## Conclusion de l'introduction

La programmation fonctionnelle est un paradigme élégant et puissant qui enrichira considérablement votre boîte à outils de développeur Python. Les concepts que vous allez découvrir - fonctions lambda, map/filter/reduce, décorateurs, générateurs, et closures - sont utilisés quotidiennement par les développeurs Python professionnels.

Ce chapitre est conçu pour vous emmener progressivement du niveau débutant à une compréhension solide de la programmation fonctionnelle. Chaque section s'appuie sur la précédente, et de nombreux exemples pratiques vous aideront à comprendre comment et quand appliquer ces concepts.

**Conseil final** : N'essayez pas de tout mémoriser du premier coup. L'objectif est de comprendre les concepts et de savoir où les retrouver quand vous en aurez besoin. Avec la pratique, ces techniques deviendront une seconde nature.

Prêt à commencer ? Passons aux fonctions lambda et aux fonctions d'ordre supérieur ! 🚀

---

## Ressources complémentaires

Si vous souhaitez approfondir certains concepts après avoir terminé ce chapitre, voici quelques ressources utiles :

**Documentation Python** :
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Module functools](https://docs.python.org/3/library/functools.html)
- [Module itertools](https://docs.python.org/3/library/itertools.html)

**Concepts à explorer** (après avoir maîtrisé ce chapitre) :
- Programmation réactive (RxPY)
- Traitement de flux de données (Pandas)
- Pattern matching (Python 3.10+)
- Programmation asynchrone fonctionnelle

Mais pour l'instant, concentrons-nous sur les fondamentaux. Bonne lecture !

⏭️ [Fonctions lambda et fonctions d'ordre supérieur](/05-programmation-fonctionnelle/01-lambda-et-fonctions-ordre-superieur.md)
