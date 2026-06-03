# ============================================================================
#   Section 3.2 : Héritage multiple
#   Description : Hériter de plusieurs classes, MRO (Method Resolution Order)
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

# --- Héritage multiple ---
class Volant:
    def voler(self):
        print("Je vole dans les airs !")


class Nageant:
    def nager(self):
        print("Je nage dans l'eau !")


class Canard(Volant, Nageant):
    def __init__(self, nom):
        self.nom = nom

    def caqueter(self):
        print(f"{self.nom} fait : Coin coin !")


donald = Canard("Donald")
donald.caqueter()  # Méthode propre
donald.voler()     # Héritée de Volant
donald.nager()     # Héritée de Nageant

# --- MRO - Résolution des conflits ---
print()

class A:
    def methode(self):
        print("Méthode de A")

class B:
    def methode(self):
        print("Méthode de B")

class C(A, B):
    pass

obj = C()
obj.methode()  # Méthode de A (A est mentionné en premier)

# Voir l'ordre de résolution des méthodes
print(C.__mro__)

# --- super() suit le MRO, pas "le parent direct" ---
print()

class Salut_A:
    def saluer(self):
        print("A")
        super().saluer()      # depuis une instance de Salut_C, appelle Salut_B !

class Salut_B:
    def saluer(self):
        print("B")             # pas de super() ici -> la chaîne s'arrête

class Salut_C(Salut_A, Salut_B):
    pass

Salut_C().saluer()   # Affiche : A puis B  (MRO : C -> A -> B -> object)
