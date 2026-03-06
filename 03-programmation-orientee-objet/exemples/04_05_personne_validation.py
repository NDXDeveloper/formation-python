# ============================================================================
#   Section 3.4 : Personne avec validation complète
#   Description : Validation nom (upper), prénom (capitalize), âge (0-150),
#                 email (@), propriétés calculées
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

class Personne:
    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur.strip().upper()

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("Le prénom ne peut pas être vide")
        self._prenom = valeur.strip().capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("L'âge doit être un entier")
        if valeur < 0 or valeur > 150:
            raise ValueError("L'âge doit être entre 0 et 150")
        self._age = valeur

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valeur):
        if '@' not in valeur:
            raise ValueError("Email invalide : doit contenir '@'")
        self._email = valeur.lower()

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    @property
    def est_majeur(self):
        return self.age >= 18

    def __str__(self):
        return f"{self.nom_complet} ({self.age} ans)"

# Utilisation
personne = Personne("  dupont  ", "MARIE", 25, "Marie.Dupont@Example.COM")

print(personne.nom)         # DUPONT (formaté automatiquement)
print(personne.prenom)      # Marie (formaté automatiquement)
print(personne.email)       # marie.dupont@example.com (formaté)
print(personne.nom_complet) # Marie DUPONT
print(personne.est_majeur)  # True
print(personne)             # Marie DUPONT (25 ans)

# Validation automatique
personne.age = 30  # OK
print(f"Nouvel âge : {personne.age}")

try:
    personne.age = 200  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")

try:
    personne.email = "invalide"  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")
