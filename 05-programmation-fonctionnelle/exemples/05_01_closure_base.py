# ============================================================================
#   Section 5.5 : Qu'est-ce qu'une closure ?
#   Description : Closure simple (salutation), multiplicateur,
#                 chaque closure garde sa propre copie des variables
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Premier exemple simple ---
print("=== Closure salutation ===")

def creer_salutation(salut):
    """Fonction externe qui crée une closure."""

    def saluer(nom):
        """Fonction interne (la closure)."""
        return f"{salut} {nom} !"

    return saluer

# Créer deux fonctions avec des salutations différentes
saluer_fr = creer_salutation("Bonjour")
saluer_en = creer_salutation("Hello")

print(saluer_fr("Alice"))  # Bonjour Alice !
print(saluer_en("Bob"))    # Hello Bob !

# --- Multiplicateur ---
print("\n=== Multiplicateur ===")

def creer_multiplicateur(facteur):
    """Crée une fonction qui multiplie par un facteur donné."""

    def multiplier(nombre):
        return nombre * facteur

    return multiplier

double = creer_multiplicateur(2)
triple = creer_multiplicateur(3)
dizaine = creer_multiplicateur(10)

print(double(5))    # 10
print(triple(5))    # 15
print(dizaine(5))   # 50
