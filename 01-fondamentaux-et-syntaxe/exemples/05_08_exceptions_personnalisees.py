# ============================================================================
#   Section 5.9 : Exceptions personnalisées
#   Description : Créer ses propres exceptions, avec attributs personnalisés
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Exception simple ---
class AgeInvalideError(Exception):
    pass

def verifier_age(age):
    if age < 0:
        raise AgeInvalideError("L'âge ne peut pas être négatif")
    if age > 150:
        raise AgeInvalideError("L'âge semble irréaliste")
    return True

try:
    verifier_age(-5)
except AgeInvalideError as e:
    print(f"Erreur de validation : {e}")

try:
    verifier_age(200)
except AgeInvalideError as e:
    print(f"Erreur de validation : {e}")

# --- Exception avec attributs personnalisés ---
print()

class SoldeInsuffisantError(Exception):
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        message = f"Solde insuffisant : {solde}€ disponible, {montant}€ requis"
        super().__init__(message)

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError(solde, montant)
    return solde - montant

try:
    nouveau_solde = retirer(100, 150)
except SoldeInsuffisantError as e:
    print(e)
    print(f"Manque : {e.montant - e.solde}€")
