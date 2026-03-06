# ============================================================================
#   Section 3.8 : La boucle for et range()
#   Description : Parcourir une chaîne, range(n), range(debut, fin),
#                 range(debut, fin, pas), somme, table de multiplication,
#                 triangle d'étoiles
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Parcourir une chaîne de caractères ---
mot = "Python"

for lettre in mot:
    print(lettre)

# --- range(n) : de 0 à n-1 ---
print("\nrange(5) :")
for i in range(5):
    print(i)

# --- range(debut, fin) : de debut à fin-1 ---
print("\nrange(1, 6) :")
for i in range(1, 6):
    print(i)

# --- range(debut, fin, pas) ---
print("\nCompter de 2 en 2 :")
for i in range(0, 10, 2):
    print(i)

# --- Compter à rebours ---
print("\nCompte à rebours :")
for i in range(10, 0, -1):
    print(i)
print("Décollage !")

# --- Calculer une somme ---
print()
somme = 0

for i in range(1, 11):
    somme += i

print(f"La somme de 1 à 10 est : {somme}")
# Affiche : La somme de 1 à 10 est : 55

# --- Table de multiplication ---
print()
nombre = 7

print(f"Table de multiplication de {nombre} :")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} × {i} = {resultat}")

# --- Dessiner un triangle ---
print()
for i in range(1, 6):
    print("*" * i)
