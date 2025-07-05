🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.2 : Structure des packages

## Introduction

Un **package** en Python est une façon d'organiser des modules connexes dans une structure hiérarchique de répertoires. Imaginez un package comme une bibliothèque organisée : au lieu d'avoir tous les livres en vrac, vous les classez par catégories dans différentes étagères et sections.

## Qu'est-ce qu'un package ?

Un package est :
- Un répertoire contenant des fichiers Python
- Qui contient un fichier spécial appelé `__init__.py`
- Qui peut contenir des sous-packages (sous-répertoires avec leurs propres `__init__.py`)

### Analogie simple
Pensez à votre ordinateur :
- **Dossier** = Package
- **Fichiers dans le dossier** = Modules
- **Sous-dossiers** = Sous-packages

## Structure de base d'un package

### Structure minimale

```
mon_package/
├── __init__.py          # Fichier qui fait du répertoire un package
├── module1.py          # Premier module
└── module2.py          # Deuxième module
```

### Le fichier `__init__.py`

Le fichier `__init__.py` peut être :
- **Vide** : indique simplement que le répertoire est un package
- **Contenir du code** : qui s'exécute lors de l'importation du package

## Exemple pratique : Package de calculs

Créons un package complet pour différents types de calculs.

### Étape 1 : Créer la structure

```
calculs/
├── __init__.py
├── basique.py
├── geometrie.py
├── finance.py
└── avance/
    ├── __init__.py
    ├── statistiques.py
    └── trigonometrie.py
```

### Étape 2 : Créer les modules

#### `calculs/basique.py`

```python
# calculs/basique.py

def additionner(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraire(a, b):
    """Soustrait deux nombres."""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres."""
    return a * b

def diviser(a, b):
    """Divise deux nombres."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def puissance(base, exposant):
    """Calcule base à la puissance exposant."""
    return base ** exposant

# Constantes utiles
PI = 3.14159265359
E = 2.71828182846
```

#### `calculs/geometrie.py`

```python
# calculs/geometrie.py

import math
from .basique import PI  # Import relatif depuis le même package

def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle."""
    return longueur * largeur

def aire_carre(cote):
    """Calcule l'aire d'un carré."""
    return cote ** 2

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle."""
    return PI * rayon ** 2

def aire_triangle(base, hauteur):
    """Calcule l'aire d'un triangle."""
    return 0.5 * base * hauteur

def perimetre_rectangle(longueur, largeur):
    """Calcule le périmètre d'un rectangle."""
    return 2 * (longueur + largeur)

def perimetre_cercle(rayon):
    """Calcule le périmètre d'un cercle."""
    return 2 * PI * rayon

def volume_cube(cote):
    """Calcule le volume d'un cube."""
    return cote ** 3

def volume_sphere(rayon):
    """Calcule le volume d'une sphère."""
    return (4/3) * PI * rayon ** 3

class Rectangle:
    """Classe pour représenter un rectangle."""

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return aire_rectangle(self.longueur, self.largeur)

    def perimetre(self):
        return perimetre_rectangle(self.longueur, self.largeur)

    def __str__(self):
        return f"Rectangle({self.longueur}x{self.largeur})"
```

#### `calculs/finance.py`

```python
# calculs/finance.py

def interet_simple(capital, taux, duree):
    """
    Calcule l'intérêt simple.

    Args:
        capital (float): Capital initial
        taux (float): Taux d'intérêt (en pourcentage)
        duree (float): Durée en années

    Returns:
        float: Montant des intérêts
    """
    return capital * (taux / 100) * duree

def interet_compose(capital, taux, duree):
    """
    Calcule l'intérêt composé.

    Args:
        capital (float): Capital initial
        taux (float): Taux d'intérêt annuel (en pourcentage)
        duree (float): Durée en années

    Returns:
        float: Montant final
    """
    return capital * ((1 + taux/100) ** duree)

def valeur_future(capital, taux, duree):
    """Calcule la valeur future d'un capital."""
    return interet_compose(capital, taux, duree)

def valeur_actuelle(valeur_future, taux, duree):
    """Calcule la valeur actuelle d'une somme future."""
    return valeur_future / ((1 + taux/100) ** duree)

def taux_rentabilite(capital_initial, capital_final, duree):
    """
    Calcule le taux de rentabilité annuel.

    Args:
        capital_initial (float): Capital de départ
        capital_final (float): Capital final
        duree (float): Durée en années

    Returns:
        float: Taux de rentabilité en pourcentage
    """
    if duree == 0:
        raise ValueError("La durée ne peut pas être zéro")

    return (((capital_final / capital_initial) ** (1/duree)) - 1) * 100

class PretImmobilier:
    """Classe pour calculer les mensualités d'un prêt immobilier."""

    def __init__(self, capital, taux_annuel, duree_annees):
        self.capital = capital
        self.taux_annuel = taux_annuel
        self.duree_annees = duree_annees
        self.taux_mensuel = taux_annuel / 12 / 100
        self.nb_mensualites = duree_annees * 12

    def mensualite(self):
        """Calcule la mensualité."""
        if self.taux_mensuel == 0:
            return self.capital / self.nb_mensualites

        return (self.capital * self.taux_mensuel *
                (1 + self.taux_mensuel) ** self.nb_mensualites) / \
               ((1 + self.taux_mensuel) ** self.nb_mensualites - 1)

    def cout_total(self):
        """Calcule le coût total du prêt."""
        return self.mensualite() * self.nb_mensualites

    def cout_credit(self):
        """Calcule le coût du crédit (intérêts)."""
        return self.cout_total() - self.capital
```

#### `calculs/avance/statistiques.py`

```python
# calculs/avance/statistiques.py

import math

def moyenne(donnees):
    """Calcule la moyenne d'une liste de nombres."""
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")
    return sum(donnees) / len(donnees)

def mediane(donnees):
    """Calcule la médiane d'une liste de nombres."""
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")

    donnees_triees = sorted(donnees)
    n = len(donnees_triees)

    if n % 2 == 0:
        # Nombre pair d'éléments
        return (donnees_triees[n//2 - 1] + donnees_triees[n//2]) / 2
    else:
        # Nombre impair d'éléments
        return donnees_triees[n//2]

def mode(donnees):
    """Trouve le mode (valeur la plus fréquente) d'une liste."""
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")

    frequences = {}
    for valeur in donnees:
        frequences[valeur] = frequences.get(valeur, 0) + 1

    max_freq = max(frequences.values())
    modes = [k for k, v in frequences.items() if v == max_freq]

    return modes[0] if len(modes) == 1 else modes

def variance(donnees):
    """Calcule la variance d'une liste de nombres."""
    if len(donnees) < 2:
        raise ValueError("Il faut au moins 2 valeurs pour calculer la variance")

    moy = moyenne(donnees)
    return sum((x - moy) ** 2 for x in donnees) / (len(donnees) - 1)

def ecart_type(donnees):
    """Calcule l'écart-type d'une liste de nombres."""
    return math.sqrt(variance(donnees))

def covariance(x, y):
    """Calcule la covariance entre deux listes de nombres."""
    if len(x) != len(y):
        raise ValueError("Les deux listes doivent avoir la même taille")

    if len(x) < 2:
        raise ValueError("Il faut au moins 2 valeurs")

    moy_x = moyenne(x)
    moy_y = moyenne(y)

    return sum((x[i] - moy_x) * (y[i] - moy_y) for i in range(len(x))) / (len(x) - 1)

def correlation(x, y):
    """Calcule le coefficient de corrélation entre deux listes."""
    return covariance(x, y) / (ecart_type(x) * ecart_type(y))

class StatistiquesDescriptives:
    """Classe pour calculer plusieurs statistiques d'un coup."""

    def __init__(self, donnees):
        if not donnees:
            raise ValueError("La liste ne peut pas être vide")
        self.donnees = list(donnees)

    def resumé(self):
        """Retourne un résumé statistique complet."""
        return {
            'count': len(self.donnees),
            'moyenne': moyenne(self.donnees),
            'mediane': mediane(self.donnees),
            'mode': mode(self.donnees),
            'min': min(self.donnees),
            'max': max(self.donnees),
            'variance': variance(self.donnees) if len(self.donnees) > 1 else None,
            'ecart_type': ecart_type(self.donnees) if len(self.donnees) > 1 else None
        }
```

#### `calculs/avance/trigonometrie.py`

```python
# calculs/avance/trigonometrie.py

import math
from ..basique import PI  # Import relatif depuis le package parent

def degres_vers_radians(degres):
    """Convertit des degrés en radians."""
    return degres * PI / 180

def radians_vers_degres(radians):
    """Convertit des radians en degrés."""
    return radians * 180 / PI

def sin_degres(degres):
    """Calcule le sinus d'un angle en degrés."""
    return math.sin(degres_vers_radians(degres))

def cos_degres(degres):
    """Calcule le cosinus d'un angle en degrés."""
    return math.cos(degres_vers_radians(degres))

def tan_degres(degres):
    """Calcule la tangente d'un angle en degrés."""
    return math.tan(degres_vers_radians(degres))

def distance_entre_points(x1, y1, x2, y2):
    """Calcule la distance entre deux points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angle_entre_points(x1, y1, x2, y2):
    """Calcule l'angle entre deux points (en degrés)."""
    radians = math.atan2(y2 - y1, x2 - x1)
    return radians_vers_degres(radians)

class Point:
    """Classe pour représenter un point dans le plan."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_vers(self, autre_point):
        """Calcule la distance vers un autre point."""
        return distance_entre_points(self.x, self.y, autre_point.x, autre_point.y)

    def angle_vers(self, autre_point):
        """Calcule l'angle vers un autre point."""
        return angle_entre_points(self.x, self.y, autre_point.x, autre_point.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Triangle:
    """Classe pour représenter un triangle."""

    def __init__(self, a, b, c):
        """Initialise avec les longueurs des trois côtés."""
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ces longueurs ne forment pas un triangle valide")
        self.a = a
        self.b = b
        self.c = c

    def aire_heron(self):
        """Calcule l'aire avec la formule de Héron."""
        s = (self.a + self.b + self.c) / 2  # Semi-périmètre
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def angles(self):
        """Retourne les trois angles du triangle en degrés."""
        # Loi des cosinus pour trouver les angles
        angle_A = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        angle_B = math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        angle_C = math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b))

        return {
            'A': radians_vers_degres(angle_A),
            'B': radians_vers_degres(angle_B),
            'C': radians_vers_degres(angle_C)
        }
```

### Étape 3 : Configurer les fichiers `__init__.py`

#### `calculs/__init__.py`

```python
# calculs/__init__.py

"""
Package de calculs mathématiques.

Ce package fournit des outils pour :
- Calculs de base (addition, soustraction, etc.)
- Géométrie (aires, volumes, etc.)
- Finance (intérêts, prêts, etc.)
- Statistiques et trigonométrie (dans le sous-package 'avance')

Exemple d'utilisation :
    from calculs import basique, geometrie

    resultat = basique.additionner(5, 3)
    aire = geometrie.aire_cercle(10)
"""

# Version du package
__version__ = "1.0.0"
__author__ = "Votre nom"

# Imports pour faciliter l'utilisation
from . import basique
from . import geometrie
from . import finance

# Rendre certaines fonctions disponibles directement
from .basique import additionner, soustraire, multiplier, diviser
from .geometrie import aire_cercle, aire_rectangle

# Liste des modules/fonctions exportés
__all__ = [
    'basique',
    'geometrie',
    'finance',
    'additionner',
    'soustraire',
    'multiplier',
    'diviser',
    'aire_cercle',
    'aire_rectangle'
]

# Code d'initialisation
print(f"Package calculs v{__version__} chargé")
```

#### `calculs/avance/__init__.py`

```python
# calculs/avance/__init__.py

"""
Sous-package pour les calculs avancés.

Contient :
- Statistiques descriptives
- Fonctions trigonométriques
"""

from . import statistiques
from . import trigonometrie

# Imports directs pour faciliter l'usage
from .statistiques import moyenne, mediane, ecart_type
from .trigonometrie import sin_degres, cos_degres, tan_degres

__all__ = [
    'statistiques',
    'trigonometrie',
    'moyenne',
    'mediane',
    'ecart_type',
    'sin_degres',
    'cos_degres',
    'tan_degres'
]
```

## Utilisation du package

### Méthode 1 : Import des modules

```python
# test_package.py

# Import des modules
from calculs import basique, geometrie, finance
from calculs.avance import statistiques, trigonometrie

# Utilisation
print("=== Tests du package calculs ===")

# Calculs de base
resultat = basique.additionner(10, 5)
print(f"10 + 5 = {resultat}")

# Géométrie
aire = geometrie.aire_cercle(5)
rectangle = geometrie.Rectangle(4, 6)
print(f"Aire du cercle (r=5) : {aire:.2f}")
print(f"Rectangle 4x6 - Aire: {rectangle.aire()}, Périmètre: {rectangle.perimetre()}")

# Finance
pret = finance.PretImmobilier(200000, 3.5, 25)
print(f"Mensualité du prêt : {pret.mensualite():.2f}€")

# Statistiques
donnees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = statistiques.StatistiquesDescriptives(donnees)
print(f"Statistiques : {stats.resumé()}")

# Trigonométrie
angle = 45
print(f"sin({angle}°) = {trigonometrie.sin_degres(angle):.3f}")
```

### Méthode 2 : Import direct grâce aux `__init__.py`

```python
# test_package_simple.py

# Import direct des fonctions exposées
from calculs import additionner, aire_cercle
from calculs.avance import moyenne, sin_degres

# Utilisation simplifiée
resultat = additionner(7, 3)
aire = aire_cercle(3)
moy = moyenne([1, 2, 3, 4, 5])
sinus = sin_degres(30)

print(f"Résultats : {resultat}, {aire:.2f}, {moy}, {sinus:.3f}")
```

### Méthode 3 : Import de tout le package

```python
# test_package_complet.py

import calculs

# Utilisation avec le nom du package
resultat = calculs.additionner(5, 3)  # Grâce à l'import dans __init__.py
aire = calculs.geometrie.aire_triangle(10, 8)

print(f"Résultat : {resultat}")
print(f"Aire triangle : {aire}")
print(f"Version du package : {calculs.__version__}")
```

## Imports relatifs vs absolus

### Imports absolus

```python
# Depuis n'importe où dans le package
from calculs.basique import additionner
from calculs.geometrie import aire_cercle
from calculs.avance.statistiques import moyenne
```

### Imports relatifs

```python
# Depuis l'intérieur du package seulement

# Import du même niveau
from .basique import PI

# Import d'un niveau supérieur
from ..basique import additionner

# Import d'un sous-package
from .avance.statistiques import moyenne
```

## Structure avancée de package

Pour des projets plus complexes :

```
mon_grand_projet/
├── __init__.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── database.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── middleware.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_utils.py
├── docs/
├── requirements.txt
├── setup.py
└── README.md
```

## Exercices pratiques

### Exercice 1 : Package de gestion de dates

Créez un package `dates` avec :
- `operations.py` : fonctions pour ajouter/soustraire des jours
- `formatage.py` : fonctions pour formater les dates
- `validation.py` : fonctions pour valider les dates

```python
# Structure attendue
dates/
├── __init__.py
├── operations.py
├── formatage.py
└── validation.py
```

### Exercice 2 : Package de jeux

Créez un package `jeux` avec des sous-packages :
- `cartes/` : jeux de cartes (poker, blackjack)
- `des/` : jeux de dés
- `plateau/` : jeux de plateau

### Exercice 3 : Améliorer le package calculs

Ajoutez au package `calculs` :
- Un module `conversions.py` pour les conversions d'unités
- Un sous-package `sciences/` avec physique et chimie
- Des tests unitaires dans un sous-package `tests/`

## Solutions des exercices

### Solution Exercice 1 : Package de gestion de dates

```python
# dates/__init__.py
"""Package pour la gestion des dates."""

from . import operations, formatage, validation
from .operations import ajouter_jours, soustraire_jours
from .formatage import formater_date_francaise

__version__ = "1.0.0"
__all__ = ['operations', 'formatage', 'validation']

# dates/operations.py
from datetime import datetime, timedelta

def ajouter_jours(date, nb_jours):
    """Ajoute des jours à une date."""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    return date + timedelta(days=nb_jours)

def soustraire_jours(date, nb_jours):
    """Soustrait des jours à une date."""
    return ajouter_jours(date, -nb_jours)

def difference_jours(date1, date2):
    """Calcule la différence en jours entre deux dates."""
    if isinstance(date1, str):
        date1 = datetime.strptime(date1, "%Y-%m-%d")
    if isinstance(date2, str):
        date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

# dates/formatage.py
from datetime import datetime

def formater_date_francaise(date):
    """Formate une date au format français (dd/mm/yyyy)."""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    return date.strftime("%d/%m/%Y")

def formater_date_complete(date):
    """Formate une date de manière complète."""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")

    mois = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]

    return f"{date.day} {mois[date.month-1]} {date.year}"

# dates/validation.py
from datetime import datetime

def est_date_valide(date_str, format="%Y-%m-%d"):
    """Vérifie si une chaîne représente une date valide."""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def est_annee_bissextile(annee):
    """Vérifie si une année est bissextile."""
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

def est_date_future(date):
    """Vérifie si une date est dans le futur."""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    return date > datetime.now()
```

## Bonnes pratiques pour les packages

### 1. Organisation logique
- Regroupez les fonctionnalités similaires
- Utilisez des noms descriptifs
- Maintenez une hiérarchie claire

### 2. Documentation
- Documentez chaque module et package
- Utilisez des docstrings détaillées
- Créez un fichier README.md

### 3. Imports intelligents
- Utilisez `__all__` pour contrôler les exports
- Facilitez l'usage avec des imports dans `__init__.py`
- Évitez les imports circulaires

### 4. Versioning
- Utilisez `__version__` dans vos packages
- Suivez le semantic versioning (1.2.3)

### 5. Tests
- Créez des tests pour chaque module
- Organisez les tests en miroir de la structure

## Résumé

Les packages permettent de :

- **Organiser** le code en structure hiérarchique
- **Éviter** les conflits de noms
- **Faciliter** la maintenance et la collaboration
- **Créer** des bibliothèques réutilisables
- **Distribuer** du code de manière professionnelle

Dans la prochaine section, nous verrons comment gérer les dépendances avec pip et créer des environnements virtuels pour nos packages.

⏭️
