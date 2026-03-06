# ============================================================================
#   Section 3.3 : Gestionnaires de contexte
#   Description : __enter__ et __exit__ avec FichierLog et Chronomètre
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

import time
import os

# --- FichierLog ---
class FichierLog:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.fichier = None

    def __enter__(self):
        print(f"Ouverture de {self.nom_fichier}")
        self.fichier = open(self.nom_fichier, 'w')
        return self.fichier

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Fermeture de {self.nom_fichier}")
        if self.fichier:
            self.fichier.close()
        return False

with FichierLog("log.txt") as f:
    f.write("Début du programme\n")
    f.write("Traitement en cours...\n")
    f.write("Fin du programme\n")

# Vérifier le contenu
with open("log.txt", 'r') as f:
    print(f.read())

# Nettoyer
os.remove("log.txt")

# --- Chronomètre ---
class Chronometre:
    def __enter__(self):
        self.debut = time.time()
        print("Chronomètre démarré...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fin = time.time()
        duree = self.fin - self.debut
        print(f"Temps écoulé : {duree:.4f} secondes")
        return False

with Chronometre():
    total = sum(range(1000000))
    print(f"Somme calculée : {total}")
