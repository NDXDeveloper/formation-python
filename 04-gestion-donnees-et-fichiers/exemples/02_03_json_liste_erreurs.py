# ============================================================================
#   Section 4.2 : JSON - Liste de personnes et gestion des erreurs
#   Description : Sauvegarder/relire une liste de dictionnaires,
#                 gérer FileNotFoundError et JSONDecodeError
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import json
import os

# --- Liste de personnes ---
print("=== Liste de personnes en JSON ===")

personnes = [
    {"nom": "Dupont", "age": 30, "ville": "Paris"},
    {"nom": "Martin", "age": 25, "ville": "Lyon"},
    {"nom": "Bernard", "age": 35, "ville": "Marseille"}
]

# Sauvegarder
with open('personnes.json', 'w', encoding='utf-8') as f:
    json.dump(personnes, f, indent=4, ensure_ascii=False)

# Relire
with open('personnes.json', 'r', encoding='utf-8') as f:
    personnes_lues = json.load(f)

# Parcourir les données
for personne in personnes_lues:
    print(f"{personne['nom']} a {personne['age']} ans")

# --- Gestion des erreurs JSON ---
print("\n=== Gestion des erreurs ===")

# Fichier inexistant
try:
    with open('config_inexistant.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Le fichier n'existe pas")
except json.JSONDecodeError as e:
    print(f"Erreur de format JSON : {e}")

# JSON invalide
try:
    json_invalide = '{"nom": "Alice", age: 30}'  # age sans guillemets
    data = json.loads(json_invalide)
except json.JSONDecodeError as e:
    print(f"Erreur de format JSON : {e}")

# Nettoyage
os.remove('personnes.json')
