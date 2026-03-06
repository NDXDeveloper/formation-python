# ============================================================================
#   Section 3.3 : __iter__ et __next__
#   Description : Rendre un objet itérable, compteur, bibliothèque
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

# --- Itérateur avec __iter__ et __next__ ---
class Compte:
    def __init__(self):
        self.valeur = 0

    def __iter__(self):
        self.valeur = 0
        return self

    def __next__(self):
        if self.valeur >= 5:
            raise StopIteration
        self.valeur += 1
        return self.valeur

compteur = Compte()
for nombre in compteur:
    print(nombre)
# 1, 2, 3, 4, 5

# --- Itérer sur une collection ---
print()

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def __iter__(self):
        return iter(self.livres)

    def __len__(self):
        return len(self.livres)

biblio = Bibliotheque()
biblio.ajouter_livre("1984")
biblio.ajouter_livre("Le Petit Prince")
biblio.ajouter_livre("Harry Potter")

for livre in biblio:
    print(f"- {livre}")
