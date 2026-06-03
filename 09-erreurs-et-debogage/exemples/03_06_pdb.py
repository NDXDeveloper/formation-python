# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Le debogueur pdb - points d'arret avec breakpoint(),
#                 inspection de variables pas a pas
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

import os

# Ce fichier contient de VRAIS appels breakpoint() (points d'arret pdb).
# Par defaut, on les NEUTRALISE pour qu'il s'execute d'un seul trait :
os.environ.setdefault("PYTHONBREAKPOINT", "0")
#
# Pour deboguer reellement pas a pas, lancez :
#     PYTHONBREAKPOINT=1 python 03_06_pdb.py
# puis utilisez les commandes pdb a l'invite (Pdb) :
#     n (next)  s (step)  c (continue)  p variable (print)
#     l (list)  w (where)  q (quit)

# ==========================================
# 1. Point d'arret avec breakpoint()
# ==========================================
print("=== pdb : breakpoint() ===\n")

def calculer_prix_total(prix_unitaire, quantite, taux_tva):
    breakpoint()  # neutralise par defaut ; ouvre pdb si PYTHONBREAKPOINT=1
    prix_ht = prix_unitaire * quantite
    montant_tva = prix_ht * taux_tva
    prix_ttc = prix_ht + montant_tva
    return prix_ttc

resultat = calculer_prix_total(100, 3, 0.20)
print(f"  Prix total : {resultat}EUR")

# ==========================================
# 2. Inspecter une boucle pas a pas
# ==========================================
print("\n=== pdb : inspecter une boucle ===\n")

def calculer_factorielle(n):
    resultat = 1
    breakpoint()  # ex. de commandes : p resultat, n (next), c (continue)
    for i in range(1, n + 1):
        resultat *= i
    return resultat

print(f"  factorielle(5) = {calculer_factorielle(5)}")
