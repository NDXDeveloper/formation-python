# ============================================================================
#   Section 2.1 : Les Dictionnaires - Créer un dictionnaire
#   Description : Dictionnaire vide, avec éléments, dict(), types mixtes
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Dictionnaire vide
mon_dict = {}
autre_dict = dict()

# Dictionnaire avec des éléments
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Utiliser dict() avec des paires clé-valeur
etudiant = dict(nom="Bob", age=22, specialite="Informatique")

# Dictionnaire avec différents types de valeurs
produit = {
    "nom": "Ordinateur",
    "prix": 999.99,
    "en_stock": True,
    "caracteristiques": ["16GB RAM", "SSD 512GB"],
    "dimensions": (30, 20, 2)
}

print(personne)
print(etudiant)
print(produit)
