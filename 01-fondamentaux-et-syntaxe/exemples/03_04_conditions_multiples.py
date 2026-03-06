# ============================================================================
#   Section 3.4 : Conditions multiples (and, or, not)
#   Description : Combiner plusieurs conditions avec opérateurs logiques
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Opérateur and ---
age = 25
a_permis = True

if age >= 18 and a_permis:
    print("Vous pouvez conduire")
else:
    print("Vous ne pouvez pas conduire")

# --- Opérateur or ---
jour = "samedi"

if jour == "samedi" or jour == "dimanche":
    print("C'est le weekend !")
else:
    print("C'est un jour de semaine")

# --- Opérateur not ---
est_pluie = False

if not est_pluie:
    print("Vous pouvez sortir sans parapluie")
else:
    print("Prenez un parapluie")

# --- Combiner plusieurs opérateurs ---
age = 25
a_permis = True
a_voiture = False

if age >= 18 and a_permis and a_voiture:
    print("Vous pouvez conduire votre voiture")
elif age >= 18 and a_permis and not a_voiture:
    print("Vous pouvez conduire mais vous n'avez pas de voiture")
else:
    print("Vous ne pouvez pas conduire")
