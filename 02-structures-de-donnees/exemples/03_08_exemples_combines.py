# ============================================================================
#   Section 2.3 : Exemples combinés - namedtuple + defaultdict + Counter
#   Description : Analyse de ventes et analyse de réseau social combinant
#                 les trois collections spécialisées
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import namedtuple, defaultdict, Counter

# --- Exemple 1 : Analyse de ventes ---
Vente = namedtuple('Vente', 'produit region montant')

ventes = [
    Vente('Laptop', 'Nord', 1000),
    Vente('Souris', 'Sud', 20),
    Vente('Laptop', 'Nord', 1000),
    Vente('Clavier', 'Est', 50),
    Vente('Souris', 'Nord', 20),
    Vente('Laptop', 'Sud', 1000)
]

# 1. Compter les ventes par produit
ventes_par_produit = Counter(v.produit for v in ventes)
print("Ventes par produit :")
for produit, count in ventes_par_produit.most_common():
    print(f"  {produit}: {count}")

# 2. Grouper les montants par région
montants_par_region = defaultdict(list)
for vente in ventes:
    montants_par_region[vente.region].append(vente.montant)

print("\nCA par région :")
for region, montants in sorted(montants_par_region.items()):
    print(f"  {region}: {sum(montants)}€")

# 3. Produit le plus vendu par région
for region in sorted(montants_par_region):
    produits_region = [v.produit for v in ventes if v.region == region]
    top_produit = Counter(produits_region).most_common(1)[0]
    print(f"  Meilleur en {region} : {top_produit[0]}")

# --- Exemple 2 : Réseau social ---
print("\n--- Réseau social ---")
Interaction = namedtuple('Interaction', 'utilisateur action cible')

interactions = [
    Interaction('Alice', 'like', 'post1'),
    Interaction('Bob', 'comment', 'post1'),
    Interaction('Alice', 'like', 'post2'),
    Interaction('Charlie', 'share', 'post1'),
    Interaction('Alice', 'comment', 'post1'),
    Interaction('Bob', 'like', 'post1')
]

# Actions par utilisateur
actions_par_user = defaultdict(Counter)
for inter in interactions:
    actions_par_user[inter.utilisateur][inter.action] += 1

print("Actions par utilisateur :")
for user, actions in sorted(actions_par_user.items()):
    details = ", ".join(f"{a}: {c}" for a, c in actions.items())
    print(f"  {user}: {details}")

# Post le plus populaire
popularite_posts = Counter(i.cible for i in interactions)
post_populaire = popularite_posts.most_common(1)[0]
print(f"\nPost le plus populaire : {post_populaire[0]} ({post_populaire[1]} interactions)")
