🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.3 Méthodes Spéciales (Dunder Methods)

## Introduction aux Méthodes Spéciales

Les **méthodes spéciales** (ou **magic methods** en anglais) sont des méthodes dont le nom est entouré de **doubles underscores** (dunders). Par exemple : `__init__`, `__str__`, `__add__`, etc.

Ces méthodes permettent de personnaliser le comportement de vos objets et de les intégrer naturellement avec les opérateurs et fonctions Python standard.

### Pourquoi "Dunder" ?

Le terme "dunder" vient de "**d**ouble **under**score". Au lieu de dire "underscore underscore init underscore underscore", on dit simplement "dunder init".

```python
__init__   # Se prononce "dunder init"
__str__    # Se prononce "dunder str"
__add__    # Se prononce "dunder add"
```

### Pourquoi Sont-Elles Utiles ?

Les méthodes spéciales permettent à vos objets de :
- Se comporter comme des types natifs Python
- Fonctionner avec les opérateurs (`+`, `-`, `*`, `==`, etc.)
- Être utilisés avec les fonctions built-in (`len()`, `str()`, `print()`, etc.)
- Avoir une représentation textuelle claire
- Être comparables, triables, itérables, etc.

## `__init__` : Le Constructeur

Vous connaissez déjà `__init__`, c'est la méthode spéciale la plus courante. Elle est appelée automatiquement lors de la création d'un objet.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

personne = Personne("Alice", 30)
# Python appelle automatiquement __init__
```

## `__str__` et `__repr__` : Représentation Textuelle

### `__str__` : Pour les Humains

La méthode `__str__` est appelée par la fonction `str()` et par `print()`. Elle doit retourner une chaîne de caractères **lisible** destinée aux utilisateurs.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, {self.age} ans"

personne = Personne("Alice", 30)  
print(personne)      # Appelle __str__  
# Affiche : Alice, 30 ans

print(str(personne)) # Appelle aussi __str__
# Affiche : Alice, 30 ans
```

**Sans `__str__`**, Python affiche quelque chose comme : `<__main__.Personne object at 0x7f8b3c4d5e10>`

**Avec `__str__`**, vous contrôlez ce qui est affiché !

### `__repr__` : Pour les Développeurs

La méthode `__repr__` est appelée par la fonction `repr()` et dans l'interpréteur interactif. Elle doit retourner une représentation **non ambiguë** de l'objet, idéalement du code Python valide qui pourrait recréer l'objet.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, {self.age} ans"

    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"

personne = Personne("Alice", 30)

print(str(personne))   # Alice, 30 ans  
print(repr(personne))  # Personne('Alice', 30)  

# Dans l'interpréteur interactif
# >>> personne
# Personne('Alice', 30)  # Utilise __repr__
```

**Différence clé** :
- `__str__` : pour l'utilisateur final (lisible, sympathique)
- `__repr__` : pour le développeur (précis, technique)

**Bonne pratique** : Si vous ne définissez qu'une seule des deux, définissez `__repr__`. Si `__str__` n'est pas défini, Python utilisera `__repr__` comme solution de repli.

### Exemple Complet

```python
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return f'"{self.titre}" de {self.auteur}'

    def __repr__(self):
        return f"Livre('{self.titre}', '{self.auteur}', {self.annee})"

livre = Livre("1984", "George Orwell", 1949)

print(livre)        # "1984" de George Orwell  
print(repr(livre))  # Livre('1984', 'George Orwell', 1949)  

# Créer une liste de livres
livres = [livre, Livre("Le Petit Prince", "Saint-Exupéry", 1943)]  
print(livres)  
# [Livre('1984', 'George Orwell', 1949), Livre('Le Petit Prince', 'Saint-Exupéry', 1943)]
```

## Méthodes pour les Opérateurs Arithmétiques

Les méthodes spéciales permettent de définir comment vos objets se comportent avec les opérateurs mathématiques.

### `__add__` : Opérateur `+`

```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        """Définit l'opération v1 + v2"""
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"

v1 = Vecteur(2, 3)  
v2 = Vecteur(1, 4)  
v3 = v1 + v2  # Appelle v1.__add__(v2)  

print(v3)  # Vecteur(3, 7)
```

Quand vous écrivez `v1 + v2`, Python appelle automatiquement `v1.__add__(v2)` !

### Autres Opérateurs Arithmétiques

```python
class Nombre:
    def __init__(self, valeur):
        self.valeur = valeur

    def __add__(self, autre):
        """Addition : self + autre"""
        return Nombre(self.valeur + autre.valeur)

    def __sub__(self, autre):
        """Soustraction : self - autre"""
        return Nombre(self.valeur - autre.valeur)

    def __mul__(self, autre):
        """Multiplication : self * autre"""
        return Nombre(self.valeur * autre.valeur)

    def __truediv__(self, autre):
        """Division : self / autre"""
        if autre.valeur == 0:
            raise ValueError("Division par zéro impossible")
        return Nombre(self.valeur / autre.valeur)

    def __str__(self):
        return str(self.valeur)

a = Nombre(10)  
b = Nombre(3)  

print(a + b)  # 13  
print(a - b)  # 7  
print(a * b)  # 30  
print(a / b)  # 3.3333...  
```

### Tableau des Opérateurs Arithmétiques

| Opérateur | Méthode | Exemple |
|-----------|---------|---------|
| `+` | `__add__(self, other)` | `a + b` |
| `-` | `__sub__(self, other)` | `a - b` |
| `*` | `__mul__(self, other)` | `a * b` |
| `/` | `__truediv__(self, other)` | `a / b` |
| `//` | `__floordiv__(self, other)` | `a // b` |
| `%` | `__mod__(self, other)` | `a % b` |
| `**` | `__pow__(self, other)` | `a ** b` |

### Exemple Pratique : Classe Argent

```python
class Argent:
    def __init__(self, montant, devise="EUR"):
        self.montant = montant
        self.devise = devise

    def __add__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Impossible d'additionner des devises différentes")
        return Argent(self.montant + autre.montant, self.devise)

    def __sub__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Impossible de soustraire des devises différentes")
        return Argent(self.montant - autre.montant, self.devise)

    def __mul__(self, facteur):
        """Permet de multiplier par un nombre : argent * 2"""
        return Argent(self.montant * facteur, self.devise)

    def __str__(self):
        return f"{self.montant:.2f} {self.devise}"

    def __repr__(self):
        return f"Argent({self.montant}, '{self.devise}')"

prix1 = Argent(50.00)  
prix2 = Argent(30.50)  

total = prix1 + prix2  
print(total)  # 80.50 EUR  

reduction = total - Argent(10)  
print(reduction)  # 70.50 EUR  

double = prix1 * 2  
print(double)  # 100.00 EUR  
```

## Méthodes de Comparaison

Ces méthodes permettent de comparer vos objets avec les opérateurs de comparaison.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, autre):
        """Égalité : self == autre"""
        return self.age == autre.age

    def __lt__(self, autre):
        """Inférieur à : self < autre"""
        return self.age < autre.age

    def __le__(self, autre):
        """Inférieur ou égal : self <= autre"""
        return self.age <= autre.age

    def __gt__(self, autre):
        """Supérieur à : self > autre"""
        return self.age > autre.age

    def __ge__(self, autre):
        """Supérieur ou égal : self >= autre"""
        return self.age >= autre.age

    def __ne__(self, autre):
        """Différent de : self != autre"""
        return self.age != autre.age

    def __str__(self):
        return f"{self.nom} ({self.age} ans)"

alice = Personne("Alice", 30)  
bob = Personne("Bob", 25)  
charlie = Personne("Charlie", 30)  

print(alice == charlie)  # True (même âge)  
print(alice == bob)      # False  
print(bob < alice)       # True (25 < 30)  
print(alice >= charlie)  # True (30 >= 30)  

# Trier une liste de personnes
personnes = [alice, bob, charlie]  
personnes_triees = sorted(personnes)  # Trie par âge grâce à __lt__  
for p in personnes_triees:  
    print(p)
```

**Résultat :**
```
True  
False  
True  
True  
Bob (25 ans)  
Alice (30 ans)  
Charlie (30 ans)  
```

### Tableau des Opérateurs de Comparaison

| Opérateur | Méthode | Exemple |
|-----------|---------|---------|
| `==` | `__eq__(self, other)` | `a == b` |
| `!=` | `__ne__(self, other)` | `a != b` |
| `<` | `__lt__(self, other)` | `a < b` |
| `<=` | `__le__(self, other)` | `a <= b` |
| `>` | `__gt__(self, other)` | `a > b` |
| `>=` | `__ge__(self, other)` | `a >= b` |

**Astuce** : Python peut déduire certaines comparaisons. Si vous définissez `__eq__` et `__lt__`, Python peut souvent déduire les autres. Vous pouvez utiliser le décorateur `@functools.total_ordering` pour cela.

## `__len__` : Longueur d'un Objet

La méthode `__len__` est appelée par la fonction `len()`.

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __len__(self):
        return len(self.chansons)

    def __str__(self):
        return f"Playlist '{self.nom}' avec {len(self)} chansons"

ma_playlist = Playlist("Mes favoris")  
ma_playlist.ajouter("Bohemian Rhapsody")  
ma_playlist.ajouter("Imagine")  
ma_playlist.ajouter("Hotel California")  

print(len(ma_playlist))  # 3  
print(ma_playlist)       # Playlist 'Mes favoris' avec 3 chansons  
```

## `__getitem__` et `__setitem__` : Indexation

Ces méthodes permettent d'utiliser la notation avec crochets `[]` sur vos objets.

### `__getitem__` : Lire un Élément

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __getitem__(self, index):
        """Permet d'accéder aux chansons avec playlist[index]"""
        return self.chansons[index]

    def __len__(self):
        return len(self.chansons)

playlist = Playlist("Rock")  
playlist.ajouter("Song 1")  
playlist.ajouter("Song 2")  
playlist.ajouter("Song 3")  

print(playlist[0])   # Song 1  
print(playlist[1])   # Song 2  
print(playlist[-1])  # Song 3 (dernier élément)  

# On peut même faire du slicing !
print(playlist[0:2])  # ['Song 1', 'Song 2']
```

### `__setitem__` : Modifier un Élément

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __getitem__(self, index):
        return self.chansons[index]

    def __setitem__(self, index, valeur):
        """Permet de modifier une chanson avec playlist[index] = nouvelle_chanson"""
        self.chansons[index] = valeur

    def __len__(self):
        return len(self.chansons)

playlist = Playlist("Rock")  
playlist.ajouter("Old Song")  

print(playlist[0])      # Old Song  
playlist[0] = "New Song"  # Utilise __setitem__  
print(playlist[0])      # New Song  
```

### `__delitem__` : Supprimer un Élément

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __getitem__(self, index):
        return self.chansons[index]

    def __setitem__(self, index, valeur):
        self.chansons[index] = valeur

    def __delitem__(self, index):
        """Permet de supprimer avec del playlist[index]"""
        del self.chansons[index]

    def __len__(self):
        return len(self.chansons)

playlist = Playlist("Rock")  
playlist.ajouter("Song 1")  
playlist.ajouter("Song 2")  
playlist.ajouter("Song 3")  

print(len(playlist))  # 3  
del playlist[1]       # Supprime "Song 2"  
print(len(playlist))  # 2  
```

## `__iter__` et `__next__` : Rendre un Objet Itérable

Ces méthodes permettent d'utiliser vos objets dans des boucles `for`.

```python
class Compte:
    def __init__(self):
        self.valeur = 0

    def __iter__(self):
        """Initialise l'itération"""
        self.valeur = 0
        return self

    def __next__(self):
        """Retourne le prochain élément"""
        if self.valeur >= 5:
            raise StopIteration  # Fin de l'itération
        self.valeur += 1
        return self.valeur

compteur = Compte()  
for nombre in compteur:  
    print(nombre)
```

**Résultat :**
```
1
2
3
4
5
```

### Exemple Plus Pratique : Itérer sur une Collection

```python
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def __iter__(self):
        """Retourne un itérateur sur les livres"""
        return iter(self.livres)

    def __len__(self):
        return len(self.livres)

biblio = Bibliotheque()  
biblio.ajouter_livre("1984")  
biblio.ajouter_livre("Le Petit Prince")  
biblio.ajouter_livre("Harry Potter")  

# On peut maintenant itérer directement sur la bibliothèque !
for livre in biblio:
    print(f"- {livre}")
```

**Résultat :**
```
- 1984
- Le Petit Prince
- Harry Potter
```

## `__contains__` : Opérateur `in`

Permet d'utiliser l'opérateur `in` pour vérifier si un élément est dans votre objet.

```python
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def __contains__(self, membre):
        """Permet d'utiliser 'membre in equipe'"""
        return membre in self.membres

    def __len__(self):
        return len(self.membres)

equipe = Equipe("Les Développeurs")  
equipe.ajouter_membre("Alice")  
equipe.ajouter_membre("Bob")  
equipe.ajouter_membre("Charlie")  

print("Alice" in equipe)    # True  
print("David" in equipe)    # False  
print("Bob" not in equipe)  # False  
```

## `__call__` : Rendre un Objet Appelable

Cette méthode permet d'utiliser votre objet comme une fonction.

```python
class Multiplicateur:
    def __init__(self, facteur):
        self.facteur = facteur

    def __call__(self, nombre):
        """Permet d'appeler l'objet comme une fonction"""
        return nombre * self.facteur

doubler = Multiplicateur(2)  
tripler = Multiplicateur(3)  

print(doubler(5))   # 10  (5 * 2)  
print(doubler(10))  # 20  (10 * 2)  
print(tripler(5))   # 15  (5 * 3)  
```

### Exemple Pratique : Compteur d'Appels

```python
class CompteurAppels:
    def __init__(self, fonction):
        self.fonction = fonction
        self.nombre_appels = 0

    def __call__(self, *args, **kwargs):
        self.nombre_appels += 1
        print(f"Appel n°{self.nombre_appels}")
        return self.fonction(*args, **kwargs)

@CompteurAppels
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Alice")  
saluer("Bob")  
saluer("Charlie")  

print(f"\nLa fonction a été appelée {saluer.nombre_appels} fois")
```

**Résultat :**
```
Appel n°1  
Bonjour Alice !  
Appel n°2  
Bonjour Bob !  
Appel n°3  
Bonjour Charlie !  

La fonction a été appelée 3 fois
```

## `__bool__` : Valeur de Vérité

Détermine si un objet est considéré comme `True` ou `False` dans un contexte booléen.

```python
class Panier:
    def __init__(self):
        self.articles = []

    def ajouter(self, article):
        self.articles.append(article)

    def __bool__(self):
        """Un panier est True s'il contient des articles"""
        return len(self.articles) > 0

    def __len__(self):
        return len(self.articles)

panier = Panier()

if panier:
    print("Le panier contient des articles")
else:
    print("Le panier est vide")
# Affiche : Le panier est vide

panier.ajouter("Pomme")

if panier:
    print("Le panier contient des articles")
else:
    print("Le panier est vide")
# Affiche : Le panier contient des articles
```

**Note** : Si `__bool__` n'est pas défini, Python utilise `__len__` (un objet est vrai si sa longueur est > 0).

## Gestionnaires de Contexte : `__enter__` et `__exit__`

Ces méthodes permettent d'utiliser vos objets avec l'instruction `with`.

```python
class FichierLog:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.fichier = None

    def __enter__(self):
        """Appelé au début du bloc 'with'"""
        print(f"Ouverture de {self.nom_fichier}")
        self.fichier = open(self.nom_fichier, 'w')
        return self.fichier

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Appelé à la fin du bloc 'with'"""
        print(f"Fermeture de {self.nom_fichier}")
        if self.fichier:
            self.fichier.close()
        return False  # Ne pas supprimer les exceptions

# Utilisation
with FichierLog("log.txt") as f:
    f.write("Début du programme\n")
    f.write("Traitement en cours...\n")
    f.write("Fin du programme\n")

# Le fichier est automatiquement fermé à la sortie du bloc with
```

### Exemple : Chronomètre de Code

```python
import time

class Chronometre:
    def __enter__(self):
        self.debut = time.time()
        print("Chronomètre démarré...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fin = time.time()
        duree = self.fin - self.debut
        print(f"Temps écoulé : {duree:.4f} secondes")
        return False

# Utilisation
with Chronometre():
    # Code à chronométrer
    total = sum(range(1000000))
    print(f"Somme calculée : {total}")
```

**Résultat :**
```
Chronomètre démarré...  
Somme calculée : 499999500000  
Temps écoulé : 0.0234 secondes  
```

## Exemple Complet : Classe Vecteur

Voici un exemple qui combine plusieurs méthodes spéciales :

```python
import math

class Vecteur:
    """Représente un vecteur 2D avec des opérations mathématiques."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Représentation
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

    # Opérations arithmétiques
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):
        return Vecteur(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire):
        """Multiplication par un scalaire"""
        return Vecteur(self.x * scalaire, self.y * scalaire)

    def __truediv__(self, scalaire):
        if scalaire == 0:
            raise ValueError("Division par zéro")
        return Vecteur(self.x / scalaire, self.y / scalaire)

    def __neg__(self):
        """Négation : -vecteur"""
        return Vecteur(-self.x, -self.y)

    # Comparaisons
    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

    def __ne__(self, autre):
        return not self.__eq__(autre)

    # Longueur
    def __abs__(self):
        """Norme du vecteur (distance à l'origine)"""
        return math.sqrt(self.x**2 + self.y**2)

    # Valeur booléenne
    def __bool__(self):
        """Un vecteur est True s'il n'est pas nul"""
        return self.x != 0 or self.y != 0

    # Accès par index
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index invalide (0 ou 1 uniquement)")

    def __setitem__(self, index, valeur):
        if index == 0:
            self.x = valeur
        elif index == 1:
            self.y = valeur
        else:
            raise IndexError("Index invalide (0 ou 1 uniquement)")

# Utilisation complète
v1 = Vecteur(3, 4)  
v2 = Vecteur(1, 2)  

print(f"v1 = {v1}")              # (3, 4)  
print(f"v2 = {v2}")              # (1, 2)  

# Opérations
v3 = v1 + v2  
print(f"v1 + v2 = {v3}")        # (4, 6)  

v4 = v1 - v2  
print(f"v1 - v2 = {v4}")        # (2, 2)  

v5 = v1 * 2  
print(f"v1 * 2 = {v5}")         # (6, 8)  

v6 = -v1  
print(f"-v1 = {v6}")            # (-3, -4)  

# Comparaison
print(f"v1 == v2 : {v1 == v2}") # False  
print(f"v1 != v2 : {v1 != v2}") # True  

# Longueur
print(f"|v1| = {abs(v1)}")      # 5.0

# Booléen
v_nul = Vecteur(0, 0)  
print(f"v1 est vrai : {bool(v1)}")      # True  
print(f"v_nul est vrai : {bool(v_nul)}") # False  

# Indexation
print(f"v1[0] = {v1[0]}")       # 3  
print(f"v1[1] = {v1[1]}")       # 4  
v1[0] = 10  
print(f"v1 après modification = {v1}")  # (10, 4)  
```

## Exemple Complet : Classe Fraction

Un autre exemple pratique qui illustre bien les méthodes spéciales :

```python
from math import gcd

class Fraction:
    """Représente une fraction avec simplification automatique."""

    def __init__(self, numerateur, denominateur):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro")

        # Simplifier la fraction
        pgcd = gcd(abs(numerateur), abs(denominateur))
        self.numerateur = numerateur // pgcd
        self.denominateur = denominateur // pgcd

        # Garder le signe au numérateur
        if self.denominateur < 0:
            self.numerateur = -self.numerateur
            self.denominateur = -self.denominateur

    def __str__(self):
        if self.denominateur == 1:
            return str(self.numerateur)
        return f"{self.numerateur}/{self.denominateur}"

    def __repr__(self):
        return f"Fraction({self.numerateur}, {self.denominateur})"

    def __add__(self, autre):
        num = self.numerateur * autre.denominateur + autre.numerateur * self.denominateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __sub__(self, autre):
        num = self.numerateur * autre.denominateur - autre.numerateur * self.denominateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __mul__(self, autre):
        num = self.numerateur * autre.numerateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __truediv__(self, autre):
        if autre.numerateur == 0:
            raise ValueError("Division par zéro")
        num = self.numerateur * autre.denominateur
        den = self.denominateur * autre.numerateur
        return Fraction(num, den)

    def __eq__(self, autre):
        return (self.numerateur == autre.numerateur and
                self.denominateur == autre.denominateur)

    def __lt__(self, autre):
        return (self.numerateur * autre.denominateur <
                autre.numerateur * self.denominateur)

    def __le__(self, autre):
        return self < autre or self == autre

    def __float__(self):
        return self.numerateur / self.denominateur

    def __int__(self):
        return self.numerateur // self.denominateur

# Utilisation
f1 = Fraction(1, 2)  
f2 = Fraction(1, 3)  

print(f"f1 = {f1}")                    # 1/2  
print(f"f2 = {f2}")                    # 1/3  

somme = f1 + f2  
print(f"f1 + f2 = {somme}")            # 5/6  

difference = f1 - f2  
print(f"f1 - f2 = {difference}")       # 1/6  

produit = f1 * f2  
print(f"f1 * f2 = {produit}")          # 1/6  

quotient = f1 / f2  
print(f"f1 / f2 = {quotient}")         # 3/2  

print(f"f1 < f2 : {f1 < f2}")          # False  
print(f"f1 > f2 : {f1 > f2}")          # True  

print(f"Valeur décimale de f1 : {float(f1)}")  # 0.5  
print(f"Partie entière de f1 : {int(f1)}")     # 0  

# Simplification automatique
f3 = Fraction(4, 8)  
print(f"4/8 simplifié = {f3}")         # 1/2  
```

## Récapitulatif des Principales Méthodes Spéciales

### Initialisation et Représentation

| Méthode | Utilisation | Appelée par |
|---------|-------------|-------------|
| `__init__(self, ...)` | Constructeur | `obj = Classe(...)` |
| `__str__(self)` | Représentation lisible | `str(obj)`, `print(obj)` |
| `__repr__(self)` | Représentation technique | `repr(obj)`, console interactive |

### Opérateurs Arithmétiques

| Méthode | Opérateur | Exemple |
|---------|-----------|---------|
| `__add__(self, other)` | `+` | `a + b` |
| `__sub__(self, other)` | `-` | `a - b` |
| `__mul__(self, other)` | `*` | `a * b` |
| `__truediv__(self, other)` | `/` | `a / b` |
| `__floordiv__(self, other)` | `//` | `a // b` |
| `__mod__(self, other)` | `%` | `a % b` |
| `__pow__(self, other)` | `**` | `a ** b` |
| `__neg__(self)` | `-` (unaire) | `-a` |

### Comparaisons

| Méthode | Opérateur | Exemple |
|---------|-----------|---------|
| `__eq__(self, other)` | `==` | `a == b` |
| `__ne__(self, other)` | `!=` | `a != b` |
| `__lt__(self, other)` | `<` | `a < b` |
| `__le__(self, other)` | `<=` | `a <= b` |
| `__gt__(self, other)` | `>` | `a > b` |
| `__ge__(self, other)` | `>=` | `a >= b` |

### Conteneurs

| Méthode | Utilisation | Exemple |
|---------|-------------|---------|
| `__len__(self)` | Longueur | `len(obj)` |
| `__getitem__(self, key)` | Accès | `obj[key]` |
| `__setitem__(self, key, value)` | Modification | `obj[key] = value` |
| `__delitem__(self, key)` | Suppression | `del obj[key]` |
| `__contains__(self, item)` | Appartenance | `item in obj` |

### Itération

| Méthode | Utilisation |
|---------|-------------|
| `__iter__(self)` | Retourne un itérateur |
| `__next__(self)` | Élément suivant |

### Autres

| Méthode | Utilisation | Exemple |
|---------|-------------|---------|
| `__call__(self, ...)` | Rend l'objet appelable | `obj(...)` |
| `__bool__(self)` | Valeur booléenne | `bool(obj)`, `if obj:` |
| `__hash__(self)` | Valeur de hachage | `hash(obj)`, dictionnaires, sets |
| `__enter__(self)` | Début de contexte | `with obj:` |
| `__exit__(self, ...)` | Fin de contexte | fin du `with` |

## Bonnes Pratiques

### 1. Ne Pas Abuser des Méthodes Spéciales

Les méthodes spéciales sont puissantes, mais n'en ajoutez que si cela a du sens pour votre classe.

```python
# ✗ Mauvais - Ajouter des personnes n'a pas de sens mathématique
class Personne:
    def __add__(self, autre):
        # Que signifie "personne1 + personne2" ?
        pass

# ✓ Bon - Addition de vecteurs a du sens
class Vecteur:
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)
```

### 2. Respecter les Conventions

Si vous implémentez une méthode spéciale, faites-le correctement :
- `__str__` doit retourner une chaîne lisible
- `__repr__` devrait idéalement retourner du code Python valide
- `__len__` doit retourner un entier >= 0
- `__bool__` doit retourner True ou False

### 3. Documenter les Comportements

```python
class MonObjet:
    def __add__(self, autre):
        """
        Addition de deux objets MonObjet.

        Args:
            autre (MonObjet): L'autre objet à additionner

        Returns:
            MonObjet: Un nouvel objet représentant la somme

        Example:
            >>> obj1 = MonObjet(5)
            >>> obj2 = MonObjet(3)
            >>> obj3 = obj1 + obj2
            >>> print(obj3.valeur)
            8
        """
        return MonObjet(self.valeur + autre.valeur)
```

### 4. Gérer les Cas d'Erreur

```python
class Fraction:
    def __truediv__(self, autre):
        if autre.numerateur == 0:
            raise ValueError("Division par zéro impossible")
        # ... suite du code
```

### 5. Maintenir la Cohérence

Depuis Python 3, `__ne__` est automatiquement déduit de `__eq__` (il n'est plus nécessaire de le définir manuellement).  
Si vous définissez `__eq__` et `__lt__`, utilisez `@functools.total_ordering` pour générer les autres comparaisons.  

## Conclusion

Les méthodes spéciales (dunder methods) sont un outil puissant qui permet de :
- **Intégrer** vos objets naturellement dans le langage Python
- **Surcharger** les opérateurs pour qu'ils fonctionnent avec vos classes
- **Rendre** vos objets plus intuitifs à utiliser
- **Créer** des APIs élégantes et pythoniques

En maîtrisant ces méthodes, vous pouvez créer des classes qui se comportent comme des types natifs Python, rendant votre code plus lisible et plus agréable à utiliser.

**Points clés à retenir** :
- `__init__` : constructeur
- `__str__` et `__repr__` : représentations textuelles
- `__add__`, `__sub__`, etc. : opérateurs arithmétiques
- `__eq__`, `__lt__`, etc. : comparaisons
- `__len__`, `__getitem__`, etc. : comportement de conteneur
- `__iter__` et `__next__` : itération
- `__call__` : objets appelables
- `__enter__` et `__exit__` : gestionnaires de contexte

Dans la prochaine section, nous explorerons les **propriétés et décorateurs**, qui vous permettront de contrôler encore plus finement l'accès aux attributs de vos classes !

⏭️ [Propriétés et décorateurs](/03-programmation-orientee-objet/04-proprietes-et-decorateurs.md)
