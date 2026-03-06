# ============================================================================
#   Section 4.1 : Écriture dans des fichiers texte
#   Description : Mode 'w' (écrasement), mode 'a' (ajout), writelines()
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

import os

# --- Mode 'w' - Écriture (écrase le contenu existant) ---
fichier = open('nouveau_fichier.txt', 'w', encoding='utf-8')
fichier.write("Bonjour, ceci est la première ligne\n")
fichier.write("Et voici la deuxième ligne\n")
fichier.close()

# Vérification
with open('nouveau_fichier.txt', 'r', encoding='utf-8') as f:
    print("=== Après écriture mode 'w' ===")
    print(f.read())

# --- Mode 'a' - Ajout (conserve le contenu existant) ---
fichier = open('nouveau_fichier.txt', 'a', encoding='utf-8')
fichier.write("Cette ligne est ajoutée à la fin\n")
fichier.write("Et encore une autre ligne\n")
fichier.close()

# Vérification
with open('nouveau_fichier.txt', 'r', encoding='utf-8') as f:
    print("=== Après ajout mode 'a' ===")
    print(f.read())

# --- Écrire plusieurs lignes avec writelines() ---
fichier = open('liste_courses.txt', 'w', encoding='utf-8')

courses = [
    "Pommes\n",
    "Pain\n",
    "Lait\n",
    "Fromage\n"
]

fichier.writelines(courses)
fichier.close()

# Vérification
with open('liste_courses.txt', 'r', encoding='utf-8') as f:
    print("=== writelines() ===")
    print(f.read())

# Nettoyage
os.remove('nouveau_fichier.txt')
os.remove('liste_courses.txt')
