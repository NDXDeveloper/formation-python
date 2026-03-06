# ============================================================================
#   Section 2.3 : defaultdict - Cas d'usage pratiques
#   Description : Compter mots, grouper étudiants, tags uniques, matrice creuse,
#                 index inversé, graphe, fréquence avec seuil, multi-niveaux
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import defaultdict

# --- 1. Compter des mots ---
texte = "le chat et le chien jouent avec le chat"
compteur = defaultdict(int)
for mot in texte.split():
    compteur[mot] += 1
print(f"Mots : {dict(compteur)}")

# --- 2. Grouper des étudiants ---
etudiants = [
    ('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'),
    ('David', 'C'), ('Eve', 'B')
]
classes = defaultdict(list)
for nom, classe in etudiants:
    classes[classe].append(nom)
print(f"Classes : {dict(sorted(classes.items()))}")

# --- 3. Tags uniques ---
articles = [
    ('Article 1', 'python'), ('Article 1', 'programmation'),
    ('Article 2', 'python'), ('Article 2', 'data'),
    ('Article 1', 'python')  # doublon
]
tags_par_article = defaultdict(set)
for article, tag in articles:
    tags_par_article[article].add(tag)
print(f"Tags : { {k: sorted(v) for k, v in sorted(tags_par_article.items())} }")

# --- 4. Matrice creuse ---
matrice = defaultdict(dict)
matrice[0][0] = 1
matrice[2][5] = 7
matrice[100][200] = 42
print(f"\nmatrice[0][0] = {matrice[0][0]}")
print(f"matrice[2][5] = {matrice[2][5]}")
print(f"matrice[50] = {matrice[50]}")  # {} par défaut

# --- 5. Index inversé ---
print()
documents = {
    'doc1': 'python est un langage de programmation',
    'doc2': 'python est facile à apprendre',
    'doc3': 'java est aussi un langage'
}
index = defaultdict(list)
for doc_id, contenu in documents.items():
    for mot in contenu.split():
        index[mot].append(doc_id)
print(f"'python' dans : {index['python']}")
print(f"'langage' dans : {index['langage']}")

# --- 6. Graphe ---
print()
graphe = defaultdict(list)
graphe['A'].append('B')
graphe['A'].append('C')
graphe['B'].append('C')
graphe['C'].append('D')
print(f"Graphe : {dict(graphe)}")
print(f"Depuis Z : {graphe['Z']}")  # [] (pas d'erreur !)

# --- 7. Multi-niveaux ---
print()
ventes = [
    ('Nord', 'Laptop', 1000), ('Sud', 'Souris', 20),
    ('Nord', 'Clavier', 50), ('Sud', 'Laptop', 1000),
    ('Nord', 'Laptop', 1000)
]
ventes_groupees = defaultdict(lambda: defaultdict(list))
for region, produit, montant in ventes:
    ventes_groupees[region][produit].append(montant)

for region, produits in sorted(ventes_groupees.items()):
    print(f"{region}:")
    for produit, montants in sorted(produits.items()):
        print(f"  {produit}: {sum(montants)}€ ({len(montants)} ventes)")
