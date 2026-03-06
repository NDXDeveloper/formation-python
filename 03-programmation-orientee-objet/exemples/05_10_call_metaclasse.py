# ============================================================================
#   Section 3.5 : __call__ dans les métaclasses
#   Description : Intercepter la création d'instances via __call__
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class CallMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Création d'une instance de {cls.__name__}")
        print(f"Arguments : {args}, {kwargs}")

        # Créer l'instance normalement
        instance = super().__call__(*args, **kwargs)

        print(f"Instance créée : {instance}")
        return instance

class Personne(metaclass=CallMeta):
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return f"Personne({self.nom}, {self.age})"

# Créer une instance
p = Personne("Alice", 30)
