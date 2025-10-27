🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7. Bibliothèques standard essentielles

## Introduction

Félicitations d'être arrivé jusqu'ici dans votre apprentissage de Python ! Vous maîtrisez maintenant les fondamentaux du langage : les variables, les structures de contrôle, les fonctions, la programmation orientée objet, et bien plus encore. Il est temps de découvrir l'un des plus grands atouts de Python : **sa bibliothèque standard**.

---

## Qu'est-ce que la bibliothèque standard ?

La **bibliothèque standard Python** (Python Standard Library) est un ensemble de modules qui sont inclus avec Python par défaut. Vous n'avez rien à installer : dès que vous installez Python, vous avez accès à ces modules puissants qui couvrent une vaste gamme de fonctionnalités.

### Pourquoi est-ce important ?

La philosophie de Python est souvent résumée par l'expression :

> **"Batteries included"** (Piles incluses)

Cela signifie que Python vient avec tout ce dont vous avez besoin pour la plupart des tâches courantes de programmation, sans avoir à installer de bibliothèques externes.

### Avantages de la bibliothèque standard

1. **Disponibilité garantie** : Les modules sont présents sur toute installation Python
2. **Stabilité** : Code testé et maintenu par la communauté Python
3. **Performance** : Souvent implémentés en C pour une exécution rapide
4. **Documentation complète** : Toutes les fonctionnalités sont bien documentées
5. **Compatibilité** : Fonctionne sur toutes les plateformes (Windows, Linux, macOS)

---

## Comment utiliser un module de la bibliothèque standard ?

C'est très simple ! Il suffit de l'importer avec le mot-clé `import` :

```python
# Importer un module complet
import math

resultat = math.sqrt(16)  # Utiliser une fonction du module
print(resultat)  # 4.0

# Importer des fonctions spécifiques
from datetime import datetime

maintenant = datetime.now()
print(maintenant)

# Importer avec un alias (raccourci)
import statistics as stats

moyenne = stats.mean([1, 2, 3, 4, 5])
print(moyenne)  # 3
```

### Bonnes pratiques d'import

```python
# ✅ Bon : import explicite
import os
import sys
from datetime import datetime, timedelta

# ✅ Bon : alias courants et reconnus
import statistics as stats

# ❌ À éviter : import wildcard (importe tout)
from math import *  # Peut causer des conflits de noms

# ❌ À éviter : alias non standards
import os as o  # Pas clair pour les autres développeurs
```

---

## Vue d'ensemble des modules que nous allons étudier

Dans cette section, nous allons explorer 6 groupes de modules essentiels qui vous seront utiles dans presque tous vos projets Python.

### 7.1 os, sys, subprocess

**Thème** : Interaction avec le système d'exploitation

Ces modules vous permettent d'interagir avec le système d'exploitation, de manipuler des fichiers et des dossiers, et d'exécuter des commandes externes.

**Exemples d'utilisation** :
- Créer, déplacer ou supprimer des fichiers et dossiers
- Naviguer dans l'arborescence de fichiers
- Obtenir des informations sur le système
- Exécuter des programmes externes depuis Python
- Gérer les variables d'environnement

```python
import os

# Obtenir le répertoire actuel
print(os.getcwd())

# Lister les fichiers
print(os.listdir('.'))
```

### 7.2 datetime et time

**Thème** : Manipulation des dates et du temps

Ces modules permettent de travailler avec des dates, des heures, des durées et des fuseaux horaires.

**Exemples d'utilisation** :
- Obtenir la date et l'heure actuelles
- Calculer des différences entre dates
- Formater des dates pour l'affichage
- Mesurer le temps d'exécution d'un code
- Créer des rappels et des planifications

```python
from datetime import datetime

maintenant = datetime.now()
print(maintenant.strftime("%d/%m/%Y %H:%M:%S"))
```

### 7.3 math, random, statistics

**Thème** : Calculs mathématiques et aléatoire

Ces modules offrent des fonctions mathématiques avancées, la génération de nombres aléatoires et des calculs statistiques.

**Exemples d'utilisation** :
- Calculs mathématiques (racines, logarithmes, trigonométrie)
- Génération de nombres aléatoires pour des jeux ou simulations
- Calculs statistiques (moyenne, médiane, écart-type)
- Combinaisons et permutations

```python
import math
import random

# Calcul mathématique
print(math.sqrt(25))  # 5.0

# Nombre aléatoire
print(random.randint(1, 100))

# Statistiques
import statistics
print(statistics.mean([1, 2, 3, 4, 5]))  # 3
```

### 7.4 itertools et functools

**Thème** : Outils pour itération et programmation fonctionnelle

Ces modules fournissent des outils puissants pour créer des itérateurs efficaces et travailler avec des fonctions d'ordre supérieur.

**Exemples d'utilisation** :
- Créer des combinaisons et permutations
- Itérer efficacement sur de grandes quantités de données
- Créer des fonctions spécialisées (programmation fonctionnelle)
- Optimiser les performances avec la mémorisation

```python
import itertools

# Générer toutes les combinaisons
for combo in itertools.combinations(['A', 'B', 'C'], 2):
    print(combo)
# ('A', 'B'), ('A', 'C'), ('B', 'C')
```

### 7.5 logging et configuration

**Thème** : Journalisation et traçage

Le module `logging` permet d'enregistrer des messages sur l'exécution du programme, ce qui est essentiel pour le débogage et la maintenance.

**Exemples d'utilisation** :
- Enregistrer des événements et des erreurs
- Créer des logs à différents niveaux (DEBUG, INFO, WARNING, ERROR)
- Écrire des logs dans des fichiers
- Tracer l'exécution d'une application en production

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("L'application a démarré")
logging.error("Une erreur s'est produite")
```

### 7.6 typing - Annotations avancées

**Thème** : Annotations de type

Le module `typing` permet d'ajouter des annotations de type pour rendre le code plus clair et détecter des erreurs avant l'exécution.

**Exemples d'utilisation** :
- Documenter les types attendus dans les fonctions
- Améliorer la détection d'erreurs avec des outils comme mypy
- Rendre le code plus lisible et maintenable
- Bénéficier d'une meilleure autocomplétion dans les IDE

```python
from typing import List, Dict

def calculer_moyenne(notes: List[float]) -> float:
    """Calcule la moyenne d'une liste de notes"""
    return sum(notes) / len(notes)
```

---

## La bibliothèque standard est bien plus vaste

Les modules que nous allons étudier ne représentent qu'une petite partie de la bibliothèque standard Python. Voici d'autres modules importants que vous découvrirez au fil de votre apprentissage :

### Manipulation de données
- **json** : Travailler avec des données JSON
- **csv** : Lire et écrire des fichiers CSV
- **xml** : Traiter des documents XML
- **sqlite3** : Base de données SQLite
- **pickle** : Sérialisation d'objets Python

### Réseau et Internet
- **urllib** : Requêtes HTTP
- **http** : Serveurs et clients HTTP
- **email** : Gestion d'emails
- **smtplib** : Envoi d'emails

### Compression et archivage
- **zipfile** : Travailler avec des archives ZIP
- **tarfile** : Archives TAR
- **gzip** : Compression GZIP

### Système et processus
- **threading** : Multithreading
- **multiprocessing** : Multiprocessing
- **asyncio** : Programmation asynchrone
- **subprocess** : Exécuter des processus

### Utilitaires
- **re** : Expressions régulières
- **collections** : Structures de données spécialisées
- **pathlib** : Manipulation moderne de chemins
- **argparse** : Parser d'arguments en ligne de commande

---

## Comment explorer la bibliothèque standard ?

### 1. Documentation officielle

La documentation officielle de Python est votre meilleure ressource :
- **En ligne** : https://docs.python.org/fr/3/library/
- **Complète** : Tous les modules sont documentés avec des exemples
- **Traduite** : Disponible en français

### 2. Fonction help() dans l'interpréteur

```python
import math

# Obtenir l'aide sur un module
help(math)

# Obtenir l'aide sur une fonction spécifique
help(math.sqrt)

# Lister les fonctions d'un module
print(dir(math))
```

### 3. Docstrings

Chaque module, classe et fonction Python a une documentation intégrée :

```python
import datetime

# Afficher la docstring
print(datetime.datetime.now.__doc__)

# Accéder à la docstring avec __doc__
print(datetime.__doc__)
```

### 4. Exploration interactive

```python
import math

# Lister tous les attributs et fonctions
attributs = dir(math)
print(attributs)

# Filtrer pour voir seulement les fonctions publiques
fonctions_publiques = [attr for attr in dir(math) if not attr.startswith('_')]
print(fonctions_publiques)
```

---

## Conseils pour bien apprendre

### 1. Pratiquez régulièrement

La meilleure façon d'apprendre ces modules est de les utiliser dans vos propres projets. N'hésitez pas à :
- Créer de petits programmes pour tester chaque module
- Réutiliser les exemples fournis dans ce tutoriel
- Modifier les exemples pour voir ce qui se passe

### 2. Ne mémorisez pas tout

Il n'est **pas nécessaire** de mémoriser toutes les fonctions de chaque module. L'important est de :
- Savoir **qu'un module existe** pour une tâche donnée
- Savoir **où trouver la documentation**
- Comprendre **les concepts généraux**

Avec la pratique, vous mémoriserez naturellement les fonctions que vous utilisez le plus souvent.

### 3. Lisez le code des autres

Examinez comment d'autres développeurs utilisent ces modules dans des projets open source. C'est une excellente façon d'apprendre les bonnes pratiques.

### 4. Créez vos propres projets

Appliquez ce que vous apprenez dans des projets concrets :
- Un gestionnaire de fichiers
- Un journal de bord automatique
- Un calculateur scientifique
- Un générateur de rapports
- Un système de planification de tâches

### 5. Combinez plusieurs modules

Les modules sont encore plus puissants quand on les combine :

```python
import os
import datetime
import logging

# Créer un système de sauvegarde automatique
logging.basicConfig(level=logging.INFO)

def sauvegarder_fichier(source):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dossier_backup = "backups"

    # Créer le dossier s'il n'existe pas
    if not os.path.exists(dossier_backup):
        os.makedirs(dossier_backup)
        logging.info(f"Dossier {dossier_backup} créé")

    # Copier le fichier avec timestamp
    destination = os.path.join(dossier_backup, f"backup_{timestamp}_{source}")
    logging.info(f"Sauvegarde de {source} vers {destination}")
    # ... code de copie ...
```

---

## Organisation de cette section

Chaque module sera présenté avec :

1. **Introduction** : À quoi sert le module ?
2. **Concepts de base** : Les notions essentielles à comprendre
3. **Fonctions principales** : Les fonctions les plus utiles avec exemples
4. **Exemples pratiques** : Des cas d'usage réels et complets
5. **Bonnes pratiques** : Comment utiliser le module efficacement
6. **Résumé** : Un récapitulatif rapide pour réviser

---

## Avant de commencer

### Vérifiez votre installation Python

Tous les modules que nous allons étudier font partie de la bibliothèque standard. Pour vérifier que Python est correctement installé :

```python
# Testez ceci dans votre interpréteur Python
import sys
print(f"Version Python : {sys.version}")
print(f"Chemin Python : {sys.executable}")

# Vérifier qu'un module est disponible
try:
    import math, datetime, random, statistics, itertools, functools, logging, typing
    print("✅ Tous les modules sont disponibles !")
except ImportError as e:
    print(f"❌ Erreur : {e}")
```

### Configurez votre environnement de développement

Pour tirer le meilleur parti de cette section, assurez-vous d'avoir :

1. **Un éditeur de code** ou un IDE (VS Code, PyCharm, etc.)
2. **Python 3.8 ou supérieur** installé
3. **Un terminal** pour exécuter vos scripts

---

## Structure recommandée pour vos fichiers de test

Pendant votre apprentissage, organisez vos fichiers de test de cette manière :

```
mon-apprentissage-python/
│
├── section7-bibliotheque-standard/
│   ├── 7.1-os-sys-subprocess/
│   │   ├── test_os.py
│   │   ├── test_sys.py
│   │   └── test_subprocess.py
│   │
│   ├── 7.2-datetime-time/
│   │   ├── test_datetime.py
│   │   └── test_time.py
│   │
│   ├── 7.3-math-random-statistics/
│   │   ├── test_math.py
│   │   ├── test_random.py
│   │   └── test_statistics.py
│   │
│   ├── 7.4-itertools-functools/
│   │   ├── test_itertools.py
│   │   └── test_functools.py
│   │
│   ├── 7.5-logging/
│   │   ├── test_logging.py
│   │   └── logs/
│   │
│   └── 7.6-typing/
│       └── test_typing.py
│
└── projets-pratiques/
    ├── gestionnaire_fichiers.py
    ├── calculatrice_avancee.py
    └── journal_automatique.py
```

---

## Créez votre "cheat sheet" personnelle

Au fur et à mesure de votre apprentissage, créez un fichier de référence rapide avec les fonctions que vous utilisez le plus :

```python
"""
MON AIDE-MÉMOIRE - BIBLIOTHÈQUE STANDARD PYTHON
================================================

OS & SYSTÈME
------------
import os
os.getcwd()                    # Répertoire actuel
os.listdir('.')                # Liste des fichiers
os.path.join('dossier', 'fichier.txt')  # Joindre chemins

DATES & TEMPS
-------------
from datetime import datetime
datetime.now()                 # Date/heure actuelle
datetime.strftime(fmt)         # Formater date

MATHÉMATIQUES
-------------
import math
math.sqrt(x)                   # Racine carrée
math.pi                        # Pi (3.14159...)

import random
random.randint(a, b)           # Entier aléatoire

LOGGING
-------
import logging
logging.info("message")        # Log d'information
logging.error("erreur")        # Log d'erreur

TYPING
------
from typing import List, Dict
def fonction(param: List[int]) -> int:
    ...

... Ajoutez vos propres notes ici ...
"""
```

---

## À retenir

1. **La bibliothèque standard est votre alliée** : Elle vous évite de réinventer la roue
2. **"Batteries included"** : Python vient avec tout ce dont vous avez besoin pour débuter
3. **Documentation = votre amie** : Consultez-la régulièrement (docs.python.org)
4. **Pratiquez, pratiquez, pratiquez** : La seule façon de vraiment apprendre
5. **Ne mémorisez pas tout** : Sachez où chercher l'information
6. **Combinez les modules** : C'est là que la vraie puissance apparaît

---

## Prêt à commencer ?

Vous avez maintenant une vue d'ensemble de ce qui vous attend dans cette section. Ne soyez pas intimidé par la quantité d'information : nous allons progresser étape par étape, avec de nombreux exemples pratiques.

La maîtrise de la bibliothèque standard Python est ce qui fait la différence entre un débutant et un développeur Python compétent. Ces modules vous accompagneront tout au long de votre carrière de développeur.

**Commençons notre voyage à travers la bibliothèque standard Python !**

---

## Ressources complémentaires

### Documentation officielle
- **Bibliothèque standard** : https://docs.python.org/fr/3/library/
- **Tutoriel Python** : https://docs.python.org/fr/3/tutorial/
- **Index des modules** : https://docs.python.org/fr/3/py-modindex.html

### Outils recommandés
- **IPython** : Interpréteur interactif amélioré
- **Jupyter Notebook** : Pour expérimenter avec du code
- **VS Code** : Éditeur avec excellent support Python
- **PyCharm** : IDE complet pour Python

### Livres de référence
- "Python Module of the Week" (PyMOTW) - Blog de Doug Hellmann
- Documentation officielle Python
- "Fluent Python" - Luciano Ramalho

---

Maintenant, passons à la première partie : **7.1 os, sys, subprocess** !

⏭️ [os, sys, subprocess](/07-bibliotheques-standard/01-os-sys-subprocess.md)
