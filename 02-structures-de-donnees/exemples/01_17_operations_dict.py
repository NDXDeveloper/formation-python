# ============================================================================
#   Section 2.1 : Les Dictionnaires - Opérations courantes
#   Description : len, in, keys(), values(), items(), copie, setdefault()
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Nombre de paires clé-valeur
print(len(personne))  # 3

# Vérifier si une clé existe
print("nom" in personne)        # True
print("profession" in personne) # False

# Obtenir toutes les clés
print(personne.keys())        # dict_keys(['nom', 'age', 'ville'])
print(list(personne.keys()))  # ['nom', 'age', 'ville']

# Obtenir toutes les valeurs
print(personne.values())  # dict_values(['Alice', 25, 'Paris'])

# Obtenir toutes les paires clé-valeur
print(personne.items())  # dict_items([('nom', 'Alice'), ('age', 25), ('ville', 'Paris')])

# --- Copier un dictionnaire ---
print("\n--- Copie ---")

# Mauvaise méthode : crée une référence
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2, 'c': 3} - dict1 est aussi modifié !

# Bonne méthode : copie superficielle
dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()
dict3 = dict(dict1)

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2}
print(dict2)  # {'a': 1, 'b': 2, 'c': 3}

# --- setdefault() ---
print("\n--- setdefault ---")
personne2 = {"nom": "Alice", "age": 25}

# Si la clé existe, retourne sa valeur
print(personne2.setdefault("nom", "Inconnu"))  # 'Alice'

# Si la clé n'existe pas, l'ajoute avec la valeur par défaut
print(personne2.setdefault("ville", "Paris"))  # 'Paris'
print(personne2)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
