🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.2 : Variables, types de données et opérateurs

## Introduction

Dans cette section, nous allons explorer les fondements de tout programme Python : les variables, les types de données et les opérateurs. Ces concepts sont essentiels pour stocker, manipuler et traiter les informations dans vos programmes.

## Les variables en Python

### Qu'est-ce qu'une variable ?

Une variable est comme une **boîte étiquetée** qui contient une valeur. Elle permet de stocker des données en mémoire et de les réutiliser dans votre programme.

### Création et assignation de variables

En Python, créer une variable est très simple :

```python
# Création de variables
nom = "Alice"
age = 25
taille = 1.65
est_etudiant = True

# Affichage des variables
print(nom)          # Alice
print(age)          # 25
print(taille)       # 1.65
print(est_etudiant) # True
```

💡 **Astuce** : En Python, pas besoin de déclarer le type de la variable, Python le détermine automatiquement !

### Règles de nommage des variables

#### Règles obligatoires
- Commencer par une lettre (a-z, A-Z) ou un underscore (_)
- Contenir uniquement des lettres, chiffres et underscores
- Être sensible à la casse (`nom` et `Nom` sont différents)
- Ne pas utiliser les mots-clés Python

```python
# ✅ Noms valides
nom = "Alice"
age_utilisateur = 25
_variable_privee = 10
nom2 = "Bob"

# ❌ Noms invalides
# 2nom = "Alice"      # Commence par un chiffre
# mon-nom = "Alice"   # Contient un tiret
# class = "Python"    # Mot-clé réservé
```

#### Conventions de nommage (PEP 8)

```python
# ✅ Style recommandé (snake_case)
nom_utilisateur = "Alice"
age_en_annees = 25
est_majeur = True

# ❌ Styles non recommandés
nomUtilisateur = "Alice"    # camelCase
NomUtilisateur = "Alice"    # PascalCase
```

### Types de variables

Python détermine automatiquement le type d'une variable :

```python
# Python détermine automatiquement le type
message = "Bonjour"        # str (chaîne de caractères)
compteur = 42              # int (entier)
prix = 19.99              # float (nombre décimal)
actif = True              # bool (booléen)

# Vérification du type
print(type(message))      # <class 'str'>
print(type(compteur))     # <class 'int'>
print(type(prix))         # <class 'float'>
print(type(actif))        # <class 'bool'>
```

## Les types de données fondamentaux

### 1. Les entiers (int)

Les entiers représentent des nombres entiers positifs ou négatifs :

```python
# Entiers positifs et négatifs
nombre_positif = 42
nombre_negatif = -17
zero = 0

# Entiers très grands (pas de limite en Python!)
grand_nombre = 123456789012345678901234567890

# Différentes bases
binaire = 0b1010        # Base 2 (binaire) = 10 en décimal
octal = 0o12           # Base 8 (octal) = 10 en décimal
hexadecimal = 0xA      # Base 16 (hexadécimal) = 10 en décimal

print(binaire, octal, hexadecimal)  # 10 10 10
```

### 2. Les nombres décimaux (float)

Les floats représentent des nombres à virgule :

```python
# Différentes façons d'écrire des floats
prix = 19.99
temperature = -5.5
pourcentage = 0.85

# Notation scientifique
petit_nombre = 1.5e-4    # 1.5 × 10^-4 = 0.00015
grand_nombre = 2.5e6     # 2.5 × 10^6 = 2500000.0

print(petit_nombre)      # 0.00015
print(grand_nombre)      # 2500000.0
```

⚠️ **Attention** : Les floats peuvent avoir des problèmes de précision :

```python
# Problème de précision des floats
resultat = 0.1 + 0.2
print(resultat)          # 0.30000000000000004 (pas exactement 0.3!)

# Solution pour les comparaisons
print(abs(resultat - 0.3) < 1e-10)  # True
```

### 3. Les chaînes de caractères (str)

Les chaînes représentent du texte :

```python
# Différentes façons de créer des chaînes
nom = "Alice"
prenom = 'Bob'
message = """Ceci est une chaîne
sur plusieurs lignes"""

# Chaînes vides
chaine_vide = ""
autre_vide = str()

# Échappement de caractères
citation = "Il a dit : \"Bonjour tout le monde!\""
chemin = "C:\\Users\\Alice\\Documents"
nouvelle_ligne = "Ligne 1\nLigne 2"

print(citation)
print(chemin)
print(nouvelle_ligne)
```

#### Opérations sur les chaînes

```python
prenom = "Alice"
nom = "Dupont"

# Concaténation
nom_complet = prenom + " " + nom
print(nom_complet)  # Alice Dupont

# Répétition
rires = "Ha" * 3
print(rires)        # HaHaHa

# Longueur
longueur = len(nom_complet)
print(longueur)     # 11

# Accès aux caractères (indexation)
premier_char = nom_complet[0]    # A
dernier_char = nom_complet[-1]   # t
print(premier_char, dernier_char)
```

#### Méthodes utiles des chaînes

```python
texte = "  Python est Génial  "

# Nettoyage
print(texte.strip())           # "Python est Génial"
print(texte.lower())           # "  python est génial  "
print(texte.upper())           # "  PYTHON EST GÉNIAL  "

# Recherche
print(texte.find("Python"))    # 2
print("Python" in texte)       # True

# Remplacement
nouveau_texte = texte.replace("Python", "Java")
print(nouveau_texte)           # "  Java est Génial  "

# Division
mots = "pomme,banane,orange".split(",")
print(mots)                    # ['pomme', 'banane', 'orange']
```

### 4. Les booléens (bool)

Les booléens représentent des valeurs de vérité :

```python
# Valeurs booléennes
vrai = True
faux = False

# Résultat de comparaisons
est_majeur = age >= 18
est_mineur = age < 18

print(est_majeur)    # True ou False selon l'âge
print(est_mineur)    # Opposé de est_majeur
```

#### Valeurs "truthy" et "falsy"

En Python, certaines valeurs sont considérées comme "fausses" :

```python
# Valeurs "falsy" (considérées comme False)
print(bool(0))           # False
print(bool(0.0))         # False
print(bool(""))          # False (chaîne vide)
print(bool([]))          # False (liste vide)
print(bool(None))        # False

# Valeurs "truthy" (considérées comme True)
print(bool(1))           # True
print(bool(-1))          # True
print(bool("hello"))     # True
print(bool([1, 2, 3]))   # True
```

## Les opérateurs

### Opérateurs arithmétiques

```python
a = 10
b = 3

# Opérateurs de base
addition = a + b        # 13
soustraction = a - b    # 7
multiplication = a * b  # 30
division = a / b        # 3.333...

# Opérateurs spéciaux
division_entiere = a // b    # 3 (division entière)
modulo = a % b              # 1 (reste de la division)
puissance = a ** b          # 1000 (10 puissance 3)

print(f"Addition: {addition}")
print(f"Division entière: {division_entiere}")
print(f"Modulo: {modulo}")
print(f"Puissance: {puissance}")
```

### Opérateurs de comparaison

```python
x = 5
y = 10

# Comparaisons
print(x == y)    # False (égalité)
print(x != y)    # True (différence)
print(x < y)     # True (inférieur)
print(x > y)     # False (supérieur)
print(x <= y)    # True (inférieur ou égal)
print(x >= y)    # False (supérieur ou égal)

# Comparaison de chaînes
nom1 = "Alice"
nom2 = "Bob"
print(nom1 == nom2)    # False
print(nom1 < nom2)     # True (ordre alphabétique)
```

### Opérateurs logiques

```python
# Variables booléennes
a = True
b = False

# Opérateurs logiques
print(a and b)    # False (ET logique)
print(a or b)     # True (OU logique)
print(not a)      # False (NON logique)
print(not b)      # True

# Exemples pratiques
age = 20
a_permis = True

peut_conduire = age >= 18 and a_permis
print(f"Peut conduire: {peut_conduire}")    # True

# Avec des nombres
x = 5
dans_plage = x >= 0 and x <= 10
print(f"Dans la plage [0,10]: {dans_plage}")    # True
```

### Opérateurs d'assignation

```python
# Assignation simple
x = 10

# Assignations composées
x += 5    # Équivaut à x = x + 5
print(x)  # 15

x -= 3    # Équivaut à x = x - 3
print(x)  # 12

x *= 2    # Équivaut à x = x * 2
print(x)  # 24

x /= 4    # Équivaut à x = x / 4
print(x)  # 6.0

x //= 2   # Équivaut à x = x // 2
print(x)  # 3.0

x %= 2    # Équivaut à x = x % 2
print(x)  # 1.0

x **= 3   # Équivaut à x = x ** 3
print(x)  # 1.0
```

## Conversion entre types (casting)

### Conversion explicite

```python
# Conversion vers entier
nombre_str = "42"
nombre_int = int(nombre_str)
print(nombre_int)           # 42
print(type(nombre_int))     # <class 'int'>

# Conversion vers float
nombre_float = float(nombre_str)
print(nombre_float)         # 42.0

# Conversion vers chaîne
age = 25
age_str = str(age)
print(age_str)              # "25"
print(type(age_str))        # <class 'str'>

# Conversion vers booléen
print(bool(1))              # True
print(bool(0))              # False
print(bool(""))             # False
print(bool("hello"))        # True
```

### Gestion des erreurs de conversion

```python
# Conversion qui peut échouer
try:
    nombre = int("abc")     # Erreur !
except ValueError:
    print("Impossible de convertir 'abc' en entier")

# Vérifier si une chaîne peut être convertie
chaine = "123"
if chaine.isdigit():
    nombre = int(chaine)
    print(f"Conversion réussie: {nombre}")
```

## Exemples pratiques

### Calculatrice simple

```python
# Calculatrice interactive
print("=== Calculatrice Simple ===")

# Saisie des nombres
a = float(input("Entrez le premier nombre: "))
b = float(input("Entrez le second nombre: "))

# Calculs
somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro impossible"

# Affichage des résultats
print(f"\nRésultats:")
print(f"{a} + {b} = {somme}")
print(f"{a} - {b} = {difference}")
print(f"{a} × {b} = {produit}")
print(f"{a} ÷ {b} = {quotient}")
```

### Gestion d'informations personnelles

```python
# Collecte d'informations
nom = input("Votre nom: ")
prenom = input("Votre prénom: ")
age = int(input("Votre âge: "))

# Traitement
nom_complet = prenom + " " + nom
est_majeur = age >= 18
annee_naissance = 2024 - age

# Affichage
print(f"\n=== Profil ===")
print(f"Nom complet: {nom_complet}")
print(f"Âge: {age} ans")
print(f"Année de naissance: {annee_naissance}")
print(f"Statut: {'Majeur' if est_majeur else 'Mineur'}")
```

## Formatage des chaînes

### Méthode format()

```python
nom = "Alice"
age = 25
taille = 1.65

# Méthode format()
message = "Je m'appelle {}, j'ai {} ans et je mesure {:.2f}m".format(nom, age, taille)
print(message)

# Avec des indices
message2 = "Je m'appelle {0}, j'ai {1} ans. Oui, {1} ans !".format(nom, age)
print(message2)

# Avec des noms
message3 = "Je m'appelle {prenom}, j'ai {age} ans".format(prenom=nom, age=age)
print(message3)
```

### f-strings (Python 3.6+) - Recommandé

```python
nom = "Alice"
age = 25
taille = 1.65

# f-strings (plus lisible et plus rapide)
message = f"Je m'appelle {nom}, j'ai {age} ans et je mesure {taille:.2f}m"
print(message)

# Avec des expressions
message2 = f"L'année prochaine, {nom} aura {age + 1} ans"
print(message2)

# Avec des méthodes
message3 = f"Nom en majuscules: {nom.upper()}"
print(message3)
```

## Exercices pratiques

### Exercice 1 : Variables et types

```python
# Créez des variables pour stocker :
# - Votre nom (chaîne)
# - Votre âge (entier)
# - Votre taille en mètres (float)
# - Si vous aimez Python (booléen)

# Affichez chaque variable et son type
```

### Exercice 2 : Calculatrice de pourboire

```python
# Calculatrice de pourboire
# Demandez à l'utilisateur :
# - Le montant de l'addition
# - Le pourcentage de pourboire souhaité
#
# Calculez et affichez :
# - Le montant du pourboire
# - Le total à payer
```

### Exercice 3 : Conversion d'unités

```python
# Convertisseur de température
# Demandez une température en Celsius
# Convertissez en Fahrenheit et Kelvin
# Formules :
# - Fahrenheit = (Celsius × 9/5) + 32
# - Kelvin = Celsius + 273.15
```

### Exercice 4 : Vérification de mot de passe

```python
# Vérificateur simple de mot de passe
# Demandez un mot de passe
# Vérifiez si :
# - Il contient au moins 8 caractères
# - Il contient à la fois des majuscules et minuscules
# - Il contient des chiffres
#
# Affichez si le mot de passe est valide ou non
```

## Bonnes pratiques

### Nommage des variables

```python
# ✅ Bon : noms explicites
prix_unitaire = 19.99
nombre_articles = 3
prix_total = prix_unitaire * nombre_articles

# ❌ Mauvais : noms peu clairs
p = 19.99
n = 3
t = p * n
```

### Constantes

```python
# Convention : constantes en majuscules
PI = 3.14159
VITESSE_LUMIERE = 299792458  # m/s
TVA = 0.20

# Utilisation
rayon = 5
aire_cercle = PI * rayon ** 2
```

### Lisibilité du code

```python
# ✅ Bon : code lisible
age_utilisateur = 25
est_majeur = age_utilisateur >= 18
message = f"L'utilisateur est {'majeur' if est_majeur else 'mineur'}"

# ❌ Mauvais : code condensé mais illisible
message = f"L'utilisateur est {'majeur' if int(input('Âge: ')) >= 18 else 'mineur'}"
```

## Pièges courants à éviter

### 1. Confusion entre = et ==

```python
# ❌ Erreur : assignation au lieu de comparaison
age = 18
if age = 18:    # SyntaxError !
    print("Majeur")

# ✅ Correct : comparaison
if age == 18:
    print("Majeur")
```

### 2. Division par zéro

```python
# ❌ Erreur potentielle
a = 10
b = 0
resultat = a / b    # ZeroDivisionError !

# ✅ Correct : vérification
if b != 0:
    resultat = a / b
    print(f"Résultat: {resultat}")
else:
    print("Division par zéro impossible")
```

### 3. Conversion de types

```python
# ❌ Erreur : conversion impossible
age_str = "vingt-cinq"
age = int(age_str)    # ValueError !

# ✅ Correct : validation
try:
    age = int(input("Votre âge: "))
except ValueError:
    print("Veuillez entrer un nombre valide")
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ **Variables** : création, nommage et bonnes pratiques
✅ **Types de données** : int, float, str, bool
✅ **Opérateurs** : arithmétiques, comparaison, logiques, assignation
✅ **Conversion** : casting entre types
✅ **Formatage** : f-strings et méthode format()
✅ **Bonnes pratiques** : nommage, lisibilité, gestion d'erreurs

**Concepts clés à retenir :**
- Python détermine automatiquement le type des variables
- Les f-strings sont la méthode recommandée pour le formatage
- Toujours vérifier les divisions par zéro
- Utiliser des noms de variables explicites
- Attention aux conversions de types

**Prochaine étape** : Dans la section 1.3, nous découvrirons les structures de contrôle pour donner de la logique à nos programmes !

---

💡 **Conseil** : Pratiquez avec les exercices proposés. La manipulation des variables et des types est fondamentale en programmation !

⏭️
