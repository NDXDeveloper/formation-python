# ============================================================================
#   Section 2.4 : Changement de casse
#   Description : upper, lower, capitalize, title, swapcase, isupper,
#                 islower, istitle
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "Python Programming"

print(texte.upper())       # PYTHON PROGRAMMING
print(texte.lower())       # python programming
print(texte.capitalize())  # Python programming (première lettre en majuscule)
print(texte.title())       # Python Programming (première de chaque mot)
print(texte.swapcase())    # pYTHON pROGRAMMING (inverse la casse)

# Vérifications
print("PYTHON".isupper())  # True
print("python".islower())  # True
print("Python".istitle())  # True
