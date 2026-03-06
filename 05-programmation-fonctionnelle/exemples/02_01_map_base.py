# ============================================================================
#   Section 5.2 : La fonction map() - Bases et exemples pratiques
#   Description : Doubler avec boucle vs map(), convertir températures,
#                 majuscules, longueurs, formatter, plusieurs itérables
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

# --- Exemple de base : doubler des nombres ---
print("=== Doubler des nombres ===")

# Approche classique avec une boucle
nombres = [1, 2, 3, 4, 5]
nombres_doubles = []

for nombre in nombres:
    nombres_doubles.append(nombre * 2)

print(nombres_doubles)  # [2, 4, 6, 8, 10]

# Avec map()
nombres = [1, 2, 3, 4, 5]
nombres_doubles = list(map(lambda x: x * 2, nombres))

print(nombres_doubles)  # [2, 4, 6, 8, 10]

# --- Convertir des températures ---
print("\n=== Convertir des températures ===")

temperatures_celsius = [0, 10, 20, 30, 40]

celsius_vers_fahrenheit = lambda c: (c * 9/5) + 32

temperatures_fahrenheit = list(map(celsius_vers_fahrenheit, temperatures_celsius))

print(f"Celsius : {temperatures_celsius}")
print(f"Fahrenheit : {temperatures_fahrenheit}")
# Fahrenheit : [32.0, 50.0, 68.0, 86.0, 104.0]

# --- Mettre des chaînes en majuscules ---
print("\n=== Majuscules ===")

mots = ["python", "javascript", "java", "ruby"]

mots_majuscules = list(map(str.upper, mots))

print(mots_majuscules)  # ['PYTHON', 'JAVASCRIPT', 'JAVA', 'RUBY']

# --- Calculer la longueur de plusieurs chaînes ---
print("\n=== Longueurs ===")

phrases = ["Bonjour", "Comment allez-vous ?", "Python", "Programmation"]

longueurs = list(map(len, phrases))

print(longueurs)  # [7, 20, 6, 13]

# --- Formatter des données ---
print("\n=== Formatter ===")

prenoms = ["alice", "bob", "charlie"]

prenoms_formatte = list(map(lambda nom: nom.capitalize(), prenoms))

print(prenoms_formatte)  # ['Alice', 'Bob', 'Charlie']

# --- map() avec plusieurs itérables ---
print("\n=== Plusieurs itérables ===")

nombres1 = [1, 2, 3, 4]
nombres2 = [10, 20, 30, 40]

sommes = list(map(lambda x, y: x + y, nombres1, nombres2))

print(sommes)  # [11, 22, 33, 44]

# Créer des phrases descriptives
prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

descriptions = list(map(
    lambda nom, age: f"{nom} a {age} ans",
    prenoms,
    ages
))

for desc in descriptions:
    print(desc)
# Alice a 25 ans
# Bob a 30 ans
# Charlie a 35 ans
