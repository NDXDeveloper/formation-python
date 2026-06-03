# ============================================================================
#   Section 5.5 : Piège de la liaison tardive (late binding)
#   Description : Une closure capture la variable, pas sa valeur ; conséquence
#                 dans une boucle, et les deux solutions classiques
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Le piège : toutes les closures partagent la même variable i ---
print("=== Piège (liaison tardive) ===")
fonctions = [lambda: i for i in range(3)]
print([f() for f in fonctions])   # [2, 2, 2] -- et non [0, 1, 2] !
# Au moment de l'appel, la boucle est finie et i vaut 2 pour toutes.

# --- Solution 1 : figer la valeur avec un argument par défaut ---
print("\n=== Solution 1 : argument par défaut ===")
fonctions = [lambda i=i: i for i in range(3)]
print([f() for f in fonctions])   # [0, 1, 2]

# --- Solution 2 : une fabrique (chaque appel crée une nouvelle portée) ---
print("\n=== Solution 2 : fabrique de fonctions ===")
def faire(i):
    return lambda: i

fonctions = [faire(i) for i in range(3)]
print([f() for f in fonctions])   # [0, 1, 2]
