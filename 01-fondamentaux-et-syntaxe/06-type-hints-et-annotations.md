🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.6 Type Hints et annotations de types

## Introduction

Python est un langage à **typage dynamique** : vous n'avez pas besoin de déclarer le type de vos variables. Python le détermine automatiquement au moment de l'exécution. C'est l'une des raisons pour lesquelles Python est si facile à apprendre !

```python
# Python détermine automatiquement les types
age = 25        # int
nom = "Alice"   # str
prix = 19.99    # float
```

Cependant, cette flexibilité peut aussi être source de confusion, surtout dans les grands projets. C'est là qu'interviennent les **type hints** (indications de type).

Les type hints permettent d'**indiquer** quel type de données est attendu, sans pour autant **forcer** ce type. Ils servent de documentation et permettent aux outils de détecter des erreurs potentielles avant l'exécution.

**Point important** : Les type hints sont **complètement optionnels** en Python. Votre code fonctionnera exactement de la même manière avec ou sans eux. Ils sont là pour vous aider, vous et les autres développeurs, à comprendre le code.

---

## Pourquoi Utiliser les Type Hints ?

### Avantages

1. **Meilleure lisibilité** : Le code se documente lui-même
   ```python
   # Sans type hints
   def calculer_prix(prix, quantite, remise):
       return prix * quantite * (1 - remise)

   # Avec type hints (beaucoup plus clair !)
   def calculer_prix(prix: float, quantite: int, remise: float) -> float:
       return prix * quantite * (1 - remise)
   ```

2. **Détection d'erreurs** : Les IDE et outils comme mypy peuvent détecter des bugs avant l'exécution
   ```python
   def additionner(a: int, b: int) -> int:
       return a + b

   # L'IDE vous avertira que ce n'est pas correct
   resultat = additionner("5", "3")  # Erreur détectée !
   ```

3. **Autocomplétion améliorée** : Votre IDE sait quels attributs et méthodes suggérer

4. **Documentation vivante** : Les types sont toujours à jour, contrairement aux commentaires

5. **Refactoring plus sûr** : Changez le code en sachant que les outils détecteront les incompatibilités

### Quand les utiliser ?

- ✅ Dans les fonctions publiques (API de votre code)
- ✅ Dans les projets professionnels ou de taille moyenne/grande
- ✅ Quand vous travaillez en équipe
- ❌ Pas obligatoire pour de petits scripts personnels
- ❌ Pas nécessaire lors de l'apprentissage initial (mais bon à connaître !)

---

## Type Hints de Base

### Syntaxe pour les Variables

Depuis Python 3.6, vous pouvez annoter les variables :

```python
# Syntaxe : nom_variable: type = valeur
age: int = 25
nom: str = "Alice"
prix: float = 19.99
est_actif: bool = True
```

**Note** : Vous pouvez aussi annoter sans assigner immédiatement :

```python
age: int
nom: str

# Plus tard dans le code
age = 25
nom = "Alice"
```

### Type Hints pour les Fonctions

La syntaxe pour les fonctions :

```python
def nom_fonction(param1: type1, param2: type2) -> type_retour:
    # Code
    return valeur
```

**Exemples** :

```python
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres entiers."""
    return a + b

def saluer(nom: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {nom} !"

def afficher_message(texte: str) -> None:
    """Affiche un message (ne retourne rien)."""
    print(texte)
```

**Note** : `-> None` indique qu'une fonction ne retourne rien (ou retourne `None`).

### Types de Base

```python
def exemples_types_base():
    # Nombres entiers
    nombre: int = 42

    # Nombres décimaux
    prix: float = 19.99

    # Chaînes de caractères
    nom: str = "Alice"

    # Booléens
    est_valide: bool = True

    # None (absence de valeur)
    resultat: None = None
```

---

## Le Module `typing`

Pour des types plus complexes, Python fournit le module `typing` (disponible depuis Python 3.5).

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any
```

### List (Liste)

Pour indiquer une liste d'éléments d'un type spécifique :

```python
from typing import List

# Liste d'entiers
nombres: List[int] = [1, 2, 3, 4, 5]

# Liste de chaînes
noms: List[str] = ["Alice", "Bob", "Charlie"]

# Liste de nombres décimaux
prix: List[float] = [19.99, 29.99, 9.99]

def calculer_moyenne(notes: List[float]) -> float:
    """Calcule la moyenne d'une liste de notes."""
    return sum(notes) / len(notes)
```

**Note** : Depuis Python 3.9, vous pouvez utiliser directement `list[int]` au lieu de `List[int]` :

```python
# Python 3.9+
nombres: list[int] = [1, 2, 3, 4, 5]
```

### Dict (Dictionnaire)

Pour indiquer un dictionnaire avec types de clés et de valeurs :

```python
from typing import Dict

# Dictionnaire : clés str, valeurs int
ages: Dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

# Dictionnaire : clés str, valeurs float
prix: Dict[str, float] = {
    "pomme": 2.50,
    "banane": 1.80,
    "orange": 3.20
}

def compter_occurrences(texte: str) -> Dict[str, int]:
    """Compte les occurrences de chaque mot."""
    mots = texte.split()
    compteur: Dict[str, int] = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur
```

**Note** : Depuis Python 3.9, vous pouvez utiliser `dict[str, int]`.

### Tuple (Tuple)

Pour des tuples, vous pouvez spécifier le type de chaque élément :

```python
from typing import Tuple

# Tuple de deux éléments : str et int
personne: Tuple[str, int] = ("Alice", 25)

# Tuple de trois éléments
coordonnees: Tuple[float, float, float] = (10.5, 20.3, 5.8)

def obtenir_info() -> Tuple[str, int, str]:
    """Retourne (nom, age, ville)."""
    return "Alice", 25, "Paris"

# Pour un tuple de longueur variable avec le même type
nombres: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8)
```

**Note** : Depuis Python 3.9, vous pouvez utiliser `tuple[str, int]`.

### Set (Ensemble)

```python
from typing import Set

# Ensemble d'entiers
nombres_uniques: Set[int] = {1, 2, 3, 4, 5}

# Ensemble de chaînes
tags: Set[str] = {"python", "programming", "tutorial"}

def obtenir_lettres_uniques(texte: str) -> Set[str]:
    """Retourne l'ensemble des lettres uniques dans un texte."""
    return set(texte.lower())
```

**Note** : Depuis Python 3.9, vous pouvez utiliser `set[int]`.

---

## Optional et Union

### Optional

`Optional[Type]` signifie qu'une valeur peut être du type spécifié **ou** `None`.

```python
from typing import Optional

def chercher_utilisateur(id: int) -> Optional[str]:
    """
    Cherche un utilisateur par ID.
    Retourne le nom ou None si non trouvé.
    """
    utilisateurs = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return utilisateurs.get(id)

# Variables optionnelles
nom: Optional[str] = None  # Peut être str ou None
nom = "Alice"  # Maintenant c'est une str

age: Optional[int] = None
age = 25
```

**Note** : `Optional[Type]` est équivalent à `Union[Type, None]`.

**Python 3.10+** : Vous pouvez utiliser la syntaxe `Type | None` :

```python
def chercher_utilisateur(id: int) -> str | None:
    # ...
```

### Union

`Union[Type1, Type2, ...]` signifie qu'une valeur peut être de plusieurs types différents.

```python
from typing import Union

# Peut être int ou float
nombre: Union[int, float] = 42
nombre = 3.14  # OK aussi

def diviser(a: Union[int, float], b: Union[int, float]) -> float:
    """Divise deux nombres (entiers ou décimaux)."""
    return a / b

# Fonction qui peut retourner str ou int
def obtenir_valeur(cle: str) -> Union[str, int]:
    valeurs = {"nom": "Alice", "age": 25}
    return valeurs.get(cle, "inconnu")
```

**Python 3.10+** : Vous pouvez utiliser l'opérateur `|` :

```python
def diviser(a: int | float, b: int | float) -> float:
    return a / b
```

---

## Any et object

### Any

`Any` signifie "n'importe quel type". C'est comme ne pas mettre de type hint du tout.

```python
from typing import Any

def traiter_donnee(donnee: Any) -> Any:
    """Accepte n'importe quel type et retourne n'importe quel type."""
    # Traitement
    return donnee

# Variables de type quelconque
valeur: Any = 42
valeur = "texte"  # OK
valeur = [1, 2, 3]  # OK aussi
```

**Conseil** : Utilisez `Any` avec modération. C'est utile quand vous ne connaissez vraiment pas le type, mais trop l'utiliser annule les bénéfices des type hints.

### object

`object` est le type parent de tous les objets en Python. Contrairement à `Any`, l'IDE supposera que vous n'avez accès qu'aux méthodes de base.

```python
def afficher(valeur: object) -> None:
    """Accepte n'importe quel objet."""
    print(valeur)  # OK, print() accepte n'importe quoi
```

---

## Callable (Fonctions comme Paramètres)

`Callable` permet d'annoter des fonctions passées en paramètre.

```python
from typing import Callable

# Callable[[types_parametres], type_retour]

# Fonction sans paramètre qui retourne int
fonction1: Callable[[], int]

# Fonction avec deux int en paramètres qui retourne str
fonction2: Callable[[int, int], str]

def appliquer_operation(
    valeur: int,
    operation: Callable[[int], int]
) -> int:
    """Applique une opération à une valeur."""
    return operation(valeur)

def doubler(x: int) -> int:
    return x * 2

def tripler(x: int) -> int:
    return x * 3

resultat1 = appliquer_operation(5, doubler)  # 10
resultat2 = appliquer_operation(5, tripler)  # 15
```

### Exemple avec map et filter

```python
from typing import Callable, List

def transformer_liste(
    liste: List[int],
    fonction: Callable[[int], int]
) -> List[int]:
    """Transforme chaque élément d'une liste."""
    return [fonction(x) for x in liste]

def carre(x: int) -> int:
    return x ** 2

nombres = [1, 2, 3, 4, 5]
carres = transformer_liste(nombres, carre)
print(carres)  # [1, 4, 9, 16, 25]
```

---

## Type Aliases (Alias de Types)

Pour des types complexes répétés, vous pouvez créer des alias :

```python
from typing import List, Dict, Tuple

# Créer un alias
Vector = List[float]
Matrix = List[List[float]]
JSON = Dict[str, Any]

# Utiliser les alias
def additionner_vecteurs(v1: Vector, v2: Vector) -> Vector:
    return [a + b for a, b in zip(v1, v2)]

def traiter_json(data: JSON) -> None:
    print(data)

# Alias pour des tuples complexes
Coordonnees = Tuple[float, float, float]
Personne = Tuple[str, int, str]  # (nom, age, ville)

def calculer_distance(p1: Coordonnees, p2: Coordonnees) -> float:
    """Calcule la distance entre deux points 3D."""
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5
```

---

## TypedDict (Dictionnaires Typés)

Pour des dictionnaires avec une structure fixe, utilisez `TypedDict` :

```python
from typing import TypedDict

# Définir la structure d'un dictionnaire
class Personne(TypedDict):
    nom: str
    age: int
    ville: str

# Utiliser le type
def creer_personne(nom: str, age: int, ville: str) -> Personne:
    return {"nom": nom, "age": age, "ville": ville}

def afficher_personne(personne: Personne) -> None:
    print(f"{personne['nom']}, {personne['age']} ans, {personne['ville']}")

# L'IDE vous aidera avec l'autocomplétion
alice: Personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

afficher_personne(alice)
```

### TypedDict avec champs optionnels

```python
from typing import TypedDict, Optional

class Utilisateur(TypedDict, total=False):
    nom: str  # Obligatoire
    age: int  # Obligatoire
    email: Optional[str]  # Optionnel
    telephone: Optional[str]  # Optionnel
```

---

## Génériques (Generics)

Les génériques permettent de créer des fonctions et classes qui fonctionnent avec n'importe quel type.

### TypeVar

```python
from typing import TypeVar, List

# Créer une variable de type générique
T = TypeVar('T')

def premier_element(liste: List[T]) -> T:
    """Retourne le premier élément d'une liste, quel que soit son type."""
    return liste[0]

# Fonctionne avec n'importe quel type
nombres = [1, 2, 3]
premier = premier_element(nombres)  # Type inféré : int

mots = ["hello", "world"]
premier_mot = premier_element(mots)  # Type inféré : str
```

### Fonction générique avec plusieurs types

```python
from typing import TypeVar, Tuple

T = TypeVar('T')
U = TypeVar('U')

def creer_paire(premier: T, second: U) -> Tuple[T, U]:
    """Crée une paire de deux éléments de types potentiellement différents."""
    return (premier, second)

paire1 = creer_paire("Alice", 25)  # Tuple[str, int]
paire2 = creer_paire(3.14, True)   # Tuple[float, bool]
```

### Classes génériques

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Pile(Generic[T]):
    """Pile générique qui peut contenir n'importe quel type."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def empiler(self, item: T) -> None:
        self._items.append(item)

    def depiler(self) -> T:
        return self._items.pop()

    def est_vide(self) -> bool:
        return len(self._items) == 0

# Utilisation
pile_nombres: Pile[int] = Pile()
pile_nombres.empiler(1)
pile_nombres.empiler(2)
print(pile_nombres.depiler())  # 2

pile_mots: Pile[str] = Pile()
pile_mots.empiler("hello")
pile_mots.empiler("world")
print(pile_mots.depiler())  # "world"
```

---

## Literal (Valeurs Littérales)

`Literal` permet de spécifier des valeurs exactes acceptables :

```python
from typing import Literal

def definir_mode(mode: Literal["debug", "production"]) -> None:
    """Le mode doit être exactement 'debug' ou 'production'."""
    print(f"Mode : {mode}")

definir_mode("debug")       # OK
definir_mode("production")  # OK
# definir_mode("test")      # Erreur détectée par mypy !

# Avec des nombres
def definir_niveau(niveau: Literal[1, 2, 3]) -> None:
    print(f"Niveau : {niveau}")

definir_niveau(2)  # OK
# definir_niveau(5)  # Erreur !
```

---

## Final (Constantes)

`Final` indique qu'une variable ne devrait jamais être réassignée :

```python
from typing import Final

PI: Final = 3.14159
MAX_TENTATIVES: Final[int] = 3

# PI = 3.14  # mypy détectera cette erreur !

def utiliser_constante() -> None:
    print(f"Pi vaut {PI}")
```

---

## Type Hints pour les Attributs de Classe

```python
from typing import ClassVar

class Compteur:
    # Attribut de classe (partagé par toutes les instances)
    total: ClassVar[int] = 0

    # Attribut d'instance
    valeur: int

    def __init__(self, valeur: int) -> None:
        self.valeur = valeur
        Compteur.total += 1

    def incrementer(self) -> None:
        self.valeur += 1

c1 = Compteur(10)
c2 = Compteur(20)
print(Compteur.total)  # 2
```

---

## Type Hints avec Valeurs par Défaut

Combiner type hints et valeurs par défaut :

```python
from typing import Optional, List

def creer_liste(
    elements: Optional[List[int]] = None,
    taille: int = 10
) -> List[int]:
    """Crée une liste avec des éléments ou une liste vide."""
    if elements is None:
        return [0] * taille
    return elements

def saluer(
    nom: str = "Anonyme",
    titre: str = "M."
) -> str:
    return f"Bonjour {titre} {nom}"
```

---

## Annotations pour *args et **kwargs

```python
from typing import Any

def somme(*nombres: int) -> int:
    """Somme un nombre variable d'entiers."""
    return sum(nombres)

def afficher_infos(**infos: str) -> None:
    """Affiche des informations (clés et valeurs str)."""
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

# Avec Any pour accepter n'importe quel type
def fonction_flexible(*args: Any, **kwargs: Any) -> None:
    print(args)
    print(kwargs)
```

---

## Vérification des Types avec mypy

**mypy** est un outil qui vérifie la cohérence des type hints dans votre code.

### Installation

```bash
pip install mypy
```

### Utilisation

```bash
# Vérifier un fichier
mypy mon_script.py

# Vérifier un répertoire
mypy mon_projet/
```

### Exemple

**Fichier : `calcul.py`**
```python
def additionner(a: int, b: int) -> int:
    return a + b

resultat = additionner(5, 3)
print(resultat)

# Cette ligne provoquera une erreur mypy
resultat2 = additionner("5", "3")  # Erreur !
```

**Exécution de mypy** :
```bash
$ mypy calcul.py
calcul.py:7: error: Argument 1 to "additionner" has incompatible type "str"; expected "int"
calcul.py:7: error: Argument 2 to "additionner" has incompatible type "str"; expected "int"
```

### Configuration de mypy

Créez un fichier `mypy.ini` ou `setup.cfg` :

```ini
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

---

## Type Hints dans les Compréhensions

Vous ne pouvez pas annoter directement les compréhensions, mais vous pouvez annoter la variable résultante :

```python
from typing import List, Dict

# Compréhension de liste
carres: List[int] = [x**2 for x in range(10)]

# Compréhension de dictionnaire
ages: Dict[str, int] = {nom: age for nom, age in [("Alice", 25), ("Bob", 30)]}

# Ou annoter dans une fonction
def generer_carres(n: int) -> List[int]:
    return [x**2 for x in range(n)]
```

---

## Bonnes Pratiques

### 1. Commencez par les fonctions publiques

Annotez d'abord les fonctions qui font partie de l'API de votre code :

```python
# API publique : annotations obligatoires
def calculer_prix(prix_ht: float, quantite: int, tva: float = 0.20) -> float:
    """Calcule le prix TTC."""
    return prix_ht * quantite * (1 + tva)

# Fonction interne privée : annotations optionnelles
def _arrondir(valeur):
    return round(valeur, 2)
```

### 2. Utilisez des alias pour les types complexes

```python
from typing import Dict, List

# ❌ Difficile à lire
def traiter(data: Dict[str, List[Dict[str, int]]]) -> List[str]:
    pass

# ✅ Plus clair avec un alias
DonneesComplexes = Dict[str, List[Dict[str, int]]]

def traiter(data: DonneesComplexes) -> List[str]:
    pass
```

### 3. Évitez l'abus de Any

```python
# ❌ Trop de Any annule les bénéfices
def traiter(data: Any) -> Any:
    pass

# ✅ Soyez aussi spécifique que possible
def traiter(data: Dict[str, int]) -> List[str]:
    pass

# ✅ Si vraiment variable, utilisez Union
def traiter(data: Union[str, int, float]) -> str:
    pass
```

### 4. Préférez Optional à Union[Type, None]

```python
# ❌ Moins lisible
def chercher(id: int) -> Union[str, None]:
    pass

# ✅ Plus clair
def chercher(id: int) -> Optional[str]:
    pass

# ✅✅ Encore mieux en Python 3.10+
def chercher(id: int) -> str | None:
    pass
```

### 5. Annotez les variables quand le type n'est pas évident

```python
# Type évident : pas besoin d'annotation
nom = "Alice"
age = 25

# Type non évident : annotation utile
from typing import List, Optional

resultats: List[int] = []
utilisateur: Optional[str] = None
```

### 6. Utilisez des type hints progressivement

Vous n'avez pas besoin d'annoter tout d'un coup :

1. Commencez par les nouvelles fonctions
2. Annotez progressivement les anciennes
3. Concentrez-vous sur les parties critiques
4. Utilisez mypy pour détecter les incohérences

---

## Compatibilité avec les Anciennes Versions

### Annotations en commentaires (Python 3.5)

Si vous devez supporter des versions très anciennes :

```python
def additionner(a, b):
    # type: (int, int) -> int
    return a + b

x = 5  # type: int
```

### Annotations avec string (forward references)

Quand vous référencez une classe avant qu'elle soit définie :

```python
from typing import Optional

class Noeud:
    def __init__(self, valeur: int, suivant: Optional["Noeud"] = None):
        self.valeur = valeur
        self.suivant = suivant
```

**Python 3.7+** : Utilisez `from __future__ import annotations` pour éviter les guillemets :

```python
from __future__ import annotations
from typing import Optional

class Noeud:
    def __init__(self, valeur: int, suivant: Optional[Noeud] = None):
        self.valeur = valeur
        self.suivant = suivant
```

---

## Exemples Pratiques Complets

### Exemple 1 : Système de gestion d'utilisateurs

```python
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Utilisateur:
    id: int
    nom: str
    email: str
    age: int

class GestionnaireUtilisateurs:
    def __init__(self) -> None:
        self._utilisateurs: Dict[int, Utilisateur] = {}
        self._prochain_id: int = 1

    def ajouter_utilisateur(
        self,
        nom: str,
        email: str,
        age: int
    ) -> Utilisateur:
        """Ajoute un nouvel utilisateur."""
        utilisateur = Utilisateur(
            id=self._prochain_id,
            nom=nom,
            email=email,
            age=age
        )
        self._utilisateurs[self._prochain_id] = utilisateur
        self._prochain_id += 1
        return utilisateur

    def obtenir_utilisateur(self, id: int) -> Optional[Utilisateur]:
        """Retourne un utilisateur ou None s'il n'existe pas."""
        return self._utilisateurs.get(id)

    def lister_utilisateurs(self) -> List[Utilisateur]:
        """Retourne la liste de tous les utilisateurs."""
        return list(self._utilisateurs.values())

    def filtrer_par_age(
        self,
        age_min: int,
        age_max: int
    ) -> List[Utilisateur]:
        """Filtre les utilisateurs par tranche d'âge."""
        return [
            user for user in self._utilisateurs.values()
            if age_min <= user.age <= age_max
        ]

# Utilisation
gestionnaire = GestionnaireUtilisateurs()
alice = gestionnaire.ajouter_utilisateur("Alice", "alice@example.com", 25)
bob = gestionnaire.ajouter_utilisateur("Bob", "bob@example.com", 30)

user = gestionnaire.obtenir_utilisateur(1)
if user:
    print(f"Utilisateur trouvé : {user.nom}")

jeunes = gestionnaire.filtrer_par_age(20, 27)
print(f"Utilisateurs entre 20 et 27 ans : {len(jeunes)}")
```

### Exemple 2 : Calculateur de statistiques

```python
from typing import List, Dict, Union, Tuple
from statistics import mean, median, stdev

Nombre = Union[int, float]
Statistiques = Dict[str, Nombre]

def calculer_statistiques(donnees: List[Nombre]) -> Statistiques:
    """
    Calcule diverses statistiques sur une liste de nombres.

    Args:
        donnees: Liste de nombres (int ou float)

    Returns:
        Dictionnaire contenant les statistiques calculées

    Raises:
        ValueError: Si la liste est vide
    """
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")

    return {
        "moyenne": mean(donnees),
        "mediane": median(donnees),
        "minimum": min(donnees),
        "maximum": max(donnees),
        "ecart_type": stdev(donnees) if len(donnees) > 1 else 0.0
    }

def analyser_notes(notes: List[int]) -> Tuple[float, List[str]]:
    """
    Analyse une liste de notes et retourne la moyenne et les appréciations.

    Args:
        notes: Liste de notes (0-20)

    Returns:
        Tuple contenant (moyenne, liste d'appréciations)
    """
    stats = calculer_statistiques(notes)
    moyenne = stats["moyenne"]

    appreciations: List[str] = []
    for note in notes:
        if note >= 16:
            appreciations.append("Très bien")
        elif note >= 14:
            appreciations.append("Bien")
        elif note >= 12:
            appreciations.append("Assez bien")
        elif note >= 10:
            appreciations.append("Passable")
        else:
            appreciations.append("Insuffisant")

    return moyenne, appreciations

# Utilisation
notes_classe = [12, 15, 8, 18, 14, 11, 16, 13]
moyenne, appreciations = analyser_notes(notes_classe)
print(f"Moyenne de la classe : {moyenne:.2f}")
```

### Exemple 3 : Cache générique

```python
from typing import TypeVar, Generic, Optional, Callable
from datetime import datetime, timedelta

K = TypeVar('K')  # Type de clé
V = TypeVar('V')  # Type de valeur

class Cache(Generic[K, V]):
    """Cache générique avec expiration."""

    def __init__(self, duree_vie: int = 300) -> None:
        """
        Args:
            duree_vie: Durée de vie en secondes (défaut: 5 minutes)
        """
        self._cache: Dict[K, Tuple[V, datetime]] = {}
        self._duree_vie = timedelta(seconds=duree_vie)

    def set(self, cle: K, valeur: V) -> None:
        """Ajoute ou met à jour une entrée dans le cache."""
        self._cache[cle] = (valeur, datetime.now())

    def get(self, cle: K) -> Optional[V]:
        """
        Récupère une valeur du cache.

        Returns:
            La valeur si elle existe et n'est pas expirée, None sinon
        """
        if cle not in self._cache:
            return None

        valeur, timestamp = self._cache[cle]

        # Vérifier l'expiration
        if datetime.now() - timestamp > self._duree_vie:
            del self._cache[cle]
            return None

        return valeur

    def get_ou_calculer(
        self,
        cle: K,
        calculateur: Callable[[], V]
    ) -> V:
        """
        Récupère une valeur ou la calcule si elle n'existe pas.

        Args:
            cle: Clé de recherche
            calculateur: Fonction qui calcule la valeur si nécessaire

        Returns:
            La valeur (depuis le cache ou calculée)
        """
        valeur = self.get(cle)
        if valeur is None:
            valeur = calculateur()
            self.set(cle, valeur)
        return valeur

# Utilisation avec différents types
cache_str: Cache[str, str] = Cache()
cache_str.set("user_1", "Alice")
print(cache_str.get("user_1"))

cache_int: Cache[int, List[int]] = Cache()
cache_int.set(1, [1, 2, 3, 4, 5])
print(cache_int.get(1))
```

---

## Type Hints et Documentation

Les type hints complètent la documentation, mais ne la remplacent pas :

```python
from typing import List, Optional

def rechercher_utilisateur(
    nom: str,
    age_min: Optional[int] = None,
    age_max: Optional[int] = None
) -> List[Dict[str, Union[str, int]]]:
    """
    Recherche des utilisateurs selon des critères.

    Les type hints indiquent les types, mais la docstring explique
    la logique et les cas particuliers.

    Args:
        nom: Nom de l'utilisateur à rechercher (insensible à la casse)
        age_min: Âge minimum (inclus). Si None, pas de limite inférieure
        age_max: Âge maximum (inclus). Si None, pas de limite supérieure

    Returns:
        Liste de dictionnaires représentant les utilisateurs trouvés.
        Chaque dictionnaire contient les clés 'nom' (str) et 'age' (int).

    Examples:
        >>> rechercher_utilisateur("Alice")
        [{'nom': 'Alice', 'age': 25}]

        >>> rechercher_utilisateur("Bob", age_min=20, age_max=30)
        [{'nom': 'Bob', 'age': 28}]
    """
    # Implémentation
    pass
```

---

## Limites et Considérations

### 1. Les type hints ne sont pas forcés

Python n'empêche **pas** d'enfreindre les type hints à l'exécution :

```python
def additionner(a: int, b: int) -> int:
    return a + b

# Cela fonctionne, même si les types ne correspondent pas !
resultat = additionner("hello", "world")  # "helloworld"
```

Les type hints sont pour **les outils** (mypy, IDE), pas pour **l'interpréteur Python**.

### 2. Impact sur les performances

Les type hints ont un **impact minimal** sur les performances. Ils sont chargés au démarrage mais n'affectent pas l'exécution.

### 3. Compatibilité

- Python 3.5+ : typing basique
- Python 3.9+ : syntaxe simplifiée (list, dict, tuple au lieu de List, Dict, Tuple)
- Python 3.10+ : opérateur `|` pour Union

### 4. Courbe d'apprentissage

Les type hints ajoutent de la complexité. Pour les débutants :
- Apprenez d'abord Python sans type hints
- Ajoutez-les progressivement quand vous êtes à l'aise
- Utilisez-les dans les projets professionnels

---

## Récapitulatif

Dans cette section, nous avons appris :

✅ **Type hints de base** : int, str, float, bool
✅ **Module typing** : List, Dict, Tuple, Set, Optional, Union
✅ **Callable** : Annoter les fonctions en paramètres
✅ **Type aliases** : Simplifier les types complexes
✅ **TypedDict** : Dictionnaires avec structure fixe
✅ **Génériques** : TypeVar et Generic
✅ **Literal et Final** : Valeurs spécifiques et constantes
✅ **mypy** : Vérification statique des types
✅ **Bonnes pratiques** : Quand et comment utiliser les type hints
✅ **Exemples pratiques** : Applications concrètes

---

## Points Clés à Retenir

1. **Les type hints sont optionnels** : votre code fonctionne sans eux
2. **Ils améliorent la lisibilité** : le code se documente lui-même
3. **Ils aident les outils** : IDE, mypy détectent les erreurs
4. **Ne sont pas forcés à l'exécution** : Python reste dynamique
5. **Utilisez-les progressivement** : commencez par les fonctions publiques
6. **mypy vérifie la cohérence** : installez-le pour un feedback
7. **La syntaxe évolue** : Python 3.9+ a une syntaxe simplifiée
8. **Documentez quand même** : type hints ≠ documentation complète

---

## Pour Aller Plus Loin

Les type hints sont maintenant un standard dans le code Python professionnel. Ils :
- Facilitent la collaboration en équipe
- Réduisent les bugs en détectant les erreurs tôt
- Rendent le code plus maintenable
- Améliorent l'expérience de développement avec l'IDE

Bien qu'optionnels, ils sont devenus une **bonne pratique** largement adoptée dans l'industrie.

---

Vous maîtrisez maintenant les type hints et annotations de types ! Vous avez terminé le chapitre 1 sur les fondamentaux de Python. Dans la section suivante, nous explorerons en détail les structures de données avancées de Python.


⏭️ [Structures de données avancées](/02-structures-de-donnees/README.md)
