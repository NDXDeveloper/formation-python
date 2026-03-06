# ============================================================================
#   Section 2.4 : Formatage ancien - format() et %
#   Description : Méthode format() avec indices/noms, opérateur % style C
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# --- Méthode format() ---

# Avec indices
print("{0} et {1}".format("Python", "Java"))  # Python et Java
print("{1} et {0}".format("Python", "Java"))  # Java et Python

# Avec noms
print("{langage} est {adjectif}".format(langage="Python", adjectif="génial"))

# Formatage des nombres
pi = 3.14159
print("Pi vaut {:.2f}".format(pi))  # Pi vaut 3.14

# Avec des dictionnaires
personne = {"nom": "Alice", "age": 25}
print("Nom : {nom}, Age : {age}".format(**personne))

# --- Opérateur % (ancienne méthode) ---
print()
nom = "Alice"
age = 25
print("Nom : %s, Age : %d" % (nom, age))  # Nom : Alice, Age : 25

# Avec dictionnaire
print("Nom : %(nom)s, Age : %(age)d" % {"nom": "Alice", "age": 25})
