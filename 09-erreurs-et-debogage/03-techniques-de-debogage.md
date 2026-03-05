🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 9.3 Techniques de débogage

## Introduction

Le débogage est une compétence essentielle pour tout développeur Python. Il s'agit du processus qui consiste à identifier, analyser et corriger les erreurs (bugs) dans votre code. Même les programmeurs expérimentés passent une partie importante de leur temps à déboguer. Heureusement, Python offre de nombreux outils et techniques pour faciliter ce processus.

Dans ce chapitre, nous allons explorer les différentes méthodes de débogage, des plus simples aux plus avancées, toutes adaptées aux débutants.

---

## 1. La méthode print() - Le débogage de base

### Pourquoi commencer par print() ?

La fonction `print()` est souvent la première technique de débogage que tout débutant apprend. Elle est simple, intuitive et ne nécessite aucun outil spécial.

### Comment utiliser print() efficacement

```python
def calculer_moyenne(notes):
    total = 0
    for note in notes:
        print(f"Note actuelle : {note}")  # Voir chaque valeur
        total += note
    print(f"Total : {total}")  # Vérifier le total
    moyenne = total / len(notes)
    print(f"Moyenne calculée : {moyenne}")  # Résultat final
    return moyenne

notes = [15, 18, 12, 16]  
resultat = calculer_moyenne(notes)  
```

### Techniques avancées avec print()

**Afficher le type d'une variable :**
```python
valeur = "123"  
print(f"Valeur : {valeur}, Type : {type(valeur)}")  
# Sortie : Valeur : 123, Type : <class 'str'>
```

**Afficher plusieurs variables en même temps :**
```python
nom = "Alice"  
age = 25  
ville = "Paris"  
print(f"Nom: {nom}, Age: {age}, Ville: {ville}")  
```

**Utiliser des séparateurs visuels :**
```python
print("="*50)  
print("DÉBUT DU DÉBOGAGE")  
print("="*50)  
# Votre code ici
print("="*50)  
print("FIN DU DÉBOGAGE")  
print("="*50)  
```

### Limites de la méthode print()

Bien que simple et efficace, `print()` présente quelques inconvénients :
- Il faut ajouter et retirer manuellement les instructions print
- Le code devient rapidement encombré
- Difficile à utiliser pour des bugs complexes
- Ralentit l'exécution du programme

---

## 2. L'instruction assert - Vérifications automatiques

### Qu'est-ce qu'une assertion ?

Une assertion est une vérification que vous placez dans votre code pour vous assurer qu'une condition est toujours vraie. Si la condition est fausse, Python lève une exception `AssertionError`.

### Syntaxe de base

```python
assert condition, "Message d'erreur optionnel"
```

### Exemples pratiques

**Vérifier qu'une valeur est positive :**
```python
def calculer_racine_carree(nombre):
    assert nombre >= 0, "Le nombre doit être positif"
    return nombre ** 0.5

# Fonctionne correctement
print(calculer_racine_carree(16))  # 4.0

# Déclenche une AssertionError
print(calculer_racine_carree(-5))
# AssertionError: Le nombre doit être positif
```

**Vérifier le type d'une variable :**
```python
def concatener_textes(texte1, texte2):
    assert isinstance(texte1, str), "texte1 doit être une chaîne"
    assert isinstance(texte2, str), "texte2 doit être une chaîne"
    return texte1 + " " + texte2

resultat = concatener_textes("Bonjour", "monde")  # Fonctionne  
resultat = concatener_textes("Bonjour", 123)  # AssertionError  
```

**Vérifier qu'une liste n'est pas vide :**
```python
def obtenir_premier_element(liste):
    assert len(liste) > 0, "La liste ne peut pas être vide"
    return liste[0]

ma_liste = [1, 2, 3]  
print(obtenir_premier_element(ma_liste))  # 1  

liste_vide = []  
print(obtenir_premier_element(liste_vide))  # AssertionError  
```

### Quand utiliser les assertions

Les assertions sont idéales pour :
- Vérifier les conditions qui ne devraient jamais être fausses
- Documenter les hypothèses de votre code
- Détecter les erreurs de programmation pendant le développement

⚠️ **Important :** Les assertions peuvent être désactivées en Python avec l'option `-O`. Ne les utilisez donc pas pour valider des données utilisateur en production.

---

## 3. Le module logging - Traçage professionnel

### Pourquoi utiliser logging plutôt que print() ?

Le module `logging` offre plusieurs avantages :
- Différents niveaux de sévérité (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Possibilité d'enregistrer dans des fichiers
- Activation/désactivation facile
- Format personnalisable
- Horodatage automatique

### Configuration de base

```python
import logging

# Configuration simple
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Utilisation
logging.debug("Message de débogage détaillé")  
logging.info("Information générale")  
logging.warning("Attention, quelque chose d'inhabituel")  
logging.error("Une erreur s'est produite")  
logging.critical("Erreur critique, le programme doit s'arrêter")  
```

**Sortie :**
```
2025-11-02 14:30:15 - DEBUG - Message de débogage détaillé
2025-11-02 14:30:15 - INFO - Information générale
2025-11-02 14:30:15 - WARNING - Attention, quelque chose d'inhabituel
2025-11-02 14:30:15 - ERROR - Une erreur s'est produite
2025-11-02 14:30:15 - CRITICAL - Erreur critique, le programme doit s'arrêter
```

### Les niveaux de logging

| Niveau | Valeur numérique | Utilisation |
|--------|------------------|-------------|
| DEBUG | 10 | Informations détaillées pour diagnostiquer un problème |
| INFO | 20 | Confirmation que les choses fonctionnent comme prévu |
| WARNING | 30 | Indication qu'il s'est passé quelque chose d'inattendu |
| ERROR | 40 | Erreur, mais le programme peut continuer |
| CRITICAL | 50 | Erreur grave, le programme risque de s'arrêter |

### Exemple pratique avec une fonction

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def diviser(a, b):
    logging.debug(f"Tentative de division : {a} / {b}")

    if b == 0:
        logging.error("Division par zéro impossible")
        return None

    resultat = a / b
    logging.info(f"Division réussie : {a} / {b} = {resultat}")
    return resultat

# Test
print(diviser(10, 2))  
print(diviser(10, 0))  
```

### Enregistrer les logs dans un fichier

```python
import logging

# Configuration pour écrire dans un fichier
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='mon_application.log',
    filemode='w'  # 'w' = écrase, 'a' = ajoute à la fin
)

def traiter_donnees(donnees):
    logging.info("Début du traitement")
    try:
        # Votre code ici
        resultat = sum(donnees) / len(donnees)
        logging.info(f"Traitement réussi : moyenne = {resultat}")
        return resultat
    except Exception as e:
        logging.error(f"Erreur lors du traitement : {e}")
        raise

traiter_donnees([10, 20, 30, 40])
```

---

## 4. Le débogueur Python (pdb) - L'outil puissant

### Introduction à pdb

`pdb` (Python Debugger) est le débogueur intégré de Python. Il permet d'exécuter votre code ligne par ligne, d'inspecter les variables et de comprendre exactement ce qui se passe.

### Démarrer pdb

**Méthode 1 : Point d'arrêt dans le code**
```python
import pdb

def calculer_factorielle(n):
    resultat = 1
    pdb.set_trace()  # Le programme s'arrêtera ici
    for i in range(1, n + 1):
        resultat *= i
    return resultat

calculer_factorielle(5)
```

**Méthode 2 : Avec breakpoint() (recommandé)**
```python
def calculer_factorielle(n):
    resultat = 1
    breakpoint()  # Plus moderne et recommandé
    for i in range(1, n + 1):
        resultat *= i
    return resultat

calculer_factorielle(5)
```

### Commandes essentielles de pdb

| Commande | Raccourci | Description |
|----------|-----------|-------------|
| `help` | `h` | Affiche l'aide |
| `next` | `n` | Exécute la ligne suivante |
| `step` | `s` | Entre dans une fonction |
| `continue` | `c` | Continue jusqu'au prochain breakpoint |
| `list` | `l` | Affiche le code autour de la ligne actuelle |
| `print variable` | `p variable` | Affiche la valeur d'une variable |
| `quit` | `q` | Quitte le débogueur |
| `where` | `w` | Affiche la pile d'exécution |

### Exemple d'utilisation pratique

```python
def calculer_prix_total(prix_unitaire, quantite, taux_tva):
    breakpoint()  # Point d'arrêt

    prix_ht = prix_unitaire * quantite
    montant_tva = prix_ht * taux_tva
    prix_ttc = prix_ht + montant_tva

    return prix_ttc

resultat = calculer_prix_total(100, 3, 0.20)  
print(f"Prix total : {resultat}€")  
```

**Session de débogage typique :**
```
> /chemin/vers/fichier.py(5)calculer_prix_total()
-> prix_ht = prix_unitaire * quantite
(Pdb) p prix_unitaire
100
(Pdb) p quantite
3
(Pdb) n
> /chemin/vers/fichier.py(6)calculer_prix_total()
-> montant_tva = prix_ht * taux_tva
(Pdb) p prix_ht
300
(Pdb) n
> /chemin/vers/fichier.py(7)calculer_prix_total()
-> prix_ttc = prix_ht + montant_tva
(Pdb) p montant_tva
60.0
(Pdb) c
Prix total : 360.0€
```

### Inspecter les variables avec pdb

```python
def traiter_liste(nombres):
    total = 0
    breakpoint()

    for i, nombre in enumerate(nombres):
        total += nombre

    return total / len(nombres)

ma_liste = [10, 20, 30, 40, 50]  
moyenne = traiter_liste(ma_liste)  
```

**Dans pdb, vous pouvez taper :**
```
(Pdb) p nombres
[10, 20, 30, 40, 50]
(Pdb) p total
0
(Pdb) p len(nombres)
5
```

---

## 5. Techniques de débogage dans les IDE

### Visual Studio Code

**Configurer le débogage :**
1. Ouvrez votre fichier Python
2. Cliquez sur l'icône "Run and Debug" (ou F5)
3. Sélectionnez "Python File"

**Points d'arrêt (Breakpoints) :**
- Cliquez dans la marge gauche à côté d'une ligne de code
- Un point rouge apparaît pour indiquer un point d'arrêt
- Le programme s'arrêtera à cette ligne lors de l'exécution

**Fonctionnalités :**
- **Watch** : Surveiller des variables spécifiques
- **Call Stack** : Voir la pile des appels de fonctions
- **Variables** : Inspecter toutes les variables locales et globales
- **Step Over** (F10) : Exécuter la ligne suivante
- **Step Into** (F11) : Entrer dans une fonction
- **Step Out** (Shift+F11) : Sortir de la fonction actuelle

### PyCharm

PyCharm offre des outils de débogage très puissants :

**Démarrer le débogage :**
- Cliquez sur l'icône de bug (insecte) au lieu du bouton Run
- Ou utilisez le raccourci Shift+F9

**Fonctionnalités avancées :**
- **Conditional Breakpoints** : Points d'arrêt conditionnels
- **Evaluate Expression** : Évaluer des expressions Python à la volée
- **Show Execution Point** : Revenir à la ligne en cours d'exécution

### Jupyter Notebooks

Dans Jupyter, utilisez le magic command `%debug` :

```python
def fonction_avec_bug(x):
    resultat = x / 0  # Erreur intentionnelle
    return resultat

try:
    fonction_avec_bug(10)
except:
    %debug  # Lance pdb automatiquement après l'erreur
```

---

## 6. Techniques avancées pour débutants

### 6.1 Afficher la trace d'exécution

Le module `traceback` permet d'afficher des informations détaillées sur les erreurs :

```python
import traceback

def fonction_a():
    fonction_b()

def fonction_b():
    fonction_c()

def fonction_c():
    x = 1 / 0  # Erreur

try:
    fonction_a()
except Exception as e:
    print("Une erreur s'est produite !")
    traceback.print_exc()
```

**Sortie :**
```
Une erreur s'est produite !  
Traceback (most recent call last):  
  File "script.py", line 12, in <module>
    fonction_a()
  File "script.py", line 4, in fonction_a
    fonction_b()
  File "script.py", line 7, in fonction_b
    fonction_c()
  File "script.py", line 10, in fonction_c
    x = 1 / 0
ZeroDivisionError: division by zero
```

### 6.2 Le module pprint - Affichage élégant

Pour afficher joliment des structures de données complexes :

```python
from pprint import pprint

donnees_complexes = {
    'utilisateurs': [
        {'nom': 'Alice', 'age': 25, 'ville': 'Paris'},
        {'nom': 'Bob', 'age': 30, 'ville': 'Lyon'},
        {'nom': 'Charlie', 'age': 35, 'ville': 'Marseille'}
    ],
    'configuration': {
        'debug': True,
        'timeout': 30,
        'options': ['option1', 'option2', 'option3']
    }
}

# Affichage standard (difficile à lire)
print(donnees_complexes)

# Affichage avec pprint (beaucoup plus lisible)
pprint(donnees_complexes, indent=2, width=60)
```

### 6.3 Le décorateur de débogage

Créer un décorateur simple pour tracer l'exécution des fonctions :

```python
def debug_function(func):
    """Décorateur qui affiche les appels de fonction."""
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        print(f"  Arguments : {args}")
        print(f"  Arguments nommés : {kwargs}")
        resultat = func(*args, **kwargs)
        print(f"  Résultat : {resultat}")
        return resultat
    return wrapper

@debug_function
def addition(a, b):
    return a + b

@debug_function
def saluer(nom, message="Bonjour"):
    return f"{message} {nom}"

# Test
addition(5, 3)  
saluer("Alice", message="Salut")  
```

**Sortie :**
```
Appel de addition
  Arguments : (5, 3)
  Arguments nommés : {}
  Résultat : 8
Appel de saluer
  Arguments : ('Alice',)
  Arguments nommés : {'message': 'Salut'}
  Résultat : Salut Alice
```

### 6.4 Le module inspect - Introspection

Pour obtenir des informations sur votre code pendant l'exécution :

```python
import inspect

def ma_fonction(param1, param2):
    """Cette fonction fait quelque chose."""
    # Obtenir le nom de la fonction actuelle
    fonction_actuelle = inspect.currentframe().f_code.co_name
    print(f"Fonction actuelle : {fonction_actuelle}")

    # Obtenir la pile d'appels
    pile = inspect.stack()
    print(f"Appelé depuis : {pile[1].function}")

    # Obtenir les variables locales
    variables_locales = inspect.currentframe().f_locals
    print(f"Variables locales : {variables_locales}")

    return param1 + param2

def fonction_principale():
    resultat = ma_fonction(10, 20)
    return resultat

fonction_principale()
```

---

## 7. Stratégies et bonnes pratiques de débogage

### 7.1 La méthode de réduction du problème

Quand vous avez un bug, suivez cette approche :

1. **Reproduire le bug** : Assurez-vous de pouvoir reproduire le problème de manière fiable
2. **Isoler le code** : Créez un exemple minimal qui reproduit le bug
3. **Vérifier les hypothèses** : Utilisez print() ou assert pour vérifier vos suppositions
4. **Diviser pour régner** : Commentez des sections de code pour localiser le problème

```python
# Exemple d'isolation du problème
def programme_complexe():
    # Section 1
    donnees = charger_donnees()
    print("✓ Chargement des données OK")

    # Section 2
    donnees_traitees = traiter_donnees(donnees)
    print("✓ Traitement des données OK")

    # Section 3
    resultat = calculer_statistiques(donnees_traitees)
    print("✓ Calcul des statistiques OK")

    # Section 4
    sauvegarder_resultats(resultat)
    print("✓ Sauvegarde OK")
```

### 7.2 Le débogage "Rubber Duck"

Cette technique célèbre consiste à expliquer votre code ligne par ligne à un objet inanimé (traditionnellement un canard en plastique). Souvent, le simple fait d'expliquer votre code vous aide à identifier le problème.

### 7.3 Lire les messages d'erreur attentivement

Python fournit des messages d'erreur détaillés. Apprenez à les lire :

```python
# Erreur typique
liste = [1, 2, 3]  
element = liste[5]  
```

**Message d'erreur :**
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    element = liste[5]
IndexError: list index out of range
```

**Comment le lire :**
- **Traceback** : Montre le chemin d'exécution
- **File "script.py", line 2** : L'erreur est à la ligne 2
- **IndexError** : Type d'erreur (index hors limites)
- **list index out of range** : Description de l'erreur

### 7.4 Utiliser le mode verbeux

Certaines bibliothèques offrent un mode verbeux qui affiche plus d'informations :

```python
import requests

# Mode normal
response = requests.get('https://api.example.com/data')

# Mode verbeux (affiche les détails de la requête)
import logging  
logging.basicConfig(level=logging.DEBUG)  
response = requests.get('https://api.example.com/data')  
```

### 7.5 Documenter les bugs connus

Quand vous trouvez un bug, documentez-le :

```python
def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.

    BUG CONNU : Ne gère pas les listes vides
    TODO : Ajouter une vérification pour les listes vides
    """
    return sum(nombres) / len(nombres)

# Version corrigée
def calculer_moyenne_v2(nombres):
    """
    Calcule la moyenne d'une liste de nombres.

    Args:
        nombres (list): Liste de nombres

    Returns:
        float: La moyenne, ou None si la liste est vide
    """
    if not nombres:
        logging.warning("Tentative de calcul de moyenne sur une liste vide")
        return None
    return sum(nombres) / len(nombres)
```

---

## 8. Checklist de débogage pour débutants

Quand vous rencontrez un bug, suivez cette checklist :

### ✅ Étape 1 : Comprendre le problème
- [ ] Quel est le comportement attendu ?
- [ ] Quel est le comportement actuel ?
- [ ] Le bug se produit-il toujours ou de manière aléatoire ?

### ✅ Étape 2 : Lire le message d'erreur
- [ ] Quel type d'erreur est levée ?
- [ ] À quelle ligne se produit l'erreur ?
- [ ] Que dit le message d'erreur ?

### ✅ Étape 3 : Vérifier les bases
- [ ] Les noms de variables sont-ils corrects ?
- [ ] L'indentation est-elle correcte ?
- [ ] Les types de données sont-ils appropriés ?
- [ ] Y a-t-il des parenthèses ou crochets manquants ?

### ✅ Étape 4 : Isoler le problème
- [ ] Ajouter des print() pour voir les valeurs des variables
- [ ] Commenter des sections de code
- [ ] Créer un exemple minimal

### ✅ Étape 5 : Utiliser les outils
- [ ] Essayer pdb ou le débogueur de votre IDE
- [ ] Utiliser logging pour tracer l'exécution
- [ ] Vérifier avec des assertions

### ✅ Étape 6 : Chercher de l'aide
- [ ] Lire la documentation officielle
- [ ] Rechercher l'erreur sur Google/Stack Overflow
- [ ] Demander sur des forums Python

---

## 9. Erreurs courantes et comment les déboguer

### Erreur 1 : IndentationError

```python
# Code incorrect
def ma_fonction():  
print("Bonjour")  # Mauvaise indentation  
```

**Solution :**
```python
def ma_fonction():
    print("Bonjour")  # Indentation correcte avec 4 espaces
```

### Erreur 2 : NameError

```python
# Code incorrect
print(prenom)  # prenom n'a pas été défini
```

**Débogage :**
```python
# Vérifier si la variable existe
import sys

def afficher_nom():
    if 'prenom' in dir():
        print(prenom)
    else:
        print("La variable 'prenom' n'existe pas")
        print("Variables disponibles :", [v for v in dir() if not v.startswith('_')])
```

### Erreur 3 : TypeError

```python
# Code incorrect
age = "25"  
nouvelle_age = age + 1  # Impossible d'additionner str et int  
```

**Débogage :**
```python
age = "25"  
print(f"Type de age : {type(age)}")  # <class 'str'>  

# Solution
age = int("25")  
nouvelle_age = age + 1  
print(nouvelle_age)  # 26  
```

### Erreur 4 : IndexError

```python
# Code incorrect
liste = [1, 2, 3]  
element = liste[10]  # Index hors limites  
```

**Débogage :**
```python
liste = [1, 2, 3]  
index = 10  

print(f"Longueur de la liste : {len(liste)}")  
print(f"Index demandé : {index}")  

if index < len(liste):
    element = liste[index]
else:
    print(f"Erreur : index {index} trop grand (max : {len(liste)-1})")
```

### Erreur 5 : KeyError

```python
# Code incorrect
personne = {'nom': 'Alice', 'age': 25}  
ville = personne['ville']  # La clé 'ville' n'existe pas  
```

**Débogage :**
```python
personne = {'nom': 'Alice', 'age': 25}  
cle = 'ville'  

print(f"Clés disponibles : {list(personne.keys())}")

# Solution 1 : vérifier avec 'in'
if cle in personne:
    ville = personne[cle]
else:
    print(f"La clé '{cle}' n'existe pas")

# Solution 2 : utiliser get()
ville = personne.get('ville', 'Non spécifié')  
print(f"Ville : {ville}")  
```

---

## 10. Résumé des outils de débogage

| Outil | Niveau | Avantages | Inconvénients | Quand l'utiliser |
|-------|--------|-----------|---------------|------------------|
| **print()** | Débutant | Simple, rapide | Encombre le code | Débogage rapide et simple |
| **assert** | Débutant | Vérifie les hypothèses | Peut être désactivé | Pendant le développement |
| **logging** | Intermédiaire | Professionnel, flexible | Configuration initiale | Tous les projets |
| **pdb** | Intermédiaire | Puissant, intégré | Courbe d'apprentissage | Bugs complexes |
| **IDE Debugger** | Tous | Interface graphique | Dépend de l'IDE | Développement quotidien |
| **traceback** | Intermédiaire | Détails complets | Verbeux | Analyser les erreurs |

---

## Conclusion

Le débogage est une compétence qui s'améliore avec la pratique. Commencez par les techniques simples comme `print()` et `assert`, puis progressez vers des outils plus avancés comme `pdb` et les débogueurs d'IDE.

**Conseils finaux pour déboguer efficacement :**

1. **Restez calme** : Tout bug a une solution
2. **Soyez méthodique** : Suivez une approche systématique
3. **Lisez les messages d'erreur** : Ils contiennent souvent la solution
4. **Simplifiez** : Créez des exemples minimaux
5. **Documentez** : Notez ce qui fonctionne et ce qui ne fonctionne pas
6. **Prenez des pauses** : Parfois, revenir avec un esprit frais aide
7. **Demandez de l'aide** : N'hésitez pas à consulter la communauté

Le débogage n'est pas un signe de faiblesse, c'est une partie normale et essentielle du développement. Même les programmeurs les plus expérimentés passent du temps à déboguer. L'important est d'avoir les bons outils et les bonnes techniques pour le faire efficacement.

Bonne chance dans votre apprentissage du débogage Python ! 🐍✨

⏭️ [Profiling et optimisation](/09-erreurs-et-debogage/04-profiling-et-optimisation.md)
