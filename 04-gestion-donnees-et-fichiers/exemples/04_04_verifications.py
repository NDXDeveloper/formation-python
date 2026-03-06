# ============================================================================
#   Section 4.4 : Vérifications et tests sur les chemins
#   Description : exists(), is_file(), is_dir(), is_absolute(),
#                 fonction d'analyse complète
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path
import os

# Créer des éléments de test
Path('test_fichier.txt').write_text("contenu de test", encoding='utf-8')
Path('test_dossier').mkdir(exist_ok=True)

# --- Vérifications de base ---
print("=== Vérifications ===")

chemin_fichier = Path('test_fichier.txt')
chemin_dossier = Path('test_dossier')
chemin_inexistant = Path('inexistant.xyz')

print(f"{chemin_fichier} existe : {chemin_fichier.exists()}")
print(f"{chemin_fichier} est un fichier : {chemin_fichier.is_file()}")
print(f"{chemin_fichier} est un dossier : {chemin_fichier.is_dir()}")
print(f"{chemin_fichier} est absolu : {chemin_fichier.is_absolute()}")

print()
print(f"{chemin_dossier} existe : {chemin_dossier.exists()}")
print(f"{chemin_dossier} est un fichier : {chemin_dossier.is_file()}")
print(f"{chemin_dossier} est un dossier : {chemin_dossier.is_dir()}")

print()
print(f"{chemin_inexistant} existe : {chemin_inexistant.exists()}")

# --- Fonction d'analyse ---
print("\n=== Analyse complète ===")

def analyser_chemin(chemin_str):
    chemin = Path(chemin_str)

    print(f"\n{'='*50}")
    print(f"Analyse de : {chemin}")
    print(f"{'='*50}")

    if not chemin.exists():
        print("Le chemin n'existe pas")
        return

    print("Le chemin existe")

    if chemin.is_file():
        print(f"Type : Fichier")
        taille = chemin.stat().st_size
        print(f"Taille : {taille} octets")
    elif chemin.is_dir():
        print(f"Type : Dossier")
        nb_fichiers = len(list(chemin.iterdir()))
        print(f"Nombre d'éléments : {nb_fichiers}")

analyser_chemin('test_fichier.txt')
analyser_chemin('test_dossier')
analyser_chemin('inexistant.xyz')

# Nettoyage
os.remove('test_fichier.txt')
os.rmdir('test_dossier')
