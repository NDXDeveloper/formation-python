# ============================================================================
#   Section 9.1 : Hierarchie des exceptions
#   Description : Exceptions courantes (ZeroDivisionError, OverflowError,
#                 IndexError, KeyError, TypeError, ValueError, NameError,
#                 AttributeError, FileNotFoundError, PermissionError,
#                 ModuleNotFoundError), capture a differents niveaux,
#                 ordre de capture
#   Fichier source : 01-hierarchie-des-exceptions.md
# ============================================================================

import math

# ==========================================
# 1. Exception de base
# ==========================================
print("=== Exception de base ===")

try:
    pass
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
print("  Aucune exception levee (pass)")

# ==========================================
# 2. ArithmeticError
# ==========================================
print("\n=== ArithmeticError ===")

# ZeroDivisionError
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("  Impossible de diviser par zero !")

# OverflowError
try:
    resultat = math.exp(1000)
except OverflowError:
    print("  Le nombre est trop grand !")

# ==========================================
# 3. LookupError
# ==========================================
print("\n=== LookupError ===")

# IndexError
ma_liste = [1, 2, 3]
try:
    element = ma_liste[10]
except IndexError:
    print("  Cet index n'existe pas dans la liste !")

# KeyError
mon_dict = {"nom": "Alice", "age": 30}
try:
    ville = mon_dict["ville"]
except KeyError:
    print("  Cette cle n'existe pas dans le dictionnaire !")

# ==========================================
# 4. TypeError
# ==========================================
print("\n=== TypeError ===")

try:
    resultat = "hello" + 5
except TypeError:
    print("  Types incompatibles pour cette operation !")

# ==========================================
# 5. ValueError
# ==========================================
print("\n=== ValueError ===")

try:
    nombre = int("abc")
except ValueError:
    print("  Impossible de convertir cette chaine en nombre !")

# ==========================================
# 6. NameError
# ==========================================
print("\n=== NameError ===")

try:
    print(variable_inexistante)
except NameError:
    print("  Cette variable n'existe pas !")

# ==========================================
# 7. AttributeError
# ==========================================
print("\n=== AttributeError ===")

ma_liste = [1, 2, 3]
try:
    ma_liste.append_all([4, 5])
except AttributeError:
    print("  Cet attribut ou cette methode n'existe pas !")

# ==========================================
# 8. OSError et sous-classes
# ==========================================
print("\n=== OSError ===")

# FileNotFoundError
try:
    with open("fichier_inexistant.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("  Le fichier n'a pas ete trouve !")

# PermissionError
try:
    with open("/root/fichier_protege.txt", "w", encoding="utf-8") as f:
        f.write("Test")
except PermissionError:
    print("  Vous n'avez pas la permission d'acceder a ce fichier !")

# ==========================================
# 9. ImportError / ModuleNotFoundError
# ==========================================
print("\n=== ImportError ===")

try:
    import module_inexistant
except ModuleNotFoundError:
    print("  Ce module n'est pas installe !")

# ==========================================
# 10. Capture multiple avec tuple
# ==========================================
print("\n=== Capture multiple ===")

try:
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"  Une erreur courante s'est produite : {e}")
print("  Aucune exception levee (pass)")

# ==========================================
# 11. Ordre de capture
# ==========================================
print("\n=== Ordre de capture ===")

# Mauvais ordre : LookupError capture avant IndexError
print("Mauvais ordre:")
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[10])
except LookupError:
    print("  Erreur de recherche (LookupError capture avant IndexError)")
except IndexError:
    print("  Index invalide (jamais atteint)")

# Bon ordre : IndexError (specifique) avant LookupError (general)
print("Bon ordre:")
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[10])
except IndexError:
    print("  Index invalide (specifique en premier)")
except LookupError:
    print("  Erreur de recherche (general ensuite)")
