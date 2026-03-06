# ============================================================================
#   Section 3.5 : Post-initialisation avec __post_init__
#   Description : Champ calculé automatiquement (email) et validation dans
#                 __post_init__
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from dataclasses import dataclass, field

@dataclass
class Employe:
    prenom: str
    nom: str
    salaire: float
    email: str = field(init=False)  # Calculé automatiquement

    def __post_init__(self):
        self.email = f"{self.prenom.lower()}.{self.nom.lower()}@entreprise.fr"
        if self.salaire < 0:
            raise ValueError("Le salaire ne peut pas être négatif")

emp = Employe("Alice", "Martin", 45000)
print(emp.email)  # alice.martin@entreprise.fr

try:
    emp2 = Employe("Bob", "Dupont", -1000)
except ValueError as e:
    print(f"Erreur : {e}")
