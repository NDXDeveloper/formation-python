# ============================================================================
#   Section 4.6 : *args et **kwargs
#   Description : Arguments positionnels variables, arguments nommés variables,
#                 combinaison complète
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- *args : arguments positionnels variables ---
def additionner(*nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total

print(additionner(1, 2, 3))           # Affiche : 6
print(additionner(10, 20, 30, 40))    # Affiche : 100
print(additionner(5))                  # Affiche : 5

# --- **kwargs : arguments nommés variables ---
print()

def afficher_infos(**informations):
    for cle, valeur in informations.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=25, ville="Paris")

# --- Combiner paramètres normaux, *args et **kwargs ---
print()

def fonction_complete(param1, param2, *args, option1="défaut", **kwargs):
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    print(f"args: {args}")
    print(f"option1: {option1}")
    print(f"kwargs: {kwargs}")

fonction_complete(1, 2, 3, 4, 5, option1="test", extra1="a", extra2="b")
