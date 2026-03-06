# ============================================================================
#   Section 3.2 : Le mot-clé super() dans le constructeur
#   Description : Appeler le constructeur parent, étendre avec super()
#                 dans les méthodes (Vehicule/Voiture, Rectangle/RectangleColore)
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

# --- super() dans le constructeur ---
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        print(f"Création d'un véhicule : {marque} {modele}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, nombre_portes):
        super().__init__(marque, modele)
        self.nombre_portes = nombre_portes
        print(f"C'est une voiture avec {nombre_portes} portes")

ma_voiture = Voiture("Renault", "Clio", 5)

# --- super() dans les méthodes ---
print()

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def afficher(self):
        print(f"Rectangle : {self.largeur} x {self.hauteur}")

    def surface(self):
        return self.largeur * self.hauteur


class RectangleColore(Rectangle):
    def __init__(self, largeur, hauteur, couleur):
        super().__init__(largeur, hauteur)
        self.couleur = couleur

    def afficher(self):
        super().afficher()
        print(f"Couleur : {self.couleur}")

rect = RectangleColore(10, 5, "rouge")
rect.afficher()
print(f"Surface : {rect.surface()} cm²")
