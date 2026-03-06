# ============================================================================
#   Section 5.5 : Variables libres et nonlocal
#   Description : Inspecter les variables libres, variables locales vs
#                 libres, compteur avec nonlocal, différence avec/sans
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Inspecter les variables libres ---
print("=== Variables libres ===")

def creer_compteur(debut):
    def incrementer():
        return debut + 1
    return incrementer

compteur = creer_compteur(10)

print(compteur.__closure__)  # (<cell at 0x...: int object at 0x...>,)
print(compteur.__code__.co_freevars)  # ('debut',)
print(compteur.__closure__[0].cell_contents)  # 10

# --- Variables locales vs variables libres ---
print("\n=== Locales vs libres ===")

def fonction_externe(x):  # x sera une variable libre
    y = 10  # y sera aussi une variable libre

    def fonction_interne(z):  # z est une variable locale
        return x + y + z

    return fonction_interne

f = fonction_externe(5)
print(f(3))  # 18 (5 + 10 + 3)
print(f.__code__.co_freevars)  # ('x', 'y')

# --- Compteur avec nonlocal ---
print("\n=== Compteur ===")

def creer_compteur():
    """Crée un compteur qui s'incrémente."""
    compte = 0

    def incrementer():
        nonlocal compte
        compte += 1
        return compte

    return incrementer

compteur1 = creer_compteur()
print(compteur1())  # 1
print(compteur1())  # 2
print(compteur1())  # 3

# Chaque compteur est indépendant
compteur2 = creer_compteur()
print(compteur2())  # 1
print(compteur1())  # 4

# --- Différence avec/sans nonlocal ---
print("\n=== Sans nonlocal ===")

def exemple_nonlocal():
    x = 10

    def modifier_sans_nonlocal():
        x = 20  # Crée une nouvelle variable locale
        print(f"Dans la fonction : x = {x}")

    modifier_sans_nonlocal()
    print(f"Après la fonction : x = {x}")  # x vaut toujours 10

exemple_nonlocal()

print("\n=== Avec nonlocal ===")

def exemple_avec_nonlocal():
    x = 10

    def modifier_avec_nonlocal():
        nonlocal x
        x = 20
        print(f"Dans la fonction : x = {x}")

    modifier_avec_nonlocal()
    print(f"Après la fonction : x = {x}")  # x vaut maintenant 20

exemple_avec_nonlocal()
