# ============================================================================
#   Section 3.5 : Conditions imbriquées
#   Description : if à l'intérieur d'autres if, simplification avec and
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Conditions imbriquées ---
age = 20
a_argent = True

if age >= 18:
    print("Vous êtes majeur")

    if a_argent:
        print("Vous pouvez aller au cinéma")
    else:
        print("Vous n'avez pas d'argent pour le cinéma")
else:
    print("Vous êtes mineur")

# --- Version simplifiée (plus lisible) ---
est_ouvert = True

# Version imbriquée (moins lisible)
if age >= 18:
    if a_argent:
        if est_ouvert:
            print("Vous pouvez entrer")

# Version simplifiée (plus lisible)
if age >= 18 and a_argent and est_ouvert:
    print("Vous pouvez entrer")
