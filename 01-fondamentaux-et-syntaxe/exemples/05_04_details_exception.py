# ============================================================================
#   Section 5.4 : Accéder aux détails de l'exception avec as
#   Description : Récupérer le message d'erreur avec except ... as e
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- ValueError avec détails ---
try:
    nombre = int("abc")
except ValueError as e:
    print(f"Erreur de valeur : {e}")

# --- FileNotFoundError avec détails ---
try:
    fichier = open("inexistant.txt")
except FileNotFoundError as e:
    print(f"Impossible d'ouvrir le fichier : {e}")
