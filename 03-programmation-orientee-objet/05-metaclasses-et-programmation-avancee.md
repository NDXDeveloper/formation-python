🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.5 : Métaclasses et programmation avancée

## Introduction

Vous avez appris que les objets sont des instances de classes. Mais savez-vous que **les classes elles-mêmes sont des objets** ? Et si les classes sont des objets, de quoi sont-elles des instances ? C'est là qu'interviennent les **métaclasses** - les "classes des classes" !

Cette section explore des concepts avancés de la programmation orientée objet. Rassurez-vous : même si ces concepts sont sophistiqués, nous les aborderons progressivement avec des exemples concrets.

## Comprendre que tout est objet en Python

En Python, **tout** est un objet, même les classes :

```python
# Les nombres sont des objets
nombre = 42
print(type(nombre))        # <class 'int'>
print(type(int))          # <class 'type'>

# Les fonctions sont des objets
def ma_fonction():
    pass

print(type(ma_fonction))   # <class 'function'>
print(type(type(ma_fonction)))  # <class 'type'>

# Les classes sont aussi des objets !
class MaClasse:
    pass

print(type(MaClasse))      # <class 'type'>
print(type(type))          # <class 'type'>

# On peut même assigner une classe à une variable
AutreNom = MaClasse
instance = AutreNom()      # Fonctionne !
print(type(instance))      # <class '__main__.MaClasse'>
```

### Que nous apprend ceci ?

- `int` est une classe, instance de `type`
- `MaClasse` est une classe, instance de `type`
- `type` est la métaclasse par défaut en Python

## Qu'est-ce qu'une métaclasse ?

Une **métaclasse** est une classe dont les instances sont des classes. En d'autres termes :

- Une **classe** définit comment créer des **objets**
- Une **métaclasse** définit comment créer des **classes**

### Analogie

Imaginez :
- **Moule à gâteau** = Classe (crée des gâteaux/objets)
- **Machine à faire des moules** = Métaclasse (crée des moules/classes)

## Création dynamique de classes

Avant d'aborder les métaclasses, voyons comment créer des classes dynamiquement :

```python
# Méthode 1 : Création normale
class PersonneNormale:
    def __init__(self, nom):
        self.nom = nom

    def saluer(self):
        return f"Bonjour, je suis {self.nom}"

# Méthode 2 : Création dynamique avec type()
def init_personne(self, nom):
    self.nom = nom

def saluer_personne(self):
    return f"Bonjour, je suis {self.nom}"

# Syntaxe : type(nom_classe, (classes_parentes,), {attributs_et_methodes})
PersonneDynamique = type(
    'PersonneDynamique',           # Nom de la classe
    (),                           # Classes parentes (tuple vide = pas d'héritage)
    {                             # Dictionnaire des attributs et méthodes
        '__init__': init_personne,
        'saluer': saluer_personne
    }
)

# Les deux classes fonctionnent de la même façon !
p1 = PersonneNormale("Alice")
p2 = PersonneDynamique("Bob")

print(p1.saluer())  # Bonjour, je suis Alice
print(p2.saluer())  # Bonjour, je suis Bob
print(type(p1))     # <class '__main__.PersonneNormale'>
print(type(p2))     # <class '__main__.PersonneDynamique'>
```

## Première métaclasse simple

Créons notre première métaclasse qui ajoute automatiquement une méthode à toutes les classes qui l'utilisent :

```python
class MetaAvecInfo(type):
    """Métaclasse qui ajoute automatiquement une méthode 'info' à toutes les classes."""

    def __new__(cls, name, bases, attrs):
        """
        Appelée lors de la création de la classe.

        Args:
            cls: La métaclasse elle-même
            name: Le nom de la classe à créer
            bases: Les classes parentes
            attrs: Les attributs et méthodes de la classe
        """
        # Ajouter automatiquement une méthode 'info'
        def info(self):
            return f"Je suis une instance de {self.__class__.__name__}"

        attrs['info'] = info

        # Créer la classe normalement
        return super().__new__(cls, name, bases, attrs)

# Utilisation de la métaclasse
class Personne(metaclass=MetaAvecInfo):
    def __init__(self, nom):
        self.nom = nom

class Voiture(metaclass=MetaAvecInfo):
    def __init__(self, marque):
        self.marque = marque

# Test : toutes les classes ont automatiquement la méthode 'info'
personne = Personne("Alice")
voiture = Voiture("Toyota")

print(personne.info())  # Je suis une instance de Personne
print(voiture.info())   # Je suis une instance de Voiture
```

## Métaclasse avec validation

Créons une métaclasse qui valide que certaines méthodes sont présentes :

```python
class MetaValidation(type):
    """Métaclasse qui valide la présence de méthodes obligatoires."""

    def __new__(cls, name, bases, attrs):
        # Ne pas valider les classes de base
        if name != 'BaseValidee':
            # Vérifier que certaines méthodes sont présentes
            methodes_obligatoires = ['sauvegarder', 'charger']

            for methode in methodes_obligatoires:
                if methode not in attrs:
                    raise AttributeError(
                        f"La classe {name} doit implémenter la méthode '{methode}'"
                    )

                # Vérifier que c'est bien une méthode (callable)
                if not callable(attrs[methode]):
                    raise TypeError(
                        f"'{methode}' doit être une méthode dans la classe {name}"
                    )

        return super().__new__(cls, name, bases, attrs)

# Classe de base utilisant la métaclasse
class BaseValidee(metaclass=MetaValidation):
    pass

# Cette classe sera validée par la métaclasse
class Document(BaseValidee):
    def __init__(self, contenu):
        self.contenu = contenu

    def sauvegarder(self):
        return f"Sauvegarde du document : {self.contenu[:20]}..."

    def charger(self):
        return f"Chargement du document"

# Test : cette classe fonctionne car elle a les méthodes obligatoires
doc = Document("Contenu important")
print(doc.sauvegarder())

# Cette classe provoquera une erreur à la définition
try:
    class DocumentIncomplet(BaseValidee):
        def __init__(self, contenu):
            self.contenu = contenu

        # Manque les méthodes 'sauvegarder' et 'charger' !
except AttributeError as e:
    print(f"Erreur de validation : {e}")
```

## Métaclasse singleton

Créons une métaclasse qui assure qu'une classe ne peut avoir qu'une seule instance (pattern Singleton) :

```python
class MetaSingleton(type):
    """Métaclasse qui implémente le pattern Singleton."""

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        """Appelée quand on crée une instance de la classe."""
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class ConfigurationApp(metaclass=MetaSingleton):
    """Configuration globale de l'application (singleton)."""

    def __init__(self):
        self.parametres = {}
        print("Configuration créée !")

    def definir(self, cle, valeur):
        self.parametres[cle] = valeur

    def obtenir(self, cle):
        return self.parametres.get(cle)

# Test du singleton
config1 = ConfigurationApp()  # Configuration créée !
config2 = ConfigurationApp()  # Pas de nouveau message

print(config1 is config2)     # True : même objet !

config1.definir("theme", "sombre")
print(config2.obtenir("theme"))  # sombre : partage les données !
```

## Métaclasse avec modification d'attributs

```python
class MetaAutoProperty(type):
    """Métaclasse qui convertit automatiquement les attributs en propriétés avec validation."""

    def __new__(cls, name, bases, attrs):
        # Chercher les attributs qui commencent par 'auto_'
        nouvelles_proprietes = {}

        for attr_name, attr_value in list(attrs.items()):
            if attr_name.startswith('auto_') and not callable(attr_value):
                # Créer une propriété automatiquement
                prop_name = attr_name[5:]  # Enlever 'auto_'
                private_name = f'_{prop_name}'

                # Créer le getter
                def make_getter(private_attr):
                    def getter(self):
                        return getattr(self, private_attr)
                    return getter

                # Créer le setter avec validation
                def make_setter(private_attr, default_value):
                    def setter(self, value):
                        # Validation du type basée sur la valeur par défaut
                        if default_value is not None and not isinstance(value, type(default_value)):
                            raise TypeError(f"{prop_name} doit être de type {type(default_value).__name__}")
                        setattr(self, private_attr, value)
                    return setter

                # Créer la propriété
                nouvelles_proprietes[prop_name] = property(
                    make_getter(private_name),
                    make_setter(private_name, attr_value)
                )

                # Supprimer l'attribut original
                del attrs[attr_name]

        # Ajouter les nouvelles propriétés
        attrs.update(nouvelles_proprietes)

        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        # Initialiser les valeurs par défaut
        original_init = attrs.get('__init__')

        def new_init(self, *args, **kwargs):
            # Initialiser les attributs privés avec les valeurs par défaut
            for attr_name in dir(cls):
                if hasattr(cls, attr_name) and isinstance(getattr(cls, attr_name), property):
                    private_name = f'_{attr_name}'
                    if not hasattr(self, private_name):
                        setattr(self, private_name, None)

            # Appeler l'__init__ original s'il existe
            if original_init:
                original_init(self, *args, **kwargs)

        cls.__init__ = new_init

class Produit(metaclass=MetaAutoProperty):
    # Ces attributs seront automatiquement convertis en propriétés
    auto_nom = "Produit par défaut"
    auto_prix = 0.0
    auto_stock = 0

    def __init__(self, nom=None, prix=None, stock=None):
        if nom is not None:
            self.nom = nom
        if prix is not None:
            self.prix = prix
        if stock is not None:
            self.stock = stock

# Test de la métaclasse
produit = Produit("Livre Python", 29.99, 50)

print(f"Nom : {produit.nom}")      # Livre Python
print(f"Prix : {produit.prix}")    # 29.99
print(f"Stock : {produit.stock}")  # 50

# Validation automatique des types
try:
    produit.prix = "gratuit"  # Erreur : type incorrect
except TypeError as e:
    print(f"Erreur : {e}")

# Les propriétés fonctionnent normalement
produit.prix = 24.99
print(f"Nouveau prix : {produit.prix}")
```

## Décorateurs de classe

Une alternative plus simple aux métaclasses pour modifier les classes :

```python
def ajouter_methode_debug(cls):
    """Décorateur qui ajoute une méthode de debug à une classe."""

    def debug(self):
        attributs = []
        for attr, valeur in self.__dict__.items():
            if not attr.startswith('_'):
                attributs.append(f"{attr}={valeur}")
        return f"{cls.__name__}({', '.join(attributs)})"

    cls.debug = debug
    return cls

def compter_instances(cls):
    """Décorateur qui compte les instances créées."""
    cls.nombre_instances = 0

    original_init = cls.__init__

    def nouveau_init(self, *args, **kwargs):
        cls.nombre_instances += 1
        original_init(self, *args, **kwargs)

    cls.__init__ = nouveau_init
    return cls

@ajouter_methode_debug
@compter_instances
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

# Test des décorateurs
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Saint-Exupéry")

print(livre1.debug())  # Livre(titre=1984, auteur=George Orwell)
print(f"Instances créées : {Livre.nombre_instances}")  # 2
```

## Classes abstraites avec ABC

Python fournit le module `abc` pour créer des classes abstraites :

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    """Classe abstraite pour les formes géométriques."""

    @abstractmethod
    def aire(self):
        """Méthode abstraite : doit être implémentée par les sous-classes."""
        pass

    @abstractmethod
    def perimetre(self):
        """Méthode abstraite : doit être implémentée par les sous-classes."""
        pass

    # Méthode concrète (optionnelle)
    def description(self):
        return f"Une forme avec une aire de {self.aire():.2f}"

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14159 * self.rayon ** 2

    def perimetre(self):
        return 2 * 3.14159 * self.rayon

# Test des classes abstraites
rectangle = Rectangle(5, 3)
cercle = Cercle(4)

print(rectangle.description())  # Une forme avec une aire de 15.00
print(cercle.description())     # Une forme avec une aire de 50.27

# Impossible de créer une instance de la classe abstraite
try:
    forme = Forme()  # Erreur !
except TypeError as e:
    print(f"Erreur : {e}")

# Classe incomplète (ne peut pas être instanciée)
try:
    class FormeIncomplete(Forme):
        def aire(self):
            return 0
        # Manque perimetre() !

    forme_incomplete = FormeIncomplete()  # Erreur !
except TypeError as e:
    print(f"Erreur classe incomplète : {e}")
```

## Mixins - Héritage multiple organisé

Les mixins sont des classes conçues pour être héritées avec d'autres classes :

```python
class TimestampMixin:
    """Mixin qui ajoute des fonctionnalités de timestamp."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.cree_le = datetime.now()
        self.modifie_le = self.cree_le

    def marquer_modification(self):
        from datetime import datetime
        self.modifie_le = datetime.now()

    def age_en_secondes(self):
        from datetime import datetime
        return (datetime.now() - self.cree_le).total_seconds()

class SerializationMixin:
    """Mixin qui ajoute des fonctionnalités de sérialisation."""

    def to_dict(self):
        """Convertit l'objet en dictionnaire."""
        result = {}
        for attr, valeur in self.__dict__.items():
            if not attr.startswith('_'):
                # Conversion des datetime en string pour JSON
                if hasattr(valeur, 'isoformat'):
                    result[attr] = valeur.isoformat()
                else:
                    result[attr] = valeur
        return result

    def from_dict(self, data):
        """Charge les données depuis un dictionnaire."""
        for attr, valeur in data.items():
            setattr(self, attr, valeur)

class ValidationMixin:
    """Mixin qui ajoute la validation des données."""

    def valider(self):
        """Valide les données de l'objet."""
        erreurs = []

        # Vérifier les attributs obligatoires
        if hasattr(self, 'ATTRIBUTS_OBLIGATOIRES'):
            for attr in self.ATTRIBUTS_OBLIGATOIRES:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    erreurs.append(f"Attribut obligatoire manquant : {attr}")

        # Vérifier les contraintes personnalisées
        if hasattr(self, 'valider_custom'):
            erreurs_custom = self.valider_custom()
            if erreurs_custom:
                erreurs.extend(erreurs_custom)

        if erreurs:
            raise ValueError("Erreurs de validation : " + ", ".join(erreurs))

        return True

# Utilisation des mixins
class Document(TimestampMixin, SerializationMixin, ValidationMixin):
    ATTRIBUTS_OBLIGATOIRES = ['titre', 'contenu']

    def __init__(self, titre, contenu, auteur="Anonyme"):
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
        super().__init__()  # Initialise les mixins

    def valider_custom(self):
        """Validation personnalisée pour les documents."""
        erreurs = []
        if len(self.titre) < 3:
            erreurs.append("Le titre doit avoir au moins 3 caractères")
        if len(self.contenu) < 10:
            erreurs.append("Le contenu doit avoir au moins 10 caractères")
        return erreurs

    def modifier_contenu(self, nouveau_contenu):
        self.contenu = nouveau_contenu
        self.marquer_modification()

# Test des mixins
doc = Document("Mon Document", "Ceci est le contenu de mon document important.")

# Fonctionnalités du TimestampMixin
print(f"Créé il y a {doc.age_en_secondes():.2f} secondes")

# Fonctionnalités du SerializationMixin
print("Sérialisation :")
print(doc.to_dict())

# Fonctionnalités du ValidationMixin
print("Validation :", doc.valider())  # True

# Test de validation avec erreur
try:
    doc_invalide = Document("X", "Court")
    doc_invalide.valider()
except ValueError as e:
    print(f"Erreur de validation : {e}")
```

## Exemple pratique : Framework ORM simple

Créons un mini-framework ORM utilisant les métaclasses :

```python
class MetaModele(type):
    """Métaclasse pour créer des modèles ORM simples."""

    def __new__(cls, name, bases, attrs):
        # Ne pas traiter la classe de base
        if name == 'Modele':
            return super().__new__(cls, name, bases, attrs)

        # Collecter les champs du modèle
        champs = {}
        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, Champ):
                champs[attr_name] = attr_value
                # Supprimer le champ de la classe (sera géré par __getattr__)
                del attrs[attr_name]

        attrs['_champs'] = champs
        attrs['_donnees'] = {}

        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        """Création d'instance avec initialisation des champs."""
        instance = super().__call__()

        # Initialiser les champs avec les valeurs par défaut
        for nom_champ, champ in cls._champs.items():
            instance._donnees[nom_champ] = champ.valeur_defaut

        # Appliquer les valeurs passées en paramètre
        for nom_champ, valeur in kwargs.items():
            if nom_champ in cls._champs:
                setattr(instance, nom_champ, valeur)

        return instance

class Champ:
    """Représente un champ dans un modèle ORM."""

    def __init__(self, type_champ=str, valeur_defaut=None, obligatoire=False):
        self.type_champ = type_champ
        self.valeur_defaut = valeur_defaut
        self.obligatoire = obligatoire

class Modele(metaclass=MetaModele):
    """Classe de base pour les modèles ORM."""

    def __getattr__(self, name):
        """Accès aux champs du modèle."""
        if name in self._champs:
            return self._donnees.get(name)
        raise AttributeError(f"'{self.__class__.__name__}' n'a pas d'attribut '{name}'")

    def __setattr__(self, name, value):
        """Assignation avec validation des champs."""
        if hasattr(self, '_champs') and name in self._champs:
            champ = self._champs[name]

            # Validation du type
            if value is not None and not isinstance(value, champ.type_champ):
                raise TypeError(f"{name} doit être de type {champ.type_champ.__name__}")

            self._donnees[name] = value
        else:
            super().__setattr__(name, value)

    def valider(self):
        """Valide tous les champs obligatoires."""
        for nom_champ, champ in self._champs.items():
            if champ.obligatoire and self._donnees.get(nom_champ) is None:
                raise ValueError(f"Le champ '{nom_champ}' est obligatoire")

    def sauvegarder(self):
        """Simule la sauvegarde en base de données."""
        self.valider()
        print(f"{self.__class__.__name__} sauvegardé : {self._donnees}")

    def __str__(self):
        donnees_str = ", ".join(f"{k}={v}" for k, v in self._donnees.items())
        return f"{self.__class__.__name__}({donnees_str})"

# Utilisation du framework ORM
class Utilisateur(Modele):
    nom = Champ(str, obligatoire=True)
    email = Champ(str, obligatoire=True)
    age = Champ(int, valeur_defaut=0)
    actif = Champ(bool, valeur_defaut=True)

class Produit(Modele):
    nom = Champ(str, obligatoire=True)
    prix = Champ(float, obligatoire=True)
    description = Champ(str, valeur_defaut="")

# Test du framework
user = Utilisateur(nom="Alice", email="alice@example.com", age=25)
print(user)  # Utilisateur(nom=Alice, email=alice@example.com, age=25, actif=True)

produit = Produit(nom="Livre Python", prix=29.99)
print(produit)  # Produit(nom=Livre Python, prix=29.99, description=)

# Validation et sauvegarde
user.sauvegarder()  # Utilisateur sauvegardé : {...}

# Test de validation
try:
    user_invalide = Utilisateur(nom="Bob")  # Manque l'email
    user_invalide.sauvegarder()
except ValueError as e:
    print(f"Erreur : {e}")
```

## Quand utiliser ces concepts avancés ?

### Métaclasses - Utilisez quand :
- Vous voulez modifier le comportement de **création** de classes
- Vous créez un framework (ORM, API, etc.)
- Vous avez besoin de validation au niveau classe
- Vous voulez ajouter automatiquement des méthodes/attributs

### Décorateurs de classe - Utilisez quand :
- Vous voulez modifier une classe **après** sa création
- C'est plus simple qu'une métaclasse
- Vous voulez une solution réutilisable et lisible

### Classes abstraites - Utilisez quand :
- Vous voulez forcer l'implémentation de certaines méthodes
- Vous créez une interface ou un contrat
- Vous avez une hiérarchie de classes avec comportement commun

### Mixins - Utilisez quand :
- Vous voulez partager des fonctionnalités entre classes non liées
- Vous préférez la composition à l'héritage
- Vous voulez éviter la duplication de code

## Exercices pratiques

### Exercice 1 : Métaclasse de logging
Créez une métaclasse qui ajoute automatiquement du logging à toutes les méthodes d'une classe.

### Exercice 2 : Décorateur de cache
Créez un décorateur de classe qui ajoute un système de cache aux méthodes spécifiées.

### Solutions :

```python
# Solution Exercice 1 : Métaclasse de logging
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class MetaLogging(type):
    """Métaclasse qui ajoute du logging à toutes les méthodes."""

    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                attrs[attr_name] = cls.ajouter_logging(attr_value, name, attr_name)

        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def ajouter_logging(methode, nom_classe, nom_methode):
        @functools.wraps(methode)
        def wrapper(self, *args, **kwargs):
            logging.info(f"{nom_classe}.{nom_methode} appelée avec args={args}, kwargs={kwargs}")
            try:
                resultat = methode(self, *args, **kwargs)
                logging.info(f"{nom_classe}.{nom_methode} terminée avec succès")
                return resultat
            except Exception as e:
                logging.error(f"{nom_classe}.{nom_methode} a échoué: {e}")
                raise
        return wrapper

class CalculatriceAvecLog(metaclass=MetaLogging):
    def additionner(self, a, b):
        return a + b

    def diviser(self, a, b):
        return a / b

# Test
calc = CalculatriceAvecLog()
print(calc.additionner(5, 3))  # Logs automatiques
try:
    calc.diviser(10, 0)
except ZeroDivisionError:
    pass

# Solution Exercice 2 : Décorateur de cache
import functools
import time

def ajouter_cache(*methodes_a_cacher):
    """Décorateur qui ajoute un cache aux méthodes spécifiées."""

    def decorateur(cls):
        # Ajouter un attribut cache à la classe
        cls._cache = {}

        # Ajouter une méthode pour vider le cache
        def vider_cache(self):
            """Vide le cache de l'instance."""
            self._cache.clear()
            print("Cache vidé")

        cls.vider_cache = vider_cache

        # Ajouter une méthode pour voir les statistiques du cache
        def stats_cache(self):
            """Affiche les statistiques du cache."""
            print(f"Éléments en cache : {len(self._cache)}")
            for cle in self._cache.keys():
                print(f"  - {cle[0]}{cle[1]}")

        cls.stats_cache = stats_cache

        # Modifier les méthodes spécifiées
        for nom_methode in methodes_a_cacher:
            if hasattr(cls, nom_methode):
                methode_originale = getattr(cls, nom_methode)
                nouvelle_methode = creer_methode_avec_cache(methode_originale, nom_methode)
                setattr(cls, nom_methode, nouvelle_methode)

        return cls

    def creer_methode_avec_cache(methode, nom_methode):
        @functools.wraps(methode)
        def wrapper(self, *args, **kwargs):
            # Créer une clé de cache
            cle_cache = (nom_methode, args, tuple(sorted(kwargs.items())))

            if cle_cache in self._cache:
                print(f"🟢 Cache hit pour {nom_methode}")
                return self._cache[cle_cache]

            print(f"🔴 Cache miss pour {nom_methode}, calcul en cours...")
            resultat = methode(self, *args, **kwargs)
            self._cache[cle_cache] = resultat
            return resultat

        return wrapper

    return decorateur

@ajouter_cache('fibonacci', 'factorielle', 'calcul_complexe')
class CalculatriceOptimisee:
    def fibonacci(self, n):
        """Calcule le n-ième nombre de Fibonacci."""
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

    def factorielle(self, n):
        """Calcule la factorielle de n."""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def calcul_complexe(self, x, y=1):
        """Simule un calcul complexe."""
        time.sleep(1)  # Simule un calcul long
        return x ** y + x * y

    def calcul_simple(self, a, b):
        """Cette méthode n'a pas de cache."""
        return a + b

# Test du décorateur de cache
print("=== Test du décorateur de cache ===")
calc = CalculatriceOptimisee()

# Premier appel (cache miss)
print(f"Fibonacci(10) = {calc.fibonacci(10)}")

# Deuxième appel (cache hit)
print(f"Fibonacci(10) = {calc.fibonacci(10)}")

# Test avec paramètres différents
print(f"Factorielle(5) = {calc.factorielle(5)}")
print(f"Calcul complexe(3, 2) = {calc.calcul_complexe(3, 2)}")
print(f"Calcul complexe(3, 2) = {calc.calcul_complexe(3, 2)}")  # Cache hit

# Méthode sans cache
print(f"Calcul simple(5, 3) = {calc.calcul_simple(5, 3)}")  # Pas de message de cache

# Statistiques du cache
calc.stats_cache()

# Vider le cache
calc.vider_cache()
```

## Exercice 3 : Système de plugins avec métaclasses

Créons un système de plugins avancé :

```python
class RegistrePlugins:
    """Registre global pour stocker tous les plugins."""
    _plugins = {}

    @classmethod
    def enregistrer(cls, nom, plugin):
        cls._plugins[nom] = plugin
        print(f"Plugin '{nom}' enregistré")

    @classmethod
    def obtenir(cls, nom):
        return cls._plugins.get(nom)

    @classmethod
    def lister(cls):
        return list(cls._plugins.keys())

    @classmethod
    def executer_tous(cls, methode, *args, **kwargs):
        """Exécute une méthode sur tous les plugins qui la supportent."""
        resultats = {}
        for nom, plugin in cls._plugins.items():
            if hasattr(plugin, methode):
                try:
                    resultats[nom] = getattr(plugin, methode)(*args, **kwargs)
                except Exception as e:
                    resultats[nom] = f"Erreur : {e}"
        return resultats

class MetaPlugin(type):
    """Métaclasse qui enregistre automatiquement les plugins."""

    def __new__(cls, name, bases, attrs):
        # Créer la classe normalement
        nouvelle_classe = super().__new__(cls, name, bases, attrs)

        # Enregistrer automatiquement comme plugin (sauf la classe de base)
        if name != 'PluginBase' and attrs.get('_auto_register', True):
            nom_plugin = attrs.get('nom_plugin', name.lower())
            RegistrePlugins.enregistrer(nom_plugin, nouvelle_classe())

        return nouvelle_classe

class PluginBase(metaclass=MetaPlugin):
    """Classe de base pour tous les plugins."""
    _auto_register = False  # Ne pas enregistrer la classe de base

    def initialiser(self):
        """Méthode appelée lors de l'initialisation du plugin."""
        pass

    def finaliser(self):
        """Méthode appelée lors de la finalisation du plugin."""
        pass

# Plugins concrets
class PluginLogging(PluginBase):
    nom_plugin = "logging"

    def __init__(self):
        self.logs = []

    def initialiser(self):
        print("📝 Plugin de logging initialisé")

    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def obtenir_logs(self):
        return self.logs.copy()

    def finaliser(self):
        print(f"📝 Plugin de logging finalisé ({len(self.logs)} logs)")

class PluginCache(PluginBase):
    nom_plugin = "cache"

    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def initialiser(self):
        print("💾 Plugin de cache initialisé")

    def obtenir(self, cle):
        if cle in self.cache:
            self.hits += 1
            return self.cache[cle]
        else:
            self.misses += 1
            return None

    def definir(self, cle, valeur):
        self.cache[cle] = valeur

    def vider(self):
        self.cache.clear()
        print("💾 Cache vidé")

    def statistiques(self):
        total = self.hits + self.misses
        if total > 0:
            taux_hit = (self.hits / total) * 100
            return f"Hits: {self.hits}, Misses: {self.misses}, Taux: {taux_hit:.1f}%"
        return "Aucune statistique disponible"

    def finaliser(self):
        print(f"💾 Plugin de cache finalisé - {self.statistiques()}")

class PluginMetriques(PluginBase):
    nom_plugin = "metriques"

    def __init__(self):
        self.compteurs = {}
        self.temps = {}

    def initialiser(self):
        print("📊 Plugin de métriques initialisé")

    def incrementer(self, nom):
        self.compteurs[nom] = self.compteurs.get(nom, 0) + 1

    def chronometre_start(self, nom):
        import time
        self.temps[nom] = time.time()

    def chronometre_stop(self, nom):
        import time
        if nom in self.temps:
            duree = time.time() - self.temps[nom]
            del self.temps[nom]
            return duree
        return 0

    def rapport(self):
        print("📊 Rapport des métriques :")
        for nom, valeur in self.compteurs.items():
            print(f"  {nom}: {valeur}")

    def finaliser(self):
        print("📊 Plugin de métriques finalisé")
        self.rapport()

# Gestionnaire d'application utilisant les plugins
class GestionnaireApplication:
    def __init__(self):
        self.plugins_actifs = []

    def demarrer(self):
        print("🚀 Démarrage de l'application")

        # Initialiser tous les plugins
        resultats = RegistrePlugins.executer_tous('initialiser')
        print(f"Plugins initialisés : {list(resultats.keys())}")

        # Exemples d'utilisation des plugins
        self.demo_plugins()

    def demo_plugins(self):
        print("\n=== Démonstration des plugins ===")

        # Plugin de logging
        logger = RegistrePlugins.obtenir('logging')
        if logger:
            logger.log("Application démarrée")
            logger.log("Traitement des données")

        # Plugin de cache
        cache = RegistrePlugins.obtenir('cache')
        if cache:
            cache.definir('user_1', {'nom': 'Alice', 'age': 25})
            print(f"Cache - obtenir user_1: {cache.obtenir('user_1')}")
            print(f"Cache - obtenir user_2: {cache.obtenir('user_2')}")  # Miss
            print(f"Statistiques cache: {cache.statistiques()}")

        # Plugin de métriques
        metriques = RegistrePlugins.obtenir('metriques')
        if metriques:
            metriques.incrementer('connexions')
            metriques.incrementer('connexions')
            metriques.incrementer('erreurs')
            metriques.chronometre_start('operation')
            time.sleep(0.1)  # Simule une opération
            duree = metriques.chronometre_stop('operation')
            print(f"Opération terminée en {duree:.3f}s")

    def arreter(self):
        print("\n🛑 Arrêt de l'application")

        # Finaliser tous les plugins
        RegistrePlugins.executer_tous('finaliser')

        print("Application arrêtée")

# Test du système de plugins
print("=== Système de plugins avec métaclasses ===")
print(f"Plugins disponibles : {RegistrePlugins.lister()}")

app = GestionnaireApplication()
app.demarrer()
app.arreter()
```

## Exercice 4 : ORM avancé avec relations

Étendons notre ORM pour supporter les relations entre modèles :

```python
class RelationChamp:
    """Représente une relation vers un autre modèle."""

    def __init__(self, modele_cible, cle_etrangere=None):
        self.modele_cible = modele_cible
        self.cle_etrangere = cle_etrangere or f"{modele_cible.__name__.lower()}_id"

class MetaModeleAvance(type):
    """Métaclasse avancée pour ORM avec relations."""

    def __new__(cls, name, bases, attrs):
        if name == 'ModeleAvance':
            return super().__new__(cls, name, bases, attrs)

        # Collecter les champs et relations
        champs = {}
        relations = {}

        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, Champ):
                champs[attr_name] = attr_value
                del attrs[attr_name]
            elif isinstance(attr_value, RelationChamp):
                relations[attr_name] = attr_value
                del attrs[attr_name]

        attrs['_champs'] = champs
        attrs['_relations'] = relations
        attrs['_donnees'] = {}
        attrs['_instances'] = {}  # Stockage en mémoire pour simulation

        # Ajouter des méthodes de classe pour la gestion des données
        attrs['tous'] = classmethod(cls._tous)
        attrs['trouver_par_id'] = classmethod(cls._trouver_par_id)
        attrs['creer'] = classmethod(cls._creer)

        return super().__new__(cls, name, bases, attrs)

    def _tous(cls):
        """Retourne toutes les instances du modèle."""
        return list(cls._instances.values())

    def _trouver_par_id(cls, id_objet):
        """Trouve un objet par son ID."""
        return cls._instances.get(id_objet)

    def _creer(cls, **kwargs):
        """Crée une nouvelle instance."""
        instance = cls(**kwargs)
        instance.sauvegarder()
        return instance

    def __call__(cls, *args, **kwargs):
        instance = super().__call__()

        # Générer un ID unique
        import uuid
        instance.id = str(uuid.uuid4())[:8]

        # Initialiser les champs
        for nom_champ, champ in cls._champs.items():
            instance._donnees[nom_champ] = champ.valeur_defaut

        # Appliquer les valeurs passées
        for nom_champ, valeur in kwargs.items():
            if nom_champ in cls._champs or nom_champ in cls._relations:
                setattr(instance, nom_champ, valeur)

        return instance

class ModeleAvance(metaclass=MetaModeleAvance):
    """Classe de base pour les modèles ORM avancés."""

    def __getattr__(self, name):
        if name in self._champs:
            return self._donnees.get(name)
        elif name in self._relations:
            relation = self._relations[name]
            cle_etrangere = getattr(self, relation.cle_etrangere, None)
            if cle_etrangere:
                return relation.modele_cible.trouver_par_id(cle_etrangere)
            return None
        raise AttributeError(f"'{self.__class__.__name__}' n'a pas d'attribut '{name}'")

    def __setattr__(self, name, value):
        if hasattr(self, '_champs') and name in self._champs:
            champ = self._champs[name]
            if value is not None and not isinstance(value, champ.type_champ):
                raise TypeError(f"{name} doit être de type {champ.type_champ.__name__}")
            self._donnees[name] = value
        elif hasattr(self, '_relations') and name in self._relations:
            # Pour les relations, stocker l'ID de l'objet lié
            relation = self._relations[name]
            if hasattr(value, 'id'):
                setattr(self, relation.cle_etrangere, value.id)
            else:
                setattr(self, relation.cle_etrangere, value)
        else:
            super().__setattr__(name, value)

    def sauvegarder(self):
        """Sauvegarde l'instance."""
        self.valider()
        self.__class__._instances[self.id] = self
        print(f"{self.__class__.__name__}({self.id}) sauvegardé")

    def supprimer(self):
        """Supprime l'instance."""
        if self.id in self.__class__._instances:
            del self.__class__._instances[self.id]
            print(f"{self.__class__.__name__}({self.id}) supprimé")

    def valider(self):
        """Valide les champs obligatoires."""
        for nom_champ, champ in self._champs.items():
            if champ.obligatoire and self._donnees.get(nom_champ) is None:
                raise ValueError(f"Le champ '{nom_champ}' est obligatoire")

    def to_dict(self):
        """Convertit l'instance en dictionnaire."""
        result = {'id': self.id}
        result.update(self._donnees)
        return result

    def __str__(self):
        donnees = {k: v for k, v in self._donnees.items() if v is not None}
        donnees_str = ", ".join(f"{k}={v}" for k, v in donnees.items())
        return f"{self.__class__.__name__}({self.id}: {donnees_str})"

# Définition des modèles avec relations
class Utilisateur(ModeleAvance):
    nom = Champ(str, obligatoire=True)
    email = Champ(str, obligatoire=True)
    age = Champ(int, valeur_defaut=0)

class Categorie(ModeleAvance):
    nom = Champ(str, obligatoire=True)
    description = Champ(str, valeur_defaut="")

class Article(ModeleAvance):
    titre = Champ(str, obligatoire=True)
    contenu = Champ(str, obligatoire=True)

    # Relations
    auteur = RelationChamp(Utilisateur, 'auteur_id')
    categorie = RelationChamp(Categorie, 'categorie_id')

    # Champs pour les clés étrangères
    auteur_id = Champ(str)
    categorie_id = Champ(str)

# Test de l'ORM avancé avec relations
print("\n=== ORM avancé avec relations ===")

# Créer des utilisateurs
alice = Utilisateur.creer(nom="Alice", email="alice@example.com", age=25)
bob = Utilisateur.creer(nom="Bob", email="bob@example.com", age=30)

# Créer des catégories
tech = Categorie.creer(nom="Technologie", description="Articles sur la tech")
lifestyle = Categorie.creer(nom="Lifestyle", description="Articles de lifestyle")

# Créer des articles avec relations
article1 = Article.creer(
    titre="Introduction à Python",
    contenu="Python est un langage fantastique...",
    auteur=alice,  # Relation vers un utilisateur
    categorie=tech  # Relation vers une catégorie
)

article2 = Article.creer(
    titre="L'art de vivre",
    contenu="Comment bien vivre au quotidien...",
    auteur=bob,
    categorie=lifestyle
)

# Test des relations
print(f"Article 1 : {article1.titre}")
print(f"  Auteur : {article1.auteur.nom}")  # Accès via relation
print(f"  Catégorie : {article1.categorie.nom}")

print(f"\nArticle 2 : {article2.titre}")
print(f"  Auteur : {article2.auteur.nom}")
print(f"  Catégorie : {article2.categorie.nom}")

# Lister tous les objets
print(f"\nUtilisateurs : {len(Utilisateur.tous())}")
for user in Utilisateur.tous():
    print(f"  - {user}")

print(f"\nArticles : {len(Article.tous())}")
for article in Article.tous():
    print(f"  - {article}")
```

## Bonnes pratiques et conseils

### Quand NE PAS utiliser les métaclasses

```python
# ❌ Mauvais usage : trop complexe pour le besoin
class MetaInutile(type):
    def __new__(cls, name, bases, attrs):
        # Juste pour ajouter une méthode simple
        attrs['dire_bonjour'] = lambda self: "Bonjour"
        return super().__new__(cls, name, bases, attrs)

# ✅ Mieux : décorateur ou héritage simple
def ajouter_salutation(cls):
    cls.dire_bonjour = lambda self: "Bonjour"
    return cls

class ClasseSimple:
    def dire_bonjour(self):
        return "Bonjour"
```

### Règles d'or

1. **Simplicité d'abord** : commencez par des solutions simples
2. **Décorateurs vs métaclasses** : préférez les décorateurs quand possible
3. **Documentation** : documentez abondamment les métaclasses
4. **Tests** : testez rigoureusement le comportement
5. **Évitez la sur-ingénierie** : ne complexifiez que si nécessaire

## Résumé complet

Dans cette section avancée, vous avez appris :

✅ **Métaclasses** : contrôler la création des classes
✅ **Création dynamique** : générer des classes à la volée
✅ **Validation** : enforcer des contraintes au niveau classe
✅ **Patterns avancés** : Singleton, ORM, plugins
✅ **Classes abstraites** : définir des interfaces
✅ **Mixins** : partager des fonctionnalités
✅ **Décorateurs de classe** : alternative plus simple
✅ **Bonnes pratiques** : quand et comment utiliser ces outils

Ces concepts avancés vous permettent de créer des frameworks et des architectures sophistiquées, mais rappelez-vous : la simplicité est souvent la meilleure approche !

---

**Félicitations !** 🎉 Vous avez maintenant une compréhension complète de la programmation orientée objet en Python, des concepts de base aux techniques les plus avancées. Vous êtes prêt à créer des applications robustes et maintenables !
⏭️
