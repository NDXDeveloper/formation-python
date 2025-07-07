🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.2 : Gestion de version avec Git

## Introduction

Imaginez que vous écrivez un roman. Vous créez plusieurs versions de votre histoire, mais après des semaines de travail, vous vous rendez compte que votre première version était meilleure. Sans système de sauvegarde, vous avez perdu votre travail !

C'est exactement ce qui arrive avec le code informatique. Git est comme un système de sauvegarde très intelligent qui :

- **Garde l'historique** de tous vos changements
- **Permet de revenir** en arrière si nécessaire
- **Facilite la collaboration** entre développeurs
- **Évite les conflits** quand plusieurs personnes travaillent ensemble

## Qu'est-ce que Git ?

### Git vs autres systèmes de sauvegarde

**Méthode traditionnelle (sans Git) :**
```
mon_projet/
├── main.py
├── main_v2.py
├── main_final.py
├── main_final_vraiment.py
├── main_final_cette_fois.py
└── main_ne_plus_toucher.py
```

**Avec Git :**
```
mon_projet/
├── main.py          # Une seule version visible
└── .git/            # Historique complet caché
    ├── version 1: "Première version"
    ├── version 2: "Ajout de la validation"
    ├── version 3: "Correction du bug"
    └── version 4: "Optimisation"
```

### Les avantages de Git

1. **Historique complet** : Chaque changement est sauvegardé avec un message explicatif
2. **Branches** : Possibilité de travailler sur plusieurs fonctionnalités en parallèle
3. **Collaboration** : Plusieurs développeurs peuvent travailler sur le même projet
4. **Sauvegarde distribuée** : Chaque développeur a une copie complète du projet

## Installation et configuration

### Installation de Git

**Windows :**
1. Téléchargez Git depuis [git-scm.com](https://git-scm.com/)
2. Lancez l'installateur
3. Gardez les options par défaut

**macOS :**
```bash
# Avec Homebrew
brew install git

# Ou téléchargez depuis git-scm.com
```

**Linux (Ubuntu/Debian) :**
```bash
sudo apt update
sudo apt install git
```

### Configuration initiale

Après l'installation, configurez Git avec vos informations :

```bash
# Votre nom (apparaîtra dans l'historique)
git config --global user.name "Votre Nom"

# Votre email
git config --global user.email "votre.email@example.com"

# Vérifier la configuration
git config --list
```

## Concepts fondamentaux

### Le dépôt (Repository)

Un **dépôt** est un dossier qui contient votre projet et son historique Git.

```
mon_projet/
├── src/              # Votre code
├── tests/            # Vos tests
├── README.md         # Documentation
└── .git/             # Historique Git (caché)
```

### Les trois zones de Git

Git organise votre travail en trois zones :

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Working Tree   │    │  Staging Area   │    │   Repository    │
│  (Répertoire    │    │   (Index)       │    │   (Historique)  │
│   de travail)   │    │                 │    │                 │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ main.py ✏️      │    │ main.py ✅      │    │ Commit 1        │
│ config.py ✏️    │    │                 │    │ Commit 2        │
│ tests.py        │    │                 │    │ Commit 3        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │                       │
        └── git add ──────────→ │                       │
                                └── git commit ────────→ │
```

1. **Working Tree** : Vos fichiers en cours de modification
2. **Staging Area** : Fichiers prêts à être sauvegardés
3. **Repository** : Historique des sauvegardes (commits)

### Le commit

Un **commit** est comme une photo instantanée de votre projet à un moment donné.

```
Commit 1: "Ajout de la fonction de calcul"
├── main.py (version 1)
├── utils.py (version 1)
└── README.md (version 1)

Commit 2: "Correction du bug dans le calcul"
├── main.py (version 2) ← Modifié
├── utils.py (version 1)
└── README.md (version 1)
```

## Commandes de base

### Initialiser un projet Git

```bash
# Créer un nouveau dossier
mkdir mon_projet
cd mon_projet

# Initialiser Git
git init

# Vérifier le statut
git status
```

**Résultat :**
```
Initialized empty Git repository in /Users/nom/mon_projet/.git/
```

### Votre premier commit

Créons un projet simple :

```bash
# Créer un fichier
echo "print('Hello, Git!')" > main.py

# Vérifier le statut
git status
```

**Résultat :**
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    main.py

nothing added to commit but untracked files present
```

```bash
# Ajouter le fichier à la staging area
git add main.py

# Vérifier le statut
git status
```

**Résultat :**
```
On branch main
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   main.py
```

```bash
# Créer le commit
git commit -m "Ajout du fichier principal"

# Vérifier l'historique
git log
```

**Résultat :**
```
commit a1b2c3d4... (HEAD -> main)
Author: Votre Nom <votre.email@example.com>
Date:   Mon Jan 15 10:30:00 2024 +0100

    Ajout du fichier principal
```

### Workflow typique

Voici le cycle de travail habituel avec Git :

```bash
# 1. Modifier des fichiers
echo "print('Bonjour le monde!')" > main.py
echo "# Mon Projet" > README.md

# 2. Vérifier les changements
git status
git diff

# 3. Ajouter les fichiers modifiés
git add main.py README.md
# Ou ajouter tous les fichiers modifiés
git add .

# 4. Créer un commit
git commit -m "Amélioration du message et ajout du README"

# 5. Voir l'historique
git log --oneline
```

## Gestion des fichiers

### Ignorer des fichiers avec .gitignore

Certains fichiers ne doivent pas être versionnés :

```bash
# Créer le fichier .gitignore
touch .gitignore
```

**Contenu du .gitignore pour Python :**
```
# Fichiers Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Environnements virtuels
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Système
.DS_Store
Thumbs.db

# Logs
*.log

# Données sensibles
config.ini
secrets.txt
```

### Exemples pratiques

```bash
# Créer des fichiers de test
mkdir __pycache__
touch __pycache__/main.cpython-39.pyc
touch config.ini
echo "password=123456" > config.ini

# Vérifier le statut
git status
```

Sans .gitignore, Git voit tous les fichiers :
```
Untracked files:
    __pycache__/
    config.ini
```

Avec .gitignore, ces fichiers sont ignorés :
```bash
# Ajouter .gitignore
git add .gitignore
git commit -m "Ajout du fichier .gitignore"

# Vérifier le statut
git status
```

## Branches : travailler en parallèle

### Comprendre les branches

Une **branche** est comme une ligne de développement parallèle :

```
main:     A---B---C---D
               \
feature:        E---F
```

- **main** : branche principale (stable)
- **feature** : branche de développement (expérimentation)

### Créer et utiliser des branches

```bash
# Voir les branches existantes
git branch

# Créer une nouvelle branche
git branch nouvelle-fonctionnalite

# Changer de branche
git checkout nouvelle-fonctionnalite

# Ou créer et changer en une commande
git checkout -b autre-fonctionnalite

# Voir sur quelle branche vous êtes
git branch
```

### Exemple pratique : Développer une calculatrice

Créons une calculatrice avec des branches pour chaque fonctionnalité :

```bash
# Branche principale
git checkout main
echo "# Calculatrice" > README.md
echo "def main(): pass" > calculatrice.py
git add .
git commit -m "Structure de base"

# Branche pour l'addition
git checkout -b feature/addition
```

**calculatrice.py** (sur la branche addition) :
```python
def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def main():
    print("Calculatrice - Addition")
    a = float(input("Premier nombre: "))
    b = float(input("Deuxième nombre: "))
    resultat = addition(a, b)
    print(f"Résultat: {resultat}")

if __name__ == "__main__":
    main()
```

```bash
# Sauvegarder les changements
git add calculatrice.py
git commit -m "Ajout de la fonction d'addition"

# Retourner sur main
git checkout main
```

Remarquez que sur la branche `main`, votre fichier `calculatrice.py` est revenu à sa version originale !

### Fusionner des branches

```bash
# Se positionner sur la branche de destination
git checkout main

# Fusionner la branche feature/addition
git merge feature/addition

# Vérifier l'historique
git log --oneline --graph
```

**Résultat :**
```
*   a1b2c3d Merge branch 'feature/addition'
|\
| * e4f5g6h Ajout de la fonction d'addition
|/
* h7i8j9k Structure de base
```

### Supprimer une branche

```bash
# Supprimer une branche fusionnée
git branch -d feature/addition

# Forcer la suppression d'une branche non fusionnée
git branch -D feature/suppression
```

## Collaborer avec Git

### Dépôts distants

Un **dépôt distant** est une copie de votre projet hébergée sur un serveur (GitHub, GitLab, etc.).

```
Votre ordinateur          Serveur (GitHub)
┌─────────────────┐      ┌─────────────────┐
│  Dépôt local    │      │  Dépôt distant  │
│  mon_projet/    │ ←──→ │  mon_projet/    │
│  ├── main.py    │      │  ├── main.py    │
│  └── .git/      │      │  └── .git/      │
└─────────────────┘      └─────────────────┘
```

### Cloner un projet existant

```bash
# Télécharger un projet depuis GitHub
git clone https://github.com/utilisateur/nom-du-projet.git

# Ou depuis GitLab
git clone https://gitlab.com/utilisateur/nom-du-projet.git

# Entrer dans le dossier
cd nom-du-projet

# Vérifier les dépôts distants
git remote -v
```

### Pousser vos changements

```bash
# Envoyer vos commits vers le serveur
git push origin main

# Si c'est votre premier push
git push -u origin main
```

### Récupérer les changements

```bash
# Télécharger les nouveaux commits
git fetch origin

# Fusionner les changements
git merge origin/main

# Ou faire les deux en une commande
git pull origin main
```

## Exemple complet : Projet collaboratif

Simulons un projet collaboratif sur une calculatrice :

### 1. Initialisation du projet

```bash
# Créer le projet
mkdir calculatrice-collaborative
cd calculatrice-collaborative
git init

# Structure initiale
mkdir src tests
touch src/__init__.py
touch tests/__init__.py
echo "# Calculatrice Collaborative" > README.md
```

**src/calculatrice.py** :
```python
"""Calculatrice collaborative."""

class Calculatrice:
    """Calculatrice simple."""

    def __init__(self):
        self.historique = []

    def ajouter_historique(self, operation, resultat):
        """Ajoute une opération à l'historique."""
        self.historique.append(f"{operation} = {resultat}")

    def afficher_historique(self):
        """Affiche l'historique des opérations."""
        if not self.historique:
            print("Aucune opération dans l'historique")
            return

        print("Historique des opérations:")
        for operation in self.historique:
            print(f"  {operation}")
```

```bash
# Premier commit
git add .
git commit -m "Structure initiale du projet"
```

### 2. Développement de fonctionnalités par branches

**Branche addition :**
```bash
git checkout -b feature/addition
```

**Modification de src/calculatrice.py** :
```python
def addition(self, a, b):
    """Additionne deux nombres."""
    resultat = a + b
    self.ajouter_historique(f"{a} + {b}", resultat)
    return resultat
```

```bash
git add src/calculatrice.py
git commit -m "Ajout de la fonction addition"
```

**Branche soustraction :**
```bash
git checkout main
git checkout -b feature/soustraction
```

**Modification de src/calculatrice.py** :
```python
def soustraction(self, a, b):
    """Soustrait deux nombres."""
    resultat = a - b
    self.ajouter_historique(f"{a} - {b}", resultat)
    return resultat
```

```bash
git add src/calculatrice.py
git commit -m "Ajout de la fonction soustraction"
```

### 3. Fusion des branches

```bash
# Fusionner addition
git checkout main
git merge feature/addition

# Fusionner soustraction
git merge feature/soustraction
```

**Résolution de conflit** (si nécessaire) :
```python
"""Calculatrice collaborative."""

class Calculatrice:
    """Calculatrice simple."""

    def __init__(self):
        self.historique = []

    def ajouter_historique(self, operation, resultat):
        """Ajoute une opération à l'historique."""
        self.historique.append(f"{operation} = {resultat}")

    def addition(self, a, b):
        """Additionne deux nombres."""
        resultat = a + b
        self.ajouter_historique(f"{a} + {b}", resultat)
        return resultat

    def soustraction(self, a, b):
        """Soustrait deux nombres."""
        resultat = a - b
        self.ajouter_historique(f"{a} - {b}", resultat)
        return resultat

    def afficher_historique(self):
        """Affiche l'historique des opérations."""
        if not self.historique:
            print("Aucune opération dans l'historique")
            return

        print("Historique des opérations:")
        for operation in self.historique:
            print(f"  {operation}")
```

### 4. Tests

**tests/test_calculatrice.py** :
```python
"""Tests pour la calculatrice."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculatrice import Calculatrice

def test_addition():
    """Test de la fonction addition."""
    calc = Calculatrice()
    resultat = calc.addition(5, 3)
    assert resultat == 8
    print("✅ Test addition réussi")

def test_soustraction():
    """Test de la fonction soustraction."""
    calc = Calculatrice()
    resultat = calc.soustraction(5, 3)
    assert resultat == 2
    print("✅ Test soustraction réussi")

def test_historique():
    """Test de l'historique."""
    calc = Calculatrice()
    calc.addition(5, 3)
    calc.soustraction(10, 4)

    assert len(calc.historique) == 2
    assert "5 + 3 = 8" in calc.historique
    assert "10 - 4 = 6" in calc.historique
    print("✅ Test historique réussi")

if __name__ == "__main__":
    test_addition()
    test_soustraction()
    test_historique()
    print("🎉 Tous les tests sont réussis!")
```

```bash
# Commit des tests
git add tests/
git commit -m "Ajout des tests unitaires"

# Nettoyer les branches
git branch -d feature/addition
git branch -d feature/soustraction
```

## Bonnes pratiques

### 1. Messages de commit clairs

```bash
# ✅ Bon
git commit -m "Ajout de la validation des emails"
git commit -m "Correction du bug de calcul des taxes"
git commit -m "Refactorisation du module d'authentification"

# ❌ Mauvais
git commit -m "fix"
git commit -m "ça marche"
git commit -m "update"
```

### 2. Commits atomiques

Un commit = un changement logique :

```bash
# ✅ Bon : Séparer les changements
git add src/models/user.py
git commit -m "Ajout du modèle User"

git add src/services/auth.py
git commit -m "Ajout du service d'authentification"

# ❌ Mauvais : Tout mélanger
git add .
git commit -m "Ajout user et auth et fix bug"
```

### 3. Utiliser des branches descriptives

```bash
# ✅ Bon
git checkout -b feature/login-oauth
git checkout -b bugfix/calculation-overflow
git checkout -b hotfix/security-patch

# ❌ Mauvais
git checkout -b test
git checkout -b branch1
git checkout -b temp
```

### 4. Workflow Git Flow

```
main          A---B---C---D---E
               \         /
develop         F---G---H
                 \     /
feature/login     I---J
```

- **main** : Version stable en production
- **develop** : Intégration des nouvelles fonctionnalités
- **feature/** : Développement de nouvelles fonctionnalités

## Commandes utiles

### Voir l'historique

```bash
# Historique simple
git log --oneline

# Historique avec graphique
git log --oneline --graph --all

# Historique détaillé
git log --stat

# Historique d'un fichier
git log --follow src/calculatrice.py
```

### Annuler des changements

```bash
# Annuler les modifications non commitées
git checkout -- fichier.py

# Annuler l'ajout à la staging area
git reset HEAD fichier.py

# Annuler le dernier commit (garder les changements)
git reset --soft HEAD~1

# Annuler le dernier commit (supprimer les changements)
git reset --hard HEAD~1
```

### Voir les différences

```bash
# Différences non commitées
git diff

# Différences dans la staging area
git diff --staged

# Différences entre deux commits
git diff commit1 commit2

# Différences entre deux branches
git diff main feature/nouvelle-fonctionnalite
```

## Résolution de conflits

Les conflits surviennent quand deux personnes modifient la même ligne de code :

```bash
# Simulation d'un conflit
git checkout main
echo "version main" > conflit.txt
git add conflit.txt
git commit -m "Version main"

git checkout -b feature/conflit
echo "version feature" > conflit.txt
git add conflit.txt
git commit -m "Version feature"

git checkout main
git merge feature/conflit
```

**Résultat :**
```
Auto-merging conflit.txt
CONFLICT (content): Merge conflict in conflit.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Contenu du fichier conflit.txt :**
```
<<<<<<< HEAD
version main
=======
version feature
>>>>>>> feature/conflit
```

**Résolution :**
```
# Éditer le fichier pour résoudre le conflit
version main et feature combinées
```

```bash
# Terminer la résolution
git add conflit.txt
git commit -m "Résolution du conflit"
```

## Outils graphiques

### Interfaces graphiques populaires

1. **GitHub Desktop** : Interface simple et intuitive
2. **SourceTree** : Outil gratuit d'Atlassian
3. **GitKraken** : Interface moderne et colorée
4. **VS Code** : Extension Git intégrée

### Utilisation dans VS Code

VS Code offre une excellente intégration Git :

- **Panneau Source Control** : Voir les changements
- **Diff intégré** : Comparer les versions
- **Commits graphiques** : Interface simple
- **Résolution de conflits** : Aide visuelle

## Exercices pratiques

### Exercice 1 : Premier projet

1. Créez un nouveau projet Python
2. Initialisez Git
3. Créez plusieurs fichiers
4. Faites plusieurs commits
5. Créez une branche pour une nouvelle fonctionnalité
6. Fusionnez la branche

### Exercice 2 : Simulation collaborative

1. Clonez un projet existant
2. Créez une branche pour votre contribution
3. Ajoutez une fonctionnalité
4. Créez une pull request (sur GitHub)

### Exercice 3 : Gestion des conflits

1. Créez deux branches qui modifient le même fichier
2. Fusionnez et résolvez les conflits
3. Vérifiez que tout fonctionne

## Résumé

Git est un outil essentiel pour :

- **Sauvegarder** l'historique de votre code
- **Collaborer** efficacement en équipe
- **Expérimenter** sans risque avec les branches
- **Revenir** en arrière si nécessaire

Les commandes essentielles à retenir :
- `git init` : Initialiser un dépôt
- `git add` : Ajouter des fichiers
- `git commit` : Sauvegarder les changements
- `git branch` : Gérer les branches
- `git merge` : Fusionner les branches
- `git push/pull` : Synchroniser avec un serveur

La maîtrise de Git est indispensable pour tout développeur professionnel. C'est un investissement qui vous fera gagner énormément de temps et vous évitera bien des problèmes !

La prochaine étape sera d'explorer les patterns de conception les plus utiles en Python.

⏭️
