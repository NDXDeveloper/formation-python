# ============================================================================
#   Section 5.2 : Cas d'usage avancés
#   Description : Pipeline de traitement de ventes, transformation de données
#                 étudiants, analyse de texte
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

from functools import reduce

# --- Pipeline de traitement de données ---
print("=== Pipeline de ventes ===")

ventes = [
    {"produit": "Laptop", "quantite": 2, "prix_unitaire": 800},
    {"produit": "Souris", "quantite": 5, "prix_unitaire": 25},
    {"produit": "Clavier", "quantite": 3, "prix_unitaire": 75},
    {"produit": "Écran", "quantite": 1, "prix_unitaire": 300},
]

def traiter_ventes(ventes):
    # 1. Calculer le montant total de chaque vente
    avec_montants = list(map(
        lambda v: {**v, "montant_total": v["quantite"] * v["prix_unitaire"]},
        ventes
    ))

    # 2. Filtrer les ventes de plus de 200EUR
    ventes_importantes = list(filter(
        lambda v: v["montant_total"] > 200,
        avec_montants
    ))

    # 3. Calculer le chiffre d'affaires total
    ca_total = reduce(
        lambda acc, v: acc + v["montant_total"],
        ventes_importantes,
        0
    )

    return ventes_importantes, ca_total

ventes_importantes, ca = traiter_ventes(ventes)

print("Ventes importantes (>200EUR) :")
for v in ventes_importantes:
    print(f"  {v['produit']}: {v['montant_total']}EUR")
print(f"\nChiffre d'affaires : {ca}EUR")

# --- Transformation de données structurées ---
print("\n=== Étudiants avec mentions ===")

etudiants = [
    {"nom": "Alice", "notes": [15, 18, 16]},
    {"nom": "Bob", "notes": [12, 14, 13]},
    {"nom": "Charlie", "notes": [17, 19, 18]},
]

# Calculer la moyenne de chaque étudiant
etudiants_avec_moyennes = list(map(
    lambda e: {
        "nom": e["nom"],
        "notes": e["notes"],
        "moyenne": sum(e["notes"]) / len(e["notes"])
    },
    etudiants
))

# Filtrer ceux qui ont la moyenne >= 15
mentions_bien = list(filter(
    lambda e: e["moyenne"] >= 15,
    etudiants_avec_moyennes
))

print("Étudiants avec mention Bien (>=15) :")
for e in mentions_bien:
    print(f"  {e['nom']}: {e['moyenne']:.2f}")

# --- Analyse de texte ---
print("\n=== Analyse de texte ===")

texte = "Python est un langage de programmation puissant et facile à apprendre"

# Compter le nombre total de caractères (sans espaces)
mots = texte.split()

# Extraire la longueur de chaque mot
longueurs = list(map(len, mots))

# Calculer la longueur totale
longueur_totale = reduce(lambda acc, x: acc + x, longueurs)

# Calculer la longueur moyenne
longueur_moyenne = longueur_totale / len(mots)

print(f"Nombre de mots : {len(mots)}")
print(f"Longueur totale : {longueur_totale} caractères")
print(f"Longueur moyenne : {longueur_moyenne:.2f} caractères/mot")
