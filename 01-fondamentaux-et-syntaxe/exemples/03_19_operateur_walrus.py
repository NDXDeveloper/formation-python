# ============================================================================
#   Section 3.19 : L'opérateur walrus := (Python 3.8+)
#   Description : Affectation dans une expression - if (réutiliser une valeur),
#                 compréhension (éviter un double calcul), while (lire + tester)
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- if : calculer une fois et réutiliser ---
nombres = [3, 7, 2, 9, 4, 8, 1]
if (n := len(nombres)) > 5:
    print(f"La liste contient {n} éléments (plus de 5)")

# --- Compréhension : éviter un double calcul ---
def carre(x):
    return x * x


# carre(x) n'est évalué qu'une seule fois par élément
resultats = [c for x in range(6) if (c := carre(x)) > 4]
print(f"Carrés > 4 : {resultats}")  # [9, 16, 25]

# --- while : lire et tester en une seule expression ---
# Version non interactive : on consomme une file de saisies simulées.
# En interactif : while (mot := input("Mot (ou 'fin') : ")) != "fin":
saisies = iter(["bonjour", "python", "fin", "ignoré"])
print("\nLecture jusqu'à 'fin' :")
while (mot := next(saisies, "fin")) != "fin":
    print(f"  Mot reçu : {mot}")
