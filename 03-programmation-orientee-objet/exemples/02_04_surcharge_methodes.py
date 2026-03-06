# ============================================================================
#   Section 3.2 : Surcharge de méthodes (Method Overriding)
#   Description : Redéfinir une méthode parente dans les classes enfants
#                 (Animal, Chien, Chat, Vache)
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_bruit(self):
        print(f"{self.nom} fait un bruit.")


class Chien(Animal):
    def faire_bruit(self):
        print(f"{self.nom} aboie : Wouf wouf !")


class Chat(Animal):
    def faire_bruit(self):
        print(f"{self.nom} miaule : Miaou miaou !")


class Vache(Animal):
    def faire_bruit(self):
        print(f"{self.nom} meugle : Meuh meuh !")


# Utilisation
rex = Chien("Rex")
felix = Chat("Felix")
marguerite = Vache("Marguerite")

rex.faire_bruit()         # Rex aboie : Wouf wouf !
felix.faire_bruit()       # Felix miaule : Miaou miaou !
marguerite.faire_bruit()  # Marguerite meugle : Meuh meuh !
