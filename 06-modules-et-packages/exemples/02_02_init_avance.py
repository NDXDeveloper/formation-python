# ============================================================================
#   Section 6.2 : Le rôle du fichier __init__.py
#   Description : Simplifier les imports via __init__.py, __version__,
#                 __all__ pour contrôler les exports
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- Créer le package avec __init__.py avancé ---
base = Path('_temp_pkg2')
pkg = base / 'mathematiques'
pkg.mkdir(parents=True, exist_ok=True)

# operations.py
(pkg / 'operations.py').write_text('''\
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
''', encoding='utf-8')

# geometrie.py
(pkg / 'geometrie.py').write_text('''\
PI = 3.14159

def aire_cercle(rayon):
    return PI * rayon ** 2

def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

def perimetre_rectangle(largeur, hauteur):
    return 2 * (largeur + hauteur)
''', encoding='utf-8')

# __init__.py avec imports simplifiés
(pkg / '__init__.py').write_text('''\
"""Package de fonctions mathématiques."""

from .operations import addition, soustraction, multiplication, division
from .geometrie import aire_cercle, aire_rectangle, perimetre_rectangle

__version__ = "1.0.0"

__all__ = [
    'addition', 'soustraction', 'multiplication', 'division',
    'aire_cercle', 'aire_rectangle', 'perimetre_rectangle'
]
''', encoding='utf-8')

sys.path.insert(0, str(base))

# --- Imports simplifiés grâce à __init__.py ---
print("=== Imports simplifiés ===")

from mathematiques import addition, multiplication

print(f"10 + 5 = {addition(10, 5)}")
print(f"6 x 7 = {multiplication(6, 7)}")

# --- Accès à __version__ ---
print("\n=== Version du package ===")

import mathematiques
print(f"Version : {mathematiques.__version__}")

# --- __all__ ---
print("\n=== __all__ ===")
print(f"Exports : {mathematiques.__all__}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
