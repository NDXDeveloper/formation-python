# ============================================================================
#   Section 3.5 : Descripteurs
#   Description : IntegerField (validation entier) et ValidatedString
#                 (validation chaîne avec taille min/max)
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Descripteur IntegerField ---
class IntegerField:
    """Descripteur qui ne stocke que des entiers"""

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} doit être un entier")
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Personne:
    age = IntegerField('age')

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age  # Utilise le descripteur

p = Personne("Alice", 30)
print(p.age)     # 30

p.age = 31       # OK
print(p.age)     # 31

try:
    p.age = "32"   # TypeError !
except TypeError as e:
    print(f"Erreur : {e}")

# --- Descripteur ValidatedString ---
print()

class ValidatedString:
    """Descripteur qui valide les chaînes de caractères"""

    def __init__(self, minsize=0, maxsize=None):
        self.minsize = minsize
        self.maxsize = maxsize

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, '')

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} doit être une chaîne")

        if len(value) < self.minsize:
            raise ValueError(
                f"{self.name} doit avoir au moins {self.minsize} caractères"
            )

        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"{self.name} ne peut pas dépasser {self.maxsize} caractères"
            )

        obj.__dict__[self.name] = value

class Utilisateur:
    nom = ValidatedString(minsize=2, maxsize=50)
    email = ValidatedString(minsize=5)

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

# Utilisation
user = Utilisateur("Alice", "alice@example.com")
print(f"{user.nom} - {user.email}")

try:
    user2 = Utilisateur("A", "test")  # ValueError (nom trop court)
except ValueError as e:
    print(f"Erreur : {e}")
