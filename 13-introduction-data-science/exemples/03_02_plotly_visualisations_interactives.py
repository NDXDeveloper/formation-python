# ============================================================================
#   Section 13.3.2 : Visualisations interactives avec Plotly
#   Description : Plotly Express et Graph Objects, line/scatter/bar/histogram/
#                 box/pie charts, graphiques 3D, heatmaps, animations, subplots,
#                 personnalisation, themes, export HTML, integration Pandas
#   Fichier source : 03.2-visualisations-interactives-plotly.md
# ============================================================================

"""Visualisations interactives avec Plotly."""

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import numpy as np
import os

# Dossier de sortie pour les fichiers HTML
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_plotly')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# VERIFICATION INSTALLATION
# ============================================================
print("=" * 50)
print("VERIFICATION INSTALLATION")
print("=" * 50)

print(f"\n  Plotly version: {plotly.__version__}")


# ============================================================
# GRAPHIQUE EN LIGNE INTERACTIF
# ============================================================
print(f"\n{'=' * 50}")
print("GRAPHIQUE EN LIGNE INTERACTIF")
print("=" * 50)

# --- Exemple simple ---
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = px.line(x=x, y=y,
              title='Fonction sinus',
              labels={'x': 'Angle (radians)', 'y': 'sin(x)'})
fig.write_html(os.path.join(OUTPUT_DIR, '01_line_simple.html'))
print(f"\n  01_line_simple.html sauvegarde")

# --- Multi-lignes ---
x = np.linspace(0, 10, 100)
df = pd.DataFrame({
    'x': x,
    'sin': np.sin(x),
    'cos': np.cos(x),
    'tan': np.tan(x)
})

df_long = df.melt(id_vars='x', var_name='fonction', value_name='valeur')

fig = px.line(df_long, x='x', y='valeur', color='fonction',
              title='Fonctions trigonometriques',
              labels={'valeur': 'f(x)', 'x': 'Angle (radians)'})
fig.write_html(os.path.join(OUTPUT_DIR, '02_line_multi.html'))
print(f"  02_line_multi.html sauvegarde")

# --- Avec markers ---
x = np.arange(0, 10)
y = x ** 2

fig = px.line(x=x, y=y,
              markers=True,
              title='Fonction quadratique')
fig.update_traces(marker=dict(size=10))
fig.write_html(os.path.join(OUTPUT_DIR, '03_line_markers.html'))
print(f"  03_line_markers.html sauvegarde")


# ============================================================
# NUAGE DE POINTS (SCATTER PLOT)
# ============================================================
print(f"\n{'=' * 50}")
print("NUAGE DE POINTS")
print("=" * 50)

# --- Exemple basique ---
np.random.seed(42)
n = 100
x = np.random.rand(n) * 100
y = np.random.rand(n) * 100

fig = px.scatter(x=x, y=y,
                 title='Nuage de points interactif',
                 labels={'x': 'Variable X', 'y': 'Variable Y'})
fig.write_html(os.path.join(OUTPUT_DIR, '04_scatter_simple.html'))
print(f"\n  04_scatter_simple.html sauvegarde")

# --- Avec couleurs et tailles variables ---
np.random.seed(42)
n = 100
df = pd.DataFrame({
    'x': np.random.rand(n) * 100,
    'y': np.random.rand(n) * 100,
    'taille': np.random.rand(n) * 50,
    'categorie': np.random.choice(['A', 'B', 'C'], n)
})

fig = px.scatter(df, x='x', y='y',
                 size='taille',
                 color='categorie',
                 hover_data=['taille'],
                 title='Nuage de points avec couleurs et tailles')
fig.write_html(os.path.join(OUTPUT_DIR, '05_scatter_avance.html'))
print(f"  05_scatter_avance.html sauvegarde")

# --- Dataset Iris ---
df_iris = px.data.iris()

fig = px.scatter(df_iris, x='sepal_width', y='sepal_length',
                 color='species',
                 size='petal_length',
                 hover_data=['petal_width'],
                 title='Dataset Iris - Analyse multidimensionnelle')
fig.write_html(os.path.join(OUTPUT_DIR, '06_scatter_iris.html'))
print(f"  06_scatter_iris.html sauvegarde")
print(f"  Dataset Iris: {len(df_iris)} lignes, {len(df_iris.columns)} colonnes")
print(f"  Especes: {list(df_iris['species'].unique())}")


# ============================================================
# DIAGRAMMES A BARRES INTERACTIFS
# ============================================================
print(f"\n{'=' * 50}")
print("DIAGRAMMES A BARRES")
print("=" * 50)

# --- Barres verticales ---
produits = ['Produit A', 'Produit B', 'Produit C', 'Produit D', 'Produit E']
ventes = [23, 45, 56, 78, 34]

fig = px.bar(x=produits, y=ventes,
             title='Ventes par produit',
             labels={'x': 'Produits', 'y': 'Ventes (en milliers)'},
             color=ventes,
             color_continuous_scale='blues')
fig.write_html(os.path.join(OUTPUT_DIR, '07_bar_vertical.html'))
print(f"\n  07_bar_vertical.html sauvegarde")

# --- Barres groupees ---
df = pd.DataFrame({
    'Trimestre': ['Q1', 'Q2', 'Q3', 'Q4'] * 2,
    'Annee': ['2023', '2023', '2023', '2023', '2024', '2024', '2024', '2024'],
    'Ventes': [20, 35, 30, 35, 25, 32, 34, 40]
})

fig = px.bar(df, x='Trimestre', y='Ventes', color='Annee',
             barmode='group',
             title='Comparaison des ventes 2023 vs 2024')
fig.write_html(os.path.join(OUTPUT_DIR, '08_bar_groupees.html'))
print(f"  08_bar_groupees.html sauvegarde")

# --- Barres empilees ---
df = pd.DataFrame({
    'Mois': ['Jan', 'Fev', 'Mar', 'Avr'] * 3,
    'Region': ['Nord', 'Nord', 'Nord', 'Nord',
               'Sud', 'Sud', 'Sud', 'Sud',
               'Est', 'Est', 'Est', 'Est'],
    'Ventes': [10, 15, 12, 18, 8, 12, 14, 16, 12, 14, 11, 15]
})

fig = px.bar(df, x='Mois', y='Ventes', color='Region',
             barmode='stack',
             title='Ventes par region et par mois')
fig.write_html(os.path.join(OUTPUT_DIR, '09_bar_empilees.html'))
print(f"  09_bar_empilees.html sauvegarde")

# --- Barres horizontales ---
langages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP', 'TypeScript']
popularite = [29.9, 19.5, 17.3, 7.1, 6.7, 6.1, 3.0]

fig = px.bar(y=langages, x=popularite,
             orientation='h',
             title='Popularite des langages de programmation 2024',
             labels={'x': "Pourcentage d'utilisation", 'y': 'Langage'},
             color=popularite,
             color_continuous_scale='viridis')
fig.write_html(os.path.join(OUTPUT_DIR, '10_bar_horizontal.html'))
print(f"  10_bar_horizontal.html sauvegarde")


# ============================================================
# HISTOGRAMMES INTERACTIFS
# ============================================================
print(f"\n{'=' * 50}")
print("HISTOGRAMMES")
print("=" * 50)

# --- Simple ---
np.random.seed(42)
data = np.random.randn(1000)

fig = px.histogram(x=data,
                   nbins=50,
                   title='Distribution normale',
                   labels={'x': 'Valeur', 'y': 'Frequence'})
fig.write_html(os.path.join(OUTPUT_DIR, '11_hist_simple.html'))
print(f"\n  11_hist_simple.html sauvegarde")

# --- Superposes ---
np.random.seed(42)
df = pd.DataFrame({
    'valeur': np.concatenate([
        np.random.normal(100, 15, 500),
        np.random.normal(120, 15, 500)
    ]),
    'groupe': ['Groupe A'] * 500 + ['Groupe B'] * 500
})

fig = px.histogram(df, x='valeur', color='groupe',
                   nbins=30,
                   title='Comparaison de deux distributions',
                   barmode='overlay',
                   opacity=0.6)
fig.write_html(os.path.join(OUTPUT_DIR, '12_hist_superposes.html'))
print(f"  12_hist_superposes.html sauvegarde")


# ============================================================
# BOX PLOTS
# ============================================================
print(f"\n{'=' * 50}")
print("BOX PLOTS")
print("=" * 50)

np.random.seed(42)
df = pd.DataFrame({
    'Categorie': np.repeat(['A', 'B', 'C'], 100),
    'Valeurs': np.concatenate([
        np.random.normal(50, 10, 100),
        np.random.normal(60, 15, 100),
        np.random.normal(55, 8, 100)
    ])
})

fig = px.box(df, x='Categorie', y='Valeurs',
             title='Distribution des valeurs par categorie',
             color='Categorie')
fig.write_html(os.path.join(OUTPUT_DIR, '13_boxplot.html'))
print(f"\n  13_boxplot.html sauvegarde")
print(f"  Medianes: A={df[df['Categorie']=='A']['Valeurs'].median():.1f}, "
      f"B={df[df['Categorie']=='B']['Valeurs'].median():.1f}, "
      f"C={df[df['Categorie']=='C']['Valeurs'].median():.1f}")


# ============================================================
# DIAGRAMME CIRCULAIRE (PIE/DONUT)
# ============================================================
print(f"\n{'=' * 50}")
print("DIAGRAMME CIRCULAIRE")
print("=" * 50)

# --- Donut chart avec Express ---
langages = ['Python', 'JavaScript', 'Java', 'C++', 'Autres']
parts = [30, 25, 20, 15, 10]

fig = px.pie(values=parts, names=langages,
             title='Langages de programmation les plus utilises',
             hole=0.3)
fig.write_html(os.path.join(OUTPUT_DIR, '14_pie_donut.html'))
print(f"\n  14_pie_donut.html sauvegarde")

# --- Pie avec Graph Objects ---
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Autres']
values = [30, 25, 20, 15, 10]
colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']

fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    marker=dict(colors=colors),
    pull=[0.1, 0, 0, 0, 0],
    textinfo='label+percent',
    hoverinfo='label+value+percent'
)])

fig.update_layout(title='Langages de programmation')
fig.write_html(os.path.join(OUTPUT_DIR, '15_pie_go.html'))
print(f"  15_pie_go.html sauvegarde")


# ============================================================
# GRAPHIQUES 3D
# ============================================================
print(f"\n{'=' * 50}")
print("GRAPHIQUES 3D")
print("=" * 50)

# --- Scatter 3D ---
np.random.seed(42)
n = 200
df = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'z': np.random.randn(n),
    'couleur': np.random.rand(n)
})

fig = px.scatter_3d(df, x='x', y='y', z='z',
                    color='couleur',
                    title='Nuage de points 3D interactif')
fig.write_html(os.path.join(OUTPUT_DIR, '16_scatter_3d.html'))
print(f"\n  16_scatter_3d.html sauvegarde")

# --- Surface 3D ---
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='viridis')])
fig.update_layout(
    title='Surface 3D : sin(sqrt(x2 + y2))',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)
fig.write_html(os.path.join(OUTPUT_DIR, '17_surface_3d.html'))
print(f"  17_surface_3d.html sauvegarde")


# ============================================================
# HEATMAPS
# ============================================================
print(f"\n{'=' * 50}")
print("HEATMAPS")
print("=" * 50)

# --- Simple ---
np.random.seed(42)
data = np.random.rand(10, 10)

fig = px.imshow(data,
                labels=dict(x='Variable X', y='Variable Y', color='Valeur'),
                title='Carte de chaleur',
                color_continuous_scale='RdBu')
fig.write_html(os.path.join(OUTPUT_DIR, '18_heatmap_simple.html'))
print(f"\n  18_heatmap_simple.html sauvegarde")

# --- Matrice de correlation ---
df_iris = px.data.iris()

corr_matrix = df_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

fig = px.imshow(corr_matrix,
                labels=dict(color='Correlation'),
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                title='Matrice de correlation - Dataset Iris',
                color_continuous_scale='RdBu',
                zmin=-1, zmax=1,
                text_auto=True)
fig.write_html(os.path.join(OUTPUT_DIR, '19_heatmap_correlation.html'))
print(f"  19_heatmap_correlation.html sauvegarde")
print(f"\n  Matrice de correlation Iris:\n{corr_matrix.round(3)}")


# ============================================================
# GRAPHIQUES ANIMES
# ============================================================
print(f"\n{'=' * 50}")
print("GRAPHIQUES ANIMES")
print("=" * 50)

# --- Scatter anime avec Gapminder ---
df_gap = px.data.gapminder()

fig = px.scatter(df_gap,
                 x='gdpPercap',
                 y='lifeExp',
                 size='pop',
                 color='continent',
                 hover_name='country',
                 log_x=True,
                 size_max=60,
                 animation_frame='year',
                 animation_group='country',
                 range_x=[100, 100000],
                 range_y=[25, 90],
                 title='Evolution mondiale : Esperance de vie vs PIB (1952-2007)')
fig.write_html(os.path.join(OUTPUT_DIR, '20_scatter_anime.html'))
print(f"\n  20_scatter_anime.html sauvegarde")
print(f"  Dataset Gapminder: {len(df_gap)} lignes, {len(df_gap.columns)} colonnes")
print(f"  Annees: {sorted(df_gap['year'].unique())}")
print(f"  Continents: {list(df_gap['continent'].unique())}")

# --- Bar chart anime ---
df_filtered = df_gap[df_gap['country'].isin(['China', 'India', 'United States',
                                              'Indonesia', 'Brazil', 'Pakistan',
                                              'Nigeria', 'Bangladesh', 'Russia', 'Japan'])]

fig = px.bar(df_filtered,
             x='pop',
             y='country',
             orientation='h',
             animation_frame='year',
             range_x=[0, 1.5e9],
             title='Evolution de la population des 10 pays les plus peuples')
fig.write_html(os.path.join(OUTPUT_DIR, '21_bar_anime.html'))
print(f"  21_bar_anime.html sauvegarde")


# ============================================================
# SUBPLOTS
# ============================================================
print(f"\n{'=' * 50}")
print("SUBPLOTS")
print("=" * 50)

# --- Facets avec Express ---
df_iris = px.data.iris()

fig = px.scatter(df_iris, x='sepal_width', y='sepal_length',
                 color='species',
                 facet_col='species',
                 title='Iris - Analyse par espece')
fig.write_html(os.path.join(OUTPUT_DIR, '22_facets.html'))
print(f"\n  22_facets.html sauvegarde")

# --- Subplots avec Graph Objects ---
np.random.seed(42)
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Ligne', 'Barres', 'Scatter', 'Histogramme')
)

# Graphique 1 : Ligne
x = np.linspace(0, 10, 100)
fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='sin(x)'),
              row=1, col=1)

# Graphique 2 : Barres
fig.add_trace(go.Bar(x=['A', 'B', 'C'], y=[3, 7, 2], name='Barres'),
              row=1, col=2)

# Graphique 3 : Scatter
fig.add_trace(go.Scatter(x=np.random.rand(50), y=np.random.rand(50),
                         mode='markers', name='Points'),
              row=2, col=1)

# Graphique 4 : Histogramme
fig.add_trace(go.Histogram(x=np.random.randn(500), name='Distribution'),
              row=2, col=2)

fig.update_layout(height=600, title_text='Tableau de bord multi-graphiques')
fig.write_html(os.path.join(OUTPUT_DIR, '23_subplots_go.html'))
print(f"  23_subplots_go.html sauvegarde")


# ============================================================
# PERSONNALISATION AVANCEE
# ============================================================
print(f"\n{'=' * 50}")
print("PERSONNALISATION AVANCEE")
print("=" * 50)

# --- Themes ---
print(f"\n  Templates disponibles: {list(pio.templates)}")

# --- Layout personnalise ---
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = px.line(x=x, y=y)
fig.update_layout(
    title={
        'text': 'Mon graphique personnalise',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': 'darkblue'}
    },
    xaxis_title='Axe X (unite)',
    yaxis_title='Axe Y (unite)',
    font=dict(family='Arial', size=14),
    plot_bgcolor='#f0f0f0',
    paper_bgcolor='white',
    hovermode='x unified',
    showlegend=True,
    legend=dict(
        x=1,
        y=1,
        bgcolor='rgba(255,255,255,0.8)'
    )
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig.write_html(os.path.join(OUTPUT_DIR, '24_personnalise.html'))
print(f"  24_personnalise.html sauvegarde")

# --- Annotations et formes ---
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

fig.add_annotation(
    x=np.pi/2, y=1,
    text='Maximum',
    showarrow=True,
    arrowhead=2,
    arrowcolor='red',
    font=dict(size=14, color='red')
)

fig.add_shape(
    type='rect',
    x0=0, y0=-0.5, x1=5, y1=0.5,
    fillcolor='lightgreen',
    opacity=0.2,
    line_width=0
)

fig.update_layout(title='Graphique avec annotations et formes')
fig.write_html(os.path.join(OUTPUT_DIR, '25_annotations.html'))
print(f"  25_annotations.html sauvegarde")


# ============================================================
# INTEGRATION PANDAS
# ============================================================
print(f"\n{'=' * 50}")
print("INTEGRATION PANDAS")
print("=" * 50)

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=365, freq='D')
df = pd.DataFrame({
    'date': dates,
    'ventes': np.cumsum(np.random.randn(365)) + 100,
    'visites': np.cumsum(np.random.randn(365)) + 500
})

fig = px.line(df, x='date', y=['ventes', 'visites'],
              title='Evolution des ventes et visites en 2024')
fig.write_html(os.path.join(OUTPUT_DIR, '26_pandas_integration.html'))
print(f"\n  26_pandas_integration.html sauvegarde")
print(f"  Ventes finales: {df['ventes'].iloc[-1]:.1f}")
print(f"  Visites finales: {df['visites'].iloc[-1]:.1f}")


# ============================================================
# EXEMPLE COMPLET : DASHBOARD INTERACTIF
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLE COMPLET : DASHBOARD INTERACTIF")
print("=" * 50)

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=12, freq='ME')
df = pd.DataFrame({
    'mois': [d.strftime('%b') for d in dates],
    'ventes': np.random.randint(50, 150, 12),
    'objectif': [100] * 12,
    'region_nord': np.random.randint(20, 60, 12),
    'region_sud': np.random.randint(15, 50, 12),
    'region_est': np.random.randint(10, 40, 12)
})

print(f"\n  Ventes mensuelles: {list(df['ventes'])}")

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Evolution des ventes mensuelles',
                    'Ventes vs Objectif',
                    'Distribution des ventes',
                    'Repartition par region'),
    specs=[[{'type': 'scatter'}, {'type': 'bar'}],
           [{'type': 'histogram'}, {'type': 'pie'}]]
)

# 1. Ligne : Evolution des ventes
fig.add_trace(
    go.Scatter(x=df['mois'], y=df['ventes'],
               mode='lines+markers',
               name='Ventes reelles',
               line=dict(color='blue', width=3)),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df['mois'], y=df['objectif'],
               mode='lines',
               name='Objectif',
               line=dict(color='red', dash='dash')),
    row=1, col=1
)

# 2. Barres : Comparaison ventes/objectif
colors = ['green' if v >= 100 else 'orange' for v in df['ventes']]
fig.add_trace(
    go.Bar(x=df['mois'], y=df['ventes'],
           name='Ventes',
           marker_color=colors),
    row=1, col=2
)

# 3. Histogramme : Distribution
fig.add_trace(
    go.Histogram(x=df['ventes'],
                 nbinsx=8,
                 name='Distribution',
                 marker_color='purple'),
    row=2, col=1
)

# 4. Pie : Repartition par region
regions = ['Nord', 'Sud', 'Est']
ventes_regions = [df['region_nord'].sum(),
                  df['region_sud'].sum(),
                  df['region_est'].sum()]
fig.add_trace(
    go.Pie(labels=regions, values=ventes_regions,
           hole=0.3),
    row=2, col=2
)

fig.update_layout(
    height=800,
    showlegend=True,
    title_text='Dashboard Commercial 2024',
    title_font_size=20
)

fig.update_xaxes(title_text='Mois', row=1, col=1)
fig.update_yaxes(title_text='Ventes', row=1, col=1)
fig.update_xaxes(title_text='Mois', row=1, col=2)
fig.update_yaxes(title_text='Ventes', row=1, col=2)
fig.update_xaxes(title_text='Ventes', row=2, col=1)
fig.update_yaxes(title_text='Frequence', row=2, col=1)

fig.write_html(os.path.join(OUTPUT_DIR, '27_dashboard_complet.html'))
print(f"\n  Ventes par region: Nord={ventes_regions[0]}, Sud={ventes_regions[1]}, Est={ventes_regions[2]}")
print(f"  Total: {sum(ventes_regions)}")
print(f"  27_dashboard_complet.html sauvegarde")


# --- Resume des fichiers generes ---
print(f"\n{'=' * 50}")
print("RESUME")
print("=" * 50)
fichiers = sorted(os.listdir(OUTPUT_DIR))
print(f"\n  {len(fichiers)} fichiers generes dans {OUTPUT_DIR}:")
for f in fichiers:
    taille = os.path.getsize(os.path.join(OUTPUT_DIR, f))
    print(f"    - {f} ({taille:,} bytes)")
