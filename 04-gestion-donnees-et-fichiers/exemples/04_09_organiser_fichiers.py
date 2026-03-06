# ============================================================================
#   Section 4.4 : Exemple pratique - Organiser des fichiers par extension
#   Description : Fonction qui organise automatiquement les fichiers d'un
#                 dossier dans des sous-dossiers par extension
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import shutil

def organiser_fichiers(dossier_source):
    """Organise les fichiers par extension dans des sous-dossiers"""
    source = Path(dossier_source)

    if not source.exists():
        print(f"Le dossier {source} n'existe pas")
        return

    print(f"Organisation des fichiers dans {source}\n")

    for fichier in sorted(source.iterdir()):
        # Ignorer les dossiers
        if not fichier.is_file():
            continue

        # Obtenir l'extension (sans le point)
        extension = fichier.suffix[1:] if fichier.suffix else 'sans_extension'

        # Créer le dossier pour cette extension
        dossier_extension = source / extension
        dossier_extension.mkdir(exist_ok=True)

        # Déplacer le fichier
        destination = dossier_extension / fichier.name

        # Si le fichier existe déjà, ajouter un numéro
        compteur = 1
        while destination.exists():
            nouveau_nom = f"{fichier.stem}_{compteur}{fichier.suffix}"
            destination = dossier_extension / nouveau_nom
            compteur += 1

        shutil.move(fichier, destination)
        print(f"  {fichier.name} -> {extension}/{destination.name}")

    print("\nOrganisation terminée !")

# --- Créer un dossier de test ---
Path('telechargements').mkdir(exist_ok=True)
Path('telechargements/photo1.jpg').write_text("img1", encoding='utf-8')
Path('telechargements/photo2.jpg').write_text("img2", encoding='utf-8')
Path('telechargements/rapport.pdf').write_text("pdf", encoding='utf-8')
Path('telechargements/script.py').write_text("py", encoding='utf-8')
Path('telechargements/notes.txt').write_text("txt", encoding='utf-8')
Path('telechargements/data.csv').write_text("csv", encoding='utf-8')

# --- Organiser ---
organiser_fichiers('telechargements')

# --- Vérification ---
print("\n=== Structure après organisation ===")
for element in sorted(Path('telechargements').rglob('*')):
    if element.is_file():
        print(f"  {element.relative_to('telechargements')}")

# Nettoyage
shutil.rmtree('telechargements')
