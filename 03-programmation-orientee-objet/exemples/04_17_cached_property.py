# ============================================================================
#   Section 3.4 : @cached_property - calculer une seule fois
#   Description : Mémorise le résultat au premier accès (functools, 3.8+),
#                 invalidation par del, différence avec @property
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

from functools import cached_property

class AnalyseTexte:
    def __init__(self, texte):
        self.texte = texte

    @cached_property
    def nb_mots_uniques(self):
        print("Calcul coûteux en cours...")   # pour voir QUAND le calcul a lieu
        return len(set(self.texte.lower().split()))

analyse = AnalyseTexte("le chat et le chien et le chat")

# Premier accès : le calcul a lieu
print(analyse.nb_mots_uniques)   # Calcul coûteux en cours...  puis  4
# Accès suivants : valeur en cache, AUCUN recalcul
print(analyse.nb_mots_uniques)   # 4

# La valeur est stockée dans l'instance
print("'nb_mots_uniques' in __dict__ :", 'nb_mots_uniques' in analyse.__dict__)

# --- Invalider le cache : del force un nouveau calcul ---
print()
del analyse.nb_mots_uniques
print(analyse.nb_mots_uniques)   # Calcul coûteux en cours...  puis  4 (recalcul)
