# ============================================================================
#   Section 2.4 : Regex - Bonnes pratiques
#   Description : Raw strings, compilation, groupes nommés, regex VERBOSE,
#                 fonction de test, performance vs méthodes natives
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# --- 1. Toujours utiliser des raw strings ---
# Mauvais : pattern = "\\d+"
# Bon :
pattern = r"\d+"
print(re.findall(pattern, "Il y a 42 pommes"))  # ['42']

# --- 2. Compiler les patterns réutilisés ---
pattern = re.compile(r'\d+')
textes = ["Python 3.9", "Java 11", "C++ 17"]
for texte in textes:
    print(f"  {texte} -> {pattern.findall(texte)}")

# --- 3. Utiliser des groupes nommés pour la clarté ---
print()
# Moins lisible : r'(\d{4})-(\d{2})-(\d{2})'
# Plus lisible :
pattern = r'(?P<annee>\d{4})-(?P<mois>\d{2})-(?P<jour>\d{2})'
match = re.search(pattern, "Date: 2024-10-27")
if match:
    print(f"Année: {match.group('annee')}, Mois: {match.group('mois')}, Jour: {match.group('jour')}")

# --- 4. Commenter les regex complexes avec VERBOSE ---
print()
email_pattern = r'''
    ^                    # Début de la chaîne
    [a-zA-Z0-9._%+-]+   # Nom d'utilisateur
    @                    # Arobase
    [a-zA-Z0-9.-]+      # Nom de domaine
    \.                   # Point
    [a-zA-Z]{2,}        # Extension (au moins 2 caractères)
    $                    # Fin de la chaîne
'''
pattern = re.compile(email_pattern, re.VERBOSE)
print(f"test@example.com valide : {pattern.match('test@example.com') is not None}")

# --- 5. Tester vos regex ---
print()
def tester_pattern(pattern, tests):
    """Fonction utilitaire pour tester des patterns"""
    compiled = re.compile(pattern)
    for texte, attendu in tests:
        resultat = compiled.match(texte) is not None
        status = "OK" if resultat == attendu else "ERREUR"
        print(f"  {status} {texte}: {resultat} (attendu: {attendu})")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
tests = [
    ("test@example.com", True),
    ("invalid.email", False),
    ("test@.com", False),
    ("test@example.co.uk", True)
]
tester_pattern(email_pattern, tests)

# --- 6. Performance : préférer les méthodes natives pour les cas simples ---
print()
texte = "Python est génial"
# Avec regex (overkill pour ce cas) :
if re.search(r'Python', texte):
    print("Trouvé avec regex")
# Plus simple et rapide avec 'in' :
if 'Python' in texte:
    print("Trouvé avec 'in'")
