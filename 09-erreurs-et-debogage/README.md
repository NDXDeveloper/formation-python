🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9. Gestion des erreurs et débogage

## Introduction au chapitre

Bienvenue dans ce chapitre essentiel sur la gestion des erreurs et le débogage en Python ! Même les programmeurs les plus expérimentés rencontrent des erreurs dans leur code. La différence réside dans leur capacité à comprendre, gérer et corriger ces erreurs efficacement.

Dans ce chapitre, nous allons apprendre à :
- Comprendre les différents types d'erreurs en Python
- Gérer les erreurs de manière élégante avec try/except
- Créer nos propres exceptions personnalisées
- Utiliser les outils de débogage pour trouver et corriger les bugs
- Optimiser notre code pour le rendre plus performant

---

## Qu'est-ce qu'une erreur ?

### Les différents types d'erreurs

En programmation, on distingue généralement trois types d'erreurs :

#### 1. Les erreurs de syntaxe (Syntax Errors)

Ce sont des erreurs dans la structure même du code. Python ne peut pas comprendre ce que vous avez écrit.

```python
# Erreur : oubli des deux-points
if x > 5
    print("x est grand")

# Message d'erreur :
# SyntaxError: invalid syntax
```

**Caractéristiques :**
- Le programme ne peut pas s'exécuter du tout
- Détectées avant l'exécution du code
- Faciles à repérer grâce aux messages d'erreur clairs

**Exemples courants :**
```python
# Oubli de fermer une parenthèse
print("Bonjour"

# Oubli de guillemets
texte = Bonjour

# Mauvaise indentation
def ma_fonction():  
print("Hello")  # Erreur : devrait être indenté  
```

#### 2. Les erreurs d'exécution (Runtime Errors / Exceptions)

Le code est syntaxiquement correct, mais une erreur se produit pendant l'exécution.

```python
# Le code est valide, mais...
nombre = int(input("Entrez un nombre : "))  # Si l'utilisateur tape "abc"
# ValueError: invalid literal for int() with base 10: 'abc'

# Division par zéro
resultat = 10 / 0
# ZeroDivisionError: division by zero

# Accès à un index inexistant
liste = [1, 2, 3]  
element = liste[10]  
# IndexError: list index out of range
```

**Caractéristiques :**
- Le programme démarre normalement
- L'erreur survient à un moment précis pendant l'exécution
- Peuvent être gérées avec try/except
- Appelées "exceptions" en Python

#### 3. Les erreurs logiques (Logic Errors / Bugs)

Le code s'exécute sans erreur, mais ne fait pas ce que vous vouliez.

```python
# Erreur logique : calcul incorrect de la moyenne
def calculer_moyenne(notes):
    total = sum(notes)
    # BUG : division par le mauvais nombre
    moyenne = total / (len(notes) + 1)  # Devrait être len(notes)
    return moyenne

notes = [15, 16, 14]  
print(calculer_moyenne(notes))  # Résultat incorrect : 11.25 au lieu de 15  
```

**Caractéristiques :**
- Aucun message d'erreur
- Le programme s'exécute "normalement"
- Les plus difficiles à détecter
- Nécessitent du débogage et des tests

---

## Pourquoi gérer les erreurs ?

### 1. Éviter les plantages du programme

Sans gestion des erreurs, votre programme s'arrête brutalement :

```python
# ❌ Sans gestion d'erreur
def diviser(a, b):
    return a / b

print(diviser(10, 2))   # ✅ Fonctionne : 5.0  
print(diviser(10, 0))   # ❌ CRASH ! Le programme s'arrête  
print("Cette ligne ne s'exécutera jamais")  
```

Avec gestion des erreurs, le programme continue :

```python
# ✅ Avec gestion d'erreur
def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : division par zéro impossible")
        return None

print(diviser(10, 2))   # ✅ 5.0  
print(diviser(10, 0))   # ✅ Affiche un message, retourne None  
print("Le programme continue normalement")  # ✅ Cette ligne s'exécute !  
```

### 2. Fournir des messages d'erreur utiles

Comparez ces deux approches :

```python
# ❌ Message d'erreur cryptique pour l'utilisateur
age = int(input("Votre âge : "))  # Si l'utilisateur tape "vingt"
# ValueError: invalid literal for int() with base 10: 'vingt'
# L'utilisateur ne comprend pas ce message !

# ✅ Message clair et compréhensible
try:
    age = int(input("Votre âge : "))
except ValueError:
    print("❌ Erreur : Veuillez entrer un nombre valide (exemple : 25)")
```

### 3. Déboguer plus facilement

Une bonne gestion des erreurs aide à identifier les problèmes :

```python
def traiter_donnees(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            donnees = f.read()
        return donnees
    except FileNotFoundError:
        print(f"❌ Le fichier '{fichier}' n'existe pas")
    except PermissionError:
        print(f"❌ Pas de permission pour lire '{fichier}'")
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
```

### 4. Créer des applications robustes

Une application professionnelle doit être résiliente :

```python
def programme_robuste():
    """Programme qui ne plante jamais."""
    while True:
        try:
            choix = input("\nQue voulez-vous faire ? (1: Calculer, 2: Quitter) : ")

            if choix == "1":
                nombre = float(input("Entrez un nombre : "))
                resultat = nombre ** 2
                print(f"Résultat : {resultat}")
            elif choix == "2":
                print("Au revoir !")
                break
            else:
                print("Choix invalide")

        except ValueError:
            print("❌ Veuillez entrer un nombre valide")
        except KeyboardInterrupt:
            print("\n⚠️ Programme interrompu par l'utilisateur")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
```

---

## Les exceptions en Python - Vue d'ensemble

### Qu'est-ce qu'une exception ?

Une **exception** est un événement qui se produit pendant l'exécution d'un programme et qui perturbe le flux normal des instructions.

Quand une exception se produit :
1. Python arrête l'exécution normale
2. Cherche un gestionnaire d'exception (bloc try/except)
3. Si trouvé : exécute le code de gestion
4. Si non trouvé : le programme plante avec un message d'erreur

### La syntaxe de base : try/except

```python
try:
    # Code qui pourrait causer une erreur
    nombre = int(input("Entrez un nombre : "))
    resultat = 100 / nombre
    print(f"Résultat : {resultat}")

except ValueError:
    # Gérer les erreurs de conversion
    print("❌ Ce n'est pas un nombre valide")

except ZeroDivisionError:
    # Gérer la division par zéro
    print("❌ Division par zéro impossible")
```

### Les exceptions les plus courantes

Voici un aperçu des exceptions que vous rencontrerez le plus souvent :

```python
# 1. ValueError - Valeur inappropriée
int("abc")  # ValueError

# 2. TypeError - Type de données incorrect
"texte" + 5  # TypeError

# 3. NameError - Variable non définie
print(variable_inexistante)  # NameError

# 4. IndexError - Index hors limites
liste = [1, 2, 3]  
liste[10]  # IndexError  

# 5. KeyError - Clé inexistante dans un dictionnaire
personne = {"nom": "Alice"}  
personne["age"]  # KeyError  

# 6. AttributeError - Attribut inexistant
texte = "Bonjour"  
texte.append("!")  # AttributeError (les strings n'ont pas de méthode append)  

# 7. FileNotFoundError - Fichier introuvable
open("fichier_inexistant.txt")  # FileNotFoundError

# 8. ZeroDivisionError - Division par zéro
10 / 0  # ZeroDivisionError

# 9. ImportError - Module introuvable
import module_inexistant  # ImportError

# 10. IndentationError - Problème d'indentation
def fonction():  
print("bug")  # IndentationError  
```

---

## Anatomie d'un message d'erreur

Comprendre les messages d'erreur est crucial pour déboguer efficacement. Analysons un message typique :

```python
def calculer(x, y):
    resultat = x / y
    return resultat

def programme_principal():
    valeur = calculer(10, 0)
    print(valeur)

programme_principal()
```

**Message d'erreur complet :**

```
Traceback (most recent call last):
  File "mon_script.py", line 8, in <module>
    programme_principal()
  File "mon_script.py", line 6, in programme_principal
    valeur = calculer(10, 0)
  File "mon_script.py", line 2, in calculer
    resultat = x / y
ZeroDivisionError: division by zero
```

### Décoder le message

**1. "Traceback (most recent call last):"**
- Indique le début de la trace d'exécution
- Liste les appels de fonctions qui ont mené à l'erreur

**2. La pile d'appels (call stack) - de bas en haut :**
```
File "mon_script.py", line 8, in <module>
    programme_principal()
```
- Le programme a commencé ici (ligne 8)
- A appelé `programme_principal()`

```
File "mon_script.py", line 6, in programme_principal
    valeur = calculer(10, 0)
```
- À l'intérieur de `programme_principal` (ligne 6)
- A appelé `calculer(10, 0)`

```
File "mon_script.py", line 2, in calculer
    resultat = x / y
```
- À l'intérieur de `calculer` (ligne 2)
- C'est ici que l'erreur s'est produite !

**3. Le type et le message d'erreur :**
```
ZeroDivisionError: division by zero
```
- **ZeroDivisionError** : Type d'exception
- **division by zero** : Description de l'erreur

### Comment lire la trace

**Lisez de bas en haut pour comprendre le contexte :**
1. ⬆️ Remontez pour voir d'où vient l'appel
2. 🔍 La dernière ligne indique exactement où l'erreur s'est produite
3. 📍 Les numéros de ligne vous guident vers le code problématique

**Exemple pratique avec annotations :**

```python
# Exemple avec plusieurs niveaux d'appels
def niveau_3(x):
    return 10 / x  # ← L'ERREUR SE PRODUIT ICI

def niveau_2(x):
    return niveau_3(x)  # ← Appelé depuis ici

def niveau_1():
    return niveau_2(0)  # ← Appelé depuis ici

niveau_1()  # ← Le programme démarre ici
```

---

## Les blocs try/except - Introduction

### Structure de base

```python
try:
    # Code qui pourrait générer une erreur
    code_risque()
except TypeException:
    # Code exécuté si une erreur de ce type se produit
    gerer_erreur()
```

### Exemple simple

```python
# Demander l'âge de l'utilisateur
try:
    age = int(input("Quel est votre âge ? "))
    print(f"Vous avez {age} ans")
except ValueError:
    print("❌ Veuillez entrer un nombre valide")
```

### Capturer plusieurs types d'exceptions

```python
try:
    fichier = input("Nom du fichier : ")
    with open(fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
    nombre = int(contenu)
    resultat = 100 / nombre

except FileNotFoundError:
    print("❌ Le fichier n'existe pas")
except ValueError:
    print("❌ Le contenu du fichier n'est pas un nombre")
except ZeroDivisionError:
    print("❌ Le nombre ne peut pas être zéro")
```

### Le bloc else (exécuté si aucune erreur)

```python
try:
    nombre = int(input("Entrez un nombre : "))
except ValueError:
    print("❌ Ce n'est pas un nombre valide")
else:
    # Exécuté seulement si aucune exception n'est levée
    print(f"✅ Vous avez entré le nombre {nombre}")
    carre = nombre ** 2
    print(f"Son carré est {carre}")
```

### Le bloc finally (toujours exécuté)

```python
try:
    fichier = open("donnees.txt", 'r', encoding='utf-8')
    contenu = fichier.read()
    print(contenu)
except FileNotFoundError:
    print("❌ Fichier introuvable")
finally:
    # Ce bloc s'exécute TOUJOURS, qu'il y ait eu une erreur ou non
    print("🔒 Fermeture des ressources...")
    try:
        fichier.close()
    except:
        pass  # Le fichier n'était pas ouvert
```

### Structure complète

```python
try:
    # Code qui pourrait générer une erreur
    resultat = operation_risquee()

except TypeErreur1:
    # Gestion de l'erreur de type 1
    traiter_erreur_1()

except TypeErreur2:
    # Gestion de l'erreur de type 2
    traiter_erreur_2()

else:
    # Exécuté si aucune exception n'est levée
    print("✅ Opération réussie")

finally:
    # Toujours exécuté, qu'il y ait eu une erreur ou non
    nettoyer_ressources()
```

---

## Bonnes pratiques de base

### 1. Soyez spécifique dans vos exceptions

```python
# ❌ Mauvais : trop général
try:
    resultat = fonction_complexe()
except:  # Capture TOUTES les exceptions
    print("Une erreur s'est produite")

# ✅ Bon : spécifique
try:
    resultat = fonction_complexe()
except ValueError:
    print("Erreur de valeur")
except TypeError:
    print("Erreur de type")
```

### 2. Ne cachez pas les erreurs

```python
# ❌ Mauvais : erreur silencieuse
try:
    operation_importante()
except:
    pass  # L'erreur est ignorée, impossible à déboguer !

# ✅ Bon : au moins logger l'erreur
try:
    operation_importante()
except Exception as e:
    print(f"⚠️ Erreur lors de l'opération : {e}")
    # Ou utiliser logging.error(e)
```

### 3. Fournissez des messages d'erreur utiles

```python
# ❌ Mauvais : message vague
try:
    age = int(input("Âge : "))
except ValueError:
    print("Erreur")

# ✅ Bon : message clair et actionnable
try:
    age = int(input("Âge : "))
except ValueError:
    print("❌ L'âge doit être un nombre entier (exemple : 25)")
```

### 4. Gérez les erreurs au bon niveau

```python
# ✅ Bon : gestion proche de l'utilisateur
def calculer_moyenne(notes):
    """Fonction de calcul pure, pas de gestion d'erreur."""
    return sum(notes) / len(notes)

def interface_utilisateur():
    """Gestion des erreurs au niveau de l'interface."""
    try:
        notes = [float(x) for x in input("Notes (séparées par des espaces) : ").split()]
        moyenne = calculer_moyenne(notes)
        print(f"✅ Moyenne : {moyenne:.2f}")
    except ValueError:
        print("❌ Toutes les notes doivent être des nombres")
    except ZeroDivisionError:
        print("❌ Vous devez entrer au moins une note")
```

---

## Quand utiliser la gestion des erreurs ?

### ✅ Utilisez try/except pour :

1. **Les entrées utilisateur**
```python
try:
    age = int(input("Votre âge : "))
except ValueError:
    print("Veuillez entrer un nombre")
```

2. **Les opérations sur les fichiers**
```python
try:
    with open("config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Fichier de configuration introuvable")
```

3. **Les opérations réseau**
```python
try:
    response = requests.get("https://api.example.com/data")
except requests.ConnectionError:
    print("Impossible de se connecter au serveur")
```

4. **Les conversions de données**
```python
try:
    nombre = float(valeur)
except ValueError:
    print("Conversion impossible")
```

### ❌ N'utilisez PAS try/except pour :

1. **La logique normale du programme**
```python
# ❌ Mauvais : utiliser les exceptions pour le contrôle de flux
try:
    valeur = dictionnaire[cle]
except KeyError:
    valeur = None

# ✅ Bon : utiliser des conditions
valeur = dictionnaire.get(cle)
```

2. **Masquer les bugs**
```python
# ❌ Mauvais : cache les vrais problèmes
try:
    fonction_avec_bug()
except:
    pass  # Ignore tous les problèmes !

# ✅ Bon : laissez les bugs apparaître pendant le développement
fonction_avec_bug()  # Si elle plante, c'est qu'il y a un bug à corriger
```

---

## Aperçu du chapitre

Dans ce chapitre, nous allons explorer en profondeur :

### 9.1 Hiérarchie des exceptions
- La structure complète des exceptions Python
- Les classes d'exceptions et leur héritage
- Comment choisir la bonne exception

### 9.2 Création d'exceptions personnalisées
- Définir vos propres classes d'exception
- Bonnes pratiques pour les exceptions custom
- Exemples d'utilisation

### 9.3 Techniques de débogage
- Utiliser print() efficacement
- Le module pdb (Python Debugger)
- Les outils de débogage des IDE
- Stratégies de débogage

### 9.4 Profiling et optimisation
- Mesurer les performances avec timeit
- Profiling avec cProfile
- Identifier les goulots d'étranglement
- Techniques d'optimisation

---

## Exemple pratique complet

Pour terminer cette introduction, voici un exemple qui met en pratique les concepts abordés :

```python
def calculatrice_robuste():
    """
    Une calculatrice simple mais robuste qui gère toutes les erreurs.
    """
    print("=" * 50)
    print("CALCULATRICE PYTHON")
    print("=" * 50)

    while True:
        try:
            # Afficher le menu
            print("\nOpérations disponibles :")
            print("  1. Addition")
            print("  2. Soustraction")
            print("  3. Multiplication")
            print("  4. Division")
            print("  5. Quitter")

            # Demander l'opération
            choix = input("\nChoisissez une opération (1-5) : ")

            # Option quitter
            if choix == "5":
                print("👋 Au revoir !")
                break

            # Vérifier que le choix est valide
            if choix not in ["1", "2", "3", "4"]:
                print("❌ Choix invalide. Choisissez entre 1 et 5.")
                continue

            # Demander les nombres
            nombre1 = float(input("Premier nombre : "))
            nombre2 = float(input("Deuxième nombre : "))

            # Effectuer l'opération
            if choix == "1":
                resultat = nombre1 + nombre2
                operation = "+"
            elif choix == "2":
                resultat = nombre1 - nombre2
                operation = "-"
            elif choix == "3":
                resultat = nombre1 * nombre2
                operation = "×"
            elif choix == "4":
                if nombre2 == 0:
                    raise ZeroDivisionError("Division par zéro impossible")
                resultat = nombre1 / nombre2
                operation = "÷"

            # Afficher le résultat
            print(f"\n✅ Résultat : {nombre1} {operation} {nombre2} = {resultat}")

        except ValueError:
            print("\n❌ Erreur : Veuillez entrer des nombres valides")
            print("   Exemple : 10.5 ou 42")

        except ZeroDivisionError as e:
            print(f"\n❌ Erreur : {e}")
            print("   Le diviseur ne peut pas être zéro")

        except KeyboardInterrupt:
            print("\n\n⚠️ Programme interrompu par l'utilisateur")
            break

        except Exception as e:
            print(f"\n❌ Erreur inattendue : {e}")
            print("   Veuillez réessayer")

        finally:
            # Ce bloc s'exécute toujours
            pass  # Ici, on pourrait sauvegarder l'historique, etc.

# Lancer la calculatrice
if __name__ == "__main__":
    calculatrice_robuste()
```

**Ce que cet exemple démontre :**
- ✅ Gestion de plusieurs types d'exceptions
- ✅ Messages d'erreur clairs et utiles
- ✅ Le programme ne plante jamais
- ✅ Bonne expérience utilisateur
- ✅ Code structuré et lisible

---

## Conseils pour débuter

### 1. Commencez simple
Ne cherchez pas à gérer toutes les erreurs possibles dès le début. Commencez par les plus évidentes.

### 2. Lisez les messages d'erreur
Les messages d'erreur Python sont très informatifs. Prenez le temps de les lire attentivement.

### 3. Testez votre code
Testez votre code avec des valeurs normales, mais aussi avec des valeurs extrêmes ou invalides.

### 4. Utilisez les outils de débogage
N'ayez pas peur d'utiliser print() au début. C'est un outil simple mais efficace.

### 5. Apprenez progressivement
La gestion des erreurs est une compétence qui se développe avec le temps et la pratique.

---

## Résumé de l'introduction

**Points clés à retenir :**

1. 🐛 **Trois types d'erreurs** : syntaxe, exécution (exceptions), et logique
2. 🛡️ **Importance** : Éviter les plantages, fournir de bons messages, créer des applications robustes
3. 🎯 **Exceptions courantes** : ValueError, TypeError, IndexError, KeyError, etc.
4. 📖 **Lire les erreurs** : Comprendre la trace (traceback) pour localiser le problème
5. 🔧 **try/except** : Syntaxe de base pour gérer les exceptions
6. ✅ **Bonnes pratiques** : Être spécifique, ne pas cacher les erreurs, fournir des messages clairs

**Dans les prochaines sections, nous allons approfondir :**
- La hiérarchie complète des exceptions Python
- Comment créer vos propres exceptions
- Les techniques avancées de débogage
- L'optimisation et le profiling de votre code

La gestion des erreurs n'est pas un obstacle, c'est un outil puissant qui fait de vous un meilleur programmeur. Avec de la pratique, vous apprendrez à anticiper les problèmes et à écrire du code plus robuste et professionnel.

Prêt à plonger dans les détails ? Passons à la section suivante ! 🚀✨

⏭️ [Hiérarchie des exceptions](/09-erreurs-et-debogage/01-hierarchie-des-exceptions.md)
