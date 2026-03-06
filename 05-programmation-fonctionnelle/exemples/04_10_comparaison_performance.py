# ============================================================================
#   Section 5.4 : Comparaison listes vs générateurs et performances
#   Description : Quand utiliser une liste vs un générateur,
#                 comparaison de consommation mémoire
#   Fichier source : 04-generateurs.md
# ============================================================================

import sys

# --- Comparaison de performance mémoire ---
print("=== Comparaison mémoire ===")

# Liste : toutes les valeurs en mémoire
liste = [i for i in range(1000000)]
print(f"Liste : {sys.getsizeof(liste) / 1024 / 1024:.2f} MB")

# Générateur : seulement l'objet générateur
gen = (i for i in range(1000000))
print(f"Générateur : {sys.getsizeof(gen) / 1024:.2f} KB")

# --- Les générateurs s'épuisent ---
print("\n=== Épuisement ===")

gen = (x for x in range(5))

# Premier parcours : fonctionne
print(list(gen))  # [0, 1, 2, 3, 4]

# Deuxième parcours : vide !
print(list(gen))  # []

# Solution : recréer le générateur
gen = (x for x in range(5))
print(list(gen))  # [0, 1, 2, 3, 4]

# --- Erreur courante : consommer puis réutiliser ---
print("\n=== Erreur courante ===")

# Mauvaise approche
gen = (x for x in range(5))
somme = sum(gen)
liste = list(gen)  # Vide !
print(f"Somme : {somme}, Liste : {liste}")

# Bonne approche
gen = (x for x in range(5))
liste = list(gen)  # Convertir d'abord
somme = sum(liste)
print(f"Somme : {somme}, Liste : {liste}")

# --- Accès par index ---
print("\n=== Accès par index ===")

gen = (x for x in range(10))

# Les générateurs ne supportent pas l'indexation
try:
    print(gen[5])
except TypeError as e:
    print(f"Erreur : {e}")

# Solution : convertir en liste
liste = list(x for x in range(10))
print(f"Element 5 : {liste[5]}")

# --- Longueur ---
print("\n=== Longueur ===")

gen = (x for x in range(10))

# Pas de len() pour les générateurs
try:
    print(len(gen))
except TypeError as e:
    print(f"Erreur : {e}")

# Solution : convertir en liste
liste = list(x for x in range(10))
print(f"Longueur : {len(liste)}")
