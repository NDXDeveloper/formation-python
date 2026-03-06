# ============================================================================
#   Section 7.3 : Les modules math, random et statistics
#   Description : Module math avancé - puissances, racines, logarithmes,
#                 trigonométrie, gcd/lcm/factorial/comb/perm, hypot
#   Fichier source : 03-math-random-statistics.md
# ============================================================================

import math

# --- Puissances et racines ---
print("=== Puissances et racines ===")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"sqrt(2) = {math.sqrt(2)}")
print(f"pow(2, 3) = {math.pow(2, 3)}")
print(f"pow(5, 2) = {math.pow(5, 2)}")
print(f"2 ** 3 = {2 ** 3}")
print(f"cbrt(27) = {math.cbrt(27)}")
print(f"27 ** (1/3) = {27 ** (1/3)}")
print(f"exp(1) = {math.exp(1)}")
print(f"exp(2) = {math.exp(2)}")
print(f"expm1(0.001) = {math.expm1(0.001)}")

# --- Intérêts composés ---
print("\n=== Intérêts composés ===")

def calculer_interets_composes(capital, taux_annuel, duree_annees):
    capital_final = capital * math.pow(1 + taux_annuel, duree_annees)
    interets = capital_final - capital
    return {
        'capital_initial': capital,
        'capital_final': round(capital_final, 2),
        'interets': round(interets, 2)
    }

resultat = calculer_interets_composes(10000, 0.03, 10)
print(f"Capital initial : {resultat['capital_initial']} EUR")
print(f"Capital final : {resultat['capital_final']} EUR")
print(f"Intérêts gagnés : {resultat['interets']} EUR")

# --- Logarithmes ---
print("\n=== Logarithmes ===")
print(f"log(e) = {math.log(math.e)}")
print(f"log(10) = {math.log(10)}")
print(f"log10(100) = {math.log10(100)}")
print(f"log10(1000) = {math.log10(1000)}")
print(f"log2(8) = {math.log2(8)}")
print(f"log2(1024) = {math.log2(1024)}")
print(f"log(8, 2) = {math.log(8, 2)}")
print(f"log(81, 3) = {math.log(81, 3)}")
print(f"log1p(0.001) = {math.log1p(0.001)}")

# --- Trigonométrie ---
print("\n=== Trigonométrie ===")

angle_degres = 90
angle_radians = math.radians(angle_degres)
print(f"{angle_degres} deg = {angle_radians} radians")

angle_radians = math.pi / 2
angle_degres = math.degrees(angle_radians)
print(f"{angle_radians} radians = {angle_degres} deg")

print(f"\nsin(pi/2) = {math.sin(math.pi / 2)}")
print(f"cos(pi) = {math.cos(math.pi)}")
print(f"tan(pi/4) = {math.tan(math.pi / 4):.10f}")

print(f"asin(1) = {math.asin(1)}")
print(f"acos(0) = {math.acos(0)}")
print(f"atan(1) = {math.atan(1)}")

print(f"atan2(1, 1) = {math.atan2(1, 1)}")
print(f"atan2(-1, 1) = {math.atan2(-1, 1)}")

print(f"\nsinh(1) = {math.sinh(1):.4f}")
print(f"cosh(0) = {math.cosh(0)}")
print(f"tanh(1) = {math.tanh(1):.4f}")

# --- Distance euclidienne ---
print("\n=== Distance entre deux points ===")

def distance_euclidienne(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angle_entre_points(x1, y1, x2, y2):
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(angle_rad)

point_a = (0, 0)
point_b = (3, 4)
distance = distance_euclidienne(*point_a, *point_b)
angle = angle_entre_points(*point_a, *point_b)
print(f"Distance A{point_a} -> B{point_b} : {distance:.2f}")
print(f"Angle : {angle:.2f} deg")

# --- Autres fonctions ---
print("\n=== Autres fonctions ===")
print(f"gcd(48, 18) = {math.gcd(48, 18)}")
print(f"gcd(100, 35) = {math.gcd(100, 35)}")
print(f"lcm(12, 18) = {math.lcm(12, 18)}")
print(f"lcm(4, 6, 8) = {math.lcm(4, 6, 8)}")
print(f"factorial(5) = {math.factorial(5)}")
print(f"factorial(0) = {math.factorial(0)}")
print(f"comb(5, 2) = {math.comb(5, 2)}")
print(f"perm(5, 2) = {math.perm(5, 2)}")

nombres = [0.1] * 10
print(f"\nsum([0.1]*10) = {sum(nombres)}")
print(f"fsum([0.1]*10) = {math.fsum(nombres)}")
print(f"prod([2, 3, 4]) = {math.prod([2, 3, 4])}")
print(f"hypot(3, 4) = {math.hypot(3, 4)}")
print(f"hypot(5, 12) = {math.hypot(5, 12)}")

# --- Probabilités (loto) ---
print("\n=== Probabilités (Loto) ===")
total_combinaisons = math.comb(49, 5)
print(f"Combinaisons au loto (5/49) : {total_combinaisons:,}")
print(f"Probabilité : 1/{total_combinaisons:,}")
print(f"Soit : {(1/total_combinaisons)*100:.10f}%")

# --- Gestion d'erreurs ---
print("\n=== Gestion d'erreurs ===")
try:
    resultat = math.log(0)
except ValueError as e:
    print(f"log(0) -> ValueError : {e}")

print(f"type(sqrt(4)) = {type(math.sqrt(4))}")
