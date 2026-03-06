# ============================================================================
#   Section 4.1 : Créer une fonction simple
#   Description : def, appel, réutilisation
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Premier exemple ---
def dire_bonjour():
    print("Bonjour !")
    print("Comment allez-vous ?")

# Appeler (exécuter) la fonction
dire_bonjour()

# --- Réutilisation ---
print()

def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
dire_bonjour()
dire_bonjour()
