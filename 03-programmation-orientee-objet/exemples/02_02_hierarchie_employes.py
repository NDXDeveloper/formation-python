# ============================================================================
#   Section 3.2 : Hiérarchie d'employés
#   Description : Classe Employe, Developpeur et Manager avec super(),
#                 augmentation de salaire
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class Employe:
    """Classe de base représentant un employé."""

    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_info(self):
        print(f"Employé : {self.prenom} {self.nom}")
        print(f"Salaire : {self.salaire}€")

    def augmentation(self, pourcentage):
        self.salaire *= (1 + pourcentage / 100)
        print(f"Nouveau salaire : {self.salaire:.2f}€")


class Developpeur(Employe):
    """Un développeur est un employé avec des compétences spécifiques."""

    def __init__(self, nom, prenom, salaire, langage):
        super().__init__(nom, prenom, salaire)
        self.langage = langage

    def afficher_info(self):
        super().afficher_info()
        print(f"Langage principal : {self.langage}")

    def coder(self):
        print(f"{self.prenom} code en {self.langage}...")


class Manager(Employe):
    """Un manager est un employé qui gère une équipe."""

    def __init__(self, nom, prenom, salaire, taille_equipe):
        super().__init__(nom, prenom, salaire)
        self.taille_equipe = taille_equipe

    def afficher_info(self):
        super().afficher_info()
        print(f"Gère une équipe de {self.taille_equipe} personnes")

    def organiser_reunion(self):
        print(f"{self.prenom} organise une réunion d'équipe.")


# Utilisation
dev = Developpeur("Dupont", "Marie", 45000, "Python")
dev.afficher_info()
dev.coder()
dev.augmentation(10)

print("\n" + "="*40 + "\n")

manager = Manager("Martin", "Pierre", 60000, 8)
manager.afficher_info()
manager.organiser_reunion()
