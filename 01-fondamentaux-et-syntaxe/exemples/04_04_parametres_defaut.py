# ============================================================================
#   Section 4.4 : Paramètres par défaut
#   Description : Valeurs par défaut, puissance, info avec ville par défaut
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Saluer avec message par défaut ---
def saluer(nom, message="Bonjour"):
    print(f"{message} {nom} !")

saluer("Alice")              # Utilise la valeur par défaut
saluer("Bob", "Bonsoir")     # Remplace la valeur par défaut

# --- Puissance avec exposant par défaut ---
print()

def puissance(nombre, exposant=2):
    return nombre ** exposant

print(puissance(5))        # 5^2 = 25
print(puissance(5, 3))     # 5^3 = 125
print(puissance(2, 10))    # 2^10 = 1024

# --- Info avec ville par défaut ---
print()

def afficher_info(nom, age, ville="Paris"):
    print(f"{nom}, {age} ans, habite à {ville}")

afficher_info("Alice", 25)              # Paris par défaut
afficher_info("Bob", 30, "Lyon")        # Ville spécifiée
