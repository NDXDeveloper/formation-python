# ============================================================================
#   Section 6.1 : Imports circulaires (le piège et sa résolution)
#   Description : Deux modules qui s'importent mutuellement au niveau top-level
#                 lèvent ImportError ; l'import LOCAL (dans la fonction) résout.
#   Fichier source : 01-importation-et-creation-modules.md
# ============================================================================

import sys
import os
import tempfile
import shutil

# On fabrique deux modules temporaires pour la démonstration.
dossier = tempfile.mkdtemp()
sys.path.insert(0, dossier)


def ecrire(nom, contenu):
    with open(os.path.join(dossier, nom), "w", encoding="utf-8") as f:
        f.write(contenu)


# --- Version CASSÉE : chaque module importe l'autre au chargement ---
print("=== Version cassée : import circulaire ===")
ecrire("module_a.py", "from module_b import fonction_b\n\ndef fonction_a():\n    return 'A'\n")
ecrire("module_b.py", "from module_a import fonction_a\n\ndef fonction_b():\n    return 'B'\n")
try:
    import module_a
except ImportError as e:
    # Le message complet est : cannot import name 'fonction_a' from
    # partially initialized module 'module_a' (most likely due to a circular import)
    print("Échec à l'import :", str(e).split(" (")[0])

# Vider le cache des imports partiels avant de réessayer
sys.modules.pop("module_a", None)
sys.modules.pop("module_b", None)

# --- Version CORRIGÉE : module_b importe localement (dans la fonction) ---
print("\n=== Version corrigée : import local dans module_b ===")
ecrire("module_b.py", "def fonction_b():\n    from module_a import fonction_a\n    return fonction_a()\n")
import module_a
print("Import réussi, fonction_a() =", module_a.fonction_a())

# Nettoyage
sys.modules.pop("module_a", None)
sys.modules.pop("module_b", None)
sys.path.remove(dossier)
shutil.rmtree(dossier)
