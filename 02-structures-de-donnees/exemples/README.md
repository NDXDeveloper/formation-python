# Chapitre 2 : Structures de données - Exemples

Ce dossier contient **80 fichiers** d'exemples exécutables correspondant aux 4 sections du chapitre 2.

## Exécution

```bash
python3 nom_du_fichier.py
```

---

## Section 2.1 : Listes, Tuples, Dictionnaires et Sets

Source : `01-listes-tuples-dicts-sets.md`

| Fichier | Description | Sortie attendue |
|---------|-------------|-----------------|
| `01_01_creer_liste.py` | Créer des listes | Listes vides, nombres, mélanges, list() |
| `01_02_acces_slicing.py` | Accès par indice et slicing | Indices positifs/négatifs, slices, pas |
| `01_03_modifier_liste.py` | Modifier une liste | append, insert, extend |
| `01_04_supprimer_elements_liste.py` | Supprimer des éléments | remove, pop, del, clear |
| `01_05_operations_listes.py` | Opérations sur les listes | len, in, count, sort, sorted, reverse |
| `01_06_copier_liste.py` | Copier une liste | Référence vs copie, copy(), deepcopy |
| `01_07_listes_imbriquees.py` | Listes imbriquées | Matrice 3x3, accès, modification |
| `01_08_creer_tuple.py` | Créer des tuples | Tuples, tuple d'un élément, packing |
| `01_09_acces_immutabilite_tuple.py` | Accès et immutabilité | Indexation, TypeError sur modification |
| `01_10_unpacking.py` | Unpacking de tuples | Unpacking multiple, *, échange de variables |
| `01_11_operations_tuples.py` | Opérations sur les tuples | count, index, clés dict, retours multiples |
| `01_12_creer_dictionnaire.py` | Créer des dictionnaires | {}, dict(), fromkeys, zip |
| `01_13_acceder_valeurs_dict.py` | Accéder aux valeurs | [], get(), KeyError |
| `01_14_modifier_dictionnaire.py` | Modifier un dictionnaire | Ajout, modification, update() |
| `01_15_supprimer_elements_dict.py` | Supprimer des éléments | del, pop(), clear() |
| `01_16_parcourir_dictionnaire.py` | Parcourir un dictionnaire | keys(), values(), items() |
| `01_17_operations_dict.py` | Opérations sur les dicts | len, in, copy, setdefault |
| `01_18_dicts_imbriques.py` | Dictionnaires imbriqués | Accès profond, modification |
| `01_19_creer_set.py` | Créer des sets | set(), pas de doublons, non ordonné |
| `01_20_modifier_set.py` | Modifier un set | add, update, remove, discard, pop |
| `01_21_operations_ensembles.py` | Opérations ensemblistes | Union, intersection, différence, comparaisons |
| `01_22_cas_usage_sets.py` | Cas d'usage des sets | Doublons, frozenset |
| `01_23_inventaire.py` | Exemple : inventaire | Stock: pommes=35, bananes=25, oranges=25 |
| `01_24_analyse_texte.py` | Exemple : analyse texte | 9 mots uniques, python et est: 2 fois |
| `01_25_gestion_etudiants.py` | Exemple : gestion étudiants | Étudiants par matière, multi-inscrits |

---

## Section 2.2 : Compréhensions

Source : `02-comprehensions.md`

| Fichier | Description | Sortie attendue |
|---------|-------------|-----------------|
| `02_01_comprehension_liste_base.py` | Compréhensions de base | Carrés, températures °F |
| `02_02_comprehension_avec_filtre.py` | Filtrage avec if | Pairs, noms longs |
| `02_03_comprehension_if_else.py` | Transformation if/else | pair/impair, catégories |
| `02_04_boucles_multiples_imbriquees.py` | Boucles multiples | Produits cartésiens, matrice aplatie |
| `02_05_cas_usage_listes.py` | Cas d'usage pratiques | prix_soldes, initiales |
| `02_06_comprehension_dictionnaire.py` | Compréhension de dict | Carrés, filtre, inversion clé/valeur |
| `02_07_comprehension_dict_cas_usage.py` | Dict cas d'usage | Comptage longueurs, groupement |
| `02_08_comprehension_sets.py` | Compréhension de sets | Voyelles, longueurs uniques |
| `02_09_comparaison_comprehensions.py` | Comparaison list/dict/set | Même donnée, 3 types |
| `02_10_comprehensions_avancees.py` | Avancées | Matrice identité, filtrage imbriqué |
| `02_11_expressions_generatrices.py` | Expressions génératrices | Mémoire, sum, max, any, all |
| `02_12_bonnes_pratiques_comprehensions.py` | Bonnes pratiques | Lisibilité, étapes intermédiaires |
| `02_13_exemple_analyse_texte.py` | Exemple : analyse texte | Fréquence des mots |
| `02_14_exemple_transformation_donnees.py` | Exemple : transformation | Salaires augmentés |
| `02_15_exemple_filtrage_regroupement.py` | Exemple : filtrage | Fruits: 2.0€, Légumes: 1.9€ |
| `02_16_exemple_operations_matricielles.py` | Exemple : matrices | Addition, transposition |

---

## Section 2.3 : Collections spécialisées

Source : `03-collections-specialisees.md`

| Fichier | Description | Sortie attendue |
|---------|-------------|-----------------|
| `03_01_namedtuple_base.py` | namedtuple : base | Création, accès, _asdict, _replace, defaults |
| `03_02_namedtuple_cas_usage.py` | namedtuple : cas d'usage | Distance 11.18, salaire moyen 51667 |
| `03_03_defaultdict_base.py` | defaultdict : base | Problème KeyError, factory int/list/set/str |
| `03_04_defaultdict_cas_usage.py` | defaultdict : cas d'usage | Comptage mots, groupement, graphe |
| `03_05_counter_base.py` | Counter : base | most_common, elements, update, subtract, arithmétique |
| `03_06_counter_cas_usage.py` | Counter : cas d'usage | Votes Alice 54.5%, inventaire, logs |
| `03_07_autres_collections.py` | deque, OrderedDict, ChainMap | Rotation, move_to_end, priorité config |
| `03_08_exemples_combines.py` | Exemples combinés | Ventes par région, réseau social |

---

## Section 2.4 : Chaînes de caractères et expressions régulières

Source : `04-chaines-et-regex.md`

| Fichier | Description | Sortie attendue |
|---------|-------------|-----------------|
| `04_01_creer_chaines.py` | Créer des chaînes | Guillemets, caractères spéciaux, raw strings |
| `04_02_concatenation_repetition.py` | Concaténation et répétition | Marie Dupont, ligne de =, concaténation implicite |
| `04_03_indexation_slicing.py` | Indexation et slicing | P, t, n, Pyt, nohtyP, TypeError |
| `04_04_longueur_appartenance.py` | Longueur et appartenance | len=17, in/not in |
| `04_05_changement_casse.py` | Changement de casse | upper, lower, capitalize, title, swapcase |
| `04_06_recherche_remplacement.py` | Recherche et remplacement | find, index, count, startswith, replace |
| `04_07_nettoyage_chaines.py` | Nettoyage des chaînes | strip, lstrip, rstrip, removeprefix/suffix |
| `04_08_division_jointure.py` | Division et jointure | split, splitlines, join |
| `04_09_verification_type_caracteres.py` | Vérifications de type | isalnum, isalpha, isdigit, isdecimal, isspace |
| `04_10_alignement_remplissage.py` | Alignement et remplissage | center, ljust, rjust, zfill |
| `04_11_partition.py` | Partition | partition, rpartition |
| `04_12_formatage_fstrings.py` | f-strings | Nombres, alignement, milliers, %, scientifique |
| `04_13_formatage_ancien.py` | format() et % | Indices, noms, dicts, style C |
| `04_14_fstrings_avances.py` | f-strings avancés | Dates, binaire/octal/hex, debug =, multi-lignes |
| `04_15_regex_search_match.py` | Regex : search et match | Trouvé 2020 position 25, début de chaîne |
| `04_16_regex_findall_finditer.py` | Regex : findall et finditer | Tous les nombres, positions |
| `04_17_regex_sub_split.py` | Regex : sub et split | Remplacement, fonction doubler, split multi-séparateurs |
| `04_18_groupes_capture.py` | Regex : groupes de capture | Email décomposé, groupes nommés, groupdict |
| `04_19_compilation_flags.py` | Regex : compilation et flags | compile, IGNORECASE, MULTILINE, DOTALL |
| `04_20_validation_email.py` | Regex : validation email | 3 valides, 2 invalides |
| `04_21_extraction_telephone.py` | Regex : extraction téléphone | 3 formats détectés |
| `04_22_nettoyage_texte_regex.py` | Regex : nettoyage texte | Espaces multiples, ponctuation, non-alphanum |
| `04_23_extraction_urls.py` | Regex : extraction URLs | https://example.com, http://docs... |
| `04_24_parsing_logs.py` | Regex : parsing de logs | 2 erreurs extraites avec date et message |
| `04_25_validation_mot_de_passe.py` | Regex : validation mot de passe | faible=<8, Faible123=pas spécial, Faible123!=OK |
| `04_26_extraction_donnees.py` | Regex : extraction facture | N° 2024-001, date, montant 1,234.56 |
| `04_27_remplacement_groupes.py` | Regex : remplacement avec groupes | Dates reformatées, emails anonymisés |
| `04_28_validation_formats.py` | Regex : validation formats | Code postal, plaque, ISBN |
| `04_29_traitement_texte_avance.py` | Regex : traitement avancé | Hashtags, mentions, camelCase/snake_case |
| `04_30_patterns_courants.py` | Regex : patterns courants | Email, URL, tél, date, IPv4, heure, hex |
| `04_31_bonnes_pratiques_regex.py` | Regex : bonnes pratiques | Raw strings, compile, VERBOSE, tests |

---


