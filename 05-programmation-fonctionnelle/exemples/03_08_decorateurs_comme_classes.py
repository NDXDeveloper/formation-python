# ============================================================================
#   Section 5.3 : Décorateurs comme classes
#   Description : Classe Compteur avec __call__, classe RepeterAction
#                 avec paramètres
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

from functools import wraps

# --- Compteur d'appels ---
print("=== Compteur d'appels ===")

class Compteur:
    """Décorateur qui compte le nombre d'appels."""
    def __init__(self, fonction):
        self.fonction = fonction
        self.nombre_appels = 0

    def __call__(self, *args, **kwargs):
        self.nombre_appels += 1
        print(f"[appel] Appel n.{self.nombre_appels} de {self.fonction.__name__}")
        return self.fonction(*args, **kwargs)

@Compteur
def dire_bonjour(nom):
    print(f"Bonjour {nom} !")

dire_bonjour("Alice")    # Appel n.1
dire_bonjour("Bob")      # Appel n.2
dire_bonjour("Charlie")  # Appel n.3

# --- Avec paramètres ---
print("\n=== RepeterAction ===")

class RepeterAction:
    """Décorateur classe qui répète une action."""
    def __init__(self, nombre_fois=2):
        self.nombre_fois = nombre_fois

    def __call__(self, fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            for i in range(self.nombre_fois):
                print(f"[exec] Exécution {i+1}/{self.nombre_fois}")
                resultat = fonction(*args, **kwargs)
            return resultat
        return wrapper

@RepeterAction(nombre_fois=3)
def afficher_message(message):
    print(f"  >> {message}")

afficher_message("Python")
# [exec] Exécution 1/3
#   >> Python
# [exec] Exécution 2/3
#   >> Python
# [exec] Exécution 3/3
#   >> Python
