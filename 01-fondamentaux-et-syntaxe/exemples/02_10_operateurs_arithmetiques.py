# ============================================================================
#   Section 2.10 : Les Opérateurs Arithmétiques
#   Description : +, -, *, /, //, %, **, modulo pair/impair, priorité,
#                 opérateurs d'affectation composée
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Opérateurs de base ---
# Addition et soustraction
somme = 10 + 5
print(somme)  # Affiche : 15

difference = 10 - 5
print(difference)  # Affiche : 5

# Multiplication
produit = 7 * 6
print(produit)  # Affiche : 42

# Division classique (toujours un float)
division = 10 / 3
print(division)  # Affiche : 3.3333333333333335

division2 = 10 / 2
print(division2)  # Affiche : 5.0 (float, même si c'est un nombre entier)

# Division entière (quotient)
quotient = 10 // 3
print(quotient)  # Affiche : 3

# Modulo (reste)
reste = 10 % 3
print(reste)  # Affiche : 1

# Puissance
carre = 5 ** 2
print(carre)  # Affiche : 25

cube = 2 ** 3
print(cube)  # Affiche : 8

# --- Utilisation pratique du modulo (pair/impair) ---
nombre = 17
reste = nombre % 2

if reste == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")  # Affiche ceci car 17 % 2 = 1

# --- Priorité des opérations ---
resultat1 = 2 + 3 * 4
print(resultat1)  # Affiche : 14 (pas 20, car * est prioritaire)

resultat2 = (2 + 3) * 4
print(resultat2)  # Affiche : 20 (les parenthèses sont prioritaires)

resultat3 = 2 ** 3 ** 2
print(resultat3)  # Affiche : 512 (2^(3^2) = 2^9, puissance associe à droite)

# --- Opérateurs d'affectation composée ---
x = 10
x += 5  # Équivalent à x = x + 5
print(x)  # Affiche : 15

# Tous les opérateurs composés
x = 10
x += 5   # x = x + 5  → x vaut 15
x -= 3   # x = x - 3  → x vaut 12
x *= 2   # x = x * 2  → x vaut 24
x /= 4   # x = x / 4  → x vaut 6.0
x //= 2  # x = x // 2 → x vaut 3.0
x %= 2   # x = x % 2  → x vaut 1.0
x **= 3  # x = x ** 3 → x vaut 1.0
print(x)  # Affiche : 1.0
