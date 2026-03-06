# ============================================================================
#   Section 2.4 : Division et jointure
#   Description : split, split avec séparateur, splitlines, join
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Split - diviser une chaîne
texte = "Python est un langage génial"
mots = texte.split()  # Split sur les espaces par défaut
print(mots)  # ['Python', 'est', 'un', 'langage', 'génial']

# Split avec séparateur personnalisé
csv = "nom,prenom,age"
donnees = csv.split(',')
print(donnees)  # ['nom', 'prenom', 'age']

# Limiter le nombre de splits
texte2 = "un:deux:trois:quatre"
parties = texte2.split(':', 2)
print(parties)  # ['un', 'deux', 'trois:quatre']

# Split sur les lignes
paragraphe = """Ligne 1
Ligne 2
Ligne 3"""
lignes = paragraphe.splitlines()
print(lignes)  # ['Ligne 1', 'Ligne 2', 'Ligne 3']

# Join - joindre des éléments
mots = ['Python', 'est', 'génial']
phrase = ' '.join(mots)
print(phrase)  # Python est génial

# Join avec différents séparateurs
print('-'.join(mots))    # Python-est-génial
print(''.join(mots))     # Pythonestgénial
print('\n'.join(mots))   # Chaque mot sur une ligne

# Join avec des nombres (convertir d'abord)
nombres = [1, 2, 3, 4]
resultat = ', '.join(str(n) for n in nombres)
print(resultat)  # 1, 2, 3, 4
