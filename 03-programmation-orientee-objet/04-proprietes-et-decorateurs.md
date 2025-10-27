🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.4 Propriétés et Décorateurs

## Introduction

Les **propriétés** et les **décorateurs** sont deux concepts puissants en Python qui permettent de rendre votre code plus élégant, plus maintenable et plus sûr.

- Les **propriétés** permettent de contrôler l'accès aux attributs d'une classe
- Les **décorateurs** permettent de modifier ou d'étendre le comportement de fonctions ou de méthodes

Dans cette section, nous allons découvrir ces deux concepts essentiels de la programmation Python moderne.

## Les Propriétés : Contrôler l'Accès aux Attributs

### Le Problème : Accès Direct aux Attributs

Imaginons une classe `CompteBancaire` :

```python
class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde

compte = CompteBancaire(1000)
print(compte.solde)  # 1000

# Problème : on peut mettre n'importe quelle valeur !
compte.solde = -5000  # Solde négatif : pas logique !
print(compte.solde)   # -5000
```

**Problème** : Rien n'empêche quelqu'un de mettre un solde négatif ou invalide. On aimerait avoir un contrôle sur les valeurs qu'on peut attribuer.

### Solution Traditionnelle : Getters et Setters

Une première solution serait d'utiliser des méthodes :

```python
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde  # Underscore = "privé par convention"

    def get_solde(self):
        return self._solde

    def set_solde(self, valeur):
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur

compte = CompteBancaire(1000)
print(compte.get_solde())  # 1000
compte.set_solde(1500)     # OK
# compte.set_solde(-500)   # ValueError !
```

**Problème** : Cette syntaxe est lourde et peu pythonique. On préférerait écrire `compte.solde` plutôt que `compte.get_solde()`.

### La Solution Python : Les Propriétés

Les propriétés permettent d'utiliser une syntaxe simple (`objet.attribut`) tout en gardant le contrôle !

```python
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde

    @property
    def solde(self):
        """Getter : lecture du solde"""
        return self._solde

    @solde.setter
    def solde(self, valeur):
        """Setter : modification du solde avec validation"""
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur

# Utilisation
compte = CompteBancaire(1000)
print(compte.solde)      # 1000 - Appelle le getter
compte.solde = 1500      # OK - Appelle le setter
print(compte.solde)      # 1500

# compte.solde = -500    # ValueError !
```

**Magie** : On utilise la syntaxe simple `compte.solde`, mais Python appelle automatiquement les bonnes méthodes en arrière-plan !

## Le Décorateur `@property`

### Qu'est-ce qu'un Décorateur ?

Un **décorateur** est une fonction qui modifie le comportement d'une autre fonction ou méthode. En Python, on les reconnaît au symbole `@` suivi du nom du décorateur.

```python
@decorateur
def ma_fonction():
    pass
```

### `@property` : Transformer une Méthode en Attribut

Le décorateur `@property` transforme une méthode en un attribut en lecture seule.

```python
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    @property
    def diametre(self):
        """Calcule le diamètre à partir du rayon"""
        return self.rayon * 2

    @property
    def circonference(self):
        """Calcule la circonférence"""
        return 2 * 3.14159 * self.rayon

    @property
    def surface(self):
        """Calcule la surface"""
        return 3.14159 * self.rayon ** 2

# Utilisation
cercle = Cercle(5)
print(f"Rayon : {cercle.rayon}")              # 5
print(f"Diamètre : {cercle.diametre}")        # 10
print(f"Circonférence : {cercle.circonference}")  # 31.4159
print(f"Surface : {cercle.surface}")          # 78.53975
```

**Avantages** :
- Syntaxe simple et naturelle
- Les valeurs sont calculées à la demande (pas stockées inutilement)
- Impossible de modifier `diametre`, `circonference` ou `surface` directement

## Le Trio : `@property`, `@setter`, `@deleter`

### `@property` : Getter (Lecture)

Permet de lire la valeur d'un attribut.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter : lire la température en Celsius"""
        return self._celsius

temp = Temperature(25)
print(temp.celsius)  # 25
```

### `@attribut.setter` : Setter (Écriture)

Permet de modifier la valeur avec validation.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        """Setter : modifier avec validation"""
        if valeur < -273.15:
            raise ValueError("Température en dessous du zéro absolu !")
        self._celsius = valeur

temp = Temperature(25)
temp.celsius = 30       # OK
print(temp.celsius)     # 30

# temp.celsius = -300   # ValueError !
```

### `@attribut.deleter` : Deleter (Suppression)

Permet de définir ce qui se passe quand on supprime l'attribut avec `del`.

```python
class Personne:
    def __init__(self, nom):
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur

    @nom.deleter
    def nom(self):
        """Deleter : supprimer le nom"""
        print(f"Suppression du nom : {self._nom}")
        self._nom = None

personne = Personne("Alice")
print(personne.nom)    # Alice
del personne.nom       # Suppression du nom : Alice
print(personne.nom)    # None
```

## Exemple Complet : Classe Rectangle

Voici un exemple qui illustre bien l'utilisation des propriétés :

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    # Propriété : largeur
    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur <= 0:
            raise ValueError("La largeur doit être positive")
        self._largeur = valeur

    # Propriété : hauteur
    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        if valeur <= 0:
            raise ValueError("La hauteur doit être positive")
        self._hauteur = valeur

    # Propriétés calculées (read-only)
    @property
    def surface(self):
        """Surface calculée automatiquement"""
        return self._largeur * self._hauteur

    @property
    def perimetre(self):
        """Périmètre calculé automatiquement"""
        return 2 * (self._largeur + self._hauteur)

    def __str__(self):
        return f"Rectangle({self._largeur}x{self._hauteur})"

# Utilisation
rect = Rectangle(5, 3)
print(rect)                    # Rectangle(5x3)
print(f"Surface : {rect.surface}")      # Surface : 15
print(f"Périmètre : {rect.perimetre}")  # Périmètre : 16

# Modifier les dimensions
rect.largeur = 10
rect.hauteur = 4
print(rect)                    # Rectangle(10x4)
print(f"Surface : {rect.surface}")      # Surface : 40 (recalculée automatiquement)

# rect.largeur = -5  # ValueError !
# rect.surface = 100  # AttributeError (read-only)
```

## Exemple Pratique : Classe Personne avec Validation

```python
class Personne:
    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email

    # Propriété : nom
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur.strip().upper()

    # Propriété : prenom
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("Le prénom ne peut pas être vide")
        self._prenom = valeur.strip().capitalize()

    # Propriété : age
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

    # Propriété : email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valeur):
        if '@' not in valeur:
            raise ValueError("Email invalide : doit contenir '@'")
        self._email = valeur.lower()

    # Propriété calculée : nom_complet
    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    # Propriété calculée : est_majeur
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
# personne.age = 200  # ValueError !
# personne.email = "invalide"  # ValueError !
```

## Les Décorateurs : Concepts Fondamentaux

### Qu'est-ce qu'un Décorateur ?

Un décorateur est une fonction qui prend une autre fonction en paramètre et retourne une nouvelle fonction modifiée.

```python
def mon_decorateur(fonction):
    def wrapper():
        print("Avant l'appel de la fonction")
        fonction()
        print("Après l'appel de la fonction")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

# Appel
dire_bonjour()
```

**Résultat :**
```
Avant l'appel de la fonction
Bonjour !
Après l'appel de la fonction
```

**Ce qui se passe** : Le `@mon_decorateur` est équivalent à :
```python
dire_bonjour = mon_decorateur(dire_bonjour)
```

### Décorateur Simple : Chronomètre

```python
import time

def chronometre(fonction):
    """Décorateur qui mesure le temps d'exécution d'une fonction"""
    def wrapper():
        debut = time.time()
        fonction()
        fin = time.time()
        duree = fin - debut
        print(f"Temps d'exécution : {duree:.4f} secondes")
    return wrapper

@chronometre
def tache_longue():
    print("Début de la tâche...")
    time.sleep(2)
    print("Fin de la tâche.")

tache_longue()
```

**Résultat :**
```
Début de la tâche...
Fin de la tâche.
Temps d'exécution : 2.0012 secondes
```

### Décorateur avec Arguments

Pour créer un décorateur qui fonctionne avec des fonctions ayant des arguments :

```python
def logger(fonction):
    """Décorateur qui affiche les appels de fonction"""
    def wrapper(*args, **kwargs):
        print(f"Appel de {fonction.__name__} avec args={args}, kwargs={kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"Résultat : {resultat}")
        return resultat
    return wrapper

@logger
def additionner(a, b):
    return a + b

@logger
def saluer(nom, message="Bonjour"):
    return f"{message} {nom} !"

# Utilisation
resultat1 = additionner(5, 3)
print()
resultat2 = saluer("Alice", message="Salut")
```

**Résultat :**
```
Appel de additionner avec args=(5, 3), kwargs={}
Résultat : 8

Appel de saluer avec args=('Alice',), kwargs={'message': 'Salut'}
Résultat : Salut Alice !
```

**Explication** :
- `*args` : capture tous les arguments positionnels
- `**kwargs` : capture tous les arguments nommés

## Décorateurs Pratiques

### 1. Décorateur de Cache (Mémoïsation)

```python
def cache(fonction):
    """Mémorise les résultats des appels précédents"""
    resultats_sauvegardes = {}

    def wrapper(*args):
        if args in resultats_sauvegardes:
            print(f"Résultat en cache pour {args}")
            return resultats_sauvegardes[args]

        print(f"Calcul pour {args}")
        resultat = fonction(*args)
        resultats_sauvegardes[args] = resultat
        return resultat

    return wrapper

@cache
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Premier appel : calcul complet
print(f"fibonacci(5) = {fibonacci(5)}")
print()

# Deuxième appel : résultats en cache
print(f"fibonacci(5) = {fibonacci(5)}")
```

### 2. Décorateur de Validation

```python
def valider_positif(fonction):
    """Vérifie que tous les arguments sont positifs"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument négatif non autorisé : {arg}")

        for valeur in kwargs.values():
            if isinstance(valeur, (int, float)) and valeur < 0:
                raise ValueError(f"Argument négatif non autorisé : {valeur}")

        return fonction(*args, **kwargs)
    return wrapper

@valider_positif
def calculer_surface_rectangle(largeur, hauteur):
    return largeur * hauteur

print(calculer_surface_rectangle(5, 3))   # 15
# print(calculer_surface_rectangle(-5, 3))  # ValueError !
```

### 3. Décorateur de Retry (Nouvelle Tentative)

```python
import time

def retry(max_tentatives=3, delai=1):
    """Réessaie la fonction en cas d'échec"""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for tentative in range(max_tentatives):
                try:
                    return fonction(*args, **kwargs)
                except Exception as e:
                    print(f"Tentative {tentative + 1}/{max_tentatives} échouée : {e}")
                    if tentative < max_tentatives - 1:
                        print(f"Nouvelle tentative dans {delai} seconde(s)...")
                        time.sleep(delai)
                    else:
                        print("Échec définitif.")
                        raise
        return wrapper
    return decorateur

# Simulation d'une fonction qui échoue parfois
import random

@retry(max_tentatives=3, delai=1)
def operation_instable():
    print("Tentative d'opération...")
    if random.random() < 0.7:  # 70% de chance d'échouer
        raise ConnectionError("Échec de connexion")
    return "Succès !"

try:
    resultat = operation_instable()
    print(f"Résultat final : {resultat}")
except Exception as e:
    print(f"Erreur finale : {e}")
```

### 4. Décorateur de Compteur d'Appels

```python
def compteur_appels(fonction):
    """Compte le nombre de fois qu'une fonction est appelée"""
    def wrapper(*args, **kwargs):
        wrapper.nombre_appels += 1
        print(f"Appel n°{wrapper.nombre_appels} de {fonction.__name__}")
        return fonction(*args, **kwargs)

    wrapper.nombre_appels = 0
    return wrapper

@compteur_appels
def saluer(nom):
    return f"Bonjour {nom} !"

print(saluer("Alice"))
print(saluer("Bob"))
print(saluer("Charlie"))
print(f"\nLa fonction a été appelée {saluer.nombre_appels} fois")
```

## Décorateurs avec Paramètres

Pour créer un décorateur qui accepte des paramètres, il faut ajouter un niveau supplémentaire de fonction :

```python
def repeter(nombre_fois):
    """Décorateur qui répète l'exécution d'une fonction"""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for i in range(nombre_fois):
                print(f"Exécution {i+1}/{nombre_fois}")
                resultat = fonction(*args, **kwargs)
            return resultat
        return wrapper
    return decorateur

@repeter(nombre_fois=3)
def afficher_message(message):
    print(f"Message : {message}")

afficher_message("Bonjour !")
```

**Résultat :**
```
Exécution 1/3
Message : Bonjour !
Exécution 2/3
Message : Bonjour !
Exécution 3/3
Message : Bonjour !
```

### Exemple : Décorateur de Debug avec Niveau

```python
def debug(niveau="INFO"):
    """Décorateur de debug avec niveau de log"""
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            print(f"[{niveau}] Appel de {fonction.__name__}")
            print(f"[{niveau}] Arguments : args={args}, kwargs={kwargs}")
            resultat = fonction(*args, **kwargs)
            print(f"[{niveau}] Résultat : {resultat}")
            return resultat
        return wrapper
    return decorateur

@debug(niveau="DEBUG")
def multiplier(a, b):
    return a * b

@debug(niveau="INFO")
def diviser(a, b):
    return a / b

resultat1 = multiplier(5, 3)
print()
resultat2 = diviser(10, 2)
```

## Empiler Plusieurs Décorateurs

On peut appliquer plusieurs décorateurs à une même fonction :

```python
def gras(fonction):
    def wrapper():
        return "<b>" + fonction() + "</b>"
    return wrapper

def italique(fonction):
    def wrapper():
        return "<i>" + fonction() + "</i>"
    return wrapper

def souligne(fonction):
    def wrapper():
        return "<u>" + fonction() + "</u>"
    return wrapper

@gras
@italique
@souligne
def texte():
    return "Python"

print(texte())  # <b><i><u>Python</u></i></b>
```

**Ordre d'application** : Les décorateurs s'appliquent de bas en haut (de celui le plus proche de la fonction au plus éloigné).

## Décorateurs de Classe

Les décorateurs peuvent aussi s'appliquer aux classes entières :

```python
def ajouter_id(classe):
    """Ajoute un ID unique à chaque instance"""
    classe_originale_init = classe.__init__
    compteur = [0]  # Liste pour permettre la modification dans la closure

    def nouvelle_init(self, *args, **kwargs):
        compteur[0] += 1
        self.id = compteur[0]
        classe_originale_init(self, *args, **kwargs)

    classe.__init__ = nouvelle_init
    return classe

@ajouter_id
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit #{self.id} : {self.nom} - {self.prix}€"

p1 = Produit("Livre", 15)
p2 = Produit("Stylo", 2)
p3 = Produit("Cahier", 5)

print(p1)  # Produit #1 : Livre - 15€
print(p2)  # Produit #2 : Stylo - 2€
print(p3)  # Produit #3 : Cahier - 5€
```

## Décorateurs Built-in de Python

Python fournit plusieurs décorateurs intégrés :

### `@staticmethod`

Définit une méthode qui n'a pas accès à `self` ou à `cls`. C'est simplement une fonction regroupée dans une classe.

```python
class Mathematiques:
    @staticmethod
    def additionner(a, b):
        """Méthode statique : pas besoin d'instance"""
        return a + b

    @staticmethod
    def multiplier(a, b):
        return a * b

# Appel sans créer d'instance
print(Mathematiques.additionner(5, 3))   # 8
print(Mathematiques.multiplier(4, 7))    # 28

# On peut aussi l'appeler depuis une instance
math = Mathematiques()
print(math.additionner(2, 3))  # 5
```

### `@classmethod`

Définit une méthode qui reçoit la classe (pas l'instance) comme premier argument.

```python
class Personne:
    nombre_personnes = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.nombre_personnes += 1

    @classmethod
    def creer_depuis_naissance(cls, nom, annee_naissance):
        """Factory method : crée une personne à partir de l'année de naissance"""
        from datetime import datetime
        age = datetime.now().year - annee_naissance
        return cls(nom, age)

    @classmethod
    def nombre_total(cls):
        """Retourne le nombre total de personnes créées"""
        return cls.nombre_personnes

# Utilisation normale
p1 = Personne("Alice", 30)

# Utilisation avec classmethod
p2 = Personne.creer_depuis_naissance("Bob", 1990)

print(f"{p2.nom} a {p2.age} ans")
print(f"Nombre total de personnes : {Personne.nombre_total()}")
```

### Comparaison : Méthode d'Instance vs Statique vs Classe

```python
class Demo:
    attribut_classe = "Je suis un attribut de classe"

    def __init__(self, valeur):
        self.attribut_instance = valeur

    def methode_instance(self):
        """A accès à self et à la classe"""
        return f"Instance: {self.attribut_instance}, Classe: {self.attribut_classe}"

    @classmethod
    def methode_classe(cls):
        """A accès à la classe, pas à l'instance"""
        return f"Classe: {cls.attribut_classe}"

    @staticmethod
    def methode_statique():
        """N'a accès ni à self ni à cls"""
        return "Je suis une méthode statique"

# Créer une instance
obj = Demo("ma valeur")

# Méthode d'instance : besoin d'une instance
print(obj.methode_instance())

# Méthode de classe : peut être appelée sur la classe ou l'instance
print(Demo.methode_classe())
print(obj.methode_classe())

# Méthode statique : peut être appelée sur la classe ou l'instance
print(Demo.methode_statique())
print(obj.methode_statique())
```

## Exemple Complet : Classe avec Propriétés et Décorateurs

```python
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
print(user1)                      # Alice Dupont (29/30 ans) - alice@example.com
print(f"Majeur : {user1.est_majeur}")  # True

# Factory method
user2 = Utilisateur.creer_mineur("Bob Martin", "bob@example.com", 16)
print(user2)                      # Bob Martin (16 ans) - bob@example.com
print(f"Majeur : {user2.est_majeur}")  # False

# Méthode statique
email_test = "test@example.com"
if Utilisateur.valider_format_email(email_test):
    print(f"{email_test} est valide")

# Nombre total d'utilisateurs
print(f"\nNombre total d'utilisateurs : {Utilisateur.nombre_utilisateurs}")
```

## Préserver les Métadonnées avec `functools.wraps`

Quand on crée un décorateur, la fonction décorée perd ses métadonnées (nom, docstring, etc.). Pour les préserver :

```python
from functools import wraps

def mon_decorateur(fonction):
    @wraps(fonction)  # Préserve les métadonnées
    def wrapper(*args, **kwargs):
        print("Avant")
        resultat = fonction(*args, **kwargs)
        print("Après")
        return resultat
    return wrapper

@mon_decorateur
def ma_fonction():
    """Ceci est ma fonction"""
    print("Ma fonction")

print(ma_fonction.__name__)  # ma_fonction (au lieu de wrapper)
print(ma_fonction.__doc__)   # Ceci est ma fonction
```

**Bonne pratique** : Toujours utiliser `@wraps(fonction)` dans vos décorateurs.

## Bonnes Pratiques

### 1. Utiliser les Propriétés pour la Validation

```python
# ✓ Bon : validation dans le setter
class Produit:
    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, valeur):
        if valeur < 0:
            raise ValueError("Prix négatif interdit")
        self._prix = valeur
```

### 2. Propriétés Read-Only pour les Calculs

```python
# ✓ Bon : pas de setter pour les valeurs calculées
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    @property
    def surface(self):
        return 3.14159 * self.rayon ** 2

    # Pas de @surface.setter - c'est read-only
```

### 3. Utiliser `@classmethod` pour les Factory Methods

```python
# ✓ Bon : factory method avec @classmethod
class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    @classmethod
    def aujourdhui(cls):
        """Crée une date pour aujourd'hui"""
        from datetime import datetime
        now = datetime.now()
        return cls(now.day, now.month, now.year)
```

### 4. Utiliser `@staticmethod` pour les Fonctions Utilitaires

```python
# ✓ Bon : fonction utilitaire avec @staticmethod
class StringUtils:
    @staticmethod
    def inverser(texte):
        return texte[::-1]

    @staticmethod
    def compter_mots(texte):
        return len(texte.split())
```

### 5. Toujours Utiliser `@wraps` dans les Décorateurs

```python
from functools import wraps

# ✓ Bon
def mon_decorateur(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper
```

## Résumé

### Propriétés

| Décorateur | Usage | Quand l'utiliser |
|------------|-------|------------------|
| `@property` | Getter (lecture) | Toujours pour exposer un attribut |
| `@attribut.setter` | Setter (écriture) | Quand on veut valider ou transformer |
| `@attribut.deleter` | Deleter (suppression) | Rarement nécessaire |

**Avantages des propriétés** :
- Syntaxe simple et naturelle
- Validation automatique
- Calculs à la demande
- Encapsulation propre

### Décorateurs

| Décorateur | Usage | Exemple |
|------------|-------|---------|
| `@staticmethod` | Méthode sans accès à l'instance | Fonctions utilitaires |
| `@classmethod` | Méthode avec accès à la classe | Factory methods |
| Décorateurs personnalisés | Modifier le comportement | Logging, cache, timing |

**Avantages des décorateurs** :
- Réutilisation du code
- Séparation des préoccupations
- Code plus lisible et maintenable
- Aspect-Oriented Programming

## Conclusion

Les **propriétés** et les **décorateurs** sont des outils essentiels en Python qui permettent de :
- **Contrôler** l'accès aux attributs avec élégance
- **Valider** les données automatiquement
- **Calculer** des valeurs à la demande
- **Modifier** le comportement des fonctions de manière réutilisable
- **Écrire** du code plus propre et plus pythonique

**Points clés à retenir** :
- Utilisez `@property` pour exposer des attributs avec contrôle
- Utilisez `@attribut.setter` pour valider les modifications
- Les décorateurs modifient le comportement des fonctions
- `@staticmethod` pour les fonctions sans instance
- `@classmethod` pour les factory methods
- Créez vos propres décorateurs pour réutiliser du code
- Utilisez `@wraps` pour préserver les métadonnées

Dans la prochaine section, nous explorerons les **métaclasses et la programmation avancée**, qui permettent de contrôler encore plus finement la création et le comportement des classes !

⏭️ [Métaclasses et programmation avancée](/03-programmation-orientee-objet/05-metaclasses-et-prog-avancee.md)
