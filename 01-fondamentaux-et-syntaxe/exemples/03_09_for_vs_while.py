# ============================================================================
#   Section 3.9 : Comparaison for vs while
#   Description : Même résultat avec les deux types de boucle
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# Même résultat avec for et while

# Avec for (plus simple quand on connaît le nombre)
print("Avec for :")
for i in range(5):
    print(i)

# Avec while (plus flexible mais plus verbeux)
print("\nAvec while :")
i = 0
while i < 5:
    print(i)
    i += 1
