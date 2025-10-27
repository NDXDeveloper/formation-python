🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.1 Les modules os, sys et subprocess

## Introduction

Dans cette section, nous allons découvrir trois modules essentiels de la bibliothèque standard Python qui permettent d'interagir avec le système d'exploitation et l'environnement d'exécution. Ces modules sont indispensables pour créer des programmes qui doivent communiquer avec le système, gérer des fichiers, ou exécuter d'autres programmes.

---

## Le module `os` - Interaction avec le système d'exploitation

Le module `os` fournit des fonctions pour interagir avec le système d'exploitation de manière portable (Windows, Linux, macOS).

### Import du module

```python
import os
```

### Obtenir des informations sur le système

```python
# Obtenir le nom du système d'exploitation
print(os.name)  # 'posix' pour Linux/Mac, 'nt' pour Windows

# Obtenir le répertoire de travail actuel
repertoire_actuel = os.getcwd()
print(f"Répertoire actuel : {repertoire_actuel}")

# Obtenir le séparateur de chemin du système
print(os.sep)  # '/' pour Linux/Mac, '\' pour Windows
```

### Manipulation des répertoires

```python
# Créer un nouveau répertoire
os.mkdir("nouveau_dossier")

# Créer plusieurs répertoires imbriqués
os.makedirs("dossier/sous_dossier/sous_sous_dossier")

# Changer de répertoire de travail
os.chdir("nouveau_dossier")
print(os.getcwd())  # Affiche le nouveau répertoire

# Revenir au répertoire parent
os.chdir("..")

# Supprimer un répertoire vide
os.rmdir("nouveau_dossier")

# Supprimer des répertoires imbriqués
os.removedirs("dossier/sous_dossier/sous_sous_dossier")
```

### Lister le contenu d'un répertoire

```python
# Lister tous les fichiers et dossiers
contenu = os.listdir(".")
print(contenu)

# Exemple plus détaillé avec filtrage
for element in os.listdir("."):
    chemin_complet = os.path.join(".", element)
    if os.path.isfile(chemin_complet):
        print(f"📄 Fichier : {element}")
    elif os.path.isdir(chemin_complet):
        print(f"📁 Dossier : {element}")
```

### Manipulation des chemins avec `os.path`

Le sous-module `os.path` est très utile pour travailler avec des chemins de fichiers de manière portable.

```python
# Joindre des parties de chemin de manière portable
chemin = os.path.join("dossier", "sous_dossier", "fichier.txt")
print(chemin)  # Utilise automatiquement le bon séparateur

# Vérifier si un chemin existe
if os.path.exists("mon_fichier.txt"):
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")

# Vérifier si c'est un fichier
if os.path.isfile("mon_fichier.txt"):
    print("C'est un fichier")

# Vérifier si c'est un répertoire
if os.path.isdir("mon_dossier"):
    print("C'est un répertoire")

# Obtenir le chemin absolu
chemin_absolu = os.path.abspath("fichier.txt")
print(chemin_absolu)

# Séparer le nom du fichier et l'extension
nom_complet = "document.pdf"
nom, extension = os.path.splitext(nom_complet)
print(f"Nom : {nom}, Extension : {extension}")

# Séparer le répertoire et le nom de fichier
chemin = "/home/utilisateur/documents/rapport.txt"
repertoire, fichier = os.path.split(chemin)
print(f"Répertoire : {repertoire}")
print(f"Fichier : {fichier}")

# Obtenir la taille d'un fichier en octets
if os.path.exists("mon_fichier.txt"):
    taille = os.path.getsize("mon_fichier.txt")
    print(f"Taille du fichier : {taille} octets")
```

### Manipulation de fichiers

```python
# Renommer un fichier ou un dossier
os.rename("ancien_nom.txt", "nouveau_nom.txt")

# Supprimer un fichier
os.remove("fichier_a_supprimer.txt")

# Obtenir des informations sur un fichier
stats = os.stat("mon_fichier.txt")
print(f"Taille : {stats.st_size} octets")
print(f"Dernière modification : {stats.st_mtime}")
```

### Variables d'environnement

Les variables d'environnement sont des valeurs stockées par le système d'exploitation que les programmes peuvent lire.

```python
# Lire une variable d'environnement
home = os.environ.get("HOME")  # Répertoire home de l'utilisateur
print(f"Répertoire home : {home}")

# Lire avec valeur par défaut si la variable n'existe pas
api_key = os.environ.get("API_KEY", "cle_par_defaut")

# Lister toutes les variables d'environnement
for cle, valeur in os.environ.items():
    print(f"{cle} = {valeur}")

# Définir une variable d'environnement (temporaire, pour le programme)
os.environ["MA_VARIABLE"] = "ma_valeur"
```

### Exemple pratique : Parcourir une arborescence

```python
# Parcourir récursivement tous les fichiers d'un répertoire
for racine, dossiers, fichiers in os.walk("."):
    print(f"\n📁 Dossier : {racine}")
    for fichier in fichiers:
        chemin_complet = os.path.join(racine, fichier)
        taille = os.path.getsize(chemin_complet)
        print(f"  📄 {fichier} ({taille} octets)")
```

---

## Le module `sys` - Interaction avec l'interpréteur Python

Le module `sys` permet d'interagir avec l'interpréteur Python et d'accéder à des informations sur l'environnement d'exécution.

### Import du module

```python
import sys
```

### Informations sur l'interpréteur

```python
# Version de Python
print(sys.version)
print(sys.version_info)  # Plus structuré

# Plateforme d'exécution
print(sys.platform)  # 'linux', 'win32', 'darwin' (macOS), etc.

# Chemin de l'exécutable Python
print(sys.executable)
```

### Arguments de ligne de commande

Lorsque vous exécutez un script Python avec des arguments, ceux-ci sont accessibles via `sys.argv`.

```python
# Fichier : mon_script.py
import sys

# sys.argv est une liste contenant le nom du script et les arguments
print(f"Nom du script : {sys.argv[0]}")
print(f"Nombre d'arguments : {len(sys.argv) - 1}")

if len(sys.argv) > 1:
    print("Arguments reçus :")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Argument {i} : {arg}")
else:
    print("Aucun argument fourni")
```

Si vous exécutez ce script avec : `python mon_script.py bonjour monde 123`

Le résultat sera :
```
Nom du script : mon_script.py
Nombre d'arguments : 3
Arguments reçus :
  Argument 1 : bonjour
  Argument 2 : monde
  Argument 3 : 123
```

### Chemins de recherche des modules

```python
# Liste des répertoires où Python cherche les modules
print(sys.path)

# Ajouter un répertoire personnalisé
sys.path.append("/mon/repertoire/personnel")
```

### Flux d'entrée/sortie standard

```python
# Écrire sur la sortie standard (stdout)
sys.stdout.write("Message sur stdout\n")

# Écrire sur la sortie d'erreur (stderr)
sys.stderr.write("Message d'erreur\n")

# Lire depuis l'entrée standard (stdin)
print("Entrez votre nom :")
nom = sys.stdin.readline().strip()
print(f"Bonjour {nom} !")
```

### Terminer un programme

```python
# Quitter le programme avec un code de sortie
# 0 = succès, autre valeur = erreur
sys.exit(0)  # Succès
# sys.exit(1)  # Erreur

# Exemple d'utilisation
import sys

def verifier_arguments():
    if len(sys.argv) < 2:
        print("Erreur : Au moins un argument est requis")
        sys.exit(1)  # Quitte avec code d'erreur
    print(f"Traitement de : {sys.argv[1]}")
    sys.exit(0)  # Quitte avec succès
```

### Informations sur la mémoire

```python
# Obtenir la taille en mémoire d'un objet
liste = [1, 2, 3, 4, 5]
taille = sys.getsizeof(liste)
print(f"Taille de la liste : {taille} octets")

chaine = "Bonjour le monde"
print(f"Taille de la chaîne : {sys.getsizeof(chaine)} octets")
```

### Exemple pratique : Script avec arguments

```python
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage : python script.py <nombre1> <nombre2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        resultat = a + b
        print(f"La somme de {a} et {b} est {resultat}")
        sys.exit(0)
    except ValueError:
        print("Erreur : Les arguments doivent être des nombres")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## Le module `subprocess` - Exécuter des commandes externes

Le module `subprocess` permet d'exécuter des commandes système et d'autres programmes depuis Python. C'est le moyen moderne et recommandé pour lancer des processus externes.

### Import du module

```python
import subprocess
```

### Exécuter une commande simple avec `run()`

La fonction `subprocess.run()` est la méthode recommandée pour exécuter des commandes.

```python
# Exemple simple : lister les fichiers (Linux/Mac)
resultat = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Afficher la sortie
print(resultat.stdout)

# Vérifier le code de retour (0 = succès)
print(f"Code de retour : {resultat.returncode}")
```

Pour Windows, la commande équivalente serait :
```python
resultat = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
```

### Paramètres importants de `run()`

```python
# capture_output=True : Capture stdout et stderr
# text=True : Retourne des chaînes de caractères (pas des bytes)
# shell=True : Exécute via le shell (nécessaire pour certaines commandes)
# check=True : Lève une exception si la commande échoue

resultat = subprocess.run(
    ["echo", "Bonjour"],
    capture_output=True,
    text=True,
    check=True
)

print(resultat.stdout)  # "Bonjour\n"
```

### Gérer les erreurs

```python
import subprocess

try:
    # Cette commande n'existe pas
    resultat = subprocess.run(
        ["commande_inexistante"],
        capture_output=True,
        text=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de la commande")
    print(f"Code de retour : {e.returncode}")
    print(f"Message d'erreur : {e.stderr}")
except FileNotFoundError:
    print("La commande n'a pas été trouvée")
```

### Exemple pratique : Obtenir des informations système

```python
import subprocess
import sys

def obtenir_info_python():
    """Obtient la version de Python via subprocess"""
    resultat = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True
    )
    return resultat.stdout.strip()

def lister_fichiers_python(repertoire="."):
    """Liste tous les fichiers Python dans un répertoire"""
    if sys.platform.startswith("win"):
        # Windows
        resultat = subprocess.run(
            ["dir", "/b", "*.py"],
            shell=True,
            capture_output=True,
            text=True,
            cwd=repertoire
        )
    else:
        # Linux/Mac
        resultat = subprocess.run(
            ["ls", "*.py"],
            shell=True,
            capture_output=True,
            text=True,
            cwd=repertoire
        )

    if resultat.returncode == 0:
        fichiers = resultat.stdout.strip().split("\n")
        return [f for f in fichiers if f]
    return []

# Utilisation
print(f"Version Python : {obtenir_info_python()}")
print(f"Fichiers Python : {lister_fichiers_python()}")
```

### Envoyer des données à un processus (stdin)

```python
# Exemple : utiliser 'grep' pour filtrer du texte (Linux/Mac)
texte = "ligne1\nligne2 important\nligne3\nligne4 important"

resultat = subprocess.run(
    ["grep", "important"],
    input=texte,
    capture_output=True,
    text=True
)

print("Lignes filtrées :")
print(resultat.stdout)
```

### Exécuter des commandes complexes avec le shell

Pour des commandes avec des pipes ou des redirections, utilisez `shell=True` :

```python
# Attention : shell=True peut être dangereux avec des entrées non fiables
import subprocess

# Linux/Mac : Compter le nombre de fichiers Python
resultat = subprocess.run(
    "ls *.py | wc -l",
    shell=True,
    capture_output=True,
    text=True
)

print(f"Nombre de fichiers Python : {resultat.stdout.strip()}")
```

**⚠️ Avertissement de sécurité** : Utiliser `shell=True` avec des données provenant d'utilisateurs peut créer des failles de sécurité (injection de commandes). Préférez toujours passer les commandes sous forme de liste sans shell=True quand c'est possible.

### Exemple pratique : Créer une sauvegarde

```python
import subprocess
import os
from datetime import datetime

def creer_sauvegarde(dossier_source, dossier_backup):
    """Crée une archive tar.gz du dossier source (Linux/Mac)"""

    # Créer le nom de la sauvegarde avec la date
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_archive = f"backup_{timestamp}.tar.gz"
    chemin_archive = os.path.join(dossier_backup, nom_archive)

    # Créer le dossier de backup s'il n'existe pas
    os.makedirs(dossier_backup, exist_ok=True)

    # Exécuter la commande tar
    try:
        resultat = subprocess.run(
            ["tar", "-czf", chemin_archive, dossier_source],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ Sauvegarde créée : {chemin_archive}")

        # Afficher la taille
        taille = os.path.getsize(chemin_archive)
        print(f"Taille : {taille / 1024:.2f} Ko")

        return chemin_archive

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la création de la sauvegarde")
        print(f"Message : {e.stderr}")
        return None

# Utilisation
creer_sauvegarde("mon_projet", "backups")
```

---

## Combinaison des trois modules : Exemple complet

Voici un exemple qui combine `os`, `sys` et `subprocess` pour créer un script utile :

```python
import os
import sys
import subprocess
from datetime import datetime

def analyser_projet():
    """Analyse un projet Python et affiche des statistiques"""

    # Vérifier les arguments
    if len(sys.argv) > 1:
        repertoire = sys.argv[1]
    else:
        repertoire = os.getcwd()

    # Vérifier que le répertoire existe
    if not os.path.isdir(repertoire):
        print(f"❌ Erreur : {repertoire} n'est pas un répertoire valide")
        sys.exit(1)

    print(f"📊 Analyse du projet : {os.path.abspath(repertoire)}")
    print("=" * 60)

    # Compter les fichiers Python
    fichiers_py = []
    total_lignes = 0

    for racine, _, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.endswith(".py"):
                chemin_complet = os.path.join(racine, fichier)
                fichiers_py.append(chemin_complet)

                # Compter les lignes
                try:
                    with open(chemin_complet, "r", encoding="utf-8") as f:
                        nb_lignes = len(f.readlines())
                        total_lignes += nb_lignes
                except Exception:
                    pass

    print(f"🐍 Fichiers Python trouvés : {len(fichiers_py)}")
    print(f"📝 Total de lignes de code : {total_lignes}")

    # Taille totale du projet
    taille_totale = 0
    for racine, _, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            chemin = os.path.join(racine, fichier)
            taille_totale += os.path.getsize(chemin)

    print(f"💾 Taille totale : {taille_totale / 1024:.2f} Ko")

    # Vérifier si Git est présent
    try:
        resultat = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=repertoire,
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Dépôt Git détecté")

        # Obtenir le dernier commit
        resultat = subprocess.run(
            ["git", "log", "-1", "--oneline"],
            cwd=repertoire,
            capture_output=True,
            text=True
        )
        if resultat.returncode == 0:
            print(f"📌 Dernier commit : {resultat.stdout.strip()}")

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ℹ️  Pas de dépôt Git")

    # Informations système
    print("\n🖥️  Environnement :")
    print(f"  Python : {sys.version.split()[0]}")
    print(f"  Plateforme : {sys.platform}")
    print(f"  Répertoire de travail : {os.getcwd()}")

    sys.exit(0)

if __name__ == "__main__":
    try:
        analyser_projet()
    except KeyboardInterrupt:
        print("\n⚠️  Analyse interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        sys.exit(1)
```

---

## Bonnes pratiques

### 1. Utiliser `pathlib` pour les chemins (Python 3.4+)

Bien que `os.path` fonctionne parfaitement, le module `pathlib` est plus moderne et plus lisible :

```python
from pathlib import Path

# Avec pathlib
chemin = Path("dossier") / "fichier.txt"

# Équivalent à
chemin = os.path.join("dossier", "fichier.txt")
```

### 2. Préférer `subprocess.run()` aux anciennes fonctions

Les fonctions `os.system()`, `os.popen()` et `subprocess.call()` sont obsolètes. Utilisez toujours `subprocess.run()`.

### 3. Gérer les erreurs

Toujours prévoir la gestion des erreurs, surtout pour les opérations sur les fichiers et les processus externes :

```python
import os

try:
    os.remove("fichier.txt")
except FileNotFoundError:
    print("Le fichier n'existe pas")
except PermissionError:
    print("Permissions insuffisantes")
except Exception as e:
    print(f"Erreur : {e}")
```

### 4. Éviter `shell=True` quand possible

Pour des raisons de sécurité, évitez `shell=True` dans `subprocess.run()` :

```python
# ❌ Moins sûr
subprocess.run("ls -l", shell=True)

# ✅ Plus sûr
subprocess.run(["ls", "-l"])
```

### 5. Utiliser des chemins absolus

Pour éviter les ambiguïtés, privilégiez les chemins absolus :

```python
chemin_absolu = os.path.abspath("fichier.txt")
```

---

## Résumé

| Module | Usage principal | Fonctions clés |
|--------|----------------|----------------|
| **os** | Interaction avec le système de fichiers | `getcwd()`, `listdir()`, `mkdir()`, `path.join()`, `path.exists()` |
| **sys** | Interaction avec l'interpréteur Python | `argv`, `exit()`, `version`, `path`, `platform` |
| **subprocess** | Exécution de commandes externes | `run()`, avec paramètres `capture_output`, `text`, `check` |

Ces trois modules sont essentiels pour créer des scripts Python qui interagissent avec le système d'exploitation. Ils vous permettent de :

- Naviguer dans le système de fichiers
- Obtenir des informations sur l'environnement d'exécution
- Exécuter des programmes externes
- Créer des scripts en ligne de commande robustes

Avec la pratique, vous découvrirez de nombreuses autres fonctionnalités utiles de ces modules !

⏭️ [datetime et time](/07-bibliotheques-standard/02-datetime-et-time.md)
