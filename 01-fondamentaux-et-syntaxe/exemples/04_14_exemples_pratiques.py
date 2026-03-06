# ============================================================================
#   Section 4.14 : Exemples pratiques complets
#   Description : Validateur email, calculateur de prix, générateur de
#                 mot de passe, calculateur de statistiques
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

import random
import string

# --- Validateur d'email ---
def valider_email(email: str) -> bool:
    """Vérifie si un email est valide (vérification basique)."""
    if not email:
        return False
    if email.count("@") != 1:
        return False
    parties = email.split("@")
    if not parties[0] or not parties[1]:
        return False
    if "." not in parties[1]:
        return False
    return True

print("=== Validateur d'email ===")
print(valider_email("alice@example.com"))  # True
print(valider_email("bob@"))               # False
print(valider_email("charlie"))            # False

# --- Calculateur de prix ---
print("\n=== Calculateur de prix ===")

def calculer_prix_final(prix_ht: float,
                       quantite: int = 1,
                       taux_remise: float = 0,
                       taux_tva: float = 0.20) -> dict:
    """Calcule le prix final avec remise et TVA."""
    montant_ht = prix_ht * quantite
    montant_remise = montant_ht * taux_remise
    montant_ht_apres_remise = montant_ht - montant_remise
    montant_tva = montant_ht_apres_remise * taux_tva
    montant_ttc = montant_ht_apres_remise + montant_tva

    return {
        "prix_unitaire_ht": prix_ht,
        "quantite": quantite,
        "montant_ht": montant_ht,
        "taux_remise": taux_remise,
        "montant_remise": montant_remise,
        "montant_ht_apres_remise": montant_ht_apres_remise,
        "montant_tva": montant_tva,
        "montant_ttc": montant_ttc
    }

resultat = calculer_prix_final(100, quantite=5, taux_remise=0.1)
print(f"Prix TTC : {resultat['montant_ttc']:.2f}€")
# 100*5 = 500, remise 10% = 50, HT après remise = 450, TVA = 90, TTC = 540

# --- Générateur de mot de passe ---
print("\n=== Générateur de mot de passe ===")

def generer_mot_de_passe(longueur: int = 12,
                         avec_majuscules: bool = True,
                         avec_chiffres: bool = True,
                         avec_symboles: bool = True) -> str:
    """Génère un mot de passe aléatoire."""
    caracteres = string.ascii_lowercase

    if avec_majuscules:
        caracteres += string.ascii_uppercase
    if avec_chiffres:
        caracteres += string.digits
    if avec_symboles:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

print(f"Mot de passe (12 chars) : {generer_mot_de_passe()}")
print(f"Mot de passe (8, sans symboles) : {generer_mot_de_passe(8, avec_symboles=False)}")
print(f"Mot de passe (16 chars) : {generer_mot_de_passe(16)}")

# --- Calculateur de statistiques ---
print("\n=== Statistiques ===")

def calculer_statistiques(nombres: list) -> dict:
    """Calcule diverses statistiques sur une liste de nombres."""
    if not nombres:
        return None

    nombres_tries = sorted(nombres)
    n = len(nombres)

    moyenne = sum(nombres) / n

    if n % 2 == 0:
        mediane = (nombres_tries[n//2 - 1] + nombres_tries[n//2]) / 2
    else:
        mediane = nombres_tries[n//2]

    minimum = min(nombres)
    maximum = max(nombres)
    etendue = maximum - minimum

    return {
        "nombre_valeurs": n,
        "moyenne": moyenne,
        "mediane": mediane,
        "minimum": minimum,
        "maximum": maximum,
        "etendue": etendue
    }

notes = [12, 15, 10, 18, 14, 16, 11, 13]
stats = calculer_statistiques(notes)

for cle, valeur in stats.items():
    print(f"{cle}: {valeur}")
