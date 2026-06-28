# ============================================================================
#   Section 4.4 : Localiser un fichier par rapport au script (__file__)
#   Description : Path(__file__).parent vise le dossier du SCRIPT, pas le
#                 répertoire de lancement (cwd) -> chemins robustes vers
#                 les ressources livrées avec le programme
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

# __file__ est le chemin de CE fichier .py ; .resolve().parent donne le
# dossier qui le contient, sous forme absolue et normalisée.
script = Path(__file__).resolve()
dossier_script = script.parent

print("Nom de ce script :", script.name)

# Construire un chemin vers un fichier VOISIN du script (à côté de lui).
# Peu importe d'où on lance la commande python, ce chemin reste correct.
config = dossier_script / 'config.json'
print("Fichier visé     :", config.name)
print("Situé à côté du script ?", config.parent == dossier_script)   # True

# Le répertoire de travail (cwd) est celui d'où on lance la commande :
# il peut différer du dossier du script. C'est pourquoi un chemin relatif
# nu comme open('config.json') n'est PAS fiable -> on part de __file__.
print("cwd identique au dossier du script ?", Path.cwd() == dossier_script)
