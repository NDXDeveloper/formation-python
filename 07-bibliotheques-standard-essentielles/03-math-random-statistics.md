🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.3 : math, random, statistics

## Introduction

Python fournit trois modules essentiels pour les calculs mathématiques : `math` pour les fonctions mathématiques de base, `random` pour la génération de nombres aléatoires, et `statistics` pour les calculs statistiques. Ces modules couvrent la plupart des besoins mathématiques courants.

### Analogie simple
Imaginez une **boîte à outils mathématiques** :
- **math** : la **calculatrice scientifique** (trigonométrie, logarithmes, constantes)
- **random** : les **dés et cartes** (hasard, échantillonnage, simulations)
- **statistics** : la **calculatrice statistique** (moyennes, médianes, corrélations)

## Module math : Fonctions mathématiques de base

Le module `math` fournit des fonctions mathématiques avancées et des constantes importantes.

### Constantes mathématiques

```python
import math

# Constantes importantes
print(f"π (pi) = {math.pi}")
print(f"e (euler) = {math.e}")
print(f"τ (tau = 2π) = {math.tau}")
print(f"Infini = {math.inf}")
print(f"NaN (Not a Number) = {math.nan}")

# Test de valeurs spéciales
print(f"math.inf > 1000000 : {math.inf > 1000000}")
print(f"math.isnan(math.nan) : {math.isnan(math.nan)}")
print(f"math.isinf(math.inf) : {math.isinf(math.inf)}")
```

### Fonctions de base

```python
import math

# Fonctions de puissance et racines
nombre = 16
print(f"Racine carrée de {nombre} : {math.sqrt(nombre)}")
print(f"Racine cubique de 27 : {math.pow(27, 1/3)}")
print(f"2 puissance 8 : {math.pow(2, 8)}")

# Arrondis et valeurs absolues
x = 3.7
print(f"Plafond de {x} : {math.ceil(x)}")  # 4
print(f"Plancher de {x} : {math.floor(x)}")  # 3
print(f"Troncature de {x} : {math.trunc(x)}")  # 3
print(f"Valeur absolue de -5.2 : {math.fabs(-5.2)}")

# Fonctions logarithmiques
print(f"log naturel de e : {math.log(math.e)}")  # 1.0
print(f"log base 10 de 100 : {math.log10(100)}")  # 2.0
print(f"log base 2 de 8 : {math.log2(8)}")  # 3.0
```

### Trigonométrie

```python
import math

def demo_trigonometrie():
    """Démonstration des fonctions trigonométriques."""

    # Conversion degrés <-> radians
    angle_degres = 45
    angle_radians = math.radians(angle_degres)

    print(f"45° = {angle_radians:.4f} radians")
    print(f"{angle_radians:.4f} radians = {math.degrees(angle_radians)}°")

    # Fonctions trigonométriques principales
    print(f"\nPour un angle de 45° :")
    print(f"sin(45°) = {math.sin(angle_radians):.4f}")
    print(f"cos(45°) = {math.cos(angle_radians):.4f}")
    print(f"tan(45°) = {math.tan(angle_radians):.4f}")

    # Fonctions inverses
    print(f"\nFonctions inverses :")
    print(f"arcsin(0.5) = {math.degrees(math.asin(0.5)):.1f}°")
    print(f"arccos(0.5) = {math.degrees(math.acos(0.5)):.1f}°")
    print(f"arctan(1) = {math.degrees(math.atan(1)):.1f}°")

demo_trigonometrie()
```

### Exemple pratique : Calculatrice scientifique

```python
import math

class CalculatriceScientifique:
    """Calculatrice scientifique simple."""

    @staticmethod
    def distance_entre_points(x1, y1, x2, y2):
        """Calcule la distance entre deux points."""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    @staticmethod
    def aire_cercle(rayon):
        """Calcule l'aire d'un cercle."""
        return math.pi * rayon**2

    @staticmethod
    def volume_sphere(rayon):
        """Calcule le volume d'une sphère."""
        return (4/3) * math.pi * rayon**3

    @staticmethod
    def resoudre_triangle_rectangle(a, b):
        """Résout un triangle rectangle (trouve l'hypoténuse et les angles)."""
        hypotenuse = math.sqrt(a**2 + b**2)
        angle_a = math.degrees(math.atan(a/b))
        angle_b = math.degrees(math.atan(b/a))

        return {
            'hypotenuse': hypotenuse,
            'angle_a': angle_a,
            'angle_b': angle_b,
            'angle_c': 90
        }

# Test de la calculatrice
calc = CalculatriceScientifique()

print("🧮 CALCULATRICE SCIENTIFIQUE")
print("-" * 30)

# Distance entre points
distance = calc.distance_entre_points(0, 0, 3, 4)
print(f"Distance entre (0,0) et (3,4) : {distance}")

# Géométrie
print(f"Aire d'un cercle de rayon 5 : {calc.aire_cercle(5):.2f}")
print(f"Volume d'une sphère de rayon 3 : {calc.volume_sphere(3):.2f}")

# Triangle rectangle
triangle = calc.resoudre_triangle_rectangle(3, 4)
print(f"Triangle rectangle (3,4) :")
print(f"  Hypoténuse : {triangle['hypotenuse']:.2f}")
print(f"  Angles : {triangle['angle_a']:.1f}°, {triangle['angle_b']:.1f}°, {triangle['angle_c']}°")
```

## Module random : Génération de nombres aléatoires

Le module `random` permet de générer des nombres aléatoires et de faire des échantillonnages.

### Nombres aléatoires de base

```python
import random

# Initialiser le générateur (optionnel, pour la reproductibilité)
random.seed(42)

# Nombres aléatoires flottants
print("Nombres aléatoires flottants :")
for i in range(5):
    print(f"  {random.random():.4f}")  # Entre 0.0 et 1.0

# Nombres entiers
print(f"\nNombres entiers :")
print(f"Entre 1 et 10 : {random.randint(1, 10)}")
print(f"Entre 0 et 99 : {random.randrange(100)}")
print(f"Entre 10 et 50 (pas de 5) : {random.randrange(10, 51, 5)}")

# Nombres flottants dans une plage
print(f"\nNombres flottants dans une plage :")
print(f"Entre 1.0 et 10.0 : {random.uniform(1.0, 10.0):.2f}")
```

### Choix et échantillonnage

```python
import random

# Listes pour les exemples
couleurs = ['rouge', 'bleu', 'vert', 'jaune', 'orange']
cartes = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']

# Choix aléatoires
print("Choix aléatoires :")
print(f"Couleur aléatoire : {random.choice(couleurs)}")
print(f"Carte aléatoire : {random.choice(cartes)}")

# Échantillonnage sans remise
print(f"\nÉchantillonnage (3 couleurs différentes) :")
echantillon = random.sample(couleurs, 3)
print(f"  {echantillon}")

# Choix avec pondération (Python 3.6+)
fruits = ['pomme', 'banane', 'orange']
poids = [0.5, 0.3, 0.2]  # Pomme plus probable
print(f"\nChoix pondéré : {random.choices(fruits, weights=poids, k=5)}")

# Mélanger une liste
nombres = list(range(1, 11))
print(f"Liste originale : {nombres}")
random.shuffle(nombres)
print(f"Liste mélangée : {nombres}")
```

### Distributions statistiques

```python
import random

def demo_distributions():
    """Démonstration des différentes distributions."""

    print("📊 DISTRIBUTIONS STATISTIQUES")
    print("-" * 35)

    # Distribution normale (gaussienne)
    print("Distribution normale (moyenne=100, écart-type=15) :")
    for i in range(5):
        valeur = random.gauss(100, 15)
        print(f"  {valeur:.1f}")

    # Distribution exponentielle
    print(f"\nDistribution exponentielle (lambda=1.5) :")
    for i in range(5):
        valeur = random.expovariate(1.5)
        print(f"  {valeur:.2f}")

    # Distribution uniforme
    print(f"\nDistribution uniforme entre 10 et 20 :")
    for i in range(5):
        valeur = random.uniform(10, 20)
        print(f"  {valeur:.2f}")

demo_distributions()
```

### Exemple pratique : Générateur de mots de passe

```python
import random
import string

class GenerateurMotDePasse:
    """Générateur de mots de passe sécurisés."""

    def __init__(self):
        self.minuscules = string.ascii_lowercase
        self.majuscules = string.ascii_uppercase
        self.chiffres = string.digits
        self.symboles = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generer_simple(self, longueur=8):
        """Génère un mot de passe simple (lettres et chiffres)."""
        caracteres = self.minuscules + self.majuscules + self.chiffres
        return ''.join(random.choice(caracteres) for _ in range(longueur))

    def generer_securise(self, longueur=12):
        """Génère un mot de passe sécurisé avec tous types de caractères."""
        # Garantir au moins un caractère de chaque type
        mot_de_passe = [
            random.choice(self.minuscules),
            random.choice(self.majuscules),
            random.choice(self.chiffres),
            random.choice(self.symboles)
        ]

        # Compléter avec des caractères aléatoires
        tous_caracteres = self.minuscules + self.majuscules + self.chiffres + self.symboles
        for _ in range(longueur - 4):
            mot_de_passe.append(random.choice(tous_caracteres))

        # Mélanger pour éviter un pattern prévisible
        random.shuffle(mot_de_passe)
        return ''.join(mot_de_passe)

    def generer_memorable(self, nb_mots=4):
        """Génère un mot de passe mémorable avec des mots."""
        mots = [
            'soleil', 'ocean', 'montagne', 'foret', 'riviere', 'nuage', 'etoile', 'lune',
            'chat', 'chien', 'oiseau', 'poisson', 'arbre', 'fleur', 'pierre', 'vent'
        ]

        mots_choisis = random.sample(mots, nb_mots)
        # Capitaliser aléatoirement et ajouter des chiffres
        for i in range(len(mots_choisis)):
            if random.choice([True, False]):
                mots_choisis[i] = mots_choisis[i].capitalize()

        # Ajouter un nombre à la fin
        nombre = random.randint(10, 99)
        return '-'.join(mots_choisis) + str(nombre)

# Test du générateur
generateur = GenerateurMotDePasse()

print("🔐 GÉNÉRATEUR DE MOTS DE PASSE")
print("-" * 35)
print(f"Simple (8 chars) : {generateur.generer_simple()}")
print(f"Sécurisé (12 chars) : {generateur.generer_securise()}")
print(f"Mémorable : {generateur.generer_memorable()}")
```

## Module statistics : Calculs statistiques

Le module `statistics` fournit des fonctions pour calculer des statistiques descriptives.

### Mesures de tendance centrale

```python
import statistics

# Données d'exemple
notes = [12, 15, 18, 11, 16, 14, 17, 13, 19, 15]
ages = [25, 30, 35, 28, 32, 29, 31, 27, 33, 30]

print("📊 MESURES DE TENDANCE CENTRALE")
print("-" * 40)

# Moyenne
print(f"Notes : {notes}")
print(f"Moyenne : {statistics.mean(notes):.2f}")
print(f"Moyenne harmonique : {statistics.harmonic_mean(notes):.2f}")
print(f"Moyenne géométrique : {statistics.geometric_mean(notes):.2f}")

# Médiane
print(f"\nÂges : {ages}")
print(f"Médiane : {statistics.median(ages)}")
print(f"Médiane faible : {statistics.median_low(ages)}")
print(f"Médiane haute : {statistics.median_high(ages)}")

# Mode (valeur la plus fréquente)
donnees_mode = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"\nDonnées : {donnees_mode}")
print(f"Mode : {statistics.mode(donnees_mode)}")

# Multimode (plusieurs modes)
try:
    modes = statistics.multimode([1, 1, 2, 2, 3])
    print(f"Multimodes : {modes}")
except AttributeError:
    print("multimode() disponible à partir de Python 3.8")
```

### Mesures de dispersion

```python
import statistics

donnees = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

print("📐 MESURES DE DISPERSION")
print("-" * 30)
print(f"Données : {donnees}")

# Variance et écart-type
print(f"Variance (population) : {statistics.pvariance(donnees):.2f}")
print(f"Variance (échantillon) : {statistics.variance(donnees):.2f}")
print(f"Écart-type (population) : {statistics.pstdev(donnees):.2f}")
print(f"Écart-type (échantillon) : {statistics.stdev(donnees):.2f}")

# Quartiles et percentiles (Python 3.8+)
try:
    q1 = statistics.quantiles(donnees, n=4)[0]  # Premier quartile
    q3 = statistics.quantiles(donnees, n=4)[2]  # Troisième quartile
    print(f"Q1 (25e percentile) : {q1}")
    print(f"Q3 (75e percentile) : {q3}")
    print(f"IQR (écart interquartile) : {q3 - q1}")
except AttributeError:
    print("quantiles() disponible à partir de Python 3.8")
```

### Exemple pratique : Analyseur de données simples

```python
import statistics
import math

class AnalyseurDonnees:
    """Analyseur statistique simple pour des listes de nombres."""

    def __init__(self, donnees):
        self.donnees = list(donnees)
        self.donnees_triees = sorted(self.donnees)

    def resume_statistique(self):
        """Retourne un résumé statistique complet."""
        if not self.donnees:
            return "Aucune donnée à analyser"

        n = len(self.donnees)

        resume = {
            'count': n,
            'min': min(self.donnees),
            'max': max(self.donnees),
            'etendue': max(self.donnees) - min(self.donnees),
            'moyenne': statistics.mean(self.donnees),
            'mediane': statistics.median(self.donnees),
            'variance': statistics.variance(self.donnees) if n > 1 else 0,
            'ecart_type': statistics.stdev(self.donnees) if n > 1 else 0
        }

        return resume

    def detecter_outliers(self, seuil=2):
        """Détecte les valeurs aberrantes (outliers)."""
        if len(self.donnees) < 3:
            return []

        moyenne = statistics.mean(self.donnees)
        ecart_type = statistics.stdev(self.donnees)

        outliers = []
        for valeur in self.donnees:
            z_score = abs(valeur - moyenne) / ecart_type
            if z_score > seuil:
                outliers.append(valeur)

        return outliers

    def afficher_rapport(self):
        """Affiche un rapport statistique complet."""
        resume = self.resume_statistique()

        print("📊 RAPPORT STATISTIQUE")
        print("-" * 30)
        print(f"Nombre de valeurs : {resume['count']}")
        print(f"Minimum : {resume['min']}")
        print(f"Maximum : {resume['max']}")
        print(f"Étendue : {resume['etendue']}")
        print(f"Moyenne : {resume['moyenne']:.2f}")
        print(f"Médiane : {resume['mediane']:.2f}")
        print(f"Variance : {resume['variance']:.2f}")
        print(f"Écart-type : {resume['ecart_type']:.2f}")

        # Coefficient de variation
        if resume['moyenne'] != 0:
            cv = (resume['ecart_type'] / resume['moyenne']) * 100
            print(f"Coefficient de variation : {cv:.1f}%")

        # Outliers
        outliers = self.detecter_outliers()
        if outliers:
            print(f"Valeurs aberrantes : {outliers}")
        else:
            print("Aucune valeur aberrante détectée")

# Test de l'analyseur
donnees_test = [85, 90, 78, 92, 88, 76, 95, 82, 87, 91, 45]  # Note: 45 est aberrante

analyseur = AnalyseurDonnees(donnees_test)
print(f"Données analysées : {donnees_test}")
analyseur.afficher_rapport()
```

## Exercices pratiques

### Exercice 1 : Simulateur de dés

```python
import random

def lancer_des(nb_des=2, nb_faces=6, nb_lancers=1):
    """Simule le lancement de dés."""
    resultats = []

    for _ in range(nb_lancers):
        lancer = [random.randint(1, nb_faces) for _ in range(nb_des)]
        resultats.append(lancer)

    return resultats

def analyser_lancers(resultats):
    """Analyse les résultats des lancers."""
    sommes = [sum(lancer) for lancer in resultats]

    print(f"🎲 Résultats de {len(resultats)} lancer(s) :")
    for i, lancer in enumerate(resultats, 1):
        print(f"  Lancer {i}: {lancer} → Somme: {sum(lancer)}")

    if len(sommes) > 1:
        print(f"\n📊 Statistiques des sommes :")
        print(f"  Moyenne : {statistics.mean(sommes):.2f}")
        print(f"  Min/Max : {min(sommes)}/{max(sommes)}")

# Test
resultats = lancer_des(nb_des=2, nb_faces=6, nb_lancers=10)
analyser_lancers(resultats)
```

### Exercice 2 : Calculateur de prêt

```python
import math

def calculer_mensualite(capital, taux_annuel, duree_annees):
    """Calcule la mensualité d'un prêt."""
    taux_mensuel = taux_annuel / 12 / 100
    nb_mensualites = duree_annees * 12

    if taux_mensuel == 0:
        return capital / nb_mensualites

    mensualite = capital * (taux_mensuel * (1 + taux_mensuel)**nb_mensualites) / \
                 ((1 + taux_mensuel)**nb_mensualites - 1)

    return mensualite

def analyser_pret(capital, taux_annuel, duree_annees):
    """Analyse complète d'un prêt."""
    mensualite = calculer_mensualite(capital, taux_annuel, duree_annees)
    cout_total = mensualite * duree_annees * 12
    cout_credit = cout_total - capital

    print(f"💰 ANALYSE DE PRÊT")
    print(f"Capital emprunté : {capital:,.0f}€")
    print(f"Taux annuel : {taux_annuel}%")
    print(f"Durée : {duree_annees} ans")
    print(f"Mensualité : {mensualite:.2f}€")
    print(f"Coût total : {cout_total:,.0f}€")
    print(f"Coût du crédit : {cout_credit:,.0f}€")

# Test
analyser_pret(200000, 3.5, 25)
```

### Exercice 3 : Générateur de quiz mathématique

```python
import random
import math

def generer_question():
    """Génère une question mathématique aléatoire."""
    type_question = random.choice(['addition', 'multiplication', 'racine', 'puissance'])

    if type_question == 'addition':
        a, b = random.randint(10, 100), random.randint(10, 100)
        question = f"{a} + {b}"
        reponse = a + b

    elif type_question == 'multiplication':
        a, b = random.randint(2, 15), random.randint(2, 15)
        question = f"{a} × {b}"
        reponse = a * b

    elif type_question == 'racine':
        carre = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        question = f"√{carre}"
        reponse = int(math.sqrt(carre))

    else:  # puissance
        base, exposant = random.randint(2, 5), random.randint(2, 4)
        question = f"{base}^{exposant}"
        reponse = base ** exposant

    return question, reponse

def quiz_mathematique(nb_questions=5):
    """Lance un quiz mathématique."""
    score = 0

    print("🧮 QUIZ MATHÉMATIQUE")
    print("-" * 25)

    for i in range(1, nb_questions + 1):
        question, reponse_correcte = generer_question()

        try:
            reponse_utilisateur = int(input(f"Question {i}: {question} = "))

            if reponse_utilisateur == reponse_correcte:
                print("✅ Correct !")
                score += 1
            else:
                print(f"❌ Incorrect. La réponse était {reponse_correcte}")

        except ValueError:
            print("❌ Réponse invalide")

        print()

    print(f"🏆 Score final : {score}/{nb_questions} ({score/nb_questions*100:.0f}%)")

# Lancer le quiz (décommenté pour tester)
# quiz_mathematique()
```

## Bonnes pratiques

### **1. Choix du bon module**
```python
# ✅ math pour calculs scientifiques
import math
aire = math.pi * rayon**2

# ✅ random pour simulations
import random
echantillon = random.sample(population, 100)

# ✅ statistics pour analyse de données
import statistics
moyenne = statistics.mean(donnees)
```

### **2. Gestion de la reproductibilité**
```python
import random

# ✅ Fixer la graine pour des résultats reproductibles
random.seed(42)
nombres = [random.randint(1, 10) for _ in range(5)]
# Résultat toujours identique : [7, 9, 4, 8, 1]
```

### **3. Validation des données**
```python
import statistics

def moyenne_securisee(donnees):
    if not donnees:
        raise ValueError("Liste vide")
    if not all(isinstance(x, (int, float)) for x in donnees):
        raise TypeError("Tous les éléments doivent être numériques")
    return statistics.mean(donnees)
```

## Cas d'usage courants

### **Simulations et modélisation**
- Simulations Monte Carlo
- Tests statistiques
- Modélisation de phénomènes aléatoires

### **Analyse de données**
- Statistiques descriptives
- Détection d'outliers
- Comparaison de distributions

### **Applications scientifiques**
- Calculs d'ingénierie
- Modèles physiques
- Analyses géométriques

### **Jeux et divertissement**
- Générateurs de nombres aléatoires
- Systèmes de scoring
- Simulations de jeux

## Résumé

Les trois modules mathématiques offrent :

1. **`math`** : Fonctions mathématiques avancées, constantes, trigonométrie
2. **`random`** : Génération aléatoire, échantillonnage, distributions
3. **`statistics`** : Calculs statistiques, mesures de tendance et dispersion

Ces modules permettent de résoudre la plupart des problèmes mathématiques courants en programmation, depuis les calculs scientifiques jusqu'à l'analyse statistique de données.

Dans la prochaine section, nous explorerons `itertools` et `functools` pour la programmation fonctionnelle avancée.

⏭️
