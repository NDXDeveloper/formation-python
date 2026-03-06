# ============================================================================
#   Section 2.4 : Regex - Compilation et drapeaux (flags)
#   Description : re.compile(), re.IGNORECASE, re.MULTILINE, re.DOTALL
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# --- Compilation de patterns ---
texte1 = "Python 3.9"
texte2 = "Java 11"

# Avec compilation (meilleure performance)
pattern = re.compile(r'\d+')
resultat1 = pattern.findall(texte1)
resultat2 = pattern.findall(texte2)

print(resultat1)  # ['3', '9']
print(resultat2)  # ['11']

# --- Drapeaux (flags) ---
print()
texte = "Python\nest\nSuper"

# re.IGNORECASE - Ignorer la casse
print(re.findall(r'python', texte, re.IGNORECASE))  # ['Python']

# re.MULTILINE - ^ et $ correspondent au début/fin de chaque ligne
print(re.findall(r'^[a-z]+', texte, re.MULTILINE | re.IGNORECASE))
# ['Python', 'est', 'Super']

# re.DOTALL - . correspond aussi aux nouvelles lignes
print(re.findall(r'Python.+Super', texte))         # [] (ne trouve pas)
print(re.findall(r'Python.+Super', texte, re.DOTALL))  # ['Python\nest\nSuper']
