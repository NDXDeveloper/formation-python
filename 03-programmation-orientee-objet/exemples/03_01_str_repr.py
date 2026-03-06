# ============================================================================
#   Section 3.3 : __str__ et __repr__
#   Description : Représentation textuelle pour les humains et les développeurs
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

# --- __str__ : pour les humains ---
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, {self.age} ans"

    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"

personne = Personne("Alice", 30)
print(personne)         # Alice, 30 ans
print(str(personne))    # Alice, 30 ans
print(repr(personne))   # Personne('Alice', 30)

# --- Exemple avec Livre ---
print()

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return f'"{self.titre}" de {self.auteur}'

    def __repr__(self):
        return f"Livre('{self.titre}', '{self.auteur}', {self.annee})"

livre = Livre("1984", "George Orwell", 1949)

print(livre)        # "1984" de George Orwell
print(repr(livre))  # Livre('1984', 'George Orwell', 1949)

# Dans une liste, __repr__ est utilisé
livres = [livre, Livre("Le Petit Prince", "Saint-Exupéry", 1943)]
print(livres)
