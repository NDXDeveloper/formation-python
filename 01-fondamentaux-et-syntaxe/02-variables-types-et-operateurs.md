🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.2 Variables, types de données et opérateurs

## Introduction

Dans cette section, nous allons découvrir les éléments fondamentaux de Python : les variables, les types de données et les opérateurs. Ce sont les briques de base de tout programme Python, et les comprendre est essentiel pour progresser dans votre apprentissage.

Imaginez les variables comme des boîtes étiquetées dans lesquelles vous pouvez ranger des informations. Les types de données définissent quel genre d'information vous pouvez y mettre (des nombres, du texte, etc.), et les opérateurs vous permettent de manipuler ces informations.

---

## Les Variables

### Qu'est-ce qu'une variable ?

Une **variable** est un nom qui fait référence à une valeur stockée en mémoire. C'est comme une étiquette que vous collez sur une boîte pour vous souvenir de ce qu'elle contient.

### Créer une variable (affectation)

En Python, créer une variable est très simple. On utilise le signe égal `=` pour affecter une valeur à un nom :

```python
age = 25
nom = "Alice"
taille = 1.75
```

Dans cet exemple :
- `age` est une variable qui contient le nombre 25
- `nom` est une variable qui contient le texte "Alice"
- `taille` est une variable qui contient le nombre décimal 1.75

**Important** : En Python, vous n'avez pas besoin de déclarer le type d'une variable à l'avance. Python le détermine automatiquement selon la valeur que vous lui donnez. C'est ce qu'on appelle le **typage dynamique**.

### Utiliser une variable

Une fois qu'une variable est créée, vous pouvez l'utiliser dans votre code :

```python
age = 25
print(age)  # Affiche : 25

# Utiliser la variable dans un calcul
annee_naissance = 2024 - age
print(annee_naissance)  # Affiche : 1999
```

### Modifier la valeur d'une variable

Les variables peuvent changer de valeur au cours du programme (c'est pour ça qu'on les appelle "variables" !) :

```python
compteur = 0
print(compteur)  # Affiche : 0

compteur = 5
print(compteur)  # Affiche : 5

compteur = compteur + 1
print(compteur)  # Affiche : 6
```

### Règles de nommage des variables

Python a quelques règles strictes et des conventions pour nommer les variables :

**Règles obligatoires** :
- Le nom doit commencer par une lettre (a-z, A-Z) ou un underscore (_)
- Le reste du nom peut contenir des lettres, des chiffres (0-9) et des underscores
- Les noms sont sensibles à la casse (`age` et `Age` sont deux variables différentes)
- On ne peut pas utiliser de mots réservés Python (comme `if`, `for`, `while`, etc.)

**Exemples valides** :
```python
nom = "Alice"
prenom_utilisateur = "Bob"
age2 = 30
_variable_privee = 42
```

**Exemples invalides** :
```python
2age = 30        # Commence par un chiffre ❌
mon-age = 25     # Contient un tiret ❌
for = 10         # Mot réservé Python ❌
mon âge = 25     # Contient un espace et un accent ❌
```

**Conventions (bonnes pratiques)** :
- Utilisez des noms descriptifs : `age_utilisateur` plutôt que `a`
- Utilisez le snake_case (mots séparés par des underscores) : `prenom_utilisateur`
- Évitez les lettres seules sauf pour les compteurs : `i`, `j`, `x`, `y`
- Les constantes s'écrivent en MAJUSCULES : `PI = 3.14159`

```python
# Bons noms de variables
nom_complet = "Alice Dupont"
age_en_annees = 25
prix_total_ttc = 99.99

# Noms à éviter (peu clairs)
x = "Alice Dupont"
n = 25
p = 99.99
```

---

## Les Types de Données Fondamentaux

Python possède plusieurs types de données de base. Comprendre ces types est crucial car ils déterminent quelles opérations vous pouvez effectuer sur vos variables.

### 1. Les Nombres Entiers (int)

Les **integers** (entiers) représentent des nombres sans partie décimale.

```python
age = 25
annee = 2024
temperature = -5
grand_nombre = 1000000
```

Python peut gérer des entiers de taille arbitraire (limité uniquement par la mémoire disponible) :

```python
tres_grand_nombre = 123456789012345678901234567890
print(tres_grand_nombre)  # Fonctionne parfaitement !
```

**Astuce** : Vous pouvez rendre les grands nombres plus lisibles avec des underscores :

```python
population = 67_000_000  # 67 millions
print(population)  # Affiche : 67000000
```

### 2. Les Nombres à Virgule Flottante (float)

Les **floats** représentent des nombres décimaux (avec une virgule... enfin, un point en informatique !).

```python
taille = 1.75
prix = 19.99
temperature = -3.5
pi = 3.14159
```

**Attention** : Les floats ont une précision limitée en raison de leur représentation en mémoire :

```python
resultat = 0.1 + 0.2
print(resultat)  # Affiche : 0.30000000000000004 (!)
```

Cette particularité est commune à tous les langages de programmation et est liée à la façon dont les ordinateurs représentent les nombres décimaux.

**Notation scientifique** :

```python
grand_nombre = 3e8  # 3 × 10^8 = 300000000
petit_nombre = 1.5e-4  # 1.5 × 10^-4 = 0.00015
```

### 3. Les Chaînes de Caractères (str)

Les **strings** (chaînes de caractères) représentent du texte. On les écrit entre guillemets simples `'` ou doubles `"`.

```python
prenom = "Alice"
nom = 'Dupont'
phrase = "J'aime Python !"
```

**Guillemets simples vs guillemets doubles** :

Les deux fonctionnent de la même manière, mais les guillemets doubles sont pratiques quand votre texte contient une apostrophe :

```python
message1 = "J'aime Python"  # Plus lisible
message2 = 'J\'aime Python'  # Nécessite d'échapper l'apostrophe avec \
```

**Chaînes multi-lignes** :

Pour écrire du texte sur plusieurs lignes, utilisez trois guillemets :

```python
poeme = """
Roses sont rouges,
Violettes sont bleues,
Python est génial,
Et vous l'aimerez aussi !
"""
print(poeme)
```

**Concaténation de chaînes** :

Vous pouvez combiner des chaînes avec l'opérateur `+` :

```python
prenom = "Alice"
nom = "Dupont"
nom_complet = prenom + " " + nom
print(nom_complet)  # Affiche : Alice Dupont
```

**Répétition de chaînes** :

L'opérateur `*` permet de répéter une chaîne :

```python
rire = "Ha" * 5
print(rire)  # Affiche : HaHaHaHaHa

ligne = "-" * 40
print(ligne)  # Affiche une ligne de 40 tirets
```

**Accéder aux caractères** :

Chaque caractère d'une chaîne a un index (position), qui commence à 0 :

```python
mot = "Python"
print(mot[0])   # Affiche : P (premier caractère)
print(mot[1])   # Affiche : y (deuxième caractère)
print(mot[-1])  # Affiche : n (dernier caractère)
print(mot[-2])  # Affiche : o (avant-dernier caractère)
```

**Longueur d'une chaîne** :

```python
texte = "Bonjour"
longueur = len(texte)
print(longueur)  # Affiche : 7
```

**Méthodes courantes des chaînes** :

```python
texte = "  Bonjour Python  "

# Convertir en majuscules / minuscules
print(texte.upper())      # Affiche :   BONJOUR PYTHON
print(texte.lower())      # Affiche :   bonjour python

# Supprimer les espaces aux extrémités
print(texte.strip())      # Affiche : Bonjour Python

# Remplacer du texte
print(texte.replace("Python", "monde"))  # Affiche :   Bonjour monde

# Vérifier le contenu
print(texte.startswith("  Bon"))  # Affiche : True
print(texte.endswith("thon  "))   # Affiche : True
print("Python" in texte)          # Affiche : True
```

### 4. Les Booléens (bool)

Les **booléens** ne peuvent prendre que deux valeurs : `True` (vrai) ou `False` (faux). Ils sont essentiels pour les conditions et la logique de votre programme.

```python
est_majeur = True
est_connecte = False
```

**Attention** : En Python, `True` et `False` commencent par une majuscule !

Les booléens sont souvent le résultat de comparaisons :

```python
age = 20
est_majeur = age >= 18
print(est_majeur)  # Affiche : True
```

**Conversions en booléen** :

Python peut convertir d'autres types en booléen. Voici les valeurs considérées comme `False` :
- `False` (bien sûr !)
- `0` et `0.0` (zéro)
- `""` (chaîne vide)
- `None` (valeur spéciale représentant "rien")
- Collections vides : `[]`, `{}`, `()`

Tout le reste est considéré comme `True` :

```python
print(bool(1))      # Affiche : True
print(bool(0))      # Affiche : False
print(bool(""))     # Affiche : False
print(bool("texte")) # Affiche : True
print(bool(-5))     # Affiche : True
```

### 5. Le Type None

`None` est une valeur spéciale en Python qui représente l'absence de valeur ou "rien". C'est différent de 0, False ou une chaîne vide.

```python
resultat = None
print(resultat)  # Affiche : None
```

C'est utile pour initialiser une variable qui recevra une valeur plus tard :

```python
nom_utilisateur = None
# ... plus tard dans le programme ...
nom_utilisateur = "Alice"
```

---

## Vérifier le Type d'une Variable

Python fournit la fonction `type()` pour connaître le type d'une variable :

```python
age = 25
print(type(age))  # Affiche : <class 'int'>

taille = 1.75
print(type(taille))  # Affiche : <class 'float'>

nom = "Alice"
print(type(nom))  # Affiche : <class 'str'>

est_majeur = True
print(type(est_majeur))  # Affiche : <class 'bool'>

vide = None
print(type(vide))  # Affiche : <class 'NoneType'>
```

---

## Conversion Entre Types (Casting)

Vous pouvez convertir une valeur d'un type à un autre. C'est ce qu'on appelle le **casting** ou la conversion de type.

### Conversions courantes

```python
# String vers int
age_texte = "25"
age_nombre = int(age_texte)
print(age_nombre + 5)  # Affiche : 30

# String vers float
prix_texte = "19.99"
prix_nombre = float(prix_texte)
print(prix_nombre * 2)  # Affiche : 39.98

# Int/Float vers string
age = 25
age_texte = str(age)
print("J'ai " + age_texte + " ans")  # Affiche : J'ai 25 ans

# Float vers int (tronque la partie décimale)
prix = 19.99
prix_entier = int(prix)
print(prix_entier)  # Affiche : 19

# Int vers float
nombre = 10
nombre_decimal = float(nombre)
print(nombre_decimal)  # Affiche : 10.0

# Vers booléen
print(bool(1))      # Affiche : True
print(bool(0))      # Affiche : False
print(bool("texte")) # Affiche : True
```

### Attention aux conversions invalides

Certaines conversions peuvent provoquer des erreurs :

```python
texte = "abc"
# nombre = int(texte)  # ❌ Erreur ! On ne peut pas convertir "abc" en nombre
```

Si vous essayez de convertir un texte qui ne représente pas un nombre valide, Python générera une erreur `ValueError`.

---

## Les Opérateurs Arithmétiques

Les opérateurs arithmétiques permettent d'effectuer des calculs mathématiques.

### Opérateurs de base

| Opérateur | Opération | Exemple | Résultat |
|-----------|-----------|---------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (retourne toujours un float) | `10 / 3` | `3.333...` |
| `//` | Division entière (quotient) | `10 // 3` | `3` |
| `%` | Modulo (reste de la division) | `10 % 3` | `1` |
| `**` | Puissance | `2 ** 3` | `8` |

### Exemples détaillés

```python
# Addition et soustraction
somme = 10 + 5
print(somme)  # Affiche : 15

difference = 10 - 5
print(difference)  # Affiche : 5

# Multiplication
produit = 7 * 6
print(produit)  # Affiche : 42

# Division classique (toujours un float)
division = 10 / 3
print(division)  # Affiche : 3.3333333333333335

division2 = 10 / 2
print(division2)  # Affiche : 5.0 (float, même si c'est un nombre entier)

# Division entière (quotient)
quotient = 10 // 3
print(quotient)  # Affiche : 3

# Modulo (reste)
reste = 10 % 3
print(reste)  # Affiche : 1

# Puissance
carre = 5 ** 2
print(carre)  # Affiche : 25

cube = 2 ** 3
print(cube)  # Affiche : 8
```

### Utilisations pratiques du modulo

Le modulo est très utile pour déterminer si un nombre est pair ou impair :

```python
nombre = 17
reste = nombre % 2

if reste == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")  # Affiche ceci car 17 % 2 = 1
```

### Priorité des opérations

Python respecte les règles mathématiques standard (PEMDAS/BODMAS) :
1. Parenthèses
2. Puissance
3. Multiplication, Division, Division entière, Modulo (de gauche à droite)
4. Addition, Soustraction (de gauche à droite)

```python
resultat1 = 2 + 3 * 4
print(resultat1)  # Affiche : 14 (pas 20, car * est prioritaire)

resultat2 = (2 + 3) * 4
print(resultat2)  # Affiche : 20 (les parenthèses sont prioritaires)

resultat3 = 2 ** 3 ** 2
print(resultat3)  # Affiche : 512 (2^(3^2) = 2^9, puissance associe à droite)
```

### Opérateurs d'affectation composée

Python permet de combiner une opération avec une affectation :

```python
# Au lieu de :
x = 10
x = x + 5

# On peut écrire :
x = 10
x += 5  # Équivalent à x = x + 5
print(x)  # Affiche : 15
```

Tous les opérateurs arithmétiques ont leur version composée :

```python
x = 10
x += 5   # x = x + 5  → x vaut 15
x -= 3   # x = x - 3  → x vaut 12
x *= 2   # x = x * 2  → x vaut 24
x /= 4   # x = x / 4  → x vaut 6.0
x //= 2  # x = x // 2 → x vaut 3.0
x %= 2   # x = x % 2  → x vaut 1.0
x **= 3  # x = x ** 3 → x vaut 1.0
```

---

## Les Opérateurs de Comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs. Ils retournent toujours un booléen (`True` ou `False`).

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `==` | Égal à | `5 == 5` | `True` |
| `!=` | Différent de | `5 != 3` | `True` |
| `>` | Supérieur à | `5 > 3` | `True` |
| `<` | Inférieur à | `5 < 3` | `False` |
| `>=` | Supérieur ou égal à | `5 >= 5` | `True` |
| `<=` | Inférieur ou égal à | `5 <= 3` | `False` |

### Exemples

```python
age = 20

print(age == 20)  # Affiche : True
print(age == 18)  # Affiche : False
print(age != 18)  # Affiche : True
print(age > 18)   # Affiche : True
print(age < 25)   # Affiche : True
print(age >= 20)  # Affiche : True
print(age <= 19)  # Affiche : False
```

### Attention : == vs =

Ne confondez pas :
- `=` : affectation (assigner une valeur à une variable)
- `==` : comparaison (tester si deux valeurs sont égales)

```python
x = 5    # Affectation : x reçoit la valeur 5
x == 5   # Comparaison : est-ce que x est égal à 5 ? (retourne True)
```

### Comparaison de chaînes

On peut aussi comparer des chaînes de caractères :

```python
nom1 = "Alice"
nom2 = "Bob"

print(nom1 == nom2)  # Affiche : False
print(nom1 != nom2)  # Affiche : True

# Comparaison alphabétique
print(nom1 < nom2)   # Affiche : True (A vient avant B dans l'alphabet)
print("abc" < "abd") # Affiche : True
```

---

## Les Opérateurs Logiques

Les opérateurs logiques permettent de combiner plusieurs conditions booléennes.

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `and` | ET logique | `True and False` | `False` |
| `or` | OU logique | `True or False` | `True` |
| `not` | NON logique (négation) | `not True` | `False` |

### L'opérateur `and` (ET)

Retourne `True` seulement si **les deux** conditions sont vraies.

```python
age = 25
a_permis = True

peut_conduire = age >= 18 and a_permis
print(peut_conduire)  # Affiche : True

# Table de vérité de AND
print(True and True)    # Affiche : True
print(True and False)   # Affiche : False
print(False and True)   # Affiche : False
print(False and False)  # Affiche : False
```

### L'opérateur `or` (OU)

Retourne `True` si **au moins une** des conditions est vraie.

```python
est_weekend = False
est_ferie = True

peut_se_reposer = est_weekend or est_ferie
print(peut_se_reposer)  # Affiche : True

# Table de vérité de OR
print(True or True)     # Affiche : True
print(True or False)    # Affiche : True
print(False or True)    # Affiche : True
print(False or False)   # Affiche : False
```

### L'opérateur `not` (NON)

Inverse une valeur booléenne.

```python
est_jour = True
est_nuit = not est_jour
print(est_nuit)  # Affiche : False

print(not True)   # Affiche : False
print(not False)  # Affiche : True
```

### Combiner plusieurs opérateurs

```python
age = 25
a_permis = True
a_voiture = False

peut_conduire = age >= 18 and a_permis and a_voiture
print(peut_conduire)  # Affiche : False

# Avec parenthèses pour clarifier
est_weekend = True
a_argent = False
peut_sortir = est_weekend and (a_argent or not a_argent)  # Toujours vrai !
```

### Priorité des opérateurs logiques

1. `not` (priorité la plus élevée)
2. `and`
3. `or` (priorité la plus faible)

```python
resultat = not False and True or False
# Évalué comme : ((not False) and True) or False
# → (True and True) or False
# → True or False
# → True
print(resultat)  # Affiche : True
```

**Conseil** : Utilisez des parenthèses pour rendre votre code plus lisible !

```python
# Moins clair
resultat = not False and True or False

# Plus clair
resultat = ((not False) and True) or False
```

---

## Les Opérateurs d'Appartenance

Ces opérateurs testent si une valeur est présente dans une séquence (chaîne, liste, etc.).

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `in` | Présent dans | `"a" in "abc"` → `True` |
| `not in` | Absent de | `"x" not in "abc"` → `True` |

### Exemples avec des chaînes

```python
texte = "Python est génial"

print("Python" in texte)     # Affiche : True
print("Java" in texte)       # Affiche : False
print("Java" not in texte)   # Affiche : True

# Vérifier si une chaîne contient une lettre
mot = "Bonjour"
print("o" in mot)  # Affiche : True
print("z" in mot)  # Affiche : False
```

Nous verrons plus d'exemples avec les listes et autres structures de données dans les prochaines sections.

---

## Les Opérateurs d'Identité

Ces opérateurs testent si deux variables référencent le **même objet en mémoire** (pas seulement si elles ont la même valeur).

| Opérateur | Signification |
|-----------|---------------|
| `is` | Même objet |
| `is not` | Objets différents |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # Affiche : True (même valeur)
print(a is b)   # Affiche : False (objets différents en mémoire)
print(a is c)   # Affiche : True (c pointe vers le même objet que a)

# Cas particulier avec None
valeur = None
print(valeur is None)      # Affiche : True (recommandé)
print(valeur == None)      # Affiche : True (fonctionne mais moins idiomatique)
```

**Note** : Pour comparer avec `None`, on utilise généralement `is None` plutôt que `== None`.

---

## Entrée Utilisateur avec input()

Pour rendre vos programmes interactifs, vous pouvez demander des informations à l'utilisateur avec la fonction `input()`.

```python
nom = input("Quel est votre nom ? ")
print("Bonjour, " + nom + " !")
```

**Important** : `input()` retourne toujours une chaîne de caractères (string), même si l'utilisateur entre un nombre !

```python
age_texte = input("Quel est votre âge ? ")
print(type(age_texte))  # Affiche : <class 'str'>

# Pour utiliser l'âge dans un calcul, il faut le convertir
age = int(age_texte)
annee_naissance = 2024 - age
print(f"Vous êtes né en {annee_naissance}")
```

### Conversion directe

On peut combiner `input()` avec une conversion :

```python
age = int(input("Quel est votre âge ? "))
taille = float(input("Quelle est votre taille en mètres ? "))

print(f"Vous avez {age} ans et vous mesurez {taille}m")
```

**Attention** : Si l'utilisateur entre quelque chose qui ne peut pas être converti en nombre, le programme générera une erreur. Nous verrons comment gérer ces erreurs dans une section ultérieure.

---

## Formatage de Chaînes (Affichage Avancé)

Python offre plusieurs façons d'afficher des variables dans du texte.

### 1. Concaténation simple (déjà vue)

```python
nom = "Alice"
age = 25
print("Je m'appelle " + nom + " et j'ai " + str(age) + " ans.")
```

**Inconvénient** : Nécessite de convertir les nombres en chaînes et beaucoup de `+`.

### 2. Méthode format()

```python
nom = "Alice"
age = 25
print("Je m'appelle {} et j'ai {} ans.".format(nom, age))
```

### 3. F-strings (Recommandé - Python 3.6+)

Les **f-strings** sont la méthode la plus moderne et la plus lisible :

```python
nom = "Alice"
age = 25
print(f"Je m'appelle {nom} et j'ai {age} ans.")
```

Vous pouvez même mettre des expressions dans les accolades :

```python
prix_ht = 100
tva = 0.20
print(f"Prix TTC : {prix_ht * (1 + tva)} euros")
# Affiche : Prix TTC : 120.0 euros

nombre = 7
print(f"Le double de {nombre} est {nombre * 2}")
# Affiche : Le double de 7 est 14
```

### Formatage avancé avec f-strings

```python
# Limiter les décimales
pi = 3.14159265
print(f"Pi vaut environ {pi:.2f}")  # Affiche : Pi vaut environ 3.14

# Afficher un pourcentage
ratio = 0.85
print(f"Taux de réussite : {ratio:.1%}")  # Affiche : Taux de réussite : 85.0%

# Aligner du texte
nom = "Alice"
print(f"{nom:>10}")   # Aligné à droite sur 10 caractères
print(f"{nom:<10}")   # Aligné à gauche sur 10 caractères
print(f"{nom:^10}")   # Centré sur 10 caractères
```

---

## Commentaires dans le Code

Les commentaires permettent d'expliquer votre code. Python ignore les commentaires lors de l'exécution.

### Commentaires sur une ligne

```python
# Ceci est un commentaire
age = 25  # Commentaire après du code
```

### Commentaires multi-lignes

Pour des explications plus longues, utilisez trois guillemets :

```python
"""
Ceci est un commentaire
sur plusieurs lignes.
Python l'ignore complètement.
"""

nom = "Alice"
```

Ou utilisez plusieurs lignes avec `#` :

```python
# Ceci est également un commentaire
# sur plusieurs lignes
# avec des dièses
```

### Bonnes pratiques pour les commentaires

✅ **Bon** : Expliquer le "pourquoi" et le "comment" complexe
```python
# Conversion des miles en kilomètres (1 mile = 1.60934 km)
distance_km = distance_miles * 1.60934
```

❌ **Mauvais** : Répéter ce que le code fait déjà de façon évidente
```python
# Afficher le nom
print(nom)
```

---

## Conventions et Bonnes Pratiques

### PEP 8 - Le Guide de Style Python

PEP 8 est le guide officiel de style pour Python. Voici quelques règles importantes :

**Espacement** :
```python
# Bon
x = 5
y = x + 1

# Mauvais
x=5
y=x+1
```

**Noms de variables** :
```python
# Bon (snake_case pour les variables)
nom_utilisateur = "Alice"
age_en_annees = 25

# Mauvais (camelCase n'est pas la convention Python pour les variables)
nomUtilisateur = "Alice"
ageEnAnnees = 25
```

**Longueur des lignes** :
- Maximum recommandé : 79 caractères par ligne
- Utilisez des parenthèses pour diviser les longues lignes :

```python
# Ligne trop longue
message = "Ceci est un très long message qui dépasse largement la limite de 79 caractères recommandée"

# Mieux
message = (
    "Ceci est un très long message qui dépasse largement "
    "la limite de 79 caractères recommandée"
)
```

### Nommage descriptif

Choisissez des noms de variables qui décrivent clairement leur contenu :

```python
# ✅ Bon
prix_unitaire = 10.50
quantite = 5
prix_total = prix_unitaire * quantite

# ❌ Mauvais
p = 10.50
q = 5
t = p * q
```

---

## Récapitulatif

Dans cette section, nous avons appris :

✅ **Variables** : Comment créer, nommer et utiliser des variables
✅ **Types de données** : int, float, str, bool, None
✅ **Opérateurs arithmétiques** : +, -, *, /, //, %, **
✅ **Opérateurs de comparaison** : ==, !=, <, >, <=, >=
✅ **Opérateurs logiques** : and, or, not
✅ **Opérateurs d'appartenance** : in, not in
✅ **Conversions de types** : int(), float(), str(), bool()
✅ **Entrée utilisateur** : input()
✅ **Formatage** : f-strings pour afficher des variables
✅ **Commentaires** : Documenter votre code

Ces concepts constituent la base de tout programme Python. Assurez-vous de bien les comprendre avant de passer à la suite !

---

## Points Clés à Retenir

1. **Les variables stockent des valeurs** : Donnez-leur des noms descriptifs
2. **Python a un typage dynamique** : Vous n'avez pas besoin de déclarer le type à l'avance
3. **Utilisez le bon type pour la bonne tâche** : int pour les entiers, float pour les décimaux, str pour le texte
4. **Les opérateurs permettent de manipuler les données** : arithmétiques pour les calculs, logiques pour les conditions
5. **input() retourne toujours une string** : Pensez à convertir si nécessaire
6. **Les f-strings sont vos amis** : Ils rendent l'affichage de variables plus simple et lisible
7. **Commentez votre code** : Votre futur vous (et vos collègues) vous remercieront

---

## Quelques Erreurs Courantes à Éviter

❌ **Confondre = et ==**
```python
# Mauvais (affectation au lieu de comparaison)
if x = 5:  # ❌ SyntaxError
    print("x vaut 5")

# Bon
if x == 5:  # ✅ Comparaison
    print("x vaut 5")
```

❌ **Oublier de convertir les types**
```python
age = input("Votre âge ? ")
# age est une string, pas un nombre !
# annee = 2024 - age  # ❌ TypeError

# Bon
annee = 2024 - int(age)  # ✅
```

❌ **Diviser par zéro**
```python
# resultat = 10 / 0  # ❌ ZeroDivisionError
```

❌ **Utiliser des noms de variables non descriptifs**
```python
# Mauvais
x = 100
y = 0.20
z = x * (1 + y)

# Bon
prix_ht = 100
taux_tva = 0.20
prix_ttc = prix_ht * (1 + taux_tva)
```

---

Vous maîtrisez maintenant les bases de Python ! Dans la prochaine section, nous verrons comment votre programme peut prendre des décisions et répéter des actions grâce aux structures de contrôle.


⏭️ [Structures de contrôle (if/else, boucles)](/01-fondamentaux-et-syntaxe/03-structures-de-controle.md)
