# ============================================================================
#   Section 5.4 : Fonctions natives utilisant des générateurs
#   Description : map(), filter(), zip(), enumerate(), reversed()
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- map() et filter() ---
print("=== map() et filter() ===")

nombres = range(10)

# map() retourne un itérateur
doubles = map(lambda x: x * 2, nombres)
print(list(doubles))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# filter() aussi
pairs = filter(lambda x: x % 2 == 0, nombres)
print(list(pairs))  # [0, 2, 4, 6, 8]

# --- zip() ---
print("\n=== zip() ===")

prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

couples = zip(prenoms, ages)

for prenom, age in couples:
    print(f"{prenom} a {age} ans")
# Alice a 25 ans
# Bob a 30 ans
# Charlie a 35 ans

# --- enumerate() ---
print("\n=== enumerate() ===")

fruits = ["pomme", "banane", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. pomme
# 2. banane
# 3. orange

# --- reversed() ---
print("\n=== reversed() ===")

nombres = [1, 2, 3, 4, 5]

for n in reversed(nombres):
    print(n, end=" ")  # 5 4 3 2 1
print()
