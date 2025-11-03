🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 13.1 Calcul numérique avec NumPy

## Introduction

Bienvenue dans le monde du calcul numérique avec Python ! Dans cette section, nous allons découvrir **NumPy** (Numerical Python), la bibliothèque fondamentale pour le calcul scientifique en Python. NumPy est utilisée par des millions de développeurs, scientifiques et data analysts à travers le monde.

## Qu'est-ce que NumPy ?

NumPy est une bibliothèque open-source qui fournit :

- **Des structures de données efficaces** : Les arrays (tableaux) NumPy permettent de stocker et manipuler de grandes quantités de données numériques
- **Des fonctions mathématiques optimisées** : Calculs vectorisés, algèbre linéaire, statistiques, et bien plus
- **Des performances exceptionnelles** : Les opérations NumPy sont écrites en C, ce qui les rend beaucoup plus rapides que le Python pur

### Petite histoire

NumPy a été créé en 2005 par Travis Oliphant en combinant les fonctionnalités de deux bibliothèques antérieures (Numeric et Numarray). Aujourd'hui, c'est la pierre angulaire de l'écosystème scientifique Python et la base de nombreuses autres bibliothèques populaires comme Pandas, SciPy, scikit-learn, et TensorFlow.

## Pourquoi utiliser NumPy ?

### 1. Performance

NumPy est beaucoup plus rapide que les listes Python pour les calculs numériques. Voici une comparaison simple :

```python
# Avec des listes Python (lent)
import time

liste = list(range(1000000))
debut = time.time()
resultat = [x * 2 for x in liste]
temps_liste = time.time() - debut
print(f"Temps avec liste Python: {temps_liste:.4f} secondes")

# Avec NumPy (rapide)
import numpy as np

arr = np.array(liste)
debut = time.time()
resultat = arr * 2
temps_numpy = time.time() - debut
print(f"Temps avec NumPy: {temps_numpy:.4f} secondes")
print(f"NumPy est {temps_liste/temps_numpy:.1f}x plus rapide!")
```

**Résultat typique** : NumPy est 10 à 100 fois plus rapide !

### 2. Simplicité du code

NumPy permet d'écrire du code plus concis et lisible :

```python
# Sans NumPy : multiplication élément par élément
liste1 = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
resultat = []
for i in range(len(liste1)):
    resultat.append(liste1[i] * liste2[i])
print(resultat)  # [10, 40, 90, 160, 250]

# Avec NumPy : une seule ligne !
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
resultat = arr1 * arr2
print(resultat)  # [10  40  90 160 250]
```

### 3. Fonctionnalités riches

NumPy offre une multitude de fonctions pour :

- **Calculs mathématiques** : trigonométrie, logarithmes, exponentielles
- **Statistiques** : moyenne, médiane, écart-type, corrélation
- **Algèbre linéaire** : produits matriciels, déterminants, inversions
- **Génération de nombres aléatoires** : distributions variées
- **Manipulation de données** : tri, recherche, filtrage

### 4. Efficacité mémoire

Les arrays NumPy utilisent moins de mémoire que les listes Python :

```python
import sys
import numpy as np

# Liste Python
liste_python = list(range(10000))
taille_liste = sys.getsizeof(liste_python)

# Array NumPy
array_numpy = np.array(range(10000))
taille_array = array_numpy.nbytes

print(f"Taille liste Python: {taille_liste} bytes")
print(f"Taille array NumPy: {taille_array} bytes")
print(f"NumPy utilise {taille_liste/taille_array:.1f}x moins de mémoire")
```

## Installation de NumPy

### Avec pip (recommandé)

La méthode la plus simple est d'utiliser pip :

```bash
pip install numpy
```

### Avec conda

Si vous utilisez Anaconda ou Miniconda :

```bash
conda install numpy
```

### Vérifier l'installation

Pour vérifier que NumPy est correctement installé :

```python
import numpy as np
print("Version de NumPy:", np.__version__)
```

## Importation de NumPy

Par convention, NumPy est toujours importé avec l'alias `np` :

```python
import numpy as np
```

**Pourquoi `np` ?**
- C'est une convention universelle dans la communauté Python
- Rend le code plus court : `np.array()` au lieu de `numpy.array()`
- Facilite la lecture et le partage de code

**❌ À éviter :**
```python
# N'utilisez pas ces formes
from numpy import *  # Pollue l'espace de noms
import numpy          # Trop long à écrire
```

**✅ Recommandé :**
```python
import numpy as np
```

## Vue d'ensemble des concepts NumPy

Avant de plonger dans les détails, voici un aperçu des principaux concepts que nous allons explorer :

### Les arrays (tableaux)

Le cœur de NumPy est l'objet **ndarray** (n-dimensional array) :

```python
import numpy as np

# Array 1D (vecteur)
vecteur = np.array([1, 2, 3, 4, 5])
print("Vecteur:", vecteur)

# Array 2D (matrice)
matrice = np.array([[1, 2, 3],
                    [4, 5, 6]])
print("Matrice:\n", matrice)

# Array 3D (tenseur)
tenseur = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
print("Tenseur:\n", tenseur)
```

### Types de données

NumPy utilise des types de données spécifiques pour optimiser la mémoire et les performances :

```python
# Entiers
arr_int = np.array([1, 2, 3], dtype=np.int32)
print("Type:", arr_int.dtype)  # int32

# Nombres à virgule flottante
arr_float = np.array([1.0, 2.5, 3.7], dtype=np.float64)
print("Type:", arr_float.dtype)  # float64

# Booléens
arr_bool = np.array([True, False, True], dtype=np.bool_)
print("Type:", arr_bool.dtype)  # bool
```

### Dimensions et formes

Les arrays peuvent avoir différentes dimensions :

```python
import numpy as np

# 1D : vecteur
arr_1d = np.array([1, 2, 3, 4])
print("Shape 1D:", arr_1d.shape)  # (4,)
print("Dimensions:", arr_1d.ndim)  # 1

# 2D : matrice
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Shape 2D:", arr_2d.shape)  # (2, 3) - 2 lignes, 3 colonnes
print("Dimensions:", arr_2d.ndim)  # 2

# 3D : tenseur
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print("Shape 3D:", arr_3d.shape)  # (2, 2, 2)
print("Dimensions:", arr_3d.ndim)  # 3
```

## Premier programme avec NumPy

Créons un petit programme qui illustre la puissance de NumPy :

```python
import numpy as np

# Créer des données de température (en Celsius)
temperatures_celsius = np.array([0, 10, 20, 25, 30, 35, 40])
print("Températures en Celsius:", temperatures_celsius)

# Convertir en Fahrenheit avec une seule opération
temperatures_fahrenheit = temperatures_celsius * 9/5 + 32
print("Températures en Fahrenheit:", temperatures_fahrenheit)

# Calculer des statistiques
print("\n--- Statistiques ---")
print(f"Température moyenne: {np.mean(temperatures_celsius):.1f}°C")
print(f"Température minimale: {np.min(temperatures_celsius)}°C")
print(f"Température maximale: {np.max(temperatures_celsius)}°C")
print(f"Écart-type: {np.std(temperatures_celsius):.2f}°C")

# Filtrer les températures > 25°C
jours_chauds = temperatures_celsius[temperatures_celsius > 25]
print(f"\nJours chauds (>25°C): {jours_chauds}")
print(f"Nombre de jours chauds: {len(jours_chauds)}")
```

**Sortie :**
```
Températures en Celsius: [ 0 10 20 25 30 35 40]
Températures en Fahrenheit: [ 32.  50.  68.  77.  86.  95. 104.]

--- Statistiques ---
Température moyenne: 22.9°C
Température minimale: 0°C
Température maximale: 40°C
Écart-type: 13.80°C

Jours chauds (>25°C): [30 35 40]
Nombre de jours chauds: 3
```

## Comparaison : Listes Python vs Arrays NumPy

Comprendre la différence est essentiel :

### Listes Python

```python
# Listes Python : flexibles mais lentes
liste = [1, 2, 3, 4, 5]

# Peuvent contenir différents types
liste_mixte = [1, "texte", 3.14, True]

# Opérations élément par élément nécessitent des boucles
liste_double = [x * 2 for x in liste]
```

**Avantages des listes :**
- Flexibles (types mixtes)
- Intégrées à Python (pas de bibliothèque externe)
- Faciles à comprendre

**Inconvénients des listes :**
- Lentes pour les calculs numériques
- Consomment plus de mémoire
- Nécessitent des boucles pour les opérations

### Arrays NumPy

```python
import numpy as np

# Arrays NumPy : optimisés pour les calculs
arr = np.array([1, 2, 3, 4, 5])

# Tous les éléments doivent être du même type
# arr_mixte = np.array([1, "texte", 3.14])  # Converti en strings

# Opérations vectorisées (sans boucle)
arr_double = arr * 2
```

**Avantages des arrays :**
- Très rapides pour les calculs
- Opérations vectorisées
- Moins de mémoire
- Fonctions mathématiques intégrées

**Inconvénients des arrays :**
- Tous les éléments doivent être du même type
- Taille fixe (difficile à redimensionner)
- Nécessite une bibliothèque externe

### Quand utiliser quoi ?

**Utilisez des listes Python quand :**
- Vous avez des données de types différents
- Vous devez ajouter/supprimer fréquemment des éléments
- Les performances ne sont pas critiques
- Les données ne sont pas numériques

**Utilisez des arrays NumPy quand :**
- Vous travaillez avec des données numériques
- Vous devez effectuer des calculs mathématiques
- Les performances sont importantes
- Vous manipulez de grandes quantités de données

## Cas d'usage de NumPy

NumPy est utilisé dans de nombreux domaines :

### 1. Science des données et Machine Learning

```python
import numpy as np

# Normalisation de données
donnees = np.array([10, 20, 30, 40, 50])
donnees_normalisees = (donnees - np.mean(donnees)) / np.std(donnees)
print("Données normalisées:", donnees_normalisees)
```

### 2. Traitement d'images

```python
# Une image est un array de pixels
# Par exemple, une image 100x100 en niveaux de gris
image = np.random.randint(0, 256, size=(100, 100))
print(f"Dimensions de l'image: {image.shape}")
print(f"Intensité moyenne: {np.mean(image):.2f}")
```

### 3. Analyse financière

```python
# Prix d'actions sur 5 jours
prix = np.array([100, 102, 98, 105, 107])

# Calculer les rendements journaliers
rendements = (prix[1:] - prix[:-1]) / prix[:-1] * 100
print("Rendements quotidiens (%):", rendements)
```

### 4. Simulations scientifiques

```python
# Simulation de la marche aléatoire
pas = np.random.choice([-1, 1], size=1000)  # 1000 pas aléatoires
position = np.cumsum(pas)  # Position cumulative
print(f"Position finale: {position[-1]}")
```

### 5. Traitement du signal

```python
# Génération d'un signal sinusoïdal
t = np.linspace(0, 1, 100)  # Temps de 0 à 1 seconde
frequence = 5  # 5 Hz
signal = np.sin(2 * np.pi * frequence * t)
print(f"Signal généré: {len(signal)} points")
```

## L'écosystème NumPy

NumPy est la base de nombreuses bibliothèques scientifiques Python :

### Bibliothèques construites sur NumPy

1. **Pandas** : Manipulation et analyse de données tabulaires
2. **SciPy** : Algorithmes scientifiques et techniques
3. **Matplotlib** : Visualisation de données
4. **scikit-learn** : Machine Learning
5. **TensorFlow / PyTorch** : Deep Learning
6. **OpenCV** : Traitement d'images

### Exemple d'intégration

```python
import numpy as np

# Créer des données avec NumPy
donnees = np.random.randn(100)

# Ces données peuvent être facilement utilisées avec d'autres bibliothèques
# import pandas as pd
# df = pd.DataFrame({'valeurs': donnees})

# import matplotlib.pyplot as plt
# plt.plot(donnees)
```

## Ressources et documentation

### Documentation officielle

- **Site officiel** : https://numpy.org/
- **Documentation** : https://numpy.org/doc/
- **Guide de démarrage** : https://numpy.org/doc/stable/user/quickstart.html

### Apprendre NumPy

- **Tutoriels officiels** : https://numpy.org/learn/
- **Exercices pratiques** : https://github.com/rougier/numpy-100
- **Cheat sheet** : https://numpy.org/doc/stable/user/absolute_beginners.html

### Communauté

- **GitHub** : https://github.com/numpy/numpy
- **Forum** : https://discuss.scientific-python.org/
- **Stack Overflow** : Tag `numpy`

## Conseils pour débuter

### 1. Pratiquez régulièrement

La meilleure façon d'apprendre NumPy est de l'utiliser. Essayez de résoudre des petits problèmes numériques chaque jour.

### 2. Consultez la documentation

La documentation NumPy est excellente. Utilisez `help()` ou consultez la documentation en ligne :

```python
import numpy as np

# Aide sur une fonction
help(np.array)

# Documentation en ligne
# https://numpy.org/doc/stable/reference/generated/numpy.array.html
```

### 3. Évitez les boucles

Essayez toujours de trouver une solution vectorisée plutôt qu'une boucle :

```python
# ❌ Moins bon
resultat = []
for x in arr:
    resultat.append(x * 2)

# ✅ Mieux
resultat = arr * 2
```

### 4. Utilisez les fonctions intégrées

NumPy a déjà implémenté la plupart des opérations courantes. Ne réinventez pas la roue !

```python
# NumPy a des fonctions pour presque tout
moyenne = np.mean(arr)
minimum = np.min(arr)
maximum = np.max(arr)
somme = np.sum(arr)
tri = np.sort(arr)
```

### 5. Commencez simple

Ne vous précipitez pas vers les fonctionnalités avancées. Maîtrisez d'abord les bases :
- Création d'arrays
- Opérations de base
- Indexation et slicing
- Fonctions mathématiques simples

## Structure de cette section

Cette section sur NumPy est organisée en plusieurs parties :

### 13.1.1 Arrays et opérations vectorisées
Vous apprendrez :
- Comment créer différents types d'arrays
- Les opérations vectorisées qui rendent NumPy si puissant
- Les fonctions mathématiques universelles
- Le broadcasting et les agrégations

### 13.1.2 Indexation et slicing avancés
Vous découvrirez :
- Comment accéder aux éléments d'un array
- Les techniques de slicing pour extraire des portions
- L'indexation booléenne pour filtrer des données
- L'indexation fancy pour des sélections complexes

Ces deux sections vous donneront une base solide pour utiliser NumPy efficacement dans vos projets de data science, d'analyse numérique, ou de calcul scientifique.

## Conclusion de l'introduction

NumPy est un outil indispensable pour quiconque travaille avec des données numériques en Python. Sa combinaison de performance, de simplicité et de fonctionnalités riches en fait la bibliothèque de référence pour le calcul scientifique.

Dans les sections suivantes, nous allons explorer en profondeur les arrays NumPy et apprendre à les manipuler avec efficacité. Préparez-vous à découvrir comment NumPy peut transformer votre façon de travailler avec les données numériques !

**Prêt à commencer ?** Passons maintenant à la section 13.1.1 pour explorer les arrays et les opérations vectorisées en détail !

⏭️ [Arrays et opérations vectorisées](/13-introduction-data-science/01.1-arrays-et-operations-vectorisees.md)
