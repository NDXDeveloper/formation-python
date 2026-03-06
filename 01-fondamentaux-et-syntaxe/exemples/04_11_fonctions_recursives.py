# ============================================================================
#   Section 4.11 : Fonctions récursives
#   Description : Factorielle, Fibonacci, somme récursive, itérative vs récursive
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Factorielle ---
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # 5! = 120
print(factorielle(0))  # 0! = 1

# --- Suite de Fibonacci ---
print()

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Afficher les 10 premiers nombres de Fibonacci
for i in range(10):
    print(fibonacci(i), end=" ")
print()  # Affiche : 0 1 1 2 3 5 8 13 21 34

# --- Somme récursive ---
print()

def somme_recursive(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + somme_recursive(liste[1:])

nombres = [1, 2, 3, 4, 5]
print(somme_recursive(nombres))  # Affiche : 15

# --- Version itérative (pas de limite de récursion) ---
print()

def factorielle_iterative(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

print(f"Récursive : {factorielle(10)}")     # 3628800
print(f"Itérative : {factorielle_iterative(10)}")  # 3628800
