# ============================================================================
#   Section 3.4 : Exemple complet - Classe avec propriétés et décorateurs
#   Description : Classe Utilisateur combinant propriétés, décorateur de
#                 validation, @classmethod, @staticmethod et propriétés calculées
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

from datetime import datetime

def valider_email(fonction):
    """Décorateur pour valider les emails"""
    def wrapper(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError(f"Email invalide : {email}")
        return fonction(self, email)
    return wrapper

class Utilisateur:
    """Classe représentant un utilisateur avec validation"""

    # Attribut de classe
    nombre_utilisateurs = 0

    def __init__(self, nom, email, date_naissance):
        self.nom = nom
        self.email = email
        self.date_naissance = date_naissance
        Utilisateur.nombre_utilisateurs += 1

    # Propriété : nom
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur or len(valeur.strip()) < 2:
            raise ValueError("Le nom doit contenir au moins 2 caractères")
        self._nom = valeur.strip()

    # Propriété : email avec décorateur personnalisé
    @property
    def email(self):
        return self._email

    @email.setter
    @valider_email
    def email(self, valeur):
        self._email = valeur.lower()

    # Propriété : date_naissance
    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, valeur):
        if not isinstance(valeur, datetime):
            raise TypeError("La date doit être un objet datetime")
        if valeur > datetime.now():
            raise ValueError("La date de naissance ne peut pas être dans le futur")
        self._date_naissance = valeur

    # Propriété calculée : age
    @property
    def age(self):
        """Calcule l'âge automatiquement"""
        aujourd_hui = datetime.now()
        age = aujourd_hui.year - self.date_naissance.year
        # Ajuster si l'anniversaire n'est pas encore passé cette année
        if (aujourd_hui.month, aujourd_hui.day) < (self.date_naissance.month, self.date_naissance.day):
            age -= 1
        return age

    # Propriété calculée : est_majeur
    @property
    def est_majeur(self):
        return self.age >= 18

    # Méthode de classe
    @classmethod
    def creer_mineur(cls, nom, email, age):
        """Factory method pour créer un utilisateur mineur"""
        date_naissance = datetime(datetime.now().year - age, 1, 1)
        return cls(nom, email, date_naissance)

    # Méthode statique
    @staticmethod
    def valider_format_email(email):
        """Vérifie si un email est valide"""
        return '@' in email and '.' in email

    def __str__(self):
        return f"{self.nom} ({self.age} ans) - {self.email}"

# Utilisation
user1 = Utilisateur("Alice Dupont", "alice@example.com", datetime(1995, 5, 15))
print(user1)
print(f"Majeur : {user1.est_majeur}")  # True

# Factory method
user2 = Utilisateur.creer_mineur("Bob Martin", "bob@example.com", 16)
print(user2)
print(f"Majeur : {user2.est_majeur}")  # False

# Méthode statique
email_test = "test@example.com"
if Utilisateur.valider_format_email(email_test):
    print(f"{email_test} est valide")

# Nombre total d'utilisateurs
print(f"\nNombre total d'utilisateurs : {Utilisateur.nombre_utilisateurs}")
