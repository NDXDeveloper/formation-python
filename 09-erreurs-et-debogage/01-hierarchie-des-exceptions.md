🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.1 Hiérarchie des exceptions

## Introduction aux exceptions

Une **exception** est un événement qui se produit pendant l'exécution d'un programme et qui perturbe son fonctionnement normal. En Python, lorsqu'une erreur se produit, le programme lève (raise) une exception.

### Exemple simple d'exception

```python
# Tentative de division par zéro
resultat = 10 / 0
# Cela provoque une ZeroDivisionError
```

Quand Python rencontre cette erreur, il affiche un message similaire à :
```
ZeroDivisionError: division by zero
```

## Pourquoi une hiérarchie ?

Python organise toutes ses exceptions dans une **hiérarchie** sous forme d'arbre. Cela signifie que :
- Toutes les exceptions héritent d'une classe de base
- Certaines exceptions sont des cas spécifiques d'exceptions plus générales
- On peut capturer une exception parent pour gérer toutes ses exceptions enfants

## La hiérarchie des exceptions Python

Voici la structure principale de la hiérarchie des exceptions en Python :

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── FloatingPointError
    │   └── OverflowError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── RuntimeError
    │   ├── NotImplementedError
    │   └── RecursionError
    ├── StopIteration
    ├── StopAsyncIteration
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    └── Warning
        ├── DeprecationWarning
        ├── UserWarning
        └── FutureWarning
```

## Les exceptions les plus courantes

### 1. **BaseException** - La racine de tout

`BaseException` est la classe parente de toutes les exceptions en Python. En pratique, on ne capture jamais directement `BaseException` car cela intercepterait même les interruptions système.

### 2. **Exception** - La base pour les erreurs standards

`Exception` est la classe parente de toutes les exceptions non-système. **C'est celle que vous devez utiliser** pour créer vos propres exceptions.

```python
try:
    # Votre code
    pass
except Exception as e:
    # Capture toutes les exceptions standards
    print(f"Une erreur s'est produite : {e}")
```

### 3. **ArithmeticError** - Erreurs mathématiques

Classe parente des erreurs liées aux opérations mathématiques.

#### ZeroDivisionError
Se produit lors d'une division par zéro.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Impossible de diviser par zéro !")
```

#### OverflowError
Se produit quand un calcul dépasse la limite numérique.

```python
import math
try:
    resultat = math.exp(1000)  # Trop grand !
except OverflowError:
    print("Le nombre est trop grand !")
```

### 4. **LookupError** - Erreurs de recherche

Classe parente des erreurs lors de l'accès à des éléments dans une collection.

#### IndexError
Se produit quand on accède à un index qui n'existe pas dans une liste.

```python
ma_liste = [1, 2, 3]
try:
    element = ma_liste[10]  # Index 10 n'existe pas
except IndexError:
    print("Cet index n'existe pas dans la liste !")
```

#### KeyError
Se produit quand on accède à une clé qui n'existe pas dans un dictionnaire.

```python
mon_dict = {"nom": "Alice", "age": 30}
try:
    ville = mon_dict["ville"]  # La clé "ville" n'existe pas
except KeyError:
    print("Cette clé n'existe pas dans le dictionnaire !")
```

### 5. **TypeError** - Erreur de type

Se produit quand une opération est appliquée à un type inapproprié.

```python
try:
    resultat = "hello" + 5  # On ne peut pas additionner une chaîne et un nombre
except TypeError:
    print("Types incompatibles pour cette opération !")
```

### 6. **ValueError** - Erreur de valeur

Se produit quand une fonction reçoit un argument du bon type mais avec une valeur inappropriée.

```python
try:
    nombre = int("abc")  # "abc" n'est pas un nombre valide
except ValueError:
    print("Impossible de convertir cette chaîne en nombre !")
```

### 7. **NameError** - Nom non défini

Se produit quand on utilise une variable qui n'a pas été définie.

```python
try:
    print(variable_inexistante)
except NameError:
    print("Cette variable n'existe pas !")
```

### 8. **AttributeError** - Attribut inexistant

Se produit quand on essaie d'accéder à un attribut qui n'existe pas sur un objet.

```python
ma_liste = [1, 2, 3]
try:
    ma_liste.append_all([4, 5])  # Cette méthode n'existe pas
except AttributeError:
    print("Cet attribut ou cette méthode n'existe pas !")
```

### 9. **OSError** et ses sous-classes - Erreurs système

#### FileNotFoundError
Se produit quand on essaie d'ouvrir un fichier qui n'existe pas.

```python
try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé !")
```

#### PermissionError
Se produit quand on n'a pas les permissions nécessaires.

```python
try:
    with open("/root/fichier_protege.txt", "w") as f:
        f.write("Test")
except PermissionError:
    print("Vous n'avez pas la permission d'accéder à ce fichier !")
```

### 10. **ImportError** et **ModuleNotFoundError**

Se produisent lors de problèmes d'importation de modules.

```python
try:
    import module_inexistant
except ModuleNotFoundError:
    print("Ce module n'est pas installé !")
```

## Capturer plusieurs niveaux d'exceptions

Grâce à la hiérarchie, vous pouvez capturer des exceptions à différents niveaux de spécificité.

### Exemple 1 : Capture spécifique

```python
try:
    nombre = int(input("Entrez un nombre : "))
    resultat = 10 / nombre
except ValueError:
    print("Vous devez entrer un nombre valide !")
except ZeroDivisionError:
    print("Le nombre ne peut pas être zéro !")
```

### Exemple 2 : Capture par parent

```python
try:
    nombre = int(input("Entrez un nombre : "))
    resultat = 10 / nombre
except ArithmeticError:
    # Capture ZeroDivisionError, OverflowError, etc.
    print("Erreur mathématique !")
except ValueError:
    print("Valeur invalide !")
```

### Exemple 3 : Capture multiple avec tuple

```python
try:
    # Votre code
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"Une erreur courante s'est produite : {e}")
```

## Bonnes pratiques

### ✅ À FAIRE

1. **Capturer des exceptions spécifiques**
```python
try:
    fichier = open("data.txt")
except FileNotFoundError:
    print("Le fichier n'existe pas")
```

2. **Utiliser plusieurs blocs except pour différents cas**
```python
try:
    resultat = operation_risquee()
except ValueError:
    print("Erreur de valeur")
except TypeError:
    print("Erreur de type")
```

3. **Capturer l'exception pour l'utiliser**
```python
try:
    nombre = int(input("Nombre : "))
except ValueError as e:
    print(f"Erreur : {e}")
```

### ❌ À ÉVITER

1. **Capturer Exception sans raison**
```python
# Trop général !
try:
    code_complexe()
except Exception:
    pass  # On ne sait pas ce qui s'est passé
```

2. **Capturer BaseException**
```python
# Ne faites JAMAIS ça !
try:
    mon_code()
except BaseException:
    pass  # Cela capture même Ctrl+C !
```

3. **Ignorer silencieusement les erreurs**
```python
# Mauvaise pratique
try:
    operation_importante()
except:
    pass  # L'erreur est perdue !
```

## Ordre de capture des exceptions

L'ordre des blocs `except` est important ! Python teste les exceptions dans l'ordre où elles sont écrites.

### ❌ Mauvais ordre

```python
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[10])
except LookupError:
    print("Erreur de recherche")  # Sera capturé ici
except IndexError:
    print("Index invalide")  # Ne sera JAMAIS atteint !
```

### ✅ Bon ordre

```python
try:
    ma_liste = [1, 2, 3]
    print(ma_liste[10])
except IndexError:
    print("Index invalide")  # Plus spécifique en premier
except LookupError:
    print("Erreur de recherche")  # Plus général ensuite
```

## Résumé

- Toutes les exceptions Python sont organisées en hiérarchie
- `BaseException` est la racine, mais on hérite généralement d'`Exception`
- Les exceptions enfants sont des cas spécifiques d'exceptions parents
- Capturer une exception parent capture aussi toutes ses exceptions enfants
- Toujours mettre les exceptions les plus spécifiques en premier
- Évitez de capturer des exceptions trop générales sans bonne raison

---

Dans la prochaine section, nous verrons comment créer nos propres exceptions personnalisées en héritant de la classe `Exception`.

⏭️ [Création d'exceptions personnalisées](/09-erreurs-et-debogage/02-exceptions-personnalisees.md)
