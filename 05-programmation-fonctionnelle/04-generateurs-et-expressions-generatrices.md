🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 5.4 : Générateurs et expressions génératrices

## Introduction

Les générateurs sont l'une des fonctionnalités les plus puissantes de Python pour travailler avec des séquences de données. Ils permettent de créer des itérateurs de manière simple et efficace en mémoire. Au lieu de créer toute une liste en mémoire, les générateurs produisent les éléments un par un, à la demande.

## Pourquoi utiliser des générateurs ?

### Problème avec les listes traditionnelles

```python
# Créer une liste de 1 million de nombres
def creer_grandes_donnees():
    return [x * 2 for x in range(1000000)]

# Cette fonction utilise beaucoup de mémoire !
# grandes_donnees = creer_grandes_donnees()  # ~8 MB en mémoire
```

### Solution avec un générateur

```python
# Générateur qui produit les mêmes données
def generer_grandes_donnees():
    for x in range(1000000):
        yield x * 2

# Cette fonction utilise très peu de mémoire !
grandes_donnees = generer_grandes_donnees()  # Quelques bytes seulement
```

## Le mot-clé `yield`

### Différence entre `return` et `yield`

```python
# Fonction normale avec return
def fonction_normale():
    return [1, 2, 3]

# Fonction générateur avec yield
def fonction_generateur():
    yield 1
    yield 2
    yield 3

# Comparaison
normale = fonction_normale()
print(type(normale))  # <class 'list'>
print(normale)        # [1, 2, 3]

generateur = fonction_generateur()
print(type(generateur))  # <class 'generator'>
print(generateur)        # <generator object fonction_generateur at 0x...>
```

### Comment utiliser un générateur

```python
def compter_jusqu_a(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Utilisation avec une boucle for
for nombre in compter_jusqu_a(5):
    print(nombre)
# Sortie : 1, 2, 3, 4, 5

# Conversion en liste si nécessaire
liste = list(compter_jusqu_a(5))
print(liste)  # [1, 2, 3, 4, 5]
```

## Fonctionnement interne des générateurs

### État suspendu

```python
def demo_yield():
    print("Début du générateur")
    yield 1
    print("Après le premier yield")
    yield 2
    print("Après le deuxième yield")
    yield 3
    print("Fin du générateur")

# Créer le générateur
gen = demo_yield()

# Appeler next() manuellement
print("Premier next():")
print(next(gen))  # 1

print("Deuxième next():")
print(next(gen))  # 2

print("Troisième next():")
print(next(gen))  # 3

# print(next(gen))  # ❌ StopIteration exception
```

### Utilisation avec next()

```python
def fibonacci_generateur():
    a, b = 0, 1
    while True:  # Générateur infini !
        yield a
        a, b = b, a + b

# Utilisation
fib = fibonacci_generateur()
for _ in range(10):
    print(next(fib), end=" ")
# Sortie : 0 1 1 2 3 5 8 13 21 34
```

## Exemples pratiques de générateurs

### 1. Lecture de fichiers volumineux

```python
def lire_fichier_par_lignes(nom_fichier):
    """Lit un fichier ligne par ligne sans tout charger en mémoire"""
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                yield ligne.strip()
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} non trouvé")
        return

# Utilisation
def compter_lignes(nom_fichier):
    compteur = 0
    for ligne in lire_fichier_par_lignes(nom_fichier):
        compteur += 1
    return compteur

# Cette fonction peut traiter des fichiers de plusieurs GB !
```

### 2. Génération de mots de passe

```python
import random
import string

def generateur_mots_de_passe(longueur=8):
    """Génère des mots de passe aléatoirement"""
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"

    while True:  # Générateur infini
        mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
        yield mot_de_passe

# Utilisation
gen_mdp = generateur_mots_de_passe(12)

# Générer 5 mots de passe
for _ in range(5):
    print(next(gen_mdp))
```

### 3. Traitement de données par lots

```python
def traiter_par_lots(donnees, taille_lot):
    """Divise une séquence en lots de taille donnée"""
    lot = []
    for element in donnees:
        lot.append(element)
        if len(lot) == taille_lot:
            yield lot
            lot = []

    # Yield du dernier lot s'il n'est pas vide
    if lot:
        yield lot

# Exemple d'utilisation
nombres = range(1, 23)  # 1 à 22
for lot in traiter_par_lots(nombres, 5):
    print(f"Lot: {list(lot)}")

# Sortie :
# Lot: [1, 2, 3, 4, 5]
# Lot: [6, 7, 8, 9, 10]
# Lot: [11, 12, 13, 14, 15]
# Lot: [16, 17, 18, 19, 20]
# Lot: [21, 22]
```

### 4. Simulation de données en temps réel

```python
import time
import random

def capteur_temperature():
    """Simule un capteur de température"""
    temperature_base = 20.0

    while True:
        # Variation aléatoire de température
        variation = random.uniform(-2, 2)
        temperature = temperature_base + variation

        yield {
            'timestamp': time.time(),
            'temperature': round(temperature, 1),
            'unite': 'Celsius'
        }

        temperature_base = temperature  # Évolution graduelle
        time.sleep(1)  # Pause d'une seconde

# Utilisation
def monitorer_temperature(duree_secondes):
    capteur = capteur_temperature()
    debut = time.time()

    while time.time() - debut < duree_secondes:
        donnee = next(capteur)
        print(f"Température: {donnee['temperature']}°C à {time.ctime(donnee['timestamp'])}")

# monitorer_temperature(10)  # Monitorer pendant 10 secondes
```

## Expressions génératrices

Les expressions génératrices sont une syntaxe concise pour créer des générateurs, similaire aux compréhensions de liste mais avec des parenthèses.

### Syntaxe de base

```python
# Compréhension de liste (crée toute la liste en mémoire)
carres_liste = [x**2 for x in range(10)]
print(type(carres_liste))  # <class 'list'>

# Expression génératrice (crée un générateur)
carres_gen = (x**2 for x in range(10))
print(type(carres_gen))    # <class 'generator'>

# Utilisation identique
for carre in carres_gen:
    print(carre, end=" ")
# Sortie : 0 1 4 9 16 25 36 49 64 81
```

### Comparaison mémoire

```python
import sys

# Listes - consomment de la mémoire
grandes_donnees_liste = [x * 2 for x in range(100000)]
print(f"Taille de la liste: {sys.getsizeof(grandes_donnees_liste)} bytes")

# Générateurs - consomment très peu de mémoire
grandes_donnees_gen = (x * 2 for x in range(100000))
print(f"Taille du générateur: {sys.getsizeof(grandes_donnees_gen)} bytes")

# Résultat typique :
# Taille de la liste: 824464 bytes
# Taille du générateur: 112 bytes
```

### Exemples d'expressions génératrices

#### 1. Filtrage et transformation

```python
# Trouver les carrés des nombres pairs
nombres = range(1, 11)
carres_pairs = (x**2 for x in nombres if x % 2 == 0)

print("Carrés des nombres pairs:")
for carre in carres_pairs:
    print(carre, end=" ")
# Sortie : 4 16 36 64 100
```

#### 2. Traitement de chaînes

```python
phrases = [
    "Bonjour tout le monde",
    "Python est génial",
    "Les générateurs sont utiles"
]

# Compter les mots dans chaque phrase
nb_mots = (len(phrase.split()) for phrase in phrases)
print("Nombre de mots par phrase:", list(nb_mots))
# Sortie : [4, 3, 4]

# Extraire les mots longs (> 5 caractères)
mots_longs = (mot for phrase in phrases
              for mot in phrase.split()
              if len(mot) > 5)

print("Mots longs:", list(mots_longs))
# Sortie : ['Bonjour', 'Python', 'génial', 'générateurs']
```

#### 3. Avec des fonctions intégrées

```python
# Utilisation avec sum()
somme_carres = sum(x**2 for x in range(1, 6))
print(f"Somme des carrés: {somme_carres}")  # 55

# Utilisation avec max()
temperatures = [18.5, 22.1, 19.8, 25.3, 20.7]
temp_fahrenheit = (temp * 9/5 + 32 for temp in temperatures)
temp_max = max(temp_fahrenheit)
print(f"Température max en Fahrenheit: {temp_max}")  # 77.54

# Utilisation avec any() et all()
nombres = [2, 4, 6, 8, 10]
tous_pairs = all(x % 2 == 0 for x in nombres)
print(f"Tous pairs: {tous_pairs}")  # True
```

## Générateurs avancés

### 1. Générateur avec paramètres

```python
def progression_arithmetique(debut, fin, pas=1):
    """Générateur de progression arithmétique"""
    actuel = debut
    while actuel < fin:
        yield actuel
        actuel += pas

# Utilisation
for nombre in progression_arithmetique(0, 10, 2):
    print(nombre, end=" ")
# Sortie : 0 2 4 6 8

print()
for nombre in progression_arithmetique(1, 2, 0.1):
    print(round(nombre, 1), end=" ")
# Sortie : 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9
```

### 2. Générateur récursif

```python
def parcourir_repertoire(chemin):
    """Parcourt récursivement un répertoire"""
    import os

    try:
        for element in os.listdir(chemin):
            chemin_complet = os.path.join(chemin, element)
            yield chemin_complet

            if os.path.isdir(chemin_complet):
                # Récursion avec yield from
                yield from parcourir_repertoire(chemin_complet)
    except PermissionError:
        pass  # Ignorer les répertoires non accessibles

# Utilisation (attention à la taille !)
# for fichier in parcourir_repertoire("/mon/repertoire"):
#     print(fichier)
```

### 3. Générateur avec état persistant

```python
def compteur_avec_memoire(initial=0):
    """Générateur qui garde son état"""
    compteur = initial

    while True:
        commande = yield compteur
        if commande == "increment":
            compteur += 1
        elif commande == "decrement":
            compteur -= 1
        elif commande == "reset":
            compteur = initial
        elif isinstance(commande, int):
            compteur = commande

# Utilisation
compteur = compteur_avec_memoire(10)
print(next(compteur))  # 10

print(compteur.send("increment"))  # 11
print(compteur.send("increment"))  # 12
print(compteur.send("decrement"))  # 11
print(compteur.send(100))          # 100
print(compteur.send("reset"))      # 10
```

## Pipeline de générateurs

Les générateurs peuvent être chaînés pour créer des pipelines de traitement efficaces.

```python
def lire_nombres(fichier_nom):
    """Générateur qui lit des nombres depuis un fichier"""
    # Simulation de lecture de fichier
    donnees = ["1", "2", "3", "4", "5", "abc", "6", "7"]
    for ligne in donnees:
        yield ligne.strip()

def convertir_en_nombres(lignes):
    """Convertit les lignes en nombres, ignore les erreurs"""
    for ligne in lignes:
        try:
            yield int(ligne)
        except ValueError:
            continue  # Ignorer les lignes non numériques

def filtrer_pairs(nombres):
    """Garde seulement les nombres pairs"""
    for nombre in nombres:
        if nombre % 2 == 0:
            yield nombre

def mettre_au_carre(nombres):
    """Met au carré chaque nombre"""
    for nombre in nombres:
        yield nombre ** 2

# Pipeline de traitement
def traiter_donnees(fichier):
    lignes = lire_nombres(fichier)
    nombres = convertir_en_nombres(lignes)
    pairs = filtrer_pairs(nombres)
    carres = mettre_au_carre(pairs)
    return carres

# Utilisation
resultat = traiter_donnees("donnees.txt")
print("Carrés des nombres pairs:", list(resultat))
# Sortie : [4, 16, 36]

# Version plus concise avec les expressions génératrices
def traiter_donnees_concis(fichier):
    lignes = lire_nombres(fichier)
    return (int(ligne)**2 for ligne in lignes
            if ligne.isdigit() and int(ligne) % 2 == 0)
```

## Avantages et inconvénients

### ✅ Avantages des générateurs

1. **Efficacité mémoire** : Ne stockent qu'un élément à la fois
2. **Évaluation paresseuse** : Calculent seulement ce qui est nécessaire
3. **Composition facile** : Peuvent être chaînés facilement
4. **Séquences infinies** : Peuvent représenter des séquences illimitées
5. **Lisibilité** : Code souvent plus clair que les itérateurs classiques

### ❌ Inconvénients

1. **Usage unique** : Un générateur ne peut être parcouru qu'une fois
2. **Pas d'accès aléatoire** : Impossible d'accéder à un élément spécifique
3. **Pas de len()** : Impossible de connaître la taille sans consommer
4. **Débogage plus difficile** : L'état est suspendu entre les yields

## Cas d'usage recommandés

### Utilisez des générateurs pour :

- **Fichiers volumineux** : Lecture ligne par ligne
- **Séquences infinies** : Suites mathématiques, flux de données
- **Transformation de données** : Pipelines de traitement
- **Économie de mémoire** : Quand la mémoire est limitée
- **APIs paginées** : Récupération de données par pages

### Utilisez des listes pour :

- **Petites collections** : Quand la mémoire n'est pas un problème
- **Accès multiple** : Quand vous devez parcourir plusieurs fois
- **Accès aléatoire** : Quand vous avez besoin d'indexation
- **Opérations de liste** : Tri, insertion, suppression

## Exercices pratiques

### Exercice 1 : Générateur de nombres premiers

```python
def est_premier(n):
    """Vérifie si un nombre est premier"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generateur_premiers(limite=None):
    """Génère des nombres premiers"""
    n = 2
    while limite is None or n <= limite:
        if est_premier(n):
            yield n
        n += 1

# Test
premiers = generateur_premiers(50)
print("Premiers jusqu'à 50:", list(premiers))

# Premiers 10 nombres premiers
premiers_infinis = generateur_premiers()
premiers_10 = []
for _ in range(10):
    premiers_10.append(next(premiers_infinis))
print("10 premiers nombres premiers:", premiers_10)
```

### Exercice 2 : Générateur de données CSV

```python
def generer_donnees_csv():
    """Génère des données CSV factices"""
    import random

    noms = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    departements = ["IT", "RH", "Finance", "Marketing"]

    # En-tête
    yield "nom,age,departement,salaire"

    # Données
    for i in range(100):
        nom = random.choice(noms)
        age = random.randint(22, 65)
        dept = random.choice(departements)
        salaire = random.randint(30000, 100000)
        yield f"{nom},{age},{dept},{salaire}"

# Utilisation
def sauvegarder_csv(nom_fichier, generateur):
    with open(nom_fichier, 'w') as f:
        for ligne in generateur:
            f.write(ligne + '\n')

# sauvegarder_csv("employes.csv", generer_donnees_csv())
```

### Exercice 3 : Expression génératrice pour analyse de texte

```python
def analyser_texte(texte):
    """Analyse un texte avec des expressions génératrices"""

    # Diviser en mots et nettoyer
    mots = (mot.lower().strip('.,!?;:"()[]')
            for mot in texte.split())

    # Filtrer les mots vides
    mots_significatifs = (mot for mot in mots
                         if len(mot) > 2 and mot.isalpha())

    # Convertir en liste pour analyse
    mots_liste = list(mots_significatifs)

    # Statistiques avec expressions génératrices
    longueurs = list(len(mot) for mot in mots_liste)

    return {
        'nb_mots': len(mots_liste),
        'mots_uniques': len(set(mots_liste)),
        'longueur_moyenne': sum(longueurs) / len(longueurs) if longueurs else 0,
        'mot_plus_long': max(mots_liste, key=len) if mots_liste else '',
        'mots_longs': list(mot for mot in mots_liste if len(mot) > 6)
    }

# Test
texte = """
Python est un langage de programmation puissant et facile à apprendre.
Les générateurs sont une fonctionnalité remarquable qui permet
d'économiser la mémoire lors du traitement de grandes quantités de données.
"""

resultat = analyser_texte(texte)
for cle, valeur in resultat.items():
    print(f"{cle}: {valeur}")
```

## Résumé

Les générateurs et expressions génératrices sont des outils essentiels pour :

- **Économiser la mémoire** en traitant les données à la demande
- **Créer des séquences infinies** ou très longues
- **Construire des pipelines** de traitement de données
- **Améliorer les performances** pour les gros volumes de données

**Points clés à retenir :**
- `yield` suspend l'exécution et retourne une valeur
- Les générateurs ne peuvent être parcourus qu'une fois
- Les expressions génératrices utilisent `()` au lieu de `[]`
- Parfaits pour les gros fichiers et flux de données
- Se combinent bien avec les autres outils de programmation fonctionnelle

Dans la prochaine section, nous explorerons les closures et les patterns fonctionnels avancés qui complètent notre boîte à outils de programmation fonctionnelle.

⏭️
