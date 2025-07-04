🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.1 : Lecture/écriture de fichiers texte et binaires

## Introduction

La manipulation de fichiers est l'une des opérations les plus courantes en programmation. Que ce soit pour lire un fichier de configuration, sauvegarder des données ou traiter des logs, Python offre des outils simples et puissants pour travailler avec les fichiers.

## Comprendre les types de fichiers

### Fichiers texte
Les fichiers texte contiennent des caractères lisibles par l'homme. Exemples :
- `.txt` : fichiers texte simple
- `.py` : code Python
- `.html` : pages web
- `.json` : données JSON
- `.csv` : données tabulaires

### Fichiers binaires
Les fichiers binaires contiennent des données sous forme de bytes. Exemples :
- `.jpg`, `.png` : images
- `.pdf` : documents PDF
- `.exe` : programmes exécutables
- `.zip` : archives compressées

## Ouverture et fermeture de fichiers

### La fonction `open()`

La fonction `open()` est la porte d'entrée pour travailler avec les fichiers :

```python
# Syntaxe de base
fichier = open('nom_du_fichier.txt', 'mode')
# ... opérations sur le fichier
fichier.close()  # Important : fermer le fichier !
```

### Les modes d'ouverture

| Mode | Description | Fichier existe | Fichier n'existe pas |
|------|-------------|----------------|----------------------|
| `'r'` | Lecture seule | ✅ Ouvre | ❌ Erreur |
| `'w'` | Écriture (efface le contenu) | ✅ Efface tout | ✅ Crée |
| `'a'` | Ajout à la fin | ✅ Ajoute à la fin | ✅ Crée |
| `'x'` | Création exclusive | ❌ Erreur | ✅ Crée |
| `'r+'` | Lecture et écriture | ✅ Ouvre | ❌ Erreur |

### Modes binaires
Ajoutez `'b'` pour les fichiers binaires :
- `'rb'` : lecture binaire
- `'wb'` : écriture binaire
- `'ab'` : ajout binaire

## Le gestionnaire de contexte `with`

### Pourquoi utiliser `with` ?

```python
# ❌ Mauvaise pratique
fichier = open('document.txt', 'r')
contenu = fichier.read()
fichier.close()  # Oubli fréquent !

# ✅ Bonne pratique
with open('document.txt', 'r') as fichier:
    contenu = fichier.read()
# Le fichier est automatiquement fermé
```

### Avantages de `with`
- **Fermeture automatique** du fichier
- **Gestion des erreurs** : le fichier est fermé même en cas d'exception
- **Code plus propre** et plus lisible

## Lecture de fichiers texte

### Lecture complète avec `read()`

```python
# Lire tout le contenu d'un coup
with open('mon_fichier.txt', 'r') as f:
    contenu = f.read()
    print(contenu)
```

**Exemple concret :**
```python
# Création d'un fichier d'exemple
with open('salutation.txt', 'w') as f:
    f.write("Bonjour le monde !\nComment allez-vous ?")

# Lecture du fichier
with open('salutation.txt', 'r') as f:
    texte = f.read()
    print(texte)
```

### Lecture ligne par ligne avec `readline()`

```python
with open('mon_fichier.txt', 'r') as f:
    ligne1 = f.readline()  # Première ligne
    ligne2 = f.readline()  # Deuxième ligne
    print(f"Ligne 1: {ligne1}")
    print(f"Ligne 2: {ligne2}")
```

### Lecture de toutes les lignes avec `readlines()`

```python
with open('mon_fichier.txt', 'r') as f:
    lignes = f.readlines()  # Liste de toutes les lignes
    for i, ligne in enumerate(lignes, 1):
        print(f"Ligne {i}: {ligne.strip()}")
```

### Itération directe sur le fichier (recommandé)

```python
# Méthode la plus élégante et efficace
with open('mon_fichier.txt', 'r') as f:
    for numero, ligne in enumerate(f, 1):
        print(f"Ligne {numero}: {ligne.strip()}")
```

## Écriture de fichiers texte

### Écriture avec `write()`

```python
# Écriture simple
with open('nouveau_fichier.txt', 'w') as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
```

### Écriture multiple avec `writelines()`

```python
lignes = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"]
with open('multiple_lignes.txt', 'w') as f:
    f.writelines(lignes)
```

### Ajout à un fichier existant

```python
# Mode 'a' pour append (ajouter)
with open('journal.txt', 'a') as f:
    f.write("Nouvelle entrée de journal\n")
```

## Gestion de l'encodage

### Qu'est-ce que l'encodage ?

L'encodage détermine comment les caractères sont convertis en bytes. UTF-8 est le standard moderne.

```python
# Spécifier l'encodage (recommandé)
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

# Écriture avec encodage
with open('fichier.txt', 'w', encoding='utf-8') as f:
    f.write("Texte avec des accents : café, naïf, œuvre")
```

### Problèmes courants d'encodage

```python
# Gestion des erreurs d'encodage
try:
    with open('fichier_suspect.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
except UnicodeDecodeError:
    print("Erreur d'encodage, essayons avec latin-1")
    with open('fichier_suspect.txt', 'r', encoding='latin-1') as f:
        contenu = f.read()
```

## Fichiers binaires

### Lecture de fichiers binaires

```python
# Lecture d'une image
with open('image.jpg', 'rb') as f:
    donnees_binaires = f.read()
    print(f"Taille du fichier: {len(donnees_binaires)} bytes")
```

### Écriture de fichiers binaires

```python
# Copie d'un fichier binaire
with open('image_originale.jpg', 'rb') as source:
    with open('image_copie.jpg', 'wb') as destination:
        destination.write(source.read())
```

### Lecture par chunks (gros fichiers)

```python
def copier_gros_fichier(source, destination):
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dst:
            while True:
                chunk = src.read(8192)  # Lit 8KB à la fois
                if not chunk:
                    break
                dst.write(chunk)

# Utilisation
copier_gros_fichier('video.mp4', 'video_copie.mp4')
```

## Gestion des erreurs

### Erreurs courantes

```python
import os

def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{nom_fichier}' n'existe pas")
        return None
    except PermissionError:
        print(f"Erreur: Permissions insuffisantes pour '{nom_fichier}'")
        return None
    except UnicodeDecodeError:
        print(f"Erreur: Problème d'encodage avec '{nom_fichier}'")
        return None
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return None
```

### Vérification de l'existence d'un fichier

```python
import os

# Vérifier si un fichier existe
if os.path.exists('mon_fichier.txt'):
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")

# Vérifier si c'est un fichier ou un dossier
if os.path.isfile('mon_fichier.txt'):
    print("C'est un fichier")
elif os.path.isdir('mon_dossier'):
    print("C'est un dossier")
```

## Exemples pratiques

### Exemple 1 : Compteur de mots

```python
def compter_mots(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
            mots = contenu.split()
            return len(mots)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas")
        return 0

# Utilisation
nb_mots = compter_mots('article.txt')
print(f"Nombre de mots: {nb_mots}")
```

### Exemple 2 : Lecteur de logs

```python
def analyser_logs(fichier_log):
    erreurs = []
    warnings = []

    try:
        with open(fichier_log, 'r', encoding='utf-8') as f:
            for numero, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if 'ERROR' in ligne:
                    erreurs.append(f"Ligne {numero}: {ligne}")
                elif 'WARNING' in ligne:
                    warnings.append(f"Ligne {numero}: {ligne}")
    except FileNotFoundError:
        print(f"Fichier de log '{fichier_log}' introuvable")
        return [], []

    return erreurs, warnings

# Utilisation
erreurs, warnings = analyser_logs('application.log')
print(f"Erreurs trouvées: {len(erreurs)}")
print(f"Warnings trouvés: {len(warnings)}")
```

### Exemple 3 : Sauvegarde de configuration

```python
def sauvegarder_config(config_dict, nom_fichier):
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            for cle, valeur in config_dict.items():
                f.write(f"{cle}={valeur}\n")
        print(f"Configuration sauvegardée dans {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde: {e}")

def charger_config(nom_fichier):
    config = {}
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if '=' in ligne:
                    cle, valeur = ligne.split('=', 1)
                    config[cle] = valeur
    except FileNotFoundError:
        print(f"Fichier de configuration '{nom_fichier}' introuvable")

    return config

# Utilisation
config = {
    'nom_utilisateur': 'alice',
    'theme': 'sombre',
    'langue': 'fr'
}

sauvegarder_config(config, 'config.txt')
config_chargee = charger_config('config.txt')
print(config_chargee)
```

## Exercices pratiques

### Exercice 1 : Créateur de fichier
Créez un programme qui demande à l'utilisateur d'entrer du texte et le sauvegarde dans un fichier.

```python
def creer_fichier():
    nom_fichier = input("Nom du fichier à créer: ")
    print("Entrez votre texte (tapez 'FIN' pour terminer):")

    lignes = []
    while True:
        ligne = input()
        if ligne == 'FIN':
            break
        lignes.append(ligne + '\n')

    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.writelines(lignes)

    print(f"Fichier '{nom_fichier}' créé avec succès!")

# Testez votre fonction
creer_fichier()
```

### Exercice 2 : Statistiques de fichier
Créez une fonction qui analyse un fichier texte et retourne :
- Nombre de lignes
- Nombre de mots
- Nombre de caractères
- Ligne la plus longue

```python
def analyser_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        nb_lignes = len(lignes)
        nb_mots = sum(len(ligne.split()) for ligne in lignes)
        nb_caracteres = sum(len(ligne) for ligne in lignes)
        ligne_plus_longue = max(lignes, key=len) if lignes else ""

        return {
            'lignes': nb_lignes,
            'mots': nb_mots,
            'caracteres': nb_caracteres,
            'ligne_plus_longue': ligne_plus_longue.strip()
        }
    except FileNotFoundError:
        return None

# Testez votre fonction
stats = analyser_fichier('test.txt')
if stats:
    print(f"Statistiques du fichier:")
    for cle, valeur in stats.items():
        print(f"  {cle}: {valeur}")
```

## Bonnes pratiques

### 1. Toujours utiliser `with`
```python
# ✅ Correct
with open('fichier.txt', 'r') as f:
    contenu = f.read()

# ❌ À éviter
f = open('fichier.txt', 'r')
contenu = f.read()
f.close()
```

### 2. Spécifier l'encodage
```python
# ✅ Correct
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

# ❌ À éviter (encodage par défaut)
with open('fichier.txt', 'r') as f:
    contenu = f.read()
```

### 3. Gérer les erreurs
```python
# ✅ Correct
try:
    with open('fichier.txt', 'r') as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier non trouvé")
```

### 4. Itérer efficacement
```python
# ✅ Efficace pour gros fichiers
with open('gros_fichier.txt', 'r') as f:
    for ligne in f:
        traiter_ligne(ligne)

# ❌ Inefficace pour gros fichiers
with open('gros_fichier.txt', 'r') as f:
    lignes = f.readlines()  # Charge tout en mémoire
    for ligne in lignes:
        traiter_ligne(ligne)
```

## Résumé

Dans cette section, vous avez appris :

- **Les bases** : ouvrir, lire, écrire et fermer des fichiers
- **Les modes** : lecture ('r'), écriture ('w'), ajout ('a')
- **Le gestionnaire de contexte** `with` pour une gestion automatique des ressources
- **Les différentes méthodes** : `read()`, `readline()`, `readlines()`, `write()`
- **L'encodage** : importance d'UTF-8 et gestion des erreurs
- **Les fichiers binaires** : lecture et écriture de données non-textuelles
- **La gestion d'erreurs** : FileNotFoundError, PermissionError, etc.
- **Les bonnes pratiques** : sécurité, performance et lisibilité

La prochaine section abordera les formats de données structurées comme JSON et CSV, qui s'appuient sur ces concepts fondamentaux.

⏭️
