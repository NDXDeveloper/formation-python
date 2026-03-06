# ============================================================================
#   Section 4.3 : Pickle - Limitations
#   Description : Objets non sérialisables : fichiers ouverts, lambdas,
#                 connexions réseau
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

# --- Fichiers ouverts ---
print("=== Fichier ouvert ===")

# Créer un fichier pour le test
with open('test.txt', 'w') as f:
    f.write("test")

fichier_ouvert = open('test.txt', 'r')
try:
    pickle.dumps(fichier_ouvert)
except TypeError as e:
    print(f"Erreur : {e}")
finally:
    fichier_ouvert.close()

# --- Fonctions lambda ---
print("\n=== Lambda ===")

ma_fonction = lambda x: x * 2
try:
    pickle.dumps(ma_fonction)
    print("Lambda sérialisée (succès inattendu)")
except (AttributeError, pickle.PicklingError) as e:
    print(f"Erreur : impossible de pickler une lambda")

# --- Fonctions réutilisables ---
print("\n=== Fonctions réutilisables ===")

from pathlib import Path

def sauvegarder(objet, fichier):
    """Sauvegarde un objet avec pickle"""
    with open(fichier, 'wb') as f:
        pickle.dump(objet, f, protocol=pickle.HIGHEST_PROTOCOL)

def charger(fichier, defaut=None):
    """Charge un objet avec pickle"""
    if not Path(fichier).exists():
        return defaut
    with open(fichier, 'rb') as f:
        return pickle.load(f)

# Utilisation simple
sauvegarder({'key': 'value'}, 'data.pkl')
data = charger('data.pkl', defaut={})
print(f"Données chargées : {data}")

data2 = charger('inexistant.pkl', defaut={'defaut': True})
print(f"Fichier inexistant -> défaut : {data2}")

# Nettoyage
os.remove('test.txt')
os.remove('data.pkl')
