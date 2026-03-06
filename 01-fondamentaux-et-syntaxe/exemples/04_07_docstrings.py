# ============================================================================
#   Section 4.7 : Documentation des fonctions (docstrings)
#   Description : Docstrings, accéder à __doc__, help()
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

def calculer_aire_rectangle(longueur, largeur):
    """
    Calcule l'aire d'un rectangle.

    Paramètres:
        longueur (float): La longueur du rectangle
        largeur (float): La largeur du rectangle

    Retourne:
        float: L'aire du rectangle
    """
    return longueur * largeur

print(calculer_aire_rectangle(5, 3))  # 15

def est_palindrome(texte):
    """
    Vérifie si un texte est un palindrome.

    Un palindrome est un mot qui se lit de la même façon
    dans les deux sens (ex: "kayak", "radar").

    Paramètres:
        texte (str): Le texte à vérifier

    Retourne:
        bool: True si le texte est un palindrome, False sinon
    """
    texte = texte.lower().replace(" ", "")
    return texte == texte[::-1]

print(est_palindrome("kayak"))   # True
print(est_palindrome("python"))  # False

# --- Accéder à la docstring ---
def dire_bonjour(nom):
    """Affiche un message de salutation."""
    print(f"Bonjour {nom} !")

print()
print("Docstring :", dire_bonjour.__doc__)
