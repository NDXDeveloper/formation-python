# ============================================================================
#   Section 5.3 : Décorateurs de classe
#   Description : Décorateur qui modifie une classe (ajouter __str__),
#                 singleton avec décorateur
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

from functools import wraps

# --- Décorateur qui modifie une classe ---
print("=== Ajouter __str__ ===")

def ajouter_methode_str(cls):
    """Ajoute une méthode __str__ à une classe."""
    def __str__(self):
        attributs = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{cls.__name__}({attributs})"

    cls.__str__ = __str__
    return cls

@ajouter_methode_str
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = Personne("Alice", 30)
print(p)  # Personne(nom=Alice, age=30)

# --- Singleton avec un décorateur ---
print("\n=== Singleton ===")

def singleton(cls):
    """Transforme une classe en singleton."""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Configuration:
    def __init__(self):
        self.parametre = "valeur"
        print("Configuration créée")

# Première création
config1 = Configuration()  # Affiche : Configuration créée
config1.parametre = "nouvelle valeur"

# Deuxième "création" : retourne la même instance
config2 = Configuration()  # N'affiche rien
print(config2.parametre)   # nouvelle valeur
print(config1 is config2)  # True
