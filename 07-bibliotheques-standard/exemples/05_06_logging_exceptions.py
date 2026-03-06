# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Gestion des exceptions avec logging - exc_info,
#                 logging.exception(), stack traces
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

# ==========================================
# 1. Enregistrer les stack traces
# ==========================================
print("=== Stack traces avec exc_info ===")

def diviser(a, b):
    try:
        resultat = a / b
        logging.info(f"Division réussie: {a} / {b} = {resultat}")
        return resultat
    except ZeroDivisionError:
        # exc_info=True ajoute la stack trace
        logging.error("Division par zéro!", exc_info=True)
        return None
    except Exception:
        # logging.exception() ajoute automatiquement exc_info
        logging.exception("Erreur inattendue lors de la division")
        return None

# Test
diviser(10, 2)   # OK
print()
diviser(10, 0)   # Erreur avec stack trace

# ==========================================
# 2. logging.exception() - Raccourci pratique
# ==========================================
print("\n=== logging.exception() ===")

def fonction_risquee():
    try:
        resultat = 10 / 0
    except Exception:
        # logging.exception() est équivalent à logging.error(..., exc_info=True)
        logging.exception("Une erreur s'est produite")

fonction_risquee()

# ==========================================
# 3. Bonnes pratiques - Niveaux appropriés
# ==========================================
print("\n=== Bonnes pratiques - Niveaux appropriés ===")

logger = logging.getLogger('bonnes_pratiques')

logger.debug("Valeur de la variable x: 42")             # Débogage détaillé
logger.info("Traitement terminé avec succès")             # Information
logger.warning("Fichier de config manquant, valeurs par défaut")  # Avertissement
logger.error("Impossible de se connecter à la base")     # Erreur
logger.critical("Le système manque de mémoire!")          # Critique

# ==========================================
# 4. Lazy formatting vs f-strings
# ==========================================
print("\n=== Lazy formatting ===")

username = "alice"
count = 5

# Lazy formatting avec %s (recommandé pour le logging)
logger.info("Utilisateur %s connecté", username)
logger.debug("Utilisateur %s a effectué %d actions", username, count)

# Comparaison des approches
print("\nApproches de formatage :")
print("  logger.debug('Valeur: ' + str(x))      # Mauvais : concaténation")
print("  logger.debug(f'Valeur: {x}')            # Mauvais : f-string")
print("  logger.debug('Valeur: %s', x)           # Bon : lazy formatting")

# ==========================================
# 5. Masquer les informations sensibles
# ==========================================
print("\n=== Masquer les informations sensibles ===")

password = "secret123"
logger.info("Tentative de connexion pour l'utilisateur: %s", username)
logger.info("Mot de passe fourni: %s", '*' * len(password))
