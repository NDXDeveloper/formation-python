🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.3 : Collections spécialisées (namedtuple, defaultdict, Counter)

## Introduction

Le module `collections` de Python offre des alternatives aux types de données built-in comme les listes, tuples et dictionnaires. Ces collections spécialisées résolvent des problèmes courants de manière plus élégante et efficace.

Dans ce chapitre, nous allons découvrir trois collections très utiles :
- **namedtuple** : pour créer des tuples avec des noms de champs
- **defaultdict** : pour des dictionnaires avec des valeurs par défaut
- **Counter** : pour compter facilement des éléments

## namedtuple : Des tuples avec des noms

### Qu'est-ce qu'un namedtuple ?

Un `namedtuple` est comme un tuple normal, mais avec des noms pour chaque position. Cela rend votre code plus lisible et plus facile à maintenir.

### Importation et création

```python
from collections import namedtuple

# Création d'un namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Création d'une instance
p1 = Point(3, 4)
print(p1)  # Point(x=3, y=4)
```

### Comparaison avec un tuple normal

```python
# Avec un tuple normal
coordonnee_normale = (3, 4)
x = coordonnee_normale[0]  # Pas très clair
y = coordonnee_normale[1]  # Pas très clair

# Avec un namedtuple
Point = namedtuple('Point', ['x', 'y'])
coordonnee_nommee = Point(3, 4)
x = coordonnee_nommee.x  # Très clair !
y = coordonnee_nommee.y  # Très clair !
```

### Exemples pratiques

#### Représenter une personne
```python
from collections import namedtuple

# Définition de la structure
Personne = namedtuple('Personne', ['nom', 'age', 'ville'])

# Création d'instances
alice = Personne('Alice', 25, 'Paris')
bob = Personne('Bob', 30, 'Lyon')

print(alice.nom)     # Alice
print(alice.age)     # 25
print(alice.ville)   # Paris

# Affichage complet
print(alice)  # Personne(nom='Alice', age=25, ville='Paris')
```

#### Gérer des coordonnées 3D
```python
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

origine = Point3D(0, 0, 0)
sommet = Point3D(1, 1, 1)

# Calcul de distance
import math
distance = math.sqrt(
    (sommet.x - origine.x)**2 +
    (sommet.y - origine.y)**2 +
    (sommet.z - origine.z)**2
)
print(f"Distance: {distance}")  # Distance: 1.7320508075688772
```

### Méthodes utiles des namedtuples

#### _replace() : Modifier un namedtuple
```python
Personne = namedtuple('Personne', ['nom', 'age', 'ville'])
alice = Personne('Alice', 25, 'Paris')

# Créer une nouvelle instance avec un changement
alice_plus_agee = alice._replace(age=26)
print(alice)           # Personne(nom='Alice', age=25, ville='Paris')
print(alice_plus_agee) # Personne(nom='Alice', age=26, ville='Paris')
```

#### _asdict() : Convertir en dictionnaire
```python
alice = Personne('Alice', 25, 'Paris')
dict_alice = alice._asdict()
print(dict_alice)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

#### _fields : Voir les champs
```python
print(Personne._fields)  # ('nom', 'age', 'ville')
```

## defaultdict : Dictionnaires avec valeurs par défaut

### Le problème avec les dictionnaires normaux

```python
# Avec un dictionnaire normal
compteur = {}
mots = ['chat', 'chien', 'chat', 'oiseau', 'chien', 'chat']

for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1  # Il faut gérer le cas où la clé n'existe pas

print(compteur)  # {'chat': 3, 'chien': 2, 'oiseau': 1}
```

### La solution avec defaultdict

```python
from collections import defaultdict

# Création d'un defaultdict avec int comme factory
compteur = defaultdict(int)  # int() retourne 0 par défaut
mots = ['chat', 'chien', 'chat', 'oiseau', 'chien', 'chat']

for mot in mots:
    compteur[mot] += 1  # Pas besoin de vérifier si la clé existe !

print(compteur)  # defaultdict(<class 'int'>, {'chat': 3, 'chien': 2, 'oiseau': 1})
print(dict(compteur))  # {'chat': 3, 'chien': 2, 'oiseau': 1}
```

### Différents types de valeurs par défaut

#### Avec des listes
```python
from collections import defaultdict

# Grouper des éléments
groupes = defaultdict(list)
donnees = [('fruits', 'pomme'), ('legumes', 'carotte'), ('fruits', 'banane'), ('legumes', 'tomate')]

for categorie, item in donnees:
    groupes[categorie].append(item)

print(dict(groupes))  # {'fruits': ['pomme', 'banane'], 'legumes': ['carotte', 'tomate']}
```

#### Avec des ensembles (sets)
```python
# Éviter les doublons
villes_par_pays = defaultdict(set)
voyages = [('France', 'Paris'), ('France', 'Lyon'), ('France', 'Paris'), ('Italie', 'Rome')]

for pays, ville in voyages:
    villes_par_pays[pays].add(ville)

print(dict(villes_par_pays))  # {'France': {'Lyon', 'Paris'}, 'Italie': {'Rome'}}
```

#### Avec des fonctions personnalisées
```python
# Utiliser lambda pour des valeurs par défaut personnalisées
scores = defaultdict(lambda: "Pas de score")
scores['Alice'] = 85
scores['Bob'] = 92

print(scores['Alice'])    # 85
print(scores['Charlie'])  # Pas de score
```

### Exemple pratique : Analyser du texte

```python
from collections import defaultdict

def analyser_texte(texte):
    # Compter les mots par longueur
    mots_par_longueur = defaultdict(list)
    # Compter les lettres
    compteur_lettres = defaultdict(int)

    mots = texte.lower().split()

    for mot in mots:
        # Nettoyer le mot (enlever la ponctuation)
        mot_propre = ''.join(char for char in mot if char.isalpha())
        if mot_propre:
            mots_par_longueur[len(mot_propre)].append(mot_propre)

            # Compter chaque lettre
            for lettre in mot_propre:
                compteur_lettres[lettre] += 1

    return dict(mots_par_longueur), dict(compteur_lettres)

texte = "Python est un langage de programmation puissant et facile"
longueurs, lettres = analyser_texte(texte)

print("Mots par longueur:")
for longueur, mots in sorted(longueurs.items()):
    print(f"  {longueur} lettres: {mots}")

print("\nLettres les plus fréquentes:")
lettres_triees = sorted(lettres.items(), key=lambda x: x[1], reverse=True)
for lettre, count in lettres_triees[:5]:
    print(f"  {lettre}: {count}")
```

## Counter : Compter facilement

### Introduction à Counter

`Counter` est un dictionnaire spécialisé pour compter des éléments. Il rend le comptage très simple et offre des méthodes pratiques.

### Création d'un Counter

```python
from collections import Counter

# À partir d'une liste
fruits = ['pomme', 'banane', 'pomme', 'orange', 'banane', 'pomme']
compteur = Counter(fruits)
print(compteur)  # Counter({'pomme': 3, 'banane': 2, 'orange': 1})

# À partir d'une chaîne
lettres = Counter('bonjour')
print(lettres)  # Counter({'o': 2, 'n': 2, 'b': 1, 'j': 1, 'u': 1, 'r': 1})

# À partir d'un dictionnaire
compteur_manual = Counter({'a': 3, 'b': 1, 'c': 2})
print(compteur_manual)  # Counter({'a': 3, 'c': 2, 'b': 1})
```

### Méthodes utiles de Counter

#### most_common() : Les éléments les plus fréquents
```python
mots = ['chat', 'chien', 'chat', 'oiseau', 'chien', 'chat', 'poisson']
compteur = Counter(mots)

# Les 3 plus fréquents
print(compteur.most_common(3))  # [('chat', 3), ('chien', 2), ('oiseau', 1)]

# Tous les éléments triés par fréquence
print(compteur.most_common())  # [('chat', 3), ('chien', 2), ('oiseau', 1), ('poisson', 1)]
```

#### Accéder aux compteurs
```python
compteur = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

print(compteur['a'])  # 3
print(compteur['b'])  # 2
print(compteur['z'])  # 0 (pas d'erreur, retourne 0)
```

#### Mettre à jour un Counter
```python
compteur = Counter(['a', 'b', 'c'])
print(compteur)  # Counter({'a': 1, 'b': 1, 'c': 1})

# Ajouter des éléments
compteur.update(['a', 'b', 'b', 'd'])
print(compteur)  # Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

# Soustraire des éléments
compteur.subtract(['a', 'b'])
print(compteur)  # Counter({'b': 2, 'a': 1, 'c': 1, 'd': 1})
```

### Opérations mathématiques avec Counter

```python
compteur1 = Counter(['a', 'b', 'c', 'a'])
compteur2 = Counter(['a', 'b', 'b', 'd'])

print("Compteur 1:", compteur1)  # Counter({'a': 2, 'b': 1, 'c': 1})
print("Compteur 2:", compteur2)  # Counter({'b': 2, 'a': 1, 'd': 1})

# Addition
print("Addition:", compteur1 + compteur2)  # Counter({'a': 3, 'b': 3, 'c': 1, 'd': 1})

# Soustraction
print("Soustraction:", compteur1 - compteur2)  # Counter({'a': 1, 'c': 1})

# Intersection (minimum)
print("Intersection:", compteur1 & compteur2)  # Counter({'a': 1, 'b': 1})

# Union (maximum)
print("Union:", compteur1 | compteur2)  # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
```

### Exemple pratique : Analyser un fichier de log

```python
from collections import Counter
import re

def analyser_logs(contenu_log):
    """Analyse un fichier de log web"""

    # Compter les codes de statut HTTP
    codes_statut = Counter()
    # Compter les adresses IP
    adresses_ip = Counter()
    # Compter les méthodes HTTP
    methodes_http = Counter()

    for ligne in contenu_log.split('\n'):
        if ligne.strip():
            # Exemple de ligne de log: 192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326
            match = re.search(r'(\d+\.\d+\.\d+\.\d+).*?"(GET|POST|PUT|DELETE).*?" (\d+)', ligne)
            if match:
                ip, methode, code = match.groups()
                adresses_ip[ip] += 1
                methodes_http[methode] += 1
                codes_statut[int(code)] += 1

    return codes_statut, adresses_ip, methodes_http

# Exemple d'utilisation
log_exemple = """192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:37] "POST /login HTTP/1.1" 200 1234
192.168.1.1 - - [10/Oct/2023:13:55:38] "GET /page.html HTTP/1.1" 404 0
192.168.1.3 - - [10/Oct/2023:13:55:39] "GET /index.html HTTP/1.1" 200 2326"""

codes, ips, methodes = analyser_logs(log_exemple)
print("Codes de statut:", codes)
print("Top IP:", ips.most_common(2))
print("Méthodes HTTP:", methodes)
```

## Exercices pratiques

### Exercice 1 : namedtuple - Gestion d'étudiants

```python
from collections import namedtuple

# Créez un namedtuple pour représenter un étudiant
Etudiant = namedtuple('Etudiant', ['nom', 'age', 'notes'])

# Créez quelques étudiants
alice = Etudiant('Alice', 20, [15, 16, 14, 18])
bob = Etudiant('Bob', 21, [12, 14, 16, 13])
charlie = Etudiant('Charlie', 19, [17, 18, 19, 16])

etudiants = [alice, bob, charlie]

# Calculez la moyenne de chaque étudiant
for etudiant in etudiants:
    moyenne = sum(etudiant.notes) / len(etudiant.notes)
    print(f"{etudiant.nom} (âge {etudiant.age}): moyenne = {moyenne:.1f}")

# Trouvez l'étudiant avec la meilleure moyenne
meilleur_etudiant = max(etudiants, key=lambda e: sum(e.notes) / len(e.notes))
print(f"Meilleur étudiant: {meilleur_etudiant.nom}")
```

### Exercice 2 : defaultdict - Organiser des données

```python
from collections import defaultdict

# Organisez ces données de ventes par mois et par produit
ventes = [
    ('janvier', 'ordinateur', 1200),
    ('janvier', 'souris', 25),
    ('février', 'ordinateur', 1500),
    ('février', 'clavier', 75),
    ('janvier', 'ordinateur', 1100),
    ('février', 'souris', 30),
    ('mars', 'ordinateur', 1300),
    ('mars', 'clavier', 80),
]

# Créez un dictionnaire imbriqué : mois -> produit -> total des ventes
ventes_par_mois = defaultdict(lambda: defaultdict(int))

for mois, produit, montant in ventes:
    ventes_par_mois[mois][produit] += montant

# Affichez les résultats
for mois, produits in ventes_par_mois.items():
    print(f"\n{mois.capitalize()}:")
    for produit, total in produits.items():
        print(f"  {produit}: {total}€")
```

### Exercice 3 : Counter - Analyse de texte

```python
from collections import Counter
import re

def analyser_poeme(texte):
    """Analyse un poème et retourne des statistiques"""

    # Nettoyer le texte et le diviser en mots
    mots = re.findall(r'\b[a-zA-ZàâäéèêëïîôöùûüÿçÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ]+\b', texte.lower())

    # Compter les mots
    compteur_mots = Counter(mots)

    # Compter les lettres
    compteur_lettres = Counter(''.join(mots))

    # Analyser les longueurs de mots
    longueurs = Counter(len(mot) for mot in mots)

    return compteur_mots, compteur_lettres, longueurs

# Exemple avec un extrait de poème
poeme = """
Demain, dès l'aube, à l'heure où blanchit la campagne,
Je partirai. Vois-tu, je sais que tu m'attends.
J'irai par la forêt, j'irai par la montagne.
Je ne puis demeurer loin de toi plus longtemps.
"""

mots, lettres, longueurs = analyser_poeme(poeme)

print("Mots les plus fréquents:")
for mot, freq in mots.most_common(5):
    print(f"  {mot}: {freq}")

print("\nLettres les plus fréquentes:")
for lettre, freq in lettres.most_common(5):
    print(f"  {lettre}: {freq}")

print("\nDistribution des longueurs de mots:")
for longueur, freq in sorted(longueurs.items()):
    print(f"  {longueur} lettres: {freq} mots")
```

## Comparaison et choix de la bonne collection

### Quand utiliser quoi ?

| Collection | Utilisation | Avantages |
|-----------|-------------|-----------|
| **namedtuple** | Données structurées simples | Lisibilité, immutabilité, moins de mémoire qu'une classe |
| **defaultdict** | Dictionnaires avec valeurs par défaut | Évite les erreurs KeyError, code plus propre |
| **Counter** | Comptage d'éléments | Méthodes spécialisées, opérations mathématiques |

### Exemple comparatif

```python
from collections import namedtuple, defaultdict, Counter

# Problème : analyser des données de ventes
ventes_donnees = [
    ('Alice', 'ordinateur', 1200),
    ('Bob', 'souris', 25),
    ('Alice', 'clavier', 75),
    ('Charlie', 'ordinateur', 1500),
    ('Bob', 'ordinateur', 1100),
    ('Alice', 'souris', 30),
]

# Solution 1 : namedtuple pour structurer les données
Vente = namedtuple('Vente', ['vendeur', 'produit', 'montant'])
ventes_structurees = [Vente(v, p, m) for v, p, m in ventes_donnees]

# Solution 2 : defaultdict pour grouper
ventes_par_vendeur = defaultdict(list)
for vente in ventes_structurees:
    ventes_par_vendeur[vente.vendeur].append(vente)

# Solution 3 : Counter pour compter
produits_vendus = Counter(vente.produit for vente in ventes_structurees)
vendeurs_actifs = Counter(vente.vendeur for vente in ventes_structurees)

# Affichage des résultats
print("Ventes par vendeur:")
for vendeur, ventes in ventes_par_vendeur.items():
    total = sum(vente.montant for vente in ventes)
    print(f"  {vendeur}: {len(ventes)} ventes, total: {total}€")

print("\nProduits les plus vendus:")
for produit, quantite in produits_vendus.most_common():
    print(f"  {produit}: {quantite}")
```

## Conseils et bonnes pratiques

### Pour namedtuple
- Utilisez des noms de champs descriptifs
- Préférez namedtuple aux tuples normaux pour des données structurées
- Considérez dataclasses pour des besoins plus complexes

### Pour defaultdict
- Choisissez la factory function appropriée (int, list, set, etc.)
- Utilisez lambda pour des valeurs par défaut complexes
- Convertissez en dict normal si nécessaire pour l'affichage

### Pour Counter
- Utilisez most_common() pour les analyses de fréquence
- Profitez des opérations mathématiques pour combiner des compteurs
- N'oubliez pas que Counter retourne 0 pour les clés inexistantes

## Résumé

Les collections spécialisées de Python sont des outils puissants qui :
- Rendent le code plus lisible et plus maintenable
- Résolvent des problèmes courants de manière élégante
- Offrent des performances optimisées pour certaines opérations

**Points clés :**
- **namedtuple** : pour des données structurées simples et lisibles
- **defaultdict** : pour éviter les erreurs KeyError et simplifier le code
- **Counter** : pour compter efficacement et analyser des fréquences

Ces collections font partie des outils essentiels du développeur Python moderne !

⏭️

