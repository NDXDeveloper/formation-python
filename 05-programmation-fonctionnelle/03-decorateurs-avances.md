🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.3 Décorateurs avancés

## Introduction

Les **décorateurs** sont l'une des fonctionnalités les plus puissantes et élégantes de Python. Ils permettent de modifier ou d'étendre le comportement de fonctions ou de classes sans modifier leur code source.

Dans ce chapitre, nous allons explorer les décorateurs en profondeur, des concepts de base aux techniques avancées. Ne vous inquiétez pas si cela semble complexe au début, nous allons progresser étape par étape !

---

## Rappel : Qu'est-ce qu'un décorateur ?

Un **décorateur** est une fonction qui prend une autre fonction en paramètre, lui ajoute des fonctionnalités, et retourne la fonction modifiée.

### Exemple simple sans décorateur

```python
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()  # Affiche : Bonjour !
```

Maintenant, imaginons que nous voulons afficher un message avant et après l'exécution de la fonction, sans modifier son code.

### Avec un décorateur basique

```python
def mon_decorateur(fonction):
    """Décorateur qui ajoute des messages avant et après."""
    def fonction_modifiee():
        print("--- Début ---")
        fonction()
        print("--- Fin ---")
    return fonction_modifiee

def dire_bonjour():
    print("Bonjour !")

# Application du décorateur
dire_bonjour = mon_decorateur(dire_bonjour)  
dire_bonjour()  

# Affiche :
# --- Début ---
# Bonjour !
# --- Fin ---
```

### Syntaxe avec @

Python offre une syntaxe plus élégante avec le symbole `@` :

```python
def mon_decorateur(fonction):
    def fonction_modifiee():
        print("--- Début ---")
        fonction()
        print("--- Fin ---")
    return fonction_modifiee

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

# Affiche :
# --- Début ---
# Bonjour !
# --- Fin ---
```

Le `@mon_decorateur` est équivalent à `dire_bonjour = mon_decorateur(dire_bonjour)`.

---

## Décorateurs avec arguments de fonction

### Le problème

Le décorateur précédent ne fonctionne que pour des fonctions sans arguments. Que faire si notre fonction a des paramètres ?

```python
@mon_decorateur
def saluer(nom):
    print(f"Bonjour {nom} !")

# ❌ Ceci produira une erreur
# saluer("Alice")
```

### La solution : *args et **kwargs

Utilisons `*args` et `**kwargs` pour accepter n'importe quels arguments :

```python
def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("--- Début ---")
        resultat = fonction(*args, **kwargs)
        print("--- Fin ---")
        return resultat
    return fonction_modifiee

@mon_decorateur
def saluer(nom):
    print(f"Bonjour {nom} !")

@mon_decorateur
def additionner(a, b):
    resultat = a + b
    print(f"{a} + {b} = {resultat}")
    return resultat

# Utilisation
saluer("Alice")
# --- Début ---
# Bonjour Alice !
# --- Fin ---

total = additionner(5, 3)
# --- Début ---
# 5 + 3 = 8
# --- Fin ---
print(f"Total : {total}")  # Total : 8
```

---

## Décorateurs avec paramètres

Parfois, nous voulons que le décorateur lui-même accepte des paramètres. Pour cela, nous devons créer une fonction qui retourne un décorateur.

### Structure à trois niveaux

```python
def repeter(nombre_fois):
    """Décorateur qui répète l'exécution d'une fonction."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            for _ in range(nombre_fois):
                resultat = fonction(*args, **kwargs)
            return resultat
        return fonction_modifiee
    return decorateur

@repeter(nombre_fois=3)
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

# Affiche :
# Bonjour !
# Bonjour !
# Bonjour !
```

### Explication du mécanisme

```python
# Ce qui se passe en coulisses :
# 1. repeter(3) retourne un décorateur
# 2. Ce décorateur est appliqué à dire_bonjour
# 3. dire_bonjour = repeter(3)(dire_bonjour)
```

### Exemple avec plusieurs paramètres

```python
def prefixe_suffixe(prefixe=">>>", suffixe="<<<"):
    """Décorateur qui ajoute un préfixe et un suffixe aux messages."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            print(prefixe)
            resultat = fonction(*args, **kwargs)
            print(suffixe)
            return resultat
        return fonction_modifiee
    return decorateur

@prefixe_suffixe(prefixe="=== DÉBUT ===", suffixe="=== FIN ===")
def afficher_message(message):
    print(message)

afficher_message("Python est génial !")

# Affiche :
# === DÉBUT ===
# Python est génial !
# === FIN ===
```

---

## Décorateurs pratiques

### 1. Mesurer le temps d'exécution

```python
import time

def mesurer_temps(fonction):
    """Mesure le temps d'exécution d'une fonction."""
    def fonction_modifiee(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        duree = fin - debut
        print(f"⏱️  {fonction.__name__} a pris {duree:.4f} secondes")
        return resultat
    return fonction_modifiee

@mesurer_temps
def calculer_somme(n):
    """Calcule la somme des n premiers nombres."""
    total = sum(range(n))
    return total

@mesurer_temps
def dormir():
    """Simule une opération longue."""
    time.sleep(2)
    print("Réveil !")

resultat = calculer_somme(1000000)  
print(f"Somme : {resultat}")  
# ⏱️  calculer_somme a pris 0.0234 secondes
# Somme : 499999500000

dormir()
# Réveil !
# ⏱️  dormir a pris 2.0012 secondes
```

### 2. Logger les appels de fonction

```python
def logger(fonction):
    """Enregistre les appels de fonction avec leurs arguments."""
    def fonction_modifiee(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        tous_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"📝 Appel de {fonction.__name__}({tous_args})")
        resultat = fonction(*args, **kwargs)
        print(f"✅ {fonction.__name__} a retourné {repr(resultat)}")
        return resultat
    return fonction_modifiee

@logger
def multiplier(a, b):
    return a * b

@logger
def saluer(nom, message="Bonjour"):
    return f"{message} {nom} !"

resultat1 = multiplier(5, 3)
# 📝 Appel de multiplier(5, 3)
# ✅ multiplier a retourné 15

resultat2 = saluer("Alice", message="Salut")
# 📝 Appel de saluer('Alice', message='Salut')
# ✅ saluer a retourné 'Salut Alice !'
```

### 3. Cache (mémorisation)

```python
def cache(fonction):
    """Mémorise les résultats d'une fonction pour éviter les recalculs."""
    resultats_sauvegardes = {}

    def fonction_modifiee(*args):
        if args in resultats_sauvegardes:
            print(f"💾 Résultat en cache pour {args}")
            return resultats_sauvegardes[args]

        print(f"🔄 Calcul en cours pour {args}")
        resultat = fonction(*args)
        resultats_sauvegardes[args] = resultat
        return resultat

    return fonction_modifiee

@cache
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
# 🔄 Calcul en cours pour (5,)
# 🔄 Calcul en cours pour (4,)
# 🔄 Calcul en cours pour (3,)
# 🔄 Calcul en cours pour (2,)
# 🔄 Calcul en cours pour (1,)
# 🔄 Calcul en cours pour (0,)
# 💾 Résultat en cache pour (1,)
# 💾 Résultat en cache pour (2,)
# 💾 Résultat en cache pour (3,)
# 5

print(fibonacci(5))  # Deuxième appel
# 💾 Résultat en cache pour (5,)
# 5
```

> 💡 **En pratique**, utilisez `functools.cache` (Python 3.9+) ou `functools.lru_cache` plutôt qu'un cache manuel :
>
> ```python
> from functools import cache
>
> @cache
> def fibonacci(n):
>     if n < 2:
>         return n
>     return fibonacci(n-1) + fibonacci(n-2)
>
> print(fibonacci(50))  # Instantané grâce au cache
> ```
>
> `lru_cache(maxsize=128)` permet de limiter la taille du cache en mémoire.

### 4. Contrôle d'accès

```python
def necessite_authentification(fonction):
    """Vérifie qu'un utilisateur est authentifié avant d'exécuter."""
    def fonction_modifiee(*args, **kwargs):
        # Simulation d'une vérification d'authentification
        utilisateur_connecte = True  # À remplacer par une vraie vérification

        if not utilisateur_connecte:
            print("❌ Accès refusé : vous devez être connecté")
            return None

        print("✅ Authentification réussie")
        return fonction(*args, **kwargs)

    return fonction_modifiee

@necessite_authentification
def voir_profil(nom):
    print(f"📋 Profil de {nom}")
    return {"nom": nom, "age": 30}

@necessite_authentification
def modifier_donnees():
    print("✏️ Modification des données...")

profil = voir_profil("Alice")
# ✅ Authentification réussie
# 📋 Profil de Alice
```

### 5. Retry (réessayer en cas d'échec)

```python
import time

def retry(nombre_essais=3, delai=1):
    """Réessaie l'exécution d'une fonction en cas d'erreur."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            for tentative in range(1, nombre_essais + 1):
                try:
                    print(f"🔄 Tentative {tentative}/{nombre_essais}")
                    resultat = fonction(*args, **kwargs)
                    print(f"✅ Succès !")
                    return resultat
                except Exception as e:
                    print(f"❌ Erreur : {e}")
                    if tentative < nombre_essais:
                        print(f"⏳ Attente de {delai} seconde(s)...")
                        time.sleep(delai)
                    else:
                        print(f"⛔ Échec après {nombre_essais} tentatives")
                        raise
        return fonction_modifiee
    return decorateur

@retry(nombre_essais=3, delai=2)
def operation_instable():
    """Simule une opération qui peut échouer."""
    import random
    if random.random() < 0.7:  # 70% de chances d'échouer
        raise Exception("Connexion perdue")
    return "Données récupérées"

# resultat = operation_instable()
```

---

## Empiler plusieurs décorateurs

On peut appliquer plusieurs décorateurs à une même fonction. Ils sont appliqués de bas en haut.

```python
def decorateur_1(fonction):
    def fonction_modifiee(*args, **kwargs):
        print(">>> Décorateur 1 - Avant")
        resultat = fonction(*args, **kwargs)
        print("<<< Décorateur 1 - Après")
        return resultat
    return fonction_modifiee

def decorateur_2(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("  >> Décorateur 2 - Avant")
        resultat = fonction(*args, **kwargs)
        print("  << Décorateur 2 - Après")
        return resultat
    return fonction_modifiee

@decorateur_1
@decorateur_2
def ma_fonction():
    print("    Exécution de la fonction")

ma_fonction()

# Affiche :
# >>> Décorateur 1 - Avant
#   >> Décorateur 2 - Avant
#     Exécution de la fonction
#   << Décorateur 2 - Après
# <<< Décorateur 1 - Après
```

### Exemple pratique : combiner logger et mesurer_temps

```python
@logger
@mesurer_temps
def calculer_factorielle(n):
    """Calcule la factorielle de n."""
    if n <= 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

resultat = calculer_factorielle(5)
# 📝 Appel de fonction_modifiee(5)
# ⏱️  calculer_factorielle a pris 0.0001 secondes
# ✅ fonction_modifiee a retourné 120
```

---

## Le module functools.wraps

### Le problème

Quand on utilise un décorateur, la fonction décorée perd ses métadonnées (nom, docstring, etc.) :

```python
def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur
def ma_fonction():
    """Ceci est ma fonction."""
    pass

print(ma_fonction.__name__)  # Affiche : fonction_modifiee  
print(ma_fonction.__doc__)   # Affiche : None  
```

### La solution : @wraps

Le décorateur `@wraps` de `functools` préserve les métadonnées :

```python
from functools import wraps

def mon_decorateur(fonction):
    @wraps(fonction)
    def fonction_modifiee(*args, **kwargs):
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur
def ma_fonction():
    """Ceci est ma fonction."""
    pass

print(ma_fonction.__name__)  # Affiche : ma_fonction  
print(ma_fonction.__doc__)   # Affiche : Ceci est ma fonction.  
```

### Pourquoi c'est important ?

```python
from functools import wraps

def mon_decorateur_propre(fonction):
    @wraps(fonction)
    def fonction_modifiee(*args, **kwargs):
        """Wrapper ajouté par le décorateur."""
        return fonction(*args, **kwargs)
    return fonction_modifiee

@mon_decorateur_propre
def calculer_carre(x):
    """Calcule le carré d'un nombre."""
    return x ** 2

# Les métadonnées sont préservées
print(f"Nom : {calculer_carre.__name__}")        # Nom : calculer_carre  
print(f"Doc : {calculer_carre.__doc__}")          # Doc : Calcule le carré d'un nombre.  
print(f"Module : {calculer_carre.__module__}")    # Module : __main__  

# Pratique pour l'aide et la documentation
help(calculer_carre)
```

### Template de décorateur recommandé

Voici le template recommandé pour créer des décorateurs :

```python
from functools import wraps

def mon_decorateur(fonction):
    """Description de ce que fait le décorateur."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        # Code avant l'exécution
        resultat = fonction(*args, **kwargs)
        # Code après l'exécution
        return resultat
    return wrapper
```

Avec paramètres :

```python
from functools import wraps

def mon_decorateur(param1, param2="valeur_par_defaut"):
    """Description de ce que fait le décorateur."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            # Utiliser param1 et param2
            resultat = fonction(*args, **kwargs)
            return resultat
        return wrapper
    return decorateur
```

---

## Décorateurs de classe

Les décorateurs peuvent aussi être appliqués aux classes entières.

### Décorateur qui modifie une classe

```python
def ajouter_methode_str(cls):
    """Ajoute une méthode __str__ à une classe."""
    def __str__(self):
        attributs = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{cls.__name__}({attributs})"

    cls.__str__ = __str__
    return cls

@ajouter_methode_str
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = Personne("Alice", 30)  
print(p)  # Affiche : Personne(nom=Alice, age=30)  
```

### Singleton avec un décorateur

```python
def singleton(cls):
    """Transforme une classe en singleton."""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Configuration:
    def __init__(self):
        self.parametre = "valeur"
        print("Configuration créée")

# Première création
config1 = Configuration()  # Affiche : Configuration créée  
config1.parametre = "nouvelle valeur"  

# Deuxième "création" : retourne la même instance
config2 = Configuration()  # N'affiche rien  
print(config2.parametre)   # Affiche : nouvelle valeur  
print(config1 is config2)  # Affiche : True  
```

---

## Décorateurs comme classes

On peut aussi créer des décorateurs sous forme de classes :

### Exemple basique

```python
class Compteur:
    """Décorateur qui compte le nombre d'appels."""
    def __init__(self, fonction):
        self.fonction = fonction
        self.nombre_appels = 0

    def __call__(self, *args, **kwargs):
        self.nombre_appels += 1
        print(f"🔢 Appel n°{self.nombre_appels} de {self.fonction.__name__}")
        return self.fonction(*args, **kwargs)

@Compteur
def dire_bonjour(nom):
    print(f"Bonjour {nom} !")

dire_bonjour("Alice")  # Appel n°1  
dire_bonjour("Bob")    # Appel n°2  
dire_bonjour("Charlie")  # Appel n°3  
```

### Avec paramètres

```python
class RepeterAction:
    """Décorateur classe qui répète une action."""
    def __init__(self, nombre_fois=2):
        self.nombre_fois = nombre_fois

    def __call__(self, fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            for i in range(self.nombre_fois):
                print(f"⚡ Exécution {i+1}/{self.nombre_fois}")
                resultat = fonction(*args, **kwargs)
            return resultat
        return wrapper

@RepeterAction(nombre_fois=3)
def afficher_message(message):
    print(f"  📢 {message}")

afficher_message("Python")
# ⚡ Exécution 1/3
#   📢 Python
# ⚡ Exécution 2/3
#   📢 Python
# ⚡ Exécution 3/3
#   📢 Python
```

---

## Cas d'usage avancés

### 1. Validation des arguments

```python
from functools import wraps

def valider_types(**type_attendu):
    """Valide les types des arguments."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            # Vérifier les kwargs
            for nom_arg, valeur in kwargs.items():
                if nom_arg in type_attendu:
                    type_requis = type_attendu[nom_arg]
                    if not isinstance(valeur, type_requis):
                        raise TypeError(
                            f"{nom_arg} doit être de type {type_requis.__name__}, "
                            f"pas {type(valeur).__name__}"
                        )
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@valider_types(nom=str, age=int)
def creer_personne(nom, age):
    return {"nom": nom, "age": age}

# ✅ Fonctionne
personne1 = creer_personne(nom="Alice", age=30)  
print(personne1)  # {'nom': 'Alice', 'age': 30}  

# ❌ Lève une erreur
# personne2 = creer_personne(nom="Bob", age="trente")
# TypeError: age doit être de type int, pas str
```

### 2. Rate limiting (limitation du taux d'appel)

```python
import time  
from functools import wraps  

def rate_limit(appels_max, periode):
    """Limite le nombre d'appels dans une période donnée."""
    def decorateur(fonction):
        appels = []

        @wraps(fonction)
        def wrapper(*args, **kwargs):
            maintenant = time.time()

            # Supprimer les appels trop anciens
            appels[:] = [t for t in appels if maintenant - t < periode]

            if len(appels) >= appels_max:
                temps_attente = periode - (maintenant - appels[0])
                print(f"⏳ Trop de requêtes. Attendez {temps_attente:.1f} secondes")
                return None

            appels.append(maintenant)
            return fonction(*args, **kwargs)

        return wrapper
    return decorateur

@rate_limit(appels_max=3, periode=10)  # 3 appels max par 10 secondes
def rechercher(terme):
    print(f"🔍 Recherche de : {terme}")
    return f"Résultats pour {terme}"

# Les 3 premiers appels fonctionnent
rechercher("Python")   # ✅  
rechercher("Django")   # ✅  
rechercher("Flask")    # ✅  
rechercher("FastAPI")  # ⏳ Trop de requêtes...  
```

### 3. Convertir des exceptions

```python
from functools import wraps

def convertir_exceptions(exception_source, exception_cible):
    """Convertit un type d'exception en un autre."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            try:
                return fonction(*args, **kwargs)
            except exception_source as e:
                raise exception_cible(f"Erreur convertie: {e}") from e
        return wrapper
    return decorateur

class ErreurMetier(Exception):
    """Exception personnalisée pour la logique métier."""
    pass

@convertir_exceptions(ValueError, ErreurMetier)
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

try:
    resultat = diviser(10, 0)
except ErreurMetier as e:
    print(f"❌ Erreur métier : {e}")
    # Affiche : ❌ Erreur métier : Erreur convertie: Division par zéro
```

### 4. Décorateur de dépréciation

```python
import warnings  
from functools import wraps  

def deprecie(message="Cette fonction est dépréciée"):
    """Marque une fonction comme dépréciée."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{fonction.__name__} est déprécié. {message}",
                category=DeprecationWarning,
                stacklevel=2
            )
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@deprecie("Utilisez nouvelle_fonction() à la place")
def ancienne_fonction():
    """Ancienne implémentation."""
    return "Ancienne version"

def nouvelle_fonction():
    """Nouvelle implémentation."""
    return "Nouvelle version"

# Lors de l'appel, un avertissement sera affiché
# resultat = ancienne_fonction()
```

---

## Décorateurs et performances

### Overhead des décorateurs

Chaque décorateur ajoute un léger coût en performance :

```python
import time  
from functools import wraps  

def mesurer_overhead():
    """Compare les performances avec et sans décorateurs."""

    # Fonction sans décorateur
    def fonction_simple(x):
        return x * 2

    # Fonction avec décorateur
    def decorateur(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @decorateur
    def fonction_decoree(x):
        return x * 2

    # Test de performance
    iterations = 1000000

    # Sans décorateur
    debut = time.time()
    for i in range(iterations):
        fonction_simple(i)
    duree_simple = time.time() - debut

    # Avec décorateur
    debut = time.time()
    for i in range(iterations):
        fonction_decoree(i)
    duree_decoree = time.time() - debut

    print(f"Sans décorateur : {duree_simple:.4f}s")
    print(f"Avec décorateur : {duree_decoree:.4f}s")
    print(f"Overhead : {((duree_decoree - duree_simple) / duree_simple * 100):.2f}%")

# mesurer_overhead()
# L'overhead est généralement négligeable pour la plupart des applications
```

---

## Bonnes pratiques

### 1. Utilisez toujours @wraps

```python
from functools import wraps

# ✅ Bon
def bon_decorateur(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper

# ❌ Mauvais
def mauvais_decorateur(fonction):
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper
```

### 2. Documentez vos décorateurs

```python
from functools import wraps

def mon_decorateur(fonction):
    """
    Description claire de ce que fait le décorateur.

    Args:
        fonction: La fonction à décorer

    Returns:
        La fonction décorée avec des fonctionnalités ajoutées

    Example:
        @mon_decorateur
        def ma_fonction():
            pass
    """
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper
```

### 3. Gardez les décorateurs simples

```python
# ✅ Bon : décorateur avec une responsabilité claire
def logger(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        print(f"Appel de {fonction.__name__}")
        return fonction(*args, **kwargs)
    return wrapper

# ❌ Mauvais : trop de responsabilités
def super_decorateur(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        print("Log")
        debut = time.time()
        try:
            resultat = fonction(*args, **kwargs)
            # ... validation ...
            # ... cache ...
            # ... etc ...
            return resultat
        finally:
            print(f"Temps: {time.time() - debut}")
    return wrapper
```

### 4. Attention à l'ordre des décorateurs

```python
# L'ordre compte !
@decorateur_A
@decorateur_B
def fonction():
    pass

# Est équivalent à :
# fonction = decorateur_A(decorateur_B(fonction))
```

---

## Résumé

Dans ce chapitre, nous avons exploré les décorateurs en profondeur :

### Concepts clés

**Décorateurs de base** :
- Fonctions qui modifient d'autres fonctions
- Syntaxe `@decorateur` pour une application élégante
- Utilisent `*args` et `**kwargs` pour accepter tous types d'arguments

**Décorateurs avec paramètres** :
- Structure à trois niveaux (fonction → décorateur → wrapper)
- Permettent de personnaliser le comportement du décorateur
- Plus flexibles mais plus complexes

**functools.wraps** :
- Préserve les métadonnées de la fonction originale
- Essentiel pour maintenir la documentation et le débogage
- À utiliser systématiquement dans vos décorateurs

**Décorateurs de classe** :
- Peuvent modifier ou étendre des classes entières
- Utiles pour le pattern Singleton et autres patterns
- Peuvent aussi être implémentés comme des classes

### Cas d'usage courants

✅ **Logging** : Enregistrer les appels de fonctions  
✅ **Timing** : Mesurer les performances  
✅ **Cache** : Mémoriser les résultats  
✅ **Validation** : Vérifier les arguments  
✅ **Authentification** : Contrôler l'accès  
✅ **Retry** : Réessayer en cas d'échec  
✅ **Rate limiting** : Limiter la fréquence d'appels

### Points à retenir

- Les décorateurs augmentent la réutilisabilité du code
- Ils séparent les préoccupations (séparation des responsabilités)
- Attention à ne pas abuser : trop de décorateurs nuisent à la lisibilité
- Toujours utiliser `@wraps` pour préserver les métadonnées
- Privilégier la simplicité : un décorateur = une responsabilité

Les décorateurs sont un outil puissant qui, utilisé correctement, rend votre code plus élégant, maintenable et réutilisable !

Dans le prochain chapitre, nous explorerons les générateurs et expressions génératrices, une autre technique essentielle de la programmation fonctionnelle en Python.

⏭️ [Générateurs et expressions génératrices](/05-programmation-fonctionnelle/04-generateurs.md)
