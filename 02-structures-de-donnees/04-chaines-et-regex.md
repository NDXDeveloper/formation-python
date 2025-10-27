🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.4 Manipulation de Chaînes de Caractères et Expressions Régulières

## Introduction

Les chaînes de caractères (ou *strings*) sont l'un des types de données les plus utilisés en programmation. Que ce soit pour traiter du texte, manipuler des fichiers, ou interagir avec des API, vous travaillerez constamment avec des chaînes.

Dans cette section, nous allons explorer :
- Les opérations de base sur les chaînes
- Les méthodes puissantes pour manipuler du texte
- Le formatage moderne des chaînes
- Les expressions régulières pour la recherche de motifs complexes

---

## Partie 1 : Manipulation de Chaînes de Caractères

### Créer des chaînes

En Python, les chaînes peuvent être créées avec des guillemets simples, doubles, ou triples.

```python
# Guillemets simples
chaine1 = 'Bonjour'

# Guillemets doubles
chaine2 = "Python"

# Triple guillemets (pour les chaînes multi-lignes)
chaine3 = """Ceci est une chaîne
qui s'étend sur
plusieurs lignes"""

chaine4 = '''Fonctionne aussi
avec des guillemets simples triples'''

print(chaine3)
```

**Caractères spéciaux :**

```python
# Nouvelle ligne
print("Ligne 1\nLigne 2")

# Tabulation
print("Colonne1\tColonne2")

# Guillemets dans une chaîne
print("Il a dit : \"Bonjour\"")
print('C\'est génial')

# Backslash
print("Chemin : C:\\Users\\Python")

# Chaînes brutes (ignorent les séquences d'échappement)
print(r"C:\Users\nouveau\fichier.txt")  # Le 'r' rend la chaîne "raw"
```

### Concaténation et répétition

```python
# Concaténation avec +
prenom = "Marie"
nom = "Dupont"
nom_complet = prenom + " " + nom
print(nom_complet)  # Marie Dupont

# Répétition avec *
ligne = "=" * 50
print(ligne)  # ==================================================

# Concaténation implicite (seulement pour les littéraux)
message = "Bonjour " "tout " "le monde"
print(message)  # Bonjour tout le monde
```

### Indexation et slicing

Les chaînes sont indexées comme les listes.

```python
texte = "Python"

# Indexation
print(texte[0])   # P
print(texte[2])   # t
print(texte[-1])  # n (dernier caractère)
print(texte[-2])  # o (avant-dernier)

# Slicing
print(texte[0:3])   # Pyt (indices 0, 1, 2)
print(texte[:4])    # Pyth (du début à l'indice 3)
print(texte[2:])    # thon (de l'indice 2 à la fin)
print(texte[::2])   # Pto (un caractère sur deux)
print(texte[::-1])  # nohtyP (inverse la chaîne)

# Les chaînes sont IMMUABLES
# texte[0] = 'J'  # TypeError: 'str' object does not support item assignment
```

### Longueur et appartenance

```python
texte = "Python est génial"

# Longueur
print(len(texte))  # 17

# Vérifier si un caractère ou sous-chaîne est présent
print('P' in texte)        # True
print('Java' in texte)     # False
print('Python' in texte)   # True
print('est' not in texte)  # False
```

---

## Méthodes de Chaînes

Python offre de nombreuses méthodes pour manipuler les chaînes. Les chaînes étant immuables, ces méthodes retournent une nouvelle chaîne.

### Changement de casse

```python
texte = "Python Programming"

print(texte.upper())       # PYTHON PROGRAMMING
print(texte.lower())       # python programming
print(texte.capitalize())  # Python programming (première lettre en majuscule)
print(texte.title())       # Python Programming (première de chaque mot)
print(texte.swapcase())    # pYTHON pROGRAMMING (inverse la casse)

# Vérifications
print("PYTHON".isupper())  # True
print("python".islower())  # True
print("Python".istitle())  # True
```

### Recherche et remplacement

```python
texte = "Python est un langage Python"

# Trouver une sous-chaîne
print(texte.find('Python'))        # 0 (première occurrence)
print(texte.find('Java'))          # -1 (non trouvé)
print(texte.find('Python', 1))     # 26 (chercher après l'indice 1)

# Index (comme find, mais lève une erreur si non trouvé)
print(texte.index('Python'))       # 0
# print(texte.index('Java'))       # ValueError

# Compter les occurrences
print(texte.count('Python'))       # 2
print(texte.count('est'))          # 1

# Vérifier le début et la fin
print(texte.startswith('Python'))  # True
print(texte.startswith('Java'))    # False
print(texte.endswith('Python'))    # True
print(texte.endswith('langage'))   # False

# Remplacer
nouveau = texte.replace('Python', 'Java')
print(nouveau)  # Java est un langage Java

# Remplacer avec limite de nombre de remplacements
nouveau = texte.replace('Python', 'Java', 1)
print(nouveau)  # Java est un langage Python (seule la première occurrence)
```

### Nettoyage des chaînes

```python
texte = "   Python   "

# Supprimer les espaces au début et à la fin
print(texte.strip())       # "Python"
print(texte.lstrip())      # "Python   " (gauche seulement)
print(texte.rstrip())      # "   Python" (droite seulement)

# Supprimer des caractères spécifiques
texte2 = "***Python***"
print(texte2.strip('*'))   # "Python"

texte3 = "https://example.com"
print(texte3.strip('https://'))  # "example.com"

# Supprimer les caractères de début/fin
url = "www.example.com"
print(url.removeprefix('www.'))  # "example.com" (Python 3.9+)
print(url.removesuffix('.com'))  # "www.example" (Python 3.9+)
```

### Division et jointure

```python
# Split - diviser une chaîne
texte = "Python est un langage génial"
mots = texte.split()  # Split sur les espaces par défaut
print(mots)  # ['Python', 'est', 'un', 'langage', 'génial']

# Split avec séparateur personnalisé
csv = "nom,prenom,age"
donnees = csv.split(',')
print(donnees)  # ['nom', 'prenom', 'age']

# Limiter le nombre de splits
texte2 = "un:deux:trois:quatre"
parties = texte2.split(':', 2)
print(parties)  # ['un', 'deux', 'trois:quatre']

# Split sur les lignes
paragraphe = """Ligne 1
Ligne 2
Ligne 3"""
lignes = paragraphe.splitlines()
print(lignes)  # ['Ligne 1', 'Ligne 2', 'Ligne 3']

# Join - joindre des éléments
mots = ['Python', 'est', 'génial']
phrase = ' '.join(mots)
print(phrase)  # "Python est génial"

# Join avec différents séparateurs
print('-'.join(mots))    # "Python-est-génial"
print(''.join(mots))     # "Pythonestgénial"
print('\n'.join(mots))   # Chaque mot sur une ligne

# Join avec des nombres (convertir d'abord)
nombres = [1, 2, 3, 4]
resultat = ', '.join(str(n) for n in nombres)
print(resultat)  # "1, 2, 3, 4"
```

### Vérifications de type de caractères

```python
# Vérifier si alphanumérique
print("Python3".isalnum())   # True
print("Python 3".isalnum())  # False (à cause de l'espace)

# Vérifier si alphabétique
print("Python".isalpha())    # True
print("Python3".isalpha())   # False

# Vérifier si numérique
print("12345".isdigit())     # True
print("123.45".isdigit())    # False

# Vérifier si décimal
print("12345".isdecimal())   # True
print("½".isdecimal())       # False

# Vérifier si espaces
print("   ".isspace())       # True
print("  a ".isspace())      # False
```

### Alignement et remplissage

```python
texte = "Python"

# Centrer
print(texte.center(20))       # "       Python       "
print(texte.center(20, '*'))  # "*******Python*******"

# Aligner à gauche
print(texte.ljust(20))        # "Python              "
print(texte.ljust(20, '-'))   # "Python--------------"

# Aligner à droite
print(texte.rjust(20))        # "              Python"
print(texte.rjust(20, '.'))   # "..............Python"

# Remplir avec des zéros (utile pour les nombres)
nombre = "42"
print(nombre.zfill(5))        # "00042"
print("-42".zfill(5))         # "-0042"
```

### Partition

```python
# Diviser en 3 parties : avant, séparateur, après
email = "utilisateur@example.com"
avant, sep, apres = email.partition('@')
print(avant)  # "utilisateur"
print(sep)    # "@"
print(apres)  # "example.com"

# rpartition - partir de la droite
chemin = "dossier/sous-dossier/fichier.txt"
dossiers, sep, fichier = chemin.rpartition('/')
print(dossiers)  # "dossier/sous-dossier"
print(fichier)   # "fichier.txt"
```

---

## Formatage de Chaînes

Le formatage permet d'insérer des valeurs dans des chaînes de manière élégante.

### 1. f-strings (méthode moderne - Python 3.6+)

Les f-strings sont la méthode recommandée aujourd'hui.

```python
# Syntaxe de base
nom = "Alice"
age = 25
message = f"Je m'appelle {nom} et j'ai {age} ans"
print(message)  # Je m'appelle Alice et j'ai 25 ans

# Expressions dans les f-strings
x = 10
y = 20
print(f"La somme de {x} et {y} est {x + y}")  # La somme de 10 et 20 est 30

# Appeler des méthodes
texte = "python"
print(f"{texte.upper()} est génial")  # PYTHON est génial

# Formatage des nombres
pi = 3.14159
print(f"Pi vaut environ {pi:.2f}")    # Pi vaut environ 3.14
print(f"Pi avec 4 décimales : {pi:.4f}")  # Pi avec 4 décimales : 3.1416

# Largeur et alignement
print(f"{'Gauche':<10}|")   # "Gauche    |"
print(f"{'Centre':^10}|")   # "  Centre  |"
print(f"{'Droite':>10}|")   # "    Droite|"

# Formatage avec séparateurs de milliers
nombre = 1234567
print(f"Population : {nombre:,}")      # Population : 1,234,567
print(f"Population : {nombre:_}")      # Population : 1_234_567

# Pourcentages
ratio = 0.857
print(f"Taux de réussite : {ratio:.1%}")  # Taux de réussite : 85.7%

# Notation scientifique
grand_nombre = 1234567890
print(f"{grand_nombre:e}")  # 1.234568e+09

# Padding avec des zéros
numero = 42
print(f"Numéro : {numero:05d}")  # Numéro : 00042
```

### 2. Méthode format() (ancienne méthode, toujours valide)

```python
# Avec indices
print("{0} et {1}".format("Python", "Java"))  # Python et Java
print("{1} et {0}".format("Python", "Java"))  # Java et Python

# Avec noms
print("{langage} est {adjectif}".format(langage="Python", adjectif="génial"))

# Formatage des nombres
pi = 3.14159
print("Pi vaut {:.2f}".format(pi))  # Pi vaut 3.14

# Avec des dictionnaires
personne = {"nom": "Alice", "age": 25}
print("Nom : {nom}, Age : {age}".format(**personne))
```

### 3. Opérateur % (ancienne méthode, déconseillée)

```python
# Style C
nom = "Alice"
age = 25
print("Nom : %s, Age : %d" % (nom, age))  # Nom : Alice, Age : 25

# Avec dictionnaire
print("Nom : %(nom)s, Age : %(age)d" % {"nom": "Alice", "age": 25})
```

### Formatage avancé avec f-strings

```python
# Dates
from datetime import datetime
maintenant = datetime.now()
print(f"Date : {maintenant:%Y-%m-%d}")       # Date : 2025-10-27
print(f"Heure : {maintenant:%H:%M:%S}")      # Heure : 14:30:45

# Affichage en binaire, octal, hexadécimal
nombre = 42
print(f"Binaire : {nombre:b}")    # Binaire : 101010
print(f"Octal : {nombre:o}")      # Octal : 52
print(f"Hexadécimal : {nombre:x}") # Hexadécimal : 2a

# Debug (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")  # x=10, y=20

# Chaînes multi-lignes
nom = "Alice"
age = 25
ville = "Paris"
info = f"""
Informations:
  Nom: {nom}
  Age: {age}
  Ville: {ville}
"""
print(info)
```

---

## Partie 2 : Expressions Régulières

### Introduction aux expressions régulières

Les **expressions régulières** (ou *regex*) sont un langage puissant pour rechercher et manipuler des motifs dans du texte. Elles permettent de :
- Valider des formats (emails, téléphones, etc.)
- Extraire des informations spécifiques
- Remplacer des motifs complexes
- Diviser des chaînes selon des règles avancées

**Pour utiliser les regex en Python, il faut importer le module `re` :**

```python
import re
```

### Syntaxe de base des patterns

Voici les symboles et patterns les plus courants :

| Pattern | Signification | Exemple |
|---------|---------------|---------|
| `.` | N'importe quel caractère (sauf nouvelle ligne) | `a.c` → "abc", "adc" |
| `^` | Début de la chaîne | `^Python` → chaîne commençant par "Python" |
| `$` | Fin de la chaîne | `Python$` → chaîne finissant par "Python" |
| `*` | 0 ou plusieurs occurrences | `ab*c` → "ac", "abc", "abbc" |
| `+` | 1 ou plusieurs occurrences | `ab+c` → "abc", "abbc" (pas "ac") |
| `?` | 0 ou 1 occurrence | `ab?c` → "ac", "abc" |
| `{n}` | Exactement n occurrences | `a{3}` → "aaa" |
| `{n,}` | Au moins n occurrences | `a{2,}` → "aa", "aaa", "aaaa" |
| `{n,m}` | Entre n et m occurrences | `a{2,4}` → "aa", "aaa", "aaaa" |
| `[]` | Ensemble de caractères | `[abc]` → "a", "b", ou "c" |
| `[^]` | Négation | `[^abc]` → tout sauf "a", "b", "c" |
| `\|` | Ou logique | `cat\|dog` → "cat" ou "dog" |
| `()` | Groupe de capture | `(ab)+` → "ab", "abab" |
| `\d` | Chiffre [0-9] | `\d{3}` → 3 chiffres |
| `\D` | Non-chiffre | |
| `\w` | Caractère alphanumérique [a-zA-Z0-9_] | |
| `\W` | Non-alphanumérique | |
| `\s` | Espace blanc (espace, tab, newline) | |
| `\S` | Non-espace blanc | |

### Méthodes du module re

#### 1. re.search() - Trouver la première occurrence

```python
import re

texte = "J'apprends Python depuis 2020"

# Chercher un motif
resultat = re.search(r'\d+', texte)  # Cherche un ou plusieurs chiffres

if resultat:
    print("Trouvé :", resultat.group())  # "2020"
    print("Position :", resultat.start()) # 26
    print("Fin :", resultat.end())       # 30
else:
    print("Non trouvé")
```

**Note :** Le préfixe `r` avant la chaîne crée une "raw string", ce qui évite les problèmes avec les backslashes.

#### 2. re.match() - Vérifier le début de la chaîne

```python
import re

texte = "Python est génial"

# match() cherche seulement au début de la chaîne
resultat = re.match(r'Python', texte)
if resultat:
    print("Commence par Python")  # ✓

resultat = re.match(r'génial', texte)
if resultat:
    print("Commence par génial")  # Ne s'affiche pas
else:
    print("Ne commence pas par génial")
```

#### 3. re.findall() - Trouver toutes les occurrences

```python
import re

texte = "Les numéros de téléphone sont : 0123456789 et 0987654321"

# Trouver tous les nombres
numeros = re.findall(r'\d+', texte)
print(numeros)  # ['0123456789', '0987654321']

# Trouver tous les mots
texte2 = "Python, Java, JavaScript"
langages = re.findall(r'\w+', texte2)
print(langages)  # ['Python', 'Java', 'JavaScript']
```

#### 4. re.finditer() - Iterator sur les correspondances

```python
import re

texte = "Python 3.9, Java 11, C++ 17"

# Obtenir un iterator
for match in re.finditer(r'\d+', texte):
    print(f"Trouvé '{match.group()}' à la position {match.start()}")
# Trouvé '3' à la position 7
# Trouvé '9' à la position 9
# Trouvé '11' à la position 17
# Trouvé '17' à la position 24
```

#### 5. re.sub() - Remplacer

```python
import re

texte = "Il y a 123 pommes et 456 oranges"

# Remplacer tous les nombres par 'X'
nouveau = re.sub(r'\d+', 'X', texte)
print(nouveau)  # "Il y a X pommes et X oranges"

# Avec une fonction de remplacement
def doubler(match):
    nombre = int(match.group())
    return str(nombre * 2)

nouveau = re.sub(r'\d+', doubler, texte)
print(nouveau)  # "Il y a 246 pommes et 912 oranges"
```

#### 6. re.split() - Diviser

```python
import re

# Split sur les espaces (multiple)
texte = "un    deux  trois     quatre"
mots = re.split(r'\s+', texte)
print(mots)  # ['un', 'deux', 'trois', 'quatre']

# Split sur plusieurs séparateurs
texte2 = "un,deux;trois:quatre"
parties = re.split(r'[,;:]', texte2)
print(parties)  # ['un', 'deux', 'trois', 'quatre']

# Split avec limite
texte3 = "a-b-c-d-e"
parties = re.split(r'-', texte3, maxsplit=2)
print(parties)  # ['a', 'b', 'c-d-e']
```

### Groupes de capture

Les parenthèses `()` créent des groupes qui peuvent être extraits séparément.

```python
import re

# Extraire le nom et le domaine d'un email
email = "utilisateur@example.com"
match = re.search(r'(\w+)@(\w+\.\w+)', email)

if match:
    print("Email complet :", match.group(0))  # utilisateur@example.com
    print("Nom :", match.group(1))            # utilisateur
    print("Domaine :", match.group(2))        # example.com
    print("Tous les groupes :", match.groups())  # ('utilisateur', 'example.com')

# Groupes nommés
match = re.search(r'(?P<nom>\w+)@(?P<domaine>\w+\.\w+)', email)
if match:
    print("Nom :", match.group('nom'))        # utilisateur
    print("Domaine :", match.group('domaine'))  # example.com
    print("Dict :", match.groupdict())  # {'nom': 'utilisateur', 'domaine': 'example.com'}
```

### Compilation de patterns

Pour des performances optimales, compilez les patterns que vous utilisez souvent.

```python
import re

# Sans compilation (recherche multiple = recompilation à chaque fois)
texte1 = "Python 3.9"
texte2 = "Java 11"
re.findall(r'\d+', texte1)
re.findall(r'\d+', texte2)

# Avec compilation (meilleure performance)
pattern = re.compile(r'\d+')
resultat1 = pattern.findall(texte1)
resultat2 = pattern.findall(texte2)

print(resultat1)  # ['3', '9']
print(resultat2)  # ['11']
```

### Drapeaux (flags)

Les drapeaux modifient le comportement des regex.

```python
import re

texte = "Python\nest\nGénial"

# re.IGNORECASE ou re.I - Ignorer la casse
print(re.findall(r'python', texte, re.IGNORECASE))  # ['Python']

# re.MULTILINE ou re.M - ^ et $ correspondent au début/fin de chaque ligne
print(re.findall(r'^[a-z]+', texte, re.MULTILINE | re.IGNORECASE))
# ['Python', 'est', 'Génial']

# re.DOTALL ou re.S - . correspond aussi aux nouvelles lignes
print(re.findall(r'Python.+Génial', texte))         # [] (ne trouve pas)
print(re.findall(r'Python.+Génial', texte, re.DOTALL))  # ['Python\nest\nGénial']

# Combiner plusieurs flags avec |
pattern = re.compile(r'python', re.IGNORECASE | re.MULTILINE)
```

---

## Cas d'Usage Pratiques

### 1. Validation d'email

```python
import re

def valider_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Tests
emails = [
    "utilisateur@example.com",    # ✓
    "nom.prenom@example.fr",      # ✓
    "invalide@.com",              # ✗
    "pas-un-email",               # ✗
    "test@example.co.uk"          # ✓
]

for email in emails:
    print(f"{email}: {'✓' if valider_email(email) else '✗'}")
```

### 2. Extraction de numéros de téléphone

```python
import re

texte = """
Contactez-nous:
Bureau: 01-23-45-67-89
Mobile: 06.12.34.56.78
Support: 0987654321
"""

# Pattern pour différents formats
patterns = [
    r'\d{2}-\d{2}-\d{2}-\d{2}-\d{2}',  # Format: 01-23-45-67-89
    r'\d{2}\.\d{2}\.\d{2}\.\d{2}\.\d{2}',  # Format: 01.23.45.67.89
    r'\d{10}'  # Format: 0123456789
]

for pattern in patterns:
    telephones = re.findall(pattern, texte)
    if telephones:
        print(f"Trouvés avec le pattern '{pattern}':", telephones)
```

### 3. Nettoyage de texte

```python
import re

texte = "   Python    est    un    langage    génial!!!   "

# Supprimer les espaces multiples
texte_nettoye = re.sub(r'\s+', ' ', texte)
print(texte_nettoye.strip())  # "Python est un langage génial!!!"

# Supprimer la ponctuation excessive
texte_nettoye = re.sub(r'[!?]{2,}', '.', texte_nettoye)
print(texte_nettoye)  # "Python est un langage génial."

# Supprimer tous les caractères non-alphanumériques sauf espaces
texte = "Python@2024! est #1"
texte_nettoye = re.sub(r'[^\w\s]', '', texte)
print(texte_nettoye)  # "Python2024 est 1"
```

### 4. Extraction d'URLs

```python
import re

texte = """
Visitez notre site : https://example.com
Documentation : http://docs.example.com/guide
Ou contactez-nous via email
"""

# Pattern pour URLs
pattern = r'https?://[^\s]+'
urls = re.findall(pattern, texte)

for url in urls:
    print(f"URL trouvée : {url}")
# URL trouvée : https://example.com
# URL trouvée : http://docs.example.com/guide
```

### 5. Parsing de logs

```python
import re

log = """
2024-10-27 14:30:15 ERROR Connection timeout
2024-10-27 14:31:22 INFO User login successful
2024-10-27 14:32:05 WARNING Low memory
2024-10-27 14:33:18 ERROR Database connection failed
"""

# Extraire les entrées d'erreur
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR) (.+)'

erreurs = re.findall(pattern, log)

print("Erreurs trouvées :")
for date, niveau, message in erreurs:
    print(f"  [{date}] {message}")
# Erreurs trouvées :
#   [2024-10-27 14:30:15] Connection timeout
#   [2024-10-27 14:33:18] Database connection failed
```

### 6. Validation de mot de passe

```python
import re

def valider_mot_de_passe(mdp):
    """
    Règles:
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial
    """
    if len(mdp) < 8:
        return False, "Doit contenir au moins 8 caractères"

    if not re.search(r'[A-Z]', mdp):
        return False, "Doit contenir au moins une majuscule"

    if not re.search(r'[a-z]', mdp):
        return False, "Doit contenir au moins une minuscule"

    if not re.search(r'\d', mdp):
        return False, "Doit contenir au moins un chiffre"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', mdp):
        return False, "Doit contenir au moins un caractère spécial"

    return True, "Mot de passe valide"

# Tests
mots_de_passe = [
    "faible",
    "Faible123",
    "Faible123!",
    "F@ible1"
]

for mdp in mots_de_passe:
    valide, message = valider_mot_de_passe(mdp)
    print(f"{mdp}: {message}")
```

### 7. Extraction de données structurées

```python
import re

# Extraire des informations d'une facture
facture = """
Facture N° 2024-001
Date: 27/10/2024
Client: Marie Dupont
Total: 1,234.56 EUR
"""

# Extraire le numéro de facture
numero = re.search(r'N° (\d{4}-\d{3})', facture)
print(f"Numéro : {numero.group(1)}")  # 2024-001

# Extraire la date
date = re.search(r'Date: (\d{2}/\d{2}/\d{4})', facture)
print(f"Date : {date.group(1)}")  # 27/10/2024

# Extraire le montant
montant = re.search(r'Total: ([\d,]+\.?\d*)', facture)
print(f"Montant : {montant.group(1)}")  # 1,234.56
```

### 8. Remplacer avec des groupes de capture

```python
import re

# Formater des dates
texte = "Les dates importantes sont : 2024/10/27 et 2024/12/25"

# Convertir du format YYYY/MM/DD au format DD-MM-YYYY
nouveau = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\3-\2-\1', texte)
print(nouveau)
# "Les dates importantes sont : 27-10-2024 et 25-12-2024"

# Anonymiser des emails
texte = "Contactez alice@example.com ou bob@test.com"
anonymise = re.sub(r'(\w+)@(\w+\.\w+)', r'****@\2', texte)
print(anonymise)
# "Contactez ****@example.com ou ****@test.com"
```

### 9. Validation de formats divers

```python
import re

def valider_code_postal_fr(code):
    """Code postal français : 5 chiffres"""
    return re.match(r'^\d{5}$', code) is not None

def valider_plaque_immatriculation_fr(plaque):
    """Format : AB-123-CD"""
    return re.match(r'^[A-Z]{2}-\d{3}-[A-Z]{2}$', plaque) is not None

def valider_isbn(isbn):
    """ISBN-10 ou ISBN-13"""
    pattern = r'^(?:\d{9}[\dX]|\d{13})$'
    isbn_clean = isbn.replace('-', '').replace(' ', '')
    return re.match(pattern, isbn_clean) is not None

# Tests
print(valider_code_postal_fr("75001"))  # True
print(valider_code_postal_fr("7500"))   # False

print(valider_plaque_immatriculation_fr("AB-123-CD"))  # True
print(valider_plaque_immatriculation_fr("AB123CD"))    # False

print(valider_isbn("978-0-13-110362-7"))  # True
print(valider_isbn("0-13-110362-8"))      # True
```

### 10. Traitement de texte avancé

```python
import re

# Extraire les hashtags d'un tweet
tweet = "J'adore #Python et #Programming ! #Dev #Code"
hashtags = re.findall(r'#(\w+)', tweet)
print("Hashtags :", hashtags)  # ['Python', 'Programming', 'Dev', 'Code']

# Extraire les mentions
texte = "Merci @Alice et @Bob pour votre aide !"
mentions = re.findall(r'@(\w+)', texte)
print("Mentions :", mentions)  # ['Alice', 'Bob']

# Camel case vers snake case
def camel_to_snake(nom):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', nom).lower()

print(camel_to_snake("MonNomDeVariable"))  # mon_nom_de_variable
print(camel_to_snake("HTTPServer"))        # h_t_t_p_server

# Snake case vers camel case
def snake_to_camel(nom):
    components = nom.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("mon_nom_de_variable"))  # monNomDeVariable
```

---

## Patterns Courants

Voici une collection de patterns regex utiles :

```python
import re

# Email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# URL
url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

# Numéro de téléphone français
tel_fr_pattern = r'^(?:0|\+33)[1-9](?:[0-9]{2}){4}$'

# Date (format DD/MM/YYYY)
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

# Code postal français
code_postal_pattern = r'^\d{5}$'

# IPv4
ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# Heure (format HH:MM)
heure_pattern = r'^([01][0-9]|2[0-3]):[0-5][0-9]$'

# Numéro de carte bancaire (espaces optionnels)
carte_pattern = r'^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$'

# Couleur hexadécimale
hex_color_pattern = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
```

---

## Bonnes Pratiques

### 1. Utilisez des raw strings

Toujours préfixer vos patterns avec `r` pour éviter les problèmes avec les backslashes.

```python
# ❌ Mauvais
pattern = "\\d+"

# ✅ Bon
pattern = r"\d+"
```

### 2. Compilez les patterns réutilisés

```python
# ❌ Moins efficace si utilisé souvent
for texte in grande_liste:
    re.search(r'\d+', texte)

# ✅ Plus efficace
pattern = re.compile(r'\d+')
for texte in grande_liste:
    pattern.search(texte)
```

### 3. Utilisez des groupes nommés pour la clarté

```python
# ❌ Moins lisible
pattern = r'(\d{4})-(\d{2})-(\d{2})'

# ✅ Plus lisible
pattern = r'(?P<annee>\d{4})-(?P<mois>\d{2})-(?P<jour>\d{2})'
```

### 4. Commentez les regex complexes

```python
# Pattern complexe pour email avec commentaires
email_pattern = r'''
    ^                    # Début de la chaîne
    [a-zA-Z0-9._%+-]+   # Nom d'utilisateur
    @                    # Arobase
    [a-zA-Z0-9.-]+      # Nom de domaine
    \.                   # Point
    [a-zA-Z]{2,}        # Extension (au moins 2 caractères)
    $                    # Fin de la chaîne
'''

# Compiler avec le flag VERBOSE pour ignorer les espaces et commentaires
pattern = re.compile(email_pattern, re.VERBOSE)
```

### 5. Testez vos regex

```python
import re

def tester_pattern(pattern, tests):
    """Fonction utilitaire pour tester des patterns"""
    compiled = re.compile(pattern)
    for texte, attendu in tests:
        resultat = compiled.match(texte) is not None
        status = "✓" if resultat == attendu else "✗"
        print(f"{status} {texte}: {resultat} (attendu: {attendu})")

# Tests pour un pattern d'email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

tests = [
    ("test@example.com", True),
    ("invalid.email", False),
    ("test@.com", False),
    ("test@example.co.uk", True)
]

tester_pattern(email_pattern, tests)
```

### 6. Attention aux performances

Les regex peuvent être lentes sur de grandes chaînes ou avec des patterns complexes. Pour des tâches simples, les méthodes de chaînes natives peuvent être plus rapides.

```python
# Pour une recherche simple
texte = "Python est génial"

# ❌ Overkill avec regex
import re
if re.search(r'Python', texte):
    print("Trouvé")

# ✅ Plus simple et rapide
if 'Python' in texte:
    print("Trouvé")
```

---

## Conclusion

Les chaînes de caractères sont au cœur de la programmation Python. Cette section vous a présenté :

**Manipulation de chaînes :**
- Les méthodes de base (upper, lower, strip, split, join, etc.)
- Le formatage moderne avec f-strings
- Les opérations courantes (recherche, remplacement, vérification)

**Expressions régulières :**
- La syntaxe des patterns
- Les méthodes du module `re` (search, match, findall, sub, etc.)
- Les groupes de capture et les drapeaux
- Des cas d'usage pratiques

**Points clés à retenir :**

1. Les chaînes sont **immuables** - les méthodes retournent de nouvelles chaînes
2. Les **f-strings** sont la méthode de formatage recommandée
3. Les **regex** sont puissantes mais complexes - utilisez-les quand nécessaire
4. Privilégiez les méthodes natives de chaînes pour les opérations simples
5. Testez toujours vos regex avec différents cas

Avec la pratique, vous développerez une intuition pour savoir quand utiliser une simple méthode de chaîne et quand sortir l'artillerie lourde des expressions régulières ! 🎯

⏭️ [Programmation orientée objet](/03-programmation-orientee-objet/README.md)
