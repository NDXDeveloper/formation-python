🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.1 Lecture et Écriture de Fichiers Texte et Binaires

## Introduction

La manipulation de fichiers est une compétence essentielle en programmation. Python offre des outils simples et puissants pour lire et écrire des fichiers, que ce soit pour sauvegarder des données, traiter des documents ou échanger des informations entre programmes.

Dans ce chapitre, nous allons découvrir comment :
- Ouvrir et fermer des fichiers de manière sécurisée
- Lire le contenu de fichiers texte
- Écrire dans des fichiers
- Travailler avec des fichiers binaires

---

## Les Modes d'Ouverture de Fichiers

Avant de travailler avec un fichier, il faut l'ouvrir en spécifiant un **mode**. Voici les modes les plus courants :

| Mode | Description | Crée le fichier | Efface le contenu |
|------|-------------|-----------------|-------------------|
| `'r'` | Lecture seule (Read) | Non | Non |
| `'w'` | Écriture (Write) | Oui | **Oui** |
| `'a'` | Ajout (Append) | Oui | Non |
| `'x'` | Création exclusive | Oui | N/A |
| `'r+'` | Lecture et écriture | Non | Non |

Pour les fichiers binaires, on ajoute le suffixe `b` : `'rb'`, `'wb'`, `'ab'`, etc.

---

## Lecture de Fichiers Texte

### Méthode 1 : Lire tout le contenu d'un coup

La méthode `read()` permet de lire l'intégralité d'un fichier en une seule fois :

```python
# Ouvrir le fichier en mode lecture
fichier = open('mon_document.txt', 'r', encoding='utf-8')

# Lire tout le contenu
contenu = fichier.read()  
print(contenu)  

# Toujours fermer le fichier !
fichier.close()
```

**Points importants :**
- `encoding='utf-8'` permet de gérer correctement les accents et caractères spéciaux
- Il est crucial de **toujours fermer** le fichier avec `close()` pour libérer les ressources

### Méthode 2 : Lire ligne par ligne

Pour les fichiers volumineux, il est préférable de lire ligne par ligne :

```python
fichier = open('mon_document.txt', 'r', encoding='utf-8')

for ligne in fichier:
    print(ligne.strip())  # strip() enlève les retours à la ligne

fichier.close()
```

### Méthode 3 : Lire toutes les lignes dans une liste

La méthode `readlines()` retourne une liste contenant toutes les lignes :

```python
fichier = open('mon_document.txt', 'r', encoding='utf-8')  
lignes = fichier.readlines()  
fichier.close()  

print(f"Le fichier contient {len(lignes)} lignes")  
for i, ligne in enumerate(lignes, 1):  
    print(f"Ligne {i}: {ligne.strip()}")
```

### Méthode 4 : Lire une seule ligne

La méthode `readline()` lit une ligne à la fois :

```python
fichier = open('mon_document.txt', 'r', encoding='utf-8')

premiere_ligne = fichier.readline()  
deuxieme_ligne = fichier.readline()  

print("Première ligne:", premiere_ligne.strip())  
print("Deuxième ligne:", deuxieme_ligne.strip())  

fichier.close()
```

---

## Écriture dans des Fichiers Texte

### Mode 'w' - Écriture (écrase le contenu existant)

```python
# Attention : le mode 'w' efface le contenu existant !
fichier = open('nouveau_fichier.txt', 'w', encoding='utf-8')

fichier.write("Bonjour, ceci est la première ligne\n")  
fichier.write("Et voici la deuxième ligne\n")  

fichier.close()
```

**Attention :** Le mode `'w'` écrase complètement le fichier s'il existe déjà !

### Mode 'a' - Ajout (conserve le contenu existant)

```python
# Le mode 'a' ajoute à la fin sans effacer
fichier = open('nouveau_fichier.txt', 'a', encoding='utf-8')

fichier.write("Cette ligne est ajoutée à la fin\n")  
fichier.write("Et encore une autre ligne\n")  

fichier.close()
```

### Écrire plusieurs lignes avec writelines()

```python
fichier = open('liste_courses.txt', 'w', encoding='utf-8')

courses = [
    "Pommes\n",
    "Pain\n",
    "Lait\n",
    "Fromage\n"
]

fichier.writelines(courses)  
fichier.close()  
```

---

## Le Gestionnaire de Contexte : `with`

La méthode recommandée pour travailler avec des fichiers est d'utiliser le mot-clé `with`. Cela garantit que le fichier sera **automatiquement fermé**, même en cas d'erreur.

### Syntaxe avec `with`

```python
# Le fichier est automatiquement fermé à la fin du bloc
with open('mon_document.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()
    print(contenu)

# Ici, le fichier est déjà fermé (pas besoin de close())
```

### Exemple complet de lecture et écriture

```python
# Lire un fichier
with open('source.txt', 'r', encoding='utf-8') as fichier_source:
    lignes = fichier_source.readlines()

# Transformer les données
lignes_majuscules = [ligne.upper() for ligne in lignes]

# Écrire dans un nouveau fichier
with open('destination.txt', 'w', encoding='utf-8') as fichier_dest:
    fichier_dest.writelines(lignes_majuscules)

print("Traitement terminé !")
```

---

## Gestion des Erreurs

Il est important de gérer les erreurs qui peuvent survenir lors de la manipulation de fichiers :

```python
try:
    with open('fichier_inexistant.txt', 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas !")
except PermissionError:
    print("Erreur : Pas les permissions pour accéder au fichier")
except Exception as e:
    print(f"Erreur inattendue : {e}")
```

---

## Fichiers Binaires

Les fichiers binaires contiennent des données non textuelles (images, vidéos, fichiers exécutables, etc.). On utilise les modes avec le suffixe `'b'`.

### Lecture d'un fichier binaire

```python
# Lire une image par exemple
with open('photo.jpg', 'rb') as fichier:
    contenu_binaire = fichier.read()
    print(f"Taille du fichier : {len(contenu_binaire)} octets")
```

### Écriture d'un fichier binaire

```python
# Créer un fichier binaire simple
donnees = bytes([0, 1, 2, 3, 4, 5])

with open('donnees.bin', 'wb') as fichier:
    fichier.write(donnees)

print("Fichier binaire créé")
```

### Copier un fichier binaire

```python
# Copier une image
with open('original.jpg', 'rb') as source:
    contenu = source.read()

with open('copie.jpg', 'wb') as destination:
    destination.write(contenu)

print("Image copiée avec succès")
```

### Lire un fichier binaire par morceaux

Pour les gros fichiers, il est préférable de lire par morceaux :

```python
taille_morceau = 1024  # 1 Ko à la fois

with open('gros_fichier.bin', 'rb') as fichier:
    while True:
        morceau = fichier.read(taille_morceau)
        if not morceau:
            break  # Fin du fichier

        # Traiter le morceau
        print(f"Lu {len(morceau)} octets")
```

---

## Vérifier l'Existence d'un Fichier

Avant d'ouvrir un fichier, on peut vérifier s'il existe avec `pathlib` :

```python
from pathlib import Path

chemin = Path('mon_document.txt')

if chemin.exists():
    print("Le fichier existe")

    if chemin.is_file():
        print("C'est bien un fichier (pas un dossier)")

    print(f"Taille : {chemin.stat().st_size} octets")
else:
    print("Le fichier n'existe pas")
```

> 💡 Vous verrez parfois l'approche plus ancienne avec `os.path.exists()` et `os.path.isfile()`. Les deux fonctionnent, mais `pathlib` est l'approche moderne recommandée (voir section 4.4).

---

## Bonnes Pratiques

### 1. Toujours utiliser `with`

```python
# ✅ Bon
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

# ❌ À éviter
f = open('fichier.txt', 'r')  
contenu = f.read()  
f.close()  # On peut oublier !  
```

### 2. Toujours spécifier l'encodage pour les fichiers texte

```python
# ✅ Bon
with open('fichier.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()

# ❌ À éviter (encodage par défaut peut varier)
with open('fichier.txt', 'r') as f:
    contenu = f.read()
```

### 3. Gérer les erreurs

```python
# ✅ Bon
try:
    with open('fichier.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier introuvable")
```

### 4. Attention au mode 'w'

```python
# ⚠️ Attention : 'w' efface le fichier existant !
# Si vous voulez ajouter, utilisez 'a'

# Pour ajouter
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write("Nouvelle entrée\n")
```

---

## Exemples Pratiques

### Exemple 1 : Compter les mots dans un fichier

```python
with open('texte.txt', 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()
    mots = contenu.split()
    print(f"Nombre de mots : {len(mots)}")
```

### Exemple 2 : Créer un fichier de log

```python
from datetime import datetime

def ajouter_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('application.log', 'a', encoding='utf-8') as log:
        log.write(f"[{timestamp}] {message}\n")

# Utilisation
ajouter_log("Application démarrée")  
ajouter_log("Traitement des données...")  
ajouter_log("Application terminée")  
```

### Exemple 3 : Lire un fichier CSV simple

```python
with open('donnees.csv', 'r', encoding='utf-8') as fichier:
    # Ignorer la première ligne (en-têtes)
    next(fichier)

    for ligne in fichier:
        # Séparer les valeurs par des virgules
        valeurs = ligne.strip().split(',')
        print(valeurs)
```

### Exemple 4 : Sauvegarder une liste en fichier

```python
noms = ["Alice", "Bob", "Charlie", "Diana"]

# Sauvegarder
with open('noms.txt', 'w', encoding='utf-8') as fichier:
    for nom in noms:
        fichier.write(nom + '\n')

# Relire
with open('noms.txt', 'r', encoding='utf-8') as fichier:
    noms_lus = [ligne.strip() for ligne in fichier]
    print(noms_lus)
```

---

## Résumé

| Opération | Méthode | Exemple |
|-----------|---------|---------|
| Lire tout | `read()` | `contenu = f.read()` |
| Lire ligne par ligne | Itération | `for ligne in f:` |
| Lire toutes les lignes | `readlines()` | `lignes = f.readlines()` |
| Lire une ligne | `readline()` | `ligne = f.readline()` |
| Écrire du texte | `write()` | `f.write("texte")` |
| Écrire des lignes | `writelines()` | `f.writelines(liste)` |

**Points clés à retenir :**
- Utilisez toujours `with` pour ouvrir des fichiers
- Spécifiez l'encodage `utf-8` pour les fichiers texte
- Le mode `'w'` écrase le fichier, `'a'` ajoute à la fin
- Les fichiers binaires utilisent les modes `'rb'`, `'wb'`, etc.
- Gérez les erreurs avec `try/except`

---

Vous maîtrisez maintenant les bases de la manipulation de fichiers en Python ! Ces compétences sont fondamentales et vous serviront dans de nombreux projets.

⏭️ [Formats de données (JSON, CSV, XML)](/04-gestion-donnees-et-fichiers/02-formats-de-donnees.md)
