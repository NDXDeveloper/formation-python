# ============================================================================
#   Section 3.5 : Tout est objet en Python
#   Description : Vérifier que nombres, chaînes, fonctions et classes sont
#                 tous des objets avec un type
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# Les nombres sont des objets
nombre = 42
print(type(nombre))  # <class 'int'>

# Les chaînes sont des objets
texte = "Bonjour"
print(type(texte))   # <class 'str'>

# Les fonctions sont des objets
def ma_fonction():
    pass

print(type(ma_fonction))  # <class 'function'>

# Les classes sont AUSSI des objets !
class MaClasse:
    pass

print(type(MaClasse))  # <class 'type'>
