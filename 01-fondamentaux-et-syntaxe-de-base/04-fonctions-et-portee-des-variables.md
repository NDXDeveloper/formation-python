🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 1.4 : Fonctions et portée des variables

## Introduction

Les fonctions sont des **blocs de code réutilisables** qui accomplissent une tâche spécifique. Imaginez-les comme des "mini-programmes" à l'intérieur de votre programme principal. Elles permettent d'organiser votre code, d'éviter la répétition et de le rendre plus lisible et maintenable.

## Pourquoi utiliser des fonctions ?

### Avantages des fonctions

1. **Réutilisabilité** : Écrivez une fois, utilisez plusieurs fois
2. **Organisation** : Diviser un problème complexe en petites parties
3. **Lisibilité** : Code plus facile à comprendre et à déboguer
4. **Maintenance** : Modifications centralisées
5. **Testabilité** : Chaque fonction peut être testée indépendamment

### Exemple sans fonctions (problématique)

```python
# ❌ Code répétitif et difficile à maintenir
nom1 = "Alice"
age1 = 25
print(f"Bonjour {nom1}!")
print(f"Vous avez {age1} ans.")
if age1 >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
print("Bienvenue!\n")

nom2 = "Bob"
age2 = 16
print(f"Bonjour {nom2}!")
print(f"Vous avez {age2} ans.")
if age2 >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
print("Bienvenue!\n")

# Et encore d'autres personnes...
```

### Exemple avec fonctions (solution)

```python
# ✅ Code organisé et réutilisable
def accueillir_personne(nom, age):
    """Fonction qui accueille une personne."""
    print(f"Bonjour {nom}!")
    print(f"Vous avez {age} ans.")
    if age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")
    print("Bienvenue!\n")

# Utilisation de la fonction
accueillir_personne("Alice", 25)
accueillir_personne("Bob", 16)
accueillir_personne("Charlie", 30)
```

## Définition et syntaxe des fonctions

### Syntaxe de base

```python
def nom_de_la_fonction(parametre1, parametre2):
    """Documentation de la fonction (optionnel mais recommandé)"""
    # Corps de la fonction
    # Instructions à exécuter
    return valeur_de_retour  # Optionnel
```

### Votre première fonction

```python
def dire_bonjour():
    """Fonction simple qui dit bonjour."""
    print("Bonjour tout le monde!")
    print("Comment allez-vous?")

# Appel de la fonction
dire_bonjour()
```

**Sortie :**
```
Bonjour tout le monde!
Comment allez-vous?
```

## Paramètres et arguments

### Fonction avec paramètres

```python
def saluer(nom):
    """Salue une personne par son nom."""
    print(f"Bonjour {nom}!")
    print("Ravi de vous rencontrer!")

# Appels avec différents arguments
saluer("Alice")
saluer("Bob")
saluer("Charlie")
```

### Fonction avec plusieurs paramètres

```python
def presenter(nom, age, ville):
    """Présente une personne avec ses informations."""
    print(f"Je m'appelle {nom}")
    print(f"J'ai {age} ans")
    print(f"J'habite à {ville}")
    print("-" * 30)

# Appel avec arguments positionnels
presenter("Alice", 25, "Paris")
presenter("Bob", 30, "Lyon")
```

### Paramètres par défaut

```python
def saluer_avec_titre(nom, titre="Monsieur/Madame"):
    """Salue une personne avec un titre."""
    print(f"Bonjour {titre} {nom}!")

# Appels avec et sans titre
saluer_avec_titre("Dupont")                    # Utilise le titre par défaut
saluer_avec_titre("Martin", "Docteur")         # Utilise le titre spécifié
saluer_avec_titre("Durand", "Professeur")
```

### Arguments nommés (keyword arguments)

```python
def calculer_prix(prix_ht, tva=0.20, remise=0.0):
    """Calcule le prix TTC avec TVA et remise."""
    prix_avec_tva = prix_ht * (1 + tva)
    prix_final = prix_avec_tva * (1 - remise)
    return prix_final

# Différentes façons d'appeler la fonction
prix1 = calculer_prix(100)                           # Prix de base
prix2 = calculer_prix(100, tva=0.10)                 # TVA réduite
prix3 = calculer_prix(100, remise=0.15)              # Avec remise
prix4 = calculer_prix(100, tva=0.055, remise=0.10)   # TVA et remise
prix5 = calculer_prix(remise=0.20, prix_ht=100, tva=0.196)  # Ordre libre

print(f"Prix 1: {prix1:.2f}€")
print(f"Prix 2: {prix2:.2f}€")
print(f"Prix 3: {prix3:.2f}€")
print(f"Prix 4: {prix4:.2f}€")
print(f"Prix 5: {prix5:.2f}€")
```

## Valeurs de retour

### Fonction avec return

```python
def addition(a, b):
    """Additionne deux nombres et retourne le résultat."""
    resultat = a + b
    return resultat

# Utilisation du résultat
somme = addition(5, 3)
print(f"5 + 3 = {somme}")

# Utilisation directe
print(f"10 + 7 = {addition(10, 7)}")
```

### Fonction sans return

```python
def afficher_info(nom, age):
    """Affiche les informations (ne retourne rien)."""
    print(f"Nom: {nom}")
    print(f"Âge: {age}")

# Cette fonction ne retourne rien (None)
resultat = afficher_info("Alice", 25)
print(f"Résultat: {resultat}")  # None
```

### Retour de plusieurs valeurs

```python
def analyser_nombre(nombre):
    """Analyse un nombre et retourne plusieurs informations."""
    est_pair = nombre % 2 == 0
    est_positif = nombre > 0
    carre = nombre ** 2
    return est_pair, est_positif, carre

# Récupération des résultats
pair, positif, carre = analyser_nombre(5)
print(f"5 est pair: {pair}")
print(f"5 est positif: {positif}")
print(f"5 au carré: {carre}")

# Ou récupération en tuple
infos = analyser_nombre(-4)
print(f"Infos sur -4: {infos}")  # (True, False, 16)
```

### Return conditionnel

```python
def categoriser_age(age):
    """Catégorise une personne selon son âge."""
    if age < 0:
        return "Âge invalide"
    elif age < 2:
        return "Bébé"
    elif age < 13:
        return "Enfant"
    elif age < 18:
        return "Adolescent"
    elif age < 65:
        return "Adulte"
    else:
        return "Senior"

# Tests
ages = [1, 10, 16, 25, 70, -5]
for age in ages:
    categorie = categoriser_age(age)
    print(f"Âge {age}: {categorie}")
```

## Portée des variables (Scope)

### Variables locales vs globales

```python
# Variable globale
compteur_global = 0

def incrementer():
    """Fonction qui utilise une variable locale."""
    # Variable locale
    compteur_local = 10
    compteur_local += 1
    print(f"Compteur local: {compteur_local}")

def afficher_global():
    """Fonction qui lit une variable globale."""
    print(f"Compteur global: {compteur_global}")

# Tests
incrementer()
afficher_global()
# print(compteur_local)  # ❌ Erreur ! Variable locale non accessible
```

### Modification de variables globales

```python
score = 0  # Variable globale

def augmenter_score():
    """Augmente le score (ne fonctionne pas sans global)."""
    # score = score + 10  # ❌ Erreur ! Référence avant assignation
    print(f"Score actuel: {score}")  # ✅ Lecture OK

def augmenter_score_correct():
    """Augmente le score correctement."""
    global score  # Déclare qu'on utilise la variable globale
    score += 10
    print(f"Nouveau score: {score}")

# Tests
augmenter_score()
augmenter_score_correct()
augmenter_score_correct()
```

### Exemple pratique de portée

```python
nom = "Alice"  # Variable globale

def modifier_nom_local():
    """Modifie le nom localement."""
    nom = "Bob"  # Variable locale (masque la globale)
    print(f"Nom dans la fonction: {nom}")

def modifier_nom_global():
    """Modifie le nom globalement."""
    global nom
    nom = "Charlie"
    print(f"Nom global modifié: {nom}")

# Tests
print(f"Nom initial: {nom}")
modifier_nom_local()
print(f"Nom après fonction locale: {nom}")
modifier_nom_global()
print(f"Nom après fonction globale: {nom}")
```

## Fonctions avancées

### Fonctions avec nombre variable d'arguments

```python
def additionner_tous(*nombres):
    """Additionne tous les nombres passés en arguments."""
    total = 0
    for nombre in nombres:
        total += nombre
    return total

# Appels avec différents nombres d'arguments
print(additionner_tous(1, 2, 3))           # 6
print(additionner_tous(10, 20, 30, 40))    # 100
print(additionner_tous(5))                 # 5
print(additionner_tous())                  # 0
```

### Fonctions avec arguments nommés variables

```python
def creer_profil(nom, **infos):
    """Crée un profil avec des informations variables."""
    print(f"Profil de {nom}:")
    for cle, valeur in infos.items():
        print(f"  {cle}: {valeur}")
    print("-" * 30)

# Appels avec différentes informations
creer_profil("Alice", age=25, ville="Paris", profession="Ingénieur")
creer_profil("Bob", age=30, pays="France", hobby="Lecture")
creer_profil("Charlie", telephone="0123456789", email="charlie@email.com")
```

### Fonctions avec tous types d'arguments

```python
def fonction_complete(requis, par_defaut="valeur", *args, **kwargs):
    """Fonction démonstrative avec tous types d'arguments."""
    print(f"Argument requis: {requis}")
    print(f"Argument par défaut: {par_defaut}")
    print(f"Arguments positionnels supplémentaires: {args}")
    print(f"Arguments nommés: {kwargs}")
    print("-" * 40)

# Différents appels
fonction_complete("obligatoire")
fonction_complete("obligatoire", "personnalisé")
fonction_complete("obligatoire", "personnalisé", 1, 2, 3)
fonction_complete("obligatoire", nom="Alice", age=25)
fonction_complete("obligatoire", "personnalisé", 1, 2, 3, nom="Bob", age=30)
```

## Fonctions en tant qu'objets

### Assigner une fonction à une variable

```python
def calculer_carre(x):
    """Calcule le carré d'un nombre."""
    return x ** 2

def calculer_cube(x):
    """Calcule le cube d'un nombre."""
    return x ** 3

# Assigner des fonctions à des variables
operation = calculer_carre
print(f"Carré de 5: {operation(5)}")  # 25

operation = calculer_cube
print(f"Cube de 5: {operation(5)}")   # 125
```

### Passer une fonction comme argument

```python
def appliquer_operation(nombre, operation):
    """Applique une opération à un nombre."""
    return operation(nombre)

def doubler(x):
    return x * 2

def tripler(x):
    return x * 3

# Utilisation
resultat1 = appliquer_operation(10, doubler)
resultat2 = appliquer_operation(10, tripler)
print(f"10 doublé: {resultat1}")  # 20
print(f"10 triplé: {resultat2}")  # 30
```

## Fonctions récursives

### Principe de la récursion

```python
def compte_a_rebours(n):
    """Compte à rebours de n à 1."""
    print(n)
    if n > 1:
        compte_a_rebours(n - 1)  # Appel récursif
    else:
        print("Décollage! 🚀")

# Test
compte_a_rebours(5)
```

### Calcul de factorielle

```python
def factorielle(n):
    """Calcule la factorielle de n."""
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)

# Tests
for i in range(1, 6):
    print(f"{i}! = {factorielle(i)}")
```

## Exemples pratiques

### Calculatrice modulaire

```python
def addition(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait b de a."""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres."""
    return a * b

def division(a, b):
    """Divise a par b."""
    if b != 0:
        return a / b
    else:
        return "Division par zéro impossible"

def calculatrice():
    """Calculatrice interactive."""
    operations = {
        '+': addition,
        '-': soustraction,
        '*': multiplication,
        '/': division
    }

    while True:
        print("\n=== CALCULATRICE ===")
        print("Opérations: +, -, *, /")
        print("Tapez 'quit' pour quitter")

        try:
            a = input("Premier nombre (ou 'quit'): ")
            if a.lower() == 'quit':
                break
            a = float(a)

            op = input("Opération (+, -, *, /): ")
            if op not in operations:
                print("Opération invalide!")
                continue

            b = float(input("Second nombre: "))

            resultat = operations[op](a, b)
            print(f"{a} {op} {b} = {resultat}")

        except ValueError:
            print("Veuillez entrer des nombres valides")
        except Exception as e:
            print(f"Erreur: {e}")

# Lancement de la calculatrice
# calculatrice()
```

### Système de gestion d'utilisateurs

```python
def creer_utilisateur(nom, email, age):
    """Crée un nouvel utilisateur."""
    utilisateur = {
        'nom': nom,
        'email': email,
        'age': age,
        'actif': True
    }
    return utilisateur

def afficher_utilisateur(utilisateur):
    """Affiche les informations d'un utilisateur."""
    statut = "Actif" if utilisateur['actif'] else "Inactif"
    print(f"Nom: {utilisateur['nom']}")
    print(f"Email: {utilisateur['email']}")
    print(f"Âge: {utilisateur['age']} ans")
    print(f"Statut: {statut}")
    print("-" * 30)

def modifier_utilisateur(utilisateur, **modifications):
    """Modifie les informations d'un utilisateur."""
    for cle, valeur in modifications.items():
        if cle in utilisateur:
            utilisateur[cle] = valeur
        else:
            print(f"Champ '{cle}' inexistant")

def est_majeur(utilisateur):
    """Vérifie si l'utilisateur est majeur."""
    return utilisateur['age'] >= 18

def calculer_age_dans_x_ans(utilisateur, x):
    """Calcule l'âge de l'utilisateur dans x années."""
    return utilisateur['age'] + x

# Utilisation du système
print("=== SYSTÈME DE GESTION D'UTILISATEURS ===")

# Création d'utilisateurs
alice = creer_utilisateur("Alice Dupont", "alice@email.com", 25)
bob = creer_utilisateur("Bob Martin", "bob@email.com", 17)

# Affichage
afficher_utilisateur(alice)
afficher_utilisateur(bob)

# Vérifications
print(f"Alice est majeure: {est_majeur(alice)}")
print(f"Bob est majeur: {est_majeur(bob)}")

# Calculs
print(f"Alice aura {calculer_age_dans_x_ans(alice, 10)} ans dans 10 ans")

# Modifications
modifier_utilisateur(alice, age=26, email="alice.dupont@email.com")
print("\nAprès modification:")
afficher_utilisateur(alice)
```

### Jeu de devine le nombre modulaire

```python
import random

def generer_nombre_secret(min_val=1, max_val=100):
    """Génère un nombre aléatoire secret."""
    return random.randint(min_val, max_val)

def obtenir_proposition():
    """Demande une proposition à l'utilisateur."""
    while True:
        try:
            return int(input("Votre proposition: "))
        except ValueError:
            print("Veuillez entrer un nombre entier")

def evaluer_proposition(proposition, secret):
    """Évalue la proposition et retourne un indice."""
    if proposition == secret:
        return "trouvé"
    elif proposition < secret:
        return "plus grand"
    else:
        return "plus petit"

def jouer_partie():
    """Joue une partie complète."""
    print("\n=== NOUVELLE PARTIE ===")
    min_val, max_val = 1, 100
    secret = generer_nombre_secret(min_val, max_val)
    tentatives = 0
    max_tentatives = 7

    print(f"Devinez le nombre entre {min_val} et {max_val}!")
    print(f"Vous avez {max_tentatives} tentatives.")

    while tentatives < max_tentatives:
        tentatives += 1
        print(f"\nTentative {tentatives}/{max_tentatives}")

        proposition = obtenir_proposition()
        resultat = evaluer_proposition(proposition, secret)

        if resultat == "trouvé":
            print(f"🎉 Bravo! Vous avez trouvé en {tentatives} tentatives!")
            return True
        else:
            print(f"C'est {resultat}!")

    print(f"😞 Perdu! Le nombre était {secret}")
    return False

def demander_rejouer():
    """Demande si l'utilisateur veut rejouer."""
    while True:
        choix = input("\nVoulez-vous rejouer? (oui/non): ").lower()
        if choix in ['oui', 'o', 'yes', 'y']:
            return True
        elif choix in ['non', 'n', 'no']:
            return False
        else:
            print("Répondez par 'oui' ou 'non'")

def jeu_complet():
    """Jeu complet avec gestion des parties multiples."""
    print("🎮 BIENVENUE AU JEU DE DEVINETTE!")

    parties_jouees = 0
    parties_gagnees = 0

    while True:
        gagne = jouer_partie()
        parties_jouees += 1

        if gagne:
            parties_gagnees += 1

        if not demander_rejouer():
            break

    # Statistiques finales
    print(f"\n📊 STATISTIQUES FINALES:")
    print(f"Parties jouées: {parties_jouees}")
    print(f"Parties gagnées: {parties_gagnees}")
    if parties_jouees > 0:
        pourcentage = (parties_gagnees / parties_jouees) * 100
        print(f"Pourcentage de réussite: {pourcentage:.1f}%")

    print("Merci d'avoir joué! 👋")

# Lancement du jeu
# jeu_complet()
```

## Exercices pratiques

### Exercice 1 : Fonctions mathématiques de base

```python
# Créez les fonctions suivantes:
# 1. aire_rectangle(longueur, largeur) -> retourne l'aire
# 2. aire_cercle(rayon) -> retourne l'aire (π = 3.14159)
# 3. est_pair(nombre) -> retourne True si pair, False sinon
# 4. plus_grand(a, b, c) -> retourne le plus grand des trois nombres
# 5. moyenne(liste_notes) -> retourne la moyenne d'une liste de notes

# Testez chaque fonction avec des exemples
```

### Exercice 2 : Convertisseur d'unités

```python
# Créez un convertisseur avec les fonctions:
# 1. celsius_vers_fahrenheit(celsius)
# 2. fahrenheit_vers_celsius(fahrenheit)
# 3. metres_vers_pieds(metres)
# 4. pieds_vers_metres(pieds)
# 5. km_vers_miles(km)
# 6. miles_vers_km(miles)

# Créez un menu interactif pour utiliser ces fonctions
```

### Exercice 3 : Gestionnaire de mots de passe

```python
# Créez les fonctions suivantes:
# 1. generer_mot_de_passe(longueur) -> génère un mot de passe aléatoire
# 2. verifier_force(mot_de_passe) -> évalue la force du mot de passe
# 3. contient_majuscule(texte) -> vérifie la présence de majuscules
# 4. contient_chiffre(texte) -> vérifie la présence de chiffres
# 5. contient_caractere_special(texte) -> vérifie les caractères spéciaux

# Créez un programme principal qui utilise toutes ces fonctions
```

### Exercice 4 : Système de notes

```python
# Créez un système de gestion de notes avec:
# 1. ajouter_note(liste_notes, note) -> ajoute une note à la liste
# 2. calculer_moyenne(liste_notes) -> calcule la moyenne
# 3. obtenir_mention(moyenne) -> retourne la mention selon la moyenne
# 4. nombre_notes_superieures(liste_notes, seuil) -> compte les notes > seuil
# 5. afficher_statistiques(liste_notes) -> affiche toutes les statistiques

# Créez un programme principal avec menu interactif
```

### Exercice 5 : Jeu de Pierre-Papier-Ciseaux

```python
# Créez un jeu complet avec:
# 1. obtenir_choix_joueur() -> demande le choix du joueur
# 2. obtenir_choix_ordinateur() -> génère le choix de l'ordinateur
# 3. determiner_gagnant(choix1, choix2) -> détermine le gagnant
# 4. afficher_resultat(choix_joueur, choix_ordi, gagnant) -> affiche le résultat
# 5. jouer_partie() -> gère une partie complète
# 6. afficher_scores(victoires, defaites, egalites) -> affiche les scores

# Créez un programme principal avec parties multiples
```

## Bonnes pratiques

### Nommage des fonctions

```python
# ✅ Bons noms : verbes décrivant l'action
def calculer_moyenne(notes):
    pass

def afficher_resultats(donnees):
    pass

def verifier_mot_de_passe(mot_de_passe):
    pass

# ❌ Mauvais noms : peu descriptifs
def calc(x):
    pass

def func1(data):
    pass

def check(p):
    pass
```

### Documentation des fonctions

```python
def calculer_prix_ttc(prix_ht, taux_tva=0.20):
    """
    Calcule le prix TTC à partir du prix HT.

    Args:
        prix_ht (float): Prix hors taxes
        taux_tva (float): Taux de TVA (par défaut 20%)

    Returns:
        float: Prix TTC

    Example:
        >>> calculer_prix_ttc(100, 0.20)
        120.0
    """
    return prix_ht * (1 + taux_tva)
```

### Fonctions courtes et spécialisées

```python
# ✅ Bon : fonctions courtes et spécialisées
def est_email_valide(email):
    """Vérifie si l'email est valide."""
    return '@' in email and '.' in email

def nettoyer_texte(texte):
    """Nettoie un texte en supprimant les espaces."""
    return texte.strip().lower()

def calculer_age(annee_naissance):
    """Calcule l'âge à partir de l'année de naissance."""
    return 2024 - annee_naissance

# ❌ Mauvais : fonction qui fait trop de choses
def traiter_utilisateur(nom, email, annee_naissance):
    """Fonction qui fait trop de choses."""
    # Nettoyer le nom
    nom = nom.strip().lower()
    # Vérifier l'email
    if '@' not in email:
        return None
    # Calculer l'âge
    age = 2024 - annee_naissance
    # Créer le profil
    profil = {'nom': nom, 'email': email, 'age': age}
    # Afficher le profil
    print(f"Profil créé: {profil}")
    return profil
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ **Définition de fonctions** : Syntaxe `def` et structure
✅ **Paramètres et arguments** : Positionnels, nommés, par défaut
✅ **Valeurs de retour** : `return` simple et multiple
✅ **Portée des variables** : Locales vs globales, mot-clé `global`
✅ **Fonctions avancées** : `*args`, `**kwargs`, récursion
✅ **Fonctions comme objets** : Assignation, passage en paramètre
✅ **Bonnes pratiques** : Nommage, documentation, spécialisation

**Concepts clés à retenir :**
- Les fonctions permettent de réutiliser du code et de l'organiser
- Les paramètres permettent de personnaliser le comportement
- `return` permet de renvoyer des résultats
- La portée détermine où une variable est accessible
- Une fonction doit faire une seule chose, mais la faire bien
- Toujours documenter vos fonctions

**Prochaine étape** : Dans la section 1.5, nous découvrirons la gestion des erreurs avec try/except pour créer des programmes robustes !

---

💡 **Conseil** : Les fonctions sont la clé d'un code bien organisé. Pratiquez en décomposant vos programmes en petites fonctions spécialisées !

⏭️
