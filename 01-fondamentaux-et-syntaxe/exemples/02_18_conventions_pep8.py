# ============================================================================
#   Section 2.18 : Conventions et Bonnes Pratiques (PEP 8)
#   Description : Espacement, nommage snake_case, longueur de lignes, nommage
#                 descriptif
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Espacement (PEP 8) ---
# Bon
x = 5
y = x + 1
print(x, y)  # 5 6

# Mauvais (mais fonctionne) :
# x=5
# y=x+1

# --- Noms de variables (snake_case) ---
# Bon (snake_case pour les variables)
nom_utilisateur = "Alice"
age_en_annees = 25

print(nom_utilisateur)  # Alice
print(age_en_annees)    # 25

# Mauvais (camelCase n'est pas la convention Python)
# nomUtilisateur = "Alice"
# ageEnAnnees = 25

# --- Longueur des lignes ---
# Ligne trop longue (à éviter) :
# message = "Ceci est un très long message qui dépasse largement la limite de 79 caractères recommandée"

# Mieux : utiliser des parenthèses
message = (
    "Ceci est un très long message qui dépasse largement "
    "la limite de 79 caractères recommandée"
)
print(message)

# --- Nommage descriptif ---
# Bon
prix_unitaire = 10.50
quantite = 5
prix_total = prix_unitaire * quantite
print(f"Prix total : {prix_total}")  # Prix total : 52.5

# Mauvais (noms non descriptifs)
p = 10.50
q = 5
t = p * q
print(f"t = {t}")  # t = 52.5
