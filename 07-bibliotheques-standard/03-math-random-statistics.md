🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.3 Les modules math, random et statistics

## Introduction

Python offre trois modules essentiels pour effectuer des calculs mathématiques, générer des nombres aléatoires et réaliser des analyses statistiques. Ces modules font partie de la bibliothèque standard et sont très utilisés dans de nombreux domaines : sciences, jeux, simulations, data science, etc.

Dans cette section, nous allons explorer :
- **math** : Fonctions mathématiques avancées
- **random** : Génération de nombres aléatoires
- **statistics** : Calculs statistiques de base

---

## Le module `math` - Fonctions mathématiques

Le module `math` fournit des fonctions mathématiques standard définies par la norme C. Il est optimisé et rapide.

### Import du module

```python
import math

# Ou importer des fonctions spécifiques
from math import sqrt, pi, sin, cos
```

---

## Constantes mathématiques

Le module `math` définit plusieurs constantes utiles.

```python
import math

# Pi (π) - Rapport entre la circonférence et le diamètre d'un cercle
print(f"Pi : {math.pi}")  # 3.141592653589793

# Nombre d'Euler (e) - Base des logarithmes naturels
print(f"e : {math.e}")  # 2.718281828459045

# Tau (τ = 2π)
print(f"Tau : {math.tau}")  # 6.283185307179586

# Infini
print(f"Infini : {math.inf}")  
print(f"Infini négatif : {-math.inf}")  

# Not a Number (NaN) - Résultat d'opération invalide
print(f"NaN : {math.nan}")
```

### Exemple pratique : Calculer la circonférence d'un cercle

```python
import math

def calculer_circonference(rayon):
    """Calcule la circonférence d'un cercle"""
    return 2 * math.pi * rayon

def calculer_aire(rayon):
    """Calcule l'aire d'un cercle"""
    return math.pi * rayon ** 2

rayon = 5  
print(f"Rayon : {rayon} cm")  
print(f"Circonférence : {calculer_circonference(rayon):.2f} cm")  
print(f"Aire : {calculer_aire(rayon):.2f} cm²")  
```

---

## Fonctions de base

### Valeur absolue et signe

```python
import math

# Valeur absolue
print(math.fabs(-5.7))  # 5.7 (retourne un float)  
print(abs(-5.7))        # 5.7 (fonction built-in, peut retourner int ou float)  

# Copier le signe d'un nombre à un autre
print(math.copysign(5, -1))   # -5.0 (prend le signe de -1)  
print(math.copysign(-5, 1))   # 5.0 (prend le signe de 1)  
```

### Arrondis et troncatures

```python
import math

nombre = 3.7

# Arrondir vers le haut (plafond)
print(math.ceil(3.2))   # 4  
print(math.ceil(3.7))   # 4  
print(math.ceil(-3.2))  # -3  

# Arrondir vers le bas (plancher)
print(math.floor(3.2))   # 3  
print(math.floor(3.7))   # 3  
print(math.floor(-3.2))  # -4  

# Tronquer (supprimer la partie décimale)
print(math.trunc(3.7))   # 3  
print(math.trunc(-3.7))  # -3  

# Arrondir au plus proche (fonction built-in)
print(round(3.4))   # 3  
print(round(3.6))   # 4  
print(round(3.456, 2))  # 3.46 (2 décimales)  

# ⚠️ Arrondi bancaire ("round half to even") :
# Quand le chiffre est exactement à .5, Python arrondit vers le nombre pair
print(round(3.5))   # 4 (arrondi vers le pair)  
print(round(4.5))   # 4 (arrondi vers le pair, pas 5 !)  
```

### Exemple pratique : Calculer une facture

```python
import math

def calculer_facture(prix_unitaire, quantite, taux_tva=0.20):
    """Calcule le montant d'une facture avec TVA"""
    montant_ht = prix_unitaire * quantite
    montant_tva = montant_ht * taux_tva
    montant_ttc = montant_ht + montant_tva

    # Arrondir au centime supérieur
    montant_ttc = math.ceil(montant_ttc * 100) / 100

    return {
        'ht': round(montant_ht, 2),
        'tva': round(montant_tva, 2),
        'ttc': montant_ttc
    }

facture = calculer_facture(19.99, 3)  
print(f"Montant HT : {facture['ht']}€")  
print(f"TVA : {facture['tva']}€")  
print(f"Montant TTC : {facture['ttc']}€")  
```

---

## Puissances et racines

```python
import math

# Racine carrée
print(math.sqrt(16))     # 4.0  
print(math.sqrt(2))      # 1.4142135623730951  

# Puissance (nombre ** exposant)
print(math.pow(2, 3))    # 8.0 (2³)  
print(math.pow(5, 2))    # 25.0 (5²)  

# Alternative avec l'opérateur **
print(2 ** 3)            # 8 (peut retourner un int)

# Racine cubique (Python 3.11+)
print(math.cbrt(27))     # 3.0000000000000004

# Alternative pour Python 3.10 : utiliser la puissance 1/3
print(27 ** (1/3))       # 3.0

# Exponentielle (e^x)
print(math.exp(1))       # 2.718281828459045 (e¹)  
print(math.exp(2))       # 7.38905609893065 (e²)  

# Exponentielle - 1 (plus précise pour les petites valeurs)
print(math.expm1(0.001)) # 0.0010005001667083846
```

### Exemple pratique : Calcul d'intérêts composés

```python
import math

def calculer_interets_composes(capital, taux_annuel, duree_annees):
    """Calcule le capital final avec intérêts composés

    Formule : C_final = C_initial × (1 + taux)^durée
    """
    capital_final = capital * math.pow(1 + taux_annuel, duree_annees)
    interets = capital_final - capital

    return {
        'capital_initial': capital,
        'capital_final': round(capital_final, 2),
        'interets': round(interets, 2)
    }

# Exemple : 10 000€ à 3% sur 10 ans
resultat = calculer_interets_composes(10000, 0.03, 10)  
print(f"Capital initial : {resultat['capital_initial']}€")  
print(f"Capital final : {resultat['capital_final']}€")  
print(f"Intérêts gagnés : {resultat['interets']}€")  
```

---

## Logarithmes

```python
import math

# Logarithme naturel (base e)
print(math.log(math.e))      # 1.0  
print(math.log(10))          # 2.302585092994046  

# Logarithme base 10
print(math.log10(100))       # 2.0  
print(math.log10(1000))      # 3.0  

# Logarithme base 2
print(math.log2(8))          # 3.0  
print(math.log2(1024))       # 10.0  

# Logarithme avec base personnalisée
print(math.log(8, 2))        # 3.0 (log base 2 de 8)  
print(math.log(81, 3))       # 4.0 (log base 3 de 81)  

# Logarithme de (1 + x) - plus précis pour les petites valeurs
print(math.log1p(0.001))     # 0.0009995003330835332
```

---

## Trigonométrie

Les fonctions trigonométriques utilisent les radians par défaut.

```python
import math

# Conversions degrés ↔ radians
angle_degres = 90  
angle_radians = math.radians(angle_degres)  
print(f"{angle_degres}° = {angle_radians} radians")  # 1.5707963267948966  

angle_radians = math.pi / 2  
angle_degres = math.degrees(angle_radians)  
print(f"{angle_radians} radians = {angle_degres}°")  # 90.0  

# Fonctions trigonométriques de base
print(f"sin(π/2) = {math.sin(math.pi / 2)}")  # 1.0  
print(f"cos(π) = {math.cos(math.pi)}")        # -1.0  
print(f"tan(π/4) = {math.tan(math.pi / 4)}")  # 1.0  

# Fonctions trigonométriques inverses
print(f"asin(1) = {math.asin(1)}")    # 1.5707... (π/2 radians)  
print(f"acos(0) = {math.acos(0)}")    # 1.5707... (π/2 radians)  
print(f"atan(1) = {math.atan(1)}")    # 0.7853... (π/4 radians)  

# atan2 : arc tangente de y/x (gère les quadrants)
print(math.atan2(1, 1))    # 0.7853... (π/4 radians, 45°)  
print(math.atan2(-1, 1))   # -0.7853... (-π/4 radians, -45°)  

# Fonctions hyperboliques
print(f"sinh(1) = {math.sinh(1)}")    # 1.1752...  
print(f"cosh(0) = {math.cosh(0)}")    # 1.0  
print(f"tanh(1) = {math.tanh(1)}")    # 0.7615...  
```

### Exemple pratique : Calculer la distance entre deux points

```python
import math

def distance_euclidienne(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre deux points

    Formule : d = √[(x2-x1)² + (y2-y1)²]
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angle_entre_points(x1, y1, x2, y2):
    """Calcule l'angle entre deux points (en degrés)"""
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(angle_rad)

# Exemple
point_a = (0, 0)  
point_b = (3, 4)  

distance = distance_euclidienne(*point_a, *point_b)  
angle = angle_entre_points(*point_a, *point_b)  

print(f"Distance entre A{point_a} et B{point_b} : {distance:.2f}")  
print(f"Angle : {angle:.2f}°")  
```

---

## Autres fonctions utiles

```python
import math

# Plus grand commun diviseur (PGCD)
print(math.gcd(48, 18))      # 6  
print(math.gcd(100, 35))     # 5  

# Plus petit commun multiple (PPCM) - Python 3.9+
print(math.lcm(12, 18))      # 36  
print(math.lcm(4, 6, 8))     # 24  

# Factorielle
print(math.factorial(5))     # 120 (5! = 5×4×3×2×1)  
print(math.factorial(0))     # 1  

# Combinaisons (n parmi k) - Python 3.8+
print(math.comb(5, 2))       # 10 (nombre de façons de choisir 2 éléments parmi 5)

# Permutations (n parmi k) - Python 3.8+
print(math.perm(5, 2))       # 20 (arrangements de 2 éléments parmi 5)

# Somme précise d'un itérable (évite les erreurs d'arrondi)
nombres = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  
print(sum(nombres))          # 1.0 (peut varier selon la version de Python)  
print(math.fsum(nombres))    # 1.0 (plus précis)  

# Produit d'un itérable - Python 3.8+
print(math.prod([2, 3, 4]))  # 24

# Hypoténuse (√(x² + y²))
print(math.hypot(3, 4))      # 5.0  
print(math.hypot(5, 12))     # 13.0  
```

### Exemple pratique : Calculateur de probabilités

```python
import math

def probabilite_combinaison(n, k):
    """Calcule la probabilité de k succès parmi n essais

    Utilise la formule des combinaisons : C(n,k) = n! / (k! × (n-k)!)
    """
    return math.comb(n, k)

def probabilite_tirage(k_succes, n_total, k_tires):
    """Probabilité de tirer k_succes éléments réussis
    parmi k_tires tirés dans un ensemble de n_total
    """
    combinaisons_favorables = math.comb(k_succes, k_tires)
    combinaisons_totales = math.comb(n_total, k_tires)
    return combinaisons_favorables / combinaisons_totales

# Exemple : Loto (choisir 5 numéros parmi 49)
total_combinaisons = math.comb(49, 5)  
print(f"Nombre de combinaisons possibles au loto : {total_combinaisons:,}")  
print(f"Probabilité de gagner : 1/{total_combinaisons:,}")  
print(f"Soit : {(1/total_combinaisons)*100:.10f}%")  
```

---

## Le module `random` - Génération de nombres aléatoires

Le module `random` permet de générer des nombres pseudo-aléatoires, utiles pour les simulations, les jeux, l'échantillonnage, etc.

### Import du module

```python
import random
```

---

## Nombres aléatoires de base

```python
import random

# Nombre flottant aléatoire entre 0.0 et 1.0 (exclu)
print(random.random())  # Ex: 0.8472517035298476

# Nombre flottant aléatoire dans un intervalle [a, b]
print(random.uniform(1.0, 10.0))  # Ex: 5.349217854

# Nombre entier aléatoire dans un intervalle [a, b] (inclus)
print(random.randint(1, 10))      # Ex: 7

# Nombre entier dans un intervalle avec un pas
# range(start, stop, step)
print(random.randrange(0, 100, 5))  # Ex: 45 (multiple de 5 entre 0 et 100)
```

### Exemple pratique : Lancer de dés

```python
import random

def lancer_de(faces=6):
    """Simule le lancer d'un dé"""
    return random.randint(1, faces)

def lancer_plusieurs_des(nombre, faces=6):
    """Simule le lancer de plusieurs dés"""
    return [lancer_de(faces) for _ in range(nombre)]

# Lancer un dé à 6 faces
print(f"Résultat du dé : {lancer_de()}")

# Lancer deux dés
des = lancer_plusieurs_des(2)  
print(f"Résultat des dés : {des}")  
print(f"Total : {sum(des)}")  

# Lancer un dé à 20 faces (jeu de rôle)
print(f"Dé à 20 faces : {lancer_de(20)}")
```

---

## Choix aléatoires dans une séquence

```python
import random

couleurs = ["rouge", "bleu", "vert", "jaune", "noir", "blanc"]

# Choisir un élément au hasard
print(random.choice(couleurs))  # Ex: "vert"

# Choisir plusieurs éléments avec remise (peuvent se répéter)
print(random.choices(couleurs, k=3))  # Ex: ['bleu', 'bleu', 'rouge']

# Choisir plusieurs éléments sans remise (uniques)
print(random.sample(couleurs, k=3))  # Ex: ['noir', 'vert', 'jaune']

# Choix avec poids (probabilités différentes)
elements = ["A", "B", "C"]  
poids = [0.5, 0.3, 0.2]  # 50% A, 30% B, 20% C  
print(random.choices(elements, weights=poids, k=10))  
```

### Exemple pratique : Tirage au sort

```python
import random

def tirage_au_sort(participants, nombre_gagnants=1):
    """Effectue un tirage au sort parmi des participants"""
    if nombre_gagnants > len(participants):
        return "Pas assez de participants!"

    gagnants = random.sample(participants, nombre_gagnants)
    return gagnants

# Exemple
participants = ["Alice", "Bob", "Charlie", "David", "Emma", "Fanny"]  
print(f"Participants : {participants}")  

gagnant = tirage_au_sort(participants, 1)  
print(f"🎉 Gagnant : {gagnant[0]}")  

gagnants_multiples = tirage_au_sort(participants, 3)  
print(f"🎉 Podium : {gagnants_multiples}")  
```

---

## Mélanger une séquence

```python
import random

# Mélanger une liste (modifie la liste en place)
cartes = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7"]  
print(f"Ordre original : {cartes}")  

random.shuffle(cartes)  
print(f"Après mélange : {cartes}")  

# Si on veut garder l'original, faire une copie d'abord
cartes_originales = ["As", "Roi", "Dame", "Valet"]  
cartes_melangees = cartes_originales.copy()  
random.shuffle(cartes_melangees)  

print(f"Original : {cartes_originales}")  
print(f"Mélangé : {cartes_melangees}")  
```

### Exemple pratique : Jeu de cartes

```python
import random

class PaquetDeCartes:
    """Représente un paquet de 52 cartes"""

    def __init__(self):
        couleurs = ["♠", "♥", "♦", "♣"]
        valeurs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R"]

        self.cartes = [f"{valeur}{couleur}" for couleur in couleurs for valeur in valeurs]
        self.melanger()

    def melanger(self):
        """Mélange le paquet"""
        random.shuffle(self.cartes)
        print("🃏 Paquet mélangé")

    def tirer(self, nombre=1):
        """Tire un nombre de cartes du paquet"""
        if nombre > len(self.cartes):
            return "Plus assez de cartes!"

        cartes_tirees = [self.cartes.pop() for _ in range(nombre)]
        return cartes_tirees

    def cartes_restantes(self):
        """Retourne le nombre de cartes restantes"""
        return len(self.cartes)

# Utilisation
paquet = PaquetDeCartes()  
print(f"Cartes restantes : {paquet.cartes_restantes()}")  

main = paquet.tirer(5)  
print(f"Main tirée : {main}")  
print(f"Cartes restantes : {paquet.cartes_restantes()}")  
```

---

## Distributions de probabilité

```python
import random

# Distribution gaussienne (normale)
# mu = moyenne, sigma = écart-type
print(random.gauss(0, 1))        # Distribution normale centrée réduite  
print(random.normalvariate(100, 15))  # Moyenne 100, écart-type 15  

# Distribution triangulaire
# low <= N <= high avec mode au milieu
print(random.triangular(0, 10, 5))   # Entre 0 et 10, pic à 5

# Distribution bêta
print(random.betavariate(2, 5))      # Distribution bêta

# Distribution exponentielle
print(random.expovariate(1.5))       # Lambda = 1.5

# Distribution gamma
print(random.gammavariate(2, 3))     # Alpha = 2, bêta = 3
```

### Exemple pratique : Simulation de notes d'examen

```python
import random

def simuler_notes_examen(nombre_etudiants, moyenne=12, ecart_type=3):
    """Simule les notes d'un examen avec distribution normale"""
    notes = []

    for _ in range(nombre_etudiants):
        note = random.gauss(moyenne, ecart_type)
        # Limiter entre 0 et 20
        note = max(0, min(20, note))
        notes.append(round(note, 1))

    return notes

def analyser_notes(notes):
    """Analyse les notes"""
    notes_triees = sorted(notes, reverse=True)

    print(f"\n📊 Analyse de {len(notes)} notes :")
    print(f"Note la plus haute : {max(notes)}/20")
    print(f"Note la plus basse : {min(notes)}/20")
    print(f"Moyenne : {sum(notes)/len(notes):.1f}/20")

    # Compteur de réussite (≥10)
    reussis = sum(1 for note in notes if note >= 10)
    taux_reussite = (reussis / len(notes)) * 100
    print(f"Taux de réussite : {taux_reussite:.1f}%")

# Simulation
notes = simuler_notes_examen(30, moyenne=12, ecart_type=3)  
analyser_notes(notes)  
```

---

## Graine aléatoire (seed)

Pour obtenir des résultats reproductibles (utile pour les tests et le débogage).

```python
import random

# Définir une graine
random.seed(42)  
print(random.random())  # Toujours le même résultat avec seed=42  
print(random.randint(1, 100))  

# Réinitialiser avec la même graine
random.seed(42)  
print(random.random())  # Même résultat qu'avant  
print(random.randint(1, 100))  # Même résultat qu'avant  

# Graine aléatoire (par défaut, basée sur l'horloge système)
random.seed()  
print(random.random())  # Résultat différent à chaque exécution  
```

---

## Le module `statistics` - Statistiques de base

Le module `statistics` fournit des fonctions pour calculer des statistiques mathématiques sur des données numériques.

### Import du module

```python
import statistics
```

---

## Mesures de tendance centrale

### Moyenne (mean)

```python
import statistics

donnees = [2, 4, 6, 8, 10]

# Moyenne arithmétique
moyenne = statistics.mean(donnees)  
print(f"Moyenne : {moyenne}")  # 6.0  

# Données avec différents types
donnees_mixtes = [1, 2.5, 3, 4.5, 5]  
print(f"Moyenne : {statistics.mean(donnees_mixtes)}")  # 3.2  

# Moyenne géométrique - Python 3.8+
donnees_geo = [2, 8]  
print(f"Moyenne géométrique : {statistics.geometric_mean(donnees_geo)}")  # 4.0  

# Moyenne harmonique
# Utile pour des moyennes de taux ou de vitesses
vitesses = [30, 60, 90]  # km/h  
print(f"Moyenne harmonique : {statistics.harmonic_mean(vitesses):.2f}")  
```

### Médiane (median)

```python
import statistics

# Médiane : valeur centrale quand les données sont triées
donnees_impaires = [1, 3, 5, 7, 9]  
print(f"Médiane : {statistics.median(donnees_impaires)}")  # 5  

# Avec un nombre pair d'éléments : moyenne des deux valeurs centrales
donnees_paires = [1, 3, 5, 7, 9, 11]  
print(f"Médiane : {statistics.median(donnees_paires)}")  # 6.0  

# Médiane basse (toujours un élément de la liste)
print(f"Médiane basse : {statistics.median_low(donnees_paires)}")  # 5

# Médiane haute (toujours un élément de la liste)
print(f"Médiane haute : {statistics.median_high(donnees_paires)}")  # 7

# Médiane groupée (pour données groupées par fréquence)
print(f"Médiane groupée : {statistics.median_grouped(donnees_paires)}")
```

### Mode (mode)

```python
import statistics

# Mode : valeur la plus fréquente
donnees = [1, 2, 2, 3, 3, 3, 4, 4, 5]  
print(f"Mode : {statistics.mode(donnees)}")  # 3  

# Avec des chaînes de caractères
couleurs = ["rouge", "bleu", "rouge", "vert", "rouge", "bleu"]  
print(f"Couleur la plus fréquente : {statistics.mode(couleurs)}")  # rouge  

# Multimode : toutes les valeurs avec la fréquence maximale - Python 3.8+
donnees_multimodales = [1, 1, 2, 2, 3]  
print(f"Modes multiples : {statistics.multimode(donnees_multimodales)}")  # [1, 2]  
```

### Exemple pratique : Analyse de salaires

```python
import statistics

def analyser_salaires(salaires):
    """Analyse une liste de salaires"""
    print("💰 Analyse des salaires")
    print("=" * 50)

    print(f"Nombre d'employés : {len(salaires)}")
    print(f"Salaire moyen : {statistics.mean(salaires):,.2f}€")
    print(f"Salaire médian : {statistics.median(salaires):,.2f}€")
    print(f"Salaire min : {min(salaires):,.2f}€")
    print(f"Salaire max : {max(salaires):,.2f}€")

    # Écart entre moyenne et médiane
    ecart = statistics.mean(salaires) - statistics.median(salaires)
    print(f"Écart moyenne-médiane : {ecart:,.2f}€")

    if ecart > 0:
        print("→ Quelques salaires élevés tirent la moyenne vers le haut")
    elif ecart < 0:
        print("→ Quelques salaires bas tirent la moyenne vers le bas")
    else:
        print("→ Distribution équilibrée")

# Exemple
salaires_entreprise = [
    25000, 28000, 30000, 32000, 35000,
    38000, 40000, 42000, 45000, 50000,
    55000, 60000, 75000, 90000, 150000  # PDG
]

analyser_salaires(salaires_entreprise)
```

---

## Mesures de dispersion

### Variance et écart-type

```python
import statistics

donnees = [2, 4, 6, 8, 10]

# Variance de population
variance_pop = statistics.pvariance(donnees)  
print(f"Variance de population : {variance_pop}")  # 8.0  

# Variance d'échantillon (estimation)
variance_ech = statistics.variance(donnees)  
print(f"Variance d'échantillon : {variance_ech}")  # 10.0  

# Écart-type de population
ecart_type_pop = statistics.pstdev(donnees)  
print(f"Écart-type de population : {ecart_type_pop:.2f}")  # 2.83  

# Écart-type d'échantillon
ecart_type_ech = statistics.stdev(donnees)  
print(f"Écart-type d'échantillon : {ecart_type_ech:.2f}")  # 3.16  
```

### Quantiles

```python
import statistics

# Quantiles : valeurs qui divisent les données en parties égales
donnees = list(range(1, 101))  # 1 à 100

# Quartiles (divise en 4 parties)
quartiles = statistics.quantiles(donnees, n=4)  
print(f"Quartiles : {quartiles}")  
# Q1 (25%), Q2/médiane (50%), Q3 (75%)

# Déciles (divise en 10 parties)
deciles = statistics.quantiles(donnees, n=10)  
print(f"Premier décile : {deciles[0]}")  # 10% des valeurs sont inférieures  

# Percentiles (divise en 100 parties)
percentiles = statistics.quantiles(donnees, n=100)  
print(f"95e percentile : {percentiles[94]}")  # 95% des valeurs sont inférieures  
```

### Exemple pratique : Analyse de performances

```python
import statistics

def analyser_performances(temps_reponse):
    """Analyse les temps de réponse d'un serveur (en millisecondes)"""
    print("\n⚡ Analyse des temps de réponse")
    print("=" * 50)

    print(f"Nombre de requêtes : {len(temps_reponse)}")
    print(f"Temps moyen : {statistics.mean(temps_reponse):.2f} ms")
    print(f"Temps médian : {statistics.median(temps_reponse):.2f} ms")
    print(f"Écart-type : {statistics.stdev(temps_reponse):.2f} ms")

    # Percentiles
    quantiles = statistics.quantiles(temps_reponse, n=100)
    print(f"\nPercentiles :")
    print(f"  P50 (médiane) : {quantiles[49]:.2f} ms")
    print(f"  P90 : {quantiles[89]:.2f} ms")
    print(f"  P95 : {quantiles[94]:.2f} ms")
    print(f"  P99 : {quantiles[98]:.2f} ms")

    # Identifier les valeurs aberrantes
    moyenne = statistics.mean(temps_reponse)
    ecart_type = statistics.stdev(temps_reponse)
    seuil = moyenne + 3 * ecart_type

    valeurs_aberrantes = [t for t in temps_reponse if t > seuil]
    print(f"\n⚠️  Valeurs aberrantes (>{seuil:.0f}ms) : {len(valeurs_aberrantes)}")

# Simulation de temps de réponse
import random  
random.seed(42)  

temps_reponse = [
    random.gauss(100, 20) for _ in range(1000)  # Temps normal
]
# Ajouter quelques pics de latence
temps_reponse.extend([300, 400, 500, 600, 800])

analyser_performances(temps_reponse)
```

---

## Corrélation et covariance

```python
import statistics

# Covariance : mesure comment deux variables varient ensemble
x = [1, 2, 3, 4, 5]  
y = [2, 4, 6, 8, 10]  # y = 2x (corrélation positive parfaite)  

covariance = statistics.covariance(x, y)  
print(f"Covariance : {covariance}")  # 5.0  

# Corrélation de Pearson : entre -1 et 1
# 1 = corrélation positive parfaite
# 0 = pas de corrélation
# -1 = corrélation négative parfaite
correlation = statistics.correlation(x, y)  
print(f"Corrélation : {correlation}")  # 1.0  

# Exemple avec corrélation négative
z = [10, 8, 6, 4, 2]  # Diminue quand x augmente  
correlation_neg = statistics.correlation(x, z)  
print(f"Corrélation négative : {correlation_neg}")  # -1.0  
```

### Exemple pratique : Relation entre température et ventes

```python
import statistics

def analyser_correlation_ventes(temperatures, ventes):
    """Analyse la corrélation entre température et ventes"""
    print("\n🌡️ Analyse température vs ventes")
    print("=" * 50)

    correlation = statistics.correlation(temperatures, ventes)
    print(f"Corrélation : {correlation:.3f}")

    if correlation > 0.7:
        print("→ Forte corrélation positive")
        print("  Les ventes augmentent avec la température")
    elif correlation > 0.3:
        print("→ Corrélation positive modérée")
    elif correlation > -0.3:
        print("→ Corrélation faible ou nulle")
    elif correlation > -0.7:
        print("→ Corrélation négative modérée")
    else:
        print("→ Forte corrélation négative")
        print("  Les ventes diminuent avec la température")

    # Statistiques descriptives
    print(f"\nTempérature moyenne : {statistics.mean(temperatures):.1f}°C")
    print(f"Ventes moyennes : {statistics.mean(ventes):.0f} unités")

# Exemple : Ventes de glaces en fonction de la température
temperatures = [15, 18, 22, 25, 28, 30, 32, 35, 38, 40]  
ventes_glaces = [50, 65, 85, 110, 140, 160, 180, 210, 250, 280]  

analyser_correlation_ventes(temperatures, ventes_glaces)
```

---

## Exemple complet : Simulateur de casino

Combinons les trois modules pour créer un simulateur de casino complet.

```python
import random  
import statistics  
import math  

class Casino:
    """Simulateur de jeux de casino"""

    def __init__(self, capital_initial=1000):
        self.capital = capital_initial
        self.historique = [capital_initial]

    def roulette(self, mise, choix):
        """Jeu de roulette

        choix: 'rouge', 'noir', 'pair', 'impair', ou un numéro (0-36)
        """
        if mise > self.capital:
            return "Mise trop élevée!"

        numero = random.randint(0, 36)
        est_rouge = numero in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        est_noir = numero != 0 and not est_rouge

        gain = 0

        if isinstance(choix, int) and choix == numero:
            gain = mise * 35  # Pari sur un numéro
        elif choix == "rouge" and est_rouge:
            gain = mise
        elif choix == "noir" and est_noir:
            gain = mise
        elif choix == "pair" and numero % 2 == 0 and numero != 0:
            gain = mise
        elif choix == "impair" and numero % 2 == 1:
            gain = mise
        else:
            gain = -mise

        self.capital += gain
        self.historique.append(self.capital)

        return {
            'numero': numero,
            'couleur': 'vert' if numero == 0 else ('rouge' if est_rouge else 'noir'),
            'gain': gain,
            'capital': self.capital
        }

    def blackjack_simplifie(self, mise):
        """Version simplifiée du blackjack"""
        if mise > self.capital:
            return "Mise trop élevée!"

        # Tirer deux cartes pour le joueur et le croupier
        main_joueur = random.randint(15, 21)
        main_croupier = random.randint(15, 21)

        gain = 0
        if main_joueur > 21:
            gain = -mise
            resultat = "Perdu (dépassement)"
        elif main_croupier > 21:
            gain = mise
            resultat = "Gagné (croupier dépasse)"
        elif main_joueur > main_croupier:
            gain = mise
            resultat = "Gagné"
        elif main_joueur < main_croupier:
            gain = -mise
            resultat = "Perdu"
        else:
            gain = 0
            resultat = "Égalité"

        self.capital += gain
        self.historique.append(self.capital)

        return {
            'main_joueur': main_joueur,
            'main_croupier': main_croupier,
            'resultat': resultat,
            'gain': gain,
            'capital': self.capital
        }

    def statistiques(self):
        """Affiche les statistiques de jeu"""
        print("\n📊 Statistiques de jeu")
        print("=" * 50)
        print(f"Capital initial : {self.historique[0]:.2f}€")
        print(f"Capital actuel : {self.capital:.2f}€")

        benefice = self.capital - self.historique[0]
        print(f"Bénéfice/Perte : {benefice:+.2f}€")

        if len(self.historique) > 1:
            print(f"\nNombre de parties : {len(self.historique) - 1}")
            print(f"Capital moyen : {statistics.mean(self.historique):.2f}€")
            print(f"Capital médian : {statistics.median(self.historique):.2f}€")
            print(f"Écart-type : {statistics.stdev(self.historique):.2f}€")
            print(f"Capital max : {max(self.historique):.2f}€")
            print(f"Capital min : {min(self.historique):.2f}€")

            # Calcul du rendement
            roi = ((self.capital - self.historique[0]) / self.historique[0]) * 100
            print(f"ROI : {roi:+.2f}%")

# Simulation
print("🎰 Bienvenue au Casino!")  
casino = Casino(capital_initial=1000)  

# Jouer quelques parties
print("\n--- Roulette ---")  
for i in range(5):  
    resultat = casino.roulette(50, "rouge")
    print(f"Partie {i+1}: Numéro {resultat['numero']} ({resultat['couleur']}) - "
          f"Gain: {resultat['gain']:+}€ - Capital: {resultat['capital']:.0f}€")

print("\n--- Blackjack ---")  
for i in range(5):  
    resultat = casino.blackjack_simplifie(50)
    print(f"Partie {i+1}: {resultat['resultat']} ({resultat['main_joueur']} vs "
          f"{resultat['main_croupier']}) - Gain: {resultat['gain']:+}€ - "
          f"Capital: {resultat['capital']:.0f}€")

# Afficher les statistiques
casino.statistiques()
```

---

## Exemple pratique : Simulation de Monte Carlo

La méthode de Monte Carlo utilise l'aléatoire pour résoudre des problèmes mathématiques.

```python
import random  
import math  

def estimer_pi(nombre_points=10000):
    """Estime la valeur de π avec la méthode de Monte Carlo

    Principe : On jette des points aléatoires dans un carré.
    Le ratio de points dans le cercle inscrit vs total
    est proportionnel à π/4.
    """
    points_dans_cercle = 0

    for _ in range(nombre_points):
        # Point aléatoire entre -1 et 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Distance du centre
        distance = math.sqrt(x**2 + y**2)

        # Le point est-il dans le cercle de rayon 1 ?
        if distance <= 1:
            points_dans_cercle += 1

    # Estimation de π
    pi_estime = 4 * (points_dans_cercle / nombre_points)
    return pi_estime

print("🎯 Estimation de π avec Monte Carlo")  
print("=" * 50)  

for n in [100, 1000, 10000, 100000, 1000000]:
    pi_estime = estimer_pi(n)
    erreur = abs(pi_estime - math.pi)
    print(f"n = {n:7d} : π ≈ {pi_estime:.6f} (erreur: {erreur:.6f})")

print(f"\nValeur réelle : π = {math.pi:.6f}")
```

---

## Bonnes pratiques

### 1. Choisir le bon module

```python
# ❌ Utiliser math pour l'aléatoire
import math
# math n'a pas de fonctions aléatoires

# ✅ Utiliser random pour l'aléatoire
import random  
nombre = random.randint(1, 10)  
```

### 2. Attention aux types de données

```python
import math  
import statistics  

# math travaille avec des floats
print(type(math.sqrt(4)))  # <class 'float'>

# statistics accepte ints et floats
donnees = [1, 2, 3, 4, 5]  
print(statistics.mean(donnees))  # 3 (peut être int ou float)  
```

### 3. Gérer les erreurs

```python
import math  
import statistics  

# Division par zéro
try:
    resultat = math.log(0)
except ValueError as e:
    print(f"Erreur : {e}")

# Liste vide
try:
    moyenne = statistics.mean([])
except statistics.StatisticsError as e:
    print(f"Erreur : {e}")
```

### 4. Utiliser seed pour la reproductibilité

```python
import random

# Pour les tests
random.seed(42)  
resultats_test = [random.randint(1, 100) for _ in range(10)]  

# Pour la production
random.seed()  # Réinitialise avec l'horloge système
```

### 5. Préférer statistics aux calculs manuels

```python
donnees = [1, 2, 3, 4, 5]

# ❌ Calcul manuel de la moyenne
moyenne = sum(donnees) / len(donnees)

# ✅ Utiliser statistics (plus robuste)
import statistics  
moyenne = statistics.mean(donnees)  
```

---

## Résumé

### Module math

| Catégorie | Fonctions principales |
|-----------|----------------------|
| **Constantes** | `pi`, `e`, `tau`, `inf`, `nan` |
| **Arrondis** | `ceil()`, `floor()`, `trunc()` |
| **Puissances** | `sqrt()`, `pow()`, `exp()`, `log()`, `log10()`, `log2()` |
| **Trigonométrie** | `sin()`, `cos()`, `tan()`, `radians()`, `degrees()` |
| **Autres** | `gcd()`, `lcm()`, `factorial()`, `comb()`, `perm()` |

### Module random

| Fonction | Usage |
|----------|-------|
| `random()` | Float entre 0 et 1 |
| `randint(a, b)` | Entier entre a et b |
| `uniform(a, b)` | Float entre a et b |
| `choice(seq)` | Élément aléatoire |
| `choices(seq, k=n)` | n éléments avec remise |
| `sample(seq, k=n)` | n éléments sans remise |
| `shuffle(list)` | Mélanger une liste |
| `seed(x)` | Définir la graine |

### Module statistics

| Fonction | Description |
|----------|-------------|
| `mean()` | Moyenne arithmétique |
| `median()` | Valeur médiane |
| `mode()` | Valeur la plus fréquente |
| `stdev()` | Écart-type d'échantillon |
| `variance()` | Variance d'échantillon |
| `quantiles()` | Quantiles/percentiles |
| `correlation()` | Corrélation de Pearson |

### Exemples d'utilisation

```python
import math  
import random  
import statistics  

# Calculs mathématiques
aire_cercle = math.pi * (5 ** 2)  
racine = math.sqrt(16)  

# Génération aléatoire
nombre = random.randint(1, 100)  
choix = random.choice(['A', 'B', 'C'])  

# Statistiques
donnees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
moyenne = statistics.mean(donnees)  
mediane = statistics.median(donnees)  
ecart_type = statistics.stdev(donnees)  
```

Ces trois modules sont des outils puissants pour effectuer des calculs mathématiques, générer de l'aléatoire et analyser des données en Python !

⏭️ [itertools et functools](/07-bibliotheques-standard/04-itertools-et-functools.md)
