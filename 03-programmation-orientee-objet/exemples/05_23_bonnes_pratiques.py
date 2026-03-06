# ============================================================================
#   Section 3.5 : Bonnes pratiques avancées
#   Description : Préférer __init_subclass__ aux métaclasses, ABC pour les
#                 interfaces, slots pour l'optimisation, documenter les
#                 métaclasses
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Préférer __init_subclass__ aux métaclasses ---
# Trop complexe avec métaclasse :
class SimpleMeta(type):
    def __new__(mcs, name, bases, attrs):
        attrs['added'] = True
        return super().__new__(mcs, name, bases, attrs)

# Plus simple avec __init_subclass__ :
class SimpleBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.added = True

class Enfant(SimpleBase):
    pass

print(f"Enfant.added = {Enfant.added}")  # True

# --- ABC pour les interfaces ---
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self, id):
        pass

class MemoryRepository(Repository):
    def __init__(self):
        self._data = {}

    def save(self, data):
        self._data[data['id']] = data
        return data['id']

    def load(self, id):
        return self._data.get(id)

repo = MemoryRepository()
repo.save({'id': 1, 'nom': 'Alice'})
print(f"Chargé : {repo.load(1)}")

# --- Slots pour l'optimisation ---
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Utile si vous créez des milliers de points
points = [Point(i, i*2) for i in range(10000)]
print(f"10000 points créés avec __slots__")

# --- Documenter les métaclasses ---
class MyMeta(type):
    """
    Métaclasse qui ajoute automatiquement un ID unique à chaque classe.

    Usage:
        class MyClass(metaclass=MyMeta):
            pass

    La classe aura automatiquement un attribut 'class_id'.
    """
    _counter = 0

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        MyMeta._counter += 1
        cls.class_id = MyMeta._counter
        return cls

class ClasseA(metaclass=MyMeta):
    pass

class ClasseB(metaclass=MyMeta):
    pass

print(f"ClasseA.class_id = {ClasseA.class_id}")  # 1
print(f"ClasseB.class_id = {ClasseB.class_id}")  # 2
