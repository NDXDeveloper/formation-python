# ============================================================================
#   Section 2.1 : Itérer avec enumerate() et zip()
#   Description : enumerate (index + valeur, start=), zip (en parallèle,
#                 construction de dict, strict= 3.10+)
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- enumerate() : index ET valeur ---
fruits = ["pomme", "banane", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Démarrer la numérotation à 1
print("---")
for numero, fruit in enumerate(fruits, start=1):
    print(f"{numero}. {fruit}")

# --- zip() : parcourir plusieurs collections en parallèle ---
print("---")
noms = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for nom, age in zip(noms, ages):
    print(f"{nom} a {age} ans")

# Construire un dictionnaire à partir de deux listes
personnes = dict(zip(noms, ages))
print(personnes)  # {'Alice': 30, 'Bob': 25, 'Charlie': 35}

# zip() s'arrête à la collection la plus courte ; strict=True (3.10+) exige
# des longueurs égales (sinon ValueError)
try:
    list(zip([1, 2, 3], [1, 2], strict=True))
except ValueError as e:
    print(f"ValueError : {e}")
