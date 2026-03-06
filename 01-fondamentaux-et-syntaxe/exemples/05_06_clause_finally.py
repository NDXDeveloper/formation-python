# ============================================================================
#   Section 5.6 : La clause finally
#   Description : Code toujours exécuté, ordre d'exécution try/except/else/finally
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Ordre d'exécution sans erreur ---
print("=== Sans erreur ===")
try:
    print("1. Dans try")
except:
    print("2. Dans except (si erreur)")
else:
    print("3. Dans else (si pas d'erreur)")
finally:
    print("4. Dans finally (toujours)")

# --- Ordre d'exécution avec erreur ---
print("\n=== Avec erreur ===")
try:
    print("1. Dans try")
    resultat = 10 / 0  # Erreur !
except:
    print("2. Dans except (si erreur)")
else:
    print("3. Dans else (si pas d'erreur)")
finally:
    print("4. Dans finally (toujours)")

# --- Exemple avec fichier ---
print("\n=== Exemple fichier ===")
fichier = None
try:
    fichier = open("inexistant_test.txt", "r")
    contenu = fichier.read()
    print(contenu)
except FileNotFoundError:
    print("Le fichier n'existe pas")
finally:
    if fichier:
        fichier.close()
        print("Fichier fermé")
    else:
        print("Pas de fichier à fermer")
