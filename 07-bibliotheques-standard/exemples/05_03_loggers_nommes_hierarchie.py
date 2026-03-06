# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Loggers nommés, hiérarchie des loggers, filtres
#                 personnalisés
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import tempfile
import os
import shutil

# ==========================================
# 1. Loggers nommés
# ==========================================
print("=== Loggers nommés ===")

# Configurer le logging de base
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# Créer des loggers pour différents modules
logger_auth = logging.getLogger('auth')
logger_db = logging.getLogger('database')
logger_api = logging.getLogger('api')

logger_auth.info("Utilisateur connecté")
logger_db.debug("Connexion à la base de données")
logger_api.warning("Taux de requêtes élevé")

# ==========================================
# 2. Hiérarchie des loggers
# ==========================================
print("\n=== Hiérarchie des loggers ===")

# Hiérarchie : app -> app.module -> app.module.fonction
logger_app = logging.getLogger('app')
logger_module = logging.getLogger('app.module')
logger_fonction = logging.getLogger('app.module.fonction')

logger_app.info("Log de l'application")
logger_module.info("Log du module")
logger_fonction.info("Log de la fonction")

# ==========================================
# 3. Filtres personnalisés
# ==========================================
print("\n=== Filtres personnalisés ===")

tmpdir = tempfile.mkdtemp(prefix="logging_filtres_")

class FiltreNiveauSpecifique(logging.Filter):
    """Filtre qui accepte uniquement certains niveaux"""

    def __init__(self, niveaux):
        super().__init__()
        self.niveaux = niveaux

    def filter(self, record):
        return record.levelno in self.niveaux

# Configuration
logger_filtre = logging.getLogger('app_filtree')
logger_filtre.setLevel(logging.DEBUG)
# Empêcher la propagation vers le root logger
logger_filtre.propagate = False

errors_log = os.path.join(tmpdir, 'errors.log')
info_log = os.path.join(tmpdir, 'info.log')

# Handler pour les erreurs uniquement
error_handler = logging.FileHandler(errors_log)
error_handler.setLevel(logging.DEBUG)
error_handler.addFilter(FiltreNiveauSpecifique([logging.ERROR, logging.CRITICAL]))

# Handler pour les infos uniquement
info_handler = logging.FileHandler(info_log)
info_handler.setLevel(logging.DEBUG)
info_handler.addFilter(FiltreNiveauSpecifique([logging.INFO]))

# Handler console pour voir ce qui se passe
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('  %(levelname)s - %(message)s'))
logger_filtre.addHandler(console_handler)

logger_filtre.addHandler(error_handler)
logger_filtre.addHandler(info_handler)

# Test
logger_filtre.debug("Debug - nulle part (sauf console)")
logger_filtre.info("Info - dans info.log")
logger_filtre.warning("Warning - nulle part (sauf console)")
logger_filtre.error("Error - dans errors.log")
logger_filtre.critical("Critical - dans errors.log")

# Vérifier les fichiers
print(f"\nContenu de errors.log :")
with open(errors_log) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

print(f"\nContenu de info.log :")
with open(info_log) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

# Nettoyage
logger_filtre.removeHandler(error_handler)
logger_filtre.removeHandler(info_handler)
logger_filtre.removeHandler(console_handler)
error_handler.close()
info_handler.close()

shutil.rmtree(tmpdir)
print(f"\nNettoyage terminé.")
