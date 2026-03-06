# ============================================================================
#   Section 3.2 : Héritage vs composition
#   Description : Relation "est-un" (héritage) vs relation "a-un" (composition),
#                 réutilisation du code, extensibilité
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

# --- Héritage : Relation "Est-Un" ---
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} mange.")

    def dormir(self):
        print(f"{self.nom} dort.")

class Chien(Animal):  # Un chien EST UN animal
    def aboyer(self):
        print(f"{self.nom} aboie : Wouf !")

class Chat(Animal):
    pass

class Oiseau(Animal):
    def voler(self):
        print(f"{self.nom} vole.")

class Poisson(Animal):
    def nager(self):
        print(f"{self.nom} nage.")

# Fonction polymorphe
def nourrir_animaux(liste_animaux):
    for animal in liste_animaux:
        animal.manger()

animaux = [Chien("Rex"), Chat("Felix"), Oiseau("Tweety")]
nourrir_animaux(animaux)

# --- Composition : Relation "A-Un" ---
print()

class Moteur:
    def demarrer(self):
        print("Moteur démarré")

class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # Une voiture A UN moteur

    def demarrer(self):
        self.moteur.demarrer()

ma_voiture = Voiture()
ma_voiture.demarrer()
