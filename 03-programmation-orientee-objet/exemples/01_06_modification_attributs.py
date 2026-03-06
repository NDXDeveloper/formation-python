# ============================================================================
#   Section 3.1 : Modification des attributs
#   Description : Modifier directement les attributs d'un objet
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.kilometrage = 0

    def afficher_info(self):
        print(f"{self.marque} {self.couleur}, {self.kilometrage} km")

ma_voiture = Voiture("Renault", "rouge")
ma_voiture.afficher_info()      # Renault rouge, 0 km

# Modifier un attribut
ma_voiture.couleur = "bleu"
ma_voiture.kilometrage = 15000

ma_voiture.afficher_info()      # Renault bleu, 15000 km
