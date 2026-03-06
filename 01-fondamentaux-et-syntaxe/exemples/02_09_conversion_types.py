# ============================================================================
#   Section 2.9 : Conversion Entre Types (Casting)
#   Description : int(), float(), str(), bool() - conversions valides et invalides
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- String vers int ---
age_texte = "25"
age_nombre = int(age_texte)
print(age_nombre + 5)  # Affiche : 30

# --- String vers float ---
prix_texte = "19.99"
prix_nombre = float(prix_texte)
print(prix_nombre * 2)  # Affiche : 39.98

# --- Int/Float vers string ---
age = 25
age_texte = str(age)
print("J'ai " + age_texte + " ans")  # Affiche : J'ai 25 ans

# --- Float vers int (tronque la partie décimale) ---
prix = 19.99
prix_entier = int(prix)
print(prix_entier)  # Affiche : 19

# --- Int vers float ---
nombre = 10
nombre_decimal = float(nombre)
print(nombre_decimal)  # Affiche : 10.0

# --- Vers booléen ---
print(bool(1))       # Affiche : True
print(bool(0))       # Affiche : False
print(bool("texte")) # Affiche : True

# --- Conversion invalide (commentée car ValueError) ---
texte = "abc"
# nombre = int(texte)  # ValueError : On ne peut pas convertir "abc" en nombre
print("int('abc') provoquerait une ValueError")
