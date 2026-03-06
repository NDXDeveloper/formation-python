# ============================================================================
#   Section 4.4 : Opérations sur fichiers et dossiers
#   Description : mkdir(), unlink(), rmdir(), rename(), shutil.copy(),
#                 shutil.rmtree()
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import shutil

# --- Créer un dossier ---
print("=== Créer des dossiers ===")

nouveau_dossier = Path('mon_nouveau_dossier')
nouveau_dossier.mkdir(exist_ok=True)
print(f"Dossier créé : {nouveau_dossier}")

chemin = Path('projets/python/mon_app/src')
chemin.mkdir(parents=True, exist_ok=True)
print(f"Hiérarchie créée : {chemin}")

# --- Créer des fichiers de test ---
Path('ancien_nom.txt').write_text("contenu original", encoding='utf-8')
Path('fichier_a_copier.txt').write_text("contenu à copier", encoding='utf-8')

# --- Renommer un fichier ---
print("\n=== Renommer ===")

ancien = Path('ancien_nom.txt')
nouveau = Path('nouveau_nom.txt')

if ancien.exists():
    ancien.rename(nouveau)
    print(f"Renommé : {ancien} -> {nouveau}")

# --- Copier un fichier ---
print("\n=== Copier ===")

source = Path('fichier_a_copier.txt')
destination = Path('copie_du_fichier.txt')

if source.exists():
    shutil.copy(source, destination)
    print(f"Fichier copié : {source} -> {destination}")

# --- Supprimer un fichier ---
print("\n=== Supprimer ===")

for f in [nouveau, source, destination]:
    if f.exists():
        f.unlink()
        print(f"Fichier supprimé : {f}")

# --- Supprimer des dossiers ---
nouveau_dossier.rmdir()  # Dossier vide
print(f"Dossier vide supprimé : {nouveau_dossier}")

shutil.rmtree('projets')  # Dossier non vide
print(f"Dossier avec contenu supprimé : projets/")
