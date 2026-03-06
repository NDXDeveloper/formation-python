# ============================================================================
#   Section 4.3 : Pickle - Système de sauvegarde de jeu
#   Description : Classe Joueur avec inventaire, sauvegarde/chargement de
#                 partie complète
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.points = 0
        self.inventaire = []

    def gagner_points(self, points):
        self.points += points
        print(f"+{points} points ! Total : {self.points}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"Objet ajouté : {objet}")

    def afficher_stats(self):
        print(f"\n{'='*40}")
        print(f"Joueur : {self.nom}")
        print(f"Niveau : {self.niveau}")
        print(f"Points : {self.points}")
        print(f"Inventaire : {', '.join(self.inventaire) if self.inventaire else 'vide'}")
        print(f"{'='*40}\n")

def sauvegarder_partie(joueur, fichier='sauvegarde.pkl'):
    """Sauvegarde la partie"""
    with open(fichier, 'wb') as f:
        pickle.dump(joueur, f)
    print("Partie sauvegardée !")

def charger_partie(fichier='sauvegarde.pkl'):
    """Charge une partie sauvegardée"""
    try:
        with open(fichier, 'rb') as f:
            joueur = pickle.load(f)
        print("Partie chargée !")
        return joueur
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée")
        return None

# === Nouvelle partie ===
joueur = Joueur("Alice")
joueur.gagner_points(100)
joueur.ajouter_objet("Épée")
joueur.ajouter_objet("Potion")
joueur.afficher_stats()

# Sauvegarder
sauvegarder_partie(joueur)

# === Simuler la fermeture du jeu ===
del joueur

# === Relancer le jeu ===
joueur = charger_partie()
if joueur:
    joueur.afficher_stats()
    joueur.gagner_points(50)
    joueur.ajouter_objet("Bouclier")
    joueur.afficher_stats()

# Nettoyage
os.remove('sauvegarde.pkl')
