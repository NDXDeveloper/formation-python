# ============================================================================
#   Section 10.1 : Tests unitaires avec unittest et pytest
#   Description : Module panier - classe Panier d'achat avec ajout,
#                 total, nombre d'articles, vidage (utilisee par les tests)
#   Fichier source : 01-tests-unitaires-unittest-pytest.md
# ============================================================================

class Panier:
    """Represente un panier d'achat."""

    def __init__(self):
        self.articles = []

    def ajouter(self, article, prix, quantite=1):
        """Ajoute un article au panier."""
        if prix < 0:
            raise ValueError("Le prix ne peut pas etre negatif")
        if quantite < 1:
            raise ValueError("La quantite doit etre au moins 1")

        self.articles.append({
            "article": article,
            "prix": prix,
            "quantite": quantite
        })

    def total(self):
        """Calcule le total du panier."""
        return sum(item["prix"] * item["quantite"] for item in self.articles)

    def nombre_articles(self):
        """Retourne le nombre total d'articles."""
        return sum(item["quantite"] for item in self.articles)

    def vider(self):
        """Vide le panier."""
        self.articles = []
