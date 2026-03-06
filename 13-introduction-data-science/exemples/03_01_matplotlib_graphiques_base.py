# ============================================================================
#   Section 13.3 / 13.3.1 : Visualisation avec Matplotlib / Graphiques de base
#   Description : Introduction visualisation, anatomie graphique, line plot,
#                 bar chart, scatter plot, histogramme, pie chart, subplots,
#                 styles, sauvegarde, exemple complet dashboard
#   Fichier source : 03-visualisation-matplotlib-plotly.md,
#                    03.1-graphiques-base-matplotlib.md
# ============================================================================

"""Graphiques de base avec Matplotlib."""

import matplotlib
matplotlib.use('Agg')  # Backend non-interactif pour execution sans affichage
import matplotlib.pyplot as plt
import numpy as np
import os

# Dossier de sortie pour les images
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_matplotlib')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# VERIFICATION INSTALLATION
# ============================================================
print("=" * 50)
print("VERIFICATION INSTALLATION")
print("=" * 50)

print(f"\n  Matplotlib version: {matplotlib.__version__}")


# ============================================================
# GRAPHIQUE EN LIGNE (LINE PLOT)
# ============================================================
print(f"\n{'=' * 50}")
print("GRAPHIQUE EN LIGNE")
print("=" * 50)

# --- Exemple simple ---
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Mon premier graphique')
plt.savefig(os.path.join(OUTPUT_DIR, '01_line_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  01_line_simple.png sauvegarde")

# --- Personnalisation ---
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label='sin(x)')
plt.plot(x, np.cos(x), color='red', linewidth=2, linestyle='--', label='cos(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fonctions trigonometriques')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, '02_line_trigo.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  02_line_trigo.png sauvegarde")


# ============================================================
# DIAGRAMME A BARRES (BAR CHART)
# ============================================================
print(f"\n{'=' * 50}")
print("DIAGRAMME A BARRES")
print("=" * 50)

# --- Barres verticales ---
categories = ['Produit A', 'Produit B', 'Produit C', 'Produit D']
valeurs = [23, 45, 56, 78]

plt.figure(figsize=(10, 6))
plt.bar(categories, valeurs, color='skyblue', edgecolor='navy')
plt.xlabel('Produits')
plt.ylabel('Ventes')
plt.title('Ventes par produit')
plt.savefig(os.path.join(OUTPUT_DIR, '03_bar_vertical.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  03_bar_vertical.png sauvegarde")

# --- Barres horizontales ---
plt.figure(figsize=(10, 6))
plt.barh(categories, valeurs, color='lightcoral')
plt.xlabel('Ventes')
plt.ylabel('Produits')
plt.title('Ventes par produit (horizontal)')
plt.savefig(os.path.join(OUTPUT_DIR, '04_bar_horizontal.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  04_bar_horizontal.png sauvegarde")

# --- Barres groupees ---
categories = ['Q1', 'Q2', 'Q3', 'Q4']
ventes_2023 = [20, 35, 30, 35]
ventes_2024 = [25, 32, 34, 40]

x = np.arange(len(categories))
largeur = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
barres1 = ax.bar(x - largeur/2, ventes_2023, largeur, label='2023', color='steelblue')
barres2 = ax.bar(x + largeur/2, ventes_2024, largeur, label='2024', color='orange')

ax.set_xlabel('Trimestre')
ax.set_ylabel('Ventes (en milliers)')
ax.set_title('Comparaison des ventes 2023 vs 2024')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.savefig(os.path.join(OUTPUT_DIR, '05_bar_groupees.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  05_bar_groupees.png sauvegarde")


# ============================================================
# NUAGE DE POINTS (SCATTER PLOT)
# ============================================================
print(f"\n{'=' * 50}")
print("NUAGE DE POINTS")
print("=" * 50)

# --- Exemple basique ---
np.random.seed(42)
x = np.random.rand(50) * 100
y = np.random.rand(50) * 100

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='purple', alpha=0.5, s=100)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Nuage de points')
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(OUTPUT_DIR, '06_scatter_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  06_scatter_simple.png sauvegarde")

# --- Couleurs et tailles variables ---
np.random.seed(42)
n = 50
x = np.random.rand(n) * 100
y = np.random.rand(n) * 100
couleurs = np.random.rand(n)
tailles = np.random.rand(n) * 1000

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=couleurs, s=tailles, alpha=0.5, cmap='viridis')
plt.colorbar(scatter, label='Intensite')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Nuage de points avec couleurs et tailles variables')
plt.savefig(os.path.join(OUTPUT_DIR, '07_scatter_avance.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  07_scatter_avance.png sauvegarde")


# ============================================================
# HISTOGRAMME
# ============================================================
print(f"\n{'=' * 50}")
print("HISTOGRAMME")
print("=" * 50)

# --- Exemple simple ---
np.random.seed(42)
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
plt.xlabel('Valeur')
plt.ylabel('Frequence')
plt.title("Histogramme d'une distribution normale")
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(OUTPUT_DIR, '08_hist_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  08_hist_simple.png sauvegarde")

# --- Histogrammes multiples ---
np.random.seed(42)
data1 = np.random.normal(100, 15, 1000)
data2 = np.random.normal(120, 15, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data1, bins=30, alpha=0.5, label='Groupe A', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Groupe B', color='red')
plt.xlabel('Valeur')
plt.ylabel('Frequence')
plt.title('Comparaison de deux distributions')
plt.legend()
plt.savefig(os.path.join(OUTPUT_DIR, '09_hist_multiples.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  09_hist_multiples.png sauvegarde")


# ============================================================
# DIAGRAMME CIRCULAIRE (PIE CHART)
# ============================================================
print(f"\n{'=' * 50}")
print("DIAGRAMME CIRCULAIRE")
print("=" * 50)

# --- Exemple simple ---
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Autres']
tailles = [30, 25, 20, 15, 10]

plt.figure(figsize=(8, 8))
plt.pie(tailles, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Langages de programmation les plus utilises')
plt.savefig(os.path.join(OUTPUT_DIR, '10_pie_simple.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  10_pie_simple.png sauvegarde")

# --- Avec personnalisation ---
couleurs = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(tailles, explode=explode, labels=labels, colors=couleurs,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Langages de programmation les plus utilises', fontsize=16)
plt.axis('equal')
plt.savefig(os.path.join(OUTPUT_DIR, '11_pie_personnalise.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"  11_pie_personnalise.png sauvegarde")


# ============================================================
# SUBPLOTS
# ============================================================
print(f"\n{'=' * 50}")
print("SUBPLOTS")
print("=" * 50)

np.random.seed(42)
x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Premier graphique (ligne)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Graphique en ligne')

# Deuxieme graphique (barres)
axes[0, 1].bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
axes[0, 1].set_title('Diagramme a barres')

# Troisieme graphique (scatter)
axes[1, 0].scatter(np.random.rand(50), np.random.rand(50))
axes[1, 0].set_title('Nuage de points')

# Quatrieme graphique (histogramme)
axes[1, 1].hist(np.random.randn(1000), bins=30)
axes[1, 1].set_title('Histogramme')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '12_subplots.png'), dpi=100, bbox_inches='tight')
plt.close()
print(f"\n  12_subplots.png sauvegarde")


# ============================================================
# STYLES PREDEFINIES
# ============================================================
print(f"\n{'=' * 50}")
print("STYLES PREDEFINIS")
print("=" * 50)

styles_disponibles = plt.style.available
print(f"\n  Styles disponibles ({len(styles_disponibles)}):")
for s in styles_disponibles[:10]:
    print(f"    - {s}")
print(f"    ... ({len(styles_disponibles) - 10} autres)")

# Utilisation d'un style
with plt.style.context('ggplot'):
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x))
    plt.title('Graphique avec style ggplot')
    plt.savefig(os.path.join(OUTPUT_DIR, '13_style_ggplot.png'), dpi=100, bbox_inches='tight')
    plt.close()
print(f"  13_style_ggplot.png sauvegarde")


# ============================================================
# SAUVEGARDE
# ============================================================
print(f"\n{'=' * 50}")
print("SAUVEGARDE")
print("=" * 50)

x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x))
plt.title('Mon graphique')

plt.savefig(os.path.join(OUTPUT_DIR, '14_sauvegarde.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"\n  14_sauvegarde.png sauvegarde (dpi=300)")


# ============================================================
# EXEMPLE COMPLET : ANALYSE DE DONNEES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLE COMPLET : DASHBOARD VENTES")
print("=" * 50)

np.random.seed(42)
mois = ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun',
        'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec']
ventes = np.random.randint(50, 150, 12)
objectifs = np.full(12, 100)

print(f"\n  Ventes mensuelles: {list(ventes)}")
print(f"  Objectif: {objectifs[0]}")
print(f"  Moyenne ventes: {np.mean(ventes):.1f}")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Tableau de bord des ventes annuelles', fontsize=16, fontweight='bold')

# 1. Graphique en ligne : Evolution des ventes
axes[0, 0].plot(mois, ventes, marker='o', linewidth=2, color='steelblue', label='Ventes reelles')
axes[0, 0].plot(mois, objectifs, linestyle='--', color='red', label='Objectif')
axes[0, 0].set_title('Evolution mensuelle des ventes')
axes[0, 0].set_xlabel('Mois')
axes[0, 0].set_ylabel('Ventes')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 2. Diagramme a barres : Ventes par mois
couleurs_barres = ['green' if v >= 100 else 'orange' for v in ventes]
axes[0, 1].bar(mois, ventes, color=couleurs_barres, alpha=0.7)
axes[0, 1].axhline(y=100, color='red', linestyle='--', label='Objectif')
axes[0, 1].set_title('Ventes mensuelles')
axes[0, 1].set_xlabel('Mois')
axes[0, 1].set_ylabel('Ventes')
axes[0, 1].legend()

# 3. Histogramme : Distribution des ventes
axes[1, 0].hist(ventes, bins=8, color='purple', alpha=0.7, edgecolor='black')
axes[1, 0].axvline(x=np.mean(ventes), color='red', linestyle='--',
                   linewidth=2, label=f'Moyenne: {np.mean(ventes):.1f}')
axes[1, 0].set_title('Distribution des ventes')
axes[1, 0].set_xlabel('Ventes')
axes[1, 0].set_ylabel('Frequence')
axes[1, 0].legend()

# 4. Diagramme circulaire : Repartition par trimestre
q1 = sum(ventes[0:3])
q2 = sum(ventes[3:6])
q3 = sum(ventes[6:9])
q4 = sum(ventes[9:12])
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
ventes_trimestres = [q1, q2, q3, q4]
axes[1, 1].pie(ventes_trimestres, labels=trimestres, autopct='%1.1f%%',
               startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axes[1, 1].set_title('Repartition par trimestre')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '15_dashboard_complet.png'), dpi=150, bbox_inches='tight')
plt.close()

print(f"\n  Ventes par trimestre: Q1={q1}, Q2={q2}, Q3={q3}, Q4={q4}")
print(f"  Total annuel: {sum(ventes)}")
print(f"  Mois au-dessus de l'objectif: {sum(1 for v in ventes if v >= 100)}/{len(ventes)}")
print(f"\n  15_dashboard_complet.png sauvegarde")

# --- Resume des fichiers generes ---
print(f"\n{'=' * 50}")
print("RESUME")
print("=" * 50)
fichiers = sorted(os.listdir(OUTPUT_DIR))
print(f"\n  {len(fichiers)} fichiers generes dans {OUTPUT_DIR}:")
for f in fichiers:
    taille = os.path.getsize(os.path.join(OUTPUT_DIR, f))
    print(f"    - {f} ({taille:,} bytes)")
