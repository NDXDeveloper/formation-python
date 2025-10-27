🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.1 Installation et configuration de l'environnement Python

## Introduction

Bienvenue dans votre première étape vers l'apprentissage de Python ! Avant de pouvoir écrire votre premier programme, vous devez installer Python sur votre ordinateur. Ce guide vous accompagnera pas à pas dans cette installation, quel que soit votre système d'exploitation.

### Qu'est-ce que Python ?

Python est un langage de programmation puissant, facile à apprendre et utilisé dans de nombreux domaines : développement web, science des données, intelligence artificielle, automatisation, et bien plus encore. Sa syntaxe claire et lisible en fait un excellent choix pour les débutants.

### Quelle version de Python choisir ?

Actuellement, il existe deux grandes versions de Python :
- **Python 2.x** : ancienne version, qui n'est plus maintenue depuis 2020
- **Python 3.x** : version moderne et activement maintenue

**Recommandation** : Installez toujours Python 3.x (la version la plus récente, actuellement Python 3.12 ou 3.13). Python 2 est obsolète et ne devrait plus être utilisé pour de nouveaux projets.

---

## Installation de Python selon votre système d'exploitation

### Windows

#### Méthode 1 : Installation depuis le site officiel (Recommandée)

1. **Télécharger Python**
   - Rendez-vous sur le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Cliquez sur le bouton "Download Python 3.x.x" (la version la plus récente)
   - Le téléchargement du fichier d'installation (.exe) commence automatiquement

2. **Lancer l'installation**
   - Double-cliquez sur le fichier téléchargé
   - **IMPORTANT** : Cochez la case "Add Python to PATH" en bas de la fenêtre d'installation
   - Cliquez sur "Install Now" pour une installation standard

3. **Pourquoi "Add Python to PATH" est important ?**
   - Cette option permet d'utiliser Python depuis n'importe quel dossier dans votre terminal
   - Sans cela, vous devrez spécifier le chemin complet vers Python à chaque fois

4. **Attendre la fin de l'installation**
   - L'installation prend quelques minutes
   - Une fois terminée, cliquez sur "Close"

#### Méthode 2 : Installation via le Microsoft Store

1. Ouvrez le Microsoft Store
2. Recherchez "Python 3.12" (ou la version la plus récente)
3. Cliquez sur "Obtenir" ou "Installer"
4. Cette méthode configure automatiquement le PATH

**Avantages** : Installation simple et mises à jour automatiques
**Inconvénients** : Moins de contrôle sur la configuration

---

### macOS

#### Vérifier si Python est déjà installé

macOS inclut souvent une version de Python, mais il s'agit généralement de Python 2.x (obsolète). Pour vérifier :

1. Ouvrez le Terminal (Applications > Utilitaires > Terminal)
2. Tapez : `python3 --version`
3. Si une version 3.x s'affiche, Python 3 est déjà installé

#### Installer ou mettre à jour Python

**Méthode 1 : Depuis le site officiel (Plus simple pour les débutants)**

1. Rendez-vous sur [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Téléchargez le fichier d'installation pour macOS (.pkg)
3. Double-cliquez sur le fichier téléchargé
4. Suivez les instructions de l'assistant d'installation
5. Entrez votre mot de passe administrateur si demandé

**Méthode 2 : Via Homebrew (Pour les utilisateurs plus avancés)**

Si vous utilisez Homebrew (un gestionnaire de paquets pour macOS) :

```bash
# Installer Homebrew si ce n'est pas déjà fait
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer Python
brew install python3
```

---

### Linux

La plupart des distributions Linux incluent Python 3 par défaut. Voici comment l'installer ou le mettre à jour selon votre distribution.

#### Ubuntu / Debian / Linux Mint

```bash
# Mettre à jour la liste des paquets
sudo apt update

# Installer Python 3 et pip (gestionnaire de paquets Python)
sudo apt install python3 python3-pip

# Installer python3-venv pour créer des environnements virtuels
sudo apt install python3-venv
```

#### Fedora / Red Hat / CentOS

```bash
# Installer Python 3
sudo dnf install python3 python3-pip

# Ou sur les versions plus anciennes avec yum
sudo yum install python3 python3-pip
```

#### Arch Linux / Manjaro

```bash
# Installer Python
sudo pacman -S python python-pip
```

---

## Vérifier l'installation de Python

Une fois l'installation terminée, il est important de vérifier que Python fonctionne correctement.

### Sur Windows

1. Ouvrez l'Invite de commandes (cmd) ou PowerShell
   - Appuyez sur `Windows + R`
   - Tapez `cmd` et appuyez sur Entrée

2. Tapez la commande suivante et appuyez sur Entrée :
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

3. Vous devriez voir s'afficher quelque chose comme :
   ```
   Python 3.12.1
   ```

### Sur macOS et Linux

1. Ouvrez le Terminal

2. Tapez la commande suivante :
   ```bash
   python3 --version
   ```

3. La version de Python installée devrait s'afficher

### Vérifier pip (gestionnaire de paquets Python)

pip est l'outil qui vous permettra d'installer des bibliothèques Python supplémentaires. Pour vérifier son installation :

```bash
pip --version
```
ou
```bash
pip3 --version
```

Vous devriez voir s'afficher la version de pip et le chemin vers Python.

---

## L'interpréteur Python interactif

Python inclut un mode interactif qui vous permet de tester rapidement du code sans créer de fichier.

### Lancer l'interpréteur

Dans votre terminal ou invite de commandes, tapez :

```bash
python
```
ou
```bash
python3
```

Vous verrez apparaître quelque chose comme :

```
Python 3.12.1 (main, Dec 18 2024, 12:00:00)
[GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Le symbole `>>>` indique que Python attend vos instructions.

### Tester votre première commande

Essayez de taper :

```python
print("Bonjour, Python !")
```

Appuyez sur Entrée. Python affichera :

```
Bonjour, Python !
```

### Quitter l'interpréteur

Pour quitter l'interpréteur Python, tapez :

```python
exit()
```
ou appuyez sur `Ctrl + D` (Linux/macOS) ou `Ctrl + Z` puis Entrée (Windows).

---

## Installation d'un éditeur de code

Bien que vous puissiez écrire du code Python dans n'importe quel éditeur de texte, un éditeur de code dédié vous facilitera grandement la vie avec des fonctionnalités comme la coloration syntaxique, l'autocomplétion et le débogage.

### Visual Studio Code (Recommandé pour les débutants)

Visual Studio Code (VS Code) est un éditeur gratuit, léger et très populaire, idéal pour Python.

#### Installation de VS Code

1. Rendez-vous sur [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Téléchargez la version correspondant à votre système d'exploitation
3. Installez le programme en suivant les instructions

#### Installation de l'extension Python pour VS Code

1. Ouvrez VS Code
2. Cliquez sur l'icône des extensions dans la barre latérale gauche (ou appuyez sur `Ctrl+Shift+X`)
3. Recherchez "Python" dans la barre de recherche
4. Installez l'extension "Python" publiée par Microsoft (la première dans les résultats)

Cette extension vous fournira :
- La coloration syntaxique
- L'autocomplétion intelligente
- Le débogage
- La détection automatique de votre installation Python
- Et bien d'autres fonctionnalités utiles

### Autres éditeurs populaires

- **PyCharm** : IDE complet et puissant, spécialisé pour Python (version Community gratuite disponible)
- **Sublime Text** : Éditeur léger et rapide
- **Atom** : Éditeur open-source et personnalisable
- **Jupyter Notebook** : Excellent pour l'apprentissage et la data science (nécessite une installation séparée)

---

## Configuration de base de l'environnement

### Créer votre premier fichier Python

1. **Créer un dossier pour vos projets Python**
   - Créez un dossier appelé `mes_projets_python` sur votre Bureau ou dans vos Documents

2. **Ouvrir le dossier dans VS Code**
   - Dans VS Code, cliquez sur "Fichier" > "Ouvrir le dossier"
   - Sélectionnez le dossier que vous venez de créer

3. **Créer un nouveau fichier**
   - Cliquez sur l'icône "Nouveau fichier" ou faites un clic droit dans l'explorateur de fichiers
   - Nommez le fichier `hello.py` (l'extension `.py` indique qu'il s'agit d'un fichier Python)

4. **Écrire votre premier programme**
   ```python
   print("Bonjour ! Ceci est mon premier programme Python.")
   print("Python est génial !")
   ```

5. **Exécuter le programme**
   - Sauvegardez le fichier (`Ctrl+S` ou `Cmd+S`)
   - Cliquez avec le bouton droit dans l'éditeur et sélectionnez "Run Python File in Terminal"
   - Ou ouvrez un terminal dans VS Code (`Ctrl+ù` ou `Cmd+ù`) et tapez :
     ```bash
     python hello.py
     ```
     ou
     ```bash
     python3 hello.py
     ```

Félicitations ! Vous venez d'exécuter votre premier programme Python !

---

## Configurer l'environnement de travail dans VS Code

### Sélectionner l'interpréteur Python

VS Code doit savoir quelle version de Python utiliser :

1. Appuyez sur `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur Mac) pour ouvrir la palette de commandes
2. Tapez "Python: Select Interpreter"
3. Sélectionnez la version de Python que vous avez installée

### Paramètres recommandés

Dans VS Code, vous pouvez configurer quelques paramètres utiles :

1. Ouvrez les paramètres : `Fichier > Préférences > Paramètres` (ou `Ctrl+,`)
2. Recherchez et configurez :
   - **"Format On Save"** : Cochez cette option pour formater automatiquement votre code à la sauvegarde
   - **"Python Linting"** : Activez le linting pour détecter les erreurs de code

---

## Installer des paquets Python avec pip

pip est le gestionnaire de paquets standard de Python. Il vous permet d'installer des milliers de bibliothèques créées par la communauté.

### Syntaxe de base

```bash
pip install nom_du_paquet
```

### Exemple : Installer la bibliothèque requests

```bash
pip install requests
```

### Lister les paquets installés

```bash
pip list
```

### Mettre à jour un paquet

```bash
pip install --upgrade nom_du_paquet
```

### Désinstaller un paquet

```bash
pip uninstall nom_du_paquet
```

**Note** : Sur certains systèmes (surtout Linux et macOS), vous devrez peut-être utiliser `pip3` au lieu de `pip`.

---

## Environnements virtuels (aperçu)

Les environnements virtuels permettent d'isoler les dépendances de vos projets Python. C'est une bonne pratique que nous explorerons en détail dans une section ultérieure (6.4).

En bref, un environnement virtuel vous permet :
- D'avoir différentes versions de bibliothèques pour différents projets
- D'éviter les conflits entre les dépendances
- De garder votre installation Python système propre

Nous reviendrons sur ce concept important plus tard dans la formation.

---

## Résolution des problèmes courants

### Python n'est pas reconnu comme commande

**Problème** : Lorsque vous tapez `python` dans le terminal, vous obtenez une erreur indiquant que la commande n'est pas reconnue.

**Solution** :
- **Windows** : Python n'a pas été ajouté au PATH lors de l'installation. Réinstallez Python en cochant bien "Add Python to PATH"
- **macOS/Linux** : Essayez d'utiliser `python3` au lieu de `python`

### Plusieurs versions de Python installées

Si vous avez plusieurs versions de Python, utilisez des commandes plus spécifiques :
- `python3.12` pour Python 3.12
- `python3.11` pour Python 3.11
- etc.

### Problèmes de permissions sur Linux/macOS

Si vous rencontrez des erreurs de permissions lors de l'installation de paquets avec pip, n'utilisez **jamais** `sudo pip` (c'est une mauvaise pratique). Utilisez plutôt :

```bash
pip install --user nom_du_paquet
```

Ou, mieux encore, utilisez un environnement virtuel (que nous verrons plus tard).

---

## Récapitulatif

Félicitations ! Vous avez maintenant :

✅ Installé Python sur votre ordinateur
✅ Vérifié que l'installation fonctionne correctement
✅ Installé un éditeur de code (VS Code)
✅ Créé et exécuté votre premier programme Python
✅ Appris les bases de pip pour installer des bibliothèques

Vous êtes maintenant prêt à commencer votre apprentissage de Python ! Dans la prochaine section, nous découvrirons les variables, les types de données et les opérateurs de base.

---

## Ressources supplémentaires

- **Documentation officielle de Python** : [https://docs.python.org/fr/3/](https://docs.python.org/fr/3/)
- **Guide d'installation officiel** : [https://docs.python.org/fr/3/using/index.html](https://docs.python.org/fr/3/using/index.html)
- **Documentation VS Code pour Python** : [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

---


⏭️ [Variables, types de données et opérateurs](/01-fondamentaux-et-syntaxe/02-variables-types-et-operateurs.md)
