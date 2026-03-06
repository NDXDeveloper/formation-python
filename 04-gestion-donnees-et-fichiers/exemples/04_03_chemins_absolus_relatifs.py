# ============================================================================
#   Section 4.4 : Chemins absolus et relatifs
#   Description : absolute(), resolve(), relative_to(), home(), cwd()
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

# --- Chemin absolu ---
print("=== Chemin absolu ===")

chemin_relatif = Path('mon_fichier.txt')
chemin_absolu = chemin_relatif.absolute()

print(f"Relatif : {chemin_relatif}")
print(f"Absolu : {chemin_absolu}")

# --- resolve() ---
print("\n=== resolve() ===")

chemin = Path('.')
chemin_resolu = chemin.resolve()
print(f"Répertoire courant : {chemin_resolu}")

# --- relative_to() ---
print("\n=== relative_to() ===")

chemin1 = Path('/home/alice/projets/python/app')
chemin2 = Path('/home/alice/projets/data/fichier.csv')

relatif = chemin2.relative_to(Path('/home/alice/projets'))
print(relatif)  # data/fichier.csv

# --- Chemins spéciaux ---
print("\n=== Chemins spéciaux ===")

home = Path.home()
print(f"Home : {home}")

cwd = Path.cwd()
print(f"Répertoire courant : {cwd}")

# Chemin portable
chemin = Path.home() / 'documents' / 'fichier.txt'
print(f"Chemin portable : {chemin}")

# --- Conversion Path <-> str ---
print("\n=== Conversion ===")

chemin = Path('dossier/fichier.txt')
chemin_str = str(chemin)
print(f"String : {chemin_str}")
print(f"Type : {type(chemin_str)}")
