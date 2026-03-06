# ============================================================================
#   Section 2.1 : Les Dictionnaires - Supprimer des éléments
#   Description : del, pop() avec valeur par défaut, clear()
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "profession": "Ingénieure"
}

# Supprimer une clé spécifique avec del
del personne["profession"]
print(personne)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}

# Supprimer avec pop() et récupérer la valeur
age = personne.pop("age")
print(age)       # 25
print(personne)  # {'nom': 'Alice', 'ville': 'Paris'}

# Supprimer avec pop() avec valeur par défaut
telephone = personne.pop("telephone", "Non renseigné")
print(telephone)  # 'Non renseigné'

# Vider complètement le dictionnaire
personne.clear()
print(personne)  # {}
