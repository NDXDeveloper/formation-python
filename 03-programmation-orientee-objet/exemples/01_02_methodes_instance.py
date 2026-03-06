# ============================================================================
#   Section 3.1 : Méthodes d'instance
#   Description : Définir des méthodes, appeler des méthodes, modifier
#                 l'état d'un objet via ses méthodes
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def aboyer(self):
        print(f"{self.nom} dit : Wouf wouf !")

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

    def vieillir(self):
        self.age += 1
        print(f"{self.nom} a maintenant {self.age} ans.")

# Utilisation
mon_chien = Chien("Rex", 5)
mon_chien.aboyer()          # Rex dit : Wouf wouf !
mon_chien.se_presenter()    # Je m'appelle Rex et j'ai 5 ans.
mon_chien.vieillir()        # Rex a maintenant 6 ans.
