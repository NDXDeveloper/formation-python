# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Itérateurs infinis - count, cycle, repeat,
#                 numérotation automatique avec GestionnaireID
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

import itertools

# --- count() ---
print("=== count() - Compteur infini ===")

compteur = itertools.count(10)
for i in range(5):
    print(f"  {next(compteur)}", end="")
print()

# Avec pas personnalisé
compteur_pas = itertools.count(0, 5)
print("Pas de 5 :", end="")
for i in range(4):
    print(f"  {next(compteur_pas)}", end="")
print()

# Avec floats
compteur_float = itertools.count(0.5, 0.5)
print("Floats :", end="")
for i in range(3):
    print(f"  {next(compteur_float)}", end="")
print()

# --- cycle() ---
print("\n=== cycle() - Cycle infini ===")

couleurs = itertools.cycle(['rouge', 'vert', 'bleu'])
for i in range(7):
    print(f"  {next(couleurs)}", end="")
print()

# --- repeat() ---
print("\n=== repeat() - Répéter ===")

repetition = itertools.repeat('salut', 3)
for mot in repetition:
    print(f"  {mot}", end="")
print()

# --- Numérotation automatique ---
print("\n=== GestionnaireID ===")

class GestionnaireID:
    """Génère des IDs uniques automatiquement"""
    def __init__(self, prefixe="ID", debut=1):
        self.prefixe = prefixe
        self.compteur = itertools.count(debut)

    def generer_id(self):
        return f"{self.prefixe}_{next(self.compteur):04d}"

gestionnaire = GestionnaireID("USER", 1)
for i in range(5):
    print(f"  {gestionnaire.generer_id()}")
