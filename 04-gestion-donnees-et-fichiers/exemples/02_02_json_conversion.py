# ============================================================================
#   Section 4.2 : JSON - Conversion entre Python et JSON
#   Description : json.dumps() et json.loads() pour convertir sans fichier
#   Fichier source : 02-formats-de-donnees.md
# ============================================================================

import json

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
