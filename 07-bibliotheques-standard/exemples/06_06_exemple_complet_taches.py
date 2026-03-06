# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Exemple complet - Système de gestion de tâches avec
#                 annotations de type (Literal, Protocol, TypeAlias,
#                 dataclass, Generic)
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

from typing import Literal, Protocol, TypeAlias
from dataclasses import dataclass, field
from datetime import datetime, timedelta

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
        print(f"  [Email] -> Utilisateur {destinataire}: {message}")
        return True


class NotificateurSMS:
    """Notificateur par SMS"""

    def envoyer(self, destinataire: UserId, message: str) -> bool:
        print(f"  [SMS] -> Utilisateur {destinataire}: {message}")
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

        tache.statut = nouveau_statut

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

    # Créer une tâche en retard (échéance passée)
    tache4 = gestionnaire.creer_tache(
        titre="Revue de code",
        description="Revoir le code du sprint",
        priorite="critique",
        assignee_id=1,
        date_echeance=datetime.now() - timedelta(days=1)
    )

    print(f"\n{tache1.titre} créée (ID: {tache1.id})")
    print(f"{tache2.titre} créée (ID: {tache2.id})")
    print(f"{tache3.titre} créée (ID: {tache3.id})")
    print(f"{tache4.titre} créée (ID: {tache4.id})")

    # Modifier les statuts
    print("\n--- Modification des statuts ---")
    gestionnaire.modifier_statut(tache1.id, "en_cours")
    gestionnaire.modifier_statut(tache2.id, "terminee")

    # Assigner une tâche
    print("\n--- Assignation ---")
    gestionnaire.assigner_tache(tache3.id, 1)

    # Afficher les statistiques
    stats = gestionnaire.obtenir_statistiques()
    print("\nStatistiques:")
    for cle, valeur in stats.items():
        print(f"  {cle}: {valeur}")

    # Lister les tâches par statut
    taches_en_cours: list[Tache] = gestionnaire.lister_taches_par_statut("en_cours")
    print(f"\nTâches en cours: {len(taches_en_cours)}")
    for tache in taches_en_cours:
        print(f"  - {tache.titre}")

    # Lister les tâches en retard
    taches_retard = gestionnaire.lister_taches_en_retard()
    print(f"\nTâches en retard: {len(taches_retard)}")
    for tache in taches_retard:
        print(f"  - {tache.titre} (échéance: {tache.date_echeance.strftime('%Y-%m-%d') if tache.date_echeance else 'N/A'})")

    # Tester avec un notificateur SMS
    print("\n--- Test avec NotificateurSMS ---")
    notif_sms: Notificateur = NotificateurSMS()
    gestionnaire2 = GestionnaireTaches(notif_sms)
    gestionnaire2.creer_tache(
        titre="Tâche urgente",
        description="Via SMS",
        priorite="critique",
        assignee_id=3
    )


if __name__ == "__main__":
    main()
