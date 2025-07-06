🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.4 : Documentation avec docstrings

## Introduction

Imaginez que vous trouvez une boîte mystérieuse dans votre grenier. Sans étiquette, sans notice, impossible de savoir ce qu'elle contient ou à quoi elle sert ! Votre code sans documentation, c'est exactement pareil : même si vous l'avez écrit, dans quelques mois vous ne vous souviendrez plus de ce qu'il fait ni comment l'utiliser.

Les **docstrings** (chaînes de documentation) sont comme des étiquettes intelligentes pour votre code. Elles expliquent ce que fait chaque fonction, comment l'utiliser, et quoi attendre en retour. Elles transforment votre code en une bibliothèque bien organisée où tout est clairement étiqueté !

## Qu'est-ce qu'une docstring ?

### Définition simple
Une docstring est une chaîne de caractères qui apparaît en première position dans une fonction, classe ou module pour expliquer ce qu'elle fait.

### Exemple basique
```python
def additionner(a, b):
    """
    Additionne deux nombres et retourne le résultat.

    Cette fonction prend deux nombres en paramètres
    et retourne leur somme.
    """
    return a + b

# La docstring est accessible avec help() ou __doc__
print(additionner.__doc__)
help(additionner)
```

### Pourquoi les docstrings sont importantes

#### 1. Pour vous dans 6 mois
```python
# ❌ Sans docstring - mystérieux
def calcul_tva(p, t):
    return p * (1 + t)

# ✅ Avec docstring - clair !
def calcul_tva(prix_ht, taux_tva):
    """
    Calcule le prix TTC à partir du prix HT et du taux de TVA.

    Args:
        prix_ht (float): Prix hors taxes en euros
        taux_tva (float): Taux de TVA (ex: 0.20 pour 20%)

    Returns:
        float: Prix toutes taxes comprises

    Example:
        >>> calcul_tva(100, 0.20)
        120.0
    """
    return prix_ht * (1 + taux_tva)
```

#### 2. Pour vos collègues
```python
class GestionnaireUtilisateurs:
    """
    Gestionnaire pour les opérations sur les utilisateurs.

    Cette classe fournit des méthodes pour créer, modifier,
    supprimer et rechercher des utilisateurs dans le système.

    Attributes:
        users (dict): Dictionnaire stockant les utilisateurs
        next_id (int): Prochain ID disponible pour un nouvel utilisateur

    Example:
        >>> gestionnaire = GestionnaireUtilisateurs()
        >>> user_id = gestionnaire.ajouter_utilisateur("Alice", "alice@test.com")
        >>> utilisateur = gestionnaire.obtenir_utilisateur(user_id)
    """

    def __init__(self):
        """Initialise un gestionnaire vide."""
        self.users = {}
        self.next_id = 1
```

#### 3. Pour les outils automatiques
```python
def diviser(a, b):
    """
    Divise le premier nombre par le second.

    Args:
        a (float): Le dividende
        b (float): Le diviseur

    Returns:
        float: Le résultat de la division

    Raises:
        ZeroDivisionError: Si b est égal à zéro
        TypeError: Si a ou b ne sont pas des nombres

    Example:
        >>> diviser(10, 2)
        5.0
        >>> diviser(7, 2)
        3.5
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return a / b

# Les IDE peuvent utiliser cette documentation pour l'autocomplétion !
```

## Formats de docstrings

### 1. Format Google (recommandé pour les débutants)

```python
def rechercher_utilisateur(nom, age_min=None, age_max=None, actif=True):
    """
    Recherche des utilisateurs selon des critères.

    Cette fonction permet de chercher des utilisateurs dans la base
    en appliquant différents filtres optionnels.

    Args:
        nom (str): Nom ou partie du nom à rechercher
        age_min (int, optional): Âge minimum. Défaut à None.
        age_max (int, optional): Âge maximum. Défaut à None.
        actif (bool, optional): Rechercher seulement les utilisateurs actifs.
            Défaut à True.

    Returns:
        list[dict]: Liste des utilisateurs trouvés. Chaque utilisateur
            est représenté par un dictionnaire avec les clés:
            - 'id': Identifiant unique
            - 'nom': Nom complet
            - 'age': Âge en années
            - 'email': Adresse email

    Raises:
        ValueError: Si nom est vide ou si age_min > age_max
        DatabaseError: Si la connexion à la base échoue

    Example:
        >>> utilisateurs = rechercher_utilisateur("Alice")
        >>> print(len(utilisateurs))
        2

        >>> seniors = rechercher_utilisateur("", age_min=65)
        >>> for user in seniors:
        ...     print(user['nom'])
        Robert Dupont
        Marie Martin

    Note:
        La recherche est insensible à la casse pour le nom.
        Les utilisateurs supprimés ne sont jamais retournés.
    """
    if not nom.strip():
        raise ValueError("Le nom ne peut pas être vide")

    if age_min and age_max and age_min > age_max:
        raise ValueError("age_min ne peut pas être supérieur à age_max")

    # Implémentation de la recherche...
    return []
```

### 2. Format NumPy (pour la documentation scientifique)

```python
def calculer_statistiques(donnees, inclure_ecart_type=True):
    """
    Calcule des statistiques descriptives sur un ensemble de données.

    Cette fonction analyse un tableau de nombres et calcule
    diverses mesures statistiques utiles pour l'analyse.

    Parameters
    ----------
    donnees : array_like
        Tableau de nombres à analyser. Peut être une liste,
        un tuple ou un array NumPy.
    inclure_ecart_type : bool, optional
        Si True, calcule l'écart-type en plus des autres statistiques.
        Par défaut True.

    Returns
    -------
    dict
        Dictionnaire contenant les statistiques calculées:

        - 'moyenne' : float
            Moyenne arithmétique des données
        - 'mediane' : float
            Valeur médiane des données
        - 'min' : float
            Valeur minimale
        - 'max' : float
            Valeur maximale
        - 'ecart_type' : float, optional
            Écart-type (seulement si inclure_ecart_type=True)

    Raises
    ------
    ValueError
        Si la liste de données est vide
    TypeError
        Si les données contiennent des éléments non numériques

    Examples
    --------
    >>> donnees = [1, 2, 3, 4, 5]
    >>> stats = calculer_statistiques(donnees)
    >>> print(stats['moyenne'])
    3.0

    >>> stats_simples = calculer_statistiques([10, 20, 30], inclure_ecart_type=False)
    >>> 'ecart_type' in stats_simples
    False

    Notes
    -----
    L'écart-type est calculé avec la formule de l'écart-type
    de la population (division par N), pas de l'échantillon (N-1).
    """
    import statistics

    if not donnees:
        raise ValueError("La liste de données ne peut pas être vide")

    # Vérifier que tous les éléments sont numériques
    try:
        donnees_numeriques = [float(x) for x in donnees]
    except (ValueError, TypeError):
        raise TypeError("Tous les éléments doivent être numériques")

    resultats = {
        'moyenne': statistics.mean(donnees_numeriques),
        'mediane': statistics.median(donnees_numeriques),
        'min': min(donnees_numeriques),
        'max': max(donnees_numeriques)
    }

    if inclure_ecart_type:
        resultats['ecart_type'] = statistics.stdev(donnees_numeriques)

    return resultats
```

### 3. Format Sphinx (format flexible)

```python
def telecharger_fichier(url, destination, timeout=30, retry=3):
    """
    Télécharge un fichier depuis une URL vers le système local.

    :param url: URL du fichier à télécharger
    :type url: str
    :param destination: Chemin local où sauvegarder le fichier
    :type destination: str or Path
    :param timeout: Délai d'attente en secondes pour la requête
    :type timeout: int
    :param retry: Nombre de tentatives en cas d'échec
    :type retry: int
    :return: True si le téléchargement a réussi, False sinon
    :rtype: bool
    :raises ValueError: Si l'URL est invalide
    :raises FileNotFoundError: Si le dossier de destination n'existe pas
    :raises requests.RequestException: En cas d'erreur réseau

    .. note::
       Le fichier est téléchargé en mode streaming pour économiser
       la mémoire avec les gros fichiers.

    .. warning::
       Cette fonction écrase le fichier de destination s'il existe déjà.

    Example:
        >>> success = telecharger_fichier(
        ...     'https://example.com/data.csv',
        ...     '/tmp/ma_donnee.csv',
        ...     timeout=60
        ... )
        >>> if success:
        ...     print("Téléchargement réussi !")
    """
    import requests
    from pathlib import Path

    # Validation de l'URL
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL invalide : doit commencer par http:// ou https://")

    # Validation du dossier de destination
    dest_path = Path(destination)
    if not dest_path.parent.exists():
        raise FileNotFoundError(f"Le dossier {dest_path.parent} n'existe pas")

    # Tentatives de téléchargement
    for tentative in range(retry):
        try:
            response = requests.get(url, timeout=timeout, stream=True)
            response.raise_for_status()

            with open(dest_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return True

        except requests.RequestException as e:
            if tentative == retry - 1:  # Dernière tentative
                raise e
            continue

    return False
```

## Docstrings pour les classes

### Classe complète avec docstrings

```python
class CompteBancaire:
    """
    Représente un compte bancaire avec les opérations de base.

    Cette classe permet de gérer un compte bancaire simple avec
    des opérations de dépôt, retrait et consultation du solde.
    Un historique des transactions est automatiquement maintenu.

    Attributes:
        numero_compte (str): Numéro unique du compte
        titulaire (str): Nom du titulaire du compte
        solde (float): Solde actuel du compte en euros
        historique (list): Liste des transactions effectuées

    Example:
        >>> compte = CompteBancaire("123456", "Alice Dupont", 1000.0)
        >>> compte.deposer(500.0)
        1500.0
        >>> compte.retirer(200.0)
        1300.0
        >>> print(len(compte.historique))
        2
    """

    def __init__(self, numero_compte, titulaire, solde_initial=0.0):
        """
        Initialise un nouveau compte bancaire.

        Args:
            numero_compte (str): Numéro unique du compte
            titulaire (str): Nom du titulaire
            solde_initial (float, optional): Solde de départ. Défaut à 0.0.

        Raises:
            ValueError: Si le solde initial est négatif
            TypeError: Si numero_compte ou titulaire ne sont pas des chaînes

        Example:
            >>> compte = CompteBancaire("123456", "Alice", 1000.0)
            >>> compte.solde
            1000.0
        """
        if not isinstance(numero_compte, str):
            raise TypeError("Le numéro de compte doit être une chaîne")

        if not isinstance(titulaire, str):
            raise TypeError("Le titulaire doit être une chaîne")

        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")

        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = float(solde_initial)
        self.historique = []

        # Enregistrer la création du compte
        self._ajouter_transaction("OUVERTURE", solde_initial)

    def deposer(self, montant):
        """
        Effectue un dépôt sur le compte.

        Args:
            montant (float): Montant à déposer (doit être positif)

        Returns:
            float: Nouveau solde après le dépôt

        Raises:
            ValueError: Si le montant est négatif ou nul
            TypeError: Si le montant n'est pas un nombre

        Example:
            >>> compte = CompteBancaire("123", "Alice", 100)
            >>> nouveau_solde = compte.deposer(50)
            >>> print(nouveau_solde)
            150.0
        """
        if not isinstance(montant, (int, float)):
            raise TypeError("Le montant doit être un nombre")

        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self.solde += montant
        self._ajouter_transaction("DEPOT", montant)
        return self.solde

    def retirer(self, montant):
        """
        Effectue un retrait du compte.

        Args:
            montant (float): Montant à retirer (doit être positif)

        Returns:
            float: Nouveau solde après le retrait

        Raises:
            ValueError: Si le montant est négatif, nul, ou supérieur au solde
            TypeError: Si le montant n'est pas un nombre

        Example:
            >>> compte = CompteBancaire("123", "Alice", 100)
            >>> nouveau_solde = compte.retirer(30)
            >>> print(nouveau_solde)
            70.0
        """
        if not isinstance(montant, (int, float)):
            raise TypeError("Le montant doit être un nombre")

        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        if montant > self.solde:
            raise ValueError("Solde insuffisant")

        self.solde -= montant
        self._ajouter_transaction("RETRAIT", -montant)
        return self.solde

    def obtenir_solde(self):
        """
        Retourne le solde actuel du compte.

        Returns:
            float: Solde actuel en euros

        Example:
            >>> compte = CompteBancaire("123", "Alice", 100)
            >>> print(compte.obtenir_solde())
            100.0
        """
        return self.solde

    def obtenir_historique(self):
        """
        Retourne l'historique des transactions.

        Returns:
            list[dict]: Liste des transactions. Chaque transaction
                est un dictionnaire avec les clés:
                - 'type': Type de transaction ('DEPOT', 'RETRAIT', 'OUVERTURE')
                - 'montant': Montant de la transaction
                - 'date': Date et heure de la transaction
                - 'solde_apres': Solde après la transaction

        Example:
            >>> compte = CompteBancaire("123", "Alice", 100)
            >>> compte.deposer(50)
            150.0
            >>> historique = compte.obtenir_historique()
            >>> len(historique)
            2
            >>> historique[0]['type']
            'OUVERTURE'
        """
        return self.historique.copy()

    def _ajouter_transaction(self, type_transaction, montant):
        """
        Ajoute une transaction à l'historique (méthode privée).

        Args:
            type_transaction (str): Type de transaction
            montant (float): Montant de la transaction

        Note:
            Cette méthode est privée (préfixe _) et ne devrait pas
            être appelée directement par les utilisateurs de la classe.
        """
        from datetime import datetime

        transaction = {
            'type': type_transaction,
            'montant': montant,
            'date': datetime.now(),
            'solde_apres': self.solde
        }
        self.historique.append(transaction)

    def __str__(self):
        """
        Retourne une représentation textuelle du compte.

        Returns:
            str: Description du compte

        Example:
            >>> compte = CompteBancaire("123456", "Alice Dupont", 1000)
            >>> print(compte)
            Compte 123456 - Alice Dupont - Solde: 1000.00€
        """
        return f"Compte {self.numero_compte} - {self.titulaire} - Solde: {self.solde:.2f}€"

    def __repr__(self):
        """
        Retourne une représentation technique du compte.

        Returns:
            str: Représentation technique pour le debugging

        Example:
            >>> compte = CompteBancaire("123456", "Alice", 1000)
            >>> repr(compte)
            "CompteBancaire('123456', 'Alice', 1000.0)"
        """
        return f"CompteBancaire('{self.numero_compte}', '{self.titulaire}', {self.solde})"
```

## Docstrings pour les modules

```python
"""
Module de gestion des comptes bancaires.

Ce module fournit des classes et fonctions pour gérer
des comptes bancaires simples avec les opérations de base.

Classes:
    CompteBancaire: Représente un compte bancaire individuel
    GestionnaireComptes: Gestionnaire pour plusieurs comptes

Fonctions:
    calculer_interets: Calcule les intérêts sur un solde
    valider_numero_compte: Valide le format d'un numéro de compte

Example:
    >>> from banking import CompteBancaire, calculer_interets
    >>> compte = CompteBancaire("123456", "Alice", 1000)
    >>> interets = calculer_interets(compte.obtenir_solde(), 0.02)
    >>> print(f"Intérêts: {interets}€")
    Intérêts: 20.0€

Author: Votre Nom
Date: 2025-01-07
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Votre Nom"
__email__ = "votre.email@example.com"

# Le reste du code du module...
```

## Doctests : Tests dans la documentation

### Concept des doctests

```python
def factorielle(n):
    """
    Calcule la factorielle d'un nombre entier positif.

    La factorielle de n (notée n!) est le produit de tous
    les entiers positifs inférieurs ou égaux à n.

    Args:
        n (int): Nombre entier positif

    Returns:
        int: Factorielle de n

    Raises:
        ValueError: Si n est négatif
        TypeError: Si n n'est pas un entier

    Example:
        >>> factorielle(0)
        1
        >>> factorielle(1)
        1
        >>> factorielle(5)
        120
        >>> factorielle(3)
        6

        # Test d'erreur
        >>> factorielle(-1)
        Traceback (most recent call last):
            ...
        ValueError: n doit être positif ou nul

        >>> factorielle("abc")
        Traceback (most recent call last):
            ...
        TypeError: n doit être un entier
    """
    if not isinstance(n, int):
        raise TypeError("n doit être un entier")

    if n < 0:
        raise ValueError("n doit être positif ou nul")

    if n <= 1:
        return 1

    resultat = 1
    for i in range(2, n + 1):
        resultat *= i

    return resultat

# Exécution des doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

### Doctests avancés

```python
def formater_prix(prix, devise="EUR", precision=2):
    """
    Formate un prix avec devise et précision.

    Args:
        prix (float): Prix à formater
        devise (str): Code de devise (EUR, USD, etc.)
        precision (int): Nombre de décimales

    Returns:
        str: Prix formaté

    Example:
        Tests basiques:
        >>> formater_prix(12.34)
        '12.34 EUR'

        >>> formater_prix(12.34, "USD")
        '12.34 USD'

        >>> formater_prix(12.3456, precision=3)
        '12.346 EUR'

        Tests avec différents types:
        >>> formater_prix(10)
        '10.00 EUR'

        >>> formater_prix(0)
        '0.00 EUR'

        Tests de cas limites:
        >>> formater_prix(1234.5678, "JPY", 0)
        '1235 JPY'

        >>> formater_prix(0.001, precision=3)
        '0.001 EUR'

        Tests avec des valeurs particulières:
        >>> import math
        >>> formater_prix(math.pi, precision=4)
        '3.1416 EUR'
    """
    prix_arrondi = round(float(prix), precision)

    if precision == 0:
        return f"{prix_arrondi:.0f} {devise}"
    else:
        format_str = f"{{:.{precision}f}} {{}}"
        return format_str.format(prix_arrondi, devise)

# Test des doctests
if __name__ == "__main__":
    import doctest
    # Test avec reporting détaillé
    doctest.testmod(verbose=True)
```

## Génération automatique de documentation

### Utilisation de Sphinx

#### Installation
```bash
pip install sphinx sphinx-autodoc-typehints
```

#### Configuration de base (conf.py)
```python
# conf.py pour Sphinx
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Mon Projet'
copyright = '2025, Mon Nom'
author = 'Mon Nom'
version = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',       # Génération auto depuis docstrings
    'sphinx.ext.viewcode',      # Liens vers code source
    'sphinx.ext.napoleon',      # Support Google/NumPy style
    'sphinx.ext.doctest',       # Support des doctests
    'sphinx_autodoc_typehints', # Support des type hints
]

html_theme = 'sphinx_rtd_theme'  # Thème Read The Docs

# Configuration Napoleon pour Google style
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
```

#### Structure pour Sphinx
```
docs/
├── conf.py
├── index.rst
├── modules/
│   ├── banking.rst
│   └── utils.rst
└── _build/
```

#### Fichier index.rst
```rst
Mon Projet Documentation
========================

Bienvenue dans la documentation de Mon Projet !

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   modules/banking
   modules/utils

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

#### Fichier banking.rst
```rst
Module Banking
==============

.. automodule:: banking
   :members:
   :undoc-members:
   :show-inheritance:
```

### Génération de la documentation
```bash
# Initialisation
sphinx-quickstart docs

# Génération
cd docs
make html

# La documentation est générée dans docs/_build/html/
```

## Type hints et documentation

### Combinaison type hints + docstrings

```python
from typing import List, Dict, Optional, Union
from datetime import datetime

def analyser_ventes(
    ventes: List[Dict[str, Union[str, float, datetime]]],
    periode_debut: Optional[datetime] = None,
    periode_fin: Optional[datetime] = None,
    grouper_par: str = "mois"
) -> Dict[str, float]:
    """
    Analyse les données de ventes et retourne des statistiques.

    Cette fonction traite une liste de ventes et calcule diverses
    métriques selon les paramètres fournis.

    Args:
        ventes: Liste des ventes. Chaque vente est un dictionnaire
            contenant au minimum les clés 'date', 'montant', et 'produit'.
        periode_debut: Date de début pour filtrer les ventes.
            Si None, toutes les ventes depuis le début sont incluses.
        periode_fin: Date de fin pour filtrer les ventes.
            Si None, toutes les ventes jusqu'à maintenant sont incluses.
        grouper_par: Méthode de regroupement des données.
            Valeurs possibles: "jour", "semaine", "mois", "annee".

    Returns:
        Dictionnaire contenant les métriques calculées:
        - 'total': Montant total des ventes
        - 'moyenne': Montant moyen par vente
        - 'nombre_ventes': Nombre total de ventes
        - 'meilleur_produit': Nom du produit le plus vendu

    Raises:
        ValueError: Si grouper_par n'est pas une valeur valide
        KeyError: Si les dictionnaires de ventes n'ont pas les clés requises
        TypeError: Si les types des paramètres ne correspondent pas

    Example:
        >>> ventes = [
        ...     {'date': datetime(2023, 1, 15), 'montant': 100.0, 'produit': 'A'},
        ...     {'date': datetime(2023, 1, 20), 'montant': 150.0, 'produit': 'B'}
        ... ]
        >>> stats = analyser_ventes(ventes)
        >>> stats['total']
        250.0
        >>> stats['nombre_ventes']
        2
    """
    # Validation des paramètres
    if grouper_par not in ["jour", "semaine", "mois", "annee"]:
        raise ValueError(f"grouper_par doit être 'jour', 'semaine', 'mois' ou 'annee', reçu: {grouper_par}")

    # Validation de la structure des ventes
    if not all(isinstance(vente, dict) for vente in ventes):
        raise TypeError("Toutes les ventes doivent être des dictionnaires")

    required_keys = {'date', 'montant', 'produit'}
    for i, vente in enumerate(ventes):
        if not required_keys.issubset(vente.keys()):
            missing = required_keys - vente.keys()
            raise KeyError(f"Vente {i} manque les clés: {missing}")

    # Filtrage par période
    ventes_filtrees = ventes
    if periode_debut:
        ventes_filtrees = [v for v in ventes_filtrees if v['date'] >= periode_debut]
    if periode_fin:
        ventes_filtrees = [v for v in ventes_filtrees if v['date'] <= periode_fin]

    if not ventes_filtrees:
        return {
            'total': 0.0,
            'moyenne': 0.0,
            'nombre_ventes': 0,
            'meilleur_produit': None
        }

    # Calculs
    total = sum(vente['montant'] for vente in ventes_filtrees)
    nombre_ventes = len(ventes_filtrees)
    moyenne = total / nombre_ventes

    # Produit le plus vendu
    compteur_produits = {}
    for vente in ventes_filtrees:
        produit = vente['produit']
        compteur_produits[produit] = compteur_produits.get(produit, 0) + 1

    meilleur_produit = max(compteur_produits.items(), key=lambda x: x[1])[0]

    return {
        'total': total,
        'moyenne': moyenne,
        'nombre_ventes': nombre_ventes,
        'meilleur_produit': meilleur_produit
    }
```

## Bonnes pratiques pour les docstrings

### 1. Soyez précis et utiles

```python
# ❌ Docstring inutile
def get_user(id):
    """Gets a user by id"""
    return database.find_user(id)

# ✅ Docstring utile
def obtenir_utilisateur(user_id):
    """
    Récupère un utilisateur par son identifiant unique.

    Args:
        user_id (int): Identifiant unique de l'utilisateur

    Returns:
        dict or None: Dictionnaire contenant les informations utilisateur
            (nom, email, date_creation) ou None si non trouvé

    Raises:
        DatabaseError: Si la connexion à la base échoue
        ValueError: Si user_id n'est pas un entier positif
    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id doit être un entier positif")

    try:
        return database.find_user(user_id)
    except DatabaseError:
        raise DatabaseError("Impossible de se connecter à la base de données")
```

### 2. Expliquez le "pourquoi", pas seulement le "quoi"

```python
# ❌ Explique seulement ce que fait le code
def normaliser_texte(texte):
    """Convertit le texte en minuscules et supprime les espaces"""
    return texte.lower().strip()

# ✅ Explique pourquoi c'est important
def normaliser_texte(texte):
    """
    Normalise un texte pour faciliter les comparaisons et recherches.

    Cette fonction standardise le texte en éliminant les variations
    de casse et d'espacement qui pourraient empêcher de reconnaître
    des entrées identiques (ex: "Alice" vs " alice ").

    Args:
        texte (str): Texte à normaliser

    Returns:
        str: Texte normalisé (minuscules, sans espaces en début/fin)

    Example:
        >>> normaliser_texte("  Alice DUPONT  ")
        'alice dupont'

        # Utile pour les comparaisons
        >>> normaliser_texte("Alice") == normaliser_texte(" ALICE ")
        True
    """
    return texte.lower().strip()
```

### 3. Documentez les cas particuliers et limitations

```python
def calculer_age(date_naissance):
    """
    Calcule l'âge en années à partir de la date de naissance.

    Args:
        date_naissance (datetime.date): Date de naissance

    Returns:
        int: Âge en années révolues

    Note:
        L'âge est calculé par rapport à la date actuelle.
        Pour une personne née le 29 février, l'anniversaire
        est considéré le 28 février les années non bissextiles.

    Warning:
        Cette fonction ne gère pas les fuseaux horaires.
        Pour des calculs précis internationaux, utilisez
        des bibliothèques spécialisées comme pytz.

    Example:
        >>> from datetime import date
        >>> naissance = date(1990, 5, 15)
        >>> age = calculer_age(naissance)
        >>> isinstance(age, int)
        True
        >>> age >= 0
        True
    """
    from datetime import date

    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year

    # Ajustement si l'anniversaire n'est pas encore passé cette année
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1

    return age
```

### 4. Utilisez des exemples concrets

```python
def calculer_remise(prix_initial, pourcentage_remise, remise_max=None):
    """
    Calcule le prix final après application d'une remise.

    Args:
        prix_initial (float): Prix de départ en euros
        pourcentage_remise (float): Pourcentage de remise (0.0 à 1.0)
        remise_max (float, optional): Montant maximum de la remise en euros.
            Si None, aucune limite.

    Returns:
        float: Prix final après remise, arrondi à 2 décimales

    Example:
        Remise simple de 20% :
        >>> calculer_remise(100.0, 0.20)
        80.0

        Remise avec plafond :
        >>> calculer_remise(1000.0, 0.50, remise_max=300.0)
        700.0

        # Sans plafond, la remise aurait été de 500€
        # Avec plafond de 300€, remise limitée à 300€

        Cas particuliers :
        >>> calculer_remise(50.0, 0.0)  # Pas de remise
        50.0
        >>> calculer_remise(0.0, 0.50)  # Prix nul
        0.0
    """
    if pourcentage_remise < 0 or pourcentage_remise > 1:
        raise ValueError("Le pourcentage de remise doit être entre 0 et 1")

    montant_remise = prix_initial * pourcentage_remise

    if remise_max is not None and montant_remise > remise_max:
        montant_remise = remise_max

    prix_final = prix_initial - montant_remise
    return round(prix_final, 2)
```

### 5. Organisez vos sections logiquement

```python
def traiter_commande(commande_id, options=None):
    """
    Traite une commande client avec validation et notifications.

    Cette fonction constitue le point d'entrée principal pour le
    traitement des commandes. Elle orchestre la validation, le calcul
    des prix, la mise à jour des stocks et l'envoi des notifications.

    Args:
        commande_id (str): Identifiant unique de la commande (format: CMD-XXXX)
        options (dict, optional): Options de traitement personnalisées.
            Clés supportées:
            - 'skip_validation' (bool): Ignore la validation (défaut: False)
            - 'force_stock' (bool): Force le traitement même si stock insuffisant
            - 'notification_email' (str): Email alternatif pour notifications

    Returns:
        dict: Résultat du traitement avec les clés:
            - 'success' (bool): True si traitement réussi
            - 'order_number' (str): Numéro de commande généré
            - 'total_amount' (float): Montant total facturé
            - 'estimated_delivery' (datetime): Date de livraison estimée
            - 'tracking_code' (str): Code de suivi si expédition

    Raises:
        ValueError: Si commande_id est invalide ou commande inexistante
        StockError: Si stock insuffisant et force_stock=False
        PaymentError: Si le paiement échoue
        ValidationError: Si la validation des données échoue

    Example:
        Traitement standard :
        >>> result = traiter_commande("CMD-1234")
        >>> result['success']
        True
        >>> 'order_number' in result
        True

        Avec options personnalisées :
        >>> options = {
        ...     'skip_validation': True,
        ...     'notification_email': 'admin@example.com'
        ... }
        >>> result = traiter_commande("CMD-5678", options)

    Note:
        - Le traitement peut prendre plusieurs secondes pour les grosses commandes
        - Les notifications sont envoyées de manière asynchrone
        - Les logs détaillés sont enregistrés dans le fichier system.log

    See Also:
        valider_commande(): Pour validation manuelle
        calculer_frais_livraison(): Pour calcul des frais de port
        annuler_commande(): Pour annulation d'une commande
    """
    # Implémentation...
    pass
```

## Documentation pour différents types de code

### API et services web

```python
from typing import Dict, List, Optional
from datetime import datetime

class APIManager:
    """
    Gestionnaire d'API pour les services web de l'application.

    Cette classe fournit une interface unifiée pour interagir avec
    les différents services web utilisés par l'application. Elle gère
    l'authentification, les retry automatiques et la limitation de débit.

    Attributes:
        base_url (str): URL de base de l'API
        timeout (int): Délai d'attente par défaut en secondes
        max_retries (int): Nombre maximum de tentatives en cas d'échec
        rate_limit (int): Limite de requêtes par minute

    Example:
        >>> api = APIManager("https://api.example.com", timeout=30)
        >>> api.authenticate("token_123")
        >>> users = api.get_users(active=True)
        >>> len(users) > 0
        True
    """

    def __init__(self, base_url: str, timeout: int = 10, max_retries: int = 3):
        """
        Initialise le gestionnaire d'API.

        Args:
            base_url: URL de base de l'API (doit inclure le protocole)
            timeout: Délai d'attente pour les requêtes en secondes
            max_retries: Nombre de tentatives en cas d'échec

        Raises:
            ValueError: Si base_url ne commence pas par http:// ou https://
        """
        if not base_url.startswith(('http://', 'https://')):
            raise ValueError("base_url doit commencer par http:// ou https://")

        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = None
        self._token = None

    def authenticate(self, token: str) -> bool:
        """
        Authentifie le client avec un token d'accès.

        Args:
            token: Token d'authentification obtenu séparément

        Returns:
            True si l'authentification réussit, False sinon

        Example:
            >>> api = APIManager("https://api.example.com")
            >>> success = api.authenticate("valid_token_123")
            >>> success
            True

        Note:
            Le token est stocké en mémoire et utilisé pour toutes
            les requêtes suivantes. Il n'est pas persisté.
        """
        # Test du token avec une requête de validation
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = self._make_request('GET', '/auth/validate', headers=headers)
            if response.status_code == 200:
                self._token = token
                return True
        except Exception:
            pass

        return False

    def get_users(self,
                  active: Optional[bool] = None,
                  limit: int = 100,
                  offset: int = 0) -> List[Dict]:
        """
        Récupère la liste des utilisateurs avec filtres optionnels.

        Args:
            active: Si spécifié, filtre par statut actif/inactif
            limit: Nombre maximum d'utilisateurs à retourner (1-1000)
            offset: Décalage pour la pagination (commence à 0)

        Returns:
            Liste de dictionnaires représentant les utilisateurs.
            Chaque utilisateur contient au minimum:
            - id (int): Identifiant unique
            - name (str): Nom complet
            - email (str): Adresse email
            - active (bool): Statut actif
            - created_at (str): Date de création (ISO format)

        Raises:
            AuthenticationError: Si pas authentifié ou token expiré
            ValueError: Si limit n'est pas dans la plage 1-1000
            APIError: Si erreur côté serveur (5xx) ou requête invalide (4xx)

        Example:
            Récupération basique :
            >>> api = APIManager("https://api.example.com")
            >>> api.authenticate("token")
            True
            >>> users = api.get_users()
            >>> len(users) <= 100
            True

            Avec filtres :
            >>> active_users = api.get_users(active=True, limit=50)
            >>> all(user['active'] for user in active_users)
            True

            Pagination :
            >>> page1 = api.get_users(limit=10, offset=0)
            >>> page2 = api.get_users(limit=10, offset=10)
            >>> len(page1) <= 10 and len(page2) <= 10
            True

        Note:
            - La pagination est basée sur offset/limit
            - Les résultats sont triés par date de création (plus récent en premier)
            - Le cache côté serveur peut causer un délai de 5 minutes pour les nouveaux utilisateurs
        """
        if not self._token:
            raise AuthenticationError("Non authentifié - appelez authenticate() d'abord")

        if not 1 <= limit <= 1000:
            raise ValueError("limit doit être entre 1 et 1000")

        params = {'limit': limit, 'offset': offset}
        if active is not None:
            params['active'] = active

        response = self._make_request('GET', '/users', params=params)
        return response.json()['users']
```

### Algorithmes et traitement de données

```python
def trier_fusion(liste):
    """
    Trie une liste en utilisant l'algorithme de tri fusion (merge sort).

    Le tri fusion est un algorithme de tri stable avec une complexité
    temporelle garantie de O(n log n) dans tous les cas. Il utilise
    la stratégie "diviser pour régner".

    Args:
        liste (list): Liste d'éléments comparables à trier

    Returns:
        list: Nouvelle liste triée par ordre croissant

    Time Complexity:
        - Meilleur cas: O(n log n)
        - Cas moyen: O(n log n)
        - Pire cas: O(n log n)

    Space Complexity:
        O(n) - Nécessite un espace supplémentaire pour la fusion

    Example:
        >>> trier_fusion([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]

        >>> trier_fusion([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]

        >>> trier_fusion([])  # Liste vide
        []

        >>> trier_fusion([42])  # Un seul élément
        [42]

        Fonctionne avec différents types :
        >>> trier_fusion(['z', 'a', 'm', 'b'])
        ['a', 'b', 'm', 'z']

    Note:
        - L'algorithme est stable : l'ordre relatif des éléments égaux est préservé
        - Fonctionne avec tout type d'éléments comparables (int, float, str, etc.)
        - Pour de petites listes (< 50 éléments), l'insertion sort peut être plus rapide
        - La liste originale n'est pas modifiée

    See Also:
        trier_rapide(): Alternative avec complexité O(n log n) en moyenne
        sorted(): Fonction built-in Python (utilise Timsort)
    """
    # Cas de base : liste de 0 ou 1 élément
    if len(liste) <= 1:
        return liste.copy()

    # Diviser la liste en deux moitiés
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]

    # Récursivement trier les deux moitiés
    gauche_triee = trier_fusion(gauche)
    droite_triee = trier_fusion(droite)

    # Fusionner les deux moitiés triées
    return _fusionner(gauche_triee, droite_triee)

def _fusionner(gauche, droite):
    """
    Fusionne deux listes triées en une seule liste triée.

    Args:
        gauche (list): Première liste triée
        droite (list): Deuxième liste triée

    Returns:
        list: Liste fusionnée et triée

    Note:
        Fonction auxiliaire pour trier_fusion().
        Ne devrait pas être appelée directement.
    """
    resultat = []
    i = j = 0

    # Comparer et fusionner élément par élément
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # Ajouter les éléments restants
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat
```

### Code de configuration et utilitaires

```python
import os
import json
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigManager:
    """
    Gestionnaire de configuration centralisé pour l'application.

    Cette classe gère le chargement, la validation et l'accès aux
    paramètres de configuration depuis plusieurs sources :
    fichiers JSON, variables d'environnement, et valeurs par défaut.

    La priorité des sources (de la plus haute à la plus basse) :
    1. Variables d'environnement
    2. Fichier de configuration local
    3. Fichier de configuration par défaut
    4. Valeurs par défaut du code

    Example:
        Configuration basique :
        >>> config = ConfigManager()
        >>> database_url = config.get('database.url')
        >>> api_timeout = config.get('api.timeout', 30)

        Avec fichier personnalisé :
        >>> config = ConfigManager('my_config.json')
        >>> config.get('app.debug', False)
        False
    """

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialise le gestionnaire de configuration.

        Args:
            config_file: Chemin vers le fichier de configuration principal.
                Si None, utilise 'config.json' dans le répertoire courant.

        Example:
            >>> config = ConfigManager()  # Utilise config.json
            >>> config = ConfigManager('/etc/myapp/config.json')  # Fichier spécifique
        """
        self.config_file = config_file or 'config.json'
        self._config = {}
        self._load_config()

    def get(self, key: str, default: Any = None) -> Any:
        """
        Récupère une valeur de configuration par sa clé.

        La clé peut utiliser la notation pointée pour accéder aux
        valeurs imbriquées (ex: 'database.connection.timeout').

        Args:
            key: Clé de configuration (notation pointée supportée)
            default: Valeur par défaut si la clé n'existe pas

        Returns:
            Valeur de configuration ou valeur par défaut

        Example:
            Configuration simple :
            >>> config.get('debug')
            True

            Configuration imbriquée :
            >>> config.get('database.host')
            'localhost'
            >>> config.get('database.port', 5432)
            5432

            Avec valeur par défaut :
            >>> config.get('inexistant.parametre', 'defaut')
            'defaut'
        """
        # Vérifier d'abord les variables d'environnement
        env_key = key.upper().replace('.', '_')
        env_value = os.getenv(env_key)
        if env_value is not None:
            return self._parse_env_value(env_value)

        # Puis chercher dans la configuration chargée
        return self._get_nested_value(self._config, key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Définit une valeur de configuration.

        Args:
            key: Clé de configuration (notation pointée supportée)
            value: Valeur à définir

        Example:
            >>> config.set('database.timeout', 60)
            >>> config.get('database.timeout')
            60

            >>> config.set('new.nested.value', 'test')
            >>> config.get('new.nested.value')
            'test'

        Note:
            Cette modification n'est que temporaire (en mémoire).
            Utilisez save() pour persister les changements.
        """
        self._set_nested_value(self._config, key, value)

    def save(self, file_path: Optional[str] = None) -> None:
        """
        Sauvegarde la configuration actuelle dans un fichier JSON.

        Args:
            file_path: Chemin de sauvegarde. Si None, utilise le fichier
                de configuration original.

        Raises:
            PermissionError: Si pas de permission d'écriture
            OSError: Si erreur d'écriture du fichier

        Example:
            >>> config.set('app.version', '2.0.0')
            >>> config.save()  # Sauvegarde dans le fichier original
            >>> config.save('/backup/config.json')  # Sauvegarde ailleurs
        """
        target_file = file_path or self.config_file

        try:
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise OSError(f"Impossible de sauvegarder la configuration : {e}")

    def _load_config(self) -> None:
        """
        Charge la configuration depuis le fichier JSON.

        Charge d'abord les valeurs par défaut, puis les écrase
        avec les valeurs du fichier de configuration s'il existe.
        """
        # Valeurs par défaut
        self._config = {
            'app': {
                'name': 'MyApp',
                'version': '1.0.0',
                'debug': False
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'timeout': 30
            },
            'api': {
                'timeout': 10,
                'max_retries': 3
            }
        }

        # Charger depuis le fichier si il existe
        if Path(self.config_file).exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    self._merge_config(self._config, file_config)
            except (json.JSONDecodeError, OSError) as e:
                print(f"Attention : Impossible de charger {self.config_file}: {e}")
                print("Utilisation des valeurs par défaut uniquement.")

    def _get_nested_value(self, config_dict: Dict, key: str, default: Any) -> Any:
        """
        Récupère une valeur imbriquée en utilisant la notation pointée.

        Args:
            config_dict: Dictionnaire de configuration
            key: Clé avec notation pointée (ex: 'a.b.c')
            default: Valeur par défaut

        Returns:
            Valeur trouvée ou valeur par défaut
        """
        keys = key.split('.')
        current = config_dict

        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default

        return current

    def _set_nested_value(self, config_dict: Dict, key: str, value: Any) -> None:
        """
        Définit une valeur imbriquée en utilisant la notation pointée.
        """
        keys = key.split('.')
        current = config_dict

        # Naviguer jusqu'au dernier niveau
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        # Définir la valeur finale
        current[keys[-1]] = value

    def _merge_config(self, base: Dict, override: Dict) -> None:
        """
        Fusionne récursivement deux dictionnaires de configuration.
        """
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def _parse_env_value(self, value: str) -> Any:
        """
        Parse une valeur de variable d'environnement en type Python approprié.

        Conversions supportées :
        - 'true'/'false' -> bool
        - Nombres -> int ou float
        - JSON valide -> dict/list
        - Autres -> str
        """
        # Booléens
        if value.lower() in ('true', '1', 'yes', 'on'):
            return True
        if value.lower() in ('false', '0', 'no', 'off'):
            return False

        # Nombres
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            pass

        # JSON
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass

        # Chaîne par défaut
        return value
```

## Outils pour maintenir la documentation

### Scripts de vérification

```python
#!/usr/bin/env python3
"""
Script de vérification de la qualité de la documentation.

Ce script analyse le code Python pour détecter les fonctions
et classes sans docstrings ou avec des docstrings incomplètes.

Usage:
    python check_docs.py [répertoire]

Example:
    python check_docs.py src/
    python check_docs.py .  # Répertoire courant
"""

import ast
import sys
from pathlib import Path
from typing import List, Tuple

class DocStringChecker:
    """
    Vérificateur de qualité des docstrings.

    Analyse les fichiers Python pour détecter :
    - Fonctions/classes sans docstring
    - Docstrings trop courtes
    - Docstrings sans sections Args/Returns
    """

    def __init__(self):
        self.issues = []

    def check_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """
        Vérifie un fichier Python.

        Args:
            file_path: Chemin vers le fichier Python

        Returns:
            Liste des problèmes trouvés (type, ligne, message)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            tree = ast.parse(content)
            checker = DocStringVisitor(str(file_path))
            checker.visit(tree)
            return checker.issues

        except Exception as e:
            return [('error', 0, f"Erreur lors de l'analyse : {e}")]

class DocStringVisitor(ast.NodeVisitor):
    """Visiteur AST pour analyser les docstrings."""

    def __init__(self, filename: str):
        self.filename = filename
        self.issues = []

    def visit_FunctionDef(self, node):
        """Visite une définition de fonction."""
        self._check_docstring(node, 'function')
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Visite une définition de classe."""
        self._check_docstring(node, 'class')
        self.generic_visit(node)

    def _check_docstring(self, node, node_type):
        """Vérifie la docstring d'un nœud."""
        docstring = ast.get_docstring(node)

        # Ignorer les méthodes privées et spéciales pour les fonctions
        if node_type == 'function' and node.name.startswith('_'):
            return

        if not docstring:
            self.issues.append((
                'missing',
                node.lineno,
                f"{node_type.capitalize()} '{node.name}' sans docstring"
            ))
            return

        # Vérifier la longueur
        if len(docstring.strip()) < 20:
            self.issues.append((
                'short',
                node.lineno,
                f"{node_type.capitalize()} '{node.name}' avec docstring trop courte"
            ))

        # Vérifier la présence de sections pour les fonctions publiques
        if node_type == 'function' and not node.name.startswith('_'):
            if len(node.args.args) > 1:  # Plus que 'self'
                if 'Args:' not in docstring and 'Parameters:' not in docstring:
                    self.issues.append((
                        'no_args',
                        node.lineno,
                        f"Fonction '{node.name}' sans section Args/Parameters"
                    ))

            # Vérifier Returns pour fonctions non-void
            has_return = any(isinstance(n, ast.Return) for n in ast.walk(node) if n != node)
            if has_return:
                if 'Returns:' not in docstring and 'Return:' not in docstring:
                    self.issues.append((
                        'no_returns',
                        node.lineno,
                        f"Fonction '{node.name}' sans section Returns"
                    ))

# 10.4 : Documentation avec docstrings (suite)

## Bonnes pratiques pour les docstrings

### 1. Soyez précis et utiles

```python
# ❌ Docstring inutile
def get_user(id):
    """Gets a user by id"""
    return database.find_user(id)

# ✅ Docstring utile
def obtenir_utilisateur(user_id):
    """
    Récupère un utilisateur par son identifiant unique.

    Args:
        user_id (int): Identifiant unique de l'utilisateur

    Returns:
        dict or None: Dictionnaire contenant les informations utilisateur
            (nom, email, date_creation) ou None si non trouvé

    Raises:
        DatabaseError: Si la connexion à la base échoue
        ValueError: Si user_id n'est pas un entier positif
    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id doit être un entier positif")

    try:
        return database.find_user(user_id)
    except DatabaseError:
        raise DatabaseError("Impossible de se connecter à la base de données")
```

### 2. Expliquez le "pourquoi", pas seulement le "quoi"

```python
# ❌ Explique seulement ce que fait le code
def normaliser_texte(texte):
    """Convertit le texte en minuscules et supprime les espaces"""
    return texte.lower().strip()

# ✅ Explique pourquoi c'est important
def normaliser_texte(texte):
    """
    Normalise un texte pour faciliter les comparaisons et recherches.

    Cette fonction standardise le texte en éliminant les variations
    de casse et d'espacement qui pourraient empêcher de reconnaître
    des entrées identiques (ex: "Alice" vs " alice ").

    Args:
        texte (str): Texte à normaliser

    Returns:
        str: Texte normalisé (minuscules, sans espaces en début/fin)

    Example:
        >>> normaliser_texte("  Alice DUPONT  ")
        'alice dupont'

        # Utile pour les comparaisons
        >>> normaliser_texte("Alice") == normaliser_texte(" ALICE ")
        True
    """
    return texte.lower().strip()
```

### 3. Documentez les cas particuliers et limitations

```python
def calculer_age(date_naissance):
    """
    Calcule l'âge en années à partir de la date de naissance.

    Args:
        date_naissance (datetime.date): Date de naissance

    Returns:
        int: Âge en années révolues

    Note:
        L'âge est calculé par rapport à la date actuelle.
        Pour une personne née le 29 février, l'anniversaire
        est considéré le 28 février les années non bissextiles.

    Warning:
        Cette fonction ne gère pas les fuseaux horaires.
        Pour des calculs précis internationaux, utilisez
        des bibliothèques spécialisées comme pytz.

    Example:
        >>> from datetime import date
        >>> naissance = date(1990, 5, 15)
        >>> age = calculer_age(naissance)
        >>> isinstance(age, int)
        True
        >>> age >= 0
        True
    """
    from datetime import date

    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year

    # Ajustement si l'anniversaire n'est pas encore passé cette année
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1

    return age
```

### 4. Utilisez des exemples concrets

```python
def calculer_remise(prix_initial, pourcentage_remise, remise_max=None):
    """
    Calcule le prix final après application d'une remise.

    Args:
        prix_initial (float): Prix de départ en euros
        pourcentage_remise (float): Pourcentage de remise (0.0 à 1.0)
        remise_max (float, optional): Montant maximum de la remise en euros.
            Si None, aucune limite.

    Returns:
        float: Prix final après remise, arrondi à 2 décimales

    Example:
        Remise simple de 20% :
        >>> calculer_remise(100.0, 0.20)
        80.0

        Remise avec plafond :
        >>> calculer_remise(1000.0, 0.50, remise_max=300.0)
        700.0

        # Sans plafond, la remise aurait été de 500€
        # Avec plafond de 300€, remise limitée à 300€

        Cas particuliers :
        >>> calculer_remise(50.0, 0.0)  # Pas de remise
        50.0
        >>> calculer_remise(0.0, 0.50)  # Prix nul
        0.0
    """
    if pourcentage_remise < 0 or pourcentage_remise > 1:
        raise ValueError("Le pourcentage de remise doit être entre 0 et 1")

    montant_remise = prix_initial * pourcentage_remise

    if remise_max is not None and montant_remise > remise_max:
        montant_remise = remise_max

    prix_final = prix_initial - montant_remise
    return round(prix_final, 2)
```

### 5. Organisez vos sections logiquement

```python
def traiter_commande(commande_id, options=None):
    """
    Traite une commande client avec validation et notifications.

    Cette fonction constitue le point d'entrée principal pour le
    traitement des commandes. Elle orchestre la validation, le calcul
    des prix, la mise à jour des stocks et l'envoi des notifications.

    Args:
        commande_id (str): Identifiant unique de la commande (format: CMD-XXXX)
        options (dict, optional): Options de traitement personnalisées.
            Clés supportées:
            - 'skip_validation' (bool): Ignore la validation (défaut: False)
            - 'force_stock' (bool): Force le traitement même si stock insuffisant
            - 'notification_email' (str): Email alternatif pour notifications

    Returns:
        dict: Résultat du traitement avec les clés:
            - 'success' (bool): True si traitement réussi
            - 'order_number' (str): Numéro de commande généré
            - 'total_amount' (float): Montant total facturé
            - 'estimated_delivery' (datetime): Date de livraison estimée
            - 'tracking_code' (str): Code de suivi si expédition

    Raises:
        ValueError: Si commande_id est invalide ou commande inexistante
        StockError: Si stock insuffisant et force_stock=False
        PaymentError: Si le paiement échoue
        ValidationError: Si la validation des données échoue

    Example:
        Traitement standard :
        >>> result = traiter_commande("CMD-1234")
        >>> result['success']
        True
        >>> 'order_number' in result
        True

        Avec options personnalisées :
        >>> options = {
        ...     'skip_validation': True,
        ...     'notification_email': 'admin@example.com'
        ... }
        >>> result = traiter_commande("CMD-5678", options)

    Note:
        - Le traitement peut prendre plusieurs secondes pour les grosses commandes
        - Les notifications sont envoyées de manière asynchrone
        - Les logs détaillés sont enregistrés dans le fichier system.log

    See Also:
        valider_commande(): Pour validation manuelle
        calculer_frais_livraison(): Pour calcul des frais de port
        annuler_commande(): Pour annulation d'une commande
    """
    # Implémentation...
    pass
```

## Documentation pour différents types de code

### API et services web

```python
from typing import Dict, List, Optional
from datetime import datetime

class APIManager:
    """
    Gestionnaire d'API pour les services web de l'application.

    Cette classe fournit une interface unifiée pour interagir avec
    les différents services web utilisés par l'application. Elle gère
    l'authentification, les retry automatiques et la limitation de débit.

    Attributes:
        base_url (str): URL de base de l'API
        timeout (int): Délai d'attente par défaut en secondes
        max_retries (int): Nombre maximum de tentatives en cas d'échec
        rate_limit (int): Limite de requêtes par minute

    Example:
        >>> api = APIManager("https://api.example.com", timeout=30)
        >>> api.authenticate("token_123")
        >>> users = api.get_users(active=True)
        >>> len(users) > 0
        True
    """

    def __init__(self, base_url: str, timeout: int = 10, max_retries: int = 3):
        """
        Initialise le gestionnaire d'API.

        Args:
            base_url: URL de base de l'API (doit inclure le protocole)
            timeout: Délai d'attente pour les requêtes en secondes
            max_retries: Nombre de tentatives en cas d'échec

        Raises:
            ValueError: Si base_url ne commence pas par http:// ou https://
        """
        if not base_url.startswith(('http://', 'https://')):
            raise ValueError("base_url doit commencer par http:// ou https://")

        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = None
        self._token = None

    def authenticate(self, token: str) -> bool:
        """
        Authentifie le client avec un token d'accès.

        Args:
            token: Token d'authentification obtenu séparément

        Returns:
            True si l'authentification réussit, False sinon

        Example:
            >>> api = APIManager("https://api.example.com")
            >>> success = api.authenticate("valid_token_123")
            >>> success
            True

        Note:
            Le token est stocké en mémoire et utilisé pour toutes
            les requêtes suivantes. Il n'est pas persisté.
        """
        # Test du token avec une requête de validation
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = self._make_request('GET', '/auth/validate', headers=headers)
            if response.status_code == 200:
                self._token = token
                return True
        except Exception:
            pass

        return False

    def get_users(self,
                  active: Optional[bool] = None,
                  limit: int = 100,
                  offset: int = 0) -> List[Dict]:
        """
        Récupère la liste des utilisateurs avec filtres optionnels.

        Args:
            active: Si spécifié, filtre par statut actif/inactif
            limit: Nombre maximum d'utilisateurs à retourner (1-1000)
            offset: Décalage pour la pagination (commence à 0)

        Returns:
            Liste de dictionnaires représentant les utilisateurs.
            Chaque utilisateur contient au minimum:
            - id (int): Identifiant unique
            - name (str): Nom complet
            - email (str): Adresse email
            - active (bool): Statut actif
            - created_at (str): Date de création (ISO format)

        Raises:
            AuthenticationError: Si pas authentifié ou token expiré
            ValueError: Si limit n'est pas dans la plage 1-1000
            APIError: Si erreur côté serveur (5xx) ou requête invalide (4xx)

        Example:
            Récupération basique :
            >>> api = APIManager("https://api.example.com")
            >>> api.authenticate("token")
            True
            >>> users = api.get_users()
            >>> len(users) <= 100
            True

            Avec filtres :
            >>> active_users = api.get_users(active=True, limit=50)
            >>> all(user['active'] for user in active_users)
            True

            Pagination :
            >>> page1 = api.get_users(limit=10, offset=0)
            >>> page2 = api.get_users(limit=10, offset=10)
            >>> len(page1) <= 10 and len(page2) <= 10
            True

        Note:
            - La pagination est basée sur offset/limit
            - Les résultats sont triés par date de création (plus récent en premier)
            - Le cache côté serveur peut causer un délai de 5 minutes pour les nouveaux utilisateurs
        """
        if not self._token:
            raise AuthenticationError("Non authentifié - appelez authenticate() d'abord")

        if not 1 <= limit <= 1000:
            raise ValueError("limit doit être entre 1 et 1000")

        params = {'limit': limit, 'offset': offset}
        if active is not None:
            params['active'] = active

        response = self._make_request('GET', '/users', params=params)
        return response.json()['users']
```

### Algorithmes et traitement de données

```python
def trier_fusion(liste):
    """
    Trie une liste en utilisant l'algorithme de tri fusion (merge sort).

    Le tri fusion est un algorithme de tri stable avec une complexité
    temporelle garantie de O(n log n) dans tous les cas. Il utilise
    la stratégie "diviser pour régner".

    Args:
        liste (list): Liste d'éléments comparables à trier

    Returns:
        list: Nouvelle liste triée par ordre croissant

    Time Complexity:
        - Meilleur cas: O(n log n)
        - Cas moyen: O(n log n)
        - Pire cas: O(n log n)

    Space Complexity:
        O(n) - Nécessite un espace supplémentaire pour la fusion

    Example:
        >>> trier_fusion([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]

        >>> trier_fusion([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]

        >>> trier_fusion([])  # Liste vide
        []

        >>> trier_fusion([42])  # Un seul élément
        [42]

        Fonctionne avec différents types :
        >>> trier_fusion(['z', 'a', 'm', 'b'])
        ['a', 'b', 'm', 'z']

    Note:
        - L'algorithme est stable : l'ordre relatif des éléments égaux est préservé
        - Fonctionne avec tout type d'éléments comparables (int, float, str, etc.)
        - Pour de petites listes (< 50 éléments), l'insertion sort peut être plus rapide
        - La liste originale n'est pas modifiée

    See Also:
        trier_rapide(): Alternative avec complexité O(n log n) en moyenne
        sorted(): Fonction built-in Python (utilise Timsort)
    """
    # Cas de base : liste de 0 ou 1 élément
    if len(liste) <= 1:
        return liste.copy()

    # Diviser la liste en deux moitiés
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]

    # Récursivement trier les deux moitiés
    gauche_triee = trier_fusion(gauche)
    droite_triee = trier_fusion(droite)

    # Fusionner les deux moitiés triées
    return _fusionner(gauche_triee, droite_triee)

def _fusionner(gauche, droite):
    """
    Fusionne deux listes triées en une seule liste triée.

    Args:
        gauche (list): Première liste triée
        droite (list): Deuxième liste triée

    Returns:
        list: Liste fusionnée et triée

    Note:
        Fonction auxiliaire pour trier_fusion().
        Ne devrait pas être appelée directement.
    """
    resultat = []
    i = j = 0

    # Comparer et fusionner élément par élément
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # Ajouter les éléments restants
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat
```

### Code de configuration et utilitaires

```python
import os
import json
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigManager:
    """
    Gestionnaire de configuration centralisé pour l'application.

    Cette classe gère le chargement, la validation et l'accès aux
    paramètres de configuration depuis plusieurs sources :
    fichiers JSON, variables d'environnement, et valeurs par défaut.

    La priorité des sources (de la plus haute à la plus basse) :
    1. Variables d'environnement
    2. Fichier de configuration local
    3. Fichier de configuration par défaut
    4. Valeurs par défaut du code

    Example:
        Configuration basique :
        >>> config = ConfigManager()
        >>> database_url = config.get('database.url')
        >>> api_timeout = config.get('api.timeout', 30)

        Avec fichier personnalisé :
        >>> config = ConfigManager('my_config.json')
        >>> config.get('app.debug', False)
        False
    """

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialise le gestionnaire de configuration.

        Args:
            config_file: Chemin vers le fichier de configuration principal.
                Si None, utilise 'config.json' dans le répertoire courant.

        Example:
            >>> config = ConfigManager()  # Utilise config.json
            >>> config = ConfigManager('/etc/myapp/config.json')  # Fichier spécifique
        """
        self.config_file = config_file or 'config.json'
        self._config = {}
        self._load_config()

    def get(self, key: str, default: Any = None) -> Any:
        """
        Récupère une valeur de configuration par sa clé.

        La clé peut utiliser la notation pointée pour accéder aux
        valeurs imbriquées (ex: 'database.connection.timeout').

        Args:
            key: Clé de configuration (notation pointée supportée)
            default: Valeur par défaut si la clé n'existe pas

        Returns:
            Valeur de configuration ou valeur par défaut

        Example:
            Configuration simple :
            >>> config.get('debug')
            True

            Configuration imbriquée :
            >>> config.get('database.host')
            'localhost'
            >>> config.get('database.port', 5432)
            5432

            Avec valeur par défaut :
            >>> config.get('inexistant.parametre', 'defaut')
            'defaut'
        """
        # Vérifier d'abord les variables d'environnement
        env_key = key.upper().replace('.', '_')
        env_value = os.getenv(env_key)
        if env_value is not None:
            return self._parse_env_value(env_value)

        # Puis chercher dans la configuration chargée
        return self._get_nested_value(self._config, key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Définit une valeur de configuration.

        Args:
            key: Clé de configuration (notation pointée supportée)
            value: Valeur à définir

        Example:
            >>> config.set('database.timeout', 60)
            >>> config.get('database.timeout')
            60

            >>> config.set('new.nested.value', 'test')
            >>> config.get('new.nested.value')
            'test'

        Note:
            Cette modification n'est que temporaire (en mémoire).
            Utilisez save() pour persister les changements.
        """
        self._set_nested_value(self._config, key, value)

    def save(self, file_path: Optional[str] = None) -> None:
        """
        Sauvegarde la configuration actuelle dans un fichier JSON.

        Args:
            file_path: Chemin de sauvegarde. Si None, utilise le fichier
                de configuration original.

        Raises:
            PermissionError: Si pas de permission d'écriture
            OSError: Si erreur d'écriture du fichier

        Example:
            >>> config.set('app.version', '2.0.0')
            >>> config.save()  # Sauvegarde dans le fichier original
            >>> config.save('/backup/config.json')  # Sauvegarde ailleurs
        """
        target_file = file_path or self.config_file

        try:
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise OSError(f"Impossible de sauvegarder la configuration : {e}")

    def _load_config(self) -> None:
        """
        Charge la configuration depuis le fichier JSON.

        Charge d'abord les valeurs par défaut, puis les écrase
        avec les valeurs du fichier de configuration s'il existe.
        """
        # Valeurs par défaut
        self._config = {
            'app': {
                'name': 'MyApp',
                'version': '1.0.0',
                'debug': False
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'timeout': 30
            },
            'api': {
                'timeout': 10,
                'max_retries': 3
            }
        }

        # Charger depuis le fichier si il existe
        if Path(self.config_file).exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    self._merge_config(self._config, file_config)
            except (json.JSONDecodeError, OSError) as e:
                print(f"Attention : Impossible de charger {self.config_file}: {e}")
                print("Utilisation des valeurs par défaut uniquement.")

    def _get_nested_value(self, config_dict: Dict, key: str, default: Any) -> Any:
        """
        Récupère une valeur imbriquée en utilisant la notation pointée.

        Args:
            config_dict: Dictionnaire de configuration
            key: Clé avec notation pointée (ex: 'a.b.c')
            default: Valeur par défaut

        Returns:
            Valeur trouvée ou valeur par défaut
        """
        keys = key.split('.')
        current = config_dict

        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default

        return current

    def _set_nested_value(self, config_dict: Dict, key: str, value: Any) -> None:
        """
        Définit une valeur imbriquée en utilisant la notation pointée.
        """
        keys = key.split('.')
        current = config_dict

        # Naviguer jusqu'au dernier niveau
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        # Définir la valeur finale
        current[keys[-1]] = value

    def _merge_config(self, base: Dict, override: Dict) -> None:
        """
        Fusionne récursivement deux dictionnaires de configuration.
        """
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def _parse_env_value(self, value: str) -> Any:
        """
        Parse une valeur de variable d'environnement en type Python approprié.

        Conversions supportées :
        - 'true'/'false' -> bool
        - Nombres -> int ou float
        - JSON valide -> dict/list
        - Autres -> str
        """
        # Booléens
        if value.lower() in ('true', '1', 'yes', 'on'):
            return True
        if value.lower() in ('false', '0', 'no', 'off'):
            return False

        # Nombres
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            pass

        # JSON
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass

        # Chaîne par défaut
        return value
```

## Outils pour maintenir la documentation

### Scripts de vérification

```python
#!/usr/bin/env python3
"""
Script de vérification de la qualité de la documentation.

Ce script analyse le code Python pour détecter les fonctions
et classes sans docstrings ou avec des docstrings incomplètes.

Usage:
    python check_docs.py [répertoire]

Example:
    python check_docs.py src/
    python check_docs.py .  # Répertoire courant
"""

import ast
import sys
from pathlib import Path
from typing import List, Tuple

class DocStringChecker:
    """
    Vérificateur de qualité des docstrings.

    Analyse les fichiers Python pour détecter :
    - Fonctions/classes sans docstring
    - Docstrings trop courtes
    - Docstrings sans sections Args/Returns
    """

    def __init__(self):
        self.issues = []

    def check_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """
        Vérifie un fichier Python.

        Args:
            file_path: Chemin vers le fichier Python

        Returns:
            Liste des problèmes trouvés (type, ligne, message)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            tree = ast.parse(content)
            checker = DocStringVisitor(str(file_path))
            checker.visit(tree)
            return checker.issues

        except Exception as e:
            return [('error', 0, f"Erreur lors de l'analyse : {e}")]

class DocStringVisitor(ast.NodeVisitor):
    """Visiteur AST pour analyser les docstrings."""

    def __init__(self, filename: str):
        self.filename = filename
        self.issues = []

    def visit_FunctionDef(self, node):
        """Visite une définition de fonction."""
        self._check_docstring(node, 'function')
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Visite une définition de classe."""
        self._check_docstring(node, 'class')
        self.generic_visit(node)

    def _check_docstring(self, node, node_type):
        """Vérifie la docstring d'un nœud."""
        docstring = ast.get_docstring(node)

        # Ignorer les méthodes privées et spéciales pour les fonctions
        if node_type == 'function' and node.name.startswith('_'):
            return

        if not docstring:
            self.issues.append((
                'missing',
                node.lineno,
                f"{node_type.capitalize()} '{node.name}' sans docstring"
            ))
            return

        # Vérifier la longueur
        if len(docstring.strip()) < 20:
            self.issues.append((
                'short',
                node.lineno,
                f"{node_type.capitalize()} '{node.name}' avec docstring trop courte"
            ))

        # Vérifier la présence de sections pour les fonctions publiques
        if node_type == 'function' and not node.name.startswith('_'):
            if len(node.args.args) > 1:  # Plus que 'self'
                if 'Args:' not in docstring and 'Parameters:' not in docstring:
                    self.issues.append((
                        'no_args',
                        node.lineno,
                        f"Fonction '{node.name}' sans section Args/Parameters"
                    ))

            # Vérifier Returns pour fonctions non-void
            has_return = any(isinstance(n, ast.Return) for n in ast.walk(node) if n != node)
            if has_return:
                if 'Returns:' not in docstring and 'Return:' not in docstring:
                    self.issues.append((
                        'no_returns',
                        node.lineno,
                        f"Fonction '{node.name}' sans section Returns"
                    ))

def main():
    """Point d'entrée principal du script."""
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
    else:
        target = Path('.')

    if not target.exists():
        print(f"Erreur : {target} n'existe pas")
        sys.exit(1)

    checker = DocStringChecker()
    total_issues = 0

    # Trouver tous les fichiers Python
    python_files = []
    if target.is_file() and target.suffix == '.py':
        python_files = [target]
    else:
        python_files = list(target.rglob('*.py'))

    print(f"Vérification de {len(python_files)} fichiers Python...")
    print("=" * 60)

    for file_path in python_files:
        issues = checker.check_file(file_path)
        if issues:
            print(f"\n📁 {file_path}")
            for issue_type, line_no, message in issues:
                emoji = {
                    'missing': '❌',
                    'short': '⚠️ ',
                    'no_args': '📝',
                    'no_returns': '↩️ ',
                    'error': '💥'
                }.get(issue_type, '⚠️')

                print(f"  {emoji} Ligne {line_no:3d}: {message}")
                total_issues += 1

    print("\n" + "=" * 60)
    if total_issues == 0:
        print("✅ Aucun problème de documentation trouvé !")
        sys.exit(0)
    else:
        print(f"❌ {total_issues} problème(s) de documentation trouvé(s)")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## Intégration dans le workflow de développement

### Pre-commit hook pour documentation

```python
#!/usr/bin/env python3
"""
Pre-commit hook pour vérifier la qualité de la documentation.

Ce script est exécuté automatiquement avant chaque commit
pour s'assurer que le code ajouté/modifié a une documentation adequate.
"""

import subprocess
import sys
from pathlib import Path

def check_staged_files():
    """
    Vérifie les fichiers Python modifiés dans le commit.

    Returns:
        bool: True si tous les fichiers ont une doc adequade, False sinon
    """
    # Obtenir la liste des fichiers Python modifiés
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only', '--diff-filter=AM'],
        capture_output=True,
        text=True
    )

    modified_files = [
        f for f in result.stdout.strip().split('\n')
        if f.endswith('.py') and Path(f).exists()
    ]

    if not modified_files:
        print("✅ Aucun fichier Python modifié")
        return True

    print(f"🔍 Vérification de {len(modified_files)} fichier(s) Python...")

    # Exécuter le vérificateur de documentation
    issues_found = False
    for file_path in modified_files:
        checker = DocStringChecker()
        issues = checker.check_file(Path(file_path))

        if issues:
            if not issues_found:
                print("\n❌ Problèmes de documentation détectés :")
                issues_found = True

            print(f"\n📁 {file_path}")
            for issue_type, line_no, message in issues:
                print(f"  • Ligne {line_no}: {message}")

    if issues_found:
        print("\n💡 Ajoutez des docstrings appropriées avant de commiter.")
        print("   Consultez le guide de style dans la documentation du projet.")
        return False
    else:
        print("✅ Documentation adequade pour tous les fichiers modifiés")
        return True

if __name__ == '__main__':
    if not check_staged_files():
        sys.exit(1)
```

### Configuration dans setup.cfg/pyproject.toml

```toml
# pyproject.toml
[tool.doc-check]
# Configuration pour le vérificateur de documentation
min_docstring_length = 20
check_args = true
check_returns = true
ignore_private = true
ignore_tests = true

[tool.sphinx]
# Configuration pour la génération automatique
source_dir = "docs/source"
build_dir = "docs/build"
auto_build = true
```

## Maintenance de la documentation

### Script de génération automatique

```python
#!/usr/bin/env python3
"""
Générateur automatique de documentation de base.

Ce script génère des docstrings de base pour les fonctions
et classes qui n'en ont pas, en se basant sur l'analyse
du code (signatures, type hints, etc.).
"""

import ast
import re
from pathlib import Path
from typing import List, Optional

class DocStringGenerator:
    """
    Générateur de docstrings de base pour code Python.

    Analyse le code existant et génère des templates de docstrings
    basés sur les signatures de fonctions et type hints.
    """

    def generate_function_docstring(self, func_node: ast.FunctionDef) -> str:
        """
        Génère une docstring de base pour une fonction.

        Args:
            func_node: Nœud AST de la fonction

        Returns:
            str: Template de docstring généré
        """
        lines = []

        # Description générique basée sur le nom
        func_name_readable = self._humanize_name(func_node.name)
        lines.append(f'    """')
        lines.append(f'    {func_name_readable}.')
        lines.append(f'    ')

        # Section Args si la fonction a des paramètres
        args = [arg.arg for arg in func_node.args.args if arg.arg != 'self']
        if args:
            lines.append(f'    Args:')
            for arg in args:
                arg_desc = self._humanize_name(arg)
                lines.append(f'        {arg}: {arg_desc}')
            lines.append(f'    ')

        # Section Returns si la fonction a un return
        has_return = any(isinstance(node, ast.Return) and node.value
                        for node in ast.walk(func_node))
        if has_return:
            lines.append(f'    Returns:')
            lines.append(f'        Description du retour')
            lines.append(f'    ')

        # Exemple basique
        lines.append(f'    Example:')
        example_call = self._generate_example_call(func_node)
        lines.append(f'        >>> {example_call}')
        lines.append(f'        # TODO: Ajouter le résultat attendu')
        lines.append(f'    """')

        return '\n'.join(lines)

    def generate_class_docstring(self, class_node: ast.ClassDef) -> str:
        """
        Génère une docstring de base pour une classe.

        Args:
            class_node: Nœud AST de la classe

        Returns:
            str: Template de docstring généré
        """
        lines = []
        class_name_readable = self._humanize_name(class_node.name)

        lines.append(f'    """')
        lines.append(f'    {class_name_readable}.')
        lines.append(f'    ')
        lines.append(f'    TODO: Décrire le rôle et la responsabilité de cette classe.')
        lines.append(f'    ')

        # Analyser les attributs d'instance depuis __init__
        init_method = None
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                init_method = node
                break

        if init_method:
            instance_attrs = self._extract_instance_attributes(init_method)
            if instance_attrs:
                lines.append(f'    Attributes:')
                for attr in instance_attrs:
                    attr_desc = self._humanize_name(attr)
                    lines.append(f'        {attr}: {attr_desc}')
                lines.append(f'    ')

        # Exemple d'utilisation
        lines.append(f'    Example:')
        lines.append(f'        >>> obj = {class_node.name}()')
        lines.append(f'        >>> # TODO: Ajouter exemple d\'utilisation')
        lines.append(f'    """')

        return '\n'.join(lines)

    def _humanize_name(self, name: str) -> str:
        """
        Convertit un nom de variable/fonction en description lisible.

        Args:
            name: Nom à convertir

        Returns:
            str: Description lisible
        """
        # Convertir snake_case en mots
        words = name.replace('_', ' ').split()

        # Capitaliser la première lettre
        if words:
            words[0] = words[0].capitalize()

        return ' '.join(words)

    def _generate_example_call(self, func_node: ast.FunctionDef) -> str:
        """Génère un appel d'exemple pour une fonction."""
        args = [arg.arg for arg in func_node.args.args if arg.arg != 'self']

        # Générer des valeurs d'exemple basiques
        example_args = []
        for arg in args:
            if 'id' in arg.lower():
                example_args.append('1')
            elif 'name' in arg.lower() or 'text' in arg.lower():
                example_args.append('"exemple"')
            elif 'count' in arg.lower() or 'num' in arg.lower():
                example_args.append('10')
            elif 'flag' in arg.lower() or 'enable' in arg.lower():
                example_args.append('True')
            else:
                example_args.append('...')

        args_str = ', '.join(example_args)
        return f"{func_node.name}({args_str})"

    def _extract_instance_attributes(self, init_node: ast.FunctionDef) -> List[str]:
        """
        Extrait les attributs d'instance depuis la méthode __init__.

        Args:
            init_node: Nœud AST de la méthode __init__

        Returns:
            List[str]: Liste des noms d'attributs
        """
        attributes = []

        for node in ast.walk(init_node):
            if (isinstance(node, ast.Assign) and
                len(node.targets) == 1 and
                isinstance(node.targets[0], ast.Attribute) and
                isinstance(node.targets[0].value, ast.Name) and
                node.targets[0].value.id == 'self'):

                attr_name = node.targets[0].attr
                attributes.append(attr_name)

        return sorted(set(attributes))

def process_file(file_path: Path, dry_run: bool = True) -> None:
    """
    Traite un fichier Python et génère les docstrings manquantes.

    Args:
        file_path: Chemin vers le fichier Python
        dry_run: Si True, affiche seulement ce qui serait généré
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"❌ Erreur de syntaxe dans {file_path}: {e}")
        return

    generator = DocStringGenerator()
    suggestions = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                # Ignorer les méthodes privées
                if node.name.startswith('_') and not node.name.startswith('__'):
                    continue

                if isinstance(node, ast.FunctionDef):
                    docstring = generator.generate_function_docstring(node)
                    suggestions.append((node.lineno, 'function', node.name, docstring))
                else:
                    docstring = generator.generate_class_docstring(node)
                    suggestions.append((node.lineno, 'class', node.name, docstring))

    if suggestions:
        print(f"\n📁 {file_path}")
        print(f"   {len(suggestions)} docstring(s) à ajouter :")

        for line_no, node_type, name, docstring in suggestions:
            print(f"\n   🔧 {node_type.capitalize()} '{name}' (ligne {line_no}):")
            if dry_run:
                print("      " + "\n      ".join(docstring.split('\n')))
            else:
                # TODO: Implémenter l'insertion automatique
                print("      Docstring ajoutée automatiquement")

    return suggestions

def main():
    """Point d'entrée principal."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Génère des docstrings de base pour code Python"
    )
    parser.add_argument('path', help='Fichier ou répertoire à traiter')
    parser.add_argument('--apply', action='store_true',
                       help='Applique les modifications (par défaut: dry-run)')

    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"❌ {target} n'existe pas")
        return 1

    if target.is_file():
        files = [target]
    else:
        files = list(target.rglob('*.py'))

    print(f"🔍 Analyse de {len(files)} fichier(s) Python...")

    total_suggestions = 0
    for file_path in files:
        suggestions = process_file(file_path, dry_run=not args.apply)
        if suggestions:
            total_suggestions += len(suggestions)

    print(f"\n📊 Résumé : {total_suggestions} docstring(s) à ajouter")
    if not args.apply and total_suggestions > 0:
        print("💡 Utilisez --apply pour appliquer les modifications")

if __name__ == '__main__':
    main()
```

## Documentation collaborative

### Templates de documentation

```python
# templates/function_template.py
"""
Template de docstring pour une fonction.

Copiez-collez ce template et adaptez-le à votre fonction.
"""

def ma_fonction(param1, param2=None, **kwargs):
    """
    [DESCRIPTION COURTE EN UNE LIGNE]

    [DESCRIPTION DÉTAILLÉE OPTIONNELLE]
    Cette section explique en détail ce que fait la fonction,
    pourquoi elle existe, et comment l'utiliser efficacement.

    Args:
        param1 (type): Description du premier paramètre.
            Peut être sur plusieurs lignes si nécessaire.
        param2 (type, optional): Description du paramètre optionnel.
            Défaut à None.
        **kwargs: Arguments supplémentaires passés à [autre_fonction].
            Clés supportées :
            - 'option1' (bool): Description de l'option
            - 'option2' (int): Description de l'autre option

    Returns:
        type: Description du retour.
            Peut décrire la structure si c'est complexe.

    Raises:
        ValueError: Si param1 est invalide
        TypeError: Si les types ne correspondent pas
        CustomError: Description de l'erreur personnalisée

    Example:
        Utilisation basique :
        >>> resultat = ma_fonction("test", param2=42)
        >>> print(resultat)
        "résultat attendu"

        Avec options avancées :
        >>> resultat = ma_fonction("test", option1=True, option2=100)
        >>> isinstance(resultat, str)
        True

    Note:
        Informations importantes sur l'utilisation,
        les limitations ou les considérations de performance.

    Warning:
        Avertissements sur les risques ou effets de bord.

    See Also:
        fonction_related(): Description de la fonction liée
        autre_module.fonction(): Référence externe
    """
    pass
```

### Guide de style pour l'équipe

```markdown
# Guide de style pour la documentation

## Principes généraux

1. **Clarté avant tout** : Écrivez pour quelqu'un qui découvre le code
2. **Concision** : Soyez précis sans être verbeux
3. **Consistance** : Utilisez le même style dans tout le projet
4. **Exemples** : Incluez des exemples pratiques quand c'est utile

## Format standard

Nous utilisons le format Google pour les docstrings :

```python
def ma_fonction(param1, param2=None):
    """
    Description courte sur une ligne.

    Description détaillée optionnelle sur plusieurs lignes.

    Args:
        param1 (type): Description
        param2 (type, optional): Description. Défaut à None.

    Returns:
        type: Description du retour

    Raises:
        ErrorType: Condition d'erreur

    Example:
        >>> ma_fonction("test")
        "résultat"
    """
```

## Règles spécifiques

### Description courte
- Une seule ligne
- Commence par une majuscule
- Se termine par un point
- Utilise l'impératif ("Calcule", "Retourne", "Vérifie")

### Arguments (Args)
- Format : `nom (type): Description`
- Pour les optionnels : `nom (type, optional): Description. Défaut à valeur.`
- Types complexes : utilisez les type hints du module `typing`

### Retours (Returns)
- Format : `type: Description`
- Décrivez la structure pour les types complexes
- Omettez pour les fonctions qui ne retournent rien

### Exemples
- Utilisez la notation doctest (`>>>`)
- Montrez les cas d'usage typiques
- Incluez le résultat attendu
- Testez vos exemples avec `python -m doctest fichier.py`

### Notes et avertissements
- `Note:` pour les informations importantes
- `Warning:` pour les risques ou limitations
- `See Also:` pour les références

## Vérification

Avant de commit :
```bash
# Vérifier la documentation
python scripts/check_docs.py

# Tester les doctests
python -m doctest src/*.py

# Générer la documentation
cd docs && make html
```
```

## Exercices pratiques

### Exercice 1 : Améliorer des docstrings existantes

```python
# Exercice : Améliorez ces docstrings
def calculate_discount(price, discount_rate, max_discount=None):
    """Calculates discount"""
    # À améliorer !
    pass

class UserAccount:
    """User account"""
    # À améliorer !

    def __init__(self, username, email):
        # À documenter !
        pass

    def change_password(self, old_password, new_password):
        """Changes password"""
        # À améliorer !
        pass

# Votre mission :
# 1. Réécrivez ces docstrings selon les bonnes pratiques
# 2. Ajoutez des sections Args, Returns, Raises appropriées
# 3. Incluez des exemples d'utilisation
# 4. Documentez les cas particuliers
```

### Exercice 2 : Documentation d'une API

```python
# Exercice : Documentez complètement cette API
class TaskManager:
    def __init__(self, storage_backend="memory"):
        # TODO: Documenter
        pass

    def create_task(self, title, description="", priority=1, due_date=None):
        # TODO: Documenter
        # Cette méthode crée une nouvelle tâche
        # priority: 1=low, 2=medium, 3=high
        # Retourne l'ID de la tâche créée
        pass

    def update_task(self, task_id, **kwargs):
        # TODO: Documenter
        # Met à jour les champs spécifiés d'une tâche
        # Lève TaskNotFound si la tâche n'existe pas
        pass

    def get_tasks(self, status=None, priority=None):
        # TODO: Documenter
        # Retourne une liste de tâches filtrées
        pass

    def mark_completed(self, task_id):
        # TODO: Documenter
        pass

# Votre mission :
# 1. Ajoutez des docstrings complètes pour la classe et toutes les méthodes
# 2. Documentez les exceptions personnalisées
# 3. Créez des exemples d'utilisation de l'API
# 4. Expliquez les différents backends de stockage
```

## Résumé

La documentation avec docstrings est essentielle pour un code maintenable :

### **Points clés :**
- **Docstrings** : Documentation intégrée au code
- **Formats** : Google, NumPy, Sphinx selon les besoins
- **Contenu** : Description, Args, Returns, Raises, Examples
- **Outils** : Sphinx pour génération, doctests pour validation

### **Bonnes pratiques :**
- Écrivez pour votre futur vous et vos collègues
- Expliquez le "pourquoi", pas seulement le "quoi"
- Incluez des exemples concrets et testables
- Documentez les cas particuliers et limitations
- Maintenez la documentation à jour avec le code

### **Workflow recommandé :**
1. **Écrivez** les docstrings en même temps que le code
2. **Vérifiez** avec des outils automatiques
3. **Testez** les exemples avec doctest
4. **Générez** la documentation avec Sphinx
5. **Intégrez** les vérifications dans votre CI/CD

### **Outils essentiels :**
- Scripts de vérification automatique
- Pre-commit hooks pour la qualité
- Sphinx pour génération HTML
- Doctests pour validation des exemples

### **Pour l'équipe :**
- Guide de style partagé
- Templates standardisés
- Processus de review incluant la documentation
- Formation sur les bonnes pratiques

Une bonne documentation est un investissement qui se rentabilise rapidement. Elle facilite la maintenance, réduit les bugs, et améliore la collaboration en équipe !

Dans la section suivante, nous verrons comment maintenir la qualité du code avec PEP 8 et les outils de linting.

---

**À retenir :** Une bonne docstring, c'est comme un bon mode d'emploi : elle vous fait gagner du temps au lieu d'en perdre !

⏭️
