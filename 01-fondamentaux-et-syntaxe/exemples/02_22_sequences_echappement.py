# ============================================================================
#   Section 2.22 : Séquences d'échappement et chaînes brutes
#   Description : \n \t \\ \" \' (caractères spéciaux) ; chaîne brute r"..."
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Séquences d'échappement (le \ introduit un caractère spécial) ---
print("Ligne 1\nLigne 2")       # \n = saut de ligne (affiche sur deux lignes)
print("Nom :\tAlice")           # \t = tabulation
print("Un antislash : \\")      # \\ = un seul antislash
print("Il a dit \"Bonjour\"")   # \" = guillemet double dans la chaîne
print('J\'aime Python')         # \' = apostrophe dans une chaîne entre '

# --- Chaîne brute r"..." : les \ ne sont PAS interprétés ---
chemin = "dossier\nouveau"        # \n interprété comme un saut de ligne !
chemin_brut = r"dossier\nouveau"  # chaîne brute : le \ reste littéral
print(chemin)
print(chemin_brut)                # Affiche : dossier\nouveau
