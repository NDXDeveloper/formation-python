# ============================================================================
#   Section 3.4 : Encapsulation - les conventions _ et __
#   Description : Python n'a pas de "private" ; conventions _attribut (usage
#                 interne) et __attribut (name mangling, anti-collision en héritage)
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- Un underscore : convention "usage interne" (NON imposée) ---
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde      # convention : "ne pas toucher de l'extérieur"

compte = CompteBancaire(1000)
print(compte._solde)             # 1000 — accessible : ce n'est qu'une convention

# --- Deux underscores : name mangling ---
class CompteSecurise:
    def __init__(self, solde):
        self.__solde = solde     # devient _CompteSecurise__solde

compte2 = CompteSecurise(1000)

# Accès direct impossible
try:
    print(compte2.__solde)
except AttributeError as e:
    print(f"AttributeError : {e}")

# ... mais le nom est juste transformé :
print(compte2._CompteSecurise__solde)  # 1000
print(compte2.__dict__)                 # {'_CompteSecurise__solde': 1000}

# --- Intérêt réel du mangling : éviter les collisions en héritage ---
print()

class Base:
    def __init__(self):
        self.__valeur = "base"        # -> _Base__valeur
    def get_base(self):
        return self.__valeur

class Derivee(Base):
    def __init__(self):
        super().__init__()
        self.__valeur = "derivee"     # -> _Derivee__valeur (PAS de collision)
    def get_derivee(self):
        return self.__valeur

d = Derivee()
print(f"get_base()    : {d.get_base()}")     # base (non écrasé)
print(f"get_derivee() : {d.get_derivee()}")  # derivee
print(f"__dict__      : {d.__dict__}")        # les deux attributs coexistent
