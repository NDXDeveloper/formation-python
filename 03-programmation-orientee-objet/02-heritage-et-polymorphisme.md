🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.2 Héritage et Polymorphisme

## Introduction

L'**héritage** et le **polymorphisme** sont deux concepts fondamentaux de la Programmation Orientée Objet qui permettent de créer des hiérarchies de classes et de réutiliser du code de manière élégante.

Dans cette section, nous allons découvrir comment ces concepts peuvent vous aider à écrire du code plus organisé, plus facile à maintenir et plus flexible.

## L'Héritage : Qu'est-ce que c'est ?

### Analogie du Monde Réel

Imaginez que vous avez une classification des animaux :
- Tous les **animaux** partagent certaines caractéristiques : ils mangent, dorment, respirent
- Les **mammifères** sont des animaux, mais ils ont des caractéristiques supplémentaires : ils allaitent leurs petits
- Les **chiens** sont des mammifères, mais ils ont encore d'autres caractéristiques : ils aboient, remuent la queue

C'est exactement le principe de l'héritage en programmation : une classe peut **hériter** des attributs et méthodes d'une autre classe, tout en ajoutant ses propres spécificités.

### Pourquoi Utiliser l'Héritage ?

L'héritage permet de :
- **Réutiliser du code** : pas besoin de réécrire les mêmes méthodes dans plusieurs classes
- **Organiser logiquement** : créer des hiérarchies qui reflètent la réalité
- **Faciliter la maintenance** : modifier une fois le code dans la classe parente suffit
- **Étendre les fonctionnalités** : ajouter de nouvelles capacités sans toucher au code existant

## Syntaxe de Base de l'Héritage

### Classe Parente (ou Classe de Base)

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} est en train de manger.")

    def dormir(self):
        print(f"{self.nom} dort paisiblement.")
```

### Classe Enfant (ou Classe Dérivée)

Une classe enfant hérite d'une classe parente en mettant le nom de la classe parente entre parenthèses :

```python
class Chien(Animal):  # Chien hérite de Animal
    def aboyer(self):
        print(f"{self.nom} dit : Wouf wouf !")

# Utilisation
mon_chien = Chien("Rex")  
mon_chien.manger()   # Méthode héritée de Animal  
mon_chien.dormir()   # Méthode héritée de Animal  
mon_chien.aboyer()   # Méthode propre à Chien  
```

**Résultat :**
```
Rex est en train de manger.  
Rex dort paisiblement.  
Rex dit : Wouf wouf !  
```

Le chien peut utiliser toutes les méthodes définies dans la classe `Animal`, même si elles ne sont pas écrites dans la classe `Chien` !

## Exemple Détaillé : Hiérarchie d'Employés

Imaginons un système de gestion d'employés dans une entreprise :

```python
class Employe:
    """Classe de base représentant un employé."""

    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_info(self):
        print(f"Employé : {self.prenom} {self.nom}")
        print(f"Salaire : {self.salaire}€")

    def augmentation(self, pourcentage):
        self.salaire *= (1 + pourcentage / 100)
        print(f"Nouveau salaire : {self.salaire:.2f}€")


class Developpeur(Employe):
    """Un développeur est un employé avec des compétences spécifiques."""

    def __init__(self, nom, prenom, salaire, langage):
        # Appeler le constructeur de la classe parente
        super().__init__(nom, prenom, salaire)
        self.langage = langage

    def afficher_info(self):
        super().afficher_info()
        print(f"Langage principal : {self.langage}")

    def coder(self):
        print(f"{self.prenom} code en {self.langage}...")


class Manager(Employe):
    """Un manager est un employé qui gère une équipe."""

    def __init__(self, nom, prenom, salaire, taille_equipe):
        super().__init__(nom, prenom, salaire)
        self.taille_equipe = taille_equipe

    def afficher_info(self):
        super().afficher_info()
        print(f"Gère une équipe de {self.taille_equipe} personnes")

    def organiser_reunion(self):
        print(f"{self.prenom} organise une réunion d'équipe.")


# Utilisation
dev = Developpeur("Dupont", "Marie", 45000, "Python")  
dev.afficher_info()  
dev.coder()  
dev.augmentation(10)  

print("\n" + "="*40 + "\n")

manager = Manager("Martin", "Pierre", 60000, 8)  
manager.afficher_info()  
manager.organiser_reunion()  
```

**Résultat :**
```
Employé : Marie Dupont  
Salaire : 45000€  
Langage principal : Python  
Marie code en Python...  
Nouveau salaire : 49500.00€  

========================================

Employé : Pierre Martin  
Salaire : 60000€  
Gère une équipe de 8 personnes  
Pierre organise une réunion d'équipe.  
```

## Le Mot-Clé `super()`

Le mot-clé `super()` permet d'accéder aux méthodes de la classe parente. C'est très utile pour :
- Appeler le constructeur de la classe parente
- Étendre (plutôt que remplacer) une méthode de la classe parente

### Utilisation dans le Constructeur

```python
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        print(f"Création d'un véhicule : {marque} {modele}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, nombre_portes):
        # Appeler le constructeur de Vehicule
        super().__init__(marque, modele)
        self.nombre_portes = nombre_portes
        print(f"C'est une voiture avec {nombre_portes} portes")

ma_voiture = Voiture("Renault", "Clio", 5)
```

**Résultat :**
```
Création d'un véhicule : Renault Clio  
C'est une voiture avec 5 portes  
```

### Utilisation dans les Méthodes

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def afficher(self):
        print(f"Rectangle : {self.largeur} x {self.hauteur}")

    def surface(self):
        return self.largeur * self.hauteur


class RectangleColore(Rectangle):
    def __init__(self, largeur, hauteur, couleur):
        super().__init__(largeur, hauteur)
        self.couleur = couleur

    def afficher(self):
        # Appeler d'abord la méthode parente
        super().afficher()
        # Puis ajouter notre propre comportement
        print(f"Couleur : {self.couleur}")

rect = RectangleColore(10, 5, "rouge")  
rect.afficher()  
print(f"Surface : {rect.surface()} cm²")  
```

**Résultat :**
```
Rectangle : 10 x 5  
Couleur : rouge  
Surface : 50 cm²  
```

## Surcharge de Méthodes (Method Overriding)

La **surcharge de méthodes** consiste à redéfinir dans une classe enfant une méthode qui existe déjà dans la classe parente.

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_bruit(self):
        print(f"{self.nom} fait un bruit.")


class Chien(Animal):
    def faire_bruit(self):
        print(f"{self.nom} aboie : Wouf wouf !")


class Chat(Animal):
    def faire_bruit(self):
        print(f"{self.nom} miaule : Miaou miaou !")


class Vache(Animal):
    def faire_bruit(self):
        print(f"{self.nom} meugle : Meuh meuh !")


# Utilisation
rex = Chien("Rex")  
felix = Chat("Felix")  
marguerite = Vache("Marguerite")  

rex.faire_bruit()         # Rex aboie : Wouf wouf !  
felix.faire_bruit()       # Felix miaule : Miaou miaou !  
marguerite.faire_bruit()  # Marguerite meugle : Meuh meuh !  
```

Chaque classe enfant **redéfinit** la méthode `faire_bruit()` avec son propre comportement.

## Le Polymorphisme : Concept Fondamental

Le **polymorphisme** (du grec "plusieurs formes") est la capacité d'utiliser une même interface pour différents types d'objets.

### Polymorphisme en Action

```python
class Forme:
    def __init__(self, nom):
        self.nom = nom

    def calculer_surface(self):
        pass  # À redéfinir dans les classes enfants

    def afficher(self):
        print(f"{self.nom} - Surface : {self.calculer_surface()} cm²")


class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14159 * self.rayon ** 2


class Carre(Forme):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def calculer_surface(self):
        return self.cote ** 2


class Triangle(Forme):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def calculer_surface(self):
        return (self.base * self.hauteur) / 2


# Le polymorphisme en action !
formes = [
    Cercle(5),
    Carre(4),
    Triangle(6, 3)
]

# Même boucle pour tous les types de formes
for forme in formes:
    forme.afficher()  # Chaque forme calcule sa surface différemment
```

**Résultat :**
```
Cercle - Surface : 78.53975 cm²  
Carré - Surface : 16 cm²  
Triangle - Surface : 9.0 cm²  
```

**Pourquoi c'est puissant ?** On peut traiter différents types d'objets de la même manière, sans se soucier de leur type spécifique. Le bon comportement est automatiquement choisi selon le type de l'objet.

## Exemple Pratique : Système de Paiement

Un excellent exemple du polymorphisme est un système de paiement qui accepte différents moyens de paiement :

```python
class MoyenPaiement:
    """Classe de base pour tous les moyens de paiement."""

    def __init__(self, montant):
        self.montant = montant

    def payer(self):
        """Méthode à redéfinir dans chaque classe enfant."""
        pass

    def afficher_recu(self):
        print(f"Paiement de {self.montant}€ effectué.")


class CarteBancaire(MoyenPaiement):
    def __init__(self, montant, numero_carte):
        super().__init__(montant)
        self.numero_carte = numero_carte

    def payer(self):
        # Masquer les chiffres de la carte
        carte_masquee = "**** **** **** " + self.numero_carte[-4:]
        print(f"Paiement par carte bancaire ({carte_masquee})")
        self.afficher_recu()


class PayPal(MoyenPaiement):
    def __init__(self, montant, email):
        super().__init__(montant)
        self.email = email

    def payer(self):
        print(f"Paiement via PayPal avec le compte : {self.email}")
        self.afficher_recu()


class Especes(MoyenPaiement):
    def __init__(self, montant):
        super().__init__(montant)

    def payer(self):
        print(f"Paiement en espèces")
        self.afficher_recu()


class Cheque(MoyenPaiement):
    def __init__(self, montant, numero_cheque):
        super().__init__(montant)
        self.numero_cheque = numero_cheque

    def payer(self):
        print(f"Paiement par chèque n°{self.numero_cheque}")
        self.afficher_recu()


# Fonction qui accepte N'IMPORTE QUEL moyen de paiement
def traiter_paiement(moyen_paiement):
    """Cette fonction fonctionne avec tous les types de paiement !"""
    print("\n--- Traitement du paiement ---")
    moyen_paiement.payer()
    print("--- Paiement terminé ---\n")


# Utilisation avec différents moyens de paiement
paiements = [
    CarteBancaire(150.50, "1234567890123456"),
    PayPal(75.00, "user@example.com"),
    Especes(30.00),
    Cheque(200.00, "CH123456")
]

# La même fonction traite tous les types de paiement !
for paiement in paiements:
    traiter_paiement(paiement)
```

**Résultat :**
```
--- Traitement du paiement ---
Paiement par carte bancaire (**** **** **** 3456)  
Paiement de 150.5€ effectué.  
--- Paiement terminé ---

--- Traitement du paiement ---
Paiement via PayPal avec le compte : user@example.com  
Paiement de 75.0€ effectué.  
--- Paiement terminé ---

--- Traitement du paiement ---
Paiement en espèces  
Paiement de 30.0€ effectué.  
--- Paiement terminé ---

--- Traitement du paiement ---
Paiement par chèque n°CH123456  
Paiement de 200.0€ effectué.  
--- Paiement terminé ---
```

## Vérification du Type et de l'Héritage

Python fournit des fonctions pour vérifier les relations d'héritage :

### `isinstance()` : Vérifier le Type d'un Objet

```python
class Animal:
    pass

class Chien(Animal):
    pass

class Chat(Animal):
    pass

rex = Chien()  
felix = Chat()  

print(isinstance(rex, Chien))     # True  
print(isinstance(rex, Animal))    # True (un Chien est aussi un Animal)  
print(isinstance(rex, Chat))      # False  
print(isinstance(felix, Chat))    # True  
print(isinstance(felix, Animal))  # True  
```

### `issubclass()` : Vérifier l'Héritage entre Classes

```python
print(issubclass(Chien, Animal))  # True  
print(issubclass(Chat, Animal))   # True  
print(issubclass(Chien, Chat))    # False  
print(issubclass(Animal, Chien))  # False  
```

## Héritage Multiple

Python permet à une classe d'hériter de **plusieurs** classes parentes en même temps. C'est l'héritage multiple.

```python
class Volant:
    def voler(self):
        print("Je vole dans les airs !")


class Nageant:
    def nager(self):
        print("Je nage dans l'eau !")


class Canard(Volant, Nageant):  # Hérite de deux classes
    def __init__(self, nom):
        self.nom = nom

    def caqueter(self):
        print(f"{self.nom} fait : Coin coin !")


# Utilisation
donald = Canard("Donald")  
donald.caqueter()  # Méthode propre  
donald.voler()     # Héritée de Volant  
donald.nager()     # Héritée de Nageant  
```

**Résultat :**
```
Donald fait : Coin coin !  
Je vole dans les airs !  
Je nage dans l'eau !  
```

### Attention avec l'Héritage Multiple

L'héritage multiple peut devenir complexe. En cas de conflit (deux classes parentes ont une méthode de même nom), Python utilise le **MRO** (Method Resolution Order) pour déterminer quelle méthode appeler.

```python
class A:
    def methode(self):
        print("Méthode de A")

class B:
    def methode(self):
        print("Méthode de B")

class C(A, B):  # C hérite de A et B
    pass

obj = C()  
obj.methode()  # Quelle méthode sera appelée ?  
# Affiche : "Méthode de A" (A est mentionné en premier)

# Voir l'ordre de résolution des méthodes
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

**Bonne pratique** : L'héritage multiple est puissant mais peut rendre le code difficile à comprendre. Utilisez-le avec parcimonie.

## Exemple Avancé : Système de Fichiers

Voici un exemple plus élaboré qui combine héritage et polymorphisme :

```python
from datetime import datetime

class ElementSysteme:
    """Classe de base pour tous les éléments du système de fichiers."""

    def __init__(self, nom):
        self.nom = nom
        self.date_creation = datetime.now()

    def afficher_info(self):
        print(f"Nom : {self.nom}")
        print(f"Créé le : {self.date_creation.strftime('%d/%m/%Y %H:%M')}")

    def obtenir_type(self):
        """À redéfinir dans les classes enfants."""
        return "Élément"


class Fichier(ElementSysteme):
    """Représente un fichier."""

    def __init__(self, nom, taille, extension):
        super().__init__(nom)
        self.taille = taille  # en Ko
        self.extension = extension

    def afficher_info(self):
        super().afficher_info()
        print(f"Type : Fichier (.{self.extension})")
        print(f"Taille : {self.taille} Ko")

    def obtenir_type(self):
        return "Fichier"

    def ouvrir(self):
        print(f"Ouverture du fichier {self.nom}.{self.extension}...")


class Dossier(ElementSysteme):
    """Représente un dossier pouvant contenir des fichiers et d'autres dossiers."""

    def __init__(self, nom):
        super().__init__(nom)
        self.contenu = []

    def ajouter(self, element):
        """Ajoute un élément (fichier ou dossier) dans ce dossier."""
        self.contenu.append(element)
        print(f"{element.nom} ajouté dans {self.nom}")

    def afficher_info(self):
        super().afficher_info()
        print(f"Type : Dossier")
        print(f"Contient {len(self.contenu)} éléments")

    def obtenir_type(self):
        return "Dossier"

    def lister_contenu(self):
        if not self.contenu:
            print(f"Le dossier {self.nom} est vide.")
            return

        print(f"\nContenu de '{self.nom}' :")
        print("-" * 40)
        for element in self.contenu:
            type_elem = element.obtenir_type()
            print(f"  [{type_elem}] {element.nom}")

    def calculer_taille_totale(self):
        """Calcule la taille totale du dossier."""
        taille = 0
        for element in self.contenu:
            if isinstance(element, Fichier):
                taille += element.taille
            elif isinstance(element, Dossier):
                taille += element.calculer_taille_totale()
        return taille


class FichierImage(Fichier):
    """Représente un fichier image avec des propriétés spécifiques."""

    def __init__(self, nom, taille, extension, largeur, hauteur):
        super().__init__(nom, taille, extension)
        self.largeur = largeur
        self.hauteur = hauteur

    def afficher_info(self):
        super().afficher_info()
        print(f"Dimensions : {self.largeur} x {self.hauteur} pixels")

    def afficher_apercu(self):
        print(f"Aperçu de l'image {self.nom} ({self.largeur}x{self.hauteur})")


# Utilisation du système
print("=== Création du système de fichiers ===\n")

# Créer des fichiers
doc1 = Fichier("rapport", 150, "pdf")  
doc2 = Fichier("presentation", 300, "pptx")  
image1 = FichierImage("photo_vacances", 2500, "jpg", 1920, 1080)  
image2 = FichierImage("logo", 50, "png", 512, 512)  

# Créer des dossiers
dossier_documents = Dossier("Documents")  
dossier_images = Dossier("Images")  
dossier_principal = Dossier("Mon_Ordinateur")  

# Organiser les fichiers
dossier_documents.ajouter(doc1)  
dossier_documents.ajouter(doc2)  
dossier_images.ajouter(image1)  
dossier_images.ajouter(image2)  
dossier_principal.ajouter(dossier_documents)  
dossier_principal.ajouter(dossier_images)  

print("\n" + "="*50)
# Lister le contenu
dossier_principal.lister_contenu()  
dossier_images.lister_contenu()  

print("\n" + "="*50)
# Afficher les infos d'un fichier image
print("\nInformations détaillées :")  
image1.afficher_info()  

print("\n" + "="*50)
# Calculer la taille totale
taille_totale = dossier_principal.calculer_taille_totale()  
print(f"\nTaille totale de '{dossier_principal.nom}' : {taille_totale} Ko")  
```

**Résultat :**
```
=== Création du système de fichiers ===

rapport ajouté dans Documents  
presentation ajouté dans Documents  
photo_vacances ajouté dans Images  
logo ajouté dans Images  
Documents ajouté dans Mon_Ordinateur  
Images ajouté dans Mon_Ordinateur  

==================================================

Contenu de 'Mon_Ordinateur' :
----------------------------------------
  [Dossier] Documents
  [Dossier] Images

Contenu de 'Images' :
----------------------------------------
  [Fichier] photo_vacances
  [Fichier] logo

==================================================

Informations détaillées :  
Nom : photo_vacances  
Créé le : 27/10/2025 14:30  
Type : Fichier (.jpg)  
Taille : 2500 Ko  
Dimensions : 1920 x 1080 pixels  

==================================================

Taille totale de 'Mon_Ordinateur' : 3000 Ko
```

## Avantages de l'Héritage et du Polymorphisme

### 1. Réutilisation du Code

```python
# Sans héritage - Code répétitif
class Chien:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} mange.")

    def dormir(self):
        print(f"{self.nom} dort.")

class Chat:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):  # Code répété !
        print(f"{self.nom} mange.")

    def dormir(self):  # Code répété !
        print(f"{self.nom} dort.")

# Avec héritage - Code réutilisé
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} mange.")

    def dormir(self):
        print(f"{self.nom} dort.")

class Chien(Animal):
    pass  # Hérite de tout !

class Chat(Animal):
    pass  # Hérite de tout !
```

### 2. Maintenance Facilitée

Si vous devez modifier le comportement de `manger()`, avec l'héritage vous ne le faites qu'une seule fois dans la classe `Animal`.

### 3. Extensibilité

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

# Ajouter de nouveaux types d'animaux est facile
class Oiseau(Animal):
    def voler(self):
        print(f"{self.nom} vole.")

class Poisson(Animal):
    def nager(self):
        print(f"{self.nom} nage.")
```

### 4. Polymorphisme pour du Code Générique

```python
def nourrir_animaux(liste_animaux):
    """Fonction qui fonctionne avec tous les types d'animaux."""
    for animal in liste_animaux:
        animal.manger()  # Peu importe le type exact

animaux = [Chien("Rex"), Chat("Felix"), Oiseau("Tweety")]  
nourrir_animaux(animaux)  
```

## Bonnes Pratiques

### 1. Principe "Est-un" (Is-A Relationship)

L'héritage doit refléter une relation "est-un" :
- Un Chien **est un** Animal ✓
- Un Développeur **est un** Employé ✓
- Une Voiture **est un** Véhicule ✓

> ⚠️ **Piège classique** : on pourrait penser qu'un Carré "est un" Rectangle, mais hériter `Carre` de `Rectangle` pose problème. Si on change la largeur d'un carré sans changer la hauteur, il cesse d'être un carré. Ce genre de subtilité est lié au *principe de substitution de Liskov*.

Contre-exemple à éviter :
- Un Employé **est un** Salaire ✗ (un employé a un salaire, mais n'est pas un salaire)

```python
# ✓ Bon
class Animal:
    pass

class Chien(Animal):  # Un chien est un animal
    pass

# ✗ À éviter
class Salaire:
    pass

class Employe(Salaire):  # Un employé n'est pas un salaire !
    pass

# ✓ Mieux : composition
class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire  # Un employé HAS-A salaire
```

### 2. Ne Pas Trop Approfondir la Hiérarchie

Évitez les hiérarchies trop profondes qui rendent le code difficile à comprendre :

```python
# ✗ Trop profond
class Etre:
    pass

class EtreVivant(Etre):
    pass

class Animal(EtreVivant):
    pass

class Mammifere(Animal):
    pass

class Carnivore(Mammifere):
    pass

class Canide(Carnivore):
    pass

class Chien(Canide):
    pass

# ✓ Plus simple et suffisant
class Animal:
    pass

class Chien(Animal):
    pass
```

### 3. Utiliser `super()` Correctement

Toujours utiliser `super()` plutôt que d'appeler directement la classe parente :

```python
# ✗ À éviter
class Chien(Animal):
    def __init__(self, nom, race):
        Animal.__init__(self, nom)  # Appel direct
        self.race = race

# ✓ Préférable
class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)  # Utiliser super()
        self.race = race
```

### 4. Documenter les Classes

```python
class Vehicule:
    """
    Classe de base pour tous les véhicules.

    Attributs:
        marque (str): La marque du véhicule
        modele (str): Le modèle du véhicule
    """

    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        """Démarre le véhicule."""
        print(f"{self.marque} {self.modele} démarre.")
```

## Quand Utiliser l'Héritage vs la Composition

L'héritage n'est pas toujours la meilleure solution. Parfois, la **composition** est préférable.

### Héritage : Relation "Est-Un"

```python
class Animal:
    def respirer(self):
        print("Respire...")

class Chien(Animal):  # Un chien EST UN animal
    def aboyer(self):
        print("Wouf !")
```

### Composition : Relation "A-Un"

```python
class Moteur:
    def demarrer(self):
        print("Moteur démarré")

class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # Une voiture A UN moteur

    def demarrer(self):
        self.moteur.demarrer()
```

**Règle générale** : Préférez la composition à l'héritage quand c'est possible. L'héritage crée un couplage fort entre les classes.

## Résumé des Concepts Clés

### Héritage
- Permet à une classe d'hériter des attributs et méthodes d'une autre classe
- Syntaxe : `class Enfant(Parent):`
- La classe enfant peut utiliser tout ce qui est défini dans la classe parente
- Permet la réutilisation du code et l'organisation logique

### `super()`
- Permet d'accéder aux méthodes de la classe parente
- Utilisé principalement dans `__init__` et pour étendre des méthodes
- Syntaxe : `super().methode()`

### Surcharge de Méthodes
- Redéfinir une méthode de la classe parente dans la classe enfant
- La nouvelle définition remplace l'ancienne
- Permet de spécialiser le comportement

### Polymorphisme
- Capacité à utiliser des objets de différents types via une interface commune
- Permet d'écrire du code générique qui fonctionne avec plusieurs types
- Le bon comportement est choisi automatiquement selon le type réel de l'objet

### Héritage Multiple
- Une classe peut hériter de plusieurs classes parentes
- Syntaxe : `class Enfant(Parent1, Parent2):`
- À utiliser avec précaution car peut compliquer le code

## Conclusion

L'héritage et le polymorphisme sont des outils puissants qui permettent de :
- **Structurer** votre code de manière logique et hiérarchique
- **Réutiliser** du code efficacement
- **Étendre** les fonctionnalités sans modifier le code existant
- **Écrire** du code générique et flexible

Ces concepts sont au cœur de la Programmation Orientée Objet et vous les retrouverez dans pratiquement tous les programmes Python de taille moyenne ou grande.

La clé est de les utiliser judicieusement : l'héritage doit refléter une vraie relation "est-un", et le polymorphisme doit servir à simplifier votre code, pas à le compliquer.

Dans la prochaine section, nous explorerons les **méthodes spéciales** (dunder methods) qui permettent de personnaliser encore plus le comportement de vos classes !

⏭️ [Méthodes spéciales (dunder methods)](/03-programmation-orientee-objet/03-methodes-speciales.md)
