🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Module 6 : Modules et packages

## Introduction

Dans ce module, nous allons explorer l'un des aspects les plus puissants de Python : son système de modules et packages. Cette fonctionnalité est au cœur de la philosophie Python qui privilégie la réutilisabilité du code et l'organisation claire des projets.

## Qu'est-ce qu'un module ?

Un **module** en Python est simplement un fichier contenant du code Python. Il peut définir des fonctions, des classes, des variables, et peut également contenir du code exécutable. Les modules permettent de :

- Organiser le code en unités logiques
- Réutiliser du code dans différents projets
- Éviter la duplication de code
- Faciliter la maintenance et les tests
- Créer des espaces de noms séparés

## Qu'est-ce qu'un package ?

Un **package** est une collection de modules organisés dans une structure hiérarchique de répertoires. Les packages permettent de :

- Structurer de gros projets en sous-modules
- Éviter les conflits de noms entre modules
- Créer des bibliothèques distribuables
- Organiser le code de manière logique et intuitive

## Pourquoi les modules et packages sont-ils importants ?

### 1. **Réutilisabilité**
Au lieu de réécrire le même code, vous pouvez créer des modules réutilisables dans différents projets.

### 2. **Maintenir la simplicité**
Diviser un gros programme en modules plus petits rend le code plus facile à comprendre et à maintenir.

### 3. **Collaboration**
Les modules facilitent le travail en équipe en permettant à différents développeurs de travailler sur différentes parties du projet.

### 4. **Écosystème Python**
Python dispose d'un écosystème riche de packages tiers via PyPI (Python Package Index) avec plus de 400 000 packages disponibles.

## Types de modules

### Modules intégrés (Built-in)
Ces modules font partie de l'installation standard de Python :
- `os` : interaction avec le système d'exploitation
- `sys` : accès aux paramètres et fonctions de l'interpréteur
- `math` : fonctions mathématiques
- `datetime` : gestion des dates et heures

### Modules de la bibliothèque standard
Python est livré avec une riche bibliothèque standard comprenant des centaines de modules prêts à l'emploi.

### Modules tiers
Créés par la communauté et disponibles via PyPI :
- `requests` : requêtes HTTP simplifiées
- `numpy` : calcul numérique
- `pandas` : manipulation de données
- `flask` : framework web léger

### Modules personnalisés
Modules que vous créez vous-même pour vos projets spécifiques.

## Structure d'un package Python

Un package Python typique a cette structure :

```
mon_package/
├── __init__.py
├── module1.py
├── module2.py
├── sous_package/
│   ├── __init__.py
│   ├── module3.py
│   └── module4.py
└── tests/
    ├── __init__.py
    ├── test_module1.py
    └── test_module2.py
```

## Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. **Créer et utiliser des modules** personnalisés
2. **Comprendre les différents types d'importation** et choisir la méthode appropriée
3. **Structurer des packages** complexes avec des sous-packages
4. **Gérer les dépendances** de vos projets avec pip
5. **Créer et utiliser des environnements virtuels** pour isoler vos projets
6. **Distribuer vos propres packages** sur PyPI

## Prérequis

Avant d'aborder ce module, vous devez être à l'aise avec :

- Les concepts de base de Python (variables, fonctions, classes)
- La manipulation de fichiers et répertoires
- Les concepts de portée des variables
- L'utilisation de base de la ligne de commande

## Bonnes pratiques à retenir

Tout au long de ce module, nous mettrons l'accent sur les bonnes pratiques :

- **Nommage cohérent** : utilisez des noms descriptifs et suivez les conventions PEP 8
- **Documentation** : documentez vos modules avec des docstrings
- **Organisation logique** : regroupez les fonctionnalités similaires
- **Gestion des dépendances** : utilisez des environnements virtuels
- **Tests** : testez vos modules de manière isolée

## Outils que nous utiliserons

- **Python** : interpréteur Python 3.x
- **pip** : gestionnaire de packages Python
- **venv** : création d'environnements virtuels
- **setuptools** : création de packages distribuables
- **PyPI** : Python Package Index

---

*Dans les sections suivantes, nous allons explorer en détail chaque aspect des modules et packages, en commençant par les techniques d'importation et la création de modules personnalisés.*

⏭️
