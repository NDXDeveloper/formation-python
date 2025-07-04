🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.2 : Héritage et polymorphisme

## Introduction

Imaginez que vous développez un jeu vidéo avec différents types de personnages : des guerriers, des mages, des archers... Ils ont tous des points communs (nom, points de vie, niveau) mais aussi des spécificités (sorts pour les mages, force pour les guerriers). Comment éviter de répéter le même code ? C'est exactement ce que l'héritage vient résoudre !

## Qu'est-ce que l'héritage ?

L'**héritage** permet de créer une nouvelle classe basée sur une classe existante. La nouvelle classe :
- **Hérite** de tous les attributs et méthodes de la classe parent
- Peut **ajouter** ses propres attributs et méthodes
- Peut **modifier** (redéfinir) les méthodes héritées

### Analogie familiale
Pensez à l'héritage génétique : un enfant hérite des caractéristiques de ses parents, mais peut aussi avoir ses propres traits uniques.

## Vocabulaire de l'héritage

- **Classe parent** (ou classe de base, superclasse) : la classe dont on hérite
- **Classe enfant** (ou classe dérivée, sous-classe) : la classe qui hérite
- **Redéfinition** : modifier une méthode héritée dans la classe enfant

## Premier exemple : Animaux

Commençons par un exemple simple avec des animaux :

```python
# Classe parent (classe de base)
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def dormir(self):
        return f"{self.nom} dort paisiblement"

    def manger(self):
        return f"{self.nom} mange"

    def faire_du_bruit(self):
        return f"{self.nom} fait du bruit"

# Classe enfant qui hérite d'Animal
class Chien(Animal):
    def __init__(self, nom, age, race):
        # Appeler le constructeur de la classe parent
        super().__init__(nom, age)
        self.race = race

    # Redéfinir la méthode faire_du_bruit
    def faire_du_bruit(self):
        return f"{self.nom} aboie : Woof!"

    # Ajouter une nouvelle méthode spécifique aux chiens
    def rapporter_balle(self):
        return f"{self.nom} rapporte la balle"

# Autre classe enfant
class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    # Redéfinir la méthode faire_du_bruit
    def faire_du_bruit(self):
        return f"{self.nom} miaule : Miaou!"

    # Méthode spécifique aux chats
    def ronronner(self):
        return f"{self.nom} ronronne de bonheur"

# Utilisation
mon_chien = Chien("Rex", 3, "Berger Allemand")
mon_chat = Chat("Whiskers", 2, "noir")

# Méthodes héritées
print(mon_chien.dormir())    # Rex dort paisiblement
print(mon_chat.manger())     # Whiskers mange

# Méthodes redéfinies
print(mon_chien.faire_du_bruit())  # Rex aboie : Woof!
print(mon_chat.faire_du_bruit())   # Whiskers miaule : Miaou!

# Méthodes spécifiques
print(mon_chien.rapporter_balle())  # Rex rapporte la balle
print(mon_chat.ronronner())         # Whiskers ronronne de bonheur
```

### Points clés :

1. **`super()`** : permet d'appeler les méthodes de la classe parent
2. **Héritage automatique** : `Chien` et `Chat` héritent automatiquement de `dormir()` et `manger()`
3. **Redéfinition** : chaque animal fait du bruit différemment
4. **Ajout de fonctionnalités** : chaque classe enfant peut avoir ses propres méthodes

## La fonction `super()`

`super()` est essentielle pour accéder aux méthodes de la classe parent :

```python
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.kilometre = 0

    def rouler(self, distance):
        self.kilometre += distance
        return f"Le véhicule a roulé {distance} km"

class Voiture(Vehicule):
    def __init__(self, marque, modele, nb_portes):
        # Appeler le constructeur parent
        super().__init__(marque, modele)
        self.nb_portes = nb_portes

    def rouler(self, distance):
        # Appeler la méthode parent et ajouter du comportement
        resultat = super().rouler(distance)
        return f"{resultat}. Total : {self.kilometre} km"

class Moto(Vehicule):
    def __init__(self, marque, modele, cylindree):
        super().__init__(marque, modele)
        self.cylindree = cylindree

    def faire_wheelie(self):
        return f"La {self.marque} fait un wheelie !"

# Test
ma_voiture = Voiture("Toyota", "Corolla", 4)
ma_moto = Moto("Yamaha", "R1", 1000)

print(ma_voiture.rouler(50))  # Utilise la méthode redéfinie
print(ma_moto.rouler(30))     # Utilise la méthode héritée
print(ma_moto.faire_wheelie())
```

## Qu'est-ce que le polymorphisme ?

Le **polymorphisme** signifie "plusieurs formes". Il permet à des objets de types différents de répondre à la même interface, chacun à sa manière.

### Exemple concret de polymorphisme

```python
class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def aire(self):
        pass  # Méthode à redéfinir dans les classes enfants

    def perimetre(self):
        pass

    def description(self):
        return f"Une forme {self.couleur}"

class Rectangle(Forme):
    def __init__(self, couleur, longueur, largeur):
        super().__init__(couleur)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def description(self):
        return f"Un rectangle {self.couleur} de {self.longueur}x{self.largeur}"

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon

    def aire(self):
        return 3.14159 * self.rayon ** 2

    def perimetre(self):
        return 2 * 3.14159 * self.rayon

    def description(self):
        return f"Un cercle {self.couleur} de rayon {self.rayon}"

# Polymorphisme en action
formes = [
    Rectangle("rouge", 5, 3),
    Cercle("bleu", 4),
    Rectangle("vert", 2, 2)
]

# Même code pour tous les types de formes !
for forme in formes:
    print(f"{forme.description()}")
    print(f"  Aire : {forme.aire():.2f}")
    print(f"  Périmètre : {forme.perimetre():.2f}")
    print("-" * 30)
```

### Avantage du polymorphisme

Le même code (`forme.aire()`, `forme.description()`) fonctionne pour tous les types de formes, même si chaque classe l'implémente différemment.

## Exemple pratique : Système d'employés

Créons un système de gestion d'employés plus complexe :

```python
class Employe:
    """Classe de base pour tous les employés."""

    def __init__(self, nom, prenom, salaire_base):
        self.nom = nom
        self.prenom = prenom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        """Calcule le salaire (à redéfinir dans les classes enfants)."""
        return self.salaire_base

    def se_presenter(self):
        """Présentation de l'employé."""
        return f"Je suis {self.prenom} {self.nom}"

    def info_salaire(self):
        """Affiche les informations de salaire."""
        return f"Salaire de {self.prenom} : {self.calculer_salaire()}€"

class Vendeur(Employe):
    def __init__(self, nom, prenom, salaire_base, commission_pct):
        super().__init__(nom, prenom, salaire_base)
        self.commission_pct = commission_pct
        self.ventes_mois = 0

    def enregistrer_vente(self, montant):
        """Enregistre une vente."""
        self.ventes_mois += montant
        return f"Vente de {montant}€ enregistrée"

    def calculer_salaire(self):
        """Salaire = salaire de base + commission sur les ventes."""
        commission = self.ventes_mois * (self.commission_pct / 100)
        return self.salaire_base + commission

    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, je suis vendeur"

class Manager(Employe):
    def __init__(self, nom, prenom, salaire_base, bonus_equipe):
        super().__init__(nom, prenom, salaire_base)
        self.bonus_equipe = bonus_equipe
        self.equipe = []

    def ajouter_employe(self, employe):
        """Ajoute un employé à l'équipe."""
        self.equipe.append(employe)
        return f"{employe.prenom} {employe.nom} ajouté à l'équipe"

    def calculer_salaire(self):
        """Salaire = salaire de base + bonus par membre d'équipe."""
        return self.salaire_base + (len(self.equipe) * self.bonus_equipe)

    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, je manage une équipe de {len(self.equipe)} personnes"

class Developpeur(Employe):
    def __init__(self, nom, prenom, salaire_base, langage_principal):
        super().__init__(nom, prenom, salaire_base)
        self.langage_principal = langage_principal
        self.projets_termines = 0

    def terminer_projet(self):
        """Marque un projet comme terminé."""
        self.projets_termines += 1
        return f"Projet terminé ! Total : {self.projets_termines}"

    def calculer_salaire(self):
        """Salaire = salaire de base + bonus par projet terminé."""
        bonus_projet = self.projets_termines * 200
        return self.salaire_base + bonus_projet

    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, je développe en {self.langage_principal}"

# Utilisation du polymorphisme
employes = [
    Vendeur("Dupont", "Alice", 2000, 5),
    Manager("Martin", "Bob", 3000, 100),
    Developpeur("Durand", "Charlie", 2500, "Python")
]

# Configuration des données
employes[0].enregistrer_vente(10000)  # Alice fait des ventes
employes[1].ajouter_employe(employes[0])  # Bob manage Alice
employes[1].ajouter_employe(employes[2])  # Bob manage Charlie
employes[2].terminer_projet()  # Charlie termine un projet
employes[2].terminer_projet()  # Charlie termine un autre projet

# Polymorphisme : même code pour tous les types d'employés
print("=== Rapport des employés ===")
for employe in employes:
    print(employe.se_presenter())
    print(employe.info_salaire())
    print("-" * 40)

# Calcul de la masse salariale totale
total_salaires = sum(employe.calculer_salaire() for employe in employes)
print(f"Masse salariale totale : {total_salaires}€")
```

## Vérification du type et de l'héritage

Python fournit des fonctions utiles pour travailler avec l'héritage :

```python
# isinstance() : vérifier si un objet est d'un certain type
mon_chien = Chien("Rex", 3, "Labrador")

print(isinstance(mon_chien, Chien))    # True
print(isinstance(mon_chien, Animal))   # True (héritage!)
print(isinstance(mon_chien, Chat))     # False

# issubclass() : vérifier si une classe hérite d'une autre
print(issubclass(Chien, Animal))  # True
print(issubclass(Chat, Animal))   # True
print(issubclass(Animal, Chien))  # False

# type() : obtenir le type exact
print(type(mon_chien))  # <class '__main__.Chien'>

# Utilisation pratique
def soigner_animal(animal):
    if isinstance(animal, Animal):
        print(f"Soins pour {animal.nom}")
        if isinstance(animal, Chien):
            print("Donner des croquettes pour chien")
        elif isinstance(animal, Chat):
            print("Donner des croquettes pour chat")
    else:
        print("Ce n'est pas un animal !")
```

## Héritage multiple (aperçu)

Python permet l'héritage multiple (hériter de plusieurs classes) :

```python
class Volant:
    def voler(self):
        return "Je vole dans les airs"

class Aquatique:
    def nager(self):
        return "Je nage dans l'eau"

class Canard(Animal, Volant, Aquatique):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def faire_du_bruit(self):
        return f"{self.nom} fait : Coin coin!"

# Le canard peut tout faire !
canard = Canard("Donald", 5)
print(canard.dormir())        # Hérité d'Animal
print(canard.voler())         # Hérité de Volant
print(canard.nager())         # Hérité d'Aquatique
print(canard.faire_du_bruit()) # Redéfini
```

## Exercices pratiques

### Exercice 1 : Véhicules
Créez une hiérarchie de véhicules :
- Classe `Vehicule` (attributs : marque, année, prix)
- Classe `Voiture` (attribut supplémentaire : nb_portes)
- Classe `Moto` (attribut supplémentaire : cylindree)
- Méthode `description()` à redéfinir dans chaque classe

### Exercice 2 : Comptes bancaires spécialisés
En partant de la classe `CompteBancaire` précédente, créez :
- `CompteEpargne` : avec un taux d'intérêt, méthode `calculer_interets()`
- `CompteCredit` : avec une limite de crédit, redéfinir `retirer()`
- Testez le polymorphisme avec une liste de différents comptes

### Solutions :

```python
# Solution Exercice 1
class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def description(self):
        return f"Véhicule {self.marque} de {self.annee}, prix : {self.prix}€"

    def age(self):
        from datetime import datetime
        return datetime.now().year - self.annee

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, nb_portes):
        super().__init__(marque, annee, prix)
        self.nb_portes = nb_portes

    def description(self):
        base = super().description()
        return f"{base}, {self.nb_portes} portes"

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, cylindree):
        super().__init__(marque, annee, prix)
        self.cylindree = cylindree

    def description(self):
        base = super().description()
        return f"{base}, {self.cylindree}cc"

# Test
vehicules = [
    Voiture("Toyota", 2020, 25000, 4),
    Moto("Honda", 2019, 8000, 600),
    Vehicule("Tesla", 2021, 50000)
]

for vehicule in vehicules:
    print(vehicule.description())
    print(f"Âge : {vehicule.age()} ans")
    print("-" * 30)

# Solution Exercice 2
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            return f"Dépôt de {montant}€ effectué"
        return "Montant invalide"

    def retirer(self, montant):
        if montant > 0 and self.solde >= montant:
            self.solde -= montant
            return f"Retrait de {montant}€ effectué"
        return "Retrait impossible"

    def consulter_solde(self):
        return f"Solde : {self.solde}€"

class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde=0, taux_interet=2.0):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet

    def calculer_interets(self):
        interets = self.solde * (self.taux_interet / 100)
        self.solde += interets
        return f"Intérêts de {interets:.2f}€ ajoutés"

class CompteCredit(CompteBancaire):
    def __init__(self, titulaire, solde=0, limite_credit=1000):
        super().__init__(titulaire, solde)
        self.limite_credit = limite_credit

    def retirer(self, montant):
        if montant > 0 and (self.solde + self.limite_credit) >= montant:
            self.solde -= montant
            return f"Retrait de {montant}€ effectué"
        return "Limite de crédit dépassée"

    def solde_disponible(self):
        return self.solde + self.limite_credit

# Test polymorphisme
comptes = [
    CompteBancaire("Alice", 1000),
    CompteEpargne("Bob", 5000, 1.5),
    CompteCredit("Charlie", 500, 2000)
]

for compte in comptes:
    print(f"Compte de {compte.titulaire}")
    print(compte.consulter_solde())

    if isinstance(compte, CompteEpargne):
        print(compte.calculer_interets())
    elif isinstance(compte, CompteCredit):
        print(f"Solde disponible : {compte.solde_disponible()}€")

    print("-" * 30)
```

## Bonnes pratiques

1. **Utilisez l'héritage pour la relation "est-un"** : un Chien EST un Animal
2. **Préférez la composition pour "a-un"** : une Voiture A un Moteur
3. **Redéfinissez les méthodes de manière cohérente**
4. **Utilisez `super()`** pour réutiliser le code parent
5. **Documentez les méthodes à redéfinir**

```python
class Animal:
    def faire_du_bruit(self):
        """Méthode à redéfinir dans les classes enfants."""
        raise NotImplementedError("Cette méthode doit être redéfinie")
```

## Résumé

Dans cette section, vous avez appris :

✅ **L'héritage** : créer des classes basées sur d'autres classes
✅ **Le polymorphisme** : même interface, comportements différents
✅ **`super()`** : accéder aux méthodes de la classe parent
✅ **Redéfinition de méthodes** : adapter le comportement aux classes enfants
✅ **Vérification de types** : `isinstance()` et `issubclass()`
✅ **Bonnes pratiques** : quand et comment utiliser l'héritage

Dans la prochaine section, nous découvrirons les méthodes spéciales qui permettent d'intégrer vos objets naturellement dans l'écosystème Python !

⏭️
