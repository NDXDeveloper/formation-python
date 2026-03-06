# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Traceback (trace d'execution), pprint (affichage elegant),
#                 decorateur de debogage, module inspect (introspection)
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

import traceback
from pprint import pprint
import inspect

# ==========================================
# 1. Traceback - Trace d'execution
# ==========================================
print("=== Traceback ===\n")

def fonction_a():
    fonction_b()

def fonction_b():
    fonction_c()

def fonction_c():
    x = 1 / 0  # Erreur

try:
    fonction_a()
except Exception as e:
    print("Une erreur s'est produite !")
    traceback.print_exc()

# ==========================================
# 2. pprint - Affichage elegant
# ==========================================
print("\n=== pprint ===\n")

donnees_complexes = {
    'utilisateurs': [
        {'nom': 'Alice', 'age': 25, 'ville': 'Paris'},
        {'nom': 'Bob', 'age': 30, 'ville': 'Lyon'},
        {'nom': 'Charlie', 'age': 35, 'ville': 'Marseille'}
    ],
    'configuration': {
        'debug': True,
        'timeout': 30,
        'options': ['option1', 'option2', 'option3']
    }
}

print("Affichage standard:")
print(donnees_complexes)

print("\nAffichage avec pprint:")
pprint(donnees_complexes, indent=2, width=60)

# ==========================================
# 3. Decorateur de debogage
# ==========================================
print("\n=== Decorateur de debogage ===\n")

def debug_function(func):
    """Decorateur qui affiche les appels de fonction."""
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        print(f"  Arguments : {args}")
        print(f"  Arguments nommes : {kwargs}")
        resultat = func(*args, **kwargs)
        print(f"  Resultat : {resultat}")
        return resultat
    return wrapper

@debug_function
def addition(a, b):
    return a + b

@debug_function
def saluer(nom, message="Bonjour"):
    return f"{message} {nom}"

addition(5, 3)
print()
saluer("Alice", message="Salut")

# ==========================================
# 4. Module inspect - Introspection
# ==========================================
print("\n=== Module inspect ===\n")

def ma_fonction(param1, param2):
    """Cette fonction fait quelque chose."""
    fonction_actuelle = inspect.currentframe().f_code.co_name
    print(f"  Fonction actuelle : {fonction_actuelle}")

    pile = inspect.stack()
    print(f"  Appelee depuis : {pile[1].function}")

    variables_locales = inspect.currentframe().f_locals
    # Filtrer pour un affichage propre
    vars_simples = {k: v for k, v in variables_locales.items()
                    if k in ('param1', 'param2', 'fonction_actuelle')}
    print(f"  Variables locales : {vars_simples}")

    return param1 + param2

def fonction_principale():
    resultat = ma_fonction(10, 20)
    return resultat

resultat = fonction_principale()
print(f"  Resultat : {resultat}")
