# ============================================================================
#   Section 6.4 : Environnements virtuels (venv)
#   Description : Créer un venv programmatiquement, inspecter sa structure,
#                 lire pyvenv.cfg, vérifier l'isolation
#   Fichier source : 04-environnements-virtuels.md
# ============================================================================

import venv
import sys
import shutil
from pathlib import Path

# --- Créer un environnement virtuel ---
print("=== Création d'un environnement virtuel ===")

venv_dir = Path('_temp_venv')
venv.create(str(venv_dir), with_pip=False)  # Sans pip pour plus de rapidité
print(f"Environnement créé dans : {venv_dir.resolve()}")

# --- Inspecter la structure ---
print("\n=== Structure du venv ===")

for item in sorted(venv_dir.rglob('*')):
    relative = item.relative_to(venv_dir)
    profondeur = len(relative.parts) - 1
    prefixe = "  " * profondeur
    if item.is_dir():
        print(f"{prefixe}{item.name}/")
    else:
        print(f"{prefixe}{item.name}")

# --- Lire pyvenv.cfg ---
print("\n=== Contenu de pyvenv.cfg ===")

cfg_file = venv_dir / 'pyvenv.cfg'
if cfg_file.exists():
    contenu = cfg_file.read_text(encoding='utf-8')
    for ligne in contenu.strip().split('\n'):
        print(f"  {ligne}")

# --- Vérifier les exécutables ---
print("\n=== Exécutables disponibles ===")

# Sur Linux/macOS c'est bin/, sur Windows c'est Scripts/
bin_dir = venv_dir / 'bin'
if not bin_dir.exists():
    bin_dir = venv_dir / 'Scripts'

if bin_dir.exists():
    executables = sorted(bin_dir.iterdir())
    for exe in executables:
        print(f"  {exe.name}")

# --- Vérifier l'interpréteur Python du venv ---
print("\n=== Python du venv vs Python système ===")

python_venv = bin_dir / 'python'
if not python_venv.exists():
    python_venv = bin_dir / 'python.exe'

if python_venv.exists():
    print(f"Python venv   : {python_venv.resolve()}")
print(f"Python système : {sys.executable}")

# --- Vérifier l'isolation (site-packages) ---
print("\n=== Répertoire site-packages ===")

lib_dir = venv_dir / 'lib'
if lib_dir.exists():
    site_packages = list(lib_dir.rglob('site-packages'))
    for sp in site_packages:
        contenu_sp = list(sp.iterdir())
        print(f"Emplacement : {sp.relative_to(venv_dir)}")
        print(f"Nombre d'éléments : {len(contenu_sp)}")
        for item in sorted(contenu_sp)[:5]:
            print(f"  {item.name}")
        if len(contenu_sp) > 5:
            print(f"  ... ({len(contenu_sp)} éléments au total)")

# --- Avantages des venv ---
print("\n=== Pourquoi utiliser des venv ? ===")

avantages = [
    "Isolation des dépendances par projet",
    "Reproductibilité (requirements.txt / poetry.lock)",
    "Pas de droits admin nécessaires",
    "Facile à recréer si corrompu",
    "Un venv par projet = pas de conflits",
]
for i, avantage in enumerate(avantages, 1):
    print(f"  {i}. {avantage}")

# Nettoyage
shutil.rmtree(venv_dir)
print(f"\nNettoyage : {venv_dir} supprimé")
