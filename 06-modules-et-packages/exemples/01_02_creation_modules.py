# ============================================================================
#   Section 6.1 : Création de modules personnalisés
#   Description : Créer un module operations.py et un module geometrie.py,
#                 les importer et les utiliser
#   Fichier source : 01-importation-et-creation-modules.md
# ============================================================================

from pathlib import Path
import importlib
import sys

# --- Créer le module operations.py dans un sous-dossier temporaire ---
print("=== Module operations ===")

dossier_temp = Path('_temp_modules')
dossier_temp.mkdir(exist_ok=True)

# Écrire le module operations.py
(dossier_temp / 'operations.py').write_text('''\
def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait b de a."""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres."""
    return a * b

def division(a, b):
    """Divise a par b."""
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

PI = 3.14159
''', encoding='utf-8')

# Ajouter au path pour pouvoir l'importer
sys.path.insert(0, str(dossier_temp))

import operations

resultat1 = operations.addition(10, 5)
print(f"10 + 5 = {resultat1}")

resultat2 = operations.multiplication(7, 3)
print(f"7 x 3 = {resultat2}")

print(f"Valeur de PI : {operations.PI}")

# --- Créer le module geometrie.py ---
print("\n=== Module geometrie ===")

(dossier_temp / 'geometrie.py').write_text('''\
class Rectangle:
    """Classe représentant un rectangle."""
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

class Cercle:
    """Classe représentant un cercle."""
    PI = 3.14159

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return self.PI * self.rayon ** 2

    def circonference(self):
        return 2 * self.PI * self.rayon
''', encoding='utf-8')

from geometrie import Rectangle, Cercle

rect = Rectangle(5, 3)
print(f"Aire du rectangle : {rect.aire()}")
print(f"Périmètre du rectangle : {rect.perimetre()}")

cercle = Cercle(7)
print(f"Aire du cercle : {cercle.aire()}")
print(f"Circonférence du cercle : {cercle.circonference()}")

# Nettoyage
sys.path.pop(0)
import shutil
shutil.rmtree(dossier_temp)
