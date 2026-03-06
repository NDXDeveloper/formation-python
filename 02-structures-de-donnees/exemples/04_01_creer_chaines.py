# ============================================================================
#   Section 2.4 : Créer des chaînes de caractères
#   Description : Guillemets simples/doubles/triples, caractères spéciaux,
#                 raw strings
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Guillemets simples et doubles
chaine1 = 'Bonjour'
chaine2 = "Python"

# Triple guillemets (multi-lignes)
chaine3 = """Ceci est une chaîne
qui s'étend sur
plusieurs lignes"""
print(chaine3)

# --- Caractères spéciaux ---
print()
print("Ligne 1\nLigne 2")
print("Colonne1\tColonne2")
print("Il a dit : \"Bonjour\"")
print('C\'est génial')
print("Chemin : C:\\Users\\Python")

# Chaînes brutes (raw strings)
print(r"C:\Users\nouveau\fichier.txt")
