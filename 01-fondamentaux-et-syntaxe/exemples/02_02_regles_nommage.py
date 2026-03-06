# ============================================================================
#   Section 2.2 : Règles de nommage des variables
#   Description : Noms valides/invalides, conventions snake_case, PEP 8
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Exemples valides ---
nom = "Alice"
prenom_utilisateur = "Bob"
age2 = 30
_variable_privee = 42

print(nom)                  # Alice
print(prenom_utilisateur)   # Bob
print(age2)                 # 30
print(_variable_privee)     # 42

# --- Exemples invalides (commentés car SyntaxError) ---
# 2age = 30        # Commence par un chiffre
# mon-age = 25     # Contient un tiret
# for = 10         # Mot réservé Python
# mon âge = 25     # Contient un espace et un accent

# --- Bons noms de variables ---
nom_complet = "Alice Dupont"
age_en_annees = 25
prix_total_ttc = 99.99

print(nom_complet)     # Alice Dupont
print(age_en_annees)   # 25
print(prix_total_ttc)  # 99.99

# --- Noms à éviter (peu clairs) ---
x = "Alice Dupont"
n = 25
p = 99.99
