# ============================================================================
#   Section 3.1 : Instances indépendantes
#   Description : Chaque instance a ses propres attributs indépendants
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Compteur:
    def __init__(self, valeur_initiale=0):
        self.valeur = valeur_initiale

    def incrementer(self):
        self.valeur += 1

    def afficher(self):
        print(f"Valeur : {self.valeur}")

compteur1 = Compteur()
compteur2 = Compteur(10)

compteur1.incrementer()
compteur1.incrementer()
compteur2.incrementer()

compteur1.afficher()  # Valeur : 2
compteur2.afficher()  # Valeur : 11
