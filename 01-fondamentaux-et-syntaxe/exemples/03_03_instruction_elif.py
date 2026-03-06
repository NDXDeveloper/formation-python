# ============================================================================
#   Section 3.3 : L'instruction elif (système de notes)
#   Description : Tester plusieurs conditions successivement
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Système de notes ---
note = 15

if note >= 16:
    print("Mention Très Bien")
elif note >= 14:
    print("Mention Bien")
elif note >= 12:
    print("Mention Assez Bien")
elif note >= 10:
    print("Admis")
else:
    print("Non admis")
# Résultat : Mention Bien (car note = 15, qui est >= 14)
