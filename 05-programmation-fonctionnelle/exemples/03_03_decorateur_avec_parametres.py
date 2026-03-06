# ============================================================================
#   Section 5.3 : Décorateurs avec paramètres
#   Description : Structure à trois niveaux, repeter(), prefixe_suffixe()
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

# --- Structure à trois niveaux ---
print("=== Répéter l'exécution ===")

def repeter(nombre_fois):
    """Décorateur qui répète l'exécution d'une fonction."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            for _ in range(nombre_fois):
                resultat = fonction(*args, **kwargs)
            return resultat
        return fonction_modifiee
    return decorateur

@repeter(nombre_fois=3)
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
# Bonjour !
# Bonjour !
# Bonjour !

# --- Préfixe et suffixe ---
print("\n=== Préfixe et suffixe ===")

def prefixe_suffixe(prefixe=">>>", suffixe="<<<"):
    """Décorateur qui ajoute un préfixe et un suffixe aux messages."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            print(prefixe)
            resultat = fonction(*args, **kwargs)
            print(suffixe)
            return resultat
        return fonction_modifiee
    return decorateur

@prefixe_suffixe(prefixe="=== DÉBUT ===", suffixe="=== FIN ===")
def afficher_message(message):
    print(message)

afficher_message("Python est génial !")
# === DÉBUT ===
# Python est génial !
# === FIN ===
