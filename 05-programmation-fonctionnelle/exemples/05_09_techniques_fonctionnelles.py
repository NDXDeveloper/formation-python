# ============================================================================
#   Section 5.5 : Techniques fonctionnelles en Python
#   Description : Structures immuables avec namedtuple, combiner prédicats,
#                 code modulaire fonctionnel
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

from collections import namedtuple

# --- Structures immuables ---
print("=== namedtuple ===")

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(3, 4)

# Pour "modifier", créer un nouveau point
p2 = Point(p1.x + 1, p1.y)
print(p1)  # Point(x=3, y=4)
print(p2)  # Point(x=4, y=4)

# --- Combiner des prédicats ---
print("\n=== Prédicats combinés ===")

def est_pair(n):
    return n % 2 == 0

def est_positif(n):
    return n > 0

def combiner_predicats(pred1, pred2):
    return lambda x: pred1(x) and pred2(x)

est_pair_et_positif = combiner_predicats(est_pair, est_positif)
nombres = [-2, -1, 0, 1, 2, 3, 4]
print(list(filter(est_pair_et_positif, nombres)))  # [2, 4]

# --- Calcul prix TTC ---
print("\n=== Fonctions pures testables ===")

def calculer_prix_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva)

assert calculer_prix_ttc(100, 0.20) == 120
print(f"100 HT -> {calculer_prix_ttc(100, 0.20)} TTC")

def filtrer_pairs(nombres):
    return [n for n in nombres if n % 2 == 0]

assert filtrer_pairs([1, 2, 3, 4]) == [2, 4]
assert filtrer_pairs([]) == []
print(f"Pairs dans [1..6] : {filtrer_pairs([1, 2, 3, 4, 5, 6])}")

# --- Somme sans effets de bord ---
print("\n=== Sans effets de bord ===")

def calculer_somme(liste):
    return sum(liste)

print(calculer_somme([1, 2, 3, 4, 5]))  # 15

# --- Traitement fonctionnel lisible ---
print("\n=== Traitement lisible ===")

def traiter_donnees(donnees):
    """Traite les données de manière fonctionnelle mais lisible."""
    nettoyees = [d.strip().lower() for d in donnees if d]
    uniques = list(set(nettoyees))
    triees = sorted(uniques)
    return triees

donnees = ["  Python ", "java", "", " PYTHON", "Ruby ", "java  "]
print(traiter_donnees(donnees))  # ['java', 'python', 'ruby']

# --- Clarté vs densité ---
print("\n=== Clarté ===")

def somme_des_carres(nombres):
    """Calcule la somme des carrés."""
    return sum(n ** 2 for n in nombres)

print(f"Somme des carrés [1..5] : {somme_des_carres([1, 2, 3, 4, 5])}")
# 1 + 4 + 9 + 16 + 25 = 55
