# ============================================================================
#   Section 5.3 : Capturer des exceptions spécifiques
#   Description : except ValueError, except ZeroDivisionError, multiples
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Exceptions spécifiques (simulation sans input) ---
# Test avec ValueError
print("Test ValueError :")
try:
    nombre = int("abc")  # Simule une entrée invalide
    resultat = 100 / nombre
    print(f"Résultat : {resultat}")
except ValueError:
    print("Erreur : vous devez entrer un nombre valide")
except ZeroDivisionError:
    print("Erreur : impossible de diviser par zéro")

print("Programme terminé")

# Test avec ZeroDivisionError
print("\nTest ZeroDivisionError :")
try:
    nombre = int("0")
    resultat = 100 / nombre
    print(f"Résultat : {resultat}")
except ValueError:
    print("Erreur : vous devez entrer un nombre valide")
except ZeroDivisionError:
    print("Erreur : impossible de diviser par zéro")

print("Programme terminé")

# --- Plusieurs exceptions en une seule ligne ---
print("\nTest multiple exceptions :")
try:
    liste = [1, 2, 3]
    element = liste[10]
except (ValueError, TypeError, KeyError, IndexError):
    print("Une erreur s'est produite")
