# ============================================================================
#   Section 4.1 : Vérifier l'existence d'un fichier
#   Description : Utiliser pathlib.Path pour vérifier exists(), is_file(),
#                 et obtenir la taille
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os
from pathlib import Path

# Créer un fichier de test
with open('mon_document.txt', 'w', encoding='utf-8') as f:
    f.write("Contenu de test\n")

chemin = Path('mon_document.txt')

if chemin.exists():
    print("Le fichier existe")

    if chemin.is_file():
        print("C'est bien un fichier (pas un dossier)")

    print(f"Taille : {chemin.stat().st_size} octets")
else:
    print("Le fichier n'existe pas")

# Tester avec un fichier inexistant
print()
chemin2 = Path('inexistant.txt')
if chemin2.exists():
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")

# Nettoyage
os.remove('mon_document.txt')
