# ============================================================================
#   Section 4.10 : Fonctions comme objets de première classe
#   Description : Assigner à variable, passer en paramètre, transformer liste
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Assigner une fonction à une variable ---
def dire_bonjour(nom):
    return f"Bonjour {nom} !"

salutation = dire_bonjour
print(salutation("Alice"))  # Affiche : Bonjour Alice !

# --- Passer une fonction en paramètre ---
print()

def appliquer_operation(fonction, valeur):
    return fonction(valeur)

def doubler(x):
    return x * 2

def tripler(x):
    return x * 3

print(appliquer_operation(doubler, 5))  # Affiche : 10
print(appliquer_operation(tripler, 5))  # Affiche : 15

# --- Fonction de transformation de liste ---
print()

def transformer_liste(liste, fonction):
    resultat = []
    for element in liste:
        resultat.append(fonction(element))
    return resultat

def carre(x):
    return x ** 2

def double(x):
    return x * 2

nombres = [1, 2, 3, 4, 5]

print(transformer_liste(nombres, carre))   # [1, 4, 9, 16, 25]
print(transformer_liste(nombres, double))  # [2, 4, 6, 8, 10]
