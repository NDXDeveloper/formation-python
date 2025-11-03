🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 13.4 Introduction à l'analyse exploratoire

## Qu'est-ce que l'analyse exploratoire des données (EDA) ?

L'**analyse exploratoire des données** (EDA pour Exploratory Data Analysis en anglais) est la première étape cruciale de tout projet de Data Science. C'est le processus d'investigation initial des données pour :

- **Découvrir des patterns** : identifier des tendances, des structures cachées
- **Détecter des anomalies** : repérer les valeurs aberrantes, les erreurs
- **Tester des hypothèses** : vérifier des suppositions initiales
- **Comprendre les relations** : voir comment les variables interagissent
- **Résumer l'information** : obtenir une vue d'ensemble des données

> "L'analyse exploratoire est une attitude, un état d'esprit flexible, une volonté de chercher ce que l'on pense être dans les données, mais aussi ce que l'on ne s'attendait pas à trouver." - John Tukey (inventeur de l'EDA)

## Pourquoi l'EDA est-elle essentielle ?

### 1. Comprendre avant de modéliser

Imaginez que vous devez construire une maison. Avant de commencer les travaux, vous devez :
- Étudier le terrain
- Comprendre la nature du sol
- Identifier les contraintes
- Planifier en conséquence

C'est exactement la même chose avec les données ! Avant de construire des modèles complexes, vous devez comprendre vos données.

### 2. Éviter les erreurs coûteuses

Sans EDA, vous risquez de :
- Utiliser des données erronées ou corrompues
- Ignorer des valeurs manquantes importantes
- Mal interpréter les relations entre variables
- Construire des modèles sur des hypothèses fausses

### 3. Gagner du temps

Bien que l'EDA prenne du temps au début, elle vous en fait gagner énormément par la suite en :
- Évitant les impasses
- Identifiant rapidement les problèmes
- Guidant vos choix de modélisation
- Anticipant les difficultés

### 4. Raconter une histoire

L'EDA vous aide à comprendre le "narratif" de vos données, ce qui est essentiel pour communiquer vos résultats.

## Les étapes de l'analyse exploratoire

L'EDA suit généralement ces étapes :

```
1. Collecte et importation des données
   ↓
2. Premières observations (aperçu des données)
   ↓
3. Nettoyage des données
   ↓
4. Analyse statistique descriptive
   ↓
5. Visualisation
   ↓
6. Détection d'anomalies
   ↓
7. Analyse des corrélations
   ↓
8. Formulation d'hypothèses
```

Nous allons explorer chacune de ces étapes avec des exemples pratiques.

## 1. Collecte et importation des données

### Chargement d'un dataset

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement depuis un fichier CSV
df = pd.read_csv('donnees.csv')

# Ou utilisation d'un dataset d'exemple
# Iris : classification de fleurs
df = sns.load_dataset('iris')
```

**Formats de données courants :**
- **CSV** : `pd.read_csv()`
- **Excel** : `pd.read_excel()`
- **JSON** : `pd.read_json()`
- **SQL** : `pd.read_sql()`
- **Parquet** : `pd.read_parquet()`

## 2. Premières observations

### 2.1 Vue d'ensemble du dataset

```python
import pandas as pd
import seaborn as sns

# Chargement du dataset Iris
df = sns.load_dataset('iris')

# Afficher les premières lignes
print("Premières lignes :")
print(df.head())

# Afficher les dernières lignes
print("\nDernières lignes :")
print(df.tail())

# Afficher un échantillon aléatoire
print("\nÉchantillon aléatoire :")
print(df.sample(5))
```

**Questions à se poser :**
- Les données ont-elles l'air cohérentes ?
- Y a-t-il des colonnes inattendues ?
- Les types de données sont-ils corrects ?

### 2.2 Informations sur la structure

```python
# Dimensions du dataset
print(f"Nombre de lignes : {df.shape[0]}")
print(f"Nombre de colonnes : {df.shape[1]}")
print(f"Dimensions : {df.shape}")

# Informations détaillées
print("\nInformations sur le dataset :")
print(df.info())

# Types de données
print("\nTypes de données :")
print(df.dtypes)

# Noms des colonnes
print("\nNoms des colonnes :")
print(df.columns.tolist())
```

### 2.3 Valeurs manquantes

```python
# Comptage des valeurs manquantes
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())

# Pourcentage de valeurs manquantes
print("\nPourcentage de valeurs manquantes :")
print((df.isnull().sum() / len(df)) * 100)

# Visualisation des valeurs manquantes
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.title('Carte des valeurs manquantes')
plt.show()
```

### 2.4 Valeurs dupliquées

```python
# Nombre de doublons
print(f"Nombre de lignes dupliquées : {df.duplicated().sum()}")

# Afficher les doublons
doublons = df[df.duplicated()]
print("\nLignes dupliquées :")
print(doublons)

# Supprimer les doublons (si nécessaire)
df_sans_doublons = df.drop_duplicates()
```

## 3. Nettoyage des données

Le nettoyage est une étape cruciale qui peut prendre 60-80% du temps d'un projet.

### 3.1 Gestion des valeurs manquantes

```python
# Stratégie 1 : Suppression des lignes avec valeurs manquantes
df_clean = df.dropna()

# Stratégie 2 : Suppression des colonnes avec trop de valeurs manquantes
seuil = 0.5  # 50% de valeurs manquantes
df_clean = df.dropna(thresh=len(df) * seuil, axis=1)

# Stratégie 3 : Remplacement par la moyenne (pour variables numériques)
df['colonne'] = df['colonne'].fillna(df['colonne'].mean())

# Stratégie 4 : Remplacement par la médiane
df['colonne'] = df['colonne'].fillna(df['colonne'].median())

# Stratégie 5 : Remplacement par la valeur la plus fréquente
df['colonne'] = df['colonne'].fillna(df['colonne'].mode()[0])

# Stratégie 6 : Remplacement par une valeur spécifique
df['colonne'] = df['colonne'].fillna(0)
```

### 3.2 Gestion des valeurs aberrantes (outliers)

```python
import numpy as np

# Méthode 1 : Règle des 1.5 IQR (Inter-Quartile Range)
def detecter_outliers_iqr(df, colonne):
    Q1 = df[colonne].quantile(0.25)
    Q3 = df[colonne].quantile(0.75)
    IQR = Q3 - Q1

    limite_basse = Q1 - 1.5 * IQR
    limite_haute = Q3 + 1.5 * IQR

    outliers = df[(df[colonne] < limite_basse) | (df[colonne] > limite_haute)]
    return outliers

# Méthode 2 : Z-score (pour distributions normales)
def detecter_outliers_zscore(df, colonne, seuil=3):
    z_scores = np.abs((df[colonne] - df[colonne].mean()) / df[colonne].std())
    outliers = df[z_scores > seuil]
    return outliers

# Visualisation des outliers avec box plot
plt.figure(figsize=(10, 6))
plt.boxplot(df['colonne_numerique'])
plt.title('Détection des valeurs aberrantes')
plt.ylabel('Valeur')
plt.show()
```

### 3.3 Conversion de types de données

```python
# Conversion en numérique
df['colonne'] = pd.to_numeric(df['colonne'], errors='coerce')

# Conversion en catégorie
df['colonne_categorielle'] = df['colonne_categorielle'].astype('category')

# Conversion en datetime
df['date'] = pd.to_datetime(df['date'])

# Conversion en string
df['colonne'] = df['colonne'].astype(str)
```

## 4. Analyse statistique descriptive

L'analyse descriptive résume les caractéristiques principales des données.

### 4.1 Variables numériques

```python
# Statistiques descriptives complètes
print("Statistiques descriptives :")
print(df.describe())

# Statistiques pour une colonne spécifique
print("\nStatistiques pour une colonne :")
print(df['sepal_length'].describe())

# Statistiques individuelles
moyenne = df['sepal_length'].mean()
mediane = df['sepal_length'].median()
mode = df['sepal_length'].mode()[0]
std = df['sepal_length'].std()
variance = df['sepal_length'].var()
minimum = df['sepal_length'].min()
maximum = df['sepal_length'].max()

print(f"Moyenne : {moyenne:.2f}")
print(f"Médiane : {mediane:.2f}")
print(f"Mode : {mode:.2f}")
print(f"Écart-type : {std:.2f}")
print(f"Variance : {variance:.2f}")
print(f"Min : {minimum:.2f}")
print(f"Max : {maximum:.2f}")

# Quartiles
Q1 = df['sepal_length'].quantile(0.25)
Q2 = df['sepal_length'].quantile(0.50)  # = médiane
Q3 = df['sepal_length'].quantile(0.75)

print(f"\nQ1 (25%) : {Q1:.2f}")
print(f"Q2 (50%) : {Q2:.2f}")
print(f"Q3 (75%) : {Q3:.2f}")
```

**Interprétation des statistiques :**

- **Moyenne** : valeur centrale, sensible aux outliers
- **Médiane** : valeur centrale, robuste aux outliers
- **Mode** : valeur la plus fréquente
- **Écart-type** : mesure de dispersion (plus il est élevé, plus les données sont dispersées)
- **Variance** : carré de l'écart-type
- **Min/Max** : valeurs extrêmes
- **Quartiles** : divisent les données en 4 parties égales

### 4.2 Variables catégorielles

```python
# Comptage des valeurs uniques
print("Valeurs uniques :")
print(df['species'].value_counts())

# Proportions
print("\nProportions :")
print(df['species'].value_counts(normalize=True))

# Nombre de valeurs uniques
print(f"\nNombre de catégories : {df['species'].nunique()}")

# Mode (valeur la plus fréquente)
print(f"Catégorie la plus fréquente : {df['species'].mode()[0]}")
```

### 4.3 Mesures de forme de distribution

```python
# Asymétrie (Skewness)
# skewness > 0 : distribution asymétrique à droite (queue à droite)
# skewness < 0 : distribution asymétrique à gauche (queue à gauche)
# skewness ≈ 0 : distribution symétrique
asymetrie = df['sepal_length'].skew()
print(f"Asymétrie : {asymetrie:.2f}")

# Aplatissement (Kurtosis)
# kurtosis > 0 : distribution pointue (leptokurtique)
# kurtosis < 0 : distribution aplatie (platikurtique)
# kurtosis ≈ 0 : distribution normale (mésokurtique)
aplatissement = df['sepal_length'].kurtosis()
print(f"Aplatissement : {aplatissement:.2f}")
```

## 5. Visualisation des données

La visualisation est le cœur de l'EDA. "Un graphique vaut mille tableaux."

### 5.1 Distribution des variables numériques

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de style
sns.set_style("whitegrid")

# Histogramme
plt.figure(figsize=(10, 6))
plt.hist(df['sepal_length'], bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Longueur du sépale')
plt.ylabel('Fréquence')
plt.title('Distribution de la longueur du sépale')
plt.axvline(df['sepal_length'].mean(), color='red', linestyle='--',
            label=f'Moyenne: {df["sepal_length"].mean():.2f}')
plt.legend()
plt.show()

# Courbe de densité (KDE)
plt.figure(figsize=(10, 6))
df['sepal_length'].plot(kind='kde')
plt.xlabel('Longueur du sépale')
plt.ylabel('Densité')
plt.title('Courbe de densité')
plt.show()

# Histogramme + KDE combinés
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, bins=30)
plt.title('Distribution avec courbe de densité')
plt.show()
```

### 5.2 Box plots pour détecter les outliers

```python
# Box plot simple
plt.figure(figsize=(10, 6))
sns.boxplot(data=df['sepal_length'])
plt.title('Box plot - Longueur du sépale')
plt.show()

# Box plots multiples (par catégorie)
plt.figure(figsize=(12, 6))
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Distribution de la longueur du sépale par espèce')
plt.show()

# Violin plot (combine box plot et KDE)
plt.figure(figsize=(12, 6))
sns.violinplot(x='species', y='sepal_length', data=df)
plt.title('Violin plot - Longueur du sépale par espèce')
plt.show()
```

### 5.3 Variables catégorielles

```python
# Diagramme à barres
plt.figure(figsize=(10, 6))
df['species'].value_counts().plot(kind='bar')
plt.xlabel('Espèce')
plt.ylabel('Nombre d\'observations')
plt.title('Distribution des espèces')
plt.xticks(rotation=45)
plt.show()

# Diagramme circulaire
plt.figure(figsize=(8, 8))
df['species'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Répartition des espèces')
plt.ylabel('')
plt.show()
```

### 5.4 Matrices de distribution

```python
# Histogrammes multiples
df.hist(figsize=(15, 12), bins=30, edgecolor='black')
plt.suptitle('Distribution de toutes les variables numériques')
plt.tight_layout()
plt.show()

# Pairplot : visualisation de toutes les relations
sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle('Matrice de relations entre variables', y=1.02)
plt.show()
```

## 6. Analyse des corrélations

Les corrélations révèlent les relations entre variables.

### 6.1 Matrice de corrélation

```python
# Calcul de la matrice de corrélation
correlation_matrix = df.select_dtypes(include=[np.number]).corr()

print("Matrice de corrélation :")
print(correlation_matrix)

# Visualisation avec heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Matrice de corrélation')
plt.show()
```

**Interprétation des corrélations :**
- **r = 1** : corrélation positive parfaite
- **r = 0.7 à 0.9** : corrélation positive forte
- **r = 0.4 à 0.7** : corrélation positive modérée
- **r = 0.1 à 0.4** : corrélation positive faible
- **r = 0** : pas de corrélation
- **r = -0.1 à -0.4** : corrélation négative faible
- **r = -0.4 à -0.7** : corrélation négative modérée
- **r = -0.7 à -0.9** : corrélation négative forte
- **r = -1** : corrélation négative parfaite

### 6.2 Nuages de points (Scatter plots)

```python
# Scatter plot simple
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal_length'], df['sepal_width'], alpha=0.6)
plt.xlabel('Longueur du sépale')
plt.ylabel('Largeur du sépale')
plt.title('Relation entre longueur et largeur du sépale')
plt.show()

# Scatter plot avec couleurs par catégorie
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'],
                label=species, alpha=0.6)
plt.xlabel('Longueur du sépale')
plt.ylabel('Largeur du sépale')
plt.title('Relation entre longueur et largeur par espèce')
plt.legend()
plt.show()

# Scatter plot avec ligne de régression
sns.lmplot(x='sepal_length', y='sepal_width', data=df,
           hue='species', height=6, aspect=1.5)
plt.title('Relation avec ligne de régression')
plt.show()
```

## 7. Analyse par groupes

Comparer les statistiques entre différents groupes.

### 7.1 Statistiques par groupe

```python
# Groupement et statistiques
stats_par_espece = df.groupby('species').agg({
    'sepal_length': ['mean', 'median', 'std', 'min', 'max'],
    'sepal_width': ['mean', 'median', 'std', 'min', 'max']
})

print("Statistiques par espèce :")
print(stats_par_espece)

# Résumé plus simple
print("\nMoyennes par espèce :")
print(df.groupby('species').mean())
```

### 7.2 Visualisations comparatives

```python
# Bar plot des moyennes
df.groupby('species')['sepal_length'].mean().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Espèce')
plt.ylabel('Longueur moyenne du sépale')
plt.title('Comparaison des moyennes par espèce')
plt.xticks(rotation=45)
plt.show()

# Box plots côte à côte
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

sns.boxplot(x='species', y='sepal_length', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Longueur du sépale')

sns.boxplot(x='species', y='sepal_width', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Largeur du sépale')

sns.boxplot(x='species', y='petal_length', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Longueur du pétale')

sns.boxplot(x='species', y='petal_width', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Largeur du pétale')

plt.tight_layout()
plt.show()
```

## 8. Exemple complet : EDA sur le dataset Titanic

Appliquons tous ces concepts sur un cas réel : le dataset Titanic.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
titanic = sns.load_dataset('titanic')

print("=" * 80)
print("ANALYSE EXPLORATOIRE DU DATASET TITANIC")
print("=" * 80)

# 1. PREMIÈRES OBSERVATIONS
print("\n1. PREMIÈRES OBSERVATIONS")
print("-" * 80)
print(f"Dimensions : {titanic.shape[0]} lignes, {titanic.shape[1]} colonnes")
print("\nPremières lignes :")
print(titanic.head())

print("\nTypes de données :")
print(titanic.dtypes)

# 2. VALEURS MANQUANTES
print("\n2. VALEURS MANQUANTES")
print("-" * 80)
missing = titanic.isnull().sum()
missing_percent = (missing / len(titanic)) * 100
missing_df = pd.DataFrame({
    'Colonne': missing.index,
    'Valeurs manquantes': missing.values,
    'Pourcentage': missing_percent.values
})
print(missing_df[missing_df['Valeurs manquantes'] > 0])

# Visualisation
plt.figure(figsize=(10, 6))
sns.heatmap(titanic.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.title('Carte des valeurs manquantes - Titanic')
plt.show()

# 3. STATISTIQUES DESCRIPTIVES
print("\n3. STATISTIQUES DESCRIPTIVES")
print("-" * 80)
print(titanic.describe())

# 4. ANALYSE DE LA SURVIE (variable cible)
print("\n4. ANALYSE DE LA SURVIE")
print("-" * 80)
print(f"Taux de survie global : {titanic['survived'].mean():.2%}")
print(f"\nNombre de survivants : {titanic['survived'].sum()}")
print(f"Nombre de décédés : {(1 - titanic['survived']).sum()}")

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Diagramme à barres
titanic['survived'].value_counts().plot(kind='bar', ax=axes[0])
axes[0].set_title('Distribution de la survie')
axes[0].set_xlabel('Survie (0 = Non, 1 = Oui)')
axes[0].set_ylabel('Nombre de passagers')
axes[0].set_xticklabels(['Décédé', 'Survécu'], rotation=0)

# Diagramme circulaire
titanic['survived'].value_counts().plot(kind='pie', ax=axes[1],
                                        autopct='%1.1f%%',
                                        labels=['Décédé', 'Survécu'])
axes[1].set_title('Proportion de survie')
axes[1].set_ylabel('')

plt.tight_layout()
plt.show()

# 5. ANALYSE PAR SEXE
print("\n5. ANALYSE PAR SEXE")
print("-" * 80)
print(titanic.groupby('sex')['survived'].agg(['count', 'sum', 'mean']))

plt.figure(figsize=(10, 6))
sns.barplot(x='sex', y='survived', data=titanic)
plt.title('Taux de survie par sexe')
plt.ylabel('Taux de survie')
plt.xlabel('Sexe')
plt.show()

# 6. ANALYSE PAR CLASSE
print("\n6. ANALYSE PAR CLASSE")
print("-" * 80)
print(titanic.groupby('pclass')['survived'].agg(['count', 'sum', 'mean']))

plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='survived', data=titanic)
plt.title('Taux de survie par classe')
plt.ylabel('Taux de survie')
plt.xlabel('Classe')
plt.show()

# 7. ANALYSE PAR ÂGE
print("\n7. ANALYSE PAR ÂGE")
print("-" * 80)
print(f"Âge moyen : {titanic['age'].mean():.2f} ans")
print(f"Âge médian : {titanic['age'].median():.2f} ans")
print(f"Âge min : {titanic['age'].min():.2f} ans")
print(f"Âge max : {titanic['age'].max():.2f} ans")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Distribution de l'âge
titanic['age'].hist(bins=30, ax=axes[0], edgecolor='black')
axes[0].set_title('Distribution de l\'âge')
axes[0].set_xlabel('Âge')
axes[0].set_ylabel('Fréquence')

# Âge par survie
sns.boxplot(x='survived', y='age', data=titanic, ax=axes[1])
axes[1].set_title('Distribution de l\'âge par survie')
axes[1].set_xticklabels(['Décédé', 'Survécu'])

plt.tight_layout()
plt.show()

# 8. ANALYSE CROISÉE : Sexe, Classe et Survie
print("\n8. ANALYSE CROISÉE")
print("-" * 80)

# Tableau croisé
cross_tab = pd.crosstab([titanic['pclass'], titanic['sex']],
                        titanic['survived'],
                        margins=True)
print("Tableau croisé Classe x Sexe x Survie :")
print(cross_tab)

# Visualisation
plt.figure(figsize=(12, 6))
sns.catplot(x='pclass', y='survived', hue='sex', data=titanic,
            kind='bar', height=6, aspect=1.5)
plt.title('Taux de survie par classe et par sexe')
plt.ylabel('Taux de survie')
plt.xlabel('Classe')
plt.show()

# 9. CORRÉLATIONS
print("\n9. MATRICE DE CORRÉLATION")
print("-" * 80)

# Sélection des variables numériques
numeric_cols = titanic.select_dtypes(include=[np.number]).columns
correlation_matrix = titanic[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Matrice de corrélation - Titanic')
plt.show()

# 10. INSIGHTS PRINCIPAUX
print("\n10. INSIGHTS PRINCIPAUX")
print("=" * 80)
print("1. Taux de survie global : ~38%")
print("2. Les femmes ont un taux de survie beaucoup plus élevé (~74%) que les hommes (~19%)")
print("3. Les passagers de 1ère classe ont survécu davantage (~63%) que ceux de 3e classe (~24%)")
print("4. L'âge influence la survie : les enfants ont un meilleur taux de survie")
print("5. Il y a des valeurs manquantes importantes dans 'age' et 'deck'")
print("6. Le facteur le plus discriminant semble être le sexe, suivi de la classe")
print("=" * 80)
```

## 9. Checklist complète de l'EDA

Utilisez cette checklist pour ne rien oublier :

### ✅ Phase 1 : Découverte initiale
- [ ] Charger les données
- [ ] Afficher les premières lignes (`head()`, `tail()`)
- [ ] Vérifier les dimensions (`shape`)
- [ ] Lister les colonnes
- [ ] Vérifier les types de données (`dtypes`)
- [ ] Afficher les informations générales (`info()`)

### ✅ Phase 2 : Qualité des données
- [ ] Identifier les valeurs manquantes
- [ ] Calculer le pourcentage de valeurs manquantes
- [ ] Détecter les doublons
- [ ] Identifier les valeurs aberrantes
- [ ] Vérifier la cohérence des données

### ✅ Phase 3 : Statistiques descriptives
- [ ] Statistiques pour variables numériques (`describe()`)
- [ ] Distribution des variables catégorielles (`value_counts()`)
- [ ] Calculer les mesures de tendance centrale (moyenne, médiane, mode)
- [ ] Calculer les mesures de dispersion (écart-type, variance)
- [ ] Calculer asymétrie et aplatissement

### ✅ Phase 4 : Visualisation univariée
- [ ] Histogrammes pour variables numériques
- [ ] Box plots pour détecter les outliers
- [ ] Diagrammes à barres pour variables catégorielles
- [ ] Courbes de densité (KDE)

### ✅ Phase 5 : Visualisation bivariée
- [ ] Scatter plots pour relations entre variables
- [ ] Box plots par catégorie
- [ ] Diagrammes à barres groupées

### ✅ Phase 6 : Visualisation multivariée
- [ ] Matrice de corrélation
- [ ] Pairplot
- [ ] Heatmap

### ✅ Phase 7 : Analyse par groupes
- [ ] Grouper et calculer des statistiques
- [ ] Comparer les distributions par groupe
- [ ] Visualiser les différences entre groupes

### ✅ Phase 8 : Synthèse
- [ ] Documenter les insights principaux
- [ ] Identifier les problèmes de qualité
- [ ] Formuler des hypothèses
- [ ] Planifier les étapes suivantes

## 10. Outils et bibliothèques essentiels

### Bibliothèques Python pour l'EDA

```python
# Manipulation de données
import pandas as pd
import numpy as np

# Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Statistiques
from scipy import stats

# Outils spécialisés pour l'EDA
import pandas_profiling  # Rapports automatiques
import sweetviz  # Comparaison de datasets
import dtale  # Interface interactive
```

### Pandas Profiling : EDA automatique

Pandas Profiling génère un rapport complet d'EDA en une seule ligne :

```python
# Installation : pip install pandas-profiling
from pandas_profiling import ProfileReport

# Génération du rapport
profile = ProfileReport(df, title='Rapport EDA', explorative=True)

# Sauvegarde en HTML
profile.to_file("rapport_eda.html")

# Affichage dans Jupyter
profile.to_widgets()
```

Le rapport inclut automatiquement :
- Aperçu du dataset
- Variables : types, valeurs manquantes, distribution
- Corrélations
- Valeurs manquantes
- Échantillon de données
- Et bien plus !

### Sweetviz : Comparaison de datasets

```python
# Installation : pip install sweetviz
import sweetviz as sv

# Analyse d'un seul dataset
report = sv.analyze(df)
report.show_html("rapport_sweetviz.html")

# Comparaison de deux datasets (ex: train vs test)
compare = sv.compare([train_df, "Training"], [test_df, "Test"])
compare.show_html("comparaison.html")
```

## 11. Bonnes pratiques de l'EDA

### 1. Commencer large, puis zoomer

Ne vous focalisez pas immédiatement sur les détails. Commencez par une vue d'ensemble, puis approfondissez progressivement.

### 2. Documenter vos découvertes

Prenez des notes tout au long de votre exploration :
- Anomalies détectées
- Hypothèses formulées
- Questions soulevées
- Décisions de nettoyage

### 3. Itérer

L'EDA n'est pas linéaire. Vous découvrirez de nouvelles choses qui vous feront revenir en arrière.

### 4. Ne pas se précipiter

Même si c'est tentant de passer rapidement à la modélisation, une bonne EDA vous fera gagner énormément de temps par la suite.

### 5. Combiner statistiques et visualisations

Les chiffres ne suffisent pas, les graphiques non plus. Utilisez les deux !

### 6. Garder un œil critique

Questionnez toujours vos données :
- Ces valeurs sont-elles logiques ?
- Y a-t-il des erreurs de saisie ?
- Les unités sont-elles cohérentes ?

### 7. Penser au contexte métier

Les données sans contexte métier sont inutiles. Comprenez d'où viennent les données et ce qu'elles représentent.

## 12. Erreurs courantes à éviter

### ❌ Erreur 1 : Sauter l'EDA
"Je connais déjà mes données, je passe directement à la modélisation."
→ Même des données familières peuvent révéler des surprises

### ❌ Erreur 2 : Se fier uniquement aux statistiques
Les statistiques peuvent être trompeuses sans visualisation (voir le quartet d'Anscombe).

### ❌ Erreur 3 : Ignorer les valeurs manquantes
Les valeurs manquantes contiennent de l'information ! Pourquoi manquent-elles ?

### ❌ Erreur 4 : Supprimer automatiquement les outliers
Les outliers peuvent être des erreurs... ou les points les plus intéressants !

### ❌ Erreur 5 : Ne pas vérifier les doublons
Des doublons peuvent biaiser complètement vos analyses.

### ❌ Erreur 6 : Confondre corrélation et causalité
"Ces variables sont corrélées" ≠ "L'une cause l'autre"

### ❌ Erreur 7 : Surcharger les graphiques
Un graphique simple et clair vaut mieux qu'un graphique complexe et illisible.

## 13. Rapport d'EDA : structure type

Quand vous documentez votre EDA, suivez cette structure :

```
1. INTRODUCTION
   - Contexte et objectif
   - Source des données
   - Description du dataset

2. APERÇU DES DONNÉES
   - Dimensions
   - Variables et types
   - Échantillon des données

3. QUALITÉ DES DONNÉES
   - Valeurs manquantes
   - Doublons
   - Incohérences détectées
   - Actions de nettoyage

4. ANALYSE DESCRIPTIVE
   - Variables numériques
   - Variables catégorielles
   - Distributions

5. RELATIONS ENTRE VARIABLES
   - Corrélations
   - Analyses croisées
   - Visualisations

6. INSIGHTS PRINCIPAUX
   - Découvertes clés
   - Patterns identifiés
   - Anomalies

7. CONCLUSIONS ET RECOMMANDATIONS
   - Synthèse
   - Prochaines étapes
   - Recommandations pour la modélisation
```

## Conclusion

L'analyse exploratoire des données est une compétence fondamentale en Data Science. C'est un mélange d'art et de science qui nécessite :
- **Curiosité** : posez des questions sans cesse
- **Rigueur** : suivez une méthode systématique
- **Créativité** : explorez sous différents angles
- **Esprit critique** : questionnez tout

Rappelez-vous : **l'EDA n'est jamais vraiment terminée**. Même après avoir construit des modèles, vous reviendrez souvent explorer vos données sous de nouveaux angles.

> "The data may not contain the answer. The combination of some data and an aching desire for an answer does not ensure that a reasonable answer can be extracted from a given body of data." - John Tukey

## Ressources complémentaires

### Livres
- **"Exploratory Data Analysis"** - John Tukey (le livre fondateur)
- **"The Art of Data Science"** - Roger Peng & Elizabeth Matsui
- **"Python for Data Analysis"** - Wes McKinney (créateur de Pandas)

### Cours en ligne
- [Exploratory Data Analysis with Python](https://www.coursera.org/learn/exploratory-data-analysis-python) - Coursera
- [Data Analysis with Python](https://www.freecodecamp.org/) - FreeCodeCamp

### Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Datasets pour pratiquer
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

*"Exploratory data analysis can never be the whole story, but nothing else can serve as the foundation stone." - John Tukey*

⏭️ Retour au [Sommaire](/SOMMAIRE.md)
