🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.1 : Hiérarchie des exceptions

## Introduction

Imaginez que vous cuisinez et que quelque chose ne va pas : vous pourriez manquer d'ingrédients, brûler le plat, ou casser un ustensile. Dans chaque cas, vous réagissez différemment selon le type de problème. C'est exactement la même chose en programmation avec les exceptions !

En Python, les exceptions sont organisées dans une hiérarchie, comme un arbre généalogique. Comprendre cette organisation vous permettra de gérer les erreurs de manière précise et efficace.

## Qu'est-ce qu'une exception ?

Une **exception** est un événement qui interrompt le cours normal d'exécution d'un programme. Quand Python rencontre une situation qu'il ne peut pas gérer, il "lève" (raise) une exception.

### Exemple simple
```python
# Ceci va provoquer une exception
nombre = 10 / 0  # Division par zéro !
```

Résultat :
```
ZeroDivisionError: division by zero
```

## La hiérarchie des exceptions Python

Toutes les exceptions Python héritent d'une classe de base appelée `BaseException`. Voici la structure principale :

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── ValueError
    ├── TypeError
    ├── NameError
    └── ... (et bien d'autres)
```

## Les exceptions les plus courantes

### 1. ValueError
Se produit quand une fonction reçoit un argument du bon type mais avec une valeur inappropriée.

```python
# Exemple : convertir une chaîne non-numérique en nombre
try:
    nombre = int("hello")
except ValueError as e:
    print(f"Erreur : {e}")
    print("Impossible de convertir 'hello' en nombre")
```

### 2. TypeError
Se produit quand une opération est effectuée sur un type incorrect.

```python
# Exemple : additionner un nombre et une chaîne
try:
    resultat = 5 + "3"
except TypeError as e:
    print(f"Erreur : {e}")
    print("On ne peut pas additionner un nombre et une chaîne directement")
```

### 3. IndexError
Se produit quand on essaie d'accéder à un index qui n'existe pas.

```python
# Exemple : accéder à un élément inexistant d'une liste
ma_liste = [1, 2, 3]
try:
    element = ma_liste[10]  # La liste n'a que 3 éléments !
except IndexError as e:
    print(f"Erreur : {e}")
    print("L'index 10 n'existe pas dans cette liste")
```

### 4. KeyError
Se produit quand on essaie d'accéder à une clé qui n'existe pas dans un dictionnaire.

```python
# Exemple : accéder à une clé inexistante
mon_dict = {"nom": "Alice", "age": 30}
try:
    ville = mon_dict["ville"]
except KeyError as e:
    print(f"Erreur : {e}")
    print("La clé 'ville' n'existe pas dans ce dictionnaire")
```

### 5. FileNotFoundError
Se produit quand on essaie d'ouvrir un fichier qui n'existe pas.

```python
# Exemple : ouvrir un fichier inexistant
try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError as e:
    print(f"Erreur : {e}")
    print("Le fichier demandé n'existe pas")
```

## Avantages de la hiérarchie

### 1. Capture spécifique vs capture générale

Grâce à la hiérarchie, vous pouvez capturer des exceptions à différents niveaux :

```python
def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro")
        return None
    except ArithmeticError:
        print("Erreur : Problème arithmétique")
        return None
    except Exception:
        print("Erreur : Problème inattendu")
        return None

# Tests
print(diviser(10, 2))    # 5.0
print(diviser(10, 0))    # Erreur : Division par zéro
```

### 2. Capture de familles d'exceptions

```python
def acceder_element(collection, cle_ou_index):
    try:
        return collection[cle_ou_index]
    except LookupError:  # Capture IndexError ET KeyError
        print("Élément introuvable")
        return None

# Tests
ma_liste = [1, 2, 3]
mon_dict = {"a": 1, "b": 2}

print(acceder_element(ma_liste, 1))    # 2
print(acceder_element(ma_liste, 10))   # Élément introuvable
print(acceder_element(mon_dict, "a"))  # 1
print(acceder_element(mon_dict, "z"))  # Élément introuvable
```

## Bonnes pratiques

### 1. Capturer les exceptions spécifiques d'abord

```python
# ✅ Bon : du spécifique au général
try:
    fichier = open("data.txt")
    nombre = int(fichier.readline())
    resultat = 100 / nombre
except FileNotFoundError:
    print("Fichier non trouvé")
except ValueError:
    print("Contenu du fichier invalide")
except ZeroDivisionError:
    print("Division par zéro")
except Exception as e:
    print(f"Erreur inattendue : {e}")
```

### 2. Éviter les captures trop générales

```python
# ❌ Mauvais : capture tout sans distinction
try:
    # du code complexe
    pass
except Exception:
    pass  # On ignore tout !

# ✅ Meilleur : capturer spécifiquement
try:
    # du code complexe
    pass
except ValueError:
    print("Problème avec les valeurs")
except TypeError:
    print("Problème avec les types")
```

### 3. Utiliser les informations de l'exception

```python
def lire_fichier_config(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Fichier de configuration manquant : {e.filename}")
        return None
    except PermissionError:
        print("Permissions insuffisantes pour lire le fichier")
        return None
    except OSError as e:
        print(f"Erreur système : {e}")
        return None

# Test
config = lire_fichier_config("config.txt")
```

## Exercices pratiques

### Exercice 1 : Identification d'exceptions
Identifiez quel type d'exception sera levé dans chaque cas :

```python
# Cas 1
liste = [1, 2, 3]
print(liste[5])  # Quelle exception ?

# Cas 2
dictionnaire = {"nom": "Alice"}
print(dictionnaire["age"])  # Quelle exception ?

# Cas 3
nombre = int("abc")  # Quelle exception ?

# Cas 4
resultat = "hello" + 5  # Quelle exception ?
```

### Exercice 2 : Gestion d'exceptions
Créez une fonction qui gère les erreurs de manière appropriée :

```python
def calculatrice_simple(a, b, operation):
    """
    Effectue une opération simple entre deux nombres.
    Gérez les erreurs possibles !
    """
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            raise ValueError("Opération non supportée")
    except ZeroDivisionError:
        return "Erreur : Division par zéro"
    except TypeError:
        return "Erreur : Types incorrects"
    except ValueError as e:
        return f"Erreur : {e}"

# Tests
print(calculatrice_simple(10, 2, "/"))     # 5.0
print(calculatrice_simple(10, 0, "/"))     # Erreur : Division par zéro
print(calculatrice_simple(10, "2", "+"))   # Erreur : Types incorrects
print(calculatrice_simple(10, 2, "^"))     # Erreur : Opération non supportée
```

## Résumé

La hiérarchie des exceptions Python est organisée comme un arbre :
- **BaseException** est la racine
- **Exception** est la classe de base pour la plupart des exceptions
- Les exceptions spécifiques héritent d'exceptions plus générales

**Points clés à retenir :**
1. Capturez les exceptions spécifiques avant les générales
2. Utilisez la hiérarchie pour grouper les exceptions similaires
3. Évitez les captures trop générales qui masquent les problèmes
4. Exploitez les informations contenues dans les exceptions

Cette compréhension de la hiérarchie vous permettra de créer des programmes plus robustes et plus faciles à déboguer. Dans la section suivante, nous verrons comment créer nos propres exceptions personnalisées !

---

**À retenir :** Les exceptions sont comme des signaux d'alarme spécialisés. Plus vous savez les reconnaître et les gérer, plus vos programmes seront fiables et professionnels.

⏭️
