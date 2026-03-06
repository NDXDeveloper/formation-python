# ============================================================================
#   Section 3.7 : La boucle while
#   Description : Compteur, compte à rebours, boucle infinie (commentée)
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Compteur simple ---
compteur = 1

while compteur <= 5:
    print(f"Compteur : {compteur}")
    compteur += 1

print("Boucle terminée")

# --- Compte à rebours ---
print()
compte = 5

while compte > 0:
    print(compte)
    compte -= 1

print("Décollage !")

# --- Boucle infinie (commentée - NE PAS EXÉCUTER) ---
# compteur = 1
# while compteur <= 5:
#     print(compteur)
#     # Oups, on a oublié d'incrémenter compteur !

# --- Version corrigée ---
print()
compteur = 1
while compteur <= 5:
    print(compteur)
    compteur += 1  # Important : on modifie compteur !
