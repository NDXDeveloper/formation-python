# ============================================================================
#   Section 3.10 : L'instruction break
#   Description : Sortir immédiatement d'une boucle while ou for
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Avec while ---
compteur = 0

while True:  # Boucle infinie !
    print(compteur)
    compteur += 1

    if compteur >= 5:
        break  # On sort de la boucle

print("Boucle terminée")

# --- Avec for ---
print()
# Chercher un nombre dans une séquence
for i in range(1, 101):
    print(f"Vérification de {i}")

    if i == 7:
        print("Trouvé !")
        break  # On arrête la recherche
