# ============================================================================
#   Section 13.2.2 : Nettoyage et transformation de donnees
#   Description : Valeurs manquantes (detection, suppression, remplissage,
#                 interpolation), doublons, types, chaines, dates, renommage,
#                 apply/map/replace, pivot/melt, concat/merge, exemples pratiques
#   Fichier source : 02.2-nettoyage-transformation.md
# ============================================================================

"""Nettoyage et transformation de donnees avec Pandas."""

import pandas as pd
import numpy as np


# ============================================================
# VALEURS MANQUANTES
# ============================================================
print("=" * 50)
print("VALEURS MANQUANTES")
print("=" * 50)

# --- Detection ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 28, np.nan],
    'Ville': ['Paris', 'Lyon', None, 'Toulouse', 'Paris'],
    'Salaire': [35000, 42000, np.nan, 38000, 32000],
    'Email': ['alice@mail.com', None, 'charlie@mail.com', 'david@mail.com', None]
})

print(f"\n  DataFrame avec valeurs manquantes:\n{df}")
print(f"\n  Nombre de NaN par colonne:\n{df.isnull().sum()}")
print(f"\n  Pourcentage de NaN:\n{(df.isnull().sum() / len(df) * 100).round(2)}")
print(f"  Total de valeurs manquantes: {df.isnull().sum().sum()}")
print(f"  Lignes avec NaN: {len(df[df.isnull().any(axis=1)])}")

# --- Suppression ---
print(f"\n  --- Suppression ---")
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})
print(f"  Original:\n{df}")
print(f"\n  dropna():\n{df.dropna()}")
print(f"\n  dropna(subset=['A']):\n{df.dropna(subset=['A'])}")
print(f"\n  dropna(thresh=2):\n{df.dropna(thresh=2)}")

# --- Suppression colonnes ---
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [np.nan, np.nan, np.nan, np.nan],
    'C': [5, 6, np.nan, 8]
})
print(f"\n  dropna(axis=1, how='all'):\n{df.dropna(axis=1, how='all')}")

# --- Remplissage ---
print(f"\n  --- Remplissage ---")
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, np.nan, 35],
    'Ville': ['Paris', None, 'Lyon'],
    'Score': [85, 90, np.nan]
})
print(f"  Original:\n{df}")
print(f"\n  fillna(0):\n{df.fillna(0)}")
print(f"\n  fillna specifique:\n{df.fillna({'Age': 30, 'Ville': 'Inconnu', 'Score': 0})}")

# --- Remplissage statistiques ---
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [10, np.nan, 30, 40, np.nan, 60, 70]
})
print(f"\n  fillna(mean):\n{df.fillna(df.mean())}")
print(f"\n  fillna(median):\n{df.fillna(df.median())}")

# --- Propagation ---
print(f"\n  --- Propagation ---")
df = pd.DataFrame({'Valeur': [1, np.nan, np.nan, 4, np.nan, 6]})
print(f"  Original:\n{df}")
print(f"\n  ffill:\n{df.ffill()}")
print(f"\n  bfill:\n{df.bfill()}")
print(f"\n  ffill(limit=1):\n{df.ffill(limit=1)}")

# --- Interpolation ---
print(f"\n  --- Interpolation ---")
print(f"  Interpolation lineaire:\n{df.interpolate()}")

# --- Remplacement valeurs invalides ---
print(f"\n  --- Remplacement ---")
df = pd.DataFrame({
    'Age': [25, -1, 35, 999, 28],
    'Ville': ['Paris', 'N/A', 'Lyon', 'Inconnu', 'Marseille'],
    'Score': [85, 0, 90, -999, 78]
})
print(f"  Original:\n{df}")
print(f"\n  replace([-1, 999, -999], NaN):\n{df.replace([-1, 999, -999], np.nan)}")

df_clean = df.replace({
    'Ville': {'N/A': np.nan, 'Inconnu': np.nan},
    'Score': {0: np.nan, -999: np.nan}
})
print(f"\n  Remplacements par colonne:\n{df_clean}")


# ============================================================
# DOUBLONS
# ============================================================
print(f"\n{'=' * 50}")
print("DOUBLONS")
print("=" * 50)

df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [25, 30, 25, 35, 30],
    'Ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon']
})

print(f"\n  DataFrame:\n{df}")
print(f"\n  duplicated():\n{df.duplicated()}")
print(f"\n  Lignes doublons:\n{df[df.duplicated()]}")
print(f"\n  drop_duplicates():\n{df.drop_duplicates()}")
print(f"\n  drop_duplicates(subset=['Nom']):\n{df.drop_duplicates(subset=['Nom'])}")


# ============================================================
# TYPES DE DONNEES
# ============================================================
print(f"\n{'=' * 50}")
print("TYPES DE DONNEES")
print("=" * 50)

df = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['1.5', '2.5', '3.5', '4.5'],
    'C': ['True', 'False', 'True', 'False']
})
print(f"\n  Types originaux:\n{df.dtypes}")

df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
df['C'] = df['C'].map({'True': True, 'False': False})
print(f"\n  Types apres conversion:\n{df.dtypes}")
print(f"\n  DataFrame:\n{df}")

# --- to_numeric ---
df2 = pd.DataFrame({'Valeur': ['1', '2', '3', 'quatre', '5']})
df2['Valeur_num'] = pd.to_numeric(df2['Valeur'], errors='coerce')
print(f"\n  to_numeric avec erreurs:\n{df2}")

# --- Categories ---
df_cat = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon', 'Paris'] * 1000
})
mem_before = df_cat.memory_usage(deep=True).sum()
df_cat['Ville'] = df_cat['Ville'].astype('category')
mem_after = df_cat.memory_usage(deep=True).sum()
print(f"\n  Memoire object: {mem_before} bytes")
print(f"  Memoire category: {mem_after} bytes")
print(f"  Categories: {df_cat['Ville'].cat.categories.tolist()}")


# ============================================================
# CHAINES DE CARACTERES
# ============================================================
print(f"\n{'=' * 50}")
print("CHAINES DE CARACTERES")
print("=" * 50)

df = pd.DataFrame({
    'Nom': ['alice', 'BOB', 'Charlie', 'DAVID'],
    'Email': ['alice@mail.com', 'bob@MAIL.com', 'charlie@mail.COM', 'david@mail.com']
})
print(f"\n  Original:\n{df}")
print(f"\n  upper(): {df['Nom'].str.upper().tolist()}")
print(f"  lower(): {df['Email'].str.lower().tolist()}")
print(f"  capitalize(): {df['Nom'].str.capitalize().tolist()}")
print(f"  title(): {df['Nom'].str.title().tolist()}")

# --- Nettoyage ---
df2 = pd.DataFrame({'Texte': ['  Alice  ', 'Bob\n', '\tCharlie', '  David\n  ']})
print(f"\n  strip(): {df2['Texte'].str.strip().tolist()}")

# --- Recherche ---
df3 = pd.DataFrame({
    'Texte': ['Bonjour le monde', 'Python est genial', 'Pandas pour tous', 'Bonjour Python']
})
df3['Contient_Python'] = df3['Texte'].str.contains('Python')
print(f"\n  contains('Python'):\n{df3[['Texte', 'Contient_Python']]}")

df3['Remplace'] = df3['Texte'].str.replace('Python', 'Java')
print(f"\n  replace Python->Java:\n{df3[['Texte', 'Remplace']]}")

# --- Extraction ---
df4 = pd.DataFrame({
    'Email': ['alice@gmail.com', 'bob@yahoo.fr', 'charlie@hotmail.com']
})
df4['Utilisateur'] = df4['Email'].str.split('@').str[0]
df4['Domaine'] = df4['Email'].str.split('@').str[1]
print(f"\n  Extraction email:\n{df4}")

# --- Longueur ---
df5 = pd.DataFrame({'Texte': ['Bonjour', 'Python est super', 'Pandas', 'Data Science']})
df5['Longueur'] = df5['Texte'].str.len()
df5['Nombre_e'] = df5['Texte'].str.count('e')
print(f"\n  Longueur et comptage:\n{df5}")


# ============================================================
# DATES
# ============================================================
print(f"\n{'=' * 50}")
print("DATES")
print("=" * 50)

# --- Conversion ---
df = pd.DataFrame({
    'Date_str': ['2024-01-01', '2024-02-15', '2024-03-30']
})
df['Date'] = pd.to_datetime(df['Date_str'])
print(f"\n  Conversion datetime:\n{df}")
print(f"  Types:\n{df.dtypes}")

# --- Formats ---
dates_eur = pd.Series(['15/01/2024', '20/02/2024', '10/03/2024'])
print(f"\n  Dates europeennes:\n{pd.to_datetime(dates_eur, format='%d/%m/%Y')}")

# --- Extraction composants ---
df = pd.DataFrame({
    'Date': pd.to_datetime(['2024-01-15', '2024-06-20', '2024-12-25'])
})
df['Annee'] = df['Date'].dt.year
df['Mois'] = df['Date'].dt.month
df['Nom_mois'] = df['Date'].dt.month_name()
df['Jour'] = df['Date'].dt.day
df['Jour_semaine'] = df['Date'].dt.dayofweek
df['Nom_jour'] = df['Date'].dt.day_name()
df['Trimestre'] = df['Date'].dt.quarter
print(f"\n  Composants extraits:\n{df}")

# --- Calculs ---
df = pd.DataFrame({
    'Date_debut': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01']),
    'Date_fin': pd.to_datetime(['2024-01-15', '2024-02-29', '2024-03-31'])
})
df['Duree_jours'] = (df['Date_fin'] - df['Date_debut']).dt.days
df['Dans_10_jours'] = df['Date_debut'] + pd.Timedelta(days=10)
print(f"\n  Calculs de dates:\n{df}")


# ============================================================
# RENOMMAGE ET REORGANISATION
# ============================================================
print(f"\n{'=' * 50}")
print("RENOMMAGE ET REORGANISATION")
print("=" * 50)

df = pd.DataFrame({
    'nom_client': ['Alice', 'Bob', 'Charlie'],
    'age_client': [25, 30, 35],
    'ville_client': ['Paris', 'Lyon', 'Marseille']
})

df_renomme = df.rename(columns={
    'nom_client': 'Nom', 'age_client': 'Age', 'ville_client': 'Ville'
})
print(f"\n  Colonnes renommees:\n{df_renomme}")

df_upper = df.rename(columns=str.upper)
print(f"\n  Colonnes en majuscules:\n{df_upper}")

# --- Reorganisation colonnes ---
df = pd.DataFrame({'D': [1, 2, 3], 'A': [4, 5, 6], 'C': [7, 8, 9], 'B': [10, 11, 12]})
print(f"\n  Reordonne [A,B,C,D]:\n{df[['A', 'B', 'C', 'D']]}")

# --- Index ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
}, index=['A', 'B', 'C'])

print(f"\n  reset_index():\n{df.reset_index()}")
print(f"\n  set_index('Nom'):\n{df.reset_index().set_index('Nom')}")


# ============================================================
# APPLY, MAP, REPLACE
# ============================================================
print(f"\n{'=' * 50}")
print("APPLY, MAP, REPLACE")
print("=" * 50)

# --- apply ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salaire': [35000, 42000, 48000]
})

def categoriser_age(age):
    if age < 30:
        return 'Jeune'
    elif age < 40:
        return 'Adulte'
    else:
        return 'Senior'

df['Categorie'] = df['Age'].apply(categoriser_age)
df['Salaire_mensuel'] = df['Salaire'].apply(lambda x: round(x / 12, 2))
df['Ratio'] = df.apply(lambda row: round(row['Salaire'] / row['Age'], 2), axis=1)
print(f"\n  apply():\n{df}")

# --- map ---
df2 = pd.DataFrame({'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon']})
code_postal = {'Paris': 75000, 'Lyon': 69000, 'Marseille': 13000}
df2['Code_postal'] = df2['Ville'].map(code_postal)
print(f"\n  map():\n{df2}")

# --- replace ---
df3 = pd.DataFrame({
    'Note': ['A', 'B', 'C', 'A', 'D'],
    'Statut': ['Actif', 'Inactif', 'Actif', 'Suspendu', 'Actif']
})
df3_remplace = df3.replace({
    'Note': {'A': 20, 'B': 15, 'C': 10, 'D': 5},
    'Statut': {'Actif': 1, 'Inactif': 0, 'Suspendu': -1}
})
print(f"\n  replace():\n{df3_remplace}")


# ============================================================
# PIVOT ET MELT
# ============================================================
print(f"\n{'=' * 50}")
print("PIVOT ET MELT")
print("=" * 50)

# --- pivot ---
df = pd.DataFrame({
    'Date': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'Produit': ['A', 'B', 'A', 'B'],
    'Ventes': [100, 150, 120, 180]
})
print(f"\n  Original:\n{df}")
print(f"\n  pivot():\n{df.pivot(index='Date', columns='Produit', values='Ventes')}")

# --- pivot_table ---
df = pd.DataFrame({
    'Date': ['2024-01', '2024-01', '2024-01', '2024-02', '2024-02', '2024-02'],
    'Produit': ['A', 'A', 'B', 'A', 'B', 'B'],
    'Ventes': [100, 110, 150, 120, 180, 190]
})
pivot = pd.pivot_table(df, values='Ventes', index='Date', columns='Produit',
                       aggfunc='sum', margins=True, margins_name='Total')
print(f"\n  pivot_table avec totaux:\n{pivot}")

# --- melt ---
df = pd.DataFrame({
    'Produit': ['A', 'B'],
    'Jan': [100, 150],
    'Fev': [120, 180],
    'Mar': [110, 170]
})
print(f"\n  Format large:\n{df}")
df_long = df.melt(id_vars=['Produit'], var_name='Mois', value_name='Ventes')
print(f"\n  Format long (melt):\n{df_long}")

# --- stack/unstack ---
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])
print(f"\n  stack():\n{df.stack()}")


# ============================================================
# CONCAT ET MERGE
# ============================================================
print(f"\n{'=' * 50}")
print("CONCAT ET MERGE")
print("=" * 50)

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
df3 = pd.DataFrame({'C': [13, 14, 15], 'D': [16, 17, 18]})

print(f"\n  concat vertical:\n{pd.concat([df1, df2], ignore_index=True)}")
print(f"\n  concat horizontal:\n{pd.concat([df1, df3], axis=1)}")

# --- merge ---
employes = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Dept_ID': [101, 102, 101, 103, 999]
})
departements = pd.DataFrame({
    'Dept_ID': [101, 102, 103],
    'Departement': ['Ventes', 'IT', 'RH']
})

print(f"\n  merge inner:\n{pd.merge(employes, departements, on='Dept_ID')}")
print(f"\n  merge left:\n{pd.merge(employes, departements, on='Dept_ID', how='left')}")
print(f"\n  merge outer:\n{pd.merge(employes, departements, on='Dept_ID', how='outer')}")


# ============================================================
# EXEMPLES PRATIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLES PRATIQUES")
print("=" * 50)

# --- Nettoyage ventes ---
print(f"\n  --- Nettoyage dataset ventes ---")
df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', None, '2024-01-04', '2024-01-05'],
    'Produit': ['Laptop', 'Souris', 'Clavier', 'Laptop', 'Souris'],
    'Quantite': [2, None, 5, 1, 8],
    'Prix': [800, 25, 60, 800, None],
    'Client': ['  Alice  ', 'BOB', 'Charlie', 'Alice', '  bob  ']
})
print(f"  Original:\n{df}")

df['Client'] = df['Client'].str.strip().str.title()
df['Date'] = pd.to_datetime(df['Date'])
df['Quantite'] = df['Quantite'].fillna(df['Quantite'].median())
df['Prix'] = df['Prix'].ffill()
df.dropna(subset=['Date'], inplace=True)
df['Montant'] = df['Quantite'] * df['Prix']
df = df[['Date', 'Client', 'Produit', 'Quantite', 'Prix', 'Montant']]

print(f"\n  Nettoye:\n{df}")
print(f"\n  Total des ventes: {df['Montant'].sum():.2f} EUR")
print(f"\n  Ventes par client:\n{df.groupby('Client')['Montant'].sum()}")

# --- Combinaison sources ---
print(f"\n  --- Combinaison de sources ---")
ventes_jan = pd.DataFrame({
    'Produit': ['A', 'B', 'C'],
    'Ventes': [100, 150, 200],
    'Mois': ['Jan', 'Jan', 'Jan']
})
ventes_fev = pd.DataFrame({
    'Produit': ['A', 'B', 'C'],
    'Ventes': [120, 140, 210],
    'Mois': ['Fev', 'Fev', 'Fev']
})
produits = pd.DataFrame({
    'Produit': ['A', 'B', 'C'],
    'Nom': ['Laptop', 'Souris', 'Clavier'],
    'Categorie': ['Ordinateur', 'Accessoire', 'Accessoire'],
    'Prix': [800, 25, 60]
})

ventes_total = pd.concat([ventes_jan, ventes_fev], ignore_index=True)
ventes_complet = pd.merge(ventes_total, produits, on='Produit')
ventes_complet['CA'] = ventes_complet['Ventes'] * ventes_complet['Prix']
print(f"  Ventes avec CA:\n{ventes_complet}")

analyse = ventes_complet.groupby(['Categorie', 'Mois'])['CA'].sum().unstack()
print(f"\n  CA par categorie et mois:\n{analyse}")
