# ============================================================================
#   Section 7.1 : Les modules os, sys et subprocess
#   Description : Module sys - informations interpréteur, argv, getsizeof,
#                 path, stdout/stderr, script avec arguments
#   Fichier source : 01-os-sys-subprocess.md
# ============================================================================

import sys
import subprocess
import os
from pathlib import Path

# --- Informations sur l'interpréteur ---
print("=== Informations interpréteur ===")
print(f"Version : {sys.version}")
print(f"Version info : {sys.version_info}")
print(f"Plateforme : {sys.platform}")
print(f"Exécutable : {sys.executable}")

# --- Chemins de recherche des modules ---
print("\n=== sys.path (3 premiers) ===")
for i, chemin in enumerate(sys.path[:3]):
    print(f"  {i}: {chemin}")
print(f"  ... ({len(sys.path)} chemins au total)")

# --- Flux d'entrée/sortie ---
print("\n=== Flux standard ===")
sys.stdout.write("Message sur stdout\n")
sys.stderr.write("Message sur stderr (erreur simulée)\n")

# --- Taille mémoire des objets ---
print("\n=== Taille mémoire (getsizeof) ===")

objets = {
    "entier 0": 0,
    "entier 1000": 1000,
    "liste [1,2,3,4,5]": [1, 2, 3, 4, 5],
    "chaîne 'Bonjour le monde'": "Bonjour le monde",
    "dict vide {}": {},
    "tuple (1,2,3)": (1, 2, 3),
    "bool True": True,
}

for description, obj in objets.items():
    taille = sys.getsizeof(obj)
    print(f"  {description:30s} : {taille} octets")

# --- Script avec arguments via subprocess ---
print("\n=== Script avec arguments (sys.argv) ===")

# Créer un script temporaire qui utilise sys.argv
script_contenu = '''\
import sys

print(f"Nom du script : {sys.argv[0]}")
print(f"Nombre d'arguments : {len(sys.argv) - 1}")

if len(sys.argv) > 1:
    print("Arguments reçus :")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Argument {i} : {arg}")
else:
    print("Aucun argument fourni")
'''

script_path = Path("_temp_script_argv.py")
script_path.write_text(script_contenu, encoding="utf-8")

# Exécuter sans arguments
print("--- Exécution sans arguments ---")
result = subprocess.run(
    [sys.executable, str(script_path)],
    capture_output=True, text=True
)
print(result.stdout, end="")

# Exécuter avec arguments
print("\n--- Exécution avec arguments ---")
result = subprocess.run(
    [sys.executable, str(script_path), "bonjour", "monde", "123"],
    capture_output=True, text=True
)
print(result.stdout, end="")

# --- Script calculateur avec validation ---
print("\n=== Script calculateur (validation argv) ===")

calc_contenu = '''\
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage : python script.py <nombre1> <nombre2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        resultat = a + b
        print(f"La somme de {a} et {b} est {resultat}")
        sys.exit(0)
    except ValueError:
        print("Erreur : Les arguments doivent être des nombres")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

calc_path = Path("_temp_calc.py")
calc_path.write_text(calc_contenu, encoding="utf-8")

# Test avec des nombres valides
result = subprocess.run(
    [sys.executable, str(calc_path), "10.5", "20.3"],
    capture_output=True, text=True
)
print(f"Valide : {result.stdout.strip()} (code: {result.returncode})")

# Test sans arguments
result = subprocess.run(
    [sys.executable, str(calc_path)],
    capture_output=True, text=True
)
print(f"Sans args : {result.stdout.strip()} (code: {result.returncode})")

# Test avec des arguments invalides
result = subprocess.run(
    [sys.executable, str(calc_path), "abc", "def"],
    capture_output=True, text=True
)
print(f"Invalide : {result.stdout.strip()} (code: {result.returncode})")

# Nettoyage
script_path.unlink()
calc_path.unlink()
print("\nNettoyage effectué")
