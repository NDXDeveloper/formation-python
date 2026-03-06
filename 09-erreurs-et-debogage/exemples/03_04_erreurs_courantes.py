# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Erreurs courantes et comment les deboguer (TypeError,
#                 IndexError, KeyError, NameError), strategies de debogage
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

# ==========================================
# 1. TypeError - Types incompatibles
# ==========================================
print("=== TypeError ===\n")

age = "25"
print(f"  Type de age : {type(age)}")

# Solution
age = int("25")
nouvelle_age = age + 1
print(f"  nouvelle_age = {nouvelle_age}")  # 26

# ==========================================
# 2. IndexError - Index hors limites
# ==========================================
print("\n=== IndexError ===\n")

liste = [1, 2, 3]
index = 10

print(f"  Longueur de la liste : {len(liste)}")
print(f"  Index demande : {index}")

if index < len(liste):
    element = liste[index]
else:
    print(f"  Erreur : index {index} trop grand (max : {len(liste)-1})")

# ==========================================
# 3. KeyError - Cle inexistante
# ==========================================
print("\n=== KeyError ===\n")

personne = {'nom': 'Alice', 'age': 25}
cle = 'ville'

print(f"  Cles disponibles : {list(personne.keys())}")

# Solution 1 : verifier avec 'in'
if cle in personne:
    ville = personne[cle]
else:
    print(f"  La cle '{cle}' n'existe pas")

# Solution 2 : utiliser get()
ville = personne.get('ville', 'Non specifie')
print(f"  Ville : {ville}")

# ==========================================
# 4. NameError - Variable non definie
# ==========================================
print("\n=== NameError ===\n")

def afficher_nom():
    if 'prenom' in dir():
        print(prenom)
    else:
        print("  La variable 'prenom' n'existe pas")
        variables = [v for v in dir() if not v.startswith('_')]
        print(f"  Variables disponibles : {variables}")

afficher_nom()

# ==========================================
# 5. Calcul de moyenne - bug et correction
# ==========================================
print("\n=== Moyenne - bug et correction ===\n")

def calculer_moyenne(nombres):
    """Version avec bug sur liste vide"""
    return sum(nombres) / len(nombres)

def calculer_moyenne_v2(nombres):
    """Version corrigee"""
    if not nombres:
        print("  Attention : liste vide")
        return None
    return sum(nombres) / len(nombres)

print(f"  moyenne([10, 20, 30]) = {calculer_moyenne([10, 20, 30])}")
print(f"  moyenne_v2([10, 20, 30]) = {calculer_moyenne_v2([10, 20, 30])}")
print(f"  moyenne_v2([]) = {calculer_moyenne_v2([])}")

try:
    calculer_moyenne([])
except ZeroDivisionError as e:
    print(f"  Erreur avec liste vide : {e}")
