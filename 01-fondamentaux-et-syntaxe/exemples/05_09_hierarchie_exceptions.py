# ============================================================================
#   Section 5.10 : Hiérarchie des exceptions
#   Description : Héritage des exceptions, ordre des blocs except
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Capturer une exception parente ---
# LookupError est parent de IndexError et KeyError
try:
    liste = [1, 2, 3]
    element = liste[10]
except LookupError:
    # Capture à la fois IndexError et KeyError
    print("Erreur de recherche (LookupError)")

# --- Ordre des blocs except ---
# Les plus spécifiques en premier !
print("\n=== Ordre correct ===")
try:
    fichier = open("test_inexistant.txt")
except FileNotFoundError:
    print("Fichier introuvable")
except OSError:
    print("Erreur système")
except Exception:
    print("Autre erreur")

# Si on met OSError avant FileNotFoundError, FileNotFoundError ne sera
# jamais atteint car FileNotFoundError hérite de OSError
