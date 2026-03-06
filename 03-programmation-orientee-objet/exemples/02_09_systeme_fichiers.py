# ============================================================================
#   Section 3.2 : Système de fichiers
#   Description : Exemple avancé combinant héritage et polymorphisme
#                 (ElementSysteme, Fichier, Dossier, FichierImage)
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

from datetime import datetime

class ElementSysteme:
    """Classe de base pour tous les éléments du système de fichiers."""

    def __init__(self, nom):
        self.nom = nom
        self.date_creation = datetime.now()

    def afficher_info(self):
        print(f"Nom : {self.nom}")
        print(f"Créé le : {self.date_creation.strftime('%d/%m/%Y %H:%M')}")

    def obtenir_type(self):
        return "Élément"


class Fichier(ElementSysteme):
    """Représente un fichier."""

    def __init__(self, nom, taille, extension):
        super().__init__(nom)
        self.taille = taille  # en Ko
        self.extension = extension

    def afficher_info(self):
        super().afficher_info()
        print(f"Type : Fichier (.{self.extension})")
        print(f"Taille : {self.taille} Ko")

    def obtenir_type(self):
        return "Fichier"

    def ouvrir(self):
        print(f"Ouverture du fichier {self.nom}.{self.extension}...")


class Dossier(ElementSysteme):
    """Représente un dossier pouvant contenir des fichiers et d'autres dossiers."""

    def __init__(self, nom):
        super().__init__(nom)
        self.contenu = []

    def ajouter(self, element):
        self.contenu.append(element)
        print(f"{element.nom} ajouté dans {self.nom}")

    def afficher_info(self):
        super().afficher_info()
        print(f"Type : Dossier")
        print(f"Contient {len(self.contenu)} éléments")

    def obtenir_type(self):
        return "Dossier"

    def lister_contenu(self):
        if not self.contenu:
            print(f"Le dossier {self.nom} est vide.")
            return

        print(f"\nContenu de '{self.nom}' :")
        print("-" * 40)
        for element in self.contenu:
            type_elem = element.obtenir_type()
            print(f"  [{type_elem}] {element.nom}")

    def calculer_taille_totale(self):
        taille = 0
        for element in self.contenu:
            if isinstance(element, Fichier):
                taille += element.taille
            elif isinstance(element, Dossier):
                taille += element.calculer_taille_totale()
        return taille


class FichierImage(Fichier):
    """Représente un fichier image avec des propriétés spécifiques."""

    def __init__(self, nom, taille, extension, largeur, hauteur):
        super().__init__(nom, taille, extension)
        self.largeur = largeur
        self.hauteur = hauteur

    def afficher_info(self):
        super().afficher_info()
        print(f"Dimensions : {self.largeur} x {self.hauteur} pixels")

    def afficher_apercu(self):
        print(f"Aperçu de l'image {self.nom} ({self.largeur}x{self.hauteur})")


# Utilisation du système
print("=== Création du système de fichiers ===\n")

# Créer des fichiers
doc1 = Fichier("rapport", 150, "pdf")
doc2 = Fichier("presentation", 300, "pptx")
image1 = FichierImage("photo_vacances", 2500, "jpg", 1920, 1080)
image2 = FichierImage("logo", 50, "png", 512, 512)

# Créer des dossiers
dossier_documents = Dossier("Documents")
dossier_images = Dossier("Images")
dossier_principal = Dossier("Mon_Ordinateur")

# Organiser les fichiers
dossier_documents.ajouter(doc1)
dossier_documents.ajouter(doc2)
dossier_images.ajouter(image1)
dossier_images.ajouter(image2)
dossier_principal.ajouter(dossier_documents)
dossier_principal.ajouter(dossier_images)

print("\n" + "="*50)
# Lister le contenu
dossier_principal.lister_contenu()
dossier_images.lister_contenu()

print("\n" + "="*50)
# Afficher les infos d'un fichier image
print("\nInformations détaillées :")
image1.afficher_info()

print("\n" + "="*50)
# Calculer la taille totale
taille_totale = dossier_principal.calculer_taille_totale()
print(f"\nTaille totale de '{dossier_principal.nom}' : {taille_totale} Ko")
