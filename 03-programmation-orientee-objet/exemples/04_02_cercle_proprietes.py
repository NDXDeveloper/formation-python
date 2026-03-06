# ============================================================================
#   Section 3.4 : Propriétés calculées (read-only)
#   Description : Cercle avec diamètre, circonférence et surface calculés
#                 automatiquement
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    @property
    def diametre(self):
        return self.rayon * 2

    @property
    def circonference(self):
        return 2 * 3.14159 * self.rayon

    @property
    def surface(self):
        return 3.14159 * self.rayon ** 2

# Utilisation
cercle = Cercle(5)
print(f"Rayon : {cercle.rayon}")              # 5
print(f"Diamètre : {cercle.diametre}")        # 10
print(f"Circonférence : {cercle.circonference}")  # 31.4159
print(f"Surface : {cercle.surface}")          # 78.53975

# Propriétés read-only
try:
    cercle.surface = 100
except AttributeError as e:
    print(f"Erreur : {e}")
