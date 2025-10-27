🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.5 Métaclasses et Programmation Avancée

## Introduction

Les **métaclasses** sont l'un des concepts les plus avancés de Python. Elles permettent de contrôler la création et le comportement des classes elles-mêmes.

**Important** : Les métaclasses sont un sujet avancé que vous n'utiliserez probablement jamais dans la plupart de vos projets. Comme le dit Tim Peters (développeur Python) : *"Les métaclasses sont une magie plus profonde que 99% des utilisateurs ne devraient jamais avoir à se soucier. Si vous vous demandez si vous en avez besoin, vous n'en avez pas besoin."*

Cependant, comprendre les métaclasses vous aidera à mieux comprendre comment Python fonctionne en profondeur.

## Tout est Objet en Python

### Principe Fondamental

En Python, **tout est objet**, y compris les classes elles-mêmes !

```python
# Les nombres sont des objets
nombre = 42
print(type(nombre))  # <class 'int'>

# Les chaînes sont des objets
texte = "Bonjour"
print(type(texte))   # <class 'str'>

# Les fonctions sont des objets
def ma_fonction():
    pass

print(type(ma_fonction))  # <class 'function'>

# Les classes sont AUSSI des objets !
class MaClasse:
    pass

print(type(MaClasse))  # <class 'type'>
```

**Observation clé** : Le type d'une classe est `type` !

## Qu'est-ce qu'une Métaclasse ?

### Analogie Simple

Imaginez une hiérarchie :
- Un **objet** est créé à partir d'une **classe**
- Une **classe** est créée à partir d'une **métaclasse**

```
Métaclasse (type)
    ↓ crée
Classe (MaClasse)
    ↓ crée
Instance/Objet (mon_objet)
```

**En d'autres termes** :
- Une classe est un **modèle** pour créer des objets
- Une métaclasse est un **modèle** pour créer des classes

### La Métaclasse par Défaut : `type`

Par défaut, toutes les classes en Python sont créées par la métaclasse `type`.

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom

# Ces deux façons de créer une classe sont équivalentes :

# 1. Syntaxe classique
class Personne:
    def __init__(self, nom):
        self.nom = nom

# 2. En utilisant type() directement
def init_personne(self, nom):
    self.nom = nom

Personne = type('Personne', (), {'__init__': init_personne})

# Les deux créent la même classe !
p1 = Personne("Alice")
print(p1.nom)  # Alice
```

### Syntaxe de `type()` pour Créer des Classes

```python
MaClasse = type(
    'NomDeLaClasse',      # Nom de la classe
    (ClassesParentes,),   # Tuple des classes parentes
    {'attributs': ...}    # Dictionnaire des attributs et méthodes
)
```

## Créer une Classe avec `type()`

### Exemple Simple

```python
# Créer une classe vide
MaClasse = type('MaClasse', (), {})

# Créer une instance
obj = MaClasse()
print(type(obj))  # <class '__main__.MaClasse'>
```

### Exemple avec Attributs

```python
# Créer une classe avec des attributs
def saluer(self):
    return f"Bonjour, je suis {self.nom}"

Personne = type('Personne', (), {
    'espece': 'Homo sapiens',  # Attribut de classe
    'saluer': saluer           # Méthode
})

# Utilisation
p = Personne()
p.nom = "Alice"
print(p.saluer())     # Bonjour, je suis Alice
print(p.espece)       # Homo sapiens
```

### Exemple avec Héritage

```python
# Classe parente
class Animal:
    def respirer(self):
        return "Je respire"

# Créer une classe qui hérite de Animal
def aboyer(self):
    return "Wouf !"

Chien = type('Chien', (Animal,), {
    'aboyer': aboyer
})

# Utilisation
rex = Chien()
print(rex.respirer())  # Je respire (hérité)
print(rex.aboyer())    # Wouf !
```

## Créer une Métaclasse Personnalisée

### Pourquoi Créer une Métaclasse ?

Les métaclasses permettent de :
- Valider ou modifier les classes au moment de leur création
- Ajouter automatiquement des attributs ou méthodes à toutes les classes
- Implémenter des patterns comme Singleton
- Créer des DSL (Domain Specific Languages)
- Logger la création de classes

### Syntaxe de Base

Pour créer une métaclasse, on hérite de `type` :

```python
class MaMetaclasse(type):
    def __new__(mcs, name, bases, attrs):
        # mcs : la métaclasse elle-même
        # name : nom de la classe à créer
        # bases : tuple des classes parentes
        # attrs : dictionnaire des attributs/méthodes

        print(f"Création de la classe {name}")

        # Créer et retourner la classe
        return super().__new__(mcs, name, bases, attrs)

# Utiliser la métaclasse
class MaClasse(metaclass=MaMetaclasse):
    pass

# Affiche : Création de la classe MaClasse
```

### Exemple : Métaclasse qui Ajoute un Timestamp

```python
from datetime import datetime

class TimestampMeta(type):
    """Métaclasse qui ajoute un timestamp à chaque classe"""

    def __new__(mcs, name, bases, attrs):
        # Ajouter un attribut timestamp
        attrs['creation_time'] = datetime.now()
        return super().__new__(mcs, name, bases, attrs)

class Produit(metaclass=TimestampMeta):
    def __init__(self, nom):
        self.nom = nom

class Service(metaclass=TimestampMeta):
    def __init__(self, nom):
        self.nom = nom

# Chaque classe a maintenant un timestamp
print(f"Produit créé le : {Produit.creation_time}")
print(f"Service créé le : {Service.creation_time}")
```

### Exemple : Métaclasse de Validation

```python
class ValidationMeta(type):
    """Vérifie que certaines méthodes sont implémentées"""

    def __new__(mcs, name, bases, attrs):
        # Ignorer la classe de base
        if name != 'Animal':
            # Vérifier que la méthode 'faire_bruit' existe
            if 'faire_bruit' not in attrs:
                raise TypeError(f"La classe {name} doit implémenter 'faire_bruit'")

        return super().__new__(mcs, name, bases, attrs)

class Animal(metaclass=ValidationMeta):
    pass

class Chien(Animal):
    def faire_bruit(self):
        return "Wouf !"

# Ceci fonctionne
rex = Chien()
print(rex.faire_bruit())

# Ceci échouerait :
# class Chat(Animal):
#     pass
# TypeError: La classe Chat doit implémenter 'faire_bruit'
```

## `__init__` vs `__new__` dans les Métaclasses

### `__new__` : Créer la Classe

`__new__` est appelé pour **créer** la classe. C'est là que vous pouvez modifier les attributs avant que la classe ne soit créée.

```python
class ModificationMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"__new__ : Création de {name}")

        # Modifier les attributs avant la création
        attrs['modifie'] = True

        return super().__new__(mcs, name, bases, attrs)

class MaClasse(metaclass=ModificationMeta):
    pass

print(MaClasse.modifie)  # True
```

### `__init__` : Initialiser la Classe

`__init__` est appelé pour **initialiser** la classe après sa création.

```python
class InitMeta(type):
    def __init__(cls, name, bases, attrs):
        print(f"__init__ : Initialisation de {name}")
        super().__init__(name, bases, attrs)

        # Faire quelque chose après la création
        cls.compteur = 0

class MaClasse(metaclass=InitMeta):
    pass

print(MaClasse.compteur)  # 0
```

### Utiliser les Deux Ensemble

```python
class CompleteMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"1. __new__ : Création de {name}")
        attrs['cree_par'] = 'CompleteMeta'
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print(f"2. __init__ : Initialisation de {name}")
        super().__init__(name, bases, attrs)
        cls.initialise = True

class MaClasse(metaclass=CompleteMeta):
    pass

# Affiche :
# 1. __new__ : Création de MaClasse
# 2. __init__ : Initialisation de MaClasse

print(MaClasse.cree_par)    # CompleteMeta
print(MaClasse.initialise)  # True
```

## Exemples Pratiques de Métaclasses

### 1. Singleton Pattern

Un Singleton est une classe dont on ne peut créer qu'une seule instance.

```python
class SingletonMeta(type):
    """Métaclasse qui implémente le pattern Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Créer la première instance
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.parametre1 = "valeur1"
        self.parametre2 = "valeur2"

# Créer deux "instances"
config1 = Configuration()
config2 = Configuration()

# Ce sont en fait la même instance !
print(config1 is config2)  # True

config1.parametre1 = "nouvelle_valeur"
print(config2.parametre1)  # nouvelle_valeur
```

### 2. Enregistrement Automatique des Classes

```python
class RegistryMeta(type):
    """Métaclasse qui enregistre toutes les classes créées"""
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)

        # Enregistrer la classe (sauf la classe de base)
        if name != 'Plugin':
            mcs.registry[name] = cls

        return cls

class Plugin(metaclass=RegistryMeta):
    pass

class PDFPlugin(Plugin):
    pass

class ExcelPlugin(Plugin):
    pass

class ImagePlugin(Plugin):
    pass

# Voir toutes les classes enregistrées
print("Plugins disponibles :")
for nom, classe in RegistryMeta.registry.items():
    print(f"  - {nom}")
```

**Résultat :**
```
Plugins disponibles :
  - PDFPlugin
  - ExcelPlugin
  - ImagePlugin
```

### 3. Conversion Automatique des Noms d'Attributs

```python
class UpperAttrMeta(type):
    """Métaclasse qui convertit tous les noms d'attributs en majuscules"""

    def __new__(mcs, name, bases, attrs):
        # Créer un nouveau dictionnaire avec les noms en majuscules
        uppercase_attrs = {}

        for attr_name, attr_value in attrs.items():
            # Ne pas modifier les méthodes spéciales (__init__, etc.)
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value

        return super().__new__(mcs, name, bases, uppercase_attrs)

class MaClasse(metaclass=UpperAttrMeta):
    attribut = "valeur"
    autre_attribut = 42

    def methode(self):
        return "Bonjour"

# Les attributs sont maintenant en majuscules
print(MaClasse.ATTRIBUT)        # valeur
print(MaClasse.AUTRE_ATTRIBUT)  # 42
obj = MaClasse()
print(obj.METHODE())            # Bonjour
```

### 4. Métaclasse pour un ORM Simple

```python
class Field:
    """Représente un champ de base de données"""
    def __init__(self, field_type):
        self.field_type = field_type

class ModelMeta(type):
    """Métaclasse pour créer des modèles ORM"""

    def __new__(mcs, name, bases, attrs):
        # Extraire les champs
        fields = {}

        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
                # Retirer le Field des attributs de classe
                attrs.pop(attr_name)

        # Stocker les champs dans la classe
        attrs['_fields'] = fields

        return super().__new__(mcs, name, bases, attrs)

class Model(metaclass=ModelMeta):
    """Classe de base pour les modèles"""

    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))

    def __repr__(self):
        field_values = ', '.join(
            f"{name}={getattr(self, name, None)}"
            for name in self._fields
        )
        return f"{self.__class__.__name__}({field_values})"

# Utiliser le "mini-ORM"
class Utilisateur(Model):
    nom = Field('varchar')
    age = Field('int')
    email = Field('varchar')

class Produit(Model):
    nom = Field('varchar')
    prix = Field('decimal')

# Créer des instances
user = Utilisateur(nom="Alice", age=30, email="alice@example.com")
print(user)  # Utilisateur(nom=Alice, age=30, email=alice@example.com)

produit = Produit(nom="Livre", prix=15.99)
print(produit)  # Produit(nom=Livre, prix=15.99)

# Voir les champs définis
print(f"Champs de Utilisateur : {list(Utilisateur._fields.keys())}")
print(f"Champs de Produit : {list(Produit._fields.keys())}")
```

## `__call__` dans les Métaclasses

La méthode `__call__` dans une métaclasse est appelée quand on crée une **instance** de la classe (pas quand on crée la classe elle-même).

```python
class CallMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Création d'une instance de {cls.__name__}")
        print(f"Arguments : {args}, {kwargs}")

        # Créer l'instance normalement
        instance = super().__call__(*args, **kwargs)

        print(f"Instance créée : {instance}")
        return instance

class Personne(metaclass=CallMeta):
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return f"Personne({self.nom}, {self.age})"

# Créer une instance
p = Personne("Alice", 30)
```

**Résultat :**
```
Création d'une instance de Personne
Arguments : ('Alice', 30), {}
Instance créée : Personne(Alice, 30)
```

## Attributs de Classe Calculés

### `__getattribute__` dans une Métaclasse

```python
class DynamicMeta(type):
    """Métaclasse qui calcule dynamiquement certains attributs"""

    def __getattribute__(cls, name):
        # Si on accède à 'dynamic_value'
        if name == 'dynamic_value':
            from datetime import datetime
            return f"Valeur générée à {datetime.now()}"

        return super().__getattribute__(name)

class MaClasse(metaclass=DynamicMeta):
    static_value = "valeur statique"

# Chaque accès génère une nouvelle valeur
print(MaClasse.dynamic_value)  # Valeur générée à 2025-10-27 ...
import time
time.sleep(1)
print(MaClasse.dynamic_value)  # Valeur générée à 2025-10-27 ... (temps différent)

print(MaClasse.static_value)   # valeur statique
```

## Descripteurs : Un Concept Avancé

Les **descripteurs** sont des objets qui définissent comment les attributs sont accédés. C'est ce qui se cache derrière `@property`.

### Créer un Descripteur

Un descripteur doit implémenter au moins une de ces méthodes :
- `__get__(self, obj, type=None)` : appelé lors de la lecture
- `__set__(self, obj, value)` : appelé lors de l'écriture
- `__delete__(self, obj)` : appelé lors de la suppression

```python
class IntegerField:
    """Descripteur qui ne stocke que des entiers"""

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} doit être un entier")
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Personne:
    age = IntegerField('age')

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age  # Utilise le descripteur

p = Personne("Alice", 30)
print(p.age)     # 30

p.age = 31       # OK
print(p.age)     # 31

# p.age = "32"   # TypeError !
```

### Descripteur de Validation

```python
class ValidatedString:
    """Descripteur qui valide les chaînes de caractères"""

    def __init__(self, minsize=0, maxsize=None):
        self.minsize = minsize
        self.maxsize = maxsize

    def __set_name__(self, owner, name):
        # Appelé automatiquement, stocke le nom de l'attribut
        self.name = name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, '')

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} doit être une chaîne")

        if len(value) < self.minsize:
            raise ValueError(
                f"{self.name} doit avoir au moins {self.minsize} caractères"
            )

        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"{self.name} ne peut pas dépasser {self.maxsize} caractères"
            )

        obj.__dict__[self.name] = value

class Utilisateur:
    nom = ValidatedString(minsize=2, maxsize=50)
    email = ValidatedString(minsize=5)

    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

# Utilisation
user = Utilisateur("Alice", "alice@example.com")
print(f"{user.nom} - {user.email}")

# user2 = Utilisateur("A", "test")  # ValueError (nom trop court)
```

## Classes Abstraites et ABC

Le module `abc` (Abstract Base Classes) permet de créer des classes abstraites qui définissent une interface que les classes dérivées doivent respecter.

### Créer une Classe Abstraite

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    """Classe abstraite pour les formes géométriques"""

    @abstractmethod
    def calculer_surface(self):
        """Méthode abstraite : doit être implémentée par les classes filles"""
        pass

    @abstractmethod
    def calculer_perimetre(self):
        """Méthode abstraite"""
        pass

    def afficher(self):
        """Méthode concrète : peut être utilisée telle quelle"""
        print(f"Forme : {self.__class__.__name__}")
        print(f"Surface : {self.calculer_surface()}")
        print(f"Périmètre : {self.calculer_perimetre()}")

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14159 * self.rayon ** 2

    def calculer_perimetre(self):
        return 2 * 3.14159 * self.rayon

# Utilisation
rect = Rectangle(5, 3)
rect.afficher()

print()

cercle = Cercle(4)
cercle.afficher()

# Ceci échouerait :
# forme = Forme()  # TypeError: Can't instantiate abstract class
```

### Vérifier l'Implémentation

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def faire_bruit(self):
        pass

    @abstractmethod
    def se_deplacer(self):
        pass

# Ceci échoue car toutes les méthodes abstraites ne sont pas implémentées
# class Chien(Animal):
#     def faire_bruit(self):
#         return "Wouf"
#     # Manque se_deplacer()
# TypeError: Can't instantiate abstract class Chien

# Ceci fonctionne
class Chien(Animal):
    def faire_bruit(self):
        return "Wouf"

    def se_deplacer(self):
        return "Je cours"

rex = Chien()
print(rex.faire_bruit())      # Wouf
print(rex.se_deplacer())      # Je cours
```

### Propriétés Abstraites

```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
    @property
    @abstractmethod
    def vitesse_max(self):
        """Propriété abstraite"""
        pass

class Voiture(Vehicule):
    def __init__(self):
        self._vitesse_max = 200

    @property
    def vitesse_max(self):
        return self._vitesse_max

voiture = Voiture()
print(f"Vitesse max : {voiture.vitesse_max} km/h")
```

## `__init_subclass__` : Alternative aux Métaclasses

Depuis Python 3.6, `__init_subclass__` offre une alternative plus simple aux métaclasses pour personnaliser la création de sous-classes.

```python
class Plugin:
    """Classe de base pour les plugins"""
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Enregistrer automatiquement chaque sous-classe
        cls.plugins.append(cls)
        print(f"Plugin enregistré : {cls.__name__}")

class PDFPlugin(Plugin):
    pass

class ExcelPlugin(Plugin):
    pass

class ImagePlugin(Plugin):
    pass

print(f"\nNombre de plugins : {len(Plugin.plugins)}")
for plugin in Plugin.plugins:
    print(f"  - {plugin.__name__}")
```

**Résultat :**
```
Plugin enregistré : PDFPlugin
Plugin enregistré : ExcelPlugin
Plugin enregistré : ImagePlugin

Nombre de plugins : 3
  - PDFPlugin
  - ExcelPlugin
  - ImagePlugin
```

### Validation avec `__init_subclass__`

```python
class RequiredMethods:
    """Classe qui impose des méthodes obligatoires"""
    required_methods = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Vérifier que toutes les méthodes requises sont présentes
        for method in cls.required_methods:
            if not hasattr(cls, method):
                raise TypeError(
                    f"La classe {cls.__name__} doit implémenter la méthode '{method}'"
                )

class DataProcessor(RequiredMethods):
    required_methods = ['process', 'validate']

class CSVProcessor(DataProcessor):
    def process(self, data):
        return f"Processing CSV: {data}"

    def validate(self, data):
        return True

# Ceci fonctionne
processor = CSVProcessor()
print(processor.process("data.csv"))

# Ceci échouerait :
# class BadProcessor(DataProcessor):
#     def process(self, data):
#         return data
#     # Manque validate()
# TypeError: La classe BadProcessor doit implémenter la méthode 'validate'
```

## Slots : Optimisation de la Mémoire

`__slots__` permet de définir explicitement les attributs d'une classe, ce qui économise de la mémoire et accélère l'accès aux attributs.

### Sans Slots

```python
class PersonneNormale:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = PersonneNormale("Alice", 30)
# On peut ajouter n'importe quel attribut
p.ville = "Paris"  # OK, stocké dans __dict__
print(p.__dict__)  # {'nom': 'Alice', 'age': 30, 'ville': 'Paris'}
```

### Avec Slots

```python
class PersonneAvecSlots:
    __slots__ = ['nom', 'age']  # Seuls ces attributs sont autorisés

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = PersonneAvecSlots("Bob", 25)
print(p.nom, p.age)  # Bob 25

# On ne peut PAS ajouter d'autres attributs
# p.ville = "Lyon"  # AttributeError !

# Pas de __dict__
# print(p.__dict__)  # AttributeError !
```

### Avantages des Slots

```python
import sys

class SansSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class AvecSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Comparer la taille en mémoire
obj1 = SansSlots(1, 2)
obj2 = AvecSlots(1, 2)

print(f"Taille sans slots : {sys.getsizeof(obj1) + sys.getsizeof(obj1.__dict__)} bytes")
print(f"Taille avec slots : {sys.getsizeof(obj2)} bytes")
```

**Avantages** :
- Économie de mémoire (important avec beaucoup d'instances)
- Accès plus rapide aux attributs
- Protection contre les erreurs (typos dans les noms d'attributs)

**Inconvénients** :
- Moins flexible (pas de __dict__)
- Ne peut pas ajouter d'attributs dynamiquement

## Protocoles et Duck Typing

### Duck Typing

En Python, on utilise le **duck typing** : "Si ça marche comme un canard et ça cancane comme un canard, alors c'est un canard."

```python
class Fichier:
    def __init__(self, nom):
        self.nom = nom
        self.contenu = []

    def write(self, texte):
        self.contenu.append(texte)

    def read(self):
        return ''.join(self.contenu)

class Logger:
    def __init__(self, sortie):
        self.sortie = sortie  # Peut être un fichier, ou notre Fichier

    def log(self, message):
        self.sortie.write(f"[LOG] {message}\n")

# Fonctionne avec un vrai fichier
# logger1 = Logger(open('log.txt', 'w'))

# Fonctionne aussi avec notre classe Fichier !
fake_file = Fichier("memory.txt")
logger2 = Logger(fake_file)
logger2.log("Message 1")
logger2.log("Message 2")

print(fake_file.read())
```

### Protocoles avec `typing.Protocol`

```python
from typing import Protocol

class Drawable(Protocol):
    """Protocole : définit une interface sans héritage"""
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "○"

class Square:
    def draw(self) -> str:
        return "□"

def render(shape: Drawable) -> None:
    """Accepte n'importe quel objet qui a une méthode draw()"""
    print(shape.draw())

# Fonctionne sans que Circle ou Square héritent de Drawable
render(Circle())  # ○
render(Square())  # □
```

## Bonnes Pratiques

### 1. Éviter les Métaclasses Quand Possible

```python
# ✗ Trop complexe : utiliser une métaclasse pour ça
class SimpleMeta(type):
    def __new__(mcs, name, bases, attrs):
        attrs['added'] = True
        return super().__new__(mcs, name, bases, attrs)

# ✓ Plus simple : utiliser __init_subclass__
class SimpleBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.added = True
```

### 2. Utiliser ABC pour les Interfaces

```python
# ✓ Bon : définir clairement une interface
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self, id):
        pass
```

### 3. Utiliser les Slots pour les Classes avec Beaucoup d'Instances

```python
# ✓ Bon pour économiser la mémoire
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Utile si vous créez des milliers de points
points = [Point(i, i*2) for i in range(10000)]
```

### 4. Documenter les Métaclasses

```python
class MyMeta(type):
    """
    Métaclasse qui ajoute automatiquement un ID unique à chaque classe.

    Usage:
        class MyClass(metaclass=MyMeta):
            pass

    La classe aura automatiquement un attribut 'class_id'.
    """
    _counter = 0

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        MyMeta._counter += 1
        cls.class_id = MyMeta._counter
        return cls
```

## Quand Utiliser ces Concepts Avancés ?

| Concept | Quand l'utiliser |
|---------|------------------|
| **Métaclasses** | Rarement. Pour des frameworks, DSL, ou quand `__init_subclass__` ne suffit pas |
| **`__init_subclass__`** | Pour personnaliser les sous-classes (enregistrement, validation) |
| **Descripteurs** | Pour des attributs avec logique complexe (validation, calcul) |
| **ABC** | Pour définir des interfaces claires que les sous-classes doivent respecter |
| **Slots** | Quand vous créez beaucoup d'instances et que la mémoire est importante |
| **Protocoles** | Pour le duck typing avec type hints |

## Résumé

### Métaclasses
- Contrôlent la création des classes
- Héritent de `type`
- Utilisent `__new__` et `__init__`
- Rarement nécessaires dans le code quotidien

### `__init_subclass__`
- Alternative plus simple aux métaclasses
- Personnalise les sous-classes
- Ajouté dans Python 3.6

### Descripteurs
- Contrôlent l'accès aux attributs
- Implémentent `__get__`, `__set__`, `__delete__`
- Base de `@property`

### Classes Abstraites (ABC)
- Définissent des interfaces
- Utilisent `@abstractmethod`
- Forcent l'implémentation dans les sous-classes

### Slots
- Optimisent la mémoire
- Limitent les attributs
- Accélèrent l'accès

## Conclusion

Les concepts avancés de Python comme les métaclasses, les descripteurs et les classes abstraites sont des outils puissants qui permettent de :
- **Contrôler** finement le comportement des classes
- **Créer** des frameworks et DSL
- **Optimiser** les performances et la mémoire
- **Définir** des interfaces claires
- **Valider** le code à la création des classes

**Points clés à retenir** :
- Les métaclasses sont des "classes de classes"
- `type` est la métaclasse par défaut
- Préférez `__init_subclass__` aux métaclasses quand possible
- Les classes abstraites (ABC) définissent des contrats
- Les descripteurs contrôlent l'accès aux attributs
- Les slots économisent de la mémoire
- Utilisez ces outils avec parcimonie

**Citation finale** : *"Si vous vous demandez si vous avez besoin d'une métaclasse, vous n'en avez probablement pas besoin."* Mais comprendre ces concepts vous permet de mieux comprendre Python et de reconnaître ces patterns quand vous les rencontrez dans du code de bibliothèques tierces.

Vous avez maintenant terminé le chapitre sur la Programmation Orientée Objet en Python ! Vous maîtrisez les fondamentaux (classes, objets, héritage) ainsi que les concepts avancés qui font la puissance de Python.

⏭️ [Gestion des données et fichiers](/04-gestion-donnees-et-fichiers/README.md)
