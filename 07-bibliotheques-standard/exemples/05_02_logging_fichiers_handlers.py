# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Écrire dans un fichier, handlers (FileHandler,
#                 RotatingFileHandler, TimedRotatingFileHandler),
#                 console + fichier simultanément
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import logging.handlers
import tempfile
import os
import shutil

# Créer un dossier temporaire pour les logs
tmpdir = tempfile.mkdtemp(prefix="logging_demo_")
print(f"Dossier temporaire : {tmpdir}")

# ==========================================
# 1. Écrire dans un fichier
# ==========================================
print("\n=== Écrire dans un fichier ===")

# On utilise un logger nommé pour éviter les conflits avec basicConfig
logger_file = logging.getLogger('demo_fichier')
logger_file.setLevel(logging.DEBUG)

log_file = os.path.join(tmpdir, 'app.log')
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger_file.addHandler(file_handler)

logger_file.info("Ce message va dans le fichier")
logger_file.error("Cette erreur aussi")

# Vérifier le contenu du fichier
with open(log_file) as f:
    contenu = f.read()
print(f"Contenu de {os.path.basename(log_file)} :")
for ligne in contenu.strip().split('\n'):
    print(f"  {ligne}")

# Nettoyer le handler
logger_file.removeHandler(file_handler)
file_handler.close()

# ==========================================
# 2. Console ET fichier simultanément
# ==========================================
print("\n=== Console ET fichier ===")

logger_dual = logging.getLogger('mon_app_dual')
logger_dual.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%H:%M:%S')

# Handler pour fichier (tout)
dual_log_file = os.path.join(tmpdir, 'dual.log')
fh = logging.FileHandler(dual_log_file, mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Handler pour console (INFO+)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

logger_dual.addHandler(fh)
logger_dual.addHandler(ch)

logger_dual.debug("Message de débogage - seulement dans le fichier")
logger_dual.info("Message d'info - fichier ET console")
logger_dual.error("Message d'erreur - fichier ET console")

# Vérifier le fichier (contient aussi le DEBUG)
print(f"\nContenu de {os.path.basename(dual_log_file)} :")
with open(dual_log_file) as f:
    for ligne in f:
        print(f"  {ligne.strip()}")

logger_dual.removeHandler(fh)
logger_dual.removeHandler(ch)
fh.close()

# ==========================================
# 3. Types de handlers
# ==========================================
print("\n=== Types de handlers ===")

print("Handlers disponibles :")
print("  1. StreamHandler     - Sortie console (stdout/stderr)")
print("  2. FileHandler       - Fichier simple")
print("  3. RotatingFileHandler    - Rotation par taille")
print("  4. TimedRotatingFileHandler - Rotation par temps")

# ==========================================
# 4. RotatingFileHandler
# ==========================================
print("\n=== RotatingFileHandler ===")

logger_rot = logging.getLogger('app_rotation')
logger_rot.setLevel(logging.DEBUG)

rotating_log = os.path.join(tmpdir, 'app_rotating.log')
handler = logging.handlers.RotatingFileHandler(
    rotating_log,
    maxBytes=1024,     # 1 KB pour la démo
    backupCount=3
)

formatter_rot = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter_rot)
logger_rot.addHandler(handler)

# Générer beaucoup de logs pour tester la rotation
for i in range(100):
    logger_rot.info(f"Message numéro {i} - " + "x" * 50)

# Vérifier les fichiers créés
fichiers_log = sorted([f for f in os.listdir(tmpdir) if f.startswith('app_rotating')])
print(f"Fichiers créés par rotation :")
for f in fichiers_log:
    taille = os.path.getsize(os.path.join(tmpdir, f))
    print(f"  {f} ({taille} octets)")

logger_rot.removeHandler(handler)
handler.close()

# ==========================================
# Nettoyage
# ==========================================
print(f"\nNettoyage du dossier temporaire : {tmpdir}")
shutil.rmtree(tmpdir)
print("Nettoyage terminé.")
