# ============================================================================
#   Section 3.3 : Égalité (==) vs identité (is) pour les objets
#   Description : par défaut == compare l'IDENTITÉ (même objet) ; __eq__ permet
#                 de comparer la VALEUR. is teste toujours l'identité.
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

# --- Sans __eq__ : == compare l'IDENTITÉ (comme is) ---
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


a = Point(1, 2)
b = Point(1, 2)   # même valeur, mais objet distinct
c = a             # même objet que a

print(a == b)   # False (deux objets distincts, même si même valeur)
print(a is b)   # False (is : est-ce le même objet ?)
print(a == c)   # True  (c est le même objet que a)
print(a is c)   # True


# --- Avec __eq__ : == compare la VALEUR ---
class PointEq:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, autre):
        if not isinstance(autre, PointEq):
            return NotImplemented
        return (self.x, self.y) == (autre.x, autre.y)


d = PointEq(1, 2)
e = PointEq(1, 2)

print(d == e)   # True  (même valeur)
print(d is e)   # False (toujours deux objets distincts en mémoire)
