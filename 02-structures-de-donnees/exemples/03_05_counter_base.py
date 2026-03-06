# ============================================================================
#   Section 2.3 : Counter - Compter des éléments
#   Description : Création, most_common, elements, update, subtract,
#                 opérations arithmétiques
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import Counter

# --- Créer un Counter ---
mots = ['pomme', 'banane', 'pomme', 'orange', 'banane', 'pomme']
compteur = Counter(mots)
print(compteur)        # Counter({'pomme': 3, 'banane': 2, 'orange': 1})
print(compteur['pomme'])  # 3
print(compteur['kiwi'])   # 0 (pas d'erreur !)

# Différentes façons de créer
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"\nDepuis liste : {c1}")

c2 = Counter("hello world")
print(f"Depuis str : {c2}")

c3 = Counter({'rouge': 4, 'bleu': 2})
print(f"Depuis dict : {c3}")

c4 = Counter(chats=4, chiens=2, oiseaux=1)
print(f"Nommé : {c4}")

# --- most_common ---
print()
mots = ['python', 'java', 'python', 'c++', 'python', 'java', 'ruby']
compteur = Counter(mots)
print(f"Tous : {compteur.most_common()}")
print(f"Top 2 : {compteur.most_common(2)}")
print(f"Top 1 : {compteur.most_common(1)}")

# --- elements ---
c = Counter(a=3, b=2, c=1)
print(f"\nelements : {list(c.elements())}")

# --- update ---
c = Counter(['a', 'b', 'c'])
c.update(['a', 'b', 'd'])
print(f"Après update : {c}")

c2 = Counter(['a', 'e'])
c.update(c2)
print(f"Après update Counter : {c}")

# --- subtract ---
c1 = Counter(a=4, b=3, c=2)
c2 = Counter(a=1, b=2, d=1)
c1.subtract(c2)
print(f"\nAprès subtract : {c1}")  # d=-1

# --- Opérations arithmétiques ---
print()
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=1)

print(f"c1 + c2 = {c1 + c2}")  # Counter({'a': 4, 'b': 3, 'c': 1})
print(f"c1 - c2 = {c1 - c2}")  # Counter({'a': 2})
print(f"c1 & c2 = {c1 & c2}")  # Counter({'a': 1, 'b': 1})
print(f"c1 | c2 = {c1 | c2}")  # Counter({'a': 3, 'b': 2, 'c': 1})

# --- Manipuler les comptages ---
print()
c = Counter(a=3, b=2, c=0, d=-1)
c_positifs = +c  # Unary plus : garde seulement les positifs
print(f"+Counter : {c_positifs}")  # Counter({'a': 3, 'b': 2})

total = sum(c.values())
print(f"Total : {total}")  # 4
