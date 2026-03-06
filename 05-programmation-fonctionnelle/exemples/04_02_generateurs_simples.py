# ============================================================================
#   Section 5.4 : Créer des générateurs simples
#   Description : Générateur de carrés, de nombres pairs, de Fibonacci
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Générateur de carrés ---
print("=== Carrés ===")

def generer_carres(n):
    """Génère les carrés des nombres de 0 à n-1."""
    for i in range(n):
        yield i ** 2

for carre in generer_carres(5):
    print(carre, end=" ")  # 0 1 4 9 16
print()

# --- Générateur de nombres pairs ---
print("\n=== Nombres pairs ===")

def generer_pairs(debut, fin):
    """Génère tous les nombres pairs entre debut et fin."""
    for nombre in range(debut, fin + 1):
        if nombre % 2 == 0:
            yield nombre

pairs = generer_pairs(1, 10)
print(list(pairs))  # [2, 4, 6, 8, 10]

# --- Générateur de Fibonacci ---
print("\n=== Fibonacci ===")

def fibonacci(n):
    """Génère les n premiers nombres de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Suite de Fibonacci (10 premiers) :")
for nombre in fibonacci(10):
    print(nombre, end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()
