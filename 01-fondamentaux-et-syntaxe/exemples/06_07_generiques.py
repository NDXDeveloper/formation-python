# ============================================================================
#   Section 6.9 : Génériques (Generics)
#   Description : TypeVar pour fonctions génériques, Generic pour classes
#                 génériques (Pile), fonctions avec plusieurs types
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import TypeVar, Generic

# --- TypeVar ---
T = TypeVar('T')

def premier_element(liste: list[T]) -> T:
    """Retourne le premier élément d'une liste, quel que soit son type."""
    return liste[0]

nombres = [1, 2, 3]
premier = premier_element(nombres)
print(f"Premier élément (int) : {premier}")  # 1

mots = ["hello", "world"]
premier_mot = premier_element(mots)
print(f"Premier élément (str) : {premier_mot}")  # hello

# --- Fonction générique avec plusieurs types ---
U = TypeVar('U')

def creer_paire(premier: T, second: U) -> tuple[T, U]:
    """Crée une paire de deux éléments de types potentiellement différents."""
    return (premier, second)

paire1 = creer_paire("Alice", 25)
paire2 = creer_paire(3.14, True)
print(f"Paire 1 : {paire1}")  # ('Alice', 25)
print(f"Paire 2 : {paire2}")  # (3.14, True)

# --- Classe générique : Pile ---
class Pile(Generic[T]):
    """Pile générique qui peut contenir n'importe quel type."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def empiler(self, item: T) -> None:
        self._items.append(item)

    def depiler(self) -> T:
        return self._items.pop()

    def est_vide(self) -> bool:
        return len(self._items) == 0

# Pile d'entiers
pile_nombres: Pile[int] = Pile()
pile_nombres.empiler(1)
pile_nombres.empiler(2)
print(f"Dépilé (int) : {pile_nombres.depiler()}")  # 2

# Pile de chaînes
pile_mots: Pile[str] = Pile()
pile_mots.empiler("hello")
pile_mots.empiler("world")
print(f"Dépilé (str) : {pile_mots.depiler()}")  # world
