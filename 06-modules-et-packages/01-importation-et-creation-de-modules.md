🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.1 : Importation et création de modules

## Introduction

Dans cette section, nous allons apprendre à créer nos propres modules et à les utiliser dans nos programmes. Un module n'est rien d'autre qu'un fichier Python avec l'extension `.py` qui contient des définitions de fonctions, classes ou variables que nous pouvons réutiliser.

## Création d'un module simple

### Étape 1 : Créer votre premier module

Créons un module appelé `calculatrice.py` :

```python
# calculatrice.py

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustrait le second nombre du premier"""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres"""
    return a * b

def diviser(a, b):
    """Divise le premier nombre par le second"""
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro impossible"

# Variable globale du module
PI = 3.14159

# Code qui s'exécute lors de l'importation
print("Module calculatrice chargé avec succès!")
```

### Étape 2 : Utiliser votre module

Maintenant, créons un autre fichier `main.py` dans le même répertoire :

```python
# main.py

# Importation du module complet
import calculatrice

# Utilisation des fonctions du module
resultat1 = calculatrice.additionner(5, 3)
resultat2 = calculatrice.multiplier(4, 7)

print(f"5 + 3 = {resultat1}")
print(f"4 × 7 = {resultat2}")
print(f"Valeur de PI : {calculatrice.PI}")
```

## Les différentes façons d'importer

### 1. Importation complète

```python
import calculatrice

# Utilisation : nom_module.fonction()
resultat = calculatrice.additionner(10, 5)
```

**Avantages :**
- Évite les conflits de noms
- Clarté sur l'origine des fonctions

**Inconvénients :**
- Code plus verbeux

### 2. Importation avec alias

```python
import calculatrice as calc

# Utilisation : alias.fonction()
resultat = calc.additionner(10, 5)
```

**Utile quand :**
- Le nom du module est long
- On veut éviter les conflits avec des variables locales

### 3. Importation spécifique

```python
from calculatrice import additionner, soustraire

# Utilisation directe
resultat1 = additionner(10, 5)
resultat2 = soustraire(10, 5)
```

**Avantages :**
- Code plus concis
- Importation sélective

**Inconvénients :**
- Risque de conflits de noms

### 4. Importation avec alias spécifique

```python
from calculatrice import additionner as add, multiplier as mult

resultat1 = add(5, 3)
resultat2 = mult(4, 7)
```

### 5. Importation complète avec *

```python
from calculatrice import *

# Toutes les fonctions sont disponibles directement
resultat = additionner(5, 3)
```

**⚠️ Attention :** Cette méthode est généralement déconseillée car elle peut créer des conflits de noms et rendre le code moins lisible.

## Exemple pratique : Module utilitaires

Créons un module plus complexe `utilitaires.py` :

```python
# utilitaires.py

import math
import random

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def est_premier(nombre):
    """Vérifie si un nombre est premier"""
    if nombre < 2:
        return False
    for i in range(2, int(math.sqrt(nombre)) + 1):
        if nombre % i == 0:
            return False
    return True

def generer_nombre_aleatoire(min_val=1, max_val=100):
    """Génère un nombre aléatoire entre min_val et max_val"""
    return random.randint(min_val, max_val)

def formater_nom(prenom, nom):
    """Formate un nom complet"""
    return f"{prenom.capitalize()} {nom.upper()}"

class Compteur:
    """Classe simple pour compter"""
    def __init__(self, valeur_initiale=0):
        self.valeur = valeur_initiale

    def incrementer(self):
        self.valeur += 1
        return self.valeur

    def decrementer(self):
        self.valeur -= 1
        return self.valeur

    def reset(self):
        self.valeur = 0

# Variables du module
VERSION = "1.0.0"
AUTEUR = "Votre nom"

# Code d'initialisation
print(f"Module utilitaires v{VERSION} par {AUTEUR}")
```

### Utilisation du module utilitaires

```python
# test_utilitaires.py

from utilitaires import est_pair, est_premier, Compteur, generer_nombre_aleatoire

# Test des fonctions
print(f"12 est pair : {est_pair(12)}")
print(f"17 est premier : {est_premier(17)}")
print(f"Nombre aléatoire : {generer_nombre_aleatoire(1, 10)}")

# Test de la classe
compteur = Compteur(5)
print(f"Valeur initiale : {compteur.valeur}")
print(f"Après incrément : {compteur.incrementer()}")
print(f"Après décrément : {compteur.decrementer()}")
```

## Gestion des chemins et importations

### Structure de fichiers

```
mon_projet/
├── main.py
├── calculatrice.py
├── utilitaires.py
└── modules/
    ├── geometrie.py
    └── conversion.py
```

### Importation depuis un sous-dossier

```python
# geometrie.py dans le dossier modules/
def aire_rectangle(longueur, largeur):
    return longueur * largeur

def aire_cercle(rayon):
    import math
    return math.pi * rayon ** 2
```

```python
# main.py
import sys
sys.path.append('./modules')  # Ajouter le dossier au chemin Python

import geometrie

aire = geometrie.aire_rectangle(5, 3)
print(f"Aire du rectangle : {aire}")
```

## Bonnes pratiques

### 1. Nommage des modules

```python
# ✅ Bon
import utilitaires_texte
import calculatrice_scientifique

# ❌ Éviter
import UtilitairesTexte
import calculatrice-scientifique  # Les tirets ne sont pas autorisés
```

### 2. Documentation des modules

```python
# mon_module.py

"""
Module de calculs mathématiques avancés.

Ce module fournit des fonctions pour effectuer des calculs
mathématiques complexes, incluant la trigonométrie et les
fonctions exponentielles.

Auteur: Votre nom
Date: 2024
Version: 1.0
"""

def fonction_exemple():
    """
    Description de la fonction.

    Args:
        param1 (type): Description du paramètre

    Returns:
        type: Description du retour

    Raises:
        Exception: Description de l'exception
    """
    pass
```

### 3. Éviter l'exécution lors de l'importation

```python
# module_avec_tests.py

def ma_fonction():
    return "Hello World"

def tester_fonction():
    """Fonction de test"""
    resultat = ma_fonction()
    print(f"Test : {resultat}")

# Ce code ne s'exécute que si le fichier est lancé directement
if __name__ == "__main__":
    print("Test du module...")
    tester_fonction()
```

## Exercices pratiques

### Exercice 1 : Module de conversion

Créez un module `conversions.py` qui contient des fonctions pour :
- Convertir des degrés Celsius en Fahrenheit
- Convertir des kilomètres en miles
- Convertir des euros en dollars (avec un taux fixe)

```python
# Solution suggérée
def celsius_vers_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometres_vers_miles(km):
    return km * 0.621371

def euros_vers_dollars(euros, taux=1.1):
    return euros * taux
```

### Exercice 2 : Module de validation

Créez un module `validation.py` avec des fonctions pour valider :
- Une adresse email
- Un numéro de téléphone français
- Un code postal français

```python
# Solution : validation.py
import re

def valider_email(email):
    """
    Valide une adresse email.

    Args:
        email (str): L'adresse email à valider

    Returns:
        bool: True si l'email est valide, False sinon
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

## Résumé

Dans cette section, nous avons appris :

- **Créer des modules** en écrivant du code Python dans des fichiers `.py`
- **Importer des modules** avec différentes syntaxes (`import`, `from...import`, etc.)
- **Organiser le code** en modules réutilisables
- **Documenter les modules** avec des docstrings
- **Appliquer les bonnes pratiques** de nommage et structure

Les modules sont un outil puissant pour organiser et réutiliser votre code. Dans la prochaine section, nous verrons comment organiser plusieurs modules en packages pour des projets plus complexes.

## Points clés à retenir

1. **Un module = un fichier Python** avec l'extension `.py`
2. **Plusieurs façons d'importer** selon vos besoins
3. **Utilisez des noms descriptifs** pour vos modules
4. **Documentez votre code** avec des docstrings
5. **Évitez l'exécution non désirée** avec `if __name__ == "__main__"`
    return re.match(pattern, email) is not None

def valider_telephone_francais(telephone):
    """
    Valide un numéro de téléphone français.

    Args:
        telephone (str): Le numéro à valider

    Returns:
        bool: True si le numéro est valide, False sinon
    """
    # Supprime les espaces et tirets
    telephone_clean = telephone.replace(' ', '').replace('-', '').replace('.', '')

    # Vérifie le format français (10 chiffres commençant par 0)
    pattern = r'^0[1-9][0-9]{8}

## Résumé

Dans cette section, nous avons appris :

- **Créer des modules** en écrivant du code Python dans des fichiers `.py`
- **Importer des modules** avec différentes syntaxes (`import`, `from...import`, etc.)
- **Organiser le code** en modules réutilisables
- **Documenter les modules** avec des docstrings
- **Appliquer les bonnes pratiques** de nommage et structure

Les modules sont un outil puissant pour organiser et réutiliser votre code. Dans la prochaine section, nous verrons comment organiser plusieurs modules en packages pour des projets plus complexes.

## Points clés à retenir

1. **Un module = un fichier Python** avec l'extension `.py`
2. **Plusieurs façons d'importer** selon vos besoins
3. **Utilisez des noms descriptifs** pour vos modules
4. **Documentez votre code** avec des docstrings
5. **Évitez l'exécution non désirée** avec `if __name__ == "__main__"`
    return re.match(pattern, telephone_clean) is not None

def valider_code_postal_francais(code_postal):
    """
    Valide un code postal français.

    Args:
        code_postal (str): Le code postal à valider

    Returns:
        bool: True si le code postal est valide, False sinon
    """
    # Code postal français : 5 chiffres
    pattern = r'^[0-9]{5}

## Résumé

Dans cette section, nous avons appris :

- **Créer des modules** en écrivant du code Python dans des fichiers `.py`
- **Importer des modules** avec différentes syntaxes (`import`, `from...import`, etc.)
- **Organiser le code** en modules réutilisables
- **Documenter les modules** avec des docstrings
- **Appliquer les bonnes pratiques** de nommage et structure

Les modules sont un outil puissant pour organiser et réutiliser votre code. Dans la prochaine section, nous verrons comment organiser plusieurs modules en packages pour des projets plus complexes.

## Points clés à retenir

1. **Un module = un fichier Python** avec l'extension `.py`
2. **Plusieurs façons d'importer** selon vos besoins
3. **Utilisez des noms descriptifs** pour vos modules
4. **Documentez votre code** avec des docstrings
5. **Évitez l'exécution non désirée** avec `if __name__ == "__main__"`
    return re.match(pattern, code_postal) is not None

def formater_telephone(telephone):
    """
    Formate un numéro de téléphone français.

    Args:
        telephone (str): Le numéro à formater

    Returns:
        str: Le numéro formaté ou None si invalide
    """
    if valider_telephone_francais(telephone):
        clean = telephone.replace(' ', '').replace('-', '').replace('.', '')
        return f"{clean[:2]} {clean[2:4]} {clean[4:6]} {clean[6:8]} {clean[8:]}"
    return None

# Test du module
if __name__ == "__main__":
    # Tests des fonctions
    print("=== Tests de validation ===")

    # Test email
    emails_test = [
        "test@example.com",
        "user.name@domain.fr",
        "invalid-email",
        "test@",
        "@domain.com"
    ]

    print("Tests d'emails :")
    for email in emails_test:
        resultat = valider_email(email)
        print(f"  {email} : {'✓' if resultat else '✗'}")

    # Test téléphone
    telephones_test = [
        "01 23 45 67 89",
        "0123456789",
        "01.23.45.67.89",
        "01-23-45-67-89",
        "123456789",
        "11 23 45 67 89"
    ]

    print("\nTests de téléphones :")
    for tel in telephones_test:
        resultat = valider_telephone_francais(tel)
        formate = formater_telephone(tel)
        print(f"  {tel} : {'✓' if resultat else '✗'} {f'→ {formate}' if formate else ''}")

    # Test codes postaux
    codes_postaux_test = [
        "75001",
        "13000",
        "1234",
        "123456",
        "ABCDE"
    ]

    print("\nTests de codes postaux :")
    for code in codes_postaux_test:
        resultat = valider_code_postal_francais(code)
        print(f"  {code} : {'✓' if resultat else '✗'}")
```

### Exercice 3 : Utilisation complète

Créez un programme principal qui utilise tous vos modules créés pour :
1. Demander des informations à l'utilisateur
2. Valider ces informations
3. Effectuer des conversions
4. Afficher les résultats

```python
# Solution : programme_principal.py

from conversions import celsius_vers_fahrenheit, kilometres_vers_miles, euros_vers_dollars
from validation import valider_email, valider_telephone_francais, valider_code_postal_francais, formater_telephone
from utilitaires import est_pair, est_premier, generer_nombre_aleatoire, formater_nom

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("           PROGRAMME MULTI-MODULES")
    print("="*50)
    print("1. Conversions d'unités")
    print("2. Validation de données")
    print("3. Utilitaires numériques")
    print("4. Formatage de nom")
    print("5. Quitter")
    print("="*50)

def menu_conversions():
    """Gère le menu des conversions"""
    print("\n--- CONVERSIONS ---")
    print("1. Celsius → Fahrenheit")
    print("2. Kilomètres → Miles")
    print("3. Euros → Dollars")

    choix = input("Votre choix (1-3) : ")

    if choix == "1":
        try:
            celsius = float(input("Température en Celsius : "))
            fahrenheit = celsius_vers_fahrenheit(celsius)
            print(f"Résultat : {celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide")

    elif choix == "2":
        try:
            km = float(input("Distance en kilomètres : "))
            miles = kilometres_vers_miles(km)
            print(f"Résultat : {km} km = {miles:.2f} miles")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide")

    elif choix == "3":
        try:
            euros = float(input("Montant en euros : "))
            taux = input("Taux de change (appuyez sur Entrée pour 1.1) : ")
            taux = float(taux) if taux else 1.1
            dollars = euros_vers_dollars(euros, taux)
            print(f"Résultat : {euros}€ = {dollars:.2f}$ (taux: {taux})")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides")

    else:
        print("Choix invalide")

def menu_validation():
    """Gère le menu de validation"""
    print("\n--- VALIDATION ---")
    print("1. Valider un email")
    print("2. Valider un téléphone français")
    print("3. Valider un code postal français")

    choix = input("Votre choix (1-3) : ")

    if choix == "1":
        email = input("Adresse email : ")
        if valider_email(email):
            print("✓ Email valide")
        else:
            print("✗ Email invalide")

    elif choix == "2":
        telephone = input("Numéro de téléphone : ")
        if valider_telephone_francais(telephone):
            formate = formater_telephone(telephone)
            print(f"✓ Téléphone valide : {formate}")
        else:
            print("✗ Téléphone invalide")

    elif choix == "3":
        code_postal = input("Code postal : ")
        if valider_code_postal_francais(code_postal):
            print("✓ Code postal valide")
        else:
            print("✗ Code postal invalide")

    else:
        print("Choix invalide")

def menu_utilitaires():
    """Gère le menu des utilitaires"""
    print("\n--- UTILITAIRES NUMÉRIQUES ---")
    print("1. Vérifier si un nombre est pair")
    print("2. Vérifier si un nombre est premier")
    print("3. Générer un nombre aléatoire")

    choix = input("Votre choix (1-3) : ")

    if choix == "1":
        try:
            nombre = int(input("Nombre à vérifier : "))
            if est_pair(nombre):
                print(f"✓ {nombre} est pair")
            else:
                print(f"✗ {nombre} est impair")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier")

    elif choix == "2":
        try:
            nombre = int(input("Nombre à vérifier : "))
            if est_premier(nombre):
                print(f"✓ {nombre} est premier")
            else:
                print(f"✗ {nombre} n'est pas premier")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier")

    elif choix == "3":
        try:
            min_val = int(input("Valeur minimale (défaut: 1) : ") or "1")
            max_val = int(input("Valeur maximale (défaut: 100) : ") or "100")
            nombre = generer_nombre_aleatoire(min_val, max_val)
            print(f"Nombre aléatoire généré : {nombre}")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres entiers")

    else:
        print("Choix invalide")

def menu_formatage():
    """Gère le formatage de nom"""
    print("\n--- FORMATAGE DE NOM ---")
    prenom = input("Prénom : ")
    nom = input("Nom : ")

    if prenom and nom:
        nom_formate = formater_nom(prenom, nom)
        print(f"Nom formaté : {nom_formate}")
    else:
        print("Veuillez entrer un prénom et un nom")

def main():
    """Fonction principale"""
    print("Bienvenue dans le programme multi-modules !")
    print("Ce programme utilise plusieurs modules personnalisés.")

    while True:
        afficher_menu()
        choix = input("Votre choix (1-5) : ")

        if choix == "1":
            menu_conversions()
        elif choix == "2":
            menu_validation()
        elif choix == "3":
            menu_utilitaires()
        elif choix == "4":
            menu_formatage()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer")

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
```

### Exercice 4 : Module de gestion de fichiers (Bonus)

Créez un module `fichiers.py` pour gérer les opérations sur les fichiers :

```python
# Solution : fichiers.py
import os
import json
from datetime import datetime

def lire_fichier_texte(nom_fichier):
    """
    Lit un fichier texte et retourne son contenu.

    Args:
        nom_fichier (str): Le nom du fichier à lire

    Returns:
        str: Le contenu du fichier ou None si erreur
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            return fichier.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")
        return None

def ecrire_fichier_texte(nom_fichier, contenu):
    """
    Écrit du contenu dans un fichier texte.

    Args:
        nom_fichier (str): Le nom du fichier
        contenu (str): Le contenu à écrire

    Returns:
        bool: True si succès, False sinon
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            fichier.write(contenu)
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture : {e}")
        return False

def sauvegarder_donnees_json(nom_fichier, donnees):
    """
    Sauvegarde des données au format JSON.

    Args:
        nom_fichier (str): Le nom du fichier JSON
        donnees (dict): Les données à sauvegarder

    Returns:
        bool: True si succès, False sinon
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde JSON : {e}")
        return False

def charger_donnees_json(nom_fichier):
    """
    Charge des données depuis un fichier JSON.

    Args:
        nom_fichier (str): Le nom du fichier JSON

    Returns:
        dict: Les données chargées ou None si erreur
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas")
        return None
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'est pas un JSON valide")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement JSON : {e}")
        return None

def lister_fichiers(repertoire="."):
    """
    Liste les fichiers d'un répertoire.

    Args:
        repertoire (str): Le répertoire à lister

    Returns:
        list: Liste des fichiers
    """
    try:
        fichiers = []
        for element in os.listdir(repertoire):
            chemin_complet = os.path.join(repertoire, element)
            if os.path.isfile(chemin_complet):
                fichiers.append(element)
        return fichiers
    except Exception as e:
        print(f"Erreur lors du listage : {e}")
        return []

def obtenir_info_fichier(nom_fichier):
    """
    Obtient les informations d'un fichier.

    Args:
        nom_fichier (str): Le nom du fichier

    Returns:
        dict: Informations du fichier ou None si erreur
    """
    try:
        stats = os.stat(nom_fichier)
        return {
            'nom': nom_fichier,
            'taille': stats.st_size,
            'date_creation': datetime.fromtimestamp(stats.st_ctime),
            'date_modification': datetime.fromtimestamp(stats.st_mtime),
            'est_fichier': os.path.isfile(nom_fichier),
            'est_repertoire': os.path.isdir(nom_fichier)
        }
    except Exception as e:
        print(f"Erreur lors de l'obtention des infos : {e}")
        return None

# Test du module
if __name__ == "__main__":
    # Test des fonctions
    print("Test du module fichiers...")

    # Test écriture/lecture
    test_contenu = "Ceci est un test\nLigne 2\nLigne 3"
    if ecrire_fichier_texte("test.txt", test_contenu):
        print("✓ Écriture réussie")
        contenu_lu = lire_fichier_texte("test.txt")
        if contenu_lu:
            print("✓ Lecture réussie")

    # Test JSON
    donnees_test = {
        "nom": "Test",
        "age": 25,
        "ville": "Paris",
        "hobbies": ["lecture", "sport", "musique"]
    }

    if sauvegarder_donnees_json("test.json", donnees_test):
        print("✓ Sauvegarde JSON réussie")
        donnees_chargees = charger_donnees_json("test.json")
        if donnees_chargees:
            print("✓ Chargement JSON réussi")

    # Test listage
    fichiers = lister_fichiers()
    print(f"Fichiers trouvés : {len(fichiers)}")

    # Test info fichier
    info = obtenir_info_fichier("test.txt")
    if info:
        print(f"Infos fichier : {info['nom']}, {info['taille']} octets")
```

## Résumé

Dans cette section, nous avons appris :

- **Créer des modules** en écrivant du code Python dans des fichiers `.py`
- **Importer des modules** avec différentes syntaxes (`import`, `from...import`, etc.)
- **Organiser le code** en modules réutilisables
- **Documenter les modules** avec des docstrings
- **Appliquer les bonnes pratiques** de nommage et structure

Les modules sont un outil puissant pour organiser et réutiliser votre code. Dans la prochaine section, nous verrons comment organiser plusieurs modules en packages pour des projets plus complexes.

## Points clés à retenir

1. **Un module = un fichier Python** avec l'extension `.py`
2. **Plusieurs façons d'importer** selon vos besoins
3. **Utilisez des noms descriptifs** pour vos modules
4. **Documentez votre code** avec des docstrings
5. **Évitez l'exécution non désirée** avec `if __name__ == "__main__"`

⏭️
