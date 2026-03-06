# ============================================================================
#   Section 2.2 : Compréhensions de dictionnaires - Cas d'usage
#   Description : Occurrences, grouper données, configuration, températures,
#                 créer depuis tuples
#   Fichier source : 02-comprehensions.md
# ============================================================================

# 1. Compter les occurrences de caractères
texte = "hello"
occurrences = {lettre: texte.count(lettre) for lettre in set(texte)}
print(f"Occurrences : {dict(sorted(occurrences.items()))}")

# 2. Grouper des données
etudiants = [
    {"nom": "Alice", "classe": "A"},
    {"nom": "Bob", "classe": "B"},
    {"nom": "Charlie", "classe": "A"}
]

index_classes = {
    classe: [e["nom"] for e in etudiants if e["classe"] == classe]
    for classe in set(e["classe"] for e in etudiants)
}
print(f"Par classe : {dict(sorted(index_classes.items()))}")

# 3. Créer un dictionnaire de configuration
parametres = ["debug", "verbose", "log"]
config = {param: True for param in parametres}
print(config)  # {'debug': True, 'verbose': True, 'log': True}

# 4. Convertir des données
temperatures_c = {"Paris": 20, "Londres": 15, "Berlin": 18}
temperatures_f = {
    ville: (temp * 9/5) + 32
    for ville, temp in temperatures_c.items()
}
print(temperatures_f)  # {'Paris': 68.0, 'Londres': 59.0, 'Berlin': 64.4}

# --- Créer depuis une liste de tuples ---
print()
# Méthode 1 : avec dict()
donnees = [("a", 1), ("b", 2), ("c", 3)]
dictionnaire = dict(donnees)
print(dictionnaire)  # {'a': 1, 'b': 2, 'c': 3}

# Méthode 2 : avec une compréhension
dictionnaire = {cle: valeur for cle, valeur in donnees}
print(dictionnaire)  # {'a': 1, 'b': 2, 'c': 3}

# Avec transformation
dictionnaire = {cle.upper(): valeur * 2 for cle, valeur in donnees}
print(dictionnaire)  # {'A': 2, 'B': 4, 'C': 6}
