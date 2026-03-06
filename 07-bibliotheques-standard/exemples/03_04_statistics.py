# ============================================================================
#   Section 7.3 : Les modules math, random et statistics
#   Description : Module statistics - mean, median, mode, variance, stdev,
#                 quantiles, corrélation, covariance, analyses pratiques
#   Fichier source : 03-math-random-statistics.md
# ============================================================================

import statistics
import random

# --- Moyenne ---
print("=== Moyenne ===")

donnees = [2, 4, 6, 8, 10]
print(f"Données : {donnees}")
print(f"Moyenne : {statistics.mean(donnees)}")

donnees_mixtes = [1, 2.5, 3, 4.5, 5]
print(f"Moyenne (mixtes) : {statistics.mean(donnees_mixtes)}")

donnees_geo = [2, 8]
print(f"Moyenne géométrique : {statistics.geometric_mean(donnees_geo)}")

vitesses = [30, 60, 90]
print(f"Moyenne harmonique : {statistics.harmonic_mean(vitesses):.2f}")

# --- Médiane ---
print("\n=== Médiane ===")

donnees_impaires = [1, 3, 5, 7, 9]
print(f"Médiane (impair) : {statistics.median(donnees_impaires)}")

donnees_paires = [1, 3, 5, 7, 9, 11]
print(f"Médiane (pair) : {statistics.median(donnees_paires)}")
print(f"Médiane basse : {statistics.median_low(donnees_paires)}")
print(f"Médiane haute : {statistics.median_high(donnees_paires)}")
print(f"Médiane groupée : {statistics.median_grouped(donnees_paires)}")

# --- Mode ---
print("\n=== Mode ===")

donnees_mode = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"Mode : {statistics.mode(donnees_mode)}")

couleurs = ["rouge", "bleu", "rouge", "vert", "rouge", "bleu"]
print(f"Couleur la plus fréquente : {statistics.mode(couleurs)}")

donnees_multimodales = [1, 1, 2, 2, 3]
print(f"Modes multiples : {statistics.multimode(donnees_multimodales)}")

# --- Analyse de salaires ---
print("\n=== Analyse de salaires ===")

salaires = [
    25000, 28000, 30000, 32000, 35000,
    38000, 40000, 42000, 45000, 50000,
    55000, 60000, 75000, 90000, 150000
]

print(f"Nombre d'employés : {len(salaires)}")
print(f"Salaire moyen : {statistics.mean(salaires):,.2f} EUR")
print(f"Salaire médian : {statistics.median(salaires):,.2f} EUR")
print(f"Salaire min : {min(salaires):,} EUR")
print(f"Salaire max : {max(salaires):,} EUR")

ecart = statistics.mean(salaires) - statistics.median(salaires)
print(f"Écart moyenne-médiane : {ecart:,.2f} EUR")
if ecart > 0:
    print("-> Quelques salaires élevés tirent la moyenne vers le haut")

# --- Variance et écart-type ---
print("\n=== Variance et écart-type ===")

donnees = [2, 4, 6, 8, 10]
print(f"Données : {donnees}")
print(f"Variance population : {statistics.pvariance(donnees)}")
print(f"Variance échantillon : {statistics.variance(donnees)}")
print(f"Écart-type population : {statistics.pstdev(donnees):.2f}")
print(f"Écart-type échantillon : {statistics.stdev(donnees):.2f}")

# --- Quantiles ---
print("\n=== Quantiles ===")

donnees = list(range(1, 101))
quartiles = statistics.quantiles(donnees, n=4)
print(f"Quartiles : {quartiles}")

deciles = statistics.quantiles(donnees, n=10)
print(f"Premier décile : {deciles[0]}")

percentiles = statistics.quantiles(donnees, n=100)
print(f"95e percentile : {percentiles[94]}")

# --- Analyse de performances ---
print("\n=== Analyse des temps de réponse ===")

random.seed(42)
temps_reponse = [random.gauss(100, 20) for _ in range(1000)]
temps_reponse.extend([300, 400, 500, 600, 800])

print(f"Nombre de requêtes : {len(temps_reponse)}")
print(f"Temps moyen : {statistics.mean(temps_reponse):.2f} ms")
print(f"Temps médian : {statistics.median(temps_reponse):.2f} ms")
print(f"Écart-type : {statistics.stdev(temps_reponse):.2f} ms")

quantiles = statistics.quantiles(temps_reponse, n=100)
print(f"P50 : {quantiles[49]:.2f} ms")
print(f"P90 : {quantiles[89]:.2f} ms")
print(f"P95 : {quantiles[94]:.2f} ms")
print(f"P99 : {quantiles[98]:.2f} ms")

moyenne = statistics.mean(temps_reponse)
ecart_type = statistics.stdev(temps_reponse)
seuil = moyenne + 3 * ecart_type
valeurs_aberrantes = [t for t in temps_reponse if t > seuil]
print(f"Valeurs aberrantes (>{seuil:.0f} ms) : {len(valeurs_aberrantes)}")

# --- Corrélation et covariance ---
print("\n=== Corrélation et covariance ===")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]  # y = 2x
z = [10, 8, 6, 4, 2]  # Diminue

print(f"Covariance(x, y) : {statistics.covariance(x, y)}")
print(f"Corrélation(x, y) : {statistics.correlation(x, y)}")
print(f"Corrélation(x, z) : {statistics.correlation(x, z)}")

# Corrélation température / ventes
temperatures = [15, 18, 22, 25, 28, 30, 32, 35, 38, 40]
ventes_glaces = [50, 65, 85, 110, 140, 160, 180, 210, 250, 280]

correlation = statistics.correlation(temperatures, ventes_glaces)
print(f"\nTempérature vs ventes de glaces :")
print(f"Corrélation : {correlation:.3f}")
if correlation > 0.7:
    print("-> Forte corrélation positive")
print(f"Température moyenne : {statistics.mean(temperatures):.1f} C")
print(f"Ventes moyennes : {statistics.mean(ventes_glaces):.0f} unités")

# --- Gestion d'erreurs ---
print("\n=== Gestion d'erreurs ===")

try:
    statistics.mean([])
except statistics.StatisticsError as e:
    print(f"mean([]) -> StatisticsError : {e}")
