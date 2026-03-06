# Exemples du chapitre 13 : Introduction a la Data Science

Ce dossier contient les fichiers d'exemples executables pour le chapitre 13.

## Fichiers

### 01_01_numpy_arrays_operations.py
- **Section** : 13.1 / 13.1.1 - Calcul numerique avec NumPy / Arrays et operations
- **Fichier source** : `01-calcul-numerique-numpy.md`, `01.1-arrays-et-operations-vectorisees.md`
- **Description** : Introduction NumPy, comparaison performance liste vs array, creation d'arrays (zeros, ones, arange, linspace, eye, random), proprietes (shape, ndim, size, dtype), operations vectorisees, fonctions mathematiques (sqrt, exp, log, sin), agregations (sum, mean, std, median sur axes), broadcasting, conditions et masques booleens, exemples pratiques (temperatures, normalisation, finance, signal)
- **Sortie attendue** :
  - Performance NumPy vs liste Python (acceleration ~10-50x)
  - Memoire: array NumPy plus compact que liste Python
  - Somme totale matrice 3x3: 45, somme par colonne: [12 15 18], somme par ligne: [6 15 24]
  - Broadcasting: matrice + vecteur correctement calcule
  - Temperatures Fahrenheit: [32, 50, 68, 77, 86, 95, 104]
  - Signal sinusoidal: 100 points generes

### 01_02_numpy_indexation_slicing.py
- **Section** : 13.1.2 - Indexation et slicing avances
- **Fichier source** : `01.2-indexation-slicing-avances.md`
- **Description** : Indexation 1D/2D, slicing, indexation par liste d'indices, indexation booleenne (conditions simples et multiples), modification avec indexation, indexation fancy (np.ix_, diagonale), fonctions utiles (where, argmax, argmin, nonzero), vues vs copies, exemples pratiques (normalisation min-max, remplacement outliers, scores etudiants, grille meshgrid)
- **Sortie attendue** :
  - Indexation: premier element=10, dernier=-1, matrice[0,2]=3
  - Slicing: arr[2:5]=[20 30 40], arr inverse=[90 80 ... 0]
  - Indexation booleenne: valeurs > 20 correctement filtrees
  - Vues: modification de la vue modifie l'original
  - Copies: modification de la copie ne modifie pas l'original
  - Normalisation: valeurs entre 0.0 et 1.0
  - Etudiants d'elite (moyenne > 85): lignes correctement filtrees

### 02_01_pandas_dataframes_series.py
- **Section** : 13.2 / 13.2.1 - Manipulation de donnees avec Pandas / DataFrames et Series
- **Fichier source** : `02-manipulation-donnees-pandas.md`, `02.1-dataframes-et-series.md`
- **Description** : Series (creation depuis liste/dict/NumPy, acces iloc/label/slice, proprietes, operations arithmetiques, statistiques describe(), filtrage), DataFrames (creation depuis dict/liste/NumPy/Series, proprietes, head/tail, acces colonnes/lignes, loc/iloc, modification, filtrage avec conditions/isin/str.contains, tri), valeurs manquantes (isnull, dropna, fillna), groupby basique, exemples pratiques (analyse ventes, notes etudiants, tracker activite)
- **Sortie attendue** :
  - Series: 5 elements, dtype float64
  - DataFrame: shape (5,3), colonnes [Nom, Age, Ville]
  - Filtrage: ages > 30 correctement selectionnes
  - Valeurs manquantes: NaN detectes et remplaces par moyenne
  - GroupBy ventes: somme par produit calculee

### 02_02_pandas_nettoyage_transformation.py
- **Section** : 13.2.2 - Nettoyage et transformation
- **Fichier source** : `02.2-nettoyage-transformation.md`
- **Description** : Valeurs manquantes (detection, dropna, fillna avec constantes/stats/ffill/bfill/interpolation), doublons (duplicated, drop_duplicates), conversion de types (astype, to_numeric avec coerce, categories), methodes string (upper/lower/strip/contains/replace/split), dates (to_datetime, extraction composants, timedelta), renommage/reorganisation, apply/map/replace, pivot/melt/stack, concat/merge (inner/left/outer), exemples pratiques (nettoyage ventes, combinaison multi-sources)
- **Sortie attendue** :
  - Valeurs manquantes: 2 NaN detectes, remplaces par moyenne ~25
  - Doublons: 2 doublons supprimes
  - Conversion categories: reduction memoire significative
  - Methodes string: upper/lower/strip fonctionnent correctement
  - Dates: composants (annee, mois, jour_semaine) extraits
  - Merge: jointures inner/left/outer avec resultats corrects

### 02_03_pandas_groupby_agregations.py
- **Section** : 13.2.3 - GroupBy et agregations
- **Fichier source** : `02.3-groupby-et-agregations.md`
- **Description** : GroupBy de base (colonne unique, objet GroupBy, get_group, iteration), fonctions d'agregation (sum/mean/count/min/max/median), agregations multiples avec agg() (noms personnalises, fonctions custom), groupby multiples colonnes, transform (moyenne par groupe, rang), filter (seuil somme, seuil count), apply (statistiques personnalisees), valeurs manquantes dans groupby, MultiIndex, groupby par date, bins avec pd.cut, rolling par groupe, exemples pratiques (ventes regionales, notes etudiants, analyse RH)
- **Sortie attendue** :
  - Ventes par ville: Lyon=330, Marseille=90, Paris=330
  - Agregations multiples: sum, mean, min, max, count par ville
  - Transform: moyenne de chaque ville ajoutee comme colonne
  - Filter: villes avec ventes > 200 (Paris et Lyon)
  - Salaire moyen par departement: IT > Ventes > RH
  - Progression notes T1->T2 calculee par etudiant

### 03_01_matplotlib_graphiques_base.py
- **Section** : 13.3 / 13.3.1 - Visualisation avec Matplotlib / Graphiques de base
- **Fichier source** : `03-visualisation-matplotlib-plotly.md`, `03.1-graphiques-base-matplotlib.md`
- **Description** : Utilise le backend Agg (non-interactif). Line plots (simple, trigonometrique), bar charts (vertical, horizontal, groupes), scatter plots (simple, couleurs/tailles variables), histogrammes (simple, multiples), pie charts (simple, personnalise), subplots (grille 2x2), styles predefinis (ggplot), sauvegarde haute resolution, exemple complet dashboard ventes annuelles
- **Sortie attendue** :
  - 15 fichiers PNG generes dans `output_matplotlib/`
  - Styles disponibles: ~29 styles
  - Dashboard: ventes mensuelles aleatoires (seed=42), moyenne ~117.5
  - Ventes par trimestre: Q1=307, Q2=301, Q3=392, Q4=410
  - Mois au-dessus de l'objectif (100): 10/12

### 03_02_plotly_visualisations_interactives.py
- **Section** : 13.3.2 - Visualisations interactives avec Plotly
- **Fichier source** : `03.2-visualisations-interactives-plotly.md`
- **Description** : Plotly Express et Graph Objects. Line plots (simple, multi-lignes, markers), scatter plots (simple, couleurs/tailles, dataset Iris), bar charts (vertical, groupes, empiles, horizontal), histogrammes (simple, superposes), box plots, pie/donut charts, graphiques 3D (scatter 3D, surface 3D), heatmaps (simple, matrice correlation Iris), graphiques animes (Gapminder scatter, bar anime), subplots (facets Express, grille Graph Objects), personnalisation (themes, layout, annotations), integration Pandas, dashboard complet
- **Sortie attendue** :
  - 27 fichiers HTML generes dans `output_plotly/`
  - Dataset Iris: 150 lignes, 3 especes (setosa, versicolor, virginica)
  - Dataset Gapminder: 1704 lignes, 5 continents, annees 1952-2007
  - Correlation Iris: petal_length/petal_width = 0.963
  - Templates disponibles: plotly, plotly_dark, seaborn, simple_white, ggplot2...
  - Dashboard: ventes par region Nord=479, Sud=363, Est=340

### 04_analyse_exploratoire.py
- **Section** : 13.4 - Introduction a l'analyse exploratoire
- **Fichier source** : `04-analyse-exploratoire.md`
- **Description** : EDA complete sur datasets Iris et Titanic avec seaborn. Premieres observations (head/tail/sample/info/dtypes), valeurs manquantes (isnull, heatmap), doublons, statistiques descriptives (describe, moyenne/mediane/mode/std/variance/quartiles), variables categorielles (value_counts, proportions), mesures de forme (skewness, kurtosis), visualisations (histogrammes, KDE, box plots, violin plots, pairplot, bar plots, pie charts, scatter plots avec regression, heatmap correlation), detection outliers (IQR, Z-score), analyse par groupes, exemple complet Titanic (survie par sexe/classe/age, analyse croisee, correlations, insights)
- **Sortie attendue** :
  - Iris: 150 lignes, 5 colonnes, 0 valeurs manquantes, 1 doublon
  - sepal_length: moyenne=5.84, mediane=5.80, ecart-type=0.83
  - Skewness sepal_length: 0.31 (approximativement symetrique)
  - Outliers sepal_width (IQR): 4 outliers
  - Titanic: 891 lignes, 15 colonnes
  - Valeurs manquantes: age 19.9%, deck 77.2%
  - Taux de survie global: 38.38%
  - Femmes: 74% survie vs Hommes: 19%
  - Classe 1: 63%, Classe 2: 47%, Classe 3: 24%
  - 23 fichiers PNG generes dans `output_eda/`

## Dependances

```
numpy
pandas
matplotlib
plotly
seaborn
```

## Dossiers de sortie

Les fichiers de visualisation generent des sous-dossiers :
- `output_matplotlib/` : images PNG des graphiques Matplotlib (15 fichiers)
- `output_plotly/` : fichiers HTML interactifs Plotly (27 fichiers)
- `output_eda/` : images PNG de l'analyse exploratoire (23 fichiers)

## Execution

```bash
python3 01_01_numpy_arrays_operations.py
python3 01_02_numpy_indexation_slicing.py
python3 02_01_pandas_dataframes_series.py
python3 02_02_pandas_nettoyage_transformation.py
python3 02_03_pandas_groupby_agregations.py
python3 03_01_matplotlib_graphiques_base.py
python3 03_02_plotly_visualisations_interactives.py
python3 04_analyse_exploratoire.py
```
