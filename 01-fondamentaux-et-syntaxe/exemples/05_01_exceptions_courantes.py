# ============================================================================
#   Section 5.1 : Exceptions courantes en Python
#   Description : Démonstration des exceptions les plus fréquentes
#                 (ZeroDivision, ValueError, IndexError, KeyError, etc.)
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# Chaque exception est encapsulée dans un try/except pour ne pas interrompre
# l'exécution des exemples suivants.

# --- ZeroDivisionError ---
try:
    resultat = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError : {e}")

# --- ValueError ---
try:
    nombre = int("abc")
except ValueError as e:
    print(f"ValueError : {e}")

# --- IndexError ---
try:
    liste = [1, 2, 3]
    element = liste[10]
except IndexError as e:
    print(f"IndexError : {e}")

# --- KeyError ---
try:
    personne = {"nom": "Alice"}
    age = personne["age"]
except KeyError as e:
    print(f"KeyError : {e}")

# --- FileNotFoundError ---
try:
    fichier = open("inexistant.txt")
except FileNotFoundError as e:
    print(f"FileNotFoundError : {e}")

# --- TypeError ---
try:
    resultat = "texte" + 5
except TypeError as e:
    print(f"TypeError : {e}")

# --- AttributeError ---
try:
    texte = "Bonjour"
    texte.append("!")
except AttributeError as e:
    print(f"AttributeError : {e}")
