# ============================================================================
#   Section 13.1 / 13.1.1 : Calcul numerique avec NumPy / Arrays et operations
#   Description : Introduction NumPy, creation d'arrays, proprietes, operations
#                 vectorisees, fonctions mathematiques, agregations, broadcasting,
#                 conditions et masques booleens, comparaison performance
#   Fichier source : 01-calcul-numerique-numpy.md, 01.1-arrays-et-operations-vectorisees.md
# ============================================================================

"""Arrays NumPy et operations vectorisees."""

import sys
import time
import numpy as np


# ============================================================
# INTRODUCTION ET PERFORMANCE
# ============================================================
print("=" * 50)
print("INTRODUCTION NUMPY - PERFORMANCE")
print("=" * 50)

# --- Performance : liste vs NumPy ---
liste = list(range(1000000))
debut = time.time()
resultat = [x * 2 for x in liste]
temps_liste = time.time() - debut
print(f"\n  Temps avec liste Python: {temps_liste:.4f} secondes")

arr = np.array(liste)
debut = time.time()
resultat = arr * 2
temps_numpy = time.time() - debut
print(f"  Temps avec NumPy: {temps_numpy:.4f} secondes")
print(f"  NumPy est {temps_liste/temps_numpy:.1f}x plus rapide!")

# --- Simplicite du code ---
print(f"\n  --- Simplicite ---")
liste1 = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
resultat_liste = []
for i in range(len(liste1)):
    resultat_liste.append(liste1[i] * liste2[i])
print(f"  Resultat avec boucle: {resultat_liste}")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
resultat_np = arr1 * arr2
print(f"  Resultat vectorise: {resultat_np}")

# --- Efficacite memoire ---
liste_python = list(range(10000))
taille_liste = sys.getsizeof(liste_python)

array_numpy = np.array(range(10000))
taille_array = array_numpy.nbytes

print(f"\n  Taille liste Python: {taille_liste} bytes")
print(f"  Taille array NumPy: {taille_array} bytes")
print(f"  NumPy utilise {taille_liste/taille_array:.1f}x moins de memoire")

# --- Version ---
print(f"\n  Version de NumPy: {np.__version__}")


# ============================================================
# CREATION D'ARRAYS
# ============================================================
print(f"\n{'=' * 50}")
print("CREATION D'ARRAYS")
print("=" * 50)

# --- A partir de listes ---
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"\n  Array 1D: {arr_1d}")

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"  Array 2D:\n{arr_2d}")

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(f"  Array 3D:\n{arr_3d}")

# --- Fonctions de creation ---
print(f"\n  --- Fonctions de creation ---")
zeros = np.zeros(5)
print(f"  Zeros: {zeros}")

ones = np.ones((3, 3))
print(f"  Ones:\n{ones}")

arange = np.arange(0, 10, 2)
print(f"  Arange: {arange}")

linspace = np.linspace(0, 1, 5)
print(f"  Linspace: {linspace}")

identity = np.eye(3)
print(f"  Identity:\n{identity}")

np.random.seed(42)
random_arr = np.random.random((2, 3))
print(f"  Random:\n{random_arr}")

# --- Types de donnees ---
print(f"\n  --- Types de donnees ---")
arr_int = np.array([1, 2, 3], dtype=np.int32)
print(f"  Type int32: {arr_int.dtype}")

arr_float = np.array([1.0, 2.5, 3.7], dtype=np.float64)
print(f"  Type float64: {arr_float.dtype}")

arr_bool = np.array([True, False, True], dtype=np.bool_)
print(f"  Type bool: {arr_bool.dtype}")


# ============================================================
# PROPRIETES DES ARRAYS
# ============================================================
print(f"\n{'=' * 50}")
print("PROPRIETES DES ARRAYS")
print("=" * 50)

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(f"\n  Shape: {arr.shape}")
print(f"  Ndim: {arr.ndim}")
print(f"  Size: {arr.size}")
print(f"  Dtype: {arr.dtype}")

# --- Dimensions ---
arr_1d = np.array([1, 2, 3, 4])
print(f"\n  Shape 1D: {arr_1d.shape}")
print(f"  Dimensions: {arr_1d.ndim}")

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"  Shape 2D: {arr_2d.shape}")
print(f"  Dimensions: {arr_2d.ndim}")

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(f"  Shape 3D: {arr_3d.shape}")
print(f"  Dimensions: {arr_3d.ndim}")


# ============================================================
# OPERATIONS VECTORISEES
# ============================================================
print(f"\n{'=' * 50}")
print("OPERATIONS VECTORISEES")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5])

print(f"\n  Addition (+5): {arr + 5}")
print(f"  Soustraction (-2): {arr - 2}")
print(f"  Multiplication (x3): {arr * 3}")
print(f"  Division (/2): {arr / 2}")
print(f"  Puissance (^2): {arr ** 2}")

# --- Operations entre arrays ---
print(f"\n  --- Operations entre arrays ---")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print(f"  Addition: {arr1 + arr2}")
print(f"  Multiplication: {arr1 * arr2}")
print(f"  Division: {arr2 / arr1}")


# ============================================================
# FONCTIONS MATHEMATIQUES UNIVERSELLES
# ============================================================
print(f"\n{'=' * 50}")
print("FONCTIONS MATHEMATIQUES")
print("=" * 50)

arr = np.array([1, 4, 9, 16, 25])
print(f"\n  Racine carree: {np.sqrt(arr)}")

arr2 = np.array([0, 1, 2])
print(f"  Exponentielle: {np.exp(arr2)}")

print(f"  Logarithme: {np.log(arr)}")

angles = np.array([0, np.pi/2, np.pi])
print(f"  Sinus: {np.sin(angles)}")


# ============================================================
# AGREGATIONS
# ============================================================
print(f"\n{'=' * 50}")
print("AGREGATIONS")
print("=" * 50)

arr = np.array([3, 7, 1, 9, 2, 8])

print(f"\n  Somme: {np.sum(arr)}")
print(f"  Moyenne: {np.mean(arr)}")
print(f"  Minimum: {np.min(arr)}")
print(f"  Maximum: {np.max(arr)}")
print(f"  Ecart-type: {np.std(arr):.10f}")
print(f"  Mediane: {np.median(arr)}")

# --- Agregations 2D ---
print(f"\n  --- Agregations 2D ---")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"  Somme totale: {np.sum(arr_2d)}")
print(f"  Somme par colonne: {np.sum(arr_2d, axis=0)}")
print(f"  Somme par ligne: {np.sum(arr_2d, axis=1)}")
print(f"  Moyenne par colonne: {np.mean(arr_2d, axis=0)}")


# ============================================================
# BROADCASTING
# ============================================================
print(f"\n{'=' * 50}")
print("BROADCASTING")
print("=" * 50)

matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

vecteur = np.array([10, 20, 30])

resultat = matrice + vecteur
print(f"\n  Resultat du broadcasting:\n{resultat}")

# --- Normalisation ---
print(f"\n  --- Normalisation ---")
notes = np.array([[85, 90, 78],
                  [92, 88, 95],
                  [78, 85, 88]])

moyennes = np.mean(notes, axis=0)
print(f"  Moyennes par examen: {moyennes}")

notes_centrees = notes - moyennes
print(f"  Notes centrees:\n{notes_centrees}")


# ============================================================
# CONDITIONS ET MASQUES BOOLEENS
# ============================================================
print(f"\n{'=' * 50}")
print("CONDITIONS ET MASQUES BOOLEENS")
print("=" * 50)

arr = np.array([1, 5, 10, 15, 20, 25])

masque = arr > 10
print(f"\n  Masque (valeurs > 10): {masque}")

valeurs_sup_10 = arr[masque]
print(f"  Valeurs > 10: {valeurs_sup_10}")

print(f"  Valeurs > 10 (concis): {arr[arr > 10]}")

arr_copie = arr.copy()
arr_copie[arr_copie < 10] = 0
print(f"  Array modifie (< 10 -> 0): {arr_copie}")

# --- Conditions multiples ---
print(f"\n  --- Conditions multiples ---")
arr = np.array([1, 5, 10, 15, 20, 25, 30])

masque = (arr >= 10) & (arr <= 20)
print(f"  Valeurs entre 10 et 20: {arr[masque]}")

masque2 = (arr < 10) | (arr > 20)
print(f"  Valeurs < 10 ou > 20: {arr[masque2]}")


# ============================================================
# EXEMPLES PRATIQUES
# ============================================================
print(f"\n{'=' * 50}")
print("EXEMPLES PRATIQUES")
print("=" * 50)

# --- Temperatures ---
print(f"\n  --- Conversion temperatures ---")
temperatures_celsius = np.array([0, 10, 20, 25, 30, 35, 40])
print(f"  Temperatures en Celsius: {temperatures_celsius}")

temperatures_fahrenheit = temperatures_celsius * 9/5 + 32
print(f"  Temperatures en Fahrenheit: {temperatures_fahrenheit}")

print(f"\n  --- Statistiques ---")
print(f"  Temperature moyenne: {np.mean(temperatures_celsius):.1f} C")
print(f"  Temperature minimale: {np.min(temperatures_celsius)} C")
print(f"  Temperature maximale: {np.max(temperatures_celsius)} C")
print(f"  Ecart-type: {np.std(temperatures_celsius):.2f} C")

jours_chauds = temperatures_celsius[temperatures_celsius > 25]
print(f"\n  Jours chauds (>25 C): {jours_chauds}")
print(f"  Nombre de jours chauds: {len(jours_chauds)}")

# --- Normalisation ---
print(f"\n  --- Normalisation de donnees ---")
donnees = np.array([10, 20, 30, 40, 50])
donnees_normalisees = (donnees - np.mean(donnees)) / np.std(donnees)
print(f"  Donnees normalisees: {donnees_normalisees}")

# --- Analyse financiere ---
print(f"\n  --- Analyse financiere ---")
prix = np.array([100, 102, 98, 105, 107])
rendements = (prix[1:] - prix[:-1]) / prix[:-1] * 100
print(f"  Rendements quotidiens (%): {rendements}")

# --- Application remise ---
print(f"\n  --- Application remise ---")
prix = np.array([19.99, 49.99, 99.99, 149.99])
prix_reduits = prix * 0.8
print(f"  Prix originaux: {prix}")
print(f"  Prix avec remise: {prix_reduits}")
prix_reduits_arrondis = np.round(prix_reduits, 2)
print(f"  Prix arrondis: {prix_reduits_arrondis}")

# --- Signal sinusoidal ---
print(f"\n  --- Signal sinusoidal ---")
t = np.linspace(0, 1, 100)
frequence = 5
signal = np.sin(2 * np.pi * frequence * t)
print(f"  Signal genere: {len(signal)} points")
