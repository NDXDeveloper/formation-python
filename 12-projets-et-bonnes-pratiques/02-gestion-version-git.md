🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.2 Gestion de version avec Git

## Introduction

Imaginez que vous travaillez sur un projet Python. Vous faites des modifications, puis vous vous rendez compte que votre code ne fonctionne plus. Vous aimeriez revenir en arrière, mais vous avez déjà sauvegardé par-dessus l'ancienne version... 😰

Ou encore : vous travaillez en équipe sur le même projet. Comment faire pour que chacun puisse travailler sans écraser le travail des autres ?

**Git** est la solution à tous ces problèmes ! C'est un système de gestion de version qui enregistre l'historique complet de votre projet et permet à plusieurs personnes de collaborer efficacement.

---

## Qu'est-ce que Git ?

Git est un **système de contrôle de version distribué** créé par Linus Torvalds (le créateur de Linux) en 2005. En termes simples, c'est comme une machine à voyager dans le temps pour votre code !

### Pourquoi utiliser Git ?

✅ **Historique complet** : vous pouvez voir toutes les modifications effectuées et revenir à n'importe quelle version

✅ **Collaboration** : plusieurs personnes peuvent travailler simultanément sur le même projet

✅ **Sécurité** : votre code est sauvegardé, même si votre ordinateur plante

✅ **Branches** : testez de nouvelles fonctionnalités sans risquer de casser le code principal

✅ **Standard de l'industrie** : utilisé par des millions de développeurs dans le monde

---

## Concepts de base

Avant de commencer à utiliser Git, comprenons quelques concepts essentiels :

### Repository (dépôt)

Un **repository** (ou "repo") est le dossier contenant votre projet et tout son historique Git. C'est comme une base de données de toutes les versions de votre projet.

Il existe deux types de repositories :
- **Local** : sur votre ordinateur
- **Distant** (remote) : sur un serveur (GitHub, GitLab, etc.)

### Commit

Un **commit** est un instantané (snapshot) de votre projet à un moment donné. C'est comme prendre une photo de tous vos fichiers à un instant T.

Chaque commit contient :
- Les modifications apportées
- Un message décrivant ces modifications
- L'auteur et la date
- Un identifiant unique (hash)

### Working Directory, Staging Area et Repository

Git fonctionne avec trois zones :

```
Working Directory    →    Staging Area    →    Repository
(Votre dossier)          (Zone de transit)     (Historique)

   fichier.py         →    git add         →    git commit
   (modifié)                (préparé)           (enregistré)
```

**Analogie** : imaginez que vous préparez un colis :
- **Working Directory** : vous mettez des objets de côté
- **Staging Area** : vous décidez ce qui va dans le colis
- **Repository** : vous fermez et envoyez le colis

### Branch (branche)

Une **branch** est une ligne de développement indépendante. C'est comme créer une copie parallèle de votre projet pour tester quelque chose sans toucher au code principal.

```
main    : A --- B --- C --- D --- E
                \
feature :        F --- G --- H
```

La branche principale s'appelle traditionnellement `main` (ou `master` dans les anciens projets).

---

## Installation de Git

### Vérifier si Git est installé

Ouvrez un terminal et tapez :

```bash
git --version
```

Si Git est installé, vous verrez la version (ex : `git version 2.42.0`).

### Installation

**Linux (Ubuntu/Debian) :**
```bash
sudo apt update
sudo apt install git
```

**macOS :**
```bash
# Avec Homebrew
brew install git

# Ou télécharger depuis git-scm.com
```

**Windows :**
- Téléchargez Git depuis [git-scm.com](https://git-scm.com/download/win)
- Installez avec les options par défaut
- Utilisez Git Bash (inclus) comme terminal

---

## Configuration initiale

Après l'installation, configurez votre identité. Ces informations apparaîtront dans tous vos commits :

```bash
# Configurer votre nom
git config --global user.name "Votre Nom"

# Configurer votre email
git config --global user.email "votre.email@example.com"

# Définir l'éditeur par défaut (optionnel)
git config --global core.editor "code --wait"  # Pour VS Code
# ou
git config --global core.editor "nano"  # Pour nano (Linux)

# Voir toute la configuration
git config --list
```

**Note** : l'option `--global` applique la configuration à tous vos projets. Sans cette option, la configuration s'applique uniquement au projet courant.

### Configuration recommandée supplémentaire

```bash
# Définir la branche par défaut comme 'main' (au lieu de 'master')
git config --global init.defaultBranch main

# Activer la coloration dans le terminal
git config --global color.ui auto

# Définir le comportement de 'git pull'
git config --global pull.rebase false
```

---

## Créer votre premier repository

### Méthode 1 : Initialiser un nouveau projet

```bash
# Créer un dossier pour votre projet
mkdir mon_projet
cd mon_projet

# Initialiser Git
git init
```

Cela crée un dossier caché `.git` qui contient tout l'historique de votre projet.

### Méthode 2 : Cloner un projet existant

```bash
# Cloner un repository depuis GitHub
git clone https://github.com/utilisateur/projet.git

# Cela crée un dossier 'projet' avec tout l'historique
cd projet
```

---

## Les commandes Git essentielles

### Vérifier l'état du repository

```bash
git status
```

Cette commande est votre meilleure amie ! Elle affiche :
- Les fichiers modifiés
- Les fichiers en staging
- La branche courante
- L'état par rapport au repository distant

**Exemple de sortie :**
```
On branch main
Changes not staged for commit:
  modified:   README.md

Untracked files:
  nouveau_fichier.py
```

### Ajouter des fichiers au staging

```bash
# Ajouter un fichier spécifique
git add fichier.py

# Ajouter plusieurs fichiers
git add fichier1.py fichier2.py

# Ajouter tous les fichiers Python
git add *.py

# Ajouter tous les fichiers modifiés
git add .

# Ajouter un dossier entier
git add mon_dossier/
```

### Créer un commit

```bash
# Commit avec message court
git commit -m "Ajout de la fonction de calcul"

# Commit avec message détaillé (ouvre l'éditeur)
git commit

# Ajouter ET commiter en une seule commande (fichiers déjà trackés)
git commit -am "Correction du bug dans la fonction"
```

### Voir l'historique des commits

```bash
# Historique complet
git log

# Historique condensé (une ligne par commit)
git log --oneline

# Historique avec graphique des branches
git log --oneline --graph --all

# Historique des 5 derniers commits
git log -5

# Historique d'un fichier spécifique
git log fichier.py
```

**Exemple de sortie :**
```
* a1b2c3d (HEAD -> main) Ajout de la documentation
* e4f5g6h Correction du bug dans la fonction calcul
* i7j8k9l Création de la fonction de base
```

### Voir les différences

```bash
# Différences non stagées (working directory vs staging)
git diff

# Différences stagées (staging vs dernier commit)
git diff --staged

# Différences d'un fichier spécifique
git diff fichier.py

# Différences entre deux commits
git diff a1b2c3d e4f5g6h
```

---

## Workflow Git de base

Voici le cycle typique de travail avec Git :

### 1. Vérifier l'état

```bash
git status
```

### 2. Modifier vos fichiers

Travaillez normalement dans votre éditeur de code.

### 3. Voir ce qui a changé

```bash
git diff
```

### 4. Ajouter les modifications au staging

```bash
git add fichier1.py fichier2.py
# ou
git add .
```

### 5. Créer un commit

```bash
git commit -m "Description claire des modifications"
```

### 6. Répéter !

Ce cycle se répète à chaque fois que vous faites des modifications significatives.

### Exemple concret

```bash
# Vous créez un nouveau fichier
touch calculatrice.py

# Vous vérifiez l'état
git status
# Output: Untracked files: calculatrice.py

# Vous ajoutez le fichier
git add calculatrice.py

# Vous vérifiez à nouveau
git status
# Output: Changes to be committed: new file: calculatrice.py

# Vous créez un commit
git commit -m "Ajout du fichier calculatrice"

# Vous modifiez le fichier
echo "def add(a, b): return a + b" > calculatrice.py

# Vous vérifiez les changements
git diff calculatrice.py

# Vous ajoutez et commitez
git add calculatrice.py
git commit -m "Ajout de la fonction addition"
```

---

## Travailler avec les branches

Les branches sont l'une des fonctionnalités les plus puissantes de Git !

### Pourquoi utiliser des branches ?

- Tester de nouvelles fonctionnalités sans risquer de casser le code principal
- Travailler sur plusieurs fonctionnalités en parallèle
- Isoler les corrections de bugs
- Collaborer plus facilement

### Commandes de base pour les branches

```bash
# Voir toutes les branches
git branch

# Créer une nouvelle branche
git branch ma-nouvelle-fonctionnalite

# Changer de branche
git checkout ma-nouvelle-fonctionnalite

# Créer ET changer de branche en une commande
git checkout -b ma-nouvelle-fonctionnalite

# Version moderne (Git 2.23+)
git switch ma-nouvelle-fonctionnalite
git switch -c ma-nouvelle-fonctionnalite  # créer et changer
```

### Fusionner des branches (merge)

```bash
# 1. Retourner sur la branche principale
git checkout main

# 2. Fusionner la branche feature
git merge ma-nouvelle-fonctionnalite

# 3. Supprimer la branche fusionnée (optionnel)
git branch -d ma-nouvelle-fonctionnalite
```

### Exemple de workflow avec branches

```bash
# Vous êtes sur main
git checkout main

# Créer une branche pour une nouvelle fonctionnalité
git checkout -b feature/ajouter-export-pdf

# Travailler sur la fonctionnalité
echo "def export_pdf(): pass" > export.py
git add export.py
git commit -m "Ajout de la fonction export PDF"

# Faire plusieurs commits si nécessaire
echo "# Amélioration" >> export.py
git commit -am "Amélioration de export_pdf"

# Retourner sur main
git checkout main

# Fusionner la fonctionnalité
git merge feature/ajouter-export-pdf

# Supprimer la branche
git branch -d feature/ajouter-export-pdf
```

### Visualisation des branches

```
Avant fusion :
main        : A --- B --- C
                       \
feature     :           D --- E

Après fusion :
main        : A --- B --- C ------- F
                       \           /
feature     :           D --- E
```

---

## Travailler avec un repository distant (GitHub/GitLab)

### Concepts clés

- **origin** : nom conventionnel du repository distant principal
- **push** : envoyer vos commits locaux vers le distant
- **pull** : récupérer les commits distants vers votre local
- **clone** : copier un repository distant en local

### Lier un repository local à GitHub/GitLab

#### Étape 1 : Créer un repository sur GitHub

1. Allez sur [github.com](https://github.com)
2. Cliquez sur "New repository"
3. Donnez un nom à votre projet
4. Ne cochez pas "Initialize with README" si vous avez déjà un projet local
5. Cliquez sur "Create repository"

#### Étape 2 : Lier votre repository local

```bash
# Ajouter le repository distant
git remote add origin https://github.com/votre-nom/votre-projet.git

# Vérifier les remotes
git remote -v

# Pousser votre code vers GitHub
git push -u origin main
```

**Note** : `-u` (ou `--set-upstream`) crée une liaison entre votre branche locale et la branche distante. Vous n'aurez à le faire qu'une seule fois.

### Commandes pour synchroniser avec le distant

```bash
# Envoyer vos commits locaux
git push

# Récupérer et fusionner les commits distants
git pull

# Récupérer sans fusionner (pour voir ce qui a changé)
git fetch

# Pousser une nouvelle branche
git push -u origin ma-nouvelle-branche

# Voir les branches distantes
git branch -r

# Voir toutes les branches (locales et distantes)
git branch -a
```

### Workflow typique avec un distant

```bash
# Matin : récupérer les dernières modifications
git pull

# Travailler sur votre code
# ... modifications ...
git add .
git commit -m "Ajout de la nouvelle fonctionnalité"

# Pousser vos modifications
git push

# Si quelqu'un a poussé avant vous
git pull  # Récupérer d'abord
git push  # Puis pousser
```

---

## Le fichier .gitignore

Le fichier `.gitignore` indique à Git quels fichiers **ne pas** suivre. C'est essentiel pour éviter de commiter des fichiers inutiles ou sensibles.

### Créer un .gitignore

Créez un fichier `.gitignore` à la racine de votre projet :

```bash
touch .gitignore
```

### Exemples de contenu pour un projet Python

```gitignore
# Fichiers Python compilés
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environnements virtuels
venv/
env/
ENV/
.venv

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Jupyter Notebook
.ipynb_checkpoints

# Tests
.pytest_cache/
.coverage
htmlcov/
.tox/

# Variables d'environnement
.env
.env.local

# Base de données
*.db
*.sqlite3

# Logs
*.log

# Fichiers système
.DS_Store
Thumbs.db

# Données sensibles
secrets.py
config.local.py
```

### Ignorer un fichier déjà tracké

Si vous avez déjà commité un fichier que vous voulez maintenant ignorer :

```bash
# Supprimer du tracking (mais garder le fichier localement)
git rm --cached fichier_a_ignorer.py

# Ajouter à .gitignore
echo "fichier_a_ignorer.py" >> .gitignore

# Commiter
git commit -m "Ajout de fichier_a_ignorer.py au .gitignore"
```

### Templates .gitignore

GitHub fournit des templates pour différents langages :
- [github.com/github/gitignore](https://github.com/github/gitignore)

Vous pouvez aussi utiliser [gitignore.io](https://www.toptal.com/developers/gitignore) pour générer un .gitignore personnalisé.

---

## Messages de commit efficaces

Un bon message de commit est essentiel pour maintenir un historique clair.

### Anatomie d'un bon message de commit

```
<type>(<scope>): <sujet>
<ligne vide>
<corps (optionnel)>
<ligne vide>
<footer (optionnel)>
```

### Types de commits courants

- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: modification de documentation
- `style`: formatage, point-virgules manquants, etc. (pas de changement de code)
- `refactor`: refactorisation du code (ni feat ni fix)
- `test`: ajout ou modification de tests
- `chore`: modifications build, dépendances, etc.

### Exemples de bons messages

```bash
# Simple et clair
git commit -m "fix: correction du calcul de la TVA"

# Avec contexte
git commit -m "feat(api): ajout de l'endpoint /users"

# Message détaillé
git commit -m "refactor: amélioration de la performance de la fonction search

- Utilisation d'un index pour accélérer la recherche
- Réduction de la complexité de O(n²) à O(n log n)
- Ajout de tests de performance"
```

### Mauvais exemples à éviter

```bash
# Trop vague
git commit -m "fix bug"
git commit -m "modifications"
git commit -m "update"

# Trop long sur une ligne
git commit -m "j'ai corrigé le bug qui faisait planter l'application quand on cliquait sur le bouton de validation du formulaire dans certaines conditions spécifiques"

# Mélange de plusieurs changements
git commit -m "fix login, ajout feature export, update readme"
```

### Règles d'or pour les messages de commit

1. **Utilisez l'impératif** : "Ajoute" plutôt que "Ajouté" ou "Ajoute"
2. **Soyez concis** : 50 caractères maximum pour la première ligne
3. **Expliquez le "pourquoi"**, pas le "quoi" (le code montre le "quoi")
4. **Un commit = une modification logique** : ne mélangez pas plusieurs changements
5. **Écrivez au présent** : "Corrige le bug" plutôt que "Corrigé le bug"

---

## Annuler des modifications

Git offre plusieurs façons d'annuler des modifications selon votre situation.

### Annuler des modifications non commitées

```bash
# Annuler les modifications d'un fichier (working directory)
git checkout -- fichier.py
# ou (Git 2.23+)
git restore fichier.py

# Annuler toutes les modifications
git checkout -- .
# ou
git restore .

# Retirer un fichier du staging (mais garder les modifications)
git reset HEAD fichier.py
# ou
git restore --staged fichier.py
```

### Modifier le dernier commit

```bash
# Modifier le message du dernier commit
git commit --amend -m "Nouveau message"

# Ajouter des fichiers oubliés au dernier commit
git add fichier_oublie.py
git commit --amend --no-edit
```

**⚠️ Attention** : n'utilisez jamais `--amend` sur un commit déjà poussé sur le distant !

### Annuler un commit (sans le supprimer)

```bash
# Créer un nouveau commit qui annule un commit précédent
git revert a1b2c3d

# Annuler le dernier commit
git revert HEAD
```

`git revert` est sûr car il crée un nouveau commit. L'historique reste intact.

### Revenir à un commit antérieur (attention !)

```bash
# Revenir à un commit en gardant les modifications en staging
git reset --soft a1b2c3d

# Revenir à un commit en gardant les modifications dans working directory
git reset --mixed a1b2c3d
# ou simplement
git reset a1b2c3d

# Revenir à un commit en supprimant TOUTES les modifications
git reset --hard a1b2c3d
```

**⚠️ Attention** : `git reset --hard` supprime définitivement vos modifications !

### Tableau récapitulatif

| Commande | Working Directory | Staging | Repository | Sécurité |
|----------|-------------------|---------|------------|----------|
| `git restore fichier.py` | Annulé | - | - | ⚠️ Perte de modifs |
| `git restore --staged` | Préservé | Annulé | - | ✅ Sûr |
| `git revert` | Préservé | Préservé | Nouveau commit | ✅ Sûr |
| `git reset --soft` | Préservé | Préservé | Revient en arrière | ⚠️ Modifie historique |
| `git reset --mixed` | Préservé | Annulé | Revient en arrière | ⚠️ Modifie historique |
| `git reset --hard` | Annulé | Annulé | Revient en arrière | ❌ Dangereux |

---

## Résolution de conflits

Les conflits surviennent quand deux personnes modifient la même partie d'un fichier. Git ne peut pas décider automatiquement quelle version garder.

### Quand les conflits apparaissent-ils ?

- Lors d'un `git merge`
- Lors d'un `git pull` (qui fait un merge)
- Lors d'un `git rebase`

### Comment résoudre un conflit ?

#### Étape 1 : Git vous informe

```bash
git pull
# Output:
Auto-merging fichier.py
CONFLICT (content): Merge conflict in fichier.py
Automatic merge failed; fix conflicts and then commit the result.
```

#### Étape 2 : Identifier les fichiers en conflit

```bash
git status
# Output:
both modified: fichier.py
```

#### Étape 3 : Ouvrir le fichier et voir les marqueurs

Git ajoute des marqueurs dans le fichier :

```python
def calculer_prix(prix_base, quantite):
<<<<<<< HEAD
    # Version locale (votre code)
    total = prix_base * quantite * 1.20  # TVA à 20%
=======
    # Version distante (code de quelqu'un d'autre)
    total = prix_base * quantite * 1.10  # TVA à 10%
>>>>>>> branch-name
    return total
```

**Marqueurs** :
- `<<<<<<< HEAD` : début de votre version
- `=======` : séparation
- `>>>>>>> branch-name` : fin de l'autre version

#### Étape 4 : Éditer le fichier

Supprimez les marqueurs et gardez le code que vous voulez :

```python
def calculer_prix(prix_base, quantite):
    # Décision : garder la TVA à 20%
    total = prix_base * quantite * 1.20
    return total
```

#### Étape 5 : Marquer comme résolu

```bash
# Ajouter le fichier résolu
git add fichier.py

# Vérifier l'état
git status

# Terminer le merge
git commit -m "Résolution du conflit sur le calcul de TVA"
```

### Outils pour faciliter la résolution

La plupart des éditeurs modernes ont des outils intégrés :

**VS Code** :
- Ouvre automatiquement les fichiers en conflit
- Boutons "Accept Current Change", "Accept Incoming Change", "Accept Both"

**Ligne de commande** :
```bash
# Utiliser un outil de merge visuel
git mergetool
```

### Éviter les conflits

1. **Tirez régulièrement** : `git pull` souvent pour rester à jour
2. **Commitez souvent** : de petits commits fréquents causent moins de conflits
3. **Communiquez** : informez votre équipe quand vous travaillez sur un fichier
4. **Utilisez des branches** : travaillez sur des fonctionnalités isolées

---

## Bonnes pratiques Git

### 1. Commitez régulièrement

- Faites de petits commits fréquents plutôt qu'un gros commit
- Chaque commit doit représenter une modification logique
- Commitez au moins une fois par jour de travail

### 2. Écrivez de bons messages de commit

```bash
# Bon
git commit -m "feat: ajout de la validation des emails"

# Mauvais
git commit -m "update"
```

### 3. Utilisez des branches pour les fonctionnalités

```bash
# Créer une branche pour chaque nouvelle fonctionnalité
git checkout -b feature/nom-de-la-fonctionnalite

# Travaillez sur la fonctionnalité
# ...

# Fusionnez quand c'est terminé
git checkout main
git merge feature/nom-de-la-fonctionnalite
```

### 4. Tirez avant de pousser

```bash
# Toujours récupérer les dernières modifications avant de pousser
git pull
git push
```

### 5. Ne commitez jamais de fichiers sensibles

```bash
# Utilisez .gitignore pour exclure :
# - Mots de passe et clés API
# - Fichiers de configuration locaux
# - Fichiers générés automatiquement
```

### 6. Vérifiez avant de commiter

```bash
# Vérifiez ce que vous allez commiter
git status
git diff --staged

# Puis commitez
git commit -m "message"
```

### 7. Utilisez des tags pour les versions

```bash
# Créer un tag pour marquer une version
git tag -a v1.0.0 -m "Version 1.0.0 - Première release"

# Pousser les tags
git push --tags

# Lister les tags
git tag
```

### 8. Revoyez l'historique régulièrement

```bash
# Voir ce qui a été fait récemment
git log --oneline -10

# Voir qui a modifié quoi
git blame fichier.py
```

---

## Workflows Git courants

### Workflow simple (solo ou petite équipe)

```
main (branche principale)
  ↓
Feature branches (branches de fonctionnalités)
  ↓
Merge vers main
```

**Étapes** :
1. Créer une branche pour chaque fonctionnalité
2. Travailler sur la branche
3. Fusionner dans main quand c'est terminé

### Git Flow (projets plus complexes)

```
main          : Production (toujours stable)
  ↓
develop       : Développement (intégration)
  ↓
feature/*     : Nouvelles fonctionnalités
hotfix/*      : Corrections urgentes
release/*     : Préparation de release
```

### GitHub Flow (projets web modernes)

```
main          : Production (toujours déployable)
  ↓
feature       : Branche de fonctionnalité
  ↓
Pull Request  : Revue de code
  ↓
Merge         : Déploiement automatique
```

---

## Commandes Git avancées (bonus)

### Voir qui a modifié chaque ligne

```bash
git blame fichier.py
```

### Chercher dans l'historique

```bash
# Chercher un mot dans les messages de commit
git log --grep="bug"

# Chercher dans le code
git log -S "nom_fonction"
```

### Sauvegarder temporairement des modifications

```bash
# Mettre de côté les modifications en cours
git stash

# Lister les stashes
git stash list

# Récupérer les modifications
git stash pop

# Récupérer sans supprimer du stash
git stash apply
```

### Nettoyer les branches

```bash
# Supprimer une branche locale
git branch -d nom-branche

# Forcer la suppression
git branch -D nom-branche

# Supprimer une branche distante
git push origin --delete nom-branche

# Voir les branches déjà fusionnées
git branch --merged
```

### Créer des alias

```bash
# Créer des raccourcis pour les commandes fréquentes
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Utilisation
git co main        # au lieu de git checkout main
git br             # au lieu de git branch
```

### Cherrypick (appliquer un commit spécifique)

```bash
# Appliquer un commit d'une autre branche
git cherry-pick a1b2c3d
```

---

## Ressources et outils utiles

### Documentation officielle

- **Pro Git Book** (gratuit) : [git-scm.com/book](https://git-scm.com/book/fr/v2)
- **Documentation Git** : [git-scm.com/doc](https://git-scm.com/doc)
- **Git Reference** : [git-scm.com/docs](https://git-scm.com/docs)

### Outils visuels

**GitHub Desktop** : client Git avec interface graphique
- Simple et intuitif
- Parfait pour débuter
- [desktop.github.com](https://desktop.github.com/)

**GitKraken** : client Git professionnel avec visualisation des branches
- Interface moderne
- Gratuit pour l'open source
- [gitkraken.com](https://www.gitkraken.com/)

**SourceTree** : client Git gratuit de Atlassian
- Très complet
- [sourcetreeapp.com](https://www.sourcetreeapp.com/)

### Intégrations IDE

- **VS Code** : extension GitLens (excellent pour voir l'historique)
- **PyCharm** : Git intégré nativement
- **Sublime Text** : package Sublime Merge

### Tutoriels interactifs

- **Learn Git Branching** : [learngitbranching.js.org](https://learngitbranching.js.org/)
- **Git-it** : tutoriel en ligne de commande
- **GitHub Learning Lab** : [lab.github.com](https://lab.github.com/)

---

## Aide-mémoire (Cheat Sheet)

### Configuration

```bash
git config --global user.name "Nom"
git config --global user.email "email@example.com"
git config --list
```

### Création de repository

```bash
git init                                    # Nouveau repo local
git clone URL                               # Cloner un repo distant
```

### Modifications

```bash
git status                                  # État du repo
git add fichier.py                          # Ajouter au staging
git add .                                   # Ajouter tous les fichiers
git commit -m "message"                     # Créer un commit
git commit -am "message"                    # Add + commit (fichiers trackés)
```

### Branches

```bash
git branch                                  # Lister les branches
git branch nom                              # Créer une branche
git checkout nom                            # Changer de branche
git checkout -b nom                         # Créer et changer
git merge nom                               # Fusionner une branche
git branch -d nom                           # Supprimer une branche
```

### Synchronisation

```bash
git remote add origin URL                   # Ajouter un distant
git push -u origin main                     # Pousser (première fois)
git push                                    # Pousser
git pull                                    # Tirer (fetch + merge)
git fetch                                   # Récupérer sans merger
```

### Historique

```bash
git log                                     # Historique complet
git log --oneline                           # Historique condensé
git log --graph --all                       # Avec graphique
git diff                                    # Différences non stagées
git diff --staged                           # Différences stagées
```

### Annulation

```bash
git restore fichier.py                      # Annuler modifications
git restore --staged fichier.py             # Retirer du staging
git reset HEAD~1                            # Annuler dernier commit (garder modifs)
git reset --hard HEAD~1                     # Annuler dernier commit (supprimer modifs)
git revert a1b2c3d                          # Créer commit qui annule
```

---

## Résumé

Git est un outil indispensable pour tout développeur Python. Voici ce que vous devez retenir :

✅ **Git sauvegarde l'historique complet** de votre projet et permet de revenir en arrière

✅ **Le workflow de base** : modifier → add → commit → push

✅ **Les branches** permettent de travailler sur plusieurs choses en parallèle

✅ **GitHub/GitLab** permettent de collaborer et de sauvegarder votre code en ligne

✅ **Le .gitignore** évite de commiter des fichiers inutiles

✅ **De bons messages de commit** rendent l'historique lisible

✅ **Commitez souvent** avec de petites modifications logiques

✅ **Tirez avant de pousser** pour éviter les conflits

### Pour bien débuter

1. **Commencez simple** : init, add, commit, push
2. **Pratiquez régulièrement** : utilisez Git pour tous vos projets
3. **Ne paniquez pas** : avec Git, il est très difficile de perdre du code
4. **Explorez progressivement** : branches, merge, rebase, etc.
5. **Utilisez les outils visuels** si la ligne de commande vous intimide

Git peut sembler complexe au début, mais avec la pratique, il deviendra une seconde nature. Chaque développeur est passé par là ! 🚀

N'oubliez pas : Git est là pour vous aider, pas pour vous compliquer la vie. Commencez par les commandes de base, et ajoutez progressivement les fonctionnalités avancées à votre arsenal.

⏭️ [Patterns de conception courants](/12-projets-et-bonnes-pratiques/03-patterns-de-conception.md)
