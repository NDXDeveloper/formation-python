# ============================================================================
#   Section 4.9 : Fonctions imbriquées et closures
#   Description : Fonctions dans des fonctions, closures pour créer
#                 des fonctions personnalisées
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Fonctions imbriquées ---
def fonction_externe():
    print("Dans fonction_externe")

    def fonction_interne():
        print("Dans fonction_interne")

    fonction_interne()

fonction_externe()

# --- Closures ---
print()

def creer_salutation(salut):
    def saluer(nom):
        return f"{salut} {nom} !"

    return saluer

# Créer des fonctions personnalisées
bonjour = creer_salutation("Bonjour")
bonsoir = creer_salutation("Bonsoir")
hello = creer_salutation("Hello")

print(bonjour("Alice"))   # Affiche : Bonjour Alice !
print(bonsoir("Bob"))     # Affiche : Bonsoir Bob !
print(hello("Charlie"))   # Affiche : Hello Charlie !
