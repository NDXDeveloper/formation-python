# ============================================================================
#   Section 7.1 : Les modules os, sys et subprocess
#   Description : Exemple complet combinant os, sys et subprocess -
#                 analyseur de projet Python avec statistiques
#   Fichier source : 01-os-sys-subprocess.md
# ============================================================================

import os
import sys
import subprocess
import shutil
from pathlib import Path

def analyser_projet(repertoire):
    """Analyse un projet Python et affiche des statistiques"""

    # Vérifier que le répertoire existe
    if not os.path.isdir(repertoire):
        print(f"Erreur : {repertoire} n'est pas un répertoire valide")
        return

    print(f"Analyse du projet : {os.path.abspath(repertoire)}")
    print("=" * 60)

    # Compter les fichiers Python
    fichiers_py = []
    total_lignes = 0

    for racine, _, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.endswith(".py"):
                chemin_complet = os.path.join(racine, fichier)
                fichiers_py.append(chemin_complet)

                # Compter les lignes
                try:
                    with open(chemin_complet, "r", encoding="utf-8") as f:
                        nb_lignes = len(f.readlines())
                        total_lignes += nb_lignes
                except Exception:
                    pass

    print(f"Fichiers Python trouvés : {len(fichiers_py)}")
    print(f"Total de lignes de code : {total_lignes}")

    # Taille totale du projet
    taille_totale = 0
    nb_fichiers_total = 0
    for racine, _, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            chemin = os.path.join(racine, fichier)
            try:
                taille_totale += os.path.getsize(chemin)
                nb_fichiers_total += 1
            except OSError:
                pass

    print(f"Fichiers totaux : {nb_fichiers_total}")
    print(f"Taille totale : {taille_totale / 1024:.2f} Ko")

    # Vérifier si Git est présent
    try:
        resultat = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=repertoire,
            capture_output=True,
            text=True,
            check=True
        )
        print("Depot Git detecte")

        resultat = subprocess.run(
            ["git", "log", "-1", "--oneline"],
            cwd=repertoire,
            capture_output=True,
            text=True
        )
        if resultat.returncode == 0:
            print(f"Dernier commit : {resultat.stdout.strip()}")

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Pas de depot Git")

    # Informations système
    print(f"\nEnvironnement :")
    print(f"  Python : {sys.version.split()[0]}")
    print(f"  Plateforme : {sys.platform}")
    print(f"  Répertoire de travail : {os.getcwd()}")


# --- Créer un mini-projet de test ---
print("=== Création d'un mini-projet de test ===\n")

projet = Path("_temp_mini_projet")
(projet / "src").mkdir(parents=True, exist_ok=True)
(projet / "tests").mkdir(exist_ok=True)

(projet / "src" / "main.py").write_text(
    "def main():\n    print('Hello World')\n\nif __name__ == '__main__':\n    main()\n",
    encoding="utf-8"
)
(projet / "src" / "utils.py").write_text(
    "def formater(nom):\n    return nom.title()\n\ndef valider(email):\n    return '@' in email\n",
    encoding="utf-8"
)
(projet / "tests" / "test_main.py").write_text(
    "from src.main import main\n\ndef test_main():\n    assert True\n",
    encoding="utf-8"
)
(projet / "README.md").write_text(
    "# Mini Projet\n\nUn projet de test.\n",
    encoding="utf-8"
)

# Analyser le mini-projet
analyser_projet(str(projet))

# Nettoyage
shutil.rmtree(projet)
print("\nNettoyage : _temp_mini_projet supprimé")
