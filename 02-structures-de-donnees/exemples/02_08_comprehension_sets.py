# ============================================================================
#   Section 2.2 : Compréhensions de sets
#   Description : Créer des sets avec compréhension, conditions, doublons,
#                 domaines emails, mots uniques, valeurs absolues
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- Exemples de base ---
# Set de carrés
carres = {x**2 for x in range(5)}
print(sorted(carres))  # [0, 1, 4, 9, 16]

# Caractères uniques d'une chaîne
texte = "hello world"
caracteres_uniques = {c for c in texte if c != ' '}
print(sorted(caracteres_uniques))  # ['d', 'e', 'h', 'l', 'o', 'r', 'w']

# Longueurs uniques des mots
mots = ["chat", "chien", "oiseau", "chat", "lion"]
longueurs_uniques = {len(mot) for mot in mots}
print(sorted(longueurs_uniques))  # [4, 5, 6]

# Premières lettres (en minuscules)
prenoms = ["Alice", "Bob", "Charlie", "Anne"]
premieres_lettres = {nom[0].lower() for nom in prenoms}
print(sorted(premieres_lettres))  # ['a', 'b', 'c']

# --- Avec conditions ---
print()
# Nombres pairs uniques
nombres = [1, 2, 2, 3, 4, 4, 5, 6, 6]
pairs_uniques = {x for x in nombres if x % 2 == 0}
print(sorted(pairs_uniques))  # [2, 4, 6]

# Voyelles présentes dans un texte
texte = "Python est un excellent langage"
voyelles = {c.lower() for c in texte if c.lower() in 'aeiouy'}
print(sorted(voyelles))  # ['a', 'e', 'o', 'u', 'y'] (pas de 'i')

# Domaines uniques d'emails
emails = ["alice@example.com", "bob@test.com", "charlie@example.com"]
domaines = {email.split('@')[1] for email in emails}
print(sorted(domaines))  # ['example.com', 'test.com']

# --- Éliminer doublons avec transformation ---
print()
# Mots uniques en minuscules
texte = "Le Chat et le Chien jouent avec le Chat"
mots_uniques = {mot.lower() for mot in texte.split()}
print(sorted(mots_uniques))  # ['avec', 'chat', 'chien', 'et', 'jouent', 'le']

# Valeurs absolues uniques
nombres = [-2, -1, 0, 1, 2, 3]
absolues_uniques = {abs(x) for x in nombres}
print(sorted(absolues_uniques))  # [0, 1, 2, 3]
