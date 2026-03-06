# ============================================================================
#   Section 5.4 : Qu'est-ce qu'un générateur ?
#   Description : Fonction normale vs générateur, le mot-clé yield,
#                 next() et StopIteration
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Fonction normale vs Générateur ---
print("=== Fonction normale vs Générateur ===")

def creer_liste_nombres(n):
    """Crée une liste de nombres de 0 à n-1."""
    liste = []
    for i in range(n):
        liste.append(i)
    return liste

nombres = creer_liste_nombres(5)
print(nombres)  # [0, 1, 2, 3, 4]
print(type(nombres))  # <class 'list'>

# Générateur
def generer_nombres(n):
    """Génère des nombres de 0 à n-1."""
    for i in range(n):
        yield i

nombres = generer_nombres(5)
print(nombres)  # <generator object generer_nombres at 0x...>
print(type(nombres))  # <class 'generator'>

# Pour voir les valeurs, il faut itérer
for nombre in nombres:
    print(nombre, end=" ")  # 0 1 2 3 4
print()

# --- Le mot-clé yield ---
print("\n=== Le mot-clé yield ===")

def mon_generateur():
    print("Première valeur")
    yield 1
    print("Deuxième valeur")
    yield 2
    print("Troisième valeur")
    yield 3
    print("Fin")

gen = mon_generateur()

print(next(gen))
# Première valeur
# 1

print(next(gen))
# Deuxième valeur
# 2

print(next(gen))
# Troisième valeur
# 3

# Le prochain appel lèverait StopIteration
try:
    next(gen)
except StopIteration:
    print("StopIteration levée")
