# ============================================================================
#   Section 4.12 : Fonctions lambda
#   Description : Lambda simple, multi-paramètres, map, filter, sorted
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Lambda simple ---
def doubler(x):
    return x * 2

doubler_lambda = lambda x: x * 2

print(doubler(5))         # Affiche : 10
print(doubler_lambda(5))  # Affiche : 10

# --- Lambda avec plusieurs paramètres ---
print()
additionner = lambda a, b: a + b
print(additionner(3, 5))  # Affiche : 8

maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Affiche : 20

# --- Avec map, filter, sorted ---
print()
nombres = [1, 2, 3, 4, 5]

# Doubler chaque nombre
doubles = list(map(lambda x: x * 2, nombres))
print(doubles)  # [2, 4, 6, 8, 10]

# Garder seulement les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4]

# Trier des tuples par le deuxième élément
personnes = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
par_age = sorted(personnes, key=lambda p: p[1])
print(par_age)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
