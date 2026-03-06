# ============================================================================
#   Section 4.4 : Lecture et écriture simplifiées avec pathlib
#   Description : read_text(), write_text(), read_bytes(), write_bytes(),
#                 traitement de fichiers texte
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import shutil
import os

# --- Écrire et lire du texte ---
print("=== write_text / read_text ===")

fichier = Path('nouveau_fichier.txt')
fichier.write_text("Bonjour depuis pathlib !\n", encoding='utf-8')

contenu = fichier.read_text(encoding='utf-8')
print(contenu)

# --- Écrire et lire des données binaires ---
print("=== write_bytes / read_bytes ===")

fichier_bin = Path('donnees.bin')
donnees = bytes([0, 1, 2, 3, 4])
fichier_bin.write_bytes(donnees)

contenu_bin = fichier_bin.read_bytes()
print(f"Taille : {len(contenu_bin)} octets")
print(f"Contenu : {list(contenu_bin)}")

# --- Traiter des fichiers texte ---
print("\n=== Traiter des fichiers .txt ===")

# Créer un dossier avec des fichiers de test
Path('documents').mkdir(exist_ok=True)
Path('documents/rapport.txt').write_text(
    "Python est génial\nIl est simple et puissant\nTroisième ligne\n",
    encoding='utf-8'
)
Path('documents/notes.txt').write_text(
    "Note 1\nNote 2\n",
    encoding='utf-8'
)

def traiter_fichiers_texte(dossier_str):
    """Compte les lignes et mots dans tous les fichiers .txt"""
    dossier = Path(dossier_str)

    for fichier in sorted(dossier.glob('*.txt')):
        contenu = fichier.read_text(encoding='utf-8')
        nb_lignes = len(contenu.splitlines())
        nb_mots = len(contenu.split())

        print(f"{fichier.name}")
        print(f"   Lignes : {nb_lignes}")
        print(f"   Mots : {nb_mots}\n")

traiter_fichiers_texte('documents')

# Nettoyage
os.remove('nouveau_fichier.txt')
os.remove('donnees.bin')
shutil.rmtree('documents')
