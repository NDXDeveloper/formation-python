# ============================================================================
#   Section 7.3 : Les modules math, random et statistics
#   Description : Module math - constantes, valeur absolue, arrondis,
#                 ceil/floor/trunc/round, calcul de facture
#   Fichier source : 03-math-random-statistics.md
# ============================================================================

import math

# --- Constantes ---
print("=== Constantes mathématiques ===")
print(f"Pi : {math.pi}")
print(f"e : {math.e}")
print(f"Tau : {math.tau}")
print(f"Infini : {math.inf}")
print(f"Infini négatif : {-math.inf}")
print(f"NaN : {math.nan}")

# --- Circonférence et aire ---
print("\n=== Cercle (rayon=5) ===")

def calculer_circonference(rayon):
    return 2 * math.pi * rayon

def calculer_aire(rayon):
    return math.pi * rayon ** 2

rayon = 5
print(f"Rayon : {rayon} cm")
print(f"Circonférence : {calculer_circonference(rayon):.2f} cm")
print(f"Aire : {calculer_aire(rayon):.2f} cm2")

# --- Valeur absolue et signe ---
print("\n=== Valeur absolue et signe ===")
print(f"fabs(-5.7) = {math.fabs(-5.7)}")
print(f"abs(-5.7) = {abs(-5.7)}")
print(f"copysign(5, -1) = {math.copysign(5, -1)}")
print(f"copysign(-5, 1) = {math.copysign(-5, 1)}")

# --- Arrondis et troncatures ---
print("\n=== Arrondis et troncatures ===")

print(f"ceil(3.2) = {math.ceil(3.2)}")
print(f"ceil(3.7) = {math.ceil(3.7)}")
print(f"ceil(-3.2) = {math.ceil(-3.2)}")

print(f"floor(3.2) = {math.floor(3.2)}")
print(f"floor(3.7) = {math.floor(3.7)}")
print(f"floor(-3.2) = {math.floor(-3.2)}")

print(f"trunc(3.7) = {math.trunc(3.7)}")
print(f"trunc(-3.7) = {math.trunc(-3.7)}")

print(f"round(3.4) = {round(3.4)}")
print(f"round(3.6) = {round(3.6)}")
print(f"round(3.456, 2) = {round(3.456, 2)}")

# Arrondi bancaire
print(f"round(3.5) = {round(3.5)}  (arrondi bancaire)")
print(f"round(4.5) = {round(4.5)}  (arrondi bancaire)")

# --- Calcul de facture ---
print("\n=== Calcul de facture ===")

def calculer_facture(prix_unitaire, quantite, taux_tva=0.20):
    montant_ht = prix_unitaire * quantite
    montant_tva = montant_ht * taux_tva
    montant_ttc = montant_ht + montant_tva
    montant_ttc = math.ceil(montant_ttc * 100) / 100
    return {
        'ht': round(montant_ht, 2),
        'tva': round(montant_tva, 2),
        'ttc': montant_ttc
    }

facture = calculer_facture(19.99, 3)
print(f"Montant HT : {facture['ht']} EUR")
print(f"TVA : {facture['tva']} EUR")
print(f"Montant TTC : {facture['ttc']} EUR")
