# ============================================================================
#   Section 5.2 : Combiner map(), filter() et reduce()
#   Description : Somme des carrés des pairs, prix total en promo,
#                 moyenne des notes supérieures à 10
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

from functools import reduce

# --- Somme des carrés des nombres pairs ---
print("=== Somme des carrés des pairs ===")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Étape 1 : Filtrer les nombres pairs
pairs = filter(lambda x: x % 2 == 0, nombres)

# Étape 2 : Calculer le carré de chaque nombre
carres = map(lambda x: x ** 2, pairs)

# Étape 3 : Faire la somme
resultat = reduce(lambda acc, x: acc + x, carres)

print(f"Somme des carrés des pairs : {resultat}")
# 2² + 4² + 6² + 8² + 10² = 4 + 16 + 36 + 64 + 100 = 220

# Version compacte
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultat = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, nombres))
)

print(f"Somme des carrés des pairs : {resultat}")  # 220

# --- Prix total des produits en promotion ---
print("\n=== Prix total en promotion ===")

produits = [
    {"nom": "Ordinateur", "prix": 800, "en_promo": True},
    {"nom": "Souris", "prix": 25, "en_promo": False},
    {"nom": "Clavier", "prix": 75, "en_promo": True},
    {"nom": "Écran", "prix": 300, "en_promo": True},
    {"nom": "Webcam", "prix": 50, "en_promo": False},
]

# Filtrer les produits en promotion
produits_promo = filter(lambda p: p["en_promo"], produits)

# Extraire les prix
prix = map(lambda p: p["prix"], produits_promo)

# Calculer le total
total = reduce(lambda acc, prix: acc + prix, prix, 0)

print(f"Prix total des produits en promotion : {total}EUR")  # 1175EUR

# --- Moyenne des notes supérieures à 10 ---
print("\n=== Moyenne des notes > 10 ===")

notes = [8, 15, 12, 9, 18, 14, 7, 16, 11]

# Filtrer les notes > 10
notes_valides = list(filter(lambda x: x > 10, notes))

# Calculer la somme
somme = reduce(lambda acc, x: acc + x, notes_valides)

# Calculer la moyenne
moyenne = somme / len(notes_valides)

print(f"Notes > 10 : {notes_valides}")
print(f"Moyenne : {moyenne:.2f}")  # Moyenne : 14.33
