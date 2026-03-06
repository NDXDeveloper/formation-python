# ============================================================================
#   Section 10.5 : PEP 8 et outils de linting
#   Description : Demonstration des regles PEP 8 - indentation, nommage,
#                 espaces, imports, comparaisons, lignes vides
#   Fichier source : 05-pep8-et-linting.md
# ============================================================================

"""Module de demonstration des regles PEP 8."""

# --- Regle 1 : Indentation (4 espaces) ---
# --- Regle 5 : Espaces autour des operateurs ---

print("=== Regles de base PEP 8 ===")


def calculer_total(prix, quantite, taux_taxe):
    """Calcule le total avec taxe (bon style PEP 8)."""
    sous_total = prix * quantite
    total = sous_total * taux_taxe
    return total


resultat = calculer_total(10.0, 5, 1.20)
print(f"calculer_total(10.0, 5, 1.20) = {resultat}")


# --- Regle 6 : Nommage ---

# Variables et fonctions : snake_case
ma_variable = 42
nombre_total = 100


def calculer_moyenne(notes):
    """Calcule la moyenne des notes."""
    return sum(notes) / len(notes)


# Classes : PascalCase
class CompteBancaire:
    """Classe de compte bancaire."""
    pass


class GestionnaireUtilisateurs:
    """Classe de gestionnaire."""
    pass


# Constantes : UPPER_CASE
PI = 3.14159
MAX_CONNEXIONS = 100
CHEMIN_CONFIG = "/etc/config"

print(f"\nma_variable = {ma_variable}")
print(f"PI = {PI}")
print(f"MAX_CONNEXIONS = {MAX_CONNEXIONS}")
print(f"calculer_moyenne([10, 15, 20]) = {calculer_moyenne([10, 15, 20])}")


# --- Regle 7 : Noms significatifs ---
print("\n=== Noms significatifs ===")

nombre_utilisateurs = 42
prix_total = calculer_total(10.0, 5, 1.0)
print(f"nombre_utilisateurs = {nombre_utilisateurs}")
print(f"prix_total = {prix_total}")


# --- Regle 8 : Comparaisons ---
print("\n=== Comparaisons PEP 8 ===")

variable = None
# is / is not pour None
if variable is None:
    print("variable is None : True")

variable = "valeur"
if variable is not None:
    print(f"variable is not None : True (variable='{variable}')")

# Test direct des collections
ma_liste = [1, 2, 3]
if ma_liste:  # Vrai si la liste n'est pas vide
    print(f"ma_liste est non vide : {ma_liste}")

liste_vide = []
if not liste_vide:  # Vrai si la liste est vide
    print("liste_vide est vide : True")


# --- Exemple complet PEP 8 ---
print("\n=== Exemple complet PEP 8 ===")

TAUX_INTERET = 0.03


class Compte:
    """Represente un compte bancaire simple.

    Attributes:
        solde (float): Le solde actuel du compte.
    """

    def __init__(self, solde_initial=0):
        """Initialise un nouveau compte.

        Args:
            solde_initial (float): Le solde de depart. Par defaut 0.
        """
        self.solde = solde_initial

    def deposer(self, montant):
        """Depose de l'argent sur le compte.

        Args:
            montant (float): Le montant a deposer.

        Returns:
            float: Le nouveau solde.

        Raises:
            ValueError: Si le montant est negatif.
        """
        if montant < 0:
            raise ValueError("Le montant doit etre positif")

        self.solde += montant
        return self.solde


compte = Compte(1000)
compte.deposer(500)
print(f"Compte : solde = {compte.solde}")
print(f"Taux d'interet : {TAUX_INTERET}")
interet = compte.solde * TAUX_INTERET
print(f"Interet annuel : {interet}")
