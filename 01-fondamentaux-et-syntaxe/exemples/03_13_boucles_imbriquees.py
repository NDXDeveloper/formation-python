# ============================================================================
#   Section 3.13 : Boucles imbriquées
#   Description : Table de multiplication, rectangle, escalier,
#                 boucle externe/interne
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Table de multiplication (3x3) ---
for i in range(1, 4):
    for j in range(1, 4):
        resultat = i * j
        print(f"{i} × {j} = {resultat}")
    print()  # Ligne vide après chaque table

# --- Dessiner un rectangle ---
print("Rectangle 4x6 :")
hauteur = 4
largeur = 6

for i in range(hauteur):
    for j in range(largeur):
        print("*", end="")  # end="" évite le retour à la ligne
    print()  # Retour à la ligne après chaque ligne

# --- Motif en escalier ---
print("\nEscalier :")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# --- Comprendre les boucles imbriquées ---
print("\nExterne / Interne :")
for i in range(3):  # Boucle externe
    print(f"Externe : i = {i}")

    for j in range(2):  # Boucle interne
        print(f"  Interne : j = {j}")
