# ============================================================================
#   Section 3.6 : L'opérateur ternaire
#   Description : Condition sur une ligne, maximum, prix avec réduction
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Syntaxe de base ---
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # Affiche : majeur

# --- Équivalent avec if/else classique ---
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"
print(statut)  # Affiche : majeur

# --- Trouver le maximum de deux nombres ---
a = 10
b = 20
maximum = a if a > b else b
print(maximum)  # Affiche : 20

# --- Affichage conditionnel ---
temperature = 25
print("Il fait chaud" if temperature > 20 else "Il fait froid")

# --- Prix avec réduction ---
prix = 100
membre = True
prix_final = prix * 0.9 if membre else prix
print(f"Prix : {prix_final}€")  # Affiche : Prix : 90.0€
