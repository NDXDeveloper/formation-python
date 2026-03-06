# ============================================================================
#   Section 8.4 : Patterns de Concurrence
#   Description : Pattern Map-Reduce - traitement parallele en deux phases
#                 (map: transformation, reduce: agregation), analyse de texte
#   Fichier source : 04-patterns-de-concurrence.md
# ============================================================================

from concurrent.futures import ProcessPoolExecutor
from collections import Counter
import re
import time

# ==========================================
# 1. Map-Reduce simple (somme des carres)
# ==========================================
print("=== Map-Reduce (somme des carres) ===\n")

def map_function(nombre):
    """Phase Map: Calcule le carre"""
    return nombre ** 2

def reduce_function(resultats):
    """Phase Reduce: Somme tous les carres"""
    return sum(resultats)

if __name__ == '__main__':
    nombres = list(range(1, 101))

    # Phase Map (parallele)
    with ProcessPoolExecutor() as executor:
        debut = time.time()
        carres = list(executor.map(map_function, nombres))
        duree_map = time.time() - debut

    # Phase Reduce
    debut = time.time()
    total = reduce_function(carres)
    duree_reduce = time.time() - debut

    print(f"Map-Reduce:")
    print(f"  Nombres: 1-100")
    print(f"  Somme des carres: {total}")
    print(f"  Temps Map: {duree_map:.3f}s")
    print(f"  Temps Reduce: {duree_reduce:.3f}s")

    # Verification
    attendu = sum(i**2 for i in range(1, 101))
    print(f"  Verification: {total == attendu} (attendu: {attendu})")

    # ==========================================
    # 2. Map-Reduce : Analyse de texte
    # ==========================================
    print("\n=== Map-Reduce (analyse de texte) ===\n")

    documents = [
        "Python est un langage de programmation. Python est facile.",
        "La programmation est amusante. Python est populaire.",
        "Le langage Python est utilise en science des donnees.",
        "Python est un excellent langage pour debuter.",
    ]

    def compter_mots(texte):
        """Phase Map: Compte les mots dans un texte"""
        mots = re.findall(r'\w+', texte.lower())
        return Counter(mots)

    def fusionner_compteurs(compteurs):
        """Phase Reduce: Fusionne tous les compteurs"""
        resultat = Counter()
        for compteur in compteurs:
            resultat.update(compteur)
        return resultat

    # Phase Map
    with ProcessPoolExecutor() as executor:
        compteurs = list(executor.map(compter_mots, documents))

    # Phase Reduce
    compteur_total = fusionner_compteurs(compteurs)

    print("Analyse Map-Reduce:")
    print("\nTop 5 des mots les plus frequents:")
    for mot, compte in compteur_total.most_common(5):
        print(f"  {mot}: {compte} fois")
