# ============================================================================
#   Section 4.3 : Pickle - Sauvegarder et charger des objets
#   Description : pickle.dump() et pickle.load() pour sérialiser/désérialiser
#                 des listes, dictionnaires et objets multiples
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

# --- Sauvegarder et charger une liste ---
print("=== Liste ===")

ma_liste = [1, 2, 3, 4, 5, "Python", True, 3.14]

with open('ma_liste.pkl', 'wb') as fichier:
    pickle.dump(ma_liste, fichier)
print("Liste sauvegardée avec succès !")

with open('ma_liste.pkl', 'rb') as fichier:
    ma_liste = pickle.load(fichier)
print("Liste chargée :", ma_liste)
print("Type :", type(ma_liste))

# --- Sauvegarder et charger un dictionnaire ---
print("\n=== Dictionnaire ===")

utilisateur = {
    'nom': 'Dupont',
    'prenom': 'Marie',
    'age': 28,
    'competences': ['Python', 'SQL', 'Django'],
    'actif': True,
    'scores': [85, 92, 78, 95]
}

with open('utilisateur.pkl', 'wb') as fichier:
    pickle.dump(utilisateur, fichier)
print("Utilisateur sauvegardé !")

with open('utilisateur.pkl', 'rb') as fichier:
    utilisateur = pickle.load(fichier)
print(f"Nom : {utilisateur['nom']}")
print(f"Age : {utilisateur['age']} ans")
print(f"Compétences : {', '.join(utilisateur['competences'])}")

# --- Sauvegarder et charger plusieurs objets ---
print("\n=== Objets multiples ===")

nom = "Alice"
age = 30
hobbies = ["lecture", "natation", "musique"]

with open('donnees_multiples.pkl', 'wb') as fichier:
    pickle.dump(nom, fichier)
    pickle.dump(age, fichier)
    pickle.dump(hobbies, fichier)
print("Plusieurs objets sauvegardés !")

with open('donnees_multiples.pkl', 'rb') as fichier:
    nom = pickle.load(fichier)
    age = pickle.load(fichier)
    hobbies = pickle.load(fichier)
print(f"{nom}, {age} ans")
print(f"Hobbies : {hobbies}")

# Nettoyage
os.remove('ma_liste.pkl')
os.remove('utilisateur.pkl')
os.remove('donnees_multiples.pkl')
