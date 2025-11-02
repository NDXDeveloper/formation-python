🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.2 Création d'exceptions personnalisées

## Pourquoi créer ses propres exceptions ?

Les exceptions intégrées de Python (ValueError, TypeError, etc.) couvrent de nombreux cas, mais parfois vous avez besoin d'exceptions spécifiques à votre application pour :

- **Rendre votre code plus expressif** : Une exception nommée `SoldeInsuffisantError` est plus claire qu'un simple `ValueError`
- **Faciliter la maintenance** : Les exceptions personnalisées documentent les erreurs métier possibles
- **Améliorer la gestion d'erreurs** : Permet de capturer précisément les erreurs de votre domaine
- **Communiquer l'intention** : Le nom de l'exception explique immédiatement ce qui ne va pas

### Exemple de situation

Imaginons une application bancaire :

```python
# ❌ Utiliser une exception générique
if solde < montant:
    raise ValueError("Pas assez d'argent")

# ✅ Utiliser une exception personnalisée
if solde < montant:
    raise SoldeInsuffisantError("Votre solde est insuffisant pour cette opération")
```

## Créer une exception simple

### La syntaxe de base

Pour créer une exception personnalisée, il suffit de créer une classe qui hérite d'`Exception` (ou d'une de ses sous-classes).

```python
class MonException(Exception):
    pass
```

C'est tout ! Vous avez créé votre première exception personnalisée.

### Utilisation

```python
class MonException(Exception):
    pass

# Lever l'exception
raise MonException("Quelque chose s'est mal passé")

# Capturer l'exception
try:
    raise MonException("Une erreur s'est produite")
except MonException as e:
    print(f"Erreur capturée : {e}")
```

## Exceptions avec messages personnalisés

### Méthode 1 : Sans constructeur (le plus simple)

```python
class AgeInvalideError(Exception):
    pass

# Utilisation
age = -5
if age < 0:
    raise AgeInvalideError(f"L'âge ne peut pas être négatif : {age}")
```

### Méthode 2 : Avec un constructeur personnalisé

```python
class AgeInvalideError(Exception):
    def __init__(self, age, message="L'âge fourni est invalide"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} : {self.age}"

# Utilisation
try:
    age = -5
    if age < 0:
        raise AgeInvalideError(age, "L'âge ne peut pas être négatif")
except AgeInvalideError as e:
    print(e)  # Affiche : L'âge ne peut pas être négatif : -5
    print(f"Âge problématique : {e.age}")  # Accès à l'attribut
```

## Exemples concrets d'exceptions personnalisées

### Exemple 1 : Application bancaire

```python
class ErreurBancaire(Exception):
    """Classe de base pour toutes les erreurs bancaires"""
    pass

class SoldeInsuffisantError(ErreurBancaire):
    """Levée quand le solde est insuffisant pour une opération"""
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        message = f"Solde insuffisant. Disponible: {solde}€, Requis: {montant}€"
        super().__init__(message)

class CompteBloqueError(ErreurBancaire):
    """Levée quand le compte est bloqué"""
    pass

class MontantInvalideError(ErreurBancaire):
    """Levée quand le montant est invalide"""
    def __init__(self, montant):
        self.montant = montant
        super().__init__(f"Montant invalide : {montant}€")

# Utilisation dans une classe Compte
class Compte:
    def __init__(self, solde=0):
        self.solde = solde
        self.bloque = False

    def retirer(self, montant):
        if self.bloque:
            raise CompteBloqueError("Ce compte est bloqué")

        if montant <= 0:
            raise MontantInvalideError(montant)

        if montant > self.solde:
            raise SoldeInsuffisantError(self.solde, montant)

        self.solde -= montant
        return self.solde

# Test
compte = Compte(100)

try:
    compte.retirer(150)
except SoldeInsuffisantError as e:
    print(f"Erreur : {e}")
    print(f"Votre solde actuel : {e.solde}€")
except MontantInvalideError as e:
    print(f"Erreur : {e}")
except CompteBloqueError as e:
    print(f"Erreur : {e}")
```

### Exemple 2 : Validation de données utilisateur

```python
class ErreurValidation(Exception):
    """Classe de base pour les erreurs de validation"""
    pass

class EmailInvalideError(ErreurValidation):
    """Levée quand l'email n'est pas au bon format"""
    def __init__(self, email):
        self.email = email
        super().__init__(f"L'email '{email}' n'est pas valide")

class MotDePasseFaibleError(ErreurValidation):
    """Levée quand le mot de passe est trop faible"""
    def __init__(self, raison):
        self.raison = raison
        super().__init__(f"Mot de passe trop faible : {raison}")

class NomUtilisateurExistantError(ErreurValidation):
    """Levée quand le nom d'utilisateur existe déjà"""
    def __init__(self, nom):
        self.nom = nom
        super().__init__(f"Le nom d'utilisateur '{nom}' est déjà pris")

# Fonction de validation
def valider_inscription(email, mot_de_passe, nom_utilisateur, utilisateurs_existants):
    # Validation email
    if "@" not in email or "." not in email:
        raise EmailInvalideError(email)

    # Validation mot de passe
    if len(mot_de_passe) < 8:
        raise MotDePasseFaibleError("Le mot de passe doit contenir au moins 8 caractères")

    if not any(c.isupper() for c in mot_de_passe):
        raise MotDePasseFaibleError("Le mot de passe doit contenir au moins une majuscule")

    # Validation nom d'utilisateur
    if nom_utilisateur in utilisateurs_existants:
        raise NomUtilisateurExistantError(nom_utilisateur)

    return True

# Utilisation
utilisateurs = ["alice", "bob"]

try:
    valider_inscription("john@example.com", "pass", "john", utilisateurs)
except EmailInvalideError as e:
    print(f"❌ {e}")
except MotDePasseFaibleError as e:
    print(f"❌ {e}")
except NomUtilisateurExistantError as e:
    print(f"❌ {e}")
else:
    print("✅ Inscription réussie !")
```

### Exemple 3 : API et codes d'erreur HTTP

```python
class ErreurAPI(Exception):
    """Classe de base pour les erreurs d'API"""
    def __init__(self, message, code_http=500):
        self.code_http = code_http
        super().__init__(message)

class RessourceNonTrouveeError(ErreurAPI):
    """Levée quand une ressource n'est pas trouvée (404)"""
    def __init__(self, ressource):
        self.ressource = ressource
        super().__init__(f"Ressource non trouvée : {ressource}", code_http=404)

class AccesNonAutoriseError(ErreurAPI):
    """Levée quand l'accès n'est pas autorisé (403)"""
    def __init__(self, message="Accès non autorisé"):
        super().__init__(message, code_http=403)

class DonneesInvalidesError(ErreurAPI):
    """Levée quand les données sont invalides (400)"""
    def __init__(self, champs_invalides):
        self.champs_invalides = champs_invalides
        message = f"Données invalides : {', '.join(champs_invalides)}"
        super().__init__(message, code_http=400)

# Simulation d'une API
def obtenir_utilisateur(user_id, token):
    if not token:
        raise AccesNonAutoriseError("Token manquant")

    if user_id not in [1, 2, 3]:
        raise RessourceNonTrouveeError(f"utilisateur/{user_id}")

    return {"id": user_id, "nom": "Alice"}

# Utilisation
try:
    utilisateur = obtenir_utilisateur(999, "mon_token")
except RessourceNonTrouveeError as e:
    print(f"Erreur {e.code_http} : {e}")
except AccesNonAutoriseError as e:
    print(f"Erreur {e.code_http} : {e}")
```

## Hiérarchie d'exceptions personnalisées

Tout comme les exceptions Python standard, vous pouvez créer une hiérarchie d'exceptions personnalisées.

### Structure recommandée

```python
# Exception de base pour votre application
class ErreurApplication(Exception):
    """Classe de base pour toutes les exceptions de l'application"""
    pass

# Catégories d'exceptions
class ErreurBaseDeDonnees(ErreurApplication):
    """Erreurs liées à la base de données"""
    pass

class ErreurReseau(ErreurApplication):
    """Erreurs liées au réseau"""
    pass

class ErreurValidation(ErreurApplication):
    """Erreurs de validation des données"""
    pass

# Exceptions spécifiques
class ConnexionBaseDeDonneesError(ErreurBaseDeDonnees):
    """Impossible de se connecter à la base de données"""
    pass

class RequeteEchoueeError(ErreurBaseDeDonnees):
    """La requête SQL a échoué"""
    pass

class TimeoutReseauError(ErreurReseau):
    """Le réseau a mis trop de temps à répondre"""
    pass
```

### Avantage de la hiérarchie

Vous pouvez capturer à différents niveaux :

```python
try:
    # Code qui peut lever différentes exceptions
    connecter_base_de_donnees()
    executer_requete()
except ConnexionBaseDeDonneesError:
    print("Erreur de connexion spécifique")
except ErreurBaseDeDonnees:
    print("Erreur de base de données générale")
except ErreurApplication:
    print("Erreur générale de l'application")
```

## Ajouter des attributs supplémentaires

Vous pouvez enrichir vos exceptions avec des données utiles :

```python
class ErreurTransfert(Exception):
    """Exception pour les erreurs de transfert d'argent"""
    def __init__(self, message, compte_source, compte_dest, montant, timestamp):
        super().__init__(message)
        self.compte_source = compte_source
        self.compte_dest = compte_dest
        self.montant = montant
        self.timestamp = timestamp

    def generer_rapport(self):
        return f"""
        Rapport d'erreur de transfert :
        --------------------------------
        Date/Heure : {self.timestamp}
        De : {self.compte_source}
        Vers : {self.compte_dest}
        Montant : {self.montant}€
        Erreur : {str(self)}
        """

# Utilisation
from datetime import datetime

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
    # On peut aussi logger les détails
```

## Bonnes pratiques

### ✅ À FAIRE

1. **Hériter d'Exception (ou d'une de ses sous-classes)**
```python
class MonErreur(Exception):  # ✅ Correct
    pass
```

2. **Donner des noms explicites se terminant par "Error"**
```python
class SoldeInsuffisantError(Exception):  # ✅ Clair et explicite
    pass
```

3. **Créer une hiérarchie pour les applications complexes**
```python
class ErreurApp(Exception):
    pass

class ErreurMetier(ErreurApp):
    pass
```

4. **Documenter vos exceptions avec des docstrings**
```python
class AgeInvalideError(Exception):
    """
    Levée quand un âge fourni est invalide.

    L'âge doit être un entier positif entre 0 et 150.
    """
    pass
```

5. **Inclure des informations contextuelles**
```python
class ErreurFichier(Exception):
    def __init__(self, fichier, raison):
        self.fichier = fichier
        self.raison = raison
        super().__init__(f"Erreur avec {fichier} : {raison}")
```

### ❌ À ÉVITER

1. **Hériter de BaseException directement**
```python
class MonErreur(BaseException):  # ❌ Ne faites pas ça !
    pass
```

2. **Créer des exceptions vides sans raison**
```python
# ❌ Si vous n'avez pas besoin de personnalisation
class MonErreur(Exception):
    pass

# ✅ Utilisez plutôt une exception standard
raise ValueError("Message explicite")
```

3. **Capturer vos exceptions trop largement**
```python
# ❌ Trop général
try:
    operation()
except Exception:
    pass

# ✅ Spécifique
try:
    operation()
except MesExceptionsMetier as e:
    gerer_erreur(e)
```

4. **Créer trop d'exceptions pour des cas similaires**
```python
# ❌ Trop spécifique
class EmailVide(Exception): pass
class EmailTropCourt(Exception): pass
class EmailSansArobase(Exception): pass

# ✅ Plus simple
class EmailInvalideError(Exception):
    def __init__(self, email, raison):
        self.email = email
        self.raison = raison
```

## Exemple complet : Système de gestion de bibliothèque

```python
from datetime import datetime, timedelta

# Hiérarchie d'exceptions
class ErreurBibliotheque(Exception):
    """Exception de base pour la bibliothèque"""
    pass

class LivreNonDisponibleError(ErreurBibliotheque):
    """Le livre n'est pas disponible à l'emprunt"""
    def __init__(self, livre, date_retour_prevue=None):
        self.livre = livre
        self.date_retour_prevue = date_retour_prevue
        message = f"Le livre '{livre}' n'est pas disponible"
        if date_retour_prevue:
            message += f" (retour prévu le {date_retour_prevue.strftime('%d/%m/%Y')})"
        super().__init__(message)

class LimiteEmpruntsDepasseeError(ErreurBibliotheque):
    """L'utilisateur a atteint sa limite d'emprunts"""
    def __init__(self, utilisateur, limite):
        self.utilisateur = utilisateur
        self.limite = limite
        super().__init__(
            f"{utilisateur} a atteint la limite de {limite} emprunts simultanés"
        )

class RetardRetourError(ErreurBibliotheque):
    """Le livre est en retard"""
    def __init__(self, livre, jours_retard, amende):
        self.livre = livre
        self.jours_retard = jours_retard
        self.amende = amende
        super().__init__(
            f"Retard de {jours_retard} jours pour '{livre}'. Amende : {amende}€"
        )

# Classe Bibliothèque
class Bibliotheque:
    def __init__(self):
        self.livres = {}  # livre -> disponible (True/False)
        self.emprunts = {}  # utilisateur -> [livres empruntés]
        self.limite_emprunts = 3

    def ajouter_livre(self, titre):
        self.livres[titre] = True

    def emprunter(self, utilisateur, livre):
        # Vérifier que le livre existe
        if livre not in self.livres:
            raise ValueError(f"Le livre '{livre}' n'existe pas dans la bibliothèque")

        # Vérifier la disponibilité
        if not self.livres[livre]:
            date_retour = datetime.now() + timedelta(days=14)
            raise LivreNonDisponibleError(livre, date_retour)

        # Vérifier la limite d'emprunts
        emprunts_utilisateur = self.emprunts.get(utilisateur, [])
        if len(emprunts_utilisateur) >= self.limite_emprunts:
            raise LimiteEmpruntsDepasseeError(utilisateur, self.limite_emprunts)

        # Effectuer l'emprunt
        self.livres[livre] = False
        if utilisateur not in self.emprunts:
            self.emprunts[utilisateur] = []
        self.emprunts[utilisateur].append(livre)
        print(f"✅ '{livre}' emprunté par {utilisateur}")

# Utilisation
biblio = Bibliotheque()
biblio.ajouter_livre("Python pour les débutants")
biblio.ajouter_livre("Le Seigneur des Anneaux")

try:
    biblio.emprunter("Alice", "Python pour les débutants")
    biblio.emprunter("Alice", "Python pour les débutants")  # Déjà emprunté
except LivreNonDisponibleError as e:
    print(f"❌ {e}")
    if e.date_retour_prevue:
        print(f"   Réservez-le pour le {e.date_retour_prevue.strftime('%d/%m/%Y')}")
except LimiteEmpruntsDepasseeError as e:
    print(f"❌ {e}")
except ErreurBibliotheque as e:
    print(f"❌ Erreur : {e}")
```

## Résumé

- Les exceptions personnalisées rendent votre code plus expressif et maintenable
- Héritez toujours d'`Exception` ou d'une de ses sous-classes
- Nommez vos exceptions clairement avec le suffixe "Error"
- Créez une hiérarchie d'exceptions pour les applications complexes
- Ajoutez des attributs pour stocker des informations contextuelles
- Documentez vos exceptions avec des docstrings
- Utilisez `super().__init__(message)` pour initialiser correctement l'exception parente

---

Dans la prochaine section, nous explorerons les techniques de débogage pour identifier et résoudre les problèmes dans votre code.

⏭️ [Techniques de débogage](/09-erreurs-et-debogage/03-techniques-de-debogage.md)
