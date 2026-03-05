🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2.3 Collections Spécialisées (namedtuple, defaultdict, Counter)

## Introduction

Python propose un module appelé `collections` qui contient des structures de données spécialisées, alternatives aux types de base comme les listes, tuples et dictionnaires. Ces structures sont conçues pour résoudre des problèmes courants de manière plus élégante et efficace.

Dans cette section, nous allons explorer trois collections particulièrement utiles :
- **namedtuple** : des tuples avec des champs nommés
- **defaultdict** : des dictionnaires avec valeurs par défaut automatiques
- **Counter** : un outil pour compter des éléments

Ces outils rendent votre code plus lisible, plus concis et moins sujet aux erreurs.

**Pour utiliser ces collections, il faut d'abord les importer :**
```python
from collections import namedtuple, defaultdict, Counter
```

---

## namedtuple - Tuples avec des Noms

### Problème avec les tuples classiques

Imaginons que vous représentez un point 2D avec un tuple :

```python
point = (10, 20)  
x = point[0]  
y = point[1]  
```

Le problème ? Ce n'est pas très explicite. Quelqu'un qui lit votre code doit deviner que `point[0]` est le x et `point[1]` est le y. De plus, c'est facile de se tromper avec les indices.

### Solution : namedtuple

Un `namedtuple` est un tuple où chaque élément a un nom. C'est comme un objet léger qui combine les avantages des tuples (immuabilité, rapidité) avec la lisibilité des classes.

```python
from collections import namedtuple

# Créer un type Point
Point = namedtuple('Point', ['x', 'y'])

# Créer une instance
point = Point(10, 20)

# Accéder aux valeurs par nom (beaucoup plus lisible !)
print(point.x)  # 10  
print(point.y)  # 20  

# On peut aussi utiliser les indices (comme un tuple normal)
print(point[0])  # 10  
print(point[1])  # 20  
```

### Créer un namedtuple

Il existe plusieurs façons de définir les champs :

```python
from collections import namedtuple

# Méthode 1 : liste de champs
Personne = namedtuple('Personne', ['nom', 'age', 'ville'])

# Méthode 2 : chaîne de caractères avec espaces
Personne = namedtuple('Personne', 'nom age ville')

# Méthode 3 : chaîne avec virgules
Personne = namedtuple('Personne', 'nom, age, ville')

# Créer une instance
alice = Personne('Alice', 25, 'Paris')  
print(alice.nom)   # Alice  
print(alice.age)   # 25  
print(alice.ville) # Paris  
```

### Caractéristiques des namedtuple

**1. Immuabilité**

Comme les tuples, les namedtuples sont immuables : on ne peut pas modifier leurs valeurs après création.

```python
Point = namedtuple('Point', ['x', 'y'])  
point = Point(10, 20)  

# Ceci provoque une erreur
# point.x = 15  # AttributeError: can't set attribute
```

**2. Déballage (unpacking)**

```python
Personne = namedtuple('Personne', 'nom age ville')  
alice = Personne('Alice', 25, 'Paris')  

# Unpacking classique
nom, age, ville = alice  
print(nom)  # Alice  

# Unpacking dans une boucle
personnes = [
    Personne('Alice', 25, 'Paris'),
    Personne('Bob', 30, 'Lyon')
]

for nom, age, ville in personnes:
    print(f"{nom} a {age} ans et habite à {ville}")
```

**3. Conversion en dictionnaire**

```python
Personne = namedtuple('Personne', 'nom age ville')  
alice = Personne('Alice', 25, 'Paris')  

# Convertir en dictionnaire
alice_dict = alice._asdict()  
print(alice_dict)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}  
print(type(alice_dict))  # <class 'dict'>  
```

**4. Créer une copie avec modifications**

Bien que les namedtuples soient immuables, vous pouvez créer une nouvelle instance avec certains champs modifiés :

```python
Personne = namedtuple('Personne', 'nom age ville')  
alice = Personne('Alice', 25, 'Paris')  

# Créer une copie avec un champ modifié
alice_plus_vieille = alice._replace(age=26)  
print(alice)              # Personne(nom='Alice', age=25, ville='Paris')  
print(alice_plus_vieille) # Personne(nom='Alice', age=26, ville='Paris')  
```

**5. Valeurs par défaut**

Vous pouvez définir des valeurs par défaut pour certains champs :

```python
Personne = namedtuple('Personne', 'nom age ville', defaults=['Inconnu'])
# Le dernier champ (ville) aura 'Inconnu' par défaut

alice = Personne('Alice', 25)  
print(alice)  # Personne(nom='Alice', age=25, ville='Inconnu')  

bob = Personne('Bob', 30, 'Lyon')  
print(bob)    # Personne(nom='Bob', age=30, ville='Lyon')  
```

### Cas d'usage pratiques

**Exemple 1 : Représenter des coordonnées**

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# Créer plusieurs points
p1 = Point(0, 0)  
p2 = Point(10, 5)  
p3 = Point(3, 8)  

# Calculer la distance entre deux points
def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

print(distance(p1, p2))  # 11.180339887498949

# Beaucoup plus lisible que point[0] et point[1] !
```

**Exemple 2 : Gérer des enregistrements**

```python
from collections import namedtuple

# Définir la structure d'un employé
Employe = namedtuple('Employe', 'nom poste salaire anciennete')

# Créer une base de données d'employés
employes = [
    Employe('Alice', 'Développeuse', 50000, 3),
    Employe('Bob', 'Designer', 45000, 2),
    Employe('Charlie', 'Manager', 60000, 5)
]

# Calculer le salaire moyen
salaire_moyen = sum(e.salaire for e in employes) / len(employes)  
print(f"Salaire moyen : {salaire_moyen}€")  

# Trouver les employés avec plus de 2 ans d'ancienneté
veterants = [e for e in employes if e.anciennete > 2]  
for emp in veterants:  
    print(f"{emp.nom} - {emp.anciennete} ans")
```

**Exemple 3 : Configuration d'application**

```python
from collections import namedtuple

# Configuration avec valeurs par défaut
Config = namedtuple('Config', 'host port debug timeout',
                    defaults=['localhost', 8000, False, 30])

# Utiliser les valeurs par défaut
config_dev = Config()  
print(config_dev)  # Config(host='localhost', port=8000, debug=False, timeout=30)  

# Personnaliser certaines valeurs
config_prod = Config(host='api.example.com', port=443, debug=False)  
print(config_prod)  # Config(host='api.example.com', port=443, debug=False, timeout=30)  
```

**Exemple 4 : Résultats de fonction**

Au lieu de retourner plusieurs valeurs dans un tuple anonyme, utilisez un namedtuple :

```python
from collections import namedtuple

Stats = namedtuple('Stats', 'moyenne mediane ecart_type')

def calculer_statistiques(nombres):
    moyenne = sum(nombres) / len(nombres)
    mediane = sorted(nombres)[len(nombres) // 2]
    # Calcul simplifié de l'écart-type
    ecart_type = (sum((x - moyenne)**2 for x in nombres) / len(nombres))**0.5

    return Stats(moyenne, mediane, ecart_type)

# Utilisation
donnees = [10, 20, 30, 40, 50]  
resultats = calculer_statistiques(donnees)  

print(f"Moyenne : {resultats.moyenne}")  
print(f"Médiane : {resultats.mediane}")  
print(f"Écart-type : {resultats.ecart_type}")  

# Beaucoup plus clair que :
# moyenne, mediane, ecart_type = calculer_statistiques(donnees)
```

### Comparaison : Tuple vs namedtuple vs Classe

```python
# 1. Tuple classique (peu lisible)
personne_tuple = ('Alice', 25, 'Paris')  
nom = personne_tuple[0]  # Indices magiques !  

# 2. namedtuple (lisible et léger)
from collections import namedtuple  
Personne = namedtuple('Personne', 'nom age ville')  
personne_named = Personne('Alice', 25, 'Paris')  
nom = personne_named.nom  # Beaucoup plus clair !  

# 3. Classe (plus de fonctionnalités mais plus verbeux)
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

personne_classe = Personne('Alice', 25, 'Paris')  
nom = personne_classe.nom  
```

**Utilisez namedtuple quand :**
- Vous avez besoin d'une structure de données simple et immuable
- Vous voulez plus de lisibilité qu'un tuple classique
- Vous n'avez pas besoin de méthodes personnalisées
- Vous voulez économiser de la mémoire par rapport à une classe complète

---

## defaultdict - Dictionnaires avec Valeurs par Défaut

### Problème avec les dictionnaires classiques

Avec un dictionnaire normal, accéder à une clé inexistante provoque une erreur :

```python
compteur = {}

# Compter les occurrences de lettres
texte = "hello"  
for lettre in texte:  
    # Ceci provoque une KeyError à la première itération !
    # compteur[lettre] = compteur[lettre] + 1

    # Solution avec dictionnaire classique : vérifier à chaque fois
    if lettre in compteur:
        compteur[lettre] += 1
    else:
        compteur[lettre] = 1

print(compteur)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

C'est fastidieux de toujours vérifier si la clé existe !

### Solution : defaultdict

Un `defaultdict` est un dictionnaire qui crée automatiquement une valeur par défaut pour les clés inexistantes.

```python
from collections import defaultdict

# Créer un defaultdict avec des valeurs par défaut à 0
compteur = defaultdict(int)  # int() retourne 0

texte = "hello"  
for lettre in texte:  
    compteur[lettre] += 1  # Pas besoin de vérifier si la clé existe !

print(compteur)  # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})  
print(dict(compteur))  # Convertir en dict normal : {'h': 1, 'e': 1, 'l': 2, 'o': 1}  
```

### Comment fonctionne defaultdict ?

Vous passez une **fonction** (appelée "factory") qui sera appelée pour créer la valeur par défaut :

```python
from collections import defaultdict

# int() retourne 0
dd_int = defaultdict(int)  
print(dd_int['cle_inexistante'])  # 0  

# list() retourne []
dd_list = defaultdict(list)  
print(dd_list['cle_inexistante'])  # []  

# set() retourne set()
dd_set = defaultdict(set)  
print(dd_set['cle_inexistante'])  # set()  

# str() retourne ''
dd_str = defaultdict(str)  
print(dd_str['cle_inexistante'])  # ''  

# Fonction personnalisée
def valeur_par_defaut():
    return "N/A"

dd_custom = defaultdict(valeur_par_defaut)  
print(dd_custom['cle_inexistante'])  # 'N/A'  
```

### Valeurs par défaut courantes

**1. defaultdict(int) - pour compter**

```python
from collections import defaultdict

# Compter les occurrences de mots
texte = "le chat et le chien jouent avec le chat"  
mots = texte.split()  

compteur = defaultdict(int)  
for mot in mots:  
    compteur[mot] += 1

print(dict(compteur))
# {'le': 3, 'chat': 2, 'et': 1, 'chien': 1, 'jouent': 1, 'avec': 1}
```

**2. defaultdict(list) - pour grouper**

```python
from collections import defaultdict

# Grouper des étudiants par classe
etudiants = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('David', 'C'),
    ('Eve', 'B')
]

classes = defaultdict(list)  
for nom, classe in etudiants:  
    classes[classe].append(nom)

print(dict(classes))
# {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Eve'], 'C': ['David']}
```

**3. defaultdict(set) - pour des collections uniques**

```python
from collections import defaultdict

# Associer des tags uniques à des articles
articles = [
    ('Article 1', 'python'),
    ('Article 1', 'programmation'),
    ('Article 2', 'python'),
    ('Article 2', 'data'),
    ('Article 1', 'python')  # doublon
]

tags_par_article = defaultdict(set)  
for article, tag in articles:  
    tags_par_article[article].add(tag)

print(dict(tags_par_article))
# {'Article 1': {'python', 'programmation'}, 'Article 2': {'python', 'data'}}
```

**4. defaultdict(dict) - pour des structures imbriquées**

```python
from collections import defaultdict

# Créer une matrice creuse (sparse matrix)
matrice = defaultdict(dict)

# Ajouter des valeurs
matrice[0][0] = 1  
matrice[2][5] = 7  
matrice[100][200] = 42  

print(matrice[0][0])    # 1  
print(matrice[2][5])    # 7  
print(matrice[50])      # {} (dictionnaire vide par défaut)  
# Attention : matrice[50][50] lèverait un KeyError (le sous-dict est vide)
```

### Cas d'usage pratiques

**Exemple 1 : Construire un index inversé**

```python
from collections import defaultdict

# Documents et leurs mots
documents = {
    'doc1': 'python est un langage de programmation',
    'doc2': 'python est facile à apprendre',
    'doc3': 'java est aussi un langage'
}

# Créer un index : mot -> liste de documents
index = defaultdict(list)

for doc_id, contenu in documents.items():
    for mot in contenu.split():
        index[mot].append(doc_id)

print(dict(index))
# {'python': ['doc1', 'doc2'], 'est': ['doc1', 'doc2', 'doc3'], ...}

# Rechercher un mot
print(f"Le mot 'python' apparaît dans : {index['python']}")
```

**Exemple 2 : Graphe (liste d'adjacence)**

```python
from collections import defaultdict

# Représenter un graphe
graphe = defaultdict(list)

# Ajouter des arêtes
graphe['A'].append('B')  
graphe['A'].append('C')  
graphe['B'].append('C')  
graphe['C'].append('D')  

print(dict(graphe))
# {'A': ['B', 'C'], 'B': ['C'], 'C': ['D']}

# Parcourir le graphe
def parcourir(graphe, depart):
    print(f"Depuis {depart}, on peut aller vers : {graphe[depart]}")

parcourir(graphe, 'A')  # Depuis A, on peut aller vers : ['B', 'C']  
parcourir(graphe, 'Z')  # Depuis Z, on peut aller vers : [] (pas d'erreur !)  
```

**Exemple 3 : Compteur de fréquence avec seuil**

```python
from collections import defaultdict

# Compter les visites par utilisateur
visites = ['alice', 'bob', 'alice', 'charlie', 'alice', 'bob', 'alice']

compteur = defaultdict(int)  
for utilisateur in visites:  
    compteur[utilisateur] += 1

# Filtrer les utilisateurs actifs (plus de 2 visites)
actifs = {user: count for user, count in compteur.items() if count > 2}  
print(actifs)  # {'alice': 4}  
```

**Exemple 4 : Regroupement multi-niveaux**

```python
from collections import defaultdict

# Ventes par région et par produit
ventes = [
    ('Nord', 'Laptop', 1000),
    ('Sud', 'Souris', 20),
    ('Nord', 'Clavier', 50),
    ('Sud', 'Laptop', 1000),
    ('Nord', 'Laptop', 1000)
]

# Grouper : région -> produit -> liste de montants
ventes_groupees = defaultdict(lambda: defaultdict(list))

for region, produit, montant in ventes:
    ventes_groupees[region][produit].append(montant)

# Afficher
for region, produits in ventes_groupees.items():
    print(f"\n{region}:")
    for produit, montants in produits.items():
        print(f"  {produit}: {sum(montants)}€ ({len(montants)} ventes)")

# Nord:
#   Laptop: 2000€ (2 ventes)
#   Clavier: 50€ (1 vente)
# Sud:
#   Souris: 20€ (1 vente)
#   Laptop: 1000€ (1 vente)
```

### Convertir en dictionnaire normal

```python
from collections import defaultdict

dd = defaultdict(int)  
dd['a'] = 1  
dd['b'] = 2  

# Convertir en dict normal
normal_dict = dict(dd)  
print(normal_dict)  # {'a': 1, 'b': 2}  
print(type(normal_dict))  # <class 'dict'>  
```

---

## Counter - Compter des Éléments

### Le problème du comptage manuel

Compter des éléments est une tâche courante en programmation :

```python
# Méthode manuelle
mots = ['pomme', 'banane', 'pomme', 'orange', 'banane', 'pomme']

compteur = {}  
for mot in mots:  
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

print(compteur)  # {'pomme': 3, 'banane': 2, 'orange': 1}
```

### Solution : Counter

`Counter` est un dictionnaire spécialisé conçu pour compter des éléments. Il rend le comptage trivial et offre des méthodes utiles.

```python
from collections import Counter

mots = ['pomme', 'banane', 'pomme', 'orange', 'banane', 'pomme']

# Créer un Counter
compteur = Counter(mots)

print(compteur)  # Counter({'pomme': 3, 'banane': 2, 'orange': 1})  
print(compteur['pomme'])   # 3  
print(compteur['kiwi'])    # 0 (pas d'erreur si la clé n'existe pas !)  
```

### Créer un Counter

Il existe plusieurs façons de créer un Counter :

```python
from collections import Counter

# 1. À partir d'une liste
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])  
print(c1)  # Counter({'a': 3, 'b': 2, 'c': 1})  

# 2. À partir d'une chaîne de caractères
c2 = Counter("hello world")  
print(c2)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})  

# 3. À partir d'un dictionnaire
c3 = Counter({'rouge': 4, 'bleu': 2})  
print(c3)  # Counter({'rouge': 4, 'bleu': 2})  

# 4. Avec des arguments nommés
c4 = Counter(chats=4, chiens=2, oiseaux=1)  
print(c4)  # Counter({'chats': 4, 'chiens': 2, 'oiseaux': 1})  

# 5. Counter vide
c5 = Counter()  
print(c5)  # Counter()  
```

### Méthodes utiles de Counter

**1. most_common() - éléments les plus fréquents**

```python
from collections import Counter

mots = ['python', 'java', 'python', 'c++', 'python', 'java', 'ruby']  
compteur = Counter(mots)  

# Obtenir les éléments les plus fréquents
print(compteur.most_common())    # [('python', 3), ('java', 2), ('c++', 1), ('ruby', 1)]  
print(compteur.most_common(2))   # [('python', 3), ('java', 2)] (top 2)  
print(compteur.most_common(1))   # [('python', 3)] (le plus fréquent)  
```

**2. elements() - itérer sur les éléments**

```python
from collections import Counter

c = Counter(a=3, b=2, c=1)

# Générer tous les éléments (répétés selon leur compte)
print(list(c.elements()))  # ['a', 'a', 'a', 'b', 'b', 'c']

# Utile pour reconstruire la liste originale
mots_originaux = list(c.elements())
```

**3. update() - ajouter des comptages**

```python
from collections import Counter

c = Counter(['a', 'b', 'c'])  
print(c)  # Counter({'a': 1, 'b': 1, 'c': 1})  

# Ajouter d'autres éléments
c.update(['a', 'b', 'd'])  
print(c)  # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})  

# Update avec un autre Counter
c2 = Counter(['a', 'e'])  
c.update(c2)  
print(c)  # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1, 'e': 1})  
```

**4. subtract() - soustraire des comptages**

```python
from collections import Counter

c1 = Counter(a=4, b=3, c=2)  
c2 = Counter(a=1, b=2, d=1)  

c1.subtract(c2)  
print(c1)  # Counter({'a': 3, 'b': 1, 'c': 2, 'd': -1})  
# Notez que les valeurs peuvent être négatives !
```

**5. Opérations arithmétiques**

```python
from collections import Counter

c1 = Counter(a=3, b=1)  
c2 = Counter(a=1, b=2, c=1)  

# Addition
print(c1 + c2)  # Counter({'a': 4, 'b': 3, 'c': 1})

# Soustraction (garde seulement les valeurs positives)
print(c1 - c2)  # Counter({'a': 2})

# Intersection (minimum)
print(c1 & c2)  # Counter({'a': 1, 'b': 1})

# Union (maximum)
print(c1 | c2)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

### Cas d'usage pratiques

**Exemple 1 : Analyser un texte**

```python
from collections import Counter

texte = """  
Python est un langage de programmation interprété, multi-paradigme et multiplateformes.  
Il favorise la programmation impérative structurée, fonctionnelle et orientée objet.  
"""

# Compter les mots
mots = texte.lower().split()  
compteur_mots = Counter(mots)  

print(f"Nombre total de mots : {sum(compteur_mots.values())}")  
print(f"Nombre de mots uniques : {len(compteur_mots)}")  
print(f"\nTop 5 des mots les plus fréquents :")  
for mot, freq in compteur_mots.most_common(5):  
    print(f"  {mot}: {freq}")

# Compter les lettres
lettres = Counter(texte.lower())  
lettres_alphabet = {c: count for c, count in lettres.items() if c.isalpha()}  
print(f"\nLettre la plus fréquente : {Counter(lettres_alphabet).most_common(1)}")  
```

**Exemple 2 : Statistiques sur des votes**

```python
from collections import Counter

# Votes pour des candidats
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob',
         'Alice', 'Charlie', 'Alice', 'Bob', 'Alice']

resultats = Counter(votes)

print("Résultats des élections :")  
for candidat, nb_votes in resultats.most_common():  
    pourcentage = (nb_votes / len(votes)) * 100
    print(f"{candidat}: {nb_votes} votes ({pourcentage:.1f}%)")

# Résultats des élections :
# Alice: 6 votes (54.5%)
# Bob: 3 votes (27.3%)
# Charlie: 2 votes (18.2%)

gagnant = resultats.most_common(1)[0][0]  
print(f"\nGagnant : {gagnant}")  
```

**Exemple 3 : Inventaire et gestion de stock**

```python
from collections import Counter

# Stock initial
stock = Counter(pommes=50, bananes=30, oranges=40)

# Ventes
ventes = Counter(pommes=10, bananes=5, oranges=15)

# Mettre à jour le stock
stock_restant = stock - ventes  
print("Stock restant :", stock_restant)  
# Counter({'pommes': 40, 'oranges': 25, 'bananes': 25})

# Nouvelle livraison
livraison = Counter(pommes=20, bananes=15, kiwis=10)  
stock_final = stock_restant + livraison  
print("Stock final :", stock_final)  
# Counter({'pommes': 60, 'bananes': 40, 'oranges': 25, 'kiwis': 10})

# Produits en rupture de stock
print("\nProduits avec moins de 30 unités :")  
for produit, quantite in stock_final.items():  
    if quantite < 30:
        print(f"  {produit}: {quantite}")
```

**Exemple 4 : Comparaison de documents**

```python
from collections import Counter

doc1 = "python est un langage de programmation"  
doc2 = "java est un langage de programmation orientée objet"  

# Créer des Counters pour chaque document
mots_doc1 = Counter(doc1.split())  
mots_doc2 = Counter(doc2.split())  

# Mots communs
mots_communs = mots_doc1 & mots_doc2  
print("Mots en commun :", dict(mots_communs))  
# {'est': 1, 'un': 1, 'langage': 1, 'de': 1, 'programmation': 1}

# Mots uniquement dans doc1
mots_uniques_doc1 = mots_doc1 - mots_doc2  
print("Mots uniques à doc1 :", dict(mots_uniques_doc1))  
# {'python': 1}

# Mots uniquement dans doc2
mots_uniques_doc2 = mots_doc2 - mots_doc1  
print("Mots uniques à doc2 :", dict(mots_uniques_doc2))  
# {'java': 1, 'orientée': 1, 'objet': 1}

# Tous les mots (union)
tous_mots = mots_doc1 | mots_doc2  
print("Nombre total de mots uniques :", len(tous_mots))  
```

**Exemple 5 : Analyse de logs**

```python
from collections import Counter

# Logs d'accès à un serveur
logs = [
    '200', '200', '404', '200', '500',
    '200', '404', '200', '200', '403'
]

# Compter les codes de statut
codes_statut = Counter(logs)

print("Statistiques du serveur :")  
for code, count in sorted(codes_statut.items()):  
    print(f"  Code {code}: {count} occurrences")

# Vérifier si on a des erreurs
erreurs = {code: count for code, count in codes_statut.items()
           if int(code) >= 400}
if erreurs:
    print(f"\n⚠️ Erreurs détectées : {sum(erreurs.values())} au total")
    for code, count in erreurs.items():
        print(f"  Code {code}: {count}")
```

### Manipuler les comptages

```python
from collections import Counter

c = Counter(a=3, b=2, c=0, d=-1)

# Supprimer les éléments avec compte zéro ou négatif
# Méthode 1 : utiliser +Counter() (unary plus)
c_positifs = +c  
print(c_positifs)  # Counter({'a': 3, 'b': 2})  

# Méthode 2 : filtrer manuellement
c_positifs = Counter({k: v for k, v in c.items() if v > 0})  
print(c_positifs)  # Counter({'a': 3, 'b': 2})  

# Obtenir le total de tous les comptages
total = sum(c.values())  
print(total)  # 4 (3 + 2 + 0 + (-1))  

# Réinitialiser
c.clear()  
print(c)  # Counter()  
```

---

## Autres Collections Utiles (Aperçu Rapide)

### deque - File double (Double-Ended Queue)

Une `deque` permet d'ajouter et retirer des éléments efficacement aux deux extrémités.

```python
from collections import deque

# Créer une deque
d = deque([1, 2, 3])

# Ajouter à droite et à gauche
d.append(4)      # [1, 2, 3, 4]  
d.appendleft(0)  # [0, 1, 2, 3, 4]  

# Retirer à droite et à gauche
d.pop()          # Retire 4, reste [0, 1, 2, 3]  
d.popleft()      # Retire 0, reste [1, 2, 3]  

print(d)  # deque([1, 2, 3])

# Rotation
d.rotate(1)   # Rotation à droite : deque([3, 1, 2])  
d.rotate(-1)  # Rotation à gauche : deque([1, 2, 3])  
```

**Utilisation :** Files d'attente, historique d'annulation/rétablissement, caches LRU.

### OrderedDict - Dictionnaire Ordonné

Depuis Python 3.7, les dictionnaires normaux conservent l'ordre d'insertion, donc `OrderedDict` est moins nécessaire. Mais il offre quelques méthodes supplémentaires.

```python
from collections import OrderedDict

# OrderedDict conserve l'ordre d'insertion (comme dict depuis Python 3.7)
od = OrderedDict()  
od['b'] = 2  
od['a'] = 1  
od['c'] = 3  

print(od)  # OrderedDict([('b', 2), ('a', 1), ('c', 3)])

# Méthode spéciale : move_to_end
od.move_to_end('a')  
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])  
```

### ChainMap - Chaîner plusieurs dictionnaires

`ChainMap` groupe plusieurs dictionnaires en une seule vue.

```python
from collections import ChainMap

# Dictionnaires de configuration
config_defaut = {'couleur': 'bleu', 'taille': 'M'}  
config_utilisateur = {'couleur': 'rouge'}  

# Combiner avec priorité (config_utilisateur > config_defaut)
config = ChainMap(config_utilisateur, config_defaut)

print(config['couleur'])  # 'rouge' (de config_utilisateur)  
print(config['taille'])   # 'M' (de config_defaut)  
print(dict(config))       # {'couleur': 'rouge', 'taille': 'M'}  
```

**Utilisation :** Gestion de configurations avec plusieurs niveaux (défaut, utilisateur, environnement).

---

## Tableau Comparatif

| Collection | But principal | Avantage clé | Cas d'usage |
|------------|---------------|--------------|-------------|
| **namedtuple** | Tuple avec champs nommés | Lisibilité + Immuabilité | Structures de données simples, coordonnées |
| **defaultdict** | Dict avec valeur par défaut | Évite les KeyError | Comptage, regroupement, graphes |
| **Counter** | Compter des éléments | Méthodes de comptage | Statistiques, fréquences, votes |
| **deque** | File double | Ajout/retrait rapide aux extrémités | Files d'attente, historique |
| **OrderedDict** | Dict ordonné | Méthodes spécifiques d'ordre | Moins utile depuis Python 3.7 |
| **ChainMap** | Chaîner des dicts | Recherche en cascade | Configurations multi-niveaux |

---

## Quand Utiliser Quoi ?

### Utilisez **namedtuple** quand :
- ✅ Vous avez des tuples avec plusieurs éléments
- ✅ Vous voulez accéder aux éléments par nom plutôt que par index
- ✅ Vous n'avez pas besoin de modifier les valeurs après création
- ✅ Vous voulez une alternative légère aux classes

### Utilisez **defaultdict** quand :
- ✅ Vous construisez un dictionnaire progressivement
- ✅ Vous voulez éviter de vérifier si une clé existe avant d'y accéder
- ✅ Vous groupez des éléments par catégorie
- ✅ Vous comptez des occurrences (bien que Counter soit souvent meilleur pour ça)

### Utilisez **Counter** quand :
- ✅ Vous comptez la fréquence d'éléments
- ✅ Vous cherchez les éléments les plus ou moins fréquents
- ✅ Vous faites des opérations sur des ensembles d'éléments comptés
- ✅ Vous analysez des statistiques ou des distributions

---

## Exemples Combinés

Voyons comment ces collections peuvent travailler ensemble.

**Exemple 1 : Analyse de ventes**

```python
from collections import namedtuple, defaultdict, Counter

# Définir une structure pour les ventes
Vente = namedtuple('Vente', 'produit region montant')

# Données de ventes
ventes = [
    Vente('Laptop', 'Nord', 1000),
    Vente('Souris', 'Sud', 20),
    Vente('Laptop', 'Nord', 1000),
    Vente('Clavier', 'Est', 50),
    Vente('Souris', 'Nord', 20),
    Vente('Laptop', 'Sud', 1000)
]

# 1. Compter les ventes par produit avec Counter
ventes_par_produit = Counter(v.produit for v in ventes)  
print("Nombre de ventes par produit :")  
for produit, count in ventes_par_produit.most_common():  
    print(f"  {produit}: {count}")

# 2. Grouper les montants par région avec defaultdict
montants_par_region = defaultdict(list)  
for vente in ventes:  
    montants_par_region[vente.region].append(vente.montant)

print("\nChiffre d'affaires par région :")  
for region, montants in montants_par_region.items():  
    print(f"  {region}: {sum(montants)}€")

# 3. Produit le plus vendu par région
for region in montants_par_region:
    produits_region = [v.produit for v in ventes if v.region == region]
    top_produit = Counter(produits_region).most_common(1)[0]
    print(f"  Meilleur produit en {region} : {top_produit[0]}")
```

**Exemple 2 : Analyse de réseau social**

```python
from collections import namedtuple, defaultdict, Counter

# Définir une interaction
Interaction = namedtuple('Interaction', 'utilisateur action cible')

# Journal d'interactions
interactions = [
    Interaction('Alice', 'like', 'post1'),
    Interaction('Bob', 'comment', 'post1'),
    Interaction('Alice', 'like', 'post2'),
    Interaction('Charlie', 'share', 'post1'),
    Interaction('Alice', 'comment', 'post1'),
    Interaction('Bob', 'like', 'post1')
]

# Compter les actions par utilisateur
actions_par_user = defaultdict(Counter)  
for inter in interactions:  
    actions_par_user[inter.utilisateur][inter.action] += 1

print("Actions par utilisateur :")  
for user, actions in actions_par_user.items():  
    print(f"\n{user}:")
    for action, count in actions.items():
        print(f"  {action}: {count}")

# Post le plus populaire
popularite_posts = Counter(i.cible for i in interactions)  
post_populaire = popularite_posts.most_common(1)[0]  
print(f"\nPost le plus populaire : {post_populaire[0]} ({post_populaire[1]} interactions)")  
```

---

## Conclusion

Les collections spécialisées du module `collections` sont des outils puissants qui rendent votre code plus élégant, lisible et performant.

**Points clés à retenir :**

1. **namedtuple** : Créez des structures de données simples et expressives sans la lourdeur d'une classe complète.

2. **defaultdict** : Simplifiez la construction de dictionnaires en évitant les vérifications répétitives de clés.

3. **Counter** : Comptez facilement des éléments et effectuez des analyses de fréquence.

4. **Autres collections** : `deque`, `OrderedDict`, et `ChainMap` résolvent des problèmes spécifiques.

**Conseil final :** N'utilisez pas ces structures par habitude, mais choisissez-les quand elles rendent vraiment votre code plus clair. Un dictionnaire ou une liste normale peut suffire dans de nombreux cas ! La clarté du code est toujours la priorité.

Avec la pratique, vous développerez une intuition pour savoir quand utiliser chaque collection. Ces outils deviendront des réflexes naturels dans votre boîte à outils Python ! 🐍

⏭️ [Manipulation de chaînes de caractères et expressions régulières](/02-structures-de-donnees/04-chaines-et-regex.md)
