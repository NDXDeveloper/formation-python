# ============================================================================
#   Section 10.4 : Documentation avec docstrings
#   Description : Cas pratique complet - API de gestion de taches avec
#                 Tache et GestionnaireTaches (docstrings Google Style)
#   Fichier source : 04-documentation-docstrings.md
# ============================================================================

"""
API de gestion de taches.

Ce module fournit une API simple pour gerer une liste de taches
avec des fonctionnalites de creation, lecture, mise a jour et
suppression (CRUD).

Example:
    >>> from api_taches import GestionnaireTaches, Tache
    >>> gestionnaire = GestionnaireTaches()
    >>> tache = gestionnaire.creer_tache("Acheter du pain")
    >>> gestionnaire.lister_taches()
    [Tache(id=1, titre='Acheter du pain', terminee=False)]

Attributes:
    VERSION (str): Version de l'API ("1.0.0").
    PRIORITE_HAUTE (int): Constante pour priorite haute (1).
    PRIORITE_NORMALE (int): Constante pour priorite normale (2).
    PRIORITE_BASSE (int): Constante pour priorite basse (3).
"""

from datetime import datetime

VERSION = "1.0.0"
PRIORITE_HAUTE = 1
PRIORITE_NORMALE = 2
PRIORITE_BASSE = 3


class Tache:
    """Represente une tache individuelle.

    Une tache contient un titre, un etat (terminee ou non),
    une priorite et une date de creation.

    Attributes:
        id (int): Identifiant unique de la tache.
        titre (str): Le titre de la tache.
        terminee (bool): True si la tache est terminee.
        priorite (int): Niveau de priorite (1=haute, 2=normale, 3=basse).
        date_creation (datetime): Date et heure de creation.

    Example:
        >>> tache = Tache(1, "Faire les courses")
        >>> tache.marquer_terminee()
        >>> tache.terminee
        True
    """

    def __init__(self, id: int, titre: str, priorite: int = PRIORITE_NORMALE):
        """Initialise une nouvelle tache.

        Args:
            id: L'identifiant unique de la tache.
            titre: Le titre de la tache.
            priorite: Le niveau de priorite (1, 2, ou 3).
                Par defaut PRIORITE_NORMALE.

        Raises:
            ValueError: Si le titre est vide ou si la priorite
                n'est pas valide.
        """
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas etre vide")
        if priorite not in [PRIORITE_HAUTE, PRIORITE_NORMALE, PRIORITE_BASSE]:
            raise ValueError("Priorite invalide")

        self.id = id
        self.titre = titre
        self.terminee = False
        self.priorite = priorite
        self.date_creation = datetime.now()

    def marquer_terminee(self) -> None:
        """Marque la tache comme terminee."""
        self.terminee = True

    def marquer_non_terminee(self) -> None:
        """Marque la tache comme non terminee."""
        self.terminee = False

    def changer_priorite(self, nouvelle_priorite: int) -> None:
        """Change la priorite de la tache.

        Args:
            nouvelle_priorite: La nouvelle priorite (1, 2, ou 3).

        Raises:
            ValueError: Si la priorite n'est pas valide.
        """
        if nouvelle_priorite not in [PRIORITE_HAUTE, PRIORITE_NORMALE, PRIORITE_BASSE]:
            raise ValueError("Priorite invalide")
        self.priorite = nouvelle_priorite

    def __repr__(self) -> str:
        """Retourne une representation textuelle de la tache."""
        return f"Tache(id={self.id}, titre='{self.titre}', terminee={self.terminee})"


class GestionnaireTaches:
    """Gere une collection de taches.

    Cette classe permet de creer, lister, modifier et supprimer
    des taches. Elle maintient un compteur pour assigner des ID
    uniques a chaque tache.

    Attributes:
        taches (dict): Dictionnaire des taches indexees par ID.

    Example:
        >>> gestionnaire = GestionnaireTaches()
        >>> tache1 = gestionnaire.creer_tache("Tache 1")
        >>> tache2 = gestionnaire.creer_tache("Tache 2", PRIORITE_HAUTE)
        >>> len(gestionnaire.lister_taches())
        2
    """

    def __init__(self):
        """Initialise un nouveau gestionnaire de taches."""
        self.taches: dict[int, Tache] = {}
        self._prochain_id = 1

    def creer_tache(self, titre: str, priorite: int = PRIORITE_NORMALE) -> Tache:
        """Cree une nouvelle tache.

        Args:
            titre: Le titre de la tache.
            priorite: Le niveau de priorite. Par defaut PRIORITE_NORMALE.

        Returns:
            La tache creee.

        Raises:
            ValueError: Si le titre est vide ou la priorite invalide.
        """
        tache = Tache(self._prochain_id, titre, priorite)
        self.taches[self._prochain_id] = tache
        self._prochain_id += 1
        return tache

    def obtenir_tache(self, tache_id: int) -> Tache | None:
        """Obtient une tache par son ID.

        Args:
            tache_id: L'identifiant de la tache.

        Returns:
            La tache correspondante, ou None si non trouvee.
        """
        return self.taches.get(tache_id)

    def supprimer_tache(self, tache_id: int) -> bool:
        """Supprime une tache.

        Args:
            tache_id: L'identifiant de la tache a supprimer.

        Returns:
            True si la tache a ete supprimee, False si inexistante.
        """
        if tache_id in self.taches:
            del self.taches[tache_id]
            return True
        return False

    def lister_taches(self, seulement_non_terminees: bool = False) -> list[Tache]:
        """Liste toutes les taches.

        Args:
            seulement_non_terminees: Si True, ne retourne que
                les taches non terminees. Par defaut False.

        Returns:
            Liste des taches, triees par priorite puis par date.
        """
        taches = list(self.taches.values())

        if seulement_non_terminees:
            taches = [t for t in taches if not t.terminee]

        taches.sort(key=lambda t: (t.priorite, t.date_creation))
        return taches

    def compter_taches(self, seulement_non_terminees: bool = False) -> int:
        """Compte le nombre de taches.

        Args:
            seulement_non_terminees: Si True, compte seulement
                les taches non terminees. Par defaut False.

        Returns:
            Le nombre de taches.
        """
        return len(self.lister_taches(seulement_non_terminees))


# --- Demonstration ---
if __name__ == "__main__":
    print(f"=== API de gestion de taches v{VERSION} ===\n")

    gestionnaire = GestionnaireTaches()

    # Creer des taches
    t1 = gestionnaire.creer_tache("Acheter du pain")
    t2 = gestionnaire.creer_tache("Faire du sport", PRIORITE_HAUTE)
    t3 = gestionnaire.creer_tache("Ranger le bureau", PRIORITE_BASSE)
    print("Taches creees :")
    for t in gestionnaire.lister_taches():
        print(f"  {t}")

    # Marquer une tache terminee
    t2.marquer_terminee()
    print(f"\nApres avoir termine '{t2.titre}' :")
    print(f"  Total : {gestionnaire.compter_taches()}")
    print(f"  Non terminees : {gestionnaire.compter_taches(seulement_non_terminees=True)}")

    # Lister les taches non terminees
    print("\nTaches restantes :")
    for t in gestionnaire.lister_taches(seulement_non_terminees=True):
        print(f"  {t}")

    # Changer la priorite
    t1.changer_priorite(PRIORITE_HAUTE)
    print(f"\nApres changement de priorite de '{t1.titre}' :")
    for t in gestionnaire.lister_taches(seulement_non_terminees=True):
        priorite_nom = {1: "haute", 2: "normale", 3: "basse"}[t.priorite]
        print(f"  {t} (priorite: {priorite_nom})")

    # Supprimer une tache
    gestionnaire.supprimer_tache(t3.id)
    print(f"\nApres suppression de '{t3.titre}' :")
    print(f"  Total : {gestionnaire.compter_taches()}")

    # Obtenir une tache
    tache = gestionnaire.obtenir_tache(t1.id)
    print(f"\nObtenir tache {t1.id} : {tache}")
    print(f"Obtenir tache 999 : {gestionnaire.obtenir_tache(999)}")

    # Titre vide
    try:
        gestionnaire.creer_tache("")
    except ValueError as e:
        print(f"\nCreer tache vide -> ValueError: {e}")

    # Priorite invalide
    try:
        gestionnaire.creer_tache("Test", priorite=99)
    except ValueError as e:
        print(f"Priorite invalide -> ValueError: {e}")
