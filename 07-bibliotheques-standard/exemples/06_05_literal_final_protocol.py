# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Literal (valeurs littérales), Final (constantes),
#                 Protocol (duck typing structurel), NewType, @overload
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

from typing import Literal, Final, Protocol, NewType, overload
import tempfile
import os
import shutil

# ==========================================
# 1. Literal - Valeurs spécifiques autorisées
# ==========================================
print("=== Literal ===")

Mode = Literal["lecture", "ecriture", "ajout"]

def ouvrir_fichier(nom: str, mode: Mode) -> None:
    """Ouvre un fichier avec un mode spécifique"""
    print(f"  Ouverture de {nom} en mode {mode}")

ouvrir_fichier("data.txt", "lecture")
ouvrir_fichier("data.txt", "ecriture")

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

print(f"  Code 200: {traiter_reponse(200)}")
print(f"  Code 404: {traiter_reponse(404)}")
print(f"  Code 500: {traiter_reponse(500)}")

# Système de permissions
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
print(f"\n  {user1.nom} peut écrire: {user1.peut_ecrire()}")
print(f"  {user2.nom} peut écrire: {user2.peut_ecrire()}")
print(f"  {user1.nom} peut supprimer: {user1.peut_supprimer()}")

# ==========================================
# 2. Final - Constantes
# ==========================================
print("\n=== Final ===")

PI: Final = 3.14159
MAX_TENTATIVES: Final[int] = 3
API_KEY: Final[str] = "secret_key_123"

print(f"PI = {PI}")
print(f"MAX_TENTATIVES = {MAX_TENTATIVES}")
print(f"API_KEY = {API_KEY}")

class Configuration:
    """Configuration de l'application"""
    MAX_CONNEXIONS: Final[int] = 100
    TIMEOUT: Final[float] = 30.0
    VERSION: Final[str] = "1.0.0"

    def __init__(self) -> None:
        self.id: Final[str] = "config_123"

config = Configuration()
print(f"\nConfiguration.MAX_CONNEXIONS = {Configuration.MAX_CONNEXIONS}")
print(f"Configuration.TIMEOUT = {Configuration.TIMEOUT}")
print(f"Configuration.VERSION = {Configuration.VERSION}")
print(f"config.id = {config.id}")

# ==========================================
# 3. Protocol - Duck Typing structurel
# ==========================================
print("\n=== Protocol ===")

class Drawable(Protocol):
    """Protocol pour les objets dessinables"""
    def draw(self) -> str:
        ...

class Circle:
    def __init__(self, rayon: float) -> None:
        self.rayon = rayon

    def draw(self) -> str:
        return f"Cercle de rayon {self.rayon}"

class Square:
    def __init__(self, cote: float) -> None:
        self.cote = cote

    def draw(self) -> str:
        return f"Carré de côté {self.cote}"

def dessiner_forme(forme: Drawable) -> None:
    """Dessine n'importe quelle forme qui implémente draw()"""
    print(f"  {forme.draw()}")

cercle = Circle(5)
carre = Square(10)

dessiner_forme(cercle)
dessiner_forme(carre)

# Protocol pour un système de stockage
print("\n--- Protocol Stockage ---")

class Stockage(Protocol):
    def sauvegarder(self, cle: str, valeur: str) -> bool: ...
    def charger(self, cle: str) -> str | None: ...
    def supprimer(self, cle: str) -> bool: ...

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

def traiter_donnees(stockage: Stockage, cle: str, valeur: str) -> None:
    """Traite des données avec n'importe quel système de stockage"""
    if stockage.sauvegarder(cle, valeur):
        print(f"  Sauvegarde réussie: {cle}")
        donnee = stockage.charger(cle)
        if donnee:
            print(f"  Chargé: {donnee}")

stockage_memoire = StockageMemoire()
traiter_donnees(stockage_memoire, "test", "valeur_test")

# ==========================================
# 4. NewType - Types distincts
# ==========================================
print("\n=== NewType ===")

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def obtenir_utilisateur(user_id: UserId) -> str:
    return f"User #{user_id}"

def obtenir_produit(product_id: ProductId) -> str:
    return f"Product #{product_id}"

user_id = UserId(123)
product_id = ProductId(456)

print(f"  {obtenir_utilisateur(user_id)}")
print(f"  {obtenir_produit(product_id)}")

# Système financier
Euro = NewType('Euro', float)
Dollar = NewType('Dollar', float)

def ajouter_euros(montant1: Euro, montant2: Euro) -> Euro:
    return Euro(montant1 + montant2)

prix1 = Euro(10.5)
prix2 = Euro(5.25)
total = ajouter_euros(prix1, prix2)
print(f"\n  {prix1} EUR + {prix2} EUR = {total} EUR")

# ==========================================
# 5. @overload - Surcharge de signatures
# ==========================================
print("\n=== @overload ===")

@overload
def traiter(valeur: int) -> int: ...

@overload
def traiter(valeur: str) -> str: ...

def traiter(valeur: int | str) -> int | str:
    """Traite une valeur selon son type"""
    if isinstance(valeur, int):
        return valeur * 2
    else:
        return valeur.upper()

resultat_int: int = traiter(5)
resultat_str: str = traiter("hello")
print(f"  traiter(5) = {resultat_int}")
print(f"  traiter('hello') = {resultat_str}")

# Surcharge plus complexe
@overload
def obtenir_elements(indices: int) -> str: ...

@overload
def obtenir_elements(indices: list[int]) -> list[str]: ...

def obtenir_elements(indices: int | list[int]) -> str | list[str]:
    """Obtient un ou plusieurs éléments d'une liste"""
    elements = ["a", "b", "c", "d", "e"]
    if isinstance(indices, int):
        return elements[indices]
    else:
        return [elements[i] for i in indices]

element: str = obtenir_elements(0)
multiples: list[str] = obtenir_elements([0, 2, 4])
print(f"  obtenir_elements(0) = {element}")
print(f"  obtenir_elements([0, 2, 4]) = {multiples}")
