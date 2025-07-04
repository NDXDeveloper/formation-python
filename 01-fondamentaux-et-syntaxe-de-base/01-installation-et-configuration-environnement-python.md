🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.1 : Installation et configuration de l'environnement Python

## Introduction

Avant de commencer à programmer en Python, il est essentiel de configurer correctement votre environnement de développement. Cette section vous guidera pas à pas pour installer Python et configurer les outils nécessaires, que vous soyez sur Windows, macOS ou Linux.

## Comprendre les versions de Python

### Python 2 vs Python 3

Python 3 est la version actuelle et recommandée. Python 2 n'est plus maintenu depuis janvier 2020. **Utilisez toujours Python 3** pour vos nouveaux projets.

### Versions de Python 3

- **Version actuelle stable** : Python 3.11 ou 3.12 (recommandé)
- **Version minimale recommandée** : Python 3.8
- **Cycle de vie** : Chaque version est maintenue pendant environ 5 ans

💡 **Astuce** : Pour ce tutoriel, nous utiliserons Python 3.8 ou supérieur.

## Installation de Python

### Sur Windows

#### Option 1 : Téléchargement depuis le site officiel (Recommandé)

1. Rendez-vous sur https://www.python.org/downloads/
2. Cliquez sur "Download Python 3.x.x" (version la plus récente)
3. Exécutez le fichier téléchargé
4. ⚠️ **Important** : Cochez "Add Python to PATH" avant de cliquer sur "Install Now"
5. Suivez les instructions d'installation

#### Option 2 : Via Microsoft Store

1. Ouvrez le Microsoft Store
2. Recherchez "Python 3.x"
3. Cliquez sur "Installer"

#### Vérification de l'installation

Ouvrez l'invite de commande (cmd) ou PowerShell et tapez :

```bash
python --version
```

ou

```bash
python3 --version
```

Vous devriez voir quelque chose comme : `Python 3.11.2`

### Sur macOS

#### Option 1 : Téléchargement depuis le site officiel

1. Rendez-vous sur https://www.python.org/downloads/
2. Téléchargez la version macOS
3. Exécutez le fichier .pkg téléchargé
4. Suivez les instructions d'installation

#### Option 2 : Via Homebrew (Recommandé pour les développeurs)

Si vous avez Homebrew installé :

```bash
brew install python3
```

Si vous n'avez pas Homebrew, installez-le d'abord :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Vérification de l'installation

Ouvrez le Terminal et tapez :

```bash
python3 --version
```

### Sur Linux (Ubuntu/Debian)

Python 3 est généralement pré-installé sur les distributions Linux modernes.

#### Vérification de l'installation existante

```bash
python3 --version
```

#### Installation si nécessaire

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Sur Red Hat/CentOS/Fedora

```bash
sudo dnf install python3 python3-pip
```

## Installation de pip (gestionnaire de paquets Python)

### Qu'est-ce que pip ?

`pip` est l'outil standard pour installer des packages Python depuis le Python Package Index (PyPI).

### Vérification de pip

```bash
pip --version
```

ou sur certains systèmes :

```bash
pip3 --version
```

### Installation de pip (si nécessaire)

#### Sur Windows et macOS
Pip est généralement installé automatiquement avec Python 3.4+.

#### Sur Linux
```bash
sudo apt install python3-pip  # Ubuntu/Debian
sudo dnf install python3-pip  # Red Hat/CentOS/Fedora
```

## Configuration de l'environnement de développement

### Choix d'un éditeur de code

#### Pour débutants (interfaces graphiques simples)

1. **Thonny** (Recommandé pour débuter)
   - Interface simple et intuitive
   - Débogueur intégré
   - Installation : https://thonny.org/

2. **IDLE**
   - Fourni avec Python
   - Lancez avec `idle` ou `idle3` dans le terminal

#### Pour développeurs expérimentés

1. **Visual Studio Code** (Recommandé)
   - Gratuit et extensible
   - Excellente extension Python
   - Installation : https://code.visualstudio.com/

2. **PyCharm**
   - IDE complet pour Python
   - Version Community gratuite
   - Installation : https://www.jetbrains.com/pycharm/

### Configuration de Visual Studio Code pour Python

1. Installez Visual Studio Code
2. Ouvrez VS Code
3. Allez dans Extensions (Ctrl+Shift+X)
4. Recherchez "Python" et installez l'extension officielle Microsoft
5. Redémarrez VS Code

### Test de votre environnement

Créez un fichier `test.py` avec le contenu suivant :

```python
# test.py
print("Hello, Python!")
print(f"Version de Python : {__import__('sys').version}")

# Test d'une opération simple
a = 5
b = 3
print(f"5 + 3 = {a + b}")
```

#### Exécution du fichier

Dans le terminal, naviguez vers le dossier contenant `test.py` et tapez :

```bash
python test.py
```

ou

```bash
python3 test.py
```

**Résultat attendu :**
```
Hello, Python!
Version de Python : 3.11.2 (main, Feb  8 2023, 11:40:44) [GCC 9.4.0] on linux
5 + 3 = 8
```

## L'interpréteur Python interactif

### Lancement de l'interpréteur

Tapez dans votre terminal :

```bash
python
```

ou

```bash
python3
```

Vous verrez quelque chose comme :

```
Python 3.11.2 (main, Feb  8 2023, 11:40:44) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Utilisation de l'interpréteur

```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
>>> x = 10
>>> x * 2
20
>>> exit()  # Pour quitter
```

💡 **Astuce** : L'interpréteur interactif est parfait pour tester rapidement des morceaux de code.

## Gestion des chemins et variables d'environnement

### Comprendre la variable PATH

La variable PATH indique au système où chercher les exécutables. Python doit être dans le PATH pour être accessible depuis n'importe quel dossier.

### Vérification du PATH

#### Windows
```cmd
echo %PATH%
```

#### macOS/Linux
```bash
echo $PATH
```

### Ajout manuel de Python au PATH (si nécessaire)

#### Windows
1. Ouvrez "Paramètres système avancés"
2. Cliquez sur "Variables d'environnement"
3. Sélectionnez "PATH" et cliquez sur "Modifier"
4. Ajoutez le chemin vers votre installation Python (ex: `C:\Python311\`)

#### macOS/Linux
Ajoutez cette ligne à votre fichier `~/.bashrc` ou `~/.zshrc` :

```bash
export PATH="/usr/local/bin/python3:$PATH"
```

## Premiers pas avec Python

### Votre premier programme

Créez un fichier `hello.py` :

```python
# hello.py - Mon premier programme Python

# Affichage d'un message
print("Bonjour, bienvenue dans Python!")

# Demander le nom de l'utilisateur
nom = input("Quel est votre nom ? ")

# Afficher un message personnalisé
print(f"Enchanté, {nom}!")

# Quelques calculs simples
age = int(input("Quel est votre âge ? "))
print(f"Dans 10 ans, vous aurez {age + 10} ans.")
```

### Exécution du programme

```bash
python hello.py
```

**Exemple d'exécution :**
```
Bonjour, bienvenue dans Python!
Quel est votre nom ? Alice
Enchanté, Alice!
Quel est votre âge ? 25
Dans 10 ans, vous aurez 35 ans.
```

## Résolution des problèmes courants

### Python n'est pas reconnu comme commande

**Problème** : Message d'erreur "python n'est pas reconnu comme une commande interne..."

**Solutions** :
1. Vérifiez que Python est dans le PATH
2. Essayez `python3` au lieu de `python`
3. Réinstallez Python en cochant "Add to PATH"

### Problème de permissions (Linux/macOS)

**Problème** : Erreur de permissions lors de l'installation de packages

**Solution** :
```bash
python3 -m pip install --user nom_du_package
```

### Versions multiples de Python

**Problème** : Plusieurs versions de Python installées

**Solution** :
- Utilisez `python3` pour Python 3
- Utilisez `python3.11` pour une version spécifique
- Configurez des alias dans votre shell

## Bonnes pratiques

### Organisation des projets

Créez un dossier pour vos projets Python :

```
mes_projets_python/
├── projet1/
│   ├── main.py
│   └── README.md
├── projet2/
│   ├── app.py
│   └── utils.py
└── tutoriel/
    ├── exercices/
    └── exemples/
```

### Conseils pour débuter

1. **Utilisez des noms explicites** pour vos fichiers et variables
2. **Commentez votre code** pour expliquer ce que vous faites
3. **Testez fréquemment** vos petits morceaux de code
4. **Sauvegardez régulièrement** votre travail

## Exercices pratiques

### Exercice 1 : Vérification de l'installation

Créez un script `verification.py` qui affiche :
- La version de Python
- Le chemin d'installation de Python
- La version de pip

```python
# verification.py
import sys
import platform

print(f"Version Python : {sys.version}")
print(f"Version courte : {platform.python_version()}")
print(f"Chemin exécutable : {sys.executable}")
```

### Exercice 2 : Calculatrice simple

Créez un script `calculatrice.py` qui demande deux nombres à l'utilisateur et affiche leur somme, différence, produit et quotient.

### Exercice 3 : Test de l'interpréteur

Utilisez l'interpréteur interactif pour :
1. Calculer 123 * 456
2. Créer une variable avec votre nom
3. Afficher "Bonjour" + votre nom
4. Importer le module `math` et utiliser `math.pi`

## Récapitulatif

À la fin de cette section, vous devriez avoir :

✅ Python 3 installé et fonctionnel
✅ pip installé et accessible
✅ Un éditeur de code configuré
✅ Capacité à exécuter des scripts Python
✅ Compréhension de l'interpréteur interactif
✅ Connaissance des commandes de base

**Prochaine étape** : Maintenant que votre environnement est prêt, nous allons explorer les variables, types de données et opérateurs dans la section 1.2.

---

💡 **Conseil** : Gardez cette section comme référence. Il est normal de revenir aux bases lors de l'apprentissage d'un nouveau langage !

⏭️
