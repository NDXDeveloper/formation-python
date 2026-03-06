# ============================================================================
#   Section 2.1 : Les Dictionnaires - Parcourir un dictionnaire
#   Description : Parcourir clés, valeurs, paires clé-valeur avec items()
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Parcourir les clés
print("Clés :")
for cle in personne:
    print(f"  {cle}")

# Parcourir les valeurs
print("Valeurs :")
for valeur in personne.values():
    print(f"  {valeur}")

# Parcourir les paires clé-valeur
print("Paires clé-valeur :")
for cle, valeur in personne.items():
    print(f"  {cle}: {valeur}")
