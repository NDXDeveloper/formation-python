# ============================================================================
#   Section 6.21 : Exemple pratique - Cache générique
#   Description : Classe Cache générique avec TypeVar, Generic, Callable,
#                 expiration par durée de vie, get_ou_calculer
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import TypeVar, Generic, Callable
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
        self._cache: dict[K, tuple[V, datetime]] = {}
        self._duree_vie = timedelta(seconds=duree_vie)

    def set(self, cle: K, valeur: V) -> None:
        """Ajoute ou met à jour une entrée dans le cache."""
        self._cache[cle] = (valeur, datetime.now())

    def get(self, cle: K) -> V | None:
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
print(f"cache_str['user_1'] = {cache_str.get('user_1')}")  # Alice

cache_int: Cache[int, list[int]] = Cache()
cache_int.set(1, [1, 2, 3, 4, 5])
print(f"cache_int[1] = {cache_int.get(1)}")  # [1, 2, 3, 4, 5]

# Utilisation de get_ou_calculer
def calcul_couteux() -> str:
    print("  (calcul en cours...)")
    return "résultat calculé"

print("\nPremier appel :")
val = cache_str.get_ou_calculer("resultat", calcul_couteux)
print(f"  valeur = {val}")

print("Deuxième appel (depuis le cache) :")
val = cache_str.get_ou_calculer("resultat", calcul_couteux)
print(f"  valeur = {val}")

print(f"\nClé inexistante : {cache_str.get('inexistant')}")  # None
