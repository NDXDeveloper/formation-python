# ============================================================================
#   Section 2.2 : Expressions génératrices (Generator Expressions)
#   Description : Parenthèses au lieu de crochets, utilisation avec sum/max,
#                 valeurs produites à la demande
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Expression génératrice : génère les valeurs à la demande
carres_gen = (x**2 for x in range(1000000))

# Utiliser le générateur
print("Carrés < 100 :")
for carre in carres_gen:
    if carre > 100:
        break
    print(carre, end=" ")
print()

# Expressions génératrices avec des fonctions
nombres = [1, 2, 3, 4, 5]
somme = sum(x**2 for x in nombres)  # Pas besoin de [] supplémentaires
print(f"Somme des carrés : {somme}")  # 55

# Maximum des valeurs absolues
nombres = [-5, 2, -8, 3]
max_abs = max(abs(x) for x in nombres)
print(f"Max absolu : {max_abs}")  # 8
