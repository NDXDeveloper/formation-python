🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.1 : Architecture de projet

## Introduction

L'architecture de projet est comme l'organisation d'une maison : une bonne structure facilite la vie quotidienne, tandis qu'une mauvaise organisation rend tout plus compliqué. Dans le développement Python, une architecture bien pensée permet de :

- Retrouver facilement le code recherché
- Ajouter de nouvelles fonctionnalités sans casser l'existant
- Collaborer efficacement avec d'autres développeurs
- Maintenir et déboguer le code plus facilement

## Pourquoi l'architecture est-elle importante ?

### Le problème du "code spaghetti"

Imaginez un projet qui commence simple :

```
mon_projet/
├── main.py (500 lignes)
├── utils.py (200 lignes)
└── data.txt
```

Puis qui grandit anarchiquement :

```
mon_projet/
├── main.py (2000 lignes)
├── utils.py (800 lignes)
├── autre_truc.py (600 lignes)
├── temp.py
├── test_machin.py
├── data.txt
├── backup_data.txt
└── old_main.py
```

**Problèmes rencontrés :**
- Difficile de trouver une fonction spécifique
- Modifications risquées (tout est interconnecté)
- Code dupliqué partout
- Impossible de tester facilement

### Les bénéfices d'une bonne architecture

```
mon_projet/
├── src/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── __init__.py
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

**Avantages :**
- Chaque élément a sa place
- Facile à naviguer
- Modifications localisées
- Tests organisés
- Documentation accessible

## Structure de projet Python standard

### La structure de base

Voici la structure recommandée pour un projet Python :

```
mon_projet/
├── README.md              # Description du projet
├── requirements.txt       # Dépendances
├── setup.py              # Configuration d'installation
├── .gitignore            # Fichiers à ignorer par Git
├── src/                  # Code source principal
│   └── mon_projet/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       ├── services/
│       └── utils/
├── tests/                # Tests unitaires
│   ├── __init__.py
│   ├── test_main.py
│   └── test_services.py
├── docs/                 # Documentation
│   └── guide.md
└── data/                 # Données (optionnel)
    └── sample.csv
```

### Détail des dossiers

#### 1. Dossier `src/` (Source)
Contient tout le code de votre application.

**Pourquoi un dossier `src/` ?**
- Sépare clairement le code source des autres fichiers
- Évite les conflits d'imports
- Facilite le packaging

#### 2. Dossier `tests/`
Contient tous les tests de votre application.

**Organisation recommandée :**
```
tests/
├── __init__.py
├── test_models.py        # Tests des modèles
├── test_services.py      # Tests des services
├── test_utils.py         # Tests des utilitaires
└── fixtures/             # Données de test
    └── sample_data.json
```

#### 3. Fichiers à la racine
- `README.md` : Description, installation, utilisation
- `requirements.txt` : Liste des dépendances
- `setup.py` : Configuration du package
- `.gitignore` : Fichiers à ignorer par Git

## Organisation du code source

### Principe de séparation des responsabilités

Chaque module doit avoir une responsabilité claire :

```
src/mon_projet/
├── __init__.py
├── main.py               # Point d'entrée
├── models/               # Structures de données
│   ├── __init__.py
│   ├── user.py
│   └── product.py
├── services/             # Logique métier
│   ├── __init__.py
│   ├── user_service.py
│   └── product_service.py
├── utils/                # Fonctions utilitaires
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
└── config/               # Configuration
    ├── __init__.py
    └── settings.py
```

### Exemple pratique : Application de gestion de livres

Créons une application simple de gestion de livres :

#### Structure du projet

```
bibliotheque/
├── README.md
├── requirements.txt
├── src/
│   └── bibliotheque/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── book.py
│       │   └── author.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── book_service.py
│       │   └── library_service.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
└── tests/
    ├── __init__.py
    ├── test_models.py
    └── test_services.py
```

#### Contenu des fichiers

**src/bibliotheque/models/book.py**
```python
"""Modèle représentant un livre."""

class Book:
    """Représente un livre dans la bibliothèque."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} par {self.author}"

    def borrow(self):
        """Emprunte le livre."""
        if self.is_borrowed:
            raise ValueError("Le livre est déjà emprunté")
        self.is_borrowed = True

    def return_book(self):
        """Retourne le livre."""
        if not self.is_borrowed:
            raise ValueError("Le livre n'est pas emprunté")
        self.is_borrowed = False
```

**src/bibliotheque/services/book_service.py**
```python
"""Service pour la gestion des livres."""

from ..models.book import Book

class BookService:
    """Service pour gérer les opérations sur les livres."""

    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        """Ajoute un livre à la collection."""
        book = Book(title, author, isbn)
        self.books.append(book)
        return book

    def find_book(self, isbn):
        """Trouve un livre par son ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_available_books(self):
        """Liste tous les livres disponibles."""
        return [book for book in self.books if not book.is_borrowed]
```

**src/bibliotheque/main.py**
```python
"""Point d'entrée de l'application."""

from .services.book_service import BookService

def main():
    """Fonction principale de l'application."""
    print("=== Bienvenue dans la Bibliothèque ===")

    # Création du service
    book_service = BookService()

    # Ajout de quelques livres
    book_service.add_book("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789")
    book_service.add_book("1984", "George Orwell", "987654321")

    # Affichage des livres disponibles
    print("\nLivres disponibles:")
    for book in book_service.list_available_books():
        print(f"- {book}")

if __name__ == "__main__":
    main()
```

## Gestion des dépendances

### Le fichier requirements.txt

Le fichier `requirements.txt` liste toutes les bibliothèques externes nécessaires :

```
# requirements.txt
requests==2.28.1
pandas==1.5.2
numpy>=1.21.0
pytest==7.2.0
```

**Formats acceptés :**
- `package==1.0.0` : Version exacte
- `package>=1.0.0` : Version minimale
- `package~=1.0.0` : Version compatible

### Générer requirements.txt

```bash
# Installer les packages
pip install requests pandas numpy

# Générer le fichier requirements.txt
pip freeze > requirements.txt
```

### Installer les dépendances

```bash
# Installer toutes les dépendances
pip install -r requirements.txt
```

## Environnements virtuels

### Pourquoi utiliser des environnements virtuels ?

Sans environnement virtuel, tous les packages sont installés globalement :

```
Système global
├── Python 3.9
├── requests 2.28.1 (pour projet A)
├── requests 2.25.0 (pour projet B) ❌ CONFLIT!
└── pandas 1.5.2
```

Avec des environnements virtuels :

```
Projet A
├── Python 3.9
├── requests 2.28.1
└── pandas 1.5.2

Projet B
├── Python 3.9
├── requests 2.25.0
└── numpy 1.21.0
```

### Créer et utiliser un environnement virtuel

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Activer l'environnement (macOS/Linux)
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Désactiver l'environnement
deactivate
```

## Le fichier __init__.py

### Rôle du fichier __init__.py

Le fichier `__init__.py` transforme un dossier en package Python :

```
mon_package/
├── __init__.py      # Fait de mon_package un package
├── module1.py
└── module2.py
```

### Contrôler les imports

**src/bibliotheque/__init__.py**
```python
"""Package principal de la bibliothèque."""

# Facilite les imports pour les utilisateurs
from .models.book import Book
from .services.book_service import BookService

# Définit ce qui est accessible avec "from bibliotheque import *"
__all__ = ['Book', 'BookService']

# Métadonnées du package
__version__ = "1.0.0"
__author__ = "Votre Nom"
```

**Utilisation simplifiée :**
```python
# Au lieu de :
from bibliotheque.models.book import Book
from bibliotheque.services.book_service import BookService

# On peut écrire :
from bibliotheque import Book, BookService
```

## Configuration et paramètres

### Fichier de configuration

**src/bibliotheque/config/settings.py**
```python
"""Configuration de l'application."""

import os

class Config:
    """Configuration de base."""

    # Paramètres de base
    APP_NAME = "Bibliothèque"
    VERSION = "1.0.0"

    # Chemins
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    # Paramètres métier
    MAX_BOOKS_PER_USER = 3
    LOAN_DURATION_DAYS = 14

    # Variables d'environnement
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///library.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

class DevelopmentConfig(Config):
    """Configuration pour le développement."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuration pour la production."""
    DEBUG = False
    TESTING = False

# Configuration par défaut
config = DevelopmentConfig()
```

### Utilisation de la configuration

```python
from .config.settings import config

def create_database_connection():
    """Crée une connexion à la base de données."""
    return connect(config.DATABASE_URL)

def get_max_books():
    """Retourne le nombre maximum de livres par utilisateur."""
    return config.MAX_BOOKS_PER_USER
```

## Bonnes pratiques d'architecture

### 1. Nommage cohérent

```python
# ✅ Bon
user_service.py
book_model.py
email_validator.py

# ❌ Mauvais
usrSvc.py
bookMODEL.py
validate_email_function.py
```

### 2. Un fichier, une responsabilité

```python
# ✅ Bon : Un modèle par fichier
# models/user.py
class User:
    pass

# models/book.py
class Book:
    pass

# ❌ Mauvais : Tout dans un fichier
# models.py
class User:
    pass

class Book:
    pass

class Author:
    pass
```

### 3. Imports organisés

```python
# ✅ Bon ordre des imports
# 1. Bibliothèques standard
import os
import sys
from datetime import datetime

# 2. Bibliothèques tierces
import requests
import pandas as pd

# 3. Modules locaux
from .models.book import Book
from .services.book_service import BookService
```

### 4. Documentation des modules

```python
"""Module de gestion des livres.

Ce module contient les classes et fonctions nécessaires
pour gérer les livres dans la bibliothèque.

Classes:
    Book: Représente un livre
    BookService: Service de gestion des livres

Fonctions:
    validate_isbn: Valide un numéro ISBN
"""

class Book:
    """Représente un livre dans la bibliothèque."""
    pass
```

## Exemple complet : Projet calculatrice

Créons une calculatrice simple avec une architecture propre :

### Structure

```
calculatrice/
├── README.md
├── requirements.txt
├── src/
│   └── calculatrice/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── calculator.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── calculation_service.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
└── tests/
    ├── __init__.py
    ├── test_calculator.py
    └── test_services.py
```

### Code

**src/calculatrice/models/calculator.py**
```python
"""Modèle de calculatrice."""

class Calculator:
    """Calculatrice simple avec historique."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Addition de deux nombres."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Soustraction de deux nombres."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiplication de deux nombres."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Division de deux nombres."""
        if b == 0:
            raise ValueError("Division par zéro impossible")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """Retourne l'historique des calculs."""
        return self.history.copy()
```

**src/calculatrice/services/calculation_service.py**
```python
"""Service de calcul avec validation."""

from ..models.calculator import Calculator
from ..utils.validators import validate_number

class CalculationService:
    """Service pour effectuer des calculs validés."""

    def __init__(self):
        self.calculator = Calculator()

    def perform_operation(self, operation, a, b):
        """Effectue une opération avec validation."""
        # Validation des entrées
        validate_number(a)
        validate_number(b)

        # Exécution de l'opération
        operations = {
            '+': self.calculator.add,
            '-': self.calculator.subtract,
            '*': self.calculator.multiply,
            '/': self.calculator.divide
        }

        if operation not in operations:
            raise ValueError(f"Opération non supportée: {operation}")

        return operations[operation](a, b)

    def get_history(self):
        """Retourne l'historique des calculs."""
        return self.calculator.get_history()
```

**src/calculatrice/utils/validators.py**
```python
"""Fonctions de validation."""

def validate_number(value):
    """Valide qu'une valeur est un nombre."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Attendu un nombre, reçu {type(value).__name__}")

    if isinstance(value, float) and (value != value):  # NaN
        raise ValueError("NaN n'est pas autorisé")
```

**src/calculatrice/main.py**
```python
"""Interface utilisateur de la calculatrice."""

from .services.calculation_service import CalculationService

def main():
    """Fonction principale."""
    print("=== Calculatrice ===")
    service = CalculationService()

    while True:
        try:
            # Saisie utilisateur
            expression = input("\nEntrez votre calcul (ou 'q' pour quitter): ")

            if expression.lower() == 'q':
                break

            if expression.lower() == 'history':
                print("\nHistorique:")
                for calculation in service.get_history():
                    print(f"  {calculation}")
                continue

            # Parsing simple (pour la démonstration)
            parts = expression.split()
            if len(parts) != 3:
                print("Format: nombre opérateur nombre")
                continue

            a = float(parts[0])
            operation = parts[1]
            b = float(parts[2])

            # Calcul
            result = service.perform_operation(operation, a, b)
            print(f"Résultat: {result}")

        except (ValueError, TypeError) as e:
            print(f"Erreur: {e}")
        except KeyboardInterrupt:
            print("\nAu revoir!")
            break

if __name__ == "__main__":
    main()
```

## Résumé

Une bonne architecture de projet Python comprend :

1. **Structure claire** : Séparation des responsabilités
2. **Nommage cohérent** : Conventions respectées
3. **Gestion des dépendances** : requirements.txt et environnements virtuels
4. **Configuration centralisée** : Paramètres regroupés
5. **Documentation** : README et docstrings
6. **Tests organisés** : Structure miroir du code source

Cette architecture vous permettra de développer des projets maintenables, évolutifs et faciles à comprendre pour toute votre équipe.

## Exercices pratiques

1. **Restructurer un projet existant** : Prenez un ancien projet et réorganisez-le selon ces principes
2. **Créer un nouveau projet** : Développez une application de gestion de tâches avec cette architecture
3. **Analyser des projets open source** : Étudiez la structure de projets populaires sur GitHub

La prochaine étape sera d'apprendre à gérer efficacement le versioning de votre code avec Git !

⏭️
