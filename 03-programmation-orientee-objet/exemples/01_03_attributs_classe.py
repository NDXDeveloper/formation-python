# ============================================================================
#   Section 3.1 : Attributs de classe
#   Description : Attributs partagés par toutes les instances vs attributs
#                 d'instance propres à chaque objet ; piège des mutables
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Chien:
    # Attribut de classe
    espece = "Canis familiaris"
    nombre_pattes = 4

    def __init__(self, nom, age):
        # Attributs d'instance
        self.nom = nom
        self.age = age

chien1 = Chien("Rex", 5)
chien2 = Chien("Bella", 3)

print(chien1.espece)        # Canis familiaris
print(chien2.espece)        # Canis familiaris
print(Chien.espece)         # Canis familiaris
print(Chien.nombre_pattes)  # 4

# --- ⚠️ Piège : un attribut de classe MUTABLE est partagé par toutes les instances ---
print()

class Panier:
    articles = []          # ❌ attribut de CLASSE, partagé par toutes les instances !

p1 = Panier()
p2 = Panier()
p1.articles.append("pomme")
print(p2.articles)         # ['pomme'] — p2 est affecté lui aussi !

# --- ✅ La bonne pratique : initialiser la collection dans __init__ ---
print()

class PanierCorrect:
    def __init__(self):
        self.articles = []   # propre à CHAQUE instance

p3 = PanierCorrect()
p4 = PanierCorrect()
p3.articles.append("pomme")
print(p3.articles)         # ['pomme']
print(p4.articles)         # [] — indépendant
