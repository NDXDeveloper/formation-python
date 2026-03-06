# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Configuration avancée par dictionnaire (dictConfig),
#                 configuration depuis un fichier INI
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import logging.config
import tempfile
import os
import shutil

# Créer un dossier temporaire pour les logs
tmpdir = tempfile.mkdtemp(prefix="logging_dictconfig_")

# ==========================================
# 1. Configuration par dictionnaire
# ==========================================
print("=== Configuration par dictionnaire (dictConfig) ===")

app_log = os.path.join(tmpdir, 'app.log')
errors_log = os.path.join(tmpdir, 'errors.log')

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
            'filename': app_log,
            'mode': 'w'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': errors_log,
            'mode': 'w'
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
        'level': 'WARNING',
        'handlers': ['console']
    }
}

# Appliquer la configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Utilisation
logger = logging.getLogger('mon_app')
logger.debug("Message de débogage (fichier seulement)")
logger.info("Message d'information")
logger.warning("Message d'avertissement")
logger.error("Message d'erreur")

# Vérifier les fichiers
print(f"\nContenu de app.log :")
with open(app_log) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

print(f"\nContenu de errors.log :")
with open(errors_log) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

# ==========================================
# 2. Configuration depuis un fichier INI
# ==========================================
print("\n=== Configuration depuis un fichier INI ===")

# Créer un fichier de configuration INI
ini_file = os.path.join(tmpdir, 'logging.conf')
ini_log = os.path.join(tmpdir, 'ini_app.log')

with open(ini_file, 'w') as f:
    f.write(f"""[loggers]
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
qualname=mon_app_ini
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
args=('{ini_log}', 'w')

[formatter_simple]
format=%(levelname)s - %(message)s

[formatter_detailed]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
""")

print(f"Fichier INI créé : {os.path.basename(ini_file)}")

# Charger la configuration depuis le fichier INI
logging.config.fileConfig(ini_file)

# Utilisation
logger_ini = logging.getLogger('mon_app_ini')
logger_ini.info("Configuration chargée depuis le fichier INI")
logger_ini.debug("Message de débogage via config INI")
logger_ini.warning("Avertissement via config INI")

# Vérifier le fichier
print(f"\nContenu de ini_app.log :")
with open(ini_log) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

# ==========================================
# Nettoyage
# ==========================================
print(f"\nNettoyage du dossier temporaire...")
shutil.rmtree(tmpdir)
print("Nettoyage terminé.")
