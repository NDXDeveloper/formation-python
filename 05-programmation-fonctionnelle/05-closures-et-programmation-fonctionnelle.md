🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.5 : Closures et programmation fonctionnelle

## Introduction

Les closures (fermetures) sont un concept avancé mais essentiel de la programmation fonctionnelle. Une closure est une fonction qui "capture" et "se souvient" des variables de son environnement, même après que cet environnement ait disparu. C'est un mécanisme puissant qui permet de créer des fonctions très flexibles et réutilisables.

## Qu'est-ce qu'une closure ?

### Concept de base

Une closure se forme quand :
1. Une fonction est définie à l'intérieur d'une autre fonction
2. La fonction interne utilise des variables de la fonction externe
3. La fonction externe retourne la fonction interne

```python
def fonction_externe(x):
    def fonction_interne(y):
        return x + y  # x vient de la fonction externe !
    return fonction_interne

# Créer une closure
additionner_5 = fonction_externe(5)

# Utiliser la closure
resultat = additionner_5(3)  # 5 + 3 = 8
print(resultat)  # 8
```

### Que se passe-t-il ?

```python
def creer_multiplicateur(facteur):
    def multiplier(nombre):
        return nombre * facteur  # facteur est "capturé"
    return multiplier

# Créer plusieurs closures
doubler = creer_multiplicateur(2)
tripler = creer_multiplicateur(3)

# Chaque closure "se souvient" de son facteur
print(doubler(4))  # 8 (4 * 2)
print(tripler(4))  # 12 (4 * 3)

# Le facteur original a disparu, mais les closures s'en souviennent !
```

## Pourquoi les closures fonctionnent-elles ?

### Variables libres et environnement lexical

```python
def demo_closure():
    # Variable de la fonction externe
    message = "Bonjour"
    compteur = 0

    def fonction_interne():
        # Ces variables sont des "variables libres"
        nonlocal compteur  # Permet de modifier compteur
        compteur += 1
        return f"{message} #{compteur}"

    return fonction_interne

# Créer la closure
saluer = demo_closure()

# Utiliser plusieurs fois
print(saluer())  # Bonjour #1
print(saluer())  # Bonjour #2
print(saluer())  # Bonjour #3

# L'état est conservé entre les appels !
```

### Inspection des variables capturées

```python
def creer_compteur(debut=0):
    def incrementer():
        nonlocal debut
        debut += 1
        return debut
    return incrementer

compteur = creer_compteur(10)

# Voir les variables capturées
print(compteur.__closure__)  # (<cell at 0x...>,)
print(compteur.__closure__[0].cell_contents)  # 10

print(compteur())  # 11
print(compteur.__closure__[0].cell_contents)  # 11
```

## Exemples pratiques de closures

### 1. Factory de fonctions de validation

```python
def creer_validateur(min_val, max_val):
    """Crée une fonction de validation pour une plage de valeurs"""
    def valider(valeur):
        if not isinstance(valeur, (int, float)):
            return False, "Doit être un nombre"
        if valeur < min_val:
            return False, f"Doit être >= {min_val}"
        if valeur > max_val:
            return False, f"Doit être <= {max_val}"
        return True, "Valide"

    return valider

# Créer différents validateurs
valider_age = creer_validateur(0, 120)
valider_pourcentage = creer_validateur(0, 100)
valider_temperature = creer_validateur(-273, 1000)

# Utilisation
print(valider_age(25))        # (True, 'Valide')
print(valider_age(-5))        # (False, 'Doit être >= 0')
print(valider_pourcentage(150))  # (False, 'Doit être <= 100')
```

### 2. Configuration de fonctions

```python
def creer_formateur_prix(devise="€", decimales=2):
    """Crée une fonction pour formater les prix"""
    def formater_prix(prix):
        format_str = f"{{:.{decimales}f}}{devise}"
        return format_str.format(prix)

    return formater_prix

# Créer des formateurs pour différentes devises
formater_euro = creer_formateur_prix("€", 2)
formater_dollar = creer_formateur_prix("$", 2)
formater_yen = creer_formateur_prix("¥", 0)

# Utilisation
prix = 19.99
print(formater_euro(prix))   # 19.99€
print(formater_dollar(prix)) # 19.99$
print(formater_yen(prix))    # 20¥
```

### 3. Générateur de fonctions mathématiques

```python
def creer_fonction_polynomiale(*coefficients):
    """Crée une fonction polynomiale : ax² + bx + c"""
    def evaluer(x):
        resultat = 0
        for i, coeff in enumerate(coefficients):
            resultat += coeff * (x ** (len(coefficients) - 1 - i))
        return resultat

    return evaluer

# Créer différentes fonctions
lineaire = creer_fonction_polynomiale(2, 3)        # 2x + 3
quadratique = creer_fonction_polynomiale(1, -2, 1) # x² - 2x + 1
cubique = creer_fonction_polynomiale(1, 0, -3, 2)  # x³ - 3x + 2

# Utilisation
x = 2
print(f"f(x) = 2x + 3, f({x}) = {lineaire(x)}")        # 7
print(f"g(x) = x² - 2x + 1, g({x}) = {quadratique(x)}") # 1
print(f"h(x) = x³ - 3x + 2, h({x}) = {cubique(x)}")    # 4
```

### 4. Système de cache avec expiration

```python
import time

def creer_cache_expire(duree_vie):
    """Crée un cache avec expiration automatique"""
    cache = {}

    def fonction_avec_cache(func):
        def wrapper(*args, **kwargs):
            # Créer une clé unique
            cle = str(args) + str(sorted(kwargs.items()))
            maintenant = time.time()

            # Vérifier si en cache et valide
            if cle in cache:
                resultat, timestamp = cache[cle]
                if maintenant - timestamp < duree_vie:
                    print(f"Cache hit pour {func.__name__}")
                    return resultat
                else:
                    # Expirer l'entrée
                    del cache[cle]

            # Calculer et mettre en cache
            print(f"Calcul en cours pour {func.__name__}")
            resultat = func(*args, **kwargs)
            cache[cle] = (resultat, maintenant)
            return resultat

        # Ajouter une méthode pour vider le cache
        wrapper.vider_cache = lambda: cache.clear()
        wrapper.info_cache = lambda: f"Cache: {len(cache)} entrées"

        return wrapper

    return fonction_avec_cache

# Utilisation
cache_5_sec = creer_cache_expire(5)

@cache_5_sec
def calcul_lent(n):
    time.sleep(1)  # Simulation
    return n * n

# Tests
print(calcul_lent(5))  # Calcul en cours
print(calcul_lent(5))  # Cache hit
print(calcul_lent.info_cache())  # Cache: 1 entrées
```

## Closures vs Classes

Parfois, les closures peuvent remplacer des classes simples :

### Avec une classe

```python
class Compteur:
    def __init__(self, debut=0, pas=1):
        self.valeur = debut
        self.pas = pas

    def incrementer(self):
        self.valeur += self.pas
        return self.valeur

    def decreementer(self):
        self.valeur -= self.pas
        return self.valeur

    def reset(self):
        self.valeur = 0

# Utilisation
compteur = Compteur(10, 2)
print(compteur.incrementer())  # 12
print(compteur.incrementer())  # 14
```

### Avec des closures

```python
def creer_compteur(debut=0, pas=1):
    valeur = [debut]  # Liste pour permettre la modification

    def incrementer():
        valeur[0] += pas
        return valeur[0]

    def decrementer():
        valeur[0] -= pas
        return valeur[0]

    def reset():
        valeur[0] = debut
        return valeur[0]

    def get_valeur():
        return valeur[0]

    # Retourner un dictionnaire de fonctions
    return {
        'incrementer': incrementer,
        'decrementer': decrementer,
        'reset': reset,
        'valeur': get_valeur
    }

# Utilisation
compteur = creer_compteur(10, 2)
print(compteur['incrementer']())  # 12
print(compteur['incrementer']())  # 14
print(compteur['valeur']())       # 14
```

## Patterns avancés avec les closures

### 1. Closure avec état multiple

```python
def creer_gestionnaire_etat():
    """Gestionnaire d'état avec plusieurs variables"""
    etat = {
        'compteur': 0,
        'historique': [],
        'actif': True
    }

    def modifier_etat(action, valeur=None):
        if not etat['actif']:
            return "Gestionnaire désactivé"

        if action == 'incrementer':
            etat['compteur'] += valeur if valeur else 1
            etat['historique'].append(f"Incrémenté de {valeur or 1}")

        elif action == 'reset':
            etat['compteur'] = 0
            etat['historique'].append("Reset")

        elif action == 'desactiver':
            etat['actif'] = False
            etat['historique'].append("Désactivé")

        elif action == 'historique':
            return etat['historique'].copy()

        elif action == 'status':
            return etat.copy()

        return etat['compteur']

    return modifier_etat

# Utilisation
gestionnaire = creer_gestionnaire_etat()

print(gestionnaire('incrementer', 5))    # 5
print(gestionnaire('incrementer'))       # 6
print(gestionnaire('status'))            # État complet
print(gestionnaire('historique'))        # Historique des actions
```

### 2. Currying avec closures

Le currying transforme une fonction à plusieurs arguments en une série de fonctions à un argument :

```python
def curry(func, arity=None):
    """Transforme une fonction en version curried"""
    if arity is None:
        arity = func.__code__.co_argcount

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        else:
            def partial(*more_args):
                return curried(*(args + more_args))
            return partial

    return curried

# Exemple d'utilisation
def additionner_trois(a, b, c):
    return a + b + c

# Version curried
add_curry = curry(additionner_trois)

# Utilisation étape par étape
add_5 = add_curry(5)
add_5_3 = add_5(3)
resultat = add_5_3(2)  # 10

# Ou en une fois
resultat2 = add_curry(1)(2)(3)  # 6

print(resultat)   # 10
print(resultat2)  # 6
```

### 3. Composition de fonctions

```python
def composer(*fonctions):
    """Compose plusieurs fonctions ensemble"""
    def composition(valeur):
        for func in reversed(fonctions):
            valeur = func(valeur)
        return valeur
    return composition

# Fonctions de base
def doubler(x):
    return x * 2

def ajouter_un(x):
    return x + 1

def mettre_au_carre(x):
    return x ** 2

# Créer une fonction composée
# f(g(h(x))) où f=doubler, g=ajouter_un, h=mettre_au_carre
operation_complexe = composer(doubler, ajouter_un, mettre_au_carre)

# Test avec x = 3
# mettre_au_carre(3) = 9
# ajouter_un(9) = 10
# doubler(10) = 20
print(operation_complexe(3))  # 20
```

## Closures et décorateurs

Les décorateurs utilisent souvent des closures :

### Décorateur avec état

```python
def compter_appels(func):
    """Décorateur qui compte les appels à une fonction"""
    nb_appels = [0]  # Liste pour permettre la modification

    def wrapper(*args, **kwargs):
        nb_appels[0] += 1
        print(f"{func.__name__} appelée {nb_appels[0]} fois")
        return func(*args, **kwargs)

    # Ajouter une méthode pour consulter le compteur
    wrapper.get_nb_appels = lambda: nb_appels[0]
    wrapper.reset_compteur = lambda: nb_appels.__setitem__(0, 0)

    return wrapper

@compter_appels
def ma_fonction():
    return "Hello"

# Tests
ma_fonction()  # ma_fonction appelée 1 fois
ma_fonction()  # ma_fonction appelée 2 fois
print(f"Total: {ma_fonction.get_nb_appels()}")  # Total: 2
```

### Factory de décorateurs

```python
def creer_limiteur_taux(max_appels, periode):
    """Crée un décorateur de limitation de taux"""
    import time

    def decorateur(func):
        appels = []  # Historique des appels

        def wrapper(*args, **kwargs):
            maintenant = time.time()

            # Nettoyer les anciens appels
            appels[:] = [t for t in appels if maintenant - t < periode]

            # Vérifier la limite
            if len(appels) >= max_appels:
                attente = periode - (maintenant - appels[0])
                raise Exception(f"Trop d'appels. Attendez {attente:.1f}s")

            # Enregistrer cet appel
            appels.append(maintenant)
            return func(*args, **kwargs)

        return wrapper
    return decorateur

# Créer différents limiteurs
@creer_limiteur_taux(max_appels=3, periode=60)  # 3 appels par minute
def api_importante():
    return "Données importantes"

@creer_limiteur_taux(max_appels=10, periode=1)  # 10 appels par seconde
def api_rapide():
    return "Données rapides"
```

## Exercices pratiques

### Exercice 1 : Générateur de séquences

```python
def creer_generateur_sequence(type_sequence):
    """Crée un générateur pour différents types de séquences"""

    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def nombres_premiers():
        def est_premier(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        n = 2
        while True:
            if est_premier(n):
                yield n
            n += 1

    def carres():
        n = 0
        while True:
            yield n * n
            n += 1

    sequences = {
        'fibonacci': fibonacci,
        'premiers': nombres_premiers,
        'carres': carres
    }

    if type_sequence in sequences:
        return sequences[type_sequence]()
    else:
        raise ValueError(f"Type de séquence inconnu: {type_sequence}")

# Tests
fib = creer_generateur_sequence('fibonacci')
premiers = creer_generateur_sequence('premiers')

print("Fibonacci:", [next(fib) for _ in range(10)])
print("Premiers:", [next(premiers) for _ in range(10)])
```

### Exercice 2 : Système de configuration

```python
def creer_configurateur():
    """Crée un système de configuration avec closures"""
    config = {}

    def definir(cle, valeur):
        config[cle] = valeur
        return f"Configuration '{cle}' définie"

    def obtenir(cle, defaut=None):
        return config.get(cle, defaut)

    def supprimer(cle):
        if cle in config:
            del config[cle]
            return f"Configuration '{cle}' supprimée"
        return f"Configuration '{cle}' introuvable"

    def lister():
        return config.copy()

    def sauvegarder_profil(nom_profil):
        profils = getattr(sauvegarder_profil, 'profils', {})
        profils[nom_profil] = config.copy()
        sauvegarder_profil.profils = profils
        return f"Profil '{nom_profil}' sauvegardé"

    def charger_profil(nom_profil):
        profils = getattr(sauvegarder_profil, 'profils', {})
        if nom_profil in profils:
            config.clear()
            config.update(profils[nom_profil])
            return f"Profil '{nom_profil}' chargé"
        return f"Profil '{nom_profil}' introuvable"

    # Retourner un dictionnaire de fonctions
    return {
        'definir': definir,
        'obtenir': obtenir,
        'supprimer': supprimer,
        'lister': lister,
        'sauvegarder_profil': sauvegarder_profil,
        'charger_profil': charger_profil
    }

# Utilisation
config = creer_configurateur()

config['definir']('theme', 'sombre')
config['definir']('langue', 'fr')
print(config['lister']())  # {'theme': 'sombre', 'langue': 'fr'}

config['sauvegarder_profil']('developpeur')
config['definir']('theme', 'clair')
config['charger_profil']('developpeur')
print(config['obtenir']('theme'))  # sombre
```

### Exercice 3 : Calculator avec historique

```python
def creer_calculatrice():
    """Crée une calculatrice avec historique des opérations"""
    historique = []
    resultat_courant = 0

    def operation(operateur, valeur=None):
        nonlocal resultat_courant

        if operateur == 'clear':
            resultat_courant = 0
            historique.append("Clear")

        elif operateur == 'set' and valeur is not None:
            resultat_courant = valeur
            historique.append(f"Set {valeur}")

        elif valeur is not None:
            ancien_resultat = resultat_courant

            if operateur == '+':
                resultat_courant += valeur
            elif operateur == '-':
                resultat_courant -= valeur
            elif operateur == '*':
                resultat_courant *= valeur
            elif operateur == '/':
                if valeur == 0:
                    raise ValueError("Division par zéro")
                resultat_courant /= valeur
            else:
                raise ValueError(f"Opérateur inconnu: {operateur}")

            historique.append(f"{ancien_resultat} {operateur} {valeur} = {resultat_courant}")

        return resultat_courant

    def get_historique():
        return historique.copy()

    def get_resultat():
        return resultat_courant

    return {
        'operation': operation,
        'historique': get_historique,
        'resultat': get_resultat
    }

# Test
calc = creer_calculatrice()

calc['operation']('set', 10)
calc['operation']('+', 5)
calc['operation']('*', 2)
calc['operation']('/', 3)

print(f"Résultat: {calc['resultat']()}")
print("Historique:")
for etape in calc['historique']():
    print(f"  {etape}")
```

## Avantages et inconvénients

### ✅ Avantages des closures

1. **Encapsulation** : Variables privées naturellement protégées
2. **État persistant** : Conservation de l'état sans classes
3. **Factory pattern** : Création facile de fonctions spécialisées
4. **Flexibilité** : Configuration dynamique de comportements
5. **Composition** : Facilite la création de pipelines de traitement

### ❌ Inconvénients

1. **Complexité** : Peut rendre le code difficile à comprendre
2. **Débogage** : Plus difficile à déboguer que les classes
3. **Performance** : Léger overhead par rapport aux variables globales
4. **Mémoire** : Les variables capturées restent en mémoire

## Bonnes pratiques

### ✅ À faire

1. **Utilisez des noms explicites** pour les fonctions de closure
2. **Documentez clairement** le comportement et l'état capturé
3. **Préférez les closures simples** pour des cas d'usage spécifiques
4. **Utilisez `nonlocal`** quand vous devez modifier l'état capturé

### ❌ À éviter

1. **Closures trop complexes** : Préférez les classes pour la logique complexe
2. **Trop de variables capturées** : Garde l'interface simple
3. **Effets de bord cachés** : Rendez les modifications d'état évidentes

## Résumé

Les closures sont un mécanisme puissant qui permet :

- **Capture de l'environnement** : Les variables externes sont "emprisonnées"
- **État persistant** : Conservation de données entre les appels
- **Factory de fonctions** : Création de fonctions spécialisées
- **Patterns fonctionnels** : Currying, composition, configuration

**Points clés :**
- Une closure "se souvient" de son environnement de création
- Utilisez `nonlocal` pour modifier les variables capturées
- Les closures sont parfaites pour créer des fonctions configurables
- Elles peuvent souvent remplacer des classes simples
- Très utiles pour les décorateurs et les factories de fonctions

Les closures complètent parfaitement les autres concepts de programmation fonctionnelle et vous permettent de créer du code élégant et réutilisable. Elles constituent la base de nombreux patterns avancés en Python.

Félicitations ! Vous avez maintenant une compréhension complète de la programmation fonctionnelle en Python. Ces concepts vous permettront d'écrire du code plus expressif, plus modulaire et souvent plus performant.

⏭️
