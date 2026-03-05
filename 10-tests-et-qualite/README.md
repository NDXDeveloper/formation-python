🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 10. Tests et qualité du code - Introduction

## Bienvenue dans le monde de la qualité logicielle !

Cette section est l'une des plus importantes de votre parcours d'apprentissage Python. Pourquoi ? Parce qu'écrire du code qui fonctionne est une chose, mais écrire du code **de qualité, fiable et maintenable** en est une autre.

**Analogie** : Imaginez deux chefs qui préparent le même plat. Le premier cuisine vite, sans se soucier de la propreté de sa cuisine, ne goûte jamais pendant la préparation, et le résultat est aléatoire. Le second travaille avec méthode, goûte régulièrement, vérifie chaque étape, et maintient sa cuisine impeccable. Les deux peuvent produire un plat, mais lequel choisiriez-vous pour un restaurant ?

C'est la même chose en programmation : les tests et la qualité du code sont ce qui distingue un développeur professionnel d'un débutant.

---

## Qu'est-ce que la qualité du code ?

### Définition

La **qualité du code** englobe plusieurs aspects qui rendent un programme :
- **Fiable** : Il fait ce qu'il est censé faire, sans bugs
- **Lisible** : Les autres (et vous dans 6 mois) peuvent le comprendre
- **Maintenable** : Il est facile de le modifier et de l'améliorer
- **Testable** : On peut vérifier qu'il fonctionne correctement
- **Performant** : Il utilise les ressources efficacement
- **Sécurisé** : Il protège contre les failles de sécurité

### Les piliers de la qualité

```
┌─────────────────────────────────────┐
│     QUALITÉ DU CODE                 │
├─────────────────────────────────────┤
│  1. Tests                           │
│     - Unitaires                     │
│     - Intégration                   │
│     - Couverture                    │
│                                     │
│  2. Style et conventions            │
│     - PEP 8                         │
│     - Linting                       │
│     - Formatage                     │
│                                     │
│  3. Documentation                   │
│     - Docstrings                    │
│     - Commentaires                  │
│     - README                        │
│                                     │
│  4. Typage                          │
│     - Type hints                    │
│     - Validation mypy               │
│                                     │
│  5. Bonnes pratiques                │
│     - Architecture                  │
│     - Patterns                      │
│     - Révision de code              │
└─────────────────────────────────────┘
```

---

## Pourquoi investir dans la qualité ?

### 1. Économie de temps à long terme

```python
# Scénario A : Code sans tests
def calculer_prix_total(prix, quantite, tva):
    return prix * quantite * tva

# 3 mois plus tard : un bug est détecté en production
# Il faut chercher dans tout le code où cette fonction est utilisée
# Réparer le bug, tester manuellement tous les cas...
# Temps perdu : plusieurs heures, voire jours
```

```python
# Scénario B : Code avec tests
def calculer_prix_total(prix, quantite, tva):
    """Calcule le prix total TTC."""
    return prix * quantite * (1 + tva)

def test_calculer_prix_total():
    assert calculer_prix_total(10, 2, 0.20) == 24.0
    assert calculer_prix_total(100, 1, 0.055) == 105.5

# Modification du code : les tests détectent immédiatement si ça casse
# Temps gagné : énorme !
```

**Règle d'or** : Le temps investi dans les tests est toujours récupéré (et plus) lors de la maintenance.

### 2. Confiance et sérénité

Avec des tests et un code de qualité :
- ✅ Vous pouvez modifier le code sans crainte de tout casser
- ✅ Vous dormez tranquille, le code est fiable
- ✅ Vous pouvez refactoriser en toute confiance
- ✅ Les nouveaux développeurs peuvent contribuer sans risque

Sans tests :
- ❌ Chaque modification est stressante
- ❌ La peur de casser quelque chose paralyse
- ❌ Le code devient "legacy" qu'on n'ose plus toucher
- ❌ Les bugs se multiplient

### 3. Professionnalisme

Dans le monde professionnel :
- **Tous les projets sérieux** ont des tests
- **Les entretiens d'embauche** évaluent la qualité du code
- **Les revues de code** vérifient tests et style
- **La dette technique** sans tests coûte très cher

**Citation** : "Code without tests is broken by design." - Jacob Kaplan-Moss (co-créateur de Django)

### 4. Documentation vivante

Les tests servent aussi de documentation :

```python
def test_creer_utilisateur_avec_email_valide():
    """Exemple d'utilisation : créer un utilisateur."""
    user = creer_utilisateur("alice@example.com", "Alice", 25)
    assert user.email == "alice@example.com"
    assert user.nom == "Alice"
    assert user.age == 25

def test_creer_utilisateur_avec_email_invalide():
    """Montre qu'un email invalide lève une erreur."""
    with pytest.raises(ValueError):
        creer_utilisateur("email_invalide", "Bob", 30)
```

Ces tests montrent **comment utiliser** la fonction et **quels sont les comportements attendus**.

---

## Les différents types de tests

### Pyramide des tests

```
                  ▲
                 /E\          E2E (End-to-End)
                /___\         Tests de bout en bout
               /     \        Peu nombreux, lents
              /       \
             /_________\      Integration
            /           \     Tests d'intégration
           /             \    Moyennement nombreux
          /               \
         /                 \
        /___________________\  Unit
       /                     \ Tests unitaires
      /                       \ Très nombreux, rapides
     /_________________________\
```

### 1. Tests unitaires (Unit Tests)

**Quoi** : Testent une petite unité de code isolément (une fonction, une méthode).

**Exemple** :
```python
def additionner(a, b):
    return a + b

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0
    assert additionner(0, 0) == 0
```

**Caractéristiques** :
- ⚡ Très rapides (millisecondes)
- 🎯 Ciblés et précis
- 🔁 Nombreux (des centaines, voire milliers)
- 🚀 Base de la qualité

### 2. Tests d'intégration (Integration Tests)

**Quoi** : Testent comment plusieurs composants fonctionnent ensemble.

**Exemple** :
```python
def test_creer_et_sauvegarder_utilisateur():
    """Teste l'intégration entre le service et la base de données."""
    db = BaseDeDonnees()
    service = ServiceUtilisateur(db)

    user_id = service.creer_utilisateur("Alice", "alice@test.com")
    utilisateur = service.obtenir_utilisateur(user_id)

    assert utilisateur.nom == "Alice"
```

**Caractéristiques** :
- 🐌 Plus lents (secondes)
- 🔗 Testent les interactions
- 📊 Moyennement nombreux (dizaines, centaines)

### 3. Tests end-to-end (E2E)

**Quoi** : Testent l'application complète, du point de vue de l'utilisateur.

**Exemple** :
```python
def test_inscription_complete():
    """Teste le parcours complet d'inscription."""
    # 1. Ouvrir la page d'inscription
    # 2. Remplir le formulaire
    # 3. Soumettre
    # 4. Vérifier l'email de confirmation
    # 5. Valider le compte
    # 6. Se connecter
    pass
```

**Caractéristiques** :
- 🐢 Très lents (minutes)
- 🎭 Simulent un utilisateur réel
- 📉 Peu nombreux (quelques-uns)
- 💰 Coûteux à maintenir

### Quel type de test choisir ?

**Règle générale** : Privilégiez les tests unitaires !

- **70-80% tests unitaires** : Rapides, fiables, faciles à maintenir
- **20-30% tests d'intégration** : Vérifient les interactions importantes
- **5-10% tests E2E** : Valident les parcours critiques

---

## Vue d'ensemble du chapitre

Dans ce chapitre, nous allons explorer en détail tous les aspects de la qualité du code :

### 10.1 Tests unitaires avec unittest et pytest

**Ce que vous apprendrez** :
- Écrire vos premiers tests unitaires
- Utiliser unittest (bibliothèque standard)
- Utiliser pytest (outil moderne et puissant)
- Organiser vos tests
- Assertions et vérifications

**Pourquoi c'est important** : Les tests unitaires sont la base de tout. Sans eux, impossible de garantir que votre code fonctionne.

### 10.2 Mocking et fixtures

**Ce que vous apprendrez** :
- Créer des fixtures pour préparer vos tests
- Utiliser le mocking pour simuler des dépendances
- Tester du code qui appelle des API ou bases de données
- Isoler les tests des dépendances externes

**Pourquoi c'est important** : Le code réel dépend souvent de services externes (API, BDD, fichiers). Le mocking permet de tester sans ces dépendances.

### 10.3 Couverture de code

**Ce que vous apprendrez** :
- Mesurer quel pourcentage de votre code est testé
- Utiliser coverage.py et pytest-cov
- Identifier les parties non testées
- Interpréter les rapports de couverture

**Pourquoi c'est important** : La couverture vous aide à savoir quelles parties de votre code manquent de tests.

### 10.4 Documentation avec docstrings

**Ce que vous apprendrez** :
- Écrire des docstrings claires et utiles
- Utiliser différents styles (Google, NumPy, Sphinx)
- Générer de la documentation automatique
- Documenter modules, classes et fonctions

**Pourquoi c'est important** : Un code bien documenté est un code que les autres (et vous-même) peuvent comprendre et utiliser facilement.

### 10.5 PEP 8 et outils de linting

**Ce que vous apprendrez** :
- Suivre les conventions de style Python (PEP 8)
- Utiliser des linters (flake8, pylint)
- Formater automatiquement avec Black
- Automatiser les vérifications

**Pourquoi c'est important** : Un style cohérent rend le code plus lisible et professionnel. Les outils automatiques détectent les erreurs potentielles.

### 10.6 Validation de types avec mypy

**Ce que vous apprendrez** :
- Ajouter des annotations de types (type hints)
- Utiliser mypy pour vérifier les types
- Détecter les bugs avant l'exécution
- Améliorer la documentation du code

**Pourquoi c'est important** : Les types aident à prévenir de nombreux bugs et rendent le code plus robuste.

---

## Concepts fondamentaux

### Qu'est-ce qu'un test ?

Un test est un **programme qui vérifie qu'un autre programme fonctionne correctement**.

**Structure d'un test** (pattern AAA) :

```python
def test_exemple():
    # 1. ARRANGE (Préparer)
    # Configurer les données et l'environnement
    utilisateur = Utilisateur("Alice", 25)

    # 2. ACT (Agir)
    # Exécuter le code à tester
    resultat = utilisateur.est_majeur()

    # 3. ASSERT (Vérifier)
    # Vérifier que le résultat est correct
    assert resultat == True
```

### Qu'est-ce qu'une assertion ?

Une **assertion** est une vérification qui échoue si la condition n'est pas vraie.

```python
# Assertions de base
assert 2 + 2 == 4              # Passe  
assert "hello".upper() == "HELLO"  # Passe  
assert len([1, 2, 3]) == 3     # Passe  

# Si l'assertion échoue, le test échoue
assert 2 + 2 == 5              # ❌ Échec !
```

**En pytest** :
```python
# Égalité
assert calculer(5, 3) == 8

# Appartenance
assert 3 in [1, 2, 3, 4]

# Exceptions
with pytest.raises(ValueError):
    diviser(10, 0)

# Approximation (nombres flottants)
assert 0.1 + 0.2 == pytest.approx(0.3)
```

### Test Driven Development (TDD)

Le **TDD** (développement piloté par les tests) est une méthode où vous écrivez les tests **avant** le code.

**Cycle TDD** :

```
1. ❌ RED : Écrire un test qui échoue
    ↓
2. ✅ GREEN : Écrire le code minimal pour le faire passer
    ↓
3. ♻️ REFACTOR : Améliorer le code
    ↓
   (Recommencer)
```

**Exemple** :

```python
# Étape 1 : Écrire le test (qui échoue)
def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3]) == 2.0

# Étape 2 : Écrire le code minimal
def calculer_moyenne(nombres):
    return sum(nombres) / len(nombres)

# Étape 3 : Refactoriser si nécessaire
def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres."""
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
    return sum(nombres) / len(nombres)

# Ajouter plus de tests
def test_calculer_moyenne_liste_vide():
    with pytest.raises(ValueError):
        calculer_moyenne([])
```

**Avantages du TDD** :
- Force à réfléchir à l'API avant d'écrire le code
- Garantit que le code est testable
- Documentation automatique via les tests
- Moins de bugs

### Règles d'or des tests

#### 1. Un test = Une vérification

```python
# ✅ Bon - chaque test vérifie une chose
def test_utilisateur_nom():
    user = Utilisateur("Alice")
    assert user.nom == "Alice"

def test_utilisateur_actif_par_defaut():
    user = Utilisateur("Alice")
    assert user.actif == True

# ❌ Mauvais - teste trop de choses
def test_utilisateur():
    user = Utilisateur("Alice")
    assert user.nom == "Alice"
    assert user.actif == True
    assert user.email is None
    assert user.age is None
    # ... trop de vérifications
```

#### 2. Tests indépendants

Chaque test doit pouvoir s'exécuter seul, dans n'importe quel ordre.

```python
# ✅ Bon - tests indépendants
def test_ajouter_utilisateur():
    db = nouvelle_base()  # Nouvelle base pour chaque test
    db.ajouter(Utilisateur("Alice"))
    assert db.compter() == 1

def test_supprimer_utilisateur():
    db = nouvelle_base()  # Nouvelle base pour chaque test
    user = Utilisateur("Bob")
    db.ajouter(user)
    db.supprimer(user)
    assert db.compter() == 0

# ❌ Mauvais - tests dépendants
db_globale = BaseDeDonnees()

def test_ajouter_utilisateur():
    db_globale.ajouter(Utilisateur("Alice"))
    assert db_globale.compter() == 1

def test_supprimer_utilisateur():
    # Dépend du test précédent !
    db_globale.supprimer_dernier()
    assert db_globale.compter() == 0
```

#### 3. Tests rapides

Les tests doivent s'exécuter rapidement pour être lancés souvent.

```python
# ✅ Bon - test rapide (~1ms)
def test_calculer():
    assert calculer(5, 3) == 8

# ❌ Mauvais - test lent (plusieurs secondes)
def test_importer_fichier_enorme():
    # Télécharge 1GB de données...
    # Traite pendant 10 secondes...
    pass
```

**Objectif** : Exécuter tous les tests unitaires en moins de 10 secondes.

#### 4. Tests lisibles

Un test doit être facile à comprendre, même sans connaître le code testé.

```python
# ✅ Bon - test clair et descriptif
def test_utilisateur_peut_se_connecter_avec_bon_mot_de_passe():
    user = Utilisateur("alice@test.com", "motdepasse123")
    resultat = user.se_connecter("motdepasse123")
    assert resultat == True

def test_utilisateur_ne_peut_pas_se_connecter_avec_mauvais_mot_de_passe():
    user = Utilisateur("alice@test.com", "motdepasse123")
    resultat = user.se_connecter("mauvais")
    assert resultat == False

# ❌ Mauvais - test cryptique
def test_login():
    u = User("a@t.c", "p")
    assert u.l("p") == True
```

#### 5. Testez les cas limites

N'oubliez pas les cas particuliers !

```python
def calculer_moyenne(nombres):
    return sum(nombres) / len(nombres)

# Tests des cas normaux
def test_moyenne_nombres_positifs():
    assert calculer_moyenne([1, 2, 3]) == 2.0

# Tests des cas limites
def test_moyenne_un_seul_nombre():
    assert calculer_moyenne([5]) == 5.0

def test_moyenne_nombres_negatifs():
    assert calculer_moyenne([-1, -2, -3]) == -2.0

def test_moyenne_avec_zero():
    assert calculer_moyenne([0, 0, 0]) == 0.0

def test_moyenne_liste_vide():
    with pytest.raises(ZeroDivisionError):
        calculer_moyenne([])
```

**Cas limites courants** :
- Valeurs nulles (None, 0, "", [])
- Valeurs négatives
- Valeurs très grandes
- Cas d'erreur
- Limites de domaine (premiers, derniers éléments)

---

## Qualité au-delà des tests

### Architecture et conception

La qualité du code ne se résume pas aux tests. Une bonne architecture est essentielle :

```python
# ❌ Mauvais - tout dans une fonction
def traiter_utilisateur(data):
    # Validation
    # Traitement
    # Sauvegarde
    # Envoi email
    # Logging
    # 200 lignes de code...
    pass

# ✅ Bon - séparation des responsabilités
def valider_utilisateur(data):
    pass

def creer_utilisateur(data):
    pass

def envoyer_email_bienvenue(user):
    pass

def traiter_utilisateur(data):
    valider_utilisateur(data)
    user = creer_utilisateur(data)
    envoyer_email_bienvenue(user)
```

### Principe SOLID

Cinq principes pour du code de qualité :

1. **S**ingle Responsibility : Une classe = une responsabilité
2. **O**pen/Closed : Ouvert à l'extension, fermé à la modification
3. **L**iskov Substitution : Les sous-classes doivent être substituables
4. **I**nterface Segregation : Interfaces spécifiques plutôt que générales
5. **D**ependency Inversion : Dépendre d'abstractions, pas de concrétions

### Code review (révision de code)

La revue de code est essentielle pour la qualité :

**Points à vérifier** :
- ✅ Les tests passent
- ✅ Le code est lisible
- ✅ Pas de duplication
- ✅ Bonne documentation
- ✅ Respect des conventions
- ✅ Pas de problèmes de sécurité
- ✅ Bonne gestion des erreurs

---

## Outils de qualité

### Checklist des outils essentiels

Pour un projet Python professionnel :

| Outil | Usage | Section |
|-------|-------|---------|
| **pytest** | Tests unitaires | 10.1 |
| **unittest** | Tests unitaires (standard) | 10.1 |
| **pytest-cov** | Couverture de code | 10.3 |
| **coverage.py** | Couverture de code | 10.3 |
| **flake8** | Linting (style) | 10.5 |
| **black** | Formatage automatique | 10.5 |
| **isort** | Organisation des imports | 10.5 |
| **mypy** | Vérification de types | 10.6 |
| **pylint** | Analyse approfondie | 10.5 |
| **pre-commit** | Automatisation | Toutes |

### Pipeline de qualité

```
┌──────────────────────────────────────┐
│  1. Écrire le code                   │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  2. Formater (black, isort)          │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  3. Linter (flake8, pylint)          │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  4. Vérifier les types (mypy)        │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  5. Lancer les tests (pytest)        │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  6. Vérifier la couverture           │
└──────────────────────────────────────┘
              ↓
┌──────────────────────────────────────┐
│  7. Commit                           │
└──────────────────────────────────────┘
```

---

## Mentalité de qualité

### Investissement vs. Coût

**Vision court terme** (mauvaise) :
- "Les tests prennent du temps"
- "La documentation, c'est pour plus tard"
- "Le style, ce n'est pas important"
- "Ça marche, c'est suffisant"

**Vision long terme** (bonne) :
- "Les tests m'économisent du temps de debug"
- "La documentation aide toute l'équipe"
- "Le style rend le code plus lisible"
- "Ça marche ET c'est maintenable"

### La dette technique

**Analogie bancaire** : La dette technique, c'est comme un crédit :
- Vous avancez plus vite au début (pas de tests, pas de doc)
- Mais vous payez des intérêts (bugs, maintenance difficile)
- Et un jour, il faut rembourser (refactoring massif)

**Règle** : Mieux vaut éviter la dette que d'avoir à la rembourser !

### Le scout rule

**"Laissez le code plus propre que vous ne l'avez trouvé"**

À chaque modification :
- Ajoutez un test s'il en manque
- Améliorez la documentation
- Refactorisez un peu
- Corrigez un problème de style

Petit à petit, le code s'améliore !

---

## Ce que vous allez apprendre

Dans les sections suivantes, vous deviendrez capable de :

### Compétences techniques

✅ Écrire des tests unitaires efficaces  
✅ Mesurer et améliorer la couverture de code  
✅ Documenter clairement votre code  
✅ Respecter les conventions Python (PEP 8)  
✅ Valider les types avec mypy  
✅ Utiliser les outils professionnels  
✅ Automatiser les vérifications

### Compétences professionnelles

✅ Travailler dans une équipe de développement  
✅ Contribuer à des projets open source  
✅ Maintenir du code à long terme  
✅ Faire des revues de code constructives  
✅ Écrire du code "production-ready"

### Mentalité de développeur senior

✅ Anticiper les problèmes  
✅ Penser à la maintenance  
✅ Valoriser la lisibilité  
✅ Chercher la simplicité  
✅ Être fier de son code

---

## Préparation

### Installation des outils

Avant de commencer les sections suivantes, installez les outils essentiels :

```bash
# Tests
pip install pytest pytest-cov

# Linting et formatage
pip install flake8 black isort

# Vérification de types
pip install mypy

# Documentation
pip install sphinx

# Automatisation
pip install pre-commit
```

### Configuration de votre éditeur

Configurez votre éditeur pour la qualité :

**VS Code** : Installez les extensions
- Python (Microsoft)
- Pylance
- Black Formatter
- Test Explorer

**PyCharm** : Déjà intégré ! Activez :
- File → Settings → Editor → Inspections → Python
- File → Settings → Tools → Python Integrated Tools → Testing

### Structure de projet recommandée

```
mon_projet/
├── src/
│   └── mon_package/
│       ├── __init__.py
│       └── module.py
├── tests/
│   ├── __init__.py
│   └── test_module.py
├── docs/
│   └── README.md
├── .flake8
├── .gitignore
├── mypy.ini
├── pyproject.toml
├── requirements.txt
└── setup.py
```

---

## Conseil pour débuter

### Commencez petit

Vous n'avez pas besoin de tout maîtriser d'un coup :

**Semaine 1** : Tests de base avec pytest  
**Semaine 2** : Couverture de code  
**Semaine 3** : PEP 8 et Black  
**Semaine 4** : Documentation  
**Semaine 5** : mypy et types  
**Semaine 6** : Automatisation complète  

### Pratiquez régulièrement

La qualité du code s'apprend par la pratique :
- Écrivez des tests pour tout nouveau code
- Revoyez votre ancien code et améliorez-le
- Lisez du code open source de qualité
- Participez à des code reviews

### Soyez patient

La qualité du code est un **voyage**, pas une destination :
- Vous ferez des erreurs, c'est normal
- Chaque projet sera meilleur que le précédent
- La qualité devient une habitude avec le temps

---

## Prêt à commencer ?

Maintenant que vous comprenez l'importance de la qualité du code et ce qui vous attend, vous êtes prêt à plonger dans les détails !

**Prochaine étape** : Section 10.1 - Tests unitaires avec unittest et pytest

**Citation de motivation** :
> "Quality is not an act, it is a habit." - Aristotle

**Citation pour les développeurs** :
> "First, solve the problem. Then, write the code." - John Johnson

Bonne route vers l'excellence en programmation ! 🚀

---

## Résumé

### Points clés à retenir

1. **La qualité du code** = fiabilité + lisibilité + maintenabilité
2. **Les tests** sont essentiels, pas optionnels
3. **Investir dans la qualité** économise du temps à long terme
4. **Les outils** automatisent les vérifications
5. **La documentation** aide toute l'équipe
6. **Le style cohérent** (PEP 8) améliore la lisibilité
7. **Les types** (mypy) préviennent les bugs
8. **La couverture** identifie le code non testé
9. **Commencez petit** et progressez régulièrement
10. **La qualité est une habitude**, pas un acte isolé

### Métriques de qualité

Pour un projet professionnel, visez :
- ✅ **Couverture de tests** : 80-90%
- ✅ **Score pylint** : > 8/10
- ✅ **Respect PEP 8** : 100%
- ✅ **Documentation** : Toutes les fonctions publiques
- ✅ **Types** : Au moins les signatures publiques

### Ce qui suit

Les 6 prochaines sections vous donneront tous les outils et techniques pour atteindre ces objectifs. Chaque section est construite sur les précédentes, créant une base solide de connaissances.

**Allons-y !** 💪

⏭️ [Tests unitaires avec unittest et pytest](/10-tests-et-qualite/01-tests-unitaires-unittest-pytest.md)
