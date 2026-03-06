# ============================================================================
#   Section 2.1 : Les Dictionnaires - Accéder aux valeurs
#   Description : Accès par clé [], get() avec valeur par défaut
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès direct par clé
print(personne["nom"])  # 'Alice'

# Accès avec get() (plus sûr)
print(personne.get("age"))        # 25
print(personne.get("profession")) # None
print(personne.get("profession", "Non spécifiée"))  # 'Non spécifiée'

# Accéder à une clé inexistante avec [] lève une erreur
try:
    print(personne["profession"])
except KeyError as e:
    print(f"KeyError : {e}")
