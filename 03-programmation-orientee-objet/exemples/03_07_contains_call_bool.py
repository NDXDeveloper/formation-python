# ============================================================================
#   Section 3.3 : __contains__, __call__, __bool__
#   Description : Opérateur in, objets appelables, valeur de vérité
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

# --- __contains__ : opérateur in ---
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def __contains__(self, membre):
        return membre in self.membres

    def __len__(self):
        return len(self.membres)

equipe = Equipe("Les Développeurs")
equipe.ajouter_membre("Alice")
equipe.ajouter_membre("Bob")
equipe.ajouter_membre("Charlie")

print("Alice" in equipe)    # True
print("David" in equipe)    # False
print("Bob" not in equipe)  # False

# --- __call__ : objets appelables ---
print()

class Multiplicateur:
    def __init__(self, facteur):
        self.facteur = facteur

    def __call__(self, nombre):
        return nombre * self.facteur

doubler = Multiplicateur(2)
tripler = Multiplicateur(3)

print(doubler(5))   # 10  (5 * 2)
print(doubler(10))  # 20  (10 * 2)
print(tripler(5))   # 15  (5 * 3)

# --- __call__ : Compteur d'appels ---
print()

class CompteurAppels:
    def __init__(self, fonction):
        self.fonction = fonction
        self.nombre_appels = 0

    def __call__(self, *args, **kwargs):
        self.nombre_appels += 1
        print(f"Appel n°{self.nombre_appels}")
        return self.fonction(*args, **kwargs)

@CompteurAppels
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Alice")
saluer("Bob")
saluer("Charlie")

print(f"\nLa fonction a été appelée {saluer.nombre_appels} fois")

# --- __bool__ : valeur de vérité ---
print()

class Panier:
    def __init__(self):
        self.articles = []

    def ajouter(self, article):
        self.articles.append(article)

    def __bool__(self):
        return len(self.articles) > 0

    def __len__(self):
        return len(self.articles)

panier = Panier()

if panier:
    print("Le panier contient des articles")
else:
    print("Le panier est vide")

panier.ajouter("Pomme")

if panier:
    print("Le panier contient des articles")
else:
    print("Le panier est vide")
