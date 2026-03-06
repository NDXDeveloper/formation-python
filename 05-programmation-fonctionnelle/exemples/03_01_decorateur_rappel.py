# ============================================================================
#   Section 5.3 : Rappel - Qu'est-ce qu'un décorateur ?
#   Description : Décorateur basique sans @, puis avec syntaxe @, ajout de
#                 messages avant et après l'exécution
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

# --- Fonction simple ---
print("=== Fonction simple ===")

def dire_bonjour():
    print("Bonjour !")

dire_bonjour()  # Affiche : Bonjour !

# --- Avec un décorateur basique (sans @) ---
print("\n=== Décorateur sans @ ===")

def mon_decorateur(fonction):
    """Décorateur qui ajoute des messages avant et après."""
    def fonction_modifiee():
        print("--- Début ---")
        fonction()
        print("--- Fin ---")
    return fonction_modifiee

def dire_bonjour():
    print("Bonjour !")

# Application du décorateur
dire_bonjour = mon_decorateur(dire_bonjour)
dire_bonjour()
# --- Début ---
# Bonjour !
# --- Fin ---

# --- Syntaxe avec @ ---
print("\n=== Syntaxe @ ===")

def mon_decorateur(fonction):
    def fonction_modifiee():
        print("--- Début ---")
        fonction()
        print("--- Fin ---")
    return fonction_modifiee

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
# --- Début ---
# Bonjour !
# --- Fin ---
