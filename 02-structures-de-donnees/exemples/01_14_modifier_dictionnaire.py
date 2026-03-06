# ============================================================================
#   Section 2.1 : Les Dictionnaires - Modifier un dictionnaire
#   Description : Modifier valeurs, ajouter clés, update()
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Modifier une valeur existante
personne["age"] = 26
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris'}

# Ajouter une nouvelle paire clé-valeur
personne["profession"] = "Ingénieure"
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris', 'profession': 'Ingénieure'}

# Mettre à jour plusieurs valeurs à la fois
personne.update({"age": 27, "ville": "Lyon", "telephone": "0123456789"})
print(personne)
