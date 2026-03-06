# ============================================================================
#   Section 5.1 : Fonctions lambda - Syntaxe de base
#   Description : Comparaison fonction classique vs lambda, doubler, est_pair,
#                 concaténer, maximum
#   Fichier source : 01-lambda-et-fonctions-ordre-superieur.md
# ============================================================================

# --- Comparaison fonction classique vs lambda ---
print("=== Classique vs lambda ===")

def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # 8

additionner_lambda = lambda a, b: a + b
resultat = additionner_lambda(5, 3)
print(resultat)  # 8

# --- Doubler un nombre ---
print("\n=== Doubler ===")

doubler = lambda x: x * 2
print(doubler(5))   # 10
print(doubler(12))  # 24

# --- Vérifier si pair ---
print("\n=== Est pair ===")

est_pair = lambda n: n % 2 == 0
print(est_pair(4))   # True
print(est_pair(7))   # False

# --- Concaténer ---
print("\n=== Saluer ===")

saluer = lambda prenom, nom: f"Bonjour {prenom} {nom} !"
print(saluer("Marie", "Dupont"))  # Bonjour Marie Dupont !

# --- Maximum ---
print("\n=== Maximum ===")

maximum = lambda a, b: a if a > b else b
print(maximum(10, 25))  # 25
print(maximum(50, 30))  # 50
