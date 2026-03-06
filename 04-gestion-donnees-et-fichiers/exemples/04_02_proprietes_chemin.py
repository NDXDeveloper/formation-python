# ============================================================================
#   Section 4.4 : Propriétés des chemins
#   Description : name, stem, suffix, suffixes, parent, parents, parts
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

# --- Propriétés de base ---
print("=== Propriétés d'un chemin ===")

chemin = Path('/home/alice/documents/projet/code/script.py')

print(f"Nom complet : {chemin.name}")         # script.py
print(f"Nom sans extension : {chemin.stem}")   # script
print(f"Extension : {chemin.suffix}")          # .py

# Toutes les extensions (pour .tar.gz par exemple)
chemin2 = Path('archive.tar.gz')
print(f"Extensions : {chemin2.suffixes}")      # ['.tar', '.gz']

# Répertoire parent
print(f"Parent : {chemin.parent}")
# /home/alice/documents/projet/code

# Parties du chemin
print(f"Parties : {chemin.parts}")
# ('/', 'home', 'alice', 'documents', 'projet', 'code', 'script.py')

# --- Exemple avec un fichier image ---
print("\n=== Exemple fichier image ===")

fichier = Path('documents/photos/vacances/plage.jpg')

print(f"Chemin complet : {fichier}")
print(f"Nom du fichier : {fichier.name}")
print(f"Nom sans extension : {fichier.stem}")
print(f"Extension : {fichier.suffix}")
print(f"Dossier parent : {fichier.parent}")
print(f"Grand-parent : {fichier.parent.parent}")
