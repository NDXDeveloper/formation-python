🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.5 Le module logging et configuration

## Introduction

Le logging (journalisation) est un aspect essentiel du développement d'applications. Plutôt que d'utiliser `print()` pour déboguer ou suivre l'exécution d'un programme, Python offre le module `logging` qui est beaucoup plus puissant et flexible.

Le logging permet de :
- Enregistrer des informations sur l'exécution du programme
- Suivre les erreurs et les avertissements
- Déboguer plus facilement
- Conserver un historique des événements
- Adapter le niveau de détail selon le contexte (développement, production)

---

## Pourquoi utiliser logging plutôt que print() ?

```python
# ❌ Avec print() - Limites évidentes
def diviser(a, b):
    print(f"Division de {a} par {b}")
    if b == 0:
        print("ERREUR: Division par zéro!")
        return None
    resultat = a / b
    print(f"Résultat: {resultat}")
    return resultat

# Problèmes avec print() :
# - Impossible de désactiver facilement
# - Pas de distinction entre info, erreur, avertissement
# - Difficile de rediriger vers un fichier
# - Mélange avec la sortie normale du programme
# - Pas d'horodatage automatique

# ✅ Avec logging - Beaucoup mieux !
import logging

def diviser_avec_log(a, b):
    logging.info(f"Division de {a} par {b}")
    if b == 0:
        logging.error("Division par zéro!")
        return None
    resultat = a / b
    logging.info(f"Résultat: {resultat}")
    return resultat

# Avantages :
# - Niveaux de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# - Facile à activer/désactiver
# - Redirection vers fichiers
# - Format personnalisable
# - Horodatage automatique
```

---

## Le module `logging` - Concepts de base

### Import du module

```python
import logging
```

---

## Niveaux de log

Le module `logging` définit 5 niveaux de gravité, du moins grave au plus grave :

| Niveau | Valeur | Usage |
|--------|--------|-------|
| **DEBUG** | 10 | Informations détaillées pour le débogage |
| **INFO** | 20 | Confirmation que les choses fonctionnent |
| **WARNING** | 30 | Avertissement, quelque chose d'inattendu |
| **ERROR** | 40 | Erreur, une fonction n'a pas pu s'exécuter |
| **CRITICAL** | 50 | Erreur grave, le programme pourrait s'arrêter |

### Utilisation basique

```python
import logging

# Par défaut, seuls les messages WARNING et supérieurs sont affichés
logging.debug("Message de débogage - pas affiché par défaut")
logging.info("Message d'information - pas affiché par défaut")
logging.warning("Message d'avertissement - AFFICHÉ")
logging.error("Message d'erreur - AFFICHÉ")
logging.critical("Message critique - AFFICHÉ")

# Sortie :
# WARNING:root:Message d'avertissement - AFFICHÉ
# ERROR:root:Message d'erreur - AFFICHÉ
# CRITICAL:root:Message critique - AFFICHÉ
```

---

## Configuration de base

### basicConfig() - Configuration simple

```python
import logging

# Configurer le logging pour afficher tous les niveaux
logging.basicConfig(level=logging.DEBUG)

logging.debug("Ceci est un message de débogage")
logging.info("Ceci est une information")
logging.warning("Ceci est un avertissement")
logging.error("Ceci est une erreur")
logging.critical("Ceci est critique")
```

### Personnaliser le format

```python
import logging

# Configuration avec format personnalisé
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Message avec format personnalisé")
# 2025-10-27 14:30:45 - INFO - Message avec format personnalisé
```

### Variables de formatage courantes

| Variable | Description | Exemple |
|----------|-------------|---------|
| `%(asctime)s` | Date et heure | 2025-10-27 14:30:45 |
| `%(levelname)s` | Niveau du log | INFO, ERROR, etc. |
| `%(message)s` | Le message | Le message du log |
| `%(name)s` | Nom du logger | root, mon_app |
| `%(filename)s` | Nom du fichier | script.py |
| `%(funcName)s` | Nom de la fonction | ma_fonction |
| `%(lineno)d` | Numéro de ligne | 42 |
| `%(pathname)s` | Chemin complet du fichier | /path/to/script.py |

### Exemple avec format détaillé

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)-8s %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def ma_fonction():
    logging.info("Fonction exécutée")
    logging.debug("Détails de débogage")

ma_fonction()

# [2025-10-27 14:30:45] INFO     script.py:12 - Fonction exécutée
# [2025-10-27 14:30:45] DEBUG    script.py:13 - Détails de débogage
```

---

## Écrire dans un fichier

### Configuration pour écrire dans un fichier

```python
import logging

# Écrire les logs dans un fichier
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'  # 'w' écrase, 'a' ajoute à la fin
)

logging.info("Ce message va dans le fichier")
logging.error("Cette erreur aussi")
```

### Écrire à la fois dans un fichier et la console

Pour afficher les logs à la fois dans la console et dans un fichier, il faut utiliser des handlers.

```python
import logging

# Créer le logger
logger = logging.getLogger('mon_app')
logger.setLevel(logging.DEBUG)

# Format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handler pour fichier
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Handler pour console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Moins de détails dans la console
console_handler.setFormatter(formatter)

# Ajouter les handlers au logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Utilisation
logger.debug("Message de débogage - seulement dans le fichier")
logger.info("Message d'info - fichier ET console")
logger.error("Message d'erreur - fichier ET console")
```

---

## Loggers nommés

Plutôt que d'utiliser le logger racine, il est recommandé de créer des loggers nommés pour différentes parties de votre application.

```python
import logging

# Créer des loggers pour différents modules
logger_auth = logging.getLogger('auth')
logger_db = logging.getLogger('database')
logger_api = logging.getLogger('api')

# Configuration basique
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# Utilisation
logger_auth.info("Utilisateur connecté")
logger_db.debug("Connexion à la base de données")
logger_api.warning("Taux de requêtes élevé")

# Sortie :
# auth - INFO - Utilisateur connecté
# database - DEBUG - Connexion à la base de données
# api - WARNING - Taux de requêtes élevé
```

### Hiérarchie des loggers

Les loggers suivent une hiérarchie basée sur les points dans leurs noms :

```python
import logging

# Hiérarchie : app -> app.module -> app.module.fonction
logger_app = logging.getLogger('app')
logger_module = logging.getLogger('app.module')
logger_fonction = logging.getLogger('app.module.fonction')

# Configuration
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(message)s')

logger_app.info("Log de l'application")
logger_module.info("Log du module")
logger_fonction.info("Log de la fonction")

# Sortie :
# app - Log de l'application
# app.module - Log du module
# app.module.fonction - Log de la fonction
```

---

## Exemple pratique : Application avec logging

```python
import logging
from datetime import datetime

class GestionnaireUtilisateurs:
    """Gestionnaire d'utilisateurs avec logging"""

    def __init__(self):
        # Créer un logger pour cette classe
        self.logger = logging.getLogger(__name__)
        self.utilisateurs = {}

    def ajouter_utilisateur(self, username, email):
        """Ajoute un nouvel utilisateur"""
        self.logger.info(f"Tentative d'ajout de l'utilisateur: {username}")

        if username in self.utilisateurs:
            self.logger.warning(f"L'utilisateur {username} existe déjà")
            return False

        if '@' not in email:
            self.logger.error(f"Email invalide pour {username}: {email}")
            return False

        self.utilisateurs[username] = {
            'email': email,
            'created_at': datetime.now()
        }

        self.logger.info(f"Utilisateur {username} ajouté avec succès")
        self.logger.debug(f"Détails: {self.utilisateurs[username]}")
        return True

    def supprimer_utilisateur(self, username):
        """Supprime un utilisateur"""
        self.logger.info(f"Tentative de suppression de l'utilisateur: {username}")

        if username not in self.utilisateurs:
            self.logger.error(f"L'utilisateur {username} n'existe pas")
            return False

        del self.utilisateurs[username]
        self.logger.info(f"Utilisateur {username} supprimé")
        return True

    def lister_utilisateurs(self):
        """Liste tous les utilisateurs"""
        self.logger.debug(f"Listage de {len(self.utilisateurs)} utilisateurs")
        return list(self.utilisateurs.keys())

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Utilisation
gestionnaire = GestionnaireUtilisateurs()

gestionnaire.ajouter_utilisateur("alice", "alice@example.com")
gestionnaire.ajouter_utilisateur("bob", "bob@example.com")
gestionnaire.ajouter_utilisateur("alice", "alice2@example.com")  # Doublon
gestionnaire.ajouter_utilisateur("charlie", "invalide")  # Email invalide
gestionnaire.supprimer_utilisateur("bob")
gestionnaire.supprimer_utilisateur("david")  # N'existe pas

print("\nUtilisateurs:", gestionnaire.lister_utilisateurs())
```

---

## Handlers - Gestionnaires de destination

Les handlers déterminent où vont les messages de log (console, fichier, email, etc.).

### Types de handlers courants

```python
import logging

logger = logging.getLogger('mon_app')
logger.setLevel(logging.DEBUG)

# 1. StreamHandler - Sortie console (stdout/stderr)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 2. FileHandler - Fichier simple
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# 3. RotatingFileHandler - Rotation par taille
from logging.handlers import RotatingFileHandler
rotating_handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1 MB
    backupCount=5        # Garde 5 fichiers de backup
)

# 4. TimedRotatingFileHandler - Rotation par temps
from logging.handlers import TimedRotatingFileHandler
timed_handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',     # Rotation à minuit
    interval=1,          # Tous les jours
    backupCount=7        # Garde 7 jours
)

# Ajouter des formatters
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Ajouter au logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

### Exemple avec RotatingFileHandler

```python
import logging
from logging.handlers import RotatingFileHandler

# Configuration avec rotation de fichiers
logger = logging.getLogger('app_rotation')
logger.setLevel(logging.DEBUG)

# Handler avec rotation (max 1KB, 3 fichiers de backup)
handler = RotatingFileHandler(
    'app_rotating.log',
    maxBytes=1024,
    backupCount=3
)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Générer beaucoup de logs pour tester la rotation
for i in range(100):
    logger.info(f"Message numéro {i} - " + "x" * 50)

# Résultat : app_rotating.log, app_rotating.log.1, app_rotating.log.2, app_rotating.log.3
```

---

## Filtres personnalisés

Les filtres permettent de contrôler quels messages de log sont traités.

```python
import logging

class FiltreNiveauSpecifique(logging.Filter):
    """Filtre qui accepte uniquement certains niveaux"""

    def __init__(self, niveaux):
        super().__init__()
        self.niveaux = niveaux

    def filter(self, record):
        return record.levelno in self.niveaux

# Configuration
logger = logging.getLogger('app_filtree')
logger.setLevel(logging.DEBUG)

# Handler pour les erreurs uniquement
error_handler = logging.FileHandler('errors.log')
error_handler.setLevel(logging.DEBUG)
error_handler.addFilter(FiltreNiveauSpecifique([logging.ERROR, logging.CRITICAL]))

# Handler pour les infos uniquement
info_handler = logging.FileHandler('info.log')
info_handler.setLevel(logging.DEBUG)
info_handler.addFilter(FiltreNiveauSpecifique([logging.INFO]))

logger.addHandler(error_handler)
logger.addHandler(info_handler)

# Test
logger.debug("Debug - nulle part")
logger.info("Info - dans info.log")
logger.warning("Warning - nulle part")
logger.error("Error - dans errors.log")
```

---

## Configuration avancée

### Configuration par dictionnaire

Pour des applications complexes, la configuration par dictionnaire est recommandée.

```python
import logging
import logging.config

# Configuration complète par dictionnaire
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    # Formatters
    'formatters': {
        'simple': {
            'format': '%(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },

    # Handlers
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'mode': 'a'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': 'errors.log',
            'mode': 'a'
        }
    },

    # Loggers
    'loggers': {
        'mon_app': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error_file'],
            'propagate': False
        }
    },

    # Root logger
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
}

# Appliquer la configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Utilisation
logger = logging.getLogger('mon_app')
logger.debug("Message de débogage")
logger.info("Message d'information")
logger.error("Message d'erreur")
```

### Configuration depuis un fichier

#### logging.conf (format INI)

```ini
[loggers]
keys=root,app

[handlers]
keys=console,file

[formatters]
keys=simple,detailed

[logger_root]
level=INFO
handlers=console

[logger_app]
level=DEBUG
handlers=console,file
qualname=mon_app
propagate=0

[handler_console]
class=StreamHandler
level=INFO
formatter=simple
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=detailed
args=('app.log', 'a')

[formatter_simple]
format=%(levelname)s - %(message)s

[formatter_detailed]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

#### Charger la configuration depuis le fichier

```python
import logging
import logging.config

# Charger la configuration depuis le fichier INI
logging.config.fileConfig('logging.conf')

# Utilisation
logger = logging.getLogger('mon_app')
logger.info("Configuration chargée depuis le fichier")
```

---

## Exemple complet : Application e-commerce

```python
import logging
import logging.config
from datetime import datetime
from typing import Dict, List

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
            'formatter': 'standard'
        },
        'file_all': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'ecommerce.log',
            'maxBytes': 1024 * 1024,  # 1 MB
            'backupCount': 3
        },
        'file_errors': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': 'errors.log'
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
        self.articles: Dict[int, tuple[Produit, int]] = {}
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
        self.logger.debug(f"Total du panier calculé: {total:.2f}€")
        return total

    def vider(self):
        """Vide le panier"""
        nb_articles = len(self.articles)
        self.articles.clear()
        self.logger.info(f"Panier vidé ({nb_articles} articles supprimés)")

class GestionnaireCommandes:
    """Gestionnaire de commandes"""

    def __init__(self):
        self.commandes: List[Dict] = []
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
            'articles': list(panier.articles.values()),
            'total': panier.calculer_total(),
            'date': datetime.now(),
            'statut': 'confirmée'
        }

        self.commandes.append(commande)
        self.logger.info(f"Commande #{commande['id']} créée avec succès: {commande['total']:.2f}€")

        # Vider le panier
        panier.vider()

        return True

    def afficher_commandes(self):
        """Affiche toutes les commandes"""
        self.logger.debug(f"Affichage de {len(self.commandes)} commandes")

        for commande in self.commandes:
            print(f"\n📦 Commande #{commande['id']}")
            print(f"   Client: {commande['client_id']}")
            print(f"   Date: {commande['date'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Total: {commande['total']:.2f}€")
            print(f"   Statut: {commande['statut']}")

# Démonstration
def main():
    """Fonction principale de démonstration"""
    logger = logging.getLogger('ecommerce.main')
    logger.info("=" * 60)
    logger.info("Démarrage de l'application e-commerce")
    logger.info("=" * 60)

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

    print(f"\n💰 Total du panier: {panier.calculer_total():.2f}€")

    # Passer la commande
    gestionnaire = GestionnaireCommandes()
    succes = gestionnaire.passer_commande(panier)

    if succes:
        logger.info("Commande passée avec succès")
        gestionnaire.afficher_commandes()
    else:
        logger.error("Échec de la commande")

    logger.info("Fin de l'application")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Erreur critique: {e}", exc_info=True)
```

---

## Gestion des exceptions avec logging

### Enregistrer les stack traces

```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def diviser(a, b):
    try:
        resultat = a / b
        logging.info(f"Division réussie: {a} / {b} = {resultat}")
        return resultat
    except ZeroDivisionError:
        # exc_info=True ajoute la stack trace
        logging.error("Division par zéro!", exc_info=True)
        return None
    except Exception as e:
        # Ou utiliser logging.exception() qui ajoute automatiquement exc_info
        logging.exception("Erreur inattendue lors de la division")
        return None

# Test
diviser(10, 2)   # OK
diviser(10, 0)   # Erreur avec stack trace
```

### logging.exception() - Raccourci pratique

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def fonction_risquee():
    try:
        # Code qui pourrait échouer
        resultat = 10 / 0
    except Exception:
        # logging.exception() est équivalent à logging.error(..., exc_info=True)
        logging.exception("Une erreur s'est produite")

fonction_risquee()
```

---

## Bonnes pratiques

### 1. Utiliser des loggers nommés

```python
# ❌ Mauvais : utiliser le logger racine
import logging
logging.info("Message")

# ✅ Bon : créer un logger nommé
import logging
logger = logging.getLogger(__name__)
logger.info("Message")
```

### 2. Configurer le logging une seule fois

```python
# ✅ Dans le fichier principal (main.py)
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

if __name__ == "__main__":
    setup_logging()
    # ... reste du code
```

### 3. Ne jamais utiliser basicConfig() dans les bibliothèques

```python
# ❌ Dans une bibliothèque/module
import logging
logging.basicConfig(...)  # NE JAMAIS FAIRE ÇA !

# ✅ Dans une bibliothèque/module
import logging
logger = logging.getLogger(__name__)
# C'est à l'utilisateur de configurer le logging
```

### 4. Utiliser les niveaux de log appropriés

```python
import logging

logger = logging.getLogger(__name__)

# ✅ Utilisation appropriée des niveaux
logger.debug("Valeur de la variable x: 42")  # Débogage détaillé
logger.info("Traitement terminé avec succès")  # Information
logger.warning("Fichier de config manquant, utilisation des valeurs par défaut")  # Avertissement
logger.error("Impossible de se connecter à la base de données")  # Erreur
logger.critical("Le système manque de mémoire!")  # Critique
```

### 5. Utiliser le lazy formatting

```python
import logging

logger = logging.getLogger(__name__)

# ❌ Mauvais : formatage immédiat (coûteux même si non loggé)
logger.debug("Valeur: " + str(valeur_couteuse_a_calculer()))

# ✅ Bon : lazy formatting (évalué seulement si nécessaire)
logger.debug("Valeur: %s", valeur_couteuse_a_calculer())
logger.debug("Valeur: {}", valeur_couteuse_a_calculer())  # Python 3.2+
```

### 6. Éviter les informations sensibles dans les logs

```python
import logging

logger = logging.getLogger(__name__)

# ❌ Mauvais : logguer des informations sensibles
logger.info(f"Connexion avec mot de passe: {password}")

# ✅ Bon : masquer les informations sensibles
logger.info(f"Tentative de connexion pour l'utilisateur: {username}")
logger.info(f"Mot de passe fourni: {'*' * len(password)}")
```

### 7. Créer une fonction de configuration réutilisable

```python
import logging
from pathlib import Path

def setup_logging(
    log_level=logging.INFO,
    log_file=None,
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
):
    """Configure le logging de l'application"""

    # Configuration de base
    handlers = []

    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)

    # Handler fichier si spécifié
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)

    # Configuration du logger racine
    logging.basicConfig(
        level=log_level,
        handlers=handlers
    )

    logging.info("Logging configuré avec succès")

# Utilisation
setup_logging(log_level=logging.DEBUG, log_file='logs/app.log')
```

---

## Exemple pratique : Application web avec logging

```python
import logging
import logging.config
from datetime import datetime

# Configuration adaptée à une application web
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'web': {
            'format': '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'access': {
            'format': '%(asctime)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'web'
        },
        'app_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'web',
            'filename': 'logs/app.log',
            'maxBytes': 10485760,  # 10 MB
            'backupCount': 5
        },
        'access_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'access',
            'filename': 'logs/access.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'web',
            'filename': 'logs/errors.log'
        }
    },

    'loggers': {
        'app': {
            'level': 'DEBUG',
            'handlers': ['console', 'app_file', 'error_file'],
            'propagate': False
        },
        'app.access': {
            'level': 'INFO',
            'handlers': ['access_file'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

class SimpleWebApp:
    """Simulation d'une application web simple"""

    def __init__(self):
        self.logger = logging.getLogger('app')
        self.access_logger = logging.getLogger('app.access')
        self.users = {'admin': 'password123'}
        self.logger.info("Application web démarrée")

    def log_request(self, method, path, status_code, user=None):
        """Log une requête HTTP"""
        user_info = f"user={user}" if user else "anonymous"
        self.access_logger.info(f"{method} {path} - {status_code} - {user_info}")

    def login(self, username, password):
        """Simule une connexion"""
        self.logger.debug(f"Tentative de connexion pour: {username}")

        if username not in self.users:
            self.logger.warning(f"Utilisateur inconnu: {username}")
            self.log_request('POST', '/login', 401, username)
            return False

        if self.users[username] != password:
            self.logger.warning(f"Mot de passe incorrect pour: {username}")
            self.log_request('POST', '/login', 401, username)
            return False

        self.logger.info(f"Connexion réussie: {username}")
        self.log_request('POST', '/login', 200, username)
        return True

    def get_page(self, path, user=None):
        """Simule l'accès à une page"""
        self.logger.debug(f"Accès à la page: {path}")

        if path.startswith('/admin') and user != 'admin':
            self.logger.warning(f"Accès refusé à {path} pour {user}")
            self.log_request('GET', path, 403, user)
            return False

        self.log_request('GET', path, 200, user)
        return True

    def process_data(self, data):
        """Simule le traitement de données"""
        self.logger.debug(f"Traitement de données: {len(data)} éléments")

        try:
            # Simulation d'une erreur
            if len(data) == 0:
                raise ValueError("Données vides")

            result = sum(data)
            self.logger.info(f"Traitement réussi: somme = {result}")
            return result

        except Exception as e:
            self.logger.exception("Erreur lors du traitement des données")
            self.log_request('POST', '/process', 500)
            return None

# Démonstration
app = SimpleWebApp()

print("=== Simulation d'activité web ===\n")

# Connexions
app.login('admin', 'password123')  # Succès
app.login('admin', 'wrongpass')    # Échec
app.login('hacker', 'test')        # Utilisateur inconnu

# Accès aux pages
app.get_page('/', 'admin')
app.get_page('/profile', 'admin')
app.get_page('/admin/settings', 'admin')  # OK
app.get_page('/admin/settings', 'user')   # Refusé

# Traitement de données
app.process_data([1, 2, 3, 4, 5])  # Succès
app.process_data([])                # Erreur

print("\n=== Les logs ont été écrits dans le dossier 'logs/' ===")
```

---

## Résumé

### Niveaux de log

| Niveau | Quand l'utiliser |
|--------|------------------|
| DEBUG | Informations détaillées pour le débogage |
| INFO | Confirmations que tout fonctionne |
| WARNING | Quelque chose d'inattendu mais pas bloquant |
| ERROR | Erreur, une fonctionnalité n'a pas pu s'exécuter |
| CRITICAL | Erreur grave, le programme pourrait s'arrêter |

### Configuration rapide

```python
import logging

# Simple
logging.basicConfig(level=logging.INFO)

# Avec fichier et format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Logger nommé
logger = logging.getLogger(__name__)
logger.info("Message")
```

### Handlers courants

```python
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Rotation par taille
RotatingFileHandler('app.log', maxBytes=1024*1024, backupCount=5)

# Rotation par temps
TimedRotatingFileHandler('app.log', when='midnight', backupCount=7)
```

### Formateurs utiles

```python
# Simple
format='%(levelname)s - %(message)s'

# Complet
format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'

# Avec couleur (nécessite colorlog)
format='%(log_color)s%(levelname)-8s%(reset)s %(message)s'
```

### Exemples d'utilisation

```python
import logging

logger = logging.getLogger(__name__)

# Messages simples
logger.debug("Variable x = 10")
logger.info("Opération terminée")
logger.warning("Attention: mémoire faible")
logger.error("Connexion échouée")
logger.critical("Système en panne!")

# Avec formatage
logger.info("Utilisateur %s connecté", username)
logger.debug("Valeurs: x=%d, y=%d", x, y)

# Exceptions
try:
    resultat = 10 / 0
except Exception:
    logger.exception("Erreur de division")
```

Le module `logging` est un outil essentiel pour créer des applications Python robustes et maintenables. Il permet de suivre l'exécution du programme, de déboguer efficacement et de conserver un historique des événements importants !

⏭️ [typing - Annotations avancées](/07-bibliotheques-standard/06-typing-annotations-avancees.md)
