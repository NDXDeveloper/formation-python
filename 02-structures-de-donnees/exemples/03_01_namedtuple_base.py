# ============================================================================
#   Section 2.3 : namedtuple - Tuples avec des noms
#   Description : Créer, accéder, immuabilité, unpacking, _asdict, _replace,
#                 valeurs par défaut
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import namedtuple

# --- Créer un namedtuple ---
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)

# Accéder aux valeurs par nom
print(point.x)   # 10
print(point.y)   # 20
print(point[0])  # 10 (aussi par index)

# Différentes façons de définir les champs
Personne = namedtuple('Personne', 'nom age ville')
alice = Personne('Alice', 25, 'Paris')
print(f"{alice.nom}, {alice.age}, {alice.ville}")

# --- Immuabilité ---
try:
    point.x = 15
except AttributeError as e:
    print(f"AttributeError : {e}")

# --- Unpacking ---
nom, age, ville = alice
print(f"Unpacking : {nom}")  # Alice

personnes = [
    Personne('Alice', 25, 'Paris'),
    Personne('Bob', 30, 'Lyon')
]
for nom, age, ville in personnes:
    print(f"  {nom} a {age} ans et habite à {ville}")

# --- Conversion en dictionnaire ---
alice_dict = alice._asdict()
print(f"_asdict : {alice_dict}")  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}

# --- Copie avec modifications ---
alice_plus_vieille = alice._replace(age=26)
print(f"Original : {alice}")
print(f"Modifié  : {alice_plus_vieille}")

# --- Valeurs par défaut ---
Personne2 = namedtuple('Personne2', 'nom age ville', defaults=['Inconnu'])
p1 = Personne2('Alice', 25)
print(f"Défaut : {p1}")  # Personne2(nom='Alice', age=25, ville='Inconnu')
p2 = Personne2('Bob', 30, 'Lyon')
print(f"Fourni : {p2}")  # Personne2(nom='Bob', age=30, ville='Lyon')
