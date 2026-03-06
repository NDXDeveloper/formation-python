# ============================================================================
#   Section 10.4 : Documentation avec docstrings
#   Description : Fonctions documentees - est_pair, calculer_prix_total,
#                 analyser_texte, formater_prix (Google Style)
#   Fichier source : 04-documentation-docstrings.md
# ============================================================================


def est_pair(nombre):
    """Verifie si un nombre est pair.

    Args:
        nombre (int): Le nombre a verifier.

    Returns:
        bool: True si le nombre est pair, False sinon.

    Example:
        >>> est_pair(4)
        True
        >>> est_pair(7)
        False
    """
    return nombre % 2 == 0


def calculer_prix_total(prix_unitaire, quantite, remise=0):
    """Calcule le prix total d'un achat.

    Cette fonction calcule le prix total en tenant compte
    de la quantite et d'une eventuelle remise.

    Args:
        prix_unitaire (float): Le prix d'un article.
        quantite (int): Le nombre d'articles achetes.
        remise (float, optional): Pourcentage de remise (0-100).
            Par defaut a 0.

    Returns:
        float: Le prix total apres remise, arrondi a 2 decimales.

    Raises:
        ValueError: Si la quantite est negative ou si la remise
            est hors de l'intervalle [0, 100].

    Example:
        >>> calculer_prix_total(10.0, 5)
        50.0
        >>> calculer_prix_total(10.0, 5, remise=20)
        40.0
    """
    if quantite < 0:
        raise ValueError("La quantite ne peut pas etre negative")
    if not 0 <= remise <= 100:
        raise ValueError("La remise doit etre entre 0 et 100")

    prix_brut = prix_unitaire * quantite
    prix_final = prix_brut * (1 - remise / 100)
    return round(prix_final, 2)


def analyser_texte(texte):
    """Analyse un texte et retourne des statistiques.

    Args:
        texte (str): Le texte a analyser.

    Returns:
        tuple: Un tuple contenant (nb_mots, nb_caracteres, nb_phrases)
            - nb_mots (int): Le nombre de mots
            - nb_caracteres (int): Le nombre de caracteres
            - nb_phrases (int): Le nombre de phrases

    Example:
        >>> analyser_texte("Bonjour. Comment allez-vous?")
        (3, 28, 2)
    """
    nb_mots = len(texte.split())
    nb_caracteres = len(texte)
    nb_phrases = texte.count('.') + texte.count('?') + texte.count('!')

    return nb_mots, nb_caracteres, nb_phrases


def formater_prix(prix, devise="EUR"):
    """Formate un prix avec sa devise.

    Args:
        prix (float): Le montant a formater.
        devise (str, optional): Le code de devise ISO 4217.
            Par defaut "EUR".

    Returns:
        str: Le prix formate avec symbole de devise.

    Example:
        >>> formater_prix(42.50)
        '42.50 EUR'
        >>> formater_prix(100, "USD")
        '100.00 $'
    """
    symboles = {"EUR": "EUR", "USD": "$", "GBP": "£"}
    symbole = symboles.get(devise, devise)
    return f"{prix:.2f} {symbole}"


# --- Demonstration ---
print("=== est_pair ===")
print(f"est_pair(4) = {est_pair(4)}")
print(f"est_pair(7) = {est_pair(7)}")

print("\n=== calculer_prix_total ===")
print(f"calculer_prix_total(10.0, 5) = {calculer_prix_total(10.0, 5)}")
print(f"calculer_prix_total(10.0, 5, remise=20) = {calculer_prix_total(10.0, 5, remise=20)}")

print("\n=== analyser_texte ===")
texte = "Bonjour. Comment allez-vous?"
mots, car, phrases = analyser_texte(texte)
print(f"analyser_texte(\"{texte}\") = ({mots}, {car}, {phrases})")

print("\n=== formater_prix ===")
print(f"formater_prix(42.50) = '{formater_prix(42.50)}'")
print(f"formater_prix(100, 'USD') = '{formater_prix(100, 'USD')}'")
print(f"formater_prix(15.5, 'GBP') = '{formater_prix(15.5, 'GBP')}'")
