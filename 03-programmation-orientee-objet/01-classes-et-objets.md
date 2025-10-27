🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 3.1 Classes et Objets en Python

## Introduction à la Programmation Orientée Objet

La **Programmation Orientée Objet (POO)** est un paradigme de programmation qui permet d'organiser votre code de manière plus structurée et réutilisable. Au lieu de manipuler simplement des données et des fonctions séparées, la POO vous permet de créer des **objets** qui regroupent à la fois des données (attributs) et des comportements (méthodes).

Imaginez que vous voulez modéliser une voiture dans votre programme. Avec la POO, vous pouvez créer un "modèle" de voiture (une **classe**) qui définit ce qu'est une voiture en général, puis créer des voitures spécifiques (des **objets**) à partir de ce modèle.

## Qu'est-ce qu'une Classe ?

Une **classe** est comme un plan de construction ou un moule. Elle définit la structure et le comportement d'un type d'objet, mais elle n'est pas l'objet lui-même.

Par analogie :
- Une classe est comme un **plan d'architecte** pour une maison
- Une classe est comme un **moule à gâteau**
- Une classe est comme une **recette de cuisine**

En Python, on définit une classe avec le mot-clé `class` :

```python
class Voiture:
    pass  # On verra le contenu plus tard
```

## Qu'est-ce qu'un Objet ?

Un **objet** est une **instance** d'une classe. C'est une réalisation concrète du modèle défini par la classe.

En reprenant les analogies :
- Un objet est une **maison construite** à partir du plan
- Un objet est un **gâteau** fait avec le moule
- Un objet est un **plat cuisiné** suivant la recette

```python
# Créer un objet à partir de la classe Voiture
ma_voiture = Voiture()
```

## Première Classe Simple

Créons notre première classe avec des attributs et des méthodes :

```python
class Chien:
    # Ceci est une classe qui représente un chien
    pass
```

Pour créer un objet (une instance) de cette classe :

```python
mon_chien = Chien()
print(mon_chien)  # <__main__.Chien object at 0x...>
```

Pour l'instant, notre classe est vide. Ajoutons-lui des caractéristiques !

## Le Constructeur : La Méthode `__init__`

Le **constructeur** est une méthode spéciale qui est automatiquement appelée quand on crée un nouvel objet. En Python, cette méthode s'appelle `__init__`.

```python
class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
```

Maintenant, quand on crée un chien, on peut lui donner un nom et un âge :

```python
mon_chien = Chien("Rex", 5)
print(mon_chien.nom)  # Affiche : Rex
print(mon_chien.age)  # Affiche : 5
```

### Comprendre `self`

Le mot `self` représente **l'instance elle-même**. C'est une référence à l'objet qui est en train d'être manipulé.

Quand vous écrivez :
```python
mon_chien = Chien("Rex", 5)
```

Python fait en réalité :
```python
Chien.__init__(mon_chien, "Rex", 5)
```

Le `self` dans la définition de la méthode correspond à `mon_chien` lors de l'appel. C'est comme si l'objet disait "moi-même".

**Important** : `self` doit toujours être le premier paramètre de toutes les méthodes d'instance, mais vous n'avez pas besoin de le passer explicitement quand vous appelez la méthode.

## Les Attributs d'Instance

Les **attributs d'instance** sont des variables qui appartiennent à un objet spécifique. Chaque objet a ses propres valeurs d'attributs.

```python
class Chien:
    def __init__(self, nom, age, race):
        self.nom = nom      # Attribut d'instance
        self.age = age      # Attribut d'instance
        self.race = race    # Attribut d'instance

# Créer deux chiens différents
chien1 = Chien("Rex", 5, "Berger Allemand")
chien2 = Chien("Bella", 3, "Labrador")

print(chien1.nom)   # Rex
print(chien2.nom)   # Bella
print(chien1.race)  # Berger Allemand
print(chien2.race)  # Labrador
```

Chaque chien a ses propres attributs, indépendants les uns des autres.

## Les Méthodes d'Instance

Les **méthodes** sont des fonctions définies à l'intérieur d'une classe. Elles représentent les comportements ou actions que peut effectuer un objet.

```python
class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def aboyer(self):
        print(f"{self.nom} dit : Wouf wouf !")

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

    def vieillir(self):
        self.age += 1
        print(f"{self.nom} a maintenant {self.age} ans.")

# Utilisation
mon_chien = Chien("Rex", 5)
mon_chien.aboyer()          # Rex dit : Wouf wouf !
mon_chien.se_presenter()    # Je m'appelle Rex et j'ai 5 ans.
mon_chien.vieillir()        # Rex a maintenant 6 ans.
```

Notez que :
- Les méthodes ont toujours `self` comme premier paramètre
- On accède aux attributs de l'objet via `self.nom_attribut`
- On appelle les méthodes avec la notation pointée : `objet.methode()`

## Les Attributs de Classe

Les **attributs de classe** sont partagés par toutes les instances d'une classe. Ils sont définis directement dans la classe, en dehors de `__init__`.

```python
class Chien:
    # Attribut de classe
    espece = "Canis familiaris"
    nombre_pattes = 4

    def __init__(self, nom, age):
        # Attributs d'instance
        self.nom = nom
        self.age = age

chien1 = Chien("Rex", 5)
chien2 = Chien("Bella", 3)

print(chien1.espece)        # Canis familiaris
print(chien2.espece)        # Canis familiaris
print(Chien.espece)         # Canis familiaris
print(Chien.nombre_pattes)  # 4
```

**Différence clé** :
- **Attributs de classe** : partagés par tous les objets, même valeur pour tous
- **Attributs d'instance** : propres à chaque objet, peuvent être différents

## Exemple Complet : Classe Compte Bancaire

Voici un exemple plus complet qui illustre tous les concepts :

```python
class CompteBancaire:
    # Attribut de classe
    taux_interet = 0.02  # 2% d'intérêt

    def __init__(self, titulaire, solde_initial=0):
        # Attributs d'instance
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(f"Dépôt : +{montant}€")
            print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        if montant > 0:
            if montant <= self.solde:
                self.solde -= montant
                self.historique.append(f"Retrait : -{montant}€")
                print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")
            else:
                print("Solde insuffisant !")
        else:
            print("Le montant doit être positif.")

    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde}€")

    def appliquer_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        self.historique.append(f"Intérêts : +{interets:.2f}€")
        print(f"Intérêts de {interets:.2f}€ appliqués.")

    def afficher_historique(self):
        print(f"Historique du compte de {self.titulaire} :")
        for operation in self.historique:
            print(f"  - {operation}")

# Utilisation
compte1 = CompteBancaire("Alice", 1000)
compte1.afficher_solde()       # Compte de Alice : 1000€
compte1.deposer(500)           # Dépôt de 500€ effectué. Nouveau solde : 1500€
compte1.retirer(200)           # Retrait de 200€ effectué. Nouveau solde : 1300€
compte1.appliquer_interets()   # Intérêts de 26.00€ appliqués.
compte1.afficher_historique()  # Affiche tout l'historique

compte2 = CompteBancaire("Bob", 500)
compte2.afficher_solde()       # Compte de Bob : 500€
```

## Exemple : Classe Personne

Un autre exemple classique pour bien comprendre :

```python
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

    def avoir_anniversaire(self):
        self.age += 1
        print(f"Joyeux anniversaire ! {self.prenom} a maintenant {self.age} ans.")

    def est_majeur(self):
        return self.age >= 18

# Créer plusieurs personnes
personne1 = Personne("Dupont", "Marie", 25)
personne2 = Personne("Martin", "Pierre", 17)

personne1.se_presenter()        # Bonjour, je m'appelle Marie Dupont et j'ai 25 ans.
personne2.se_presenter()        # Bonjour, je m'appelle Pierre Martin et j'ai 17 ans.

print(personne1.est_majeur())   # True
print(personne2.est_majeur())   # False

personne2.avoir_anniversaire()  # Joyeux anniversaire ! Pierre a maintenant 18 ans.
print(personne2.est_majeur())   # True
```

## Modification des Attributs

Vous pouvez modifier les attributs d'un objet directement :

```python
class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.kilometrage = 0

    def afficher_info(self):
        print(f"{self.marque} {self.couleur}, {self.kilometrage} km")

ma_voiture = Voiture("Renault", "rouge")
ma_voiture.afficher_info()      # Renault rouge, 0 km

# Modifier un attribut
ma_voiture.couleur = "bleu"
ma_voiture.kilometrage = 15000

ma_voiture.afficher_info()      # Renault bleu, 15000 km
```

## Plusieurs Instances Indépendantes

Il est important de comprendre que chaque instance est **indépendante** :

```python
class Compteur:
    def __init__(self, valeur_initiale=0):
        self.valeur = valeur_initiale

    def incrementer(self):
        self.valeur += 1

    def afficher(self):
        print(f"Valeur : {self.valeur}")

compteur1 = Compteur()
compteur2 = Compteur(10)

compteur1.incrementer()
compteur1.incrementer()
compteur2.incrementer()

compteur1.afficher()  # Valeur : 2
compteur2.afficher()  # Valeur : 11
```

Même si les deux objets sont créés à partir de la même classe, leurs attributs sont complètement indépendants.

## Bonnes Pratiques

### 1. Noms de Classe en CamelCase
Les noms de classes utilisent la convention CamelCase (première lettre de chaque mot en majuscule) :

```python
class VoitureElectrique:  # ✓ Correct
    pass

class voiture_electrique:  # ✗ À éviter
    pass
```

### 2. Initialiser tous les attributs dans `__init__`
Il est préférable de définir tous les attributs d'instance dans le constructeur :

```python
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.pages_lues = 0  # Même avec une valeur par défaut
        self.termine = False
```

### 3. Utiliser des méthodes pour modifier les attributs
Plutôt que de modifier directement les attributs, créez des méthodes :

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def modifier_dimensions(self, nouvelle_largeur, nouvelle_hauteur):
        if nouvelle_largeur > 0 and nouvelle_hauteur > 0:
            self.largeur = nouvelle_largeur
            self.hauteur = nouvelle_hauteur
        else:
            print("Les dimensions doivent être positives !")

    def calculer_surface(self):
        return self.largeur * self.hauteur
```

### 4. Documentation avec des docstrings
Documentez vos classes et méthodes :

```python
class Etudiant:
    """
    Classe représentant un étudiant.

    Attributs:
        nom (str): Le nom de famille de l'étudiant
        prenom (str): Le prénom de l'étudiant
        notes (list): Liste des notes obtenues
    """

    def __init__(self, nom, prenom):
        """Initialise un nouvel étudiant."""
        self.nom = nom
        self.prenom = prenom
        self.notes = []

    def ajouter_note(self, note):
        """
        Ajoute une note à l'étudiant.

        Args:
            note (float): La note à ajouter (entre 0 et 20)
        """
        if 0 <= note <= 20:
            self.notes.append(note)
        else:
            print("La note doit être entre 0 et 20.")

    def moyenne(self):
        """
        Calcule la moyenne des notes.

        Returns:
            float: La moyenne des notes, ou 0 si aucune note
        """
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)
```

## Exemple Pratique : Gestionnaire de Tâches

Voici un exemple complet d'application des concepts :

```python
class Tache:
    """Représente une tâche à accomplir."""

    def __init__(self, titre, description=""):
        self.titre = titre
        self.description = description
        self.terminee = False

    def marquer_terminee(self):
        self.terminee = True
        print(f"✓ Tâche '{self.titre}' marquée comme terminée.")

    def marquer_non_terminee(self):
        self.terminee = False
        print(f"○ Tâche '{self.titre}' marquée comme non terminée.")

    def afficher(self):
        statut = "✓" if self.terminee else "○"
        print(f"{statut} {self.titre}")
        if self.description:
            print(f"  Description : {self.description}")


class GestionnaireTaches:
    """Gère une liste de tâches."""

    def __init__(self):
        self.taches = []

    def ajouter_tache(self, titre, description=""):
        nouvelle_tache = Tache(titre, description)
        self.taches.append(nouvelle_tache)
        print(f"Tâche '{titre}' ajoutée.")

    def afficher_toutes(self):
        if not self.taches:
            print("Aucune tâche.")
            return

        print("\n=== Liste des tâches ===")
        for i, tache in enumerate(self.taches, 1):
            print(f"{i}. ", end="")
            tache.afficher()

    def afficher_non_terminees(self):
        taches_non_terminees = [t for t in self.taches if not t.terminee]
        if not taches_non_terminees:
            print("Toutes les tâches sont terminées ! 🎉")
            return

        print("\n=== Tâches à faire ===")
        for tache in taches_non_terminees:
            tache.afficher()

    def nombre_taches_terminees(self):
        return sum(1 for t in self.taches if t.terminee)

    def nombre_taches_total(self):
        return len(self.taches)

# Utilisation
gestionnaire = GestionnaireTaches()

gestionnaire.ajouter_tache("Faire les courses", "Acheter du pain et du lait")
gestionnaire.ajouter_tache("Répondre aux emails")
gestionnaire.ajouter_tache("Réviser Python", "Chapitre sur les classes")

gestionnaire.afficher_toutes()

# Marquer une tâche comme terminée
gestionnaire.taches[0].marquer_terminee()

gestionnaire.afficher_non_terminees()

print(f"\nProgress : {gestionnaire.nombre_taches_terminees()}/{gestionnaire.nombre_taches_total()} tâches terminées")
```

## Résumé des Concepts Clés

### Classe
- Un modèle ou blueprint pour créer des objets
- Définit les attributs (données) et méthodes (comportements)
- Se déclare avec le mot-clé `class`

### Objet (Instance)
- Une réalisation concrète d'une classe
- Possède ses propres valeurs d'attributs
- Se crée en appelant la classe comme une fonction

### `__init__` (Constructeur)
- Méthode spéciale appelée automatiquement lors de la création d'un objet
- Permet d'initialiser les attributs de l'objet
- Toujours le premier paramètre est `self`

### `self`
- Référence à l'instance courante
- Premier paramètre de toutes les méthodes d'instance
- Permet d'accéder aux attributs et méthodes de l'objet

### Attributs
- **Attributs d'instance** : propres à chaque objet, définis dans `__init__` avec `self`
- **Attributs de classe** : partagés par toutes les instances, définis directement dans la classe

### Méthodes
- Fonctions définies dans une classe
- Représentent les actions/comportements des objets
- Premier paramètre toujours `self`

## Conclusion

Les classes et objets sont les fondations de la Programmation Orientée Objet en Python. Ils permettent de :
- **Organiser** le code de manière logique et structurée
- **Réutiliser** le code facilement
- **Modéliser** des concepts du monde réel dans votre programme
- **Encapsuler** les données et les comportements ensemble

Dans les prochaines sections, nous explorerons des concepts plus avancés comme l'héritage, le polymorphisme et les méthodes spéciales qui vous permettront de créer des classes encore plus puissantes et flexibles.

La pratique est essentielle pour maîtriser ces concepts. N'hésitez pas à créer vos propres classes pour modéliser des objets qui vous intéressent : des livres, des films, des recettes de cuisine, des personnages de jeu vidéo, etc. Plus vous pratiquerez, plus ces concepts deviendront naturels !

⏭️ [Héritage et polymorphisme](/03-programmation-orientee-objet/02-heritage-et-polymorphisme.md)
