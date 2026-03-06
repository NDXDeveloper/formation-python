# ============================================================================
#   Section 2.4 : Regex - re.findall() et re.finditer()
#   Description : Trouver toutes les occurrences, itérer sur les correspondances
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# --- re.findall() - Trouver toutes les occurrences ---
texte = "Les numéros de téléphone sont : 0123456789 et 0987654321"

numeros = re.findall(r'\d+', texte)
print(numeros)  # ['0123456789', '0987654321']

# Trouver tous les mots
texte2 = "Python, Java, JavaScript"
langages = re.findall(r'\w+', texte2)
print(langages)  # ['Python', 'Java', 'JavaScript']

# --- re.finditer() - Iterator sur les correspondances ---
print()
texte = "Python 3.9, Java 11, C++ 17"

for match in re.finditer(r'\d+', texte):
    print(f"Trouvé '{match.group()}' à la position {match.start()}")
