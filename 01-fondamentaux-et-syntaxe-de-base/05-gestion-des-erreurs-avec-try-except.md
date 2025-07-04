🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.5 : Gestion des erreurs avec try/except

## Introduction

Les erreurs font partie intégrante de la programmation. Même les meilleurs développeurs écrivent du code qui peut parfois échouer : fichier introuvable, division par zéro, entrée utilisateur invalide... La **gestion des erreurs** permet à votre programme de continuer à fonctionner même quand quelque chose se passe mal, plutôt que de s'arrêter brutalement.

## Pourquoi gérer les erreurs ?

### Programme sans gestion d'erreurs (problématique)

```python
# ❌ Programme fragile
print("=== Calculatrice Simple ===")
a = int(input("Premier nombre : "))      # Erreur si l'utilisateur tape "abc"
b = int(input("Second nombre : "))       # Erreur si l'utilisateur tape "xyz"
resultat = a / b                         # Erreur si b = 0
print(f"Résultat : {resultat}")
```

Si l'utilisateur entre `"abc"` au lieu d'un nombre, le programme s'arrête avec une erreur :
```
ValueError: invalid literal for int() with base 10: 'abc'
```

### Programme avec gestion d'erreurs (solution)

```python
# ✅ Programme robuste
print("=== Calculatrice Robuste ===")

try:
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    resultat = a / b
    print(f"Résultat : {resultat}")
except ValueError:
    print("Erreur : Veuillez entrer des nombres entiers valides")
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
```

## Les types d'erreurs en Python

### Erreurs de syntaxe vs erreurs d'exécution

```python
# ❌ Erreur de syntaxe (le code ne peut pas s'exécuter)
# if age >= 18    # SyntaxError : manque ':'

# ❌ Erreur d'exécution (le code s'exécute mais échoue)
age = int("abc")  # ValueError lors de l'exécution
```

### Erreurs courantes

```python
# ValueError : valeur inappropriée
nombre = int("hello")        # ValueError

# ZeroDivisionError : division par zéro
resultat = 10 / 0           # ZeroDivisionError

# TypeError : type inapproprié
texte = "Hello"
longueur = len(5)           # TypeError : len() attend une séquence

# IndexError : index hors limites
liste = [1, 2, 3]
element = liste[10]         # IndexError

# KeyError : clé inexistante dans un dictionnaire
personne = {"nom": "Alice"}
age = personne["age"]       # KeyError

# FileNotFoundError : fichier introuvable
with open("fichier_inexistant.txt") as f:  # FileNotFoundError
    contenu = f.read()
```

## Structure try/except de base

### Syntaxe simple

```python
try:
    # Code qui peut provoquer une erreur
    operation_risquee()
except TypeErreur:
    # Code à exécuter si cette erreur spécifique se produit
    print("Gestion de l'erreur")
```

### Exemple pratique : Saisie d'un nombre

```python
def demander_nombre():
    """Demande un nombre à l'utilisateur avec gestion d'erreurs."""
    while True:
        try:
            nombre = int(input("Entrez un nombre entier : "))
            return nombre
        except ValueError:
            print("❌ Ce n'est pas un nombre entier valide. Réessayez.")

# Utilisation
print("Programme de saisie sécurisée")
mon_nombre = demander_nombre()
print(f"Vous avez saisi : {mon_nombre}")
```

### Gestion de plusieurs types d'erreurs

```python
def division_securisee(a, b):
    """Effectue une division avec gestion d'erreurs."""
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("❌ Erreur : Division par zéro impossible")
        return None
    except TypeError:
        print("❌ Erreur : Les arguments doivent être des nombres")
        return None

# Tests
print("=== Tests de division sécurisée ===")
print(f"10 / 2 = {division_securisee(10, 2)}")        # ✅ 5.0
print(f"10 / 0 = {division_securisee(10, 0)}")        # ❌ Division par zéro
print(f"'10' / 2 = {division_securisee('10', 2)}")    # ❌ TypeError
```

## Structure try/except/else/finally

### Syntaxe complète

```python
try:
    # Code qui peut provoquer une erreur
    pass
except TypeErreur1:
    # Gestion de l'erreur de type 1
    pass
except TypeErreur2:
    # Gestion de l'erreur de type 2
    pass
else:
    # Code exécuté SEULEMENT si aucune erreur ne s'est produite
    pass
finally:
    # Code exécuté TOUJOURS, qu'il y ait eu erreur ou non
    pass
```

### Exemple pratique : Lecture de fichier

```python
def lire_fichier(nom_fichier):
    """Lit un fichier avec gestion complète d'erreurs."""
    fichier = None
    try:
        print(f"Tentative d'ouverture du fichier : {nom_fichier}")
        fichier = open(nom_fichier, 'r', encoding='utf-8')
        contenu = fichier.read()
        print("✅ Fichier lu avec succès")
        return contenu

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{nom_fichier}' n'existe pas")
        return None

    except PermissionError:
        print(f"❌ Erreur : Pas de permission pour lire '{nom_fichier}'")
        return None

    except UnicodeDecodeError:
        print(f"❌ Erreur : Problème d'encodage du fichier")
        return None

    else:
        # Exécuté seulement si aucune erreur
        print("📊 Statistiques du fichier :")
        print(f"   Nombre de caractères : {len(contenu)}")
        print(f"   Nombre de lignes : {contenu.count(chr(10)) + 1}")

    finally:
        # Toujours exécuté
        if fichier and not fichier.closed:
            fichier.close()
            print("🔒 Fichier fermé")

# Test
# contenu = lire_fichier("test.txt")
```

## Capture et utilisation des informations d'erreur

### Récupérer les détails de l'erreur

```python
def analyser_erreur():
    """Montre comment récupérer les informations d'erreur."""
    try:
        # Provoquer différentes erreurs pour les analyser
        choix = input("Choisissez l'erreur (1:ValueError, 2:ZeroDivision, 3:IndexError) : ")

        if choix == "1":
            int("abc")  # ValueError
        elif choix == "2":
            10 / 0      # ZeroDivisionError
        elif choix == "3":
            [1, 2, 3][10]  # IndexError
        else:
            print("Aucune erreur générée")

    except ValueError as e:
        print(f"❌ ValueError capturée : {e}")
        print(f"   Type : {type(e).__name__}")

    except ZeroDivisionError as e:
        print(f"❌ ZeroDivisionError capturée : {e}")
        print(f"   Type : {type(e).__name__}")

    except IndexError as e:
        print(f"❌ IndexError capturée : {e}")
        print(f"   Type : {type(e).__name__}")

    except Exception as e:
        # Capture toutes les autres erreurs
        print(f"❌ Erreur inattendue : {e}")
        print(f"   Type : {type(e).__name__}")

# Test
# analyser_erreur()
```

### Gestion générique avec Exception

```python
def operation_avec_log(operation, *args):
    """Exécute une opération avec journalisation des erreurs."""
    try:
        resultat = operation(*args)
        print(f"✅ Opération réussie : {resultat}")
        return resultat

    except Exception as e:
        print(f"❌ Erreur lors de l'opération :")
        print(f"   Type d'erreur : {type(e).__name__}")
        print(f"   Message : {e}")
        print(f"   Arguments : {args}")
        return None

# Tests avec différentes opérations
def diviser(a, b):
    return a / b

def acceder_liste(liste, index):
    return liste[index]

print("=== Tests d'opérations ===")
operation_avec_log(diviser, 10, 2)      # ✅ Réussite
operation_avec_log(diviser, 10, 0)      # ❌ ZeroDivisionError
operation_avec_log(acceder_liste, [1, 2, 3], 1)  # ✅ Réussite
operation_avec_log(acceder_liste, [1, 2, 3], 10) # ❌ IndexError
```

## Lever des exceptions avec raise

### Créer ses propres erreurs

```python
def valider_age(age):
    """Valide un âge et lève une exception si invalide."""
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier")

    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")

    if age > 150:
        raise ValueError("L'âge ne peut pas dépasser 150 ans")

    return True

def creer_personne(nom, age):
    """Crée une personne avec validation."""
    try:
        valider_age(age)
        personne = {"nom": nom, "age": age}
        print(f"✅ Personne créée : {personne}")
        return personne

    except TypeError as e:
        print(f"❌ Erreur de type : {e}")
        return None

    except ValueError as e:
        print(f"❌ Erreur de valeur : {e}")
        return None

# Tests
print("=== Tests de création de personne ===")
creer_personne("Alice", 25)    # ✅ Valide
creer_personne("Bob", -5)      # ❌ Âge négatif
creer_personne("Charlie", 200) # ❌ Âge trop élevé
creer_personne("David", "25")  # ❌ Type incorrect
```

### Re-lever une exception

```python
def traiter_donnees(donnees):
    """Traite des données et re-lève l'erreur avec contexte."""
    try:
        # Simulation de traitement
        if not donnees:
            raise ValueError("Les données sont vides")

        resultat = [x * 2 for x in donnees]
        return resultat

    except Exception as e:
        print(f"🔍 Erreur détectée dans traiter_donnees()")
        print(f"   Données reçues : {donnees}")
        raise  # Re-lève la même exception

def programme_principal():
    """Programme principal avec gestion d'erreurs."""
    try:
        donnees = []  # Données vides pour provoquer l'erreur
        resultat = traiter_donnees(donnees)
        print(f"Résultat : {resultat}")

    except ValueError as e:
        print(f"❌ Erreur dans le programme principal : {e}")

# Test
programme_principal()
```

## Exemples pratiques

### Calculatrice robuste complète

```python
def obtenir_nombre(message):
    """Demande un nombre avec validation."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Veuillez entrer un nombre valide")

def obtenir_operation():
    """Demande une opération valide."""
    operations_valides = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input(f"Opération ({', '.join(operations_valides)}) : ")
        if op in operations_valides:
            return op
        else:
            print(f"❌ Opération invalide. Utilisez : {', '.join(operations_valides)}")

def calculer(a, b, operation):
    """Effectue le calcul avec gestion d'erreurs."""
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("Division par zéro")
            return a / b
        elif operation == '**':
            if a == 0 and b < 0:
                raise ValueError("0 ne peut pas être élevé à une puissance négative")
            return a ** b
        elif operation == '%':
            if b == 0:
                raise ZeroDivisionError("Modulo par zéro")
            return a % b

    except OverflowError:
        raise ValueError("Le résultat est trop grand pour être calculé")

def calculatrice_robuste():
    """Calculatrice avec gestion complète d'erreurs."""
    print("🧮 === CALCULATRICE ROBUSTE ===")

    while True:
        try:
            print("\n" + "─" * 40)

            # Saisie des données
            a = obtenir_nombre("Premier nombre : ")
            operation = obtenir_operation()
            b = obtenir_nombre("Second nombre : ")

            # Calcul
            resultat = calculer(a, b, operation)

            # Affichage du résultat
            print(f"✅ {a} {operation} {b} = {resultat}")

        except (ZeroDivisionError, ValueError) as e:
            print(f"❌ Erreur de calcul : {e}")

        except KeyboardInterrupt:
            print("\n👋 Programme interrompu par l'utilisateur")
            break

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

        finally:
            # Demander si continuer
            try:
                continuer = input("\nContinuer ? (o/n) : ").lower()
                if continuer not in ['o', 'oui', 'y', 'yes']:
                    print("👋 Au revoir !")
                    break
            except KeyboardInterrupt:
                print("\n👋 Au revoir !")
                break

# Lancement de la calculatrice
# calculatrice_robuste()
```

### Gestionnaire de fichier sécurisé

```python
import os
from datetime import datetime

def creer_fichier_log():
    """Crée un fichier de log avec gestion d'erreurs."""
    nom_fichier = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(f"Log créé le {datetime.now()}\n")
            f.write("-" * 50 + "\n")

        print(f"✅ Fichier de log créé : {nom_fichier}")
        return nom_fichier

    except PermissionError:
        print("❌ Erreur : Pas de permission d'écriture dans ce dossier")
        return None

    except OSError as e:
        print(f"❌ Erreur système : {e}")
        return None

def ajouter_entree_log(nom_fichier, message):
    """Ajoute une entrée au fichier de log."""
    if not nom_fichier:
        print("❌ Aucun fichier de log disponible")
        return False

    try:
        with open(nom_fichier, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] {message}\n")

        print(f"✅ Entrée ajoutée au log : {message}")
        return True

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {nom_fichier} n'existe plus")
        return False

    except PermissionError:
        print(f"❌ Erreur : Pas de permission d'écriture sur {nom_fichier}")
        return False

    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return False

def lire_log(nom_fichier):
    """Lit et affiche le contenu du fichier de log."""
    if not nom_fichier:
        print("❌ Aucun fichier de log disponible")
        return

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()

        if contenu.strip():
            print(f"\n📋 Contenu du log ({nom_fichier}) :")
            print("─" * 50)
            print(contenu)
            print("─" * 50)
        else:
            print("📋 Le fichier de log est vide")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {nom_fichier} n'existe pas")

    except PermissionError:
        print(f"❌ Erreur : Pas de permission de lecture sur {nom_fichier}")

    except UnicodeDecodeError:
        print(f"❌ Erreur : Problème d'encodage du fichier")

    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")

def gestionnaire_log():
    """Interface principale du gestionnaire de log."""
    print("📝 === GESTIONNAIRE DE LOG SÉCURISÉ ===")

    fichier_log = None

    while True:
        try:
            print("\n🔧 Menu :")
            print("1. Créer un nouveau fichier de log")
            print("2. Ajouter une entrée")
            print("3. Lire le log")
            print("4. Quitter")

            choix = input("\nVotre choix (1-4) : ").strip()

            if choix == "1":
                fichier_log = creer_fichier_log()

            elif choix == "2":
                if fichier_log:
                    message = input("Message à ajouter : ")
                    ajouter_entree_log(fichier_log, message)
                else:
                    print("❌ Créez d'abord un fichier de log")

            elif choix == "3":
                lire_log(fichier_log)

            elif choix == "4":
                print("👋 Au revoir !")
                break

            else:
                print("❌ Choix invalide")

        except KeyboardInterrupt:
            print("\n👋 Programme interrompu")
            break

        except Exception as e:
            print(f"❌ Erreur dans le menu : {e}")

# Lancement du gestionnaire
# gestionnaire_log()
```

### Système de validation de données

```python
class ValidatorError(Exception):
    """Exception personnalisée pour les erreurs de validation."""
    pass

def valider_email(email):
    """Valide une adresse email."""
    if not isinstance(email, str):
        raise ValidatorError("L'email doit être une chaîne de caractères")

    if '@' not in email:
        raise ValidatorError("L'email doit contenir un @")

    if '.' not in email.split('@')[1]:
        raise ValidatorError("L'email doit contenir un domaine valide")

    if email.count('@') != 1:
        raise ValidatorError("L'email ne doit contenir qu'un seul @")

    return True

def valider_telephone(telephone):
    """Valide un numéro de téléphone français."""
    # Nettoyer le numéro
    numero_propre = ''.join(c for c in telephone if c.isdigit())

    if len(numero_propre) != 10:
        raise ValidatorError("Le numéro doit contenir exactement 10 chiffres")

    if not numero_propre.startswith('0'):
        raise ValidatorError("Le numéro doit commencer par 0")

    return True

def valider_age(age):
    """Valide un âge."""
    try:
        age_int = int(age)
    except ValueError:
        raise ValidatorError("L'âge doit être un nombre entier")

    if age_int < 0:
        raise ValidatorError("L'âge ne peut pas être négatif")

    if age_int > 150:
        raise ValidatorError("L'âge ne peut pas dépasser 150 ans")

    return True

def valider_donnees_utilisateur(donnees):
    """Valide toutes les données d'un utilisateur."""
    erreurs = []

    # Validation du nom
    try:
        nom = donnees.get('nom', '').strip()
        if not nom:
            erreurs.append("Le nom est obligatoire")
        elif len(nom) < 2:
            erreurs.append("Le nom doit contenir au moins 2 caractères")
    except Exception as e:
        erreurs.append(f"Erreur avec le nom : {e}")

    # Validation de l'email
    try:
        email = donnees.get('email', '')
        if email:  # Si un email est fourni
            valider_email(email)
    except ValidatorError as e:
        erreurs.append(f"Email invalide : {e}")
    except Exception as e:
        erreurs.append(f"Erreur avec l'email : {e}")

    # Validation du téléphone
    try:
        telephone = donnees.get('telephone', '')
        if telephone:  # Si un téléphone est fourni
            valider_telephone(telephone)
    except ValidatorError as e:
        erreurs.append(f"Téléphone invalide : {e}")
    except Exception as e:
        erreurs.append(f"Erreur avec le téléphone : {e}")

    # Validation de l'âge
    try:
        age = donnees.get('age')
        if age is not None:
            valider_age(age)
    except ValidatorError as e:
        erreurs.append(f"Âge invalide : {e}")
    except Exception as e:
        erreurs.append(f"Erreur avec l'âge : {e}")

    return erreurs

def saisir_utilisateur():
    """Interface de saisie d'un utilisateur avec validation."""
    print("👤 === SAISIE D'UTILISATEUR AVEC VALIDATION ===")

    while True:
        try:
            print("\nVeuillez entrer les informations :")

            donnees = {}
            donnees['nom'] = input("Nom (obligatoire) : ")
            donnees['email'] = input("Email (optionnel) : ")
            donnees['telephone'] = input("Téléphone (optionnel) : ")

            age_str = input("Âge (optionnel) : ")
            if age_str.strip():
                donnees['age'] = age_str

            # Validation
            erreurs = valider_donnees_utilisateur(donnees)

            if erreurs:
                print("\n❌ Erreurs détectées :")
                for erreur in erreurs:
                    print(f"   • {erreur}")

                retry = input("\nCorreger les erreurs ? (o/n) : ").lower()
                if retry not in ['o', 'oui', 'y', 'yes']:
                    break
            else:
                print("\n✅ Données valides !")
                print(f"   Utilisateur créé : {donnees}")
                break

        except KeyboardInterrupt:
            print("\n👋 Saisie annulée")
            break

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

# Test du système
# saisir_utilisateur()
```

## Exercices pratiques

### Exercice 1 : Gestionnaire de division sécurisée

```python
# Créez un programme qui :
# 1. Demande deux nombres à l'utilisateur
# 2. Effectue la division avec gestion d'erreurs
# 3. Gère les cas : nombres invalides, division par zéro
# 4. Permet de recommencer en cas d'erreur
# 5. Affiche un historique des calculs réussis
```

### Exercice 2 : Lecteur de fichier robuste

```python
# Créez un programme qui :
# 1. Demande le nom d'un fichier à l'utilisateur
# 2. Tente de le lire avec gestion d'erreurs complète
# 3. Affiche des statistiques (lignes, mots, caractères)
# 4. Gère : fichier inexistant, permissions, encodage
# 5. Propose de réessayer avec un autre fichier
```

### Exercice 3 : Convertisseur de types sécurisé

```python
# Créez un programme qui :
# 1. Propose de convertir une chaîne vers différents types
# 2. Types : int, float, bool, list (avec eval sécurisé)
# 3. Gère toutes les erreurs de conversion possibles
# 4. Affiche le résultat et le type de la conversion
# 5. Permet de faire plusieurs conversions
```

### Exercice 4 : Validateur de formulaire

```python
# Créez un système de validation qui :
# 1. Demande nom, email, âge, code postal
# 2. Valide chaque champ avec des règles spécifiques
# 3. Collecte toutes les erreurs avant de les afficher
# 4. Permet de corriger champ par champ
# 5. Sauvegarde les données valides dans un fichier
```

### Exercice 5 : Gestionnaire d'opérations mathématiques

```python
# Créez un programme qui :
# 1. Propose différentes opérations : +, -, *, /, **, sqrt, log
# 2. Gère les erreurs spécifiques à chaque opération
# 3. Calculs impossibles : log de nombre négatif, sqrt de négatif, etc.
# 4. Historique des calculs avec gestion d'erreurs d'écriture
# 5. Menu interactif avec gestion d'interruption clavier
```

## Bonnes pratiques

### Gestion spécifique vs générale

```python
# ✅ Bon : gestion spécifique puis générale
try:
    resultat = operation_complexe()
except ValueError as e:
    print(f"Erreur de valeur : {e}")
except TypeError as e:
    print(f"Erreur de type : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")

# ❌ Mauvais : trop général
try:
    resultat = operation_complexe()
except Exception:
    print("Une erreur s'est produite")  # Pas assez spécifique
```

### Messages d'erreur informatifs

```python
# ✅ Bon : messages utiles pour l'utilisateur
try:
    age = int(input("Votre âge : "))
except ValueError:
    print("❌ Veuillez entrer un nombre entier (par exemple : 25)")

# ❌ Mauvais : message technique
try:
    age = int(input("Votre âge : "))
except ValueError as e:
    print(f"ValueError: {e}")  # Trop technique pour l'utilisateur
```

### Ne pas ignorer les erreurs

```python
# ❌ Très mauvais : ignorer les erreurs
try:
    operation_importante()
except:
    pass  # Silence les erreurs - DANGEREUX !

# ✅ Bon : au minimum logger l'erreur
try:
    operation_importante()
except Exception as e:
    print(f"Erreur lors de l'opération : {e}")
    # Et/ou logger l'erreur pour debug
```

### Utiliser finally pour le nettoyage

```python
# ✅ Bon : nettoyage garanti
fichier = None
try:
    fichier = open("donnees.txt")
    traiter_fichier(fichier)
except Exception as e:
    print(f"Erreur : {e}")
finally:
    if fichier:
        fichier.close()  # Toujours fermé
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ **Importance de la gestion d'erreurs** : Créer des programmes robustes
✅ **Structure try/except** : Syntaxe de base et avancée
✅ **Types d'erreurs courantes** : ValueError, TypeError, ZeroDivisionError, etc.
✅ **Clauses else et finally** : Contrôle fin du flux d'exécution
✅ **Capture d'informations** : Récupérer et utiliser les détails d'erreur
✅ **Lever des exceptions** : Créer ses propres erreurs avec raise
✅ **Applications pratiques** : Calculatrice, gestionnaire de fichiers, validation

**Concepts clés à retenir :**
- Anticipez les erreurs possibles dans votre code
- Gérez les erreurs spécifiques avant les générales
- Fournissez des messages d'erreur compréhensibles pour l'utilisateur
- Utilisez `finally` pour les opérations de nettoyage obligatoires
- Ne jamais ignorer complètement une erreur avec `pass`
- Loggez les erreurs pour faciliter le débogage
- Validez les entrées utilisateur le plus tôt possible

**Prochaine étape** : Félicitations ! Vous avez terminé le Module 1 - Fondamentaux et syntaxe de base. Vous maîtrisez maintenant :
- L'installation et configuration de Python
- Les variables, types de données et opérateurs
- Les structures de contrôle (conditions et boucles)
- Les fonctions et la portée des variables
- La gestion des erreurs avec try/except

Dans le Module 2, nous explorerons les structures de données avancées qui vous permettront de manipuler des collections d'informations plus complexes !

---

💡 **Félicitations !** Vous avez terminé le Module 1 avec succès. Ce projet démontre votre maîtrise des fondamentaux de Python. Vous êtes maintenant prêt pour le Module 2 : Structures de données avancées !

⏭️

---

## Projet final du Module 1 : Gestionnaire de contacts

Pour mettre en pratique tout ce que vous avez appris dans ce module, voici un projet complet qui combine tous les concepts :

### Cahier des charges

Créez un **gestionnaire de contacts** avec les fonctionnalités suivantes :

1. **Menu principal** avec options : ajouter, lister, rechercher, modifier, supprimer, sauvegarder, charger
2. **Validation des données** : nom (obligatoire), email (format), téléphone (format français)
3. **Gestion d'erreurs** complète pour toutes les opérations
4. **Sauvegarde** des contacts dans un fichier texte
5. **Interface utilisateur** claire et conviviale

### Code du projet complet

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Contacts - Projet final Module 1
Combine tous les concepts appris : variables, structures de contrôle,
fonctions, gestion d'erreurs
"""

import os
import json
from datetime import datetime

# ===== FONCTIONS DE VALIDATION =====

def valider_nom(nom):
    """
    Valide un nom de contact.

    Args:
        nom (str): Le nom à valider

    Returns:
        str: Le nom nettoyé

    Raises:
        ValueError: Si le nom est invalide
    """
    if not isinstance(nom, str):
        raise ValueError("Le nom doit être une chaîne de caractères")

    nom_propre = nom.strip()
    if not nom_propre:
        raise ValueError("Le nom ne peut pas être vide")

    if len(nom_propre) < 2:
        raise ValueError("Le nom doit contenir au moins 2 caractères")

    return nom_propre

def valider_email(email):
    """
    Valide une adresse email.

    Args:
        email (str): L'email à valider

    Returns:
        str: L'email nettoyé

    Raises:
        ValueError: Si l'email est invalide
    """
    if not email:  # Email optionnel
        return ""

    if not isinstance(email, str):
        raise ValueError("L'email doit être une chaîne de caractères")

    email_propre = email.strip().lower()

    if '@' not in email_propre:
        raise ValueError("L'email doit contenir un @")

    if email_propre.count('@') != 1:
        raise ValueError("L'email ne doit contenir qu'un seul @")

    parties = email_propre.split('@')
    if not parties[0] or not parties[1]:
        raise ValueError("L'email doit avoir une partie avant et après le @")

    if '.' not in parties[1]:
        raise ValueError("Le domaine doit contenir au moins un point")

    return email_propre

def valider_telephone(telephone):
    """
    Valide un numéro de téléphone français.

    Args:
        telephone (str): Le téléphone à valider

    Returns:
        str: Le téléphone formaté

    Raises:
        ValueError: Si le téléphone est invalide
    """
    if not telephone:  # Téléphone optionnel
        return ""

    if not isinstance(telephone, str):
        raise ValueError("Le téléphone doit être une chaîne de caractères")

    # Nettoyer : garder seulement les chiffres
    chiffres = ''.join(c for c in telephone if c.isdigit())

    if not chiffres:
        raise ValueError("Le téléphone doit contenir des chiffres")

    if len(chiffres) != 10:
        raise ValueError("Le téléphone doit contenir exactement 10 chiffres")

    if not chiffres.startswith('0'):
        raise ValueError("Le téléphone doit commencer par 0")

    # Formatage : 01 23 45 67 89
    return f"{chiffres[:2]} {chiffres[2:4]} {chiffres[4:6]} {chiffres[6:8]} {chiffres[8:]}"

# ===== CLASSE CONTACT =====

class Contact:
    """Représente un contact avec nom, email et téléphone."""

    def __init__(self, nom, email="", telephone=""):
        """
        Initialise un contact.

        Args:
            nom (str): Nom du contact (obligatoire)
            email (str): Email du contact (optionnel)
            telephone (str): Téléphone du contact (optionnel)
        """
        self.nom = valider_nom(nom)
        self.email = valider_email(email)
        self.telephone = valider_telephone(telephone)
        self.date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        """Représentation textuelle du contact."""
        lignes = [f"📋 {self.nom}"]
        if self.email:
            lignes.append(f"📧 {self.email}")
        if self.telephone:
            lignes.append(f"📱 {self.telephone}")
        lignes.append(f"📅 Créé le {self.date_creation}")
        return "\n".join(lignes)

    def to_dict(self):
        """Convertit le contact en dictionnaire pour la sauvegarde."""
        return {
            'nom': self.nom,
            'email': self.email,
            'telephone': self.telephone,
            'date_creation': self.date_creation
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un contact à partir d'un dictionnaire."""
        contact = cls(data['nom'], data.get('email', ''), data.get('telephone', ''))
        contact.date_creation = data.get('date_creation', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return contact

# ===== GESTIONNAIRE DE CONTACTS =====

class GestionnaireContacts:
    """Gestionnaire principal des contacts."""

    def __init__(self):
        """Initialise le gestionnaire avec une liste vide."""
        self.contacts = []
        self.fichier_sauvegarde = "contacts.json"

    def ajouter_contact(self, nom, email="", telephone=""):
        """
        Ajoute un nouveau contact.

        Args:
            nom (str): Nom du contact
            email (str): Email du contact
            telephone (str): Téléphone du contact

        Returns:
            bool: True si ajouté avec succès
        """
        try:
            # Vérifier si le contact existe déjà
            if self.rechercher_contact_exact(nom):
                raise ValueError(f"Un contact nommé '{nom}' existe déjà")

            contact = Contact(nom, email, telephone)
            self.contacts.append(contact)
            print(f"✅ Contact '{nom}' ajouté avec succès")
            return True

        except ValueError as e:
            print(f"❌ Erreur lors de l'ajout : {e}")
            return False

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
            return False

    def lister_contacts(self):
        """Affiche tous les contacts."""
        if not self.contacts:
            print("📭 Aucun contact enregistré")
            return

        print(f"\n📚 Liste des contacts ({len(self.contacts)} contact(s)) :")
        print("=" * 50)

        for i, contact in enumerate(self.contacts, 1):
            print(f"\n{i}. {contact}")
            print("-" * 30)

    def rechercher_contact_exact(self, nom):
        """
        Recherche un contact par nom exact.

        Args:
            nom (str): Nom à rechercher

        Returns:
            Contact: Le contact trouvé ou None
        """
        nom_recherche = nom.strip().lower()
        for contact in self.contacts:
            if contact.nom.lower() == nom_recherche:
                return contact
        return None

    def rechercher_contacts(self, terme):
        """
        Recherche des contacts par terme partiel.

        Args:
            terme (str): Terme à rechercher

        Returns:
            list: Liste des contacts trouvés
        """
        if not terme:
            return []

        terme_recherche = terme.strip().lower()
        contacts_trouves = []

        for contact in self.contacts:
            if (terme_recherche in contact.nom.lower() or
                terme_recherche in contact.email.lower() or
                terme_recherche in contact.telephone):
                contacts_trouves.append(contact)

        return contacts_trouves

    def modifier_contact(self, nom_actuel, nouveau_nom=None, nouvel_email=None, nouveau_telephone=None):
        """
        Modifie un contact existant.

        Args:
            nom_actuel (str): Nom actuel du contact
            nouveau_nom (str): Nouveau nom (optionnel)
            nouvel_email (str): Nouvel email (optionnel)
            nouveau_telephone (str): Nouveau téléphone (optionnel)

        Returns:
            bool: True si modifié avec succès
        """
        try:
            contact = self.rechercher_contact_exact(nom_actuel)
            if not contact:
                print(f"❌ Contact '{nom_actuel}' introuvable")
                return False

            # Modifications
            if nouveau_nom is not None:
                contact.nom = valider_nom(nouveau_nom)

            if nouvel_email is not None:
                contact.email = valider_email(nouvel_email)

            if nouveau_telephone is not None:
                contact.telephone = valider_telephone(nouveau_telephone)

            print(f"✅ Contact modifié avec succès")
            return True

        except ValueError as e:
            print(f"❌ Erreur de validation : {e}")
            return False

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
            return False

    def supprimer_contact(self, nom):
        """
        Supprime un contact.

        Args:
            nom (str): Nom du contact à supprimer

        Returns:
            bool: True si supprimé avec succès
        """
        try:
            contact = self.rechercher_contact_exact(nom)
            if not contact:
                print(f"❌ Contact '{nom}' introuvable")
                return False

            self.contacts.remove(contact)
            print(f"✅ Contact '{nom}' supprimé avec succès")
            return True

        except Exception as e:
            print(f"❌ Erreur lors de la suppression : {e}")
            return False

    def sauvegarder(self, fichier=None):
        """
        Sauvegarde les contacts dans un fichier.

        Args:
            fichier (str): Nom du fichier (optionnel)

        Returns:
            bool: True si sauvegardé avec succès
        """
        if fichier is None:
            fichier = self.fichier_sauvegarde

        try:
            donnees = {
                'contacts': [contact.to_dict() for contact in self.contacts],
                'date_sauvegarde': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'version': '1.0'
            }

            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)

            print(f"✅ {len(self.contacts)} contact(s) sauvegardé(s) dans '{fichier}'")
            return True

        except PermissionError:
            print(f"❌ Erreur : Pas de permission d'écriture pour '{fichier}'")
            return False

        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")
            return False

    def charger(self, fichier=None):
        """
        Charge les contacts depuis un fichier.

        Args:
            fichier (str): Nom du fichier (optionnel)

        Returns:
            bool: True si chargé avec succès
        """
        if fichier is None:
            fichier = self.fichier_sauvegarde

        try:
            if not os.path.exists(fichier):
                print(f"📄 Le fichier '{fichier}' n'existe pas encore")
                return False

            with open(fichier, 'r', encoding='utf-8') as f:
                donnees = json.load(f)

            # Vider la liste actuelle
            self.contacts.clear()

            # Charger les contacts
            for contact_data in donnees.get('contacts', []):
                try:
                    contact = Contact.from_dict(contact_data)
                    self.contacts.append(contact)
                except Exception as e:
                    print(f"⚠️ Erreur lors du chargement d'un contact : {e}")

            print(f"✅ {len(self.contacts)} contact(s) chargé(s) depuis '{fichier}'")

            # Afficher info de sauvegarde
            if 'date_sauvegarde' in donnees:
                print(f"📅 Dernière sauvegarde : {donnees['date_sauvegarde']}")

            return True

        except FileNotFoundError:
            print(f"❌ Fichier '{fichier}' introuvable")
            return False

        except json.JSONDecodeError:
            print(f"❌ Erreur : Le fichier '{fichier}' n'est pas un JSON valide")
            return False

        except PermissionError:
            print(f"❌ Erreur : Pas de permission de lecture pour '{fichier}'")
            return False

        except Exception as e:
            print(f"❌ Erreur lors du chargement : {e}")
            return False

# ===== INTERFACE UTILISATEUR =====

def obtenir_entree(message, obligatoire=True):
    """
    Demande une entrée à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher
        obligatoire (bool): Si l'entrée est obligatoire

    Returns:
        str: L'entrée utilisateur
    """
    while True:
        try:
            entree = input(message).strip()
            if obligatoire and not entree:
                print("❌ Cette information est obligatoire")
                continue
            return entree
        except KeyboardInterrupt:
            print("\n⏹️ Opération annulée")
            return None

def menu_ajouter_contact(gestionnaire):
    """Interface pour ajouter un contact."""
    print("\n➕ === AJOUTER UN CONTACT ===")

    nom = obtenir_entree("Nom (obligatoire) : ")
    if nom is None:
        return

    email = obtenir_entree("Email (optionnel) : ", obligatoire=False)
    if email is None:
        return

    telephone = obtenir_entree("Téléphone (optionnel) : ", obligatoire=False)
    if telephone is None:
        return

    gestionnaire.ajouter_contact(nom, email, telephone)

def menu_rechercher_contacts(gestionnaire):
    """Interface pour rechercher des contacts."""
    print("\n🔍 === RECHERCHER DES CONTACTS ===")

    terme = obtenir_entree("Terme de recherche : ")
    if terme is None:
        return

    contacts_trouves = gestionnaire.rechercher_contacts(terme)

    if not contacts_trouves:
        print(f"❌ Aucun contact trouvé pour '{terme}'")
        return

    print(f"\n✅ {len(contacts_trouves)} contact(s) trouvé(s) :")
    print("=" * 50)

    for i, contact in enumerate(contacts_trouves, 1):
        print(f"\n{i}. {contact}")
        print("-" * 30)

def menu_modifier_contact(gestionnaire):
    """Interface pour modifier un contact."""
    print("\n✏️ === MODIFIER UN CONTACT ===")

    nom_actuel = obtenir_entree("Nom du contact à modifier : ")
    if nom_actuel is None:
        return

    contact = gestionnaire.rechercher_contact_exact(nom_actuel)
    if not contact:
        print(f"❌ Contact '{nom_actuel}' introuvable")
        return

    print(f"\nContact actuel :")
    print(contact)

    print(f"\nLaissez vide pour conserver la valeur actuelle")

    nouveau_nom = obtenir_entree("Nouveau nom : ", obligatoire=False)
    if nouveau_nom is None:
        return

    nouvel_email = obtenir_entree("Nouvel email : ", obligatoire=False)
    if nouvel_email is None:
        return

    nouveau_telephone = obtenir_entree("Nouveau téléphone : ", obligatoire=False)
    if nouveau_telephone is None:
        return

    # Appliquer seulement les modifications non vides
    gestionnaire.modifier_contact(
        nom_actuel,
        nouveau_nom if nouveau_nom else None,
        nouvel_email if nouvel_email else None,
        nouveau_telephone if nouveau_telephone else None
    )

def menu_supprimer_contact(gestionnaire):
    """Interface pour supprimer un contact."""
    print("\n🗑️ === SUPPRIMER UN CONTACT ===")

    nom = obtenir_entree("Nom du contact à supprimer : ")
    if nom is None:
        return

    contact = gestionnaire.rechercher_contact_exact(nom)
    if not contact:
        print(f"❌ Contact '{nom}' introuvable")
        return

    print(f"\nContact à supprimer :")
    print(contact)

    confirmation = obtenir_entree("\nÊtes-vous sûr ? (oui/non) : ")
    if confirmation is None:
        return

    if confirmation.lower() in ['oui', 'o', 'yes', 'y']:
        gestionnaire.supprimer_contact(nom)
    else:
        print("⏹️ Suppression annulée")

def afficher_menu_principal():
    """Affiche le menu principal."""
    print("\n" + "=" * 60)
    print("📇 GESTIONNAIRE DE CONTACTS".center(60))
    print("=" * 60)
    print("1. ➕ Ajouter un contact")
    print("2. 📚 Lister tous les contacts")
    print("3. 🔍 Rechercher des contacts")
    print("4. ✏️  Modifier un contact")
    print("5. 🗑️  Supprimer un contact")
    print("6. 💾 Sauvegarder les contacts")
    print("7. 📁 Charger les contacts")
    print("8. 📊 Statistiques")
    print("9. ❌ Quitter")
    print("-" * 60)

def afficher_statistiques(gestionnaire):
    """Affiche les statistiques des contacts."""
    print("\n📊 === STATISTIQUES ===")

    nb_total = len(gestionnaire.contacts)
    nb_avec_email = sum(1 for c in gestionnaire.contacts if c.email)
    nb_avec_telephone = sum(1 for c in gestionnaire.contacts if c.telephone)
    nb_complets = sum(1 for c in gestionnaire.contacts if c.email and c.telephone)

    print(f"👥 Nombre total de contacts : {nb_total}")

    if nb_total > 0:
        print(f"📧 Contacts avec email : {nb_avec_email} ({nb_avec_email/nb_total*100:.1f}%)")
        print(f"📱 Contacts avec téléphone : {nb_avec_telephone} ({nb_avec_telephone/nb_total*100:.1f}%)")
        print(f"✅ Contacts complets : {nb_complets} ({nb_complets/nb_total*100:.1f}%)")

        if gestionnaire.contacts:
            print(f"\n📅 Dernier contact ajouté : {gestionnaire.contacts[-1].nom}")

def main():
    """Fonction principale du programme."""
    print("🎉 Bienvenue dans le Gestionnaire de Contacts !")

    gestionnaire = GestionnaireContacts()

    # Tentative de chargement automatique
    print("\n📁 Chargement automatique des contacts...")
    gestionnaire.charger()

    while True:
        try:
            afficher_menu_principal()

            choix = input("Votre choix (1-9) : ").strip()

            if choix == "1":
                menu_ajouter_contact(gestionnaire)

            elif choix == "2":
                gestionnaire.lister_contacts()

            elif choix == "3":
                menu_rechercher_contacts(gestionnaire)

            elif choix == "4":
                menu_modifier_contact(gestionnaire)

            elif choix == "5":
                menu_supprimer_contact(gestionnaire)

            elif choix == "6":
                gestionnaire.sauvegarder()

            elif choix == "7":
                gestionnaire.charger()

            elif choix == "8":
                afficher_statistiques(gestionnaire)

            elif choix == "9":
                print("\n💾 Sauvegarde automatique...")
                gestionnaire.sauvegarder()
                print("👋 Au revoir et à bientôt !")
                break

            else:
                print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 9.")

        except KeyboardInterrupt:
            print("\n\n⏹️ Programme interrompu par l'utilisateur")
            print("💾 Sauvegarde automatique...")
            gestionnaire.sauvegarder()
            print("👋 Au revoir !")
            break

        except Exception as e:
            print(f"❌ Erreur inattendue dans le menu : {e}")
            print("🔄 Retour au menu principal...")

if __name__ == "__main__":
    main()
```

### Instructions pour le projet

1. **Copiez le code** dans un fichier `gestionnaire_contacts.py`
2. **Exécutez le programme** : `python gestionnaire_contacts.py`
3. **Testez toutes les fonctionnalités** :
   - Ajout de contacts avec validation
   - Recherche et modification
   - Sauvegarde et chargement
   - Gestion d'erreurs

### Concepts du Module 1 utilisés

✅ **Variables et types** : Chaînes, listes, dictionnaires, booléens
✅ **Structures de contrôle** : if/else, boucles while et for
✅ **Fonctions** : Définition, paramètres, valeurs de retour, portée
✅ **Gestion d'erreurs** : try/except/finally, exceptions personnalisées
✅ **Bonnes pratiques** : Validation, messages clairs, code modulaire

### Extensions possibles

Pour aller plus loin, vous pourriez ajouter :
- Interface graphique avec tkinter
- Base de données SQLite
- Import/export CSV
- Groupes de contacts
- Historique des modifications


---


