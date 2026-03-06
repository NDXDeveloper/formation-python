# ============================================================================
#   Section 5.1 : Fonctions d'ordre supérieur
#   Description : Fonctions prenant des fonctions en argument, fonctions
#                 retournant des fonctions, filtrer et transformer
#   Fichier source : 01-lambda-et-fonctions-ordre-superieur.md
# ============================================================================

# --- Fonction prenant une fonction en argument ---
print("=== Appliquer une opération ===")

def appliquer_operation(nombre, operation):
    """Applique une opération sur un nombre."""
    return operation(nombre)

doubler = lambda x: x * 2
tripler = lambda x: x * 3
carre = lambda x: x ** 2

print(appliquer_operation(5, doubler))   # 10
print(appliquer_operation(5, tripler))   # 15
print(appliquer_operation(5, carre))     # 25

# --- Fonction retournant une fonction ---
print("\n=== Créer un multiplicateur ===")

def creer_multiplicateur(n):
    """Crée une fonction qui multiplie par n."""
    return lambda x: x * n

multiplier_par_2 = creer_multiplicateur(2)
multiplier_par_5 = creer_multiplicateur(5)
multiplier_par_10 = creer_multiplicateur(10)

print(multiplier_par_2(7))   # 14
print(multiplier_par_5(7))   # 35
print(multiplier_par_10(7))  # 70

# --- Filtrer une liste ---
print("\n=== Filtrer ===")

def filtrer(liste, condition):
    """Filtre une liste selon une condition."""
    resultat = []
    for element in liste:
        if condition(element):
            resultat.append(element)
    return resultat

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pairs = filtrer(nombres, lambda x: x % 2 == 0)
print(f"Nombres pairs : {pairs}")  # [2, 4, 6, 8, 10]

superieurs_a_5 = filtrer(nombres, lambda x: x > 5)
print(f"Nombres > 5 : {superieurs_a_5}")  # [6, 7, 8, 9, 10]

multiples_de_3 = filtrer(nombres, lambda x: x % 3 == 0)
print(f"Multiples de 3 : {multiples_de_3}")  # [3, 6, 9]

# --- Transformer une liste ---
print("\n=== Transformer ===")

def transformer(liste, transformation):
    """Applique une transformation à chaque élément."""
    resultat = []
    for element in liste:
        resultat.append(transformation(element))
    return resultat

nombres = [1, 2, 3, 4, 5]

doubles = transformer(nombres, lambda x: x * 2)
print(f"Doublés : {doubles}")  # [2, 4, 6, 8, 10]

carres = transformer(nombres, lambda x: x ** 2)
print(f"Carrés : {carres}")  # [1, 4, 9, 16, 25]

chaines = transformer(nombres, lambda x: f"Numéro {x}")
print(f"Chaînes : {chaines}")

# --- Composition de fonctions ---
print("\n=== Composition ===")

def composer(f, g):
    """Crée une nouvelle fonction qui applique g puis f."""
    return lambda x: f(g(x))

ajouter_5 = lambda x: x + 5
multiplier_par_2 = lambda x: x * 2

fonction_composee = composer(ajouter_5, multiplier_par_2)

print(fonction_composee(3))   # (3 * 2) + 5 = 11
print(fonction_composee(10))  # (10 * 2) + 5 = 25
