# ============================================================================
#   Section 4.3 : L'instruction return
#   Description : Retourner une valeur, print vs return, types de retour,
#                 return arrête la fonction, fonction sans return
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Return de base ---
def additionner(a, b):
    resultat = a + b
    return resultat

somme = additionner(5, 3)
print(somme)  # Affiche : 8

total = additionner(10, 20) + additionner(5, 5)
print(total)  # Affiche : 40 (30 + 10)

# --- Différence print() vs return ---
print("\n--- print() vs return ---")

def additionner_print(a, b):
    print(a + b)

resultat = additionner_print(5, 3)  # Affiche : 8
print(resultat)  # Affiche : None

def additionner_return(a, b):
    return a + b

resultat = additionner_return(5, 3)
print(resultat)  # Affiche : 8

# --- Retourner différents types ---
print("\n--- Types de retour ---")

def est_majeur(age):
    return age >= 18

def obtenir_info():
    return "Alice", 25, "France"

majeur = est_majeur(20)
print(majeur)  # Affiche : True

nom, age, pays = obtenir_info()
print(f"{nom}, {age} ans, {pays}")  # Affiche : Alice, 25 ans, France

# --- Return arrête l'exécution ---
print("\n--- Return précoce ---")

def verifier_age(age):
    if age < 0:
        return "Âge invalide"

    if age < 18:
        return "Mineur"

    return "Majeur"

print(verifier_age(25))   # Affiche : Majeur
print(verifier_age(15))   # Affiche : Mineur
print(verifier_age(-5))   # Affiche : Âge invalide

# --- Fonction sans return ---
print("\n--- Sans return ---")

def dire_bonjour():
    print("Bonjour !")

resultat = dire_bonjour()
print(resultat)  # Affiche : None
