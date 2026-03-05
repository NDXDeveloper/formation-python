🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.1 Importation et création de modules

## Introduction

Un module en Python est simplement un fichier contenant du code Python (fonctions, classes, variables). Les modules permettent d'organiser et de réutiliser votre code de manière efficace. Au lieu d'écrire tout votre code dans un seul fichier, vous pouvez le diviser en plusieurs modules logiques.

Python dispose d'une riche bibliothèque standard (modules intégrés) et vous pouvez également créer vos propres modules personnalisés.

---

## Pourquoi utiliser des modules ?

Les modules offrent plusieurs avantages :

- **Organisation du code** : Diviser un programme complexe en fichiers plus petits et gérables
- **Réutilisabilité** : Utiliser le même code dans différents projets sans duplication
- **Espaces de noms** : Éviter les conflits de noms entre différentes parties du code
- **Maintenance** : Faciliter la correction de bugs et les mises à jour
- **Collaboration** : Permettre à plusieurs développeurs de travailler sur différentes parties du projet

---

## Importation de modules

### Importation simple avec `import`

La façon la plus basique d'importer un module est d'utiliser le mot-clé `import` :

```python
import math

# Utilisation des fonctions du module
resultat = math.sqrt(16)  
print(resultat)  # Affiche : 4.0  

print(math.pi)   # Affiche : 3.141592653589793
```

Avec cette syntaxe, vous devez préfixer chaque utilisation par le nom du module (`math.sqrt`, `math.pi`).

### Importation avec alias

Pour raccourcir le nom d'un module, vous pouvez lui donner un alias avec le mot-clé `as` :

```python
import math as m

resultat = m.sqrt(25)  
print(resultat)  # Affiche : 5.0  

print(m.pi)      # Affiche : 3.141592653589793
```

Cette technique est particulièrement utile pour les modules avec des noms longs.

### Importation d'éléments spécifiques avec `from`

Si vous n'avez besoin que de certains éléments d'un module, vous pouvez les importer directement :

```python
from math import sqrt, pi

# Utilisation directe sans préfixe
resultat = sqrt(36)  
print(resultat)  # Affiche : 6.0  

print(pi)        # Affiche : 3.141592653589793
```

Vous pouvez également donner un alias aux éléments importés :

```python
from math import sqrt as racine_carree

resultat = racine_carree(49)  
print(resultat)  # Affiche : 7.0  
```

### Importation de tous les éléments (à éviter)

Il est possible d'importer tous les éléments d'un module avec `*` :

```python
from math import *

resultat = sqrt(64)  
print(resultat)  # Affiche : 8.0  
```

**⚠️ Attention :** Cette pratique est généralement déconseillée car :
- Elle pollue l'espace de noms global
- Elle peut créer des conflits de noms
- Elle rend le code moins lisible (on ne sait pas d'où viennent les fonctions)

### Importation de modules de la bibliothèque standard

Python possède de nombreux modules intégrés. Voici quelques exemples courants :

```python
# Module pour les dates et heures
import datetime

maintenant = datetime.datetime.now()  
print(maintenant)  

# Module pour les nombres aléatoires
import random

nombre_aleatoire = random.randint(1, 10)  
print(nombre_aleatoire)  

# Module pour les opérations sur les fichiers et dossiers
import os

chemin_actuel = os.getcwd()  
print(chemin_actuel)  

# Module pour les expressions régulières
import re

texte = "Mon email est exemple@email.com"  
email = re.search(r'\S+@\S+', texte)  
print(email.group())  
```

---

## Création de vos propres modules

### Module simple

Créer un module est aussi simple que créer un fichier Python. Voici comment procéder :

**Étape 1 :** Créez un fichier nommé `operations.py` :

```python
# Fichier : operations.py

def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait b de a."""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres."""
    return a * b

def division(a, b):
    """Divise a par b."""
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

# Variable du module
PI = 3.14159
```

**Étape 2 :** Utilisez votre module dans un autre fichier Python (dans le même dossier) :

```python
# Fichier : main.py

import operations

resultat1 = operations.addition(10, 5)  
print(f"10 + 5 = {resultat1}")  

resultat2 = operations.multiplication(7, 3)  
print(f"7 × 3 = {resultat2}")  

print(f"Valeur de PI : {operations.PI}")
```

### Module avec des classes

Vous pouvez également inclure des classes dans vos modules :

```python
# Fichier : geometrie.py

class Rectangle:
    """Classe représentant un rectangle."""

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        """Calcule l'aire du rectangle."""
        return self.largeur * self.hauteur

    def perimetre(self):
        """Calcule le périmètre du rectangle."""
        return 2 * (self.largeur + self.hauteur)

class Cercle:
    """Classe représentant un cercle."""

    PI = 3.14159

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        """Calcule l'aire du cercle."""
        return self.PI * self.rayon ** 2

    def circonference(self):
        """Calcule la circonférence du cercle."""
        return 2 * self.PI * self.rayon
```

Utilisation :

```python
# Fichier : main.py

from geometrie import Rectangle, Cercle

rect = Rectangle(5, 3)  
print(f"Aire du rectangle : {rect.aire()}")  
print(f"Périmètre du rectangle : {rect.perimetre()}")  

cercle = Cercle(7)  
print(f"Aire du cercle : {cercle.aire()}")  
print(f"Circonférence du cercle : {cercle.circonference()}")  
```

---

## L'attribut `__name__`

Chaque module Python possède un attribut spécial `__name__`. Quand un fichier est exécuté directement, `__name__` vaut `"__main__"`. Quand il est importé, `__name__` vaut le nom du module.

Cela permet d'écrire du code qui ne s'exécute que lorsque le module est lancé directement :

```python
# Fichier : calculs.py

def carre(x):
    """Retourne le carré d'un nombre."""
    return x ** 2

def cube(x):
    """Retourne le cube d'un nombre."""
    return x ** 3

# Ce code ne s'exécute que si le fichier est lancé directement
if __name__ == "__main__":
    print("Test du module calculs")
    print(f"Carré de 5 : {carre(5)}")
    print(f"Cube de 3 : {cube(3)}")
```

Si vous exécutez `python calculs.py`, les tests s'afficheront. Mais si vous importez le module dans un autre fichier, les tests ne s'exécuteront pas :

```python
# Fichier : autre_fichier.py

import calculs  # Les tests ne s'affichent pas

resultat = calculs.carre(10)  
print(resultat)  # Affiche : 100  
```

---

## Organisation des modules

### Structure recommandée d'un module

Un module bien organisé suit généralement cette structure :

```python
"""
Module de gestion des utilisateurs.

Ce module fournit des fonctions pour créer, modifier et supprimer  
des utilisateurs dans l'application.  
"""

# Imports de la bibliothèque standard
import os  
import datetime  

# Imports de bibliothèques tierces
# import requests

# Imports locaux (vos propres modules)
# from .database import connexion

# Constantes du module
VERSION = "1.0.0"  
MAX_UTILISATEURS = 1000  

# Classes
class Utilisateur:
    """Représente un utilisateur du système."""

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.date_creation = datetime.datetime.now()

# Fonctions
def creer_utilisateur(nom, email):
    """
    Crée un nouvel utilisateur.

    Args:
        nom (str): Le nom de l'utilisateur
        email (str): L'email de l'utilisateur

    Returns:
        Utilisateur: L'objet utilisateur créé
    """
    return Utilisateur(nom, email)

# Code principal (tests, exemples)
if __name__ == "__main__":
    user = creer_utilisateur("Alice", "alice@example.com")
    print(f"Utilisateur créé : {user.nom}")
```

### Documentation des modules (docstrings)

Chaque module devrait avoir une docstring au début du fichier pour expliquer son rôle :

```python
"""
Module utilitaires.

Ce module contient diverses fonctions utilitaires pour  
le traitement de texte et les conversions de données.  

Fonctions principales:
    - nettoyer_texte : Supprime les espaces superflus
    - convertir_majuscules : Convertit un texte en majuscules
    - compter_mots : Compte le nombre de mots dans un texte

Exemple d'utilisation:
    import utilitaires
    texte_propre = utilitaires.nettoyer_texte("  Bonjour  monde  ")
"""

def nettoyer_texte(texte):
    """Supprime les espaces en début et fin de chaîne."""
    return texte.strip()

def convertir_majuscules(texte):
    """Convertit tout le texte en majuscules."""
    return texte.upper()

def compter_mots(texte):
    """Compte le nombre de mots dans le texte."""
    return len(texte.split())
```

---

## Chemins d'importation et `sys.path`

Python recherche les modules dans plusieurs emplacements définis dans `sys.path` :

```python
import sys

# Afficher tous les chemins de recherche
for chemin in sys.path:
    print(chemin)
```

L'ordre de recherche est :

1. Le répertoire du script en cours d'exécution
2. Les répertoires listés dans la variable d'environnement `PYTHONPATH`
3. Les répertoires d'installation par défaut de Python

Pour ajouter un chemin personnalisé temporairement :

```python
import sys

# Ajouter un nouveau chemin
sys.path.append('/chemin/vers/mes/modules')

# Maintenant vous pouvez importer depuis ce chemin
import mon_module
```

---

## Bonnes pratiques pour les modules

### 1. Un module, une responsabilité

Chaque module devrait avoir un objectif clair et défini :

```python
# ✅ BON : Module dédié aux opérations mathématiques
# Fichier : math_utils.py
def addition(a, b):
    return a + b

def moyenne(liste):
    return sum(liste) / len(liste)

# ❌ MAUVAIS : Module qui fait trop de choses différentes
# Fichier : tout.py
def addition(a, b):
    return a + b

def envoyer_email(destinataire):
    # Code pour envoyer un email
    pass

def dessiner_graphique(data):
    # Code pour dessiner
    pass
```

### 2. Nommer clairement vos modules

Utilisez des noms descriptifs en minuscules, avec des underscores si nécessaire :

```python
# ✅ BON
import gestion_utilisateurs  
import traitement_images  
import calculs_statistiques  

# ❌ MAUVAIS
import Gu  
import stuff  
import myModule123  
```

### 3. Éviter les imports circulaires

Les imports circulaires se produisent quand deux modules s'importent mutuellement :

```python
# ❌ MAUVAIS : Import circulaire

# Fichier : module_a.py
from module_b import fonction_b

def fonction_a():
    return fonction_b()

# Fichier : module_b.py
from module_a import fonction_a

def fonction_b():
    return fonction_a()
```

Solution : Restructurer le code ou importer localement dans les fonctions.

### 4. Utiliser des imports absolus

Préférez les imports absolus pour plus de clarté :

```python
# ✅ BON : Import absolu
from mon_projet.utilitaires.texte import nettoyer_texte

# ⚠️ Moins clair : Import relatif
from ..utilitaires.texte import nettoyer_texte
```

### 5. Regrouper les imports

Organisez vos imports par catégories :

```python
# Imports de la bibliothèque standard
import os  
import sys  
import datetime  

# Imports de bibliothèques tierces
import numpy as np  
import pandas as pd  

# Imports locaux
from mon_projet import config  
from mon_projet.utils import helpers  
```

---

## Recharger un module

Pendant le développement, si vous modifiez un module déjà importé, vous devez le recharger :

```python
import mon_module  
import importlib  

# Après avoir modifié mon_module.py
importlib.reload(mon_module)
```

Note : En général, il est plus simple de redémarrer l'interpréteur Python.

---

## Résumé

Dans cette section, vous avez appris :

- Comment importer des modules existants avec différentes syntaxes (`import`, `from ... import`)
- Comment créer vos propres modules en organisant votre code dans des fichiers séparés
- L'utilisation de `__name__` pour distinguer l'exécution directe de l'importation
- Les bonnes pratiques pour structurer et documenter vos modules
- Comment Python recherche les modules avec `sys.path`
- Les conventions de nommage et d'organisation

Les modules sont un concept fondamental en Python qui vous permet d'écrire du code plus organisé, réutilisable et maintenable. Dans les prochaines sections, nous verrons comment organiser plusieurs modules en packages et comment gérer les dépendances externes.

⏭️ [Structure des packages](/06-modules-et-packages/02-structure-des-packages.md)
