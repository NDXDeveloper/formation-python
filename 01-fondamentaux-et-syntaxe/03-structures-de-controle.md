🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.3 Structures de contrôle (if/else, boucles)

## Introduction

Les structures de contrôle sont essentielles en programmation. Elles permettent à votre programme de :
- **Prendre des décisions** : exécuter du code seulement si une condition est vraie (if/else)
- **Répéter des actions** : exécuter du code plusieurs fois (boucles for et while)

Sans structures de contrôle, votre programme exécuterait toujours les mêmes instructions dans le même ordre, du début à la fin. Avec elles, votre programme peut s'adapter, réagir et répéter des tâches !

---

## Les Structures Conditionnelles

### L'instruction `if` (si)

L'instruction `if` permet d'exécuter un bloc de code **seulement si** une condition est vraie.

**Syntaxe de base** :
```python
if condition:
    # Code à exécuter si la condition est vraie
    instruction1
    instruction2
```

**Points importants** :
- La condition se termine par deux points `:`
- Le bloc de code sous le `if` doit être **indenté** (décalé vers la droite avec 4 espaces)
- L'indentation est **obligatoire** en Python (contrairement à d'autres langages)

### Premier exemple

```python
age = 20

if age >= 18:
    print("Vous êtes majeur !")
    print("Vous pouvez voter.")

print("Ce message s'affiche toujours")
```

**Résultat** :
```
Vous êtes majeur !
Vous pouvez voter.
Ce message s'affiche toujours
```

Si `age` était 15, seule la dernière ligne s'afficherait car la condition serait fausse.

### L'importance de l'indentation

En Python, l'indentation (les espaces au début de la ligne) définit les blocs de code. C'est **obligatoire** et fait partie de la syntaxe du langage.

```python
age = 20

if age >= 18:
    print("Ligne 1 dans le if")
    print("Ligne 2 dans le if")
print("Ligne en dehors du if")
```

**Convention** : Utilisez toujours **4 espaces** pour l'indentation (la plupart des éditeurs de code le font automatiquement quand vous appuyez sur Tab).

❌ **Erreur d'indentation** :
```python
if age >= 18:
print("Erreur !")  # ❌ IndentationError : pas indenté
```

---

## L'instruction `else` (sinon)

`else` permet de définir un bloc de code qui s'exécute si la condition du `if` est **fausse**.

**Syntaxe** :
```python
if condition:
    # Code si la condition est vraie
else:
    # Code si la condition est fausse
```

### Exemple

```python
age = 15

if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

print("Programme terminé")
```

**Résultat** :
```
Vous êtes mineur
Programme terminé
```

### Exemple interactif

```python
mot_de_passe = input("Entrez le mot de passe : ")

if mot_de_passe == "python123":
    print("✓ Accès autorisé")
    print("Bienvenue dans le système")
else:
    print("✗ Accès refusé")
    print("Mot de passe incorrect")
```

---

## L'instruction `elif` (sinon si)

`elif` (contraction de "else if") permet de tester **plusieurs conditions** successivement.

**Syntaxe** :
```python
if condition1:
    # Code si condition1 est vraie
elif condition2:
    # Code si condition1 est fausse et condition2 est vraie
elif condition3:
    # Code si condition1 et condition2 sont fausses et condition3 est vraie
else:
    # Code si toutes les conditions sont fausses
```

### Exemple : système de notes

```python
note = 15

if note >= 16:
    print("Mention Très Bien")
elif note >= 14:
    print("Mention Bien")
elif note >= 12:
    print("Mention Assez Bien")
elif note >= 10:
    print("Admis")
else:
    print("Non admis")
```

**Résultat** : `Mention Bien` (car note = 15, qui est >= 14)

**Important** : Dès qu'une condition est vraie, Python exécute le bloc correspondant et **ignore les autres** (même si elles seraient vraies aussi).

### Exemple : classification d'âge

```python
age = int(input("Quel est votre âge ? "))

if age < 0:
    print("Âge invalide")
elif age < 2:
    print("Vous êtes un bébé")
elif age < 12:
    print("Vous êtes un enfant")
elif age < 18:
    print("Vous êtes un adolescent")
elif age < 60:
    print("Vous êtes un adulte")
else:
    print("Vous êtes un senior")
```

---

## Conditions Multiples

Vous pouvez combiner plusieurs conditions avec les opérateurs logiques `and`, `or` et `not`.

### Opérateur `and` (ET)

Les **deux** conditions doivent être vraies.

```python
age = 25
a_permis = True

if age >= 18 and a_permis:
    print("Vous pouvez conduire")
else:
    print("Vous ne pouvez pas conduire")
```

### Opérateur `or` (OU)

**Au moins une** condition doit être vraie.

```python
jour = "samedi"

if jour == "samedi" or jour == "dimanche":
    print("C'est le weekend !")
else:
    print("C'est un jour de semaine")
```

### Opérateur `not` (NON)

Inverse le résultat d'une condition.

```python
est_pluie = False

if not est_pluie:
    print("Vous pouvez sortir sans parapluie")
else:
    print("Prenez un parapluie")
```

### Combiner plusieurs opérateurs

```python
age = 25
a_permis = True
a_voiture = False

if age >= 18 and a_permis and a_voiture:
    print("Vous pouvez conduire votre voiture")
elif age >= 18 and a_permis and not a_voiture:
    print("Vous pouvez conduire mais vous n'avez pas de voiture")
else:
    print("Vous ne pouvez pas conduire")
```

**Conseil** : Utilisez des parenthèses pour clarifier les conditions complexes :

```python
if (age >= 18 and a_permis) or est_accompagne:
    print("Vous pouvez conduire")
```

---

## Conditions Imbriquées

Vous pouvez mettre des `if` à l'intérieur d'autres `if`.

```python
age = 20
a_argent = True

if age >= 18:
    print("Vous êtes majeur")

    if a_argent:
        print("Vous pouvez aller au cinéma")
    else:
        print("Vous n'avez pas d'argent pour le cinéma")
else:
    print("Vous êtes mineur")
```

**Attention** : Chaque niveau d'imbrication ajoute 4 espaces d'indentation !

Cependant, **évitez d'imbriquer trop de niveaux**. Préférez utiliser `and` pour simplifier :

```python
# Version imbriquée (moins lisible)
if age >= 18:
    if a_argent:
        if est_ouvert:
            print("Vous pouvez entrer")

# Version simplifiée (plus lisible)
if age >= 18 and a_argent and est_ouvert:
    print("Vous pouvez entrer")
```

---

## L'Opérateur Ternaire (Condition sur une ligne)

Python permet d'écrire une condition simple sur une seule ligne. C'est pratique pour les cas simples.

**Syntaxe** :
```python
valeur_si_vrai if condition else valeur_si_faux
```

### Exemple

```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # Affiche : majeur
```

C'est équivalent à :
```python
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"
```

### Autres exemples

```python
# Trouver le maximum de deux nombres
a = 10
b = 20
maximum = a if a > b else b
print(maximum)  # Affiche : 20

# Affichage conditionnel
temperature = 25
print("Il fait chaud" if temperature > 20 else "Il fait froid")

# Prix avec réduction
prix = 100
membre = True
prix_final = prix * 0.9 if membre else prix
print(f"Prix : {prix_final}€")  # Affiche : Prix : 90.0€
```

**Attention** : N'abusez pas de l'opérateur ternaire pour des conditions complexes. Il est fait pour les cas simples !

---

## Les Boucles

Les boucles permettent de répéter du code plusieurs fois. Python propose deux types de boucles : `while` et `for`.

---

## La Boucle `while` (tant que)

La boucle `while` répète un bloc de code **tant qu'une condition est vraie**.

**Syntaxe** :
```python
while condition:
    # Code à répéter
    instruction1
    instruction2
```

### Exemple simple

```python
compteur = 1

while compteur <= 5:
    print(f"Compteur : {compteur}")
    compteur += 1  # Équivalent à compteur = compteur + 1

print("Boucle terminée")
```

**Résultat** :
```
Compteur : 1
Compteur : 2
Compteur : 3
Compteur : 4
Compteur : 5
Boucle terminée
```

### Fonctionnement de la boucle while

1. Python évalue la condition
2. Si elle est vraie, il exécute le bloc de code
3. Il retourne au début et réévalue la condition
4. Tant que la condition est vraie, il répète les étapes 2-3
5. Quand la condition devient fausse, il sort de la boucle

### Exemple : compte à rebours

```python
compte = 5

while compte > 0:
    print(compte)
    compte -= 1

print("Décollage ! 🚀")
```

**Résultat** :
```
5
4
3
2
1
Décollage ! 🚀
```

### Exemple interactif : deviner un nombre

```python
nombre_secret = 42
devine = 0

while devine != nombre_secret:
    devine = int(input("Devinez le nombre : "))

    if devine < nombre_secret:
        print("Trop petit !")
    elif devine > nombre_secret:
        print("Trop grand !")
    else:
        print("Bravo, vous avez trouvé !")
```

### ⚠️ Attention aux boucles infinies !

Si la condition reste toujours vraie, la boucle ne s'arrête jamais !

```python
# ❌ BOUCLE INFINIE - N'exécutez pas ce code !
compteur = 1
while compteur <= 5:
    print(compteur)
    # Oups, on a oublié d'incrémenter compteur !
    # compteur += 1
```

**Pour arrêter un programme bloqué** : Appuyez sur `Ctrl + C` dans le terminal.

**Solution** : Assurez-vous que la condition finira par devenir fausse :
```python
compteur = 1
while compteur <= 5:
    print(compteur)
    compteur += 1  # ✓ Important : on modifie compteur !
```

---

## La Boucle `for` (pour chaque)

La boucle `for` permet d'itérer (parcourir) sur une séquence d'éléments.

**Syntaxe** :
```python
for variable in sequence:
    # Code à répéter pour chaque élément
```

### Parcourir une chaîne de caractères

```python
mot = "Python"

for lettre in mot:
    print(lettre)
```

**Résultat** :
```
P
y
t
h
o
n
```

### La fonction `range()`

`range()` génère une séquence de nombres. C'est très utile avec `for` pour répéter une action un certain nombre de fois.

#### range(n) : de 0 à n-1

```python
for i in range(5):
    print(i)
```

**Résultat** :
```
0
1
2
3
4
```

**Important** : `range(5)` génère les nombres de 0 à 4 (5 nombres au total, mais s'arrête avant 5).

#### range(debut, fin) : de debut à fin-1

```python
for i in range(1, 6):
    print(i)
```

**Résultat** :
```
1
2
3
4
5
```

#### range(debut, fin, pas) : avec un pas personnalisé

```python
# Compter de 2 en 2
for i in range(0, 10, 2):
    print(i)
```

**Résultat** :
```
0
2
4
6
8
```

```python
# Compter à rebours
for i in range(10, 0, -1):
    print(i)

print("Décollage ! 🚀")
```

**Résultat** :
```
10
9
8
7
6
5
4
3
2
1
Décollage ! 🚀
```

### Exemples pratiques avec for

#### Calculer une somme

```python
somme = 0

for i in range(1, 11):
    somme += i  # somme = somme + i

print(f"La somme de 1 à 10 est : {somme}")
# Affiche : La somme de 1 à 10 est : 55
```

#### Table de multiplication

```python
nombre = 7

print(f"Table de multiplication de {nombre} :")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} × {i} = {resultat}")
```

**Résultat** :
```
Table de multiplication de 7 :
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
```

#### Dessiner un triangle

```python
for i in range(1, 6):
    print("*" * i)
```

**Résultat** :
```
*
**
***
****
*****
```

---

## Choisir entre `while` et `for`

### Utiliser `for` quand :
- Vous connaissez à l'avance **combien de fois** vous voulez répéter
- Vous parcourez une **séquence** (chaîne, liste, etc.)

**Exemples** :
- Répéter 10 fois
- Parcourir chaque lettre d'un mot
- Afficher les nombres de 1 à 100

### Utiliser `while` quand :
- Vous ne savez **pas à l'avance** combien de fois répéter
- La répétition dépend d'une **condition dynamique**

**Exemples** :
- Demander un mot de passe jusqu'à ce qu'il soit correct
- Continuer tant que l'utilisateur répond "oui"
- Répéter jusqu'à ce qu'un objectif soit atteint

### Comparaison

```python
# Même résultat avec for et while

# Avec for (plus simple quand on connaît le nombre)
for i in range(5):
    print(i)

# Avec while (plus flexible mais plus verbeux)
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## L'instruction `break` (sortir de la boucle)

`break` permet de **sortir immédiatement** d'une boucle, même si la condition est encore vraie.

### Exemple avec while

```python
compteur = 0

while True:  # Boucle infinie !
    print(compteur)
    compteur += 1

    if compteur >= 5:
        break  # On sort de la boucle

print("Boucle terminée")
```

**Résultat** :
```
0
1
2
3
4
Boucle terminée
```

### Exemple avec for

```python
# Chercher un nombre dans une séquence
for i in range(1, 101):
    print(f"Vérification de {i}")

    if i == 7:
        print("Trouvé !")
        break  # On arrête la recherche
```

### Exemple pratique : validation d'entrée

```python
while True:
    age = input("Entrez votre âge : ")

    if age.isdigit():  # Vérifie si c'est un nombre
        age = int(age)
        if age > 0:
            break  # L'âge est valide, on sort de la boucle
        else:
            print("L'âge doit être positif")
    else:
        print("Veuillez entrer un nombre")

print(f"Votre âge : {age}")
```

---

## L'instruction `continue` (passer à l'itération suivante)

`continue` permet de **sauter le reste du code** dans la boucle et de passer directement à l'itération suivante.

### Exemple : afficher seulement les nombres impairs

```python
for i in range(1, 11):
    if i % 2 == 0:  # Si le nombre est pair
        continue    # On passe au suivant

    print(i)  # Cette ligne n'est exécutée que pour les impairs
```

**Résultat** :
```
1
3
5
7
9
```

### Différence entre break et continue

```python
# Avec break : arrête complètement la boucle
for i in range(5):
    if i == 3:
        break
    print(i)
# Affiche : 0, 1, 2

# Avec continue : saute seulement l'itération actuelle
for i in range(5):
    if i == 3:
        continue
    print(i)
# Affiche : 0, 1, 2, 4
```

### Exemple pratique : ignorer les valeurs invalides

```python
temperatures = [23, -999, 25, 28, -999, 22]  # -999 = valeur manquante

somme = 0
count = 0

for temp in temperatures:
    if temp == -999:
        continue  # On ignore cette valeur

    somme += temp
    count += 1

moyenne = somme / count
print(f"Température moyenne : {moyenne}°C")
# Affiche : Température moyenne : 24.5°C
```

---

## L'instruction `pass` (ne rien faire)

`pass` est une instruction qui ne fait **rien**. C'est un placeholder (espace réservé) utilisé quand la syntaxe Python exige du code mais que vous n'avez rien à mettre pour l'instant.

### Exemples d'utilisation

```python
# Structure de condition vide (à compléter plus tard)
age = 20

if age < 18:
    pass  # TODO : ajouter le code pour les mineurs
else:
    print("Majeur")
```

```python
# Boucle vide
for i in range(10):
    pass  # On ne fait rien, mais la syntaxe est valide
```

`pass` est surtout utile pendant le développement pour créer une structure de code que vous remplirez plus tard :

```python
# Esquisse de programme
reponse = input("Voulez-vous continuer ? (o/n) ")

if reponse == "o":
    pass  # TODO : implémenter la suite
elif reponse == "n":
    print("Au revoir !")
else:
    pass  # TODO : gérer les entrées invalides
```

---

## Boucles Imbriquées

Vous pouvez mettre des boucles à l'intérieur d'autres boucles.

### Exemple : table de multiplication complète

```python
for i in range(1, 4):
    for j in range(1, 4):
        resultat = i * j
        print(f"{i} × {j} = {resultat}")
    print()  # Ligne vide après chaque table
```

**Résultat** :
```
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3

2 × 1 = 2
2 × 2 = 4
2 × 3 = 6

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
```

### Exemple : dessiner un rectangle

```python
hauteur = 4
largeur = 6

for i in range(hauteur):
    for j in range(largeur):
        print("*", end="")  # end="" évite le retour à la ligne
    print()  # Retour à la ligne après chaque ligne
```

**Résultat** :
```
******
******
******
******
```

### Exemple : motif en escalier

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Résultat** :
```
*
* *
* * *
* * * *
* * * * *
```

### Comprendre les boucles imbriquées

Pour chaque itération de la boucle **externe**, la boucle **interne** s'exécute **complètement**.

```python
for i in range(3):  # Boucle externe
    print(f"Externe : i = {i}")

    for j in range(2):  # Boucle interne
        print(f"  Interne : j = {j}")
```

**Résultat** :
```
Externe : i = 0
  Interne : j = 0
  Interne : j = 1
Externe : i = 1
  Interne : j = 0
  Interne : j = 1
Externe : i = 2
  Interne : j = 0
  Interne : j = 1
```

---

## La Clause `else` avec les Boucles

Python permet d'ajouter un `else` après une boucle `for` ou `while`. Le code dans le `else` s'exécute **seulement si la boucle se termine normalement** (sans `break`).

### Avec une boucle for

```python
# Chercher un nombre premier
nombre = 17

for i in range(2, nombre):
    if nombre % i == 0:
        print(f"{nombre} n'est pas premier (divisible par {i})")
        break
else:
    # Cette partie s'exécute si on n'a pas trouvé de diviseur
    print(f"{nombre} est premier")
```

### Avec une boucle while

```python
tentatives = 0
max_tentatives = 3
mot_de_passe = "python123"

while tentatives < max_tentatives:
    mdp = input("Mot de passe : ")
    tentatives += 1

    if mdp == mot_de_passe:
        print("Accès autorisé !")
        break
else:
    # S'exécute si on sort de la boucle sans break
    print("Trop de tentatives. Accès bloqué.")
```

**Note** : Cette fonctionnalité est peu utilisée en pratique car elle peut rendre le code moins lisible. Elle est surtout utile dans des algorithmes de recherche.

---

## Bonnes Pratiques avec les Structures de Contrôle

### 1. Simplicité avant tout

✅ **Bon** : Simple et clair
```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

❌ **Mauvais** : Trop compliqué pour rien
```python
if age >= 18:
    est_majeur = True
else:
    est_majeur = False

if est_majeur == True:
    print("Majeur")
else:
    print("Mineur")
```

### 2. Éviter les conditions redondantes

✅ **Bon**
```python
if age >= 18 and a_permis:
    print("Peut conduire")
```

❌ **Mauvais**
```python
if age >= 18:
    if a_permis:
        print("Peut conduire")
```

### 3. Utiliser des noms de variables descriptifs

✅ **Bon**
```python
est_majeur = age >= 18
a_permis = True

if est_majeur and a_permis:
    print("Peut conduire")
```

❌ **Mauvais**
```python
if x >= 18 and y:
    print("Peut conduire")
```

### 4. Retours précoces pour simplifier

✅ **Bon** : Retour précoce
```python
def verifier_acces(age, a_billet):
    if age < 18:
        return "Accès interdit - mineur"

    if not a_billet:
        return "Accès interdit - pas de billet"

    return "Accès autorisé"
```

❌ **Mauvais** : Trop imbriqué
```python
def verifier_acces(age, a_billet):
    if age >= 18:
        if a_billet:
            return "Accès autorisé"
        else:
            return "Accès interdit - pas de billet"
    else:
        return "Accès interdit - mineur"
```

### 5. Limiter la profondeur d'imbrication

Évitez d'imbriquer plus de 2-3 niveaux. Si vous en avez besoin, c'est peut-être le signe que votre code devrait être réorganisé.

### 6. Choisir le bon type de boucle

```python
# ✅ Bon : for quand on connaît le nombre d'itérations
for i in range(10):
    print(i)

# ❌ Moins bon : while pour un nombre fixe d'itérations
i = 0
while i < 10:
    print(i)
    i += 1
```

---

## Exemples Pratiques Complets

### Exemple 1 : Menu interactif

```python
while True:
    print("\n=== Menu Principal ===")
    print("1. Dire bonjour")
    print("2. Afficher l'heure")
    print("3. Calculer une somme")
    print("4. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":
        nom = input("Votre nom : ")
        print(f"Bonjour {nom} !")

    elif choix == "2":
        from datetime import datetime
        maintenant = datetime.now()
        print(f"Il est {maintenant.strftime('%H:%M:%S')}")

    elif choix == "3":
        a = int(input("Premier nombre : "))
        b = int(input("Deuxième nombre : "))
        print(f"La somme est : {a + b}")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Réessayez.")
```

### Exemple 2 : Jeu du plus ou moins

```python
import random

nombre_secret = random.randint(1, 100)
tentatives = 0
max_tentatives = 10

print("=== Jeu du Plus ou Moins ===")
print(f"Devinez le nombre entre 1 et 100 (vous avez {max_tentatives} tentatives)")

while tentatives < max_tentatives:
    tentatives += 1
    essai = int(input(f"\nTentative {tentatives}/{max_tentatives} : "))

    if essai < nombre_secret:
        print("⬆️  C'est plus !")
    elif essai > nombre_secret:
        print("⬇️  C'est moins !")
    else:
        print(f"🎉 Bravo ! Vous avez trouvé en {tentatives} tentative(s) !")
        break
else:
    print(f"\n💥 Perdu ! Le nombre était {nombre_secret}")
```

### Exemple 3 : Calculer le PGCD (algorithme d'Euclide)

```python
a = int(input("Premier nombre : "))
b = int(input("Deuxième nombre : "))

# Algorithme d'Euclide
while b != 0:
    reste = a % b
    a = b
    b = reste

print(f"Le PGCD est : {a}")
```

### Exemple 4 : Vérifier si un nombre est premier

```python
nombre = int(input("Entrez un nombre : "))

if nombre < 2:
    print(f"{nombre} n'est pas premier")
else:
    est_premier = True

    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            est_premier = False
            break

    if est_premier:
        print(f"{nombre} est premier")
    else:
        print(f"{nombre} n'est pas premier")
```

### Exemple 5 : Générer un triangle de Pascal

```python
n = int(input("Nombre de lignes : "))

for i in range(n):
    # Espaces pour centrer
    for j in range(n - i - 1):
        print(" ", end="")

    # Calculer les coefficients binomiaux
    nombre = 1
    for j in range(i + 1):
        print(nombre, end=" ")
        nombre = nombre * (i - j) // (j + 1)

    print()
```

**Résultat** (pour n=5) :
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

---

## Erreurs Courantes à Éviter

### 1. Oublier les deux points

❌ **Erreur**
```python
if age >= 18
    print("Majeur")
```

✅ **Correct**
```python
if age >= 18:
    print("Majeur")
```

### 2. Mauvaise indentation

❌ **Erreur**
```python
if age >= 18:
print("Majeur")  # Pas indenté !
```

✅ **Correct**
```python
if age >= 18:
    print("Majeur")
```

### 3. Utiliser = au lieu de ==

❌ **Erreur** (affectation au lieu de comparaison)
```python
if age = 18:
    print("Vous avez 18 ans")
```

✅ **Correct**
```python
if age == 18:
    print("Vous avez 18 ans")
```

### 4. Boucle infinie involontaire

❌ **Erreur**
```python
i = 0
while i < 10:
    print(i)
    # Oublié d'incrémenter i !
```

✅ **Correct**
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### 5. Range qui ne fait pas ce qu'on attend

```python
# range(5) génère : 0, 1, 2, 3, 4 (pas 5 !)
for i in range(5):
    print(i)  # Affiche 0 à 4

# Pour avoir 1 à 5 :
for i in range(1, 6):
    print(i)  # Affiche 1 à 5
```

---

## Récapitulatif

Dans cette section, nous avons appris :

✅ **Structures conditionnelles** : if, elif, else pour prendre des décisions
✅ **Conditions multiples** : and, or, not pour combiner des conditions
✅ **Opérateur ternaire** : condition sur une ligne pour les cas simples
✅ **Boucle while** : répéter tant qu'une condition est vraie
✅ **Boucle for** : parcourir une séquence ou répéter un nombre défini de fois
✅ **Fonction range()** : générer des séquences de nombres
✅ **break** : sortir d'une boucle
✅ **continue** : passer à l'itération suivante
✅ **pass** : placeholder pour du code à venir
✅ **Boucles imbriquées** : boucles dans des boucles

---

## Points Clés à Retenir

1. **L'indentation est obligatoire** : 4 espaces par niveau
2. **Les conditions retournent des booléens** : True ou False
3. **Utilisez `for` pour un nombre connu d'itérations** : parcourir une séquence ou répéter n fois
4. **Utilisez `while` pour une condition dynamique** : quand vous ne savez pas à l'avance combien de fois répéter
5. **Attention aux boucles infinies** : assurez-vous que la condition devient fausse
6. **break sort de la boucle, continue passe à l'itération suivante**
7. **Gardez votre code simple et lisible** : évitez les imbrications excessives

---

## Pour Aller Plus Loin

Voici quelques défis pour pratiquer (à réaliser par vous-même) :

- Créer un convertisseur de température (Celsius ↔ Fahrenheit) avec menu
- Afficher tous les nombres premiers entre 1 et 100
- Créer une calculatrice avec boucle pour continuer les calculs
- Deviner un mot lettre par lettre (jeu du pendu simplifié)
- Calculer la suite de Fibonacci jusqu'au n-ième terme

---

Vous maîtrisez maintenant les structures de contrôle ! Dans la prochaine section, nous découvrirons comment organiser votre code en fonctions réutilisables.


⏭️ [Fonctions et portée des variables](/01-fondamentaux-et-syntaxe/04-fonctions-et-portee.md)
