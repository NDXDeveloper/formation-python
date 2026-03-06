# ============================================================================
#   Section 2.4 : Regex - Nettoyage de texte
#   Description : Supprimer espaces multiples, ponctuation excessive,
#                 caractères non-alphanumériques
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

texte = "   Python    est    un    langage    génial!!!   "

# Supprimer les espaces multiples
texte_nettoye = re.sub(r'\s+', ' ', texte)
print(texte_nettoye.strip())  # Python est un langage génial!!!

# Supprimer la ponctuation excessive
texte_nettoye = re.sub(r'[!?]{2,}', '.', texte_nettoye)
print(texte_nettoye.strip())  # Python est un langage génial.

# Supprimer tous les caractères non-alphanumériques sauf espaces
texte = "Python@2024! est #1"
texte_nettoye = re.sub(r'[^\w\s]', '', texte)
print(texte_nettoye)  # Python2024 est 1
