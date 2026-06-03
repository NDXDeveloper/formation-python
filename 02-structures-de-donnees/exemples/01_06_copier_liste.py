# ============================================================================
#   Section 2.1 : Les Listes - Copier une liste
#   Description : Référence vs copie, copy(), slicing [:], list(), deepcopy
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Mauvaise méthode : crée une référence
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] - liste1 est aussi modifiée !

# Bonnes méthodes pour copier
liste1 = [1, 2, 3]
liste2 = liste1.copy()
# ou
liste3 = liste1[:]
# ou
liste4 = list(liste1)

liste2.append(4)
print(liste1)  # [1, 2, 3] - liste1 n'est pas modifiée
print(liste2)  # [1, 2, 3, 4]
print(liste3)  # [1, 2, 3]
print(liste4)  # [1, 2, 3]

# --- Copie superficielle vs copie profonde ---
import copy

# copy() est superficielle : les sous-listes restent partagées
original = [[1, 2], [3, 4]]
copie = original.copy()
copie[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]] - l'original est touché !

# deepcopy copie en profondeur (sous-objets inclus)
original = [[1, 2], [3, 4]]
copie = copy.deepcopy(original)
copie[0].append(99)
print(original)  # [[1, 2], [3, 4]] - l'original est intact
