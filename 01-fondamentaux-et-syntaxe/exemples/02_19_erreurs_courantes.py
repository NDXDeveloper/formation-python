# ============================================================================
#   Section 2.19 : Erreurs Courantes à Éviter
#   Description : Confusion = et ==, oubli de conversion, division par zéro,
#                 noms non descriptifs
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Erreur 1 : Confondre = et == ---
x = 5

# Mauvais (SyntaxError) :
# if x = 5:       # Affectation au lieu de comparaison
#     print("x vaut 5")

# Bon :
if x == 5:        # Comparaison
    print("x vaut 5")  # Affiche : x vaut 5

# --- Erreur 2 : Oublier de convertir les types ---
# Simulé sans input() pour être exécutable
age = "25"  # Comme si on venait de input()
# annee = 2025 - age  # TypeError : on ne peut pas soustraire une string

# Bon :
annee = 2025 - int(age)
print(f"Année de naissance : {annee}")  # Affiche : Année de naissance : 2000

# --- Erreur 3 : Diviser par zéro ---
# resultat = 10 / 0  # ZeroDivisionError
print("10 / 0 provoquerait une ZeroDivisionError")

# --- Erreur 4 : Noms de variables non descriptifs ---
# Mauvais
x = 100
y = 0.20
z = x * (1 + y)

# Bon
prix_ht = 100
taux_tva = 0.20
prix_ttc = prix_ht * (1 + taux_tva)
print(f"Prix TTC : {prix_ttc}")  # Affiche : Prix TTC : 120.0
