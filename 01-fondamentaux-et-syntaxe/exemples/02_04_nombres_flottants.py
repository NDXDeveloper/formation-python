# ============================================================================
#   Section 2.4 : Les Nombres à Virgule Flottante (float)
#   Description : Floats, précision limitée, notation scientifique
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Floats de base ---
taille = 1.75
prix = 19.99
temperature = -3.5
pi = 3.14159

print(taille)       # 1.75
print(prix)         # 19.99
print(temperature)  # -3.5
print(pi)           # 3.14159

# --- Précision limitée des floats ---
resultat = 0.1 + 0.2
print(resultat)  # Affiche : 0.30000000000000004 (!)

# --- Notation scientifique ---
grand_nombre = 3e8       # 3 × 10^8 = 300000000
petit_nombre = 1.5e-4    # 1.5 × 10^-4 = 0.00015

print(grand_nombre)   # 300000000.0
print(petit_nombre)   # 0.00015
