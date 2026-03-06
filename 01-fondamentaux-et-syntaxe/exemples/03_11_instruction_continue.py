# ============================================================================
#   Section 3.11 : L'instruction continue
#   Description : Passer à l'itération suivante, différence break/continue,
#                 ignorer des valeurs invalides
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Afficher seulement les nombres impairs ---
for i in range(1, 11):
    if i % 2 == 0:  # Si le nombre est pair
        continue    # On passe au suivant

    print(i)  # Cette ligne n'est exécutée que pour les impairs

# --- Différence entre break et continue ---
print("\nAvec break :")
# Avec break : arrête complètement la boucle
for i in range(5):
    if i == 3:
        break
    print(i)
# Affiche : 0, 1, 2

print("\nAvec continue :")
# Avec continue : saute seulement l'itération actuelle
for i in range(5):
    if i == 3:
        continue
    print(i)
# Affiche : 0, 1, 2, 4

# --- Ignorer les valeurs invalides ---
print("\nTempérature moyenne :")
temperatures = [23, -999, 25, 28, -999, 22]  # -999 = valeur manquante

somme = 0
count = 0

for temp in temperatures:
    if temp == -999:
        continue  # On ignore cette valeur

    somme += temp
    count += 1

moyenne = somme / count
print(f"Température moyenne : {moyenne}°C")
# Affiche : Température moyenne : 24.5°C
