# ============================================================================
#   Section 7.3 : Les modules math, random et statistics
#   Description : Module random - nombres aléatoires, choix, mélange,
#                 seed pour reproductibilité, distributions, jeu de cartes
#   Fichier source : 03-math-random-statistics.md
# ============================================================================

import random

# Seed fixe pour résultats reproductibles dans les tests
random.seed(42)

# --- Nombres aléatoires de base ---
print("=== Nombres aléatoires de base ===")
print(f"random() = {random.random():.4f}")
print(f"uniform(1.0, 10.0) = {random.uniform(1.0, 10.0):.4f}")
print(f"randint(1, 10) = {random.randint(1, 10)}")
print(f"randrange(0, 100, 5) = {random.randrange(0, 100, 5)}")

# --- Lancer de dés ---
print("\n=== Lancer de dés ===")

random.seed(42)

def lancer_de(faces=6):
    return random.randint(1, faces)

def lancer_plusieurs_des(nombre, faces=6):
    return [lancer_de(faces) for _ in range(nombre)]

print(f"Résultat du dé : {lancer_de()}")
des = lancer_plusieurs_des(2)
print(f"Résultat des dés : {des}")
print(f"Total : {sum(des)}")
print(f"Dé à 20 faces : {lancer_de(20)}")

# --- Choix aléatoires ---
print("\n=== Choix aléatoires ===")

random.seed(42)
couleurs = ["rouge", "bleu", "vert", "jaune", "noir", "blanc"]

print(f"choice : {random.choice(couleurs)}")
print(f"choices(k=3) : {random.choices(couleurs, k=3)}")
print(f"sample(k=3) : {random.sample(couleurs, k=3)}")

# Choix avec poids
elements = ["A", "B", "C"]
poids = [0.5, 0.3, 0.2]
resultats = random.choices(elements, weights=poids, k=10)
print(f"choices avec poids : {resultats}")

# --- Tirage au sort ---
print("\n=== Tirage au sort ===")

random.seed(42)
participants = ["Alice", "Bob", "Charlie", "David", "Emma", "Fanny"]
print(f"Participants : {participants}")

gagnant = random.sample(participants, 1)
print(f"Gagnant : {gagnant[0]}")

random.seed(42)
gagnants = random.sample(participants, 3)
print(f"Podium : {gagnants}")

# --- Mélanger ---
print("\n=== Mélanger (shuffle) ===")

random.seed(42)
cartes = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7"]
print(f"Ordre original : {cartes}")

random.shuffle(cartes)
print(f"Après mélange : {cartes}")

# Garder l'original
cartes_originales = ["As", "Roi", "Dame", "Valet"]
cartes_melangees = cartes_originales.copy()
random.shuffle(cartes_melangees)
print(f"Original : {cartes_originales}")
print(f"Mélangé : {cartes_melangees}")

# --- Jeu de cartes ---
print("\n=== Jeu de cartes ===")

random.seed(42)

class PaquetDeCartes:
    def __init__(self):
        couleurs = ["P", "C", "K", "T"]  # Pique, Coeur, Carreau, Trefle
        valeurs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]
        self.cartes = [f"{v}{c}" for c in couleurs for v in valeurs]
        self.melanger()

    def melanger(self):
        random.shuffle(self.cartes)
        print("Paquet mélangé")

    def tirer(self, nombre=1):
        if nombre > len(self.cartes):
            return "Plus assez de cartes!"
        return [self.cartes.pop() for _ in range(nombre)]

    def cartes_restantes(self):
        return len(self.cartes)

paquet = PaquetDeCartes()
print(f"Cartes restantes : {paquet.cartes_restantes()}")

main_tiree = paquet.tirer(5)
print(f"Main tirée : {main_tiree}")
print(f"Cartes restantes : {paquet.cartes_restantes()}")

# --- Seed pour reproductibilité ---
print("\n=== Seed (reproductibilité) ===")

random.seed(42)
serie1 = [random.randint(1, 100) for _ in range(5)]
print(f"Série 1 (seed=42) : {serie1}")

random.seed(42)
serie2 = [random.randint(1, 100) for _ in range(5)]
print(f"Série 2 (seed=42) : {serie2}")
print(f"Identiques ? {serie1 == serie2}")

# --- Distributions ---
print("\n=== Distributions ===")

random.seed(42)
print(f"gauss(0, 1) = {random.gauss(0, 1):.4f}")
print(f"normalvariate(100, 15) = {random.normalvariate(100, 15):.2f}")
print(f"triangular(0, 10, 5) = {random.triangular(0, 10, 5):.4f}")
print(f"expovariate(1.5) = {random.expovariate(1.5):.4f}")
