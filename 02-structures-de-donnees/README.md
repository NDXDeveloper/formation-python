🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 2. Structures de Données Avancées

## Introduction Générale

Bienvenue dans cette section consacrée aux structures de données avancées en Python ! Si vous avez maîtrisé les fondamentaux du langage (variables, boucles, fonctions), vous êtes maintenant prêt à découvrir comment organiser et manipuler efficacement vos données.

### Qu'est-ce qu'une structure de données ?

Une **structure de données** est une manière d'organiser et de stocker des informations dans un programme. Imaginez votre code comme une bibliothèque : vous pourriez empiler tous vos livres n'importe comment, mais il est beaucoup plus efficace de les organiser sur des étagères, par catégories, avec un système de classement.

De la même manière, Python vous offre différents "conteneurs" pour stocker vos données, chacun avec ses propres caractéristiques et avantages.

### Pourquoi apprendre les structures de données ?

**1. Efficacité**

Choisir la bonne structure de données peut transformer un programme lent en un programme rapide. Par exemple, chercher un élément dans une liste de 10 000 éléments peut prendre beaucoup plus de temps que dans un dictionnaire.

```python
# Exemple simple
# Liste : recherche lente pour de grandes quantités de données
utilisateurs_liste = ["alice", "bob", "charlie", ...]  # 10 000 utilisateurs  
if "marie" in utilisateurs_liste:  # Doit parcourir toute la liste  
    print("Utilisateur trouvé")

# Set : recherche instantanée
utilisateurs_set = {"alice", "bob", "charlie", ...}  # 10 000 utilisateurs  
if "marie" in utilisateurs_set:  # Recherche ultra-rapide  
    print("Utilisateur trouvé")
```

**2. Lisibilité**

Utiliser la bonne structure rend votre code plus clair et plus facile à comprendre.

```python
# ❌ Peu lisible : utiliser des indices numériques
personne = ("Alice", 25, "Paris")  
nom = personne[0]  # Qu'est-ce que personne[0] ?  
age = personne[1]  # Et personne[1] ?  

# ✅ Plus lisible : utiliser des clés explicites
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}  
nom = personne["nom"]  # Beaucoup plus clair !  
age = personne["age"]  
```

**3. Fonctionnalités**

Chaque structure offre des opérations spécifiques qui simplifient votre travail.

```python
# Compter automatiquement les occurrences
from collections import Counter

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]  
resultats = Counter(votes)  
print(resultats)  # Counter({'Alice': 3, 'Bob': 2, 'Charlie': 1})  
print(resultats.most_common(1))  # [('Alice', 3)]  
```

### Analogies du monde réel

Pour mieux comprendre les structures de données, voici quelques analogies :

| Structure | Analogie | Caractéristique principale |
|-----------|----------|---------------------------|
| **Liste** | File d'attente au supermarché | Ordre préservé, peut contenir des doublons |
| **Tuple** | Coordonnées GPS fixées | Comme une liste mais immuable |
| **Dictionnaire** | Annuaire téléphonique | Association nom → numéro |
| **Set** | Ensemble mathématique | Éléments uniques, pas d'ordre |

### Les concepts clés à maîtriser

Avant de plonger dans les détails, voici les concepts fondamentaux que nous allons explorer :

**1. Mutabilité vs Immuabilité**

Certaines structures peuvent être modifiées après leur création (mutables), d'autres non (immuables).

```python
# Mutable : on peut modifier
ma_liste = [1, 2, 3]  
ma_liste[0] = 10  # ✓ Fonctionne  
print(ma_liste)   # [10, 2, 3]  

# Immuable : on ne peut pas modifier
mon_tuple = (1, 2, 3)
# mon_tuple[0] = 10  # ✗ Erreur !
```

**2. Ordre vs Non-ordre**

Certaines structures conservent l'ordre dans lequel vous ajoutez les éléments, d'autres non.

```python
# Ordonné : conserve l'ordre
ma_liste = [3, 1, 2]  
print(ma_liste)  # [3, 1, 2] - ordre préservé  

# Non-ordonné : ordre arbitraire
mon_set = {3, 1, 2}  
print(mon_set)  # Peut afficher {1, 2, 3} ou autre  
```

**3. Unicité des éléments**

Certaines structures acceptent les doublons, d'autres garantissent l'unicité.

```python
# Avec doublons
ma_liste = [1, 2, 2, 3, 3, 3]  
print(ma_liste)  # [1, 2, 2, 3, 3, 3]  

# Sans doublons
mon_set = {1, 2, 2, 3, 3, 3}  
print(mon_set)  # {1, 2, 3} - doublons automatiquement supprimés  
```

**4. Accès aux données**

Différentes méthodes pour accéder aux éléments : par indice, par clé, ou par itération.

```python
# Accès par indice
ma_liste = ["a", "b", "c"]  
print(ma_liste[1])  # "b"  

# Accès par clé
mon_dict = {"nom": "Alice", "age": 25}  
print(mon_dict["nom"])  # "Alice"  

# Pas d'accès direct, seulement par itération
mon_set = {1, 2, 3}  
for element in mon_set:  
    print(element)
```

### Vue d'ensemble de cette section

Dans cette section, nous allons explorer en profondeur quatre chapitres essentiels :

#### **2.1 Listes, Tuples, Dictionnaires et Sets**

Les quatre structures de données fondamentales de Python. Vous apprendrez :
- Comment créer et manipuler chaque structure
- Les opérations courantes (ajout, suppression, recherche)
- Quand utiliser chaque structure
- Les pièges à éviter

```python
# Aperçu rapide
liste = [1, 2, 3, 4]              # Collection ordonnée et modifiable  
mon_tuple = (1, 2, 3, 4)          # Collection ordonnée et immuable  
dictionnaire = {"a": 1, "b": 2}   # Paires clé-valeur  
ensemble = {1, 2, 3, 4}           # Collection d'éléments uniques  
```

#### **2.2 Compréhensions de Listes et Dictionnaires**

Une syntaxe élégante pour créer des collections en une seule ligne. Vous découvrirez :
- Comment transformer des données efficacement
- Le filtrage avec des conditions
- Les compréhensions imbriquées
- Les expressions génératrices

```python
# Aperçu rapide
# Au lieu de :
carres = []  
for i in range(10):  
    carres.append(i ** 2)

# Vous écrirez :
carres = [i ** 2 for i in range(10)]
```

#### **2.3 Collections Spécialisées**

Des structures avancées du module `collections` pour des besoins spécifiques :
- **namedtuple** : tuples avec des champs nommés
- **defaultdict** : dictionnaires avec valeurs par défaut
- **Counter** : compter des éléments facilement
- Et d'autres outils puissants

```python
# Aperçu rapide
from collections import Counter

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice"]  
resultats = Counter(votes)  
print(resultats.most_common(1))  # [('Alice', 3)]  
```

#### **2.4 Manipulation de Chaînes et Expressions Régulières**

Les chaînes de caractères sont omniprésentes en programmation. Vous maîtriserez :
- Les méthodes de manipulation de texte
- Le formatage moderne avec f-strings
- Les expressions régulières pour rechercher des motifs complexes
- Les cas d'usage pratiques (validation, extraction, nettoyage)

```python
# Aperçu rapide
nom = "Alice"  
age = 25  
message = f"Je m'appelle {nom} et j'ai {age} ans"  

# Expressions régulières
import re  
email = "alice@example.com"  
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):  
    print("Email valide")
```

### Comment aborder cette section ?

**1. Suivez l'ordre**

Les chapitres sont conçus pour être étudiés dans l'ordre. Chaque concept s'appuie sur les précédents.

**2. Pratiquez avec des exemples**

Chaque chapitre contient de nombreux exemples de code. N'hésitez pas à les exécuter, les modifier, et expérimenter !

**3. Prenez votre temps**

Les structures de données sont un concept fondamental. Il est normal de prendre plusieurs jours, voire semaines, pour bien les assimiler.

**4. Créez vos propres exemples**

La meilleure façon d'apprendre est de créer vos propres programmes utilisant ces structures.

**5. Revenez-y régulièrement**

Vous découvrirez de nouveaux détails et subtilités à chaque relecture.

### Prérequis

Avant de commencer cette section, assurez-vous d'être à l'aise avec :

✓ Les variables et les types de données de base (int, float, str, bool)  
✓ Les structures de contrôle (if/else, boucles for et while)  
✓ Les fonctions de base  
✓ La syntaxe Python générale

Si vous n'êtes pas sûr de ces concepts, il peut être utile de revoir la section "Fondamentaux et syntaxe de base" avant de continuer.

### Tableau récapitulatif des structures

Voici un tableau de référence rapide que vous pourrez consulter tout au long de votre apprentissage :

| Structure | Syntaxe | Ordonné | Modifiable | Doublons | Usage principal |
|-----------|---------|---------|------------|----------|-----------------|
| **Liste** | `[1, 2, 3]` | ✓ | ✓ | ✓ | Collection générale |
| **Tuple** | `(1, 2, 3)` | ✓ | ✗ | ✓ | Données immuables |
| **Dictionnaire** | `{"a": 1}` | ✓* | ✓ | ✗ (clés) | Paires clé-valeur |
| **Set** | `{1, 2, 3}` | ✗ | ✓ | ✗ | Éléments uniques |

*Depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion.

### Conseils pour bien démarrer

**💡 Conseil n°1 : Expérimentez**

N'ayez pas peur d'essayer différentes structures pour résoudre le même problème. C'est en comparant que vous développerez votre intuition.

```python
# Même problème, différentes approches
# Stocker des étudiants avec leurs notes

# Approche 1 : Dictionnaire
notes_dict = {"Alice": 18, "Bob": 15, "Charlie": 17}

# Approche 2 : Liste de tuples
notes_list = [("Alice", 18), ("Bob", 15), ("Charlie", 17)]

# Approche 3 : namedtuple
from collections import namedtuple  
Etudiant = namedtuple('Etudiant', 'nom note')  
notes_named = [Etudiant("Alice", 18), Etudiant("Bob", 15), Etudiant("Charlie", 17)]  

# Quelle approche est la meilleure ? Ça dépend de votre cas d'usage !
```

**💡 Conseil n°2 : Pensez aux performances**

Pour de petites quantités de données, la différence de performance est négligeable. Mais pour de gros volumes, le choix de la structure peut être crucial.

```python
# Pour 10 éléments : peu de différence
# Pour 10 000 éléments : grande différence !

# Recherche dans une liste : O(n) - peut être lent
if "element" in ma_grande_liste:
    pass

# Recherche dans un set : O(1) - très rapide
if "element" in mon_grand_set:
    pass
```

**💡 Conseil n°3 : Privilégiez la lisibilité**

Un code clair vaut mieux qu'un code "intelligent" mais incompréhensible.

```python
# ❌ Concis mais difficile à comprendre
d = {k: [x for x in v if x > 0] for k, v in data.items() if len(v) > 2}

# ✅ Plus verbeux mais plus clair
resultat = {}  
for cle, valeurs in data.items():  
    if len(valeurs) > 2:
        valeurs_positives = [x for x in valeurs if x > 0]
        resultat[cle] = valeurs_positives
```

**💡 Conseil n°4 : Documentez-vous**

Python a une excellente documentation. N'hésitez pas à utiliser la fonction `help()` :

```python
# Dans l'interpréteur Python
help(list)  
help(dict)  
help(set)  

# Ou pour une méthode spécifique
help(str.split)
```

### Objectifs d'apprentissage

À la fin de cette section, vous serez capable de :

✓ Choisir la structure de données appropriée pour chaque situation  
✓ Manipuler efficacement les listes, tuples, dictionnaires et sets  
✓ Utiliser les compréhensions pour créer des collections de manière concise  
✓ Exploiter les collections spécialisées pour des besoins avancés  
✓ Maîtriser la manipulation de texte et les expressions régulières  
✓ Écrire du code plus lisible, plus efficace et plus pythonique

### Erreurs courantes à éviter

Voici quelques pièges dans lesquels les débutants tombent souvent :

**Erreur n°1 : Créer une référence au lieu d'une copie**

```python
# ❌ Erreur
liste1 = [1, 2, 3]  
liste2 = liste1  # liste2 référence liste1  
liste2.append(4)  
print(liste1)  # [1, 2, 3, 4] - liste1 a aussi changé !  

# ✓ Correct
liste1 = [1, 2, 3]  
liste2 = liste1.copy()  # Crée une vraie copie  
liste2.append(4)  
print(liste1)  # [1, 2, 3] - liste1 n'a pas changé  
```

**Erreur n°2 : Modifier une liste pendant l'itération**

```python
# ❌ Erreur
nombres = [1, 2, 3, 4, 5]  
for n in nombres:  
    if n % 2 == 0:
        nombres.remove(n)  # Dangereux !

# ✓ Correct
nombres = [1, 2, 3, 4, 5]  
nombres = [n for n in nombres if n % 2 != 0]  
```

**Erreur n°3 : Utiliser une liste quand un set suffirait**

```python
# ❌ Moins efficace
elements_uniques = []  
for item in grande_liste:  
    if item not in elements_uniques:
        elements_uniques.append(item)

# ✓ Plus efficace
elements_uniques = set(grande_liste)
```

**Erreur n°4 : Oublier que les dictionnaires sont mutables**

```python
# ❌ Erreur : argument mutable par défaut
def ajouter_entree(nom, dico={}):
    dico[nom] = len(dico) + 1
    return dico

# Le dictionnaire par défaut est partagé entre tous les appels !
print(ajouter_entree("alice"))   # {'alice': 1}  
print(ajouter_entree("bob"))     # {'alice': 1, 'bob': 2} — surprise !  

# ✓ Correct : utiliser None comme valeur par défaut
def ajouter_entree(nom, dico=None):
    if dico is None:
        dico = {}
    dico[nom] = len(dico) + 1
    return dico

print(ajouter_entree("alice"))   # {'alice': 1}  
print(ajouter_entree("bob"))     # {'bob': 1} — un nouveau dict à chaque appel  
```

### Ressources complémentaires

Pour approfondir votre apprentissage :

- **Documentation officielle Python** : [docs.python.org](https://docs.python.org/fr/3/)
- **Python Tutor** : Visualisez l'exécution de votre code étape par étape
- **StackOverflow** : Une mine d'or pour les questions spécifiques
- **Real Python** : Tutoriels de qualité sur tous les aspects de Python

### Un mot sur la notation Big O

Vous entendrez souvent parler de "complexité algorithmique" ou "notation Big O" quand on discute de structures de données. En bref :

- **O(1)** : Temps constant - très rapide, ne dépend pas de la taille des données
- **O(n)** : Temps linéaire - proportionnel à la taille des données
- **O(n²)** : Temps quadratique - peut devenir très lent

```python
# O(1) - Accès à un élément du dictionnaire
valeur = mon_dict["cle"]  # Temps constant

# O(n) - Recherche dans une liste
if element in ma_liste:  # Doit potentiellement parcourir toute la liste
    pass

# O(n²) - Boucles imbriquées
for i in liste1:
    for j in liste2:
        # Opération
        pass
```

Ne vous inquiétez pas si ce concept n'est pas encore clair. Vous le comprendrez progressivement en travaillant avec les structures de données.

### Prêt à commencer ?

Vous avez maintenant une vue d'ensemble de ce qui vous attend dans cette section. Les structures de données sont un pilier fondamental de la programmation, et les maîtriser vous permettra d'écrire du code Python élégant, efficace et professionnel.

Prenez votre temps, pratiquez beaucoup, et n'oubliez pas : chaque expert a commencé comme débutant. La clé du succès est la pratique régulière et la persévérance.

Bonne chance et bon apprentissage ! 🚀

---


⏭️ [Listes, tuples, dictionnaires et sets](/02-structures-de-donnees/01-listes-tuples-dicts-sets.md)
