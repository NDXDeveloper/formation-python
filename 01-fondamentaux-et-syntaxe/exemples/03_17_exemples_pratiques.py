# ============================================================================
#   Section 3.17 : Exemples pratiques complets
#   Description : Nombre premier, triangle de Pascal (non-interactif) ;
#                 Menu, jeu du plus ou moins, PGCD, classification d'âge,
#                 mot de passe (interactif avec --interactif)
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

import sys

# ---- Exemples non-interactifs ----

# --- Vérifier si un nombre est premier ---
nombre = 29

if nombre < 2:
    print(f"{nombre} n'est pas premier")
else:
    est_premier = True

    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            est_premier = False
            break

    if est_premier:
        print(f"{nombre} est premier")
    else:
        print(f"{nombre} n'est pas premier")

# --- Triangle de Pascal ---
n = 5
print(f"\nTriangle de Pascal ({n} lignes) :")

for i in range(n):
    # Espaces pour centrer
    for j in range(n - i - 1):
        print(" ", end="")

    # Calculer les coefficients binomiaux
    nombre = 1
    for j in range(i + 1):
        print(nombre, end=" ")
        nombre = nombre * (i - j) // (j + 1)

    print()

# --- PGCD (algorithme d'Euclide, non-interactif) ---
a, b = 48, 18
a_orig, b_orig = a, b

while b != 0:
    reste = a % b
    a = b
    b = reste

print(f"\nPGCD({a_orig}, {b_orig}) = {a}")

# ---- Exemples interactifs ----
if len(sys.argv) > 1 and sys.argv[1] == "--interactif":
    print("\n=== Exemples interactifs ===")
    print("1. Mot de passe")
    print("2. Classification d'âge")
    print("3. Deviner un nombre")
    print("4. PGCD interactif")
    print("5. Nombre premier interactif")

    choix = input("\nVotre choix : ")

    if choix == "1":
        mot_de_passe = input("Entrez le mot de passe : ")
        if mot_de_passe == "python123":
            print("Accès autorisé")
            print("Bienvenue dans le système")
        else:
            print("Accès refusé")
            print("Mot de passe incorrect")

    elif choix == "2":
        age = int(input("Quel est votre âge ? "))
        if age < 0:
            print("Âge invalide")
        elif age < 2:
            print("Vous êtes un bébé")
        elif age < 12:
            print("Vous êtes un enfant")
        elif age < 18:
            print("Vous êtes un adolescent")
        elif age < 60:
            print("Vous êtes un adulte")
        else:
            print("Vous êtes un senior")

    elif choix == "3":
        import random
        nombre_secret = random.randint(1, 100)
        tentatives = 0
        max_tentatives = 10

        print(f"Devinez le nombre entre 1 et 100 ({max_tentatives} tentatives)")

        while tentatives < max_tentatives:
            tentatives += 1
            essai = int(input(f"Tentative {tentatives}/{max_tentatives} : "))

            if essai < nombre_secret:
                print("C'est plus !")
            elif essai > nombre_secret:
                print("C'est moins !")
            else:
                print(f"Bravo ! Trouvé en {tentatives} tentative(s) !")
                break
        else:
            print(f"Perdu ! Le nombre était {nombre_secret}")

    elif choix == "4":
        a = int(input("Premier nombre : "))
        b = int(input("Deuxième nombre : "))
        a_orig, b_orig = a, b

        while b != 0:
            reste = a % b
            a = b
            b = reste

        print(f"Le PGCD de {a_orig} et {b_orig} est : {a}")

    elif choix == "5":
        nombre = int(input("Entrez un nombre : "))

        if nombre < 2:
            print(f"{nombre} n'est pas premier")
        else:
            est_premier = True
            for i in range(2, int(nombre ** 0.5) + 1):
                if nombre % i == 0:
                    est_premier = False
                    break

            if est_premier:
                print(f"{nombre} est premier")
            else:
                print(f"{nombre} n'est pas premier")
else:
    if not (len(sys.argv) > 1 and sys.argv[1] == "--interactif"):
        print("\nExemples interactifs disponibles avec --interactif")
        print("  python3 03_17_exemples_pratiques.py --interactif")
