🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.5 Gestion des erreurs avec try/except

## Introduction

Les erreurs font partie intégrante de la programmation. Même les meilleurs programmeurs en rencontrent quotidiennement ! Ce qui distingue un bon programme d'un mauvais, c'est la façon dont il **gère** ces erreurs.

Imaginez une application qui plante complètement parce que l'utilisateur a entré une lettre au lieu d'un nombre. Ce n'est pas une bonne expérience ! La gestion des erreurs permet à votre programme de :
- **Anticiper les problèmes** : prévoir ce qui peut mal tourner
- **Réagir élégamment** : afficher un message clair au lieu de planter
- **Continuer à fonctionner** : ne pas arrêter tout le programme pour une petite erreur

En Python, on utilise le mécanisme des **exceptions** pour gérer les erreurs de manière propre et structurée.

---

## Types d'Erreurs en Python

### 1. Erreurs de Syntaxe (Syntax Errors)

Les **erreurs de syntaxe** se produisent quand vous écrivez du code qui ne respecte pas les règles de Python. Le programme ne peut même pas démarrer.

**Exemples** :
```python
# Oublier les deux points
if age >= 18
    print("Majeur")
# SyntaxError: invalid syntax

# Oublier de fermer une parenthèse
print("Bonjour"
# SyntaxError: unexpected EOF while parsing

# Indentation incorrecte
def ma_fonction():
print("Erreur")
# IndentationError: expected an indented block
```

Ces erreurs doivent être **corrigées dans le code**. Elles ne peuvent pas être gérées avec try/except car le programme ne peut pas s'exécuter.

### 2. Exceptions (Runtime Errors)

Les **exceptions** sont des erreurs qui se produisent **pendant l'exécution** du programme. Le code est syntaxiquement correct, mais quelque chose ne se passe pas comme prévu.

**Exemples courants** :

```python
# Division par zéro
resultat = 10 / 0
# ZeroDivisionError: division by zero

# Conversion impossible
nombre = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'

# Accès à un index qui n'existe pas
liste = [1, 2, 3]
element = liste[10]
# IndexError: list index out of range

# Clé inexistante dans un dictionnaire
personne = {"nom": "Alice"}
age = personne["age"]
# KeyError: 'age'

# Fichier introuvable
fichier = open("inexistant.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'inexistant.txt'
```

Ces erreurs **peuvent** être gérées avec try/except pour que le programme continue à fonctionner.

---

## Le Bloc try/except de Base

### Syntaxe

```python
try:
    # Code qui peut provoquer une erreur
    instruction_risquee()
except:
    # Code à exécuter si une erreur se produit
    print("Une erreur s'est produite")
```

### Premier exemple

Sans gestion d'erreur, le programme plante :

```python
nombre = int(input("Entrez un nombre : "))
print(f"Le double est : {nombre * 2}")
```

Si l'utilisateur entre "abc", le programme s'arrête avec une erreur.

**Avec gestion d'erreur** :

```python
try:
    nombre = int(input("Entrez un nombre : "))
    print(f"Le double est : {nombre * 2}")
except:
    print("Erreur : vous devez entrer un nombre valide")

print("Le programme continue...")
```

Maintenant, si l'utilisateur entre "abc", le programme affiche un message d'erreur mais **continue à fonctionner** !

### Comment ça fonctionne ?

1. Python essaie d'exécuter le code dans le bloc `try`
2. Si tout se passe bien, le bloc `except` est ignoré
3. Si une erreur se produit, Python **saute immédiatement** au bloc `except`
4. Après le `except`, le programme continue normalement

```python
try:
    print("Début du try")
    resultat = 10 / 0  # Erreur ici !
    print("Cette ligne ne sera jamais exécutée")
except:
    print("Une erreur s'est produite")

print("Le programme continue")
```

**Résultat** :
```
Début du try
Une erreur s'est produite
Le programme continue
```

---

## Capturer des Exceptions Spécifiques

Utiliser `except` sans spécifier le type d'erreur capture **toutes** les erreurs. C'est souvent trop large. Il est préférable de capturer des exceptions **spécifiques**.

### Syntaxe

```python
try:
    # Code risqué
    pass
except TypeErreur:
    # Gérer ce type d'erreur spécifique
    pass
```

### Exemples

```python
try:
    nombre = int(input("Entrez un nombre : "))
    resultat = 100 / nombre
    print(f"Résultat : {resultat}")
except ValueError:
    print("Erreur : vous devez entrer un nombre valide")
except ZeroDivisionError:
    print("Erreur : impossible de diviser par zéro")

print("Programme terminé")
```

**Avantages** :
- Messages d'erreur plus précis pour l'utilisateur
- Meilleur contrôle sur ce qui est géré
- Code plus clair et maintenable

### Plusieurs exceptions en une seule ligne

Si vous voulez gérer plusieurs exceptions de la même manière :

```python
try:
    # Code risqué
    pass
except (ValueError, TypeError, KeyError):
    print("Une erreur s'est produite")
```

---

## Accéder aux Détails de l'Exception

Vous pouvez accéder aux informations de l'exception avec le mot-clé `as` :

```python
try:
    nombre = int(input("Entrez un nombre : "))
except ValueError as e:
    print(f"Erreur de valeur : {e}")
```

**Exemple d'utilisation** :

```python
try:
    fichier = open("inexistant.txt")
except FileNotFoundError as e:
    print(f"Impossible d'ouvrir le fichier : {e}")
```

Cela affiche le message d'erreur complet, utile pour le débogage.

---

## La Clause `else`

Le bloc `else` s'exécute **seulement si aucune exception n'a été levée** dans le `try`.

### Syntaxe

```python
try:
    # Code risqué
    pass
except ExceptionType:
    # En cas d'erreur
    pass
else:
    # Si tout s'est bien passé
    pass
```

### Exemple

```python
try:
    nombre = int(input("Entrez un nombre : "))
except ValueError:
    print("Erreur : ce n'est pas un nombre valide")
else:
    print(f"Vous avez entré : {nombre}")
    print("C'est un nombre valide !")
```

**Pourquoi utiliser else ?**

Cela permet de séparer clairement :
- Le code qui peut causer des erreurs (dans `try`)
- Le code qui ne devrait s'exécuter qu'en cas de succès (dans `else`)

### Exemple pratique : lecture de fichier

```python
try:
    fichier = open("donnees.txt", "r")
except FileNotFoundError:
    print("Le fichier n'existe pas")
else:
    contenu = fichier.read()
    print(contenu)
    fichier.close()
```

---

## La Clause `finally`

Le bloc `finally` s'exécute **toujours**, qu'il y ait eu une erreur ou non. C'est utile pour le nettoyage (fermer des fichiers, des connexions, etc.).

### Syntaxe

```python
try:
    # Code risqué
    pass
except ExceptionType:
    # Gestion d'erreur
    pass
finally:
    # S'exécute TOUJOURS
    pass
```

### Exemple : fermer un fichier

```python
fichier = None
try:
    fichier = open("donnees.txt", "r")
    contenu = fichier.read()
    print(contenu)
except FileNotFoundError:
    print("Le fichier n'existe pas")
finally:
    if fichier:
        fichier.close()
        print("Fichier fermé")
```

Le fichier sera fermé que l'opération réussisse ou non !

### Ordre d'exécution complet

```python
try:
    print("1. Dans try")
    # Code risqué
except:
    print("2. Dans except (si erreur)")
else:
    print("3. Dans else (si pas d'erreur)")
finally:
    print("4. Dans finally (toujours)")
```

**Sans erreur** :
```
1. Dans try
3. Dans else (si pas d'erreur)
4. Dans finally (toujours)
```

**Avec erreur** :
```
1. Dans try
2. Dans except (si erreur)
4. Dans finally (toujours)
```

---

## Structure Complète try/except/else/finally

Voici un exemple complet qui combine tous les éléments :

```python
def diviser_nombres():
    try:
        print("=== Calculateur de division ===")
        a = int(input("Entrez le premier nombre : "))
        b = int(input("Entrez le deuxième nombre : "))
        resultat = a / b

    except ValueError:
        print("Erreur : vous devez entrer des nombres valides")
        return None

    except ZeroDivisionError:
        print("Erreur : division par zéro impossible")
        return None

    else:
        print(f"Résultat : {a} / {b} = {resultat}")
        return resultat

    finally:
        print("Opération terminée")

# Utilisation
resultat = diviser_nombres()
if resultat:
    print(f"Résultat stocké : {resultat}")
```

---

## Lever une Exception avec `raise`

Vous pouvez **lever** (déclencher) volontairement une exception avec le mot-clé `raise`.

### Syntaxe

```python
raise TypeException("Message d'erreur")
```

### Exemples

```python
def calculer_racine_carree(nombre):
    if nombre < 0:
        raise ValueError("Impossible de calculer la racine d'un nombre négatif")

    return nombre ** 0.5

# Utilisation
try:
    resultat = calculer_racine_carree(-4)
except ValueError as e:
    print(f"Erreur : {e}")
```

### Relancer une exception

Vous pouvez capturer une exception, faire quelque chose, puis la relancer :

```python
def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Log : tentative de division par zéro")
        raise  # Relance la même exception
```

Le simple mot `raise` sans argument relance l'exception actuelle.

---

## Exceptions Courantes en Python

Voici les exceptions que vous rencontrerez le plus souvent :

### ValueError

Se produit quand une fonction reçoit un argument du bon type mais avec une valeur inappropriée.

```python
int("abc")        # ValueError
float("xyz")      # ValueError
```

### TypeError

Se produit quand une opération est appliquée à un objet d'un type inapproprié.

```python
"texte" + 5       # TypeError (str + int)
len(42)           # TypeError (int n'a pas de longueur)
```

### IndexError

Se produit lors de l'accès à un index qui n'existe pas.

```python
liste = [1, 2, 3]
element = liste[10]  # IndexError
```

### KeyError

Se produit lors de l'accès à une clé de dictionnaire inexistante.

```python
dico = {"nom": "Alice"}
age = dico["age"]  # KeyError
```

### FileNotFoundError

Se produit quand on essaie d'ouvrir un fichier qui n'existe pas.

```python
f = open("inexistant.txt")  # FileNotFoundError
```

### ZeroDivisionError

Se produit lors d'une division par zéro.

```python
resultat = 10 / 0  # ZeroDivisionError
```

### AttributeError

Se produit quand on accède à un attribut ou une méthode inexistant.

```python
texte = "Bonjour"
texte.append("!")  # AttributeError (str n'a pas de méthode append)
```

### ImportError / ModuleNotFoundError

Se produit quand un import échoue.

```python
import module_inexistant  # ModuleNotFoundError
```

---

## Créer des Exceptions Personnalisées

Vous pouvez créer vos propres types d'exceptions en héritant de la classe `Exception`.

### Syntaxe de base

```python
class MonException(Exception):
    pass
```

### Exemple simple

```python
class AgeInvalideError(Exception):
    pass

def verifier_age(age):
    if age < 0:
        raise AgeInvalideError("L'âge ne peut pas être négatif")

    if age > 150:
        raise AgeInvalideError("L'âge semble irréaliste")

    return True

# Utilisation
try:
    verifier_age(-5)
except AgeInvalideError as e:
    print(f"Erreur de validation : {e}")
```

### Exception avec attributs personnalisés

```python
class SoldeInsuffisantError(Exception):
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        message = f"Solde insuffisant : {solde}€ disponible, {montant}€ requis"
        super().__init__(message)

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError(solde, montant)
    return solde - montant

# Utilisation
try:
    nouveau_solde = retirer(100, 150)
except SoldeInsuffisantError as e:
    print(e)
    print(f"Manque : {e.montant - e.solde}€")
```

---

## Bonnes Pratiques de Gestion des Erreurs

### 1. Soyez spécifique dans vos exceptions

✅ **Bon** : Capturer des exceptions spécifiques
```python
try:
    nombre = int(input("Nombre : "))
except ValueError:
    print("Entrée invalide")
```

❌ **Mauvais** : Capturer toutes les exceptions
```python
try:
    nombre = int(input("Nombre : "))
except:  # Trop large !
    print("Erreur")
```

### 2. N'utilisez pas try/except pour le flux normal

✅ **Bon** : Vérifier avant
```python
if cle in dictionnaire:
    valeur = dictionnaire[cle]
else:
    valeur = None
```

❌ **Mauvais** : Utiliser les exceptions pour la logique normale
```python
try:
    valeur = dictionnaire[cle]
except KeyError:
    valeur = None
```

**Exception** : Le principe EAFP ("Easier to Ask for Forgiveness than Permission") est parfois préféré en Python, mais avec modération.

### 3. Ne cachez pas les erreurs

❌ **Très mauvais** : Ignorer silencieusement les erreurs
```python
try:
    # Code important
    pass
except:
    pass  # Erreur ignorée !
```

Si vous ne pouvez rien faire, au minimum loggez l'erreur :

```python
try:
    # Code
    pass
except Exception as e:
    print(f"Erreur ignorée : {e}")
```

### 4. Donnez des messages d'erreur utiles

✅ **Bon** : Message clair et actionnable
```python
except ValueError:
    print("Erreur : veuillez entrer un nombre entier (ex: 42)")
```

❌ **Mauvais** : Message vague
```python
except ValueError:
    print("Erreur")
```

### 5. Nettoyez les ressources avec finally ou with

✅ **Bon** : Utiliser with (gestionnaire de contexte)
```python
with open("fichier.txt", "r") as f:
    contenu = f.read()
# Le fichier est automatiquement fermé
```

✅ **Bon** : Utiliser finally
```python
f = None
try:
    f = open("fichier.txt", "r")
    contenu = f.read()
finally:
    if f:
        f.close()
```

❌ **Risqué** : Ne pas garantir la fermeture
```python
f = open("fichier.txt", "r")
contenu = f.read()  # Si erreur ici, le fichier reste ouvert !
f.close()
```

### 6. Documentez les exceptions dans les docstrings

```python
def diviser(a, b):
    """
    Divise a par b.

    Args:
        a (float): Le dividende
        b (float): Le diviseur

    Returns:
        float: Le résultat de la division

    Raises:
        ZeroDivisionError: Si b est égal à zéro
        TypeError: Si a ou b ne sont pas des nombres
    """
    if b == 0:
        raise ZeroDivisionError("Le diviseur ne peut pas être zéro")
    return a / b
```

---

## Hiérarchie des Exceptions

Les exceptions en Python sont organisées en hiérarchie. Voici une vue simplifiée :

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── IsADirectoryError
    └── RuntimeError
```

### Importance de la hiérarchie

Quand vous capturez une exception, vous capturez aussi toutes ses **sous-classes** :

```python
try:
    # Code
    pass
except LookupError:
    # Capture à la fois IndexError et KeyError
    print("Erreur de recherche")
```

### Ordre des blocs except

Mettez toujours les exceptions **les plus spécifiques en premier** :

✅ **Bon**
```python
try:
    # Code
    pass
except FileNotFoundError:
    print("Fichier introuvable")
except OSError:
    print("Erreur système")
except Exception:
    print("Autre erreur")
```

❌ **Mauvais** (OSError capture FileNotFoundError avant qu'il soit testé)
```python
try:
    # Code
    pass
except OSError:
    print("Erreur système")
except FileNotFoundError:  # Ne sera jamais atteint !
    print("Fichier introuvable")
```

---

## Exemples Pratiques Complets

### Exemple 1 : Saisie sécurisée d'un nombre

```python
def demander_nombre(message, min_val=None, max_val=None):
    """
    Demande un nombre à l'utilisateur avec validation.

    Args:
        message (str): Le message à afficher
        min_val (int, optional): Valeur minimale acceptée
        max_val (int, optional): Valeur maximale acceptée

    Returns:
        int: Le nombre saisi par l'utilisateur
    """
    while True:
        try:
            nombre = int(input(message))

            if min_val is not None and nombre < min_val:
                print(f"Le nombre doit être >= {min_val}")
                continue

            if max_val is not None and nombre > max_val:
                print(f"Le nombre doit être <= {max_val}")
                continue

            return nombre

        except ValueError:
            print("Erreur : veuillez entrer un nombre entier valide")
        except KeyboardInterrupt:
            print("\nOpération annulée par l'utilisateur")
            return None

# Utilisation
age = demander_nombre("Entrez votre âge : ", min_val=0, max_val=150)
if age:
    print(f"Votre âge : {age} ans")
```

### Exemple 2 : Lecture de fichier robuste

```python
def lire_fichier_securise(nom_fichier):
    """
    Lit un fichier avec gestion complète des erreurs.

    Args:
        nom_fichier (str): Chemin du fichier à lire

    Returns:
        str: Contenu du fichier ou None en cas d'erreur
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            return contenu

    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' n'existe pas")
        return None

    except PermissionError:
        print(f"Erreur : permission refusée pour '{nom_fichier}'")
        return None

    except UnicodeDecodeError:
        print(f"Erreur : encodage du fichier incompatible")
        return None

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

# Utilisation
contenu = lire_fichier_securise("donnees.txt")
if contenu:
    print(contenu)
else:
    print("Impossible de lire le fichier")
```

### Exemple 3 : Calculatrice robuste

```python
def calculatrice():
    """Calculatrice simple avec gestion des erreurs."""

    print("=== Calculatrice Simple ===")
    print("Opérations : + - * /")
    print("Tapez 'q' pour quitter")
    print()

    while True:
        try:
            # Saisie de l'expression
            expression = input("Calcul (ex: 5 + 3) : ")

            # Vérifier si l'utilisateur veut quitter
            if expression.lower() == 'q':
                print("Au revoir !")
                break

            # Découper l'expression
            parties = expression.split()

            if len(parties) != 3:
                print("Format invalide. Utilisez : nombre opérateur nombre")
                continue

            # Extraire les éléments
            nombre1 = float(parties[0])
            operateur = parties[1]
            nombre2 = float(parties[2])

            # Effectuer le calcul
            if operateur == '+':
                resultat = nombre1 + nombre2
            elif operateur == '-':
                resultat = nombre1 - nombre2
            elif operateur == '*':
                resultat = nombre1 * nombre2
            elif operateur == '/':
                if nombre2 == 0:
                    raise ZeroDivisionError("Division par zéro")
                resultat = nombre1 / nombre2
            else:
                print(f"Opérateur inconnu : {operateur}")
                continue

            print(f"Résultat : {resultat}")

        except ValueError:
            print("Erreur : les nombres doivent être valides")

        except ZeroDivisionError as e:
            print(f"Erreur : {e}")

        except KeyboardInterrupt:
            print("\n\nInterruption clavier. Au revoir !")
            break

        except Exception as e:
            print(f"Erreur inattendue : {e}")

        print()  # Ligne vide pour la lisibilité

# Lancer la calculatrice
calculatrice()
```

### Exemple 4 : Validation de données utilisateur

```python
class ValidationError(Exception):
    """Exception pour les erreurs de validation."""
    pass

def valider_email(email):
    """
    Valide un email basique.

    Args:
        email (str): L'email à valider

    Raises:
        ValidationError: Si l'email est invalide
    """
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
    """
    Valide un âge.

    Args:
        age (int): L'âge à valider

    Raises:
        ValidationError: Si l'âge est invalide
    """
    if not isinstance(age, int):
        raise ValidationError("L'âge doit être un nombre entier")

    if age < 0:
        raise ValidationError("L'âge ne peut pas être négatif")

    if age > 150:
        raise ValidationError("L'âge semble irréaliste")

def creer_utilisateur(nom, email, age):
    """
    Crée un utilisateur après validation.

    Args:
        nom (str): Nom de l'utilisateur
        email (str): Email de l'utilisateur
        age (int): Âge de l'utilisateur

    Returns:
        dict: Données de l'utilisateur si validation réussie
    """
    try:
        # Validation du nom
        if not nom or len(nom) < 2:
            raise ValidationError("Le nom doit contenir au moins 2 caractères")

        # Validation de l'email
        valider_email(email)

        # Validation de l'âge
        valider_age(age)

        # Si tout est valide, créer l'utilisateur
        utilisateur = {
            "nom": nom,
            "email": email,
            "age": age
        }

        print(f"✓ Utilisateur créé : {nom}")
        return utilisateur

    except ValidationError as e:
        print(f"✗ Erreur de validation : {e}")
        return None

# Exemples d'utilisation
print("Test 1:")
creer_utilisateur("Alice", "alice@example.com", 25)

print("\nTest 2:")
creer_utilisateur("B", "email_invalide", -5)

print("\nTest 3:")
creer_utilisateur("Charlie", "charlie@domain.com", 200)
```

### Exemple 5 : Gestionnaire de configuration

```python
import json

class ConfigError(Exception):
    """Exception pour les erreurs de configuration."""
    pass

def charger_configuration(fichier_config):
    """
    Charge une configuration depuis un fichier JSON.

    Args:
        fichier_config (str): Chemin du fichier de configuration

    Returns:
        dict: Configuration chargée

    Raises:
        ConfigError: Si la configuration est invalide
    """
    try:
        # Essayer de lire le fichier
        with open(fichier_config, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Valider les champs obligatoires
        champs_obligatoires = ['host', 'port', 'database']
        for champ in champs_obligatoires:
            if champ not in config:
                raise ConfigError(f"Champ obligatoire manquant : {champ}")

        # Valider les types
        if not isinstance(config['port'], int):
            raise ConfigError("Le port doit être un nombre entier")

        if config['port'] < 1 or config['port'] > 65535:
            raise ConfigError("Le port doit être entre 1 et 65535")

        print("✓ Configuration chargée avec succès")
        return config

    except FileNotFoundError:
        raise ConfigError(f"Fichier de configuration introuvable : {fichier_config}")

    except json.JSONDecodeError as e:
        raise ConfigError(f"Fichier JSON invalide : {e}")

    except Exception as e:
        raise ConfigError(f"Erreur lors du chargement : {e}")

# Utilisation
try:
    config = charger_configuration("config.json")
    print(f"Connexion à {config['host']}:{config['port']}")
except ConfigError as e:
    print(f"Erreur de configuration : {e}")
    print("Utilisation de la configuration par défaut")
    config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'mydb'
    }
```

---

## Le Pattern EAFP vs LBYL

Python favorise le style **EAFP** ("Easier to Ask for Forgiveness than Permission") par rapport au style **LBYL** ("Look Before You Leap").

### LBYL (Look Before You Leap)

Vérifier les conditions avant d'agir :

```python
if 'cle' in dictionnaire:
    valeur = dictionnaire['cle']
else:
    valeur = None

if os.path.exists(fichier):
    with open(fichier) as f:
        contenu = f.read()
```

### EAFP (Easier to Ask for Forgiveness than Permission)

Essayer d'abord, gérer les erreurs ensuite :

```python
try:
    valeur = dictionnaire['cle']
except KeyError:
    valeur = None

try:
    with open(fichier) as f:
        contenu = f.read()
except FileNotFoundError:
    # Gérer l'erreur
    pass
```

### Quand utiliser chaque style ?

**EAFP** est généralement préféré en Python car :
- Plus concis
- Évite les race conditions (le fichier peut être supprimé entre la vérification et l'utilisation)
- Plus "pythonique"

**LBYL** peut être préférable quand :
- La vérification est vraiment simple
- Vous voulez éviter les exceptions pour des raisons de performance
- Le code est plus lisible ainsi

---

## Erreurs Courantes à Éviter

### 1. Capturer Exception ou BaseException

❌ **Mauvais**
```python
try:
    # Code
    pass
except Exception:  # Trop large
    pass
```

Cela capture presque tout, y compris des erreurs que vous ne devriez pas ignorer.

### 2. Bloc except vide

❌ **Très mauvais**
```python
try:
    # Code
    pass
except:
    pass  # Erreur complètement ignorée !
```

Au minimum, loggez l'erreur.

### 3. Ne pas relancer les exceptions importantes

❌ **Problématique**
```python
try:
    # Code critique
    pass
except Exception as e:
    print(f"Erreur : {e}")
    # L'erreur est loggée mais le programme continue
    # alors qu'il devrait peut-être s'arrêter
```

### 4. Utiliser try/except pour le flux normal

❌ **Anti-pattern**
```python
def obtenir_premier_element(liste):
    try:
        return liste[0]
    except IndexError:
        return None
```

✅ **Mieux**
```python
def obtenir_premier_element(liste):
    return liste[0] if liste else None
```

### 5. Oublier finally pour le nettoyage

❌ **Risqué**
```python
f = open("fichier.txt")
try:
    # Traitement
    pass
except:
    # Gestion d'erreur
    pass
f.close()  # Ne sera pas exécuté si erreur dans except !
```

✅ **Correct**
```python
f = open("fichier.txt")
try:
    # Traitement
    pass
except:
    # Gestion d'erreur
    pass
finally:
    f.close()  # Toujours exécuté
```

---

## Assertions pour le Débogage

Les **assertions** permettent de vérifier des conditions qui devraient toujours être vraies. Si la condition est fausse, une `AssertionError` est levée.

### Syntaxe

```python
assert condition, "Message d'erreur optionnel"
```

### Exemples

```python
def diviser(a, b):
    assert b != 0, "Le diviseur ne peut pas être zéro"
    return a / b

def calculer_moyenne(notes):
    assert len(notes) > 0, "La liste ne peut pas être vide"
    return sum(notes) / len(notes)

age = 25
assert 0 <= age <= 150, "Âge invalide"
```

### Quand utiliser assert ?

✅ **Bon usage** : Vérifier des conditions internes, bugs de programmation
```python
def process(data):
    assert isinstance(data, list), "data doit être une liste"
    # Suite du traitement
```

❌ **Mauvais usage** : Valider les entrées utilisateur
```python
# Ne PAS faire cela
age = int(input("Âge : "))
assert age >= 0, "Âge invalide"  # Les assertions peuvent être désactivées !
```

**Important** : Les assertions peuvent être désactivées avec `python -O script.py`, donc ne les utilisez **jamais** pour valider des données externes ou utilisateur.

---

## Récapitulatif

Dans cette section, nous avons appris :

✅ **Types d'erreurs** : Syntaxe vs Exceptions
✅ **try/except** : Capturer et gérer les exceptions
✅ **Exceptions spécifiques** : ValueError, TypeError, etc.
✅ **else** : Code à exécuter si pas d'erreur
✅ **finally** : Code toujours exécuté (nettoyage)
✅ **raise** : Lever des exceptions volontairement
✅ **Exceptions personnalisées** : Créer ses propres types d'erreurs
✅ **Hiérarchie des exceptions** : Comprendre l'héritage
✅ **Bonnes pratiques** : Code robuste et maintenable
✅ **EAFP vs LBYL** : Deux philosophies de programmation
✅ **Assertions** : Vérifications pour le débogage

---

## Points Clés à Retenir

1. **Les exceptions permettent une gestion élégante des erreurs** : le programme peut continuer
2. **Soyez spécifique dans vos except** : ne capturez que ce que vous pouvez gérer
3. **finally garantit le nettoyage** : fermer des fichiers, libérer des ressources
4. **raise permet de signaler des erreurs** : créez des exceptions claires et descriptives
5. **Documentez les exceptions** : indiquez dans les docstrings ce qui peut être levé
6. **Ne cachez pas les erreurs** : loggez au minimum ce qui se passe
7. **Python favorise EAFP** : essayez d'abord, gérez les erreurs ensuite
8. **Les assertions sont pour le débogage** : pas pour valider les entrées utilisateur

---

## Pour Aller Plus Loin

Avec la gestion des erreurs, vous pouvez maintenant :
- Créer des programmes robustes qui ne plantent pas au moindre problème
- Donner un feedback clair à vos utilisateurs
- Déboguer plus facilement en comprenant où et pourquoi les erreurs se produisent
- Écrire du code professionnel et maintenable

La gestion des erreurs est un signe de maturité en programmation. Un débutant ignore les erreurs ou laisse le programme planter. Un programmeur expérimenté anticipe les problèmes et les gère élégamment !

---

Vous maîtrisez maintenant la gestion des erreurs ! Dans la prochaine section, nous approfondirons les annotations de types (Type Hints) pour rendre votre code encore plus clair et robuste.


⏭️ [Type Hints et annotations de types](/01-fondamentaux-et-syntaxe/06-type-hints-et-annotations.md)
