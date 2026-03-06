# ============================================================================
#   Section 5.5 : Curryfication et functools.partial
#   Description : Concept de curryfication, curryfication générique,
#                 application pratique avec URL, functools.partial
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

from functools import partial

# --- Concept de base ---
print("=== Curryfication ===")

# Fonction normale
def additionner(a, b):
    return a + b

print(additionner(3, 5))  # 8

# Version currifiée
def additionner_currifie(a):
    def ajouter_b(b):
        return a + b
    return ajouter_b

ajouter_3 = additionner_currifie(3)
print(ajouter_3(5))   # 8
print(ajouter_3(10))  # 13

# --- Curryfication générique ---
print("\n=== Curryfication générique ===")

def curryfier(fonction, *args_fixes):
    """Transforme une fonction en version currifiée."""
    def fonction_currifiee(*args_supplementaires):
        return fonction(*args_fixes, *args_supplementaires)
    return fonction_currifiee

def multiplier(a, b, c):
    return a * b * c

multiplier_par_2 = curryfier(multiplier, 2)
print(multiplier_par_2(3, 4))  # 2 * 3 * 4 = 24

multiplier_par_2_et_3 = curryfier(multiplier, 2, 3)
print(multiplier_par_2_et_3(5))  # 2 * 3 * 5 = 30

# --- Application pratique ---
print("\n=== URLs ===")

def creer_url(protocole, domaine, chemin):
    """Construit une URL."""
    return f"{protocole}://{domaine}/{chemin}"

creer_url_https = curryfier(creer_url, "https")
creer_url_site = curryfier(creer_url, "https", "example.com")

print(creer_url_https("example.com", "api/users"))  # https://example.com/api/users
print(creer_url_site("products"))  # https://example.com/products

# --- functools.partial ---
print("\n=== functools.partial ===")

def puissance(base, exposant):
    return base ** exposant

carre = partial(puissance, exposant=2)
cube = partial(puissance, exposant=3)

print(carre(5))  # 25
print(cube(3))   # 27

# Avec print
print_avec_prefix = partial(print, "[LOG]", sep=" - ")
print_avec_prefix("Message important")  # [LOG] - Message important
