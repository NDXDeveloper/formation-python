# ============================================================================
#   Section 7.1 : Les modules os, sys et subprocess
#   Description : Module subprocess - exécuter des commandes, capture_output,
#                 gestion d'erreurs, stdin, commandes shell
#   Fichier source : 01-os-sys-subprocess.md
# ============================================================================

import subprocess
import sys
import os

# --- Exécuter une commande simple ---
print("=== subprocess.run() - commande simple ===")

resultat = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# Afficher seulement les premières lignes
lignes = resultat.stdout.strip().split("\n")
for ligne in lignes[:3]:
    print(f"  {ligne}")
if len(lignes) > 3:
    print(f"  ... ({len(lignes)} lignes au total)")

print(f"Code de retour : {resultat.returncode}")

# --- Commande avec check=True ---
print("\n=== echo avec check=True ===")

resultat = subprocess.run(
    ["echo", "Bonjour"],
    capture_output=True,
    text=True,
    check=True
)
print(f"Sortie : {resultat.stdout.strip()}")

# --- Gérer les erreurs ---
print("\n=== Gestion des erreurs ===")

# Commande inexistante
try:
    resultat = subprocess.run(
        ["commande_inexistante"],
        capture_output=True,
        text=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"CalledProcessError : code {e.returncode}")
except FileNotFoundError:
    print("FileNotFoundError : la commande n'a pas été trouvée")

# Commande qui échoue
try:
    resultat = subprocess.run(
        ["ls", "/repertoire_inexistant_xyz"],
        capture_output=True,
        text=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"CalledProcessError : code {e.returncode}")
    print(f"  stderr : {e.stderr.strip()[:60]}...")

# --- Obtenir des informations système ---
print("\n=== Informations système ===")

def obtenir_info_python():
    """Obtient la version de Python via subprocess"""
    resultat = subprocess.run(
        [sys.executable, "--version"],
        capture_output=True,
        text=True
    )
    return resultat.stdout.strip()

def lister_fichiers_python(repertoire="."):
    """Liste tous les fichiers Python dans un répertoire"""
    resultat = subprocess.run(
        "ls *.py 2>/dev/null",
        shell=True,
        capture_output=True,
        text=True,
        cwd=repertoire
    )
    if resultat.returncode == 0:
        fichiers = resultat.stdout.strip().split("\n")
        return [f for f in fichiers if f]
    return []

print(f"Version Python : {obtenir_info_python()}")
fichiers_py = lister_fichiers_python()
print(f"Fichiers Python : {len(fichiers_py)} fichiers")
for f in fichiers_py[:5]:
    print(f"  {f}")
if len(fichiers_py) > 5:
    print(f"  ... ({len(fichiers_py)} au total)")

# --- Envoyer des données via stdin ---
print("\n=== Envoi de données via stdin (grep) ===")

texte = "ligne1\nligne2 important\nligne3\nligne4 important"

resultat = subprocess.run(
    ["grep", "important"],
    input=texte,
    capture_output=True,
    text=True
)

print("Lignes filtrées :")
print(resultat.stdout, end="")

# --- Commandes shell avec pipes ---
print("\n=== Commande shell avec pipe ===")

resultat = subprocess.run(
    "ls *.py | wc -l",
    shell=True,
    capture_output=True,
    text=True
)
print(f"Nombre de fichiers Python : {resultat.stdout.strip()}")

# --- Bonnes pratiques ---
print("\n=== Bonnes pratiques ===")

# Utiliser pathlib pour les chemins
from pathlib import Path

chemin_pathlib = Path("dossier") / "fichier.txt"
chemin_ospath = os.path.join("dossier", "fichier.txt")
print(f"pathlib  : {chemin_pathlib}")
print(f"os.path  : {chemin_ospath}")
print(f"Identiques ? {str(chemin_pathlib) == chemin_ospath}")

# Gestion d'erreurs fichier
print("\nGestion d'erreurs fichier :")
try:
    os.remove("fichier_qui_nexiste_pas.txt")
except FileNotFoundError:
    print("  FileNotFoundError : le fichier n'existe pas")
except PermissionError:
    print("  PermissionError : permissions insuffisantes")
