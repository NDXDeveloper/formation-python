# ============================================================================
#   Section 3.5 : Singleton Pattern avec métaclasse
#   Description : Une classe dont on ne peut créer qu'une seule instance
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class SingletonMeta(type):
    """Métaclasse qui implémente le pattern Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.parametre1 = "valeur1"
        self.parametre2 = "valeur2"

# Créer deux "instances"
config1 = Configuration()
config2 = Configuration()

# Ce sont en fait la même instance !
print(config1 is config2)  # True

config1.parametre1 = "nouvelle_valeur"
print(config2.parametre1)  # nouvelle_valeur
