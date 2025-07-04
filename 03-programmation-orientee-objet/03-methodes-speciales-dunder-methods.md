🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.3 : Méthodes spéciales (dunder methods)

## Introduction

Avez-vous déjà remarqué que quand vous faites `print(5 + 3)`, Python sait comment additionner deux nombres ? Ou que `len([1, 2, 3])` retourne 3 ? Comment Python sait-il quoi faire avec vos objets personnalisés ? C'est grâce aux **méthodes spéciales** !

Les méthodes spéciales (appelées aussi "dunder methods" pour "**d**ouble **under**score") permettent à vos objets de s'intégrer naturellement dans l'écosystème Python.

## Qu'est-ce que les méthodes spéciales ?

Les **méthodes spéciales** sont des méthodes avec des noms particuliers entourés de double underscores (`__nom__`). Elles définissent comment vos objets se comportent avec les opérateurs Python et les fonctions built-in.

### Exemples d'utilisation courante :
- `print(mon_objet)` → appelle `__str__()`
- `len(mon_objet)` → appelle `__len__()`
- `mon_objet1 + mon_objet2` → appelle `__add__()`
- `mon_objet == autre_objet` → appelle `__eq__()`

## Les méthodes de représentation

### `__str__()` : Représentation pour les humains

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        """Représentation lisible pour les humains."""
        return f"{self.nom}, {self.age} ans"

# Test
personne = Personne("Alice", 25)
print(personne)  # Alice, 25 ans
print(str(personne))  # Alice, 25 ans
```

### `__repr__()` : Représentation pour les développeurs

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        """Pour l'affichage utilisateur."""
        return f"{self.nom}, {self.age} ans"

    def __repr__(self):
        """Pour le débogage et développement."""
        return f"Personne(nom='{self.nom}', age={self.age})"

# Test
personne = Personne("Bob", 30)
print(personne)      # Bob, 30 ans (utilise __str__)
print(repr(personne)) # Personne(nom='Bob', age=30) (utilise __repr__)

# Dans une liste, __repr__ est utilisé
personnes = [personne]
print(personnes)     # [Personne(nom='Bob', age=30)]
```

### Différence entre `__str__` et `__repr__`

- **`__str__`** : pour l'utilisateur final (lisible, informatif)
- **`__repr__`** : pour le développeur (précis, idéalement exécutable)

## Les méthodes de comparaison

```python
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} ({self.prix}€)"

    def __eq__(self, other):
        """Égalité : =="""
        if not isinstance(other, Produit):
            return False
        return self.nom == other.nom and self.prix == other.prix

    def __lt__(self, other):
        """Inférieur : <"""
        if not isinstance(other, Produit):
            return NotImplemented
        return self.prix < other.prix

    def __le__(self, other):
        """Inférieur ou égal : <="""
        return self < other or self == other

    def __gt__(self, other):
        """Supérieur : >"""
        if not isinstance(other, Produit):
            return NotImplemented
        return self.prix > other.prix

    def __ge__(self, other):
        """Supérieur ou égal : >="""
        return self > other or self == other

    def __ne__(self, other):
        """Différent : !="""
        return not self == other

# Test des comparaisons
livre = Produit("Python Guide", 29.99)
dvd = Produit("Film Action", 19.99)
livre2 = Produit("Python Guide", 29.99)

print(livre == livre2)  # True
print(livre == dvd)     # False
print(livre > dvd)      # True (29.99 > 19.99)
print(dvd < livre)      # True

# Tri automatique !
produits = [livre, dvd, Produit("Jeu", 39.99)]
produits_tries = sorted(produits)
for produit in produits_tries:
    print(produit)
# Film Action (19.99€)
# Python Guide (29.99€)
# Jeu (39.99€)
```

## Les méthodes arithmétiques

```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"

    def __add__(self, other):
        """Addition : +"""
        if isinstance(other, Vecteur):
            return Vecteur(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Soustraction : -"""
        if isinstance(other, Vecteur):
            return Vecteur(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        """Multiplication par un scalaire : *"""
        if isinstance(other, (int, float)):
            return Vecteur(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        """Division par un scalaire : /"""
        if isinstance(other, (int, float)) and other != 0:
            return Vecteur(self.x / other, self.y / other)
        return NotImplemented

    def __neg__(self):
        """Négation : -vecteur"""
        return Vecteur(-self.x, -self.y)

    def __abs__(self):
        """Valeur absolue (norme) : abs()"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Test des opérations arithmétiques
v1 = Vecteur(3, 4)
v2 = Vecteur(1, 2)

print(v1)           # Vecteur(3, 4)
print(v1 + v2)      # Vecteur(4, 6)
print(v1 - v2)      # Vecteur(2, 2)
print(v1 * 3)       # Vecteur(9, 12)
print(v1 / 2)       # Vecteur(1.5, 2.0)
print(-v1)          # Vecteur(-3, -4)
print(abs(v1))      # 5.0 (norme du vecteur)
```

## Les méthodes de conteneur

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        """Ajoute une chanson à la playlist."""
        self.chansons.append(chanson)

    def __len__(self):
        """Nombre de chansons : len()"""
        return len(self.chansons)

    def __getitem__(self, index):
        """Accès par index : playlist[0]"""
        return self.chansons[index]

    def __setitem__(self, index, chanson):
        """Modification par index : playlist[0] = "nouvelle chanson" """
        self.chansons[index] = chanson

    def __delitem__(self, index):
        """Suppression par index : del playlist[0]"""
        del self.chansons[index]

    def __contains__(self, chanson):
        """Test d'appartenance : "chanson" in playlist"""
        return chanson in self.chansons

    def __iter__(self):
        """Itération : for chanson in playlist"""
        return iter(self.chansons)

    def __str__(self):
        return f"Playlist '{self.nom}' ({len(self)} chansons)"

# Test des fonctionnalités de conteneur
ma_playlist = Playlist("Mes favoris")
ma_playlist.ajouter("Bohemian Rhapsody")
ma_playlist.ajouter("Imagine")
ma_playlist.ajouter("Hotel California")

print(ma_playlist)                    # Playlist 'Mes favoris' (3 chansons)
print(len(ma_playlist))              # 3
print(ma_playlist[0])                # Bohemian Rhapsody
print("Imagine" in ma_playlist)      # True

# Modification
ma_playlist[1] = "Yesterday"
print(ma_playlist[1])                # Yesterday

# Itération
print("Toutes les chansons :")
for chanson in ma_playlist:
    print(f"  ♪ {chanson}")

# Suppression
del ma_playlist[0]
print(f"Après suppression : {len(ma_playlist)} chansons")
```

## Les méthodes d'appel

```python
class Calculatrice:
    def __init__(self, nom="Calculatrice"):
        self.nom = nom
        self.historique = []

    def __call__(self, operation, a, b):
        """Permet d'utiliser l'objet comme une fonction."""
        if operation == "+":
            resultat = a + b
        elif operation == "-":
            resultat = a - b
        elif operation == "*":
            resultat = a * b
        elif operation == "/":
            if b != 0:
                resultat = a / b
            else:
                return "Erreur : division par zéro"
        else:
            return "Opération non supportée"

        # Enregistrer dans l'historique
        self.historique.append(f"{a} {operation} {b} = {resultat}")
        return resultat

    def afficher_historique(self):
        print(f"Historique de {self.nom}:")
        for calcul in self.historique:
            print(f"  {calcul}")

# Test de __call__
calc = Calculatrice("Ma calculette")

# L'objet peut être appelé comme une fonction !
print(calc("+", 5, 3))    # 8
print(calc("*", 4, 7))    # 28
print(calc("/", 10, 2))   # 5.0

calc.afficher_historique()
# Historique de Ma calculette:
#   5 + 3 = 8
#   4 * 7 = 28
#   10 / 2 = 5.0
```

## Gestion des attributs

```python
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self._prix = prix  # Attribut "privé"

    def __getattr__(self, name):
        """Appelé quand un attribut n'existe pas."""
        if name == "description":
            return f"Produit : {self.nom}"
        raise AttributeError(f"'{type(self).__name__}' n'a pas d'attribut '{name}'")

    def __setattr__(self, name, value):
        """Contrôle l'assignation d'attributs."""
        if name == "prix":
            if value < 0:
                raise ValueError("Le prix ne peut pas être négatif")
            self._prix = value
        else:
            # Comportement normal pour les autres attributs
            super().__setattr__(name, value)

    def __getattribute__(self, name):
        """Intercepte TOUS les accès aux attributs."""
        if name == "prix":
            # Retourner l'attribut privé
            return super().__getattribute__("_prix")
        return super().__getattribute__(name)

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

# Test
produit = Produit("Livre", 25.99)
print(produit.prix)        # 25.99 (via __getattribute__)
print(produit.description) # Produit : Livre (via __getattr__)

# Contrôle de l'assignation
produit.prix = 30.00       # OK
print(produit.prix)        # 30.0

try:
    produit.prix = -5      # Erreur !
except ValueError as e:
    print(f"Erreur : {e}")
```

## Exemple pratique complet : Classe Compte bancaire

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
        self.operations = []

    # Représentation
    def __str__(self):
        return f"Compte de {self.titulaire} : {self.solde}€"

    def __repr__(self):
        return f"CompteBancaire('{self.titulaire}', {self.solde})"

    # Comparaisons (basées sur le solde)
    def __eq__(self, other):
        if isinstance(other, CompteBancaire):
            return self.solde == other.solde
        return False

    def __lt__(self, other):
        if isinstance(other, CompteBancaire):
            return self.solde < other.solde
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    # Opérations arithmétiques
    def __add__(self, montant):
        """Dépôt : compte + 100"""
        if isinstance(montant, (int, float)) and montant > 0:
            nouveau_compte = CompteBancaire(self.titulaire, self.solde + montant)
            nouveau_compte.operations = self.operations.copy()
            nouveau_compte.operations.append(f"Dépôt de {montant}€")
            return nouveau_compte
        return NotImplemented

    def __sub__(self, montant):
        """Retrait : compte - 50"""
        if isinstance(montant, (int, float)) and montant > 0:
            if self.solde >= montant:
                nouveau_compte = CompteBancaire(self.titulaire, self.solde - montant)
                nouveau_compte.operations = self.operations.copy()
                nouveau_compte.operations.append(f"Retrait de {montant}€")
                return nouveau_compte
            else:
                raise ValueError("Solde insuffisant")
        return NotImplemented

    # Méthodes de conteneur
    def __len__(self):
        """Nombre d'opérations."""
        return len(self.operations)

    def __getitem__(self, index):
        """Accès aux opérations par index."""
        return self.operations[index]

    def __contains__(self, operation):
        """Test si une opération existe."""
        return operation in self.operations

    # Méthode d'appel
    def __call__(self, montant, operation="depot"):
        """Utilisation comme fonction pour les opérations."""
        if operation == "depot":
            return self + montant
        elif operation == "retrait":
            return self - montant
        else:
            raise ValueError("Opération inconnue")

# Test complet
compte1 = CompteBancaire("Alice", 1000)
compte2 = CompteBancaire("Bob", 500)

print(compte1)          # Compte de Alice : 1000€
print(repr(compte1))    # CompteBancaire('Alice', 1000)

# Comparaisons
print(compte1 > compte2)  # True
print(compte1 == compte2) # False

# Opérations arithmétiques
compte1_apres_depot = compte1 + 200
print(compte1_apres_depot)  # Compte de Alice : 1200€

compte1_apres_retrait = compte1_apres_depot - 150
print(compte1_apres_retrait)  # Compte de Alice : 1050€

# Conteneur
print(f"Nombre d'opérations : {len(compte1_apres_retrait)}")
for i, operation in enumerate(compte1_apres_retrait.operations):
    print(f"  {i+1}. {operation}")

# Appel comme fonction
compte_final = compte1("depot", 300)
print(compte_final)
```

## Méthodes spéciales utiles - Récapitulatif

### Représentation
- `__str__()` : affichage pour utilisateurs
- `__repr__()` : affichage pour développeurs
- `__format__()` : formatage personnalisé

### Comparaisons
- `__eq__()` : égalité (`==`)
- `__ne__()` : inégalité (`!=`)
- `__lt__()` : inférieur (`<`)
- `__le__()` : inférieur ou égal (`<=`)
- `__gt__()` : supérieur (`>`)
- `__ge__()` : supérieur ou égal (`>=`)

### Arithmétique
- `__add__()` : addition (`+`)
- `__sub__()` : soustraction (`-`)
- `__mul__()` : multiplication (`*`)
- `__truediv__()` : division (`/`)
- `__mod__()` : modulo (`%`)
- `__pow__()` : puissance (`**`)

### Conteneurs
- `__len__()` : longueur (`len()`)
- `__getitem__()` : accès par index (`obj[key]`)
- `__setitem__()` : assignation par index (`obj[key] = value`)
- `__delitem__()` : suppression par index (`del obj[key]`)
- `__contains__()` : appartenance (`in`)
- `__iter__()` : itération (`for ... in`)

### Autres
- `__call__()` : rendre l'objet callable
- `__bool__()` : conversion en booléen
- `__hash__()` : pour utiliser l'objet comme clé de dictionnaire

## Exercices pratiques

### Exercice 1 : Classe Fraction
Créez une classe `Fraction` qui supporte :
- Représentation (`__str__`, `__repr__`)
- Opérations arithmétiques (`+`, `-`, `*`, `/`)
- Comparaisons (`==`, `<`, `>`)
- Simplification automatique

### Exercice 2 : Classe Matrice
Créez une classe `Matrice` qui supporte :
- Accès aux éléments (`matrice[i][j]`)
- Addition et multiplication de matrices
- Affichage formaté
- Test d'égalité

### Solutions :

```python
# Solution Exercice 1 : Fraction
from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur=1):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro")

        # Simplification automatique
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

    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self.numerateur * other.denominateur + other.numerateur * self.denominateur
            den = self.denominateur * other.denominateur
            return Fraction(num, den)
        elif isinstance(other, int):
            return self + Fraction(other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.numerateur * other.denominateur - other.numerateur * self.denominateur
            den = self.denominateur * other.denominateur
            return Fraction(num, den)
        elif isinstance(other, int):
            return self - Fraction(other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerateur * other.numerateur,
                          self.denominateur * other.denominateur)
        elif isinstance(other, int):
            return Fraction(self.numerateur * other, self.denominateur)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self * Fraction(other.denominateur, other.numerateur)
        elif isinstance(other, int):
            return self / Fraction(other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerateur == other.numerateur and
                   self.denominateur == other.denominateur)
        elif isinstance(other, int):
            return self == Fraction(other)
        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self.numerateur * other.denominateur <
                   other.numerateur * self.denominateur)
        elif isinstance(other, int):
            return self < Fraction(other)
        return NotImplemented

    def __float__(self):
        return self.numerateur / self.denominateur

# Test de la classe Fraction
f1 = Fraction(3, 4)
f2 = Fraction(1, 2)

print(f1)           # 3/4
print(f1 + f2)      # 5/4
print(f1 * f2)      # 3/8
print(f1 > f2)      # True
print(float(f1))    # 0.75

# Solution Exercice 2 : Matrice
class Matrice:
    def __init__(self, donnees):
        """Initialise une matrice à partir d'une liste de listes."""
        if not donnees or not donnees[0]:
            raise ValueError("La matrice ne peut pas être vide")

        # Vérifier que toutes les lignes ont la même longueur
        largeur = len(donnees[0])
        if not all(len(ligne) == largeur for ligne in donnees):
            raise ValueError("Toutes les lignes doivent avoir la même longueur")

        self.donnees = [ligne[:] for ligne in donnees]  # Copie profonde
        self.hauteur = len(donnees)
        self.largeur = largeur

    def __str__(self):
        """Affichage formaté de la matrice."""
        lignes = []
        for ligne in self.donnees:
            ligne_str = " ".join(f"{val:6.2f}" if isinstance(val, float)
                                else f"{val:6}" for val in ligne)
            lignes.append(f"[{ligne_str}]")
        return "\n".join(lignes)

    def __repr__(self):
        return f"Matrice({self.donnees})"

    def __getitem__(self, index):
        """Accès aux lignes : matrice[i]"""
        return self.donnees[index]

    def __setitem__(self, index, valeur):
        """Modification de lignes : matrice[i] = [...]"""
        if len(valeur) != self.largeur:
            raise ValueError(f"La ligne doit avoir {self.largeur} éléments")
        self.donnees[index] = list(valeur)

    def __eq__(self, other):
        """Test d'égalité entre matrices."""
        if not isinstance(other, Matrice):
            return False
        return self.donnees == other.donnees

    def __add__(self, other):
        """Addition de matrices."""
        if not isinstance(other, Matrice):
            return NotImplemented

        if self.hauteur != other.hauteur or self.largeur != other.largeur:
            raise ValueError("Les matrices doivent avoir les mêmes dimensions")

        resultat = []
        for i in range(self.hauteur):
            ligne = []
            for j in range(self.largeur):
                ligne.append(self[i][j] + other[i][j])
            resultat.append(ligne)

        return Matrice(resultat)

    def __mul__(self, other):
        """Multiplication matricielle ou par scalaire."""
        if isinstance(other, (int, float)):
            # Multiplication par scalaire
            resultat = []
            for ligne in self.donnees:
                nouvelle_ligne = [val * other for val in ligne]
                resultat.append(nouvelle_ligne)
            return Matrice(resultat)

        elif isinstance(other, Matrice):
            # Multiplication matricielle
            if self.largeur != other.hauteur:
                raise ValueError("Nombre de colonnes de A doit égaler nombre de lignes de B")

            resultat = []
            for i in range(self.hauteur):
                ligne = []
                for j in range(other.largeur):
                    somme = sum(self[i][k] * other[k][j] for k in range(self.largeur))
                    ligne.append(somme)
                resultat.append(ligne)

            return Matrice(resultat)

        return NotImplemented

# Test de la classe Matrice
m1 = Matrice([[1, 2], [3, 4]])
m2 = Matrice([[5, 6], [7, 8]])

print("Matrice 1:")
print(m1)
print("\nMatrice 2:")
print(m2)

print("\nAddition:")
print(m1 + m2)

print("\nMultiplication par 2:")
print(m1 * 2)

print("\nMultiplication matricielle:")
print(m1 * m2)

print(f"\nÉgalité : {m1 == m2}")
print(f"Accès m1[0][1] : {m1[0][1]}")
```

## Bonnes pratiques

1. **Cohérence** : si vous implémentez `__eq__`, implémentez aussi `__hash__` si nécessaire
2. **Symétrie** : `a == b` doit donner le même résultat que `b == a`
3. **Type checking** : utilisez `isinstance()` et retournez `NotImplemented` si approprié
4. **Documentation** : documentez le comportement de vos méthodes spéciales

## Résumé

Dans cette section, vous avez appris :

✅ **Les méthodes spéciales** : intégration naturelle avec Python
✅ **Représentation** : `__str__()` et `__repr__()`
✅ **Comparaisons** : `__eq__()`, `__lt__()`, etc.
✅ **Arithmétique** : `__add__()`, `__sub__()`, etc.
✅ **Conteneurs** : `__len__()`, `__getitem__()`, etc.
✅ **Méthodes d'appel** : `__call__()`
✅ **Bonnes pratiques** : cohérence et documentation

Dans la prochaine section, nous découvrirons les propriétés et décorateurs pour contrôler l'accès aux attributs de manière élégante !

⏭️
