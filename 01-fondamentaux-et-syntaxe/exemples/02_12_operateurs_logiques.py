# ============================================================================
#   Section 2.12 : Les Opérateurs Logiques
#   Description : and, or, not, tables de vérité, combinaisons, priorité
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Opérateur and (ET) ---
age = 25
a_permis = True

peut_conduire = age >= 18 and a_permis
print(peut_conduire)  # Affiche : True

# Table de vérité de AND
print(True and True)    # Affiche : True
print(True and False)   # Affiche : False
print(False and True)   # Affiche : False
print(False and False)  # Affiche : False

# --- Opérateur or (OU) ---
est_weekend = False
est_ferie = True

peut_se_reposer = est_weekend or est_ferie
print(peut_se_reposer)  # Affiche : True

# Table de vérité de OR
print(True or True)     # Affiche : True
print(True or False)    # Affiche : True
print(False or True)    # Affiche : True
print(False or False)   # Affiche : False

# --- Opérateur not (NON) ---
est_jour = True
est_nuit = not est_jour
print(est_nuit)  # Affiche : False

print(not True)   # Affiche : False
print(not False)  # Affiche : True

# --- Combiner plusieurs opérateurs ---
age = 25
a_permis = True
a_voiture = False

peut_conduire = age >= 18 and a_permis and a_voiture
print(peut_conduire)  # Affiche : False

# Avec parenthèses pour clarifier
est_weekend = True
a_argent = False
peut_sortir = est_weekend and (a_argent or not a_argent)  # Toujours vrai !
print(peut_sortir)  # Affiche : True

# --- Priorité des opérateurs logiques ---
# 1. not (priorité la plus élevée)
# 2. and
# 3. or (priorité la plus faible)
resultat = not False and True or False
# Évalué comme : ((not False) and True) or False
# → (True and True) or False
# → True or False
# → True
print(resultat)  # Affiche : True

# Plus clair avec parenthèses
resultat = ((not False) and True) or False
print(resultat)  # Affiche : True
