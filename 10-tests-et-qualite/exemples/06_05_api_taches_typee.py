# ============================================================================
#   Section 10.6 : Validation de types avec mypy
#   Description : Cas pratique complet - API de gestion de taches avec
#                 types complets (Enum, TypedDict, annotations)
#   Fichier source : 06-validation-types-mypy.md
# ============================================================================

"""API de gestion de taches avec types complets."""

from typing import TypedDict
from datetime import datetime
from enum import Enum


class Priorite(Enum):
    """Niveaux de priorite pour les taches."""
    HAUTE = 1
    NORMALE = 2
    BASSE = 3


class TacheDict(TypedDict):
    """Structure d'une tache."""
    id: int
    titre: str
    terminee: bool
    priorite: Priorite
    date_creation: datetime


class Tache:
    """Represente une tache individuelle."""

    def __init__(
        self,
        id: int,
        titre: str,
        priorite: Priorite = Priorite.NORMALE
    ) -> None:
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas etre vide")

        self.id: int = id
        self.titre: str = titre
        self.terminee: bool = False
        self.priorite: Priorite = priorite
        self.date_creation: datetime = datetime.now()

    def marquer_terminee(self) -> None:
        """Marque la tache comme terminee."""
        self.terminee = True

    def marquer_non_terminee(self) -> None:
        """Marque la tache comme non terminee."""
        self.terminee = False

    def changer_priorite(self, nouvelle_priorite: Priorite) -> None:
        """Change la priorite de la tache."""
        self.priorite = nouvelle_priorite

    def to_dict(self) -> TacheDict:
        """Convertit la tache en dictionnaire."""
        return {
            "id": self.id,
            "titre": self.titre,
            "terminee": self.terminee,
            "priorite": self.priorite,
            "date_creation": self.date_creation
        }

    def __repr__(self) -> str:
        return f"Tache(id={self.id}, titre='{self.titre}', priorite={self.priorite.name})"


class GestionnaireTaches:
    """Gere une collection de taches."""

    def __init__(self) -> None:
        self.taches: dict[int, Tache] = {}
        self._prochain_id: int = 1

    def creer_tache(
        self,
        titre: str,
        priorite: Priorite = Priorite.NORMALE
    ) -> Tache:
        """Cree une nouvelle tache."""
        tache = Tache(self._prochain_id, titre, priorite)
        self.taches[self._prochain_id] = tache
        self._prochain_id += 1
        return tache

    def obtenir_tache(self, tache_id: int) -> Tache | None:
        """Obtient une tache par son ID."""
        return self.taches.get(tache_id)

    def supprimer_tache(self, tache_id: int) -> bool:
        """Supprime une tache."""
        if tache_id in self.taches:
            del self.taches[tache_id]
            return True
        return False

    def lister_taches(
        self,
        seulement_non_terminees: bool = False,
        priorite: Priorite | None = None
    ) -> list[Tache]:
        """Liste les taches selon des criteres."""
        taches = list(self.taches.values())

        if seulement_non_terminees:
            taches = [t for t in taches if not t.terminee]

        if priorite is not None:
            taches = [t for t in taches if t.priorite == priorite]

        taches.sort(key=lambda t: (t.priorite.value, t.date_creation))
        return taches

    def compter_taches(self, seulement_non_terminees: bool = False) -> int:
        """Compte le nombre de taches."""
        return len(self.lister_taches(seulement_non_terminees))

    def obtenir_statistiques(self) -> dict[str, int]:
        """Calcule des statistiques sur les taches."""
        total = len(self.taches)
        terminees = sum(1 for t in self.taches.values() if t.terminee)

        return {
            "total": total,
            "terminees": terminees,
            "non_terminees": total - terminees,
            "haute_priorite": sum(
                1 for t in self.taches.values()
                if t.priorite == Priorite.HAUTE
            )
        }


def exemple_utilisation() -> None:
    """Exemple d'utilisation du gestionnaire de taches."""
    gestionnaire = GestionnaireTaches()

    # Creer des taches
    tache1 = gestionnaire.creer_tache("Faire les courses", Priorite.HAUTE)
    tache2 = gestionnaire.creer_tache("Lire un livre")
    tache3 = gestionnaire.creer_tache("Faire du sport", Priorite.BASSE)

    print("=== Toutes les taches ===")
    for t in gestionnaire.lister_taches():
        print(f"  {t}")

    # Marquer une tache comme terminee
    tache1.marquer_terminee()

    # Lister les taches non terminees
    non_terminees: list[Tache] = gestionnaire.lister_taches(
        seulement_non_terminees=True
    )
    print(f"\nTaches non terminees : {len(non_terminees)}")
    for t in non_terminees:
        print(f"  {t}")

    # Filtrer par priorite
    hautes: list[Tache] = gestionnaire.lister_taches(priorite=Priorite.HAUTE)
    print(f"\nTaches haute priorite : {len(hautes)}")

    # Statistiques
    stats: dict[str, int] = gestionnaire.obtenir_statistiques()
    print(f"\nStatistiques : {stats}")

    # Supprimer
    gestionnaire.supprimer_tache(tache3.id)
    print(f"\nApres suppression : {gestionnaire.compter_taches()} taches")

    # Titre vide
    try:
        gestionnaire.creer_tache("")
    except ValueError as e:
        print(f"\nTitre vide -> ValueError: {e}")


if __name__ == "__main__":
    exemple_utilisation()
