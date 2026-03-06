# ============================================================================
#   Section 7.5 : Le module logging et configuration
#   Description : Logging vs print, niveaux de log, basicConfig, format
#                 personnalisé, variables de formatage
#   Fichier source : 05-logging-et-configuration.md
# ============================================================================

import logging
import subprocess
import sys
import textwrap
import tempfile
import os

# ==========================================
# 1. Pourquoi logging plutôt que print()
# ==========================================
print("=== Logging vs print() ===")

# Avec print() - Limites évidentes
def diviser(a, b):
    print(f"Division de {a} par {b}")
    if b == 0:
        print("ERREUR: Division par zéro!")
        return None
    resultat = a / b
    print(f"Résultat: {resultat}")
    return resultat

diviser(10, 3)
diviser(10, 0)

# Avec logging - Beaucoup mieux !
# Note : on utilise un subprocess pour chaque config basicConfig
# car basicConfig ne peut être appelé qu'une fois par processus

print("\n--- Avec logging ---")
script = textwrap.dedent("""\
    import logging

    def diviser_avec_log(a, b):
        logging.info(f"Division de {a} par {b}")
        if b == 0:
            logging.error("Division par zéro!")
            return None
        resultat = a / b
        logging.info(f"Résultat: {resultat}")
        return resultat

    # Par défaut, seuls WARNING et supérieurs sont affichés
    logging.basicConfig(level=logging.WARNING)
    diviser_avec_log(10, 3)
    diviser_avec_log(10, 0)
""")

tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
tmpfile.write(script)
tmpfile.close()
result = subprocess.run([sys.executable, tmpfile.name], capture_output=True, text=True)
print(result.stderr.strip() if result.stderr.strip() else "(Seul le message ERROR s'affiche)")
os.unlink(tmpfile.name)

# ==========================================
# 2. Niveaux de log
# ==========================================
print("\n=== Niveaux de log ===")

print(f"DEBUG    = {logging.DEBUG}")
print(f"INFO     = {logging.INFO}")
print(f"WARNING  = {logging.WARNING}")
print(f"ERROR    = {logging.ERROR}")
print(f"CRITICAL = {logging.CRITICAL}")

# ==========================================
# 3. Utilisation basique (par défaut WARNING+)
# ==========================================
print("\n=== Utilisation basique (par défaut) ===")

script = textwrap.dedent("""\
    import logging

    # Par défaut, seuls les messages WARNING et supérieurs sont affichés
    logging.debug("Message de débogage - pas affiché par défaut")
    logging.info("Message d'information - pas affiché par défaut")
    logging.warning("Message d'avertissement - AFFICHÉ")
    logging.error("Message d'erreur - AFFICHÉ")
    logging.critical("Message critique - AFFICHÉ")
""")

tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
tmpfile.write(script)
tmpfile.close()
result = subprocess.run([sys.executable, tmpfile.name], capture_output=True, text=True)
print(result.stderr.strip())
os.unlink(tmpfile.name)

# ==========================================
# 4. basicConfig() - Afficher tous les niveaux
# ==========================================
print("\n=== basicConfig(level=DEBUG) ===")

script = textwrap.dedent("""\
    import logging

    logging.basicConfig(level=logging.DEBUG)

    logging.debug("Ceci est un message de débogage")
    logging.info("Ceci est une information")
    logging.warning("Ceci est un avertissement")
    logging.error("Ceci est une erreur")
    logging.critical("Ceci est critique")
""")

tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
tmpfile.write(script)
tmpfile.close()
result = subprocess.run([sys.executable, tmpfile.name], capture_output=True, text=True)
print(result.stderr.strip())
os.unlink(tmpfile.name)

# ==========================================
# 5. Format personnalisé
# ==========================================
print("\n=== Format personnalisé ===")

script = textwrap.dedent("""\
    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info("Message avec format personnalisé")
    logging.warning("Un avertissement formaté")
""")

tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
tmpfile.write(script)
tmpfile.close()
result = subprocess.run([sys.executable, tmpfile.name], capture_output=True, text=True)
print(result.stderr.strip())
os.unlink(tmpfile.name)

# ==========================================
# 6. Format détaillé avec filename et lineno
# ==========================================
print("\n=== Format détaillé ===")

script = textwrap.dedent("""\
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
""")

tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
tmpfile.write(script)
tmpfile.close()
result = subprocess.run([sys.executable, tmpfile.name], capture_output=True, text=True)
print(result.stderr.strip())
os.unlink(tmpfile.name)
