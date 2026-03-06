# ============================================================================
#   Section 4.3 : Pickle - Objets personnalisés
#   Description : Sauvegarder et charger des instances de classes personnalisées
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

# La classe doit être définie avant le chargement
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def se_presenter(self):
        return f"Je m'appelle {self.nom}, j'ai {self.age} ans et j'habite à {self.ville}"

# --- Sauvegarder l'objet ---
personne1 = Personne("Marie", 28, "Paris")
print(personne1.se_presenter())

with open('personne.pkl', 'wb') as fichier:
    pickle.dump(personne1, fichier)
print("Objet Personne sauvegardé !")

# --- Charger l'objet ---
with open('personne.pkl', 'rb') as fichier:
    personne_chargee = pickle.load(fichier)

# L'objet fonctionne normalement !
print(personne_chargee.se_presenter())
print(f"Type : {type(personne_chargee)}")

# Nettoyage
os.remove('personne.pkl')
