# ============================================================================
#   Section 3.3 : Générer les comparaisons avec @functools.total_ordering
#   Description : à partir de __eq__ et __lt__ seulement, le décorateur génère
#                 __le__, __gt__, __ge__ (et __ne__ vient de __eq__)
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

from functools import total_ordering


@total_ordering
class Temperature:
    def __init__(self, degres):
        self.degres = degres

    def __eq__(self, autre):
        return self.degres == autre.degres

    def __lt__(self, autre):
        return self.degres < autre.degres

    def __repr__(self):
        return f"Temperature({self.degres})"


t1 = Temperature(20)
t2 = Temperature(25)

# Avec seulement __eq__ et __lt__, les six comparaisons fonctionnent :
print(t1 < t2)   # True
print(t1 <= t2)  # True  (généré par total_ordering)
print(t1 > t2)   # False (généré)
print(t1 >= t2)  # False (généré)
print(t1 == t2)  # False
print(t1 != t2)  # True  (déduit de __eq__)

# Conséquence pratique : tri et min/max fonctionnent aussi
temperatures = [Temperature(30), Temperature(15), Temperature(22)]
print(sorted(temperatures))   # [Temperature(15), Temperature(22), Temperature(30)]
print(min(temperatures))      # Temperature(15)
print(max(temperatures))      # Temperature(30)
