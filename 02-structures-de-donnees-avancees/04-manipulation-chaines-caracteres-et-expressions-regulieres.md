🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.4 : Manipulation de chaînes de caractères et expressions régulières

## Introduction

Les chaînes de caractères (strings) sont l'un des types de données les plus utilisés en programmation. Python offre de nombreuses méthodes puissantes pour manipuler le texte, ainsi que les expressions régulières pour des traitements plus complexes.

Dans ce chapitre, nous verrons :
- Les méthodes essentielles pour manipuler les chaînes
- Le formatage de chaînes moderne
- Introduction aux expressions régulières
- Cas d'usage pratiques et exemples concrets

## Rappel : Bases des chaînes de caractères

### Création de chaînes

```python
# Différentes façons de créer des chaînes
nom = "Alice"
message = 'Bonjour le monde'
citation = """C'est une citation
sur plusieurs lignes"""
chemin = r"C:\Users\nom\Documents"  # Raw string (chaîne brute)

print(nom)      # Alice
print(message)  # Bonjour le monde
print(citation) # C'est une citation
                # sur plusieurs lignes
print(chemin)   # C:\Users\nom\Documents
```

### Caractères d'échappement

```python
# Caractères spéciaux
texte_avec_guillemets = "Il a dit : \"Bonjour\""
texte_avec_retour = "Ligne 1\nLigne 2"
texte_avec_tabulation = "Nom\tAge\tVille"

print(texte_avec_guillemets)  # Il a dit : "Bonjour"
print(texte_avec_retour)      # Ligne 1
                              # Ligne 2
print(texte_avec_tabulation)  # Nom	Age	Ville
```

## Méthodes essentielles des chaînes

### Transformation de casse

```python
texte = "Python Est Génial"

print(texte.upper())      # PYTHON EST GÉNIAL
print(texte.lower())      # python est génial
print(texte.capitalize()) # Python est génial
print(texte.title())      # Python Est Génial
print(texte.swapcase())   # pYTHON eST gÉNIAL

# Vérification de casse
print(texte.isupper())    # False
print(texte.islower())    # False
print(texte.istitle())    # True
```

### Nettoyage des chaînes

```python
texte_sale = "   Bonjour le monde   \n"

print(f"'{texte_sale}'")                    # '   Bonjour le monde   \n'
print(f"'{texte_sale.strip()}'")            # 'Bonjour le monde'
print(f"'{texte_sale.lstrip()}'")           # 'Bonjour le monde   \n'
print(f"'{texte_sale.rstrip()}'")           # '   Bonjour le monde'

# Enlever des caractères spécifiques
texte_ponctuation = "...Bonjour!!!"
print(texte_ponctuation.strip(".!"))        # Bonjour
```

### Recherche dans les chaînes

```python
phrase = "Python est un langage de programmation"

# Vérifier la présence
print("Python" in phrase)           # True
print("Java" in phrase)             # False

# Trouver la position
print(phrase.find("est"))            # 7
print(phrase.find("Java"))           # -1 (non trouvé)
print(phrase.index("est"))           # 7
# print(phrase.index("Java"))        # ValueError!

# Compter les occurrences
print(phrase.count("a"))             # 4
print(phrase.count("on"))            # 2

# Vérifications de début/fin
print(phrase.startswith("Python"))   # True
print(phrase.endswith("ation"))      # True
```

### Division et assemblage

```python
# Diviser une chaîne
phrase = "pomme,banane,orange,kiwi"
fruits = phrase.split(",")
print(fruits)  # ['pomme', 'banane', 'orange', 'kiwi']

# Diviser par lignes
texte_multilignes = "ligne1\nligne2\nligne3"
lignes = texte_multilignes.splitlines()
print(lignes)  # ['ligne1', 'ligne2', 'ligne3']

# Assembler des chaînes
separateur = " - "
resultat = separateur.join(fruits)
print(resultat)  # pomme - banane - orange - kiwi

# Assembler avec différents séparateurs
print(", ".join(fruits))    # pomme, banane, orange, kiwi
print(" et ".join(fruits))  # pomme et banane et orange et kiwi
```

### Remplacement

```python
texte = "J'aime les chats. Les chats sont mignons."

# Remplacement simple
nouveau_texte = texte.replace("chats", "chiens")
print(nouveau_texte)  # J'aime les chiens. Les chiens sont mignons.

# Remplacement limité
texte_limite = texte.replace("chats", "chiens", 1)
print(texte_limite)   # J'aime les chiens. Les chats sont mignons.

# Remplacement avec plusieurs espaces
texte_espaces = "mot1    mot2     mot3"
texte_propre = " ".join(texte_espaces.split())
print(texte_propre)   # mot1 mot2 mot3
```

### Vérifications de contenu

```python
# Vérifier le type de contenu
print("123".isdigit())         # True
print("abc".isalpha())         # True
print("abc123".isalnum())      # True
print("   ".isspace())         # True
print("Hello World".isascii()) # True

# Exemples pratiques
def valider_mot_de_passe(mot_de_passe):
    """Valide un mot de passe selon certains critères"""
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères"

    if not any(c.isupper() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins une majuscule"

    if not any(c.islower() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins une minuscule"

    if not any(c.isdigit() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins un chiffre"

    return True, "Mot de passe valide"

# Test
resultat, message = valider_mot_de_passe("MonMotDePasse123")
print(f"{resultat}: {message}")  # True: Mot de passe valide
```

## Formatage de chaînes

### Méthode format()

```python
nom = "Alice"
age = 25
ville = "Paris"

# Formatage avec des positions
message1 = "Je m'appelle {} et j'ai {} ans".format(nom, age)
print(message1)  # Je m'appelle Alice et j'ai 25 ans

# Formatage avec des index
message2 = "Je vis à {2}, je m'appelle {0} et j'ai {1} ans".format(nom, age, ville)
print(message2)  # Je vis à Paris, je m'appelle Alice et j'ai 25 ans

# Formatage avec des noms
message3 = "Je m'appelle {nom} et j'ai {age} ans".format(nom=nom, age=age)
print(message3)  # Je m'appelle Alice et j'ai 25 ans
```

### f-strings (recommandé depuis Python 3.6)

```python
nom = "Alice"
age = 25
note = 15.7

# Syntaxe simple
message = f"Je m'appelle {nom} et j'ai {age} ans"
print(message)  # Je m'appelle Alice et j'ai 25 ans

# Avec expressions
print(f"L'année prochaine, j'aurai {age + 1} ans")  # L'année prochaine, j'aurai 26 ans

# Formatage des nombres
prix = 19.99
print(f"Le prix est {prix:.2f}€")        # Le prix est 19.99€
print(f"La note est {note:.1f}/20")      # La note est 15.7/20

# Formatage avancé
nombre = 1234567
print(f"Nombre: {nombre:,}")             # Nombre: 1,234,567
print(f"Nombre: {nombre:_}")             # Nombre: 1_234_567

# Alignement
print(f"'{nom:>10}'")                    # '     Alice'
print(f"'{nom:<10}'")                    # 'Alice     '
print(f"'{nom:^10}'")                    # '  Alice   '
print(f"'{nom:*^10}'")                   # '**Alice***'
```

### Exemples pratiques de formatage

```python
# Tableau formaté
etudiants = [
    ("Alice", 15.5, 17.2, 16.8),
    ("Bob", 12.3, 14.1, 13.9),
    ("Charlie", 18.2, 16.5, 17.8)
]

print(f"{'Nom':<10} {'Math':<6} {'Phys':<6} {'Info':<6} {'Moy':<6}")
print("-" * 40)

for nom, math, phys, info in etudiants:
    moyenne = (math + phys + info) / 3
    print(f"{nom:<10} {math:<6.1f} {phys:<6.1f} {info:<6.1f} {moyenne:<6.1f}")
```

## Introduction aux expressions régulières

### Qu'est-ce qu'une expression régulière ?

Une expression régulière (regex) est un pattern qui permet de rechercher, extraire ou valider du texte selon des règles précises. C'est très utile pour :
- Valider des formats (email, téléphone, etc.)
- Extraire des informations spécifiques
- Nettoyer du texte
- Rechercher des motifs complexes

### Import du module re

```python
import re

# Exemple simple
texte = "Mon numéro est 06-12-34-56-78"
pattern = r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}"
resultat = re.search(pattern, texte)

if resultat:
    print(f"Numéro trouvé: {resultat.group()}")  # Numéro trouvé: 06-12-34-56-78
```

### Métacaractères de base

```python
import re

# . : n'importe quel caractère
print(re.findall(r"c.t", "chat, cot, cut, cart"))  # ['hat', 'cot', 'cut', 'art']

# * : zéro ou plusieurs occurrences
print(re.findall(r"go*gle", "ggle google gooogle"))  # ['ggle', 'google', 'gooogle']

# + : une ou plusieurs occurrences
print(re.findall(r"go+gle", "ggle google gooogle"))  # ['google', 'gooogle']

# ? : zéro ou une occurrence
print(re.findall(r"colou?r", "color colour"))  # ['color', 'colour']

# ^ : début de ligne
print(re.findall(r"^Python", "Python est génial\nJava aussi"))  # ['Python']

# $ : fin de ligne
print(re.findall(r"génial$", "Python est génial\nJava aussi"))  # ['génial']
```

### Classes de caractères

```python
import re

texte = "J'ai 25 ans et mon code postal est 75001"

# \d : chiffres (équivalent à [0-9])
print(re.findall(r"\d+", texte))  # ['25', '75001']

# \w : lettres, chiffres et underscore
print(re.findall(r"\w+", "hello_world 123"))  # ['hello_world', '123']

# \s : espaces, tabulations, retours à la ligne
print(re.findall(r"\S+", "mot1 mot2\tmot3"))  # ['mot1', 'mot2', 'mot3']

# Classes personnalisées
print(re.findall(r"[aeiou]", "bonjour"))  # ['o', 'o', 'u']
print(re.findall(r"[A-Z][a-z]+", "Alice Bob Charlie"))  # ['Alice', 'Bob', 'Charlie']
```

### Quantificateurs

```python
import re

# {n} : exactement n occurrences
print(re.findall(r"\d{4}", "L'année 2023 et le code 1234"))  # ['2023', '1234']

# {n,m} : entre n et m occurrences
print(re.findall(r"\d{2,4}", "12 123 1234 12345"))  # ['12', '123', '1234', '1234']

# {n,} : n occurrences ou plus
print(re.findall(r"\d{3,}", "12 123 1234 12345"))  # ['123', '1234', '12345']
```

## Fonctions principales du module re

### re.search() vs re.match() vs re.findall()

```python
import re

texte = "Mon email est alice@example.com et mon numéro est 06-12-34-56-78"

# search() : trouve la première occurrence
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_match = re.search(email_pattern, texte)
if email_match:
    print(f"Email trouvé: {email_match.group()}")  # Email trouvé: alice@example.com

# findall() : trouve toutes les occurrences
numeros = re.findall(r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", texte)
print(f"Numéros: {numeros}")  # Numéros: ['06-12-34-56-78']

# match() : vérifie si le début correspond
debut_match = re.match(r"Mon", texte)
if debut_match:
    print("Le texte commence par 'Mon'")  # Le texte commence par 'Mon'
```

### Groupes et capture

```python
import re

# Groupes avec parenthèses
texte = "Alice (25 ans) et Bob (30 ans)"
pattern = r"(\w+) \((\d+) ans\)"

matches = re.findall(pattern, texte)
print(matches)  # [('Alice', '25'), ('Bob', '30')]

# Accès aux groupes individuels
for match in re.finditer(pattern, texte):
    nom = match.group(1)
    age = match.group(2)
    print(f"Nom: {nom}, Âge: {age}")
```

### re.sub() : Remplacement avec regex

```python
import re

# Remplacement simple
texte = "Mon numéro est 06-12-34-56-78"
texte_anonyme = re.sub(r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", "XX-XX-XX-XX-XX", texte)
print(texte_anonyme)  # Mon numéro est XX-XX-XX-XX-XX

# Remplacement avec groupes
dates = "Aujourd'hui: 15/03/2023, Demain: 16/03/2023"
dates_us = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2/\1/\3", dates)
print(dates_us)  # Aujourd'hui: 03/15/2023, Demain: 03/16/2023

# Fonction de remplacement
def formater_numero(match):
    numero = match.group().replace("-", "")
    return f"+33{numero[1:]}"

texte_fr = "Appelez-moi au 06-12-34-56-78"
texte_international = re.sub(r"0\d-\d{2}-\d{2}-\d{2}-\d{2}", formater_numero, texte_fr)
print(texte_international)  # Appelez-moi au +33612345678
```

## Exemples pratiques

### Validation d'adresses email

```python
import re

def valider_email(email):
    """Valide une adresse email avec une regex simple"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Tests
emails_test = [
    "alice@example.com",      # Valide
    "bob.smith@test.fr",      # Valide
    "invalid.email",          # Invalide
    "@example.com",           # Invalide
    "test@",                  # Invalide
]

for email in emails_test:
    statut = "✓" if valider_email(email) else "✗"
    print(f"{statut} {email}")
```

### Extraction d'informations d'un texte

```python
import re

def extraire_infos_contact(texte):
    """Extrait emails, téléphones et URLs d'un texte"""

    # Patterns
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    tel_pattern = r"(?:0[1-9](?:[-.\s]?\d{2}){4})"
    url_pattern = r"https?://[^\s]+"

    # Extraction
    emails = re.findall(email_pattern, texte)
    telephones = re.findall(tel_pattern, texte)
    urls = re.findall(url_pattern, texte)

    return {
        "emails": emails,
        "telephones": telephones,
        "urls": urls
    }

# Test
texte_contact = """
Contactez-nous:
Email: support@entreprise.com ou info@entreprise.fr
Téléphone: 01-23-45-67-89 ou 06.12.34.56.78
Site web: https://www.entreprise.com
Documentation: https://docs.entreprise.com/guide
"""

infos = extraire_infos_contact(texte_contact)
print("Emails trouvés:", infos["emails"])
print("Téléphones trouvés:", infos["telephones"])
print("URLs trouvées:", infos["urls"])
```

### Nettoyage et formatage de texte

```python
import re

def nettoyer_texte(texte):
    """Nettoie un texte en supprimant les éléments indésirables"""

    # Supprimer les URLs
    texte = re.sub(r"https?://[^\s]+", "", texte)

    # Supprimer les mentions @utilisateur
    texte = re.sub(r"@\w+", "", texte)

    # Supprimer les hashtags
    texte = re.sub(r"#\w+", "", texte)

    # Supprimer les caractères répétés (plus de 2)
    texte = re.sub(r"(.)\1{2,}", r"\1\1", texte)

    # Normaliser les espaces
    texte = re.sub(r"\s+", " ", texte)

    # Nettoyer les débuts/fins
    texte = texte.strip()

    return texte

# Test
texte_sale = """
Salutttt tout le monde !!! 😊
Regardez ce lien: https://example.com/super-article
Merci @alice et @bob pour vos commentaires #python #coding
Trop cooooool ce tutoriel !!!
"""

texte_propre = nettoyer_texte(texte_sale)
print("Texte original:")
print(texte_sale)
print("\nTexte nettoyé:")
print(texte_propre)
```

### Analyseur de logs

```python
import re
from collections import defaultdict, Counter

def analyser_logs_apache(contenu_log):
    """Analyse un fichier de log Apache"""

    # Pattern pour une ligne de log Apache
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

    resultats = {
        "ips": Counter(),
        "codes_statut": Counter(),
        "methodes": Counter(),
        "pages": Counter(),
        "erreurs": []
    }

    for ligne in contenu_log.strip().split('\n'):
        match = re.match(pattern, ligne)
        if match:
            ip, timestamp, requete, code, taille = match.groups()

            # Analyser la requête
            requete_parts = requete.split()
            if len(requete_parts) >= 2:
                methode = requete_parts[0]
                page = requete_parts[1]

                # Compter les éléments
                resultats["ips"][ip] += 1
                resultats["codes_statut"][int(code)] += 1
                resultats["methodes"][methode] += 1
                resultats["pages"][page] += 1

                # Collecter les erreurs
                if int(code) >= 400:
                    resultats["erreurs"].append({
                        "ip": ip,
                        "code": code,
                        "page": page,
                        "timestamp": timestamp
                    })

    return resultats

# Exemple de logs
logs_exemple = """
192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:37] "POST /login HTTP/1.1" 200 1234
192.168.1.1 - - [10/Oct/2023:13:55:38] "GET /page404.html HTTP/1.1" 404 0
192.168.1.3 - - [10/Oct/2023:13:55:39] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:40] "GET /admin HTTP/1.1" 403 0
"""

resultats = analyser_logs_apache(logs_exemple)

print("IPs les plus actives:")
for ip, count in resultats["ips"].most_common(3):
    print(f"  {ip}: {count} requêtes")

print("\nCodes de statut:")
for code, count in sorted(resultats["codes_statut"].items()):
    print(f"  {code}: {count}")

print("\nErreurs détectées:")
for erreur in resultats["erreurs"]:
    print(f"  {erreur['ip']} - Code {erreur['code']} - {erreur['page']}")
```

## Exercices pratiques

### Exercice 1 : Validation de données

```python
import re

def valider_donnees_utilisateur(donnees):
    """Valide les données d'inscription d'un utilisateur"""

    erreurs = []

    # Validation du nom (lettres et espaces seulement)
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", donnees.get("nom", "")):
        erreurs.append("Le nom ne doit contenir que des lettres et des espaces")

    # Validation de l'email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, donnees.get("email", "")):
        erreurs.append("L'email n'est pas valide")

    # Validation du téléphone français
    tel_pattern = r"^0[1-9](?:[-.\s]?\d{2}){4}$"
    if not re.match(tel_pattern, donnees.get("telephone", "")):
        erreurs.append("Le numéro de téléphone n'est pas valide")

    # Validation du code postal français
    cp_pattern = r"^[0-9]{5}$"
    if not re.match(cp_pattern, donnees.get("code_postal", "")):
        erreurs.append("Le code postal doit contenir 5 chiffres")

    return len(erreurs) == 0, erreurs

# Tests
utilisateurs_test = [
    {
        "nom": "Jean Dupont",
        "email": "jean.dupont@example.com",
        "telephone": "01-23-45-67-89",
        "code_postal": "75001"
    },
    {
        "nom": "Alice123",  # Invalide
        "email": "alice@",  # Invalide
        "telephone": "123", # Invalide
        "code_postal": "ABC" # Invalide
    }
]

for i, user in enumerate(utilisateurs_test, 1):
    valide, erreurs = valider_donnees_utilisateur(user)
    print(f"Utilisateur {i}: {'✓ Valide' if valide else '✗ Invalide'}")
    if erreurs:
        for erreur in erreurs:
            print(f"  - {erreur}")
    print()
```

### Exercice 2 : Extracteur de prix

```python
import re

def extraire_prix(texte):
    """Extrait tous les prix d'un texte"""

    # Patterns pour différents formats de prix
    patterns = [
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*€",           # 123.45€, 1,234.56€
        r"€\s*(\d+(?:,\d{3})*(?:\.\d{2})?)",           # €123.45
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*euros?",      # 123.45 euros
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*EUR",         # 123.45 EUR
    ]

    prix_trouves = []

    for pattern in patterns:
        matches = re.finditer(pattern, texte, re.IGNORECASE)
        for match in matches:
            prix_str = match.group(1)
            # Convertir en float (enlever les virgules de milliers)
            prix_float = float(prix_str.replace(',', ''))
            prix_trouves.append({
                'prix': prix_float,
                'texte_original': match.group(0),
                'position': match.span()
            })

    return prix_trouves

# Test
texte_prix = """
Produits en promotion:
- Ordinateur portable: 899.99€
- Souris: €25.50
- Clavier: 75 euros
- Écran: 1,299.00 EUR
- Webcam: 45.99€
Total: environ 2,346.48 euros
"""

prix_extraits = extraire_prix(texte_prix)
print("Prix trouvés:")
for prix in prix_extraits:
    print(f"  {prix['prix']:.2f}€ ('{prix['texte_original']}')")

total = sum(p['prix'] for p in prix_extraits)
print(f"\nTotal des prix trouvés: {total:.2f}€")
```

### Exercice 3 : Formateur de texte

```python
import re

def formater_document(texte):
    """Formate un document selon des règles spécifiques"""

    # 1. Corriger les espaces autour de la ponctuation
    texte = re.sub(r'\s*([.!?])\s*', r'\1 ', texte)
    texte = re.sub(r'\s*([,;:])\s*', r'\1 ', texte)

    # 2. Corriger les guillemets
    texte = re.sub(r'"([^"]+)"', r'« \1 »', texte)

    # 3. Formater les nombres avec des séparateurs de milliers
    def formater_nombre(match):
        nombre = match.group()
        if len(nombre) > 3:
            # Ajouter des espaces tous les 3 chiffres
            return f"{int(nombre):,}".replace(',', ' ')
        return nombre

    texte = re.sub(r'\b\d{4,}\b', formater_nombre, texte)

    # 4. Mettre en forme les titres (ligne commençant par des mots en majuscules)
    def formater_titre(match):
        titre = match.group(1)
        return f"\n## {titre}\n"

    texte = re.sub(r'^([A-Z][A-Z\s]+)$', formater_titre, texte, flags=re.MULTILINE)

    # 5. Supprimer les espaces multiples
    texte = re.sub(r' +', ' ', texte)

    # 6. Nettoyer les débuts/fins de lignes
    texte = re.sub(r'^ +| +$', '', texte, flags=re.MULTILINE)

    return texte.strip()

# Test
document_brut = """
INTRODUCTION

Python est un langage de programmation créé en 1991.
Il compte aujourd'hui plus de 8000000 d'utilisateurs dans le monde.

"Python est génial" disent souvent les développeurs.
Les entreprises    utilisent Python pour    de nombreux projets.

CONCLUSION

Python    continuera   d'évoluer  .
"""

document_formate = formater_document(document_brut)
print("Document formaté:")
print(document_formate)
```

## Conseils et bonnes pratiques

### Pour les chaînes de caractères

1. **Utilisez les f-strings** pour le formatage (Python 3.6+)
2. **Préférez les méthodes intégrées** aux manipulations manuelles
3. **Attention à l'immutabilité** : les chaînes ne peuvent pas être modifiées en place
4. **Utilisez join()** pour concaténer plusieurs chaînes plutôt que l'opérateur +

```python
# ✅ Bon
mots = ["Python", "est", "génial"]
phrase = " ".join(mots)

# ❌ Moins efficace pour de nombreuses chaînes
phrase = ""
for mot in mots:
    phrase += mot + " "
```

### Pour les expressions régulières

1. **Compilez les regex réutilisées** avec `re.compile()`
2. **Utilisez des raw strings** (r"") pour éviter les problèmes d'échappement
3. **Commencez simple** puis complexifiez progressivement
4. **Testez vos regex** avec des outils en ligne comme regex101.com
5. **Commentez les regex complexes**

```python
# ✅ Bon : regex compilée et commentée
import re

# Pattern pour valider un numéro de téléphone français
# Format: 0X-XX-XX-XX-XX ou 0X.XX.XX.XX.XX ou 0XXXXXXXXX
TEL_PATTERN = re.compile(r"""
    ^                    # Début de ligne
    0                    # Commence par 0
    [1-9]                # Suivi d'un chiffre de 1 à 9
    (?:[-.\s]?\d{2}){4}  # Puis 4 groupes de 2 chiffres avec séparateurs optionnels
    $                    # Fin de ligne
""", re.VERBOSE)

def valider_telephone(numero):
    return TEL_PATTERN.match(numero) is not None
```

## Cas d'usage avancés

### Validation de mots de passe complexe

```python
import re

def valider_mot_de_passe_avance(mot_de_passe):
    """
    Valide un mot de passe selon des critères stricts:
    - Au moins 8 caractères
    - Au moins 1 majuscule, 1 minuscule, 1 chiffre, 1 caractère spécial
    - Pas plus de 2 caractères identiques consécutifs
    - Ne contient pas de mots courants
    """

    mots_interdits = ['password', 'motdepasse', '123456', 'azerty', 'qwerty']

    criteres = {
        'longueur': len(mot_de_passe) >= 8,
        'majuscule': bool(re.search(r'[A-Z]', mot_de_passe)),
        'minuscule': bool(re.search(r'[a-z]', mot_de_passe)),
        'chiffre': bool(re.search(r'\d', mot_de_passe)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', mot_de_passe)),
        'pas_repetition': not bool(re.search(r'(.)\1{2,}', mot_de_passe)),
        'pas_mot_courant': not any(mot in mot_de_passe.lower() for mot in mots_interdits)
    }

    score = sum(criteres.values())
    force = ['Très faible', 'Faible', 'Moyen', 'Fort', 'Très fort'][min(score-1, 4)] if score > 0 else 'Très faible'

    return {
        'valide': all(criteres.values()),
        'score': score,
        'force': force,
        'criteres': criteres
    }

# Test
mots_de_passe_test = [
    'motdepasse',
    'MotDePasse123',
    'M0tD3P@ss3!',
    'SuperMotDePasse2024!'
]

for mdp in mots_de_passe_test:
    resultat = valider_mot_de_passe_avance(mdp)
    print(f"Mot de passe: {mdp}")
    print(f"Valide: {resultat['valide']}, Force: {resultat['force']}")
    print(f"Score: {resultat['score']}/7")
    print()
```

### Extracteur de données structurées

```python
import re
from datetime import datetime

def extraire_donnees_facture(texte_facture):
    """Extrait les informations importantes d'une facture"""

    patterns = {
        'numero_facture': r'(?:Facture|Invoice)\s*#?\s*:?\s*([A-Z0-9-]+)',
        'date': r'(?:Date|Du)\s*:?\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})',
        'montant_total': r'(?:Total|TOTAL)\s*:?\s*(\d+(?:,\d{3})*(?:\.\d{2})?)\s*€?',
        'tva': r'(?:TVA|T\.V\.A\.)\s*(?:\(\d+%\))?\s*:?\s*(\d+(?:\.\d{2})?)\s*€?',
        'email': r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
        'telephone': r'(?:Tél|Tel|Téléphone)\s*:?\s*([+33|0]\d(?:[-.\s]?\d{2}){4})',
        'siret': r'(?:SIRET|Siret)\s*:?\s*(\d{14})'
    }

    donnees_extraites = {}

    for cle, pattern in patterns.items():
        match = re.search(pattern, texte_facture, re.IGNORECASE | re.MULTILINE)
        if match:
            valeur = match.group(1).strip()

            # Post-traitement selon le type
            if cle == 'date':
                try:
                    # Essayer de parser la date
                    for fmt in ['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y']:
                        try:
                            valeur = datetime.strptime(valeur, fmt).strftime('%Y-%m-%d')
                            break
                        except ValueError:
                            continue
                except:
                    pass

            elif cle in ['montant_total', 'tva']:
                # Nettoyer les montants
                valeur = float(valeur.replace(',', ''))

            donnees_extraites[cle] = valeur

    return donnees_extraites

# Test avec une facture exemple
facture_texte = """
FACTURE #2024-001

Date: 15/03/2024

Entreprise ABC
SIRET: 12345678901234
Email: contact@entreprise-abc.fr
Tél: 01-23-45-67-89

Prestations:
- Développement web: 1,500.00€
- Maintenance: 300.00€

Sous-total: 1,800.00€
TVA (20%): 360.00€
TOTAL: 2,160.00€
"""

donnees = extraire_donnees_facture(facture_texte)
print("Données extraites de la facture:")
for cle, valeur in donnees.items():
    print(f"  {cle}: {valeur}")
```

### Générateur de slug pour URLs

```python
import re
import unicodedata

def generer_slug(texte, max_longueur=50):
    """
    Génère un slug pour une URL à partir d'un texte
    Ex: "Mon Article Génial!" -> "mon-article-genial"
    """

    # Normaliser les caractères unicode (enlever les accents)
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(char for char in texte if unicodedata.category(char) != 'Mn')

    # Convertir en minuscules
    texte = texte.lower()

    # Remplacer les caractères non alphanumériques par des tirets
    texte = re.sub(r'[^a-z0-9]+', '-', texte)

    # Supprimer les tirets en début et fin
    texte = texte.strip('-')

    # Limiter la longueur
    if len(texte) > max_longueur:
        # Couper au dernier tiret avant la limite
        texte = texte[:max_longueur]
        dernier_tiret = texte.rfind('-')
        if dernier_tiret > max_longueur // 2:  # Si le tiret n'est pas trop loin
            texte = texte[:dernier_tiret]

    return texte

# Tests
titres_test = [
    "Mon Premier Article de Blog!",
    "Les Expressions Régulières en Python",
    "Comment créer une API REST avec Flask?",
    "Développement Web Moderne: Vue.js vs React",
    "À propos de l'Intelligence Artificielle (IA)",
    "Tutoriel Python 3.12 - Nouveautés & Améliorations"
]

print("Génération de slugs:")
for titre in titres_test:
    slug = generer_slug(titre)
    print(f"'{titre}' -> '{slug}'")
```

### Analyseur de sentiment simple

```python
import re
from collections import Counter

def analyser_sentiment(texte):
    """
    Analyse simple du sentiment d'un texte en français
    Retourne un score entre -1 (très négatif) et 1 (très positif)
    """

    # Dictionnaires de mots positifs et négatifs
    mots_positifs = {
        'excellent', 'génial', 'fantastique', 'parfait', 'super', 'top',
        'magnifique', 'merveilleux', 'extraordinaire', 'formidable',
        'incroyable', 'splendide', 'remarquable', 'exceptionnel',
        'love', 'adore', 'j\'aime', 'bravo', 'félicitations'
    }

    mots_negatifs = {
        'horrible', 'nul', 'terrible', 'affreux', 'catastrophique',
        'décevant', 'mauvais', 'pire', 'déteste', 'horreur',
        'problème', 'erreur', 'bug', 'cassé', 'inutile',
        'hate', 'déteste', 'n\'aime pas'
    }

    # Mots d'intensification
    intensificateurs = {
        'très', 'vraiment', 'extrêmement', 'particulièrement',
        'super', 'hyper', 'ultra', 'mega'
    }

    # Négations
    negations = {
        'ne', 'n\'', 'pas', 'point', 'jamais', 'rien',
        'personne', 'aucun', 'nulle', 'sans'
    }

    # Nettoyer et tokeniser le texte
    texte = texte.lower()
    mots = re.findall(r'\b[a-zA-ZàâäéèêëïîôöùûüÿçÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ\']+\b', texte)

    score_positif = 0
    score_negatif = 0

    for i, mot in enumerate(mots):
        multiplicateur = 1

        # Vérifier les intensificateurs précédents
        if i > 0 and mots[i-1] in intensificateurs:
            multiplicateur = 2

        # Vérifier les négations précédentes
        negation = False
        for j in range(max(0, i-3), i):
            if mots[j] in negations:
                negation = True
                break

        # Calculer le score
        if mot in mots_positifs:
            if negation:
                score_negatif += multiplicateur
            else:
                score_positif += multiplicateur
        elif mot in mots_negatifs:
            if negation:
                score_positif += multiplicateur
            else:
                score_negatif += multiplicateur

    # Calculer le score final
    total = score_positif + score_negatif
    if total == 0:
        return 0, "neutre"

    score = (score_positif - score_negatif) / total

    # Déterminer le sentiment
    if score > 0.5:
        sentiment = "très positif"
    elif score > 0.1:
        sentiment = "positif"
    elif score > -0.1:
        sentiment = "neutre"
    elif score > -0.5:
        sentiment = "négatif"
    else:
        sentiment = "très négatif"

    return score, sentiment

# Tests
commentaires_test = [
    "Ce produit est vraiment génial! Je le recommande vivement.",
    "Service client horrible, très décevant.",
    "Pas mal, sans plus. Ça peut aller.",
    "Extraordinaire! C'est exactement ce que je cherchais.",
    "Ne fonctionne pas du tout, très mauvaise qualité.",
    "J'adore cette application, elle est super pratique!"
]

print("Analyse de sentiment:")
for commentaire in commentaires_test:
    score, sentiment = analyser_sentiment(commentaire)
    print(f"Score: {score:.2f} | Sentiment: {sentiment}")
    print(f"Texte: '{commentaire}'")
    print("-" * 50)
```

## Performance et optimisation

### Compilation de regex

```python
import re
import time

def test_performance_regex():
    """Compare les performances avec et sans compilation"""

    texte = "test@example.com, alice@test.fr, bob@domain.org" * 1000
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Sans compilation
    start = time.time()
    for _ in range(100):
        re.findall(pattern, texte)
    temps_sans_compilation = time.time() - start

    # Avec compilation
    regex_compilee = re.compile(pattern)
    start = time.time()
    for _ in range(100):
        regex_compilee.findall(texte)
    temps_avec_compilation = time.time() - start

    print(f"Sans compilation: {temps_sans_compilation:.4f}s")
    print(f"Avec compilation: {temps_avec_compilation:.4f}s")
    print(f"Amélioration: {temps_sans_compilation/temps_avec_compilation:.1f}x")

# test_performance_regex()
```

### Optimisation des chaînes

```python
import time

def test_performance_join():
    """Compare différentes méthodes de concaténation"""

    mots = ["mot"] * 10000

    # Méthode 1: + (inefficace)
    start = time.time()
    resultat = ""
    for mot in mots:
        resultat += mot + " "
    temps_plus = time.time() - start

    # Méthode 2: join (efficace)
    start = time.time()
    resultat = " ".join(mots)
    temps_join = time.time() - start

    # Méthode 3: liste + join (très efficace)
    start = time.time()
    liste_temp = []
    for mot in mots:
        liste_temp.append(mot)
    resultat = " ".join(liste_temp)
    temps_liste_join = time.time() - start

    print(f"Concaténation avec +: {temps_plus:.4f}s")
    print(f"Méthode join(): {temps_join:.4f}s")
    print(f"Liste + join(): {temps_liste_join:.4f}s")

# test_performance_join()
```

## Résumé et points clés

### Manipulation de chaînes
- **Méthodes essentielles** : `strip()`, `split()`, `join()`, `replace()`, `find()`
- **Formatage moderne** : privilégier les f-strings `f"Hello {name}"`
- **Immutabilité** : les chaînes ne peuvent pas être modifiées en place
- **Performance** : utiliser `join()` pour concaténer plusieurs chaînes

### Expressions régulières
- **Modules** : `import re` pour toutes les fonctions regex
- **Fonctions principales** : `search()`, `findall()`, `sub()`, `match()`
- **Métacaractères** : `.`, `*`, `+`, `?`, `^`, `# 2.4 : Manipulation de chaînes de caractères et expressions régulières

## Introduction

Les chaînes de caractères (strings) sont l'un des types de données les plus utilisés en programmation. Python offre de nombreuses méthodes puissantes pour manipuler le texte, ainsi que les expressions régulières pour des traitements plus complexes.

Dans ce chapitre, nous verrons :
- Les méthodes essentielles pour manipuler les chaînes
- Le formatage de chaînes moderne
- Introduction aux expressions régulières
- Cas d'usage pratiques et exemples concrets

## Rappel : Bases des chaînes de caractères

### Création de chaînes

```python
# Différentes façons de créer des chaînes
nom = "Alice"
message = 'Bonjour le monde'
citation = """C'est une citation
sur plusieurs lignes"""
chemin = r"C:\Users\nom\Documents"  # Raw string (chaîne brute)

print(nom)      # Alice
print(message)  # Bonjour le monde
print(citation) # C'est une citation
                # sur plusieurs lignes
print(chemin)   # C:\Users\nom\Documents
```

### Caractères d'échappement

```python
# Caractères spéciaux
texte_avec_guillemets = "Il a dit : \"Bonjour\""
texte_avec_retour = "Ligne 1\nLigne 2"
texte_avec_tabulation = "Nom\tAge\tVille"

print(texte_avec_guillemets)  # Il a dit : "Bonjour"
print(texte_avec_retour)      # Ligne 1
                              # Ligne 2
print(texte_avec_tabulation)  # Nom	Age	Ville
```

## Méthodes essentielles des chaînes

### Transformation de casse

```python
texte = "Python Est Génial"

print(texte.upper())      # PYTHON EST GÉNIAL
print(texte.lower())      # python est génial
print(texte.capitalize()) # Python est génial
print(texte.title())      # Python Est Génial
print(texte.swapcase())   # pYTHON eST gÉNIAL

# Vérification de casse
print(texte.isupper())    # False
print(texte.islower())    # False
print(texte.istitle())    # True
```

### Nettoyage des chaînes

```python
texte_sale = "   Bonjour le monde   \n"

print(f"'{texte_sale}'")                    # '   Bonjour le monde   \n'
print(f"'{texte_sale.strip()}'")            # 'Bonjour le monde'
print(f"'{texte_sale.lstrip()}'")           # 'Bonjour le monde   \n'
print(f"'{texte_sale.rstrip()}'")           # '   Bonjour le monde'

# Enlever des caractères spécifiques
texte_ponctuation = "...Bonjour!!!"
print(texte_ponctuation.strip(".!"))        # Bonjour
```

### Recherche dans les chaînes

```python
phrase = "Python est un langage de programmation"

# Vérifier la présence
print("Python" in phrase)           # True
print("Java" in phrase)             # False

# Trouver la position
print(phrase.find("est"))            # 7
print(phrase.find("Java"))           # -1 (non trouvé)
print(phrase.index("est"))           # 7
# print(phrase.index("Java"))        # ValueError!

# Compter les occurrences
print(phrase.count("a"))             # 4
print(phrase.count("on"))            # 2

# Vérifications de début/fin
print(phrase.startswith("Python"))   # True
print(phrase.endswith("ation"))      # True
```

### Division et assemblage

```python
# Diviser une chaîne
phrase = "pomme,banane,orange,kiwi"
fruits = phrase.split(",")
print(fruits)  # ['pomme', 'banane', 'orange', 'kiwi']

# Diviser par lignes
texte_multilignes = "ligne1\nligne2\nligne3"
lignes = texte_multilignes.splitlines()
print(lignes)  # ['ligne1', 'ligne2', 'ligne3']

# Assembler des chaînes
separateur = " - "
resultat = separateur.join(fruits)
print(resultat)  # pomme - banane - orange - kiwi

# Assembler avec différents séparateurs
print(", ".join(fruits))    # pomme, banane, orange, kiwi
print(" et ".join(fruits))  # pomme et banane et orange et kiwi
```

### Remplacement

```python
texte = "J'aime les chats. Les chats sont mignons."

# Remplacement simple
nouveau_texte = texte.replace("chats", "chiens")
print(nouveau_texte)  # J'aime les chiens. Les chiens sont mignons.

# Remplacement limité
texte_limite = texte.replace("chats", "chiens", 1)
print(texte_limite)   # J'aime les chiens. Les chats sont mignons.

# Remplacement avec plusieurs espaces
texte_espaces = "mot1    mot2     mot3"
texte_propre = " ".join(texte_espaces.split())
print(texte_propre)   # mot1 mot2 mot3
```

### Vérifications de contenu

```python
# Vérifier le type de contenu
print("123".isdigit())         # True
print("abc".isalpha())         # True
print("abc123".isalnum())      # True
print("   ".isspace())         # True
print("Hello World".isascii()) # True

# Exemples pratiques
def valider_mot_de_passe(mot_de_passe):
    """Valide un mot de passe selon certains critères"""
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères"

    if not any(c.isupper() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins une majuscule"

    if not any(c.islower() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins une minuscule"

    if not any(c.isdigit() for c in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins un chiffre"

    return True, "Mot de passe valide"

# Test
resultat, message = valider_mot_de_passe("MonMotDePasse123")
print(f"{resultat}: {message}")  # True: Mot de passe valide
```

## Formatage de chaînes

### Méthode format()

```python
nom = "Alice"
age = 25
ville = "Paris"

# Formatage avec des positions
message1 = "Je m'appelle {} et j'ai {} ans".format(nom, age)
print(message1)  # Je m'appelle Alice et j'ai 25 ans

# Formatage avec des index
message2 = "Je vis à {2}, je m'appelle {0} et j'ai {1} ans".format(nom, age, ville)
print(message2)  # Je vis à Paris, je m'appelle Alice et j'ai 25 ans

# Formatage avec des noms
message3 = "Je m'appelle {nom} et j'ai {age} ans".format(nom=nom, age=age)
print(message3)  # Je m'appelle Alice et j'ai 25 ans
```

### f-strings (recommandé depuis Python 3.6)

```python
nom = "Alice"
age = 25
note = 15.7

# Syntaxe simple
message = f"Je m'appelle {nom} et j'ai {age} ans"
print(message)  # Je m'appelle Alice et j'ai 25 ans

# Avec expressions
print(f"L'année prochaine, j'aurai {age + 1} ans")  # L'année prochaine, j'aurai 26 ans

# Formatage des nombres
prix = 19.99
print(f"Le prix est {prix:.2f}€")        # Le prix est 19.99€
print(f"La note est {note:.1f}/20")      # La note est 15.7/20

# Formatage avancé
nombre = 1234567
print(f"Nombre: {nombre:,}")             # Nombre: 1,234,567
print(f"Nombre: {nombre:_}")             # Nombre: 1_234_567

# Alignement
print(f"'{nom:>10}'")                    # '     Alice'
print(f"'{nom:<10}'")                    # 'Alice     '
print(f"'{nom:^10}'")                    # '  Alice   '
print(f"'{nom:*^10}'")                   # '**Alice***'
```

### Exemples pratiques de formatage

```python
# Tableau formaté
etudiants = [
    ("Alice", 15.5, 17.2, 16.8),
    ("Bob", 12.3, 14.1, 13.9),
    ("Charlie", 18.2, 16.5, 17.8)
]

print(f"{'Nom':<10} {'Math':<6} {'Phys':<6} {'Info':<6} {'Moy':<6}")
print("-" * 40)

for nom, math, phys, info in etudiants:
    moyenne = (math + phys + info) / 3
    print(f"{nom:<10} {math:<6.1f} {phys:<6.1f} {info:<6.1f} {moyenne:<6.1f}")
```

## Introduction aux expressions régulières

### Qu'est-ce qu'une expression régulière ?

Une expression régulière (regex) est un pattern qui permet de rechercher, extraire ou valider du texte selon des règles précises. C'est très utile pour :
- Valider des formats (email, téléphone, etc.)
- Extraire des informations spécifiques
- Nettoyer du texte
- Rechercher des motifs complexes

### Import du module re

```python
import re

# Exemple simple
texte = "Mon numéro est 06-12-34-56-78"
pattern = r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}"
resultat = re.search(pattern, texte)

if resultat:
    print(f"Numéro trouvé: {resultat.group()}")  # Numéro trouvé: 06-12-34-56-78
```

### Métacaractères de base

```python
import re

# . : n'importe quel caractère
print(re.findall(r"c.t", "chat, cot, cut, cart"))  # ['hat', 'cot', 'cut', 'art']

# * : zéro ou plusieurs occurrences
print(re.findall(r"go*gle", "ggle google gooogle"))  # ['ggle', 'google', 'gooogle']

# + : une ou plusieurs occurrences
print(re.findall(r"go+gle", "ggle google gooogle"))  # ['google', 'gooogle']

# ? : zéro ou une occurrence
print(re.findall(r"colou?r", "color colour"))  # ['color', 'colour']

# ^ : début de ligne
print(re.findall(r"^Python", "Python est génial\nJava aussi"))  # ['Python']

# $ : fin de ligne
print(re.findall(r"génial$", "Python est génial\nJava aussi"))  # ['génial']
```

### Classes de caractères

```python
import re

texte = "J'ai 25 ans et mon code postal est 75001"

# \d : chiffres (équivalent à [0-9])
print(re.findall(r"\d+", texte))  # ['25', '75001']

# \w : lettres, chiffres et underscore
print(re.findall(r"\w+", "hello_world 123"))  # ['hello_world', '123']

# \s : espaces, tabulations, retours à la ligne
print(re.findall(r"\S+", "mot1 mot2\tmot3"))  # ['mot1', 'mot2', 'mot3']

# Classes personnalisées
print(re.findall(r"[aeiou]", "bonjour"))  # ['o', 'o', 'u']
print(re.findall(r"[A-Z][a-z]+", "Alice Bob Charlie"))  # ['Alice', 'Bob', 'Charlie']
```

### Quantificateurs

```python
import re

# {n} : exactement n occurrences
print(re.findall(r"\d{4}", "L'année 2023 et le code 1234"))  # ['2023', '1234']

# {n,m} : entre n et m occurrences
print(re.findall(r"\d{2,4}", "12 123 1234 12345"))  # ['12', '123', '1234', '1234']

# {n,} : n occurrences ou plus
print(re.findall(r"\d{3,}", "12 123 1234 12345"))  # ['123', '1234', '12345']
```

## Fonctions principales du module re

### re.search() vs re.match() vs re.findall()

```python
import re

texte = "Mon email est alice@example.com et mon numéro est 06-12-34-56-78"

# search() : trouve la première occurrence
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_match = re.search(email_pattern, texte)
if email_match:
    print(f"Email trouvé: {email_match.group()}")  # Email trouvé: alice@example.com

# findall() : trouve toutes les occurrences
numeros = re.findall(r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", texte)
print(f"Numéros: {numeros}")  # Numéros: ['06-12-34-56-78']

# match() : vérifie si le début correspond
debut_match = re.match(r"Mon", texte)
if debut_match:
    print("Le texte commence par 'Mon'")  # Le texte commence par 'Mon'
```

### Groupes et capture

```python
import re

# Groupes avec parenthèses
texte = "Alice (25 ans) et Bob (30 ans)"
pattern = r"(\w+) \((\d+) ans\)"

matches = re.findall(pattern, texte)
print(matches)  # [('Alice', '25'), ('Bob', '30')]

# Accès aux groupes individuels
for match in re.finditer(pattern, texte):
    nom = match.group(1)
    age = match.group(2)
    print(f"Nom: {nom}, Âge: {age}")
```

### re.sub() : Remplacement avec regex

```python
import re

# Remplacement simple
texte = "Mon numéro est 06-12-34-56-78"
texte_anonyme = re.sub(r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", "XX-XX-XX-XX-XX", texte)
print(texte_anonyme)  # Mon numéro est XX-XX-XX-XX-XX

# Remplacement avec groupes
dates = "Aujourd'hui: 15/03/2023, Demain: 16/03/2023"
dates_us = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2/\1/\3", dates)
print(dates_us)  # Aujourd'hui: 03/15/2023, Demain: 03/16/2023

# Fonction de remplacement
def formater_numero(match):
    numero = match.group().replace("-", "")
    return f"+33{numero[1:]}"

texte_fr = "Appelez-moi au 06-12-34-56-78"
texte_international = re.sub(r"0\d-\d{2}-\d{2}-\d{2}-\d{2}", formater_numero, texte_fr)
print(texte_international)  # Appelez-moi au +33612345678
```

## Exemples pratiques

### Validation d'adresses email

```python
import re

def valider_email(email):
    """Valide une adresse email avec une regex simple"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Tests
emails_test = [
    "alice@example.com",      # Valide
    "bob.smith@test.fr",      # Valide
    "invalid.email",          # Invalide
    "@example.com",           # Invalide
    "test@",                  # Invalide
]

for email in emails_test:
    statut = "✓" if valider_email(email) else "✗"
    print(f"{statut} {email}")
```

### Extraction d'informations d'un texte

```python
import re

def extraire_infos_contact(texte):
    """Extrait emails, téléphones et URLs d'un texte"""

    # Patterns
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    tel_pattern = r"(?:0[1-9](?:[-.\s]?\d{2}){4})"
    url_pattern = r"https?://[^\s]+"

    # Extraction
    emails = re.findall(email_pattern, texte)
    telephones = re.findall(tel_pattern, texte)
    urls = re.findall(url_pattern, texte)

    return {
        "emails": emails,
        "telephones": telephones,
        "urls": urls
    }

# Test
texte_contact = """
Contactez-nous:
Email: support@entreprise.com ou info@entreprise.fr
Téléphone: 01-23-45-67-89 ou 06.12.34.56.78
Site web: https://www.entreprise.com
Documentation: https://docs.entreprise.com/guide
"""

infos = extraire_infos_contact(texte_contact)
print("Emails trouvés:", infos["emails"])
print("Téléphones trouvés:", infos["telephones"])
print("URLs trouvées:", infos["urls"])
```

### Nettoyage et formatage de texte

```python
import re

def nettoyer_texte(texte):
    """Nettoie un texte en supprimant les éléments indésirables"""

    # Supprimer les URLs
    texte = re.sub(r"https?://[^\s]+", "", texte)

    # Supprimer les mentions @utilisateur
    texte = re.sub(r"@\w+", "", texte)

    # Supprimer les hashtags
    texte = re.sub(r"#\w+", "", texte)

    # Supprimer les caractères répétés (plus de 2)
    texte = re.sub(r"(.)\1{2,}", r"\1\1", texte)

    # Normaliser les espaces
    texte = re.sub(r"\s+", " ", texte)

    # Nettoyer les débuts/fins
    texte = texte.strip()

    return texte

# Test
texte_sale = """
Salutttt tout le monde !!! 😊
Regardez ce lien: https://example.com/super-article
Merci @alice et @bob pour vos commentaires #python #coding
Trop cooooool ce tutoriel !!!
"""

texte_propre = nettoyer_texte(texte_sale)
print("Texte original:")
print(texte_sale)
print("\nTexte nettoyé:")
print(texte_propre)
```

### Analyseur de logs

```python
import re
from collections import defaultdict, Counter

def analyser_logs_apache(contenu_log):
    """Analyse un fichier de log Apache"""

    # Pattern pour une ligne de log Apache
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

    resultats = {
        "ips": Counter(),
        "codes_statut": Counter(),
        "methodes": Counter(),
        "pages": Counter(),
        "erreurs": []
    }

    for ligne in contenu_log.strip().split('\n'):
        match = re.match(pattern, ligne)
        if match:
            ip, timestamp, requete, code, taille = match.groups()

            # Analyser la requête
            requete_parts = requete.split()
            if len(requete_parts) >= 2:
                methode = requete_parts[0]
                page = requete_parts[1]

                # Compter les éléments
                resultats["ips"][ip] += 1
                resultats["codes_statut"][int(code)] += 1
                resultats["methodes"][methode] += 1
                resultats["pages"][page] += 1

                # Collecter les erreurs
                if int(code) >= 400:
                    resultats["erreurs"].append({
                        "ip": ip,
                        "code": code,
                        "page": page,
                        "timestamp": timestamp
                    })

    return resultats

# Exemple de logs
logs_exemple = """
192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:37] "POST /login HTTP/1.1" 200 1234
192.168.1.1 - - [10/Oct/2023:13:55:38] "GET /page404.html HTTP/1.1" 404 0
192.168.1.3 - - [10/Oct/2023:13:55:39] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:40] "GET /admin HTTP/1.1" 403 0
"""

resultats = analyser_logs_apache(logs_exemple)

print("IPs les plus actives:")
for ip, count in resultats["ips"].most_common(3):
    print(f"  {ip}: {count} requêtes")

print("\nCodes de statut:")
for code, count in sorted(resultats["codes_statut"].items()):
    print(f"  {code}: {count}")

print("\nErreurs détectées:")
for erreur in resultats["erreurs"]:
    print(f"  {erreur['ip']} - Code {erreur['code']} - {erreur['page']}")
```

## Exercices pratiques

### Exercice 1 : Validation de données

```python
import re

def valider_donnees_utilisateur(donnees):
    """Valide les données d'inscription d'un utilisateur"""

    erreurs = []

    # Validation du nom (lettres et espaces seulement)
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", donnees.get("nom", "")):
        erreurs.append("Le nom ne doit contenir que des lettres et des espaces")

    # Validation de l'email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, donnees.get("email", "")):
        erreurs.append("L'email n'est pas valide")

    # Validation du téléphone français
    tel_pattern = r"^0[1-9](?:[-.\s]?\d{2}){4}$"
    if not re.match(tel_pattern, donnees.get("telephone", "")):
        erreurs.append("Le numéro de téléphone n'est pas valide")

    # Validation du code postal français
    cp_pattern = r"^[0-9]{5}$"
    if not re.match(cp_pattern, donnees.get("code_postal", "")):
        erreurs.append("Le code postal doit contenir 5 chiffres")

    return len(erreurs) == 0, erreurs

# Tests
utilisateurs_test = [
    {
        "nom": "Jean Dupont",
        "email": "jean.dupont@example.com",
        "telephone": "01-23-45-67-89",
        "code_postal": "75001"
    },
    {
        "nom": "Alice123",  # Invalide
        "email": "alice@",  # Invalide
        "telephone": "123", # Invalide
        "code_postal": "ABC" # Invalide
    }
]

for i, user in enumerate(utilisateurs_test, 1):
    valide, erreurs = valider_donnees_utilisateur(user)
    print(f"Utilisateur {i}: {'✓ Valide' if valide else '✗ Invalide'}")
    if erreurs:
        for erreur in erreurs:
            print(f"  - {erreur}")
    print()
```

### Exercice 2 : Extracteur de prix

```python
import re

def extraire_prix(texte):
    """Extrait tous les prix d'un texte"""

    # Patterns pour différents formats de prix
    patterns = [
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*€",           # 123.45€, 1,234.56€
        r"€\s*(\d+(?:,\d{3})*(?:\.\d{2})?)",           # €123.45
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*euros?",      # 123.45 euros
        r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*EUR",         # 123.45 EUR
    ]

    prix_trouves = []

    for pattern in patterns:
        matches = re.finditer(pattern, texte, re.IGNORECASE)
        for match in matches:
            prix_str = match.group(1)
            # Convertir en float (enlever les virgules de milliers)
            prix_float = float(prix_str.replace(',', ''))
            prix_trouves.append({
                'prix': prix_float,
                'texte_original': match.group(0),
                'position': match.span()
            })

    return prix_trouves

# Test
texte_prix = """
Produits en promotion:
- Ordinateur portable: 899.99€
- Souris: €25.50
- Clavier: 75 euros
- Écran: 1,299.00 EUR
- Webcam: 45.99€
Total: environ 2,346.48 euros
"""

prix_extraits = extraire_prix(texte_prix)
print("Prix trouvés:")
for prix in prix_extraits:
    print(f"  {prix['prix']:.2f}€ ('{prix['texte_original']}')")

total = sum(p['prix'] for p in prix_extraits)
print(f"\nTotal des prix trouvés: {total:.2f}€")
```

### Exercice 3 : Formateur de texte

```python
import re

def formater_document(texte):
    """Formate un document selon des règles spécifiques"""

    # 1. Corriger les espaces autour de la ponctuation
    texte = re.sub(r'\s*([.!?])\s*', r'\1 ', texte)
    texte = re.sub(r'\s*([,;:])\s*', r'\1 ', texte)

    # 2. Corriger les guillemets
    texte = re.sub(r'"([^"]+)"', r'« \1 »', texte)

    # 3. Formater les nombres avec des séparateurs de milliers
    def formater_nombre(match):
        nombre = match.group()
        if len(nombre) > 3:
            # Ajouter des espaces tous les 3 chiffres
            return f"{int(nombre):,}".replace(',', ' ')
        return nombre

    texte = re.sub(r'\b\d{4,}\b', formater_nombre, texte)

    # 4. Mettre en forme les titres (ligne commençant par des mots en majuscules)
    def formater_titre(match):
        titre = match.group(1)
        return f"\n## {titre}\n"

    texte = re.sub(r'^([A-Z][A-Z\s]+)$', formater_titre, texte, flags=re.MULTILINE)

    # 5. Supprimer les espaces multiples
    texte = re.sub(r' +', ' ', texte)

    # 6. Nettoyer les débuts/fins de lignes
    texte = re.sub(r'^ +| +$', '', texte, flags=re.MULTILINE)

    return texte.strip()

# Test
document_brut = """
INTRODUCTION

Python est un langage de programmation créé en 1991.
Il compte aujourd'hui plus de 8000000 d'utilisateurs dans le monde.

"Python est génial" disent souvent les développeurs.
Les entreprises    utilisent Python pour    de nombreux projets.

CONCLUSION

Python    continuera   d'évoluer  .
"""

document_formate = formater_document(document_brut)
print("Document formaté:")
print(document_formate)
```

## Conseils et bonnes pratiques

, `[]`, `{}`
- **Classes** : `\d` (chiffres), `\w` (mots), `\s` (espaces)
- **Groupes** : utiliser `()` pour capturer des parties
- **Compilation** : utiliser `re.compile()` pour les regex réutilisées

### Bonnes pratiques
1. **Simplicité** : commencer simple puis complexifier
2. **Lisibilité** : préférer plusieurs étapes simples à une regex complexe
3. **Tests** : toujours tester avec des données variées
4. **Performance** : compiler les regex fréquemment utilisées
5. **Documentation** : commenter les regex complexes

### Applications pratiques
- **Validation** : emails, téléphones, codes postaux
- **Extraction** : données structurées, prix, dates
- **Nettoyage** : formatage de texte, suppression d'éléments
- **Analyse** : logs, sentiment, fréquences

Les chaînes de caractères et les expressions régulières sont des outils fondamentaux pour tout développeur Python. Maîtriser ces concepts vous permettra de traiter efficacement tous types de données textuelles!

⏭️

