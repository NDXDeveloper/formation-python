# ============================================================================
#   Section 3.4 : Propriétés - Base
#   Description : Problème d'accès direct, solution avec @property, getter
#                 et setter avec validation
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- Problème : accès direct sans contrôle ---
class CompteSansControle:
    def __init__(self, solde):
        self.solde = solde

compte = CompteSansControle(1000)
print(compte.solde)  # 1000
compte.solde = -5000  # Pas de validation !
print(compte.solde)   # -5000

# --- Solution Python : les propriétés ---
print()

class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde

    @property
    def solde(self):
        """Getter : lecture du solde"""
        return self._solde

    @solde.setter
    def solde(self, valeur):
        """Setter : modification du solde avec validation"""
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur

# Utilisation
compte = CompteBancaire(1000)
print(compte.solde)      # 1000 - Appelle le getter
compte.solde = 1500      # OK - Appelle le setter
print(compte.solde)      # 1500

try:
    compte.solde = -500  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")
