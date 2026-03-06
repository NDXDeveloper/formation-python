# ============================================================================
#   Section 5.4 : Avantages des générateurs
#   Description : Économie de mémoire, évaluation paresseuse (lazy),
#                 séquences infinies
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Économie de mémoire ---
print("=== Économie de mémoire ===")

# Avec une liste (tout en mémoire)
def creer_grands_nombres():
    """Crée une liste de 1 million de nombres."""
    return [i for i in range(1000000)]

liste = creer_grands_nombres()
print(f"Liste - Taille en mémoire : ~{liste.__sizeof__()} bytes")

# Avec un générateur (valeurs à la demande)
def generer_grands_nombres():
    """Génère 1 million de nombres à la demande."""
    for i in range(1000000):
        yield i

gen = generer_grands_nombres()
print(f"Générateur - Taille en mémoire : ~{gen.__sizeof__()} bytes")

# --- Évaluation paresseuse ---
print("\n=== Évaluation paresseuse ===")

def generer_avec_traitement(n):
    """Génère des nombres avec un traitement coûteux."""
    for i in range(n):
        print(f"  Traitement de {i}...")
        yield i * 2

gen = generer_avec_traitement(5)
print("Générateur créé")

print("\nItération :")
for valeur in gen:
    print(f"Reçu : {valeur}")
    if valeur >= 4:  # On peut s'arrêter tôt
        break

# --- Séquences infinies ---
print("\n=== Séquence infinie ===")

def compteur_infini(debut=0):
    """Génère une séquence infinie de nombres."""
    nombre = debut
    while True:
        yield nombre
        nombre += 1

compteur = compteur_infini(10)
for i, valeur in enumerate(compteur):
    print(valeur, end=" ")
    if i >= 9:  # Afficher seulement 10 valeurs
        break
# 10 11 12 13 14 15 16 17 18 19
print()
