# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Exemple complet - Application e-commerce avec logging
#                 (Produit, Panier, GestionnaireCommandes, dictConfig)
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import logging.config
from datetime import datetime
import tempfile
import os
import shutil

# Créer un dossier temporaire pour les logs
tmpdir = tempfile.mkdtemp(prefix="ecommerce_logs_")

# Configuration du logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file_all': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': os.path.join(tmpdir, 'ecommerce.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 3
        },
        'file_errors': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': os.path.join(tmpdir, 'errors.log')
        }
    },

    'loggers': {
        'ecommerce': {
            'level': 'DEBUG',
            'handlers': ['console', 'file_all', 'file_errors'],
            'propagate': False
        }
    }
}

# Appliquer la configuration
logging.config.dictConfig(LOGGING_CONFIG)


class Produit:
    """Représente un produit"""

    def __init__(self, id: int, nom: str, prix: float, stock: int):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.stock = stock
        self.logger = logging.getLogger('ecommerce.produit')
        self.logger.debug(f"Produit créé: {nom} (ID: {id})")

    def verifier_disponibilite(self, quantite: int) -> bool:
        """Vérifie si le produit est disponible en quantité suffisante"""
        disponible = self.stock >= quantite

        if disponible:
            self.logger.info(f"Produit {self.nom} disponible: {quantite}/{self.stock}")
        else:
            self.logger.warning(f"Stock insuffisant pour {self.nom}: demandé={quantite}, stock={self.stock}")

        return disponible

    def reduire_stock(self, quantite: int):
        """Réduit le stock du produit"""
        if self.verifier_disponibilite(quantite):
            self.stock -= quantite
            self.logger.info(f"Stock réduit pour {self.nom}: nouveau stock={self.stock}")
            return True
        return False


class Panier:
    """Panier d'achat"""

    def __init__(self, client_id: str):
        self.client_id = client_id
        self.articles: dict[int, tuple] = {}
        self.logger = logging.getLogger('ecommerce.panier')
        self.logger.info(f"Panier créé pour le client {client_id}")

    def ajouter(self, produit: Produit, quantite: int = 1):
        """Ajoute un produit au panier"""
        self.logger.debug(f"Ajout de {quantite}x {produit.nom} au panier")

        if not produit.verifier_disponibilite(quantite):
            self.logger.error(f"Impossible d'ajouter {produit.nom}: stock insuffisant")
            return False

        if produit.id in self.articles:
            _, qte_actuelle = self.articles[produit.id]
            quantite_totale = qte_actuelle + quantite

            if not produit.verifier_disponibilite(quantite_totale):
                self.logger.warning(f"Quantité totale trop élevée pour {produit.nom}")
                return False

            self.articles[produit.id] = (produit, quantite_totale)
            self.logger.info(f"Quantité mise à jour: {produit.nom} x{quantite_totale}")
        else:
            self.articles[produit.id] = (produit, quantite)
            self.logger.info(f"Produit ajouté au panier: {produit.nom} x{quantite}")

        return True

    def calculer_total(self) -> float:
        """Calcule le total du panier"""
        total = sum(produit.prix * qte for produit, qte in self.articles.values())
        self.logger.debug(f"Total du panier calculé: {total:.2f} EUR")
        return total

    def vider(self):
        """Vide le panier"""
        nb_articles = len(self.articles)
        self.articles.clear()
        self.logger.info(f"Panier vidé ({nb_articles} articles supprimés)")


class GestionnaireCommandes:
    """Gestionnaire de commandes"""

    def __init__(self):
        self.commandes: list[dict] = []
        self.logger = logging.getLogger('ecommerce.commandes')
        self.logger.info("Gestionnaire de commandes initialisé")

    def passer_commande(self, panier: Panier) -> bool:
        """Passe une commande à partir d'un panier"""
        self.logger.info(f"Traitement de commande pour le client {panier.client_id}")

        if not panier.articles:
            self.logger.warning("Impossible de passer commande: panier vide")
            return False

        # Vérifier et réduire les stocks
        for produit, quantite in panier.articles.values():
            if not produit.reduire_stock(quantite):
                self.logger.error(f"Échec de la commande: stock insuffisant pour {produit.nom}")
                return False

        # Créer la commande
        commande = {
            'id': len(self.commandes) + 1,
            'client_id': panier.client_id,
            'articles': [(p.nom, q) for p, q in panier.articles.values()],
            'total': panier.calculer_total(),
            'date': datetime.now(),
            'statut': 'confirmée'
        }

        self.commandes.append(commande)
        self.logger.info(f"Commande #{commande['id']} créée avec succès: {commande['total']:.2f} EUR")

        panier.vider()
        return True

    def afficher_commandes(self):
        """Affiche toutes les commandes"""
        self.logger.debug(f"Affichage de {len(self.commandes)} commandes")

        for commande in self.commandes:
            print(f"\nCommande #{commande['id']}")
            print(f"   Client: {commande['client_id']}")
            print(f"   Date: {commande['date'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Articles: {commande['articles']}")
            print(f"   Total: {commande['total']:.2f} EUR")
            print(f"   Statut: {commande['statut']}")


# Démonstration
def main():
    """Fonction principale de démonstration"""
    logger = logging.getLogger('ecommerce.main')
    logger.info("=" * 50)
    logger.info("Démarrage de l'application e-commerce")
    logger.info("=" * 50)

    # Créer des produits
    p1 = Produit(1, "Ordinateur portable", 899.99, 5)
    p2 = Produit(2, "Souris sans fil", 25.99, 20)
    p3 = Produit(3, "Clavier mécanique", 129.99, 3)

    # Créer un panier
    panier = Panier("client_001")

    # Ajouter des produits
    panier.ajouter(p1, 1)
    panier.ajouter(p2, 2)
    panier.ajouter(p3, 1)

    # Tentative d'ajout avec stock insuffisant
    panier.ajouter(p3, 5)  # Stock insuffisant

    print(f"\nTotal du panier: {panier.calculer_total():.2f} EUR")

    # Passer la commande
    gestionnaire = GestionnaireCommandes()
    succes = gestionnaire.passer_commande(panier)

    if succes:
        logger.info("Commande passée avec succès")
        gestionnaire.afficher_commandes()
    else:
        logger.error("Échec de la commande")

    logger.info("Fin de l'application")

    # Afficher le contenu du fichier de log
    ecommerce_log = os.path.join(tmpdir, 'ecommerce.log')
    print("\n--- Extrait du fichier ecommerce.log (5 dernières lignes) ---")
    with open(ecommerce_log) as f:
        lignes = f.readlines()
        for ligne in lignes[-5:]:
            print(f"  {ligne.strip()}")

    # Nettoyage
    print(f"\nNettoyage des logs temporaires...")
    shutil.rmtree(tmpdir)
    print("Nettoyage terminé.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Erreur critique: {e}", exc_info=True)
