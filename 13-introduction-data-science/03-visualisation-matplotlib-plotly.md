🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 13.3 Visualisation avec Matplotlib et Plotly

## Introduction à la visualisation de données

La visualisation de données est une compétence essentielle en Data Science et en programmation. Elle permet de :

- **Comprendre les données** : une image vaut mille mots, un bon graphique révèle des tendances invisibles dans les tableaux de chiffres
- **Communiquer des insights** : transmettre des informations complexes de manière claire et accessible
- **Détecter des anomalies** : identifier rapidement des valeurs aberrantes ou des comportements inattendus
- **Prendre des décisions** : aider à la prise de décision basée sur les données
- **Raconter une histoire** : construire un récit cohérent autour des données

En Python, deux bibliothèques dominent le domaine de la visualisation :
- **Matplotlib** : la bibliothèque historique et la plus complète
- **Plotly** : la bibliothèque moderne pour des visualisations interactives

## Pourquoi la visualisation est-elle importante ?

### 1. Le cerveau humain et les visuels

Notre cerveau traite les informations visuelles **60 000 fois plus rapidement** que le texte. Face à un tableau de milliers de lignes de données, il est quasiment impossible de détecter des patterns. Un graphique bien conçu révèle instantanément :
- Des tendances (hausse, baisse, stagnation)
- Des corrélations entre variables
- Des distributions de données
- Des valeurs extrêmes ou anomalies

### 2. Le quartet d'Anscombe : un exemple célèbre

Le quartet d'Anscombe est un ensemble de quatre jeux de données qui ont des propriétés statistiques presque identiques :
- Même moyenne
- Même variance
- Même corrélation
- Même ligne de régression

Pourtant, quand on les visualise, ces quatre datasets sont **complètement différents** ! C'est la preuve qu'on ne peut pas se fier uniquement aux statistiques sans visualiser les données.

```python
# Les quatre datasets ont les mêmes statistiques...
# Moyenne X ≈ 9.0
# Moyenne Y ≈ 7.5
# Corrélation ≈ 0.816

# Mais leurs graphiques révèlent des patterns totalement différents :
# Dataset 1 : relation linéaire classique
# Dataset 2 : relation non-linéaire (parabolique)
# Dataset 3 : relation linéaire avec une valeur aberrante
# Dataset 4 : pas de relation sauf un point extrême
```

**La leçon** : toujours visualiser vos données avant de les analyser !

## Les deux piliers de la visualisation en Python

### Matplotlib : La fondation

**Matplotlib** est la bibliothèque de visualisation la plus ancienne et la plus utilisée en Python. Créée en 2003, elle s'inspire de MATLAB.

**Points forts :**
- ✅ Très complète et mature
- ✅ Contrôle total sur chaque élément du graphique
- ✅ Parfaite pour les publications scientifiques
- ✅ Génère des images de haute qualité
- ✅ Large communauté et documentation extensive
- ✅ Compatible avec NumPy et Pandas

**Points faibles :**
- ❌ Syntaxe parfois complexe
- ❌ Graphiques statiques par défaut
- ❌ Style "daté" sans personnalisation
- ❌ Courbe d'apprentissage plus raide

**Cas d'usage typiques :**
- Rapports et publications scientifiques
- Graphiques pour des présentations imprimées
- Visualisations nécessitant une personnalisation extrême
- Intégration dans des scripts automatisés

### Plotly : La modernité

**Plotly** est une bibliothèque moderne (2012) qui se concentre sur l'interactivité et l'esthétique.

**Points forts :**
- ✅ Graphiques interactifs natifs (zoom, survol, filtrage)
- ✅ Interface simple avec Plotly Express
- ✅ Design moderne et professionnel
- ✅ Parfait pour les dashboards web
- ✅ Animations intégrées
- ✅ Excellent pour l'exploration de données

**Points faibles :**
- ❌ Peut être lent avec de très grandes quantités de données
- ❌ Moins de contrôle fin que Matplotlib
- ❌ Nécessite un navigateur pour l'interactivité

**Cas d'usage typiques :**
- Dashboards interactifs
- Présentations dynamiques
- Applications web
- Exploration de données
- Visualisations 3D

## Comparaison rapide

| Critère | Matplotlib | Plotly |
|---------|-----------|--------|
| **Année de création** | 2003 | 2012 |
| **Type** | Statique | Interactif |
| **Facilité d'utilisation** | Moyenne | Facile (Express) |
| **Qualité visuelle** | Bonne (avec config) | Excellente (native) |
| **Personnalisation** | Totale | Bonne |
| **Performance** | Très rapide | Bonne |
| **Export** | PNG, PDF, SVG | HTML, PNG, PDF |
| **Courbe d'apprentissage** | Moyenne | Facile |
| **Utilisation web** | Complexe | Native |
| **Taille de la communauté** | Très grande | Grande |

## Quand utiliser quelle bibliothèque ?

### Utilisez Matplotlib si :
- Vous avez besoin d'images statiques de haute qualité
- Vous créez des graphiques pour des publications scientifiques
- Vous avez besoin d'un contrôle très précis sur chaque élément
- Vous travaillez avec d'énormes volumes de données
- Vous voulez intégrer des graphiques dans des scripts automatisés
- Vous créez des types de graphiques très spécialisés

### Utilisez Plotly si :
- Vous créez des dashboards interactifs
- Vous voulez permettre l'exploration des données par l'utilisateur
- Vous faites des présentations dynamiques
- Vous développez une application web
- Vous voulez des graphiques "prêts à l'emploi" rapidement
- Vous créez des visualisations 3D complexes
- Vous voulez des animations

### L'approche hybride : le meilleur des deux mondes

En pratique, beaucoup de data scientists utilisent **les deux bibliothèques** en fonction du contexte :

```python
# Pour l'exploration rapide : Plotly Express
import plotly.express as px  
fig = px.scatter(df, x='age', y='salaire', color='departement')  
fig.show()  # Interactif, parfait pour explorer  

# Pour le rapport final : Matplotlib
import matplotlib.pyplot as plt  
plt.figure(figsize=(10, 6))  
plt.scatter(df['age'], df['salaire'])  
plt.savefig('rapport.png', dpi=300)  # Image haute qualité  
```

## Les types de graphiques essentiels

Quelle que soit la bibliothèque, vous devez maîtriser ces types de graphiques fondamentaux :

### 1. Graphique en ligne (Line Plot)
**Quand l'utiliser :** Évolution dans le temps, tendances  
**Exemple :** Cours de bourse, température sur une année, croissance d'une entreprise  

### 2. Diagramme à barres (Bar Chart)
**Quand l'utiliser :** Comparaison de catégories  
**Exemple :** Ventes par produit, population par pays, résultats d'enquête  

### 3. Nuage de points (Scatter Plot)
**Quand l'utiliser :** Relations entre deux variables continues  
**Exemple :** Taille vs poids, prix vs surface d'un logement, âge vs revenu  

### 4. Histogramme
**Quand l'utiliser :** Distribution d'une variable  
**Exemple :** Distribution des âges, des salaires, des notes d'examen  

### 5. Diagramme circulaire (Pie Chart)
**Quand l'utiliser :** Proportions d'un tout (avec parcimonie !)  
**Exemple :** Parts de marché, répartition du budget  

### 6. Box Plot (Boîte à moustaches)
**Quand l'utiliser :** Comparer des distributions, détecter des outliers  
**Exemple :** Salaires par département, temps de réponse par serveur  

### 7. Heatmap (Carte de chaleur)
**Quand l'utiliser :** Matrices, corrélations, données tabulaires  
**Exemple :** Matrice de corrélation, calendrier d'activité  

## Principes de base d'une bonne visualisation

Avant de plonger dans le code, voici les principes fondamentaux pour créer des visualisations efficaces :

### 1. La simplicité avant tout
> "La perfection est atteinte non quand il n'y a plus rien à ajouter, mais quand il n'y a plus rien à retirer." - Antoine de Saint-Exupéry

- Évitez les éléments décoratifs inutiles
- Un graphique = une idée principale
- Supprimez tout ce qui ne contribue pas à la compréhension

### 2. Choisir le bon type de graphique

| Objectif | Type de graphique recommandé |
|----------|----------------------------|
| Montrer une évolution | Ligne |
| Comparer des valeurs | Barres |
| Montrer une relation | Nuage de points |
| Montrer une distribution | Histogramme, Box plot |
| Montrer des proportions | Barres empilées, (rarement) Pie chart |
| Montrer des corrélations | Heatmap, Nuage de points |

### 3. Les couleurs avec sagesse
- Utilisez des couleurs ayant une signification (rouge = alerte, vert = positif)
- Limitez le nombre de couleurs (3-5 maximum)
- Pensez aux daltoniens (évitez rouge/vert seul)
- Utilisez des palettes professionnelles (ColorBrewer, Viridis)

### 4. Toujours étiqueter
Un graphique sans labels est inutile :
- **Titre** : Que montre ce graphique ?
- **Axes** : Quelles variables ? Quelles unités ?
- **Légende** : Que représentent les couleurs/symboles ?
- **Source** : D'où viennent ces données ?

### 5. Adapter à votre audience
- **Audience technique** : graphiques détaillés, multiples variables
- **Audience générale** : graphiques simples, message clair
- **Présentation** : grands titres, peu de texte
- **Rapport** : détails, annotations, contexte

## Structure de ce chapitre

Ce chapitre est divisé en deux parties complémentaires :

### 13.3.1 Graphiques de base avec Matplotlib
Vous apprendrez :
- Installation et configuration de Matplotlib
- L'anatomie d'un graphique (Figure, Axes, Axis)
- Les graphiques essentiels : ligne, barres, scatter, histogramme, pie chart
- La création de subplots (plusieurs graphiques)
- La personnalisation : couleurs, styles, labels, légendes
- La sauvegarde de graphiques
- Les bonnes pratiques
- Un exemple complet d'analyse de données

### 13.3.2 Visualisations interactives avec Plotly
Vous apprendrez :
- Installation et les deux interfaces (Express et Graph Objects)
- Les graphiques interactifs de base
- Les graphiques avancés : 3D, heatmaps, animations
- La création de dashboards
- La personnalisation et les thèmes
- L'export et le partage
- L'intégration web
- Comparaison avec Matplotlib

## Prérequis

Avant de commencer ce chapitre, vous devriez être à l'aise avec :

- **Python de base** : variables, boucles, fonctions
- **NumPy** : arrays et opérations de base (section 13.1)
- **Pandas** : DataFrames et manipulation de données (section 13.2)

Si vous ne connaissez pas encore NumPy et Pandas, je vous recommande de les étudier d'abord car la visualisation s'appuie fortement sur ces bibliothèques.

## Installation des bibliothèques

Avant de commencer, installez les deux bibliothèques :

```bash
# Matplotlib
pip install matplotlib

# Plotly
pip install plotly

# Optionnel : pour exporter Plotly en images
pip install kaleido
```

Vérification de l'installation :

```python
# Test Matplotlib
import matplotlib  
print(f"Matplotlib version: {matplotlib.__version__}")  

# Test Plotly
import plotly  
print(f"Plotly version: {plotly.__version__}")  
```

## Votre premier graphique

### Avec Matplotlib

```python
import matplotlib.pyplot as plt

# Données simples
x = [1, 2, 3, 4, 5]  
y = [2, 4, 6, 8, 10]  

# Création du graphique
plt.plot(x, y)  
plt.xlabel('X')  
plt.ylabel('Y')  
plt.title('Mon premier graphique Matplotlib')  
plt.show()  
```

### Avec Plotly

```python
import plotly.express as px

# Données simples
x = [1, 2, 3, 4, 5]  
y = [2, 4, 6, 8, 10]  

# Création du graphique
fig = px.line(x=x, y=y, title='Mon premier graphique Plotly',
              labels={'x': 'X', 'y': 'Y'})
fig.show()  # S'ouvre dans le navigateur, interactif !
```

**Différence visible immédiatement :**
- Matplotlib : image statique, simple
- Plotly : graphique interactif, moderne, tooltips au survol

## Conseils pour apprendre efficacement

1. **Pratiquez avec vos propres données** : utilisez des données qui vous intéressent (sport, finance, météo, etc.)

2. **Consultez les galeries d'exemples** :
   - [Galerie Matplotlib](https://matplotlib.org/stable/gallery/index.html)
   - [Galerie Plotly](https://plotly.com/python/)

3. **Copiez et modifiez** : trouvez un exemple proche de ce que vous voulez, puis adaptez-le

4. **Itérez** : votre premier graphique sera simple, améliorez-le progressivement

5. **Demandez des retours** : montrez vos visualisations à d'autres et écoutez leurs commentaires

## La visualisation est un art ET une science

Créer de bonnes visualisations nécessite :
- **Des compétences techniques** : maîtriser les outils (Matplotlib, Plotly)
- **Une compréhension des données** : savoir ce que vous voulez montrer
- **Un sens esthétique** : rendre le graphique agréable à regarder
- **De l'empathie** : comprendre ce que votre audience a besoin de voir

Comme toute compétence, cela s'améliore avec la pratique. Ne vous découragez pas si vos premiers graphiques ne sont pas parfaits !

## Ressources complémentaires

### Livres recommandés
- **"Storytelling with Data"** de Cole Nussbaumer Knaflic
- **"The Visual Display of Quantitative Information"** de Edward Tufte
- **"Python Data Science Handbook"** de Jake VanderPlas

### Sites web utiles
- [From Data to Viz](https://www.data-to-viz.com/) - Guide pour choisir le bon graphique
- [ColorBrewer](https://colorbrewer2.org/) - Palettes de couleurs
- [Python Graph Gallery](https://python-graph-gallery.com/) - Exemples de code

### Communautés
- [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/) - Inspiration
- [Stack Overflow](https://stackoverflow.com/questions/tagged/matplotlib) - Questions techniques

## Conclusion de l'introduction

La visualisation de données est une compétence essentielle qui transforme des nombres bruts en insights compréhensibles. Que vous choisissiez Matplotlib pour sa puissance et sa précision, ou Plotly pour son interactivité et sa modernité, vous avez entre les mains des outils extraordinaires.

Dans les sections suivantes, nous allons explorer en détail chacune de ces bibliothèques, en commençant par les fondamentaux de Matplotlib, puis en découvrant la magie de l'interactivité avec Plotly.

**Prêt à créer vos premières visualisations ?** Commençons par Matplotlib dans la section 13.3.1 !

---

*"The simple graph has brought more information to the data analyst's mind than any other device."* — John Tukey, mathématicien et statisticien

⏭️ [Graphiques de base avec Matplotlib](/13-introduction-data-science/03.1-graphiques-base-matplotlib.md)
