🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.3 Sérialisation avec Pickle

## Introduction

Imaginez que vous avez passé du temps à créer des objets Python complexes : des listes, des dictionnaires, des objets personnalisés... et vous voulez les **sauvegarder** pour les réutiliser plus tard sans avoir à les recréer. C'est exactement ce que fait **pickle** !

**Pickle** est un module Python qui permet de :
- **Sérialiser** : convertir des objets Python en un format binaire sauvegardable
- **Désérialiser** : recréer les objets Python à partir du format binaire

C'est comme mettre vos objets Python "en conserve" pour les utiliser plus tard !

---

## Qu'est-ce que la Sérialisation ?

La **sérialisation** est le processus de transformation d'un objet en mémoire en une séquence d'octets qui peut être :
- Sauvegardée dans un fichier
- Transmise sur un réseau
- Stockée dans une base de données

La **désérialisation** est l'opération inverse : recréer l'objet à partir de ces octets.

### Analogie

Pensez à un meuble en kit :
- **Sérialisation** = démonter le meuble et le mettre dans un carton plat
- **Sauvegarde** = stocker le carton dans votre garage
- **Désérialisation** = ressortir le carton et remonter le meuble

---

## Le Module `pickle`

### Importation

```python
import pickle
```

Le module `pickle` est inclus dans la bibliothèque standard Python, aucune installation nécessaire !

### Les Fonctions Principales

| Fonction | Description | Usage |
|----------|-------------|-------|
| `pickle.dump()` | Sérialise un objet dans un **fichier** | Sauvegarde |
| `pickle.dumps()` | Sérialise un objet en **bytes** (string) | Transmission |
| `pickle.load()` | Désérialise depuis un **fichier** | Chargement |
| `pickle.loads()` | Désérialise depuis des **bytes** | Réception |

**Astuce :** Le "s" dans `dumps()` et `loads()` signifie "string" (chaîne de bytes).

---

## Sauvegarder des Objets (Sérialisation)

### Exemple 1 : Sauvegarder une liste

```python
import pickle

# Liste à sauvegarder
ma_liste = [1, 2, 3, 4, 5, "Python", True, 3.14]

# Sauvegarder dans un fichier
with open('ma_liste.pkl', 'wb') as fichier:
    pickle.dump(ma_liste, fichier)

print("Liste sauvegardée avec succès !")
```

**Points importants :**
- Mode `'wb'` : **w**rite **b**inary (écriture binaire)
- Extension `.pkl` : convention pour les fichiers pickle

### Exemple 2 : Sauvegarder un dictionnaire

```python
import pickle

# Dictionnaire avec des données complexes
utilisateur = {
    'nom': 'Dupont',
    'prenom': 'Marie',
    'age': 28,
    'competences': ['Python', 'SQL', 'Django'],
    'actif': True,
    'scores': [85, 92, 78, 95]
}

# Sauvegarder
with open('utilisateur.pkl', 'wb') as fichier:
    pickle.dump(utilisateur, fichier)

print("Utilisateur sauvegardé !")
```

### Exemple 3 : Sauvegarder plusieurs objets

```python
import pickle

nom = "Alice"  
age = 30  
hobbies = ["lecture", "natation", "musique"]  

# Sauvegarder plusieurs objets dans le même fichier
with open('donnees_multiples.pkl', 'wb') as fichier:
    pickle.dump(nom, fichier)
    pickle.dump(age, fichier)
    pickle.dump(hobbies, fichier)

print("Plusieurs objets sauvegardés !")
```

---

## Charger des Objets (Désérialisation)

### Exemple 1 : Charger une liste

```python
import pickle

# Charger la liste sauvegardée précédemment
with open('ma_liste.pkl', 'rb') as fichier:
    ma_liste = pickle.load(fichier)

print("Liste chargée :", ma_liste)  
print("Type :", type(ma_liste))  
```

**Point important :** Mode `'rb'` : **r**ead **b**inary (lecture binaire)

### Exemple 2 : Charger un dictionnaire

```python
import pickle

# Charger le dictionnaire
with open('utilisateur.pkl', 'rb') as fichier:
    utilisateur = pickle.load(fichier)

# Utiliser les données
print(f"Nom : {utilisateur['nom']}")  
print(f"Âge : {utilisateur['age']} ans")  
print(f"Compétences : {', '.join(utilisateur['competences'])}")  
```

### Exemple 3 : Charger plusieurs objets

```python
import pickle

# Charger dans le même ordre que la sauvegarde
with open('donnees_multiples.pkl', 'rb') as fichier:
    nom = pickle.load(fichier)
    age = pickle.load(fichier)
    hobbies = pickle.load(fichier)

print(f"{nom}, {age} ans")  
print(f"Hobbies : {hobbies}")  
```

**Attention :** Il faut charger les objets dans le **même ordre** qu'ils ont été sauvegardés !

---

## Sérialisation en Bytes (Sans Fichier)

### Avec `dumps()` et `loads()`

Parfois, on veut sérialiser un objet sans utiliser de fichier, par exemple pour l'envoyer sur un réseau.

```python
import pickle

# Objet à sérialiser
donnees = {'nom': 'Python', 'version': 3.12, 'tags': ['simple', 'puissant']}

# Sérialiser en bytes
donnees_bytes = pickle.dumps(donnees)

print("Type :", type(donnees_bytes))  # <class 'bytes'>  
print("Taille :", len(donnees_bytes), "octets")  

# Désérialiser
donnees_restaurees = pickle.loads(donnees_bytes)  
print("Données restaurées :", donnees_restaurees)  
```

---

## Sauvegarder des Objets Personnalisés

L'un des grands avantages de pickle est qu'il peut sauvegarder des **objets de classes personnalisées** !

### Exemple : Classe Personne

```python
import pickle

# Définir une classe
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def se_presenter(self):
        return f"Je m'appelle {self.nom}, j'ai {self.age} ans et j'habite à {self.ville}"

# Créer une instance
personne1 = Personne("Marie", 28, "Paris")  
print(personne1.se_presenter())  

# Sauvegarder l'objet
with open('personne.pkl', 'wb') as fichier:
    pickle.dump(personne1, fichier)

print("Objet Personne sauvegardé !")
```

### Charger l'objet personnalisé

```python
import pickle

# IMPORTANT : La classe doit être définie avant de charger !
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def se_presenter(self):
        return f"Je m'appelle {self.nom}, j'ai {self.age} ans et j'habite à {self.ville}"

# Charger l'objet
with open('personne.pkl', 'rb') as fichier:
    personne_chargee = pickle.load(fichier)

# L'objet fonctionne normalement !
print(personne_chargee.se_presenter())  
print(f"Type : {type(personne_chargee)}")  
```

**Important :** La définition de la classe doit être disponible lors du chargement !

---

## Exemple Pratique : Système de Sauvegarde de Jeu

Imaginons un jeu simple avec sauvegarde :

```python
import pickle

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.points = 0
        self.inventaire = []

    def gagner_points(self, points):
        self.points += points
        print(f"+{points} points ! Total : {self.points}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"Objet ajouté : {objet}")

    def afficher_stats(self):
        print(f"\n{'='*40}")
        print(f"Joueur : {self.nom}")
        print(f"Niveau : {self.niveau}")
        print(f"Points : {self.points}")
        print(f"Inventaire : {', '.join(self.inventaire) if self.inventaire else 'vide'}")
        print(f"{'='*40}\n")

def sauvegarder_partie(joueur, fichier='sauvegarde.pkl'):
    """Sauvegarde la partie"""
    with open(fichier, 'wb') as f:
        pickle.dump(joueur, f)
    print("✅ Partie sauvegardée !")

def charger_partie(fichier='sauvegarde.pkl'):
    """Charge une partie sauvegardée"""
    try:
        with open(fichier, 'rb') as f:
            joueur = pickle.load(f)
        print("✅ Partie chargée !")
        return joueur
    except FileNotFoundError:
        print("❌ Aucune sauvegarde trouvée")
        return None

# === Nouvelle partie ===
joueur = Joueur("Alice")  
joueur.gagner_points(100)  
joueur.ajouter_objet("Épée")  
joueur.ajouter_objet("Potion")  
joueur.afficher_stats()  

# Sauvegarder
sauvegarder_partie(joueur)

# === Simuler la fermeture du jeu ===
del joueur

# === Relancer le jeu ===
joueur = charger_partie()  
if joueur:  
    joueur.afficher_stats()
    joueur.gagner_points(50)
    joueur.ajouter_objet("Bouclier")
    joueur.afficher_stats()
```

---

## Exemple : Cache de Résultats

Pickle est utile pour mettre en cache des calculs coûteux :

```python
import pickle  
import time  

def calcul_long(n):
    """Simule un calcul long"""
    print(f"Calcul en cours pour n={n}...")
    time.sleep(2)  # Simule un calcul de 2 secondes
    return n ** 2

def calcul_avec_cache(n, fichier_cache='cache.pkl'):
    """Calcul avec système de cache"""

    # Essayer de charger depuis le cache
    try:
        with open(fichier_cache, 'rb') as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    # Si le résultat est en cache, le retourner
    if n in cache:
        print(f"✅ Résultat trouvé en cache pour n={n}")
        return cache[n]

    # Sinon, calculer et sauvegarder
    resultat = calcul_long(n)
    cache[n] = resultat

    with open(fichier_cache, 'wb') as f:
        pickle.dump(cache, f)

    return resultat

# Premier appel : calcul de 2 secondes
print("Premier appel :")  
resultat = calcul_avec_cache(10)  
print(f"Résultat : {resultat}\n")  

# Deuxième appel : instantané (depuis le cache)
print("Deuxième appel :")  
resultat = calcul_avec_cache(10)  
print(f"Résultat : {resultat}")  
```

---

## Gestion des Erreurs

Il est important de gérer les erreurs lors de l'utilisation de pickle :

```python
import pickle

def sauvegarder_securise(objet, fichier):
    """Sauvegarde avec gestion d'erreurs"""
    try:
        with open(fichier, 'wb') as f:
            pickle.dump(objet, f)
        print(f"✅ Sauvegarde réussie : {fichier}")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False

def charger_securise(fichier, defaut=None):
    """Chargement avec gestion d'erreurs"""
    try:
        with open(fichier, 'rb') as f:
            objet = pickle.load(f)
        print(f"✅ Chargement réussi : {fichier}")
        return objet
    except FileNotFoundError:
        print(f"⚠️ Fichier non trouvé : {fichier}")
        return defaut
    except pickle.UnpicklingError:
        print(f"❌ Fichier pickle corrompu : {fichier}")
        return defaut
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        return defaut

# Utilisation
donnees = {'clé': 'valeur'}  
sauvegarder_securise(donnees, 'donnees.pkl')  

# Charger avec valeur par défaut
resultat = charger_securise('donnees.pkl', defaut={})  
print(f"Données : {resultat}")  
```

---

## Protocoles Pickle

Pickle a évolué au fil des versions de Python. Il existe plusieurs **protocoles** :

```python
import pickle

donnees = {'nom': 'Python', 'version': 3.12}

# Protocole 0 : ASCII, compatible avec anciennes versions
with open('proto0.pkl', 'wb') as f:
    pickle.dump(donnees, f, protocol=0)

# Protocole le plus récent (recommandé)
with open('proto_recent.pkl', 'wb') as f:
    pickle.dump(donnees, f, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Protocole le plus récent : {pickle.HIGHEST_PROTOCOL}")
```

**Recommandation :** Utilisez toujours `protocol=pickle.HIGHEST_PROTOCOL` pour de meilleures performances, sauf si vous devez être compatible avec de très anciennes versions de Python.

---

## Comparaison : Pickle vs JSON

### Tableau Comparatif

| Critère | Pickle | JSON |
|---------|--------|------|
| **Format** | Binaire | Texte |
| **Lisible** | ❌ Non | ✅ Oui |
| **Types supportés** | ✅ Tous les types Python | ⚠️ Types limités |
| **Objets personnalisés** | ✅ Oui | ❌ Non (sans conversion) |
| **Sécurité** | ⚠️ Risques | ✅ Sûr |
| **Portabilité** | ⚠️ Python uniquement | ✅ Universel |
| **Taille fichier** | ✅ Compact | ⚠️ Plus volumineux |
| **Vitesse** | ✅ Rapide | ⚠️ Plus lent |

### Exemple Comparatif

```python
import pickle  
import json  

# Données complexes
donnees = {
    'nom': 'Alice',
    'date': (2024, 10, 27),  # Tuple
    'set': {1, 2, 3},         # Set
    'bytes': b'data'          # Bytes
}

# Pickle : fonctionne avec tous les types
with open('donnees.pkl', 'wb') as f:
    pickle.dump(donnees, f)
print("✅ Pickle : sauvegarde réussie")

# JSON : ne supporte pas tous les types
try:
    with open('donnees.json', 'w') as f:
        json.dump(donnees, f)
except TypeError as e:
    print(f"❌ JSON : {e}")
```

### Quand Utiliser Quoi ?

#### Utilisez Pickle quand :
✅ Vous travaillez uniquement avec Python  
✅ Vous devez sauvegarder des objets complexes  
✅ Vous voulez la meilleure performance  
✅ Les données restent dans votre système (pas d'échange externe)

#### Utilisez JSON quand :
✅ Vous devez échanger des données avec d'autres langages  
✅ Vous voulez un format lisible par l'humain  
✅ Vous travaillez avec des APIs web  
✅ La sécurité est une priorité

---

## ⚠️ Sécurité et Précautions

### Le Danger de Pickle

**ATTENTION :** Pickle peut exécuter du code arbitraire lors de la désérialisation !

```python
import pickle

# ⚠️ DANGER : Ne JAMAIS charger un fichier pickle non fiable !
# Pickle peut exécuter du code malveillant !

# ❌ TRÈS RISQUÉ
with open('fichier_externe.pkl', 'rb') as f:
    donnees = pickle.load(f)  # Peut exécuter du code !
```

### Règles de Sécurité

1. **Ne JAMAIS** charger de fichiers pickle provenant de sources non fiables
2. **Ne JAMAIS** accepter de fichiers pickle envoyés par des utilisateurs
3. Utilisez pickle **uniquement** pour vos propres données
4. Pour échanger des données, préférez JSON ou d'autres formats sûrs

### Alternative Sécurisée

Si vous devez partager des données, utilisez JSON :

```python
import json

# ✅ Sûr pour l'échange de données
donnees = {'utilisateur': 'Alice', 'role': 'admin'}

# Sauvegarder
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(donnees, f)

# Charger (sûr même depuis une source externe)
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
```

---

## Limitations de Pickle

Certains objets ne peuvent pas être pickled :

### 1. Connexions et fichiers ouverts

```python
import pickle

# ❌ Ne fonctionne pas
fichier_ouvert = open('test.txt', 'r')  
try:  
    pickle.dumps(fichier_ouvert)
except TypeError as e:
    print(f"Erreur : {e}")
finally:
    fichier_ouvert.close()
```

### 2. Fonctions lambda

```python
import pickle

# ❌ Ne fonctionne pas
ma_fonction = lambda x: x * 2  
try:  
    pickle.dumps(ma_fonction)
except AttributeError as e:
    print(f"Erreur : impossible de pickler une lambda")
```

### 3. Objets avec des connexions réseau

```python
# ❌ Ne fonctionne pas
import socket

# Les sockets ne peuvent pas être picklés
sock = socket.socket()
# pickle.dumps(sock)  # Erreur !
```

---

## Bonnes Pratiques

### 1. Toujours utiliser le mode binaire

```python
# ✅ Bon
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# ❌ Erreur
with open('data.pkl', 'w') as f:
    pickle.dump(data, f)  # TypeError !
```

### 2. Utiliser le protocole le plus récent

```python
# ✅ Recommandé
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
```

### 3. Documenter les dépendances de classes

```python
# ✅ Bon : documenter les classes nécessaires
"""
Pour charger ce fichier pickle, vous devez avoir :
- La classe Joueur définie
- Le module datetime importé
"""
```

### 4. Versionner vos données

```python
import pickle

# Inclure un numéro de version
donnees = {
    'version': 1,
    'utilisateur': 'Alice',
    'score': 100
}

with open('save.pkl', 'wb') as f:
    pickle.dump(donnees, f)

# Lors du chargement, vérifier la version
with open('save.pkl', 'rb') as f:
    donnees = pickle.load(f)
    if donnees.get('version') != 1:
        print("⚠️ Version incompatible !")
```

### 5. Créer des fonctions réutilisables

```python
import pickle  
from pathlib import Path  

def sauvegarder(objet, fichier):
    """Sauvegarde un objet avec pickle"""
    with open(fichier, 'wb') as f:
        pickle.dump(objet, f, protocol=pickle.HIGHEST_PROTOCOL)

def charger(fichier, defaut=None):
    """Charge un objet avec pickle"""
    if not Path(fichier).exists():
        return defaut
    with open(fichier, 'rb') as f:
        return pickle.load(f)

# Utilisation simple
sauvegarder({'key': 'value'}, 'data.pkl')  
data = charger('data.pkl', defaut={})  
```

---

## Résumé

### Fonctions Principales

```python
import pickle

# Sauvegarder dans un fichier
pickle.dump(objet, fichier)

# Charger depuis un fichier
objet = pickle.load(fichier)

# Sérialiser en bytes
bytes_data = pickle.dumps(objet)

# Désérialiser depuis bytes
objet = pickle.loads(bytes_data)
```

### Points Clés à Retenir

✅ **Pickle** permet de sauvegarder n'importe quel objet Python  
✅ Parfait pour **sauvegardes** et **caches** locaux  
✅ Utiliser toujours le mode **binaire** (`'wb'` et `'rb'`)  
✅ Peut sauvegarder des **objets personnalisés**  
⚠️ **DANGER** : ne jamais charger de fichiers pickle non fiables  
⚠️ Format **Python uniquement**, pas pour l'échange avec d'autres langages  
⚠️ Certains objets ne peuvent pas être picklés (fichiers, connexions)

### Quand Utiliser Pickle ?

| ✅ Utilisez Pickle | ❌ N'utilisez PAS Pickle |
|-------------------|------------------------|
| Sauvegardes locales | Échange avec d'autres langages |
| Cache de calculs | APIs web |
| Objets Python complexes | Données provenant d'utilisateurs |
| États de session | Configuration partagée |
| Prototypes rapides | Production critique |

---

Vous maîtrisez maintenant la sérialisation avec pickle ! N'oubliez pas : pickle est puissant mais doit être utilisé avec précaution, uniquement pour vos propres données.

⏭️ [Gestion des chemins avec pathlib](/04-gestion-donnees-et-fichiers/04-gestion-chemins-pathlib.md)
