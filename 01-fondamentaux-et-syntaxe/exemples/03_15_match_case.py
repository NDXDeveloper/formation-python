# ============================================================================
#   Section 3.15 : L'instruction match/case (Python 3.10+)
#   Description : Pattern matching - menu (motif simple), motifs multiples (|),
#                 codes HTTP
#   Fichier source : 03-structures-de-controle.md
# ============================================================================

# --- Menu de commande (motif simple) ---
commande = "thé"  # en interactif : commande = input("Votre commande : ")
match commande:
    case "café":
        print("Voici votre café ☕")
    case "thé":
        print("Voici votre thé 🍵")
    case "jus":
        print("Voici votre jus 🧃")
    case _:
        print("Commande non disponible")

# --- Motifs multiples avec | ---
print()
jour = "samedi"  # en interactif : jour = input("Quel jour ? ")
match jour:
    case "samedi" | "dimanche":
        print("C'est le weekend !")
    case "lundi" | "mardi" | "mercredi" | "jeudi" | "vendredi":
        print("C'est un jour de semaine")
    case _:
        print("Jour non reconnu")

# --- Exemple : code HTTP ---
print()
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
