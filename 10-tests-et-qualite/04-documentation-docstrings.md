🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.4 Documentation avec docstrings

## Introduction à la documentation

### Pourquoi documenter son code ?

La documentation est essentielle pour plusieurs raisons :

1. **Pour vous-même** : Vous vous souviendrez de ce que fait votre code dans 6 mois
2. **Pour votre équipe** : Vos collègues comprendront votre code
3. **Pour les utilisateurs** : Ils sauront comment utiliser votre code
4. **Pour la maintenance** : Facilite les modifications et corrections

**Analogie** : Imaginez une recette de cuisine sans instructions. Vous avez les ingrédients, mais comment préparer le plat ? La documentation est comme les instructions d'une recette.

### Qu'est-ce qu'une docstring ?

Une **docstring** (documentation string) est une chaîne de caractères qui documente un module, une classe, une fonction ou une méthode en Python.

```python
def additionner(a, b):
    """Additionne deux nombres et retourne le résultat."""
    return a + b
```

La docstring est la chaîne entre les `"""` juste après la définition de la fonction.

### Comment Python utilise les docstrings

Les docstrings sont accessibles via l'attribut `__doc__` :

```python
def saluer(nom):
    """Salue une personne par son nom."""
    return f"Bonjour {nom} !"

# Accéder à la docstring
print(saluer.__doc__)
# Affiche: Salue une personne par son nom.

# La fonction help() utilise les docstrings
help(saluer)
```

---

## Les bases des docstrings

### Syntaxe de base

Les docstrings utilisent des triples guillemets `"""` :

```python
def ma_fonction():
    """Ceci est une docstring simple sur une ligne."""
    pass

def autre_fonction():
    """
    Ceci est une docstring
    sur plusieurs lignes.
    """
    pass
```

### Convention PEP 257

Python a des conventions officielles pour les docstrings (PEP 257) :

1. **Utilisez des triples guillemets doubles** : `"""`
2. **Une ligne pour les docstrings simples**
3. **Pour les docstrings multi-lignes** :
   - Première ligne : résumé court
   - Ligne vide
   - Description détaillée

```python
def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.

    Cette fonction prend une liste de nombres et retourne
    leur moyenne arithmétique. La liste ne doit pas être vide.
    """
    return sum(nombres) / len(nombres)
```

### Où placer les docstrings ?

Les docstrings peuvent documenter :

1. **Modules** (en haut du fichier)
2. **Classes** (juste après la définition)
3. **Fonctions/Méthodes** (juste après la définition)

```python
"""
Module de calculs mathématiques.

Ce module fournit des fonctions pour effectuer  
des opérations mathématiques de base.  
"""

class Calculatrice:
    """
    Classe pour effectuer des calculs mathématiques.

    Cette classe encapsule des opérations mathématiques
    de base comme l'addition et la soustraction.
    """

    def additionner(self, a, b):
        """Additionne deux nombres."""
        return a + b
```

---

## Styles de docstrings

Il existe plusieurs styles de docstrings. Les trois plus populaires sont :

1. **Google Style** (le plus lisible)
2. **NumPy/SciPy Style** (pour la data science)
3. **reStructuredText (Sphinx)** (le plus formel)

### 1. Google Style (recommandé pour débutants)

Le plus facile à lire et à écrire :

```python
def diviser(dividende, diviseur):
    """Divise deux nombres.

    Cette fonction effectue une division et gère
    le cas de la division par zéro.

    Args:
        dividende (float): Le nombre à diviser.
        diviseur (float): Le nombre par lequel diviser.

    Returns:
        float: Le résultat de la division.

    Raises:
        ValueError: Si le diviseur est zéro.

    Example:
        >>> diviser(10, 2)
        5.0
        >>> diviser(10, 0)
        Traceback (most recent call last):
        ValueError: Division par zéro impossible
    """
    if diviseur == 0:
        raise ValueError("Division par zéro impossible")
    return dividende / diviseur
```

**Sections du Google Style** :
- **Args** : Les paramètres de la fonction
- **Returns** : Ce que retourne la fonction
- **Raises** : Les exceptions qui peuvent être levées
- **Example** : Exemples d'utilisation
- **Note** : Notes importantes
- **Warning** : Avertissements

### 2. NumPy/SciPy Style

Populaire dans la communauté scientifique :

```python
def calculer_statistiques(donnees):
    """
    Calcule des statistiques sur un ensemble de données.

    Cette fonction calcule la moyenne, la médiane
    et l'écart-type d'une liste de nombres.

    Parameters
    ----------
    donnees : list of float
        Liste des valeurs numériques à analyser.
        Ne doit pas être vide.

    Returns
    -------
    dict
        Dictionnaire contenant les statistiques :
        - 'moyenne' : float
            La moyenne arithmétique
        - 'mediane' : float
            La valeur médiane
        - 'ecart_type' : float
            L'écart-type de la population

    Raises
    ------
    ValueError
        Si la liste est vide.

    Examples
    --------
    >>> calculer_statistiques([1, 2, 3, 4, 5])
    {'moyenne': 3.0, 'mediane': 3.0, 'ecart_type': 1.41}

    Notes
    -----
    Cette fonction utilise la formule de l'écart-type
    pour une population complète, pas un échantillon.
    """
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")

    # Implémentation...
    pass
```

### 3. reStructuredText (Sphinx)

Format officiel pour la documentation Sphinx :

```python
def creer_utilisateur(nom, email, age=None):
    """
    Crée un nouvel utilisateur dans le système.

    Cette fonction valide les données et crée un
    objet utilisateur avec les informations fournies.

    :param nom: Le nom complet de l'utilisateur
    :type nom: str
    :param email: L'adresse email de l'utilisateur
    :type email: str
    :param age: L'âge de l'utilisateur (optionnel)
    :type age: int, optional
    :return: L'utilisateur créé
    :rtype: Utilisateur
    :raises ValueError: Si l'email est invalide
    :raises TypeError: Si l'âge n'est pas un entier

    .. note::
       L'email doit être unique dans le système.

    .. warning::
       Cette fonction ne vérifie pas si l'email
       existe déjà dans la base de données.

    **Exemple:**

    .. code-block:: python

       user = creer_utilisateur("Alice", "alice@example.com", 25)
       print(user.nom)  # "Alice"
    """
    # Implémentation...
    pass
```

### Quel style choisir ?

| Style | Avantages | Quand l'utiliser |
|-------|-----------|------------------|
| **Google** | Très lisible, simple | Projets généraux, débutants |
| **NumPy** | Structuré, détaillé | Data science, calcul scientifique |
| **Sphinx** | Standard officiel | Documentation complexe, grands projets |

**Pour débutants** : Commencez avec le **Google Style** !

---

## Documentation des fonctions

### Fonction simple

```python
def est_pair(nombre):
    """Vérifie si un nombre est pair.

    Args:
        nombre (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est pair, False sinon.

    Example:
        >>> est_pair(4)
        True
        >>> est_pair(7)
        False
    """
    return nombre % 2 == 0
```

### Fonction avec plusieurs paramètres

```python
def calculer_prix_total(prix_unitaire, quantite, remise=0):
    """Calcule le prix total d'un achat.

    Cette fonction calcule le prix total en tenant compte
    de la quantité et d'une éventuelle remise.

    Args:
        prix_unitaire (float): Le prix d'un article.
        quantite (int): Le nombre d'articles achetés.
        remise (float, optional): Pourcentage de remise (0-100).
            Par défaut à 0.

    Returns:
        float: Le prix total après remise, arrondi à 2 décimales.

    Raises:
        ValueError: Si la quantité est négative ou si la remise
            est hors de l'intervalle [0, 100].

    Example:
        >>> calculer_prix_total(10.0, 5)
        50.0
        >>> calculer_prix_total(10.0, 5, remise=20)
        40.0

    Note:
        Le prix est arrondi à 2 décimales pour représenter
        correctement les valeurs monétaires.
    """
    if quantite < 0:
        raise ValueError("La quantité ne peut pas être négative")
    if not 0 <= remise <= 100:
        raise ValueError("La remise doit être entre 0 et 100")

    prix_brut = prix_unitaire * quantite
    prix_final = prix_brut * (1 - remise / 100)
    return round(prix_final, 2)
```

### Fonction qui retourne plusieurs valeurs

```python
def analyser_texte(texte):
    """Analyse un texte et retourne des statistiques.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        tuple: Un tuple contenant (nb_mots, nb_caracteres, nb_phrases)
            - nb_mots (int): Le nombre de mots
            - nb_caracteres (int): Le nombre de caractères
            - nb_phrases (int): Le nombre de phrases

    Example:
        >>> analyser_texte("Bonjour. Comment allez-vous?")
        (3, 28, 2)
    """
    nb_mots = len(texte.split())
    nb_caracteres = len(texte)
    nb_phrases = texte.count('.') + texte.count('?') + texte.count('!')

    return nb_mots, nb_caracteres, nb_phrases
```

### Fonction avec type hints

Combiner type hints et docstrings :

```python
def calculer_moyenne(nombres: list[float]) -> float:
    """Calcule la moyenne d'une liste de nombres.

    Args:
        nombres: Liste de nombres à moyenner.

    Returns:
        La moyenne arithmétique des nombres.

    Raises:
        ValueError: Si la liste est vide.

    Example:
        >>> calculer_moyenne([1.0, 2.0, 3.0])
        2.0
    """
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
    return sum(nombres) / len(nombres)

def trouver_utilisateur(user_id: int) -> dict | None:
    """Recherche un utilisateur par son ID.

    Args:
        user_id: L'identifiant de l'utilisateur.

    Returns:
        Le dictionnaire représentant l'utilisateur,
        ou None si non trouvé.

    Example:
        >>> trouver_utilisateur(1)
        {'id': 1, 'nom': 'Alice'}
        >>> trouver_utilisateur(999)
        None
    """
    # Implémentation...
    pass
```

---

## Documentation des classes

### Classe simple

```python
class CompteBancaire:
    """Représente un compte bancaire.

    Cette classe permet de gérer un compte bancaire avec
    des opérations de dépôt et de retrait.

    Attributes:
        titulaire (str): Le nom du titulaire du compte.
        solde (float): Le solde actuel du compte.
        numero (str): Le numéro unique du compte.

    Example:
        >>> compte = CompteBancaire("Alice", "FR123456")
        >>> compte.deposer(1000)
        >>> compte.solde
        1000.0
    """

    def __init__(self, titulaire, numero):
        """Initialise un nouveau compte bancaire.

        Args:
            titulaire (str): Le nom du titulaire.
            numero (str): Le numéro de compte.
        """
        self.titulaire = titulaire
        self.numero = numero
        self.solde = 0.0

    def deposer(self, montant):
        """Dépose de l'argent sur le compte.

        Args:
            montant (float): Le montant à déposer.

        Raises:
            ValueError: Si le montant est négatif ou nul.

        Example:
            >>> compte.deposer(500)
            >>> compte.solde
            500.0
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant

    def retirer(self, montant):
        """Retire de l'argent du compte.

        Args:
            montant (float): Le montant à retirer.

        Raises:
            ValueError: Si le montant est négatif, nul,
                ou supérieur au solde.

        Example:
            >>> compte.deposer(1000)
            >>> compte.retirer(300)
            >>> compte.solde
            700.0
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
```

### Classe avec héritage

```python
class Vehicule:
    """Classe de base pour représenter un véhicule.

    Cette classe définit les propriétés communes à tous
    les véhicules.

    Attributes:
        marque (str): La marque du véhicule.
        modele (str): Le modèle du véhicule.
        annee (int): L'année de fabrication.
    """

    def __init__(self, marque, modele, annee):
        """Initialise un véhicule.

        Args:
            marque (str): La marque.
            modele (str): Le modèle.
            annee (int): L'année.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def description(self):
        """Retourne une description du véhicule.

        Returns:
            str: Description formatée du véhicule.
        """
        return f"{self.marque} {self.modele} ({self.annee})"

class Voiture(Vehicule):
    """Représente une voiture.

    Cette classe hérite de Vehicule et ajoute des
    propriétés spécifiques aux voitures.

    Attributes:
        marque (str): Hérité de Vehicule.
        modele (str): Hérité de Vehicule.
        annee (int): Hérité de Vehicule.
        nb_portes (int): Le nombre de portes.

    Example:
        >>> voiture = Voiture("Renault", "Clio", 2020, 5)
        >>> voiture.description()
        'Renault Clio (2020) - 5 portes'
    """

    def __init__(self, marque, modele, annee, nb_portes):
        """Initialise une voiture.

        Args:
            marque (str): La marque.
            modele (str): Le modèle.
            annee (int): L'année.
            nb_portes (int): Le nombre de portes (3 ou 5).

        Raises:
            ValueError: Si le nombre de portes n'est pas 3 ou 5.
        """
        super().__init__(marque, modele, annee)
        if nb_portes not in [3, 5]:
            raise ValueError("Une voiture a 3 ou 5 portes")
        self.nb_portes = nb_portes

    def description(self):
        """Retourne une description détaillée de la voiture.

        Surcharge la méthode de la classe parente pour inclure
        le nombre de portes.

        Returns:
            str: Description formatée de la voiture.
        """
        desc_base = super().description()
        return f"{desc_base} - {self.nb_portes} portes"
```

---

## Documentation des modules

### En-tête de module

Chaque fichier Python devrait commencer par une docstring de module :

```python
"""
Module de gestion des utilisateurs.

Ce module fournit des fonctions et des classes pour gérer  
les utilisateurs d'une application, incluant la création,  
la modification, la suppression et l'authentification.  

Example:
    Utilisation basique du module::

        from utilisateurs import creer_utilisateur, authentifier

        user = creer_utilisateur("alice@example.com", "motdepasse123")
        if authentifier(user, "motdepasse123"):
            print("Authentification réussie")

Attributes:
    DUREE_SESSION (int): Durée de session en secondes (3600).
    NIVEAU_LOG (str): Niveau de log par défaut ("INFO").

Todo:
    * Ajouter la réinitialisation de mot de passe
    * Implémenter l'authentification à deux facteurs
    * Améliorer la validation des emails
"""

# Constantes du module
DUREE_SESSION = 3600  
NIVEAU_LOG = "INFO"  

# Reste du code...
```

### Module avec sections

Pour les modules plus complexes :

```python
"""
Module de traitement de données.

Ce module fournit des outils pour nettoyer, transformer  
et analyser des données tabulaires.  

Sections:
    - Nettoyage : Fonctions pour nettoyer les données
    - Transformation : Fonctions pour transformer les données
    - Analyse : Fonctions d'analyse statistique
    - Visualisation : Fonctions de génération de graphiques

Constants:
    VALEURS_MANQUANTES (list): Liste des valeurs considérées
        comme manquantes ["", "NA", "N/A", None].
    FORMATS_DATE (list): Formats de date acceptés.

Dependencies:
    - pandas >= 1.3.0
    - numpy >= 1.21.0
    - matplotlib >= 3.4.0

Author:
    Votre Nom (votre.email@example.com)

License:
    MIT License

Version:
    1.0.0

Example:
    >>> import traitement_donnees as td
    >>> donnees = td.charger_csv("data.csv")
    >>> donnees_propres = td.nettoyer(donnees)
    >>> stats = td.analyser(donnees_propres)
"""

# Imports
import pandas as pd  
import numpy as np  

# Constantes
VALEURS_MANQUANTES = ["", "NA", "N/A", None]  
FORMATS_DATE = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]  

# Code du module...
```

---

## Bonnes pratiques de documentation

### 1. Soyez clair et concis

```python
# ❌ Mauvais - trop vague
def traiter(x):
    """Traite x."""
    pass

# ✅ Bon - clair et précis
def valider_email(email):
    """Valide le format d'une adresse email.

    Vérifie que l'email contient un @ et un domaine valide.

    Args:
        email (str): L'adresse email à valider.

    Returns:
        bool: True si l'email est valide, False sinon.
    """
    pass
```

### 2. Documentez les cas limites

```python
def diviser(a, b):
    """Divise a par b.

    Args:
        a (float): Le dividende.
        b (float): Le diviseur.

    Returns:
        float: Le résultat de a / b.

    Raises:
        ValueError: Si b est égal à zéro.

    Note:
        La division de zéro par un nombre non-nul retourne 0.
        La division par un nombre très proche de zéro peut
        produire des résultats très grands ou des erreurs
        d'arrondi.
    """
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b
```

### 3. Incluez des exemples

```python
def formater_prix(prix, devise="EUR"):
    """Formate un prix avec sa devise.

    Args:
        prix (float): Le montant à formater.
        devise (str, optional): Le code de devise ISO 4217.
            Par défaut "EUR".

    Returns:
        str: Le prix formaté avec symbole de devise.

    Example:
        >>> formater_prix(42.50)
        '42.50 €'
        >>> formater_prix(100, "USD")
        '100.00 $'
        >>> formater_prix(15.5, "GBP")
        '15.50 £'
    """
    symboles = {"EUR": "€", "USD": "$", "GBP": "£"}
    symbole = symboles.get(devise, devise)
    return f"{prix:.2f} {symbole}"
```

### 4. Expliquez le "pourquoi", pas seulement le "comment"

```python
def hacher_mot_de_passe(mot_de_passe, sel=None):
    """Hache un mot de passe avec bcrypt.

    Cette fonction utilise bcrypt plutôt que SHA256 car bcrypt
    est spécifiquement conçu pour les mots de passe :
    - Il est intentionnellement lent (résistant au brute force)
    - Il inclut automatiquement un sel unique
    - Il utilise un facteur de coût ajustable

    Args:
        mot_de_passe (str): Le mot de passe en clair.
        sel (bytes, optional): Sel personnalisé. Si None,
            un sel aléatoire est généré.

    Returns:
        str: Le hash du mot de passe (60 caractères).

    Warning:
        Ne stockez jamais les mots de passe en clair !

    Example:
        >>> hash = hacher_mot_de_passe("monMotDePasse123")
        >>> print(len(hash))
        60
    """
    # Implémentation...
    pass
```

### 5. Documentez les effets de bord

```python
def enregistrer_dans_fichier(donnees, fichier="data.json"):
    """Enregistre des données dans un fichier JSON.

    Args:
        donnees (dict): Les données à enregistrer.
        fichier (str, optional): Le chemin du fichier.
            Par défaut "data.json".

    Returns:
        bool: True si l'enregistrement a réussi.

    Side Effects:
        - Crée le fichier s'il n'existe pas
        - Écrase le contenu existant du fichier
        - Crée les répertoires parents si nécessaires

    Raises:
        PermissionError: Si l'écriture est interdite.
        IOError: Si une erreur d'écriture survient.

    Example:
        >>> enregistrer_dans_fichier({"nom": "Alice"})
        True
    """
    # Implémentation...
    pass
```

### 6. Utilisez des sections appropriées

```python
def analyser_image(chemin_image, format_sortie="json"):
    """Analyse une image et extrait des informations.

    Cette fonction utilise un réseau de neurones pré-entraîné
    pour détecter des objets dans une image.

    Args:
        chemin_image (str): Chemin vers le fichier image.
        format_sortie (str, optional): Format de sortie
            ("json" ou "xml"). Par défaut "json".

    Returns:
        dict ou str: Les résultats de l'analyse dans le format
            demandé.

    Raises:
        FileNotFoundError: Si l'image n'existe pas.
        ValueError: Si le format de sortie est invalide.

    Note:
        Cette fonction nécessite TensorFlow >= 2.0
        et un GPU pour des performances optimales.

    Warning:
        Le traitement peut prendre plusieurs secondes
        pour de grandes images (>5MB).

    Example:
        >>> resultats = analyser_image("photo.jpg")
        >>> print(resultats["objets"])
        ['chat', 'chien', 'arbre']

    See Also:
        - analyser_video(): Pour analyser des vidéos
        - analyser_lot(): Pour traiter plusieurs images

    References:
        [1] Paper original du modèle : https://arxiv.org/...
        [2] Documentation TensorFlow : https://tensorflow.org/...
    """
    # Implémentation...
    pass
```

---

## Outils de génération de documentation

### Sphinx : L'outil standard

**Sphinx** est l'outil le plus utilisé pour générer de la documentation HTML à partir de docstrings.

#### Installation

```bash
pip install sphinx  
pip install sphinx-rtd-theme  # Thème "Read the Docs"  
```

#### Initialisation

```bash
# Dans le répertoire de votre projet
mkdir docs  
cd docs  
sphinx-quickstart  
```

Le script posera des questions :
- Nom du projet
- Auteur
- Version
- etc.

#### Configuration (conf.py)

```python
# docs/conf.py
import os  
import sys  

# Ajouter le chemin du code source
sys.path.insert(0, os.path.abspath('..'))

# Extensions Sphinx
extensions = [
    'sphinx.ext.autodoc',      # Documentation automatique
    'sphinx.ext.napoleon',     # Support Google/NumPy style
    'sphinx.ext.viewcode',     # Liens vers le code source
    'sphinx.ext.intersphinx',  # Liens vers autres docs
]

# Configuration
project = 'Mon Projet'  
author = 'Votre Nom'  
version = '1.0'  
release = '1.0.0'  

# Thème
html_theme = 'sphinx_rtd_theme'

# Support du style Google
napoleon_google_docstring = True  
napoleon_numpy_docstring = True  
```

#### Génération de la documentation

```bash
# Générer les fichiers .rst automatiquement
sphinx-apidoc -o docs/ mon_package/

# Générer la documentation HTML
cd docs  
make html  

# Ouvrir la documentation
open _build/html/index.html
```

### pdoc : Alternative plus simple

**pdoc** génère de la documentation automatiquement, sans configuration :

```bash
# Installation
pip install pdoc3

# Générer la documentation
pdoc --html --output-dir docs mon_package

# Serveur local pour développement
pdoc --http localhost:8080 mon_package
```

### pydoc : Outil intégré

Python inclut `pydoc` par défaut :

```bash
# Afficher la doc dans le terminal
python -m pydoc mon_module

# Lancer un serveur web
python -m pydoc -b  # Ouvre automatiquement le navigateur
```

---

## Documentation interactive avec help()

### Dans le REPL Python

```python
>>> def ma_fonction(x, y):
...     """Additionne x et y."""
...     return x + y

>>> help(ma_fonction)
Help on function ma_fonction in module __main__:

ma_fonction(x, y)
    Additionne x et y.

>>> # Aussi disponible via ?
>>> ma_fonction?  # Dans IPython/Jupyter
```

### Accès programmatique

```python
# Accéder à la docstring
print(ma_fonction.__doc__)

# Obtenir la signature
import inspect  
print(inspect.signature(ma_fonction))  
```

---

## Cas pratique : API de gestion de tâches

Voici un exemple complet d'API bien documentée :

```python
"""
API de gestion de tâches.

Ce module fournit une API simple pour gérer une liste de tâches  
avec des fonctionnalités de création, lecture, mise à jour et  
suppression (CRUD).  

Example:
    >>> from taches import GestionnaireTaches, Tache
    >>> gestionnaire = GestionnaireTaches()
    >>> tache = gestionnaire.creer_tache("Acheter du pain")
    >>> gestionnaire.lister_taches()
    [Tache(id=1, titre='Acheter du pain', terminee=False)]

Attributes:
    VERSION (str): Version de l'API ("1.0.0").
    PRIORITE_HAUTE (int): Constante pour priorité haute (1).
    PRIORITE_NORMALE (int): Constante pour priorité normale (2).
    PRIORITE_BASSE (int): Constante pour priorité basse (3).

Todo:
    * Ajouter les dates d'échéance
    * Implémenter les catégories
    * Ajouter un système de tags
"""

from datetime import datetime
# Constantes du module
VERSION = "1.0.0"  
PRIORITE_HAUTE = 1  
PRIORITE_NORMALE = 2  
PRIORITE_BASSE = 3  


class Tache:
    """Représente une tâche individuelle.

    Une tâche contient un titre, un état (terminée ou non),
    une priorité et une date de création.

    Attributes:
        id (int): Identifiant unique de la tâche.
        titre (str): Le titre de la tâche.
        terminee (bool): True si la tâche est terminée.
        priorite (int): Niveau de priorité (1=haute, 2=normale, 3=basse).
        date_creation (datetime): Date et heure de création.

    Example:
        >>> tache = Tache(1, "Faire les courses")
        >>> tache.marquer_terminee()
        >>> tache.terminee
        True
    """

    def __init__(self, id: int, titre: str, priorite: int = PRIORITE_NORMALE):
        """Initialise une nouvelle tâche.

        Args:
            id: L'identifiant unique de la tâche.
            titre: Le titre de la tâche.
            priorite: Le niveau de priorité (1, 2, ou 3).
                Par défaut PRIORITE_NORMALE.

        Raises:
            ValueError: Si le titre est vide ou si la priorité
                n'est pas valide.
        """
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if priorite not in [PRIORITE_HAUTE, PRIORITE_NORMALE, PRIORITE_BASSE]:
            raise ValueError("Priorité invalide")

        self.id = id
        self.titre = titre
        self.terminee = False
        self.priorite = priorite
        self.date_creation = datetime.now()

    def marquer_terminee(self) -> None:
        """Marque la tâche comme terminée.

        Cette méthode est idempotente : l'appeler plusieurs fois
        n'a pas d'effet après le premier appel.

        Example:
            >>> tache = Tache(1, "Lire un livre")
            >>> tache.marquer_terminee()
            >>> tache.terminee
            True
        """
        self.terminee = True

    def marquer_non_terminee(self) -> None:
        """Marque la tâche comme non terminée.

        Permet de réouvrir une tâche précédemment terminée.

        Example:
            >>> tache = Tache(1, "Appeler le médecin")
            >>> tache.marquer_terminee()
            >>> tache.marquer_non_terminee()
            >>> tache.terminee
            False
        """
        self.terminee = False

    def changer_priorite(self, nouvelle_priorite: int) -> None:
        """Change la priorité de la tâche.

        Args:
            nouvelle_priorite: La nouvelle priorité (1, 2, ou 3).

        Raises:
            ValueError: Si la priorité n'est pas valide.

        Example:
            >>> tache = Tache(1, "Tâche urgente")
            >>> tache.changer_priorite(PRIORITE_HAUTE)
            >>> tache.priorite
            1
        """
        if nouvelle_priorite not in [PRIORITE_HAUTE, PRIORITE_NORMALE, PRIORITE_BASSE]:
            raise ValueError("Priorité invalide")
        self.priorite = nouvelle_priorite

    def __repr__(self) -> str:
        """Retourne une représentation textuelle de la tâche.

        Returns:
            Chaîne représentant la tâche au format :
            "Tache(id=X, titre='...', terminee=True/False)"
        """
        return f"Tache(id={self.id}, titre='{self.titre}', terminee={self.terminee})"


class GestionnaireTaches:
    """Gère une collection de tâches.

    Cette classe permet de créer, lister, modifier et supprimer
    des tâches. Elle maintient un compteur pour assigner des ID
    uniques à chaque tâche.

    Attributes:
        taches (dict): Dictionnaire des tâches indexées par ID.

    Example:
        >>> gestionnaire = GestionnaireTaches()
        >>> tache1 = gestionnaire.creer_tache("Tâche 1")
        >>> tache2 = gestionnaire.creer_tache("Tâche 2", PRIORITE_HAUTE)
        >>> len(gestionnaire.lister_taches())
        2
    """

    def __init__(self):
        """Initialise un nouveau gestionnaire de tâches.

        Crée un gestionnaire vide avec un compteur d'ID initialisé à 1.
        """
        self.taches: dict[int, Tache] = {}
        self._prochain_id = 1

    def creer_tache(self, titre: str, priorite: int = PRIORITE_NORMALE) -> Tache:
        """Crée une nouvelle tâche.

        Args:
            titre: Le titre de la tâche.
            priorite: Le niveau de priorité. Par défaut PRIORITE_NORMALE.

        Returns:
            La tâche créée.

        Raises:
            ValueError: Si le titre est vide ou la priorité invalide.

        Example:
            >>> gestionnaire = GestionnaireTaches()
            >>> tache = gestionnaire.creer_tache("Faire du sport")
            >>> tache.id
            1
        """
        tache = Tache(self._prochain_id, titre, priorite)
        self.taches[self._prochain_id] = tache
        self._prochain_id += 1
        return tache

    def obtenir_tache(self, tache_id: int) -> Tache | None:
        """Obtient une tâche par son ID.

        Args:
            tache_id: L'identifiant de la tâche.

        Returns:
            La tâche correspondante, ou None si non trouvée.

        Example:
            >>> gestionnaire = GestionnaireTaches()
            >>> tache = gestionnaire.creer_tache("Test")
            >>> gestionnaire.obtenir_tache(tache.id) is tache
            True
            >>> gestionnaire.obtenir_tache(999) is None
            True
        """
        return self.taches.get(tache_id)

    def supprimer_tache(self, tache_id: int) -> bool:
        """Supprime une tâche.

        Args:
            tache_id: L'identifiant de la tâche à supprimer.

        Returns:
            True si la tâche a été supprimée, False si elle
            n'existait pas.

        Example:
            >>> gestionnaire = GestionnaireTaches()
            >>> tache = gestionnaire.creer_tache("À supprimer")
            >>> gestionnaire.supprimer_tache(tache.id)
            True
            >>> gestionnaire.supprimer_tache(999)
            False
        """
        if tache_id in self.taches:
            del self.taches[tache_id]
            return True
        return False

    def lister_taches(self, seulement_non_terminees: bool = False) -> list[Tache]:
        """Liste toutes les tâches.

        Args:
            seulement_non_terminees: Si True, ne retourne que
                les tâches non terminées. Par défaut False.

        Returns:
            Liste des tâches, triées par priorité puis par date.

        Example:
            >>> gestionnaire = GestionnaireTaches()
            >>> t1 = gestionnaire.creer_tache("Tâche 1")
            >>> t2 = gestionnaire.creer_tache("Tâche 2")
            >>> t1.marquer_terminee()
            >>> len(gestionnaire.lister_taches())
            2
            >>> len(gestionnaire.lister_taches(seulement_non_terminees=True))
            1
        """
        taches = list(self.taches.values())

        if seulement_non_terminees:
            taches = [t for t in taches if not t.terminee]

        # Trier par priorité puis par date
        taches.sort(key=lambda t: (t.priorite, t.date_creation))

        return taches

    def compter_taches(self, seulement_non_terminees: bool = False) -> int:
        """Compte le nombre de tâches.

        Args:
            seulement_non_terminees: Si True, compte seulement
                les tâches non terminées. Par défaut False.

        Returns:
            Le nombre de tâches.

        Example:
            >>> gestionnaire = GestionnaireTaches()
            >>> gestionnaire.creer_tache("Tâche 1")
            >>> gestionnaire.creer_tache("Tâche 2")
            >>> gestionnaire.compter_taches()
            2
        """
        return len(self.lister_taches(seulement_non_terminees))
```

---

## Documentation pour différents publics

### Documentation pour les développeurs

Détaillée, technique, avec références au code :

```python
def optimiser_requete_sql(requete, parametres):
    """Optimise une requête SQL avant exécution.

    Cette fonction analyse la requête et applique plusieurs
    optimisations :
    1. Ajout d'index hints si pertinent
    2. Réécriture des sous-requêtes en JOINs
    3. Simplification des WHERE redondants

    Args:
        requete (str): La requête SQL à optimiser.
        parametres (dict): Les paramètres de la requête.

    Returns:
        tuple: (requete_optimisee, nouveaux_parametres, stats)

    Implementation Notes:
        - Utilise l'AST SQL via sqlparse
        - Cache les plans d'exécution fréquents
        - Thread-safe via verrous locaux

    Performance:
        - O(n) où n est la longueur de la requête
        - ~50ms pour requêtes typiques (<1KB)
        - Cache hit ratio : ~80% en production
    """
    pass
```

### Documentation pour les utilisateurs finaux

Simple, orientée cas d'usage, sans détails techniques :

```python
def envoyer_email(destinataire, sujet, message):
    """Envoie un email.

    Permet d'envoyer facilement un email à une personne.

    Args:
        destinataire (str): L'adresse email du destinataire.
            Exemple : "alice@example.com"
        sujet (str): Le sujet de l'email.
        message (str): Le contenu du message.

    Returns:
        bool: True si l'email a été envoyé avec succès.

    Example:
        Envoyer un email de bienvenue::

            succes = envoyer_email(
                "nouvel.utilisateur@example.com",
                "Bienvenue !",
                "Merci de vous être inscrit."
            )

            if succes:
                print("Email envoyé !")

    Note:
        L'email peut prendre quelques minutes à arriver.
        Vérifiez vos spams si vous ne le recevez pas.
    """
    pass
```

---

## Outils de vérification de documentation

### pydocstyle

Vérifie que les docstrings suivent les conventions :

```bash
# Installation
pip install pydocstyle

# Vérification
pydocstyle mon_module.py
```

Configuration `.pydocstyle` :

```ini
[pydocstyle]
convention = google  
match = .*\.py  
match_dir = ^(?!tests|docs|\.)[^.].*  
```

### darglint

Vérifie la cohérence entre docstrings et code :

```bash
# Installation
pip install darglint

# Vérification
darglint -v 2 mon_module.py
```

Exemple d'erreur détectée :

```python
def calculer(a, b, c):
    """Calcule quelque chose.

    Args:
        a (int): Premier nombre.
        b (int): Deuxième nombre.

    Returns:
        int: Résultat.
    """
    return a + b + c

# darglint détectera que le paramètre 'c' n'est pas documenté
```

### interrogate

Mesure la couverture de documentation :

```bash
# Installation
pip install interrogate

# Vérification
interrogate -v mon_package/

# Avec badge
interrogate --generate-badge docs/
```

---

## Résumé

### Points clés à retenir

1. **Les docstrings documentent** modules, classes, fonctions et méthodes
2. **Format triple guillemet** : `"""` pour les docstrings
3. **Trois styles principaux** : Google (simple), NumPy (scientifique), Sphinx (formel)
4. **Sections importantes** : Args, Returns, Raises, Example
5. **Sphinx génère** de la documentation HTML automatiquement
6. **help()** accède aux docstrings dans le REPL
7. **Bonnes pratiques** : Être clair, donner des exemples, documenter les cas limites

### Template de docstring Google Style

```python
def ma_fonction(param1, param2, param3=None):
    """Résumé court sur une ligne.

    Description détaillée sur plusieurs lignes si nécessaire.
    Expliquez ce que fait la fonction et pourquoi.

    Args:
        param1 (type): Description du paramètre 1.
        param2 (type): Description du paramètre 2.
        param3 (type, optional): Description du paramètre optionnel.
            Par défaut None.

    Returns:
        type: Description de ce qui est retourné.

    Raises:
        ExceptionType: Quand cette exception est levée.
        AutreException: Autre cas d'erreur.

    Example:
        >>> ma_fonction(1, 2)
        3
        >>> ma_fonction(1, 2, param3=10)
        13

    Note:
        Notes importantes pour les utilisateurs.

    Warning:
        Avertissements importants.
    """
    pass
```

### Checklist pour une bonne documentation

- [ ] Chaque module a une docstring d'en-tête
- [ ] Chaque classe publique est documentée
- [ ] Chaque fonction publique est documentée
- [ ] Les paramètres sont documentés avec leurs types
- [ ] Les valeurs de retour sont documentées
- [ ] Les exceptions levées sont documentées
- [ ] Des exemples sont fournis
- [ ] Les cas limites sont mentionnés
- [ ] Le style est cohérent dans tout le projet
- [ ] La documentation est à jour avec le code

### Commandes utiles

```bash
# Générer documentation avec Sphinx
sphinx-quickstart  
sphinx-apidoc -o docs/ mon_package/  
cd docs && make html  

# Alternative simple avec pdoc
pdoc --html --output-dir docs mon_package

# Vérifier les docstrings
pydocstyle mon_package/  
darglint mon_package/*.py  
interrogate mon_package/  

# Voir la documentation dans le terminal
python -m pydoc mon_module
```

### Ressources complémentaires

- PEP 257 (Docstring Conventions) : https://peps.python.org/pep-0257/
- Google Style Guide : https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
- NumPy Style Guide : https://numpydoc.readthedocs.io/
- Sphinx Documentation : https://www.sphinx-doc.org/
- Real Python Documenting : https://realpython.com/documenting-python-code/

**Une bonne documentation est un investissement qui facilite la maintenance et la collaboration !** 📚

⏭️ [PEP 8 et outils de linting](/10-tests-et-qualite/05-pep8-et-linting.md)
