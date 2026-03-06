# ============================================================================
#   Section 5.15 : Bonnes pratiques de gestion des erreurs
#   Description : Exceptions spécifiques, messages clairs, nettoyage,
#                 ne pas cacher les erreurs, documenter les exceptions
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- 1. Être spécifique ---
# Bon : exceptions spécifiques
try:
    nombre = int("42")
except ValueError:
    print("Entrée invalide")
else:
    print(f"Bon : nombre = {nombre}")

# --- 2. Ne pas cacher les erreurs ---
# Au minimum, logger l'erreur
try:
    resultat = 10 / 0
except Exception as e:
    print(f"Erreur ignorée : {e}")

# --- 3. Messages d'erreur utiles ---
try:
    nombre = int("abc")
except ValueError:
    print("Erreur : veuillez entrer un nombre entier (ex: 42)")

# --- 4. Nettoyage avec with (gestionnaire de contexte) ---
# Le fichier est automatiquement fermé même en cas d'erreur
try:
    with open("test_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier non trouvé (with garantit la fermeture)")

# --- 5. Documenter les exceptions dans les docstrings ---
def diviser(a, b):
    """
    Divise a par b.

    Args:
        a (float): Le dividende
        b (float): Le diviseur

    Returns:
        float: Le résultat de la division

    Raises:
        ZeroDivisionError: Si b est égal à zéro
    """
    if b == 0:
        raise ZeroDivisionError("Le diviseur ne peut pas être zéro")
    return a / b

print(f"\n{diviser(10, 3):.4f}")  # 3.3333

# --- 6. Anti-pattern : obtenir premier element ---
# Mauvais
def obtenir_premier_mauvais(liste):
    try:
        return liste[0]
    except IndexError:
        return None

# Mieux
def obtenir_premier_bon(liste):
    return liste[0] if liste else None

print(obtenir_premier_bon([1, 2, 3]))  # 1
print(obtenir_premier_bon([]))         # None
