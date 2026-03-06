# ============================================================================
#   Section 5.2 : La fonction filter() - Bases et exemples pratiques
#   Description : Filtrer pairs avec boucle vs filter(), positifs, chaînes
#                 longues, dictionnaires, chaînes non vides, fonction perso
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

# --- Exemple de base : filtrer les nombres pairs ---
print("=== Filtrer les nombres pairs ===")

# Approche classique avec une boucle
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = []

for nombre in nombres:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)

print(nombres_pairs)  # [2, 4, 6, 8, 10]

# Avec filter()
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))

print(nombres_pairs)  # [2, 4, 6, 8, 10]

# --- Filtrer les nombres positifs ---
print("\n=== Nombres positifs ===")

nombres = [-5, 3, -2, 8, -1, 0, 7, -9]

positifs = list(filter(lambda x: x > 0, nombres))

print(positifs)  # [3, 8, 7]

# --- Filtrer les chaînes longues ---
print("\n=== Chaînes longues ===")

mots = ["chat", "chien", "éléphant", "oiseau", "papillon", "rat"]

mots_longs = list(filter(lambda mot: len(mot) > 5, mots))

print(mots_longs)  # ['éléphant', 'oiseau', 'papillon']

# --- Filtrer des dictionnaires ---
print("\n=== Produits pas chers ===")

produits = [
    {"nom": "Pomme", "prix": 2.5},
    {"nom": "Banane", "prix": 1.8},
    {"nom": "Mangue", "prix": 5.2},
    {"nom": "Orange", "prix": 3.0},
]

produits_pas_chers = list(filter(lambda p: p["prix"] < 3, produits))

print("Produits à moins de 3EUR :")
for p in produits_pas_chers:
    print(f"  - {p['nom']}: {p['prix']}EUR")
# Pomme: 2.5EUR
# Banane: 1.8EUR

# --- Filtrer les chaînes non vides ---
print("\n=== Chaînes non vides ===")

textes = ["Bonjour", "", "Python", "   ", "Monde", ""]

textes_valides = list(filter(lambda t: t.strip() != "", textes))

print(textes_valides)  # ['Bonjour', 'Python', 'Monde']

# --- Filtrer avec une fonction personnalisée ---
print("\n=== Adultes ===")

def est_adulte(personne):
    """Vérifie si une personne est majeure."""
    return personne["age"] >= 18

personnes = [
    {"nom": "Alice", "age": 25},
    {"nom": "Bob", "age": 17},
    {"nom": "Charlie", "age": 30},
    {"nom": "David", "age": 16},
]

adultes = list(filter(est_adulte, personnes))

print("Adultes :")
for p in adultes:
    print(f"  - {p['nom']} ({p['age']} ans)")
# Alice (25 ans)
# Charlie (30 ans)
