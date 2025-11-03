🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 13.2 Manipulation de données avec Pandas

## Introduction

Bienvenue dans le monde de la manipulation de données avec **Pandas** ! Si NumPy est le fondement du calcul numérique en Python, Pandas est la bibliothèque de référence pour l'analyse et la manipulation de données structurées. Son nom vient de "Panel Data" (données de panel), un terme d'économétrie, et de "Python Data Analysis".

Pandas est devenue l'outil incontournable pour les data scientists, les analystes de données, et tous ceux qui travaillent avec des données tabulaires en Python.

## Qu'est-ce que Pandas ?

Pandas est une bibliothèque open-source qui fournit des structures de données puissantes et des outils d'analyse pour Python. Elle est particulièrement adaptée pour :

- **Données tabulaires** : comme des feuilles de calcul Excel ou des tables de bases de données
- **Séries temporelles** : données horodatées avec fréquence régulière ou irrégulière
- **Données étiquetées** : chaque ligne et colonne peut avoir un nom
- **Données hétérogènes** : les colonnes peuvent contenir différents types de données

### Petite histoire

Pandas a été créée en 2008 par Wes McKinney alors qu'il travaillait chez AQR Capital Management, un fonds d'investissement quantitatif. Il avait besoin d'un outil performant pour analyser des données financières. Le projet est devenu open-source en 2009 et est aujourd'hui maintenu par une large communauté.

En 2017, Wes McKinney a publié le livre "Python for Data Analysis", devenu une référence pour apprendre Pandas.

## Pourquoi utiliser Pandas ?

### 1. Manipulation de données intuitive

Pandas rend la manipulation de données aussi simple qu'avec Excel, mais avec la puissance du code :

```python
import pandas as pd

# Imaginez que vous avez un tableau de ventes
ventes = pd.DataFrame({
    'Produit': ['Laptop', 'Souris', 'Clavier', 'Écran'],
    'Prix': [800, 25, 60, 250],
    'Quantité': [10, 50, 30, 15]
})

# Calculer le total en une ligne
ventes['Total'] = ventes['Prix'] * ventes['Quantité']

# Filtrer les produits chers
produits_chers = ventes[ventes['Prix'] > 100]

print(produits_chers)
```

### 2. Lecture et écriture de multiples formats

Pandas peut lire et écrire de nombreux formats de fichiers :

```python
# Lire depuis différents formats
df_csv = pd.read_csv('donnees.csv')
df_excel = pd.read_excel('donnees.xlsx')
df_json = pd.read_json('donnees.json')
df_sql = pd.read_sql('SELECT * FROM table', connection)
df_html = pd.read_html('https://example.com/table.html')

# Écrire vers différents formats
df.to_csv('sortie.csv', index=False)
df.to_excel('sortie.xlsx', sheet_name='Données')
df.to_json('sortie.json')
df.to_sql('table_name', connection)
df.to_html('sortie.html')
```

### 3. Nettoyage de données efficace

Les données réelles sont rarement propres. Pandas facilite leur nettoyage :

```python
# Gérer les valeurs manquantes
df.dropna()  # Supprimer les lignes avec valeurs manquantes
df.fillna(0)  # Remplir les valeurs manquantes avec 0

# Supprimer les doublons
df.drop_duplicates()

# Changer les types de données
df['Date'] = pd.to_datetime(df['Date'])

# Renommer les colonnes
df.rename(columns={'ancien_nom': 'nouveau_nom'})
```

### 4. Analyses puissantes

Pandas offre des fonctions d'analyse statistique intégrées :

```python
# Statistiques descriptives
print(df.describe())

# Grouper et agréger
ventes_par_ville = df.groupby('Ville')['Ventes'].sum()

# Pivoter les données
pivot = df.pivot_table(values='Ventes', index='Mois', columns='Produit')

# Fusionner des DataFrames
resultat = pd.merge(clients, commandes, on='client_id')
```

### 5. Intégration avec l'écosystème Python

Pandas s'intègre parfaitement avec d'autres bibliothèques :

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Utiliser NumPy avec Pandas
df['log_values'] = np.log(df['values'])

# Visualiser directement depuis Pandas
df['Ventes'].plot()
plt.show()

# Compatible avec scikit-learn pour le Machine Learning
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target])
```

## Installation de Pandas

### Avec pip (recommandé)

```bash
pip install pandas
```

Pandas sera installé avec ses dépendances principales (NumPy, python-dateutil, pytz).

### Avec conda

```bash
conda install pandas
```

### Dépendances optionnelles

Pour certaines fonctionnalités, vous aurez besoin de bibliothèques supplémentaires :

```bash
# Pour lire/écrire Excel
pip install openpyxl xlrd

# Pour lire HTML
pip install lxml html5lib beautifulsoup4

# Pour le clipboard
pip install pyperclip

# Pour de meilleures performances
pip install bottleneck numexpr
```

### Vérifier l'installation

```python
import pandas as pd
print("Version de Pandas:", pd.__version__)

# Afficher les informations de configuration
pd.show_versions()
```

## Importation de Pandas

Par convention universelle, Pandas est importé avec l'alias `pd` :

```python
import pandas as pd
import numpy as np  # Souvent utilisé ensemble
```

**Pourquoi `pd` ?**
- C'est la convention standard dans toute la communauté
- Rend le code plus concis
- Facilite le partage et la lecture de code

**❌ À éviter :**
```python
from pandas import *  # Pollue l'espace de noms
import pandas          # Trop long à écrire
```

**✅ Recommandé :**
```python
import pandas as pd
```

## Vue d'ensemble des concepts Pandas

### Les deux structures principales

Pandas repose sur deux structures de données fondamentales :

#### 1. Series (1D)
Une Series est comme une colonne d'un tableur - un tableau unidimensionnel étiqueté.

```python
# Exemple de Series
temperatures = pd.Series([15, 18, 22, 20, 17],
                         index=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'])
print(temperatures)
```

**Sortie :**
```
Lundi        15
Mardi        18
Mercredi     22
Jeudi        20
Vendredi     17
dtype: int64
```

#### 2. DataFrame (2D)
Un DataFrame est comme un tableur complet - un tableau bidimensionnel avec des lignes et des colonnes étiquetées.

```python
# Exemple de DataFrame
employes = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Âge': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille'],
    'Salaire': [35000, 42000, 48000]
})
print(employes)
```

**Sortie :**
```
       Nom  Âge       Ville  Salaire
0    Alice   25       Paris    35000
1      Bob   30        Lyon    42000
2  Charlie   35  Marseille    48000
```

### Analogies utiles

Pour mieux comprendre Pandas :

- **Series** ≈ Colonne Excel / Liste Python avec étiquettes
- **DataFrame** ≈ Feuille Excel / Table SQL / Dictionnaire de listes
- **Index** ≈ Numéros de lignes dans Excel (mais peut être personnalisé)
- **Colonnes** ≈ En-têtes de colonnes dans Excel

## Premier programme avec Pandas

Créons un petit programme qui illustre les capacités de Pandas :

```python
import pandas as pd
import numpy as np

# Créer des données de ventes
ventes = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=7, freq='D'),
    'Produit': ['Laptop', 'Souris', 'Clavier', 'Écran', 'Webcam', 'Casque', 'Clavier'],
    'Prix': [800, 25, 60, 250, 80, 50, 65],
    'Quantité': [2, 10, 5, 3, 4, 8, 3],
    'Ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon', 'Paris', 'Marseille']
})

print("=== Données de ventes ===")
print(ventes)

# Calculer le montant total
ventes['Montant'] = ventes['Prix'] * ventes['Quantité']

# Statistiques de base
print("\n=== Statistiques ===")
print(f"Chiffre d'affaires total: {ventes['Montant'].sum()}€")
print(f"Vente moyenne: {ventes['Montant'].mean():.2f}€")
print(f"Nombre de transactions: {len(ventes)}")

# Ventes par ville
print("\n=== Ventes par ville ===")
ventes_par_ville = ventes.groupby('Ville')['Montant'].sum().sort_values(ascending=False)
print(ventes_par_ville)

# Produits les plus vendus
print("\n=== Top 3 des produits ===")
top_produits = ventes.groupby('Produit')['Montant'].sum().nlargest(3)
print(top_produits)

# Filtrer les ventes > 200€
print("\n=== Ventes importantes (>200€) ===")
ventes_importantes = ventes[ventes['Montant'] > 200][['Date', 'Produit', 'Montant']]
print(ventes_importantes)
```

## Comparaison : Excel vs Pandas

Comprendre comment Pandas se compare à Excel aide à saisir ses avantages :

| Opération | Excel | Pandas |
|-----------|-------|--------|
| **Ouvrir un fichier** | Clic sur le fichier | `pd.read_excel('fichier.xlsx')` |
| **Filtrer des lignes** | Menu Données > Filtrer | `df[df['Colonne'] > 100]` |
| **Créer une colonne** | Formule =A1*B1 | `df['Nouvelle'] = df['A'] * df['B']` |
| **Calculer une somme** | =SOMME(A:A) | `df['Colonne'].sum()` |
| **Tableau croisé** | Insertion > Tableau croisé | `df.pivot_table()` |
| **Supprimer doublons** | Données > Supprimer doublons | `df.drop_duplicates()` |
| **Trier** | Données > Trier | `df.sort_values('Colonne')` |

### Avantages d'Excel

- Interface graphique intuitive
- Pas de code nécessaire
- Visualisation immédiate
- Facile pour les non-programmeurs
- Parfait pour de petites analyses rapides

### Avantages de Pandas

- **Automatisation** : Répétez l'analyse sur de nouveaux fichiers sans effort
- **Volumétrie** : Gère des millions de lignes (Excel limité à ~1M)
- **Reproductibilité** : Le code documente exactement ce qui a été fait
- **Puissance** : Opérations complexes en quelques lignes
- **Version control** : Code versionnable avec Git
- **Performance** : Beaucoup plus rapide sur de gros volumes

### Quand utiliser quoi ?

**Utilisez Excel quand :**
- Vous avez moins de 100 000 lignes
- C'est une analyse ponctuelle
- Vous voulez un résultat visuel rapide
- Vous partagez avec des non-programmeurs

**Utilisez Pandas quand :**
- Vous avez plus de 100 000 lignes
- Vous répétez l'analyse régulièrement
- Vous devez automatiser le processus
- Vous travaillez avec plusieurs sources de données
- Vous voulez une analyse reproductible

## Cas d'usage de Pandas

### 1. Analyse financière

```python
# Analyser des données boursières
stocks = pd.read_csv('stocks.csv', parse_dates=['Date'])
stocks['Rendement'] = stocks['Close'].pct_change() * 100

# Calculer des moyennes mobiles
stocks['MA_50'] = stocks['Close'].rolling(window=50).mean()
stocks['MA_200'] = stocks['Close'].rolling(window=200).mean()

# Identifier des signaux d'achat/vente
stocks['Signal'] = np.where(stocks['MA_50'] > stocks['MA_200'], 'Achat', 'Vente')
```

### 2. Analyse marketing et CRM

```python
# Segmenter les clients
clients = pd.read_csv('clients.csv')

# Calculer la valeur vie client (CLV)
clv = clients.groupby('Client_ID').agg({
    'Montant_achat': 'sum',
    'Date_achat': 'count',
    'Date_derniere_visite': 'max'
})

# Créer des segments
clients['Segment'] = pd.cut(clients['Total_achats'],
                             bins=[0, 100, 500, 1000, float('inf')],
                             labels=['Bronze', 'Argent', 'Or', 'Platine'])
```

### 3. Analyse de données web

```python
# Analyser les logs web
logs = pd.read_csv('web_logs.csv')
logs['DateTime'] = pd.to_datetime(logs['DateTime'])

# Trafic par heure
trafic_horaire = logs.groupby(logs['DateTime'].dt.hour).size()

# Pages les plus visitées
pages_populaires = logs['URL'].value_counts().head(10)

# Taux de conversion par source
conversion = logs.groupby('Source')['Conversion'].mean() * 100
```

### 4. Analyse RH

```python
# Analyser les données RH
employes = pd.read_excel('employes.xlsx')

# Salaire moyen par département
sal_dept = employes.groupby('Département')['Salaire'].mean()

# Taux d'attrition
employes['Attrition'] = employes['Date_sortie'].notna()
taux_attrition = employes.groupby('Année')['Attrition'].mean() * 100

# Ancienneté moyenne
employes['Ancienneté'] = (pd.Timestamp.now() - employes['Date_embauche']).dt.days / 365
```

### 5. Analyse scientifique

```python
# Analyser des résultats d'expériences
experiences = pd.read_csv('resultats.csv')

# Statistiques par groupe
stats = experiences.groupby('Groupe').agg({
    'Mesure': ['mean', 'std', 'count'],
    'Efficacite': 'mean'
})

# Comparaison avant/après
resultats = experiences.pivot_table(
    values='Mesure',
    index='Sujet',
    columns='Phase',
    aggfunc='mean'
)
resultats['Amelioration'] = resultats['Apres'] - resultats['Avant']
```

## L'écosystème Pandas

Pandas s'intègre dans un écosystème riche de bibliothèques Python :

### Bibliothèques complémentaires

1. **NumPy** : Calculs numériques de base (Pandas est construit sur NumPy)
2. **Matplotlib / Seaborn** : Visualisation de données
3. **Plotly** : Visualisations interactives
4. **Scikit-learn** : Machine Learning
5. **Statsmodels** : Modèles statistiques
6. **SQLAlchemy** : Interface avec bases de données SQL
7. **Beautiful Soup / Scrapy** : Web scraping

### Flux de travail typique

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Charger les données
df = pd.read_csv('donnees.csv')

# 2. Explorer
print(df.head())
print(df.describe())
print(df.info())

# 3. Nettoyer
df = df.dropna()
df = df.drop_duplicates()
df['Date'] = pd.to_datetime(df['Date'])

# 4. Transformer
df['Log_value'] = np.log(df['Value'])
df_groupe = df.groupby('Categorie').mean()

# 5. Visualiser
df['Value'].plot(kind='hist')
plt.show()

# 6. Modéliser (avec scikit-learn)
X = df[['feature1', 'feature2']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Exporter
df.to_csv('resultats_clean.csv', index=False)
```

## Ressources et documentation

### Documentation officielle

- **Site officiel** : https://pandas.pydata.org/
- **Documentation** : https://pandas.pydata.org/docs/
- **Guide utilisateur** : https://pandas.pydata.org/docs/user_guide/index.html
- **API Reference** : https://pandas.pydata.org/docs/reference/index.html

### Apprendre Pandas

- **10 minutes to pandas** : Guide de démarrage rapide officiel
- **Pandas Cookbook** : Recettes pour des tâches courantes
- **Livre "Python for Data Analysis"** : Par Wes McKinney (créateur de Pandas)
- **Kaggle Learn** : Cours interactifs gratuits
- **Real Python** : Tutoriels détaillés

### Communauté

- **GitHub** : https://github.com/pandas-dev/pandas
- **Stack Overflow** : Tag `pandas` (questions très actives)
- **PyData** : Conférences et meetups
- **Twitter** : @pandas_dev

### Cheat Sheets

Des aide-mémoires PDF sont disponibles :
- Pandas Cheat Sheet (DataCamp)
- Pandas Basics Cheat Sheet (Pandas.pydata.org)
- Data Wrangling with pandas (Cheat Sheet)

## Conseils pour débuter

### 1. Commencez petit

Ne vous laissez pas intimider par toutes les fonctionnalités. Commencez par :
- Lire un fichier CSV
- Explorer avec `head()`, `describe()`, `info()`
- Sélectionner des colonnes
- Filtrer des lignes
- Faire des calculs simples

```python
# Programme débutant typique
df = pd.read_csv('donnees.csv')
print(df.head())
print(df['colonne'].mean())
resultat = df[df['colonne'] > 100]
```

### 2. Utilisez la documentation et l'auto-complétion

```python
# Dans un notebook Jupyter, utilisez ?
df.groupby?  # Affiche la documentation

# Utilisez l'auto-complétion avec Tab
df.gr[Tab]  # Affiche toutes les méthodes commençant par 'gr'
```

### 3. Explorez vos données

Prenez toujours le temps d'explorer avant d'analyser :

```python
# Ces 5 commandes vous donneront une bonne vue d'ensemble
print(df.head())        # Premières lignes
print(df.info())        # Types et valeurs manquantes
print(df.describe())    # Statistiques descriptives
print(df.shape)         # Dimensions
print(df.columns)       # Noms des colonnes
```

### 4. Évitez les boucles

Pandas est optimisé pour les opérations vectorisées :

```python
# ❌ Lent : boucle Python
for i in range(len(df)):
    df.loc[i, 'nouvelle_col'] = df.loc[i, 'col1'] * 2

# ✅ Rapide : opération vectorisée
df['nouvelle_col'] = df['col1'] * 2
```

### 5. Faites des copies quand nécessaire

```python
# ✅ Bon : créer une copie
df_filtre = df[df['colonne'] > 100].copy()
df_filtre['nouvelle'] = 123  # N'affecte pas df original

# ⚠️ Attention : vue, pas copie
df_vue = df[df['colonne'] > 100]
# Modifications peuvent affecter l'original
```

### 6. Chaînez les opérations

Pour un code plus lisible :

```python
# ✅ Bon : chaînage
resultat = (df
    .query('Valeur > 100')
    .groupby('Categorie')
    .agg({'Ventes': 'sum'})
    .sort_values('Ventes', ascending=False)
    .head(10)
)

# Au lieu de :
df_filtre = df.query('Valeur > 100')
df_groupe = df_filtre.groupby('Categorie')
df_agg = df_groupe.agg({'Ventes': 'sum'})
df_trie = df_agg.sort_values('Ventes', ascending=False)
resultat = df_trie.head(10)
```

## Performance et bonnes pratiques

### 1. Choisir le bon type de données

```python
# Optimiser les types pour économiser de la mémoire
df['Categorie'] = df['Categorie'].astype('category')  # Au lieu de 'object'
df['Valeur_entiere'] = df['Valeur_entiere'].astype('int32')  # Au lieu de 'int64'
```

### 2. Lire par morceaux pour les gros fichiers

```python
# Pour les fichiers très volumineux
chunks = []
for chunk in pd.read_csv('gros_fichier.csv', chunksize=10000):
    # Traiter chaque chunk
    chunk_filtre = chunk[chunk['colonne'] > 100]
    chunks.append(chunk_filtre)

df = pd.concat(chunks, ignore_index=True)
```

### 3. Utiliser les index intelligemment

```python
# Définir un index approprié accélère les recherches
df.set_index('ID', inplace=True)

# Recherche rapide par index
resultat = df.loc[12345]  # Très rapide
```

### 4. Éviter les opérations coûteuses dans les boucles

```python
# ❌ Lent : agrandir un DataFrame dans une boucle
df = pd.DataFrame()
for i in range(10000):
    df = df.append({'A': i}, ignore_index=True)

# ✅ Rapide : créer une liste puis un DataFrame
data = []
for i in range(10000):
    data.append({'A': i})
df = pd.DataFrame(data)
```

## Structure de cette section

Cette section sur Pandas est organisée en trois parties principales :

### 13.2.1 DataFrames et Series
Vous apprendrez :
- Les deux structures de données fondamentales de Pandas
- Comment créer et manipuler des Series et DataFrames
- Accès, sélection et modification des données
- Opérations de base et statistiques

### 13.2.2 Nettoyage et transformation de données
Vous découvrirez :
- Gestion des valeurs manquantes et doublons
- Transformation de types de données
- Manipulation de chaînes de caractères et dates
- Renommage et réorganisation
- Fusion et concaténation de données

### 13.2.3 GroupBy et agrégations
Vous maîtriserez :
- Le concept Split-Apply-Combine
- Fonctions d'agrégation
- Groupements simples et multiples
- Transform, Filter et Apply
- Analyses par groupe

Ces trois sections vous donneront une base solide pour utiliser Pandas efficacement dans vos projets d'analyse de données, que ce soit pour le business, la science, ou tout autre domaine nécessitant la manipulation de données tabulaires.

## Conclusion de l'introduction

Pandas est un outil extraordinaire qui a révolutionné l'analyse de données en Python. Sa combinaison de puissance, de flexibilité et de simplicité en fait la bibliothèque de choix pour manipuler des données structurées.

**Points clés à retenir :**

1. **Pandas** = bibliothèque pour données tabulaires (comme Excel, mais en code)
2. **Deux structures** : Series (1D) et DataFrame (2D)
3. **Construit sur NumPy** : hérite de sa performance
4. **Très versatile** : lecture, nettoyage, transformation, analyse, export
5. **Bien intégré** : fonctionne avec tout l'écosystème Python

**Ce que vous gagnerez en apprenant Pandas :**

- Automatisation de tâches répétitives d'analyse
- Capacité à gérer de gros volumes de données
- Analyses reproductibles et documentées
- Compétence très recherchée dans l'industrie
- Base pour le Machine Learning et la Data Science

Dans les sections suivantes, nous allons plonger dans les détails pratiques de Pandas, en commençant par ses structures de données fondamentales : les DataFrames et les Series.

**Prêt à maîtriser Pandas ?** Passons maintenant à la section 13.2.1 pour explorer en profondeur les DataFrames et Series !

⏭️ [DataFrames et Series](/13-introduction-data-science/02.1-dataframes-et-series.md)
