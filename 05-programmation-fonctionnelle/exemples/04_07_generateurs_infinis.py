# ============================================================================
#   Section 5.4 : Générateurs infinis
#   Description : Compteur infini avec pas, cycle, répétition
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Compteur infini ---
print("=== Compteur infini ===")

def compteur(debut=0, pas=1):
    """Générateur de compteur infini."""
    valeur = debut
    while True:
        yield valeur
        valeur += pas

c = compteur(10, 2)
for _ in range(5):
    print(next(c), end=" ")  # 10 12 14 16 18
print()

# --- Cycle ---
print("\n=== Cycle ===")

def cycle(iterable):
    """Répète indéfiniment les éléments d'un itérable."""
    while True:
        for element in iterable:
            yield element

couleurs = cycle(['rouge', 'vert', 'bleu'])
for _ in range(8):
    print(next(couleurs), end=" ")
# rouge vert bleu rouge vert bleu rouge vert
print()

# --- Répétition ---
print("\n=== Répétition ===")

def repeter(valeur, n=None):
    """Répète une valeur n fois (ou indéfiniment si n=None)."""
    if n is None:
        while True:
            yield valeur
    else:
        for _ in range(n):
            yield valeur

cinq_fois = repeter("Python", 5)
print(list(cinq_fois))  # ['Python', 'Python', 'Python', 'Python', 'Python']
