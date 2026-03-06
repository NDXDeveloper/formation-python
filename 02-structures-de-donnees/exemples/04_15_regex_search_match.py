# ============================================================================
#   Section 2.4 : Regex - re.search() et re.match()
#   Description : Chercher la première occurrence, vérifier le début de chaîne
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# --- re.search() - Trouver la première occurrence ---
texte = "J'apprends Python depuis 2020"

resultat = re.search(r'\d+', texte)  # Cherche un ou plusieurs chiffres

if resultat:
    print("Trouvé :", resultat.group())  # 2020
    print("Position :", resultat.start()) # 25
    print("Fin :", resultat.end())       # 29
else:
    print("Non trouvé")

# --- re.match() - Vérifier le début de la chaîne ---
print()
texte = "Python est génial"

resultat = re.match(r'Python', texte)
if resultat:
    print("Commence par Python")  # Affiché

resultat = re.match(r'génial', texte)
if resultat:
    print("Commence par génial")
else:
    print("Ne commence pas par génial")  # Affiché
