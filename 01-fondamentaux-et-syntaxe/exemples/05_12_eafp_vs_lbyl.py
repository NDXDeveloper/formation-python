# ============================================================================
#   Section 5.13 : EAFP vs LBYL
#   Description : Deux philosophies de programmation Python
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- LBYL : Look Before You Leap (vérifier avant d'agir) ---
dictionnaire = {"nom": "Alice", "age": 25}

# Vérifier d'abord
if 'cle' in dictionnaire:
    valeur = dictionnaire['cle']
else:
    valeur = None
print(f"LBYL - valeur : {valeur}")

# --- EAFP : Easier to Ask for Forgiveness than Permission ---
# Essayer d'abord, gérer les erreurs ensuite
try:
    valeur = dictionnaire['cle']
except KeyError:
    valeur = None
print(f"EAFP - valeur : {valeur}")

# --- Exemple avec fichier ---
print()

# LBYL
import os
fichier = "test_inexistant.txt"
if os.path.exists(fichier):
    with open(fichier) as f:
        contenu = f.read()
    print(f"LBYL - contenu lu")
else:
    print(f"LBYL - fichier n'existe pas")

# EAFP
try:
    with open(fichier) as f:
        contenu = f.read()
    print(f"EAFP - contenu lu")
except FileNotFoundError:
    print(f"EAFP - fichier n'existe pas")
