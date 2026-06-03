# ============================================================================
#   Section 8.1 : Threading et Multiprocessing
#   Description : Sous-interpreteurs (PEP 734) - InterpreterPoolExecutor,
#                 vrai parallelisme CPU sans multiprocessing (Python 3.14+)
#   Fichier source : README.md
# ============================================================================

import sys

# Fonction au niveau du module (executee dans un sous-interpreteur isole).
def calcul_cpu(n):
    """Tache CPU-bound : somme des carres jusqu'a n"""
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    # InterpreterPoolExecutor expose plusieurs interpreteurs Python dans le meme
    # processus ; depuis Python 3.12 chaque sous-interpreteur a son propre GIL
    # (PEP 684), donc ils s'executent vraiment en parallele pour le CPU-bound.
    # L'API (PEP 734) arrive dans la bibliotheque standard en Python 3.14.
    if sys.version_info >= (3, 14):
        from concurrent.futures import InterpreterPoolExecutor

        print("=== InterpreterPoolExecutor (PEP 734, Python 3.14+) ===")
        nombres = [100000, 200000, 300000, 400000]
        with InterpreterPoolExecutor(max_workers=4) as executor:
            totaux = list(executor.map(calcul_cpu, nombres))
        print(f"Sommes des carres : {len(totaux)} resultats calcules en parallele")
        print("Chaque sous-interpreteur a son propre GIL : vrai parallelisme CPU,")
        print("plus leger qu'un processus (on reste dans le meme processus systeme).")
    else:
        v = f"{sys.version_info.major}.{sys.version_info.minor}"
        print("InterpreterPoolExecutor (sous-interpreteurs) necessite Python 3.14+")
        print(f"Version actuelle : {v} -> exemple ignore")
