# ============================================================================
#   Section 13.2 / 13.2.1 : Manipulation de donnees avec Pandas / DataFrames et Series
#   Description : Series (creation, acces, proprietes, operations, filtrage),
#                 DataFrames (creation, proprietes, acces loc/iloc, ajout/modif,
#                 filtrage, tri, valeurs manquantes, groupby), exemples pratiques
#   Fichier source : 02-manipulation-donnees-pandas.md, 02.1-dataframes-et-series.md
# ============================================================================

"""DataFrames et Series avec Pandas."""

import pandas as pd
import numpy as np


# ============================================================
# SERIES
# ============================================================
print("=" * 50)
print("SERIES")
print("=" * 50)

# --- Creation ---
print("\n  --- Creation ---")
temperatures = pd.Series([15, 18, 22, 20, 17])
print(f"  Series simple:\n{temperatures}")

temperatures = pd.Series([15, 18, 22, 20, 17],
                         index=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'])
print(f"\n  Avec index:\n{temperatures}")

villes_population = pd.Series({
    'Paris': 2_161_000,
    'Marseille': 869_000,
    'Lyon': 516_000,
    'Toulouse': 475_000
})
print(f"\n  Depuis dictionnaire:\n{villes_population}")

arr = np.array([10, 20, 30, 40, 50])
serie = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e'])
print(f"\n  Depuis NumPy:\n{serie}")

serie_constante = pd.Series(100, index=['a', 'b', 'c', 'd'])
print(f"\n  Series constante:\n{serie_constante}")

# --- Acces ---
print(f"\n  --- Acces ---")
temperatures = pd.Series([15, 18, 22, 20, 17],
                         index=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'])

print(f"  Premier element: {temperatures.iloc[0]}")
print(f"  Temperature mardi: {temperatures['Mardi']}")
print(f"  Lundi et Vendredi:\n{temperatures[['Lundi', 'Vendredi']]}")
print(f"  Lundi a Mercredi:\n{temperatures['Lundi':'Mercredi']}")

# --- Proprietes ---
print(f"\n  --- Proprietes ---")
print(f"  Valeurs: {temperatures.values}")
print(f"  Index: {temperatures.index.tolist()}")
print(f"  Type: {temperatures.dtype}")
print(f"  Taille: {temperatures.size}")
print(f"  Forme: {temperatures.shape}")

# --- Operations ---
print(f"\n  --- Operations arithmetiques ---")
print(f"  Temperatures + 5:\n{temperatures + 5}")
print(f"  En Fahrenheit:\n{temperatures * 9/5 + 32}")

ventes_janvier = pd.Series([100, 150, 200], index=['Produit A', 'Produit B', 'Produit C'])
ventes_fevrier = pd.Series([120, 140, 210], index=['Produit A', 'Produit B', 'Produit C'])

ventes_totales = ventes_janvier + ventes_fevrier
print(f"\n  Ventes totales:\n{ventes_totales}")

evolution = ventes_fevrier - ventes_janvier
print(f"  Evolution:\n{evolution}")

# --- Statistiques ---
print(f"\n  --- Statistiques ---")
temperatures = pd.Series([15, 18, 22, 20, 17, 19, 21])
print(f"  Moyenne: {temperatures.mean():.6f}")
print(f"  Mediane: {temperatures.median()}")
print(f"  Ecart-type: {temperatures.std():.6f}")
print(f"  Minimum: {temperatures.min()}")
print(f"  Maximum: {temperatures.max()}")
print(f"  Somme: {temperatures.sum()}")
print(f"\n  describe():\n{temperatures.describe()}")

# --- Filtrage ---
print(f"\n  --- Filtrage ---")
temperatures = pd.Series([15, 18, 22, 20, 17],
                         index=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'])

jours_chauds = temperatures[temperatures > 18]
print(f"  Jours chauds (>18 C):\n{jours_chauds}")

jours_doux = temperatures[(temperatures >= 17) & (temperatures <= 20)]
print(f"  Jours doux (17-20 C):\n{jours_doux}")


# ============================================================
# DATAFRAMES
# ============================================================
print(f"\n{'=' * 50}")
print("DATAFRAMES")
print("=" * 50)

# --- Creation ---
print("\n  --- Creation ---")
donnees = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse']
}
df = pd.DataFrame(donnees)
print(f"  Depuis dictionnaire:\n{df}")

etudiants = [
    {'nom': 'Alice', 'note': 15, 'matiere': 'Math'},
    {'nom': 'Bob', 'note': 12, 'matiere': 'Math'},
    {'nom': 'Alice', 'note': 18, 'matiere': 'Physique'}
]
df = pd.DataFrame(etudiants)
print(f"\n  Depuis liste de dicts:\n{df}")

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'], index=['Ligne1', 'Ligne2', 'Ligne3'])
print(f"\n  Depuis NumPy:\n{df}")

# --- Index personnalise ---
donnees = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
}
df = pd.DataFrame(donnees, index=['E001', 'E002', 'E003'])
print(f"\n  Avec index personnalise:\n{df}")

# --- Proprietes ---
print(f"\n  --- Proprietes ---")
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
    'Salaire': [35000, 42000, 48000, 38000]
})

print(f"  Shape: {df.shape}")
print(f"  Nombre de lignes: {len(df)}")
print(f"  Nombre de colonnes: {len(df.columns)}")
print(f"  Colonnes: {df.columns.tolist()}")
print(f"  Index: {df.index.tolist()}")
print(f"  Types:\n{df.dtypes}")
print(f"  Taille: {df.size}")


# ============================================================
# ACCES AUX DONNEES
# ============================================================
print(f"\n{'=' * 50}")
print("ACCES AUX DONNEES")
print("=" * 50)

# --- head / tail ---
df = pd.DataFrame({
    'Jour': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'Temperature': [15, 18, 22, 20, 17, 19, 21],
    'Pluie': [0, 0, 5, 2, 0, 0, 1]
})

print(f"\n  3 premieres lignes:\n{df.head(3)}")
print(f"\n  2 dernieres lignes:\n{df.tail(2)}")

# --- Acces colonnes ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
})

print(f"\n  Colonne Age:\n{df['Age']}")
print(f"\n  Nom et Ville:\n{df[['Nom', 'Ville']]}")

# --- loc / iloc ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
}, index=['E001', 'E002', 'E003'])

print(f"\n  Ligne E002:\n{df.loc['E002']}")
print(f"\n  Lignes E001 et E003:\n{df.loc[['E001', 'E003']]}")
print(f"\n  Premiere ligne (iloc):\n{df.iloc[0]}")
print(f"\n  Lignes 0 et 2 (iloc):\n{df.iloc[[0, 2]]}")

# --- Cellules specifiques ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
})
print(f"\n  Age de Bob (index 1): {df.loc[1, 'Age']}")
print(f"  Element [0, 2]: {df.iloc[0, 2]}")


# ============================================================
# AJOUT ET MODIFICATION
# ============================================================
print(f"\n{'=' * 50}")
print("AJOUT ET MODIFICATION")
print("=" * 50)

# --- Ajouter colonne ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df['Ville'] = ['Paris', 'Lyon', 'Marseille']
df['Age_dans_10_ans'] = df['Age'] + 10
df['Pays'] = 'France'
print(f"\n  Apres ajout colonnes:\n{df}")

# --- Modifier valeurs ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
})

df.loc[0, 'Age'] = 26
df['Age'] = df['Age'] + 1
df.loc[df['Nom'] == 'Bob', 'Ville'] = 'Nice'
print(f"\n  Apres modifications:\n{df}")

# --- Ajouter ligne ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Ville': ['Paris', 'Lyon']
})

nouvelle_ligne = pd.DataFrame({
    'Nom': ['Charlie'],
    'Age': [35],
    'Ville': ['Marseille']
})

df = pd.concat([df, nouvelle_ligne], ignore_index=True)
print(f"\n  Apres ajout ligne:\n{df}")

# --- Supprimer ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille'],
    'Code': ['A1', 'B2', 'C3']
})

df_sans_code = df.drop('Code', axis=1)
print(f"\n  Sans colonne Code:\n{df_sans_code}")

df_sans_premiere = df.drop(0, axis=0)
print(f"\n  Sans premiere ligne:\n{df_sans_premiere}")


# ============================================================
# FILTRAGE ET TRI
# ============================================================
print(f"\n{'=' * 50}")
print("FILTRAGE ET TRI")
print("=" * 50)

df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon'],
    'Salaire': [35000, 42000, 48000, 38000, 32000]
})

print(f"\n  Personnes de plus de 30 ans:\n{df[df['Age'] > 30]}")
print(f"\n  Parisiens de moins de 30 ans:\n{df[(df['Ville'] == 'Paris') & (df['Age'] < 30)]}")
print(f"\n  Lyon ou Marseille:\n{df[(df['Ville'] == 'Lyon') | (df['Ville'] == 'Marseille')]}")
print(f"\n  Grandes villes (isin):\n{df[df['Ville'].isin(['Paris', 'Lyon'])]}")
print(f"\n  Noms contenant 'a':\n{df[df['Nom'].str.contains('a', case=False)]}")

# --- Tri ---
df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
    'Salaire': [35000, 42000, 48000, 38000]
})

print(f"\n  Trie par age:\n{df.sort_values('Age')}")
print(f"\n  Trie par salaire decroissant:\n{df.sort_values('Salaire', ascending=False)}")


# ============================================================
# VALEURS MANQUANTES
# ============================================================
print(f"\n{'=' * 50}")
print("VALEURS MANQUANTES")
print("=" * 50)

df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, 28],
    'Ville': ['Paris', 'Lyon', None, 'Toulouse'],
    'Salaire': [35000, 42000, 48000, None]
})

print(f"\n  DataFrame avec NaN:\n{df}")
print(f"\n  Valeurs manquantes:\n{df.isnull().sum()}")
print(f"\n  Sans lignes NaN:\n{df.dropna()}")
print(f"\n  NaN remplaces par 0:\n{df.fillna(0)}")

df_rempli = df.fillna({
    'Age': df['Age'].mean(),
    'Ville': 'Inconnu',
    'Salaire': df['Salaire'].median()
})
print(f"\n  NaN remplis intelligemment:\n{df_rempli}")


# ============================================================
# OPERATIONS PAR GROUPE
# ============================================================
print(f"\n{'=' * 50}")
print("OPERATIONS PAR GROUPE")
print("=" * 50)

df = pd.DataFrame({
    'Ville': ['Paris', 'Lyon', 'Paris', 'Lyon', 'Marseille'],
    'Produit': ['A', 'A', 'B', 'B', 'A'],
    'Ventes': [100, 150, 120, 180, 90],
    'Prix': [10, 15, 12, 18, 9]
})

print(f"\n  Moyenne ventes par ville:\n{df.groupby('Ville')['Ventes'].mean()}")
print(f"\n  Somme ventes par produit:\n{df.groupby('Produit')['Ventes'].sum()}")

stats = df.groupby('Ville').agg({
    'Ventes': ['mean', 'sum'],
    'Prix': ['min', 'max']
})
print(f"\n  Statistiques par ville:\n{stats}")


# ============================================================
# EXEMPLES PRATIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLES PRATIQUES")
print("=" * 50)

# --- Analyse de ventes ---
print(f"\n  --- Analyse de ventes ---")
ventes = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Produit': ['Laptop', 'Souris', 'Clavier', 'Laptop', 'Ecran'],
    'Quantite': [2, 10, 5, 1, 3],
    'Prix_unitaire': [800, 25, 60, 800, 250]
})

ventes['Montant'] = ventes['Quantite'] * ventes['Prix_unitaire']
print(f"  Tableau des ventes:\n{ventes}")
print(f"\n  Revenu total: {ventes['Montant'].sum()} EUR")
print(f"  Vente moyenne: {ventes['Montant'].mean():.2f} EUR")
print(f"  Produit le plus vendu: {ventes.loc[ventes['Quantite'].idxmax(), 'Produit']}")

ventes_par_produit = ventes.groupby('Produit')['Montant'].sum().sort_values(ascending=False)
print(f"\n  Ventes par produit:\n{ventes_par_produit}")

# --- Notes d'etudiants ---
print(f"\n  --- Notes d'etudiants ---")
notes = pd.DataFrame({
    'Etudiant': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Math': [15, 12, 18, 14, 16],
    'Physique': [13, 14, 16, 15, 12],
    'Chimie': [16, 11, 17, 13, 15],
    'Anglais': [14, 15, 15, 16, 14]
})

notes['Moyenne'] = notes[['Math', 'Physique', 'Chimie', 'Anglais']].mean(axis=1)
print(f"  Avec moyennes:\n{notes}")

print(f"\n  Moyenne de classe par matiere:\n{notes[['Math', 'Physique', 'Chimie', 'Anglais']].mean()}")

meilleur = notes.loc[notes['Moyenne'].idxmax()]
print(f"\n  Meilleur etudiant: {meilleur['Etudiant']} avec {meilleur['Moyenne']:.2f}")

mentions = notes[notes['Moyenne'] >= 15]
print(f"\n  Etudiants avec mention (>=15):\n{mentions[['Etudiant', 'Moyenne']]}")

# --- Suivi d'activite ---
print(f"\n  --- Suivi d'activite physique ---")
activite = pd.DataFrame({
    'Jour': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'Sport': ['Course', 'Repos', 'Velo', 'Course', 'Repos', 'Natation', 'Randonnee'],
    'Duree_min': [30, 0, 45, 30, 0, 60, 120],
    'Calories': [300, 0, 400, 300, 0, 500, 600]
})

print(f"  Suivi:\n{activite}")
print(f"\n  Temps total: {activite['Duree_min'].sum()} minutes")
print(f"  Calories brulees: {activite['Calories'].sum()} kcal")
print(f"  Duree moyenne par seance: {activite[activite['Duree_min'] > 0]['Duree_min'].mean():.1f} min")

jours_actifs = activite[activite['Duree_min'] > 0]
print(f"  Nombre de jours actifs: {len(jours_actifs)}")

sports_actifs = activite[activite['Sport'] != 'Repos']
sport_favoris = sports_actifs.groupby('Sport')['Duree_min'].sum().idxmax()
print(f"  Sport le plus pratique: {sport_favoris}")
