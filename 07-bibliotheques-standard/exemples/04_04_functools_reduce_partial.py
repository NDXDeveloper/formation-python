# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Module functools - reduce, partial, conversion d'unités,
#                 fusion de dictionnaires
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

from functools import reduce, partial
import operator

# --- reduce() ---
print("=== reduce() ===")

nombres = [1, 2, 3, 4, 5]

somme = reduce(lambda x, y: x + y, nombres)
print(f"Somme : {somme}")

somme2 = reduce(operator.add, nombres)
print(f"Somme (operator) : {somme2}")

produit = reduce(operator.mul, nombres)
print(f"Produit : {produit}")

maximum = reduce(lambda x, y: x if x > y else y, nombres)
print(f"Maximum : {maximum}")

somme_plus_10 = reduce(operator.add, nombres, 10)
print(f"Somme + 10 : {somme_plus_10}")

# --- Fusionner des dictionnaires ---
print("\n=== Fusionner des dictionnaires ===")

def fusionner_dictionnaires(liste_dicts):
    return reduce(
        lambda d1, d2: {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)},
        liste_dicts
    )

ventes_jour1 = {'pommes': 10, 'bananes': 5, 'oranges': 8}
ventes_jour2 = {'pommes': 12, 'bananes': 7, 'poires': 6}
ventes_jour3 = {'pommes': 8, 'oranges': 10, 'poires': 4}

ventes_totales = fusionner_dictionnaires([ventes_jour1, ventes_jour2, ventes_jour3])
print("Ventes totales :")
for fruit, quantite in sorted(ventes_totales.items()):
    print(f"  {fruit}: {quantite}")

# --- partial() ---
print("\n=== partial() ===")

def puissance(base, exposant):
    return base ** exposant

carre = partial(puissance, exposant=2)
cube = partial(puissance, exposant=3)

print(f"carre(5) = {carre(5)}")
print(f"cube(3) = {cube(3)}")

def multiplier(x, y):
    return x * y

doubler = partial(multiplier, 2)
tripler = partial(multiplier, 3)

print(f"doubler(5) = {doubler(5)}")
print(f"tripler(5) = {tripler(5)}")

# --- partial avec print ---
print("\n=== partial avec print ===")

print_erreur = partial(print, "[ERREUR]", sep=" - ")
print_info = partial(print, "[INFO]", sep=" - ")

print_erreur("Fichier introuvable")
print_info("Connexion établie")

# --- Conversion d'unités ---
print("\n=== Conversion d'unités ===")

def convertir(valeur, facteur):
    return valeur * facteur

km_vers_miles = partial(convertir, facteur=0.621371)
miles_vers_km = partial(convertir, facteur=1.60934)

def convertir_temperature(valeur, formule):
    return formule(valeur)

celsius_vers_kelvin = partial(convertir_temperature, formule=lambda c: c + 273.15)
fahrenheit_vers_celsius = partial(convertir_temperature, formule=lambda f: (f - 32) * 5/9)

print(f"100 km = {km_vers_miles(100):.2f} miles")
print(f"50 miles = {miles_vers_km(50):.2f} km")
print(f"25 C = {celsius_vers_kelvin(25):.2f} K")
print(f"77 F = {fahrenheit_vers_celsius(77):.2f} C")
