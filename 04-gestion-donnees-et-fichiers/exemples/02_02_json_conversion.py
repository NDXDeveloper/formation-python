# ============================================================================
#   Section 4.2 : JSON - Conversion entre Python et JSON
#   Description : json.dumps() et json.loads() pour convertir sans fichier,
#                 et les pièges de conversion (tuple, clés, types non sérialisables)
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import json
from datetime import datetime

# --- Python -> JSON (chaîne de caractères) ---
print("=== dumps() : Python -> JSON ===")

data = {"nom": "Alice", "age": 30}

json_string = json.dumps(data, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>

# --- JSON -> Python ---
print("\n=== loads() : JSON -> Python ===")

json_string = '{"nom": "Bob", "age": 25}'

data = json.loads(json_string)
print(data)
print(type(data))  # <class 'dict'>

# --- Pièges de conversion à connaître ---
print("\n=== Pièges de conversion ===")

# 1. Les tuples deviennent des tableaux (relus comme des listes)
print("tuple ->", json.dumps({"t": (1, 2)}))          # {"t": [1, 2]}

# 2. Les clés de dictionnaire sont converties en chaînes
print("clé 1 ->", json.dumps({1: "a"}))               # {"1": "a"}

# 3. Tous les objets ne sont pas sérialisables
try:
    json.dumps({"date": datetime(2026, 6, 1)})
except TypeError as e:
    print("datetime ->", e)                            # Object of type datetime is not JSON serializable

# Solution simple : default=str (convertit en texte)
print("avec default=str ->", json.dumps({"date": datetime(2026, 6, 1)}, default=str))
