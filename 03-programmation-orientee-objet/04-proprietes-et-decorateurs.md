🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.4 : Propriétés et décorateurs

## Introduction

Imaginez que vous ayez une classe `Personne` avec un attribut `age`. Que se passe-t-il si quelqu'un assigne un âge négatif ? Ou si vous voulez automatiquement calculer l'année de naissance quand on accède à cet attribut ? Les **propriétés** et **décorateurs** vous permettent de contrôler élégamment l'accès aux attributs de vos objets !

## Le problème : accès direct aux attributs

Voici un exemple problématique :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

# Problème : aucun contrôle !
personne = Personne("Alice", 25)
personne.age = -10  # Âge négatif ?!
personne.age = "vingt"  # Âge non numérique ?!
print(personne.age)  # vingt
```

Comment résoudre cela tout en gardant une syntaxe simple ?

## Solution 1 : Méthodes getter et setter (approche traditionnelle)

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age  # Attribut "privé" (convention)

    def get_age(self):
        """Getter : récupère l'âge."""
        return self._age

    def set_age(self, nouvelle_valeur):
        """Setter : définit l'âge avec validation."""
        if not isinstance(nouvelle_valeur, int):
            raise TypeError("L'âge doit être un entier")
        if nouvelle_valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        if nouvelle_valeur > 150:
            raise ValueError("L'âge ne peut pas dépasser 150 ans")
        self._age = nouvelle_valeur

# Utilisation (pas très élégante)
personne = Personne("Alice", 25)
print(personne.get_age())  # 25
personne.set_age(30)
print(personne.get_age())  # 30

try:
    personne.set_age(-5)
except ValueError as e:
    print(f"Erreur : {e}")
```

**Problème** : la syntaxe n'est pas naturelle (`get_age()` au lieu de `.age`)

## Solution 2 : Les propriétés avec `@property`

Les propriétés permettent d'utiliser la syntaxe d'attribut tout en exécutant du code :

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age  # Stockage interne

    @property
    def age(self):
        """Getter : récupère l'âge."""
        return self._age

    @age.setter
    def age(self, nouvelle_valeur):
        """Setter : définit l'âge avec validation."""
        if not isinstance(nouvelle_valeur, int):
            raise TypeError("L'âge doit être un entier")
        if nouvelle_valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        if nouvelle_valeur > 150:
            raise ValueError("L'âge ne peut pas dépasser 150 ans")
        self._age = nouvelle_valeur

# Utilisation naturelle !
personne = Personne("Alice", 25)
print(personne.age)    # 25 (appelle le getter)
personne.age = 30      # (appelle le setter)
print(personne.age)    # 30

try:
    personne.age = -5   # Validation automatique !
except ValueError as e:
    print(f"Erreur : {e}")
```

## Qu'est-ce qu'un décorateur ?

Un **décorateur** est une fonction qui modifie le comportement d'une autre fonction ou méthode. En Python, on les utilise avec la syntaxe `@nom_decorateur`.

### Décorateur simple

```python
def mon_decorateur(fonction):
    """Décorateur qui ajoute un message avant et après l'exécution."""
    def wrapper(*args, **kwargs):
        print("Avant l'exécution")
        resultat = fonction(*args, **kwargs)
        print("Après l'exécution")
        return resultat
    return wrapper

@mon_decorateur
def dire_bonjour(nom):
    print(f"Bonjour {nom} !")

# Test
dire_bonjour("Alice")
# Avant l'exécution
# Bonjour Alice !
# Après l'exécution
```

### `@property` est un décorateur !

`@property` transforme une méthode en attribut accessible en lecture.

## Propriétés avancées

### Propriété en lecture seule

```python
from datetime import datetime

class Personne:
    def __init__(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance

    @property
    def age(self):
        """Calcule l'âge automatiquement (lecture seule)."""
        return datetime.now().year - self.annee_naissance

    @property
    def est_majeur(self):
        """Détermine si la personne est majeure (lecture seule)."""
        return self.age >= 18

# Test
personne = Personne("Bob", 1990)
print(personne.age)        # Calculé automatiquement
print(personne.est_majeur) # True

# Tentative de modification (erreur !)
try:
    personne.age = 25
except AttributeError as e:
    print(f"Erreur : {e}")  # can't set attribute
```

### Propriété avec getter, setter et deleter

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde
        self._historique = []

    @property
    def solde(self):
        """Getter : accès au solde."""
        return self._solde

    @solde.setter
    def solde(self, nouveau_solde):
        """Setter : modification du solde avec historique."""
        if not isinstance(nouveau_solde, (int, float)):
            raise TypeError("Le solde doit être numérique")

        ancienne_valeur = self._solde
        self._solde = nouveau_solde

        # Enregistrer dans l'historique
        if nouveau_solde > ancienne_valeur:
            operation = f"Dépôt de {nouveau_solde - ancienne_valeur}€"
        else:
            operation = f"Retrait de {ancienne_valeur - nouveau_solde}€"

        self._historique.append(operation)

    @solde.deleter
    def solde(self):
        """Deleter : remise à zéro du solde."""
        self._historique.append("Fermeture du compte - solde remis à zéro")
        self._solde = 0

    @property
    def historique(self):
        """Historique en lecture seule."""
        return self._historique.copy()  # Copie pour éviter les modifications

# Test
compte = CompteBancaire("Alice", 1000)

print(compte.solde)        # 1000 (getter)
compte.solde = 1200        # (setter avec validation)
compte.solde = 800         # (setter avec historique)

print(compte.historique)   # ['Dépôt de 200€', 'Retrait de 400€']

del compte.solde           # (deleter)
print(compte.solde)        # 0
print(compte.historique)   # [..., 'Fermeture du compte - solde remis à zéro']
```

## Propriétés calculées

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    @property
    def aire(self):
        """Calcule l'aire automatiquement."""
        return self.longueur * self.largeur

    @property
    def perimetre(self):
        """Calcule le périmètre automatiquement."""
        return 2 * (self.longueur + self.largeur)

    @property
    def est_carre(self):
        """Détermine si c'est un carré."""
        return self.longueur == self.largeur

    @property
    def diagonale(self):
        """Calcule la longueur de la diagonale."""
        return (self.longueur ** 2 + self.largeur ** 2) ** 0.5

# Test
rect = Rectangle(4, 3)
print(f"Aire : {rect.aire}")           # 12
print(f"Périmètre : {rect.perimetre}") # 14
print(f"Est un carré : {rect.est_carre}") # False
print(f"Diagonale : {rect.diagonale:.2f}") # 5.00

# Modification des dimensions
rect.longueur = 5
print(f"Nouvelle aire : {rect.aire}")  # 15 (recalculée automatiquement)
```

## Validation avec propriétés

```python
class Produit:
    def __init__(self, nom, prix, stock=0):
        self.nom = nom
        self.prix = prix      # Utilise le setter
        self.stock = stock    # Utilise le setter

    @property
    def prix(self):
        """Prix du produit."""
        return self._prix

    @prix.setter
    def prix(self, valeur):
        """Validation du prix."""
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le prix doit être numérique")
        if valeur < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self._prix = round(valeur, 2)  # Arrondi à 2 décimales

    @property
    def stock(self):
        """Stock disponible."""
        return self._stock

    @stock.setter
    def stock(self, valeur):
        """Validation du stock."""
        if not isinstance(valeur, int):
            raise TypeError("Le stock doit être un entier")
        if valeur < 0:
            raise ValueError("Le stock ne peut pas être négatif")
        self._stock = valeur

    @property
    def valeur_stock(self):
        """Valeur totale du stock (lecture seule)."""
        return self.prix * self.stock

    @property
    def disponible(self):
        """Indique si le produit est disponible."""
        return self.stock > 0

    def vendre(self, quantite):
        """Vend une certaine quantité."""
        if quantite > self.stock:
            raise ValueError(f"Stock insuffisant. Disponible : {self.stock}")
        self.stock -= quantite
        return f"{quantite} unité(s) vendue(s)"

    def __str__(self):
        return f"{self.nom} - {self.prix}€ (Stock: {self.stock})"

# Test avec validation
produit = Produit("Livre Python", 29.99, 50)
print(produit)  # Livre Python - 29.99€ (Stock: 50)

print(f"Valeur du stock : {produit.valeur_stock}€")  # 1499.5€
print(f"Disponible : {produit.disponible}")          # True

# Vente
print(produit.vendre(5))  # 5 unité(s) vendue(s)
print(f"Stock restant : {produit.stock}")  # 45

# Validation des erreurs
try:
    produit.prix = -10  # Prix négatif
except ValueError as e:
    print(f"Erreur prix : {e}")

try:
    produit.stock = "beaucoup"  # Type incorrect
except TypeError as e:
    print(f"Erreur stock : {e}")
```

## Décorateurs personnalisés pour classes

### Décorateur de validation

```python
def valider_type(type_attendu):
    """Décorateur pour valider le type d'un paramètre."""
    def decorateur(setter):
        def wrapper(self, valeur):
            if not isinstance(valeur, type_attendu):
                nom_type = type_attendu.__name__
                raise TypeError(f"Valeur doit être de type {nom_type}")
            return setter(self, valeur)
        return wrapper
    return decorateur

def valider_positif(setter):
    """Décorateur pour valider qu'une valeur est positive."""
    def wrapper(self, valeur):
        if valeur < 0:
            raise ValueError("La valeur doit être positive")
        return setter(self, valeur)
    return wrapper

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    @valider_type((int, float))
    @valider_positif
    def rayon(self, valeur):
        self._rayon = valeur

    @property
    def aire(self):
        return 3.14159 * self.rayon ** 2

    @property
    def circonference(self):
        return 2 * 3.14159 * self.rayon

# Test
cercle = Cercle(5)
print(f"Aire : {cercle.aire:.2f}")  # 78.54

try:
    cercle.rayon = -3  # Erreur : valeur négative
except ValueError as e:
    print(f"Erreur : {e}")

try:
    cercle.rayon = "grand"  # Erreur : type incorrect
except TypeError as e:
    print(f"Erreur : {e}")
```

## Cache avec propriétés

```python
class CalculComplexe:
    def __init__(self, n):
        self.n = n
        self._factorielle_cache = None
        self._fibonacci_cache = None

    @property
    def factorielle(self):
        """Calcule la factorielle avec cache."""
        if self._factorielle_cache is None:
            print(f"Calcul de {self.n}! en cours...")
            resultat = 1
            for i in range(1, self.n + 1):
                resultat *= i
            self._factorielle_cache = resultat
        return self._factorielle_cache

    @property
    def fibonacci(self):
        """Calcule le n-ième nombre de Fibonacci avec cache."""
        if self._fibonacci_cache is None:
            print(f"Calcul de fibonacci({self.n}) en cours...")
            if self.n <= 1:
                self._fibonacci_cache = self.n
            else:
                a, b = 0, 1
                for _ in range(2, self.n + 1):
                    a, b = b, a + b
                self._fibonacci_cache = b
        return self._fibonacci_cache

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, valeur):
        """Quand n change, vider les caches."""
        self._n = valeur
        self._factorielle_cache = None
        self._fibonacci_cache = None

# Test du cache
calc = CalculComplexe(10)

print(calc.factorielle)  # Calcul de 10! en cours... 3628800
print(calc.factorielle)  # 3628800 (depuis le cache, pas de recalcul)

print(calc.fibonacci)    # Calcul de fibonacci(10) en cours... 55
print(calc.fibonacci)    # 55 (depuis le cache)

# Changement de n vide les caches
calc.n = 12
print(calc.factorielle)  # Calcul de 12! en cours... 479001600
```

## Propriétés et héritage

```python
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self._vitesse = 0

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, valeur):
        if valeur < 0:
            raise ValueError("La vitesse ne peut pas être négative")
        self._vitesse = valeur

    @property
    def description(self):
        return f"{self.marque} {self.modele}"

class Voiture(Vehicule):
    def __init__(self, marque, modele, nb_portes):
        super().__init__(marque, modele)
        self.nb_portes = nb_portes

    @property
    def vitesse(self):
        """Getter hérité, mais on peut ajouter du comportement."""
        return super().vitesse

    @vitesse.setter
    def vitesse(self, valeur):
        """Setter avec validation supplémentaire pour les voitures."""
        if valeur > 200:
            raise ValueError("Vitesse limitée à 200 km/h pour les voitures")
        # Appeler le setter parent pour la validation de base
        Vehicule.vitesse.fset(self, valeur)

    @property
    def description(self):
        """Redéfinition avec information supplémentaire."""
        base = super().description
        return f"{base} ({self.nb_portes} portes)"

class Moto(Vehicule):
    @vitesse.setter
    def vitesse(self, valeur):
        """Validation différente pour les motos."""
        if valeur > 300:
            raise ValueError("Vitesse limitée à 300 km/h pour les motos")
        Vehicule.vitesse.fset(self, valeur)

# Test de l'héritage
voiture = Voiture("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "R1")

print(voiture.description)  # Toyota Corolla (4 portes)
print(moto.description)     # Yamaha R1

voiture.vitesse = 150  # OK
try:
    voiture.vitesse = 250  # Erreur : trop rapide pour une voiture
except ValueError as e:
    print(f"Erreur voiture : {e}")

moto.vitesse = 250  # OK pour une moto
try:
    moto.vitesse = 350  # Erreur : trop rapide même pour une moto
except ValueError as e:
    print(f"Erreur moto : {e}")
```

## Exercices pratiques

### Exercice 1 : Classe Température
Créez une classe `Temperature` avec :
- Propriété `celsius` (stockage interne)
- Propriété `fahrenheit` (conversion automatique)
- Propriété `kelvin` (conversion automatique)
- Validation : température absolue impossible (< -273.15°C)

### Exercice 2 : Classe CompteBancaire avancé
Créez une classe `CompteBancaire` avec :
- Propriété `solde` avec validation
- Propriété `taux_interet` (entre 0 et 10%)
- Propriété `interets_annuels` (calculée)
- Propriété `type_compte` (lecture seule basée sur le solde)

### Solutions :

```python
# Solution Exercice 1 : Température
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius  # Utilise le setter pour validation

    @property
    def celsius(self):
        """Température en Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        """Validation de la température."""
        if not isinstance(valeur, (int, float)):
            raise TypeError("La température doit être numérique")
        if valeur < -273.15:
            raise ValueError("Température impossible (en dessous du zéro absolu)")
        self._celsius = round(valeur, 2)

    @property
    def fahrenheit(self):
        """Conversion automatique en Fahrenheit."""
        return round(self._celsius * 9/5 + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, valeur):
        """Définit la température via Fahrenheit."""
        celsius_equivalent = (valeur - 32) * 5/9
        self.celsius = celsius_equivalent  # Utilise la validation du setter celsius

    @property
    def kelvin(self):
        """Conversion automatique en Kelvin."""
        return round(self._celsius + 273.15, 2)

    @kelvin.setter
    def kelvin(self, valeur):
        """Définit la température via Kelvin."""
        celsius_equivalent = valeur - 273.15
        self.celsius = celsius_equivalent

    @property
    def etat_eau(self):
        """Détermine l'état de l'eau à cette température."""
        if self._celsius < 0:
            return "solide (glace)"
        elif self._celsius < 100:
            return "liquide"
        else:
            return "gazeux (vapeur)"

    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit}°F, {self.kelvin}K)"

# Test Température
temp = Temperature(25)
print(temp)  # 25°C (77°F, 298.15K)
print(f"État de l'eau : {temp.etat_eau}")  # liquide

# Conversion via Fahrenheit
temp.fahrenheit = 100
print(temp)  # 37.78°C (100°F, 310.93K)

# Validation
try:
    temp.celsius = -300  # Impossible !
except ValueError as e:
    print(f"Erreur : {e}")

# Solution Exercice 2 : CompteBancaire avancé
class CompteBancaire:
    def __init__(self, titulaire, solde=0, taux_interet=2.0):
        self.titulaire = titulaire
        self.solde = solde
        self.taux_interet = taux_interet

    @property
    def solde(self):
        """Solde du compte."""
        return self._solde

    @solde.setter
    def solde(self, valeur):
        """Validation du solde."""
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le solde doit être numérique")
        self._solde = round(valeur, 2)

    @property
    def taux_interet(self):
        """Taux d'intérêt annuel."""
        return self._taux_interet

    @taux_interet.setter
    def taux_interet(self, valeur):
        """Validation du taux d'intérêt."""
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le taux doit être numérique")
        if not 0 <= valeur <= 10:
            raise ValueError("Le taux doit être entre 0 et 10%")
        self._taux_interet = valeur

    @property
    def interets_annuels(self):
        """Calcule les intérêts annuels possibles."""
        if self._solde > 0:
            return round(self._solde * self._taux_interet / 100, 2)
        return 0

    @property
    def type_compte(self):
        """Détermine le type de compte basé sur le solde."""
        if self._solde < 0:
            return "Compte à découvert"
        elif self._solde == 0:
            return "Compte vide"
        elif self._solde < 1000:
            return "Compte standard"
        elif self._solde < 10000:
            return "Compte privilège"
        else:
            return "Compte premium"

    @property
    def statut(self):
        """Statut global du compte."""
        return {
            'solde': self._solde,
            'type': self.type_compte,
            'taux': self._taux_interet,
            'interets_possibles': self.interets_annuels
        }

    def __str__(self):
        return f"Compte de {self.titulaire}: {self._solde}€ ({self.type_compte})"

# Test CompteBancaire
compte = CompteBancaire("Alice", 5000, 3.5)
print(compte)  # Compte de Alice: 5000€ (Compte privilège)
print(f"Intérêts annuels : {compte.interets_annuels}€")  # 175.0€

# Changement de statut automatique
compte.solde = 15000
print(compte)  # Compte de Alice: 15000€ (Compte premium)

# Validation
try:
    compte.taux_interet = 15  # Taux trop élevé
except ValueError as e:
    print(f"Erreur : {e}")

print(compte.statut)
```

## Bonnes pratiques

1. **Nommage** : utilisez un underscore pour les attributs "privés" (`_attribut`)
2. **Validation** : validez toujours dans les setters
3. **Cohérence** : si vous avez un setter, ayez aussi un getter
4. **Performance** : utilisez le cache pour les calculs coûteux
5. **Documentation** : documentez le comportement de vos propriétés

```python
class ExempleBonnesPratiques:
    def __init__(self, valeur):
        self._valeur = None
        self.valeur = valeur  # Utilise le setter pour validation initiale

    @property
    def valeur(self):
        """
        Valeur stockée (lecture/écriture).

        Returns:
            float: La valeur actuelle
        """
        return self._valeur

    @valeur.setter
    def valeur(self, nouvelle_valeur):
        """
        Définit une nouvelle valeur avec validation.

        Args:
            nouvelle_valeur (float): La nouvelle valeur

        Raises:
            TypeError: Si la valeur n'est pas numérique
            ValueError: Si la valeur est négative
        """
        if not isinstance(nouvelle_valeur, (int, float)):
            raise TypeError("La valeur doit être numérique")
        if nouvelle_valeur < 0:
            raise ValueError("La valeur doit être positive")
        self._valeur = float(nouvelle_valeur)
```

## Résumé

Dans cette section, vous avez appris :

✅ **Les propriétés** : contrôler l'accès aux attributs avec `@property`
✅ **Validation élégante** : syntaxe naturelle avec contrôle automatique
✅ **Propriétés calculées** : valeurs dérivées mises à jour automatiquement
✅ **Décorateurs** : modifier le comportement des méthodes
✅ **Cache et performance** : optimiser les calculs coûteux
✅ **Héritage de propriétés** : redéfinir le comportement dans les classes enfants
✅ **Bonnes pratiques** : validation, documentation, nommage

Dans la prochaine section, nous explorerons les concepts avancés comme les métaclasses et la programmation orientée objet de haut niveau !

⏭️
