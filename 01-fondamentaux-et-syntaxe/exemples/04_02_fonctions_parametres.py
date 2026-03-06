# ============================================================================
#   Section 4.2 : Fonctions avec paramètres
#   Description : Un paramètre, plusieurs paramètres, ordre des paramètres
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Un seul paramètre ---
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Alice")
saluer("Bob")
saluer("Charlie")

# --- Plusieurs paramètres ---
print()

def saluer_complet(prenom, nom):
    print(f"Bonjour {prenom} {nom} !")

saluer_complet("Alice", "Dupont")
saluer_complet("Bob", "Martin")

# --- Paramètres et calculs ---
print()

def additionner(a, b):
    somme = a + b
    print(f"{a} + {b} = {somme}")

additionner(5, 3)
additionner(10, 20)

# --- Attention à l'ordre des paramètres ---
print()

def diviser(dividende, diviseur):
    resultat = dividende / diviseur
    print(f"{dividende} / {diviseur} = {resultat}")

diviser(10, 2)   # 10 / 2 = 5.0
diviser(2, 10)   # 2 / 10 = 0.2 (ordre différent !)
