🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10.6 Validation de types avec mypy

## Introduction au typage en Python

### Python est dynamiquement typé

Python est un langage à **typage dynamique** : vous n'avez pas besoin de déclarer le type des variables, Python le détermine automatiquement à l'exécution.

```python
# Python devine automatiquement les types
x = 5           # x est un int
y = "hello"     # y est un str
z = [1, 2, 3]   # z est une list
```

C'est pratique pour écrire du code rapidement, mais cela peut causer des problèmes :

```python
def additionner(a, b):
    return a + b

# Ça fonctionne
print(additionner(5, 3))        # 8

# Ça fonctionne aussi (mais est-ce voulu ?)
print(additionner("Hello", " World"))  # "Hello World"

# Ça plante à l'exécution !
print(additionner(5, "3"))      # TypeError: unsupported operand type(s)
```

**Le problème** : L'erreur n'est détectée qu'à l'exécution, quand le code s'exécute.

### Les type hints : annotations de types

Python 3.5+ permet d'ajouter des **annotations de types** (type hints) pour indiquer quels types sont attendus :

```python
def additionner(a: int, b: int) -> int:
    return a + b

# Maintenant c'est clair : a et b doivent être des int
# Et la fonction retourne un int
```

**Important** : Les type hints sont **optionnels** et **ignorés par Python** à l'exécution. Ils servent de documentation et peuvent être vérifiés par des outils externes.

```python
def additionner(a: int, b: int) -> int:
    return a + b

# Python n'empêche PAS cela !
resultat = additionner("5", "3")  # Pas d'erreur à l'exécution !
```

### Qu'est-ce que mypy ?

**mypy** est un outil qui analyse votre code et vérifie que les types sont utilisés correctement, **avant** l'exécution.

**Analogie** : C'est comme un correcteur orthographique pour les types. Il vous prévient des erreurs potentielles avant que vous ne lanciez le programme.

**Avantages de mypy** :
1. **Détection précoce des bugs** : Trouve les erreurs de types avant l'exécution
2. **Documentation automatique** : Les types documentent le code
3. **Meilleure autocomplétion** : Les IDE comprennent mieux votre code
4. **Refactoring plus sûr** : Détecte les incohérences lors des modifications
5. **Code plus robuste** : Moins de bugs en production

---

## Installation et premiers pas

### Installation

```bash
# Installation avec pip
pip install mypy

# Vérifier l'installation
mypy --version
```

### Premier exemple

Créons un fichier simple avec une erreur de type :

```python
# fichier: exemple.py
def saluer(nom: str) -> str:
    """Salue une personne par son nom."""
    return f"Bonjour {nom} !"

# Utilisation correcte
message = saluer("Alice")
print(message)

# Erreur de type
nombre = saluer(42)  # ❌ 42 est un int, pas un str
```

Exécutons mypy :

```bash
$ mypy exemple.py
exemple.py:10: error: Argument 1 to "saluer" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

**mypy a détecté l'erreur !** Sans exécuter le code.

### Exécution de mypy

```bash
# Vérifier un fichier
mypy mon_fichier.py

# Vérifier un dossier
mypy mon_package/

# Vérifier avec plus de détails
mypy --show-error-codes mon_fichier.py

# Mode strict (plus de vérifications)
mypy --strict mon_fichier.py

# Ignorer les erreurs dans les bibliothèques externes
mypy --ignore-missing-imports mon_fichier.py
```

---

## Les type hints de base

### Types primitifs

Les types Python de base :

```python
# Entiers
age: int = 25
annee: int = 2024

# Flottants
prix: float = 19.99
temperature: float = -5.5

# Chaînes de caractères
nom: str = "Alice"
message: str = "Bonjour"

# Booléens
est_actif: bool = True
a_termine: bool = False

# None
resultat: None = None
```

### Fonctions avec types

Annotez les paramètres et le retour :

```python
def additionner(a: int, b: int) -> int:
    """Additionne deux entiers."""
    return a + b

def diviser(a: float, b: float) -> float:
    """Divise deux nombres."""
    return a / b

def afficher_message(message: str) -> None:
    """Affiche un message (ne retourne rien)."""
    print(message)

def obtenir_nom() -> str:
    """Demande et retourne un nom."""
    return input("Votre nom : ")
```

**Note** : `-> None` indique qu'une fonction ne retourne rien (comme `void` en C/Java).

### Variables avec annotation

```python
# Déclaration avec valeur
nom: str = "Bob"
age: int = 30

# Déclaration sans valeur (utile dans les classes)
class Personne:
    nom: str
    age: int

    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
```

---

## Types complexes avec typing

Le module `typing` fournit des types plus avancés.

### List, Dict, Set, Tuple

```python
from typing import List, Dict, Set, Tuple

# Liste d'entiers
nombres: List[int] = [1, 2, 3, 4, 5]

# Liste de chaînes
prenoms: List[str] = ["Alice", "Bob", "Charlie"]

# Dictionnaire (clés str, valeurs int)
ages: Dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

# Ensemble d'entiers
uniques: Set[int] = {1, 2, 3, 4, 5}

# Tuple de taille fixe (str, int, bool)
personne: Tuple[str, int, bool] = ("Alice", 25, True)

# Tuple de taille variable (tous des int)
coordonnees: Tuple[int, ...] = (10, 20, 30, 40)
```

**Note importante** : En Python 3.9+, vous pouvez utiliser la syntaxe simplifiée :

```python
# Python 3.9+
nombres: list[int] = [1, 2, 3]
ages: dict[str, int] = {"Alice": 25}
coordonnees: tuple[int, ...] = (10, 20)

# Plus besoin d'importer de typing !
```

### Optional : valeur ou None

`Optional[Type]` signifie "Type ou None" :

```python
from typing import Optional

def trouver_utilisateur(user_id: int) -> Optional[str]:
    """Trouve un utilisateur par son ID.

    Returns:
        Le nom de l'utilisateur, ou None si non trouvé.
    """
    utilisateurs = {1: "Alice", 2: "Bob"}
    return utilisateurs.get(user_id)

# Utilisation
nom = trouver_utilisateur(1)  # Type: Optional[str]
if nom is not None:
    print(f"Trouvé : {nom}")

# Équivalent à Optional[str]
nom: str | None = trouver_utilisateur(1)  # Python 3.10+
```

**Note** : `Optional[X]` est équivalent à `Union[X, None]`.

### Union : plusieurs types possibles

`Union[Type1, Type2]` signifie "Type1 ou Type2" :

```python
from typing import Union

def formater_valeur(valeur: Union[int, float, str]) -> str:
    """Formate une valeur en chaîne.

    Args:
        valeur: Peut être int, float ou str.

    Returns:
        La valeur formatée en chaîne.
    """
    return f"Valeur : {valeur}"

# Utilisations valides
formater_valeur(42)         # int
formater_valeur(3.14)       # float
formater_valeur("texte")    # str

# Python 3.10+ : syntaxe simplifiée avec |
def formater_valeur(valeur: int | float | str) -> str:
    return f"Valeur : {valeur}"
```

### Any : tout type accepté

`Any` accepte n'importe quel type (désactive la vérification) :

```python
from typing import Any

def traiter_donnees(donnees: Any) -> None:
    """Traite des données de type inconnu."""
    print(donnees)

# Tout est accepté
traiter_donnees(42)
traiter_donnees("texte")
traiter_donnees([1, 2, 3])
traiter_donnees({"cle": "valeur"})
```

**⚠️ Attention** : Utilisez `Any` avec parcimonie ! Cela désactive la vérification de types.

### Callable : fonctions comme paramètres

`Callable` représente une fonction appelable :

```python
from typing import Callable

def executer_operation(
    x: int,
    y: int,
    operation: Callable[[int, int], int]
) -> int:
    """Exécute une opération sur deux nombres.

    Args:
        x: Premier nombre.
        y: Deuxième nombre.
        operation: Fonction prenant 2 int et retournant un int.

    Returns:
        Le résultat de l'opération.
    """
    return operation(x, y)

# Définir des opérations
def additionner(a: int, b: int) -> int:
    return a + b

def multiplier(a: int, b: int) -> int:
    return a * b

# Utilisation
resultat1 = executer_operation(5, 3, additionner)   # 8
resultat2 = executer_operation(5, 3, multiplier)    # 15
```

**Format** : `Callable[[type_param1, type_param2], type_retour]`

---

## Types pour les collections

### Iterable, Iterator, Sequence

```python
from typing import Iterable, Iterator, Sequence

def somme(nombres: Iterable[int]) -> int:
    """Calcule la somme de nombres itérables.

    Args:
        nombres: N'importe quelle collection itérable d'entiers.

    Returns:
        La somme.
    """
    return sum(nombres)

# Fonctionne avec différents types itérables
somme([1, 2, 3])        # list
somme((1, 2, 3))        # tuple
somme({1, 2, 3})        # set
somme(range(1, 4))      # range

def premier_element(sequence: Sequence[str]) -> str:
    """Retourne le premier élément d'une séquence.

    Args:
        sequence: Une séquence (indexable) de chaînes.

    Returns:
        Le premier élément.
    """
    return sequence[0]

# Fonctionne avec des séquences
premier_element(["a", "b", "c"])    # list
premier_element(("a", "b", "c"))    # tuple
premier_element("abc")              # str
```

### Mapping : dictionnaires génériques

```python
from typing import Mapping

def compter_occurrences(texte: str) -> Mapping[str, int]:
    """Compte les occurrences de chaque caractère.

    Args:
        texte: Le texte à analyser.

    Returns:
        Dictionnaire des occurrences.
    """
    compteur: dict[str, int] = {}
    for char in texte:
        compteur[char] = compteur.get(char, 0) + 1
    return compteur
```

---

## Classes et types personnalisés

### Annoter une classe

```python
class Utilisateur:
    """Représente un utilisateur."""

    # Annotations de classe
    nom: str
    email: str
    age: int
    actif: bool

    def __init__(self, nom: str, email: str, age: int) -> None:
        """Initialise un utilisateur.

        Args:
            nom: Le nom de l'utilisateur.
            email: L'adresse email.
            age: L'âge.
        """
        self.nom = nom
        self.email = email
        self.age = age
        self.actif = True

    def desactiver(self) -> None:
        """Désactive l'utilisateur."""
        self.actif = False

    def est_majeur(self) -> bool:
        """Vérifie si l'utilisateur est majeur.

        Returns:
            True si majeur, False sinon.
        """
        return self.age >= 18

    def obtenir_info(self) -> str:
        """Retourne une chaîne d'information.

        Returns:
            Chaîne descriptive de l'utilisateur.
        """
        statut = "actif" if self.actif else "inactif"
        return f"{self.nom} ({self.email}) - {statut}"
```

### Utiliser une classe comme type

```python
def envoyer_email(utilisateur: Utilisateur, sujet: str, message: str) -> bool:
    """Envoie un email à un utilisateur.

    Args:
        utilisateur: L'utilisateur destinataire.
        sujet: Le sujet de l'email.
        message: Le contenu de l'email.

    Returns:
        True si l'email a été envoyé.
    """
    if not utilisateur.actif:
        return False

    # Envoyer l'email...
    print(f"Email envoyé à {utilisateur.email}")
    return True

# Utilisation
user = Utilisateur("Alice", "alice@example.com", 25)
envoyer_email(user, "Bienvenue", "Merci de votre inscription")
```

### TypeAlias : créer des alias de types

```python
from typing import TypeAlias

# Définir des alias pour des types complexes
UserId: TypeAlias = int
Email: TypeAlias = str
Utilisateurs: TypeAlias = dict[UserId, Utilisateur]

def obtenir_utilisateur(
    utilisateurs: Utilisateurs,
    user_id: UserId
) -> Utilisateur | None:
    """Obtient un utilisateur par son ID.

    Args:
        utilisateurs: Dictionnaire des utilisateurs.
        user_id: L'ID de l'utilisateur.

    Returns:
        L'utilisateur ou None.
    """
    return utilisateurs.get(user_id)
```

### Générics : types paramétrés

```python
from typing import TypeVar, Generic

T = TypeVar('T')  # Variable de type générique

class Boite(Generic[T]):
    """Une boîte générique pouvant contenir n'importe quel type."""

    def __init__(self, contenu: T) -> None:
        """Initialise la boîte.

        Args:
            contenu: Le contenu de type T.
        """
        self.contenu = contenu

    def obtenir(self) -> T:
        """Retourne le contenu.

        Returns:
            Le contenu de type T.
        """
        return self.contenu

    def remplacer(self, nouveau: T) -> None:
        """Remplace le contenu.

        Args:
            nouveau: Le nouveau contenu de type T.
        """
        self.contenu = nouveau

# Utilisation avec différents types
boite_int: Boite[int] = Boite(42)
nombre = boite_int.obtenir()  # Type: int

boite_str: Boite[str] = Boite("Hello")
texte = boite_str.obtenir()  # Type: str

# mypy détecte les erreurs de type
boite_int.remplacer(100)      # ✅ OK
boite_int.remplacer("texte")  # ❌ Erreur: expected int, got str
```

---

## Fonctionnalités avancées

### Literal : valeurs spécifiques

`Literal` limite les valeurs possibles :

```python
from typing import Literal

def changer_couleur(
    couleur: Literal["rouge", "vert", "bleu"]
) -> None:
    """Change la couleur.

    Args:
        couleur: Doit être "rouge", "vert" ou "bleu".
    """
    print(f"Couleur changée en {couleur}")

# Utilisations valides
changer_couleur("rouge")   # ✅ OK
changer_couleur("vert")    # ✅ OK

# Erreur détectée par mypy
changer_couleur("jaune")   # ❌ Erreur: expected Literal["rouge", "vert", "bleu"]
```

### TypedDict : dictionnaires avec structure

`TypedDict` définit la structure exacte d'un dictionnaire :

```python
from typing import TypedDict

class PersonneDict(TypedDict):
    """Structure d'un dictionnaire personne."""
    nom: str
    age: int
    email: str
    actif: bool

def creer_personne(nom: str, age: int, email: str) -> PersonneDict:
    """Crée un dictionnaire personne.

    Args:
        nom: Le nom.
        age: L'âge.
        email: L'email.

    Returns:
        Dictionnaire structuré.
    """
    return {
        "nom": nom,
        "age": age,
        "email": email,
        "actif": True
    }

def afficher_personne(personne: PersonneDict) -> None:
    """Affiche les informations d'une personne.

    Args:
        personne: Le dictionnaire personne.
    """
    print(f"{personne['nom']}, {personne['age']} ans")

# mypy vérifie la structure
personne = creer_personne("Alice", 25, "alice@example.com")
afficher_personne(personne)  # ✅ OK

# Erreur si la structure est incorrecte
mauvaise_personne = {"nom": "Bob"}  # ❌ Manque 'age', 'email', 'actif'
afficher_personne(mauvaise_personne)
```

### Final : valeurs constantes

`Final` indique qu'une valeur ne doit pas être modifiée :

```python
from typing import Final

# Constante de module
PI: Final = 3.14159
MAX_CONNEXIONS: Final[int] = 100

class Configuration:
    """Configuration de l'application."""

    # Constantes de classe
    VERSION: Final[str] = "1.0.0"
    DEBUG: Final[bool] = False

    def __init__(self) -> None:
        # Constante d'instance (ne peut pas être réassignée)
        self.app_name: Final = "MonApp"

# mypy détecte les tentatives de modification
PI = 3.14  # ❌ Erreur: Cannot assign to final name "PI"
```

### Protocol : duck typing avec types

`Protocol` définit une interface sans héritage explicite :

```python
from typing import Protocol

class Affichable(Protocol):
    """Protocole pour les objets affichables."""

    def afficher(self) -> str:
        """Retourne une représentation textuelle."""
        ...

class Utilisateur:
    """Utilisateur - implémente le protocole implicitement."""

    def __init__(self, nom: str) -> None:
        self.nom = nom

    def afficher(self) -> str:
        return f"Utilisateur: {self.nom}"

class Produit:
    """Produit - implémente aussi le protocole."""

    def __init__(self, nom: str, prix: float) -> None:
        self.nom = nom
        self.prix = prix

    def afficher(self) -> str:
        return f"Produit: {self.nom} - {self.prix}€"

def afficher_objet(obj: Affichable) -> None:
    """Affiche n'importe quel objet affichable.

    Args:
        obj: Un objet ayant une méthode afficher().
    """
    print(obj.afficher())

# Fonctionne avec n'importe quelle classe ayant afficher()
user = Utilisateur("Alice")
produit = Produit("Livre", 15.99)

afficher_objet(user)      # ✅ OK
afficher_objet(produit)   # ✅ OK
```

---

## Configuration de mypy

### Fichier mypy.ini

Créez un fichier `mypy.ini` à la racine du projet :

```ini
# fichier: mypy.ini
[mypy]
# Version Python ciblée
python_version = 3.10

# Fichiers à vérifier
files = src/

# Fichiers à ignorer
exclude = tests/|docs/|build/

# Strictness (niveau de sévérité)
warn_return_any = True
warn_unused_configs = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True

# Erreurs de type
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_calls = False

# Gestion des imports
ignore_missing_imports = False
follow_imports = normal

# Divers
strict_optional = True
strict_equality = True
show_error_codes = True
show_column_numbers = True
```

### Configuration dans pyproject.toml

Alternative moderne avec `pyproject.toml` :

```toml
# fichier: pyproject.toml
[tool.mypy]
python_version = "3.10"
files = ["src"]
exclude = ["tests", "docs", "build"]

# Strictness
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true

# Type checking
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true

# Misc
strict_optional = true
strict_equality = true
show_error_codes = true
show_column_numbers = true

# Configuration par module
[[tool.mypy.overrides]]
module = "tests.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "external_lib.*"
ignore_missing_imports = true
```

### Niveaux de strictness

```bash
# Mode normal
mypy mon_fichier.py

# Mode strict (recommandé pour nouveaux projets)
mypy --strict mon_fichier.py

# Ignorer les imports manquants
mypy --ignore-missing-imports mon_fichier.py

# Afficher les codes d'erreur
mypy --show-error-codes mon_fichier.py

# Rapport détaillé
mypy --verbose mon_fichier.py
```

---

## Gérer les erreurs mypy

### Ignorer une ligne spécifique

```python
from typing import Any

def fonction_legacy(data: Any) -> Any:
    # Ignorer cette ligne
    return data.process()  # type: ignore

# Ignorer avec raison
resultat = fonction_externe()  # type: ignore[no-untyped-call]

# Ignorer avec commentaire explicatif
valeur = calcul_complexe()  # type: ignore  # TODO: Ajouter les types
```

### Ignorer un fichier entier

```python
# mypy: ignore-errors

# Tout le fichier est ignoré par mypy
def ma_fonction():
    pass
```

### Ignorer des imports

```python
import numpy  # type: ignore
import pandas as pd  # type: ignore[import]
```

### cast : forcer un type

```python
from typing import cast

def obtenir_donnees() -> Any:
    """Retourne des données de type inconnu."""
    return {"nom": "Alice", "age": 25}

# Forcer le type (à utiliser avec précaution)
donnees = cast(dict[str, Any], obtenir_donnees())
```

---

## Cas pratique : API de gestion de tâches

Voici un exemple complet avec types :

```python
"""API de gestion de tâches avec types complets."""

from typing import Optional, List, Dict, TypedDict
from datetime import datetime
from enum import Enum


class Priorite(Enum):
    """Niveaux de priorité pour les tâches."""
    HAUTE = 1
    NORMALE = 2
    BASSE = 3


class TacheDict(TypedDict):
    """Structure d'une tâche."""
    id: int
    titre: str
    terminee: bool
    priorite: Priorite
    date_creation: datetime


class Tache:
    """Représente une tâche individuelle.

    Attributes:
        id: Identifiant unique.
        titre: Le titre de la tâche.
        terminee: État de complétion.
        priorite: Niveau de priorité.
        date_creation: Date et heure de création.
    """

    def __init__(
        self,
        id: int,
        titre: str,
        priorite: Priorite = Priorite.NORMALE
    ) -> None:
        """Initialise une nouvelle tâche.

        Args:
            id: L'identifiant unique.
            titre: Le titre de la tâche.
            priorite: Le niveau de priorité (par défaut NORMALE).

        Raises:
            ValueError: Si le titre est vide.
        """
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")

        self.id: int = id
        self.titre: str = titre
        self.terminee: bool = False
        self.priorite: Priorite = priorite
        self.date_creation: datetime = datetime.now()

    def marquer_terminee(self) -> None:
        """Marque la tâche comme terminée."""
        self.terminee = True

    def marquer_non_terminee(self) -> None:
        """Marque la tâche comme non terminée."""
        self.terminee = False

    def changer_priorite(self, nouvelle_priorite: Priorite) -> None:
        """Change la priorité de la tâche.

        Args:
            nouvelle_priorite: La nouvelle priorité.
        """
        self.priorite = nouvelle_priorite

    def to_dict(self) -> TacheDict:
        """Convertit la tâche en dictionnaire.

        Returns:
            Représentation dictionnaire de la tâche.
        """
        return {
            "id": self.id,
            "titre": self.titre,
            "terminee": self.terminee,
            "priorite": self.priorite,
            "date_creation": self.date_creation
        }


class GestionnaireTaches:
    """Gère une collection de tâches.

    Attributes:
        taches: Dictionnaire des tâches indexées par ID.
    """

    def __init__(self) -> None:
        """Initialise un nouveau gestionnaire de tâches."""
        self.taches: Dict[int, Tache] = {}
        self._prochain_id: int = 1

    def creer_tache(
        self,
        titre: str,
        priorite: Priorite = Priorite.NORMALE
    ) -> Tache:
        """Crée une nouvelle tâche.

        Args:
            titre: Le titre de la tâche.
            priorite: Le niveau de priorité.

        Returns:
            La tâche créée.

        Raises:
            ValueError: Si le titre est invalide.
        """
        tache = Tache(self._prochain_id, titre, priorite)
        self.taches[self._prochain_id] = tache
        self._prochain_id += 1
        return tache

    def obtenir_tache(self, tache_id: int) -> Optional[Tache]:
        """Obtient une tâche par son ID.

        Args:
            tache_id: L'identifiant de la tâche.

        Returns:
            La tâche correspondante, ou None si non trouvée.
        """
        return self.taches.get(tache_id)

    def supprimer_tache(self, tache_id: int) -> bool:
        """Supprime une tâche.

        Args:
            tache_id: L'identifiant de la tâche.

        Returns:
            True si la tâche a été supprimée, False sinon.
        """
        if tache_id in self.taches:
            del self.taches[tache_id]
            return True
        return False

    def lister_taches(
        self,
        seulement_non_terminees: bool = False,
        priorite: Optional[Priorite] = None
    ) -> List[Tache]:
        """Liste les tâches selon des critères.

        Args:
            seulement_non_terminees: Si True, ne retourne que
                les tâches non terminées.
            priorite: Si spécifié, filtre par priorité.

        Returns:
            Liste des tâches correspondant aux critères.
        """
        taches = list(self.taches.values())

        if seulement_non_terminees:
            taches = [t for t in taches if not t.terminee]

        if priorite is not None:
            taches = [t for t in taches if t.priorite == priorite]

        # Trier par priorité puis par date
        taches.sort(key=lambda t: (t.priorite.value, t.date_creation))

        return taches

    def compter_taches(
        self,
        seulement_non_terminees: bool = False
    ) -> int:
        """Compte le nombre de tâches.

        Args:
            seulement_non_terminees: Si True, compte seulement
                les tâches non terminées.

        Returns:
            Le nombre de tâches.
        """
        return len(self.lister_taches(seulement_non_terminees))

    def obtenir_statistiques(self) -> Dict[str, int]:
        """Calcule des statistiques sur les tâches.

        Returns:
            Dictionnaire contenant les statistiques.
        """
        total = len(self.taches)
        terminees = sum(1 for t in self.taches.values() if t.terminee)
        non_terminees = total - terminees

        return {
            "total": total,
            "terminees": terminees,
            "non_terminees": non_terminees,
            "haute_priorite": sum(
                1 for t in self.taches.values()
                if t.priorite == Priorite.HAUTE
            )
        }


# Fonction d'exemple utilisant le gestionnaire
def exemple_utilisation() -> None:
    """Exemple d'utilisation du gestionnaire de tâches."""
    gestionnaire = GestionnaireTaches()

    # Créer des tâches
    tache1 = gestionnaire.creer_tache("Faire les courses", Priorite.HAUTE)
    tache2 = gestionnaire.creer_tache("Lire un livre")
    tache3 = gestionnaire.creer_tache("Faire du sport", Priorite.BASSE)

    # Marquer une tâche comme terminée
    tache1.marquer_terminee()

    # Lister les tâches non terminées
    non_terminees: List[Tache] = gestionnaire.lister_taches(
        seulement_non_terminees=True
    )

    print(f"Tâches non terminées : {len(non_terminees)}")

    # Afficher les statistiques
    stats: Dict[str, int] = gestionnaire.obtenir_statistiques()
    print(f"Statistiques : {stats}")


if __name__ == "__main__":
    exemple_utilisation()
```

Vérification avec mypy :

```bash
$ mypy taches.py
Success: no issues found in 1 source file
```

---

## Intégration avec les outils

### VS Code

Extensions recommandées :
- **Pylance** : Type checking en temps réel
- **Python** (Microsoft) : Support complet

Configuration `settings.json` :

```json
{
    "python.analysis.typeCheckingMode": "basic",
    "python.linting.mypyEnabled": true,
    "python.linting.mypyArgs": [
        "--ignore-missing-imports",
        "--show-column-numbers"
    ]
}
```

### PyCharm

PyCharm inclut un vérificateur de types intégré.

Configuration :
1. **Settings** → **Editor** → **Inspections**
2. **Python** → **Type checker** → Activer
3. Choisir "mypy" comme vérificateur externe

### pre-commit

Ajoutez mypy à vos hooks pre-commit :

```yaml
# fichier: .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--ignore-missing-imports]
```

### GitHub Actions

Intégrez mypy dans votre CI/CD :

```yaml
# fichier: .github/workflows/type-check.yml
name: Type Checking

on: [push, pull_request]

jobs:
  mypy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install mypy
        pip install -r requirements.txt

    - name: Run mypy
      run: mypy src/
```

---

## Migration progressive vers les types

### Stratégie pour les projets existants

1. **Commencez par les nouvelles fonctions** :
   - Annotez tout nouveau code
   - Ne touchez pas l'ancien code au début

2. **Activez mypy progressivement** :
   ```bash
   # Commencez sans strictness
   mypy --ignore-missing-imports src/

   # Puis augmentez graduellement
   mypy --disallow-untyped-defs src/nouveau_module.py
   ```

3. **Un fichier à la fois** :
   ```ini
   # mypy.ini - Configuration progressive
   [mypy]

   [mypy-ancien_module.*]
   ignore_errors = True

   [mypy-nouveau_module.*]
   disallow_untyped_defs = True
   ```

4. **Utilisez `Any` temporairement** :
   ```python
   from typing import Any

   # Temporaire : annoter avec Any
   def fonction_legacy(data: Any) -> Any:
       # TODO: Typer correctement plus tard
       pass
   ```

### Ajouter des stubs pour les bibliothèques

Certaines bibliothèques n'ont pas de types. Utilisez des stubs :

```bash
# Installer les stubs (types) pour les bibliothèques populaires
pip install types-requests
pip install types-PyYAML
pip install types-redis
```

Ou créez vos propres stubs :

```python
# fichier: stubs/external_lib.pyi
def fonction_externe(param: str) -> int: ...

class ClasseExterne:
    def methode(self) -> None: ...
```

---

## Bonnes pratiques

### 1. Commencez simple

```python
# ✅ Bon - commencer simple
def calculer(x: int, y: int) -> int:
    return x + y

# ❌ Trop complexe pour commencer
def calculer(
    x: Union[int, float, Decimal],
    y: Union[int, float, Decimal],
    options: Optional[Dict[str, Any]] = None
) -> Union[int, float, Decimal]:
    pass
```

### 2. Annotez les signatures publiques

```python
class MonAPI:
    # ✅ API publique : annotée
    def methode_publique(self, param: str) -> int:
        return self._methode_privee(param)

    # Méthode privée : optionnel
    def _methode_privee(self, param):
        return len(param)
```

### 3. Préférez les types spécifiques à Any

```python
# ❌ Mauvais - trop vague
def traiter(data: Any) -> Any:
    pass

# ✅ Meilleur - plus précis
def traiter(data: dict[str, str]) -> list[int]:
    pass
```

### 4. Utilisez Optional explicitement

```python
# ✅ Clair
def trouver(id: int) -> Optional[str]:
    pass

# ❌ Moins clair
def trouver(id: int) -> str | None:  # Fonctionnellement identique
    pass
```

### 5. Documentez les types complexes

```python
# ✅ Bon - avec documentation
UserDict: TypeAlias = Dict[int, Dict[str, Any]]

def obtenir_utilisateurs() -> UserDict:
    """Retourne les utilisateurs.

    Returns:
        Dictionnaire: {user_id: {nom, email, age}}
    """
    pass

# ❌ Mauvais - type complexe non documenté
def obtenir_utilisateurs() -> Dict[int, Dict[str, Any]]:
    pass
```

### 6. Vérifiez régulièrement

```bash
# Ajoutez mypy à votre workflow quotidien
git add .
mypy src/
git commit -m "..."
```

---

## Dépannage des erreurs courantes

### Erreur : "error: Cannot determine type of..."

```python
# ❌ Problème
liste = []  # Type: List[Any] (trop vague)
liste.append(1)
liste.append("texte")  # mypy est confus

# ✅ Solution : annoter explicitement
liste: list[int] = []
liste.append(1)
```

### Erreur : "error: Incompatible types in assignment"

```python
# ❌ Problème
def obtenir_age() -> int:
    return "25"  # Erreur: str au lieu de int

# ✅ Solution : corriger le type de retour
def obtenir_age() -> int:
    return 25
```

### Erreur : "error: Missing return statement"

```python
# ❌ Problème
def calculer(x: int) -> int:
    if x > 0:
        return x
    # Manque un return pour x <= 0

# ✅ Solution : couvrir tous les cas
def calculer(x: int) -> int:
    if x > 0:
        return x
    return 0
```

### Erreur avec les bibliothèques externes

```python
# ❌ Problème
import une_lib_sans_types
result = une_lib_sans_types.fonction()  # error: Cannot find...

# ✅ Solution 1 : ignorer
import une_lib_sans_types  # type: ignore

# ✅ Solution 2 : configuration
# Dans mypy.ini :
# [mypy-une_lib_sans_types.*]
# ignore_missing_imports = True
```

---

## Résumé

### Points clés à retenir

1. **mypy vérifie les types** avant l'exécution (analyse statique)
2. **Les type hints** documentent le code et aident les outils
3. **Commencez simple** : int, str, bool, list, dict
4. **typing module** : Optional, Union, List, Dict, etc.
5. **Python 3.9+** : syntaxe simplifiée (list[int] au lieu de List[int])
6. **Configuration** : mypy.ini ou pyproject.toml
7. **Migration progressive** : un fichier à la fois
8. **type: ignore** pour ignorer des erreurs spécifiques
9. **Intégration IDE** : VSCode, PyCharm supportent mypy
10. **CI/CD** : intégrer mypy dans les tests automatiques

### Types essentiels

| Type | Usage | Exemple |
|------|-------|---------|
| `int`, `str`, `bool`, `float` | Types de base | `x: int = 5` |
| `list[T]` | Liste d'éléments de type T | `nombres: list[int]` |
| `dict[K, V]` | Dictionnaire | `ages: dict[str, int]` |
| `Optional[T]` | T ou None | `nom: Optional[str]` |
| `Union[T1, T2]` | T1 ou T2 | `valeur: int \| str` |
| `Any` | N'importe quel type | `data: Any` |
| `Callable` | Fonction | `func: Callable[[int], str]` |
| `TypedDict` | Structure de dict | `class User(TypedDict): ...` |

### Commandes utiles

```bash
# Vérifier un fichier
mypy fichier.py

# Vérifier un projet
mypy src/

# Mode strict
mypy --strict fichier.py

# Ignorer imports manquants
mypy --ignore-missing-imports fichier.py

# Afficher codes d'erreur
mypy --show-error-codes fichier.py

# Configuration
mypy --config-file mypy.ini src/
```

### Checklist mypy

- [ ] Installer mypy : `pip install mypy`
- [ ] Annoter les fonctions publiques
- [ ] Utiliser Optional pour les valeurs nullables
- [ ] Configurer mypy.ini ou pyproject.toml
- [ ] Intégrer dans l'IDE (VS Code, PyCharm)
- [ ] Ajouter à pre-commit hooks
- [ ] Intégrer dans CI/CD
- [ ] Vérifier régulièrement : `mypy src/`
- [ ] Documenter les types complexes
- [ ] Migration progressive sur projets existants

### Template de fonction typée

```python
from typing import Optional, List

def ma_fonction(
    param1: str,
    param2: int,
    param3: Optional[bool] = None
) -> List[dict[str, Any]]:
    """Description de la fonction.

    Args:
        param1: Description du paramètre 1.
        param2: Description du paramètre 2.
        param3: Description du paramètre optionnel.

    Returns:
        Liste de dictionnaires contenant les résultats.

    Raises:
        ValueError: Si param2 est négatif.
    """
    if param2 < 0:
        raise ValueError("param2 doit être positif")

    # Implémentation...
    return []
```

---

## Ressources complémentaires

- **Documentation officielle mypy** : https://mypy.readthedocs.io/
- **PEP 484** (Type Hints) : https://peps.python.org/pep-0484/
- **PEP 585** (Syntaxe moderne) : https://peps.python.org/pep-0585/
- **typing module** : https://docs.python.org/3/library/typing.html
- **Real Python - Type Checking** : https://realpython.com/python-type-checking/
- **mypy cheat sheet** : https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

**Les types rendent votre code plus robuste et plus facile à maintenir !** 🎯

⏭️ [Développement web et APIs](/11-developpement-web-et-apis/README.md)
