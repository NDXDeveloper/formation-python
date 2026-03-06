# ============================================================================
#   Section 5.3 : Décorateurs avec arguments de fonction
#   Description : *args et **kwargs pour accepter tous les arguments,
#                 décorateur universel compatible avec toute fonction
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

# --- Décorateur universel avec *args et **kwargs ---
print("=== Décorateur avec arguments ===")

def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("--- Début ---")
        resultat = fonction(*args, **kwargs)
        print("--- Fin ---")
        return resultat
    return fonction_modifiee

@mon_decorateur
def saluer(nom):
    print(f"Bonjour {nom} !")

@mon_decorateur
def additionner(a, b):
    resultat = a + b
    print(f"{a} + {b} = {resultat}")
    return resultat

# Utilisation
saluer("Alice")
# --- Début ---
# Bonjour Alice !
# --- Fin ---

print()

total = additionner(5, 3)
# --- Début ---
# 5 + 3 = 8
# --- Fin ---
print(f"Total : {total}")  # Total : 8
