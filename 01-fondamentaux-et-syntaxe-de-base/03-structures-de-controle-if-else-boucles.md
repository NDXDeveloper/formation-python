🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.3 : Structures de contrôle (if/else, boucles)

## Introduction

Les structures de contrôle sont les éléments qui permettent de donner de la **logique** à vos programmes. Elles déterminent quelles parties du code seront exécutées et combien de fois. C'est ce qui transforme une simple liste d'instructions en un programme intelligent capable de prendre des décisions et de répéter des actions.

## L'indentation en Python

### Pourquoi l'indentation est importante

Contrairement à d'autres langages qui utilisent des accolades `{}`, Python utilise l'**indentation** (espaces en début de ligne) pour délimiter les blocs de code.

```python
# ✅ Correct : indentation cohérente
age = 20
if age >= 18:
    print("Vous êtes majeur")        # 4 espaces
    print("Vous pouvez voter")       # 4 espaces
print("Fin du programme")            # 0 espace (retour au niveau principal)

# ❌ Incorrect : indentation incohérente
if age >= 18:
    print("Vous êtes majeur")        # 4 espaces
  print("Vous pouvez voter")         # 2 espaces - ERREUR!
```

### Règles d'indentation

- **Utilisez 4 espaces** par niveau d'indentation (recommandation PEP 8)
- **Soyez cohérent** dans tout votre code
- **Ne mélangez pas** espaces et tabulations

💡 **Astuce** : Configurez votre éditeur pour afficher les espaces et remplacer les tabulations par 4 espaces.

## Les structures conditionnelles

### La structure if

La structure `if` permet d'exécuter du code seulement si une condition est vraie :

```python
# Structure de base
age = int(input("Quel est votre âge ? "))

if age >= 18:
    print("Vous êtes majeur")
    print("Vous pouvez voter")
    print("Bienvenue dans le monde des adultes!")

print("Cette ligne s'affiche toujours")
```

### La structure if/else

Pour exécuter du code différent selon que la condition soit vraie ou fausse :

```python
age = int(input("Quel est votre âge ? "))

if age >= 18:
    print("Vous êtes majeur")
    print("Vous pouvez voter")
else:
    print("Vous êtes mineur")
    print("Vous ne pouvez pas encore voter")

print("Merci pour votre participation")
```

### La structure if/elif/else

Pour tester plusieurs conditions successives :

```python
note = float(input("Entrez votre note sur 20 : "))

if note >= 16:
    print("Excellent ! Très bien !")
    mention = "Très bien"
elif note >= 14:
    print("Bien ! Bon travail !")
    mention = "Bien"
elif note >= 12:
    print("Assez bien. Peut mieux faire.")
    mention = "Assez bien"
elif note >= 10:
    print("Passable. Il faut travailler.")
    mention = "Passable"
else:
    print("Insuffisant. Redoublez d'efforts.")
    mention = "Insuffisant"

print(f"Votre mention : {mention}")
```

### Conditions complexes

Vous pouvez combiner plusieurs conditions avec `and`, `or` et `not` :

```python
age = int(input("Votre âge : "))
a_permis = input("Avez-vous le permis ? (oui/non) : ").lower() == "oui"

# Condition avec AND
if age >= 18 and a_permis:
    print("Vous pouvez conduire")
elif age >= 18 and not a_permis:
    print("Vous pouvez passer le permis")
else:
    print("Vous ne pouvez pas encore conduire")

# Condition avec OR
jour = input("Quel jour sommes-nous ? ").lower()
if jour == "samedi" or jour == "dimanche":
    print("C'est le week-end !")
else:
    print("C'est un jour de semaine")

# Vérification d'une plage de valeurs
temperature = float(input("Température (°C) : "))
if 18 <= temperature <= 25:
    print("Température idéale")
elif temperature < 18:
    print("Il fait froid")
else:
    print("Il fait chaud")
```

### L'opérateur ternaire (conditionnel)

Pour des conditions simples, vous pouvez utiliser l'opérateur ternaire :

```python
age = 20

# Version longue
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"

# Version courte (opérateur ternaire)
statut = "majeur" if age >= 18 else "mineur"
print(f"Vous êtes {statut}")

# Autre exemple
nombre = -5
signe = "positif" if nombre > 0 else "négatif" if nombre < 0 else "nul"
print(f"Le nombre est {signe}")
```

## Les boucles

### La boucle for

La boucle `for` permet de répéter du code un nombre déterminé de fois ou de parcourir une séquence :

#### Boucle avec range()

```python
# Compter de 0 à 4
print("Comptage simple :")
for i in range(5):
    print(f"Tour numéro {i}")

# Compter de 1 à 5
print("\nComptage de 1 à 5 :")
for i in range(1, 6):
    print(f"Tour numéro {i}")

# Compter de 2 en 2
print("\nComptage de 2 en 2 :")
for i in range(0, 11, 2):
    print(f"Nombre : {i}")

# Compter à l'envers
print("\nComptage à l'envers :")
for i in range(10, 0, -1):
    print(f"Décompte : {i}")
print("Décollage ! 🚀")
```

#### Parcourir une chaîne de caractères

```python
mot = "Python"
print("Lettres du mot Python :")
for lettre in mot:
    print(f"Lettre : {lettre}")

# Avec index et valeur
print("\nAvec index :")
for index, lettre in enumerate(mot):
    print(f"Index {index} : {lettre}")
```

#### Parcourir une liste

```python
fruits = ["pomme", "banane", "orange", "fraise"]

print("Liste des fruits :")
for fruit in fruits:
    print(f"- {fruit}")

# Avec index
print("\nAvec numérotation :")
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

### La boucle while

La boucle `while` répète du code tant qu'une condition reste vraie :

```python
# Exemple simple
compteur = 0
while compteur < 5:
    print(f"Compteur : {compteur}")
    compteur += 1  # Important : modifier la condition !

print("Fin de la boucle")
```

#### Boucle interactive

```python
# Menu interactif
continuer = True
while continuer:
    print("\n=== MENU ===")
    print("1. Dire bonjour")
    print("2. Dire au revoir")
    print("3. Quitter")

    choix = input("Votre choix (1-3) : ")

    if choix == "1":
        nom = input("Votre nom : ")
        print(f"Bonjour {nom} !")
    elif choix == "2":
        print("Au revoir !")
    elif choix == "3":
        print("À bientôt !")
        continuer = False
    else:
        print("Choix invalide. Réessayez.")
```

#### Validation d'entrée

```python
# Demander un nombre jusqu'à ce que l'entrée soit valide
while True:
    try:
        age = int(input("Entrez votre âge : "))
        if age < 0:
            print("L'âge ne peut pas être négatif")
            continue
        if age > 150:
            print("Âge peu probable, réessayez")
            continue
        break  # Sortir de la boucle si tout est OK
    except ValueError:
        print("Veuillez entrer un nombre entier")

print(f"Votre âge : {age} ans")
```

## Contrôle de flux dans les boucles

### L'instruction break

`break` permet de sortir immédiatement d'une boucle :

```python
# Recherche dans une liste
nombres = [1, 3, 7, 12, 8, 15, 20]
recherche = 12

print(f"Recherche du nombre {recherche}...")
for i, nombre in enumerate(nombres):
    print(f"Vérification de {nombre}")
    if nombre == recherche:
        print(f"Trouvé à l'index {i} !")
        break
else:
    # Cette partie s'exécute si la boucle se termine sans break
    print("Nombre non trouvé")

# Limite de tentatives
tentatives = 0
max_tentatives = 3

while tentatives < max_tentatives:
    mot_de_passe = input("Mot de passe : ")
    if mot_de_passe == "secret":
        print("Accès autorisé !")
        break
    else:
        tentatives += 1
        print(f"Incorrect. {max_tentatives - tentatives} tentatives restantes")
else:
    print("Accès bloqué. Trop de tentatives échouées.")
```

### L'instruction continue

`continue` permet de passer à l'itération suivante sans exécuter le reste du code :

```python
# Afficher seulement les nombres pairs
print("Nombres pairs de 1 à 10 :")
for i in range(1, 11):
    if i % 2 != 0:  # Si le nombre est impair
        continue    # Passer au suivant
    print(f"Nombre pair : {i}")

# Filtrer les entrées vides
mots = ["python", "", "programming", "", "fun"]
print("\nMots non vides :")
for mot in mots:
    if not mot:  # Si le mot est vide
        continue
    print(f"- {mot}")
```

## Boucles imbriquées

### Principe des boucles imbriquées

Vous pouvez placer une boucle à l'intérieur d'une autre :

```python
# Table de multiplication
print("Table de multiplication :")
for i in range(1, 6):  # Boucle externe
    print(f"\nTable de {i} :")
    for j in range(1, 6):  # Boucle interne
        resultat = i * j
        print(f"{i} × {j} = {resultat}")

# Dessin d'un rectangle
hauteur = 4
largeur = 6
print("\nDessin d'un rectangle :")
for ligne in range(hauteur):
    for colonne in range(largeur):
        print("*", end="")  # end="" évite le retour à la ligne
    print()  # Retour à la ligne après chaque ligne
```

### Exemple pratique : Jeu de devinette

```python
import random

print("=== JEU DE DEVINETTE ===")
rejouer = True

while rejouer:
    # Génération d'un nombre aléatoire
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 7
    gagne = False

    print(f"\nDevinez le nombre entre 1 et 100 !")
    print(f"Vous avez {max_tentatives} tentatives.")

    while tentatives < max_tentatives:
        try:
            proposition = int(input(f"\nTentative {tentatives + 1}/{max_tentatives} : "))
            tentatives += 1

            if proposition == nombre_secret:
                print(f"🎉 Bravo ! Vous avez trouvé en {tentatives} tentatives !")
                gagne = True
                break
            elif proposition < nombre_secret:
                print("C'est plus grand !")
            else:
                print("C'est plus petit !")

        except ValueError:
            print("Veuillez entrer un nombre entier")
            continue

    if not gagne:
        print(f"😞 Perdu ! Le nombre était {nombre_secret}")

    # Demander si on veut rejouer
    while True:
        choix = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
        if choix in ["oui", "o", "yes", "y"]:
            break
        elif choix in ["non", "n", "no"]:
            rejouer = False
            break
        else:
            print("Répondez par oui ou non")

print("Merci d'avoir joué !")
```

## Exemples pratiques

### Calculatrice avancée

```python
def calculatrice():
    print("=== CALCULATRICE ===")

    while True:
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Puissance (^)")
        print("6. Quitter")

        choix = input("\nChoisissez une opération (1-6) : ")

        if choix == "6":
            print("Au revoir !")
            break

        if choix not in ["1", "2", "3", "4", "5"]:
            print("Choix invalide !")
            continue

        # Saisie des nombres
        try:
            a = float(input("Premier nombre : "))
            b = float(input("Second nombre : "))
        except ValueError:
            print("Veuillez entrer des nombres valides")
            continue

        # Calculs
        if choix == "1":
            resultat = a + b
            print(f"{a} + {b} = {resultat}")
        elif choix == "2":
            resultat = a - b
            print(f"{a} - {b} = {resultat}")
        elif choix == "3":
            resultat = a * b
            print(f"{a} × {b} = {resultat}")
        elif choix == "4":
            if b != 0:
                resultat = a / b
                print(f"{a} ÷ {b} = {resultat}")
            else:
                print("Division par zéro impossible !")
        elif choix == "5":
            resultat = a ** b
            print(f"{a} ^ {b} = {resultat}")

# Lancement de la calculatrice
calculatrice()
```

### Gestionnaire de notes

```python
def gestionnaire_notes():
    notes = []

    while True:
        print("\n=== GESTIONNAIRE DE NOTES ===")
        print("1. Ajouter une note")
        print("2. Afficher toutes les notes")
        print("3. Calculer la moyenne")
        print("4. Trouver la meilleure note")
        print("5. Trouver la moins bonne note")
        print("6. Supprimer une note")
        print("7. Quitter")

        choix = input("\nVotre choix : ")

        if choix == "1":
            try:
                note = float(input("Entrez la note (0-20) : "))
                if 0 <= note <= 20:
                    notes.append(note)
                    print(f"Note {note} ajoutée !")
                else:
                    print("La note doit être entre 0 et 20")
            except ValueError:
                print("Veuillez entrer un nombre valide")

        elif choix == "2":
            if notes:
                print("\n--- Toutes les notes ---")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}/20")
            else:
                print("Aucune note enregistrée")

        elif choix == "3":
            if notes:
                moyenne = sum(notes) / len(notes)
                print(f"Moyenne : {moyenne:.2f}/20")
            else:
                print("Aucune note pour calculer la moyenne")

        elif choix == "4":
            if notes:
                meilleure = max(notes)
                print(f"Meilleure note : {meilleure}/20")
            else:
                print("Aucune note enregistrée")

        elif choix == "5":
            if notes:
                moins_bonne = min(notes)
                print(f"Moins bonne note : {moins_bonne}/20")
            else:
                print("Aucune note enregistrée")

        elif choix == "6":
            if notes:
                print("\n--- Notes actuelles ---")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}/20")
                try:
                    index = int(input("Numéro de la note à supprimer : ")) - 1
                    if 0 <= index < len(notes):
                        note_supprimee = notes.pop(index)
                        print(f"Note {note_supprimee} supprimée !")
                    else:
                        print("Numéro invalide")
                except ValueError:
                    print("Veuillez entrer un numéro valide")
            else:
                print("Aucune note à supprimer")

        elif choix == "7":
            print("Au revoir !")
            break

        else:
            print("Choix invalide !")

# Lancement du gestionnaire
gestionnaire_notes()
```

## Exercices pratiques

### Exercice 1 : Système de vote

```python
# Créez un programme qui :
# 1. Demande l'âge de l'utilisateur
# 2. Vérifie s'il peut voter (≥ 18 ans)
# 3. Si oui, demande son choix parmi 3 candidats
# 4. Affiche un message de confirmation
# 5. Si non, affiche dans combien d'années il pourra voter
```

### Exercice 2 : Tables de multiplication

```python
# Créez un programme qui :
# 1. Demande un nombre à l'utilisateur
# 2. Affiche la table de multiplication de ce nombre de 1 à 10
# 3. Demande s'il veut une autre table
# 4. Répète jusqu'à ce que l'utilisateur refuse
```

### Exercice 3 : Jeu du plus ou moins

```python
# Créez un jeu où :
# 1. L'ordinateur choisit un nombre entre 1 et 50
# 2. L'utilisateur doit deviner avec des indices "plus grand" ou "plus petit"
# 3. Limite à 6 tentatives
# 4. Affiche le score à la fin
```

### Exercice 4 : Analyseur de texte

```python
# Créez un programme qui :
# 1. Demande une phrase à l'utilisateur
# 2. Compte le nombre de mots
# 3. Compte le nombre de voyelles
# 4. Compte le nombre de consonnes
# 5. Affiche les statistiques
```

### Exercice 5 : Menu restaurant

```python
# Créez un système de commande qui :
# 1. Affiche un menu avec des plats et leurs prix
# 2. Permet de choisir plusieurs plats
# 3. Calcule le total
# 4. Demande si c'est pour emporter ou sur place (taxe différente)
# 5. Affiche la facture finale
```

## Bonnes pratiques

### Structure du code

```python
# ✅ Bon : structure claire
age = int(input("Votre âge : "))

if age >= 18:
    print("Vous êtes majeur")
    # Logique pour majeur
    if age >= 65:
        print("Vous bénéficiez de réductions senior")
else:
    print("Vous êtes mineur")
    # Logique pour mineur
    annees_restantes = 18 - age
    print(f"Plus que {annees_restantes} ans avant la majorité")

# ❌ Mauvais : structure confuse
if age < 18: print("Mineur"); print("Pas le droit de voter")
else: print("Majeur")
if age >= 65: print("Senior")
```

### Éviter les boucles infinies

```python
# ❌ Risque de boucle infinie
compteur = 0
while compteur < 10:
    print(compteur)
    # Oubli d'incrémenter compteur !

# ✅ Bon : modification de la condition
compteur = 0
while compteur < 10:
    print(compteur)
    compteur += 1  # Important !

# ✅ Alternative sûre avec for
for compteur in range(10):
    print(compteur)
```

### Limiter la complexité

```python
# ❌ Trop complexe : conditions imbriquées
if age >= 18:
    if a_permis:
        if a_voiture:
            if essence > 0:
                print("Peut conduire")
            else:
                print("Pas d'essence")
        else:
            print("Pas de voiture")
    else:
        print("Pas de permis")
else:
    print("Trop jeune")

# ✅ Plus lisible : conditions combinées
peut_conduire = age >= 18 and a_permis and a_voiture and essence > 0

if peut_conduire:
    print("Peut conduire")
elif age < 18:
    print("Trop jeune")
elif not a_permis:
    print("Pas de permis")
elif not a_voiture:
    print("Pas de voiture")
else:
    print("Pas d'essence")
```

## Pièges courants à éviter

### 1. Indentation incorrecte

```python
# ❌ Erreur d'indentation
age = 20
if age >= 18:
print("Majeur")  # IndentationError !

# ✅ Correct
if age >= 18:
    print("Majeur")
```

### 2. Comparaison d'assignation

```python
# ❌ Erreur : = au lieu de ==
x = 5
if x = 5:  # SyntaxError !
    print("x vaut 5")

# ✅ Correct
if x == 5:
    print("x vaut 5")
```

### 3. Modification de liste pendant itération

```python
# ❌ Problématique
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    if nombre % 2 == 0:
        nombres.remove(nombre)  # Modifie la liste pendant l'itération

# ✅ Correct : créer une nouvelle liste
nombres = [1, 2, 3, 4, 5]
nombres_impairs = []
for nombre in nombres:
    if nombre % 2 != 0:
        nombres_impairs.append(nombre)
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ **Indentation** : La règle fondamentale de Python (4 espaces)
✅ **Conditions** : if, elif, else pour prendre des décisions
✅ **Boucles for** : Pour répéter un nombre déterminé de fois
✅ **Boucles while** : Pour répéter tant qu'une condition est vraie
✅ **Contrôle de flux** : break et continue pour contrôler les boucles
✅ **Boucles imbriquées** : Boucles dans des boucles
✅ **Exemples pratiques** : Applications concrètes des structures de contrôle

**Concepts clés à retenir :**
- L'indentation détermine la structure du code en Python
- `if/elif/else` pour les décisions
- `for` pour les itérations sur des séquences
- `while` pour les boucles conditionnelles
- `break` pour sortir d'une boucle, `continue` pour passer à l'itération suivante
- Toujours modifier la condition dans une boucle `while`

**Prochaine étape** : Dans la section 1.4, nous découvrirons les fonctions pour organiser et réutiliser notre code !

---

💡 **Conseil** : Les structures de contrôle sont le cœur de la logique de programmation. Pratiquez avec les exercices pour bien maîtriser ces concepts essentiels !

⏭️
