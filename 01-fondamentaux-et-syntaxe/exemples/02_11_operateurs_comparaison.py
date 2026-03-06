# ============================================================================
#   Section 2.11 : Les Opérateurs de Comparaison
#   Description : ==, !=, >, <, >=, <=, comparaison de chaînes, == vs =
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Comparaisons de base ---
age = 20

print(age == 20)  # Affiche : True
print(age == 18)  # Affiche : False
print(age != 18)  # Affiche : True
print(age > 18)   # Affiche : True
print(age < 25)   # Affiche : True
print(age >= 20)  # Affiche : True
print(age <= 19)  # Affiche : False

# --- Différence entre == et = ---
x = 5      # Affectation : x reçoit la valeur 5
print(x == 5)   # Comparaison : est-ce que x est égal à 5 ? (retourne True)

# --- Comparaison de chaînes ---
nom1 = "Alice"
nom2 = "Bob"

print(nom1 == nom2)  # Affiche : False
print(nom1 != nom2)  # Affiche : True

# Comparaison alphabétique
print(nom1 < nom2)    # Affiche : True (A vient avant B dans l'alphabet)
print("abc" < "abd")  # Affiche : True
