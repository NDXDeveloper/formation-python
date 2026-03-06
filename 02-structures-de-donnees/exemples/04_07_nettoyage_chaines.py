# ============================================================================
#   Section 2.4 : Nettoyage des chaînes
#   Description : strip, lstrip, rstrip, removeprefix, removesuffix
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "   Python   "

# Supprimer les espaces au début et à la fin
print(f"'{texte.strip()}'")       # 'Python'
print(f"'{texte.lstrip()}'")      # 'Python   ' (gauche seulement)
print(f"'{texte.rstrip()}'")      # '   Python' (droite seulement)

# Supprimer des caractères spécifiques
texte2 = "***Python***"
print(texte2.strip('*'))   # Python

# strip() supprime des CARACTÈRES individuels, pas un préfixe
texte3 = "...texte..."
print(texte3.strip('.'))  # texte

# Pour supprimer un préfixe ou suffixe exact (Python 3.9+)
url = "www.example.com"
print(url.removeprefix('www.'))  # example.com
print(url.removesuffix('.com'))  # www.example
