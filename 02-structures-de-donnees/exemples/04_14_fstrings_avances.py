# ============================================================================
#   Section 2.4 : Formatage avancé avec f-strings
#   Description : Dates, binaire/octal/hexadécimal, debug (=), multi-lignes
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

from datetime import datetime

# Dates
maintenant = datetime.now()
print(f"Date : {maintenant:%Y-%m-%d}")
print(f"Heure : {maintenant:%H:%M:%S}")

# Affichage en binaire, octal, hexadécimal
nombre = 42
print(f"Binaire : {nombre:b}")    # Binaire : 101010
print(f"Octal : {nombre:o}")      # Octal : 52
print(f"Hexadécimal : {nombre:x}") # Hexadécimal : 2a

# Debug (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")  # x=10, y=20

# Chaînes multi-lignes
nom = "Alice"
age = 25
ville = "Paris"
info = f"""
Informations:
  Nom: {nom}
  Age: {age}
  Ville: {ville}
"""
print(info)
