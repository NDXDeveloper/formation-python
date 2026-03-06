# ============================================================================
#   Section 4.4 : Créer des objets Path et construire des chemins
#   Description : Création de Path, opérateur /, joinpath(), construction
#                 progressive
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

# --- Créer un objet Path ---
print("=== Création de Path ===")

chemin1 = Path('mon_fichier.txt')
repertoire_actuel = Path('.')
repertoire_parent = Path('..')

print(chemin1)
print(type(chemin1))

# --- Opérateur / ---
print("\n=== Opérateur / ===")

base = Path('mes_documents')
sous_dossier = base / 'projets'
fichier = sous_dossier / 'python' / 'script.py'

print(fichier)
# mes_documents/projets/python/script.py

# --- joinpath() ---
print("\n=== joinpath() ===")

chemin = Path('dossier').joinpath('sous_dossier', 'fichier.txt')
print(chemin)
# dossier/sous_dossier/fichier.txt

# --- Construction à partir de variables ---
print("\n=== Construction avec variables ===")

projet = Path('projets')
python = 'python'
app = 'mon_app'
fichier = 'main.py'

chemin_complet = projet / python / app / fichier
print(chemin_complet)
# projets/python/mon_app/main.py
