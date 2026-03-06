# ============================================================================
#   Section 2.2 : Bonnes pratiques des compréhensions
#   Description : Lisibilité, limiter la complexité, noms expressifs,
#                 quand ne PAS utiliser les compréhensions
#   Fichier source : 02-comprehensions.md
# ============================================================================

# --- 1. Privilégiez la lisibilité ---
# Plus lisible avec des étapes intermédiaires
carres_pairs = [y**2 for y in range(10) if y % 2 == 0]
resultat = [x * 2 for x in carres_pairs if x > 10]
print(f"Étapes intermédiaires : {resultat}")

# --- 2. Limiter la complexité ---
donnees = {"A": [1, -2, 3, -4], "B": [5, -6, 7], "C": [8, 9]}

# Clair avec boucle traditionnelle
resultat = {}
for k, v in donnees.items():
    if len(v) > 2:
        resultat[k] = [x * 2 for x in v if x > 0]
print(f"Boucle traditionnelle : {resultat}")

# --- 3. Noms expressifs ---
liste_prix = [5, 15, 25, 8, 30]
prix_eleves = [prix for prix in liste_prix if prix > 10]
print(f"Prix élevés (> 10) : {prix_eleves}")

# --- 4. Quand ne PAS utiliser ---
# Utilisez une boucle normale pour les effets de bord
nombres = [1, 2, 3]
print("Boucle normale pour print :")
for x in nombres:
    print(f"  -> {x}")
