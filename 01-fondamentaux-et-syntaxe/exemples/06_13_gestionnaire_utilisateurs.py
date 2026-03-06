# ============================================================================
#   Section 6.19 : Exemple pratique - Système de gestion d'utilisateurs
#   Description : Utilisation de dataclass, dict typé, filtrage par âge,
#                 ajout et recherche d'utilisateurs avec type hints complets
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from dataclasses import dataclass

@dataclass
class Utilisateur:
    id: int
    nom: str
    email: str
    age: int

class GestionnaireUtilisateurs:
    def __init__(self) -> None:
        self._utilisateurs: dict[int, Utilisateur] = {}
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

    def obtenir_utilisateur(self, id: int) -> Utilisateur | None:
        """Retourne un utilisateur ou None s'il n'existe pas."""
        return self._utilisateurs.get(id)

    def lister_utilisateurs(self) -> list[Utilisateur]:
        """Retourne la liste de tous les utilisateurs."""
        return list(self._utilisateurs.values())

    def filtrer_par_age(
        self,
        age_min: int,
        age_max: int
    ) -> list[Utilisateur]:
        """Filtre les utilisateurs par tranche d'âge."""
        return [
            user for user in self._utilisateurs.values()
            if age_min <= user.age <= age_max
        ]

# Utilisation
gestionnaire = GestionnaireUtilisateurs()
alice = gestionnaire.ajouter_utilisateur("Alice", "alice@example.com", 25)
bob = gestionnaire.ajouter_utilisateur("Bob", "bob@example.com", 30)

print(f"Alice : {alice}")
print(f"Bob : {bob}")

user = gestionnaire.obtenir_utilisateur(1)
if user:
    print(f"Utilisateur trouvé : {user.nom}")

jeunes = gestionnaire.filtrer_par_age(20, 27)
print(f"Utilisateurs entre 20 et 27 ans : {len(jeunes)}")  # 1

tous = gestionnaire.lister_utilisateurs()
print(f"Total utilisateurs : {len(tous)}")  # 2
