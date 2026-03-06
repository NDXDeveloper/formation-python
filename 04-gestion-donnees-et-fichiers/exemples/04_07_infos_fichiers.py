# ============================================================================
#   Section 4.4 : Informations sur les fichiers
#   Description : stat() pour taille, dates de modification/création,
#                 fonction d'informations détaillées
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
from datetime import datetime
import os

# Créer un fichier de test
Path('mon_fichier.txt').write_text("Bonjour depuis pathlib !\nDeuxième ligne.\n",
                                   encoding='utf-8')

# --- Statistiques d'un fichier ---
print("=== Statistiques ===")

fichier = Path('mon_fichier.txt')

if fichier.exists():
    stats = fichier.stat()

    taille = stats.st_size
    print(f"Taille : {taille} octets ({taille / 1024:.2f} Ko)")

    timestamp = stats.st_mtime
    date_modif = datetime.fromtimestamp(timestamp)
    print(f"Dernière modification : {date_modif}")

    timestamp_creation = stats.st_ctime
    date_creation = datetime.fromtimestamp(timestamp_creation)
    print(f"Création/Changement : {date_creation}")

# --- Fonction d'informations détaillées ---
print()

def infos_fichier(chemin_str):
    """Affiche des informations détaillées sur un fichier"""
    chemin = Path(chemin_str)

    if not chemin.exists():
        print(f"{chemin} n'existe pas")
        return

    print(f"{'='*60}")
    print(f"Informations : {chemin.name}")
    print(f"{'='*60}")

    if chemin.is_file():
        print(f"Type : Fichier")
    elif chemin.is_dir():
        print(f"Type : Dossier")

    print(f"Chemin complet : {chemin.absolute()}")
    print(f"Dossier parent : {chemin.parent}")

    if chemin.is_file():
        print(f"Extension : {chemin.suffix}")
        stats = chemin.stat()
        taille = stats.st_size
        print(f"Taille : {taille:,} octets")
        modif = datetime.fromtimestamp(stats.st_mtime)
        print(f"Dernière modification : {modif.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"{'='*60}\n")

infos_fichier('mon_fichier.txt')
infos_fichier('inexistant.xyz')

# Nettoyage
os.remove('mon_fichier.txt')
