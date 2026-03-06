# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Multiprocessing - processus simple, Pool avec map,
#                 comparaison séquentiel vs parallèle
#   Fichier source : 01-threading-et-multiprocessing.md
# ============================================================================

import multiprocessing
import time

def calculer_carre(nombre):
    """Calcule le carré d'un nombre"""
    resultat = nombre ** 2
    print(f"  Carré de {nombre} = {resultat}")
    return resultat

def calculer_cube(nombre):
    """Calcule le cube d'un nombre"""
    return nombre ** 3

def calcul_intensif(n):
    """Fonction qui effectue un calcul coûteux"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def execution_sequentielle(nombres):
    """Exécution séquentielle"""
    debut = time.time()
    resultats = [calcul_intensif(n) for n in nombres]
    duree = time.time() - debut
    print(f"  Séquentiel: {duree:.2f} secondes")
    return resultats

def execution_parallele(nombres):
    """Exécution parallèle"""
    debut = time.time()
    with multiprocessing.Pool() as pool:
        resultats = pool.map(calcul_intensif, nombres)
    duree = time.time() - debut
    print(f"  Parallèle:  {duree:.2f} secondes")
    return resultats

if __name__ == '__main__':
    # ==========================================
    # 1. Premier processus simple
    # ==========================================
    print("=== Premier processus simple ===")

    processus = multiprocessing.Process(target=calculer_carre, args=(5,))
    processus.start()
    print("Le processus a été lancé!")
    processus.join()
    print("Le processus est terminé")

    # ==========================================
    # 2. Pool avec map
    # ==========================================
    print("\n=== Pool avec map ===")

    nombres = [1, 2, 3, 4, 5, 6, 7, 8]

    with multiprocessing.Pool(processes=4) as pool:
        resultats = pool.map(calculer_cube, nombres)

    print(f"Nombres: {nombres}")
    print(f"Cubes:   {resultats}")

    # ==========================================
    # 3. Comparaison séquentiel vs parallèle
    # ==========================================
    print("\n=== Comparaison séquentiel vs parallèle ===")

    # Taille réduite pour un test rapide
    nombres_calcul = [1000000] * 4

    print("Calculs intensifs:")
    r_seq = execution_sequentielle(nombres_calcul)
    r_par = execution_parallele(nombres_calcul)

    # Vérifier que les résultats sont identiques
    print(f"  Résultats identiques: {r_seq == r_par}")
    print(f"  Nombre de CPU disponibles: {multiprocessing.cpu_count()}")
