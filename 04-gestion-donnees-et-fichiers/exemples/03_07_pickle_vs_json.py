# ============================================================================
#   Section 4.3 : Pickle vs JSON - Comparaison
#   Description : Pickle gère tous les types Python (tuples, sets, bytes),
#                 JSON ne supporte que les types de base
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import json
import os

# Données complexes avec types non supportés par JSON
donnees = {
    'nom': 'Alice',
    'date': (2024, 10, 27),  # Tuple
    'set': {1, 2, 3},         # Set
    'bytes': b'data'          # Bytes
}

# Pickle : fonctionne avec tous les types
with open('donnees.pkl', 'wb') as f:
    pickle.dump(donnees, f)
print("Pickle : sauvegarde réussie")

# Vérification
with open('donnees.pkl', 'rb') as f:
    donnees_pickle = pickle.load(f)
print(f"  Tuple restauré : {donnees_pickle['date']}")
print(f"  Set restauré : {donnees_pickle['set']}")
print(f"  Bytes restauré : {donnees_pickle['bytes']}")

# JSON : ne supporte pas tous les types
try:
    with open('donnees.json', 'w') as f:
        json.dump(donnees, f)
except TypeError as e:
    print(f"\nJSON : {e}")

# Nettoyage
os.remove('donnees.pkl')
