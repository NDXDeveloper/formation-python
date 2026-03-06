# ============================================================================
#   Section 9.2 : Creation d'exceptions personnalisees
#   Description : Exceptions simples, avec constructeur personnalise,
#                 application bancaire, validation de donnees, API avec
#                 codes HTTP, hierarchie d'exceptions, attributs supplementaires
#   Fichier source : 02-exceptions-personnalisees.md
# ============================================================================

from datetime import datetime

# ==========================================
# 1. Exception simple
# ==========================================
print("=== Exception simple ===")

class MonException(Exception):
    pass

try:
    raise MonException("Une erreur s'est produite")
except MonException as e:
    print(f"  Erreur capturee : {e}")

# ==========================================
# 2. Exception avec constructeur personnalise
# ==========================================
print("\n=== Exception avec constructeur ===")

class AgeInvalideError(Exception):
    def __init__(self, age, message="L'age fourni est invalide"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} : {self.age}"

try:
    age = -5
    if age < 0:
        raise AgeInvalideError(age, "L'age ne peut pas etre negatif")
except AgeInvalideError as e:
    print(f"  {e}")
    print(f"  Age problematique : {e.age}")

# ==========================================
# 3. Application bancaire
# ==========================================
print("\n=== Application bancaire ===")

class ErreurBancaire(Exception):
    """Classe de base pour toutes les erreurs bancaires"""
    pass

class SoldeInsuffisantError(ErreurBancaire):
    """Levee quand le solde est insuffisant pour une operation"""
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        message = f"Solde insuffisant. Disponible: {solde}EUR, Requis: {montant}EUR"
        super().__init__(message)

class CompteBloqueError(ErreurBancaire):
    """Levee quand le compte est bloque"""
    pass

class MontantInvalideError(ErreurBancaire):
    """Levee quand le montant est invalide"""
    def __init__(self, montant):
        self.montant = montant
        super().__init__(f"Montant invalide : {montant}EUR")

class Compte:
    def __init__(self, solde=0):
        self.solde = solde
        self.bloque = False

    def retirer(self, montant):
        if self.bloque:
            raise CompteBloqueError("Ce compte est bloque")
        if montant <= 0:
            raise MontantInvalideError(montant)
        if montant > self.solde:
            raise SoldeInsuffisantError(self.solde, montant)
        self.solde -= montant
        return self.solde

compte = Compte(100)

try:
    compte.retirer(150)
except SoldeInsuffisantError as e:
    print(f"  Erreur : {e}")
    print(f"  Votre solde actuel : {e.solde}EUR")
except MontantInvalideError as e:
    print(f"  Erreur : {e}")
except CompteBloqueError as e:
    print(f"  Erreur : {e}")

# ==========================================
# 4. Validation de donnees utilisateur
# ==========================================
print("\n=== Validation de donnees ===")

class ErreurValidation(Exception):
    """Classe de base pour les erreurs de validation"""
    pass

class EmailInvalideError(ErreurValidation):
    def __init__(self, email):
        self.email = email
        super().__init__(f"L'email '{email}' n'est pas valide")

class MotDePasseFaibleError(ErreurValidation):
    def __init__(self, raison):
        self.raison = raison
        super().__init__(f"Mot de passe trop faible : {raison}")

class NomUtilisateurExistantError(ErreurValidation):
    def __init__(self, nom):
        self.nom = nom
        super().__init__(f"Le nom d'utilisateur '{nom}' est deja pris")

def valider_inscription(email, mot_de_passe, nom_utilisateur, utilisateurs_existants):
    if "@" not in email or "." not in email:
        raise EmailInvalideError(email)
    if len(mot_de_passe) < 8:
        raise MotDePasseFaibleError("Le mot de passe doit contenir au moins 8 caracteres")
    if not any(c.isupper() for c in mot_de_passe):
        raise MotDePasseFaibleError("Le mot de passe doit contenir au moins une majuscule")
    if nom_utilisateur in utilisateurs_existants:
        raise NomUtilisateurExistantError(nom_utilisateur)
    return True

utilisateurs = ["alice", "bob"]

try:
    valider_inscription("john@example.com", "pass", "john", utilisateurs)
except EmailInvalideError as e:
    print(f"  {e}")
except MotDePasseFaibleError as e:
    print(f"  {e}")
except NomUtilisateurExistantError as e:
    print(f"  {e}")
else:
    print("  Inscription reussie !")

# ==========================================
# 5. API et codes d'erreur HTTP
# ==========================================
print("\n=== API et codes HTTP ===")

class ErreurAPI(Exception):
    def __init__(self, message, code_http=500):
        self.code_http = code_http
        super().__init__(message)

class RessourceNonTrouveeError(ErreurAPI):
    def __init__(self, ressource):
        self.ressource = ressource
        super().__init__(f"Ressource non trouvee : {ressource}", code_http=404)

class AccesNonAutoriseError(ErreurAPI):
    def __init__(self, message="Acces non autorise"):
        super().__init__(message, code_http=403)

class DonneesInvalidesError(ErreurAPI):
    def __init__(self, champs_invalides):
        self.champs_invalides = champs_invalides
        message = f"Donnees invalides : {', '.join(champs_invalides)}"
        super().__init__(message, code_http=400)

def obtenir_utilisateur(user_id, token):
    if not token:
        raise AccesNonAutoriseError("Token manquant")
    if user_id not in [1, 2, 3]:
        raise RessourceNonTrouveeError(f"utilisateur/{user_id}")
    return {"id": user_id, "nom": "Alice"}

try:
    utilisateur = obtenir_utilisateur(999, "mon_token")
except RessourceNonTrouveeError as e:
    print(f"  Erreur {e.code_http} : {e}")
except AccesNonAutoriseError as e:
    print(f"  Erreur {e.code_http} : {e}")

# ==========================================
# 6. Exception avec attributs supplementaires
# ==========================================
print("\n=== Exception avec rapport ===")

class ErreurTransfert(Exception):
    def __init__(self, message, compte_source, compte_dest, montant, timestamp):
        super().__init__(message)
        self.compte_source = compte_source
        self.compte_dest = compte_dest
        self.montant = montant
        self.timestamp = timestamp

    def generer_rapport(self):
        return (
            f"  Rapport d'erreur de transfert :\n"
            f"  --------------------------------\n"
            f"  Date/Heure : {self.timestamp}\n"
            f"  De : {self.compte_source}\n"
            f"  Vers : {self.compte_dest}\n"
            f"  Montant : {self.montant}EUR\n"
            f"  Erreur : {str(self)}"
        )

try:
    raise ErreurTransfert(
        "Solde insuffisant",
        compte_source="FR123456",
        compte_dest="FR789012",
        montant=1000,
        timestamp=datetime.now()
    )
except ErreurTransfert as e:
    print(e.generer_rapport())
