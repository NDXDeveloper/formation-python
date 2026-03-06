# ============================================================================
#   Section 3.14 : La clause else avec les boucles
#   Description : else après for (nombre premier), else après while
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Chercher un nombre premier ---
nombre = 17

for i in range(2, nombre):
    if nombre % i == 0:
        print(f"{nombre} n'est pas premier (divisible par {i})")
        break
else:
    # Cette partie s'exécute si on n'a pas trouvé de diviseur
    print(f"{nombre} est premier")

# Test avec un nombre non premier
print()
nombre = 15

for i in range(2, nombre):
    if nombre % i == 0:
        print(f"{nombre} n'est pas premier (divisible par {i})")
        break
else:
    print(f"{nombre} est premier")
