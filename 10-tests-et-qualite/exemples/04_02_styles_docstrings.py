# ============================================================================
#   Section 10.4 : Documentation avec docstrings
#   Description : Trois styles de docstrings - Google Style, NumPy Style,
#                 reStructuredText (Sphinx) avec exemples fonctionnels
#   Fichier source : 04-documentation-docstrings.md
# ============================================================================

import statistics


# --- Google Style (recommande pour debutants) ---

def diviser(dividende, diviseur):
    """Divise deux nombres.

    Cette fonction effectue une division et gere
    le cas de la division par zero.

    Args:
        dividende (float): Le nombre a diviser.
        diviseur (float): Le nombre par lequel diviser.

    Returns:
        float: Le resultat de la division.

    Raises:
        ValueError: Si le diviseur est zero.

    Example:
        >>> diviser(10, 2)
        5.0
        >>> diviser(10, 0)
        Traceback (most recent call last):
        ValueError: Division par zero impossible
    """
    if diviseur == 0:
        raise ValueError("Division par zero impossible")
    return dividende / diviseur


# --- NumPy/SciPy Style ---

def calculer_statistiques(donnees):
    """
    Calcule des statistiques sur un ensemble de donnees.

    Cette fonction calcule la moyenne, la mediane
    et l'ecart-type d'une liste de nombres.

    Parameters
    ----------
    donnees : list of float
        Liste des valeurs numeriques a analyser.
        Ne doit pas etre vide.

    Returns
    -------
    dict
        Dictionnaire contenant les statistiques :
        - 'moyenne' : float
            La moyenne arithmetique
        - 'mediane' : float
            La valeur mediane
        - 'ecart_type' : float
            L'ecart-type de la population

    Raises
    ------
    ValueError
        Si la liste est vide.

    Examples
    --------
    >>> calculer_statistiques([1, 2, 3, 4, 5])
    {'moyenne': 3.0, 'mediane': 3.0, 'ecart_type': 1.41}
    """
    if not donnees:
        raise ValueError("La liste ne peut pas etre vide")

    moyenne = sum(donnees) / len(donnees)
    mediane = statistics.median(donnees)
    ecart_type = round(statistics.pstdev(donnees), 2)

    return {
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type
    }


# --- reStructuredText (Sphinx) ---

def creer_utilisateur(nom, email, age=None):
    """
    Cree un nouvel utilisateur dans le systeme.

    Cette fonction valide les donnees et cree un
    dictionnaire utilisateur avec les informations fournies.

    :param nom: Le nom complet de l'utilisateur
    :type nom: str
    :param email: L'adresse email de l'utilisateur
    :type email: str
    :param age: L'age de l'utilisateur (optionnel)
    :type age: int, optional
    :return: L'utilisateur cree
    :rtype: dict
    :raises ValueError: Si l'email est invalide
    """
    if "@" not in email:
        raise ValueError("Email invalide")
    return {"nom": nom, "email": email, "age": age, "actif": True}


# --- Demonstration ---
print("=== Google Style : diviser ===")
print(f"diviser(10, 2) = {diviser(10, 2)}")
try:
    diviser(10, 0)
except ValueError as e:
    print(f"diviser(10, 0) -> ValueError: {e}")

print("\n=== NumPy Style : calculer_statistiques ===")
stats = calculer_statistiques([1, 2, 3, 4, 5])
print(f"calculer_statistiques([1, 2, 3, 4, 5]) = {stats}")

print("\n=== Sphinx Style : creer_utilisateur ===")
user = creer_utilisateur("Alice", "alice@example.com", 25)
print(f"creer_utilisateur('Alice', 'alice@example.com', 25) = {user}")

print("\n=== Docstrings accessibles ===")
print(f"diviser.__doc__ (debut) : {diviser.__doc__.strip().split(chr(10))[0]}")
print(f"calculer_statistiques.__doc__ (debut) : {calculer_statistiques.__doc__.strip().split(chr(10))[0]}")
print(f"creer_utilisateur.__doc__ (debut) : {creer_utilisateur.__doc__.strip().split(chr(10))[0]}")
