# ============================================================================
#   Section 5.7 : Lever une exception avec raise
#   Description : Déclencher volontairement une exception, relancer
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Lever une exception ---
def calculer_racine_carree(nombre):
    if nombre < 0:
        raise ValueError("Impossible de calculer la racine d'un nombre négatif")
    return nombre ** 0.5

try:
    resultat = calculer_racine_carree(-4)
except ValueError as e:
    print(f"Erreur : {e}")

# Cas valide
resultat = calculer_racine_carree(25)
print(f"Racine de 25 = {resultat}")  # 5.0

# --- Relancer une exception ---
print()

def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Log : tentative de division par zéro")
        raise  # Relance la même exception

try:
    diviser(10, 0)
except ZeroDivisionError:
    print("Exception relancée et capturée ici")
