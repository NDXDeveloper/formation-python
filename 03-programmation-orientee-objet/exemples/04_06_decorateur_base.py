# ============================================================================
#   Section 3.4 : Décorateurs - Base
#   Description : Décorateur simple, décorateur chronomètre
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

import time

# --- Décorateur simple ---
def mon_decorateur(fonction):
    def wrapper():
        print("Avant l'appel de la fonction")
        fonction()
        print("Après l'appel de la fonction")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

# --- Décorateur chronomètre ---
print()

def chronometre(fonction):
    """Décorateur qui mesure le temps d'exécution"""
    def wrapper():
        debut = time.time()
        fonction()
        fin = time.time()
        duree = fin - debut
        print(f"Temps d'exécution : {duree:.4f} secondes")
    return wrapper

@chronometre
def tache_rapide():
    print("Début de la tâche...")
    total = sum(range(1000000))
    print(f"Fin de la tâche. (total={total})")

tache_rapide()
