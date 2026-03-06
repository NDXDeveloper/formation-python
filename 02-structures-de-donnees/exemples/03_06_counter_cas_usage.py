# ============================================================================
#   Section 2.3 : Counter - Cas d'usage pratiques
#   Description : Analyse texte, votes, inventaire/stock, comparaison documents,
#                 analyse de logs
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import Counter

# --- 1. Analyser un texte ---
texte = """
Python est un langage de programmation interprété, multi-paradigme et multiplateformes.
Il favorise la programmation impérative structurée, fonctionnelle et orientée objet.
"""
mots = texte.lower().split()
compteur_mots = Counter(mots)

print(f"Nombre total de mots : {sum(compteur_mots.values())}")
print(f"Nombre de mots uniques : {len(compteur_mots)}")
print(f"Top 5 :")
for mot, freq in compteur_mots.most_common(5):
    print(f"  {mot}: {freq}")

# --- 2. Votes ---
print()
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob',
         'Alice', 'Charlie', 'Alice', 'Bob', 'Alice']
resultats = Counter(votes)

print("Résultats des élections :")
for candidat, nb_votes in resultats.most_common():
    pourcentage = (nb_votes / len(votes)) * 100
    print(f"  {candidat}: {nb_votes} votes ({pourcentage:.1f}%)")

gagnant = resultats.most_common(1)[0][0]
print(f"Gagnant : {gagnant}")

# --- 3. Inventaire et stock ---
print()
stock = Counter(pommes=50, bananes=30, oranges=40)
ventes = Counter(pommes=10, bananes=5, oranges=15)

stock_restant = stock - ventes
print(f"Stock restant : {stock_restant}")

livraison = Counter(pommes=20, bananes=15, kiwis=10)
stock_final = stock_restant + livraison
print(f"Stock final : {stock_final}")

print("Produits < 30 unités :")
for produit, quantite in stock_final.items():
    if quantite < 30:
        print(f"  {produit}: {quantite}")

# --- 4. Comparaison de documents ---
print()
doc1 = "python est un langage de programmation"
doc2 = "java est un langage de programmation orientée objet"

mots_doc1 = Counter(doc1.split())
mots_doc2 = Counter(doc2.split())

mots_communs = mots_doc1 & mots_doc2
print(f"Mots communs : {dict(mots_communs)}")

mots_uniques_doc1 = mots_doc1 - mots_doc2
print(f"Uniques à doc1 : {dict(mots_uniques_doc1)}")

mots_uniques_doc2 = mots_doc2 - mots_doc1
print(f"Uniques à doc2 : {dict(mots_uniques_doc2)}")

# --- 5. Analyse de logs ---
print()
logs = ['200', '200', '404', '200', '500',
        '200', '404', '200', '200', '403']
codes_statut = Counter(logs)

print("Statistiques serveur :")
for code, count in sorted(codes_statut.items()):
    print(f"  Code {code}: {count} occurrences")

erreurs = {code: count for code, count in codes_statut.items()
           if int(code) >= 400}
if erreurs:
    print(f"Erreurs détectées : {sum(erreurs.values())} au total")
