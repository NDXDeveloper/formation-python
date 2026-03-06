# ============================================================================
#   Section 5.5 : Récursion en programmation fonctionnelle
#   Description : Factorielle, Fibonacci, somme récursive, récursion
#                 terminale
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Factorielle ---
print("=== Factorielle ===")

def factorielle(n):
    """Calcule la factorielle de manière récursive."""
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # 120

# --- Fibonacci ---
print("\n=== Fibonacci ===")

def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# --- Somme d'une liste ---
print("\n=== Somme récursive ===")

def somme_recursive(liste):
    """Calcule la somme des éléments d'une liste."""
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:])

print(somme_recursive([1, 2, 3, 4, 5]))  # 15

# --- Récursion terminale ---
print("\n=== Récursion terminale ===")

def factorielle_tail(n, acc=1):
    """Factorielle avec récursion terminale."""
    if n <= 1:
        return acc
    return factorielle_tail(n - 1, n * acc)

print(factorielle_tail(5))  # 120
