# ============================================================================
#   Section 7.1 : Les modules os, sys et subprocess
#   Description : Module os - informations système, manipulation de
#                 répertoires, création et suppression de dossiers
#   Fichier source : 01-os-sys-subprocess.md
# ============================================================================

import os

# --- Informations sur le système ---
print("=== Informations système ===")
print(f"Nom du système : {os.name}")  # 'posix' pour Linux/Mac, 'nt' pour Windows
print(f"Répertoire actuel : {os.getcwd()}")
print(f"Séparateur de chemin : {os.sep}")

# --- Manipulation des répertoires ---
print("\n=== Manipulation des répertoires ===")

# Créer un répertoire simple
os.mkdir("nouveau_dossier")
print("Dossier 'nouveau_dossier' créé")

# Créer des répertoires imbriqués
os.makedirs("dossier/sous_dossier/sous_sous_dossier")
print("Dossiers imbriqués créés")

# Changer de répertoire et vérifier
ancien_rep = os.getcwd()
os.chdir("nouveau_dossier")
print(f"Répertoire après chdir : {os.getcwd()}")

# Revenir au répertoire parent
os.chdir(ancien_rep)
print(f"Retour au répertoire : {os.getcwd()}")

# Supprimer les répertoires créés
os.rmdir("nouveau_dossier")
print("'nouveau_dossier' supprimé")

os.removedirs("dossier/sous_dossier/sous_sous_dossier")
print("Dossiers imbriqués supprimés")

# --- Lister le contenu d'un répertoire ---
print("\n=== Lister le contenu ===")

# Créer une structure temporaire pour la démo
os.makedirs("_temp_demo/sous_dossier", exist_ok=True)
with open("_temp_demo/fichier1.txt", "w") as f:
    f.write("contenu 1")
with open("_temp_demo/fichier2.py", "w") as f:
    f.write("# script python")

contenu = os.listdir("_temp_demo")
print(f"Contenu de _temp_demo : {sorted(contenu)}")

# Filtrer fichiers et dossiers
for element in sorted(os.listdir("_temp_demo")):
    chemin_complet = os.path.join("_temp_demo", element)
    if os.path.isfile(chemin_complet):
        print(f"  Fichier : {element}")
    elif os.path.isdir(chemin_complet):
        print(f"  Dossier : {element}")

# Nettoyage
import shutil
shutil.rmtree("_temp_demo")
print("\nNettoyage : _temp_demo supprimé")
