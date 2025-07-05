🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.3 : Décorateurs avancés

## Introduction

Les décorateurs sont l'une des fonctionnalités les plus puissantes de Python. Ils permettent de modifier ou d'étendre le comportement d'une fonction sans changer son code source. Dans cette section, nous allons explorer les décorateurs en profondeur, depuis les concepts de base jusqu'aux techniques avancées.

## Rappel : Qu'est-ce qu'un décorateur ?

Un décorateur est une fonction qui prend une autre fonction comme paramètre et retourne une fonction modifiée. C'est une application pratique des fonctions d'ordre supérieur que nous avons vues précédemment.

### Syntaxe de base

```python
@decorateur
def ma_fonction():
    pass

# Équivalent à :
# ma_fonction = decorateur(ma_fonction)
```

## Décorateurs simples : Révision

### Exemple de base

```python
def mon_decorateur(func):
    def wrapper():
        print("Quelque chose avant la fonction")
        resultat = func()
        print("Quelque chose après la fonction")
        return resultat
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

# Utilisation
dire_bonjour()
# Sortie :
# Quelque chose avant la fonction
# Bonjour !
# Quelque chose après la fonction
```

### Problème avec les arguments

```python
def mon_decorateur(func):
    def wrapper():  # Pas d'arguments !
        print("Avant")
        resultat = func()
        print("Après")
        return resultat
    return wrapper

@mon_decorateur
def saluer(nom):  # Cette fonction prend un argument
    print(f"Bonjour {nom} !")

# saluer("Alice")  # ❌ Erreur ! wrapper() ne prend pas d'arguments
```

## Décorateurs avec *args et **kwargs

Pour créer des décorateurs qui fonctionnent avec n'importe quelle fonction, nous utilisons `*args` et `**kwargs`.

### Solution universelle

```python
def decorateur_universel(func):
    def wrapper(*args, **kwargs):
        print("Avant l'exécution")
        resultat = func(*args, **kwargs)
        print("Après l'exécution")
        return resultat
    return wrapper

@decorateur_universel
def additionner(a, b):
    return a + b

@decorateur_universel
def saluer(nom, titre="M."):
    print(f"Bonjour {titre} {nom} !")

# Tests
print(additionner(3, 5))
saluer("Dupont", titre="Dr.")
```

### Décorateur de mesure de temps

```python
import time
from functools import wraps

def mesurer_temps(func):
    @wraps(func)  # Préserve les métadonnées de la fonction originale
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} a pris {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@mesurer_temps
def calcul_lent():
    time.sleep(1)
    return "Calcul terminé"

@mesurer_temps
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Tests
print(calcul_lent())
print(fibonacci(10))
```

## Décorateurs avec paramètres

Les décorateurs avec paramètres sont des fonctions qui retournent un décorateur. C'est un niveau d'abstraction supplémentaire.

### Structure générale

```python
def decorateur_avec_params(param1, param2):
    def decorateur_reel(func):
        def wrapper(*args, **kwargs):
            # Utiliser param1 et param2 ici
            return func(*args, **kwargs)
        return wrapper
    return decorateur_reel

# Utilisation
@decorateur_avec_params("valeur1", "valeur2")
def ma_fonction():
    pass
```

### Exemple : Décorateur de répétition

```python
def repeter(nb_fois):
    def decorateur(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(nb_fois):
                resultat = func(*args, **kwargs)
            return resultat  # Retourne le résultat de la dernière exécution
        return wrapper
    return decorateur

@repeter(3)
def dire_hello():
    print("Hello!")

@repeter(5)
def compter(n):
    print(f"Comptage : {n}")
    return n

# Tests
dire_hello()
# Sortie :
# Hello!
# Hello!
# Hello!

print(compter(42))
# Sortie :
# Comptage : 42
# Comptage : 42
# Comptage : 42
# Comptage : 42
# Comptage : 42
# 42
```

### Exemple : Décorateur de cache avec TTL

```python
import time
from functools import wraps

def cache_avec_ttl(ttl_secondes):
    def decorateur(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Créer une clé unique pour les arguments
            cle = str(args) + str(sorted(kwargs.items()))
            maintenant = time.time()

            # Vérifier si le résultat est en cache et encore valide
            if cle in cache:
                resultat, timestamp = cache[cle]
                if maintenant - timestamp < ttl_secondes:
                    print(f"Cache hit pour {func.__name__}")
                    return resultat

            # Calculer et mettre en cache
            print(f"Calcul en cours pour {func.__name__}")
            resultat = func(*args, **kwargs)
            cache[cle] = (resultat, maintenant)
            return resultat

        return wrapper
    return decorateur

@cache_avec_ttl(5)  # Cache valide pendant 5 secondes
def calcul_complexe(n):
    time.sleep(2)  # Simulation d'un calcul long
    return n * n

# Tests
print(calcul_complexe(4))  # Calcul en cours
print(calcul_complexe(4))  # Cache hit
time.sleep(6)
print(calcul_complexe(4))  # Cache expiré, nouveau calcul
```

## Décorateurs de classe

Les décorateurs peuvent aussi être appliqués aux classes pour modifier leur comportement.

### Décorateur simple pour classe

```python
def ajouter_methode_string(cls):
    def to_string(self):
        attributs = []
        for cle, valeur in self.__dict__.items():
            attributs.append(f"{cle}={valeur}")
        return f"{cls.__name__}({', '.join(attributs)})"

    cls.to_string = to_string
    return cls

@ajouter_methode_string
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

# Test
p = Personne("Alice", 25)
print(p.to_string())  # Personne(nom=Alice, age=25)
```

### Décorateur singleton

```python
def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Création de la connexion à la base de données")
        self.connection_id = id(self)

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1.connection_id == db2.connection_id)  # True
```

## Décorateurs comme classes

Vous pouvez également créer des décorateurs en utilisant des classes au lieu de fonctions.

### Décorateur classe de base

```python
class CompteurAppels:
    def __init__(self, func):
        self.func = func
        self.nb_appels = 0
        # Préserver les métadonnées
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args, **kwargs):
        self.nb_appels += 1
        print(f"{self.func.__name__} appelée {self.nb_appels} fois")
        return self.func(*args, **kwargs)

@CompteurAppels
def ma_fonction():
    print("Exécution de ma fonction")

# Test
ma_fonction()  # ma_fonction appelée 1 fois
ma_fonction()  # ma_fonction appelée 2 fois
```

### Décorateur classe avec paramètres

```python
class LimiteurAppels:
    def __init__(self, max_appels):
        self.max_appels = max_appels

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, 'nb_appels'):
                wrapper.nb_appels = 0

            if wrapper.nb_appels >= self.max_appels:
                raise Exception(f"Limite de {self.max_appels} appels dépassée")

            wrapper.nb_appels += 1
            return func(*args, **kwargs)

        return wrapper

@LimiteurAppels(3)
def fonction_limitee():
    print("Fonction exécutée")

# Test
fonction_limitee()  # OK
fonction_limitee()  # OK
fonction_limitee()  # OK
# fonction_limitee()  # ❌ Exception !
```

## Décorateurs intégrés utiles

### @property

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    @property
    def aire(self):
        """Calculée dynamiquement"""
        return self._largeur * self._hauteur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur <= 0:
            raise ValueError("La largeur doit être positive")
        self._largeur = valeur

# Test
rect = Rectangle(5, 3)
print(rect.aire)  # 15
rect.largeur = 10
print(rect.aire)  # 30
```

### @staticmethod et @classmethod

```python
class MathUtils:
    pi = 3.14159

    @staticmethod
    def additionner(a, b):
        """Méthode statique - pas d'accès à self ou cls"""
        return a + b

    @classmethod
    def aire_cercle(cls, rayon):
        """Méthode de classe - accès à cls"""
        return cls.pi * rayon * rayon

    def aire_rectangle(self, largeur, hauteur):
        """Méthode d'instance normale"""
        return largeur * hauteur

# Tests
print(MathUtils.additionner(5, 3))  # 8
print(MathUtils.aire_cercle(5))     # 78.53975
```

## Décorateurs multiples

Vous pouvez appliquer plusieurs décorateurs à une même fonction.

```python
def gras(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italique(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

def souligner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"_{result}_"
    return wrapper

@gras
@italique
@souligner
def dire_hello():
    return "Hello World"

print(dire_hello())  # **_*Hello World*_**

# L'ordre d'application est de bas en haut :
# 1. souligner(dire_hello)
# 2. italique(résultat de 1)
# 3. gras(résultat de 2)
```

## Cas d'usage avancés

### Décorateur de validation d'arguments

```python
def valider_types(**types_attendus):
    def decorateur(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Récupérer les noms des paramètres
            import inspect
            sig = inspect.signature(func)
            noms_params = list(sig.parameters.keys())

            # Valider les arguments positionnels
            for i, arg in enumerate(args):
                if i < len(noms_params):
                    nom_param = noms_params[i]
                    if nom_param in types_attendus:
                        type_attendu = types_attendus[nom_param]
                        if not isinstance(arg, type_attendu):
                            raise TypeError(f"{nom_param} doit être de type {type_attendu.__name__}")

            # Valider les arguments nommés
            for nom, valeur in kwargs.items():
                if nom in types_attendus:
                    type_attendu = types_attendus[nom]
                    if not isinstance(valeur, type_attendu):
                        raise TypeError(f"{nom} doit être de type {type_attendu.__name__}")

            return func(*args, **kwargs)
        return wrapper
    return decorateur

@valider_types(nom=str, age=int, salaire=float)
def creer_employe(nom, age, salaire):
    return f"Employé: {nom}, {age} ans, {salaire}€"

# Tests
print(creer_employe("Alice", 25, 3000.0))  # OK
# creer_employe("Alice", "25", 3000.0)     # ❌ TypeError
```

### Décorateur de retry avec backoff

```python
import random
import time
from functools import wraps

def retry_avec_backoff(max_tentatives=3, delai_base=1, backoff_factor=2):
    def decorateur(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tentative in range(max_tentatives):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentative == max_tentatives - 1:
                        print(f"Échec après {max_tentatives} tentatives")
                        raise e

                    delai = delai_base * (backoff_factor ** tentative)
                    print(f"Tentative {tentative + 1} échouée: {e}")
                    print(f"Nouvelle tentative dans {delai} secondes...")
                    time.sleep(delai)

        return wrapper
    return decorateur

@retry_avec_backoff(max_tentatives=3, delai_base=0.5)
def operation_instable():
    """Simule une opération qui échoue parfois"""
    if random.random() < 0.7:  # 70% de chance d'échouer
        raise ConnectionError("Connexion échouée")
    return "Opération réussie !"

# Test
try:
    resultat = operation_instable()
    print(resultat)
except Exception as e:
    print(f"Échec final: {e}")
```

## Exercices pratiques

### Exercice 1 : Décorateur de logging

Créez un décorateur qui enregistre les appels de fonction avec leurs arguments et résultats.

```python
import datetime
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Appel de {func.__name__}")
        print(f"  Arguments: args={args}, kwargs={kwargs}")

        try:
            resultat = func(*args, **kwargs)
            print(f"  Résultat: {resultat}")
            return resultat
        except Exception as e:
            print(f"  Exception: {e}")
            raise

    return wrapper

@logger
def diviser(a, b):
    return a / b

# Test
print(diviser(10, 2))
print(diviser(10, 0))  # Lèvera une exception
```

### Exercice 2 : Décorateur de rate limiting

Créez un décorateur qui limite le nombre d'appels par seconde.

```python
import time
from functools import wraps

def rate_limit(appels_par_seconde):
    def decorateur(func):
        derniers_appels = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            maintenant = time.time()

            # Nettoyer les anciens appels (plus vieux qu'une seconde)
            derniers_appels[:] = [t for t in derniers_appels if maintenant - t < 1.0]

            # Vérifier la limite
            if len(derniers_appels) >= appels_par_seconde:
                raise Exception(f"Rate limit dépassé: max {appels_par_seconde} appels/seconde")

            # Enregistrer cet appel
            derniers_appels.append(maintenant)

            return func(*args, **kwargs)

        return wrapper
    return decorateur

@rate_limit(2)  # Maximum 2 appels par seconde
def api_call():
    return "Appel API réussi"

# Test
print(api_call())  # OK
print(api_call())  # OK
# print(api_call())  # ❌ Rate limit dépassé
```

### Exercice 3 : Décorateur de memoization avancé

Créez un décorateur de memoization avec une taille limite de cache.

```python
from functools import wraps
from collections import OrderedDict

def memoize_lru(max_size=128):
    def decorateur(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Créer une clé unique
            cle = str(args) + str(sorted(kwargs.items()))

            # Si déjà en cache, déplacer en fin (LRU)
            if cle in cache:
                cache.move_to_end(cle)
                return cache[cle]

            # Calculer le résultat
            resultat = func(*args, **kwargs)

            # Ajouter au cache
            cache[cle] = resultat
            cache.move_to_end(cle)

            # Respecter la taille limite
            if len(cache) > max_size:
                cache.popitem(last=False)  # Supprimer le plus ancien

            return resultat

        # Ajouter des méthodes utiles
        wrapper.cache_info = lambda: f"Cache size: {len(cache)}/{max_size}"
        wrapper.cache_clear = lambda: cache.clear()

        return wrapper
    return decorateur

@memoize_lru(max_size=3)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test
print(fibonacci(10))
print(fibonacci.cache_info())
```

## Bonnes pratiques

### ✅ À faire

1. **Utilisez `@wraps`** pour préserver les métadonnées de la fonction originale
2. **Gérez les exceptions** correctement dans vos décorateurs
3. **Documentez vos décorateurs** clairement
4. **Gardez-les simples** : un décorateur = une responsabilité
5. **Utilisez des noms explicites** pour vos décorateurs

### ❌ À éviter

1. **Décorateurs trop complexes** : Si c'est compliqué, utilisez une classe
2. **Modifications silencieuses** : Le comportement modifié doit être évident
3. **Effets de bord cachés** : Évitez les modifications globales
4. **Performances non considérées** : Attention à l'overhead des décorateurs

## Cas d'usage recommandés

Les décorateurs sont parfaits pour :

- **Logging et monitoring** : Enregistrer les appels de fonction
- **Authentification** : Vérifier les permissions
- **Cache** : Mémoriser les résultats de calculs coûteux
- **Validation** : Vérifier les arguments
- **Mesure de performance** : Chronométrer l'exécution
- **Retry logic** : Répéter les opérations échouées
- **Rate limiting** : Limiter la fréquence d'exécution

## Résumé

Les décorateurs avancés permettent de :

- Créer des fonctions qui modifient d'autres fonctions
- Ajouter des fonctionnalités sans modifier le code source
- Utiliser des paramètres pour personnaliser le comportement
- Appliquer plusieurs décorateurs à une même fonction
- Créer des patterns réutilisables et élégants

Les décorateurs sont un outil puissant qui, une fois maîtrisé, vous permettra d'écrire du code plus propre, plus modulaire et plus maintenable.

Dans la prochaine section, nous découvrirons les générateurs et expressions génératrices, qui nous permettront de créer des itérateurs efficaces en mémoire.

⏭️
