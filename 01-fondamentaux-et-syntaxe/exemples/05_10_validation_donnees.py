# ============================================================================
#   Section 5.11 : Validation de données utilisateur
#   Description : ValidationError personnalisée, validateur email/age,
#                 création d'utilisateur
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

class ValidationError(Exception):
    """Exception pour les erreurs de validation."""
    pass

def valider_email(email):
    """Valide un email basique."""
    if not email:
        raise ValidationError("L'email ne peut pas être vide")
    if "@" not in email:
        raise ValidationError("L'email doit contenir un @")
    parties = email.split("@")
    if len(parties) != 2:
        raise ValidationError("L'email doit contenir exactement un @")
    if not parties[0]:
        raise ValidationError("La partie avant @ ne peut pas être vide")
    if not parties[1] or "." not in parties[1]:
        raise ValidationError("Le domaine est invalide")

def valider_age(age):
    """Valide un âge."""
    if not isinstance(age, int):
        raise ValidationError("L'âge doit être un nombre entier")
    if age < 0:
        raise ValidationError("L'âge ne peut pas être négatif")
    if age > 150:
        raise ValidationError("L'âge semble irréaliste")

def creer_utilisateur(nom, email, age):
    """Crée un utilisateur après validation."""
    try:
        if not nom or len(nom) < 2:
            raise ValidationError("Le nom doit contenir au moins 2 caractères")
        valider_email(email)
        valider_age(age)

        utilisateur = {"nom": nom, "email": email, "age": age}
        print(f"Utilisateur créé : {nom}")
        return utilisateur

    except ValidationError as e:
        print(f"Erreur de validation : {e}")
        return None

# Exemples d'utilisation
print("Test 1:")
creer_utilisateur("Alice", "alice@example.com", 25)

print("\nTest 2:")
creer_utilisateur("B", "email_invalide", -5)

print("\nTest 3:")
creer_utilisateur("Charlie", "charlie@domain.com", 200)
