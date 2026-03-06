# ============================================================================
#   Section 13.4 : Introduction a l'analyse exploratoire
#   Description : EDA complete avec dataset Iris et Titanic : premieres
#                 observations, valeurs manquantes, doublons, statistiques
#                 descriptives, visualisations (histogrammes, boxplots,
#                 violin plots, pairplots, heatmaps), correlations,
#                 analyse par groupes, outliers, exemple complet Titanic
#   Fichier source : 04-analyse-exploratoire.md
# ============================================================================

"""Introduction a l'analyse exploratoire des donnees (EDA)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Dossier de sortie pour les images
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_eda')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# CHARGEMENT DU DATASET
# ============================================================
print("=" * 50)
print("CHARGEMENT DU DATASET IRIS")
print("=" * 50)

df = sns.load_dataset('iris')
print(f"\n  Dataset charge: {df.shape[0]} lignes, {df.shape[1]} colonnes")


# ============================================================
# PREMIERES OBSERVATIONS
# ============================================================
print(f"\n{'=' * 50}")
print("PREMIERES OBSERVATIONS")
print("=" * 50)

print(f"\n  Premieres lignes:")
print(df.head())

print(f"\n  Dernieres lignes:")
print(df.tail())

print(f"\n  Echantillon aleatoire:")
print(df.sample(5, random_state=42))


# ============================================================
# INFORMATIONS SUR LA STRUCTURE
# ============================================================
print(f"\n{'=' * 50}")
print("STRUCTURE DU DATASET")
print("=" * 50)

print(f"\n  Nombre de lignes: {df.shape[0]}")
print(f"  Nombre de colonnes: {df.shape[1]}")
print(f"  Dimensions: {df.shape}")

print(f"\n  Types de donnees:")
print(df.dtypes)

print(f"\n  Noms des colonnes:")
print(df.columns.tolist())

print(f"\n  Informations:")
df.info()


# ============================================================
# VALEURS MANQUANTES
# ============================================================
print(f"\n{'=' * 50}")
print("VALEURS MANQUANTES")
print("=" * 50)

print(f"\n  Valeurs manquantes par colonne:")
print(df.isnull().sum())

print(f"\n  Pourcentage de valeurs manquantes:")
print((df.isnull().sum() / len(df)) * 100)

# Visualisation des valeurs manquantes
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.title('Carte des valeurs manquantes')
plt.savefig(os.path.join(OUTPUT_DIR, '01_valeurs_manquantes.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  01_valeurs_manquantes.png sauvegarde")


# ============================================================
# VALEURS DUPLIQUEES
# ============================================================
print(f"\n{'=' * 50}")
print("VALEURS DUPLIQUEES")
print("=" * 50)

print(f"\n  Nombre de lignes dupliquees: {df.duplicated().sum()}")

doublons = df[df.duplicated()]
print(f"\n  Lignes dupliquees:")
print(doublons)

df_sans_doublons = df.drop_duplicates()
print(f"\n  Apres suppression: {df_sans_doublons.shape[0]} lignes")


# ============================================================
# STATISTIQUES DESCRIPTIVES - VARIABLES NUMERIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("STATISTIQUES DESCRIPTIVES")
print("=" * 50)

print(f"\n  Statistiques descriptives:")
print(df.describe())

print(f"\n  Statistiques pour sepal_length:")
print(df['sepal_length'].describe())

moyenne = df['sepal_length'].mean()
mediane = df['sepal_length'].median()
mode = df['sepal_length'].mode()[0]
std = df['sepal_length'].std()
variance = df['sepal_length'].var()
minimum = df['sepal_length'].min()
maximum = df['sepal_length'].max()

print(f"\n  Moyenne: {moyenne:.2f}")
print(f"  Mediane: {mediane:.2f}")
print(f"  Mode: {mode:.2f}")
print(f"  Ecart-type: {std:.2f}")
print(f"  Variance: {variance:.2f}")
print(f"  Min: {minimum:.2f}")
print(f"  Max: {maximum:.2f}")

# Quartiles
Q1 = df['sepal_length'].quantile(0.25)
Q2 = df['sepal_length'].quantile(0.50)
Q3 = df['sepal_length'].quantile(0.75)

print(f"\n  Q1 (25%): {Q1:.2f}")
print(f"  Q2 (50%): {Q2:.2f}")
print(f"  Q3 (75%): {Q3:.2f}")


# ============================================================
# STATISTIQUES - VARIABLES CATEGORIELLES
# ============================================================
print(f"\n{'=' * 50}")
print("VARIABLES CATEGORIELLES")
print("=" * 50)

print(f"\n  Valeurs uniques:")
print(df['species'].value_counts())

print(f"\n  Proportions:")
print(df['species'].value_counts(normalize=True))

print(f"\n  Nombre de categories: {df['species'].nunique()}")
print(f"  Categorie la plus frequente: {df['species'].mode()[0]}")


# ============================================================
# MESURES DE FORME
# ============================================================
print(f"\n{'=' * 50}")
print("MESURES DE FORME")
print("=" * 50)

asymetrie = df['sepal_length'].skew()
print(f"\n  Asymetrie (skewness): {asymetrie:.2f}")

aplatissement = df['sepal_length'].kurtosis()
print(f"  Aplatissement (kurtosis): {aplatissement:.2f}")

print(f"\n  Interpretation:")
if abs(asymetrie) < 0.5:
    print(f"    - Distribution approximativement symetrique")
elif asymetrie > 0:
    print(f"    - Distribution asymetrique a droite (queue a droite)")
else:
    print(f"    - Distribution asymetrique a gauche (queue a gauche)")


# ============================================================
# VISUALISATION - DISTRIBUTIONS
# ============================================================
print(f"\n{'=' * 50}")
print("VISUALISATION - DISTRIBUTIONS")
print("=" * 50)

sns.set_style("whitegrid")

# Histogramme
plt.figure(figsize=(10, 6))
plt.hist(df['sepal_length'], bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Longueur du sepale')
plt.ylabel('Frequence')
plt.title('Distribution de la longueur du sepale')
plt.axvline(df['sepal_length'].mean(), color='red', linestyle='--',
            label=f'Moyenne: {df["sepal_length"].mean():.2f}')
plt.legend()
plt.savefig(os.path.join(OUTPUT_DIR, '02_histogramme.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  02_histogramme.png sauvegarde")

# Histogramme + KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, bins=30)
plt.title('Distribution avec courbe de densite')
plt.savefig(os.path.join(OUTPUT_DIR, '03_hist_kde.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  03_hist_kde.png sauvegarde")

# Histogrammes multiples
fig = df.hist(figsize=(15, 12), bins=30, edgecolor='black')
plt.suptitle('Distribution de toutes les variables numeriques')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '04_hist_multiples.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  04_hist_multiples.png sauvegarde")


# ============================================================
# VISUALISATION - BOX PLOTS
# ============================================================
print(f"\n{'=' * 50}")
print("BOX PLOTS")
print("=" * 50)

# Box plot simple
plt.figure(figsize=(10, 6))
sns.boxplot(data=df['sepal_length'])
plt.title('Box plot - Longueur du sepale')
plt.savefig(os.path.join(OUTPUT_DIR, '05_boxplot_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  05_boxplot_simple.png sauvegarde")

# Box plots par categorie
plt.figure(figsize=(12, 6))
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Distribution de la longueur du sepale par espece')
plt.savefig(os.path.join(OUTPUT_DIR, '06_boxplot_espece.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  06_boxplot_espece.png sauvegarde")

# Violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='species', y='sepal_length', data=df)
plt.title('Violin plot - Longueur du sepale par espece')
plt.savefig(os.path.join(OUTPUT_DIR, '07_violin.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  07_violin.png sauvegarde")


# ============================================================
# VISUALISATION - VARIABLES CATEGORIELLES
# ============================================================
print(f"\n{'=' * 50}")
print("VARIABLES CATEGORIELLES")
print("=" * 50)

# Diagramme a barres
plt.figure(figsize=(10, 6))
df['species'].value_counts().plot(kind='bar')
plt.xlabel('Espece')
plt.ylabel("Nombre d'observations")
plt.title('Distribution des especes')
plt.xticks(rotation=45)
plt.savefig(os.path.join(OUTPUT_DIR, '08_bar_especes.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  08_bar_especes.png sauvegarde")

# Diagramme circulaire
plt.figure(figsize=(8, 8))
df['species'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Repartition des especes')
plt.ylabel('')
plt.savefig(os.path.join(OUTPUT_DIR, '09_pie_especes.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  09_pie_especes.png sauvegarde")


# ============================================================
# PAIRPLOT
# ============================================================
print(f"\n{'=' * 50}")
print("PAIRPLOT")
print("=" * 50)

sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle('Matrice de relations entre variables', y=1.02)
plt.savefig(os.path.join(OUTPUT_DIR, '10_pairplot.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  10_pairplot.png sauvegarde")


# ============================================================
# CORRELATIONS
# ============================================================
print(f"\n{'=' * 50}")
print("CORRELATIONS")
print("=" * 50)

correlation_matrix = df.select_dtypes(include=[np.number]).corr()

print(f"\n  Matrice de correlation:")
print(correlation_matrix.round(3))

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Matrice de correlation')
plt.savefig(os.path.join(OUTPUT_DIR, '11_correlation.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  11_correlation.png sauvegarde")


# ============================================================
# SCATTER PLOTS
# ============================================================
print(f"\n{'=' * 50}")
print("SCATTER PLOTS")
print("=" * 50)

# Scatter simple
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal_length'], df['sepal_width'], alpha=0.6)
plt.xlabel('Longueur du sepale')
plt.ylabel('Largeur du sepale')
plt.title('Relation entre longueur et largeur du sepale')
plt.savefig(os.path.join(OUTPUT_DIR, '12_scatter_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  12_scatter_simple.png sauvegarde")

# Scatter par categorie
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'],
                label=species, alpha=0.6)
plt.xlabel('Longueur du sepale')
plt.ylabel('Largeur du sepale')
plt.title('Relation entre longueur et largeur par espece')
plt.legend()
plt.savefig(os.path.join(OUTPUT_DIR, '13_scatter_especes.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  13_scatter_especes.png sauvegarde")

# Scatter avec regression
sns.lmplot(x='sepal_length', y='sepal_width', data=df,
           hue='species', height=6, aspect=1.5)
plt.title('Relation avec ligne de regression')
plt.savefig(os.path.join(OUTPUT_DIR, '14_scatter_regression.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  14_scatter_regression.png sauvegarde")


# ============================================================
# ANALYSE PAR GROUPES
# ============================================================
print(f"\n{'=' * 50}")
print("ANALYSE PAR GROUPES")
print("=" * 50)

stats_par_espece = df.groupby('species').agg({
    'sepal_length': ['mean', 'median', 'std', 'min', 'max'],
    'sepal_width': ['mean', 'median', 'std', 'min', 'max']
})

print(f"\n  Statistiques par espece:")
print(stats_par_espece)

print(f"\n  Moyennes par espece:")
print(df.groupby('species').mean(numeric_only=True))

# Bar plot des moyennes
df.groupby('species')['sepal_length'].mean().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Espece')
plt.ylabel('Longueur moyenne du sepale')
plt.title('Comparaison des moyennes par espece')
plt.xticks(rotation=45)
plt.savefig(os.path.join(OUTPUT_DIR, '15_bar_moyennes.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  15_bar_moyennes.png sauvegarde")

# Box plots cote a cote
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

sns.boxplot(x='species', y='sepal_length', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Longueur du sepale')

sns.boxplot(x='species', y='sepal_width', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Largeur du sepale')

sns.boxplot(x='species', y='petal_length', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Longueur du petale')

sns.boxplot(x='species', y='petal_width', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Largeur du petale')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '16_boxplots_complets.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  16_boxplots_complets.png sauvegarde")


# ============================================================
# DETECTION D'OUTLIERS
# ============================================================
print(f"\n{'=' * 50}")
print("DETECTION D'OUTLIERS")
print("=" * 50)

def detecter_outliers_iqr(df, colonne):
    Q1 = df[colonne].quantile(0.25)
    Q3 = df[colonne].quantile(0.75)
    IQR = Q3 - Q1
    limite_basse = Q1 - 1.5 * IQR
    limite_haute = Q3 + 1.5 * IQR
    outliers = df[(df[colonne] < limite_basse) | (df[colonne] > limite_haute)]
    return outliers

def detecter_outliers_zscore(df, colonne, seuil=3):
    z_scores = np.abs((df[colonne] - df[colonne].mean()) / df[colonne].std())
    outliers = df[z_scores > seuil]
    return outliers

for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
    outliers_iqr = detecter_outliers_iqr(df, col)
    outliers_zscore = detecter_outliers_zscore(df, col)
    print(f"\n  {col}:")
    print(f"    Outliers IQR: {len(outliers_iqr)}")
    print(f"    Outliers Z-score: {len(outliers_zscore)}")


# ============================================================
# EXEMPLE COMPLET : DATASET TITANIC
# ============================================================
print(f"\n{'=' * 80}")
print("ANALYSE EXPLORATOIRE DU DATASET TITANIC")
print("=" * 80)

titanic = sns.load_dataset('titanic')

# 1. PREMIERES OBSERVATIONS
print(f"\n1. PREMIERES OBSERVATIONS")
print("-" * 80)
print(f"  Dimensions: {titanic.shape[0]} lignes, {titanic.shape[1]} colonnes")
print(f"\n  Premieres lignes:")
print(titanic.head())

print(f"\n  Types de donnees:")
print(titanic.dtypes)

# 2. VALEURS MANQUANTES
print(f"\n2. VALEURS MANQUANTES")
print("-" * 80)
missing = titanic.isnull().sum()
missing_percent = (missing / len(titanic)) * 100
missing_df = pd.DataFrame({
    'Colonne': missing.index,
    'Valeurs manquantes': missing.values,
    'Pourcentage': missing_percent.values
})
print(missing_df[missing_df['Valeurs manquantes'] > 0].to_string(index=False))

plt.figure(figsize=(10, 6))
sns.heatmap(titanic.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.title('Carte des valeurs manquantes - Titanic')
plt.savefig(os.path.join(OUTPUT_DIR, '17_titanic_missing.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  17_titanic_missing.png sauvegarde")

# 3. STATISTIQUES DESCRIPTIVES
print(f"\n3. STATISTIQUES DESCRIPTIVES")
print("-" * 80)
print(titanic.describe())

# 4. ANALYSE DE LA SURVIE
print(f"\n4. ANALYSE DE LA SURVIE")
print("-" * 80)
print(f"  Taux de survie global: {titanic['survived'].mean():.2%}")
print(f"  Nombre de survivants: {titanic['survived'].sum()}")
print(f"  Nombre de decedes: {(1 - titanic['survived']).sum():.0f}")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

titanic['survived'].value_counts().plot(kind='bar', ax=axes[0])
axes[0].set_title('Distribution de la survie')
axes[0].set_xlabel('Survie (0 = Non, 1 = Oui)')
axes[0].set_ylabel('Nombre de passagers')
axes[0].set_xticklabels(['Decede', 'Survecu'], rotation=0)

titanic['survived'].value_counts().plot(kind='pie', ax=axes[1],
                                        autopct='%1.1f%%',
                                        labels=['Decede', 'Survecu'])
axes[1].set_title('Proportion de survie')
axes[1].set_ylabel('')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '18_titanic_survie.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  18_titanic_survie.png sauvegarde")

# 5. ANALYSE PAR SEXE
print(f"\n5. ANALYSE PAR SEXE")
print("-" * 80)
print(titanic.groupby('sex')['survived'].agg(['count', 'sum', 'mean']))

plt.figure(figsize=(10, 6))
sns.barplot(x='sex', y='survived', data=titanic)
plt.title('Taux de survie par sexe')
plt.ylabel('Taux de survie')
plt.xlabel('Sexe')
plt.savefig(os.path.join(OUTPUT_DIR, '19_titanic_sexe.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  19_titanic_sexe.png sauvegarde")

# 6. ANALYSE PAR CLASSE
print(f"\n6. ANALYSE PAR CLASSE")
print("-" * 80)
print(titanic.groupby('pclass')['survived'].agg(['count', 'sum', 'mean']))

plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='survived', data=titanic)
plt.title('Taux de survie par classe')
plt.ylabel('Taux de survie')
plt.xlabel('Classe')
plt.savefig(os.path.join(OUTPUT_DIR, '20_titanic_classe.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  20_titanic_classe.png sauvegarde")

# 7. ANALYSE PAR AGE
print(f"\n7. ANALYSE PAR AGE")
print("-" * 80)
print(f"  Age moyen: {titanic['age'].mean():.2f} ans")
print(f"  Age median: {titanic['age'].median():.2f} ans")
print(f"  Age min: {titanic['age'].min():.2f} ans")
print(f"  Age max: {titanic['age'].max():.2f} ans")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

titanic['age'].hist(bins=30, ax=axes[0], edgecolor='black')
axes[0].set_title("Distribution de l'age")
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequence')

sns.boxplot(x='survived', y='age', data=titanic, ax=axes[1])
axes[1].set_title("Distribution de l'age par survie")
axes[1].set_xticklabels(['Decede', 'Survecu'])

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '21_titanic_age.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  21_titanic_age.png sauvegarde")

# 8. ANALYSE CROISEE
print(f"\n8. ANALYSE CROISEE")
print("-" * 80)

cross_tab = pd.crosstab([titanic['pclass'], titanic['sex']],
                        titanic['survived'],
                        margins=True)
print(f"  Tableau croise Classe x Sexe x Survie:")
print(cross_tab)

g = sns.catplot(x='pclass', y='survived', hue='sex', data=titanic,
                kind='bar', height=6, aspect=1.5)
g.fig.suptitle('Taux de survie par classe et par sexe', y=1.02)
plt.savefig(os.path.join(OUTPUT_DIR, '22_titanic_croise.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  22_titanic_croise.png sauvegarde")

# 9. CORRELATIONS
print(f"\n9. MATRICE DE CORRELATION")
print("-" * 80)

numeric_cols = titanic.select_dtypes(include=[np.number]).columns
correlation_matrix = titanic[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
            center=0, square=True, linewidths=1, fmt='.2f')
plt.title('Matrice de correlation - Titanic')
plt.savefig(os.path.join(OUTPUT_DIR, '23_titanic_correlation.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  23_titanic_correlation.png sauvegarde")

print(f"\n  Correlations avec la survie:")
print(correlation_matrix['survived'].sort_values(ascending=False).round(3))

# 10. INSIGHTS PRINCIPAUX
print(f"\n10. INSIGHTS PRINCIPAUX")
print("=" * 80)
print("  1. Taux de survie global: ~38%")
taux_femmes = titanic[titanic['sex'] == 'female']['survived'].mean()
taux_hommes = titanic[titanic['sex'] == 'male']['survived'].mean()
print(f"  2. Femmes: {taux_femmes:.0%} de survie vs Hommes: {taux_hommes:.0%}")
for cls in [1, 2, 3]:
    taux = titanic[titanic['pclass'] == cls]['survived'].mean()
    print(f"  3. Classe {cls}: {taux:.0%} de survie")
print(f"  4. Age moyen des survivants: {titanic[titanic['survived']==1]['age'].mean():.1f} ans")
print(f"     Age moyen des decedes: {titanic[titanic['survived']==0]['age'].mean():.1f} ans")
print("  5. Le sexe est le facteur le plus discriminant, suivi de la classe")
print("=" * 80)

# --- Resume des fichiers generes ---
print(f"\n{'=' * 50}")
print("RESUME")
print("=" * 50)
fichiers = sorted(os.listdir(OUTPUT_DIR))
print(f"\n  {len(fichiers)} fichiers generes dans {OUTPUT_DIR}:")
for f in fichiers:
    taille = os.path.getsize(os.path.join(OUTPUT_DIR, f))
    print(f"    - {f} ({taille:,} bytes)")
