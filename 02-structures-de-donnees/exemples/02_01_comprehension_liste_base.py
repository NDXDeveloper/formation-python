# ============================================================================
#   Section 2.2 : Compréhensions de listes - Concept de base
#   Description : Syntaxe de base, carrés, doubles, températures, majuscules
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- Méthode traditionnelle vs compréhension ---
# Méthode classique
carres = []
for i in range(5):
    carres.append(i ** 2)
print(carres)  # [0, 1, 4, 9, 16]

# Avec une compréhension de liste
carres = [i ** 2 for i in range(5)]
print(carres)  # [0, 1, 4, 9, 16]

# --- Exemples de base ---
# Créer une liste de nombres
nombres = [x for x in range(10)]
print(nombres)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplier chaque nombre par 2
doubles = [x * 2 for x in range(5)]
print(doubles)  # [0, 2, 4, 6, 8]

# Convertir des températures Celsius en Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# Mettre tous les mots en majuscules
mots = ["python", "est", "génial"]
mots_majuscules = [mot.upper() for mot in mots]
print(mots_majuscules)  # ['PYTHON', 'EST', 'GÉNIAL']

# Extraire la première lettre de chaque mot
premieres_lettres = [mot[0] for mot in mots]
print(premieres_lettres)  # ['p', 'e', 'g']
