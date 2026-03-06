# ============================================================================
#   Section 5.5 : Fonctions pures et immuabilité
#   Description : Fonctions pures vs impures, convertir impure en pure,
#                 travailler de manière immuable, copies superficielle/profonde
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

import copy

# --- Fonctions pures ---
print("=== Fonctions pures ===")

def additionner(a, b):
    """Toujours le même résultat, pas d'effets de bord."""
    return a + b

print(additionner(3, 4))  # Toujours 7
print(additionner(3, 4))  # Toujours 7

def calculer_carre(n):
    """Pure : pas de modification externe."""
    return n * n

print(calculer_carre(5))  # 25

# --- Convertir impure en pure ---
print("\n=== Impure vs pure ===")

# Pure : retourne une nouvelle liste
def ajouter_pure(liste, element):
    """Retourne une nouvelle liste sans modifier l'originale."""
    return liste + [element]

ma_liste = [1, 2, 3]
nouvelle_liste = ajouter_pure(ma_liste, 4)
print(ma_liste)         # [1, 2, 3] - Non modifiée
print(nouvelle_liste)   # [1, 2, 3, 4]

# --- Travailler de manière immuable ---
print("\n=== Style immuable ===")

def augmenter_prix_immuable(produits, pourcentage):
    return [
        {**produit, 'prix': produit['prix'] * (1 + pourcentage / 100)}
        for produit in produits
    ]

produits_originaux = [
    {'nom': 'Pomme', 'prix': 2.5},
    {'nom': 'Banane', 'prix': 1.8}
]

nouveaux_produits = augmenter_prix_immuable(produits_originaux, 10)
print("Originaux :", produits_originaux)  # Non modifiés
print("Nouveaux :", nouveaux_produits)    # Prix augmentés de 10%

# --- Copies ---
print("\n=== Copies ===")

# Copie superficielle
liste_originale = [1, 2, [3, 4]]
copie_superficielle = liste_originale.copy()
copie_superficielle[2][0] = 99
print(f"Après copie superficielle : {liste_originale}")  # [1, 2, [99, 4]]

# Copie profonde
liste_originale = [1, 2, [3, 4]]
copie_profonde = copy.deepcopy(liste_originale)
copie_profonde[2][0] = 99
print(f"Après copie profonde : {liste_originale}")  # [1, 2, [3, 4]]
