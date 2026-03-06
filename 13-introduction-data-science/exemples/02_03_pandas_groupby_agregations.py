# ============================================================================
#   Section 13.2.3 : GroupBy et agregations
#   Description : Split-Apply-Combine, groupby de base, fonctions d'agregation,
#                 agg() multiples, groupby multiples, transform, filter, apply,
#                 MultiIndex, valeurs manquantes, bins, rolling, exemples pratiques
#   Fichier source : 02.3-groupby-et-agregations.md
# ============================================================================

"""GroupBy et agregations avec Pandas."""

import pandas as pd
import numpy as np


# ============================================================
# GROUPBY DE BASE
# ============================================================
print("=" * 50)
print("GROUPBY DE BASE")
print("=" * 50)

df = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Marseille', 'Paris'],
    'Produit': ['A', 'A', 'B', 'B', 'A', 'A'],
    'Ventes': [100, 150, 120, 180, 90, 110],
    'Quantite': [5, 8, 6, 9, 4, 5]
})

print(f"\n  DataFrame:\n{df}")

ventes_par_ville = df.groupby('Ville')['Ventes'].sum()
print(f"\n  Ventes totales par ville:\n{ventes_par_ville}")

# --- Objet GroupBy ---
groupe = df.groupby('Ville')
print(f"\n  Nombre de groupes: {groupe.ngroups}")
print(f"  Noms des groupes: {list(groupe.groups.keys())}")

print(f"\n  Contenu des groupes:")
for nom, groupe_df in groupe:
    print(f"  --- {nom} ---")
    print(f"{groupe_df}")

groupe_paris = df.groupby('Ville').get_group('Paris')
print(f"\n  Groupe Paris:\n{groupe_paris}")


# ============================================================
# FONCTIONS D'AGREGATION
# ============================================================
print(f"\n{'=' * 50}")
print("FONCTIONS D'AGREGATION")
print("=" * 50)

df = pd.DataFrame({
    'Categorie': ['A', 'B', 'A', 'B', 'A'],
    'Ventes': [100, 150, 120, 180, 90],
    'Quantite': [5, 8, 6, 9, 4]
})

print(f"\n  Somme par categorie:\n{df.groupby('Categorie')['Ventes'].sum()}")
print(f"\n  Moyenne par categorie:\n{df.groupby('Categorie')['Ventes'].mean()}")
print(f"\n  Count par categorie:\n{df.groupby('Categorie')['Ventes'].count()}")
print(f"\n  Min par categorie:\n{df.groupby('Categorie')['Ventes'].min()}")
print(f"\n  Max par categorie:\n{df.groupby('Categorie')['Ventes'].max()}")
print(f"\n  Mediane par categorie:\n{df.groupby('Categorie')['Ventes'].median()}")


# ============================================================
# AGREGATIONS MULTIPLES AVEC AGG()
# ============================================================
print(f"\n{'=' * 50}")
print("AGREGATIONS MULTIPLES")
print("=" * 50)

df = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Marseille'],
    'Produit': ['A', 'A', 'B', 'B', 'A'],
    'Ventes': [100, 150, 120, 180, 90],
    'Quantite': [5, 8, 6, 9, 4]
})

# --- Plusieurs fonctions sur une colonne ---
stats = df.groupby('Ville')['Ventes'].agg(['sum', 'mean', 'min', 'max', 'count'])
print(f"\n  Statistiques ventes par ville:\n{stats}")

# --- Fonctions differentes par colonne ---
resultat = df.groupby('Ville').agg({
    'Ventes': ['sum', 'mean'],
    'Quantite': ['sum', 'max']
})
print(f"\n  Agregations personnalisees:\n{resultat}")

# --- Noms personnalises ---
resultat = df.groupby('Ville').agg(
    Ventes_totales=('Ventes', 'sum'),
    Ventes_moyennes=('Ventes', 'mean'),
    Quantite_totale=('Quantite', 'sum'),
    Quantite_max=('Quantite', 'max')
)
print(f"\n  Avec noms personnalises:\n{resultat}")

# --- Fonctions personnalisees ---
def etendue(serie):
    return serie.max() - serie.min()

resultat = df.groupby('Ville')['Ventes'].agg(['mean', etendue])
print(f"\n  Avec fonction personnalisee:\n{resultat}")


# ============================================================
# GROUPBY MULTIPLES
# ============================================================
print(f"\n{'=' * 50}")
print("GROUPBY MULTIPLES")
print("=" * 50)

df = pd.DataFrame({
    'Region': ['Nord', 'Nord', 'Sud', 'Sud', 'Nord', 'Sud'],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Paris', 'Marseille'],
    'Produit': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Ventes': [100, 150, 90, 120, 110, 130]
})

print(f"\n  DataFrame:\n{df}")

ventes_rv = df.groupby(['Region', 'Ville'])['Ventes'].sum()
print(f"\n  Ventes par Region et Ville:\n{ventes_rv}")

ventes_df = df.groupby(['Region', 'Ville'])['Ventes'].sum().reset_index()
print(f"\n  Avec index reinitialise:\n{ventes_df}")

ventes_triees = (df.groupby(['Region', 'Ville'])['Ventes']
                   .sum()
                   .sort_values(ascending=False)
                   .reset_index())
print(f"\n  Trie par ventes decroissantes:\n{ventes_triees}")


# ============================================================
# TRANSFORM
# ============================================================
print(f"\n{'=' * 50}")
print("TRANSFORM")
print("=" * 50)

df = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Paris'],
    'Ventes': [100, 150, 120, 180, 90]
})

print(f"\n  DataFrame:\n{df}")

df['Moyenne_ville'] = df.groupby('Ville')['Ventes'].transform('mean')
print(f"\n  Avec moyenne par ville:\n{df}")

df['Rang_dans_ville'] = df.groupby('Ville')['Ventes'].transform(lambda x: x.rank(method='dense'))
print(f"\n  Avec rang dans ville:\n{df}")


# ============================================================
# FILTER
# ============================================================
print(f"\n{'=' * 50}")
print("FILTER")
print("=" * 50)

df = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Marseille', 'Paris'],
    'Ventes': [100, 150, 120, 180, 50, 90]
})

print(f"\n  DataFrame:\n{df}")

villes_importantes = df.groupby('Ville').filter(lambda x: x['Ventes'].sum() > 200)
print(f"\n  Villes avec ventes totales > 200:\n{villes_importantes}")

villes_frequentes = df.groupby('Ville').filter(lambda x: len(x) >= 3)
print(f"\n  Villes avec au moins 3 entrees:\n{villes_frequentes}")


# ============================================================
# APPLY
# ============================================================
print(f"\n{'=' * 50}")
print("APPLY")
print("=" * 50)

df = pd.DataFrame({
    'Categorie': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Valeur': [10, 15, 20, 25, 12, 22]
})

print(f"\n  DataFrame:\n{df}")

def stats_groupe(groupe):
    return pd.Series({
        'min': groupe['Valeur'].min(),
        'max': groupe['Valeur'].max(),
        'etendue': groupe['Valeur'].max() - groupe['Valeur'].min()
    })

stats = df.groupby('Categorie').apply(stats_groupe)
print(f"\n  Statistiques par categorie:\n{stats}")


# ============================================================
# VALEURS MANQUANTES
# ============================================================
print(f"\n{'=' * 50}")
print("VALEURS MANQUANTES")
print("=" * 50)

df = pd.DataFrame({
    'Categorie': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Valeur': [10, np.nan, 20, 25, 15, np.nan]
})

print(f"\n  DataFrame avec NaN:\n{df}")
print(f"\n  Moyenne (ignore NaN):\n{df.groupby('Categorie')['Valeur'].mean()}")
print(f"\n  Count (sans NaN):\n{df.groupby('Categorie')['Valeur'].count()}")
print(f"\n  Size (avec NaN):\n{df.groupby('Categorie')['Valeur'].size()}")
print(f"\n  Somme:\n{df.groupby('Categorie')['Valeur'].sum()}")


# ============================================================
# MULTIINDEX ET INDEX
# ============================================================
print(f"\n{'=' * 50}")
print("MULTIINDEX ET DATES")
print("=" * 50)

# --- MultiIndex ---
arrays = [['A', 'A', 'B', 'B'], ['X', 'Y', 'X', 'Y']]
index = pd.MultiIndex.from_arrays(arrays, names=['Groupe', 'Sous_groupe'])
df = pd.DataFrame({'Valeur': [10, 20, 30, 40]}, index=index)

print(f"\n  DataFrame MultiIndex:\n{df}")
print(f"\n  Somme par Groupe:\n{df.groupby(level='Groupe')['Valeur'].sum()}")
print(f"\n  Somme par Sous_groupe:\n{df.groupby(level='Sous_groupe')['Valeur'].sum()}")

# --- Grouper par date ---
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Ventes': [100, 120, 90, 110, 130, 95, 105, 115, 125, 100]
})
df.set_index('Date', inplace=True)

print(f"\n  Ventes par jour de la semaine:\n{df.groupby(df.index.dayofweek)['Ventes'].mean()}")


# ============================================================
# TECHNIQUES AVANCEES
# ============================================================
print(f"\n{'=' * 50}")
print("TECHNIQUES AVANCEES")
print("=" * 50)

# --- Bins ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [23, 35, 28, 45, 31, 52],
    'Salaire': [35000, 45000, 40000, 55000, 42000, 60000]
})

df['Tranche_age'] = pd.cut(df['Age'], bins=[20, 30, 40, 60], labels=['20-30', '30-40', '40-60'])
print(f"\n  Avec tranches d'age:\n{df}")
print(f"\n  Salaire moyen par tranche:\n{df.groupby('Tranche_age', observed=True)['Salaire'].mean()}")

# --- Rolling par groupe ---
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=10),
    'Ville': ['Paris', 'Lyon'] * 5,
    'Ventes': [100, 120, 110, 130, 105, 125, 115, 135, 120, 140]
})

df = df.sort_values(['Ville', 'Date'])
df['Moyenne_mobile'] = df.groupby('Ville')['Ventes'].transform(
    lambda x: x.rolling(3, min_periods=1).mean()
)
print(f"\n  Avec moyenne mobile par ville:\n{df}")


# ============================================================
# EXEMPLES PRATIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLES PRATIQUES")
print("=" * 50)

# --- Analyse ventes par region ---
print(f"\n  --- Analyse ventes par region ---")
ventes = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=12, freq='MS'),
    'Region': ['Nord', 'Sud', 'Est', 'Ouest'] * 3,
    'Produit': ['A', 'A', 'B', 'B'] * 3,
    'Ventes': [1000, 1200, 800, 900, 1100, 1300, 850, 950, 1050, 1250, 900, 1000],
    'Quantite': [50, 60, 40, 45, 55, 65, 42, 48, 52, 62, 45, 50]
})

ventes_region = ventes.groupby('Region')['Ventes'].sum().sort_values(ascending=False)
print(f"  Ventes par region:\n{ventes_region}")

perf = ventes.groupby(['Region', 'Produit']).agg(
    Ventes_totales=('Ventes', 'sum'),
    Ventes_moyennes=('Ventes', 'mean')
).reset_index()
print(f"\n  Performance par region et produit:\n{perf}")

total_ventes = ventes['Ventes'].sum()
pct = (ventes.groupby('Region')['Ventes'].sum() / total_ventes * 100).round(2)
print(f"\n  Pourcentage par region:\n{pct}")

# --- Notes etudiants ---
print(f"\n  --- Notes etudiants ---")
notes = pd.DataFrame({
    'Etudiant': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'] * 2,
    'Matiere': ['Math', 'Math', 'Math', 'Physique', 'Physique', 'Physique'] * 2,
    'Trimestre': ['T1'] * 6 + ['T2'] * 6,
    'Note': [15, 12, 18, 13, 14, 16, 16, 13, 17, 14, 15, 18]
})

moy_etudiant = notes.groupby('Etudiant')['Note'].mean().round(2)
print(f"  Moyenne par etudiant:\n{moy_etudiant}")

classement = (notes.groupby('Etudiant')['Note']
              .mean()
              .sort_values(ascending=False)
              .reset_index()
              .rename(columns={'Note': 'Moyenne'}))
classement['Rang'] = range(1, len(classement) + 1)
print(f"\n  Classement:\n{classement}")

notes_pivot = notes.pivot_table(values='Note', index='Etudiant',
                                 columns='Trimestre', aggfunc='mean')
notes_pivot['Progression'] = notes_pivot['T2'] - notes_pivot['T1']
print(f"\n  Progression T1 -> T2:\n{notes_pivot}")

# --- Analyse RH ---
print(f"\n  --- Analyse RH ---")
employes = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Departement': ['IT', 'Ventes', 'IT', 'RH', 'Ventes', 'IT', 'RH', 'Ventes'],
    'Poste': ['Dev', 'Manager', 'Dev', 'Recrut', 'Vendeur', 'Manager', 'Recrut', 'Vendeur'],
    'Salaire': [45000, 55000, 48000, 40000, 38000, 65000, 42000, 40000],
    'Anciennete': [2, 5, 3, 4, 1, 8, 6, 2]
})

sal_dept = employes.groupby('Departement')['Salaire'].mean().round(2)
print(f"  Salaire moyen par departement:\n{sal_dept}")

masse_sal = employes.groupby('Departement').agg(
    Masse_salariale=('Salaire', 'sum'),
    Effectif=('Nom', 'count')
)
masse_sal['Salaire_moyen'] = (masse_sal['Masse_salariale'] / masse_sal['Effectif']).round(2)
print(f"\n  Masse salariale:\n{masse_sal}")

employes['Sal_moy_dept'] = employes.groupby('Departement')['Salaire'].transform('mean')
employes['Au_dessus_moy'] = employes['Salaire'] > employes['Sal_moy_dept']
print(f"\n  Employes au-dessus de la moyenne:\n{employes[['Nom', 'Departement', 'Salaire', 'Au_dessus_moy']]}")
