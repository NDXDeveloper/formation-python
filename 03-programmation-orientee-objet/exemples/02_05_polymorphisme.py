# ============================================================================
#   Section 3.2 : Polymorphisme
#   Description : Interface commune pour différents types (Cercle, Carré,
#                 Triangle), même boucle pour tous
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class Forme:
    def __init__(self, nom):
        self.nom = nom

    def calculer_surface(self):
        pass  # À redéfinir dans les classes enfants

    def afficher(self):
        print(f"{self.nom} - Surface : {self.calculer_surface()} cm²")


class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14159 * self.rayon ** 2


class Carre(Forme):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def calculer_surface(self):
        return self.cote ** 2


class Triangle(Forme):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def calculer_surface(self):
        return (self.base * self.hauteur) / 2


# Le polymorphisme en action !
formes = [
    Cercle(5),
    Carre(4),
    Triangle(6, 3)
]

for forme in formes:
    forme.afficher()
