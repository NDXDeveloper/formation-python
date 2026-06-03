# ============================================================================
#   Section 6.2 : Création d'un package simple
#   Description : Créer un package mathematiques avec operations.py et
#                 geometrie.py, différentes méthodes d'importation
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- Créer la structure du package ---
base = Path('_temp_pkg')
pkg = base / 'mathematiques'
pkg.mkdir(parents=True, exist_ok=True)

# __init__.py vide
(pkg / '__init__.py').write_text('', encoding='utf-8')

# operations.py
(pkg / 'operations.py').write_text('''\
"""Module contenant des opérations mathématiques de base."""

def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait b de a."""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres."""
    return a * b

def division(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
''', encoding='utf-8')

# geometrie.py
(pkg / 'geometrie.py').write_text('''\
"""Module contenant des fonctions de géométrie."""

PI = 3.14159

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle."""
    return PI * rayon ** 2

def aire_rectangle(largeur, hauteur):
    """Calcule l'aire d'un rectangle."""
    return largeur * hauteur

def perimetre_rectangle(largeur, hauteur):
    """Calcule le périmètre d'un rectangle."""
    return 2 * (largeur + hauteur)
''', encoding='utf-8')

# Ajouter au path
sys.path.insert(0, str(base))

# --- Méthode 1 : import complet ---
print("=== Import complet ===")

import mathematiques.operations
import mathematiques.geometrie

resultat1 = mathematiques.operations.addition(10, 5)
print(f"10 + 5 = {resultat1}")

aire = mathematiques.geometrie.aire_cercle(7)
print(f"Aire du cercle : {aire}")

# --- Méthode 2 : import avec alias ---
print("\n=== Import avec alias ===")

import mathematiques.operations as ops

resultat2 = ops.multiplication(6, 7)
print(f"6 x 7 = {resultat2}")

# --- Méthode 3 : import de fonctions spécifiques ---
print("\n=== Import spécifique ===")

from mathematiques.geometrie import aire_rectangle

aire_rect = aire_rectangle(5, 3)
print(f"Aire du rectangle : {aire_rect}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
