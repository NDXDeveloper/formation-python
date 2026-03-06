# ============================================================================
#   Section 2.15 : Entrée Utilisateur avec input()
#   Description : Lecture d'entrée utilisateur, conversion de types
#   Fichier source : 02-variables-types-et-operateurs.md
#   Note : Exemples interactifs, exécuter directement pour tester
# ============================================================================

import sys

if len(sys.argv) > 1 and sys.argv[1] == "--interactif":
    print("=== Exemple 1 : input() basique ===")
    nom = input("Quel est votre nom ? ")
    print("Bonjour, " + nom + " !")

    print("\n=== Exemple 2 : input() avec conversion ===")
    age_texte = input("Quel est votre âge ? ")
    print(type(age_texte))  # Affiche : <class 'str'>

    # Pour utiliser l'âge dans un calcul, il faut le convertir
    age = int(age_texte)
    annee_naissance = 2025 - age
    print(f"Vous êtes né en {annee_naissance}")

    print("\n=== Exemple 3 : Conversion directe ===")
    age = int(input("Quel est votre âge ? "))
    taille = float(input("Quelle est votre taille en mètres ? "))
    print(f"Vous avez {age} ans et vous mesurez {taille}m")
else:
    print("Exemples interactifs avec input().")
    print("Exécutez avec --interactif pour tester :")
    print("  python3 02_15_entree_utilisateur.py --interactif")
    print()

    # Démonstration non-interactive des concepts
    print("--- Démonstration sans input() ---")

    # input() retourne toujours une chaîne
    age_texte = "25"
    print(f"type(age_texte) = {type(age_texte)}")  # <class 'str'>

    # Conversion pour calculs
    age = int(age_texte)
    annee_naissance = 2025 - age
    print(f"Vous êtes né en {annee_naissance}")  # 2000
