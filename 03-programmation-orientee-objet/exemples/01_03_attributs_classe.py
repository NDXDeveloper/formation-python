# ============================================================================
#   Section 3.1 : Attributs de classe
#   Description : Attributs partagés par toutes les instances vs attributs
#                 d'instance propres à chaque objet
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Chien:
    # Attribut de classe
    espece = "Canis familiaris"
    nombre_pattes = 4

    def __init__(self, nom, age):
        # Attributs d'instance
        self.nom = nom
        self.age = age

chien1 = Chien("Rex", 5)
chien2 = Chien("Bella", 3)

print(chien1.espece)        # Canis familiaris
print(chien2.espece)        # Canis familiaris
print(Chien.espece)         # Canis familiaris
print(Chien.nombre_pattes)  # 4
