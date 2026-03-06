# ============================================================================
#   Section 3.2 : Héritage de base
#   Description : Classe parente Animal, classe enfant Chien, méthodes héritées
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} est en train de manger.")

    def dormir(self):
        print(f"{self.nom} dort paisiblement.")


class Chien(Animal):  # Chien hérite de Animal
    def aboyer(self):
        print(f"{self.nom} dit : Wouf wouf !")


# Utilisation
mon_chien = Chien("Rex")
mon_chien.manger()   # Méthode héritée de Animal
mon_chien.dormir()   # Méthode héritée de Animal
mon_chien.aboyer()   # Méthode propre à Chien
