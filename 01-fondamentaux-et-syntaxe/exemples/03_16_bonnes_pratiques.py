# ============================================================================
#   Section 3.16 : Bonnes pratiques avec les structures de contrôle
#   Description : Simplicité, conditions claires, retours précoces,
#                 choix du bon type de boucle
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Simplicité avant tout ---
age = 20

# Bon : Simple et clair
if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# --- Utiliser des noms de variables descriptifs ---
a_permis = True

est_majeur = age >= 18

if est_majeur and a_permis:
    print("Peut conduire")

# --- Retours précoces pour simplifier ---
def verifier_acces(age, a_billet):
    if age < 18:
        return "Accès interdit - mineur"

    if not a_billet:
        return "Accès interdit - pas de billet"

    return "Accès autorisé"

print(verifier_acces(20, True))   # Accès autorisé
print(verifier_acces(15, True))   # Accès interdit - mineur
print(verifier_acces(20, False))  # Accès interdit - pas de billet

# --- Choisir le bon type de boucle ---
# for quand on connaît le nombre d'itérations
print("\nfor range(5) :")
for i in range(5):
    print(i, end=" ")
print()

# while quand c'est conditionnel (ici for est mieux)
print("while < 5 :")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()
