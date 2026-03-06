# ============================================================================
#   Section 5.4 : Cas d'usage pratiques des générateurs
#   Description : Lecture de fichiers, pagination, pipeline de données,
#                 génération de données de test, parcours d'arborescence
#   Fichier source : 04-generateurs.md
# ============================================================================

from pathlib import Path

# --- Lecture de fichiers volumineux ---
print("=== Lecture de fichier ===")

def lire_lignes(nom_fichier):
    """Génère les lignes d'un fichier une par une."""
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            yield ligne.strip()

# Créer un fichier de test
Path('test_generateur.txt').write_text(
    "Ligne 1\nLigne 2 avec erreur\nLigne 3\nLigne 4 avec erreur\nLigne 5",
    encoding='utf-8'
)

for ligne in lire_lignes('test_generateur.txt'):
    if 'erreur' in ligne.lower():
        print(f"  Trouvée : {ligne}")

# --- Pagination de résultats ---
print("\n=== Pagination ===")

def paginer(elements, taille_page):
    """Génère des pages d'éléments."""
    for i in range(0, len(elements), taille_page):
        yield elements[i:i + taille_page]

items = list(range(1, 26))  # 25 items

for numero_page, page in enumerate(paginer(items, taille_page=5), start=1):
    print(f"Page {numero_page}: {page}")
# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# ...

# --- Pipeline de traitement de données ---
print("\n=== Pipeline ===")

def lire_nombres():
    """Simule la lecture de données."""
    for i in range(1, 11):
        yield i

def filtrer_pairs(nombres):
    """Filtre les nombres pairs."""
    for n in nombres:
        if n % 2 == 0:
            yield n

def multiplier_par_10(nombres):
    """Multiplie chaque nombre par 10."""
    for n in nombres:
        yield n * 10

donnees = lire_nombres()
pairs = filtrer_pairs(donnees)
resultat = multiplier_par_10(pairs)

print(list(resultat))  # [20, 40, 60, 80, 100]

# --- Génération de données de test ---
print("\n=== Données de test ===")

def generer_utilisateurs(n):
    """Génère n utilisateurs de test."""
    for i in range(1, n + 1):
        yield {
            "id": i,
            "nom": f"Utilisateur_{i}",
            "email": f"user{i}@example.com",
            "actif": i % 2 == 0
        }

for utilisateur in generer_utilisateurs(5):
    print(utilisateur)

# Nettoyage
Path('test_generateur.txt').unlink()
