# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Exemple complet - Simulation d'application web avec
#                 logging (accès, authentification, erreurs, dictConfig)
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import logging.config
from datetime import datetime
import tempfile
import os
import shutil

# Créer un dossier temporaire pour les logs
tmpdir = tempfile.mkdtemp(prefix="webapp_logs_")
os.makedirs(os.path.join(tmpdir, 'logs'), exist_ok=True)
logs_dir = os.path.join(tmpdir, 'logs')

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
            'formatter': 'web',
            'stream': 'ext://sys.stdout'
        },
        'app_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'web',
            'filename': os.path.join(logs_dir, 'app.log'),
            'maxBytes': 10485760,
            'backupCount': 5
        },
        'access_file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'access',
            'filename': os.path.join(logs_dir, 'access.log')
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'web',
            'filename': os.path.join(logs_dir, 'errors.log')
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
            if len(data) == 0:
                raise ValueError("Données vides")

            result = sum(data)
            self.logger.info(f"Traitement réussi: somme = {result}")
            return result

        except Exception:
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

# Afficher les fichiers de log
print("\n--- Contenu de access.log ---")
with open(os.path.join(logs_dir, 'access.log')) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

print("\n--- Contenu de errors.log ---")
errors_file = os.path.join(logs_dir, 'errors.log')
with open(errors_file) as f:
    contenu = f.read().strip()
    if contenu:
        # Afficher seulement la première ligne de l'erreur (pas toute la stacktrace)
        lignes = contenu.split('\n')
        print(f"  {lignes[0]}")
        print(f"  ... ({len(lignes) - 1} lignes de stack trace)")
    else:
        print("  (vide)")

# Nettoyage
print(f"\nNettoyage des logs temporaires...")
shutil.rmtree(tmpdir)
print("Nettoyage terminé.")
