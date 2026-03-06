# ============================================================================
#   Section 4.4 : Recherche de fichiers avec glob et rglob
#   Description : glob() pour patterns, rglob() pour recherche récursive,
#                 iterdir() pour lister le contenu
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import shutil

# Créer une structure de test
Path('test_glob').mkdir(exist_ok=True)
Path('test_glob/script1.py').write_text("# script 1", encoding='utf-8')
Path('test_glob/script2.py').write_text("# script 2", encoding='utf-8')
Path('test_glob/notes.txt').write_text("notes", encoding='utf-8')
Path('test_glob/readme.md').write_text("# readme", encoding='utf-8')
Path('test_glob/sous_dossier').mkdir(exist_ok=True)
Path('test_glob/sous_dossier/utils.py').write_text("# utils", encoding='utf-8')
Path('test_glob/sous_dossier/data.txt').write_text("data", encoding='utf-8')

dossier = Path('test_glob')

# --- iterdir() ---
print("=== Contenu du dossier ===")
for element in sorted(dossier.iterdir()):
    type_element = "[D]" if element.is_dir() else "[F]"
    print(f"  {type_element} {element.name}")

# --- glob() ---
print("\n=== glob('*.py') ===")
for fichier in sorted(dossier.glob('*.py')):
    print(f"  {fichier.name}")

print("\n=== glob('*.txt') ===")
for fichier in sorted(dossier.glob('*.txt')):
    print(f"  {fichier.name}")

# --- rglob() récursif ---
print("\n=== rglob('*.py') - récursif ===")
for fichier in sorted(dossier.rglob('*.py')):
    print(f"  {fichier}")

print("\n=== rglob('*.txt') - récursif ===")
for fichier in sorted(dossier.rglob('*.txt')):
    print(f"  {fichier}")

# --- Filtrer par extension multiple ---
print("\n=== Extensions multiples (.txt, .md) ===")
for fichier in sorted(dossier.rglob('*')):
    if fichier.is_file() and fichier.suffix in ('.txt', '.md'):
        print(f"  {fichier}")

# --- Statistiques ---
print("\n=== Statistiques ===")
scripts = list(dossier.rglob('*.py'))
print(f"{len(scripts)} scripts Python trouvés")
for script in sorted(scripts):
    taille = script.stat().st_size
    print(f"  {script} ({taille} octets)")

# Nettoyage
shutil.rmtree('test_glob')
