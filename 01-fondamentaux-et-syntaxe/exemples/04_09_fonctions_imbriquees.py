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

# --- nonlocal : modifier une variable de la fonction englobante ---
print()

def compteur():
    total = 0  # variable de la fonction englobante

    def incrementer():
        nonlocal total  # modifie le total de compteur(), pas une nouvelle variable
        total += 1
        return total

    print(incrementer())  # 1
    print(incrementer())  # 2
    print(incrementer())  # 3

compteur()
