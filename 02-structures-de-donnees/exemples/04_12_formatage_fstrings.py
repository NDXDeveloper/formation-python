# ============================================================================
#   Section 2.4 : Formatage avec f-strings
#   Description : Syntaxe de base, expressions, méthodes, nombres, alignement,
#                 séparateurs de milliers, pourcentages, notation scientifique
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Syntaxe de base
nom = "Alice"
age = 25
message = f"Je m'appelle {nom} et j'ai {age} ans"
print(message)  # Je m'appelle Alice et j'ai 25 ans

# Expressions dans les f-strings
x = 10
y = 20
print(f"La somme de {x} et {y} est {x + y}")  # La somme de 10 et 20 est 30

# Appeler des méthodes
texte = "python"
print(f"{texte.upper()} est génial")  # PYTHON est génial

# Formatage des nombres
pi = 3.14159
print(f"Pi vaut environ {pi:.2f}")    # Pi vaut environ 3.14
print(f"Pi avec 4 décimales : {pi:.4f}")  # Pi avec 4 décimales : 3.1416

# Largeur et alignement
print(f"{'Gauche':<10}|")   # Gauche    |
print(f"{'Centre':^10}|")   # Centre    |
print(f"{'Droite':>10}|")   #     Droite|

# Formatage avec séparateurs de milliers
nombre = 1234567
print(f"Population : {nombre:,}")      # Population : 1,234,567
print(f"Population : {nombre:_}")      # Population : 1_234_567

# Pourcentages
ratio = 0.857
print(f"Taux de réussite : {ratio:.1%}")  # Taux de réussite : 85.7%

# Notation scientifique
grand_nombre = 1234567890
print(f"{grand_nombre:e}")  # 1.234568e+09

# Padding avec des zéros
numero = 42
print(f"Numéro : {numero:05d}")  # Numéro : 00042
