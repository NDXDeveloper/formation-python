🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.3 : Techniques de débogage

## Introduction

Le débogage, c'est comme être un détective numérique ! Quand votre code ne fonctionne pas comme prévu, vous devez mener l'enquête pour découvrir ce qui s'est passé. Parfois le coupable est évident, parfois il se cache bien.

Dans cette section, nous allons explorer les différentes techniques et outils pour traquer les bugs efficacement, depuis les méthodes simples jusqu'aux outils professionnels.

## Les différents types de bugs

### 1. Erreurs de syntaxe
Python vous les signale immédiatement :

```python
# Erreur de syntaxe - parenthèse manquante
print("Hello World"
# SyntaxError: unexpected EOF while parsing
```

### 2. Erreurs d'exécution (Runtime Errors)
Le code démarre mais plante pendant l'exécution :

```python
# Erreur d'exécution
nombres = [1, 2, 3]
print(nombres[5])  # IndexError: list index out of range
```

### 3. Erreurs logiques
Le code fonctionne mais ne fait pas ce qu'on attend :

```python
# Erreur logique - calcul de moyenne incorrect
def moyenne(nombres):
    return sum(nombres) / len(nombres) + 1  # +1 ne devrait pas être là !

print(moyenne([2, 4, 6]))  # Résultat: 5.0 au lieu de 4.0
```

## Technique 1 : Le débogage avec print()

### La méthode classique

```python
def calculer_factorielle(n):
    print(f"🔍 Calcul factorielle de {n}")  # Debug

    if n < 0:
        print("❌ Nombre négatif détecté")  # Debug
        return None

    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f"📊 i={i}, resultat={resultat}")  # Debug

    print(f"✅ Résultat final: {resultat}")  # Debug
    return resultat

# Test
factorielle = calculer_factorielle(5)
```

### Améliorer les prints de débogage

```python
import time

def debug_print(message, niveau="INFO"):
    """Print de débogage avec timestamp et niveau"""
    timestamp = time.strftime("%H:%M:%S")
    emoji = {"INFO": "ℹ️", "ERROR": "❌", "SUCCESS": "✅", "DEBUG": "🔍"}
    print(f"[{timestamp}] {emoji.get(niveau, '📝')} {message}")

def traiter_commande(produits, quantites):
    debug_print("Début du traitement de commande", "INFO")

    total = 0
    for i, produit in enumerate(produits):
        debug_print(f"Traitement produit {i}: {produit}", "DEBUG")

        if i >= len(quantites):
            debug_print(f"Quantité manquante pour {produit}", "ERROR")
            continue

        prix = obtenir_prix(produit)
        sous_total = prix * quantites[i]
        total += sous_total

        debug_print(f"{produit}: {quantites[i]} x {prix}€ = {sous_total}€", "INFO")

    debug_print(f"Total final: {total}€", "SUCCESS")
    return total
```

## Technique 2 : Le module logging

### Configuration basique

```python
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),  # Sauvegarde dans un fichier
        logging.StreamHandler()            # Affichage dans la console
    ]
)

def diviser(a, b):
    logging.debug(f"Tentative de division: {a} / {b}")

    if b == 0:
        logging.error("Division par zéro détectée !")
        raise ZeroDivisionError("Division par zéro")

    resultat = a / b
    logging.info(f"Division réussie: {a} / {b} = {resultat}")
    return resultat

# Tests
try:
    diviser(10, 2)
    diviser(10, 0)
except ZeroDivisionError:
    logging.error("Erreur capturée dans le main")
```

### Logging avancé avec décorateur

```python
import functools

def log_fonction(func):
    """Décorateur pour logger l'entrée et sortie d'une fonction"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"📥 Entrée dans {func.__name__} avec args={args}, kwargs={kwargs}")
        try:
            resultat = func(*args, **kwargs)
            logging.debug(f"📤 Sortie de {func.__name__} avec résultat={resultat}")
            return resultat
        except Exception as e:
            logging.error(f"💥 Erreur dans {func.__name__}: {e}")
            raise
    return wrapper

@log_fonction
def calculer_age(annee_naissance, annee_actuelle=2025):
    if annee_naissance > annee_actuelle:
        raise ValueError("L'année de naissance ne peut pas être dans le futur")
    return annee_actuelle - annee_naissance

# Test
try:
    age = calculer_age(1990)
    age_futur = calculer_age(2030)
except ValueError as e:
    print(f"Erreur: {e}")
```

## Technique 3 : Le débogueur Python (pdb)

### Utilisation basique de pdb

```python
import pdb

def rechercher_dans_liste(liste, element):
    print("Début de la recherche")

    # Point d'arrêt ici
    pdb.set_trace()

    for i, item in enumerate(liste):
        if item == element:
            print(f"Élément trouvé à l'index {i}")
            return i

    print("Élément non trouvé")
    return -1

# Test
ma_liste = ["pomme", "banane", "orange", "pomme"]
index = rechercher_dans_liste(ma_liste, "orange")
```

**Commandes pdb essentielles :**
- `n` (next) : ligne suivante
- `s` (step) : entrer dans la fonction
- `c` (continue) : continuer l'exécution
- `l` (list) : voir le code autour
- `p variable` : afficher une variable
- `pp variable` : affichage formaté d'une variable
- `h` (help) : aide
- `q` (quit) : quitter

### Débogage post-mortem

```python
import pdb

def fonction_problematique():
    liste = [1, 2, 3]
    print(liste[10])  # Va provoquer une erreur

try:
    fonction_problematique()
except:
    # Lance le débogueur sur l'erreur
    pdb.post_mortem()
```

## Technique 4 : Les assertions

### Vérifications avec assert

```python
def calculer_moyenne(notes):
    # Vérifications de développement
    assert isinstance(notes, list), "Les notes doivent être une liste"
    assert len(notes) > 0, "La liste ne peut pas être vide"
    assert all(0 <= note <= 20 for note in notes), "Les notes doivent être entre 0 et 20"

    moyenne = sum(notes) / len(notes)

    # Vérification du résultat
    assert 0 <= moyenne <= 20, f"Moyenne invalide: {moyenne}"

    return moyenne

# Tests
try:
    print(calculer_moyenne([12, 15, 18]))  # OK
    print(calculer_moyenne([]))            # AssertionError
except AssertionError as e:
    print(f"Assertion échouée: {e}")
```

### Assertions personnalisées

```python
def assert_type(variable, type_attendu, nom_variable="variable"):
    """Vérifie le type d'une variable avec un message personnalisé"""
    if not isinstance(variable, type_attendu):
        raise TypeError(
            f"{nom_variable} doit être de type {type_attendu.__name__}, "
            f"reçu {type(variable).__name__}"
        )

def traiter_texte(texte, longueur_max):
    assert_type(texte, str, "texte")
    assert_type(longueur_max, int, "longueur_max")

    assert longueur_max > 0, "La longueur maximale doit être positive"

    if len(texte) > longueur_max:
        return texte[:longueur_max] + "..."
    return texte

# Tests
print(traiter_texte("Hello World", 5))  # "Hello..."
# traiter_texte(123, 5)  # TypeError
```

## Technique 5 : Analyse de la pile d'appels (traceback)

### Comprendre les tracebacks

```python
import traceback

def fonction_a():
    print("Dans fonction_a")
    fonction_b()

def fonction_b():
    print("Dans fonction_b")
    fonction_c()

def fonction_c():
    print("Dans fonction_c")
    # Erreur volontaire
    resultat = 10 / 0

try:
    fonction_a()
except Exception as e:
    print("=== TRACEBACK COMPLET ===")
    traceback.print_exc()

    print("\n=== TRACEBACK FORMATÉ ===")
    tb_lines = traceback.format_exc().split('\n')
    for i, line in enumerate(tb_lines):
        if line.strip():
            print(f"{i:2d}: {line}")
```

### Traceback personnalisé

```python
import traceback
import sys

def analyser_erreur():
    """Analyse détaillée d'une erreur"""
    exc_type, exc_value, exc_tb = sys.exc_info()

    print(f"🚨 Type d'erreur: {exc_type.__name__}")
    print(f"📝 Message: {exc_value}")
    print(f"📍 Pile d'appels:")

    # Analyse de chaque frame
    tb = exc_tb
    niveau = 0
    while tb is not None:
        frame = tb.tb_frame
        filename = frame.f_code.co_filename
        line_number = tb.tb_lineno
        function_name = frame.f_code.co_name

        print(f"  {'  ' * niveau}├─ {function_name}() ligne {line_number}")
        print(f"  {'  ' * niveau}   📁 {filename}")

        # Variables locales au moment de l'erreur
        if niveau == 0:  # Frame de l'erreur
            print(f"  {'  ' * niveau}   🔍 Variables locales:")
            for var_name, var_value in frame.f_locals.items():
                if not var_name.startswith('__'):
                    print(f"  {'  ' * niveau}     {var_name} = {repr(var_value)}")

        tb = tb.tb_next
        niveau += 1

def diviser_avec_analyse(a, b):
    try:
        return a / b
    except Exception:
        analyser_erreur()
        raise

# Test
try:
    diviser_avec_analyse(10, 0)
except:
    pass
```

## Technique 6 : Débogage conditionnel

### Points d'arrêt conditionnels

```python
DEBUG = True

def debug_if(condition, message):
    """Debug seulement si la condition est vraie"""
    if DEBUG and condition:
        print(f"🔍 DEBUG: {message}")

def traiter_liste(nombres):
    total = 0
    for i, nombre in enumerate(nombres):
        debug_if(nombre < 0, f"Nombre négatif détecté à l'index {i}: {nombre}")
        debug_if(nombre > 100, f"Nombre très grand à l'index {i}: {nombre}")
        debug_if(i == len(nombres) - 1, f"Dernier élément traité: {nombre}")

        total += nombre

    return total

# Test
resultat = traiter_liste([5, -2, 150, 30])
```

### Débogage par contexte

```python
class DebugContext:
    """Gestionnaire de contexte pour le débogage"""

    def __init__(self, nom_operation):
        self.nom_operation = nom_operation
        self.start_time = None

    def __enter__(self):
        print(f"🚀 Début: {self.nom_operation}")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        duration = time.time() - self.start_time

        if exc_type is None:
            print(f"✅ Fin: {self.nom_operation} ({duration:.3f}s)")
        else:
            print(f"❌ Erreur dans {self.nom_operation}: {exc_value} ({duration:.3f}s)")

        return False  # Ne supprime pas l'exception

# Utilisation
def operation_complexe():
    with DebugContext("Calcul complexe"):
        time.sleep(0.1)  # Simulation
        resultat = sum(range(1000))
        return resultat

def operation_avec_erreur():
    with DebugContext("Opération problématique"):
        time.sleep(0.05)
        raise ValueError("Quelque chose s'est mal passé")

# Tests
operation_complexe()
try:
    operation_avec_erreur()
except ValueError:
    pass
```

## Outils visuels de débogage

### Utilisation dans VS Code

```python
# Pour déboguer dans VS Code:
# 1. Placez un point d'arrêt en cliquant à gauche du numéro de ligne
# 2. Appuyez sur F5 ou utilisez le menu "Run and Debug"
# 3. Utilisez les boutons pour naviguer:
#    - Continue (F5)
#    - Step Over (F10)
#    - Step Into (F11)
#    - Step Out (Shift+F11)

def exemple_debug_vscode():
    variables_locales = {"nom": "Alice", "age": 30}

    for cle, valeur in variables_locales.items():
        # Point d'arrêt ici pour examiner les variables
        resultat = f"{cle}: {valeur}"
        print(resultat)

    return variables_locales

exemple_debug_vscode()
```

## Stratégies de débogage

### 1. La méthode de bissection

```python
def recherche_bug_bissection():
    """
    Stratégie: commenter/décommenter des parties du code
    pour isoler le problème
    """

    # Partie 1 - ça marche
    donnees = [1, 2, 3, 4, 5]
    print("✅ Données créées")

    # Partie 2 - à tester
    donnees_transformees = [x * 2 for x in donnees]
    print("✅ Transformation réussie")

    # Partie 3 - le problème est peut-être ici ?
    # resultat = sum(donnees_transformees) / 0  # Bug ici !
    resultat = sum(donnees_transformees) / len(donnees_transformees)
    print(f"✅ Résultat: {resultat}")

    return resultat
```

### 2. Le rubber duck debugging

```python
def expliquer_au_canard():
    """
    Technique: expliquez votre code ligne par ligne
    à un canard en plastique (ou à vous-même)
    """

    print("🦆 Canard, je vais t'expliquer ce code...")

    # Étape 1: je crée une liste
    print("🦆 D'abord, je crée une liste de nombres")
    nombres = [1, 2, 3, 4, 5]

    # Étape 2: je calcule la somme
    print("🦆 Ensuite, je calcule la somme...")
    total = sum(nombres)
    print(f"🦆 La somme est {total}")

    # Étape 3: je calcule la moyenne
    print("🦆 Maintenant je calcule la moyenne...")
    # Ah ! Je viens de réaliser que je divise par la longueur
    # mais si la liste est vide, ça va planter !
    if len(nombres) == 0:
        print("🦆 Merci canard ! J'ai trouvé le problème !")
        return None

    moyenne = total / len(nombres)
    print(f"🦆 La moyenne est {moyenne}")

    return moyenne
```

## Exercices pratiques

### Exercice 1 : Debug d'une fonction de tri

```python
def tri_bulle_bugge(liste):
    """
    Cette fonction de tri à bulles contient des bugs.
    Utilisez les techniques de débogage pour les trouver !
    """
    n = len(liste)

    for i in range(n):
        for j in range(n - i - 1):
            # Bug potentiel ici ?
            if liste[j] < liste[j + 1]:  # Devrait être > pour tri croissant
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste

# Test
test_liste = [64, 34, 25, 12, 22, 11, 90]
print("Original:", test_liste)
resultat = tri_bulle_bugge(test_liste.copy())
print("Trié:", resultat)
# Attendu: [11, 12, 22, 25, 34, 64, 90]
```

### Exercice 2 : Debug d'un calculateur

```python
class CalculatriceDebug:
    def __init__(self):
        self.historique = []

    def calculer(self, operation):
        """
        Opération format: "5 + 3" ou "10 * 2"
        Cette fonction contient plusieurs bugs !
        """
        parties = operation.split()

        # Bug 1: que se passe-t-il si l'opération est mal formatée ?
        a = int(parties[0])
        operateur = parties[1]
        b = int(parties[2])

        # Bug 2: division par zéro non gérée
        if operateur == "+":
            resultat = a + b
        elif operateur == "-":
            resultat = a - b
        elif operateur == "*":
            resultat = a * b
        elif operateur == "/":
            resultat = a / b  # Division par zéro possible !

        # Bug 3: l'historique n'est jamais nettoyé
        self.historique.append(f"{operation} = {resultat}")

        return resultat

# Tests pour identifier les bugs
calc = CalculatriceDebug()
try:
    print(calc.calculer("5 + 3"))
    print(calc.calculer("10 / 0"))  # Bug !
    print(calc.calculer("5 +"))      # Bug !
except Exception as e:
    print(f"Erreur: {e}")
```

## Résumé

Les techniques de débogage sont vos outils de détective :

### **Techniques de base :**
1. **Print debugging** - Simple et efficace pour débuter
2. **Logging** - Plus professionnel et configurable
3. **Assertions** - Vérifications automatiques

### **Techniques avancées :**
4. **Débogueur pdb** - Contrôle total de l'exécution
5. **Analyse de traceback** - Comprendre les erreurs
6. **Débogage conditionnel** - Cibler les problèmes

### **Stratégies :**
- **Bissection** : diviser le problème en deux
- **Rubber duck** : expliquer le code pour clarifier
- **Outils visuels** : IDE avec débogueur intégré

### **Conseils pratiques :**
- Reproduisez le bug de manière consistante
- Simplifiez le code au maximum
- Vérifiez vos hypothèses avec des assertions
- Documentez vos découvertes
- N'ayez pas peur de recommencer

Le débogage devient plus facile avec l'expérience. Chaque bug résolu vous apprend quelque chose de nouveau !

Dans la section suivante, nous verrons comment optimiser les performances de votre code grâce au profiling.

---

**À retenir :** Un bon développeur n'est pas celui qui ne fait jamais de bugs, mais celui qui sait les trouver et les corriger efficacement !

⏭️
