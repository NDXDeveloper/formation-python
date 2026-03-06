# ============================================================================
#   Section 3.1 : Classe Personne
#   Description : Présentation, anniversaire, vérification majorité
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

    def avoir_anniversaire(self):
        self.age += 1
        print(f"Joyeux anniversaire ! {self.prenom} a maintenant {self.age} ans.")

    def est_majeur(self):
        return self.age >= 18

# Créer plusieurs personnes
personne1 = Personne("Dupont", "Marie", 25)
personne2 = Personne("Martin", "Pierre", 17)

personne1.se_presenter()        # Bonjour, je m'appelle Marie Dupont et j'ai 25 ans.
personne2.se_presenter()        # Bonjour, je m'appelle Pierre Martin et j'ai 17 ans.

print(personne1.est_majeur())   # True
print(personne2.est_majeur())   # False

personne2.avoir_anniversaire()  # Joyeux anniversaire ! Pierre a maintenant 18 ans.
print(personne2.est_majeur())   # True
