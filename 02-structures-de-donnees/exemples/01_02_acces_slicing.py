# ============================================================================
#   Section 2.1 : Les Listes - Accéder aux éléments et slicing
#   Description : Index positif/négatif, tranches (slicing) avec début:fin:pas
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Accès par index ---
fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# Accès par index positif
print(fruits[0])   # 'pomme' (premier élément)
print(fruits[2])   # 'orange'

# Accès par index négatif
print(fruits[-1])  # 'kiwi' (dernier élément)
print(fruits[-2])  # 'fraise' (avant-dernier)

# --- Slicing (tranches) ---
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntaxe : liste[début:fin:pas]
print(nombres[2:5])      # [2, 3, 4] (de l'index 2 à 4)
print(nombres[:3])       # [0, 1, 2] (du début jusqu'à l'index 2)
print(nombres[5:])       # [5, 6, 7, 8, 9] (de l'index 5 jusqu'à la fin)
print(nombres[::2])      # [0, 2, 4, 6, 8] (tous les 2 éléments)
print(nombres[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverse la liste)
