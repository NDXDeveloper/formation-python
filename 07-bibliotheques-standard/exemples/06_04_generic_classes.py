# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Classes génériques avec Generic - Pile générique,
#                 Cache générique avec expiration
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

from typing import Generic, TypeVar
from datetime import datetime, timedelta

T = TypeVar('T')

# ==========================================
# 1. Pile générique
# ==========================================
print("=== Pile générique (Generic[T]) ===")

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

# Utilisation avec des entiers
pile_entiers: Pile[int] = Pile[int]()
pile_entiers.empiler(1)
pile_entiers.empiler(2)
pile_entiers.empiler(3)
print(f"Pile d'entiers - taille: {pile_entiers.taille()}")
print(f"  depiler: {pile_entiers.depiler()}")
print(f"  depiler: {pile_entiers.depiler()}")

# Utilisation avec des strings
pile_strings: Pile[str] = Pile[str]()
pile_strings.empiler("a")
pile_strings.empiler("b")
print(f"\nPile de strings - taille: {pile_strings.taille()}")
print(f"  depiler: {pile_strings.depiler()}")
print(f"  est_vide: {pile_strings.est_vide()}")
print(f"  depiler: {pile_strings.depiler()}")
print(f"  est_vide: {pile_strings.est_vide()}")

# ==========================================
# 2. Cache générique avec expiration
# ==========================================
print("\n=== Cache générique (Generic[K, V]) ===")

K = TypeVar('K')
V = TypeVar('V')

class Cache(Generic[K, V]):
    """Cache générique avec expiration"""

    def __init__(self, duree_expiration: int = 300) -> None:
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

# Cache pour des utilisateurs (clé: int, valeur: str)
cache_users: Cache[int, str] = Cache[int, str](duree_expiration=60)
cache_users.ajouter(1, "Alice")
cache_users.ajouter(2, "Bob")

utilisateur = cache_users.obtenir(1)
print(f"Utilisateur 1: {utilisateur}")

utilisateur_inexistant = cache_users.obtenir(99)
print(f"Utilisateur 99: {utilisateur_inexistant}")

# Cache pour de la configuration (clé: str, valeur: dict)
cache_config: Cache[str, dict] = Cache[str, dict](duree_expiration=300)
cache_config.ajouter("db", {"host": "localhost", "port": 5432})
config = cache_config.obtenir("db")
print(f"\nConfig 'db': {config}")

# Supprimer une entrée
cache_users.supprimer(2)
print(f"\nAprès suppression, utilisateur 2: {cache_users.obtenir(2)}")

# Nettoyer les expirés (rien à nettoyer, tout est frais)
nb_expires = cache_users.nettoyer_expires()
print(f"Entrées expirées nettoyées: {nb_expires}")
