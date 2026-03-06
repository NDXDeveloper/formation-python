# ============================================================================
#   Section 3.1 : Bonnes pratiques
#   Description : CamelCase, initialiser dans __init__, méthodes pour modifier,
#                 docstrings, classe Etudiant avec notes et moyenne
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

# --- 1. Initialiser tous les attributs dans __init__ ---
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.pages_lues = 0
        self.termine = False

livre = Livre("Python", "Guido")
print(f"{livre.titre} par {livre.auteur}, pages lues: {livre.pages_lues}")

# --- 2. Utiliser des méthodes pour modifier les attributs ---
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def modifier_dimensions(self, nouvelle_largeur, nouvelle_hauteur):
        if nouvelle_largeur > 0 and nouvelle_hauteur > 0:
            self.largeur = nouvelle_largeur
            self.hauteur = nouvelle_hauteur
        else:
            print("Les dimensions doivent être positives !")

    def calculer_surface(self):
        return self.largeur * self.hauteur

rect = Rectangle(5, 3)
print(f"Surface : {rect.calculer_surface()}")  # 15
rect.modifier_dimensions(10, 7)
print(f"Nouvelle surface : {rect.calculer_surface()}")  # 70

# --- 3. Documentation avec docstrings ---
print()

class Etudiant:
    """
    Classe représentant un étudiant.

    Attributs:
        nom (str): Le nom de famille de l'étudiant
        prenom (str): Le prénom de l'étudiant
        notes (list): Liste des notes obtenues
    """

    def __init__(self, nom, prenom):
        """Initialise un nouvel étudiant."""
        self.nom = nom
        self.prenom = prenom
        self.notes = []

    def ajouter_note(self, note):
        """Ajoute une note à l'étudiant (entre 0 et 20)."""
        if 0 <= note <= 20:
            self.notes.append(note)
        else:
            print("La note doit être entre 0 et 20.")

    def moyenne(self):
        """Calcule la moyenne des notes."""
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

etudiant = Etudiant("Dupont", "Marie")
etudiant.ajouter_note(15)
etudiant.ajouter_note(12)
etudiant.ajouter_note(18)
print(f"{etudiant.prenom} {etudiant.nom}: moyenne = {etudiant.moyenne()}")
