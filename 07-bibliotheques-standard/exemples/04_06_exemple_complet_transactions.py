# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Exemple complet - analyse de transactions e-commerce
#                 et pipeline de traitement de texte
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

import itertools
import functools
from operator import itemgetter
from collections import Counter

# ==========================================
# 1. Analyse de transactions
# ==========================================
print("=== Analyse de transactions e-commerce ===")

transactions = [
    {'id': 1, 'client': 'Alice', 'categorie': 'Livres', 'montant': 25.50},
    {'id': 2, 'client': 'Bob', 'categorie': 'Electronique', 'montant': 450.00},
    {'id': 3, 'client': 'Alice', 'categorie': 'Livres', 'montant': 15.00},
    {'id': 4, 'client': 'Charlie', 'categorie': 'Vetements', 'montant': 89.99},
    {'id': 5, 'client': 'Alice', 'categorie': 'Electronique', 'montant': 120.00},
    {'id': 6, 'client': 'Bob', 'categorie': 'Livres', 'montant': 30.00},
    {'id': 7, 'client': 'Charlie', 'categorie': 'Electronique', 'montant': 199.99},
]

class AnalyseurTransactions:
    def __init__(self, transactions):
        self.transactions = transactions

    def total_par_client(self, client):
        transactions_client = [t for t in self.transactions if t['client'] == client]
        return functools.reduce(
            lambda total, t: total + t['montant'],
            transactions_client, 0
        )

    def grouper_par_categorie(self):
        transactions_triees = sorted(self.transactions, key=itemgetter('categorie'))
        print("\nTransactions par catégorie :")
        print("=" * 50)
        for categorie, groupe in itertools.groupby(transactions_triees, key=itemgetter('categorie')):
            liste_trans = list(groupe)
            total = sum(t['montant'] for t in liste_trans)
            print(f"\n{categorie} ({len(liste_trans)} transactions) :")
            for t in liste_trans:
                print(f"  - {t['client']:10s} : {t['montant']:7.2f} EUR")
            print(f"  Total : {total:.2f} EUR")

    def top_clients(self, n=3):
        clients = set(t['client'] for t in self.transactions)
        totaux = [(client, self.total_par_client(client)) for client in clients]
        totaux_tries = sorted(totaux, key=itemgetter(1), reverse=True)
        print(f"\nTop {n} clients :")
        print("=" * 50)
        for i, (client, total) in enumerate(itertools.islice(totaux_tries, n), 1):
            print(f"  {i}. {client:15s} : {total:7.2f} EUR")

    def statistiques_globales(self):
        montants = [t['montant'] for t in self.transactions]
        cumul = list(itertools.accumulate(montants))
        print("\nStatistiques globales :")
        print("=" * 50)
        print(f"Nombre de transactions : {len(self.transactions)}")
        print(f"Montant total : {sum(montants):.2f} EUR")
        print(f"Montant moyen : {sum(montants) / len(montants):.2f} EUR")
        print(f"Montant min : {min(montants):.2f} EUR")
        print(f"Montant max : {max(montants):.2f} EUR")
        print(f"\nEvolution CA cumulé :")
        for i, total in enumerate(cumul, 1):
            barre = "#" * int(total / 20)
            print(f"  Transaction {i}: {total:7.2f} EUR {barre}")

analyseur = AnalyseurTransactions(transactions)
analyseur.grouper_par_categorie()
analyseur.top_clients(3)
analyseur.statistiques_globales()

# ==========================================
# 2. Pipeline de traitement de texte
# ==========================================
print("\n\n=== Pipeline de traitement de texte ===")

def nettoyer_texte(texte):
    return texte.lower().strip()

def tokeniser(texte):
    return texte.split()

def filtrer_mots_courts(mots, longueur_min=3):
    return [mot for mot in mots if len(mot) >= longueur_min]

pipeline_texte = functools.partial(filtrer_mots_courts, longueur_min=4)

textes = [
    "Python est un langage de programmation puissant",
    "Python est facile a apprendre et tres populaire",
    "La programmation Python est utilisee partout",
    "Apprendre Python ouvre de nombreuses opportunites"
]

tous_les_mots = []
for texte in textes:
    texte_propre = nettoyer_texte(texte)
    mots = tokeniser(texte_propre)
    mots_filtres = pipeline_texte(mots)
    tous_les_mots.extend(mots_filtres)

compteur = Counter(tous_les_mots)

print("\nMots les plus fréquents :")
for mot, freq in itertools.islice(compteur.most_common(), 5):
    print(f"  {mot:15s} : {freq} fois")

print(f"\nStatistiques :")
print(f"  Nombre total de mots : {len(tous_les_mots)}")
print(f"  Mots uniques : {len(compteur)}")
print(f"  Hapax (1 seule fois) : {sum(1 for f in compteur.values() if f == 1)}")
