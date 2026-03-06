# ============================================================================
#   Section 2.2 : Compréhensions de dictionnaires
#   Description : Créer des dicts avec compréhension, conditions, transformer
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- Exemples de base ---
# Dictionnaire de carrés
carres = {x: x**2 for x in range(5)}
print(carres)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Créer à partir de deux listes
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
personnes = {nom: age for nom, age in zip(noms, ages)}
print(personnes)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Longueurs de mots
mots = ["chat", "chien", "oiseau"]
longueurs = {mot: len(mot) for mot in mots}
print(longueurs)  # {'chat': 4, 'chien': 5, 'oiseau': 6}

# Inverser un dictionnaire
original = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in original.items()}
print(inverse)  # {1: 'a', 2: 'b', 3: 'c'}

# --- Avec conditions ---
print()
# Filtrer les notes supérieures à 12
notes = {"Alice": 18, "Bob": 10, "Charlie": 15, "David": 8}
bonnes_notes = {nom: note for nom, note in notes.items() if note > 12}
print(bonnes_notes)  # {'Alice': 18, 'Charlie': 15}

# Garder seulement les nombres pairs
nombres = {f"n{i}": i for i in range(10) if i % 2 == 0}
print(nombres)  # {'n0': 0, 'n2': 2, 'n4': 4, 'n6': 6, 'n8': 8}

# Mots avec plus de 2 lettres
mots = ["le", "chat", "et", "le", "chien"]
mots_longs = {mot: len(mot) for mot in mots if len(mot) > 2}
print(mots_longs)  # {'chat': 4, 'chien': 5}

# --- Transformer les valeurs ---
print()
# Réduction de 20% sur tous les prix
prix = {"pomme": 2.5, "banane": 1.8, "orange": 3.0}
prix_soldes = {produit: prix * 0.8 for produit, prix in prix.items()}
print(prix_soldes)  # {'pomme': 2.0, 'banane': 1.44, 'orange': 2.4}

# Convertir valeurs en chaînes
donnees = {"a": 1, "b": 2, "c": 3}
donnees_str = {cle: str(valeur) for cle, valeur in donnees.items()}
print(donnees_str)  # {'a': '1', 'b': '2', 'c': '3'}

# Clés en majuscules
original = {"nom": "Alice", "age": 25, "ville": "Paris"}
majuscules = {cle.upper(): valeur for cle, valeur in original.items()}
print(majuscules)  # {'NOM': 'Alice', 'AGE': 25, 'VILLE': 'Paris'}

# --- Avec if-else ---
print()
# Classifier les notes
notes = {"Alice": 18, "Bob": 10, "Charlie": 15}
appreciations = {nom: "Admis" if note >= 12 else "Refusé"
                 for nom, note in notes.items()}
print(appreciations)  # {'Alice': 'Admis', 'Bob': 'Refusé', 'Charlie': 'Admis'}

# Ajuster les prix en fonction du stock
produits = {"laptop": 1000, "souris": 20, "clavier": 50}
stock = {"laptop": 5, "souris": 100, "clavier": 30}

prix_ajustes = {
    produit: prix * 1.1 if stock[produit] < 10 else prix * 0.9
    for produit, prix in produits.items()
}
print(prix_ajustes)  # {'laptop': 1100.0, 'souris': 18.0, 'clavier': 45.0}
