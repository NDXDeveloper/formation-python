# ============================================================================
#   Section 2.1 : Exemple pratique - Gestion d'un inventaire
#   Description : Dictionnaire + liste de tuples pour gérer un inventaire
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Dictionnaire pour stocker les produits avec leurs quantités
inventaire = {
    "pommes": 50,
    "bananes": 30,
    "oranges": 40
}

# Liste des commandes reçues (tuples)
commandes = [
    ("pommes", 10),
    ("bananes", 5),
    ("oranges", 15),
    ("pommes", 5)
]

# Traiter les commandes
for produit, quantite in commandes:
    if produit in inventaire:
        inventaire[produit] -= quantite
        print(f"Commande traitée : {quantite} {produit}")

print("Inventaire mis à jour :", inventaire)
# {'pommes': 35, 'bananes': 25, 'oranges': 25}
