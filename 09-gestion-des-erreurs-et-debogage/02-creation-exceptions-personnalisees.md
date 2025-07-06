🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.2 : Création d'exceptions personnalisées

## Introduction

Imaginez que vous développez un jeu vidéo. Quand un joueur essaie d'acheter un objet sans avoir assez d'argent, quelle exception utiliser ? `ValueError` ? `TypeError` ? Aucune des exceptions Python standards ne décrit vraiment cette situation !

C'est là que les exceptions personnalisées entrent en jeu. Elles vous permettent de créer des erreurs spécifiques à votre application, rendant votre code plus expressif et plus facile à déboguer.

## Pourquoi créer des exceptions personnalisées ?

### 1. Clarté du code
```python
# ❌ Pas très clair
if solde < prix:
    raise ValueError("Pas assez d'argent")

# ✅ Beaucoup plus clair !
if solde < prix:
    raise SoldeInsuffisantError("Pas assez d'argent")
```

### 2. Gestion spécifique
```python
try:
    acheter_objet(joueur, objet)
except SoldeInsuffisantError:
    print("Vous n'avez pas assez d'argent !")
except ObjetIndisponibleError:
    print("Cet objet n'est plus disponible")
except NiveauInsuffisantError:
    print("Votre niveau est trop bas pour cet objet")
```

### 3. Maintenance facilitée
Les exceptions personnalisées rendent votre code plus professionnel et plus facile à maintenir.

## Création d'exceptions simples

### La base : hériter d'Exception

```python
class MonErreurPersonnalisee(Exception):
    """Exception personnalisée pour mon application"""
    pass

# Utilisation
def ma_fonction():
    raise MonErreurPersonnalisee("Quelque chose s'est mal passé")

try:
    ma_fonction()
except MonErreurPersonnalisee as e:
    print(f"Erreur capturée : {e}")
```

### Exemple concret : Gestion d'âge

```python
class AgeInvalideError(Exception):
    """Exception levée quand l'âge est invalide"""
    pass

def verifier_age(age):
    if age < 0:
        raise AgeInvalideError("L'âge ne peut pas être négatif")
    if age > 150:
        raise AgeInvalideError("L'âge ne peut pas dépasser 150 ans")
    return True

# Tests
try:
    verifier_age(-5)
except AgeInvalideError as e:
    print(f"Erreur : {e}")  # Erreur : L'âge ne peut pas être négatif

try:
    verifier_age(200)
except AgeInvalideError as e:
    print(f"Erreur : {e}")  # Erreur : L'âge ne peut pas dépasser 150 ans
```

## Exceptions avec des attributs personnalisés

### Ajouter des informations supplémentaires

```python
class CompteError(Exception):
    """Exception pour les opérations sur les comptes bancaires"""

    def __init__(self, message, solde_actuel, montant_demande):
        super().__init__(message)
        self.solde_actuel = solde_actuel
        self.montant_demande = montant_demande

    def __str__(self):
        return f"{self.args[0]} (Solde: {self.solde_actuel}€, Demandé: {self.montant_demande}€)"

def retirer_argent(solde, montant):
    if montant > solde:
        raise CompteError(
            "Solde insuffisant",
            solde_actuel=solde,
            montant_demande=montant
        )
    return solde - montant

# Utilisation
try:
    nouveau_solde = retirer_argent(100, 150)
except CompteError as e:
    print(f"Erreur : {e}")
    print(f"Il vous manque {e.montant_demande - e.solde_actuel}€")
```

## Hiérarchie d'exceptions personnalisées

### Créer une famille d'exceptions

```python
# Exception de base pour notre application
class JeuError(Exception):
    """Exception de base pour le jeu"""
    pass

# Exceptions spécifiques
class JoueurError(JeuError):
    """Erreurs liées au joueur"""
    pass

class InventaireError(JeuError):
    """Erreurs liées à l'inventaire"""
    pass

class CombatError(JeuError):
    """Erreurs liées au combat"""
    pass

# Exceptions encore plus spécifiques
class SoldeInsuffisantError(JoueurError):
    """Le joueur n'a pas assez d'argent"""
    pass

class NiveauInsuffisantError(JoueurError):
    """Le niveau du joueur est trop bas"""
    pass

class InventairePleinError(InventaireError):
    """L'inventaire est plein"""
    pass

class ObjetIntrouvableError(InventaireError):
    """L'objet n'est pas dans l'inventaire"""
    pass
```

### Utilisation de la hiérarchie

```python
def acheter_objet(joueur, objet):
    # Vérifications diverses
    if joueur.niveau < objet.niveau_requis:
        raise NiveauInsuffisantError(
            f"Niveau {objet.niveau_requis} requis (vous êtes niveau {joueur.niveau})"
        )

    if joueur.argent < objet.prix:
        raise SoldeInsuffisantError(
            f"Prix: {objet.prix} or (vous avez {joueur.argent} or)"
        )

    if len(joueur.inventaire) >= joueur.taille_inventaire:
        raise InventairePleinError("Inventaire plein ! Vendez des objets d'abord")

    # Achat réussi
    joueur.argent -= objet.prix
    joueur.inventaire.append(objet)

# Gestion avec la hiérarchie
try:
    acheter_objet(mon_joueur, epee_legendaire)
except NiveauInsuffisantError as e:
    print(f"❌ {e}")
except SoldeInsuffisantError as e:
    print(f"💰 {e}")
except InventairePleinError as e:
    print(f"🎒 {e}")
except JoueurError as e:  # Capture toutes les erreurs de joueur
    print(f"⚠️ Erreur joueur : {e}")
except JeuError as e:     # Capture toutes les erreurs du jeu
    print(f"🎮 Erreur de jeu : {e}")
```

## Exemples pratiques par domaine

### 1. Validation de données

```python
class ValidationError(Exception):
    """Exception pour les erreurs de validation"""
    pass

class EmailInvalideError(ValidationError):
    """Email invalide"""
    pass

class MotDePasseTropFaibleError(ValidationError):
    """Mot de passe trop faible"""
    pass

def valider_utilisateur(email, mot_de_passe):
    if "@" not in email:
        raise EmailInvalideError("L'email doit contenir un @")

    if len(mot_de_passe) < 8:
        raise MotDePasseTropFaibleError("Le mot de passe doit faire au moins 8 caractères")

    return True

# Utilisation
try:
    valider_utilisateur("alice.example.com", "123")
except EmailInvalideError as e:
    print(f"📧 {e}")
except MotDePasseTropFaibleError as e:
    print(f"🔒 {e}")
except ValidationError as e:
    print(f"❌ Erreur de validation : {e}")
```

### 2. API et web

```python
class APIError(Exception):
    """Exception de base pour l'API"""
    pass

class RessourceIntrouvableError(APIError):
    """Ressource non trouvée (404)"""
    def __init__(self, ressource_id):
        super().__init__(f"Ressource {ressource_id} introuvable")
        self.ressource_id = ressource_id
        self.status_code = 404

class AccesRefuseError(APIError):
    """Accès refusé (403)"""
    def __init__(self, message="Accès refusé"):
        super().__init__(message)
        self.status_code = 403

def obtenir_utilisateur(user_id, token):
    if not token:
        raise AccesRefuseError("Token manquant")

    if user_id not in base_utilisateurs:
        raise RessourceIntrouvableError(user_id)

    return base_utilisateurs[user_id]

# Gestion
try:
    utilisateur = obtenir_utilisateur(123, None)
except RessourceIntrouvableError as e:
    print(f"Erreur {e.status_code}: {e}")
except AccesRefuseError as e:
    print(f"Erreur {e.status_code}: {e}")
```

## Bonnes pratiques

### 1. Nommage des exceptions

```python
# ✅ Bon : se terminent par "Error" ou "Exception"
class ConfigurationError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

# ❌ Éviter : noms peu clairs
class Problem(Exception):
    pass

class Bad(Exception):
    pass
```

### 2. Documentation

```python
class CalculatriceError(Exception):
    """
    Exception de base pour les erreurs de la calculatrice.

    Cette exception est levée quand une opération mathématique
    ne peut pas être effectuée.
    """
    pass

class DivisionParZeroError(CalculatriceError):
    """
    Exception levée lors d'une division par zéro.

    Attributes:
        numerateur -- le numérateur de la division
        denominateur -- le dénominateur (toujours 0)
    """

    def __init__(self, numerateur, denominateur=0):
        message = f"Division impossible : {numerateur} / {denominateur}"
        super().__init__(message)
        self.numerateur = numerateur
        self.denominateur = denominateur
```

### 3. Héritage approprié

```python
# ✅ Bon : hériter de la classe appropriée
class MonFichierError(OSError):  # Erreurs liées aux fichiers
    pass

class MonValidationError(ValueError):  # Erreurs de validation
    pass

class MonTypeError(TypeError):  # Erreurs de type
    pass

# ✅ Ou créer sa propre hiérarchie
class MonAppError(Exception):
    """Exception de base pour mon application"""
    pass
```

## Exercices pratiques

### Exercice 1 : Système de notes

Créez des exceptions pour un système de gestion de notes :

```python
class NoteError(Exception):
    """Exception de base pour les notes"""
    pass

class NoteInvalideError(NoteError):
    """Note en dehors de la plage valide"""
    pass

class EtudiantIntrouvableError(NoteError):
    """Étudiant non trouvé"""
    pass

def ajouter_note(etudiant_id, note):
    """
    Ajoute une note à un étudiant.
    Note doit être entre 0 et 20.
    """
    # À compléter !
    pass

# Tests
try:
    ajouter_note("12345", 25)  # Doit lever NoteInvalideError
except NoteInvalideError as e:
    print(f"Erreur : {e}")
```

### Exercice 2 : E-commerce

Créez des exceptions pour un système e-commerce :

```python
class BoutiqueError(Exception):
    """Exception de base pour la boutique"""
    pass

# Créez les exceptions suivantes :
# - ProduitIndisponibleError
# - StockInsuffisantError
# - PrixInvalideError
# - ClientIntrouvableError

def commander_produit(client_id, produit_id, quantite):
    """
    Commande un produit pour un client.
    Doit gérer tous les cas d'erreur possibles.
    """
    # À compléter !
    pass
```

## Résumé

Les exceptions personnalisées vous permettent de :

1. **Rendre votre code plus expressif** avec des noms d'erreurs significatifs
2. **Organiser vos erreurs** dans une hiérarchie logique
3. **Ajouter des informations supplémentaires** aux exceptions
4. **Faciliter la maintenance** et le débogage

**Étapes pour créer une exception personnalisée :**
1. Hériter de `Exception` ou d'une exception plus spécifique
2. Ajouter un docstring explicatif
3. Personnaliser `__init__` si nécessaire
4. Optionnellement, personnaliser `__str__` pour l'affichage

**Conseils :**
- Utilisez des noms expressifs terminés par "Error"
- Documentez vos exceptions
- Créez une hiérarchie logique
- N'hésitez pas à ajouter des attributs utiles

Dans la section suivante, nous verrons comment utiliser les outils de débogage pour traquer efficacement ces exceptions dans votre code !

---

**À retenir :** Les exceptions personnalisées sont comme des panneaux de signalisation sur mesure pour votre code. Elles guident les développeurs (y compris vous !) vers la source du problème.

⏭️
