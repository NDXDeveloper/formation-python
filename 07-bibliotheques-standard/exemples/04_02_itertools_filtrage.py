# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Itérateurs de filtrage - chain, compress, dropwhile,
#                 takewhile, filterfalse, islice, groupby
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

import itertools

# --- chain() ---
print("=== chain() ===")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [7, 8, 9]

chaine = itertools.chain(liste1, liste2, liste3)
print(f"chain : {list(chaine)}")

resultat = itertools.chain([1, 2], "abc", (7, 8))
print(f"types mixtes : {list(resultat)}")

listes = [[1, 2], [3, 4], [5, 6]]
chaine = itertools.chain.from_iterable(listes)
print(f"from_iterable : {list(chaine)}")

# --- compress() ---
print("\n=== compress() ===")

donnees = ['A', 'B', 'C', 'D', 'E']
selecteur = [1, 0, 1, 0, 1]
resultat = itertools.compress(donnees, selecteur)
print(f"compress : {list(resultat)}")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
est_pair = [n % 2 == 0 for n in nombres]
pairs = itertools.compress(nombres, est_pair)
print(f"pairs : {list(pairs)}")

# --- dropwhile() et takewhile() ---
print("\n=== dropwhile() et takewhile() ===")

nombres = [1, 3, 5, 7, 10, 12, 14, 2, 4]

resultat = itertools.dropwhile(lambda x: x < 10, nombres)
print(f"dropwhile(< 10) : {list(resultat)}")

resultat = itertools.takewhile(lambda x: x < 10, nombres)
print(f"takewhile(< 10) : {list(resultat)}")

# --- filterfalse() ---
print("\n=== filterfalse() ===")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"filter (pairs) : {pairs}")

impairs = list(itertools.filterfalse(lambda x: x % 2 == 0, nombres))
print(f"filterfalse (impairs) : {impairs}")

# --- islice() ---
print("\n=== islice() ===")

nombres = range(10)
print(f"islice(0, 5) : {list(itertools.islice(nombres, 5))}")
print(f"islice(2, 7) : {list(itertools.islice(nombres, 2, 7))}")
print(f"islice(0, 10, 2) : {list(itertools.islice(nombres, 0, 10, 2))}")

compteur = itertools.count(1)
premiers = itertools.islice(compteur, 5)
print(f"5 premiers de count(1) : {list(premiers)}")

# --- groupby() ---
print("\n=== groupby() ===")

donnees = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'A']
for cle, groupe in itertools.groupby(donnees):
    print(f"  {cle}: {list(groupe)}")

# Avec fonction de clé
print("\nGrouper par âge :")
personnes = [
    {'nom': 'Alice', 'age': 25},
    {'nom': 'Bob', 'age': 25},
    {'nom': 'Charlie', 'age': 30},
    {'nom': 'David', 'age': 30},
    {'nom': 'Emma', 'age': 25}
]

personnes_triees = sorted(personnes, key=lambda p: p['age'])
for age, groupe in itertools.groupby(personnes_triees, key=lambda p: p['age']):
    liste_p = list(groupe)
    print(f"  Age {age}: {[p['nom'] for p in liste_p]}")

# --- Analyse de logs ---
print("\n=== Analyse de logs (groupby) ===")

def get_niveau(ligne):
    if 'ERROR' in ligne:
        return 'ERROR'
    elif 'WARNING' in ligne:
        return 'WARNING'
    return 'INFO'

logs = [
    "[10:00] INFO: Application démarrée",
    "[10:01] ERROR: Connexion échouée",
    "[10:02] WARNING: Mémoire faible",
    "[10:03] INFO: Utilisateur connecté",
    "[10:04] ERROR: Fichier introuvable",
    "[10:05] INFO: Traitement terminé"
]

lignes_triees = sorted(logs, key=get_niveau)
for niveau, groupe in itertools.groupby(lignes_triees, key=get_niveau):
    liste_logs = list(groupe)
    print(f"\n{niveau} ({len(liste_logs)} entrées):")
    for log in liste_logs:
        print(f"  - {log}")
