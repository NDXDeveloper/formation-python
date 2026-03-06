# ============================================================================
#   Section 4.2 : JSON - Lire et écrire des fichiers JSON
#   Description : json.load() pour lire, json.dump() pour écrire avec
#                 indent et ensure_ascii
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import json
import os

# --- Créer un fichier JSON de test ---
personne_data = {
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 28,
    "ville": "Paris",
    "competences": ["Python", "JavaScript", "SQL"],
    "actif": True,
    "adresse": {
        "rue": "12 rue de la Paix",
        "code_postal": "75002"
    }
}

with open('personne.json', 'w', encoding='utf-8') as f:
    json.dump(personne_data, f, indent=4, ensure_ascii=False)

# --- Lire un fichier JSON ---
print("=== Lire un fichier JSON ===")

with open('personne.json', 'r', encoding='utf-8') as fichier:
    donnees = json.load(fichier)

print(donnees['nom'])               # Dupont
print(donnees['age'])                # 28
print(donnees['competences'])        # ['Python', 'JavaScript', 'SQL']
print(donnees['adresse']['rue'])     # 12 rue de la Paix

# --- Écrire dans un fichier JSON ---
print("\n=== Écrire dans un fichier JSON ===")

personne = {
    "nom": "Martin",
    "prenom": "Lucas",
    "age": 35,
    "ville": "Lyon",
    "competences": ["Python", "Django", "PostgreSQL"],
    "actif": True
}

with open('nouvelle_personne.json', 'w', encoding='utf-8') as fichier:
    json.dump(personne, fichier, indent=4, ensure_ascii=False)

print("Fichier JSON créé avec succès !")

# Vérification
with open('nouvelle_personne.json', 'r', encoding='utf-8') as f:
    print(f.read())

# Nettoyage
os.remove('personne.json')
os.remove('nouvelle_personne.json')
