# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Module logging - niveaux de severite (DEBUG, INFO, WARNING,
#                 ERROR, CRITICAL), fonction avec logging, ecriture fichier
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

import logging
import os

# ==========================================
# 1. Configuration de base et niveaux
# ==========================================
print("=== Logging - Niveaux de severite ===\n")

# Configuration simple vers la console (stderr)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("Message de debogage detaille")
logging.info("Information generale")
logging.warning("Attention, quelque chose d'inhabituel")
logging.error("Une erreur s'est produite")
logging.critical("Erreur critique, le programme doit s'arreter")

# ==========================================
# 2. Exemple pratique avec une fonction
# ==========================================
print("\n=== Logging - Fonction diviser ===\n")

def diviser(a, b):
    logging.debug(f"Tentative de division : {a} / {b}")

    if b == 0:
        logging.error("Division par zero impossible")
        return None

    resultat = a / b
    logging.info(f"Division reussie : {a} / {b} = {resultat}")
    return resultat

print(f"diviser(10, 2) = {diviser(10, 2)}")
print(f"diviser(10, 0) = {diviser(10, 0)}")

# ==========================================
# 3. Enregistrer les logs dans un fichier
# ==========================================
print("\n=== Logging - Ecriture dans un fichier ===\n")

# Creer un logger separe pour le fichier
logger_fichier = logging.getLogger('fichier')
logger_fichier.setLevel(logging.DEBUG)

# Handler pour fichier
fichier_log = 'mon_application.log'
handler = logging.FileHandler(fichier_log, mode='w')
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger_fichier.addHandler(handler)

def traiter_donnees(donnees):
    logger_fichier.info("Debut du traitement")
    try:
        resultat = sum(donnees) / len(donnees)
        logger_fichier.info(f"Traitement reussi : moyenne = {resultat}")
        return resultat
    except Exception as e:
        logger_fichier.error(f"Erreur lors du traitement : {e}")
        raise

moyenne = traiter_donnees([10, 20, 30, 40])
print(f"Moyenne calculee : {moyenne}")

# Lire et afficher le contenu du fichier log
with open(fichier_log, 'r') as f:
    contenu = f.read()
print(f"\nContenu de {fichier_log}:")
for line in contenu.strip().split('\n'):
    print(f"  {line}")

# Nettoyage
os.remove(fichier_log)
print(f"\nFichier {fichier_log} nettoye")
