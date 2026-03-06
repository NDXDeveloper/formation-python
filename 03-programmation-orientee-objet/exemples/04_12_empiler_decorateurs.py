# ============================================================================
#   Section 3.4 : Empiler plusieurs décorateurs
#   Description : Appliquer gras, italique, souligné sur une même fonction,
#                 décorateur de classe avec ID unique
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- Empiler des décorateurs ---
def gras(fonction):
    def wrapper():
        return "<b>" + fonction() + "</b>"
    return wrapper

def italique(fonction):
    def wrapper():
        return "<i>" + fonction() + "</i>"
    return wrapper

def souligne(fonction):
    def wrapper():
        return "<u>" + fonction() + "</u>"
    return wrapper

@gras
@italique
@souligne
def texte():
    return "Python"

print(texte())  # <b><i><u>Python</u></i></b>

# --- Décorateur de classe ---
print()

def ajouter_id(classe):
    """Ajoute un ID unique à chaque instance"""
    classe_originale_init = classe.__init__
    compteur = [0]

    def nouvelle_init(self, *args, **kwargs):
        compteur[0] += 1
        self.id = compteur[0]
        classe_originale_init(self, *args, **kwargs)

    classe.__init__ = nouvelle_init
    return classe

@ajouter_id
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit #{self.id} : {self.nom} - {self.prix}€"

p1 = Produit("Livre", 15)
p2 = Produit("Stylo", 2)
p3 = Produit("Cahier", 5)

print(p1)  # Produit #1 : Livre - 15€
print(p2)  # Produit #2 : Stylo - 2€
print(p3)  # Produit #3 : Cahier - 5€
