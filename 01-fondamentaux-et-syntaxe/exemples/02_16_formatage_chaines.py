# ============================================================================
#   Section 2.16 : Formatage de Chaînes (Affichage Avancé)
#   Description : Concaténation, format(), f-strings, formatage avancé
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- 1. Concaténation simple ---
nom = "Alice"
age = 25
print("Je m'appelle " + nom + " et j'ai " + str(age) + " ans.")

# --- 2. Méthode format() ---
nom = "Alice"
age = 25
print("Je m'appelle {} et j'ai {} ans.".format(nom, age))

# --- 3. F-strings (Recommandé - Python 3.6+) ---
nom = "Alice"
age = 25
print(f"Je m'appelle {nom} et j'ai {age} ans.")

# --- F-strings avec expressions ---
prix_ht = 100
tva = 0.20
print(f"Prix TTC : {prix_ht * (1 + tva)} euros")
# Affiche : Prix TTC : 120.0 euros

nombre = 7
print(f"Le double de {nombre} est {nombre * 2}")
# Affiche : Le double de 7 est 14

# --- Formatage avancé avec f-strings ---
# Limiter les décimales
pi = 3.14159265
print(f"Pi vaut environ {pi:.2f}")  # Affiche : Pi vaut environ 3.14

# Afficher un pourcentage
ratio = 0.85
print(f"Taux de réussite : {ratio:.1%}")  # Affiche : Taux de réussite : 85.0%

# Aligner du texte
nom = "Alice"
print(f"{nom:>10}")   # Aligné à droite sur 10 caractères
print(f"{nom:<10}")   # Aligné à gauche sur 10 caractères
print(f"{nom:^10}")   # Centré sur 10 caractères
