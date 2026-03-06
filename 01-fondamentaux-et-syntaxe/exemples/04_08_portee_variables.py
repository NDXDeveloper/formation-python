# ============================================================================
#   Section 4.8 : Portée des variables (scope)
#   Description : Variables locales, globales, global, LEGB
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Variables locales ---
def ma_fonction():
    x = 10  # Variable locale
    print(f"Dans la fonction : x = {x}")

ma_fonction()
# print(x)  # Erreur ! x n'existe pas en dehors

# --- Variables globales ---
print()
x = 10  # Variable globale

def afficher_x():
    print(f"x = {x}")  # On peut lire x

afficher_x()  # Affiche : x = 10
print(x)      # Affiche : 10

# --- Modification d'une variable globale (piège) ---
print()
x = 10

def modifier_x():
    x = 20  # Crée une nouvelle variable LOCALE x
    print(f"Dans la fonction : x = {x}")

modifier_x()
print(f"En dehors : x = {x}")  # x = 10 (inchangé !)

# --- Avec le mot-clé global ---
print()
x = 10

def modifier_x_global():
    global x
    x = 20
    print(f"Dans la fonction : x = {x}")

modifier_x_global()
print(f"En dehors : x = {x}")  # x = 20 (modifié !)

# --- Bonne pratique : paramètres et retour ---
print()

def incrementer(compteur):
    return compteur + 1

compteur = 0
compteur = incrementer(compteur)
print(f"compteur = {compteur}")  # 1

# --- Règle LEGB ---
print()
x = "global"

def externe():
    x = "enclosing"

    def interne():
        x = "local"
        print(x)

    interne()
    print(x)

externe()
print(x)
# Affiche : local, enclosing, global
