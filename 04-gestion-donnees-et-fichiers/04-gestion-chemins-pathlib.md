🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.4 Gestion des Chemins avec Pathlib

## Introduction

Travailler avec des fichiers et des dossiers nécessite de manipuler des **chemins** (paths). Traditionnellement, on utilisait le module `os.path`, mais Python 3.4 a introduit **pathlib**, une approche moderne et orientée objet qui rend la manipulation de chemins beaucoup plus simple et intuitive.

**Pourquoi pathlib ?**
- ✅ Syntaxe plus claire et lisible
- ✅ Orienté objet (les chemins sont des objets)
- ✅ Compatible Windows, Linux et macOS
- ✅ Méthodes intégrées pour toutes les opérations courantes
- ✅ Plus sûr et moins sujet aux erreurs

---

## Première Approche : L'Ancienne Méthode vs pathlib

### Avec `os.path` (ancienne méthode)

```python
import os

# Construire un chemin
chemin = os.path.join('dossier', 'sous_dossier', 'fichier.txt')

# Vérifier l'existence
if os.path.exists(chemin):
    # Obtenir le nom du fichier
    nom = os.path.basename(chemin)
    # Obtenir l'extension
    extension = os.path.splitext(nom)[1]
```

### Avec `pathlib` (méthode moderne)

```python
from pathlib import Path

# Construire un chemin
chemin = Path('dossier') / 'sous_dossier' / 'fichier.txt'

# Vérifier l'existence
if chemin.exists():
    # Obtenir le nom du fichier
    nom = chemin.name
    # Obtenir l'extension
    extension = chemin.suffix
```

**Beaucoup plus clair, n'est-ce pas ?** 😊

---

## La Classe `Path`

### Importation

```python
from pathlib import Path
```

### Créer un Objet Path

```python
from pathlib import Path

# Chemin relatif
chemin1 = Path('mon_fichier.txt')

# Chemin absolu
chemin2 = Path('/home/utilisateur/documents/fichier.txt')

# Chemin Windows (fonctionne aussi sur Windows)
chemin3 = Path('C:/Users/Alice/Documents/fichier.txt')

# Chemin du répertoire courant
repertoire_actuel = Path('.')

# Chemin du répertoire parent
repertoire_parent = Path('..')

print(chemin1)  
print(type(chemin1))  # <class 'pathlib.PosixPath'> ou WindowsPath  
```

---

## Construction de Chemins

### Utiliser l'Opérateur `/` (recommandé)

L'une des fonctionnalités les plus élégantes de pathlib est l'utilisation de `/` pour joindre des chemins :

```python
from pathlib import Path

# Construction progressive
base = Path('mes_documents')  
sous_dossier = base / 'projets'  
fichier = sous_dossier / 'python' / 'script.py'  

print(fichier)
# Résultat : mes_documents/projets/python/script.py
```

### Joindre avec `joinpath()`

```python
from pathlib import Path

chemin = Path('dossier').joinpath('sous_dossier', 'fichier.txt')  
print(chemin)  
# Résultat : dossier/sous_dossier/fichier.txt
```

### Construction à partir de plusieurs parties

```python
from pathlib import Path

# Créer un chemin complexe
projet = Path('projets')  
python = 'python'  
app = 'mon_app'  
fichier = 'main.py'  

chemin_complet = projet / python / app / fichier  
print(chemin_complet)  
# Résultat : projets/python/mon_app/main.py
```

---

## Propriétés des Chemins

Un objet `Path` dispose de nombreuses propriétés utiles :

```python
from pathlib import Path

chemin = Path('/home/alice/documents/projet/code/script.py')

# Nom complet du fichier
print(f"Nom complet : {chemin.name}")
# Résultat : script.py

# Nom sans extension
print(f"Nom sans extension : {chemin.stem}")
# Résultat : script

# Extension
print(f"Extension : {chemin.suffix}")
# Résultat : .py

# Toutes les extensions (pour .tar.gz par exemple)
chemin2 = Path('archive.tar.gz')  
print(f"Extensions : {chemin2.suffixes}")  
# Résultat : ['.tar', '.gz']

# Répertoire parent
print(f"Parent : {chemin.parent}")
# Résultat : /home/alice/documents/projet/code

# Tous les parents
print(f"Parents : {list(chemin.parents)}")
# Résultat : [PosixPath('/home/alice/documents/projet/code'), ...]

# Parties du chemin
print(f"Parties : {chemin.parts}")
# Résultat : ('/', 'home', 'alice', 'documents', 'projet', 'code', 'script.py')
```

### Exemple Complet

```python
from pathlib import Path

fichier = Path('documents/photos/vacances/plage.jpg')

print(f"📁 Chemin complet : {fichier}")  
print(f"📄 Nom du fichier : {fichier.name}")  
print(f"🏷️  Nom sans extension : {fichier.stem}")  
print(f"🔖 Extension : {fichier.suffix}")  
print(f"📂 Dossier parent : {fichier.parent}")  
print(f"🗂️  Grand-parent : {fichier.parent.parent}")  
```

---

## Chemins Absolus et Relatifs

### Chemin Absolu

Un **chemin absolu** commence à la racine du système de fichiers :

```python
from pathlib import Path

# Obtenir le chemin absolu
chemin_relatif = Path('mon_fichier.txt')  
chemin_absolu = chemin_relatif.absolute()  

print(f"Relatif : {chemin_relatif}")  
print(f"Absolu : {chemin_absolu}")  
```

### Résoudre un Chemin (resolve)

La méthode `resolve()` retourne le chemin absolu en résolvant les liens symboliques :

```python
from pathlib import Path

chemin = Path('.')  
chemin_resolu = chemin.resolve()  

print(f"Répertoire courant : {chemin_resolu}")
```

### Chemin Relatif Entre Deux Chemins

```python
from pathlib import Path

chemin1 = Path('/home/alice/projets/python/app')  
chemin2 = Path('/home/alice/projets/data/fichier.csv')  

# Obtenir le chemin relatif de chemin2 par rapport à chemin1
relatif = chemin2.relative_to(Path('/home/alice/projets'))  
print(relatif)  
# Résultat : data/fichier.csv
```

---

## Vérifications et Tests

### Vérifier l'Existence

```python
from pathlib import Path

chemin = Path('mon_fichier.txt')

# Existe-t-il ?
if chemin.exists():
    print("Le chemin existe")
else:
    print("Le chemin n'existe pas")
```

### Types de Chemins

```python
from pathlib import Path

chemin = Path('documents/fichier.txt')

# Est-ce un fichier ?
if chemin.is_file():
    print("C'est un fichier")

# Est-ce un dossier ?
if chemin.is_dir():
    print("C'est un dossier")

# Est-ce un lien symbolique ?
if chemin.is_symlink():
    print("C'est un lien symbolique")

# Est-ce un chemin absolu ?
if chemin.is_absolute():
    print("C'est un chemin absolu")
```

### Exemple de Vérification Complète

```python
from pathlib import Path

def analyser_chemin(chemin_str):
    chemin = Path(chemin_str)

    print(f"\n{'='*50}")
    print(f"Analyse de : {chemin}")
    print(f"{'='*50}")

    if not chemin.exists():
        print("❌ Le chemin n'existe pas")
        return

    print("✅ Le chemin existe")

    if chemin.is_file():
        print(f"📄 Type : Fichier")
        taille = chemin.stat().st_size
        print(f"📊 Taille : {taille} octets")
    elif chemin.is_dir():
        print(f"📁 Type : Dossier")
        nb_fichiers = len(list(chemin.iterdir()))
        print(f"📊 Nombre d'éléments : {nb_fichiers}")

# Utilisation
analyser_chemin('mon_fichier.txt')
```

---

## Opérations sur les Fichiers et Dossiers

### Créer un Dossier

```python
from pathlib import Path

# Créer un dossier
nouveau_dossier = Path('mon_nouveau_dossier')  
nouveau_dossier.mkdir(exist_ok=True)  
print(f"Dossier créé : {nouveau_dossier}")  

# Créer une hiérarchie de dossiers
chemin = Path('projets/python/mon_app/src')  
chemin.mkdir(parents=True, exist_ok=True)  
print(f"Hiérarchie créée : {chemin}")  
```

**Paramètres importants :**
- `parents=True` : crée les dossiers parents si nécessaire
- `exist_ok=True` : ne génère pas d'erreur si le dossier existe déjà

### Supprimer un Fichier ou Dossier

```python
from pathlib import Path

# Supprimer un fichier
fichier = Path('fichier_temporaire.txt')  
if fichier.exists():  
    fichier.unlink()
    print("Fichier supprimé")

# Supprimer un dossier vide
dossier = Path('dossier_vide')  
if dossier.exists() and dossier.is_dir():  
    dossier.rmdir()
    print("Dossier supprimé")
```

**Note :** `rmdir()` ne fonctionne que sur des dossiers vides.

### Supprimer un Dossier Non Vide

```python
import shutil  
from pathlib import Path  

dossier = Path('dossier_avec_contenu')  
if dossier.exists():  
    shutil.rmtree(dossier)
    print("Dossier et contenu supprimés")
```

### Renommer ou Déplacer

```python
from pathlib import Path

# Renommer un fichier
ancien = Path('ancien_nom.txt')  
nouveau = Path('nouveau_nom.txt')  

if ancien.exists():
    ancien.rename(nouveau)
    print(f"Renommé : {ancien} → {nouveau}")

# Déplacer vers un autre dossier
fichier = Path('fichier.txt')  
destination = Path('dossier/fichier.txt')  

if fichier.exists():
    fichier.rename(destination)
    print(f"Déplacé vers : {destination}")
```

### Copier un Fichier

```python
import shutil  
from pathlib import Path  

source = Path('original.txt')  
destination = Path('copie.txt')  

if source.exists():
    shutil.copy(source, destination)
    print(f"Fichier copié : {source} → {destination}")
```

---

## Lister le Contenu d'un Dossier

### Avec `iterdir()`

```python
from pathlib import Path

dossier = Path('.')

print("Contenu du dossier courant :")  
for element in dossier.iterdir():  
    type_element = "📁" if element.is_dir() else "📄"
    print(f"{type_element} {element.name}")
```

### Filtrer par Type

```python
from pathlib import Path

dossier = Path('.')

# Seulement les fichiers
print("Fichiers :")  
for fichier in dossier.iterdir():  
    if fichier.is_file():
        print(f"  📄 {fichier.name}")

# Seulement les dossiers
print("\nDossiers :")  
for sous_dossier in dossier.iterdir():  
    if sous_dossier.is_dir():
        print(f"  📁 {sous_dossier.name}")
```

---

## Recherche de Fichiers avec `glob()`

La méthode `glob()` permet de rechercher des fichiers selon un pattern :

### Patterns de Base

```python
from pathlib import Path

dossier = Path('.')

# Tous les fichiers .txt
print("Fichiers .txt :")  
for fichier in dossier.glob('*.txt'):  
    print(f"  {fichier.name}")

# Tous les fichiers .py
print("\nFichiers .py :")  
for fichier in dossier.glob('*.py'):  
    print(f"  {fichier.name}")
```

### Recherche Récursive

```python
from pathlib import Path

dossier = Path('.')

# Rechercher tous les .txt récursivement (dans tous les sous-dossiers)
print("Tous les .txt (récursif) :")  
for fichier in dossier.rglob('*.txt'):  
    print(f"  {fichier}")
```

**Note :** `rglob()` = recherche récursive (recursive glob)

### Patterns Avancés

```python
from pathlib import Path

dossier = Path('documents')

# Fichiers commençant par "test"
for fichier in dossier.glob('test*.py'):
    print(fichier)

# Fichiers dans un sous-dossier spécifique
for fichier in dossier.glob('scripts/*.py'):
    print(fichier)

# Plusieurs extensions (glob ne supporte pas {txt,md,pdf})
for fichier in dossier.iterdir():
    if fichier.suffix in ('.txt', '.md', '.pdf'):
        print(fichier)
```

### Exemple : Trouver Tous les Scripts Python

```python
from pathlib import Path

def trouver_scripts_python(racine='.'):
    """Trouve tous les fichiers .py récursivement"""
    racine = Path(racine)
    scripts = list(racine.rglob('*.py'))

    print(f"🔍 {len(scripts)} scripts Python trouvés :\n")

    for script in sorted(scripts):
        taille = script.stat().st_size
        print(f"📄 {script} ({taille} octets)")

    return scripts

# Utilisation
trouver_scripts_python('.')
```

---

## Informations sur les Fichiers

### Obtenir les Statistiques

```python
from pathlib import Path  
from datetime import datetime  

fichier = Path('mon_fichier.txt')

if fichier.exists():
    stats = fichier.stat()

    # Taille
    taille = stats.st_size
    print(f"Taille : {taille} octets ({taille / 1024:.2f} Ko)")

    # Date de modification
    timestamp = stats.st_mtime
    date_modif = datetime.fromtimestamp(timestamp)
    print(f"Dernière modification : {date_modif}")

    # Date de création (Windows) ou changement de statut (Unix)
    timestamp_creation = stats.st_ctime
    date_creation = datetime.fromtimestamp(timestamp_creation)
    print(f"Création/Changement : {date_creation}")
```

### Exemple : Afficher des Informations Détaillées

```python
from pathlib import Path  
from datetime import datetime  

def infos_fichier(chemin_str):
    """Affiche des informations détaillées sur un fichier"""
    chemin = Path(chemin_str)

    if not chemin.exists():
        print(f"❌ {chemin} n'existe pas")
        return

    print(f"\n{'='*60}")
    print(f"📄 Informations : {chemin.name}")
    print(f"{'='*60}")

    # Type
    if chemin.is_file():
        print(f"Type : Fichier")
    elif chemin.is_dir():
        print(f"Type : Dossier")

    # Chemin
    print(f"Chemin complet : {chemin.absolute()}")
    print(f"Dossier parent : {chemin.parent}")

    if chemin.is_file():
        # Extension
        print(f"Extension : {chemin.suffix}")

        # Statistiques
        stats = chemin.stat()
        taille = stats.st_size
        print(f"Taille : {taille:,} octets")

        # Dates
        modif = datetime.fromtimestamp(stats.st_mtime)
        print(f"Dernière modification : {modif.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"{'='*60}\n")

# Utilisation
infos_fichier('mon_script.py')
```

---

## Lecture et Écriture de Fichiers

Pathlib simplifie aussi la lecture et l'écriture de fichiers :

### Lire un Fichier

```python
from pathlib import Path

fichier = Path('mon_fichier.txt')

# Lire tout le contenu
contenu = fichier.read_text(encoding='utf-8')  
print(contenu)  

# Lire un fichier binaire
fichier_bin = Path('image.jpg')  
contenu_bin = fichier_bin.read_bytes()  
print(f"Taille : {len(contenu_bin)} octets")  
```

### Écrire dans un Fichier

```python
from pathlib import Path

fichier = Path('nouveau_fichier.txt')

# Écrire du texte
fichier.write_text("Bonjour depuis pathlib !\n", encoding='utf-8')

# Écrire des données binaires
fichier_bin = Path('donnees.bin')  
donnees = bytes([0, 1, 2, 3, 4])  
fichier_bin.write_bytes(donnees)  
```

### Exemple : Traiter des Fichiers

```python
from pathlib import Path

def traiter_fichiers_texte(dossier_str):
    """Compte les lignes dans tous les fichiers .txt"""
    dossier = Path(dossier_str)

    for fichier in dossier.glob('*.txt'):
        contenu = fichier.read_text(encoding='utf-8')
        nb_lignes = len(contenu.splitlines())
        nb_mots = len(contenu.split())

        print(f"📄 {fichier.name}")
        print(f"   Lignes : {nb_lignes}")
        print(f"   Mots : {nb_mots}\n")

# Utilisation
traiter_fichiers_texte('documents')
```

---

## Exemple Pratique : Organiser des Fichiers

Voici un exemple complet qui organise des fichiers par extension :

```python
from pathlib import Path  
import shutil  

def organiser_fichiers(dossier_source):
    """Organise les fichiers par extension dans des sous-dossiers"""
    source = Path(dossier_source)

    if not source.exists():
        print(f"❌ Le dossier {source} n'existe pas")
        return

    print(f"🗂️  Organisation des fichiers dans {source}\n")

    # Parcourir tous les fichiers
    for fichier in source.iterdir():
        # Ignorer les dossiers
        if not fichier.is_file():
            continue

        # Obtenir l'extension (sans le point)
        extension = fichier.suffix[1:] if fichier.suffix else 'sans_extension'

        # Créer le dossier pour cette extension
        dossier_extension = source / extension
        dossier_extension.mkdir(exist_ok=True)

        # Déplacer le fichier
        destination = dossier_extension / fichier.name

        # Si le fichier existe déjà, ajouter un numéro
        compteur = 1
        while destination.exists():
            nouveau_nom = f"{fichier.stem}_{compteur}{fichier.suffix}"
            destination = dossier_extension / nouveau_nom
            compteur += 1

        shutil.move(fichier, destination)
        print(f"📁 {fichier.name} → {extension}/{destination.name}")

    print("\n✅ Organisation terminée !")

# Utilisation
organiser_fichiers('telechargements')
```

---

## Exemple Pratique : Backup de Fichiers

```python
from pathlib import Path  
import shutil  
from datetime import datetime  

def backup_fichiers(dossier_source, dossier_backup):
    """Crée une sauvegarde horodatée d'un dossier"""
    source = Path(dossier_source)
    backup = Path(dossier_backup)

    if not source.exists():
        print(f"❌ {source} n'existe pas")
        return

    # Créer un nom avec timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dossier_destination = backup / f"backup_{timestamp}"

    # Créer le dossier de backup
    dossier_destination.mkdir(parents=True, exist_ok=True)

    print(f"💾 Backup en cours...")
    print(f"Source : {source}")
    print(f"Destination : {dossier_destination}\n")

    compteur = 0
    for fichier in source.rglob('*'):
        if fichier.is_file():
            # Calculer le chemin relatif
            chemin_relatif = fichier.relative_to(source)
            destination = dossier_destination / chemin_relatif

            # Créer les dossiers parents si nécessaire
            destination.parent.mkdir(parents=True, exist_ok=True)

            # Copier le fichier
            shutil.copy2(fichier, destination)
            compteur += 1
            print(f"✓ {chemin_relatif}")

    print(f"\n✅ Backup terminé : {compteur} fichiers copiés")
    print(f"📁 Dossier : {dossier_destination}")

# Utilisation
backup_fichiers('projets/mon_app', 'backups')
```

---

## Compatibilité Multi-Plateformes

Pathlib gère automatiquement les différences entre Windows, Linux et macOS :

```python
from pathlib import Path

# Sur Windows
chemin_windows = Path('C:/Users/Alice/Documents/fichier.txt')

# Sur Linux/macOS
chemin_unix = Path('/home/alice/documents/fichier.txt')

# Pathlib adapte automatiquement selon l'OS
chemin = Path.home() / 'documents' / 'fichier.txt'  
print(chemin)  
# Windows : C:\Users\Alice\documents\fichier.txt
# Linux : /home/alice/documents/fichier.txt
```

### Chemins Spéciaux

```python
from pathlib import Path

# Dossier personnel de l'utilisateur
home = Path.home()  
print(f"Home : {home}")  

# Répertoire de travail actuel
cwd = Path.cwd()  
print(f"Répertoire courant : {cwd}")  
```

---

## Conversion avec l'Ancien Module `os`

Si nécessaire, vous pouvez convertir entre Path et chaînes :

```python
from pathlib import Path  
import os  

# Path → str
chemin = Path('dossier/fichier.txt')  
chemin_str = str(chemin)  
print(f"String : {chemin_str}")  

# Les fonctions standard acceptent directement des objets Path
with open(chemin, 'r', encoding='utf-8') as f:
    contenu = f.read()

# os.path fonctionne aussi directement avec Path
os.path.exists(chemin)  # Pas besoin de str()
```

---

## Comparaison : os.path vs pathlib

### Tableau Comparatif

| Opération | os.path | pathlib |
|-----------|---------|---------|
| **Joindre chemins** | `os.path.join(a, b)` | `Path(a) / b` |
| **Nom fichier** | `os.path.basename(p)` | `Path(p).name` |
| **Extension** | `os.path.splitext(p)[1]` | `Path(p).suffix` |
| **Existe ?** | `os.path.exists(p)` | `Path(p).exists()` |
| **Est fichier ?** | `os.path.isfile(p)` | `Path(p).is_file()` |
| **Est dossier ?** | `os.path.isdir(p)` | `Path(p).is_dir()` |
| **Absolu** | `os.path.abspath(p)` | `Path(p).absolute()` |
| **Parent** | `os.path.dirname(p)` | `Path(p).parent` |
| **Lister** | `os.listdir(p)` | `Path(p).iterdir()` |

### Exemple de Migration

**Avant (os.path) :**
```python
import os

base = 'projets'  
sous_dossier = 'python'  
fichier = 'script.py'  

chemin = os.path.join(base, sous_dossier, fichier)

if os.path.exists(chemin):
    nom = os.path.basename(chemin)
    extension = os.path.splitext(nom)[1]
    taille = os.path.getsize(chemin)
```

**Après (pathlib) :**
```python
from pathlib import Path

chemin = Path('projets') / 'python' / 'script.py'

if chemin.exists():
    nom = chemin.name
    extension = chemin.suffix
    taille = chemin.stat().st_size
```

---

## Bonnes Pratiques

### 1. Toujours utiliser Path pour les nouveaux projets

```python
# ✅ Recommandé
from pathlib import Path  
chemin = Path('dossier') / 'fichier.txt'  

# ❌ Ancien style
import os  
chemin = os.path.join('dossier', 'fichier.txt')  
```

### 2. Utiliser Path.home() pour les chemins utilisateurs

```python
# ✅ Portable
from pathlib import Path  
config = Path.home() / '.config' / 'mon_app' / 'config.json'  

# ❌ Codé en dur
config = '/home/alice/.config/mon_app/config.json'  # Ne marche que sur Linux !
```

### 3. Vérifier l'existence avant les opérations

```python
from pathlib import Path

fichier = Path('donnees.txt')

# ✅ Bon
if fichier.exists():
    contenu = fichier.read_text()

# ❌ Peut causer une erreur
contenu = fichier.read_text()  # FileNotFoundError si n'existe pas
```

### 4. Utiliser parents=True pour créer des dossiers

```python
from pathlib import Path

# ✅ Crée toute la hiérarchie
chemin = Path('projets/python/mon_app/src')  
chemin.mkdir(parents=True, exist_ok=True)  

# ❌ Erreur si les parents n'existent pas
chemin.mkdir()  # FileNotFoundError
```

### 5. Préférer rglob() pour les recherches récursives

```python
from pathlib import Path

# ✅ Recherche récursive
fichiers = list(Path('.').rglob('*.py'))

# ❌ Moins lisible avec os.walk
import os  
fichiers = []  
for root, dirs, files in os.walk('.'):  
    for file in files:
        if file.endswith('.py'):
            fichiers.append(os.path.join(root, file))
```

---

## Pièges Courants et Solutions

### 1. Confondre / avec +

```python
from pathlib import Path

# ✅ Correct
chemin = Path('base') / 'sous_dossier'

# ❌ Erreur de type
# chemin = Path('base') + 'sous_dossier'  # TypeError
```

### 2. Utiliser rmdir() sur un dossier non vide

```python
from pathlib import Path  
import shutil  

dossier = Path('mon_dossier')

# ❌ Erreur si le dossier contient des fichiers
# dossier.rmdir()  # OSError

# ✅ Pour supprimer avec contenu
shutil.rmtree(dossier)
```

---

## Résumé

### Opérations Principales

```python
from pathlib import Path

# Création
chemin = Path('dossier') / 'fichier.txt'

# Propriétés
chemin.name          # Nom du fichier  
chemin.stem          # Nom sans extension  
chemin.suffix        # Extension  
chemin.parent        # Dossier parent  
chemin.absolute()    # Chemin absolu  

# Tests
chemin.exists()      # Existe ?  
chemin.is_file()     # Est un fichier ?  
chemin.is_dir()      # Est un dossier ?  

# Opérations
chemin.mkdir()       # Créer un dossier  
chemin.unlink()      # Supprimer un fichier  
chemin.rename(new)   # Renommer/déplacer  

# Lecture/Écriture
chemin.read_text()   # Lire le contenu  
chemin.write_text()  # Écrire du contenu  

# Recherche
Path('.').iterdir()  # Lister le contenu  
Path('.').glob('*.txt')   # Recherche  
Path('.').rglob('*.py')   # Recherche récursive  
```

### Points Clés

✅ **pathlib** est la méthode moderne pour gérer les chemins  
✅ Syntaxe orientée objet plus claire que os.path  
✅ Opérateur `/` pour joindre des chemins naturellement  
✅ Compatible Windows, Linux et macOS automatiquement  
✅ Méthodes intégrées pour toutes les opérations courantes  
✅ Utilisez `rglob()` pour les recherches récursives  
✅ Toujours utiliser `parents=True` et `exist_ok=True` pour mkdir()

### Migration de os.path

Si vous avez du code utilisant `os.path`, migrez progressivement vers `pathlib` :
- Plus lisible
- Moins d'erreurs
- Code plus maintenable
- Standard moderne

---

Vous maîtrisez maintenant pathlib ! C'est un outil essentiel pour tout développeur Python moderne. Utilisez-le dans tous vos nouveaux projets !

⏭️ [Programmation fonctionnelle](/05-programmation-fonctionnelle/README.md)
