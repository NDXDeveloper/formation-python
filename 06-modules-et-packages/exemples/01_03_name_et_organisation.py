# ============================================================================
#   Section 6.1 : L'attribut __name__ et organisation des modules
#   Description : __name__ == "__main__", structure recommandée d'un module,
#                 docstrings de module, sys.path
#   Fichier source : 01-importation-et-creation-modules.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- __name__ == "__main__" ---
print("=== __name__ ===")

dossier_temp = Path('_temp_modules2')
dossier_temp.mkdir(exist_ok=True)

# Créer un module calculs.py avec if __name__ == "__main__"
(dossier_temp / 'calculs.py').write_text('''\
def carre(x):
    """Retourne le carré d'un nombre."""
    return x ** 2

def cube(x):
    """Retourne le cube d'un nombre."""
    return x ** 3

if __name__ == "__main__":
    print("Test du module calculs")
    print(f"Carré de 5 : {carre(5)}")
    print(f"Cube de 3 : {cube(3)}")
''', encoding='utf-8')

# Exécuter directement le module
import subprocess
result = subprocess.run(
    [sys.executable, str(dossier_temp / 'calculs.py')],
    capture_output=True, text=True
)
print("Exécution directe :")
print(result.stdout.strip())

# Importer le module (les tests ne s'affichent pas)
sys.path.insert(0, str(dossier_temp))
import calculs

print("\nImportation :")
resultat = calculs.carre(10)
print(f"Carré de 10 : {resultat}")  # 100

# --- Structure recommandée ---
print("\n=== Module bien structuré ===")

(dossier_temp / 'utilitaires.py').write_text('''\
"""
Module utilitaires.

Ce module contient diverses fonctions utilitaires pour
le traitement de texte et les conversions de données.
"""

VERSION = "1.0.0"

def nettoyer_texte(texte):
    """Supprime les espaces en début et fin de chaîne."""
    return texte.strip()

def convertir_majuscules(texte):
    """Convertit tout le texte en majuscules."""
    return texte.upper()

def compter_mots(texte):
    """Compte le nombre de mots dans le texte."""
    return len(texte.split())

if __name__ == "__main__":
    print("Test du module utilitaires")
    print(nettoyer_texte("  Bonjour  "))
    print(convertir_majuscules("python"))
    print(compter_mots("Python est génial"))
''', encoding='utf-8')

import utilitaires

print(f"Version : {utilitaires.VERSION}")
print(f"Nettoyé : '{utilitaires.nettoyer_texte('  Bonjour  ')}'")
print(f"Majuscules : {utilitaires.convertir_majuscules('python')}")
print(f"Mots : {utilitaires.compter_mots('Python est génial')}")

# --- sys.path ---
print("\n=== sys.path (premiers chemins) ===")

for chemin in sys.path[:3]:
    print(f"  {chemin}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(dossier_temp)
