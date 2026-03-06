# ============================================================================
#   Section 2.1 : Créer, utiliser et modifier des variables
#   Description : Affectation, utilisation dans des calculs, modification
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Créer une variable (affectation) ---
age = 25
nom = "Alice"
taille = 1.75

print(age)      # 25
print(nom)      # Alice
print(taille)   # 1.75

# --- Utiliser une variable ---
age = 25
print(age)  # Affiche : 25

# Utiliser la variable dans un calcul
annee_naissance = 2025 - age
print(annee_naissance)  # Affiche : 2000

# --- Modifier la valeur d'une variable ---
compteur = 0
print(compteur)  # Affiche : 0

compteur = 5
print(compteur)  # Affiche : 5

compteur = compteur + 1
print(compteur)  # Affiche : 6
