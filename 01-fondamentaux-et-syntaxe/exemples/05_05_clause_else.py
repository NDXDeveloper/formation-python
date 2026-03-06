# ============================================================================
#   Section 5.5 : La clause else
#   Description : Code exécuté seulement si aucune exception levée
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- else avec conversion réussie ---
print("Test réussi :")
try:
    nombre = int("42")  # Simule une entrée valide
except ValueError:
    print("Erreur : ce n'est pas un nombre valide")
else:
    print(f"Vous avez entré : {nombre}")
    print("C'est un nombre valide !")

# --- else avec conversion échouée ---
print("\nTest échoué :")
try:
    nombre = int("abc")  # Simule une entrée invalide
except ValueError:
    print("Erreur : ce n'est pas un nombre valide")
else:
    print(f"Vous avez entré : {nombre}")
    print("C'est un nombre valide !")
