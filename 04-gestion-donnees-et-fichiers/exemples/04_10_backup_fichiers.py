# ============================================================================
#   Section 4.4 : Exemple pratique - Backup de fichiers
#   Description : Fonction de sauvegarde horodatée d'un dossier complet
#                 avec conservation de la structure
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import shutil
from datetime import datetime

def backup_fichiers(dossier_source, dossier_backup):
    """Crée une sauvegarde horodatée d'un dossier"""
    source = Path(dossier_source)
    backup = Path(dossier_backup)

    if not source.exists():
        print(f"{source} n'existe pas")
        return

    # Créer un nom avec timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dossier_destination = backup / f"backup_{timestamp}"

    # Créer le dossier de backup
    dossier_destination.mkdir(parents=True, exist_ok=True)

    print(f"Backup en cours...")
    print(f"Source : {source}")
    print(f"Destination : {dossier_destination}\n")

    compteur = 0
    for fichier in source.rglob('*'):
        if fichier.is_file():
            chemin_relatif = fichier.relative_to(source)
            destination = dossier_destination / chemin_relatif

            destination.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(fichier, destination)
            compteur += 1
            print(f"  [ok] {chemin_relatif}")

    print(f"\nBackup terminé : {compteur} fichiers copiés")
    print(f"Dossier : {dossier_destination}")

# --- Créer un dossier source de test ---
Path('projets/mon_app/src').mkdir(parents=True, exist_ok=True)
Path('projets/mon_app/src/main.py').write_text("# main", encoding='utf-8')
Path('projets/mon_app/src/utils.py').write_text("# utils", encoding='utf-8')
Path('projets/mon_app/README.md').write_text("# Mon App", encoding='utf-8')

# --- Exécuter le backup ---
backup_fichiers('projets/mon_app', 'backups')

# Nettoyage
shutil.rmtree('projets')
shutil.rmtree('backups')
