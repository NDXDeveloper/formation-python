# ============================================================================
#   Section 5.2 : Le bloc try/except de base
#   Description : Capturer une erreur, le programme continue
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Fonctionnement ---
try:
    print("Début du try")
    resultat = 10 / 0  # Erreur ici !
    print("Cette ligne ne sera jamais exécutée")
except:
    print("Une erreur s'est produite")

print("Le programme continue")
