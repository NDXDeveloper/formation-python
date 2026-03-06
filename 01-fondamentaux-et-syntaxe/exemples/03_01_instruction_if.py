# ============================================================================
#   Section 3.1 : L'instruction if et l'indentation
#   Description : Condition simple, blocs de code indentés
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Premier exemple ---
age = 20

if age >= 18:
    print("Vous êtes majeur !")
    print("Vous pouvez voter.")

print("Ce message s'affiche toujours")

# --- L'importance de l'indentation ---
age = 20

if age >= 18:
    print("Ligne 1 dans le if")
    print("Ligne 2 dans le if")
print("Ligne en dehors du if")

# --- Erreur d'indentation (commentée car IndentationError) ---
# if age >= 18:
# print("Erreur !")  # IndentationError : pas indenté
