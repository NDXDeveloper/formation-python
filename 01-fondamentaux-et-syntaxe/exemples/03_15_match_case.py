# ============================================================================
#   Section 3.15 : L'instruction match/case (Python 3.10+)
#   Description : Pattern matching - codes HTTP, motifs multiples
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Exemple : code HTTP ---
code = 404

match code:
    case 200:
        print("Succès")
    case 301 | 302:
        print("Redirection")
    case 404:
        print("Page non trouvée")
    case 500:
        print("Erreur serveur")
    case _:
        print(f"Code HTTP : {code}")

# --- Test avec d'autres codes ---
print()
for code in [200, 301, 404, 500, 418]:
    match code:
        case 200:
            print(f"{code} → Succès")
        case 301 | 302:
            print(f"{code} → Redirection")
        case 404:
            print(f"{code} → Page non trouvée")
        case 500:
            print(f"{code} → Erreur serveur")
        case _:
            print(f"{code} → Code HTTP inconnu")
