# ============================================================================
#   Section 2.2 : Exemple pratique - Filtrage et regroupement
#   Description : Produits par catégorie, prix moyen par catégorie
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Liste de produits avec catégories
produits = [
    {"nom": "Pomme", "categorie": "Fruits", "prix": 2.5},
    {"nom": "Carotte", "categorie": "Légumes", "prix": 1.8},
    {"nom": "Banane", "categorie": "Fruits", "prix": 1.5},
    {"nom": "Tomate", "categorie": "Légumes", "prix": 2.0}
]

# Créer un dictionnaire : catégorie → liste de noms de produits
produits_par_categorie = {
    categorie: [p["nom"] for p in produits if p["categorie"] == categorie]
    for categorie in set(p["categorie"] for p in produits)
}
print("Produits par catégorie :")
for cat, noms in sorted(produits_par_categorie.items()):
    print(f"  {cat}: {noms}")

# Prix moyen par catégorie
prix_moyens = {
    categorie: sum(p["prix"] for p in produits if p["categorie"] == categorie) /
               len([p for p in produits if p["categorie"] == categorie])
    for categorie in set(p["categorie"] for p in produits)
}
print(f"\nPrix moyens : {dict(sorted(prix_moyens.items()))}")
# Fruits: (2.5+1.5)/2=2.0, Légumes: (1.8+2.0)/2=1.9
