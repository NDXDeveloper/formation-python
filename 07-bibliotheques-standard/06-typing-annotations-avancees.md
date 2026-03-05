🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.6 Le module typing - Annotations avancées

## Introduction

Python est un langage à typage dynamique, ce qui signifie qu'on n'a pas besoin de déclarer le type des variables. Cependant, depuis Python 3.5, il est possible d'ajouter des **annotations de type** pour indiquer quel type de données une variable, un paramètre ou une valeur de retour devrait avoir.

Les annotations de type offrent plusieurs avantages :
- **Meilleure lisibilité** : Le code est plus clair et auto-documenté
- **Détection d'erreurs précoce** : Les outils peuvent détecter des erreurs avant l'exécution
- **Meilleur support IDE** : Autocomplétion et vérification en temps réel
- **Documentation automatique** : Les types servent de documentation

**Important** : Les annotations de type ne changent pas le comportement de Python à l'exécution. Ce sont des "indices" pour les développeurs et les outils d'analyse.

---

## Annotations de type basiques

### Variables simples

```python
# Sans annotation (ancien style)
nom = "Alice"  
age = 25  
prix = 19.99  

# Avec annotations de type
nom: str = "Alice"  
age: int = 25  
prix: float = 19.99  
actif: bool = True  

# Python n'applique PAS ces types à l'exécution
age: int = 25  
age = "vingt-cinq"  # Pas d'erreur à l'exécution, mais les outils signaleront un problème  
```

### Fonctions

```python
# Annotations pour les paramètres et la valeur de retour
def saluer(nom: str) -> str:
    """Retourne un message de salutation"""
    return f"Bonjour {nom}!"

def additionner(a: int, b: int) -> int:
    """Additionne deux nombres"""
    return a + b

def afficher_info(nom: str, age: int) -> None:
    """Affiche des informations (ne retourne rien)"""
    print(f"{nom} a {age} ans")

# Utilisation
resultat: str = saluer("Alice")  
somme: int = additionner(5, 3)  
afficher_info("Bob", 30)  
```

---

## Le module `typing` - Types avancés

Le module `typing` fournit des types plus complexes pour annoter des structures de données sophistiquées.

### Import du module

Depuis **Python 3.10+**, la plupart des types de collections peuvent être utilisés directement sans import :

```python
# ✅ Python 3.10+ : types natifs (pas besoin d'import)
nombres: list[int] = [1, 2, 3]  
ages: dict[str, int] = {"Alice": 25}  
coord: tuple[float, float] = (48.8, 2.3)  
tags: set[str] = {"python", "dev"}  

# ✅ Python 3.10+ : union avec |
valeur: int | str = 42  
resultat: str | None = None  # remplace Optional[str]  

# Pour les types avancés, on importe encore depuis typing
from typing import Any, Callable, TypeVar, Generic, Protocol, Literal, Final
```

> **Note historique :** Avant Python 3.9, il fallait importer `List`, `Dict`, `Tuple`, `Set` depuis `typing`. Avant Python 3.10, il fallait utiliser `Union` et `Optional`. Ces formes fonctionnent encore mais sont considérées comme **obsolètes**.

---

## Types de collections

### list - Listes

```python
# Liste d'entiers
nombres: list[int] = [1, 2, 3, 4, 5]

# Liste de chaînes
prenoms: list[str] = ["Alice", "Bob", "Charlie"]

# Liste de listes
matrice: list[list[int]] = [[1, 2], [3, 4], [5, 6]]

def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes"""
    return sum(notes) / len(notes)
```

### dict - Dictionnaires

```python
# Dictionnaire avec clés string et valeurs int
ages: dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

# Dictionnaire avec clés int et valeurs string
codes: dict[int, str] = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
}

# Dictionnaire imbriqué
utilisateurs: dict[str, dict[str, str]] = {
    "alice": {"email": "alice@example.com", "ville": "Paris"},
    "bob": {"email": "bob@example.com", "ville": "Lyon"}
}

def compter_occurrences(mots: list[str]) -> dict[str, int]:
    """Compte les occurrences de chaque mot"""
    compteur: dict[str, int] = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur
```

### tuple - Tuples

```python
# Tuple de taille fixe avec types spécifiques
coordonnees: tuple[float, float] = (48.8566, 2.3522)

# Tuple avec types différents
personne: tuple[str, int, bool] = ("Alice", 25, True)

# Tuple de longueur variable (tous du même type)
nombres: tuple[int, ...] = (1, 2, 3, 4, 5)

def diviser(a: int, b: int) -> tuple[int, int]:
    """Retourne le quotient et le reste"""
    return a // b, a % b

quotient, reste = diviser(10, 3)
```

### set - Ensembles

```python
# Ensemble d'entiers
nombres_uniques: set[int] = {1, 2, 3, 4, 5}

# Ensemble de chaînes
tags: set[str] = {"python", "programmation", "tutorial"}

def obtenir_elements_uniques(items: list[str]) -> set[str]:
    """Retourne les éléments uniques d'une liste"""
    return set(items)
```

---

## Union et valeurs optionnelles

### L'opérateur `|` - Plusieurs types possibles

Depuis Python 3.10, l'opérateur `|` permet d'indiquer qu'une valeur peut être de plusieurs types (PEP 604).

```python
# Peut être int ou float
nombre: int | float = 42  
nombre = 3.14  # OK aussi  

# Peut être str, int ou None
identifiant: str | int | None = "ABC123"  
identifiant = 12345  
identifiant = None  

def traiter_donnee(valeur: int | str | float) -> str:
    """Traite différents types de données"""
    if isinstance(valeur, int):
        return f"Entier: {valeur}"
    elif isinstance(valeur, float):
        return f"Flottant: {valeur:.2f}"
    else:
        return f"Chaîne: {valeur}"

print(traiter_donnee(42))        # Entier: 42  
print(traiter_donnee(3.14))      # Flottant: 3.14  
print(traiter_donnee("test"))    # Chaîne: test  
```

### Valeur ou None (`X | None`)

Pour indiquer qu'une valeur peut être d'un type donné ou `None`, on utilise `X | None` :

```python
# Variable qui peut être str ou None
nom: str | None = None  
nom = "Alice"  # OK  
nom = None     # OK aussi  

def trouver_utilisateur(id: int) -> str | None:
    """Cherche un utilisateur par ID, retourne None si introuvable"""
    utilisateurs = {1: "Alice", 2: "Bob"}
    return utilisateurs.get(id)

resultat: str | None = trouver_utilisateur(1)  
if resultat is not None:  
    print(f"Utilisateur trouvé: {resultat}")
else:
    print("Utilisateur introuvable")
```

> **Note historique :** Avant Python 3.10, on utilisait `Union[X, Y]` et `Optional[X]` depuis le module `typing`. `Optional[X]` était équivalent à `Union[X, None]`. Ces formes fonctionnent encore mais `X | Y` est la syntaxe recommandée.

---

## Any - Type quelconque

`Any` indique qu'une valeur peut être de n'importe quel type. À utiliser avec parcimonie.

```python
from typing import Any

# Accepte n'importe quel type
valeur: Any = 42  
valeur = "texte"  
valeur = [1, 2, 3]  
valeur = {"clé": "valeur"}  

def afficher(valeur: Any) -> None:
    """Affiche n'importe quelle valeur"""
    print(valeur)

# À éviter quand possible, préférer des types plus spécifiques
def traiter_json(data: Any) -> Any:
    """Traite des données JSON (type inconnu)"""
    return data
```

---

## Type Aliases - Alias de types

Les alias permettent de donner des noms significatifs à des types complexes.

```python
from typing import TypeAlias

# Alias pour des types simples
UserId: TypeAlias = int  
Email: TypeAlias = str  

# Alias pour des types complexes
Coordonnees: TypeAlias = tuple[float, float]  
Utilisateur: TypeAlias = dict[str, str]  
ListeUtilisateurs: TypeAlias = list[Utilisateur]  

# Utilisation
def creer_utilisateur(id: UserId, email: Email) -> Utilisateur:
    """Crée un utilisateur"""
    return {"id": str(id), "email": email}

def obtenir_position() -> Coordonnees:
    """Retourne des coordonnées GPS"""
    return (48.8566, 2.3522)

users: ListeUtilisateurs = [
    {"nom": "Alice", "email": "alice@example.com"},
    {"nom": "Bob", "email": "bob@example.com"}
]
```

> **Note :** `TypeAlias` rend l'intention explicite — sans lui, `UserId = int` pourrait être confondu avec une simple variable.

---

## Callable - Types de fonctions

`Callable` est utilisé pour annoter des fonctions comme paramètres ou valeurs de retour.

```python
from typing import Callable

# Fonction qui prend deux int et retourne un int
Operation = Callable[[int, int], int]

def additionner(a: int, b: int) -> int:
    return a + b

def multiplier(a: int, b: int) -> int:
    return a * b

def appliquer_operation(a: int, b: int, operation: Operation) -> int:
    """Applique une opération sur deux nombres"""
    return operation(a, b)

# Utilisation
resultat = appliquer_operation(5, 3, additionner)    # 8  
resultat = appliquer_operation(5, 3, multiplier)     # 15  

# Fonction sans paramètres qui retourne str
GenerateurMessage = Callable[[], str]

def dire_bonjour() -> str:
    return "Bonjour!"

def executer_generateur(gen: GenerateurMessage) -> None:
    print(gen())

executer_generateur(dire_bonjour)  # Bonjour!

# Fonction avec paramètres variables
Transformateur = Callable[[str], str]

def mettre_en_majuscules(texte: str) -> str:
    return texte.upper()

def appliquer_transformation(textes: list[str],
                            transform: Transformateur) -> list[str]:
    """Applique une transformation à une liste de textes"""
    return [transform(texte) for texte in textes]

mots = ["bonjour", "monde"]  
resultat = appliquer_transformation(mots, mettre_en_majuscules)  
print(resultat)  # ['BONJOUR', 'MONDE']  
```

---

## TypeVar - Variables de type génériques

`TypeVar` permet de créer des types génériques qui peuvent être réutilisés.

```python
from typing import TypeVar

# Créer une variable de type
T = TypeVar('T')

def premier_element(liste: list[T]) -> T:
    """Retourne le premier élément d'une liste (de n'importe quel type)"""
    return liste[0]

# Le type de retour correspond au type de la liste
nombres: list[int] = [1, 2, 3]  
premier: int = premier_element(nombres)  # Type inféré: int  

mots: list[str] = ["a", "b", "c"]  
premier_mot: str = premier_element(mots)  # Type inféré: str  

# Avec contraintes de type
Numerique = TypeVar('Numerique', int, float)

def doubler(valeur: Numerique) -> Numerique:
    """Double un nombre (int ou float)"""
    return valeur * 2

print(doubler(5))      # 10 (int)  
print(doubler(3.14))   # 6.28 (float)  
# doubler("text")  # Erreur de type!

# Avec borne supérieure
T = TypeVar('T', bound=str)

def concatener(items: list[T]) -> T:
    """Concatène des éléments (doivent être des strings ou sous-classes)"""
    return items[0].__class__(''.join(items))
```

---

## Generic - Classes génériques

Les classes génériques permettent de créer des classes paramétrées par un type.

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Pile(Generic[T]):
    """Pile générique qui peut contenir n'importe quel type"""

    def __init__(self) -> None:
        self.items: list[T] = []

    def empiler(self, item: T) -> None:
        """Ajoute un élément sur la pile"""
        self.items.append(item)

    def depiler(self) -> T | None:
        """Retire et retourne l'élément au sommet"""
        if self.items:
            return self.items.pop()
        return None

    def est_vide(self) -> bool:
        """Vérifie si la pile est vide"""
        return len(self.items) == 0

    def taille(self) -> int:
        """Retourne la taille de la pile"""
        return len(self.items)

# Utilisation avec différents types
pile_entiers: Pile[int] = Pile[int]()  
pile_entiers.empiler(1)  
pile_entiers.empiler(2)  
pile_entiers.empiler(3)  
print(pile_entiers.depiler())  # 3  

pile_strings: Pile[str] = Pile[str]()  
pile_strings.empiler("a")  
pile_strings.empiler("b")  
print(pile_strings.depiler())  # "b"  
```

### Exemple pratique : Cache générique

```python
from typing import Generic, TypeVar  
from datetime import datetime, timedelta  

K = TypeVar('K')  # Type de la clé  
V = TypeVar('V')  # Type de la valeur  

class Cache(Generic[K, V]):
    """Cache générique avec expiration"""

    def __init__(self, duree_expiration: int = 300) -> None:
        """
        Args:
            duree_expiration: Durée en secondes avant expiration
        """
        self.donnees: dict[K, tuple[V, datetime]] = {}
        self.duree_expiration = timedelta(seconds=duree_expiration)

    def ajouter(self, cle: K, valeur: V) -> None:
        """Ajoute une valeur au cache"""
        self.donnees[cle] = (valeur, datetime.now())

    def obtenir(self, cle: K) -> V | None:
        """Récupère une valeur du cache si elle n'a pas expiré"""
        if cle not in self.donnees:
            return None

        valeur, timestamp = self.donnees[cle]

        # Vérifier l'expiration
        if datetime.now() - timestamp > self.duree_expiration:
            del self.donnees[cle]
            return None

        return valeur

    def supprimer(self, cle: K) -> None:
        """Supprime une entrée du cache"""
        if cle in self.donnees:
            del self.donnees[cle]

    def nettoyer_expires(self) -> int:
        """Supprime les entrées expirées, retourne le nombre supprimé"""
        cles_a_supprimer = []

        for cle, (_, timestamp) in self.donnees.items():
            if datetime.now() - timestamp > self.duree_expiration:
                cles_a_supprimer.append(cle)

        for cle in cles_a_supprimer:
            del self.donnees[cle]

        return len(cles_a_supprimer)

# Utilisation
cache_users: Cache[int, str] = Cache[int, str](duree_expiration=60)  
cache_users.ajouter(1, "Alice")  
cache_users.ajouter(2, "Bob")  

utilisateur = cache_users.obtenir(1)  
print(f"Utilisateur: {utilisateur}")  

# Cache pour des données différentes
cache_config: Cache[str, dict] = Cache[str, dict](duree_expiration=300)  
cache_config.ajouter("db", {"host": "localhost", "port": 5432})  
config = cache_config.obtenir("db")  
```

---

## Literal - Valeurs littérales

`Literal` permet de spécifier des valeurs exactes autorisées.

```python
from typing import Literal

# Seulement ces valeurs spécifiques sont autorisées
Mode = Literal["lecture", "ecriture", "ajout"]

def ouvrir_fichier(nom: str, mode: Mode) -> None:
    """Ouvre un fichier avec un mode spécifique"""
    print(f"Ouverture de {nom} en mode {mode}")

ouvrir_fichier("data.txt", "lecture")  # OK  
ouvrir_fichier("data.txt", "ecriture")  # OK  
# ouvrir_fichier("data.txt", "modifier")  # Erreur de type!

# Avec plusieurs types
Statut = Literal["actif", "inactif", "suspendu"]  
Code = Literal[200, 404, 500]  

def traiter_reponse(code: Code) -> str:
    """Traite un code de réponse HTTP"""
    if code == 200:
        return "Succès"
    elif code == 404:
        return "Non trouvé"
    else:
        return "Erreur serveur"

# Exemple pratique : système de permissions
from typing import Literal

Permission = Literal["lecture", "ecriture", "suppression", "admin"]

class Utilisateur:
    def __init__(self, nom: str, permission: Permission) -> None:
        self.nom = nom
        self.permission = permission

    def peut_ecrire(self) -> bool:
        return self.permission in ("ecriture", "admin")

    def peut_supprimer(self) -> bool:
        return self.permission in ("suppression", "admin")

user1 = Utilisateur("Alice", "admin")  
user2 = Utilisateur("Bob", "lecture")  
```

---

## Final - Constantes

`Final` indique qu'une variable ne doit pas être réassignée.

```python
from typing import Final

# Constante qui ne doit jamais changer
PI: Final = 3.14159  
MAX_TENTATIVES: Final[int] = 3  
API_KEY: Final[str] = "secret_key_123"  

# Ceci devrait être signalé comme une erreur par les outils de type checking
# PI = 3.14  # Erreur!

class Configuration:
    """Configuration de l'application"""

    # Constantes de classe
    MAX_CONNEXIONS: Final[int] = 100
    TIMEOUT: Final[float] = 30.0
    VERSION: Final[str] = "1.0.0"

    def __init__(self) -> None:
        # Constante d'instance (ne peut être changée après initialisation)
        self.id: Final[str] = "config_123"

config = Configuration()
# config.id = "autre"  # Erreur!
```

---

## Protocol - Duck Typing structurel

`Protocol` permet de définir des interfaces basées sur la structure plutôt que sur l'héritage.

```python
from typing import Protocol

class Drawable(Protocol):
    """Protocol pour les objets dessinables"""

    def draw(self) -> str:
        """Dessine l'objet"""
        ...

class Circle:
    """Cercle (implémente implicitement Drawable)"""

    def __init__(self, rayon: float) -> None:
        self.rayon = rayon

    def draw(self) -> str:
        return f"Cercle de rayon {self.rayon}"

class Square:
    """Carré (implémente implicitement Drawable)"""

    def __init__(self, cote: float) -> None:
        self.cote = cote

    def draw(self) -> str:
        return f"Carré de côté {self.cote}"

def dessiner_forme(forme: Drawable) -> None:
    """Dessine n'importe quelle forme qui implémente draw()"""
    print(forme.draw())

# Utilisation
cercle = Circle(5)  
carre = Square(10)  

dessiner_forme(cercle)  # OK  
dessiner_forme(carre)   # OK  

# Pas besoin d'héritage explicite!
```

### Exemple pratique : Protocol pour un système de stockage

```python
from typing import Protocol

class Stockage(Protocol):
    """Protocol pour un système de stockage"""

    def sauvegarder(self, cle: str, valeur: str) -> bool:
        """Sauvegarde une valeur"""
        ...

    def charger(self, cle: str) -> str | None:
        """Charge une valeur"""
        ...

    def supprimer(self, cle: str) -> bool:
        """Supprime une valeur"""
        ...

class StockageFichier:
    """Stockage dans des fichiers"""

    def sauvegarder(self, cle: str, valeur: str) -> bool:
        with open(f"{cle}.txt", "w", encoding="utf-8") as f:
            f.write(valeur)
        return True

    def charger(self, cle: str) -> str | None:
        try:
            with open(f"{cle}.txt", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def supprimer(self, cle: str) -> bool:
        import os
        try:
            os.remove(f"{cle}.txt")
            return True
        except FileNotFoundError:
            return False

class StockageMemoire:
    """Stockage en mémoire"""

    def __init__(self) -> None:
        self.donnees: dict[str, str] = {}

    def sauvegarder(self, cle: str, valeur: str) -> bool:
        self.donnees[cle] = valeur
        return True

    def charger(self, cle: str) -> str | None:
        return self.donnees.get(cle)

    def supprimer(self, cle: str) -> bool:
        if cle in self.donnees:
            del self.donnees[cle]
            return True
        return False

# Fonction qui accepte n'importe quel stockage
def traiter_donnees(stockage: Stockage, cle: str, valeur: str) -> None:
    """Traite des données avec n'importe quel système de stockage"""
    if stockage.sauvegarder(cle, valeur):
        print(f"Sauvegarde réussie: {cle}")

        donnee = stockage.charger(cle)
        if donnee:
            print(f"Chargé: {donnee}")

# Les deux implémentations fonctionnent
stockage_fichier = StockageFichier()  
stockage_memoire = StockageMemoire()  

traiter_donnees(stockage_fichier, "test", "valeur")  
traiter_donnees(stockage_memoire, "test", "valeur")  
```

---

## NewType - Créer de nouveaux types

`NewType` crée un type distinct pour éviter les confusions entre types similaires.

```python
from typing import NewType

# Créer de nouveaux types basés sur des types existants
UserId = NewType('UserId', int)  
ProductId = NewType('ProductId', int)  

def obtenir_utilisateur(user_id: UserId) -> str:
    """Obtient un utilisateur par son ID"""
    return f"User #{user_id}"

def obtenir_produit(product_id: ProductId) -> str:
    """Obtient un produit par son ID"""
    return f"Product #{product_id}"

# Utilisation
user_id = UserId(123)  
product_id = ProductId(456)  

print(obtenir_utilisateur(user_id))    # OK
# print(obtenir_utilisateur(product_id))  # Erreur de type!

# Même si les deux sont des int, ils sont traités différemment
# Ceci évite les erreurs de confusion

# Exemple pratique : système financier
from typing import NewType

Euro = NewType('Euro', float)  
Dollar = NewType('Dollar', float)  

def ajouter_euros(montant1: Euro, montant2: Euro) -> Euro:
    """Additionne deux montants en euros"""
    return Euro(montant1 + montant2)

prix1 = Euro(10.5)  
prix2 = Euro(5.25)  
total = ajouter_euros(prix1, prix2)  

prix_dollar = Dollar(15.0)
# total = ajouter_euros(prix1, prix_dollar)  # Erreur!
```

---

## @overload - Surcharge de signatures

`@overload` permet de définir plusieurs signatures pour une même fonction.

```python
from typing import overload

@overload
def traiter(valeur: int) -> int:
    ...

@overload
def traiter(valeur: str) -> str:
    ...

def traiter(valeur: int | str) -> int | str:
    """Traite une valeur selon son type"""
    if isinstance(valeur, int):
        return valeur * 2
    else:
        return valeur.upper()

# Les IDEs et type checkers comprennent que:
resultat_int: int = traiter(5)        # Type de retour: int  
resultat_str: str = traiter("hello")  # Type de retour: str  

# Exemple plus complexe
@overload
def obtenir_elements(indices: int) -> str:
    """Obtient un seul élément"""
    ...

@overload
def obtenir_elements(indices: list[int]) -> list[str]:
    """Obtient plusieurs éléments"""
    ...

def obtenir_elements(indices: int | list[int]) -> str | list[str]:
    """Obtient un ou plusieurs éléments d'une liste"""
    elements = ["a", "b", "c", "d", "e"]

    if isinstance(indices, int):
        return elements[indices]
    else:
        return [elements[i] for i in indices]

# Utilisation
element: str = obtenir_elements(0)           # "a"  
multiples: list[str] = obtenir_elements([0, 2, 4])  # ["a", "c", "e"]  
```

---

## Exemple complet : Système de gestion de tâches

```python
from typing import Literal, Protocol, TypeAlias  
from dataclasses import dataclass, field  
from datetime import datetime  

# Type aliases pour plus de clarté
TaskId: TypeAlias = int  
UserId: TypeAlias = int  
Priorite = Literal["basse", "moyenne", "haute", "critique"]  
Statut = Literal["a_faire", "en_cours", "terminee", "annulee"]  

@dataclass
class Tache:
    """Représente une tâche"""
    id: TaskId
    titre: str
    description: str
    priorite: Priorite
    statut: Statut
    assignee_id: UserId | None = None
    date_creation: datetime = field(default_factory=datetime.now)
    date_echeance: datetime | None = None

    def est_en_retard(self) -> bool:
        """Vérifie si la tâche est en retard"""
        if self.date_echeance and self.statut != "terminee":
            return datetime.now() > self.date_echeance
        return False

    def peut_etre_assignee(self) -> bool:
        """Vérifie si la tâche peut être assignée"""
        return self.statut in ("a_faire", "en_cours")

class Notificateur(Protocol):
    """Protocol pour les systèmes de notification"""

    def envoyer(self, destinataire: UserId, message: str) -> bool:
        """Envoie une notification"""
        ...

class NotificateurEmail:
    """Notificateur par email"""

    def envoyer(self, destinataire: UserId, message: str) -> bool:
        print(f"📧 Email envoyé à l'utilisateur {destinataire}: {message}")
        return True

class NotificateurSMS:
    """Notificateur par SMS"""

    def envoyer(self, destinataire: UserId, message: str) -> bool:
        print(f"📱 SMS envoyé à l'utilisateur {destinataire}: {message}")
        return True

class GestionnaireTaches:
    """Gestionnaire de tâches avec annotations de type complètes"""

    def __init__(self, notificateur: Notificateur) -> None:
        self.taches: dict[TaskId, Tache] = {}
        self.compteur_id: TaskId = 0
        self.notificateur = notificateur

    def creer_tache(
        self,
        titre: str,
        description: str,
        priorite: Priorite,
        assignee_id: UserId | None = None,
        date_echeance: datetime | None = None
    ) -> Tache:
        """Crée une nouvelle tâche"""
        self.compteur_id += 1

        tache = Tache(
            id=self.compteur_id,
            titre=titre,
            description=description,
            priorite=priorite,
            statut="a_faire",
            assignee_id=assignee_id,
            date_echeance=date_echeance
        )

        self.taches[tache.id] = tache

        # Notifier si assignée
        if assignee_id:
            self.notificateur.envoyer(
                assignee_id,
                f"Nouvelle tâche assignée: {titre}"
            )

        return tache

    def obtenir_tache(self, task_id: TaskId) -> Tache | None:
        """Récupère une tâche par son ID"""
        return self.taches.get(task_id)

    def modifier_statut(self, task_id: TaskId, nouveau_statut: Statut) -> bool:
        """Modifie le statut d'une tâche"""
        tache = self.obtenir_tache(task_id)

        if not tache:
            return False

        ancien_statut = tache.statut
        tache.statut = nouveau_statut

        # Notifier si terminée
        if nouveau_statut == "terminee" and tache.assignee_id:
            self.notificateur.envoyer(
                tache.assignee_id,
                f"Tâche terminée: {tache.titre}"
            )

        return True

    def assigner_tache(self, task_id: TaskId, user_id: UserId) -> bool:
        """Assigne une tâche à un utilisateur"""
        tache = self.obtenir_tache(task_id)

        if not tache or not tache.peut_etre_assignee():
            return False

        tache.assignee_id = user_id

        self.notificateur.envoyer(
            user_id,
            f"Tâche assignée: {tache.titre}"
        )

        return True

    def lister_taches_par_statut(self, statut: Statut) -> list[Tache]:
        """Liste toutes les tâches avec un statut donné"""
        return [t for t in self.taches.values() if t.statut == statut]

    def lister_taches_par_priorite(self, priorite: Priorite) -> list[Tache]:
        """Liste toutes les tâches avec une priorité donnée"""
        return [t for t in self.taches.values() if t.priorite == priorite]

    def lister_taches_en_retard(self) -> list[Tache]:
        """Liste toutes les tâches en retard"""
        return [t for t in self.taches.values() if t.est_en_retard()]

    def obtenir_statistiques(self) -> dict[str, int]:
        """Retourne des statistiques sur les tâches"""
        stats: dict[str, int] = {
            "total": len(self.taches),
            "a_faire": 0,
            "en_cours": 0,
            "terminee": 0,
            "annulee": 0,
            "en_retard": 0
        }

        for tache in self.taches.values():
            stats[tache.statut] += 1
            if tache.est_en_retard():
                stats["en_retard"] += 1

        return stats

# Démonstration
def main() -> None:
    """Fonction principale de démonstration"""
    print("=== Système de Gestion de Tâches ===\n")

    # Créer le gestionnaire avec notifications par email
    notificateur: Notificateur = NotificateurEmail()
    gestionnaire = GestionnaireTaches(notificateur)

    # Créer des tâches
    tache1 = gestionnaire.creer_tache(
        titre="Implémenter l'API",
        description="Créer les endpoints REST",
        priorite="haute",
        assignee_id=1
    )

    tache2 = gestionnaire.creer_tache(
        titre="Écrire les tests",
        description="Tests unitaires et d'intégration",
        priorite="moyenne",
        assignee_id=2
    )

    tache3 = gestionnaire.creer_tache(
        titre="Documentation",
        description="Rédiger la documentation technique",
        priorite="basse"
    )

    print(f"\n✅ {tache1.titre} créée (ID: {tache1.id})")
    print(f"✅ {tache2.titre} créée (ID: {tache2.id})")
    print(f"✅ {tache3.titre} créée (ID: {tache3.id})")

    # Modifier les statuts
    gestionnaire.modifier_statut(tache1.id, "en_cours")
    gestionnaire.modifier_statut(tache2.id, "terminee")

    # Assigner une tâche
    gestionnaire.assigner_tache(tache3.id, 1)

    # Afficher les statistiques
    stats = gestionnaire.obtenir_statistiques()
    print("\n📊 Statistiques:")
    for cle, valeur in stats.items():
        print(f"  {cle}: {valeur}")

    # Lister les tâches par statut
    taches_en_cours: list[Tache] = gestionnaire.lister_taches_par_statut("en_cours")
    print(f"\n🔄 Tâches en cours: {len(taches_en_cours)}")
    for tache in taches_en_cours:
        print(f"  - {tache.titre}")

if __name__ == "__main__":
    main()
```

---

## Vérification de types avec mypy

`mypy` est un outil de vérification statique de types pour Python.

### Installation

```bash
pip install mypy
```

### Utilisation

```python
# fichier: exemple.py
def additionner(a: int, b: int) -> int:
    return a + b

resultat: int = additionner(5, 3)  
resultat_erreur: str = additionner(5, 3)  # Erreur de type!  
```

```bash
# Vérifier le fichier
mypy exemple.py

# Sortie:
# exemple.py:5: error: Incompatible types in assignment (expression has type "int", variable has type "str")
```

### Configuration mypy

Créer un fichier `mypy.ini` :

```ini
[mypy]
python_version = 3.10  
warn_return_any = True  
warn_unused_configs = True  
disallow_untyped_defs = True  
disallow_any_unimported = False  
no_implicit_optional = True  
warn_redundant_casts = True  
warn_unused_ignores = True  
warn_no_return = True  
check_untyped_defs = True  
```

---

## Bonnes pratiques

### 1. Annoter les fonctions publiques

```python
# ✅ Bon : fonctions publiques annotées
def calculer_moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)

# ❌ Éviter : pas d'annotations
def calculer_moyenne(notes):
    return sum(notes) / len(notes)
```

### 2. Indiquer clairement quand None est possible

```python
# ✅ Bon : indiquer clairement que None est possible
def trouver_element(liste: list[int], valeur: int) -> int | None:
    try:
        return liste.index(valeur)
    except ValueError:
        return None

# ❌ Éviter : ambiguïté
def trouver_element(liste: list[int], valeur: int) -> int:
    # Peut retourner None mais ce n'est pas indiqué
    ...
```

### 3. Préférer les types spécifiques à Any

```python
from typing import Any

# ❌ Trop général
def traiter(data: Any) -> Any:
    return data

# ✅ Plus spécifique
def traiter(data: dict[str, str]) -> list[str]:
    return list(data.values())
```

### 4. Utiliser des Type Aliases pour les types complexes

```python
from typing import TypeAlias

# ❌ Répétitif et difficile à lire
def f1(data: dict[str, list[tuple[int, str]]]) -> dict[str, list[tuple[int, str]]]:
    ...

# ✅ Plus lisible avec un alias
DataType: TypeAlias = dict[str, list[tuple[int, str]]]

def f1(data: DataType) -> DataType:
    ...
```

### 5. Annoter les variables quand le type n'est pas évident

```python
from typing import Any

# ✅ Type évident, annotation optionnelle
x = 5  # int évident  
nom = "Alice"  # str évident  

# ✅ Type non évident, annotation recommandée
donnees: list[dict[str, Any]] = obtenir_donnees()  
resultat: User | None = rechercher_utilisateur(id)  
```

### 6. Utiliser Protocol pour la flexibilité

```python
# ✅ Flexible avec Protocol
from typing import Protocol

class Serializable(Protocol):
    def to_json(self) -> str: ...

def sauvegarder(obj: Serializable) -> None:
    json_data = obj.to_json()
    # ...

# Toute classe avec to_json() fonctionne, pas besoin d'héritage
```

### 7. Documenter les types complexes

```python
from typing import TypeAlias

# ✅ Type alias documenté
ConfigDict: TypeAlias = dict[str, dict[str, str | int | bool]]
"""
Structure de configuration:
{
    "section": {
        "key": value (str, int ou bool)
    }
}
"""

def charger_config(fichier: str) -> ConfigDict:
    """Charge la configuration depuis un fichier"""
    ...
```

---

## Résumé

### Types de base

```python
# Types simples
x: int = 5  
y: float = 3.14  
z: str = "texte"  
b: bool = True  

# Collections (types natifs, pas besoin d'import)
liste: list[int] = [1, 2, 3]  
dico: dict[str, int] = {"a": 1}  
tuple_: tuple[int, str] = (1, "a")  
ensemble: set[str] = {"a", "b"}  
```

### Types spéciaux

```python
from typing import Any, Literal, Final

# Valeur ou None
x: int | None = None

# Plusieurs types possibles
y: int | str = 5

# N'importe quel type
z: Any = "anything"

# Valeurs littérales spécifiques
mode: Literal["r", "w", "a"] = "r"

# Constante
MAX: Final[int] = 100
```

### Types avancés

```python
from typing import Callable, TypeVar, Generic, Protocol

# Fonction
Func = Callable[[int, int], int]

# Générique
T = TypeVar('T')  
def premier(liste: list[T]) -> T: ...  

# Classe générique
class Pile(Generic[T]): ...

# Protocol
class Drawable(Protocol):
    def draw(self) -> str: ...
```

### Vérification avec mypy

```bash
# Installer
pip install mypy

# Vérifier un fichier
mypy script.py

# Vérifier un projet
mypy src/
```

Les annotations de type rendent le code Python plus robuste, plus lisible et plus facile à maintenir. Elles sont particulièrement utiles dans les projets de grande taille et pour les bibliothèques !

⏭️ [Programmation concurrente](/08-programmation-concurrente/README.md)
