# Exemples - Chapitre 05 : Programmation fonctionnelle

40 fichiers d'exemples exécutables, répartis sur 5 fichiers source.

## Fichier 01 : Lambda et fonctions d'ordre supérieur (3 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `01_01_lambda_base.py` | 5.1 | Classique vs lambda, doubler, est_pair, saluer, maximum | 8, 10, True/False, Bonjour Marie Dupont !, 25 |
| `01_02_fonctions_ordre_superieur.py` | 5.1 | Appliquer opération, créer multiplicateur, filtrer, transformer, composer | 10/15/25, 14/35/70, pairs/multiples, doublés/carrés, 11/25 |
| `01_03_cas_usage_pratiques.py` | 5.1 | Tri personnalisé, réduction de prix, validation mot de passe | Triées par âge/nom, prix réduits de 20%, True/False |

**Fichier source** : `01-lambda-et-fonctions-ordre-superieur.md`

## Fichier 02 : map(), filter(), reduce() (7 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `02_01_map_base.py` | 5.2 | Doubler (boucle vs map), températures, majuscules, longueurs, formatter, plusieurs itérables | [2,4,6,8,10], Fahrenheit [32..104], PYTHON/JAVASCRIPT, [7,20,6,13], Alice/Bob/Charlie |
| `02_02_filter_base.py` | 5.2 | Filtrer pairs, positifs, chaînes longues, dictionnaires, non vides, adultes | [2,4,6,8,10], [3,8,7], éléphant/oiseau/papillon, Pomme/Banane, Alice/Charlie |
| `02_03_reduce_base.py` | 5.2 | Somme, produit, maximum, concaténer, occurrences, aplatir, factorielle | 15, 120, 89, Python est génial, {pomme:3...}, [1..8], 5!=120 |
| `02_04_combiner_map_filter_reduce.py` | 5.2 | Somme carrés des pairs, prix total promo, moyenne notes > 10 | 220, 1175EUR, 14.33 |
| `02_05_comprehensions_vs_fonctionnel.py` | 5.2 | map() vs compréhension, filter() vs compréhension, combiné | [2,4,6,8,10], [4,16,36,64,100] |
| `02_06_cas_usage_avances.py` | 5.2 | Pipeline de ventes, étudiants avec mentions, analyse de texte | Laptop 1600EUR, Alice/Charlie >=15, 11 mots |
| `02_07_alternatives_bonnes_pratiques.py` | 5.2 | sum() vs reduce(), max() vs reduce(), all(), lisibilité, fonctions nommées | 15, 89, True, [4,8,12,16,20], prix TTC |

**Fichier source** : `02-map-filter-reduce.md`

## Fichier 03 : Décorateurs avancés (9 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `03_01_decorateur_rappel.py` | 5.3 | Rappel : décorateur sans @, puis avec syntaxe @ | --- Début --- / Bonjour ! / --- Fin --- |
| `03_02_decorateur_avec_arguments.py` | 5.3 | *args et **kwargs pour accepter tous les arguments | Bonjour Alice !, 5 + 3 = 8, Total : 8 |
| `03_03_decorateur_avec_parametres.py` | 5.3 | Structure 3 niveaux, repeter(), prefixe_suffixe() | Bonjour ! x3, === DÉBUT/FIN === |
| `03_04_decorateurs_pratiques.py` | 5.3 | Mesurer temps, logger, cache (fibonacci), contrôle d'accès | Temps en secondes, log appels, cache 5, auth réussie |
| `03_05_retry_empiler.py` | 5.3 | Retry (réessayer en cas d'échec), empiler décorateurs | 3 tentatives, décorateurs 1+2 imbriqués |
| `03_06_functools_wraps.py` | 5.3 | Perte de métadonnées sans @wraps, solution avec @wraps | fonction_modifiee/None vs ma_fonction/docstring |
| `03_07_decorateurs_de_classe.py` | 5.3 | Ajouter __str__ à une classe, singleton avec décorateur | Personne(nom=Alice, age=30), config1 is config2 |
| `03_08_decorateurs_comme_classes.py` | 5.3 | Classe Compteur avec __call__, RepeterAction avec paramètres | Appel n.1/2/3, Exécution 1/2/3 |
| `03_09_cas_usage_avances.py` | 5.3 | Validation types, rate limiting, convertir exceptions, dépréciation | TypeError, trop de requêtes, ErreurMetier, warning |

**Fichier source** : `03-decorateurs-avances.md`

## Fichier 04 : Générateurs et expressions génératrices (11 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `04_01_generateur_base.py` | 5.4 | Fonction normale vs générateur, yield, next(), StopIteration | [0,1,2,3,4], generator object, 1/2/3 |
| `04_02_generateurs_simples.py` | 5.4 | Carrés, nombres pairs, Fibonacci | 0 1 4 9 16, [2,4,6,8,10], 0 1 1 2 3 5 8 13 21 34 |
| `04_03_avantages_generateurs.py` | 5.4 | Économie mémoire, évaluation paresseuse, séquence infinie | ~8MB vs ~176 bytes, traitement à la demande, 10..19 |
| `04_04_expressions_generatrices.py` | 5.4 | Syntaxe compacte, comparaison, filtrage, somme, chaîner | [0,1,4,9,16], [4,8,12,16,20], [64,100,144,196,256,324] |
| `04_05_fonctions_natives.py` | 5.4 | map(), filter(), zip(), enumerate(), reversed() | Doubles, pairs, Alice/Bob/Charlie, 1.pomme, 5 4 3 2 1 |
| `04_06_cas_usage_pratiques.py` | 5.4 | Lecture fichier, pagination, pipeline, données de test | Lignes erreur, 5 pages, [20,40,60,80,100], 5 utilisateurs |
| `04_07_generateurs_infinis.py` | 5.4 | Compteur infini avec pas, cycle, répétition | 10 12 14 16 18, rouge vert bleu..., Python x5 |
| `04_08_methodes_avancees.py` | 5.4 | send(), close(), throw() | Total 0/10/15/18, fermé, ValueError capturée |
| `04_09_yield_from.py` | 5.4 | Combiner générateurs, aplatir listes, parcourir arbre | [1,2,3,4], [1..9], [1,2,4,5,3] |
| `04_10_comparaison_performance.py` | 5.4 | Mémoire liste vs générateur, épuisement, erreurs courantes | 8 MB vs 0.19 KB, [] après épuisement, TypeError |
| `04_11_itertools.py` | 5.4 | count(), cycle(), repeat(), chain(), islice(), takewhile(), dropwhile() | 10 12 14 16 18, R G B..., 5 6 7 8 9, 1 4, 6 4 1 |

**Fichier source** : `04-generateurs.md`

## Fichier 05 : Closures et programmation fonctionnelle (10 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `05_01_closure_base.py` | 5.5 | Closure salutation, multiplicateur | Bonjour Alice !, Hello Bob !, 10/15/50 |
| `05_02_variables_libres_nonlocal.py` | 5.5 | Variables libres, __closure__, nonlocal, avec/sans | ('debut',), 10, 18, compteur 1/2/3/1/4 |
| `05_03_closures_pratiques.py` | 5.5 | Puissances, formateur HTML, compte bancaire, compteur appels, callbacks | 25/27/16, `<b>`, solde 1300EUR, 3 appels, CLICK/HOVER |
| `05_04_fonctions_premiere_classe.py` | 5.5 | Assignation, arguments, retour de fonctions, structures | Bonjour Alice !, 8/15, 15/50 |
| `05_05_fonctions_pures_immutabilite.py` | 5.5 | Pures vs impures, immuabilité, copies superficielle/profonde | 7, [1,2,3] inchangé, deepcopy préserve |
| `05_06_composition_pipeline.py` | 5.5 | Composition manuelle, composer(), pipeline texte | 256, *** PYTHON!!! *** |
| `05_07_curryfication_partial.py` | 5.5 | Curryfication, générique, URLs, functools.partial | 8/13, 24/30, https://..., carre 25, cube 27 |
| `05_08_recursion.py` | 5.5 | Factorielle, Fibonacci, somme récursive, tail recursion | 120, [0,1,1,2,3,5,8,13,21,34], 15, 120 |
| `05_09_techniques_fonctionnelles.py` | 5.5 | namedtuple, prédicats, testabilité, traitement lisible | Point(3,4), [2,4], 120 TTC, ['java','python','ruby'] |
| `05_10_exemple_complet.py` | 5.5 | Pipeline étudiants : moyenne, filtrer admis, extraire noms | Alice/Bob/Charlie admis, David refusé |

**Fichier source** : `05-closures-et-prog-fonctionnelle.md`

## Exécution

Chaque fichier peut être exécuté indépendamment :

```bash
python3 01_01_lambda_base.py
python3 05_10_exemple_complet.py
```

Tous les fichiers créent et nettoient leurs fichiers temporaires automatiquement.

Pour exécuter tous les fichiers et vérifier qu'il n'y a pas d'erreur :

```bash
for f in *.py; do echo "=== $f ===" && python3 "$f" || echo "ERREUR: $f"; done
```
