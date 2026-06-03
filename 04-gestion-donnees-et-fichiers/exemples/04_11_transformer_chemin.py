# ============================================================================
#   Section 4.4 : Transformer un chemin (with_suffix, with_name, with_stem)
#   Description : Dériver un nouveau Path en changeant l'extension, le nom
#                 complet ou le nom sans extension (sans modifier l'original)
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

fichier = Path('rapports/donnees.csv')

# --- with_suffix : changer l'extension ---
print("=== with_suffix / with_name / with_stem ===")
print(f"Original          : {fichier}")
print(f"with_suffix('.json') : {fichier.with_suffix('.json')}")   # rapports/donnees.json

# --- with_name : changer le nom complet (nom + extension) ---
print(f"with_name('resume.txt') : {fichier.with_name('resume.txt')}")  # rapports/resume.txt

# --- with_stem : changer le nom sans toucher à l'extension (Python 3.9+) ---
print(f"with_stem('donnees_2024') : {fichier.with_stem('donnees_2024')}")  # rapports/donnees_2024.csv

# L'objet d'origine n'est pas modifié
print(f"Original inchangé : {fichier}")

# --- Cas d'usage : fichier de sauvegarde dérivé ---
print("\n=== Cas d'usage : sauvegarde ===")
source = Path('document.txt')
sauvegarde = source.with_suffix('.bak')
print(f"{source} -> {sauvegarde}")   # document.txt -> document.bak
