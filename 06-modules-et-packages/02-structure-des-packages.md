🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.2 Structure des packages

## Introduction

Un package en Python est une manière d'organiser plusieurs modules dans une structure hiérarchique en utilisant des dossiers. Alors qu'un module est un simple fichier Python, un package est un dossier contenant plusieurs modules et potentiellement d'autres packages.

Les packages permettent de structurer de grands projets en regroupant logiquement les modules liés entre eux, créant ainsi une architecture claire et maintenable.

---

## Différence entre module et package

Pour bien comprendre, voici la distinction :

- **Module** : Un fichier Python unique (`.py`)
  ```
  mon_module.py
  ```

- **Package** : Un dossier contenant plusieurs modules Python et un fichier spécial `__init__.py`
  ```
  mon_package/
      __init__.py
      module1.py
      module2.py
  ```

**Analogie :** Si les modules sont comme des livres, les packages sont comme des bibliothèques qui organisent ces livres par catégories et sections.

---

## Création d'un package simple

### Structure de base

Créons notre premier package. Voici la structure des fichiers :

```
mon_projet/
    main.py
    mathematiques/
        __init__.py
        operations.py
        geometrie.py
```

### Le fichier `__init__.py`

Le fichier `__init__.py` est un fichier spécial qui indique à Python qu'un dossier est un package. Il peut être vide ou contenir du code d'initialisation.

**Fichier : `mathematiques/__init__.py`** (peut être vide pour l'instant)
```python
# Ce fichier peut être vide
```

### Création des modules du package

**Fichier : `mathematiques/operations.py`**
```python
"""Module contenant des opérations mathématiques de base."""

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
        raise ValueError("Division par zéro impossible")
    return a / b
```

**Fichier : `mathematiques/geometrie.py`**
```python
"""Module contenant des fonctions de géométrie."""

PI = 3.14159

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle."""
    return PI * rayon ** 2

def aire_rectangle(largeur, hauteur):
    """Calcule l'aire d'un rectangle."""
    return largeur * hauteur

def perimetre_rectangle(largeur, hauteur):
    """Calcule le périmètre d'un rectangle."""
    return 2 * (largeur + hauteur)
```

### Utilisation du package

**Fichier : `main.py`**
```python
# Méthode 1 : Importer le module complet
import mathematiques.operations
import mathematiques.geometrie

resultat1 = mathematiques.operations.addition(10, 5)
print(f"10 + 5 = {resultat1}")

aire = mathematiques.geometrie.aire_cercle(7)
print(f"Aire du cercle : {aire}")

# Méthode 2 : Importer le module avec un alias
import mathematiques.operations as ops

resultat2 = ops.multiplication(6, 7)
print(f"6 × 7 = {resultat2}")

# Méthode 3 : Importer des fonctions spécifiques
from mathematiques.geometrie import aire_rectangle

aire_rect = aire_rectangle(5, 3)
print(f"Aire du rectangle : {aire_rect}")
```

---

## Le rôle du fichier `__init__.py`

### Package avec `__init__.py` vide

Dans les versions récentes de Python (3.3+), un package peut fonctionner avec un `__init__.py` vide ou même sans ce fichier (namespace packages). Cependant, il est recommandé de l'inclure pour la compatibilité et la clarté.

### Initialisation du package

Le fichier `__init__.py` s'exécute lors de l'importation du package. Vous pouvez l'utiliser pour :

1. **Importer des éléments pour simplifier l'accès**

**Fichier : `mathematiques/__init__.py`**
```python
"""Package de fonctions mathématiques."""

# Importer les fonctions des sous-modules
from .operations import addition, soustraction, multiplication, division
from .geometrie import aire_cercle, aire_rectangle, perimetre_rectangle

# Version du package
__version__ = "1.0.0"

# Liste des éléments exportés
__all__ = [
    'addition',
    'soustraction',
    'multiplication',
    'division',
    'aire_cercle',
    'aire_rectangle',
    'perimetre_rectangle'
]
```

Maintenant, l'utilisation devient plus simple :

```python
# Au lieu de : from mathematiques.operations import addition
# On peut écrire :
from mathematiques import addition, multiplication

resultat = addition(10, 5)
print(resultat)
```

2. **Définir des variables ou constantes du package**

```python
# mathematiques/__init__.py

"""Package mathématiques."""

# Constantes du package
VERSION = "1.0.0"
PRECISION = 10

# Configuration par défaut
CONFIG = {
    'mode': 'standard',
    'arrondi': 2
}

# Imports simplifiés
from .operations import *
from .geometrie import *
```

3. **Exécuter du code d'initialisation**

```python
# mathematiques/__init__.py

"""Package mathématiques avec initialisation."""

print("Initialisation du package mathématiques...")

# Vérifications ou configurations
import sys

if sys.version_info < (3, 6):
    raise RuntimeError("Ce package nécessite Python 3.6 ou supérieur")

# Imports
from .operations import addition, soustraction
from .geometrie import aire_cercle

print("Package mathématiques chargé avec succès !")
```

---

## Packages imbriqués (sous-packages)

Les packages peuvent contenir d'autres packages, créant ainsi une hiérarchie multi-niveaux.

### Structure d'un projet avec sous-packages

```
mon_application/
    main.py
    utilitaires/
        __init__.py
        texte/
            __init__.py
            formatage.py
            validation.py
        fichiers/
            __init__.py
            lecture.py
            ecriture.py
        mathematiques/
            __init__.py
            calculs.py
```

### Exemple de sous-package

**Structure des fichiers :**

```
utilitaires/
    __init__.py
    texte/
        __init__.py
        formatage.py
        validation.py
```

**Fichier : `utilitaires/texte/formatage.py`**
```python
"""Module de formatage de texte."""

def mettre_en_majuscules(texte):
    """Convertit le texte en majuscules."""
    return texte.upper()

def mettre_en_minuscules(texte):
    """Convertit le texte en minuscules."""
    return texte.lower()

def capitaliser(texte):
    """Met la première lettre de chaque mot en majuscule."""
    return texte.title()

def nettoyer(texte):
    """Supprime les espaces superflus."""
    return ' '.join(texte.split())
```

**Fichier : `utilitaires/texte/validation.py`**
```python
"""Module de validation de texte."""

import re

def est_email_valide(email):
    """Vérifie si l'email est valide."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def est_telephone_valide(telephone):
    """Vérifie si le numéro de téléphone est valide (format français)."""
    pattern = r'^0[1-9](\d{2}){4}$'
    return bool(re.match(pattern, telephone.replace(' ', '')))

def contient_chiffres(texte):
    """Vérifie si le texte contient des chiffres."""
    return bool(re.search(r'\d', texte))
```

**Fichier : `utilitaires/texte/__init__.py`**
```python
"""Sous-package pour le traitement de texte."""

from .formatage import (
    mettre_en_majuscules,
    mettre_en_minuscules,
    capitaliser,
    nettoyer
)

from .validation import (
    est_email_valide,
    est_telephone_valide,
    contient_chiffres
)

__all__ = [
    'mettre_en_majuscules',
    'mettre_en_minuscules',
    'capitaliser',
    'nettoyer',
    'est_email_valide',
    'est_telephone_valide',
    'contient_chiffres'
]
```

**Fichier : `utilitaires/__init__.py`**
```python
"""Package utilitaires principal."""

__version__ = "1.0.0"

# Faciliter l'accès aux sous-packages
from . import texte
from . import fichiers
```

### Utilisation des sous-packages

```python
# Méthode 1 : Import complet
import utilitaires.texte.formatage

texte = "bonjour le monde"
resultat = utilitaires.texte.formatage.mettre_en_majuscules(texte)
print(resultat)  # BONJOUR LE MONDE

# Méthode 2 : Import avec alias
from utilitaires.texte import formatage as fmt

resultat = fmt.capitaliser("bonjour le monde")
print(resultat)  # Bonjour Le Monde

# Méthode 3 : Import direct des fonctions
from utilitaires.texte import mettre_en_majuscules, est_email_valide

print(mettre_en_majuscules("python"))  # PYTHON
print(est_email_valide("test@example.com"))  # True

# Méthode 4 : Import du sous-package
from utilitaires import texte

resultat = texte.nettoyer("  trop    d'espaces  ")
print(resultat)  # "trop d'espaces"
```

---

## Imports relatifs dans les packages

À l'intérieur d'un package, vous pouvez utiliser des imports relatifs pour référencer d'autres modules du même package.

### Syntaxe des imports relatifs

- `.` : Répertoire courant
- `..` : Répertoire parent
- `...` : Deux niveaux au-dessus

### Exemple pratique

**Structure :**
```
application/
    __init__.py
    core/
        __init__.py
        moteur.py
        config.py
    utils/
        __init__.py
        helpers.py
    interface/
        __init__.py
        ui.py
```

**Fichier : `application/core/moteur.py`**
```python
"""Module principal du moteur."""

# Import relatif du même package
from .config import PARAMETRES

# Import relatif d'un package parent
from ..utils.helpers import logger

class Moteur:
    """Classe principale du moteur."""

    def __init__(self):
        self.config = PARAMETRES
        logger("Moteur initialisé")

    def demarrer(self):
        """Démarre le moteur."""
        logger("Démarrage du moteur...")
        print(f"Moteur démarré avec config : {self.config}")
```

**Fichier : `application/core/config.py`**
```python
"""Configuration du moteur."""

PARAMETRES = {
    'version': '1.0',
    'mode': 'production',
    'debug': False
}
```

**Fichier : `application/utils/helpers.py`**
```python
"""Fonctions utilitaires."""

import datetime

def logger(message):
    """Affiche un message avec timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
```

**Fichier : `application/interface/ui.py`**
```python
"""Interface utilisateur."""

# Import depuis le package core (niveau supérieur puis descente)
from ..core.moteur import Moteur

def lancer_application():
    """Lance l'application."""
    moteur = Moteur()
    moteur.demarrer()
```

### Quand utiliser les imports relatifs ?

**✅ Utilisez les imports relatifs :**
- À l'intérieur d'un package pour référencer d'autres modules du même package
- Pour maintenir la portabilité du package
- Dans les packages destinés à être distribués

**❌ Évitez les imports relatifs :**
- Dans le script principal (fichier lancé directement)
- Pour importer des packages externes
- Si cela rend le code moins lisible

---

## Structure de projet recommandée

### Petit projet

Pour un petit projet, une structure simple suffit :

```
mon_projet/
    README.md
    requirements.txt
    main.py
    mon_package/
        __init__.py
        module1.py
        module2.py
    tests/
        test_module1.py
        test_module2.py
```

### Projet moyen

Pour un projet plus complexe :

```
mon_projet/
    README.md
    requirements.txt
    setup.py
    docs/
        index.md
        guide.md
    src/
        mon_application/
            __init__.py
            core/
                __init__.py
                moteur.py
                config.py
            utils/
                __init__.py
                helpers.py
                validators.py
            interface/
                __init__.py
                cli.py
                gui.py
    tests/
        __init__.py
        test_core/
            test_moteur.py
            test_config.py
        test_utils/
            test_helpers.py
    scripts/
        run.py
```

### Grand projet

Pour un projet d'entreprise complexe :

```
mon_projet/
    README.md
    LICENSE
    setup.py
    requirements/
        base.txt
        dev.txt
        prod.txt
    docs/
        source/
            conf.py
            index.rst
    src/
        mon_application/
            __init__.py
            __main__.py
            api/
                __init__.py
                routes/
                    __init__.py
                    users.py
                    products.py
                models/
                    __init__.py
                    user.py
                    product.py
            core/
                __init__.py
                database.py
                auth.py
                config.py
            utils/
                __init__.py
                decorators.py
                validators.py
                helpers.py
            services/
                __init__.py
                email.py
                notifications.py
    tests/
        unit/
            test_api/
            test_core/
            test_utils/
        integration/
            test_database.py
            test_api.py
    scripts/
        deploy.py
        migrate.py
    data/
        sample_data.json
```

---

## Fichier `__main__.py`

Le fichier `__main__.py` permet d'exécuter un package comme un script avec `python -m nom_package`.

### Exemple

**Structure :**
```
calculatrice/
    __init__.py
    __main__.py
    operations.py
```

**Fichier : `calculatrice/__main__.py`**
```python
"""Point d'entrée du package calculatrice."""

from .operations import addition, soustraction

def main():
    """Fonction principale."""
    print("=== Calculatrice ===")

    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))

    print(f"\n{a} + {b} = {addition(a, b)}")
    print(f"{a} - {b} = {soustraction(a, b)}")

if __name__ == "__main__":
    main()
```

**Fichier : `calculatrice/operations.py`**
```python
"""Opérations mathématiques."""

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
```

**Utilisation :**
```bash
python -m calculatrice
```

---

## L'attribut `__all__`

L'attribut `__all__` définit ce qui est exporté lors d'un `from package import *`.

### Sans `__all__`

```python
# module.py
def fonction_publique():
    pass

def _fonction_privee():
    pass

CONSTANTE = 42
```

```python
# Importe tout (y compris _fonction_privee)
from module import *
```

### Avec `__all__`

```python
# module.py
def fonction_publique():
    pass

def _fonction_privee():
    pass

CONSTANTE = 42

# Définir explicitement ce qui est exporté
__all__ = ['fonction_publique', 'CONSTANTE']
```

```python
# Importe seulement fonction_publique et CONSTANTE
from module import *
```

### Dans un package

**Fichier : `mon_package/__init__.py`**
```python
"""Mon package avec exports contrôlés."""

from .module1 import fonction_a, fonction_b
from .module2 import classe_c

# Contrôler ce qui est accessible avec "from mon_package import *"
__all__ = [
    'fonction_a',
    'fonction_b',
    'classe_c'
]
```

---

## Bonnes pratiques pour la structure des packages

### 1. Une hiérarchie claire et logique

Organisez vos modules par fonctionnalité, pas par type de fichier :

```
✅ BON :
mon_app/
    utilisateurs/
        models.py
        views.py
        services.py
    produits/
        models.py
        views.py
        services.py

❌ MAUVAIS :
mon_app/
    models/
        user.py
        product.py
    views/
        user.py
        product.py
```

### 2. Nommage cohérent

- **Packages et modules** : minuscules, avec underscores si nécessaire
  ```
  mon_package/
      sous_module.py
      traitement_donnees.py
  ```

- **Classes** : PascalCase
  ```python
  class GestionnaireUtilisateur:
      pass
  ```

- **Fonctions et variables** : snake_case
  ```python
  def calculer_moyenne(liste_nombres):
      valeur_moyenne = sum(liste_nombres) / len(liste_nombres)
      return valeur_moyenne
  ```

### 3. Documentation du package

Chaque package doit avoir une documentation claire dans son `__init__.py` :

```python
"""
Package de gestion des utilisateurs.

Ce package fournit des outils pour créer, modifier et gérer
les utilisateurs de l'application.

Modules:
    - models : Définitions des modèles de données
    - services : Logique métier
    - validators : Validation des données

Exemple d'utilisation:
    from utilisateurs import creer_utilisateur

    user = creer_utilisateur("Alice", "alice@example.com")
"""

__version__ = "1.0.0"
__author__ = "Votre Nom"

from .services import creer_utilisateur, modifier_utilisateur
from .models import Utilisateur

__all__ = ['creer_utilisateur', 'modifier_utilisateur', 'Utilisateur']
```

### 4. Éviter les imports circulaires

Structure problématique :
```python
# ❌ package_a/__init__.py
from package_b import fonction_b

# ❌ package_b/__init__.py
from package_a import fonction_a
```

Solutions :
- Restructurer le code
- Utiliser des imports locaux dans les fonctions
- Créer un troisième module pour les dépendances communes

### 5. Séparer la logique de l'interface

```
application/
    __init__.py
    core/              # Logique métier (réutilisable)
        __init__.py
        business.py
    interface/         # Interface utilisateur
        __init__.py
        cli.py         # Interface ligne de commande
        web.py         # Interface web
```

### 6. Isoler les dépendances externes

```python
# ✅ BON : Isoler les imports de bibliothèques externes
# mon_package/external.py
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

def fetch_data(url):
    if not REQUESTS_AVAILABLE:
        raise RuntimeError("La bibliothèque requests n'est pas installée")
    return requests.get(url)
```

---

## Exemple complet : Package de gestion de bibliothèque

Voici un exemple concret de package bien structuré :

```
bibliotheque/
    __init__.py
    __main__.py
    models/
        __init__.py
        livre.py
        auteur.py
        emprunt.py
    services/
        __init__.py
        gestion_livres.py
        gestion_emprunts.py
    utils/
        __init__.py
        validation.py
        formatage.py
    data/
        __init__.py
        database.py
```

**Fichier : `bibliotheque/__init__.py`**
```python
"""
Package de gestion de bibliothèque.

Ce package permet de gérer une bibliothèque : livres, auteurs et emprunts.
"""

__version__ = "1.0.0"

# Exports principaux
from .models import Livre, Auteur, Emprunt
from .services import (
    ajouter_livre,
    rechercher_livre,
    emprunter_livre,
    retourner_livre
)

__all__ = [
    'Livre',
    'Auteur',
    'Emprunt',
    'ajouter_livre',
    'rechercher_livre',
    'emprunter_livre',
    'retourner_livre'
]
```

**Fichier : `bibliotheque/models/livre.py`**
```python
"""Modèle de données pour les livres."""

class Livre:
    """Représente un livre de la bibliothèque."""

    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} par {self.auteur} ({statut})"
```

**Fichier : `bibliotheque/services/gestion_livres.py`**
```python
"""Services de gestion des livres."""

from ..models.livre import Livre

# Base de données simple (liste en mémoire)
_catalogue = []

def ajouter_livre(titre, auteur, isbn):
    """Ajoute un livre au catalogue."""
    livre = Livre(titre, auteur, isbn)
    _catalogue.append(livre)
    return livre

def rechercher_livre(titre):
    """Recherche un livre par son titre."""
    for livre in _catalogue:
        if titre.lower() in livre.titre.lower():
            return livre
    return None

def lister_livres():
    """Retourne tous les livres du catalogue."""
    return _catalogue.copy()
```

**Utilisation :**
```python
from bibliotheque import ajouter_livre, rechercher_livre

# Ajouter des livres
livre1 = ajouter_livre("Python pour débutants", "John Doe", "123-456")
livre2 = ajouter_livre("JavaScript avancé", "Jane Smith", "789-012")

# Rechercher un livre
livre = rechercher_livre("Python")
print(livre)  # Python pour débutants par John Doe (disponible)
```

---

## Résumé

Dans cette section, vous avez appris :

- La différence entre modules et packages
- Comment créer un package avec le fichier `__init__.py`
- L'organisation de packages imbriqués (sous-packages)
- Les imports relatifs et absolus dans les packages
- Le rôle de `__main__.py` pour rendre un package exécutable
- L'utilisation de `__all__` pour contrôler les exports
- Les bonnes pratiques pour structurer des projets Python de différentes tailles
- Comment documenter et organiser un package professionnel

Les packages sont essentiels pour créer des applications Python maintenables et réutilisables. Une bonne structure de package facilite la collaboration, la maintenance et l'évolution de votre code. Dans la section suivante, nous verrons comment gérer les dépendances externes avec pip.

⏭️ [Gestion des dépendances avec pip](/06-modules-et-packages/03-gestion-dependances-pip.md)
