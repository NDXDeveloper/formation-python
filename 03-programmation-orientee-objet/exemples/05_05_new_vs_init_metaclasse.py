# ============================================================================
#   Section 3.5 : __new__ vs __init__ dans les métaclasses
#   Description : __new__ crée la classe, __init__ l'initialise,
#                 utilisation combinée
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- __new__ : Créer la classe ---
class ModificationMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"__new__ : Création de {name}")
        attrs['modifie'] = True
        return super().__new__(mcs, name, bases, attrs)

class MaClasse1(metaclass=ModificationMeta):
    pass

print(MaClasse1.modifie)  # True

# --- __init__ : Initialiser la classe ---
print()

class InitMeta(type):
    def __init__(cls, name, bases, attrs):
        print(f"__init__ : Initialisation de {name}")
        super().__init__(name, bases, attrs)
        cls.compteur = 0

class MaClasse2(metaclass=InitMeta):
    pass

print(MaClasse2.compteur)  # 0

# --- Utiliser les deux ensemble ---
print()

class CompleteMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"1. __new__ : Création de {name}")
        attrs['cree_par'] = 'CompleteMeta'
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print(f"2. __init__ : Initialisation de {name}")
        super().__init__(name, bases, attrs)
        cls.initialise = True

class MaClasse3(metaclass=CompleteMeta):
    pass

print(MaClasse3.cree_par)    # CompleteMeta
print(MaClasse3.initialise)  # True
