# ============================================================================
#   Section 6.2 : __main__.py et __all__
#   Description : Rendre un package exécutable avec __main__.py,
#                 contrôler les exports avec __all__
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import subprocess
import shutil

# --- Créer un package avec __main__.py ---
print("=== __main__.py ===")

base = Path('_temp_pkg4')
pkg = base / 'calculatrice'
pkg.mkdir(parents=True, exist_ok=True)

(pkg / '__init__.py').write_text('', encoding='utf-8')

(pkg / 'operations.py').write_text('''\
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
''', encoding='utf-8')

(pkg / '__main__.py').write_text('''\
"""Point d'entrée du package calculatrice."""
from .operations import addition, soustraction

def main():
    print("=== Calculatrice ===")
    a, b = 15, 7
    print(f"{a} + {b} = {addition(a, b)}")
    print(f"{a} - {b} = {soustraction(a, b)}")

if __name__ == "__main__":
    main()
''', encoding='utf-8')

# Exécuter avec python -m calculatrice
result = subprocess.run(
    [sys.executable, '-m', 'calculatrice'],
    capture_output=True, text=True, cwd=str(base)
)
print("Exécution avec python -m calculatrice :")
print(result.stdout.strip())

# --- __all__ pour contrôler les exports ---
print("\n=== __all__ ===")

pkg2 = base / 'monmodule'
pkg2.mkdir(parents=True, exist_ok=True)

(pkg2 / '__init__.py').write_text('''\
def fonction_publique():
    return "publique"

def _fonction_privee():
    return "privee"

CONSTANTE = 42

__all__ = ['fonction_publique', 'CONSTANTE']
''', encoding='utf-8')

sys.path.insert(0, str(base))

import monmodule

# Les éléments dans __all__
print(f"fonction_publique() : {monmodule.fonction_publique()}")
print(f"CONSTANTE : {monmodule.CONSTANTE}")

# _fonction_privee est accessible mais pas dans __all__
print(f"_fonction_privee() : {monmodule._fonction_privee()}")
print(f"__all__ : {monmodule.__all__}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
