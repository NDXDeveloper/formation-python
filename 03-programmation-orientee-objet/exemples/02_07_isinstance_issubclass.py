# ============================================================================
#   Section 3.2 : Vérification de type et d'héritage
#   Description : isinstance() et issubclass() pour vérifier les relations
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class Animal:
    pass

class Chien(Animal):
    pass

class Chat(Animal):
    pass

rex = Chien()
felix = Chat()

# --- isinstance() ---
print(isinstance(rex, Chien))     # True
print(isinstance(rex, Animal))    # True (un Chien est aussi un Animal)
print(isinstance(rex, Chat))      # False
print(isinstance(felix, Chat))    # True
print(isinstance(felix, Animal))  # True

# --- issubclass() ---
print()
print(issubclass(Chien, Animal))  # True
print(issubclass(Chat, Animal))   # True
print(issubclass(Chien, Chat))    # False
print(issubclass(Animal, Chien))  # False
