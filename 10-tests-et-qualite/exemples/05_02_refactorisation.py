# ============================================================================
#   Section 10.5 : PEP 8 et outils de linting
#   Description : Cas pratique de refactorisation - code corrige selon PEP 8
#                 avec nommage, docstrings, indentation, espaces
#   Fichier source : 05-pep8-et-linting.md
# ============================================================================

"""Module de gestion d'utilisateurs.

Exemple de code refactorise selon PEP 8.
Avant (ne suit pas PEP 8) :
    import sys,os
    from datetime import *
    def calc(x,y,z):
     result=x+y;
     if result>z:return result
     else:return 0
    class user:
     def __init__(self,n,a):self.name=n;self.age=a
     def isAdult(self):
      if self.age>=18:return True
      else:return False
"""

import os
import sys
from datetime import datetime


def calculer_resultat(valeur_x, valeur_y, seuil):
    """Calcule un resultat base sur un seuil.

    Args:
        valeur_x (int): Premiere valeur.
        valeur_y (int): Deuxieme valeur.
        seuil (int): Valeur seuil.

    Returns:
        int: Le resultat du calcul, ou 0 si sous le seuil.
    """
    resultat = valeur_x + valeur_y

    if resultat > seuil:
        return resultat
    else:
        return 0


class Utilisateur:
    """Represente un utilisateur.

    Attributes:
        nom (str): Le nom de l'utilisateur.
        age (int): L'age de l'utilisateur.
    """

    def __init__(self, nom, age):
        """Initialise un utilisateur.

        Args:
            nom (str): Le nom.
            age (int): L'age.
        """
        self.nom = nom
        self.age = age

    def est_majeur(self):
        """Verifie si l'utilisateur est majeur.

        Returns:
            bool: True si majeur, False sinon.
        """
        return self.age >= 18


# --- Demonstration ---
print("=== Refactorisation PEP 8 ===")

# Fonction refactorisee
print(f"calculer_resultat(10, 20, 25) = {calculer_resultat(10, 20, 25)}")
print(f"calculer_resultat(10, 20, 50) = {calculer_resultat(10, 20, 50)}")

# Classe refactorisee
alice = Utilisateur("Alice", 25)
bob = Utilisateur("Bob", 16)

print(f"\n{alice.nom} (age: {alice.age}) est majeur : {alice.est_majeur()}")
print(f"{bob.nom} (age: {bob.age}) est majeur : {bob.est_majeur()}")

# Utilisation correcte de datetime (au lieu de from datetime import *)
print(f"\nDate actuelle : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"Python path : {sys.executable}")
print(f"Repertoire courant : {os.getcwd()}")
