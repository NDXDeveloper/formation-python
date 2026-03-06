# ============================================================================
#   Section 5.2 : Alternatives natives et bonnes pratiques
#   Description : sum() vs reduce(), max()/min() vs reduce(), any()/all(),
#                 lisibilité, fonctions nommées, compréhensions
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

from functools import reduce

# --- sum() au lieu de reduce() ---
print("=== sum() vs reduce() ===")

nombres = [1, 2, 3, 4, 5]

# Avec reduce()
somme_reduce = reduce(lambda acc, x: acc + x, nombres)

# Plus simple et plus rapide
somme_native = sum(nombres)

print(somme_reduce)  # 15
print(somme_native)  # 15

# --- max() et min() au lieu de reduce() ---
print("\n=== max() vs reduce() ===")

nombres = [45, 12, 89, 34, 67]

# Avec reduce()
max_reduce = reduce(lambda acc, x: acc if acc > x else x, nombres)

# Plus simple et plus rapide
max_native = max(nombres)

print(max_reduce)  # 89
print(max_native)  # 89

# --- any() et all() ---
print("\n=== all() ===")

nombres = [2, 4, 6, 8, 10]

# Vérifier si tous les nombres sont pairs
tous_pairs = all(map(lambda x: x % 2 == 0, nombres))

# Ou plus simple avec compréhension
tous_pairs_comp = all(x % 2 == 0 for x in nombres)

print(tous_pairs)       # True
print(tous_pairs_comp)  # True

# --- Bonnes pratiques : lisibilité ---
print("\n=== Lisibilité ===")

# Difficile à lire (une seule ligne)
resultat = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, map(lambda x: x + 1, range(10)))))
print(f"Compact : {resultat}")

# Plus clair avec des étapes
nombres = range(10)
increments = map(lambda x: x + 1, nombres)
pairs = filter(lambda x: x % 2 == 0, increments)
doubles = map(lambda x: x * 2, pairs)
resultat = list(doubles)
print(f"Par étapes : {resultat}")

# Encore mieux avec compréhension
resultat = [2 * (x + 1) for x in range(10) if (x + 1) % 2 == 0]
print(f"Compréhension : {resultat}")

# --- Fonctions nommées pour la clarté ---
print("\n=== Fonctions nommées ===")

def calculer_montant_tva(prix, taux_tva=0.20):
    """Calcule le montant TTC."""
    return prix * (1 + taux_tva)

prix_ht = [100, 200, 150, 300]

prix_ttc = list(map(calculer_montant_tva, prix_ht))

print(f"Prix HT : {prix_ht}")
print(f"Prix TTC : {prix_ttc}")
