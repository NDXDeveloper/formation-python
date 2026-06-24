# ============================================================================
#   Section 3.20 : Tester directement une valeur (la « véracité »)
#   Description : une condition peut être n'importe quelle valeur ; idiome
#                 if nom: / if not nom: plutôt que == "" ou len() > 0
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Une valeur "vraie" / "fausse" sert directement de condition ---
nom = "Alice"
if nom:                      # vrai si nom n'est PAS vide
    print(f"Bonjour {nom} !")
else:
    print("Vous n'avez rien saisi.")

# Chaîne vide = "fausse"
texte = ""
if texte:
    print("Le texte contient quelque chose")
else:
    print("Le texte est vide")   # s'affiche

# --- if not X teste "X est vide / faux" ---
saisie = ""
if not saisie:
    print("Rien n'a ete saisi")  # s'affiche

# --- Équivalences (toutes vraies pour une chaîne non vide) ---
nom = "Bob"
print(bool(nom))             # True
print(nom != "")             # True (équivalent verbeux)
print(len(nom) > 0)          # True (équivalent verbeux)
