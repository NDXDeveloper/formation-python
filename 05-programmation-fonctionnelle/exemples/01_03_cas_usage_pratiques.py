# ============================================================================
#   Section 5.1 : Cas d'usage pratiques
#   Description : Tri personnalisé, traitement de données avec réduction,
#                 validation de données
#   Fichier source : 01-lambda-et-fonctions-ordre-superieur.md
# ============================================================================

# --- Tri personnalisé ---
print("=== Tri personnalisé ===")

personnes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
    {"nom": "David", "age": 28}
]

personnes_par_age = sorted(personnes, key=lambda p: p["age"])
print("Triées par âge :")
for p in personnes_par_age:
    print(f"  {p['nom']} : {p['age']} ans")

personnes_par_nom = sorted(personnes, key=lambda p: p["nom"])
print("\nTriées par nom :")
for p in personnes_par_nom:
    print(f"  {p['nom']} : {p['age']} ans")

# --- Traitement de données ---
print("\n=== Réduction de prix ===")

produits = [
    {"nom": "Pomme", "prix": 2.5},
    {"nom": "Banane", "prix": 1.8},
    {"nom": "Orange", "prix": 3.2},
    {"nom": "Poire", "prix": 2.9}
]

def appliquer_reduction(produits, calculer_nouveau_prix):
    """Applique une réduction sur tous les produits."""
    return [
        {
            "nom": p["nom"],
            "prix_original": p["prix"],
            "prix_reduit": calculer_nouveau_prix(p["prix"])
        }
        for p in produits
    ]

avec_reduction = appliquer_reduction(produits, lambda prix: prix * 0.8)

print("Produits avec réduction de 20% :")
for p in avec_reduction:
    print(f"{p['nom']}: {p['prix_original']}EUR -> {p['prix_reduit']:.2f}EUR")

# --- Validation de données ---
print("\n=== Validation mot de passe ===")

def valider_donnees(donnees, validateurs):
    """Vérifie si les données passent tous les validateurs."""
    for validateur in validateurs:
        if not validateur(donnees):
            return False
    return True

validateurs_mdp = [
    lambda mdp: len(mdp) >= 8,
    lambda mdp: any(c.isupper() for c in mdp),
    lambda mdp: any(c.isdigit() for c in mdp),
]

mot_de_passe_1 = "Password123"
mot_de_passe_2 = "faible"

print(f"'{mot_de_passe_1}' est valide : {valider_donnees(mot_de_passe_1, validateurs_mdp)}")
print(f"'{mot_de_passe_2}' est valide : {valider_donnees(mot_de_passe_2, validateurs_mdp)}")
