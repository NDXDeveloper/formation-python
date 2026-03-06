# ============================================================================
#   Section 3.4 : Trio @property, @setter, @deleter
#   Description : Temperature avec validation (zéro absolu), Personne avec
#                 deleter
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- Temperature avec setter ---
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        if valeur < -273.15:
            raise ValueError("Température en dessous du zéro absolu !")
        self._celsius = valeur

temp = Temperature(25)
temp.celsius = 30       # OK
print(temp.celsius)     # 30

try:
    temp.celsius = -300  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")

# --- Personne avec deleter ---
print()

class Personne:
    def __init__(self, nom):
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur

    @nom.deleter
    def nom(self):
        print(f"Suppression du nom : {self._nom}")
        self._nom = None

personne = Personne("Alice")
print(personne.nom)    # Alice
del personne.nom       # Suppression du nom : Alice
print(personne.nom)    # None
