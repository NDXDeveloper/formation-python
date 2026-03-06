# ============================================================================
#   Section 6.3 : Gestion des dépendances avec pip
#   Description : Vérifier pip, lister packages, pip show, pip freeze,
#                 créer et lire un requirements.txt
#   Fichier source : 03-gestion-dependances-pip.md
# ============================================================================

import subprocess
import sys
from pathlib import Path

# --- Vérifier pip ---
print("=== Version de pip ===")

result = subprocess.run(
    [sys.executable, '-m', 'pip', '--version'],
    capture_output=True, text=True
)
print(result.stdout.strip())

# --- Lister quelques packages installés ---
print("\n=== Packages installés (5 premiers) ===")

result = subprocess.run(
    [sys.executable, '-m', 'pip', 'list', '--format=columns'],
    capture_output=True, text=True
)
lignes = result.stdout.strip().split('\n')
for ligne in lignes[:7]:  # En-tête + 5 premiers
    print(ligne)
print("...")

# --- pip show sur un module standard ---
print("\n=== pip show pip ===")

result = subprocess.run(
    [sys.executable, '-m', 'pip', 'show', 'pip'],
    capture_output=True, text=True
)
for ligne in result.stdout.strip().split('\n')[:5]:
    print(ligne)

# --- pip freeze ---
print("\n=== pip freeze (5 premiers) ===")

result = subprocess.run(
    [sys.executable, '-m', 'pip', 'freeze'],
    capture_output=True, text=True
)
lignes = result.stdout.strip().split('\n')
for ligne in lignes[:5]:
    if ligne:
        print(ligne)
if len(lignes) > 5:
    print(f"... ({len(lignes)} packages au total)")

# --- Créer un requirements.txt de démonstration ---
print("\n=== Création d'un requirements.txt ===")

contenu_requirements = """\
# Requêtes HTTP
requests==2.31.0

# Analyse de données
pandas>=1.5.0
numpy>=1.24.0,<2.0.0

# Visualisation
matplotlib==3.7.2
"""

fichier = Path('_demo_requirements.txt')
fichier.write_text(contenu_requirements, encoding='utf-8')
print("Contenu du fichier :")
print(fichier.read_text(encoding='utf-8'))

# Nettoyage
fichier.unlink()
