🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.1 : Classes et objets

## Introduction

Imaginez que vous vouliez créer un programme pour gérer les informations d'une bibliothèque. Vous pourriez avoir des livres, des auteurs, des emprunts... Comment organiser tout cela de manière logique et réutilisable ? C'est exactement le problème que les classes et objets viennent résoudre !

## Qu'est-ce qu'une classe ?

Une **classe** est comme un plan ou un modèle qui décrit :
- Les **caractéristiques** (appelées attributs) d'un type d'objet
- Les **actions** (appelées méthodes) que cet objet peut effectuer

Pensez à une classe comme à un plan d'architecte : le plan décrit comment construire une maison, mais ce n'est pas la maison elle-même.

## Qu'est-ce qu'un objet ?

Un **objet** est une instance concrète d'une classe. Si la classe est le plan, l'objet est la maison construite à partir de ce plan.

Vous pouvez créer plusieurs objets (instances) à partir d'une même classe, chacun avec ses propres valeurs.

## Créer votre première classe

Commençons par un exemple simple : une classe `Chien`.

```python
class Chien:
    # Ceci est une classe vide pour l'instant
    pass
```

### Explication :
- `class` : mot-clé pour déclarer une classe
- `Chien` : nom de la classe (convention : première lettre en majuscule)
- `pass` : instruction qui ne fait rien (placeholder)

## Créer des objets (instances)

```python
# Créer des objets à partir de la classe Chien
mon_chien = Chien()
autre_chien = Chien()

print(type(mon_chien))  # <class '__main__.Chien'>
print(mon_chien == autre_chien)  # False (objets différents)
```

## Ajouter des attributs

Les attributs sont les caractéristiques de nos objets. Il y a deux types principaux :

### 1. Attributs d'instance

Chaque objet a ses propres valeurs pour ces attributs.

```python
class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom      # Attribut d'instance
        self.race = race    # Attribut d'instance
        self.age = age      # Attribut d'instance
```

### La méthode `__init__` (constructeur)

- `__init__` est une méthode spéciale appelée automatiquement lors de la création d'un objet
- `self` fait référence à l'objet en cours de création
- Les autres paramètres sont les valeurs à assigner aux attributs

### Exemple complet :

```python
class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

# Créer des objets avec des valeurs
mon_chien = Chien("Rex", "Berger Allemand", 3)
autre_chien = Chien("Bella", "Labrador", 2)

# Accéder aux attributs
print(mon_chien.nom)    # Rex
print(autre_chien.race) # Labrador
```

### 2. Attributs de classe

Ces attributs sont partagés par toutes les instances de la classe.

```python
class Chien:
    # Attribut de classe
    espece = "Canis lupus"

    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

# Tous les chiens ont la même espèce
print(Chien.espece)        # Canis lupus
print(mon_chien.espece)    # Canis lupus
print(autre_chien.espece)  # Canis lupus
```

## Ajouter des méthodes

Les méthodes sont les actions que peuvent effectuer nos objets.

```python
class Chien:
    espece = "Canis lupus"

    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        return f"{self.nom} dit : Woof!"

    def se_presenter(self):
        return f"Je suis {self.nom}, un {self.race} de {self.age} ans."

    def vieillir(self):
        self.age += 1
        return f"{self.nom} a maintenant {self.age} ans."

# Utilisation
mon_chien = Chien("Rex", "Berger Allemand", 3)

print(mon_chien.aboyer())        # Rex dit : Woof!
print(mon_chien.se_presenter())  # Je suis Rex, un Berger Allemand de 3 ans.
print(mon_chien.vieillir())      # Rex a maintenant 4 ans.
```

### Points importants sur les méthodes :

1. **`self`** : premier paramètre de toute méthode d'instance
2. **`self`** fait référence à l'objet qui appelle la méthode
3. Les méthodes peuvent accéder et modifier les attributs de l'objet

## Exemple pratique : Classe Livre

Créons une classe plus complète pour notre exemple de bibliothèque :

```python
class Livre:
    def __init__(self, titre, auteur, annee_publication, pages):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.pages = pages
        self.emprunte = False  # État par défaut

    def emprunter(self):
        if not self.emprunte:
            self.emprunte = True
            return f"'{self.titre}' a été emprunté."
        else:
            return f"'{self.titre}' est déjà emprunté."

    def rendre(self):
        if self.emprunte:
            self.emprunte = False
            return f"'{self.titre}' a été rendu."
        else:
            return f"'{self.titre}' n'était pas emprunté."

    def description(self):
        statut = "emprunté" if self.emprunte else "disponible"
        return f"'{self.titre}' par {self.auteur} ({self.annee_publication}) - {self.pages} pages - {statut}"

# Utilisation
livre1 = Livre("1984", "George Orwell", 1949, 328)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 96)

print(livre1.description())
# '1984' par George Orwell (1949) - 328 pages - disponible

print(livre1.emprunter())
# '1984' a été emprunté.

print(livre1.description())
# '1984' par George Orwell (1949) - 328 pages - emprunté
```

## Accéder et modifier les attributs

```python
# Accès direct aux attributs
print(livre1.titre)      # 1984
print(livre1.auteur)     # George Orwell

# Modification des attributs
livre1.pages = 350
print(livre1.pages)      # 350

# Attention : on peut aussi créer de nouveaux attributs
livre1.genre = "Science-fiction"
print(livre1.genre)      # Science-fiction
```

## Méthodes vs Fonctions

La différence principale :

```python
# Fonction classique
def dire_bonjour(nom):
    return f"Bonjour {nom}!"

# Méthode de classe
class Personne:
    def __init__(self, nom):
        self.nom = nom

    def dire_bonjour(self):
        return f"Bonjour, je suis {self.nom}!"

# Utilisation
print(dire_bonjour("Alice"))  # Fonction
personne = Personne("Bob")
print(personne.dire_bonjour())  # Méthode
```

## Exercices pratiques

### Exercice 1 : Classe Voiture
Créez une classe `Voiture` avec :
- Attributs : marque, modèle, année, kilométrage
- Méthodes :
  - `demarrer()` : affiche "La voiture démarre"
  - `rouler(distance)` : ajoute la distance au kilométrage
  - `info()` : affiche toutes les informations

### Exercice 2 : Classe CompteBancaire
Créez une classe `CompteBancaire` avec :
- Attributs : titulaire, solde (initial à 0)
- Méthodes :
  - `deposer(montant)` : ajoute de l'argent
  - `retirer(montant)` : retire de l'argent (vérifier que le solde est suffisant)
  - `consulter_solde()` : affiche le solde actuel

### Solutions :

```python
# Solution Exercice 1
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage=0):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def demarrer(self):
        return "La voiture démarre"

    def rouler(self, distance):
        self.kilometrage += distance
        return f"Vous avez roulé {distance} km. Kilométrage total : {self.kilometrage} km"

    def info(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.kilometrage} km"

# Test
ma_voiture = Voiture("Toyota", "Prius", 2020)
print(ma_voiture.demarrer())
print(ma_voiture.rouler(150))
print(ma_voiture.info())

# Solution Exercice 2
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            return f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€"
        else:
            return "Le montant doit être positif"

    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                return f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€"
            else:
                return "Solde insuffisant"
        else:
            return "Le montant doit être positif"

    def consulter_solde(self):
        return f"Solde du compte de {self.titulaire} : {self.solde}€"

# Test
compte = CompteBancaire("Alice", 1000)
print(compte.consulter_solde())
print(compte.deposer(200))
print(compte.retirer(50))
print(compte.consulter_solde())
```

## Bonnes pratiques

1. **Nommage des classes** : PascalCase (première lettre de chaque mot en majuscule)
2. **Nommage des attributs/méthodes** : snake_case (mots séparés par des underscores)
3. **Docstrings** : documenter vos classes et méthodes
4. **Initialisation** : toujours initialiser les attributs dans `__init__`

```python
class Etudiant:
    """Classe représentant un étudiant."""

    def __init__(self, nom, prenom, age):
        """Initialise un nouvel étudiant."""
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.notes = []

    def ajouter_note(self, note):
        """Ajoute une note à l'étudiant."""
        if 0 <= note <= 20:
            self.notes.append(note)
            return f"Note {note} ajoutée"
        else:
            return "La note doit être entre 0 et 20"

    def calculer_moyenne(self):
        """Calcule la moyenne des notes."""
        if self.notes:
            return sum(self.notes) / len(self.notes)
        else:
            return 0
```

## Résumé

Dans cette section, vous avez appris :

✅ **Qu'est-ce qu'une classe** : un modèle pour créer des objets
✅ **Qu'est-ce qu'un objet** : une instance d'une classe
✅ **Le constructeur `__init__`** : pour initialiser les objets
✅ **Les attributs** : les caractéristiques des objets
✅ **Les méthodes** : les actions que peuvent effectuer les objets
✅ **La différence entre attributs de classe et d'instance**
✅ **Les bonnes pratiques** de nommage et de documentation

Dans la prochaine section, nous verrons comment les classes peuvent hériter les unes des autres pour créer des hiérarchies plus complexes et réutilisables !

⏭️
